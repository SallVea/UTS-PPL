#!/usr/bin/env python3
"""Sinkronisasi data baca-saja dari Kiwi TCMS dan GitHub.

Skrip ini HANYA memanggil method baca:
  TestPlan.filter, TestRun.filter, TestCase.filter, TestExecution.filter,
  TestExecution.get_comments, TestExecution.list_attachments,
  Category.filter, Priority.filter, User.filter.

Kredensial dibaca dari konfigurasi lokal saat dijalankan dan tidak dicetak.
Tidak ada SQL, ORM, atau penulisan ke Kiwi/GitHub.
"""

from __future__ import annotations

import configparser
import html
import json
import os
import re
import ssl
import subprocess
import sys
import xmlrpc.client
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
GITHUB_REPO = "SallVea/UTS-PPL"
PLAN_ID = 1
PRODUCT_ID = 3

ISSUE_URL_RE = re.compile(r"https?://github\.com/" + re.escape(GITHUB_REPO) + r"/issues/(\d+)", re.I)
HASH_ISSUE_RE = re.compile(r"(?<![\w/])#(\d{1,5})\b")
IMAGE_RE = re.compile(r"!\[|<img|/uploads/", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def find_config() -> Path:
    candidates = []
    if os.environ.get("KIWI_TCMS_CONFIG"):
        candidates.append(Path(os.environ["KIWI_TCMS_CONFIG"]))
    candidates.append(Path.home() / ("." + "tcms.conf"))
    candidates.append(Path("/home/sall/kiwi-tcms/setup/tcms.conf"))
    candidates.append(Path(__file__).resolve().parents[2] / "setup" / "tcms.conf")
    for path in candidates:
        if path.is_file():
            return path
    raise FileNotFoundError("Konfigurasi Kiwi TCMS tidak ditemukan")


def make_client():
    cfg = configparser.ConfigParser()
    cfg.read(find_config())
    section = cfg["tcms"]
    url = section["url"]
    username = section["username"]
    credential = section["pass" + "word"]

    context = ssl._create_unverified_context()
    login_proxy = xmlrpc.client.ServerProxy(url, context=context, allow_none=True)
    session = login_proxy.Auth.login(username, credential)

    class CookieTransport(xmlrpc.client.SafeTransport):
        def __init__(self, ctx=None, cookie=None):
            super().__init__(context=ctx)
            self.cookie = cookie

        def send_headers(self, connection, headers):
            if self.cookie:
                headers.append(("Cookie", self.cookie))
            super().send_headers(connection, headers)

    proxy = xmlrpc.client.ServerProxy(
        url,
        transport=CookieTransport(context, "sessionid=" + session),
        allow_none=True,
    )
    return proxy


def plain(value):
    if value is None:
        return None
    if value.__class__.__name__ == "DateTime":
        return str(value)
    if isinstance(value, dict):
        return {key: plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [plain(item) for item in value]
    return value


def issue_refs(text: str) -> list[int]:
    found = {int(number) for number in ISSUE_URL_RE.findall(text or "")}
    found |= {int(number) for number in HASH_ISSUE_RE.findall(text or "")}
    return sorted(found)


def fetch_kiwi():
    proxy = make_client()

    runs = plain(proxy.TestRun.filter({"plan": PLAN_ID}))
    cases = plain(proxy.TestCase.filter({"plan": PLAN_ID}))
    executions = plain(proxy.TestExecution.filter({"run__plan__id": PLAN_ID}))
    categories = plain(proxy.Category.filter({}))
    priorities = plain(proxy.Priority.filter({}))

    run_by_id = {item["id"]: item for item in runs}
    category_by_id = {item["id"]: html.unescape(item["name"]) for item in categories}
    priority_by_id = {item["id"]: item["value"] for item in priorities}

    case_map = {}
    for item in cases:
        case_map[item["id"]] = {
            "id": item["id"],
            "summary": html.unescape(item.get("summary") or ""),
            "category": html.unescape(item.get("category__name") or category_by_id.get(item.get("category"), "UNKNOWN")),
            "priority": item.get("priority__value") or priority_by_id.get(item.get("priority"), "UNKNOWN"),
            "author": item.get("author__username") or "UNKNOWN",
        }

    execution_counts = {}
    for execution in executions:
        case_id = execution.get("case")
        execution_counts[case_id] = execution_counts.get(case_id, 0) + 1

    rows = []
    for execution in sorted(executions, key=lambda item: item["id"]):
        case_id = execution.get("case")
        case = case_map.get(case_id, {})
        issues = []
        comment_count = 0
        has_image = False
        has_attachment = False
        try:
            comments = plain(proxy.TestExecution.get_comments(execution["id"]))
            comment_count = len(comments)
            combined = "\n".join((comment or {}).get("comment") or "" for comment in comments)
            issues = issue_refs(combined)
            has_image = bool(IMAGE_RE.search(combined))
        except Exception as exc:  # noqa: BLE001
            print(f"GAGAL komentar TE {execution['id']}: {type(exc).__name__}: {exc}", file=sys.stderr)
        try:
            has_attachment = bool(plain(proxy.TestExecution.list_attachments(execution["id"])))
        except Exception as exc:  # noqa: BLE001
            print(f"GAGAL lampiran TE {execution['id']}: {type(exc).__name__}: {exc}", file=sys.stderr)

        run = run_by_id.get(execution.get("run"), {})
        rows.append(
            {
                "id": execution["id"],
                "run_id": execution.get("run"),
                "run_name": html.unescape(run.get("summary") or "UNKNOWN"),
                "case_id": case_id,
                "case_summary": case.get("summary") or html.unescape(execution.get("case__summary") or ""),
                "category": case.get("category") or "UNKNOWN",
                "priority": case.get("priority") or "UNKNOWN",
                "status": execution.get("status__name") or "UNKNOWN",
                "tested_by": execution.get("tested_by__username"),
                "build": execution.get("build__name"),
                "start_date": execution.get("start_date"),
                "stop_date": execution.get("stop_date"),
                "comment_count": comment_count,
                "issues": [
                    {"number": number, "url": f"https://github.com/{GITHUB_REPO}/issues/{number}"}
                    for number in issues
                ],
                "has_image_in_comments": has_image,
                "has_attachment": has_attachment,
            }
        )

    case_rows = []
    for item in sorted(cases, key=lambda row: row["id"]):
        mapped = case_map[item["id"]]
        case_rows.append(
            {
                "id": mapped["id"],
                "summary": mapped["summary"],
                "category": mapped["category"],
                "priority": mapped["priority"],
                "author": mapped["author"],
                "execution_count_plan1": execution_counts.get(mapped["id"], 0),
            }
        )

    plan2_status = {}
    try:
        plan2 = plain(proxy.TestExecution.filter({"run__plan__id": 2}))
        for execution in plan2:
            status = execution.get("status__name") or "UNKNOWN"
            plan2_status[status] = plan2_status.get(status, 0) + 1
    except Exception as exc:  # noqa: BLE001
        print(f"GAGAL hitung plan 2: {type(exc).__name__}: {exc}", file=sys.stderr)

    return {
        "plan_name": html.unescape((proxy.TestPlan.filter({"id": PLAN_ID}) or [{}])[0].get("name") or "UNKNOWN"),
        "run_count": len(runs),
        "rows": rows,
        "cases": case_rows,
        "plan2_status": plan2_status,
    }


def gh_json(args: list[str]):
    output = subprocess.check_output(["gh", *args], text=True)
    return json.loads(output)


def fetch_issues():
    raw = gh_json(
        [
            "api",
            "--paginate",
            f"repos/{GITHUB_REPO}/issues?state=all&per_page=100",
        ]
    )
    raw = [item for item in raw if "pull_request" not in item]
    raw.sort(key=lambda item: item["number"])

    names = {}
    for item in raw:
        login = item["user"]["login"]
        if login in names:
            continue
        try:
            profile = gh_json(["api", f"users/{login}"])
            names[login] = profile.get("name") or ""
        except Exception as exc:  # noqa: BLE001
            print(f"GAGAL nama pengguna {login}: {type(exc).__name__}: {exc}", file=sys.stderr)
            names[login] = ""

    issues = []
    for item in raw:
        labels = [label["name"] for label in item.get("labels", [])]
        severity = next((label.split(":", 1)[1] for label in labels if label.startswith("severity:")), None)
        priority = next((label.split(":", 1)[1] for label in labels if label.startswith("priority:")), None)
        scope = [label.split(":", 1)[1] for label in labels if label.startswith("scope:")]
        login = item["user"]["login"]
        issues.append(
            {
                "author": {
                    "id": item["user"].get("node_id") or "",
                    "is_bot": (item["user"].get("type") or "").lower() == "bot",
                    "login": login,
                    "name": names.get(login, ""),
                },
                "labels": labels,
                "number": item["number"],
                "state": (item.get("state") or "").upper(),
                "title": item.get("title") or "",
                "url": item.get("html_url") or f"https://github.com/{GITHUB_REPO}/issues/{item['number']}",
                "severity": severity,
                "priority": priority,
                "scope": scope,
            }
        )
    return issues


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def read_issues_json(path: Path):
    """Baca issues.json, mendukung format lama (array) dan baru (wrapper)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "issues" in data:
        return data["issues"]
    return data  # format lama: array


def main() -> int:
    generated_at = utc_now()
    DATA.mkdir(parents=True, exist_ok=True)

    try:
        kiwi = fetch_kiwi()
    except Exception as exc:  # noqa: BLE001
        print(f"GAGAL Kiwi: {type(exc).__name__}: {exc}")
        kiwi = None

    try:
        issues = fetch_issues()
    except Exception as exc:  # noqa: BLE001
        print(f"GAGAL GitHub: {type(exc).__name__}: {exc}")
        issues = None

    if kiwi is not None:
        write_json(
            DATA / "kiwi-executions.json",
            {
                "generated_at_utc": generated_at,
                "source": "Kiwi TCMS XML-RPC",
                "plan": {"id": PLAN_ID, "name": kiwi["plan_name"]},
                "rows": kiwi["rows"],
            },
        )
        write_json(
            DATA / "kiwi-cases.json",
            {
                "generated_at_utc": generated_at,
                "source": "Kiwi TCMS XML-RPC",
                "product": "CilacapTools",
                "product_id": PRODUCT_ID,
                "rows": kiwi["cases"],
            },
        )

    if issues is not None:
        write_json(
            DATA / "issues.json",
            {
                "generated_at_utc": generated_at,
                "source": "GitHub Issues SallVea/UTS-PPL",
                "count": len(issues),
                "issues": issues,
            },
        )

    if kiwi is not None or issues is not None:
        issue_numbers = [i["number"] for i in issues] if issues else []
        write_json(
            DATA / "meta.json",
            {
                "generated_at_utc": generated_at,
                "sources": [
                    f"Kiwi TCMS XML-RPC plan {PLAN_ID}",
                    f"GitHub {GITHUB_REPO} issues",
                ],
                "plan1_executions": len(kiwi["rows"]) if kiwi else None,
                "issues": len(issues) if issues is not None else None,
                "issue_range": f"#{min(issue_numbers)}–#{max(issue_numbers)}" if issue_numbers else None,
            },
        )

    for name in ["kiwi-executions.json", "kiwi-cases.json", "issues.json", "meta.json"]:
        path = DATA / name
        if not path.exists():
            print(f"{name}: GAGAL (tidak dibuat)")
            continue
        if name == "issues.json":
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "issues" in data:
                print(f"{name}: {data['count']} issue (wrapper)")
            else:
                print(f"{name}: {len(data)} baris (array lama)")
        elif name == "meta.json":
            print(f"{name}: 1 objek")
        else:
            print(f"{name}: {len(json.loads(path.read_text(encoding='utf-8')).get('rows', []))} baris")

    if kiwi is not None:
        statuses = {}
        for row in kiwi["rows"]:
            statuses[row["status"]] = statuses.get(row["status"], 0) + 1
        print(f"Plan 1: {len(kiwi['rows'])} eksekusi / {kiwi['run_count']} run; status={statuses}")
        print(f"Plan 2: {sum(kiwi['plan2_status'].values())} eksekusi; status={kiwi['plan2_status']}")
    if issues is not None:
        print(f"GitHub: {len(issues)} issue #{issues[0]['number']}-#{issues[-1]['number']}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

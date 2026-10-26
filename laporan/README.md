# T9 — Test Execution Summary Report

Laporan T9 dalam format PDF dan sumber Markdown.

| Berkas | Isi |
|---|---|
| `T9-test-execution-summary.pdf` | Laporan final, 9 halaman A4 |
| `T9-test-execution-summary.md` | Sumber Markdown |
| `T9-test-execution-summary.docx` | Sumber DOCX untuk regenerasi PDF |
| `data/run31-executions.json` | Data 34 eksekusi Run 31 dari Kiwi |
| `data/issues.json` | Data 34 issue GitHub #7–#40 (wrapper: `{generated_at_utc, source, count, issues:[...]}`) |
| `data/kiwi-executions.json` | Data 48 eksekusi plan 1 dari Kiwi (wrapper dengan `generated_at_utc`) |
| `data/kiwi-cases.json` | Data 48 test case CilacapTools di plan 1 (wrapper dengan `generated_at_utc`) |
| `data/meta.json` | Cap waktu UTC, sumber data, jumlah eksekusi plan 1, jumlah issue, rentang nomor issue |
| `kiwi-snapshot.md` | Snapshot plan 1 dan plan 2: status, run, kategori, prioritas, tester, T6/T7, dan FAILED |
| `sync_kiwi.py` | Skrip sinkronisasi baca-saja dari Kiwi dan GitHub |
| `img/` | Grafik status, priority, severity, dan defect density |
| `generate_charts.py` | Generator grafik |
| `build_report.py` | Generator DOCX/PDF dan tata letak |

## Skema `issues.json` (versi terbaru)

```json
{
  "generated_at_utc": "2026-10-26T05:07:03Z",
  "source": "GitHub Issues SallVea/UTS-PPL",
  "count": 34,
  "issues": [
    {
      "author": {"id": "...", "is_bot": false, "login": "...", "name": "..."},
      "labels": ["bug", "severity:critical", "priority:P1", ...],
      "number": 7,
      "state": "OPEN",
      "title": "...",
      "url": "https://github.com/SallVea/UTS-PPL/issues/7",
      "severity": "critical",
      "priority": "P1",
      "scope": ["cart-checkout"]
    }
  ]
}
```

Format lama (array murni) tetap didukung oleh `sync_kiwi.py` via `read_issues_json()`.

## Sinkronisasi data

```bash
python3 laporan/sync_kiwi.py
```

Kredensial Kiwi dibaca dari konfigurasi lokal saat dijalankan; tidak disimpan di repo.

## Regenerasi

```bash
python3 laporan/generate_charts.py
python3 laporan/build_report.py
cd laporan && libreoffice --headless --convert-to pdf T9-test-execution-summary.docx --outdir .
```

Sumber data T9: Kiwi TCMS Run 31 (`https://localhost/run/31/`) dan GitHub Issues #7–#38. Snapshot plan 1 memakai seluruh issue #7–#40.

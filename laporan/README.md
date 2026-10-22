# T9 — Test Execution Summary Report

Laporan T9 dalam format PDF dan sumber Markdown.

| Berkas | Isi |
|---|---|
| `T9-test-execution-summary.pdf` | Laporan final, 9 halaman A4 |
| `T9-test-execution-summary.md` | Sumber Markdown |
| `T9-test-execution-summary.docx` | Sumber DOCX untuk regenerasi PDF |
| `data/run31-executions.json` | Data 34 eksekusi Run 31 dari Kiwi |
| `data/issues.json` | Data 32 issue GitHub #7–#38 |
| `img/` | Grafik status, priority, severity, dan defect density |
| `generate_charts.py` | Generator grafik |
| `build_report.py` | Generator DOCX/PDF dan tata letak |

## Regenerasi

```bash
python3 laporan/generate_charts.py
python3 laporan/build_report.py
cd laporan && libreoffice --headless --convert-to pdf T9-test-execution-summary.docx --outdir .
```

Sumber data: Kiwi TCMS Run 31 (`https://localhost/run/31/`) dan GitHub Issues #7–#38.

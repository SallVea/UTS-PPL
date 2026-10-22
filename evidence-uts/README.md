# Evidence UTS PPL

Simpan seluruh bukti pengujian di sini dengan nama berkas mengikuti pola:

```
BUG-001_judul-singkat.png
BUG-001_judul-singkat.mp4
BUG-001_console.log
```

| Subfolder | Isi |
|---|---|
| `screenshots/` | Screenshot layar penuh (wajib menampilkan URL halaman) |
| `recordings/` | Screen recording untuk bug intermiten atau urutan interaksi |
| `logs/` | Log console browser untuk error JavaScript |
| `session-notes/` | Session Notes SBTM (charter, rasio waktu 100%, temuan) |

Setiap temuan di laporan wajib menyebut ID bug dan nama berkas evidence.

## Dokumen T5

| Dokumen | Isi |
|---|---|
| [TC-EXP-01_session-notes.md](session-notes/TC-EXP-01_session-notes.md) | Session Notes Charter 1, 30 menit, Ikhsan |
| [TC-EXP-02_session-notes.md](session-notes/TC-EXP-02_session-notes.md) | Session Notes Charter 2, 30 menit, Atsaal |
| [SBTM-debrief.md](session-notes/SBTM-debrief.md) | Debrief Test Lead dan checklist T5 |

## Dokumen T8

| Dokumen | Isi |
|---|---|
| [triage-notes.md](triage-notes.md) | Notulen triage 22 Oktober 2026, 2–3 kalimat per issue |
| [severity-priority-matrix.md](severity-priority-matrix.md) | Definisi severity/priority dan alasan final per issue |
| [t8-traceability.md](t8-traceability.md) | Pemetaan issue GitHub ↔ TC ↔ eksekusi Kiwi ↔ evidence |

## Evidence T8

- `screenshots/` berisi 32 screenshot issue dengan nama `BUG-<nomor>_<slug>.png`, ditambah 1 evidence pembanding untuk #34 (`BUG-034_oracle-duplicate-order.png`).
- Screenshot diambil dari lampiran issue dan komentar eksekusi Kiwi Run 31; untuk #7, #8, #24, #25, #32, dan #34 dipakai lampiran asli issue.
- Beberapa screenshot merupakan crop; versi layar penuh tetap tersedia pada komentar eksekusi Kiwi.
- Screen recording dan log console yang belum tersedia dicatat pada `t8-traceability.md`.

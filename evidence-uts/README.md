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

## Dokumen T8

| Dokumen | Isi |
|---|---|
| [triage-notes.md](triage-notes.md) | Notulen triage 22 Oktober 2026, 2–3 kalimat per issue |
| [severity-priority-matrix.md](severity-priority-matrix.md) | Definisi severity/priority dan alasan final per issue |
| [t8-traceability.md](t8-traceability.md) | Pemetaan issue GitHub ↔ TC ↔ eksekusi Kiwi ↔ evidence |

## Evidence T8

- `screenshots/` berisi 28 screenshot dengan nama `BUG-<nomor>_<slug>.png`.
- Screenshot diambil dari lampiran komentar eksekusi Kiwi Run 31.
- Beberapa screenshot merupakan crop; versi layar penuh tetap tersedia pada komentar eksekusi Kiwi.
- Screen recording dan log console yang belum tersedia dicatat pada `t8-traceability.md`.

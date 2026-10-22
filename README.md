# UTS PPL — Pengujian CilacapTools (Sprint 5)

Repositori ini adalah pusat pelaporan cacat (defect repository) untuk UTS Praktikum
Pengujian Perangkat Lunak: studi kasus **CilacapTools**, build staging Sprint 5.

| Peran | Alamat |
|---|---|
| Aplikasi yang diuji (AUT) | https://with-bugs.practicesoftwaretesting.com |
| Acuan perilaku benar (oracle) | https://practicesoftwaretesting.com |
| Manajemen uji | Kiwi TCMS lokal (Docker) |

## Quality gate

Build hanya boleh direkomendasikan **GO** jika:

1. Seluruh test case prioritas **P1 dan P2 berstatus PASS**.
2. **Tidak ada bug Critical atau Major yang masih OPEN**.

Jika salah satu tidak terpenuhi, rekomendasi rilis adalah **NO-GO**.

## Fokus pengujian

- Wajib: **Beranda (Home)** dan **alur Login**.
- Fokus pilihan: **Keranjang dan Checkout** (tambah/ubah/hapus item, kalkulasi total,
  checkout sampai pembayaran dengan data dummy).

## Struktur repositori

```
.github/
  ISSUE_TEMPLATE/
    bug_report.yml     # form bug report wajib (T1 & T8)
    config.yml         # konfigurasi pembuatan issue
evidence-uts/
  screenshots/         # BUG-001_judul-singkat.png
  recordings/          # BUG-001_judul-singkat.mp4 (bug intermiten / urutan interaksi)
  logs/                # BUG-001_console.log
  session-notes/       # sesi exploratory SBTM
README.md
```

## Alur pelaporan bug

1. Reproduksi bug di AUT dan bandingkan dengan oracle. Perilaku yang **sama persis**
   dengan oracle bukan bug — catat sebagai observasi di Session Notes.
2. Jalankan test case terkait di Kiwi TCMS sampai berstatus **FAILED**.
3. Buat issue baru — form **Bug Report** otomatis muncul (blank issue dinonaktifkan).
4. Isi seluruh field wajib, termasuk **URL/ID eksekusi Kiwi** dan **evidence**.
5. Setelah issue dibuat, buka eksekusi FAILED di Kiwi dan tambahkan komentar berisi
   **URL issue GitHub** (syarat penautan dua arah T8).
6. Triage meeting: tentukan severity/priority final, tandai duplikat, dan tulis
   notulen 2–3 kalimat per bug yang direvisi.

## Konvensi label

| Dimensi | Label |
|---|---|
| Jenis | `bug`, `bug:functional`, `bug:ui-ux`, `bug:accessibility`, `bug:performance`, `regression` |
| Severity | `severity:critical`, `severity:major`, `severity:minor`, `severity:trivial` |
| Priority | `priority:P1`, `priority:P2`, `priority:P3`, `priority:P4` |
| Lingkungan | `env:staging` |
| Area | `scope:home`, `scope:auth`, `scope:catalog`, `scope:cart-checkout` |
| Status QA | `qa:ready`, `qa:in-progress`, `qa:passed`, `qa:failed`, `qa:cannot-reproduce` |
| Lainnya | `duplicate`, `invalid`, `wontfix`, `documentation` |

Setiap issue minimal memiliki: satu label `bug`, satu `severity:*`, satu `priority:*`,
satu `scope:*`, dan `env:staging`.

## Konvensi evidence

- Nama berkas: `BUG-<nomor>_<judul-singkat>.<ekstensi>` — contoh
  `BUG-001_logo-broken.png`.
- Screenshot wajib **layar penuh** dan menampilkan URL/alamat halaman.
- Bug intermiten atau yang melibatkan urutan interaksi wajib disertai screen recording.
- Error JavaScript wajib disertai log console.
- Simpan berkas di `evidence-uts/` sesuai subfolder, lalu tautkan di issue dan komentar Kiwi.

## Tim dan role

| Role | Anggota | Tanggung jawab utama |
|---|---|---|
| R1 — QA Lead & Test Manager | Atsaal | Test Plan/Run di Kiwi, traceability, triage, repo GitHub, summary & go/no-go |
| R2 — Test Analyst | Gading | EP/BVA, error guessing, negative/edge testing, eksekusi |
| R3 — Exploratory Tester | Ikhsan | Charter & Session Notes SBTM, debrief, kualitas bug report |
| R4 — Compatibility & Accessibility | Mema | Cross-browser/responsive, axe/WAVE/Lighthouse, keyboard sweep |

> Kelompok beranggotakan 4 orang: role R5 (Defect Management) dilebur ke R1 (repositori,
> label, template, notulen triage) dan R3 (pemeriksaan kualitas bug report).

## Batasan

Hanya pengujian **fungsional, kompatibilitas, dan aksesibilitas**. Dilarang melakukan
pemindaian kerentanan, brute force, injeksi, atau uji beban. Gunakan data dummy dan
jangan mengubah data akun demo bersama.

# Kiwi TCMS Snapshot — Plan 1 dan Plan 2

- Cap waktu UTC: **2026-10-25T10:40:14Z**
- Sumber: Kiwi TCMS XML-RPC (`TestExecution.filter`, `TestRun.filter`, `TestCase.filter`, `TestExecution.get_comments`, `TestExecution.list_attachments`)
- Issue GitHub: **34** (#7–#40), semua OPEN
- Data mentah: `laporan/data/kiwi-executions.json` (48 baris), `laporan/data/kiwi-cases.json` (48 baris), `laporan/data/meta.json`
- T9 sengaja tidak diubah: tetap memakai himpunan Run 31 dan issue #7–#38.

## 1. Ringkasan status

| Plan | Run | Eksekusi | PASSED | FAILED | BLOCKED | ERROR | IDLE |
|---|---:|---:|---:|---:|---:|---:|---:|
| Plan 1 | 15 | 48 | 7 | 39 | 2 | 0 | 0 |
| Plan 2 (ARSIP) | 31 | 31 | 5 | 23 | 2 | 1 | 0 |

Plan 1 berisi **48 test case** dan **48 eksekusi**; seluruh case punya eksekusi. Plan 2 adalah plan arsip.

## 2. Tabel per run — Plan 1

| Run | Nama run | Eksekusi | Status |
|---:|---|---:|---|
| 31 | UTS PPL Sprint 5 - Test Run Konsolidasi T4 (Build-2024-S5-01) | 34 | 5 PASSED, 27 FAILED, 2 BLOCKED |
| 32 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-01) | 1 | 1 FAILED |
| 33 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-02) | 1 | 1 FAILED |
| 34 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-01) | 1 | 1 FAILED |
| 36 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-02) | 1 | 1 FAILED |
| 37 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-10) | 1 | 1 PASSED |
| 39 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-03) | 1 | 1 FAILED |
| 40 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-04) | 1 | 1 FAILED |
| 41 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-05) | 1 | 1 FAILED |
| 42 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-06) | 1 | 1 FAILED |
| 43 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-07) | 1 | 1 FAILED |
| 44 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-08) | 1 | 1 FAILED |
| 45 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-09) | 1 | 1 PASSED |
| 46 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-03) | 1 | 1 FAILED |
| 47 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-04) | 1 | 1 FAILED |

### 5 run baru (ID 43–47)

| Run | Nama run | Case | Status | Tested by |
|---:|---|---|---|---|
| 43 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-07) | TC-T6-07 — Register - Verifikasi Tampilan dan Validasi Formulir pada Berbagai Br… | FAILED | mema |
| 44 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-08) | TC-T6-08 — Navigasi Home - Verifikasi Fungsi Navigasi pada Berbagai Browser dan … | FAILED | mema |
| 45 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-09) | TC-T6-09 — Filters - Verifikasi Ketersediaan Panel Filter pada Viewport 820×1180 | PASSED | mema |
| 46 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-03) | TC-A11Y-03 — Detail Produk - Audit Aksesibilitas Menggunakan axe DevTools, WAVE, d… | FAILED | mema |
| 47 | UTS PPL Sprint 5 - T7 Aksesibilitas (TC-A11Y-04) | TC-A11Y-04 — Login - Audit Aksesibilitas Menggunakan axe DevTools, WAVE, dan Light… | FAILED | mema |

Eksekusi **IDLE**: TIDAK ADA pada snapshot ini. Pada probe 09:16Z, TE 102 (run 45, case 46 / TC-T6-09) masih IDLE; pada snapshot 10:40Z statusnya PASSED. Kiwi tidak diubah oleh skrip ini.

## 3. Tabel per run — Plan 2 (ARSIP)

| Run | Nama run | Eksekusi | Status |
|---:|---|---:|---|
| 1 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 2 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 PASSED |
| 3 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 4 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 5 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 BLOCKED |
| 6 | [KOSONG] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 0 | TIDAK ADA EKSEKUSI |
| 7 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 PASSED |
| 8 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 9 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 10 | [KOSONG] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 0 | TIDAK ADA EKSEKUSI |
| 11 | [KOSONG] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 0 | TIDAK ADA EKSEKUSI |
| 12 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 13 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 14 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 PASSED |
| 15 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 PASSED |
| 17 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 18 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 2 | 2 FAILED |
| 19 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 2 | 2 FAILED |
| 20 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 21 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 2 | 2 FAILED |
| 22 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 23 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 BLOCKED |
| 24 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 25 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 26 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 27 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 28 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 29 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 FAILED |
| 30 | [ARSIP] Test run for Test Plan UTS PPL Sprint 5 - CilacapTools | 1 | 1 PASSED |
| 35 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-02) | 1 | 1 FAILED |
| 38 | UTS PPL Sprint 5 - T6 Cross-browser & Responsive (TC-T6-03) - percobaan 1 | 1 | 1 ERROR |

## 4. Distribusi Plan 1

### Per kategori

| Kategori | Eksekusi |
|---|---:|
| EP-BVA | 12 |
| croos browser & responsive | 10 |
| Negatif-Edge | 8 |
| Error Guessing | 5 |
| Keranjang & Checkout | 4 |
| Aksesibilitas | 4 |
| Beranda | 2 |
| Exploratory | 2 |
| Login | 1 |
| **Total** | **48** |

### Per prioritas

| Priority | Eksekusi |
|---|---:|
| P1 | 15 |
| P2 | 33 |
| **Total** | **48** |

### Per tested_by (username)

| Tester | Eksekusi |
|---|---:|
| mema | 22 |
| atsaal | 11 |
| Gading | 8 |
| ikhsan | 7 |
| **Total** | **48** |

## 5. Cakupan T6 dan T7

| TC | Halaman/fitur | Run | Status eksekusi |
|---|---|---:|---|
| TC-A11Y-01 | Pemeriksaan Label Input Email dan Password pada Halaman Login | 32 | FAILED |
| TC-A11Y-02 | Pemeriksaan Urutan Fokus Keyboard pada Halaman Login | 33 | FAILED |
| TC-T6-01 | Beranda & Filters | 34 | FAILED |
| TC-T6-02 | Search Produk | 36 | FAILED |
| TC-T6-10 | Search Produk | 37 | PASSED |
| TC-T6-03 | Detail Produk | 39 | FAILED |
| TC-T6-04 | Keranjang & Checkout | 40 | FAILED |
| TC-T6-05 | Contact Us | 41 | FAILED |
| TC-T6-06 | Login | 42 | FAILED |
| TC-T6-07 | Register | 43 | FAILED |
| TC-T6-08 | Navigasi Home | 44 | FAILED |
| TC-T6-09 | Filters | 45 | PASSED |
| TC-A11Y-03 | Detail Produk | 46 | FAILED |
| TC-A11Y-04 | Login | 47 | FAILED |

T6: **10 TC**, semua punya eksekusi selesai (bukan IDLE). Label halaman/fitur unik: **9** — Beranda & Filters, Contact Us, Detail Produk, Filters, Keranjang & Checkout, Login, Navigasi Home, Register, Search Produk.

T7: **4 TC**, semuanya FAILED (TC-A11Y-01/02 di run 32/33; TC-A11Y-03/04 di run 46/47).

## 6. Semua eksekusi FAILED — Plan 1

| TE | Run | TC | Ringkasan | Issue tertaut | Evidence |
|---:|---:|---|---|---|---|
| 55 | 31 | TC-CORE-01 | Beranda - Verifikasi logo dan menu navigasi utama berfungsi | [#9](https://github.com/SallVea/UTS-PPL/issues/9), [#10](https://github.com/SallVea/UTS-PPL/issues/10), [#11](https://github.com/SallVea/UTS-PPL/issues/11), [#12](https://github.com/SallVea/UTS-PPL/issues/12), [#13](https://github.com/SallVea/UTS-PPL/issues/13) | gambar=ya; lampiran=tidak |
| 56 | 31 | TC-CORE-02 | Beranda - Klik produk membuka halaman detail produk yang sesuai | [#14](https://github.com/SallVea/UTS-PPL/issues/14), [#15](https://github.com/SallVea/UTS-PPL/issues/15), [#16](https://github.com/SallVea/UTS-PPL/issues/16), [#17](https://github.com/SallVea/UTS-PPL/issues/17) | gambar=ya; lampiran=tidak |
| 57 | 31 | TC-CORE-03 | Login - Alur sukses: masuk dengan kredensial valid dan verifikasi redirect serta header | [#18](https://github.com/SallVea/UTS-PPL/issues/18), [#19](https://github.com/SallVea/UTS-PPL/issues/19) | gambar=ya; lampiran=tidak |
| 58 | 31 | TC-CORE-04 | Keranjang - Tambah produk dari detail ke keranjang belanja | TIDAK ADA | gambar=ya; lampiran=tidak |
| 59 | 31 | TC-CORE-05 | Keranjang - Ubah kuantitas produk valid memperbarui subtotal dan total | TIDAK ADA | gambar=ya; lampiran=tidak |
| 60 | 31 | TC-CORE-06 | Keranjang - Hapus produk dari keranjang dan verifikasi hitung ulang total | TIDAK ADA | gambar=ya; lampiran=tidak |
| 61 | 31 | TC-CORE-07 | Checkout - Selesaikan proses checkout pembayaran hingga konfirmasi invoice | [#8](https://github.com/SallVea/UTS-PPL/issues/8), [#24](https://github.com/SallVea/UTS-PPL/issues/24), [#25](https://github.com/SallVea/UTS-PPL/issues/25), [#32](https://github.com/SallVea/UTS-PPL/issues/32) | gambar=ya; lampiran=tidak |
| 62 | 31 | TC-EP-01 | Quantity - Qty 1 (Batas bawah partisi valid) | [#26](https://github.com/SallVea/UTS-PPL/issues/26) | gambar=ya; lampiran=tidak |
| 63 | 31 | TC-EP-02 | Quantity - Qty 0 (Tepat di bawah batas bawah / invalid) | [#28](https://github.com/SallVea/UTS-PPL/issues/28) | gambar=ya; lampiran=tidak |
| 64 | 31 | TC-EP-03 | Quantity - Qty 10 (Wakil partisi valid tengah) | [#26](https://github.com/SallVea/UTS-PPL/issues/26) | gambar=ya; lampiran=tidak |
| 65 | 31 | TC-EP-04 | Quantity - Qty 100 (U+1, tepat di atas batas stok 99 / invalid) | [#29](https://github.com/SallVea/UTS-PPL/issues/29) | gambar=ya; lampiran=tidak |
| 67 | 31 | TC-EP-06 | Email Login - Format invalid tanpa karakter '@' | [#33](https://github.com/SallVea/UTS-PPL/issues/33) | gambar=ya; lampiran=tidak |
| 68 | 31 | TC-EP-07 | Email Login - Format invalid tanpa nama domain | [#33](https://github.com/SallVea/UTS-PPL/issues/33) | gambar=ya; lampiran=tidak |
| 69 | 31 | TC-EP-08 | Expiration Date - Tanggal valid masa depan (MM/YYYY) | [#31](https://github.com/SallVea/UTS-PPL/issues/31) | gambar=ya; lampiran=tidak |
| 70 | 31 | TC-EP-09 | Expiration Date - Bulan 13 dan 00 (di luar rentang bulan 01-12) | [#31](https://github.com/SallVea/UTS-PPL/issues/31) | gambar=ya; lampiran=tidak |
| 72 | 31 | TC-EG-01 | Kuantitas berubah cepat berulang kali menjaga konsistensi total | TIDAK ADA | gambar=ya; lampiran=tidak |
| 73 | 31 | TC-EG-02 | Konsistensi harga satuan antara katalog, keranjang, dan checkout | [#20](https://github.com/SallVea/UTS-PPL/issues/20), [#21](https://github.com/SallVea/UTS-PPL/issues/21), [#22](https://github.com/SallVea/UTS-PPL/issues/22), [#23](https://github.com/SallVea/UTS-PPL/issues/23) | gambar=ya; lampiran=tidak |
| 75 | 31 | TC-EG-04 | Persistensi filter kategori dan slider harga saat navigasi paginasi | TIDAK ADA | gambar=ya; lampiran=tidak |
| 78 | 31 | TC-NEG-02 | Nilai negatif: Input angka negatif (-1) pada kuantitas keranjang | [#28](https://github.com/SallVea/UTS-PPL/issues/28) | gambar=ya; lampiran=tidak |
| 79 | 31 | TC-NEG-03 | Tipe salah: Input karakter alfabet/huruf pada field nomor pembayaran | [#31](https://github.com/SallVea/UTS-PPL/issues/31) | gambar=ya; lampiran=tidak |
| 80 | 31 | TC-NEG-04 | Karakter khusus: Input simbol khusus pada kotak pencarian beranda | [#30](https://github.com/SallVea/UTS-PPL/issues/30) | gambar=ya; lampiran=tidak |
| 81 | 31 | TC-NEG-05 | Buffer panjang: Input string 300+ karakter pada field alamat billing | [#27](https://github.com/SallVea/UTS-PPL/issues/27) | gambar=ya; lampiran=tidak |
| 83 | 31 | TC-NEG-07 | Klik ganda cepat pada tombol konfirmasi pesanan akhir | [#34](https://github.com/SallVea/UTS-PPL/issues/34) | gambar=ya; lampiran=tidak |
| 85 | 31 | TC-EXP-01 | Charter 1: Eksplorasi manipulasi keranjang dan alur checkout dinamis | [#7](https://github.com/SallVea/UTS-PPL/issues/7), [#8](https://github.com/SallVea/UTS-PPL/issues/8), [#29](https://github.com/SallVea/UTS-PPL/issues/29), [#30](https://github.com/SallVea/UTS-PPL/issues/30), [#34](https://github.com/SallVea/UTS-PPL/issues/34) | gambar=ya; lampiran=tidak |
| 86 | 31 | TC-EXP-02 | Charter 2: Eksplorasi pencarian katalog dan ketahanan sesi login/logout | [#38](https://github.com/SallVea/UTS-PPL/issues/38) | gambar=ya; lampiran=tidak |
| 87 | 31 | TC-EP-12 | Quantity - Input huruf dan desimal pada field kuantitas (EP P4/P5) | [#36](https://github.com/SallVea/UTS-PPL/issues/36), [#37](https://github.com/SallVea/UTS-PPL/issues/37) | gambar=ya; lampiran=tidak |
| 88 | 31 | TC-EP-11 | Email Login - Format invalid dengan dua simbol '@' (BVA 2 simbol @) | [#35](https://github.com/SallVea/UTS-PPL/issues/35) | gambar=ya; lampiran=tidak |
| 89 | 32 | TC-A11Y-01 | Pemeriksaan Label Input Email dan Password pada Halaman Login | [#39](https://github.com/SallVea/UTS-PPL/issues/39) | gambar=ya; lampiran=tidak |
| 90 | 33 | TC-A11Y-02 | Pemeriksaan Urutan Fokus Keyboard pada Halaman Login | [#40](https://github.com/SallVea/UTS-PPL/issues/40) | gambar=ya; lampiran=tidak |
| 91 | 34 | TC-T6-01 | Beranda & Filters - Verifikasi Panel Filter pada Tampilan Mobile | TIDAK ADA | gambar=ya; lampiran=tidak |
| 93 | 36 | TC-T6-02 | Search Produk - Verifikasi Fungsi Pencarian pada Berbagai Browser dan viewport mobile | TIDAK ADA | gambar=ya; lampiran=tidak |
| 96 | 39 | TC-T6-03 | Detail Produk - Verifikasi Tampilan dan Fungsi pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 97 | 40 | TC-T6-04 | Keranjang & Checkout - Verifikasi Alur Pembelian pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 98 | 41 | TC-T6-05 | Contact Us - Verifikasi Tampilan dan Fungsi Formulir pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 99 | 42 | TC-T6-06 | Login - Verifikasi Fungsi dan Tampilan Login pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 100 | 43 | TC-T6-07 | Register - Verifikasi Tampilan dan Validasi Formulir pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 101 | 44 | TC-T6-08 | Navigasi Home - Verifikasi Fungsi Navigasi pada Berbagai Browser dan Viewport | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 103 | 46 | TC-A11Y-03 | Detail Produk - Audit Aksesibilitas Menggunakan axe DevTools, WAVE, dan Lighthouse Mobile | TIDAK ADA | gambar=tidak; lampiran=tidak |
| 104 | 47 | TC-A11Y-04 | Login - Audit Aksesibilitas Menggunakan axe DevTools, WAVE, dan Lighthouse Mobile | TIDAK ADA | gambar=tidak; lampiran=tidak |

Catatan: 39 eksekusi FAILED; 24 di antaranya menyebut minimal satu nomor issue di komentar Kiwi, 15 tidak menyebut issue. Isi komentar tidak disalin; hanya nomor issue dan penanda boolean.

## 7. Catatan drift data

| Waktu | Plan 1 run | Plan 1 eksekusi | Status plan 1 | Plan 2 eksekusi |
|---|---:|---:|---|---:|
| 2026-10-25T09:16Z | 17 | 47 | 6 P, 37 F, 2 B, 1 ERROR, 1 IDLE | 30 |
| 2026-10-25T10:40Z | 15 | 48 | 7 P, 39 F, 2 B | 31 |

Perubahan terjadi di Kiwi selama sesi (bukan oleh skrip ini): run kosong 6/10/11 tidak lagi ada di plan 1; run 35 dan 38 pindah ke plan 2; run 46/47 ditambahkan; TE 102 berubah IDLE → PASSED.


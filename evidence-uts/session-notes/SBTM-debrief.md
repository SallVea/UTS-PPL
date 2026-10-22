# Debrief SBTM T5 — 22 Oktober 2026

**Test Lead:** Atsaal (R1)  
**Peserta:** Atsaal (R1), Ikhsan (R3)  
**Acuan:** Session Notes TE-85 dan TE-86, oracle `https://practicesoftwaretesting.com`  
**Agenda:** review Session Notes, validasi temuan, pemilihan bug yang dieskalasi, dan action items.

## 1. Ringkasan Sesi

| Item | Sesi 1 | Sesi 2 |
|---|---|---|
| Test Case | `TC-EXP-01` (Charter 1) | `TC-EXP-02` (Charter 2) |
| Tester | Ikhsan (R3) | Atsaal (R1), reviewer Ikhsan (R3) |
| Tanggal | 21 Oktober 2026 | 22 Oktober 2026 |
| Durasi | 30 menit (23:07–23:37) | 30 menit (18:36–19:06) |
| Browser | Chrome | Firefox |
| Charter | Manipulasi keranjang dan alur checkout | Pencarian katalog, filter harga, sesi login/logout |
| Data uji | Kuantitas, billing, metode pembayaran | Keyword ekstrem, filter harga, pengetikan keyword; multi-tab/URL belum diuji |
| Session Notes | [TC-EXP-01](TC-EXP-01_session-notes.md) | [TC-EXP-02](TC-EXP-02_session-notes.md) |
| Rasio waktu | 100% | 100% |
| Eskalasi | 2 bug: #7, #8 | 1 bug: #38 |

## 2. Sesi 1 — Keranjang dan Checkout

**Temuan utama:** semua metode pembayaran memakai field Account Name/Number yang sama dan menampilkan opsi `Errror 304`; setelah Confirm tidak ada konfirmasi order atau nomor invoice; kuantitas dibatasi 10 tanpa toast; total baris `$00.00`; form billing memiliki typo, field tanpa label, dan tombol tanpa teks.

**Yang dieskalasi:**
- [#7](https://github.com/SallVea/UTS-PPL/issues/7) — Critical/P1, karena pembayaran non-COD tidak dapat diselesaikan.
- [#8](https://github.com/SallVea/UTS-PPL/issues/8) — Critical/P1, karena checkout berhenti tanpa invoice/konfirmasi.

**Alasan pemilihan:** dua temuan ini memblokir alur checkout dan merupakan temuan dengan severity tertinggi. Temuan kuantitas, total baris, dan form billing tetap dicatat di Session Notes sebagai observasi karena batas maksimal eskalasi per sesi adalah 2.

**Tindak lanjut:** klik ganda Confirm diuji sebagai `TC-NEG-07` (#34), qty 100 sebagai `TC-EP-04` (#29), dan Back/refresh sebagai `TC-NEG-08` (#30).

## 3. Sesi 2 — Pencarian dan Sesi

**Temuan utama:** keyword tanpa hasil menampilkan seluruh 26 produk; judul kartu berpindah saat slider harga diubah; nama produk berubah-ubah saat mengetik; area login/logout belum selesai diuji.

**Yang dieskalasi:**
- [#38](https://github.com/SallVea/UTS-PPL/issues/38) — Major/P2, karena hasil pencarian menampilkan produk yang tidak sesuai keyword dan bertentangan dengan oracle.

**Alasan pemilihan:** #38 adalah temuan dengan dampak terbesar dan bukti paling lengkap. Dua temuan lain berkategori Minor dan tidak memblokir alur utama; sesuai batas maksimal 2, keduanya dicatat sebagai observasi, bukan issue baru.

**Tindak lanjut:** uji paginasi, logout multi-tab, dan keyword nyata seperti `pliers`; temuan yang belum stabil dicatat sebagai observasi, bukan issue baru.

## 4. Keputusan Test Lead

1. Kedua sesi **diterima** sebagai sesi SBTM T5: 30 menit, tester berbeda, charter dan data uji berbeda.
2. Session Notes kedua sesi **lengkap** dan rasio waktu berjumlah **100%**.
3. Charter terdaftar sebagai test case **Exploratory P2** di Kiwi: `TC-EXP-01` dan `TC-EXP-02`.
4. Eskalasi dibatasi maksimal 2 bug per sesi: Sesi 1 = 2 bug, Sesi 2 = 1 bug. Tidak ada eskalasi berlebih.
5. Temuan yang tidak dieskalasi tetap tercatat sebagai observasi di Session Notes dan tidak dihapus.

## 5. Checklist T5

| Syarat | Bukti | Status |
|---|---|---|
| Dua sesi, masing-masing 30 menit | TE-85 dan TE-86 | Terpenuhi |
| Tester berbeda | Ikhsan (Sesi 1), Atsaal (Sesi 2) | Terpenuhi |
| Charter dan data uji berbeda | TC-EXP-01 vs TC-EXP-02 | Terpenuhi |
| Session Notes lengkap, rasio 100% | Dua file Session Notes di folder ini | Terpenuhi |
| Charter terdaftar sebagai Exploratory P2 | Test case 31 dan 32 di Kiwi | Terpenuhi |
| Debrief dengan Test Lead | Dokumen ini + komentar TE-85/TE-86 | Terpenuhi |
| Maksimal 2 bug dieskalasi per sesi | 2 dan 1 bug | Terpenuhi |

**Test Lead:** Atsaal (R1) — debrief selesai.

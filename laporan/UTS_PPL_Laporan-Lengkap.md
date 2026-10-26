# Laporan Uji Tenaga Semester — CilacapTools (Toolshop Sprint 5)

> Dokumen kerja Markdown. Versi akhir dikumpulkan dalam format PDF dengan nama
> berkas `UTS_PPL_Kelompok-XX_Fokus-X.pdf` — nomor kelompok dan nomor fokus
> ditetapkan manual (lihat `CHECKLIST-Laporan.md`).

---

## 0. Sampul, Pengesahan, dan Pernyataan

| Field | Nilai |
|---|---|
| Institusi | Politeknik Negeri Cilacap |
| Jurusan | Komputer dan Bisnis — Rekayasa Keamanan Siber |
| Mata kuliah / SKS | Praktikum Pengujian Perangkat Lunak / 2 SKS |
| Semester / TA | V Gasal / 2026/2027 |
| Dosen pengampu | Krisna Nuresa Qodri, S.T., M.Eng. |
| Kelompok | [ISI MANUAL: nomor kelompok] |
| Fokus pengujian | [ISI MANUAL: fokus] |
| Judul | Pengujian Aplikasi Toko Daring Toolshop (`with-bugs.practicesoftwaretesting.com`) |
| Nama berkas akhir | `UTS_PPL_Kelompok-XX_Fokus-X.pdf` |

### 0.1 Daftar Anggota dan Role

Role mengikuti Test Plan TP-1; nama lengkap dan NPM tidak tersedia di repositori.

| Role | Tanggung jawab utama | Anggota | Nama lengkap | NPM |
|---|---|---|---|---|
| R1 — QA Lead & Test Manager (melebur R5) | Test Plan/Run Kiwi, traceability, triage, repositori, summary & go/no-go | Atsaal | [ISI MANUAL: nama lengkap] | [ISI MANUAL: NPM] |
| R2 — Test Analyst | EP/BVA, error guessing, negative/edge testing, eksekusi | Gading | [ISI MANUAL: nama lengkap] | [ISI MANUAL: NPM] |
| R3 — Exploratory Tester (melebur pemeriksaan kualitas bug report) | Charter & Session Notes SBTM, debrief, kualitas bug report | Ikhsan | [ISI MANUAL: nama lengkap] | [ISI MANUAL: NPM] |
| R4 — Compatibility & Accessibility Tester | Cross-browser/responsive, axe/WAVE/Lighthouse, keyboard sweep | Mema | [ISI MANUAL: nama lengkap] | [ISI MANUAL: NPM] |

Sumber: `README.md` bagian "Tim dan role"; peleburan role R5 mengikuti ketentuan
soal untuk kelompok 4 orang (R5 dilebur ke R1 dan R3).

### 0.2 Pengesahan dan Pernyataan

[ISI MANUAL: lembar pengesahan — NPM, nama pengesah, tanggal pengesahan, tanda tangan]

[ISI MANUAL: pernyataan keaslian karya semua anggota — nama anggota, tanggal, tanda tangan]

Pengungkapan alat bantu: lihat **Lampiran D — Penggunaan Alat Bantu**.

---

## BAB I — Pendahuluan

### 1.1 Latar Belakang Studi Kasus

CilacapTools adalah toko perkakas daring milik UMKM di Cilacap yang akan membuka
penjualan online bulan depan. Mitra developer merilis build staging pertama
(Sprint 5) pada alamat Application Under Test (AUT)
`https://with-bugs.practicesoftwaretesting.com`. Versi tanpa cacat dari aplikasi
yang sama dipakai sebagai acuan perilaku yang benar (oracle)
`https://practicesoftwaretesting.com`. Pemilik toko menetapkan quality gate:
build hanya boleh dirilis jika seluruh test case berprioritas P1 dan P2
berstatus PASS dan tidak ada bug Critical atau Major yang masih terbuka.
Pemilik toko juga menerima dua keluhan: situs "terlihat berantakan" di sebagian
HP dan browser pelanggan, serta "sulit dipakai" oleh pengguna dengan
keterbatasan. (Sumber: `soal.md`, bagian Skenario dan Target Pengujian.)

Kelompok bertindak sebagai tim QE yang memeriksa satu paket fokus selama 7 hari,
lalu merekomendasikan go atau no-go rilis berdasarkan bukti. Tidak ada dokumen
spesifikasi; perilaku benar ditentukan dari (1) versi tanpa cacat, dan (2)
aturan yang tampil di antarmuka (placeholder, petunjuk, pesan validasi).

### 1.2 Tujuan

1. Melakukan pengujian fungsional, kompatibilitas, dan aksesibilitas pada build
   staging Sprint 5 aplikasi Toolshop dengan data dummy.
2. Mengelola test case, eksekusi, dan hasilnya di Kiwi TCMS, serta mengelola
   bug report di GitHub Issues.
3. Menyusun metrik eksekusi (coverage, defect density, distribusi
   severity/priority) dan merekomendasikan go atau no-go rilis berdasarkan
   kriteria quality gate.
4. Menjawab keluhan pemilik toko tentang tampilan lintas perangkat (T6) dan
   kemudahan penggunaan bagi pengguna berkebutuhan khusus (T7) dengan data.

### 1.3 Ruang Lingkup Fokus Pengujian

| Komponen | Area | Sumber |
|---|---|---|
| Wajib (semua kelompok) | Beranda (Home), alur login | `soal.md` (Fokus), `README.md` |
| Pilihan kelompok | Keranjang dan Checkout — tambah/ubah/hapus item, kalkulasi total, alur checkout sampai pembayaran dengan data dummy | `README.md` |

Kelompok memilih fokus pilihan **Keranjang dan Checkout** (tercatat di
`README.md`). Nomor fokus untuk nama berkas akhir: [ISI MANUAL: fokus].

### 1.4 Batasan

Batasan pengujian mengikuti `soal.md` (Target Pengujian dan Aturan) dan
`README.md` (bagian Batasan):

- Hanya pengujian **fungsional, kompatibilitas, dan aksesibilitas**. Tidak
  diperkenankan pemindaian kerentanan, brute force, injeksi, dan uji beban.
- Menggunakan **data dummy**; tidak memakai nama, alamat, nomor kartu, atau
  password asli yang dipakai di layanan lain.
- Tidak mengubah password atau tidak menghapus data akun demo bersama, dan
  tidak melakukan operasi destruktif memakai akun admin.
- Fitur lupa password benar-benar mengatur ulang password akun; tidak dipakai
  pada akun demo bersama, hanya pada akun yang didaftarkan sendiri.
- Spesifikasi API (Swagger) dibaca sebagai referensi, dan tab Network pada
  DevTools boleh dipakai sebagai evidence.
- Perilaku yang sama persis dengan versi tanpa cacat bukan bug; dicatat sebagai
  observasi atau pertanyaan di Session Notes.

---

## BAB II — Landasan Teori

Ringkasan konsep; tanpa kutipan pustaka. Bagian ini ditandai
"PERLU DIBACA ULANG OLEH PENULIS" di `CHECKLIST-Laporan.md`.

- **Status eksekusi.** Status terakhir dari menjalankan sebuah test case pada
  satu test run, umumnya PASS (sesuai expected result), FAIL (tidak sesuai),
  atau BLOCKED (tidak dapat dijalankan karena dependensi).
- **Lifecycle bug.** Siklus hidup cacat: ditemukan (failed execution) →
  dilaporkan (issue baru) → ditriage dan ditetapkan severity/priority →
  diperbaiki → diverifikasi ulang → ditutup; status juga dapat berubah menjadi
  duplikat, invalid, atau wontfix.
- **Severity.** Tingkat dampak teknis cacat terhadap fungsi atau data, misalnya
  Critical (alur bisnis utama terblokir total), Major (fitur utama gagal atau
  hasil salah), Minor (fitur terganggu tetapi ada workaround), Trivial
  (kosmetik/typo).
- **Priority.** Urutan kapan cacat harus diperbaiki (P1 blocker rilis, P2
  target sprint berjalan, P3 sprint berikutnya, P4 backlog), ditentukan dari
  dampak, jumlah pengguna terdampak, dan posisi di alur rilis; severity dan
  priority ditetapkan terpisah (lihat matriks pada `evidence-uts/severity-priority-matrix.md`).
- **Evidence.** Bukti yang membuat temuan dapat diverifikasi ulang; berupa
  screenshot layar penuh, screen recording untuk bug intermiten/urutan
  interaksi, dan log console/network untuk error JavaScript.
- **Anatomi bug report.** Penataan isi laporan cacat: judul, langkah
  reproduksi, expected result (termasuk hasil pada versi tanpa cacat), actual
  result, evidence, environment/build, tautan eksekusi Kiwi, serta severity dan
  priority beserta alasannya.
- **Metrik pengujian.** Ukuran kuantitatif proses dan hasil, misalnya coverage
  eksekusi (test case dieksekusi / direncanakan), defect density per area
  (jumlah bug / jumlah test case × 100%), distribusi severity dan priority.
- **Equivalence Partitioning (EP).** Membagi domain masukan ke partisi yang
  diperlakukan sama, lalu memilih satu wakil per partisi untuk diuji.
- **Boundary Value Analysis (BVA).** Menguji nilai tepat pada, tepat di bawah,
  dan tepat di atas batas partisi, karena cacat sering muncul di tepi.
- **Error guessing.** Merancang pengujian dari pengalaman tester terhadap
  titik lemah yang sering salah, misalnya input cepat berulang dan navigasi
  yang tidak biasa.
- **Negative testing.** Menguji input atau kondisi yang tidak valid (kosong,
  tipe salah, karakter khusus, nilai negatif) untuk memastikan sistem
  menolaknya dengan tertib.
- **Session-Based Test Management (SBTM).** Pengujian exploratory terstruktur
  dalam sesi berwaktu tetap dengan charter; hasil dicatat sebagai Session Notes
  dengan rasio waktu, lalu dibahas pada debrief.
- **Cross-browser testing.** Memeriksa fungsi dan tampilan halaman yang sama
  pada beberapa browser (mis. Chrome, Firefox, Edge) agar perbedaan rendering
  dan perilaku terdokumentasi.
- **Responsive testing.** Memeriksa tampilan dan fungsi pada beberapa ukuran
  layar/viewport (DevTools) dan perangkat/emulator nyata.
- **WCAG, POUR, level A/AA/AAA.** Web Content Accessibility Guidelines
  menyusun kemudahan akses web di seputar empat prinsip (Perceivable,
  Operable, Understandable, Robust) dan tingkat kepatuhan A, AA, serta AAA
  yang bertingkat.
- **Batas pengujian aksesibilitas otomatis.** Alat audit otomatis (axe,
  WAVE, Lighthouse) hanya dapat mendeteksi sebagian pelanggaran; pemakaian
  keyboard, urutan fokus, dan keterbacaan konten perlu dipastikan secara
  manual, sehingga alat otomatis tidak boleh dianggap mencakup seluruh
  kriteria WCAG.

---

## BAB III — Perencanaan dan Lingkungan Uji

### 3.1 Test Plan dan Kriteria Keberhasilan

- Test Plan di Kiwi TCMS: **"Test Plan UTS PPL Sprint 5 - CilacapTools"**
  (nama tercantum pada data plan 1, `laporan/data/kiwi-cases.json`).
- Kriteria keberhasilan (quality gate) sesuai `soal.md` T1 dan `README.md`:
  1. Seluruh test case prioritas **P1 dan P2 berstatus PASS**.
  2. **Tidak ada bug Critical atau Major yang masih OPEN**.
  3. Jika salah satu tidak terpenuhi, rekomendasi rilis adalah **NO-GO**.
- Teks lengkap Test Plan TP-1: [ISI MANUAL: teks Test Plan TP-1 — kriteria dan
  persiapan Kiwi: Classification, Product, Version, dan Build].

### 3.2 Versi Build dan Lingkungan

| Item | Nilai | Sumber |
|---|---|---|
| AUT | `https://with-bugs.practicesoftwaretesting.com` | `soal.md`, `README.md` |
| Oracle | `https://practicesoftwaretesting.com` | `soal.md`, `README.md` |
| Build | `Build-2024-S5-01` (Angular 20.0.5) | `laporan/data/kiwi-executions.json` |
| Versi build (catatan sesi) | Build v2.5 (2026-10-11) | `evidence-uts/session-notes/TC-EXP-01_session-notes.md` |
| Manajemen uji | Kiwi TCMS lokal (Docker) | `README.md` |
| Browser yang tercatat dipakai | Chrome (Sesi 1), Firefox (Sesi 2) | Session Notes T5 |
| OS, versi browser lain, Edge, emulator/perangkat, dan versi alat audit | [ISI MANUAL: OS dan versi dipakai tiap tester; emulator atau perangkat nyata T6] | — |

Alat audit aksesibilitas yang direncanakan (T7): axe DevTools, WAVE, dan
Lighthouse (kategori Accessibility, mode Mobile) pada minimal dua halaman
(`soal.md` T7; nama disebut pada `TC-A11Y-03` dan `TC-A11Y-04`).

### 3.3 Data Uji

Data uji memakai data dummy sesuai batasan Bab I. Data uji yang tercatat:

- Variasi kuantitas (1, 5, 2, 4), kuantitas ekstrem (10, 100), pengisian
  billing, pergantian metode pembayaran (Sesi 1, `TC-EXP-01_session-notes.md`).
- Keyword ekstrem, filter rentang harga, pengetikan keyword; multi-tab dan URL
  langsung belum diuji (Sesi 2, `TC-EXP-02_session-notes.md`).
- Partisi Quantity, Email Login, dan Expiration Date (Bab IV).

### 3.4 Role dan Jadwal

| Role | Luaran individu | Sumber |
|---|---|---|
| R1 (Atsaal) | Test Plan dan Test Run, Test Execution Summary, metrik, keputusan go/no-go; repositori, label, template, notulen triage | `soal.md`, `README.md`, `laporan/T9-test-execution-summary.md` |
| R2 (Gading) | Tabel partisi dan titik batas, error guessing, test case negatif/edge dan hasilnya | `soal.md`, `README.md` |
| R3 (Ikhsan) | Dua charter, Session Notes dengan rasio waktu, debrief; pemeriksaan kualitas bug report | `soal.md`, `README.md` |
| R4 (Mema) | Matriks cross-browser/responsive, matriks axe/WAVE/Lighthouse, prioritisasi temuan | `soal.md`, `README.md` |

Jadwal per hari selama 7 hari: [ISI MANUAL: pembagian jadwal per hari].

### 3.5 Daftar Risiko Pengujian

TIDAK ADA DATA — daftar risiko pengujian belum ditemukan pada berkas repo
(`README.md`, `evidence-uts/`, dan data Kiwi tidak memuat daftar risiko).

### 3.6 Strategi Test Oracle

- Acuan perilaku benar: versi tanpa cacat `https://practicesoftwaretesting.com`.
- Perilaku yang benar juga ditentukan dari aturan yang tampil di antarmuka
  (placeholder, petunjuk, pesan validasi).
- Sebuah temuan dianggap bug hanya jika perilakunya berbeda dari versi tanpa
  cacat atau melanggar aturan yang terlihat di antarmuka.
- Alur kerja cacat: reproduksi di AUT dibandingkan dengan oracle; hasil sama
  persis dengan oracle dicatat sebagai observasi di Session Notes, bukan bug
  (`README.md` bagian "Alur pelaporan bug").

---

## BAB IV — Desain Pengujian

Sumber utama bagian ini: teks Test Plan TP-1 dan test case di Kiwi (baca-saja).
Teks TP-1 tidak tersedia sebagai berkas di repo; tabel partisi dan titik batas
di bawah disusun dari **nama test case dan deskriasinya di data Kiwi**
(`laporan/data/kiwi-cases.json`, plan 1) yang mengelompokkan field,
prioritas, dan keterkaitannya.

### 4.1 Tabel Partisi dan Titik Batas — Quantity (angka, kolom kuantitas keranjang)

**Tabel 4.1** Partisi dan titik batas field Quantity (sumber: ringkasan test
case EP-BVA; hasil dianggap per 25 Okt 2026)

| No | Input | Klasifikasi | Titik batas / alasan | Test case | Hasil eksekusi |
|---:|---|---|---|---|---|
| 1 | 0 | Invalid | Tepat di bawah batas bawah; oracle menolak dan kembali ke 1 | `TC-EP-02` | FAILED (#28), FAILED (#28 juga dari `TC-NEG-02`) |
| 2 | 1 | Valid | Batas bawah partisi valid | `TC-EP-01` | FAILED (#26) |
| 3 | 2–9 | Valid | Wakil partisi valid | — | [ISI MANUAL] |
| 4 | 10 | Valid | Wakil partisi valid tengah; juga batas perilaku AUT (dipotong tanpa peringatan) | `TC-EP-03` | FAILED (#26) |
| 5 | 100 | Invalid | U+1, tepat di atas batas stok 99; AUT memotong ke 10 tanpa peringatan | `TC-EP-04` | FAILED (#29) |
| 6 | huruf / desimal 1.5 | Invalid | Tipe salah pada field kuantitas | `TC-EP-12` | FAILED (#36), FAILED (#37) |
| 7 | -1 | Invalid | Nilai negatif (negative testing) | `TC-NEG-02` | FAILED (#28) |

Catatan data: perilaku AUT membatasi kuantitas ke 10 tanpa peringatan (baru
dibatasi hanya di bagian atas), sedangkan aturan oracle membatasi 99, tercatat
pada Session Notes Sesi 1 (#29 dipilih dari dugaan ini) dan pada `triage-notes.md` untuk #29.

### 4.2 Tabel Partisi dan Titik Batas — Email (Login)

**Tabel 4.2** Partisi field Email Login (sumber: test case EP-BVA)

| No | Input | Klasifikasi | Test case | Hasil eksekusi |
|---:|---|---|---|---|
| 1 | Format email valid | Valid | `TC-EP-05` | PASSED |
| 2 | Tanpa karakter '@' | Invalid | `TC-EP-06` | FAILED (#33) |
| 3 | Tanpa nama domain | Invalid | `TC-EP-07` | FAILED (#33) |
| 4 | Dua simbol '@' (mis. `admin@@...`) | Invalid | `TC-EP-11` | FAILED (#35) |

Titik batas format email: [ISI MANUAL: tabel titik batas format email dari TP-1].

### 4.3 Tabel Partisi dan Titik Batas — Expiration Date (MM/YYYY)

**Tabel 4.3** Partisi field Expiration Date (sumber: test case EP-BVA)

| No | Input | Klasifikasi | Test case | Hasil eksekusi |
|---:|---|---|---|---|
| 1 | Tanggal valid masa depan | Valid | `TC-EP-08` | FAILED (#31: field kartu tidak muncul) |
| 2 | Bulan 13 dan 00 | Invalid (di luar rentang bulan 01–12) | `TC-EP-09` | FAILED (#31) |
| 3 | Tanggal lampau (kartu kedaluwarsa) | Invalid | `TC-EP-10` | BLOCKED (Bab VII) |

### 4.4 Dugaan Error Guessing (5)

| No | Dugaan | Test case | Hasil |
|---:|---|---|---|
| 1 | Kuantitas yang berubah cepat berulang kali menjaga konsistensi total | `TC-EG-01` | FAILED |
| 2 | Konsistensi harga satuan antara katalog, keranjang, dan checkout | `TC-EG-02` | FAILED (#20, #21, #22, #23) |
| 3 | Halaman akun tidak dapat diakses via tombol Back browser setelah logout | `TC-EG-03` | PASSED |
| 4 | Persistensi filter kategori dan slider harga saat navigasi paginasi | `TC-EG-04` | FAILED |
| 5 | Pencarian produk tidak sensitif huruf besar/kecil (case insensitive) | `TC-EG-05` | PASSED |

### 4.5 Test Case Negatif dan Edge (8)

| No | Skenario | Test case | Hasil |
|---:|---|---|---|
| 1 | Input kosong: seluruh field wajib form billing dikosongkan saat submit | `TC-NEG-01` | PASSED |
| 2 | Nilai negatif: angka negatif (-1) pada kuantitas keranjang | `TC-NEG-02` | FAILED (#28) |
| 3 | Tipe salah: karakter alfabet/huruf pada field nomor pembayaran | `TC-NEG-03` | FAILED (#31) |
| 4 | Karakter khusus: simbol khusus pada kotak pencarian beranda | `TC-NEG-04` | FAILED (#30) |
| 5 | Buffer panjang: string 300+ karakter pada field alamat billing | `TC-NEG-05` | FAILED (#27) |
| 6 | Karakter emoji: emoji Unicode pada field kota billing | `TC-NEG-06` | PASSED |
| 7 | Klik ganda cepat pada tombol konfirmasi pesanan akhir | `TC-NEG-07` | FAILED (#34) |
| 8 | Tombol Back browser setelah proses pembayaran order selesai | `TC-NEG-08` | BLOCKED |

### 4.6 Charter Exploratory (T5)

| No | Charter | Test case | Tester | Durasi | Bug dieskalasi |
|---|---|---|---|---|---|
| 1 | Explore keranjang belanja dan alur checkout — variasi ubah kuantitas, kuantitas ekstrem, pengisian billing, pergantian metode pembayaran, dan konfirmasi pembayaran — untuk menemukan anomali kalkulasi total, freeze pada form, atau error JavaScript yang tidak tertangani | `TC-EXP-01` | Ikhsan (R3) | 30 menit | #7, #8 (2 bug; batas maksimal 2) |
| 2 | Explore pencarian katalog, filter rentang harga, dan status sesi login/logout — manipulasi URL langsung, multi-tab browsing, dan penghentian sesi mendadak — untuk menemukan kebocoran data sesi, inkonsistensi hasil pencarian, atau broken link pada pagination | `TC-EXP-02` | Atsaal (R1), reviewer Ikhsan (R3) | 30 menit | #38 (1 bug; batas maksimal 2) |

Sumber: `evidence-uts/session-notes/TC-EXP-01_session-notes.md`,
`evidence-uts/session-notes/TC-EXP-02_session-notes.md`,
`evidence-uts/session-notes/SBTM-debrief.md`.

### 4.7 Rencana Cross-browser, Responsive, dan Aksesibilitas (T6/T7)

Dari test case T6 dan T7 di Kiwi (nama test case di `laporan/data/kiwi-cases.json`):

**Tabel 4.4** Rencana T6 — cross-browser & responsive (10 test case)

| No | Test case | Halaman/fitur | Browser dan viewport yang tercantum di teks test case |
|---:|---|---|---|
| 1 | `TC-T6-01` | Beranda & Filters | Tampilan Mobile |
| 2 | `TC-T6-02` | Search Produk | Berbagai browser dan viewport mobile |
| 3 | `TC-T6-03` | Detail Produk | Berbagai browser dan viewport |
| 4 | `TC-T6-04` | Keranjang & Checkout | Berbagai browser dan viewport |
| 5 | `TC-T6-05` | Contact Us | Berbagai browser dan viewport |
| 6 | `TC-T6-06` | Login | Berbagai browser dan viewport |
| 7 | `TC-T6-07` | Register | Berbagai browser dan viewport |
| 8 | `TC-T6-08` | Navigasi Home | Berbagai browser dan viewport |
| 9 | `TC-T6-09` | Filters | Viewport 820×1180 |
| 10 | `TC-T6-10` | Search Produk | Viewport 820×1180 |

**Tabel 4.5** Rencana T7 — aksesibilitas (4 test case)

| No | Test case | Halaman | Alat |
|---:|---|---|---|
| 1 | `TC-A11Y-01` | Login (label input Email dan Password) | Pemeriksaan label aksesibel |
| 2 | `TC-A11Y-02` | Login (urutan fokus keyboard) | Keyboard sweep |
| 3 | `TC-A11Y-03` | Detail Produk | axe DevTools, WAVE, Lighthouse Mobile |
| 4 | `TC-A11Y-04` | Login | axe DevTools, WAVE, Lighthouse Mobile |

Matriks lengkap per browser dan per viewport (Chrome, Firefox, Edge; empat
viewport `375x667`, `390x844`, `412x915`, `820x1180` sesuai `soal.md` T6) dan
matriks perbandingan axe/WAVE/Lighthouse: [ISI MANUAL: matriks per browser dan
viewport] dan [ISI MANUAL: matriks perbandingan axe/WAVE/Lighthouse].

### 4.8 Matriks Keterlacakan Fitur ke Test Case

Dari `laporan/data/kiwi-cases.json` (48 test case, plan 1, semua punya satu eksekusi).

**Tabel 4.6** Keterlacakan fitur → test case

| Fitur/kategori | Test case (kode, prioritas) |
|---|---|
| Beranda | `TC-CORE-01` (P1), `TC-CORE-02` (P1) |
| Login | `TC-CORE-03` (P1) |
| Keranjang & Checkout | `TC-CORE-04` (P1), `TC-CORE-05` (P1), `TC-CORE-06` (P1), `TC-CORE-07` (P1) |
| EP/BVA — Quantity | `TC-EP-01` (P1), `TC-EP-02` (P2), `TC-EP-03` (P2), `TC-EP-04` (P2), `TC-EP-12` (P2) |
| EP/BVA — Email Login | `TC-EP-05` (P1), `TC-EP-06` (P2), `TC-EP-07` (P2), `TC-EP-11` (P2) |
| EP/BVA — Expiration Date | `TC-EP-08` (P1), `TC-EP-09` (P2), `TC-EP-10` (P2) |
| Error Guessing | `TC-EG-01` (P1), `TC-EG-02` (P1), `TC-EG-03` (P2), `TC-EG-04` (P2), `TC-EG-05` (P2) |
| Negative/Edge | `TC-NEG-01` (P2), `TC-NEG-02` (P2), `TC-NEG-03` (P2), `TC-NEG-04` (P2), `TC-NEG-05` (P2), `TC-NEG-06` (P2), `TC-NEG-07` (P1), `TC-NEG-08` (P2) |
| Exploratory (charter) | `TC-EXP-01` (P2), `TC-EXP-02` (P2) |
| Cross-browser & responsive (T6) | `TC-T6-01` (P2), `TC-T6-02` (P2), `TC-T6-03` (P2), `TC-T6-04` (P1), `TC-T6-05` (P2), `TC-T6-06` (P1), `TC-T6-07` (P2), `TC-T6-08` (P2), `TC-T6-09` (P2), `TC-T6-10` (P2) |
| Aksesibilitas (T7) | `TC-A11Y-01` (P2), `TC-A11Y-02` (P2), `TC-A11Y-03` (P2), `TC-A11Y-04` (P2) |

---

## BAB V — Eksekusi dan Hasil

### 5.1 Rekap Test Run

**Tabel 5.1** Rekap Test Run — Plan 1 (48 eksekusi, cap waktu data
2026-10-26T05:07:03Z; sumber: `laporan/kiwi-snapshot.md` dan
`laporan/data/kiwi-executions.json`)

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

Rekapitulasi: 48 eksekusi pada 15 run — 7 PASSED, 39 FAILED, 2 BLOCKED
(`TC-EP-10` dan `TC-NEG-08`); seluruh 48 test case mempunyai satu eksekusi
(tidak ada TC tanpa eksekusi, tidak ada TC dengan lebih dari satu eksekusi di
plan 1).

**Tabel 5.2** Rekap per kategori (plan 1; sumber: `laporan/kiwi-snapshot.md`)

| Kategori | Eksekusi |
|---|---:|
| EP-BVA | 12 |
| Cross browser & responsive (T6) | 10 |
| Negatif-Edge | 8 |
| Error Guessing | 5 |
| Keranjang & Checkout (CORE) | 4 |
| Aksesibilitas (T7) | 4 |
| Beranda | 2 |
| Exploratory | 2 |
| Login | 1 |
| **Total** | **48** |

Eksekusi per prioritas: P1 = 15, P2 = 33. Eksekusi per tester (username Kiwi):
mema = 22, atsaal = 11, Gading = 8, ikhsan = 7 (Lampiran C).

### 5.2 Session Notes (T5)

Dua sesi SBTM, masing-masing 30 menit dengan tester berbeda; charter dan data
uji berbeda; rasio waktu berjumlah 100% pada kedua sesi
(`evidence-uts/session-notes/`).

**Tabel 5.3** Ringkasan Session Notes

| Item | Sesi 1 | Sesi 2 |
|---|---|---|
| Test case | `TC-EXP-01` | `TC-EXP-02` |
| Tester | Ikhsan (R3) | Atsaal (R1), reviewer Ikhsan (R3) |
| Tanggal/waktu | 21 Okt 2026, 23:07–23:37 WIB | 22 Okt 2026, 18:36–19:06 WIB |
| Browser | Chrome | Firefox |
| Rasio waktu | Setup 2 menit = 7%; Test design & execution 18 menit = 60%; Bug investigation & reporting 10 menit = 33% | Setup 7 menit = 23%; Test design & execution 13 menit = 44%; Bug investigation & reporting 10 menit = 33% |
| Temuan dieskalasi | #7, #8 (2 batas) | #38 (1 batas) |

Ringkasan temuan per sesi (kutipan dari Session Notes):

- Sesi 1 (`TC-EXP-01_session-notes.md`): form pembayaran semua metode memakai
  field Account Name/Number yang sama dan ada opsi "Errror 304 - Missing
  Payment Gateway" (#7); setelah Confirm payment tidak ada konfirmasi order
  dan nomor invoice (#8); kuantitas dibatasi maksimum 10 tanpa toast (dilaporkan
  terpisah sebagai #29); kolom total per baris $00.00 (dilaporkan sebagai
  #20); form billing tanpa label, data awal salah, tanpa auto-fill, tombol
  tanpa teks, judul typo (#24, #25 ditindaklanjuti lewat eksekusi lain).
  Observasi: saat qty 5 sebelum Enter, total sempat $694.80 lalu menjadi
  $634.75 setelah Enter, sama dengan acuan — "Bukan bug".
- Sesi 2 (`TC-EXP-02_session-notes.md`): keyword tanpa hasil menampilkan semua
  produk "26 products found" (#38; acuan "0 products found"). Observasi yang
  tidak dieskalasi: judul kartu rata kanan berpindah saat slider harga diubah;
  saat mengetik keyword, nama produk berubah-ubah (acuan tidak).

Debrief SBTM direkap di `evidence-uts/session-notes/SBTM-debrief.md`: kedua
sesi diterima, Session Notes lengkap, charter terdaftar sebagai test case
Exploratory P2, eskalasi tidak melebihi batas 2 bug per sesi.

![Charter 1 — evidence sesi 1](evidence-uts/session-notes/TC-EXP-01_evidence-01.png)

**Gambar 5.1** Evidence Charter 1 sesi SBTM (sumber: `evidence-uts/session-notes/TC-EXP-01_evidence-01.png`).

![Charter 1 — evidence sesi 1 kedua](evidence-uts/session-notes/TC-EXP-01_evidence-02.png)

**Gambar 5.2** Evidence Charter 1 sesi SBTM kedua (sumber: `evidence-uts/session-notes/TC-EXP-01_evidence-02.png`).

![Charter 2 — evidence sesi 2](evidence-uts/session-notes/TC-EXP-02_evidence-01.png)

**Gambar 5.3** Evidence Charter 2 sesi SBTM (sumber: `evidence-uts/session-notes/TC-EXP-02_evidence-01.png`).

### 5.3 Matriks Cross-browser dan Responsive (T6)

Data yang tersedia di repo adalah **status per test case** (`TC-T6-01` FAILED,
`TC-T6-02` FAILED, `TC-T6-03` FAILED, `TC-T6-04` FAILED, `TC-T6-05` FAILED,
`TC-T6-06` FAILED, `TC-T6-07` FAILED, `TC-T6-08` FAILED, `TC-T6-09` PASSED,
`TC-T6-10` PASSED; 10 test case pada Run 32–47) dan berkas PDF evidence
untuk 8 halaman/fitur: `SS_EVIDENCE - T6_BERANDA_FILTERS.pdf`,
`SS_EVIDENCE - T6_CONTACTUS.pdf`, `SS_EVIDENCE - T6_Detail_Produk.pdf`,
`SS_EVIDENCE - T6_KeranjangdanCheckout.pdf`, `SS_EVIDENCE - T6_LOGIN.pdf`,
`SS_EVIDENCE - T6_NAVIGASI_HOME.pdf`, `SS_EVIDENCE - T6_REGISTER_compressed.pdf`,
`SS_EVIDENCE - T6_SEARCH_PRODUCT.pdf` (di `evidence-uts/screenshots/`).

Matriks per browser (Chrome, Firefox, Edge) dan per viewport:
[ISI MANUAL: matriks per browser dan viewport].

### 5.4 Perbandingan axe, WAVE, Lighthouse (T7)

Data yang tersedia: status per test case — `TC-A11Y-01` FAILED (#39),
`TC-A11Y-02` FAILED (#40), `TC-A11Y-03` FAILED, `TC-A11Y-04` FAILED — dan
berkas `SS_EVIDENCE - T7_LOGIN.pdf`,
`SS_EVIDENCE - T7_DETAIL_PRODUK_COMBINATION_PLIERS.pdf`, serta
`EVIDENCE_T7_KEYBOARD_SWEEP.pdf` di `evidence-uts/screenshots/`. Sub-hasil
per alat (jumlah pelanggaran axe/WAVE/Lighthouse per halaman):
[ISI MANUAL: matriks perbandingan axe/WAVE/Lighthouse].

### 5.5 Indeks Evidence

Indeks lengkap seluruh berkas `evidence-uts/` ada di **Lampiran A**.

---

## BAB VI — Manajemen Cacat

Data cacat: 34 issue OPEN #7–#40 di GitHub
(`laporan/data/issues.json`, cap waktu 2026-10-26T05:07:03Z),
pemetaan test case/evidence dari `evidence-uts/t8-traceability.md`,
alasan severity/priority dari `evidence-uts/severity-priority-matrix.md`, dan
notulen triage dari `evidence-uts/triage-notes.md`.

**Tabel 6.1** Rekap seluruh bug

| ID | Judul (ringkas) | Severity | Priority | Status | Test case terkait | Evidence (berkas di `evidence-uts/screenshots/`) |
|---|---|---|---|---|---|---|
| [#7](https://github.com/SallVea/UTS-PPL/issues/7) | Semua metode pembayaran memakai field Account Name/Number dan ada opsi "Errror 304" | Critical | P1 | OPEN | `TC-EXP-01` | `BUG-007_payment-method-fields.png` |
| [#8](https://github.com/SallVea/UTS-PPL/issues/8) | Setelah Confirm payment tidak ada konfirmasi order dan nomor invoice | Critical | P1 | OPEN | `TC-CORE-07` | `BUG-008_no-order-confirmation.png` |
| [#9](https://github.com/SallVea/UTS-PPL/issues/9) | Logo header tidak tampil (broken image) | Minor | P2 | OPEN | `TC-CORE-01` | `BUG-009_logo-broken.png` |
| [#10](https://github.com/SallVea/UTS-PPL/issues/10) | Typo menu Contact tertulis Contakt | Trivial | P3 | OPEN | `TC-CORE-01` | `BUG-010_contact-typo.png` |
| [#11](https://github.com/SallVea/UTS-PPL/issues/11) | Item dropdown UNDEFINED menggantikan Other | Major | P1 | OPEN | `TC-CORE-01` | `BUG-011_undefined-category.png` |
| [#12](https://github.com/SallVea/UTS-PPL/issues/12) | Item Chainsaws menghasilkan 404 Page Not Found | Major | P1 | OPEN | `TC-CORE-01` | `BUG-012_chainsaws-404.png` |
| [#13](https://github.com/SallVea/UTS-PPL/issues/13) | Pemilih bahasa EN tidak ada di header | Minor | P3 | OPEN | `TC-CORE-01` | `BUG-013_language-selector-missing.png` |
| [#14](https://github.com/SallVea/UTS-PPL/issues/14) | Badge brand tampil "Brand name 1" | Minor | P3 | OPEN | `TC-CORE-02` | `BUG-014_brand-name-wrong.png` |
| [#15](https://github.com/SallVea/UTS-PPL/issues/15) | Bagian Specifications tidak tampil di detail produk | Minor | P2 | OPEN | `TC-CORE-02` | `BUG-015_specifications-missing.png` |
| [#16](https://github.com/SallVea/UTS-PPL/issues/16) | Tombol Compare tidak ada di katalog dan detail produk | Minor | P3 | OPEN | `TC-CORE-02` | `BUG-016_compare-button-missing.png` |
| [#17](https://github.com/SallVea/UTS-PPL/issues/17) | Badge ECO tampil padahal tidak ada di oracle | Minor | P3 | OPEN | `TC-CORE-02` | `BUG-017_eco-badge.png` |
| [#18](https://github.com/SallVea/UTS-PPL/issues/18) | Header menampilkan "User Data not found" setelah login | Minor | P2 | OPEN | `TC-CORE-03` | `BUG-018_user-data-not-found.png` |
| [#19](https://github.com/SallVea/UTS-PPL/issues/19) | Link Privacy Policy tidak ada di footer | Minor | P3 | OPEN | `TC-CORE-03` | `BUG-019_privacy-policy-missing.png` |
| [#20](https://github.com/SallVea/UTS-PPL/issues/20) | Total baris item menampilkan $00.00 | Major | P1 | OPEN | `TC-EG-02` | `BUG-020_row-total-zero.png` |
| [#21](https://github.com/SallVea/UTS-PPL/issues/21) | Header kolom Total muncul dua kali | Trivial | P3 | OPEN | `TC-EG-02` | `BUG-021_duplicate-total-header.png` |
| [#22](https://github.com/SallVea/UTS-PPL/issues/22) | Tombol Continue Shopping tidak ada di keranjang | Minor | P3 | OPEN | `TC-EG-02` | `BUG-022_continue-shopping-missing.png` |
| [#23](https://github.com/SallVea/UTS-PPL/issues/23) | Label langkah 3 tertulis ADDRESS, bukan BILLING ADDRESS | Trivial | P3 | OPEN | `TC-EG-02` | `BUG-023_address-label.png` |
| [#24](https://github.com/SallVea/UTS-PPL/issues/24) | Judul form billing tertulis Blliling Adress | Trivial | P3 | OPEN | `TC-CORE-07` (ditemukan saat `TC-NEG-01`) | `BUG-024_billing-title-typo.png` |
| [#25](https://github.com/SallVea/UTS-PPL/issues/25) | Tombol lanjut form billing tidak memiliki label teks | Minor | P2 | OPEN | `TC-CORE-07` (ditemukan saat `TC-NEG-01`) | `BUG-025_billing-button-no-label.png` |
| [#26](https://github.com/SallVea/UTS-PPL/issues/26) | Subtotal tetap 0 saat kuantitas diubah | Major | P1 | OPEN | `TC-EP-01` | `BUG-026_subtotal-zero.png` |
| [#27](https://github.com/SallVea/UTS-PPL/issues/27) | Alamat 320 karakter lolos validasi dan lanjut ke Payment | Minor | P2 | OPEN | `TC-NEG-05` | `BUG-027_address-320-chars.png` |
| [#28](https://github.com/SallVea/UTS-PPL/issues/28) | Quantity 0 diterima dan mengosongkan keranjang | Minor | P2 | OPEN | `TC-EP-02`; juga `TC-NEG-02` | `BUG-028_quantity-zero.png` |
| [#29](https://github.com/SallVea/UTS-PPL/issues/29) | Quantity di atas 10 dipotong ke 10 tanpa peringatan | Major | P2 | OPEN | `TC-EP-04` | `BUG-029_quantity-capped-10.png` |
| [#30](https://github.com/SallVea/UTS-PPL/issues/30) | Karakter khusus memicu HTTP 500 pada pencarian | Major | P2 | OPEN | `TC-NEG-04` | `BUG-030_search-special-chars-500.png` |
| [#31](https://github.com/SallVea/UTS-PPL/issues/31) | Credit Card menampilkan Account Name/Number, field kartu tidak muncul | Major | P1 | OPEN | `TC-EP-08` | `BUG-031_credit-card-fields-missing.png` |
| [#32](https://github.com/SallVea/UTS-PPL/issues/32) | POST /invoices mengembalikan 500, invoice tidak terbentuk | Major | P1 | OPEN | `TC-CORE-07` | `BUG-032_invoice-post-500.png` |
| [#33](https://github.com/SallVea/UTS-PPL/issues/33) | Validasi format email tidak sesuai saat input invalid | Minor | P2 | OPEN | `TC-EP-06`, `TC-EP-07` | `BUG-033_email-validation.png` |
| [#34](https://github.com/SallVea/UTS-PPL/issues/34) | Klik ganda cepat Confirm mengirim 2 request pembuatan pesanan | Major | P2 | OPEN | `TC-NEG-07` | `BUG-034_double-click-confirm.png`, `BUG-034_oracle-duplicate-order.png` |
| [#35](https://github.com/SallVea/UTS-PPL/issues/35) | Email dengan dua simbol @ tidak divalidasi formatnya | Minor | P2 | OPEN | `TC-EP-11` | `BUG-035_email-double-at.png` |
| [#36](https://github.com/SallVea/UTS-PPL/issues/36) | Kolom kuantitas menerima huruf dan total menjadi $0.00 | Minor | P2 | OPEN | `TC-EP-12` | `BUG-036_quantity-letters.png` |
| [#37](https://github.com/SallVea/UTS-PPL/issues/37) | Kuantitas desimal 1.5 diubah diam-diam menjadi 1 | Minor | P2 | OPEN | `TC-EP-12` | `BUG-037_quantity-decimal.png` |
| [#38](https://github.com/SallVea/UTS-PPL/issues/38) | Pencarian tanpa hasil menampilkan semua produk (26 products found) | Major | P2 | OPEN | `TC-EXP-02` | `BUG-038_search-no-result-all-products.png` |
| [#39](https://github.com/SallVea/UTS-PPL/issues/39) | Input Email dan Password terdeteksi tanpa label aksesibel (T7) | Major | P2 | OPEN | `TC-A11Y-01` | `BUG-039_login-input-missing-label-1.png`, `BUG-039_login-input-missing-label-2.png` |
| [#40](https://github.com/SallVea/UTS-PPL/issues/40) | Urutan fokus keyboard tidak sesuai alur formulir Login (T7) | Major | P2 | OPEN | `TC-A11Y-02` | `BUG-040_login-focus-order-1.png` … `BUG-040_login-focus-order-5.png` (5 berkas) |

Tabel 6.1 memuat 34 baris, sama dengan jumlah issue di
`laporan/data/issues.json` (34, #7–#40).

### 6.1 Alasan Severity dan Priority

Definisi label (kutipan `evidence-uts/severity-priority-matrix.md`):

| Severity | Definisi |
|---|---|
| Critical | Alur bisnis utama terblokir total, kehilangan data, atau risiko keamanan; tidak ada workaround. |
| Major | Fitur utama gagal atau hasil salah; workaround tidak wajar / berisiko. |
| Minor | Fitur terganggu, tetapi ada workaround; dampak terbatas. |
| Trivial | Kosmetik, typo, atau duplikasi tampilan. |

| Priority | Definisi | Target |
|---|---|---|
| P1 | Blocker rilis; harus diperbaiki sebelum build boleh GO. | Hari ini / sebelum rilis. |
| P2 | Tinggi; target sprint ini, tetapi tidak memblokir seluruh rilis. | Sprint berjalan. |
| P3 | Sedang; dikerjakan setelah P2. | Sprint berikutnya. |
| P4 | Rendah; jika ada waktu. | Backlog. |

**Tabel 6.2** Alasan severity/priority per bug (kutipan verbatim bagian
"Alasan" di `evidence-uts/severity-priority-matrix.md`)

| ID | Alasan (kutipan) |
|---|---|
| #7 | "Pembayaran non-COD tidak dapat diselesaikan karena field dan opsi metode salah." |
| #8 | "Alur checkout berhenti tanpa invoice atau halaman konfirmasi." |
| #9 | "Branding rusak di semua halaman, tetapi navigasi tetap berfungsi." |
| #10 | "Hanya kesalahan teks kosmetik." |
| #11 | "Kategori valid hilang dan diganti label UNDEFINED." |
| #12 | "Satu kategori tidak dapat dibuka sama sekali." |
| #13 | "Fitur bahasa hilang, tetapi ada workaround di browser." |
| #14 | "Data brand salah tampil, tetapi alur beli tetap berjalan." |
| #15 | "Informasi produk penting hilang sehingga keputusan pembelian terganggu." |
| #16 | "Fitur sekunder hilang, tidak memblokir pembelian." |
| #17 | "Informasi badge menyesatkan, tetapi tidak menghambat alur." |
| #18 | "Login berhasil, tetapi status pengguna di header salah." |
| #19 | "Masalah kepatuhan dan kepercayaan, bukan blocker fungsional." |
| #20 | "Kalkulasi harga per baris salah dan memengaruhi kepercayaan pada total." |
| #21 | "Duplikasi header hanya kosmetik." |
| #22 | "Navigasi kembali ke katalog hilang, tetapi ada workaround menu." |
| #23 | "Label langkah tidak konsisten, hanya kosmetik." |
| #24 | "Typo pada judul form, tidak menghambat pengisian." |
| #25 | "Tombol tanpa label menyulitkan pengguna, terutama screen reader." |
| #26 | "Kalkulasi subtotal inti salah saat qty berubah." |
| #27 | "Validasi panjang alamat tidak berjalan; data tidak wajar diterima." |
| #28 | "Validasi batas bawah gagal; keranjang bisa kosong tanpa konfirmasi." |
| #29 | "Aturan stok salah: oracle 99, AUT membatasi 10 tanpa notifikasi." |
| #30 | "Fitur pencarian rusak dan menghasilkan error server." |
| #31 | "Pembayaran kartu kredit tidak dapat dilakukan karena field wajib tidak tampil." |
| #32 | "Checkout gagal total dan invoice tidak terbentuk." |
| #33 | "Pesan validasi tidak spesifik, tetapi login tetap dicegah." |
| #34 | "Risiko duplikasi order akibat dua request." |
| #35 | "Pesan validasi email menyesatkan, tetapi login tetap dicegah." |
| #36 | "Input huruf merusak total keranjang, tetapi dapat diperbaiki dengan input ulang." |
| #37 | "Nilai desimal berubah tanpa peringatan dan berpotensi mengubah jumlah pesanan." |
| #38 | "Hasil pencarian menampilkan seluruh katalog dan menyesatkan pengguna." |
| #39 | ALASAN BELUM DITULIS |
| #40 | ALASAN BELUM DITULIS |

Catatan: severity dan priority #39 dan #40 berasal dari label issue di GitHub
(`severity:major`, `priority:P2`, tercatat di `laporan/data/issues.json`), tetapi
kalimat alasannya belum ditulis di `triage-notes.md` maupun di
`severity-priority-matrix.md`.

![Bug #7 — form pembayaran](evidence-uts/screenshots/BUG-007_payment-method-fields.png)

**Gambar 6.1** Bukti #7 (`BUG-007_payment-method-fields.png`): semua metode pembayaran memakai field Account Name/Number dan ada opsi "Errror 304".

![Bug #8 — tanpa konfirmasi](evidence-uts/screenshots/BUG-008_no-order-confirmation.png)

**Gambar 6.2** Bukti #8 (`BUG-008_no-order-confirmation.png`): tidak ada halaman konfirmasi dan nomor invoice setelah Confirm payment.

![Bug #20 — total baris $00.00](evidence-uts/screenshots/BUG-020_row-total-zero.png)

**Gambar 6.3** Bukti #20 (`BUG-020_row-total-zero.png`): total baris item menampilkan $00.00.

![Bug #26 — subtotal 0](evidence-uts/screenshots/BUG-026_subtotal-zero.png)

**Gambar 6.4** Bukti #26 (`BUG-026_subtotal-zero.png`): subtotal tetap 0 saat kuantitas diubah.

![Bug #32 — POST /invoices 500](evidence-uts/screenshots/BUG-032_invoice-post-500.png)

**Gambar 6.5** Bukti #32 (`BUG-032_invoice-post-500.png`): POST /invoices mengembalikan 500, invoice tidak terbentuk.

![Bug #30 — pencarian 500](evidence-uts/screenshots/BUG-030_search-special-chars-500.png)

**Gambar 6.6** Bukti #30 (`BUG-030_search-special-chars-500.png`): karakter khusus memicu HTTP 500 pada pencarian.

![Bug #38 — pencarian tanpa hasil](evidence-uts/screenshots/BUG-038_search-no-result-all-products.png)

**Gambar 6.7** Bukti #38 (`BUG-038_search-no-result-all-products.png`): keyword tanpa hasil menampilkan semua produk (26 products found).

![Bug #39 — label aksesibel input](evidence-uts/screenshots/BUG-039_login-input-missing-label-1.png)

**Gambar 6.8** Bukti #39 (`BUG-039_login-input-missing-label-1.png` dan `BUG-039_login-input-missing-label-2.png`): input Email dan Password terdeteksi tanpa label aksesibel.

![Bug #40 — urutan fokus](evidence-uts/screenshots/BUG-040_login-focus-order-1.png)

**Gambar 6.9** Bukti #40 (`BUG-040_login-focus-order-1.png` sampai `BUG-040_login-focus-order-5.png`, 5 berkas): urutan fokus keyboard tidak sesuai alur formulir Login.

### 6.2 Notulen Triage

Notulen triage 22 Oktober 2026 salinan verbatim dari
`evidence-uts/triage-notes.md` (bagian per issue; keputusan umum: seluruh issue dinyatakan valid dan
tetap OPEN sampai diperbaiki; peserta: Atsaal (Test Lead), Gading,
Ikhsan, Mema).

| ID | Tindak lanjut / catatan triage (kutipan verbatim) |
|---|---|
| #7 | "Ditemukan pada sesi EXP-01. Terkait #31, tetapi #31 hanya field kartu kredit; issue ini mencakup semua metode. Tindak lanjut: perbaiki pemetaan field per metode dan hapus opsi Errror 304." |
| #8 | "Gejala utama dari kegagalan POST /invoices. Terkait #32 sebagai akar teknis; tetap dicatat sebagai dampak pengguna. Tindak lanjut: verifikasi ulang setelah #32 diperbaiki." |
| #9 | "Logo broken.png 404 dan muncul di seluruh halaman. Tidak menghalangi alur, sehingga Minor/P2. Tindak lanjut: perbaiki aset logo." |
| #10 | "Typo terlihat pada header. Tidak memengaruhi fungsi, sehingga Trivial/P3. Tindak lanjut: perbaiki label." |
| #11 | "Navigasi kategori berubah dan membingungkan pengguna. Terkait #12 tetapi root cause berbeda (label vs route 404). Tindak lanjut: perbaiki data/label kategori." |
| #12 | "Klik Chainsaws mengarah ke route yang tidak ada. Bukan duplikat #11; keduanya perlu diperbaiki. Tindak lanjut: perbaiki route kategori." |
| #13 | "Tidak memblokir alur utama. Tindak lanjut: tambahkan pemilih bahasa atau dokumentasikan sebagai fitur nonaktif." |
| #14 | "Informasi produk tidak akurat dan mengurangi kepercayaan. Tindak lanjut: perbaiki relasi brand." |
| #15 | "Deskripsi masih tersedia sebagai workaround. Tindak lanjut: tampilkan spesifikasi dari data produk." |
| #16 | "Tindak lanjut: tambahkan tombol atau hapus dari ekspektasi oracle jika fitur memang tidak disediakan." |
| #17 | "Tindak lanjut: hapus badge atau sesuaikan dengan data produk." |
| #18 | "Membingungkan pengguna dan mengurangi kepercayaan pada sesi. Tindak lanjut: perbaiki pengambilan data user setelah login." |
| #19 | "Tindak lanjut: tambahkan link ke halaman kebijakan privasi." |
| #20 | "Terkait #26, tetapi #20 fokus total baris sedangkan #26 fokus subtotal setelah perubahan qty. Tindak lanjut: perbaiki kalkulasi baris." |
| #21 | "Tindak lanjut: hapus header duplikat." |
| #22 | "Tindak lanjut: tambahkan tombol atau link kembali." |
| #23 | "Tindak lanjut: perbaiki teks label." |
| #24 | "Ditemukan saat TC-NEG-01; eksekusi FAIL terkait adalah TC-CORE-07. Tindak lanjut: perbaiki teks." |
| #25 | "Ditemukan saat TC-NEG-01; eksekusi FAIL terkait adalah TC-CORE-07. Tindak lanjut: tambahkan label aksesibel." |
| #26 | "Terkait #20; keduanya dapat diperbaiki bersama. Tindak lanjut: sinkronkan state subtotal." |
| #27 | "Tidak memblokir, tetapi berpotensi merusak layout dan data. Tindak lanjut: tetapkan batas panjang dan pesan validasi." |
| #28 | "Ada workaround refresh, tetapi perilaku tidak sesuai oracle. Tindak lanjut: tolak 0 dan kembalikan ke 1." |
| #29 | "Bukan duplikat #28; #28 tentang batas bawah, #29 tentang batas atas. Tindak lanjut: ubah batas ke 99 dan tampilkan toast." |
| #30 | "Perlu log console/network untuk analisis root cause. Tindak lanjut: sanitasi input dan tangani error." |
| #31 | "Terkait #7; #7 mencakup semua metode, #31 spesifik kartu kredit. Tindak lanjut: render field per metode." |
| #32 | "Akar teknis dari #8. Tindak lanjut: perbaiki endpoint dan tambahkan error handling." |
| #33 | "Terkait TC-EP-07; eksekusi TE-68 juga FAIL. Tindak lanjut: tampilkan pesan format email yang jelas." |
| #34 | "Perlu screen recording urutan interaksi; saat ini bukti berupa dua screenshot, yaitu with-bugs dengan 2 request 500 dan oracle dengan 2 invoice. Tindak lanjut: nonaktifkan tombol setelah klik pertama." |
| #35 | "Input `admin@@practicesoftwaretesting.com` tidak ditandai sebagai format email salah; AUT menampilkan pesan kredensial yang menyesatkan, sedangkan oracle menandai field dan mencegah login. Tindak lanjut: validasi format email sebelum request autentikasi." |
| #36 | "Huruf dapat diketik pada kolom kuantitas, lalu total baris dan total keranjang berubah menjadi `$0.00` tanpa pesan error. Tindak lanjut: batasi input ke bilangan bulat dan tampilkan validasi." |
| #37 | "Nilai `1.5` langsung berubah menjadi `1` tanpa peringatan; oracle menampilkan popup bahwa kuantitas harus bilangan bulat. Tindak lanjut: gunakan validasi integer dan pesan error yang eksplisit." |
| #38 | "Keyword tanpa kecocokan tetap menampilkan `26 products found` dan seluruh katalog; oracle menampilkan `0 products found` beserta pesan kosong. Tindak lanjut: perbaiki query pencarian dan tampilkan empty state." |
| #39 | TIDAK ADA NOTULEN |
| #40 | TIDAK ADA NOTULEN |

---

## BAB VII — Metrik dan Summary

Seluruh angka bagian ini diambil dari `laporan/T9-test-execution-summary.md`
versi terbaru dan identik dengan dokumen tersebut.

**Tabel 7.1** Informasi Test Run (T9 Tabel 7.1)

| Item | Nilai |
|---|---|
| Test Run | Plan 1 — Run 31 konsolidasi + Run 32–47 T6/T7 |
| Test Plan | Test Plan UTS PPL Sprint 5 - CilacapTools |
| Build | `Build-2024-S5-01` (Angular 20.0.5) |
| Manajer | Atsaal |
| Eksekutor | Atsaal (11 TC), Gading (8 TC), Mema (22 TC), Ikhsan (7 TC) |
| Total test case | 48 |
| Status akhir | 7 PASSED, 39 FAILED, 2 BLOCKED |
| Sumber data | Kiwi TCMS Plan 1 dan GitHub Issues #7–#40 |

**Tabel 7.2** Test Execution Summary (T9 Tabel 7.2)

| Metrik | Nilai | Persentase |
|---|---:|---:|
| Test case direncanakan | 48 | 100% |
| Test case dieksekusi | 48 | 100% |
| PASSED | 7 | 14,6% |
| FAILED | 39 | 81,3% |
| BLOCKED | 2 | 4,2% |
| Issue OPEN | 34 | — |
| Defect density keseluruhan | 94,1 bug per 100 TC (area) / 100,0 bug per 100 TC (48 TC) | — |

**Tabel 7.3** Hasil berdasarkan priority test case (T9 Tabel 7.3)

| Priority | Total | PASSED | FAILED | BLOCKED | Pass rate |
|---|---:|---:|---:|---:|---:|
| P1 | 15 | 1 | 14 | 0 | 6,7% |
| P2 | 33 | 6 | 25 | 2 | 18,2% |
| **Total** | **48** | **7** | **39** | **2** | **14,6%** |

**Tabel 7.4** Coverage per paket fitur (T9 Tabel 7.4; basis 34 test case fungsional Run 31)

| Paket fitur | TC | Exec | PASS | FAIL | BLOCK | Coverage | Lulus |
|---|---:|---:|---:|---:|---:|---:|---:|
| Beranda/Katalog | 7 | 7 | 1 | 6 | 0 | 100% | 14,3% |
| Login | 6 | 6 | 2 | 4 | 0 | 100% | 33,3% |
| Keranjang | 10 | 10 | 0 | 10 | 0 | 100% | 0% |
| Checkout | 11 | 11 | 2 | 7 | 2 | 100% | 18,2% |
| **Total** | **34** | **34** | **5** | **27** | **2** | **100%** | **14,7%** |

**Tabel 7.5** Defect density per area (T9 Tabel 7.5; rumus
`defect density = (jumlah bug pada area / jumlah test case area) × 100%`;
"satu area primer per issue"; issue tanpa label scope tidak dihitung dalam
density per area)

| Area | Jumlah TC | Jumlah bug | Defect density | Issue |
|---|---:|---:|---:|---|
| Beranda & Katalog | 7 | 12 | **171,4%** | #9, #10, #11, #12, #13, #14, #15, #16, #17, #19, #30, #38 |
| Login & Auth | 6 | 3 | **50,0%** | #18, #33, #35 |
| Keranjang | 10 | 8 | **80,0%** | #20, #21, #22, #26, #28, #29, #36, #37 |
| Checkout & Pembayaran | 11 | 9 | **81,8%** | #7, #8, #23, #24, #25, #27, #31, #32, #34 |
| Tanpa area | — | 2 | — | #39, #40 |
| **Total** | **34** | **34** | **100,0%** | #7–#40 |

**Tabel 7.6** Distribusi severity issue OPEN (T9 Tabel 7.6)

| Severity | Jumlah | Persentase | Issue |
|---|---:|---:|---|
| Critical | 2 | 5,9% | #7, #8 |
| Major | 12 | 35,3% | #11, #12, #20, #26, #29, #30, #31, #32, #34, #38, #39, #40 |
| Minor | 16 | 47,1% | #9, #13, #14, #15, #16, #17, #18, #19, #22, #25, #27, #28, #33, #35, #36, #37 |
| Trivial | 4 | 11,8% | #10, #21, #23, #24 |
| **Total** | **34** | **100%** | — |

**Tabel 7.7** Distribusi priority issue OPEN (T9 Tabel 7.7)

| Priority | Jumlah | Persentase | Issue |
|---|---:|---:|---|
| P1 | 8 | 23,5% | #7, #8, #11, #12, #20, #26, #31, #32 |
| P2 | 16 | 47,1% | #9, #15, #18, #25, #27, #28, #29, #30, #33, #34, #35, #36, #37, #38, #39, #40 |
| P3 | 10 | 29,4% | #10, #13, #14, #16, #17, #19, #21, #22, #23, #24 |
| **Total** | **34** | **100%** | — |

**Tabel 7.8** Cross-tab priority dan severity (T9 Tabel 7.8)

| Priority | Critical | Major | Minor | Trivial | Total |
|---|---:|---:|---:|---:|---:|
| P1 | 2 | 6 | 0 | 0 | **8** |
| P2 | 0 | 6 | 10 | 0 | **16** |
| P3 | 0 | 0 | 6 | 4 | **10** |
| **Total** | **2** | **12** | **16** | **4** | **34** |

**Tabel 7.9** Evaluasi quality gate (T9 Tabel 7.9)

| Kriteria quality gate | Target | Aktual | Status |
|---|---|---|---|
| Seluruh test case P1 PASS | 15/15 PASS | 1/15 PASS, 14/15 FAILED | **GAGAL** |
| Seluruh test case P2 PASS | 33/33 PASS | 6/33 PASS, 25 FAILED, 2 BLOCKED | **GAGAL** |
| Tidak ada bug Critical/Major OPEN | 0 OPEN | 14 OPEN (2 Critical, 12 Major) | **GAGAL** |
| Eksekusi test case 100% | 48/48 | 48/48 | **LULUS** |
| Tidak ada test case BLOCKED | 0 | 2 | **GAGAL** |

**Rekomendasi: NO-GO.** Sesuai T9: `Build-2024-S5-01` tidak direkomendasikan
untuk rilis; empat dari lima kriteria quality gate gagal; satu-satunya kriteria
yang lulus adalah coverage eksekusi 100%, tetapi coverage tinggi tanpa hasil
PASS tidak menunjukkan kualitas produk. Alasan utama NO-GO (kutipan T9):

- Checkout tidak dapat diselesaikan sampai invoice terbentuk (#8, #32).
- Metode pembayaran tidak konsisten dan sebagian tidak dapat digunakan (#7, #31).
- Kalkulasi keranjang salah (#20, #26) dan batas kuantitas tidak sesuai oracle (#29).
- Pencarian dapat menghasilkan HTTP 500 (#30).
- Dua test case BLOCKED membuat verifikasi akhir alur pembayaran belum lengkap.

Rilis hanya boleh berstatus GO setelah seluruh P1/P2 PASS, tidak ada
Critical/Major OPEN, dan kedua test case BLOCKED sudah dieksekusi ulang pada
build baru.

**Tabel 7.10** Tindak lanjut sebelum rilis ulang (T9 Tabel 7.10)

| Prioritas | Tindakan | Penanggung jawab | Exit criteria |
|---|---|---|---|
| P0 | Perbaiki dan verifikasi checkout/payment #7, #8, #31, #32 | R1 + R2 | Checkout menghasilkan invoice; semua metode pembayaran menampilkan field yang benar |
| P0 | Perbaiki kalkulasi keranjang #20, #26 | R2 | Total baris dan subtotal sesuai oracle pada semua kuantitas |
| P1 | Perbaiki kategori dan stok #11, #12, #29 | R1 + R2 | Kategori valid; batas stok 99; tidak ada 404 |
| P1 | Perbaiki pencarian #30 dan #38 | R4 | Tidak ada HTTP 500; keyword tanpa hasil menampilkan 0 produk |
| P1 | Selesaikan BLOCKED `TC-EP-10` dan `TC-NEG-08` | R1 | Kedua test case punya status final dan evidence |
| P1 | Evaluasi hasil T6 dan T7 | R4 | 10 TC T6 (8 FAILED, 2 PASSED), 4 TC T7 (4 FAILED) |
| P2 | Perbaiki Major P2 #34 dan issue P2 lainnya | R1/R2/R4 | Tidak ada Major OPEN |
| P2 | Rerun seluruh 48 test case pada build baru | R1 | P1/P2 PASS; tidak ada Critical/Major OPEN |

Keluhan pemilik toko ("terlihat berantakan" di sebagian HP/browser dan "sulit
dipakai" oleh pengguna berkebutuhan khusus) dijawab dengan data T6 (10 test
case, 8 FAILED dan 2 PASSED) dan T7 (4 test case, semuanya FAILED, termasuk
#39 dan #40).

---

## BAB VIII — Analisis dan Refleksi

### 8.1 Bug yang Disingkirkan / Tidak Dieskalasi

Dari `evidence-uts/session-notes/` dan `evidence-uts/session-notes/SBTM-debrief.md`:

- **Bukan bug (disingkirkan):** pada Sesi 1, perubahan total sempat `$694.80`
  karena input Pliers belum di-commit, dan menjadi `$634.75` (sama dengan
  acuan) setelah Enter — "Bukan bug. Hipotesis EG-01 (race condition) tidak
  terbukti pada total keseluruhan." (`TC-EXP-01_session-notes.md`, catatan 23:17).
- **Observasi yang tidak dieskalasi (batas 2 bug per sesi):**
  - Sesi 1: kuantitas dibatasi maksimum 10 tanpa toast (#29 kemudian
    diuji/dilaporkan lewat `TC-EP-04` dan `TC-EP-04`), kolom total per baris
    `$00.00` (#20 kemudian diuji lewat `TC-EG-02`), form billing tanpa label
    dan typo (#24, #25 kemudian diuji/dilaporkan lewat `TC-NEG-01` dan
    `TC-CORE-07`), typo "Contakt", header "User Data not found", dan logo
    broken.png 404 ("Hanya dicatat, info ke R1").
  - Sesi 2: judul kartu rata kanan berpindah saat slider harga diubah, dan
    nama produk berubah-ubah saat mengetik keyword — keduanya Minor dan tidak
    memblokir alur utama, sehingga tidak menjadi issue baru
    (`TC-EXP-02_session-notes.md`, `SBTM-debrief.md` bagian Sesi 2).
- Daftar observasi lain di luarnya: TIDAK ADA DATA.

### 8.2 Batas Pengujian Aksesibilitas Otomatis (T7)

Alat audit otomatis (axe DevTools, WAVE, Lighthouse) menguji halaman yang
dirender dan melaporkan yang dapat dideteksi secara deterministik, seperti
label elemen formulir yang hilang (#39 pada `TC-A11Y-01`). Sebagian kriteria
WCAG terkait urutan fokus, operabilitas keyboard, dan keterbacaan konten tidak
sepenuhnya tertangkap oleh audit otomatis; hal itu perlu dipastikan manual —
pada proyek ini berupa pemeriksaan urutan fokus keyboard (keyboard sweep) yang
menghasilkan #40 pada `TC-A11Y-02`. Dengan demikian, hasil audit otomatis
dirangkap pembekuan temuan yang dapat diulang, bukan pengukuran penuh
kepatuhan WCAG; catatan batas pengujian otomatis dalam bentuk paragraf resmi:
[ISI MANUAL: paragraf batas pengujian otomatis versi final].

### 8.3 Kekurangan Proses dan Saran Perbaikan (berdasar catatan di repo)

Berdasarkan data yang tercantum:

- 15 dari 39 eksekusi FAILED mengandung komentar Kiwi yang **tidak
  menyebut** nomor issue (`laporan/kiwi-snapshot.md`, tabel semua eksekusi
  FAILED — TE 58, 59, 60, 72, 75, 91, 93, 96, 97, 98, 99, 100, 101, 103, 104);
  `soal.md` T8 mensyaratkan setiap bug ditautkan ke eksekusi FAIL.
- #39 dan #40 belum memiliki notulen triage (`triage-notes.md` berhenti di
  #38) dan belum memiliki kalimat alasan severity/priority
  (`severity-priority-matrix.md` berhenti di #38).
- Screen recording untuk #34 belum tersedia; bukti saat ini berupa dua
  screenshot dan urutan langkah pada komentar eksekusi
  (`t8-traceability.md`, "Catatan Evidence").
- Log console/network mentah untuk #30 dan #32 belum diekspor; status 500
  sudah terlihat pada screenshot (`t8-traceability.md`, "Catatan Evidence").
- Eksekusi `TC-T6-03` sampai `TC-A11Y-04` (TE 96, 97, 98, 99, 100, 101, 103,
  104) tidak menyertakan gambar maupun lampiran pada komentar Kiwi
  (`laporan/kiwi-snapshot.md`); PDF evidence untuk T6/T7 tersedia di repositori
  sebagai `SS_EVIDENCE - T6_*.pdf` dan `SS_EVIDENCE - T7_*.pdf`.
- Area sesi login/logout belum selesai diuji pada Sesi 2 (multi-tab, Back
  setelah logout, URL akun langsung) di `TC-EXP-02_session-notes.md`,
  dengan tindak lanjut terdapat di `SBTM-debrief.md`.

Saran perbaikan yang didukung catatan repo (kutipan "Tindak lanjut" di
`triage-notes.md` dan Tindak Lanjut `T9` daring pada Tabel 7.10). Refleksi
kualitas-kualitas proses lebih lanjut: [ISI MANUAL: catatan kekurangan proses
versi final].

### 8.4 Refleksi Individu

- **R1 — Atsaal (QA Lead & Test Manager):** [ISI MANUAL: refleksi setengah halaman]
- **R2 — Gading (Test Analyst):** [ISI MANUAL: refleksi setengah halaman]
- **R3 — Ikhsan (Exploratory Tester):** [ISI MANUAL: refleksi setengah halaman]
- **R4 — Mema (Compatibility & Accessibility Tester):** [ISI MANUAL: refleksi setengah halaman]

---

## LAMPIRAN A — Indeks Evidence

Semua berkas pada `evidence-uts/` (ukuran dalam byte). Tag **Bug terkait**
dibaca dari `evidence-uts/t8-traceability.md`; jika tidak ada pemetaan di
file itu, ditulis "TIDAK ADA PEMETAAN". Dalam tautan, spasi nama berkas
dirubah menjadi `%20`.

**Tabel A.1** Indeks evidence — `evidence-uts/screenshots/` (40 PNG + 11 PDF = 51 berkas)

| No | Subfolder | Nama berkas | Bug terkait | Ukuran (byte) |
|---:|---|---|---|---:|
| 1 | screenshots/ | `BUG-007_payment-method-fields.png` | #7 | 487090 |
| 2 | screenshots/ | `BUG-008_no-order-confirmation.png` | #8 | 480397 |
| 3 | screenshots/ | `BUG-009_logo-broken.png` | #9 | 800149 |
| 4 | screenshots/ | `BUG-010_contact-typo.png` | #10 | 800149 |
| 5 | screenshots/ | `BUG-011_undefined-category.png` | #11 | 800149 |
| 6 | screenshots/ | `BUG-012_chainsaws-404.png` | #12 | 120618 |
| 7 | screenshots/ | `BUG-013_language-selector-missing.png` | #13 | 800149 |
| 8 | screenshots/ | `BUG-014_brand-name-wrong.png` | #14 | 95316 |
| 9 | screenshots/ | `BUG-015_specifications-missing.png` | #15 | 450480 |
| 10 | screenshots/ | `BUG-016_compare-button-missing.png` | #16 | 450480 |
| 11 | screenshots/ | `BUG-017_eco-badge.png` | #17 | 450480 |
| 12 | screenshots/ | `BUG-018_user-data-not-found.png` | #18 | 134827 |
| 13 | screenshots/ | `BUG-019_privacy-policy-missing.png` | #19 | 115514 |
| 14 | screenshots/ | `BUG-020_row-total-zero.png` | #20 | 107281 |
| 15 | screenshots/ | `BUG-021_duplicate-total-header.png` | #21 | 129208 |
| 16 | screenshots/ | `BUG-022_continue-shopping-missing.png` | #22 | 107281 |
| 17 | screenshots/ | `BUG-023_address-label.png` | #23 | 129208 |
| 18 | screenshots/ | `BUG-024_billing-title-typo.png` | #24 | 4229 |
| 19 | screenshots/ | `BUG-025_billing-button-no-label.png` | #25 | 451 |
| 20 | screenshots/ | `BUG-026_subtotal-zero.png` | #26 | 89158 |
| 21 | screenshots/ | `BUG-027_address-320-chars.png` | #27 | 109743 |
| 22 | screenshots/ | `BUG-028_quantity-zero.png` | #28 | 84964 |
| 23 | screenshots/ | `BUG-029_quantity-capped-10.png` | #29 | 89445 |
| 24 | screenshots/ | `BUG-030_search-special-chars-500.png` | #30 | 959597 |
| 25 | screenshots/ | `BUG-031_credit-card-fields-missing.png` | #31 | 79899 |
| 26 | screenshots/ | `BUG-032_invoice-post-500.png` | #32 | 133192 |
| 27 | screenshots/ | `BUG-033_email-validation.png` | #33 | 313128 |
| 28 | screenshots/ | `BUG-034_double-click-confirm.png` | #34 | 170604 |
| 29 | screenshots/ | `BUG-034_oracle-duplicate-order.png` | #34 | 136994 |
| 30 | screenshots/ | `BUG-035_email-double-at.png` | #35 | 88887 |
| 31 | screenshots/ | `BUG-036_quantity-letters.png` | #36 | 100566 |
| 32 | screenshots/ | `BUG-037_quantity-decimal.png` | #37 | 130103 |
| 33 | screenshots/ | `BUG-038_search-no-result-all-products.png` | #38 | 439355 |
| 34 | screenshots/ | `BUG-039_login-input-missing-label-1.png` | #39 | 256286 |
| 35 | screenshots/ | `BUG-039_login-input-missing-label-2.png` | #39 | 248577 |
| 36 | screenshots/ | `BUG-040_login-focus-order-1.png` | #40 | 224236 |
| 37 | screenshots/ | `BUG-040_login-focus-order-2.png` | #40 | 188451 |
| 38 | screenshots/ | `BUG-040_login-focus-order-3.png` | #40 | 201257 |
| 39 | screenshots/ | `BUG-040_login-focus-order-4.png` | #40 | 209622 |
| 40 | screenshots/ | `BUG-040_login-focus-order-5.png` | #40 | 188665 |
| 41 | screenshots/ | [SS_EVIDENCE - T6_BERANDA_FILTERS.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_BERANDA_FILTERS.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-01`) | 1485203 |
| 42 | screenshots/ | [SS_EVIDENCE - T6_CONTACTUS.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_CONTACTUS.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-05`) | 10488839 |
| 43 | screenshots/ | [SS_EVIDENCE - T6_Detail_Produk.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_Detail_Produk.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-03`) | 9449388 |
| 44 | screenshots/ | [SS_EVIDENCE - T6_KeranjangdanCheckout.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_KeranjangdanCheckout.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-04`) | 22613724 |
| 45 | screenshots/ | [SS_EVIDENCE - T6_LOGIN.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_LOGIN.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-06`) | 15574031 |
| 46 | screenshots/ | [SS_EVIDENCE - T6_NAVIGASI_HOME.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_NAVIGASI_HOME.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-08`) | 3842969 |
| 47 | screenshots/ | [SS_EVIDENCE - T6_REGISTER_compressed.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_REGISTER_compressed.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-07`) | 5183579 |
| 48 | screenshots/ | [SS_EVIDENCE - T6_SEARCH_PRODUCT.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T6_SEARCH_PRODUCT.pdf) | TIDAK ADA PEMETAAN (evidence T6 `TC-T6-02`/`TC-T6-10`) | 1408364 |
| 49 | screenshots/ | [SS_EVIDENCE - T7_LOGIN.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T7_LOGIN.pdf) | TIDAK ADA PEMETAAN (evidence T7 `TC-A11Y-04`) | 4123566 |
| 50 | screenshots/ | [SS_EVIDENCE - T7_DETAIL_PRODUK_COMBINATION_PLIERS.pdf](evidence-uts/screenshots/SS_EVIDENCE%20-%20T7_DETAIL_PRODUK_COMBINATION_PLIERS.pdf) | TIDAK ADA PEMETAAN (evidence T7 `TC-A11Y-03`) | 6039943 |
| 51 | screenshots/ | [EVIDENCE_T7_KEYBOARD_SWEEP.pdf](evidence-uts/screenshots/EVIDENCE_T7_KEYBOARD_SWEEP.pdf) | TIDAK ADA PEMETAAN (evidence T7 keyboard sweep `TC-A11Y-02`) | 196210 |

**Tabel A.2** Indeks evidence — `evidence-uts/session-notes/` (2 Markdown + 7 PNG + 1 Markdown).

| No | Subfolder | Nama berkas | Bug terkait | Ukuran (byte) |
|---:|---|---|---|---:|
| 52 | session-notes/ | [TC-EXP-01_session-notes.md](evidence-uts/session-notes/TC-EXP-01_session-notes.md) | #7, #8 (eskalasi Charter 1) | 5635 |
| 53 | session-notes/ | [TC-EXP-01_evidence-01.png](evidence-uts/session-notes/TC-EXP-01_evidence-01.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 1) | 114168 |
| 54 | session-notes/ | [TC-EXP-01_evidence-02.png](evidence-uts/session-notes/TC-EXP-01_evidence-02.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 1) | 480397 |
| 55 | session-notes/ | [TC-EXP-02_session-notes.md](evidence-uts/session-notes/TC-EXP-02_session-notes.md) | #38 (eskalasi Charter 2) | 3638 |
| 56 | session-notes/ | [TC-EXP-02_evidence-01.png](evidence-uts/session-notes/TC-EXP-02_evidence-01.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 2) | 439355 |
| 57 | session-notes/ | [TC-EXP-02_evidence-02.png](evidence-uts/session-notes/TC-EXP-02_evidence-02.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 2) | 509665 |
| 58 | session-notes/ | [TC-EXP-02_evidence-03.png](evidence-uts/session-notes/TC-EXP-02_evidence-03.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 2) | 79928 |
| 59 | session-notes/ | [TC-EXP-02_evidence-04.png](evidence-uts/session-notes/TC-EXP-02_evidence-04.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 2) | 444997 |
| 60 | session-notes/ | [TC-EXP-02_evidence-05.png](evidence-uts/session-notes/TC-EXP-02_evidence-05.png) | TIDAK ADA PEMETAAN (evidence sesi SBTM 2) | 559116 |
| 61 | session-notes/ | [SBTM-debrief.md](evidence-uts/session-notes/SBTM-debrief.md) | TIDAK ADA PEMETAAN (notulen debrief SBTM) | 4195 |

**Tabel A.3** Indeks evidence — akar `evidence-uts/` (dokumen T8/T5 dan
panduan; berkas kosong `recordings/` dan `logs/` dipakai saat bug
intermiten, urutan interaksi, atau jurnal khusus diperlukan; saat ini belum ada
laporan yang membutuhkan)

| No | Subfolder | Nama berkas | Bug terkait | Ukuran (byte) |
|---:|---|---|---|---:|
| 62 | — | [README.md](evidence-uts/README.md) | TIDAK ADA PEMETAAN (panduan folder) | 1822 |
| 63 | — | [severity-priority-matrix.md](evidence-uts/severity-priority-matrix.md) | #7–#38 (alasan per issue) | 6174 |
| 64 | — | [t8-traceability.md](evidence-uts/t8-traceability.md) | #7–#40 (pemetaan) | 12402 |
| 65 | — | [triage-notes.md](evidence-uts/triage-notes.md) | #7–#38 (notulen) | 16792 |
| 66 | — | `recordings/` | TIDAK ADA PEMETAAN (folder kosong) | 0 |
| 67 | — | `logs/` | TIDAK ADA PEMETAAN (folder kosong) | 0 |

---

## LAMPIRAN B — Session Notes Lengkap

Isi lengkap Session Notes tidak disalin ulang di laporan ini; daftar dan
tautan:

- [TC-EXP-01_session-notes.md](evidence-uts/session-notes/TC-EXP-01_session-notes.md) — Charter 1,
  Ikhsan (R3), 21 Okt 2026, 23:07–23:37 WIB; charter, rasio waktu 7%/60%/33%,
  catatan kronologis, temuan, pertanyaan, dan evidence.
- [TC-EXP-02_session-notes.md](evidence-uts/session-notes/TC-EXP-02_session-notes.md) — Charter 2,
  Atsaal (R1) dengan reviewer Ikhsan (R3), 22 Okt 2026, 18:36–19:06 WIB;
  charter, rasio waktu 23%/44%/33%, catatan kronologis, temuan, pertanyaan, dan evidence.
- [SBTM-debrief.md](evidence-uts/session-notes/SBTM-debrief.md) — debrief Test
  Lead dengan keputusan eskalasi dan checklist T5.
- Evidence per sesi: 2 PNG (Charter 1) dan 5 PNG (Charter 2) pada folder yang
  sama (Lampiran A, Tabel A.2).

---

## LAMPIRAN C — Lembar Kontribusi dan Log

### C.1 Log Kiwi TCMS — plan 1 (cap waktu 2026-10-26T05:07:03Z)

Eksekusi per username (sumber: `laporan/data/kiwi-executions.json`):

| Username Kiwi | Jumlah eksekusi di plan 1 |
|---|---:|
| mema | 22 |
| atsaal | 11 |
| Gading | 8 |
| ikhsan | 7 |
| **Total** | **48** |

Test case dibuat per kategori per penulis (sumber: `laporan/data/kiwi-cases.json`):

| Username | Kategori → jumlah | Total |
|---|---|---:|
| atsaal | Beranda 2; Login 1; Keranjang & Checkout 1; Error Guessing 1; Negatif-Edge 3; EP-BVA 2 | 10 |
| Gading | EP-BVA 6; Negatif-Edge 2 | 8 |
| ikhsan | Keranjang & Checkout 3; Error Guessing 2; Negatif-Edge 1; Exploratory 2 | 8 |
| mema | EP-BVA 4; Error Guessing 2; Negatif-Edge 2; Aksesibilitas 4; Cross browser & responsive 10 | 22 |

### C.2 Log GitHub Issues (34 issue #7–#40)

| Login GitHub | Jumlah issue | Dipetakan ke anggota |
|---|---:|---|
| SallVea | 24 | [ISI MANUAL: pemetaan login ke anggota] |
| gadingrafa | 4 | [ISI MANUAL: pemetaan login ke anggota] |
| mema121 | 4 | [ISI MANUAL: pemetaan login ke anggota] |
| moochin071-cell | 2 | [ISI MANUAL: pemetaan login ke anggota] |

---

## LAMPIRAN D — Penggunaan Alat Bantu

Alat yang terdeteksi dari repo dan data:

| Alat | Dipakai untuk | Bukti di repo |
|---|---|---|
| Kiwi TCMS (lokal, Docker) | Manajemen test case, test run, eksekusi, komentar | `laporan/data/*.json`, `laporan/kiwi-snapshot.md` |
| GitHub Issues + label | Repositori cacat, template bug report, label severity/priority/scope | `.github/ISSUE_TEMPLATE/`, `README.md`, issue #7–#40 |
| gh CLI | Sinkronisasi baca-saja data issue | `laporan/sync_kiwi.py` |
| Python | `laporan/sync_kiwi.py` (XML-RPC baca-saja), `laporan/build_report.py`, `laporan/generate_charts.py` | berkas di `laporan/` |
| Chrome, Firefox | Browser pengujian tercatat pada Sesi 1 dan 2 | Session Notes T5 |
| axe DevTools, WAVE, Lighthouse (Mobile, Accessibility) | Audit aksesibilitas T7 | `TC-A11Y-03`, `TC-A11Y-04` |
| DevTools (viewport/emulator) | T6 cross-browser dan responsive | `TC-T6-*` |

Bagian alat bantu AI:

[ISI MANUAL: pengungkapan penggunaan alat bantu AI oleh tim: nama alat, tujuan, dan bagian yang dibantu]

---

## LAMPIRAN E — Tautan Repositori

- Repositori: https://github.com/SallVea/UTS-PPL
- Folder laporan: https://github.com/SallVea/UTS-PPL/tree/main/laporan
- Folder evidence: https://github.com/SallVea/UTS-PPL/tree/main/evidence-uts
- Data issue: https://github.com/SallVea/UTS-PPL/issues?q=is%3Aissue

---

## LAMPIRAN F — Formulir Penetapan Role

Fokus pengujian: **Keranjang dan Checkout** (wajib: Beranda, Login).
Tanggal penetapan: [ISI MANUAL: tanggal penetapan role].

| NPM | Nama | Role/Peran | Tanda Tangan |
|---|---|---|---|
| [ISI MANUAL: NPM] | [ISI MANUAL: nama] | R1 — QA Lead & Test Manager | [ISI MANUAL: tanda tangan] |
| [ISI MANUAL: NPM] | [ISI MANUAL: nama] | R2 — Test Analyst | [ISI MANUAL: tanda tangan] |
| [ISI MANUAL: NPM] | [ISI MANUAL: nama] | R3 — Exploratory Tester | [ISI MANUAL: tanda tangan] |
| [ISI MANUAL: NPM] | [ISI MANUAL: nama] | R4 — Compatibility & Accessibility Tester | [ISI MANUAL: tanda tangan] |

---

Akhiri dokumen. Laporan ini dikumpulkan sebagai PDF dengan nama berkas
`UTS_PPL_Kelompok-XX_Fokus-X.pdf` (ketentuan format: kertas A4, font 11–12 pt,
spasi 1,15, margin 2,5 cm; setiap tabel dan gambar bernomor dan berketerangan).

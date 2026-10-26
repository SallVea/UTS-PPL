# Checklist Pemeriksaan — Laporan Lengkap UTS PPL

Pemeriksaan atas `UTS_PPL_Laporan-Lengkap.md` terhadap ketentuan struktur
laporan pada bagian G `soal.md`. Status:

- **TERISI DARI DATA** — isi bersumber dari berkas repo/data Kiwi/GitHub.
- **ISI MANUAL** — ada placeholder `[ISI MANUAL: ...]` yang harus diisi penulis.
- **TIDAK ADA DATA** — data tidak tersedia di repo; ditulis persis begitu di laporan.
- **PERLU DIBACA ULANG** — ditulis dari pengetahuan umum dan perlu dibaca ulang penulis.

## 1. Tabel Checklist Bagian Laporan

| Bagian laporan | Status | Sumber data/berkas | Catatan |
|---|---|---|---|
| Sampul, identitas kelompok/fokus | ISI MANUAL | `soal.md`; role dari `README.md` | Nomor kelompok, fokus (nomor), kelas belum ada di repo |
| Daftar anggota dan role | TERISI DARI DATA (role) + ISI MANUAL (nama, NPM) | `README.md` "Tim dan role"; `soal.md` | Role R1 Atsaal, R2 Gading, R3 Ikhsan, R4 Mema |
| Pengesahan dan pernyataan | ISI MANUAL | — | Kerangka tersedia |
| Pengungkapan alat bantu AI | ISI MANUAL | Lampiran D | Jangan diisi agen; isi oleh tim |
| Bab I Pendahuluan | TERISI DARI DATA | `soal.md`, `README.md` | Latar belakang, tujuan, fokus, batasan |
| Bab II Landasan Teori | PERLU DIBACA ULANG OLEH PENULIS | — | Ditulis dari pengetahuan umum, tanpa kutipan pustaka |
| Bab III Test Plan & kriteria | TERISI DARI DATA + ISI MANUAL | Quality gate: `soal.md` T1, `README.md`; nama plan: `laporan/data/kiwi-cases.json` | Teks lengkap TP-1: [ISI MANUAL] |
| Bab III versi build & lingkungan | TERISI DARI DATA (build, AUT, oracle, browser sesi) + ISI MANUAL (OS, versi browser, emulator) | `kiwi-executions.json`, Session Notes | — |
| Bab III data uji | TERISI DARI DATA | Session Notes T5; struktur partisi Bab IV | — |
| Bab III role & jadwal | TERISI DARI DATA (role) + ISI MANUAL (jadwal per hari) | `soal.md`, `README.md` | — |
| Bab III daftar risiko | TIDAK ADA DATA | — | Tidak ada daftar risiko di repo |
| Bab III strategi oracle | TERISI DARI DATA | `soal.md` Skenario; `README.md` "Alur pelaporan bug" | — |
| Bab IV tabel partisi & titik batas | TERISI DARI DATA (dari nama test case) + ISI MANUAL (titik batas email, detail TP-1) | `laporan/data/kiwi-cases.json` (TC-EP-*) | TP-1 tidak berupa berkas di repo |
| Bab IV 5 dugaan error guessing | TERISI DARI DATA | TC-EG-01..05 | — |
| Bab IV 8 test case negatif/edge | TERISI DARI DATA | TC-NEG-01..08 | — |
| Bab IV charter exploratory | TERISI DARI DATA | Session Notes T5 | — |
| Bab IV rencana T6/T7 | TERISI DARI DATA + ISI MANUAL (matriks per browser/viewport) | TC T6/T7 di `kiwi-cases.json` | Viewport lengkap `soal.md` T6 |
| Bab IV matriks keterlacakan | TERISI DARI DATA | `laporan/data/kiwi-cases.json` (48 TC) | — |
| Bab V rekap Test Run | TERISI DARI DATA | `laporan/kiwi-snapshot.md`, `kiwi-executions.json` | 15 run, 48 eksekusi |
| Bab V Session Notes | TERISI DARI DATA | `evidence-uts/session-notes/` | Gaya kutip ringkasan saja |
| Bab V matriks cross-browser/responsive | TIDAK ADA DATA + ISI MANUAL | status per TC; PDF T6 | Isi matriks manual |
| Bab V perbandingan axe/WAVE/Lighthouse | TIDAK ADA DATA + ISI MANUAL | status per TC; PDF T7 | Sub-hasil per alat tidak di repo |
| Bab V indeks evidence | TERISI DARI DATA | Lampiran A; daftar isi folder `evidence-uts/` | — |
| Bab VI tabel seluruh bug | TERISI DARI DATA | `issues.json`, `t8-traceability.md` | 34 baris, sama dengan jumlah issue |
| Bab VI alasan severity/priority | TERISI DARI DATA | `severity-priority-matrix.md` | #39, #40: ALASAN BELUM DITULIS |
| Bab VI notulen triage | TERISI DARI DATA | `triage-notes.md` | #39, #40: TIDAK ADA NOTULEN |
| Bab VII metrik & summary | TERISI DARI DATA | `laporan/T9-test-execution-summary.md` | Angka identik T9; lihat catatan #8 di bawah |
| Bab VIII bug disingkirkan | TERISI DARI DATA | Session Notes, SBTM-debrief | Observasi yang tidak dieskalasi |
| Bab VIII batas a11y otomatis | TERISI DARI DATA (konsep) + ISI MANUAL (paragraf final) | TC-A11Y-01/02, #39/#40 | — |
| Bab VIII kekurangan & saran | TERISI DARI DATA | `kiwi-snapshot.md`, `t8-traceability.md`, `triage-notes.md` | Hanya yang didukung catatan repo |
| Bab VIII refleksi individu | ISI MANUAL | — | 4 kerangka kosong |
| Lampiran A indeks evidence | TERISI DARI DATA | daftar isi folder + `t8-traceability.md` + ukuran berkas | 51 berkas screenshots + 10 session-notes + 4 dokumen root |
| Lampiran B Session Notes daftar | TERISI DARI DATA | `evidence-uts/session-notes/` | Link saja, tidak menyalin isi |
| Lampiran lembar kontribusi & log | TERISI DARI DATA + ISI MANUAL (pemetaan login) | `kiwi-executions.json`, `kiwi-cases.json`, `issues.json` | — |
| Lampiran alat bantu | TERISI DARI DATA + ISI MANUAL (AI) | repo | — |
| Lampiran tautan repo | TERISI DARI DATA | URL repo | — |
| Lampiran F formulir role | ISI MANUAL | `soal.md` Lampiran I | — |

## 2. Daftar Placeholder `[ISI MANUAL]` (34 buah, baris di `UTS_PPL_Laporan-Lengkap.md`)

| Baris | Konteks |
|---:|---|
| 18, 19 | Kelompok, fokus (sampul) |
| 29–32 | Nama lengkap + NPM per R1–R4 |
| 39 | Lembar pengesahan |
| 41 | Pernyataan keaslian |
| 88 | Nomor fokus untuk nama berkas akhir |
| 180 | Teks lengkap Test Plan TP-1 |
| 193 | Lingkungan: OS, versi browser lain, Edge, emulator/perangkat, versi alat audit |
| 218 | Jadwal per hari selama 7 hari |
| 255 | Wakil partisi valid kuantitas 2–9 (data eksekusi tidak ada) |
| 276 | Titik batas format email dari TP-1 |
| 352, 353 | Matriks per browser dan viewport; matriks perbandingan axe/WAVE/Lighthouse (Bab IV) |
| 488 | Matriks per browser dan viewport (Bab V) |
| 498 | Matriks perbandingan axe/WAVE/Lighthouse (Bab V) |
| 870 | Paragraf batas pengujian otomatis versi final |
| 898 | Catatan kekurangan proses versi final |
| 903–906 | Refleksi R1–R4 (4 baris) |
| 1049–1052 | Pemetaan login GitHub ke anggota (4 baris) |
| 1072 | Pengungkapan alat bantu AI |
| 1088 | Tanggal penetapan role |
| 1092–1095 | NPM, nama, tanda tangan per anggota (formulir role) |

Periksa ulang dengan: `grep -n "ISI MANUAL" laporan/UTS_PPL_Laporan-Lengkap.md`.

## 3. Bug Tanpa Alasan Severity/Priority Tertulis

| ID | Keterangan |
|---|---|
| #39 | Tidak ada kalimat alasan di `severity-priority-matrix.md` / `triage-notes.md`; label `severity:major`, `priority:P2` dari GitHub |
| #40 | Tidak ada kalimat alasan di `severity-priority-matrix.md` / `triage-notes.md`; label `severity:major`, `priority:P2` dari GitHub |

## 4. Bug Tanpa Notulen Triage

| ID | Keterangan |
|---|---|
| #39 | `triage-notes.md` berhenti di #38 |
| #40 | `triage-notes.md` berhenti di #38 |

## 5. Eksekusi FAILED Kiwi Tanpa URL Issue di Komentar (15)

Sumber: `laporan/kiwi-snapshot.md` (tabel semua eksekusi FAILED, kolom "Issue tertaut = TIDAK ADA").

| TE | Run | Test case |
|---:|---:|---|
| 58 | 31 | TC-CORE-04 |
| 59 | 31 | TC-CORE-05 |
| 60 | 31 | TC-CORE-06 |
| 72 | 31 | TC-EG-01 |
| 75 | 31 | TC-EG-04 |
| 91 | 34 | TC-T6-01 |
| 93 | 36 | TC-T6-02 |
| 96 | 39 | TC-T6-03 |
| 97 | 40 | TC-T6-04 |
| 98 | 41 | TC-T6-05 |
| 99 | 42 | TC-T6-06 |
| 100 | 43 | TC-T6-07 |
| 101 | 44 | TC-T6-08 |
| 103 | 46 | TC-A11Y-03 |
| 104 | 47 | TC-A11Y-04 |

Catatan: 15 eksekusi ini FAILED dan komentarnya tidak menyebut nomor issue
maupun URL issue. Ketentuan T8 (`soal.md`) mensyaratkan tiap bug ditautkan ke
eksekusi FAIL melalui komentar berisi URL issue. Untuk TE 58/59/60/72/75 bug
terkait belum tertaut di data; untuk TE 91–104 belum ada issue yang dilaporkan
dari eksekusi tersebut (TE 103 dan 104, hasil audit axe/WAVE/Lighthouse, belum
ditautkan ke issue manapun).

## 6. Test Case Tanpa Eksekusi

TIDAK ADA — seluruh 48 test case plan 1 punya tepat satu eksekusi
(`laporan/kiwi-executions.json`, 48 baris; TC unik dieksekusi 48).

## 7. Nama Berkas Laporan Akhir

Nama wajib: `UTS_PPL_Kelompok-XX_Fokus-X.pdf`.

- Nilai **XX** (nomor kelompok) dan **X** (nomor fokus) **belum ada datanya di
  repo** — tulis manual sebelum konversi PDF. Isi keduanya di sampul, di
  Lampiran F, dan di bagian akhir dokumen.
- Fokus yang tercatat di repo adalah "Keranjang dan Checkout" (`README.md`).
- Sampul dan Lampiran F memakai `[ISI MANUAL: nomor kelompok]` dan
  `[ISI MANUAL: fokus]` — isi sebelum mengekspor PDF.

## 8. Ketentuan Format Laporan Akhir (pengingat untuk DOCX/PDF manual)

- Kertas **A4**.
- Font **11–12 pt**.
- Spasi **1,15**.
- Margin **2,5 cm**.
- Setiap tabel dan gambar diberi nomor dan keterangan (nama tabel **di atas**
  tabel, keterangan gambar **di bawah** gambar) — sudah berlaku pada Markdown.
- Setiap temuan menyebut ID bug dan nama berkas evidence — sudah berlaku.
- Jangan menjalankan `build_report.py` atau `generate_charts.py`; konversi
  DOCX/PDF dilakukan sendiri.

## 9. Inkonsistensi yang Dicatat (tidak dipilih sendiri oleh agen)

- **[SELESAI ATAS INSTRUKSI PENGGUNA] Judul Tabel 7.6 dan 7.7 di
  `laporan/T9-test-execution-summary.md` sebelumnya tertulis "dari 32 issue
  OPEN" padahal isi tabelnya menyajikan 34 issue;** kini judulnya diubah
  menjadi "dari 34 issue OPEN" (perintah penulis, sebelum commit).
- Di Bab VII laporan ini, judul Tabel 7.6/7.7 ditulis tanpa jumlah pada
  caption ("Distribusi severity/priority issue OPEN") dan baris Total
  Tabel 7.5 kini identik dengan T9 (`Total | 34 | 34 | 100,0% | #7–#40`).
- **`laporan/img/*.png` (status.png, priority-status.png, severity.png,
  defect-density.png) dibangun dari data lama Run 31 (5 PASSED, 27 FAILED,
  2 BLOCKED; 32 issue) dan belum diregenerasi** — T9 menandainya "data basi".
  Bab VII laporan ini tidak menyertakan grafik tersebut.
- **Angka defect density keseluruhan di T9 Tabel 7.2** disajikan berpasangan
  "94,1 bug per 100 TC (area) / 100,0 bug per 100 TC (48 TC)" — disalin
  apa adanya dari T9 tanpa penyesuaian.

## 10. Cek Akhir Sebelum Konversi PDF

- [ ] Semua `[ISI MANUAL]` terisi (34 lokasi, bagian 2 di atas).
- [ ] `TIDAK ADA DATA` dibaca ulang atau terisi manual setelah data ditemukan.
- [ ] Bab II dibaca ulang oleh penulis (PERLU DIBACA ULANG).
- [ ] Bab VII: angka disamakan dengan T9 terbaru (sudah identik).
- [ ] Nama berkas PDF: `UTS_PPL_Kelompok-XX_Fokus-X.pdf` dengan XX/X terisi.
- [ ] Format: A4, 11–12 pt, spasi 1,15, margin 2,5 cm.

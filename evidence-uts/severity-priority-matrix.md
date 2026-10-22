# Matriks Severity dan Priority — T8
Dokumen ini menjadi acuan final penentuan severity/priority seluruh bug CilacapTools. Disusun dari hasil eksekusi Run 31 dan triage 22 Oktober 2026.
## 1. Matriks Severity
| Severity | Definisi | Dampak / Contoh |
|---|---|---|
| Critical | Alur bisnis utama terblokir total, kehilangan data, atau risiko keamanan; tidak ada workaround. | Checkout tidak menghasilkan invoice; semua metode pembayaran salah. |
| Major | Fitur utama gagal atau hasil salah; workaround tidak wajar / berisiko. | Total baris $00.00; pencarian HTTP 500; batas stok salah. |
| Minor | Fitur terganggu, tetapi ada workaround; dampak terbatas. | Spesifikasi produk hilang; label tombol tidak ada. |
| Trivial | Kosmetik, typo, atau duplikasi tampilan. | Typo Contakt; header Total duplikat. |
## 2. Matriks Priority
| Priority | Definisi | Target |
|---|---|---|
| P1 | Blocker rilis; harus diperbaiki sebelum build boleh GO. | Hari ini / sebelum rilis. |
| P2 | Tinggi; target sprint ini, tetapi tidak memblokir seluruh rilis. | Sprint berjalan. |
| P3 | Sedang; dikerjakan setelah P2. | Sprint berikutnya. |
| P4 | Rendah; jika ada waktu. | Backlog. |
## 3. Keputusan per Issue
| Issue | Area | Severity | Priority | Alasan |
|---|---|---|---|---|
| [#7](https://github.com/SallVea/UTS-PPL/issues/7) | Checkout / Pembayaran | Critical | P1 | Pembayaran non-COD tidak dapat diselesaikan karena field dan opsi metode salah. |
| [#8](https://github.com/SallVea/UTS-PPL/issues/8) | Checkout / Pembayaran | Critical | P1 | Alur checkout berhenti tanpa invoice atau halaman konfirmasi. |
| [#9](https://github.com/SallVea/UTS-PPL/issues/9) | Beranda | Minor | P2 | Branding rusak di semua halaman, tetapi navigasi tetap berfungsi. |
| [#10](https://github.com/SallVea/UTS-PPL/issues/10) | Beranda | Trivial | P3 | Hanya kesalahan teks kosmetik. |
| [#11](https://github.com/SallVea/UTS-PPL/issues/11) | Beranda / Katalog | Major | P1 | Kategori valid hilang dan diganti label UNDEFINED. |
| [#12](https://github.com/SallVea/UTS-PPL/issues/12) | Beranda / Katalog | Major | P1 | Satu kategori tidak dapat dibuka sama sekali. |
| [#13](https://github.com/SallVea/UTS-PPL/issues/13) | Beranda | Minor | P3 | Fitur bahasa hilang, tetapi ada workaround di browser. |
| [#14](https://github.com/SallVea/UTS-PPL/issues/14) | Katalog | Minor | P3 | Data brand salah tampil, tetapi alur beli tetap berjalan. |
| [#15](https://github.com/SallVea/UTS-PPL/issues/15) | Katalog | Minor | P2 | Informasi produk penting hilang sehingga keputusan pembelian terganggu. |
| [#16](https://github.com/SallVea/UTS-PPL/issues/16) | Katalog | Minor | P3 | Fitur sekunder hilang, tidak memblokir pembelian. |
| [#17](https://github.com/SallVea/UTS-PPL/issues/17) | Katalog | Minor | P3 | Informasi badge menyesatkan, tetapi tidak menghambat alur. |
| [#18](https://github.com/SallVea/UTS-PPL/issues/18) | Login / Auth | Minor | P2 | Login berhasil, tetapi status pengguna di header salah. |
| [#19](https://github.com/SallVea/UTS-PPL/issues/19) | Beranda / Footer | Minor | P3 | Masalah kepatuhan dan kepercayaan, bukan blocker fungsional. |
| [#20](https://github.com/SallVea/UTS-PPL/issues/20) | Keranjang | Major | P1 | Kalkulasi harga per baris salah dan memengaruhi kepercayaan pada total. |
| [#21](https://github.com/SallVea/UTS-PPL/issues/21) | Keranjang | Trivial | P3 | Duplikasi header hanya kosmetik. |
| [#22](https://github.com/SallVea/UTS-PPL/issues/22) | Keranjang | Minor | P3 | Navigasi kembali ke katalog hilang, tetapi ada workaround menu. |
| [#23](https://github.com/SallVea/UTS-PPL/issues/23) | Checkout | Trivial | P3 | Label langkah tidak konsisten, hanya kosmetik. |
| [#24](https://github.com/SallVea/UTS-PPL/issues/24) | Checkout | Trivial | P3 | Typo pada judul form, tidak menghambat pengisian. |
| [#25](https://github.com/SallVea/UTS-PPL/issues/25) | Checkout | Minor | P2 | Tombol tanpa label menyulitkan pengguna, terutama screen reader. |
| [#26](https://github.com/SallVea/UTS-PPL/issues/26) | Keranjang | Major | P1 | Kalkulasi subtotal inti salah saat qty berubah. |
| [#27](https://github.com/SallVea/UTS-PPL/issues/27) | Checkout | Minor | P2 | Validasi panjang alamat tidak berjalan; data tidak wajar diterima. |
| [#28](https://github.com/SallVea/UTS-PPL/issues/28) | Keranjang | Minor | P2 | Validasi batas bawah gagal; keranjang bisa kosong tanpa konfirmasi. |
| [#29](https://github.com/SallVea/UTS-PPL/issues/29) | Keranjang | Major | P2 | Aturan stok salah: oracle 99, AUT membatasi 10 tanpa notifikasi. |
| [#30](https://github.com/SallVea/UTS-PPL/issues/30) | Pencarian | Major | P2 | Fitur pencarian rusak dan menghasilkan error server. |
| [#31](https://github.com/SallVea/UTS-PPL/issues/31) | Checkout / Pembayaran | Major | P1 | Pembayaran kartu kredit tidak dapat dilakukan karena field wajib tidak tampil. |
| [#32](https://github.com/SallVea/UTS-PPL/issues/32) | Checkout / Pembayaran | Major | P1 | Checkout gagal total dan invoice tidak terbentuk. |
| [#33](https://github.com/SallVea/UTS-PPL/issues/33) | Login | Minor | P2 | Pesan validasi tidak spesifik, tetapi login tetap dicegah. |
| [#34](https://github.com/SallVea/UTS-PPL/issues/34) | Checkout / Pembayaran | Major | P2 | Risiko duplikasi order akibat dua request. |

## 4. Catatan
- Severity ditentukan oleh dampak teknis, bukan tingkat urgensi bisnis.
- Priority ditentukan oleh kombinasi dampak, jumlah pengguna terdampak, dan posisi di alur rilis.
- Issue #7 dan #8 sebelumnya belum berlabel; hasil triage menetapkan Critical/P1.

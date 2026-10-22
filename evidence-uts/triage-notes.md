# Notulen Triage T8 — 22 Oktober 2026
**Peserta:** Atsaal (Test Lead), Gading, Ikhsan, Mema  
**Acuan:** Run 31, oracle practicesoftwaretesting.com, dan label severity/priority pada repo.
**Keputusan umum:** seluruh issue di bawah dinyatakan valid dan tetap OPEN sampai diperbaiki. Issue duplikat/terkait ditandai pada catatan, bukan dihapus. Notulen ini disusun dari hasil eksekusi dan bukti yang tersedia; mohon dicek ulang saat meeting triage resmi.
## Ringkasan
| Keputusan | Jumlah |
|---|---:|
| Valid, tetap OPEN | 28 |
| Duplikat dihapus | 0 |
| Ditutup karena bukan bug | 0 |

## Catatan per Issue
<a id="issue-7"></a>

### Issue #7 — Semua metode pembayaran memakai field Account Name/Number dan opsi Errror 304
**Final:** Critical / P1 · **Area:** Checkout / Pembayaran · **TC:** TC-EXP-01 · **Eksekusi:** TE-85 ([Run 31](https://localhost/run/31/#c85)) · **Issue:** [#7](https://github.com/SallVea/UTS-PPL/issues/7)

Ditemukan pada sesi EXP-01. Terkait #31, tetapi #31 hanya field kartu kredit; issue ini mencakup semua metode. Tindak lanjut: perbaiki pemetaan field per metode dan hapus opsi Errror 304.

**Alasan severity/priority:** Pembayaran non-COD tidak dapat diselesaikan karena field dan opsi metode salah.

<a id="issue-8"></a>

### Issue #8 — Setelah Confirm payment tidak ada konfirmasi order dan nomor invoice
**Final:** Critical / P1 · **Area:** Checkout / Pembayaran · **TC:** TC-CORE-07 · **Eksekusi:** TE-61 ([Run 31](https://localhost/run/31/#c61)) · **Issue:** [#8](https://github.com/SallVea/UTS-PPL/issues/8)

Gejala utama dari kegagalan POST /invoices. Terkait #32 sebagai akar teknis; tetap dicatat sebagai dampak pengguna. Tindak lanjut: verifikasi ulang setelah #32 diperbaiki.

**Alasan severity/priority:** Alur checkout berhenti tanpa invoice atau halaman konfirmasi.

<a id="issue-9"></a>

### Issue #9 — Logo header tidak tampil (broken image)
**Final:** Minor / P2 · **Area:** Beranda · **TC:** TC-CORE-01 · **Eksekusi:** TE-55 ([Run 31](https://localhost/run/31/#c55)) · **Issue:** [#9](https://github.com/SallVea/UTS-PPL/issues/9)

Logo broken.png 404 dan muncul di seluruh halaman. Tidak menghalangi alur, sehingga Minor/P2. Tindak lanjut: perbaiki aset logo.

**Alasan severity/priority:** Branding rusak di semua halaman, tetapi navigasi tetap berfungsi.

<a id="issue-10"></a>

### Issue #10 — Typo menu Contact tertulis Contakt
**Final:** Trivial / P3 · **Area:** Beranda · **TC:** TC-CORE-01 · **Eksekusi:** TE-55 ([Run 31](https://localhost/run/31/#c55)) · **Issue:** [#10](https://github.com/SallVea/UTS-PPL/issues/10)

Typo terlihat pada header. Tidak memengaruhi fungsi, sehingga Trivial/P3. Tindak lanjut: perbaiki label.

**Alasan severity/priority:** Hanya kesalahan teks kosmetik.

<a id="issue-11"></a>

### Issue #11 — Item dropdown UNDEFINED menggantikan Other
**Final:** Major / P1 · **Area:** Beranda / Katalog · **TC:** TC-CORE-01 · **Eksekusi:** TE-55 ([Run 31](https://localhost/run/31/#c55)) · **Issue:** [#11](https://github.com/SallVea/UTS-PPL/issues/11)

Navigasi kategori berubah dan membingungkan pengguna. Terkait #12 tetapi root cause berbeda (label vs route 404). Tindak lanjut: perbaiki data/label kategori.

**Alasan severity/priority:** Kategori valid hilang dan diganti label UNDEFINED.

<a id="issue-12"></a>

### Issue #12 — Item Chainsaws menghasilkan 404 Page Not Found
**Final:** Major / P1 · **Area:** Beranda / Katalog · **TC:** TC-CORE-01 · **Eksekusi:** TE-55 ([Run 31](https://localhost/run/31/#c55)) · **Issue:** [#12](https://github.com/SallVea/UTS-PPL/issues/12)

Klik Chainsaws mengarah ke route yang tidak ada. Bukan duplikat #11; keduanya perlu diperbaiki. Tindak lanjut: perbaiki route kategori.

**Alasan severity/priority:** Satu kategori tidak dapat dibuka sama sekali.

<a id="issue-13"></a>

### Issue #13 — Pemilih bahasa EN tidak ada di header
**Final:** Minor / P3 · **Area:** Beranda · **TC:** TC-CORE-01 · **Eksekusi:** TE-55 ([Run 31](https://localhost/run/31/#c55)) · **Issue:** [#13](https://github.com/SallVea/UTS-PPL/issues/13)

Tidak memblokir alur utama. Tindak lanjut: tambahkan pemilih bahasa atau dokumentasikan sebagai fitur nonaktif.

**Alasan severity/priority:** Fitur bahasa hilang, tetapi ada workaround di browser.

<a id="issue-14"></a>

### Issue #14 — Badge brand tampil Brand name 1
**Final:** Minor / P3 · **Area:** Katalog · **TC:** TC-CORE-02 · **Eksekusi:** TE-56 ([Run 31](https://localhost/run/31/#c56)) · **Issue:** [#14](https://github.com/SallVea/UTS-PPL/issues/14)

Informasi produk tidak akurat dan mengurangi kepercayaan. Tindak lanjut: perbaiki relasi brand.

**Alasan severity/priority:** Data brand salah tampil, tetapi alur beli tetap berjalan.

<a id="issue-15"></a>

### Issue #15 — Bagian Specifications tidak tampil di detail produk
**Final:** Minor / P2 · **Area:** Katalog · **TC:** TC-CORE-02 · **Eksekusi:** TE-56 ([Run 31](https://localhost/run/31/#c56)) · **Issue:** [#15](https://github.com/SallVea/UTS-PPL/issues/15)

Deskripsi masih tersedia sebagai workaround. Tindak lanjut: tampilkan spesifikasi dari data produk.

**Alasan severity/priority:** Informasi produk penting hilang sehingga keputusan pembelian terganggu.

<a id="issue-16"></a>

### Issue #16 — Tombol Compare tidak ada di katalog dan detail produk
**Final:** Minor / P3 · **Area:** Katalog · **TC:** TC-CORE-02 · **Eksekusi:** TE-56 ([Run 31](https://localhost/run/31/#c56)) · **Issue:** [#16](https://github.com/SallVea/UTS-PPL/issues/16)

Tindak lanjut: tambahkan tombol atau hapus dari ekspektasi oracle jika fitur memang tidak disediakan.

**Alasan severity/priority:** Fitur sekunder hilang, tidak memblokir pembelian.

<a id="issue-17"></a>

### Issue #17 — Badge ECO tampil padahal tidak ada di oracle
**Final:** Minor / P3 · **Area:** Katalog · **TC:** TC-CORE-02 · **Eksekusi:** TE-56 ([Run 31](https://localhost/run/31/#c56)) · **Issue:** [#17](https://github.com/SallVea/UTS-PPL/issues/17)

Tindak lanjut: hapus badge atau sesuaikan dengan data produk.

**Alasan severity/priority:** Informasi badge menyesatkan, tetapi tidak menghambat alur.

<a id="issue-18"></a>

### Issue #18 — Header menampilkan User Data not found setelah login
**Final:** Minor / P2 · **Area:** Login / Auth · **TC:** TC-CORE-03 · **Eksekusi:** TE-57 ([Run 31](https://localhost/run/31/#c57)) · **Issue:** [#18](https://github.com/SallVea/UTS-PPL/issues/18)

Membingungkan pengguna dan mengurangi kepercayaan pada sesi. Tindak lanjut: perbaiki pengambilan data user setelah login.

**Alasan severity/priority:** Login berhasil, tetapi status pengguna di header salah.

<a id="issue-19"></a>

### Issue #19 — Link Privacy Policy tidak ada di footer
**Final:** Minor / P3 · **Area:** Beranda / Footer · **TC:** TC-CORE-03 · **Eksekusi:** TE-57 ([Run 31](https://localhost/run/31/#c57)) · **Issue:** [#19](https://github.com/SallVea/UTS-PPL/issues/19)

Tindak lanjut: tambahkan link ke halaman kebijakan privasi.

**Alasan severity/priority:** Masalah kepatuhan dan kepercayaan, bukan blocker fungsional.

<a id="issue-20"></a>

### Issue #20 — Total baris item menampilkan $00.00
**Final:** Major / P1 · **Area:** Keranjang · **TC:** TC-EG-02 · **Eksekusi:** TE-73 ([Run 31](https://localhost/run/31/#c73)) · **Issue:** [#20](https://github.com/SallVea/UTS-PPL/issues/20)

Terkait #26, tetapi #20 fokus total baris sedangkan #26 fokus subtotal setelah perubahan qty. Tindak lanjut: perbaiki kalkulasi baris.

**Alasan severity/priority:** Kalkulasi harga per baris salah dan memengaruhi kepercayaan pada total.

<a id="issue-21"></a>

### Issue #21 — Header kolom Total muncul dua kali
**Final:** Trivial / P3 · **Area:** Keranjang · **TC:** TC-EG-02 · **Eksekusi:** TE-73 ([Run 31](https://localhost/run/31/#c73)) · **Issue:** [#21](https://github.com/SallVea/UTS-PPL/issues/21)

Tindak lanjut: hapus header duplikat.

**Alasan severity/priority:** Duplikasi header hanya kosmetik.

<a id="issue-22"></a>

### Issue #22 — Tombol Continue Shopping tidak ada di keranjang
**Final:** Minor / P3 · **Area:** Keranjang · **TC:** TC-EG-02 · **Eksekusi:** TE-73 ([Run 31](https://localhost/run/31/#c73)) · **Issue:** [#22](https://github.com/SallVea/UTS-PPL/issues/22)

Tindak lanjut: tambahkan tombol atau link kembali.

**Alasan severity/priority:** Navigasi kembali ke katalog hilang, tetapi ada workaround menu.

<a id="issue-23"></a>

### Issue #23 — Label langkah 3 tertulis ADDRESS, bukan BILLING ADDRESS
**Final:** Trivial / P3 · **Area:** Checkout · **TC:** TC-EG-02 · **Eksekusi:** TE-73 ([Run 31](https://localhost/run/31/#c73)) · **Issue:** [#23](https://github.com/SallVea/UTS-PPL/issues/23)

Tindak lanjut: perbaiki teks label.

**Alasan severity/priority:** Label langkah tidak konsisten, hanya kosmetik.

<a id="issue-24"></a>

### Issue #24 — Judul form billing tertulis Blliling Adress
**Final:** Trivial / P3 · **Area:** Checkout · **TC:** TC-CORE-07 · **Eksekusi:** TE-61 ([Run 31](https://localhost/run/31/#c61)) · **Issue:** [#24](https://github.com/SallVea/UTS-PPL/issues/24)

Ditemukan saat TC-NEG-01; eksekusi FAIL terkait adalah TC-CORE-07. Tindak lanjut: perbaiki teks.

**Alasan severity/priority:** Typo pada judul form, tidak menghambat pengisian.

<a id="issue-25"></a>

### Issue #25 — Tombol lanjut form billing tidak memiliki label teks
**Final:** Minor / P2 · **Area:** Checkout · **TC:** TC-CORE-07 · **Eksekusi:** TE-61 ([Run 31](https://localhost/run/31/#c61)) · **Issue:** [#25](https://github.com/SallVea/UTS-PPL/issues/25)

Ditemukan saat TC-NEG-01; eksekusi FAIL terkait adalah TC-CORE-07. Tindak lanjut: tambahkan label aksesibel.

**Alasan severity/priority:** Tombol tanpa label menyulitkan pengguna, terutama screen reader.

<a id="issue-26"></a>

### Issue #26 — Subtotal tetap 0 saat kuantitas diubah
**Final:** Major / P1 · **Area:** Keranjang · **TC:** TC-EP-01 · **Eksekusi:** TE-62 ([Run 31](https://localhost/run/31/#c62)) · **Issue:** [#26](https://github.com/SallVea/UTS-PPL/issues/26)

Terkait #20; keduanya dapat diperbaiki bersama. Tindak lanjut: sinkronkan state subtotal.

**Alasan severity/priority:** Kalkulasi subtotal inti salah saat qty berubah.

<a id="issue-27"></a>

### Issue #27 — Alamat 320 karakter lolos validasi dan lanjut ke Payment
**Final:** Minor / P2 · **Area:** Checkout · **TC:** TC-NEG-05 · **Eksekusi:** TE-81 ([Run 31](https://localhost/run/31/#c81)) · **Issue:** [#27](https://github.com/SallVea/UTS-PPL/issues/27)

Tidak memblokir, tetapi berpotensi merusak layout dan data. Tindak lanjut: tetapkan batas panjang dan pesan validasi.

**Alasan severity/priority:** Validasi panjang alamat tidak berjalan; data tidak wajar diterima.

<a id="issue-28"></a>

### Issue #28 — Quantity 0 diterima dan mengosongkan keranjang
**Final:** Minor / P2 · **Area:** Keranjang · **TC:** TC-EP-02 · **Eksekusi:** TE-63 ([Run 31](https://localhost/run/31/#c63)) · **Issue:** [#28](https://github.com/SallVea/UTS-PPL/issues/28)

Ada workaround refresh, tetapi perilaku tidak sesuai oracle. Tindak lanjut: tolak 0 dan kembalikan ke 1.

**Alasan severity/priority:** Validasi batas bawah gagal; keranjang bisa kosong tanpa konfirmasi.

<a id="issue-29"></a>

### Issue #29 — Quantity di atas 10 dipotong ke 10 tanpa peringatan
**Final:** Major / P2 · **Area:** Keranjang · **TC:** TC-EP-04 · **Eksekusi:** TE-65 ([Run 31](https://localhost/run/31/#c65)) · **Issue:** [#29](https://github.com/SallVea/UTS-PPL/issues/29)

Bukan duplikat #28; #28 tentang batas bawah, #29 tentang batas atas. Tindak lanjut: ubah batas ke 99 dan tampilkan toast.

**Alasan severity/priority:** Aturan stok salah: oracle 99, AUT membatasi 10 tanpa notifikasi.

<a id="issue-30"></a>

### Issue #30 — Karakter khusus memicu HTTP 500 pada pencarian
**Final:** Major / P2 · **Area:** Pencarian · **TC:** TC-NEG-04 · **Eksekusi:** TE-80 ([Run 31](https://localhost/run/31/#c80)) · **Issue:** [#30](https://github.com/SallVea/UTS-PPL/issues/30)

Perlu log console/network untuk analisis root cause. Tindak lanjut: sanitasi input dan tangani error.

**Alasan severity/priority:** Fitur pencarian rusak dan menghasilkan error server.

<a id="issue-31"></a>

### Issue #31 — Credit Card menampilkan Account Name/Number, field kartu tidak muncul
**Final:** Major / P1 · **Area:** Checkout / Pembayaran · **TC:** TC-EP-08 · **Eksekusi:** TE-69 ([Run 31](https://localhost/run/31/#c69)) · **Issue:** [#31](https://github.com/SallVea/UTS-PPL/issues/31)

Terkait #7; #7 mencakup semua metode, #31 spesifik kartu kredit. Tindak lanjut: render field per metode.

**Alasan severity/priority:** Pembayaran kartu kredit tidak dapat dilakukan karena field wajib tidak tampil.

<a id="issue-32"></a>

### Issue #32 — POST /invoices mengembalikan 500, invoice tidak terbentuk
**Final:** Major / P1 · **Area:** Checkout / Pembayaran · **TC:** TC-CORE-07 · **Eksekusi:** TE-61 ([Run 31](https://localhost/run/31/#c61)) · **Issue:** [#32](https://github.com/SallVea/UTS-PPL/issues/32)

Akar teknis dari #8. Tindak lanjut: perbaiki endpoint dan tambahkan error handling.

**Alasan severity/priority:** Checkout gagal total dan invoice tidak terbentuk.

<a id="issue-33"></a>

### Issue #33 — Validasi format email tidak sesuai saat input invalid
**Final:** Minor / P2 · **Area:** Login · **TC:** TC-EP-06 · **Eksekusi:** TE-67 ([Run 31](https://localhost/run/31/#c67)) · **Issue:** [#33](https://github.com/SallVea/UTS-PPL/issues/33)

Terkait TC-EP-07; eksekusi TE-68 juga FAIL. Tindak lanjut: tampilkan pesan format email yang jelas.

**Alasan severity/priority:** Pesan validasi tidak spesifik, tetapi login tetap dicegah.

<a id="issue-34"></a>

### Issue #34 — Klik ganda cepat Confirm mengirim 2 request pembuatan pesanan
**Final:** Major / P2 · **Area:** Checkout / Pembayaran · **TC:** TC-NEG-07 · **Eksekusi:** TE-83 ([Run 31](https://localhost/run/31/#c83)) · **Issue:** [#34](https://github.com/SallVea/UTS-PPL/issues/34)

Perlu screen recording urutan interaksi; saat ini bukti berupa dua screenshot, yaitu with-bugs dengan 2 request 500 dan oracle dengan 2 invoice. Tindak lanjut: nonaktifkan tombol setelah klik pertama.

**Alasan severity/priority:** Risiko duplikasi order akibat dua request.


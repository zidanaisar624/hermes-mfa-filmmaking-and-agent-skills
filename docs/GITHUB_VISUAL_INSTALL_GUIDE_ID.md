# Paket Visual Hermes MFA — Cara Memasang

## Apa yang disediakan
Paket ini menambahkan **16 visual baru + 1 template SVG editable** untuk `hermes-mfa-filmmaking-and-agent-skills`. Identitas visual: studio sinematik penuh warna (midnight blue, violet, cyan, coral, amber), **bukan** Business Sage.

Pemetaan gambar mengikuti dokumen yang diberikan: 47 skills; skill utama MFA Filmmaking dan Auto-Curiousity; tahapan produksi; arsitektur ArtCraft + Blender (rancangan); mode single/multi-agent; dan format deliverable. Integrasi memerlukan konfigurasi terpisah.

## Pilih salah satu metode

### Metode A — Tambahkan saja (paling aman)
1. Ekstrak `HERMES_MFA_Visual_Pack_ADD_ONLY.zip`.
2. Dari hasil ekstrak, salin hanya folder `assets/cinematic-studio/` ke repository GitHub lokal, tanpa mengubah file lama di `assets/`.
3. Buka `docs/README_PATCHED_PREVIEW.md` sebagai **contoh** integrasi visual. Pindahkan blok gambar pilihan ke README sesuai bab yang dijelaskan. Jangan langsung menimpa README yang mungkin sudah berkembang di GitHub.
4. Periksa diff, commit, dan push normal (jangan `--force`).

### Metode B — Full snapshot siap ditinjau
1. Ekstrak `HERMES_MFA_Repo_Visual_Expanded_READY.zip` ke folder baru.
2. Isi ZIP dibuat dari **arsip snapshot lokal yang diberikan** (`HERMES_Updated_Repository.zip`), jadi repo GitHub publik terkini mungkin sudah memiliki perubahan lain.
3. Bandingkan dahulu perbedaan antara README lokal dan README di GitHub. Gabungkan yang relevan; jangan mengunggah seluruh snapshot secara buta bila ada pembaruan terbaru.
4. Semua file skill dan keempat gambar existing di `assets/` dari snapshot lokal tetap byte-identical. README ditambah penempatan gambar baru.

## GitHub social preview
Gunakan `assets/cinematic-studio/13_github_social_preview_1280x640.jpg` dengan ukuran 1280×640. Di halaman repository buka **Settings → Social preview → Edit** dan unggah JPG tersebut. Mengunggahnya ke folder `assets` saja **tidak otomatis** mengubah social preview GitHub.

## Susunan visual
- Awal: `01` Creative Universe + `02` pillars + `03` capability atlas.
- Bagian S2 MFA: `04` 5-phase pipeline, `06` story, `07` cinematography, `08` postproduction.
- Section Auto-Curiousity: `05` R&D loop.
- Section ArtCraft + Blender: `09` toolchain (gambaran dokumentasi, bukan koneksi aktif).
- Section Work Modes: `10` single vs multi-agent.
- Hasil: `11` delivery formats.
- Akhir: `12` end card.
- Branding opsional: `14` icon. Bonus illustrations: `15`, `16`.

## Sumber dan keterbatasan
- Konten kemampuan dipetakan dari README serta file skill yang ada di ZIP yang disediakan. Website repo live tidak dapat diaudit langsung pada sesi ini.
- Foto/ilustrasi referensi yang kamu kirim **tidak ditempel dan tidak diberi nama bot**. Gambar baru memakai ilustrasi orisinal dan visualisasi kemampuan.
- Keempat gambar yang sudah ada tidak diganti. Bandingkan SHA-256 di `docs/PRESERVATION_AUDIT.json` untuk verifikasi.

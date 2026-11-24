---
name: lemo-opuscar
description: Katalog 15 kategori dan 99 gaya film pendek & video explainer berbasis kode (Lemo-Opuscar by Lemomo / LemoLab) terpasang otomatis: jelaskan kategori & rekomendasikan gaya dulu, kunci pilihan pengguna, lalu rancang film berbasis kode selaras Concepting First.
license: MIT
metadata:
  upstream: https://github.com/lemomo-ai/lemo-opuscar
  upstream_commit: f9e204293930952b61ba921cd8944d05f121beee
  upstream_license: MIT (code); CC-BY-NC-4.0 with film-making permission (docs); CC-BY-4.0 (demo films/pictures)
  default_installed: true
---

# Gaya Film Pendek Berbasis Kode (`Lemo-Opuscar` — 15 Kategori, 99 Gaya · Aktif Otomatis)

Di repositori **`hermes-mfa-filmmaking-and-agent-skills`**, integrasi **`lemo-opuscar`** terpasang dan aktif **secara otomatis (*default-ON*, tanpa perlu flag opt-in)** untuk seluruh agen yang terhubung (**Hermes Agent**, **OpenClaw**, **Claude Code**, **ChatGPT / Codex**, **Cursor**, dan **Google Antigravity**).

Skill ini mendampingi `filmmaking-videography-photography-s2` (*Concepting First*), `auto-curiousity-for-film-making`, dan `cli-anything-filmmaking-bridge` saat kreator manusia ingin membuat film pendek, dokumenter data, trailer produk, animasi tipografi, atau video explainer berbasis kode dengan bahasa visual sinematik yang terkurasi—tanpa mengubah `config.yaml`, `provider`, `model`, atau `SOUL.md` pengguna.

## 0. Aturan Wajib Sebelum Eksekusi: Jelaskan Kategori & Kunci 1 Gaya Dulu!

Setiap kali pengguna meminta pembuatan film pendek/video explainer berbasis kode atau memanggil `lemo-opuscar` tanpa menyebutkan 1 `slug` gaya spesifik, **JANGAN langsung menulis kode render**. Lakukan 3 langkah ini terlebih dahulu:

1. **Perkenalkan ringkas 15 kategori estetika yang tersedia** (dokumenter/edit, lukisan, sketsa papan, kerajinan tradisional, cetak/poster, grafik & tipografi, diagram garis, kartun, gim, pita seluloid, antarmuka layar, cahaya & garis, miniatur 3D, instrumen bukti, serta data & peta).
2. **Rekomendasikan 3–5 gaya (`slug`) paling relevan** dengan cerita, durasi, dan suasana emosi proyek pengguna.
3. **Tunggu persetujuan 1 gaya dari pengguna**, lalu muat hanya panduan untuk **1 gaya terpilih tersebut** (*jangan* memuat 99 gaya sekaligus ke dalam konteks agar tetap hemat token).

## 1. Cara Mengambil Referensi 1 Gaya Secara Hemat Token (0 Bloat di `skills/`)

Repositori upstream `lemomo-ai/lemo-opuscar` berukuran ~133 MB karena berisi poster & video demo, sehingga **tidak** disalin mentah ke dalam folder `skills/`. Ambil hanya teks panduan (`STYLE.md` & `style.json`) untuk 1 gaya yang dipilih pengguna di luar folder `skills/`:

- **Jika `msshi` CLI tersedia di perangkat:**
  ```text
  msshi integrations source --home HERMES_ROOT --name lemo-opuscar --fetch
  msshi integrations source --home HERMES_ROOT --name lemo-opuscar --query "isometric"
  msshi integrations source --home HERMES_ROOT --name lemo-opuscar --skill blueprint
  ```
- **Jika memakai `hermes-mfa-filmmaking-and-agent-skills` secara mandiri (tanpa `msshi`):**
  - Baca metadata gaya langsung pada pin komit terverifikasi `f9e204293930952b61ba921cd8944d05f121beee` (`styles/<slug>/STYLE.md` dan `styles/<slug>/style.json` di `https://github.com/lemomo-ai/lemo-opuscar`), atau simpan *sparse checkout* ringan di luar direktori `skills/` (mis. `curiosity_ledger/external_refs/lemo-opuscar/`).

## 2. Peta Lengkap 15 Kategori & 99 Gaya Sinematik

1. **Edit & Documentary (8)**: `caption-news`, `newsreel`, `countdown`, `city-symphony`, `visual-investigation`, `kino-montage`, `telestrator`, `news-package`.
2. **Painting & Illustration (5)**: `crayon-book`, `watercolor`, `impasto`, `urban-sketch`, `colored-pencil`.
3. **Sketch & Board (7)**: `one-line`, `whiteboard`, `chalkboard`, `sketchnote`, `stick-explainer`, `ipad-sketch`, `marker-paper`.
4. **Traditional Crafts (7)**: `ink-wash`, `shadow-puppet`, `ukiyoe`, `papercut-red`, `paper-lantern`, `stained-glass`, `gilded-illumination`.
5. **Print & Printmaking (8)**: `risograph`, `halftone-dossier`, `woodcut`, `engraving`, `silkscreen-poster`, `printed-long-take`, `pop-art`, `vintage-collage`.
6. **Graphic & Type (8)**: `swiss-motion`, `spy-titles`, `art-deco`, `pictogram-motion`, `bauhaus-shapes`, `flat-space-explainer`, `text-flash-cuts`, `silhouette-rhythm`.
7. **Line Diagrams (8)**: `blueprint`, `iso-infographic`, `teardown`, `hardcore-info`, `precise-mechanism`, `instruction-manual`, `pen-plotter`, `assembly-line-diagram`.
8. **Cartoons (6)**: `rubber-hose`, `cel-anime-80s`, `scifi-toon`, `midcentury-toon`, `comic-history`, `manga-panels`.
9. **Games (4)**: `pixel-rpg`, `hd-2d`, `microgame`, `game-show`.
10. **Film & Tape (5)**: `ascii-crt`, `silent-film`, `backrooms`, `scratch-film`, `double-exposure`.
11. **Screens & Interfaces (6)**: `dark-keynote`, `living-screencast`, `hologram-hud`, `desktop-flythrough`, `spreadsheet`, `one-bit-dither`.
12. **Light & Lines (5)**: `circuit-board`, `firefly-pointillism`, `flow-field`, `oscilloscope-math`, `neon-tubes`.
13. **3D & Miniature (8)**: `brick-toy`, `paper-popup`, `tilt-shift`, `lowpoly-island`, `glass-product`, `memphis-diorama`, `isometric-picture-book`, `crayon-world`.
14. **Instruments & Evidence (8)**: `satellite-briefing`, `briefing-board`, `lidar-survey`, `microscope`, `archive-lighttable`, `security-xray`, `dark-documentary`, `thermal-camera`.
15. **Data & Maps (6)**: `dataviz`, `white-model`, `data-physical`, `transit-map`, `map-explainer`, `pip-simulation`.

## 3. Sinergi dengan Advisor S1–S2 Filmmaking (*Human-in-the-Loop*)

1. **Concepting First**: Susun logline, *beat sheet* / *Two-Column AV Script*, rasio aspek (`16:9` sinema/YouTube atau `9:16` vertikal), palet warna, dan ritme *cutting* sesuai prinsip Walter Murch di `filmmaking-videography-photography-s2`.
2. **Kunci 1 Gaya & Uji Segmen Pendek**: Terapkan panduan dari 1 gaya `lemo-opuscar` pada draf 3–5 detik pertama terlebih dahulu untuk ditinjau kreator manusia sebelum me-render durasi penuh.
3. **Finishing Audio & Ekspor Bersih**: Gunakan standar loudness `-14.0 LUFS` (`-1.0 dBTP`) untuk platform digital atau `-24.0 LKFS` untuk broadcast via `ffmpeg` di `cli-anything-filmmaking-bridge`.

## 4. Atribusi & Batas Lisensi Wajib (`LICENSE.upstream`)

- Kredit sumber: **Lemo-Opuscar by Lemomo (LemoLab)** (`https://github.com/lemomo-ai/lemo-opuscar`), beserta kontributor eksternal **Memphis Diorama by EianLu** dan **Crayon World 3D by 2nd1st**.
- Lisensi upstream multi-lapis: **MIT** untuk kode; **CC BY-NC 4.0** (dengan izin tertulis tambahan bebas royalti untuk membaca, mengikuti, dan mengadaptasi panduan guna memproduksi film pribadi maupun komersial/klien) untuk dokumentasi Markdown & prompt; **CC BY 4.0** untuk film/gambar demo.
- **Film hasil karya Anda sepenuhnya milik Anda (termasuk film komersial/klien)**, namun **jangan** menjual ulang berkas dokumentasi upstream secara komersial tanpa lisensi komersial Lemomo, dan **jangan** memakai karakter/merek dagang pihak ketiga yang dikecualikan di `LICENSE.upstream` (seperti karakter Clawd milik Anthropic, antarmuka merek pihak ketiga, atau 6 trek narasi TTS demo). Wrapper ini 100% ditulis orisinal (0 byte dokumen upstream disalin ke repositori ini).

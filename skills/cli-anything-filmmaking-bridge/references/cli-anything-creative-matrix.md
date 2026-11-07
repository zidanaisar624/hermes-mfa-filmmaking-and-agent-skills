# CLI-Anything & Native CLI Creative Execution Matrix (Zero-MCP Token Reference)

Use this reference from `cli-anything-filmmaking-bridge`, `filmmaking-videography-photography-s2`, and `auto-curiousity-for-film-making` to execute videography, photography, 3D, and audio tasks deterministically via CLI without MCP token overhead.

## 1. Installing CLI-Anything Hub & Scoped Creative Harnesses

```bash
# Install CLI-Hub package manager
python -m pip install cli-anything-hub

# Inspect creative workflow matrices before installing
cli-hub matrix list
cli-hub matrix preflight video-creation --json
cli-hub matrix preflight image-design --json

# Install only the specific harness needed for the creator's project
cli-hub install blender
cli-hub install kdenlive
cli-hub install gimp
cli-hub install inkscape
cli-hub install audacity
cli-hub install videocaptioner
```

For Hermes Agent users who also want Hermes to generate brand-new CLI harnesses from software source repos:
```bash
git clone https://github.com/HKUDS/CLI-Anything.git
# Windows PowerShell:
& .\CLI-Anything\hermes-skill\scripts\install.ps1
# Linux / macOS / WSL:
./CLI-Anything/hermes-skill/scripts/install.sh
```

---

## 2. Deterministic Zero-MCP Command Patterns by Department

### A. Optical, Exposure & Loudness Advisory (`hmfa` / `cli-anything-filmmaking`)
```bash
# Calculate exact 180-deg shutter, hyperfocal distance, DoF limits, IRE targets & LUFS targets
hmfa --json optics --focal-mm 35 --f-stop 2.0 --fps 24 --distance-m 2.2 --platform youtube --lighting natural_drama
```

### B. 3D Camera Previz & Lighting Simulation (`cli-anything-blender` / `blender`)
```bash
# Using CLI-Anything Blender harness with JSON output
cli-anything-blender --json --help

# Direct headless Blender fallback (1-frame lighting & lens check in sandbox)
blender --background sandbox_previz.blend --render-output ./sandbox_frame_#### --render-frame 1
```

### C. Photography, RAW Development & High-CTR Thumbnails
```bash
# Inspect optical EXIF & ICC color profile
exiftool -json -FocalLength -FNumber -ExposureTime -ISO -ICC_Profile:ColorSpaceData input.ARW

# Headless RAW development with XMP style/LUT via darktable-cli
darktable-cli input.ARW look_recipe.xmp output_16bit.tif --core --conf plugins/imageio/format/tiff/bpp=16

# Raster compositing & thumbnail assembly via CLI-Anything GIMP/Krita
cli-anything-gimp --json --help
cli-anything-krita --json --help
```

### D. Video Editing, Captions, Color LUT & Quality Doctor (`kdenlive` / `shotcut` / `ffmpeg`)
```bash
# Probe exact stream resolution, FPS, color space, and duration
ffprobe -v quiet -print_format json -show_format -show_streams input.mp4

# Apply 3D LUT (.cube) + gentle highlight roll-off + burn styled ASS captions
ffmpeg -y -i rough_cut.mp4 -vf "lut3d=file='kodak_2383_warm.cube',subtitles='captions.ass'" \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a copy graded_preview.mp4

# Detect black frames, frozen frames, or silence gaps before human review
ffmpeg -i graded_preview.mp4 -vf "blackdetect=d=0.1:pix_th=0.05,freezedetect=n=0.003:d=1.5" \
  -af "silencedetect=n=-45dB:d=1.0" -f null -
```

### E. Psychoacoustic Audio Mixing & `-14 LUFS` / `-24 LKFS` Mastering (`audacity` / `ffmpeg`)
```bash
# Measure integrated loudness (I), Loudness Range (LRA), and True Peak (TP)
ffmpeg -i mix_candidate.wav -af ebur128=peak=true -f null -

# Two-pass or precision EBU R128 loudness normalization for YouTube/Shorts (-14 LUFS, -1.0 dBTP)
ffmpeg -y -i mix_candidate.wav -af "highpass=f=80,loudnorm=I=-14:TP=-1.0:LRA=11:print_format=json" \
  -ar 48000 mastered_web.wav
```

### F. Direct Local Suite CLI Execution (e.g., ArtCraft `*-cli` Without MCP!)
If `hmfa preflight` detects a local CLI suite (such as `filmcraft-cli.exe`, `lightcraft-cli.exe`, `photocraft-cli.exe`, `soundcraft-cli.exe`, `craft-anything-cli.exe` on any drive), invoke the `*-cli` executable directly via shell with `--help` discovery first—consuming **zero MCP schema tokens**!

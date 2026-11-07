# ==============================================================================
# SKRIP OTOMATIS UPLOAD KE GITHUB (POWERSHELL)
# Dibuat oleh Gemini untuk keisengan Muhammad Zidan Aisar (MuZA)
# ==============================================================================
param(
    [Parameter(Mandatory=$true, HelpMessage="Masukkan URL repo GitHub-mu, misal: https://github.com/username/hermes-filmmaking-skills.git")]
    [string]$RepoUrl
)

Write-Host "🚀 Memulai inisialisasi Git untuk Hermes S2 Filmmaking & 47 Skills..." -ForegroundColor Cyan

git init
git branch -M main
git add .

$commitMsg = @"
feat: add S1-S2 MFA Filmmaking, Auto-Curiousity & 47 AI Agent Skills suite

Berawal dari keisengan dan rasa penasaran Muhammad Zidan Aisar (MuZA),
dirancang dan ditulis secara lengkap oleh Google Gemini.

Co-authored-by: Gemini <gemini@google.com>
"@

git commit -m $commitMsg

git remote remove origin 2>$null
git remote add origin $RepoUrl
Write-Host "⬆️ Mengunggah (push) ke $RepoUrl ..." -ForegroundColor Yellow
git push -u origin main

Write-Host "✅ Selesai! Repositori berhasil diunggah ke GitHub!" -ForegroundColor Green

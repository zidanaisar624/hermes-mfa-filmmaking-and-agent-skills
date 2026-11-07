# ==============================================================================
# SKRIP OTOMATIS UPLOAD / UPDATE KE GITHUB (POWERSHELL - ASCII SAFE)
# Mendukung inisialisasi baru maupun push update rutin ke repo yang sudah ada!
# ==============================================================================
param(
    [Parameter(Mandatory = $false)]
    [string]$RepoUrl = "https://github.com/zidanaisar624/hermes-mfa-filmmaking-and-agent-skills.git",
    [Parameter(Mandatory = $false)]
    [string]$Message = "feat(v2.0): add CLI-Anything zero-MCP bridge, universal multi-agent auto-discovery, Eternal-Student trend forecasting, cross-skill synergy & terminal self-updater"
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "[*] Preparing upload/update to GitHub ($RepoUrl)..." -ForegroundColor Cyan

if (-not (Test-Path ".git")) {
    git init
    git branch -M main
}

$existingOrigin = git remote get-url origin 2>$null
if (-not $existingOrigin) {
    git remote add origin $RepoUrl
} elseif ($existingOrigin -ne $RepoUrl) {
    git remote set-url origin $RepoUrl
}

git add -A
$status = git status --porcelain
if (-not $status) {
    Write-Host "[i] No file changes to commit." -ForegroundColor Yellow
    exit 0
}

git commit -m $Message
Write-Host "[*] Pushing to $RepoUrl ..." -ForegroundColor Yellow
git push -u origin main

Write-Host "[OK] Done! Repository updated on GitHub and ready for users via 'hmfa update'!" -ForegroundColor Green

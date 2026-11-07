# ==============================================================================
# TERMINAL AUTO-CHECK & SELF-UPDATE ENGINE (POWERSHELL & CMD)
# Check & pull updates directly in Terminal without opening GitHub in browser!
# Usage:
#   hmfa check                 (or .\update.ps1 check / .\update.ps1 -CheckOnly)
#   hmfa update                (or .\update.ps1 update / .\update.ps1)
#   hmfa status                (or .\update.ps1 status)
#   hmfa auto-check enable     (enable non-intrusive PowerShell update reminder)
#   hmfa auto-check disable    (remove PowerShell update reminder)
# ==============================================================================
param(
    [Parameter(Position = 0)]
    [string]$Command = "update",
    [Parameter(Position = 1)]
    [string]$SubArg = "",
    [switch]$CheckOnly,
    [switch]$Force,
    [switch]$HermesOnly,
    [switch]$Json
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoOwner = "zidanaisar624"
$RepoName  = "hermes-mfa-filmmaking-and-agent-skills"

if ($CheckOnly) { $Command = "check" }

# Handle optional PowerShell terminal startup auto-check toggle
if ($Command -eq "auto-check") {
    $BeginMarker = "# >>> hmfa-auto-update-check >>>"
    $EndMarker   = "# <<< hmfa-auto-update-check <<<"
    $ProfilePath = $PROFILE.CurrentUserAllHosts
    if (-not $ProfilePath) { $ProfilePath = $PROFILE }

    if ($SubArg -eq "enable" -or $SubArg -eq "on") {
        New-Item -ItemType Directory -Force -Path (Split-Path $ProfilePath -Parent) | Out-Null
        $Existing = if (Test-Path $ProfilePath) { Get-Content $ProfilePath -Raw } else { "" }
        if ($Existing -notmatch [regex]::Escape($BeginMarker)) {
            $Block = @"

$BeginMarker
# Checks once every 24h in background cache if a new Hermes Filmmaking Skills update exists
try {
    `$hmfaStamp = Join-Path `$env:LOCALAPPDATA "hermes-filmmaking-cli\last_check.txt"
    if (-not (Test-Path `$hmfaStamp) -or ((Get-Date) - (Get-Item `$hmfaStamp).LastWriteTime).TotalHours -ge 24) {
        New-Item -ItemType Directory -Force -Path (Split-Path `$hmfaStamp -Parent) | Out-Null
        Set-Date | Out-String | Set-Content `$hmfaStamp -ErrorAction SilentlyContinue
        `$res = hmfa check --json 2>`$null | ConvertFrom-Json
        if (`$res.update_available) {
            Write-Host "[HMFA] Update baru tersedia di repo Filmmaking Skills (`$(`$res.remote.commit_short))! Ketik 'hmfa update' untuk update otomatis." -ForegroundColor Yellow
        }
    }
} catch {}
$EndMarker
"@
            Add-Content -Path $ProfilePath -Value $Block -Encoding UTF8
        }
        Write-Host "[OK] Auto-check 24 jam diaktifkan di PowerShell Profile: $ProfilePath" -ForegroundColor Green
        exit 0
    } elseif ($SubArg -eq "disable" -or $SubArg -eq "off") {
        if (Test-Path $ProfilePath) {
            $Raw = Get-Content $ProfilePath -Raw
            $Pattern = "(?s)\r?\n?" + [regex]::Escape($BeginMarker) + ".*?" + [regex]::Escape($EndMarker)
            $Cleaned = [regex]::Replace($Raw, $Pattern, "")
            Set-Content -Path $ProfilePath -Value $Cleaned -Encoding UTF8
        }
        Write-Host "[OK] Auto-check dinonaktifkan dari PowerShell Profile." -ForegroundColor Cyan
        exit 0
    } else {
        Write-Host "Usage: hmfa auto-check enable | disable" -ForegroundColor Yellow
        exit 1
    }
}

# Delegate to Python harness if available
$PythonCmd = $null
foreach ($cand in @("python", "python3", "py")) {
    if (Get-Command $cand -ErrorAction SilentlyContinue) {
        try {
            $ver = & $cand --version 2>&1
            if ($LASTEXITCODE -eq 0 -and "$ver" -match "Python 3") {
                $PythonCmd = $cand
                break
            }
        } catch {}
    }
}

if ($PythonCmd) {
    $env:PYTHONPATH = "$(Join-Path $RepoRoot 'agent-harness');$env:PYTHONPATH"
    $Forward = @("-m", "cli_anything.filmmaking_advisor", "--repo", $RepoRoot, $Command)
    if ($SubArg)     { $Forward += $SubArg }
    if ($Force)      { $Forward += "--force" }
    if ($HermesOnly) { $Forward += "--hermes-only" }
    if ($Json)       { $Forward += "--json" }
    & $PythonCmd @Forward
    exit $LASTEXITCODE
}

# Pure PowerShell fallback when Python 3 is not installed
$LocalVer = if (Test-Path (Join-Path $RepoRoot "VERSION")) { (Get-Content (Join-Path $RepoRoot "VERSION") -TotalCount 1).Trim() } else { "unknown" }
$LocalSha = "unknown"
if ((Test-Path (Join-Path $RepoRoot ".git")) -and (Get-Command git -ErrorAction SilentlyContinue)) {
    $LocalSha = (git -C $RepoRoot rev-parse --short HEAD 2>$null).Trim()
}

$ApiInfo = Invoke-RestMethod -Uri "https://api.github.com/repos/$RepoOwner/$RepoName/commits/main" -UseBasicParsing
$RemoteSha = $ApiInfo.sha.Substring(0, 7)
$RemoteMsg = ($ApiInfo.commit.message -split "`n")[0]

if ($Command -eq "check") {
    Write-Host "============================================================"
    Write-Host " Local  : v$LocalVer ($LocalSha)"
    Write-Host " Remote : $RemoteSha - $RemoteMsg"
    if ($LocalSha -ne $RemoteSha) {
        Write-Host " Status : UPDATE AVAILABLE! Jalankan: hmfa update" -ForegroundColor Yellow
    } else {
        Write-Host " Status : UP TO DATE!" -ForegroundColor Green
    }
    Write-Host "============================================================"
    exit 0
}

if ($Command -eq "update") {
    if ((Test-Path (Join-Path $RepoRoot ".git")) -and (Get-Command git -ErrorAction SilentlyContinue)) {
        git -C $RepoRoot pull --ff-only origin main
    } else {
        $ZipTmp = Join-Path $env:TEMP "hmfa_update.zip"
        $ExtTmp = Join-Path $env:TEMP "hmfa_update_ext"
        Invoke-WebRequest -Uri "https://codeload.github.com/$RepoOwner/$RepoName/zip/refs/heads/main" -OutFile $ZipTmp -UseBasicParsing
        if (Test-Path $ExtTmp) { Remove-Item $ExtTmp -Recurse -Force }
        Expand-Archive -Path $ZipTmp -DestinationPath $ExtTmp -Force
        $Inner = Get-ChildItem -Path $ExtTmp -Directory | Select-Object -First 1
        Get-ChildItem -Path $Inner.FullName | Where-Object { $_.Name -notin @("curiosity_ledger", ".git") } | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination $RepoRoot -Recurse -Force
        }
    }
    & (Join-Path $RepoRoot "install.ps1") -HermesOnly:$HermesOnly
}

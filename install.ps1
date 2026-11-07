# ==============================================================================
# UNIVERSAL AUTO-DISCOVERY INSTALLER (POWERSHELL 5.1 / 7+)
# Hermes Agent (#1) + OpenClaw + Claude + ChatGPT/Codex + Universal Agents
# - Automatically scans all drives & env/registry to find Hermes for ANY user
# - Preserves 100% of existing config.yaml, provider, model, and SOUL.md
# - Registers global `hmfa` & `hermes-filmmaking` terminal commands (CMD & PS)
# ==============================================================================
[CmdletBinding()]
param(
    [switch]$HermesOnly,
    [switch]$CoreOnly,
    [switch]$CopyFiles,
    [switch]$DryRun,
    [string]$HermesHome = "",
    [string]$CloneDir = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoOwner = "zidanaisar624"
$RepoName  = "hermes-mfa-filmmaking-and-agent-skills"
$RepoUrl   = "https://github.com/$RepoOwner/$RepoName.git"

# 1. Determine Repo Root (supports both local execution AND `irm .../install.ps1 | iex`)
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { "" }
if ($ScriptDir -and (Test-Path (Join-Path $ScriptDir "skills"))) {
    $RepoRoot = (Resolve-Path $ScriptDir).Path
} else {
    $DefaultBase = if ($CloneDir) { $CloneDir } else { Join-Path $env:LOCALAPPDATA "hermes-filmmaking-cli\repo" }
    $RepoRoot = $DefaultBase
    Write-Host "[*] Remote one-liner mode detected. Preparing local repository at: $RepoRoot" -ForegroundColor Cyan
    if (-not (Test-Path (Join-Path $RepoRoot "skills"))) {
        New-Item -ItemType Directory -Force -Path (Split-Path $RepoRoot -Parent) | Out-Null
        if (Get-Command git -ErrorAction SilentlyContinue) {
            git clone $RepoUrl $RepoRoot
        } else {
            $ZipTmp = Join-Path $env:TEMP "hmfa_bootstrap.zip"
            $ExtractTmp = Join-Path $env:TEMP "hmfa_bootstrap_extract"
            Invoke-WebRequest -Uri "https://codeload.github.com/$RepoOwner/$RepoName/zip/refs/heads/main" -OutFile $ZipTmp -UseBasicParsing
            if (Test-Path $ExtractTmp) { Remove-Item $ExtractTmp -Recurse -Force }
            Expand-Archive -Path $ZipTmp -DestinationPath $ExtractTmp -Force
            $Inner = Get-ChildItem -Path $ExtractTmp -Directory | Select-Object -First 1
            New-Item -ItemType Directory -Force -Path $RepoRoot | Out-Null
            Copy-Item -Path (Join-Path $Inner.FullName "*") -Destination $RepoRoot -Recurse -Force
        }
    }
}

# 2. Prefer Python deep-discovery harness when Python 3 is available
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
    $PyArgs = @((Join-Path $RepoRoot "install.py"), "--export-chatgpt")
    if ($HermesOnly) { $PyArgs += "--hermes-only" }
    if ($CoreOnly)   { $PyArgs += "--core-only" }
    if ($CopyFiles)  { $PyArgs += "--copy" }
    if ($DryRun)     { $PyArgs += "--dry-run" }
    if ($HermesHome) { $PyArgs += @("--hermes-home", $HermesHome) }

    & $PythonCmd @PyArgs
    $ExitCode = $LASTEXITCODE
    # Refresh current session PATH so `hmfa` works immediately without reopening terminal
    $BinDir = Join-Path $env:LOCALAPPDATA "hermes-filmmaking-cli\bin"
    if ((Test-Path $BinDir) -and ($env:PATH -notlike "*$BinDir*")) {
        $env:PATH = "$BinDir;$env:PATH"
    }
    Write-Host "`n[TIP] Di PowerShell atau CMD kapan pun, ketik: hmfa check  atau  hmfa update" -ForegroundColor Green
    exit $ExitCode
}

# 3. Pure PowerShell Zero-Python Fallback (Multi-Drive Hermes & Agent Auto-Discovery)
Write-Host "[*] Python 3 not detected -- running Native PowerShell Multi-Drive Deep Discovery..." -ForegroundColor Yellow

function Test-IsHermesHome([string]$PathToCheck) {
    if (-not $PathToCheck -or -not (Test-Path -LiteralPath $PathToCheck -PathType Container)) { return $false }
    $hasCfg = (Test-Path (Join-Path $PathToCheck "config.yaml")) -or (Test-Path (Join-Path $PathToCheck "SOUL.md")) -or (Test-Path (Join-Path $PathToCheck "profile.yaml"))
    $hasDir = (Test-Path (Join-Path $PathToCheck "skills")) -or (Test-Path (Join-Path $PathToCheck "profiles")) -or (Test-Path (Join-Path $PathToCheck "hermes-agent"))
    return ($hasCfg -and $hasDir)
}

$DiscoveredHermes = New-Object System.Collections.Generic.List[string]
$CandidatePaths = @()
if ($HermesHome) { $CandidatePaths += $HermesHome }
if ($env:HERMES_HOME) { $CandidatePaths += $env:HERMES_HOME }
$RegHermes = [Environment]::GetEnvironmentVariable("HERMES_HOME", "User")
if ($RegHermes) { $CandidatePaths += $RegHermes }
$CandidatePaths += (Join-Path $HOME ".hermes")
$CandidatePaths += (Join-Path $env:LOCALAPPDATA "hermes")
$CandidatePaths += (Join-Path $env:APPDATA "hermes")

Get-PSDrive -PSProvider FileSystem | ForEach-Object {
    $drv = $_.Root
    if ($drv -and (Test-Path $drv)) {
        foreach ($sub in @("HermesData", "Hermes", ".hermes", "AI\HermesData", "Program\HermesData\.hermes")) {
            $CandidatePaths += (Join-Path $drv $sub)
        }
    }
}

foreach ($c in $CandidatePaths) {
    if ($c -and (Test-IsHermesHome $c)) {
        $full = [System.IO.Path]::GetFullPath($c)
        if (-not ($DiscoveredHermes -contains $full)) { $DiscoveredHermes.Add($full) }
    }
}

$Targets = @()
foreach ($hRoot in $DiscoveredHermes) {
    $Targets += [PSCustomObject]@{ Label = "Hermes Root ($hRoot)"; SkillsDir = (Join-Path $hRoot "skills") }
    $profDir = Join-Path $hRoot "profiles"
    if (Test-Path $profDir) {
        Get-ChildItem -Path $profDir -Directory | Where-Object { $_.Name -notlike ".*" } | ForEach-Object {
            if (Test-Path (Join-Path $_.FullName "config.yaml")) {
                $Targets += [PSCustomObject]@{ Label = "Hermes Profile [$($_.Name)]"; SkillsDir = (Join-Path $_.FullName "skills") }
            }
        }
    }
}

if (-not $HermesOnly) {
    foreach ($pair in @(
        @{ Name = "OpenClaw"; Dir = (Join-Path $HOME ".openclaw") },
        @{ Name = "Claude Code"; Dir = (Join-Path $HOME ".claude") },
        @{ Name = "OpenAI Codex"; Dir = (Join-Path $HOME ".codex") },
        @{ Name = "Universal Agents"; Dir = (Join-Path $HOME ".agents") }
    )) {
        if (Test-Path $pair.Dir) {
            $Targets += [PSCustomObject]@{ Label = $pair.Name; SkillsDir = (Join-Path $pair.Dir "skills") }
        }
    }
}

$CoreSet = @("filmmaking-videography-photography-s2", "auto-curiousity-for-film-making", "cli-anything-filmmaking-bridge")
$SkillFolders = Get-ChildItem -Path (Join-Path $RepoRoot "skills") -Directory | Where-Object {
    (Test-Path (Join-Path $_.FullName "SKILL.md")) -and (-not $CoreOnly -or ($CoreSet -contains $_.Name))
}

foreach ($t in $Targets) {
    $countSkills = $SkillFolders.Count
    if ($DryRun) {
        Write-Host (" [DRY-RUN] {0} -> {1} ({2} skills)" -f $t.Label, $t.SkillsDir, $countSkills)
        continue
    }
    New-Item -ItemType Directory -Force -Path $t.SkillsDir | Out-Null
    foreach ($sf in $SkillFolders) {
        $dst = Join-Path $t.SkillsDir $sf.Name
        if (Test-Path -LiteralPath $dst) {
            & cmd.exe /c rmdir "$dst" 2>$null
            if (Test-Path -LiteralPath $dst) { Remove-Item -LiteralPath $dst -Recurse -Force }
        }
        if (-not $CopyFiles) {
            & cmd.exe /c mklink /J "$dst" "$($sf.FullName)" >$null 2>$null
        }
        if (-not (Test-Path -LiteralPath $dst)) {
            Copy-Item -LiteralPath $sf.FullName -Destination $dst -Recurse -Force
        }
    }
    Write-Host (" [OK] {0} -> {1}" -f $t.Label, $t.SkillsDir) -ForegroundColor Green
}

if (-not $DryRun) {
    $BinDir = Join-Path $env:LOCALAPPDATA "hermes-filmmaking-cli\bin"
    New-Item -ItemType Directory -Force -Path $BinDir | Out-Null
    $UpdScript = Join-Path $RepoRoot "update.ps1"
    foreach ($name in @("hmfa", "hermes-filmmaking")) {
        $CmdPath = Join-Path $BinDir "$name.cmd"
        Set-Content -Path $CmdPath -Encoding Ascii -Value "@echo off`r`npowershell -NoProfile -ExecutionPolicy Bypass -File `"$UpdScript`" %*`r`n"
    }
    $UserPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($UserPath -notlike "*$BinDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$UserPath;$BinDir", "User")
    }
    if ($env:PATH -notlike "*$BinDir*") { $env:PATH = "$BinDir;$env:PATH" }
    Write-Host "`n[OK] Global CLI installed! Run 'hmfa check' or 'hmfa update' anytime in CMD or PowerShell." -ForegroundColor Cyan
}

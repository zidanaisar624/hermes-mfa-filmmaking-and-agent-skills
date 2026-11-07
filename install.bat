@echo off
setlocal
chcp 65001 >nul 2>nul
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
exit /b %ERRORLEVEL%

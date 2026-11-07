#!/usr/bin/env sh
# ==============================================================================
# UNIVERSAL AUTO-DISCOVERY INSTALLER (LINUX / MACOS / WSL / GIT BASH)
# Hermes Agent (#1) + OpenClaw + Claude + ChatGPT/Codex + Universal Agents
# ==============================================================================
set -e

REPO_OWNER="zidanaisar624"
REPO_NAME="hermes-mfa-filmmaking-and-agent-skills"
REPO_URL="https://github.com/${REPO_OWNER}/${REPO_NAME}.git"

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd || pwd)"
if [ -d "${SCRIPT_DIR}/skills" ] && [ -f "${SCRIPT_DIR}/install.py" ]; then
    REPO_ROOT="${SCRIPT_DIR}"
else
    REPO_ROOT="${HOME}/.local/share/hermes-filmmaking-cli/repo"
    echo "[*] Remote one-liner detected. Preparing repository at ${REPO_ROOT}..."
    mkdir -p "$(dirname "${REPO_ROOT}")"
    if [ ! -d "${REPO_ROOT}/.git" ]; then
        git clone "${REPO_URL}" "${REPO_ROOT}"
    fi
fi

if command -v python3 >/dev/null 2>&1; then
    python3 "${REPO_ROOT}/install.py" --export-chatgpt "$@"
elif command -v python >/dev/null 2>&1; then
    python "${REPO_ROOT}/install.py" --export-chatgpt "$@"
else
    echo "[!] Python 3 is required on POSIX systems to run install.py." >&2
    exit 1
fi

echo ""
echo "[TIP] Add ~/.local/bin to PATH if needed, then run: hmfa check  or  hmfa update"

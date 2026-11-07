# Using This Suite in Claude (Claude Code, Claude Desktop & Claude.ai Projects)

## 1. Claude Code CLI (Automatic Zero-MCP Setup)
Run the repository's universal installer (`install.bat`, `./install.ps1`, `./install.sh`, or `python install.py`). It automatically detects `~/.claude` and links/syncs all **48 skills** into `~/.claude/skills/`.

Alternatively, register directly via Claude Code's plugin marketplace:
```text
/plugin marketplace add zidanaisar624/hermes-mfa-filmmaking-and-agent-skills
```

## 2. Claude.ai Web & Claude Desktop Projects
1. Create a new **Claude Project** (e.g., *Filmmaking & Photography Research Advisor*).
2. Run `hmfa export-chatgpt` (or `python -m cli_anything.filmmaking_advisor export-chatgpt`) — the generated files in `exports/chatgpt/` work cleanly in **Claude Projects** too:
   - Paste `01_PASTE_INTO_CHATGPT_INSTRUCTIONS.md` into **Project Instructions**.
   - Upload `02_UPLOAD_AS_CHATGPT_KNOWLEDGE_BASE.md` (plus `docs/BUKU_KULIAH_LENGKAP_S1_S2_MFA_FILMMAKING_VIDEOGRAFI_FOTOGRAFI.md`) to **Project Knowledge**.
3. You can also zip any individual skill folder under `skills/<skill-name>/` and upload it directly to **Claude Settings -> Capabilities -> Skills**!

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal home-directory git repository (`C:\Users\ADMIN`) used as an AI agent workspace. It tracks shell utilities, agent configuration files, and personal tooling. It is **not** a standalone application project.

## Code

### `.local/bin/logging.py`

The only tracked code so far — a Python logging utility. Key design:

- `get_logger(name, ...)` is the main entry point; returns a named logger with a stdout `StreamHandler` and optional `FileHandler`.
- `LevelFilter` and `_apply_level_filter()` enable per-handler min/max level clamping (e.g. suppress DEBUG noise on stdout while keeping it in the file).
- Idempotent: returns the existing logger unchanged if handlers are already attached.

No build step, no test suite, no dependencies beyond the stdlib `logging` module.

## Environment Variables

See `.env.example` for the expected variables:
- `GITHUB_TOKEN` — GitHub personal access token
- `SUPABASE_URL` / `SUPABASE_ANON_KEY` — Supabase project credentials

Actual values live in `.env` (not tracked).

## Agent Workspace Conventions

Key rules from `AGENTS.md` that apply when working in this repo:

- Prefer `trash` over `rm` for deletions (recoverable beats gone).
- Before modifying any scheduler or shell RC file, inspect its current state and merge rather than overwrite.
- `MEMORY.md` is the agent's long-term memory index — read it at session start in main sessions only; do not expose in shared/group contexts.
- Daily session notes go in `memory/YYYY-MM-DD.md`; curated learnings go in `MEMORY.md`.
- `HEARTBEAT.md` controls periodic background checks — keep it small to limit token usage.

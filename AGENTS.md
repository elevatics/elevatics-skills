# AGENTS.md

Repo-wide instructions for any coding agent (Claude Code, OpenAI Codex, Cursor, Windsurf, Gemini CLI, GitHub Copilot, etc.) working in this repository. `AGENTS.md` and `SKILL.md` are complementary, both part of the open agent-tooling standards:

- **`AGENTS.md`** (this file) — always-loaded, repo-wide conventions and commands.
- **`skills/<name>/SKILL.md`** — task-specific procedures, loaded on demand when their `description` matches the task.

## What this repo is

A shared library of [Agent Skills](https://agentskills.io) — self-contained `SKILL.md` folders usable across any agent that supports the open Agent Skills standard (Claude, Codex, Cursor, Windsurf, Gemini CLI, and others).

## Conventions

- One skill = one folder under `skills/<skill-name>/`, folder name matches the `name` frontmatter field (lowercase-hyphenated).
- Every skill folder must contain a `SKILL.md` with `name` and `description` frontmatter — see [`template/SKILL.md`](template/SKILL.md).
- Instructions inside `SKILL.md` are written as direct directives to the agent, not human-facing documentation.
- Supporting scripts/assets for a skill live inside that skill's own folder and are referenced by relative path.

## Commands

```bash
python scripts/validate_skills.py   # validate all SKILL.md frontmatter before committing
```

## Adding or editing a skill

See [CONTRIBUTING.md](CONTRIBUTING.md).

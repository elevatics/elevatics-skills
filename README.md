# Elevatics Skills

A shared library of [Agent Skills](https://agentskills.io) for Claude — self-contained folders that teach Claude how to perform specific tasks. Each skill is loaded dynamically by Claude when its `description` matches the task at hand.

## Repository structure

```
elevatics-skills/
├── skills/            # All skills live here, one folder per skill
│   └── <skill-name>/
│       ├── SKILL.md   # Required: YAML frontmatter + instructions
│       └── ...         # Optional: scripts, references, assets
├── template/           # Starter scaffold for new skills
│   └── SKILL.md
└── spec/ (see anthropics/skills for the full specification)
```

## What is a skill?

A skill is a folder containing a `SKILL.md` file with YAML frontmatter (`name`, `description`) followed by Markdown instructions. When a task matches a skill's `description`, Claude reads the full file into context and follows it — optionally running bundled scripts or reading referenced files.

```markdown
---
name: my-skill-name
description: What this skill does and when Claude should use it.
---

# My Skill Name

Instructions for Claude...
```

## Adding a new skill

1. Copy [`template/SKILL.md`](template/SKILL.md) into a new folder under `skills/<skill-name>/`.
2. Use a lowercase, hyphenated `name` that matches the folder name.
3. Write a `description` that clearly states the trigger conditions — this is what Claude uses to decide when to load the skill.
4. Keep instructions directive ("do X", "when Y, do Z") rather than descriptive documentation.
5. Add any supporting scripts/assets alongside `SKILL.md` in the same folder.
6. Open a PR — see [CONTRIBUTING.md](CONTRIBUTING.md).

## Naming conventions

- Folder name = `name` field = lowercase-with-hyphens
- One skill = one folder = one clear responsibility
- Avoid overlapping trigger conditions between skills

## Universal / cross-agent compatibility

`SKILL.md` is not Claude-specific — it's the open [Agent Skills](https://agentskills.io) standard, natively supported by 40+ tools including Claude Code, OpenAI Codex, GitHub Copilot, Cursor, Windsurf, Gemini CLI, Goose, and OpenCode. Storing skills this way means they work unmodified across agents without per-platform forks or converters.

This repo also ships a root [`AGENTS.md`](AGENTS.md) — the complementary, always-loaded, repo-wide instruction file read by the same set of tools (Codex, Cursor, Windsurf, etc.), for conventions that shouldn't be gated behind a specific task trigger.

| Standard | Scope | Loaded | Read natively by |
|---|---|---|---|
| `skills/<name>/SKILL.md` | One task/procedure | On demand, when `description` matches | Claude, Codex, Cursor, Windsurf, Gemini CLI, Copilot, Goose, OpenCode |
| `AGENTS.md` | Whole repo | Always | Same tools above (repo-instructions convention) |
| MCP servers | Tool/data access | Connected at session start | Complementary, not a skill-storage format — MCP gives an agent *hands*, skills give it the *procedure* |

## Reference

- [Agent Skills specification](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) — the open standard this repo follows
- [agentskills.io](https://agentskills.io) — cross-platform adoption and showcase

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

## Reference

Built on the open [Agent Skills specification](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md) originally developed by Anthropic.

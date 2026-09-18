#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md has correct frontmatter.

Checks:
- SKILL.md exists directly under each skills/<folder>
- YAML frontmatter present with required fields: name, description
- `name` is lowercase-with-hyphens and matches the folder name
- `description` is non-empty
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    data = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    errors = []

    if not SKILLS_DIR.exists():
        print(f"No skills/ directory found at {SKILLS_DIR}")
        return 0

    skill_dirs = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    for skill_dir in sorted(skill_dirs):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue

        text = skill_md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        if frontmatter is None:
            errors.append(f"{skill_dir.name}/SKILL.md: missing or malformed YAML frontmatter")
            continue

        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if not name:
            errors.append(f"{skill_dir.name}/SKILL.md: missing 'name' field")
        elif not NAME_RE.match(name):
            errors.append(f"{skill_dir.name}/SKILL.md: 'name' must be lowercase-with-hyphens, got '{name}'")
        elif name != skill_dir.name:
            errors.append(f"{skill_dir.name}/SKILL.md: 'name' ('{name}') must match folder name ('{skill_dir.name}')")

        if not description:
            errors.append(f"{skill_dir.name}/SKILL.md: missing or empty 'description' field")

    if errors:
        print("Skill validation failed:\n")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(f"All {len(skill_dirs)} skill(s) validated successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

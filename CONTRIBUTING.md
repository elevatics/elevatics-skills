# Contributing a skill

1. **Create the folder**: `skills/<your-skill-name>/SKILL.md`, starting from [`template/SKILL.md`](template/SKILL.md).
2. **Frontmatter is required and must include**:
   - `name`: lowercase, hyphenated, matches the folder name
   - `description`: states *what* the skill does and *when* Claude should trigger it
3. **Keep skills self-contained**: any scripts, reference docs, or assets the skill needs live inside the same folder and are referenced by relative path.
4. **One responsibility per skill**: don't combine unrelated tasks in a single SKILL.md; split them instead.
5. **Avoid trigger overlap**: check existing skills in `skills/` so descriptions don't compete for the same tasks.
6. **Validate locally** before opening a PR:
   ```bash
   python scripts/validate_skills.py
   ```
7. **Open a PR** describing the skill's purpose and any manual testing you did.

CI runs the same validation script on every PR and will fail if a `SKILL.md` is missing required frontmatter or malformed.

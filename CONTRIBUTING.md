# Contributing Skills

Thanks for adding to `opencolin/skills`. This repository is intentionally simple so humans and coding agents can contribute without ceremony.

## Repository Shape

Each skill belongs in a top-level folder:

```text
skill-name/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

Only `SKILL.md` is required. Add `agents/openai.yaml` when the skill should have user-facing metadata. Add `references`, `scripts`, or `assets` only when they are genuinely useful.

## Skill Rules

- Use lowercase hyphen-case folder names.
- Keep one skill per top-level folder.
- Make the folder name match the `name` in `SKILL.md`.
- Write a specific `description` in frontmatter. This is what tells agents when to load the skill.
- Keep `SKILL.md` concise and procedural.
- Put long examples, schemas, policies, or brand guidance in `references/`.
- Put deterministic repeated code in `scripts/`.
- Put templates, icons, fonts, or reusable output materials in `assets/`.
- Do not include secrets, private customer data, credentials, or proprietary files.

## Adding A Skill

1. Copy `templates/skill` to a new top-level folder.
2. Search for overlapping skills before writing a new one:

```bash
rg -n "your-domain|your-deliverable|your-workflow" */SKILL.md README.md
```

3. Rename the folder and update `SKILL.md`.
4. Update `agents/openai.yaml` if present.
5. Add the skill to the table in `README.md`.
6. Run validation and duplicate checks:

```bash
python3 scripts/validate_skills.py
python3 scripts/check_duplicate_skills.py
```

If the duplicate checker flags a pair, merge the skills, narrow their boundaries, or document the intentional overlap in `.duplicate-skills.json`.

## Quality Bar

A good skill should answer:

- When should an agent use this?
- What workflow should the agent follow?
- What output should the agent produce?
- What edge cases should the agent handle?
- How does the agent know it did a good job?

Prefer a useful, narrow skill over a sprawling prompt essay.

## Pull Requests

PRs should include:

- a short explanation of the skill or change
- any example prompt used to test it
- confirmation that `python3 scripts/validate_skills.py` passes
- confirmation that `python3 scripts/check_duplicate_skills.py` passes

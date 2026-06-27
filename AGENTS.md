# Agent Contribution Guide

This repository is a public skill library. Keep it useful by reusing and refining existing skills before adding new ones.

## DRY Workflow For Skills

Follow the [DRY.codes](https://dry.codes/) pattern: search first, read the strongest matches, then check for duplication before finishing.

Before creating or changing a skill:

1. Search for nearby skills by domain, artifact, and verb.

```bash
rg -n "sponsor|event|email|hackathon|strategy|deploy|audit" */SKILL.md README.md
```

2. Read the closest `SKILL.md` files completely.
3. Prefer extending, renaming, or narrowing an existing skill over creating a parallel one.
4. If a new skill is still right, make its boundary explicit in the description and workflow.
5. Run both checks before you finish.

```bash
python3 scripts/validate_skills.py
python3 scripts/check_duplicate_skills.py
```

## Handling Overlap

Use these defaults:

- If two skills produce the same deliverable for the same audience, merge them.
- If one skill is a broad workflow and another is a focused sub-workflow, keep both but name the boundary clearly.
- If overlap is intentional, add a short justification to `.duplicate-skills.json`.
- If the duplicate checker reports a known candidate, avoid expanding either skill until that pair is merged or renamed.

Do not add secrets, credentials, private customer data, or proprietary project files.

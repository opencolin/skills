#!/usr/bin/env python3
"""Validate top-level skill folders in this repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SKIP_DIRS = {".git", ".github", "scripts", "templates"}


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["missing opening frontmatter fence"]

    try:
        _, raw, _ = text.split("---\n", 2)
    except ValueError:
        return {}, ["missing closing frontmatter fence"]

    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"').strip("'")
        data[key.strip()] = value
    return data, errors


def is_skill_dir(path: Path) -> bool:
    return path.is_dir() and path.name not in SKIP_DIRS and (path / "SKILL.md").exists()


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"

    if not NAME_RE.match(path.name):
        errors.append("folder name must be lowercase hyphen-case")

    frontmatter, parse_errors = parse_frontmatter(skill_file)
    errors.extend(parse_errors)

    name = frontmatter.get("name", "")
    description = frontmatter.get("description", "")

    if not name:
        errors.append("frontmatter missing name")
    elif name != path.name:
        errors.append(f"frontmatter name {name!r} must match folder name {path.name!r}")
    elif not NAME_RE.match(name):
        errors.append("frontmatter name must be lowercase hyphen-case")

    if not description:
        errors.append("frontmatter missing description")
    elif len(description) < 40:
        errors.append("description should be specific enough to trigger reliably")

    agent_yaml = path / "agents" / "openai.yaml"
    if agent_yaml.exists():
        text = agent_yaml.read_text(encoding="utf-8")
        if f"${path.name}" not in text:
            errors.append("agents/openai.yaml default prompt should mention the skill as $skill-name")

    return errors


def main() -> int:
    skill_dirs = sorted(p for p in ROOT.iterdir() if is_skill_dir(p))
    if not skill_dirs:
        print("No skill directories found.", file=sys.stderr)
        return 1

    failed = False
    for skill_dir in skill_dirs:
        errors = validate_skill(skill_dir)
        if errors:
            failed = True
            print(f"FAIL {skill_dir.name}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {skill_dir.name}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

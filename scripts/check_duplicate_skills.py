#!/usr/bin/env python3
"""Find duplicated or highly overlapping skills before they land."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / ".duplicate-skills.json"
DEFAULT_THRESHOLD = 0.22
SKIP_DIRS = {".git", ".github", "scripts", "templates"}
TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9-]{2,}")
HEADING_RE = re.compile(r"^#{1,4}\s+(.+)$", re.MULTILINE)

STOPWORDS = {
    "about",
    "after",
    "again",
    "agent",
    "agents",
    "also",
    "and",
    "any",
    "are",
    "before",
    "but",
    "can",
    "clear",
    "complete",
    "create",
    "deliverable",
    "deliverables",
    "doc",
    "docs",
    "each",
    "for",
    "from",
    "generate",
    "give",
    "has",
    "have",
    "how",
    "into",
    "its",
    "make",
    "must",
    "not",
    "one",
    "only",
    "output",
    "pack",
    "prompt",
    "provide",
    "run",
    "should",
    "skill",
    "skills",
    "step",
    "that",
    "the",
    "then",
    "this",
    "through",
    "use",
    "used",
    "user",
    "when",
    "with",
    "workflow",
    "write",
    "you",
    "your",
}


@dataclass(frozen=True)
class Skill:
    name: str
    path: Path
    description: str
    body: str
    headings: tuple[str, ...]
    tokens: Counter[str]


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    try:
        _, raw_frontmatter, body = text.split("---\n", 2)
    except ValueError:
        return {}, text

    return parse_frontmatter(raw_frontmatter), body


def parse_frontmatter(raw: str) -> dict[str, str]:
    data: dict[str, str] = {}
    lines = raw.splitlines()
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped or line.startswith((" ", "\t")):
            index += 1
            continue
        if ":" not in line:
            index += 1
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value in {"|", ">"}:
            block: list[str] = []
            index += 1
            while index < len(lines):
                continuation = lines[index]
                if continuation and not continuation.startswith((" ", "\t")):
                    break
                block.append(continuation.strip())
                index += 1
            data[key] = " ".join(part for part in block if part)
            continue

        data[key] = value.strip('"').strip("'")
        index += 1

    return data


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def digest(text: str) -> str:
    return hashlib.sha256(normalize_text(text).encode("utf-8")).hexdigest()


def tokenize(text: str) -> Counter[str]:
    words: list[str] = []
    for token in TOKEN_RE.findall(text.lower().replace("_", "-")):
        parts = [part for part in token.split("-") if keep_token(part)]
        if keep_token(token):
            words.append(token)
        words.extend(parts)

    tokens = Counter(words)
    for first, second in zip(words, words[1:]):
        if first != second:
            tokens[f"{first}__{second}"] += 1
    return tokens


def keep_token(token: str) -> bool:
    return len(token) >= 3 and token not in STOPWORDS and not token.isdigit()


def skill_dirs() -> list[Path]:
    return sorted(
        path
        for path in ROOT.iterdir()
        if path.is_dir() and path.name not in SKIP_DIRS and (path / "SKILL.md").exists()
    )


def read_skill(path: Path) -> Skill:
    skill_file = path / "SKILL.md"
    text = skill_file.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)
    description = frontmatter.get("description", "")
    headings = tuple(match.group(1).strip() for match in HEADING_RE.finditer(body))
    search_text = "\n".join((path.name, description, " ".join(headings), body))

    return Skill(
        name=frontmatter.get("name", path.name),
        path=skill_file,
        description=description,
        body=body,
        headings=headings,
        tokens=tokenize(search_text),
    )


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        print(f"FAIL {path.name}: invalid JSON: {error}", file=sys.stderr)
        raise SystemExit(1) from error


def pair_key(first: str, second: str) -> str:
    return "|".join(sorted((first, second)))


def pair_entries(config: dict, key: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for entry in config.get(key, []):
        skills = entry.get("skills", [])
        if len(skills) != 2:
            continue
        entries[pair_key(skills[0], skills[1])] = entry.get("reason", "")
    return entries


def validate_config(config: dict, names: set[str]) -> list[str]:
    errors: list[str] = []
    for section in ("allowed_pairs", "known_duplicate_candidates"):
        for entry in config.get(section, []):
            skills = entry.get("skills", [])
            if len(skills) != 2:
                errors.append(f"{section} entry must name exactly two skills: {entry!r}")
                continue
            for skill in skills:
                if skill not in names:
                    errors.append(f"{section} references unknown skill {skill!r}")
            if not entry.get("reason"):
                errors.append(f"{section} entry for {skills!r} needs a reason")
    return errors


def build_vectors(skills: list[Skill]) -> dict[str, dict[str, float]]:
    document_frequency: Counter[str] = Counter()
    for skill in skills:
        document_frequency.update(skill.tokens.keys())

    skill_count = len(skills)
    vectors: dict[str, dict[str, float]] = {}
    for skill in skills:
        vector: dict[str, float] = {}
        for token, count in skill.tokens.items():
            idf = math.log((1 + skill_count) / (1 + document_frequency[token])) + 1
            vector[token] = count * idf
        vectors[skill.name] = vector
    return vectors


def cosine(first: dict[str, float], second: dict[str, float]) -> float:
    if not first or not second:
        return 0.0

    if len(first) > len(second):
        first, second = second, first

    dot = sum(weight * second.get(token, 0.0) for token, weight in first.items())
    first_norm = math.sqrt(sum(weight * weight for weight in first.values()))
    second_norm = math.sqrt(sum(weight * weight for weight in second.values()))
    if not first_norm or not second_norm:
        return 0.0
    return dot / (first_norm * second_norm)


def find_exact_duplicates(skills: list[Skill]) -> list[str]:
    failures: list[str] = []

    by_description: defaultdict[str, list[str]] = defaultdict(list)
    by_body: defaultdict[str, list[str]] = defaultdict(list)
    for skill in skills:
        if skill.description:
            by_description[digest(skill.description)].append(skill.name)
        if normalize_text(skill.body):
            by_body[digest(skill.body)].append(skill.name)

    for names in by_description.values():
        if len(names) > 1:
            failures.append(f"identical frontmatter descriptions: {', '.join(sorted(names))}")

    for names in by_body.values():
        if len(names) > 1:
            failures.append(f"identical SKILL.md bodies: {', '.join(sorted(names))}")

    return failures


def skill_pair_score(skills: list[Skill]) -> dict[str, tuple[float, str, str]]:
    vectors = build_vectors(skills)
    scores: dict[str, tuple[float, str, str]] = {}

    for first, second in itertools.combinations(skills, 2):
        score = cosine(vectors[first.name], vectors[second.name])
        scores[pair_key(first.name, second.name)] = (score, first.name, second.name)

    return scores


def print_pair(label: str, first: str, second: str, score: float, reason: str = "") -> None:
    suffix = f" - {reason}" if reason else ""
    print(f"{label} {first} <-> {second} ({score:.3f}){suffix}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--threshold", type=float, default=None)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config)
    threshold = args.threshold if args.threshold is not None else float(config.get("threshold", DEFAULT_THRESHOLD))
    skills = [read_skill(path) for path in skill_dirs()]
    names = {skill.name for skill in skills}

    config_errors = validate_config(config, names)
    if config_errors:
        for error in config_errors:
            print(f"FAIL config: {error}")
        return 1

    allowed = pair_entries(config, "allowed_pairs")
    known = pair_entries(config, "known_duplicate_candidates")
    exact_failures = find_exact_duplicates(skills)
    scores = skill_pair_score(skills)

    unreviewed: list[tuple[float, str, str]] = []
    allowed_hits: list[tuple[float, str, str, str]] = []
    known_hits: list[tuple[float, str, str, str]] = []

    for key, (score, first, second) in scores.items():
        if score < threshold:
            continue
        if key in allowed:
            allowed_hits.append((score, first, second, allowed[key]))
        elif key in known:
            known_hits.append((score, first, second, known[key]))
        else:
            unreviewed.append((score, first, second))

    for key, reason in known.items():
        if key not in scores:
            continue
        score, first, second = scores[key]
        if all(pair_key(first, second) != pair_key(hit[1], hit[2]) for hit in known_hits):
            known_hits.append((score, first, second, reason))

    if exact_failures:
        print("FAIL exact duplicate skills found:")
        for failure in exact_failures:
            print(f"  - {failure}")

    if known_hits:
        print("KNOWN duplicate candidates to resolve:")
        for score, first, second, reason in sorted(known_hits, reverse=True):
            print_pair("  ?", first, second, score, reason)

    if args.verbose and allowed_hits:
        print("Reviewed overlaps allowed by .duplicate-skills.json:")
        for score, first, second, reason in sorted(allowed_hits, reverse=True):
            print_pair("  OK", first, second, score, reason)

    if unreviewed:
        print("FAIL unreviewed duplicate skill candidates:")
        for score, first, second in sorted(unreviewed, reverse=True):
            print_pair("  -", first, second, score)
        print(
            "\nResolve these by merging skills, narrowing their boundaries, or adding "
            "a justified entry to .duplicate-skills.json."
        )

    if exact_failures or unreviewed:
        return 1

    print(f"OK no unreviewed duplicate skills found at threshold {threshold:.2f}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

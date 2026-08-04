#!/usr/bin/env python3
"""Validate repository structure, skills, references, JSON, and JSONL files."""

from __future__ import annotations

import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "skills/create-agent-skill/scripts/validate_skill.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("portable_skill_validator", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load skill validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_json_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    for path in ROOT.rglob("*.jsonl"):
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"{path.relative_to(ROOT)}:{number}: {exc}")


def validate_markdown_links(errors: list[str]) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in link_re.finditer(text):
            raw_target = match.group(1)
            target = raw_target.split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT):
                errors.append(f"{path.relative_to(ROOT)}: link escapes repository: {raw_target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing link target: {raw_target}")


def main() -> int:
    errors: list[str] = []
    validator = load_validator()
    skill_dirs = sorted({path.parent for path in (ROOT / "skills").glob("*/SKILL.md")})
    example_dirs = sorted({path.parent for path in (ROOT / "examples").glob("*/SKILL.md")})
    if not skill_dirs:
        errors.append("no installable skills found")
    for skill_dir in skill_dirs + example_dirs:
        for error in validator.validate(skill_dir):
            errors.append(f"{skill_dir.relative_to(ROOT)}: {error}")
    validate_json_files(errors)
    validate_markdown_links(errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(skill_dirs)} installable skills and {len(example_dirs)} examples")
    return 0


if __name__ == "__main__":
    sys.exit(main())

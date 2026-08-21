#!/usr/bin/env python3
"""Deterministic structure, privacy, and routing-fixture validator for qiaobs-skills."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXPECTED = {"trace-feature-chain", "run-autonomous-workpacks", "reason-from-reality"}
BANNED = re.compile(r"\b(?:TODO|TBD|PLACEHOLDER)\b|<owner>|gho_[A-Za-z0-9]{10,}|github_pat_[A-Za-z0-9_]{20,}|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY|https?://[^\s/]+/[^\s]*(?:token|signature|sig=|secret)", re.I)
PERSONAL_PATH = re.compile(r"(?:[A-Z]:\\Users\\|/Users/|/home/)[^\s`\"']+", re.I)
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(errors, f"{path}: missing frontmatter")
        return {}
    parts = text.split("\n---", 1)
    if len(parts) != 2:
        fail(errors, f"{path}: malformed frontmatter")
        return {}
    result: dict[str, str] = {}
    for line in parts[0][4:].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            fail(errors, f"{path}: invalid frontmatter line {line!r}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in result:
            fail(errors, f"{path}: duplicate frontmatter key {key}")
        if len(value) >= 2 and value[0] == value[-1] == '"':
            value = value[1:-1].replace('\\"', '"')
        result[key] = value
    return result


def scan_public_text(path: Path, errors: list[str]) -> None:
    raw = path.read_text(encoding="utf-8")
    # The validator's own regex and diagnostic prose necessarily mention forbidden markers.
    if path.as_posix().endswith("scripts/validate_skills.py"):
        return
    if BANNED.search(raw) or PERSONAL_PATH.search(raw):
        fail(errors, f"{path}: banned placeholder, secret, URL, or personal path")


def validate_skill(name: str, errors: list[str]) -> None:
    directory = SKILLS_DIR / name
    skill = directory / "SKILL.md"
    if not skill.exists():
        fail(errors, f"{name}: missing SKILL.md")
        return
    front = parse_frontmatter(skill, errors)
    if set(front) != {"name", "description"}:
        fail(errors, f"{skill}: frontmatter keys must be exactly name and description")
    if front.get("name") != name:
        fail(errors, f"{skill}: name does not match directory")
    if not NAME.fullmatch(front.get("name", "")):
        fail(errors, f"{skill}: invalid name")
    description = front.get("description", "")
    if not description or len(description) > 1024:
        fail(errors, f"{skill}: description empty or too long")
    text = skill.read_text(encoding="utf-8")
    if len(text.splitlines()) > 500:
        fail(errors, f"{skill}: over 500 lines")
    scan_public_text(skill, errors)
    yaml = directory / "agents" / "openai.yaml"
    if not yaml.exists():
        fail(errors, f"{name}: missing agents/openai.yaml")
    else:
        ytext = yaml.read_text(encoding="utf-8")
        if "interface:" not in ytext or "display_name:" not in ytext or "short_description:" not in ytext:
            fail(errors, f"{yaml}: missing generated interface fields")
        scan_public_text(yaml, errors)
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if link.startswith(("http://", "https://", "#")):
            continue
        target = (skill.parent / link).resolve()
        if not target.exists():
            fail(errors, f"{skill}: missing referenced file {link}")
    for ref in (directory / "references").glob("*"):
        if ref.is_file():
            scan_public_text(ref, errors)


def validate_evals(errors: list[str]) -> None:
    paths = sorted((ROOT / "evals").glob("*.trigger.json"))
    if len(paths) != 3:
        fail(errors, f"evals: expected three trigger files, found {len(paths)}")
    for path in paths:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            fail(errors, f"{path}: invalid JSON: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
            fail(errors, f"{path}: expected object with cases array")
            continue
        ids = [item.get("id") for item in data["cases"] if isinstance(item, dict)]
        if len(data["cases"]) != 20 or len(set(ids)) != 20:
            fail(errors, f"{path}: expected 20 unique cases")
        values = [item.get("should_trigger") for item in data["cases"] if isinstance(item, dict)]
        if values.count(True) != 10 or values.count(False) != 10:
            fail(errors, f"{path}: expected 10 positive and 10 negative cases")
        for item in data["cases"]:
            if not isinstance(item, dict) or not item.get("prompt"):
                fail(errors, f"{path}: every case needs a prompt")
        scan_public_text(path, errors)


def main() -> int:
    errors: list[str] = []
    found = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()} if SKILLS_DIR.exists() else set()
    if found != EXPECTED:
        fail(errors, f"skills: expected exactly {sorted(EXPECTED)}, found {sorted(found)}")
    for name in sorted(EXPECTED):
        validate_skill(name, errors)
    validate_evals(errors)
    required = [
        ROOT / "README.md", ROOT / "README.zh-CN.md", ROOT / "LICENSE", ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md", ROOT / "CODE_OF_CONDUCT.md", ROOT / "SECURITY.md",
        ROOT / "ACKNOWLEDGEMENTS.md", ROOT / "docs" / "skill-engineering-notes.md", ROOT / "docs" / "origins-and-method.md",
        ROOT / "evals" / "verification-record.md",
    ]
    for path in required:
        if not path.exists():
            fail(errors, f"missing required file {path.relative_to(ROOT)}")
        else:
            scan_public_text(path, errors)
    if errors:
        print("VALIDATION_FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"VALIDATION_PASS skills={len(EXPECTED)} eval_files=3")
    return 0


if __name__ == "__main__":
    sys.exit(main())

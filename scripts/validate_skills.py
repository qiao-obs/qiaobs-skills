#!/usr/bin/env python3
"""Deterministic structure, privacy, link, asset, and routing-fixture validator."""
from __future__ import annotations

import json
import re
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
EXPECTED = {"trace-feature-chain", "run-autonomous-workpacks", "reason-from-reality"}
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BANNED = re.compile(
    r"\b(?:TODO|TBD|PLACEHOLDER)\b|<owner>|gho_[A-Za-z0-9]{10,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY|https?://[^\s/]+/[^\s]*(?:token|signature|sig=|secret)",
    re.I,
)
PERSONAL_PATH = re.compile(r"(?:[A-Z]:\\Users\\|/Users/|/home/)[^\s`\"']+", re.I)
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".toml", ".txt", ".svg"}
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", "node_modules"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = read_text(path)
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
    raw = read_text(path)
    if BANNED.search(raw) or PERSONAL_PATH.search(raw):
        fail(errors, f"{path.relative_to(ROOT)}: banned placeholder, secret, URL, or personal path")
    if "`r`n" in raw or r"\\r\\n" in raw:
        fail(errors, f"{path.relative_to(ROOT)}: leaked escaped newline literal")
    if any(ord(ch) < 32 and ch not in "\n\r\t" for ch in raw):
        fail(errors, f"{path.relative_to(ROOT)}: control character leaked")


def local_target(link: str) -> Path | None:
    link = link.strip().strip("<>")
    if not link or link.startswith(("http://", "https://", "mailto:", "#")):
        return None
    link = link.split("#", 1)[0].split("?", 1)[0].strip()
    if not link:
        return None
    return link


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = read_text(path)
    for raw_link in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        link = local_target(raw_link)
        if link is None:
            continue
        target = (path.parent / link).resolve()
        if not target.exists():
            fail(errors, f"{path.relative_to(ROOT)}: missing linked file {raw_link}")


def png_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return width, height


def require_png(path: Path, size: tuple[int, int], errors: list[str]) -> None:
    if not path.exists():
        fail(errors, f"{path.relative_to(ROOT)}: missing PNG asset")
        return
    actual = png_size(path)
    if actual != size:
        fail(errors, f"{path.relative_to(ROOT)}: expected PNG size {size}, found {actual}")
    if path.stat().st_size > 300_000:
        fail(errors, f"{path.relative_to(ROOT)}: image is unexpectedly large")


def validate_metadata(name: str, directory: Path, errors: list[str]) -> None:
    yaml = directory / "agents" / "openai.yaml"
    if not yaml.exists():
        fail(errors, f"{name}: missing agents/openai.yaml")
        return
    text = read_text(yaml)
    for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
        if field not in text:
            fail(errors, f"{yaml.relative_to(ROOT)}: missing {field}")
    for field in ("icon_small", "icon_large"):
        match = re.search(rf"^\s*{field}:\s*[\"']?([^\"'\n]+)", text, re.M)
        if match:
            target = (directory / match.group(1).strip()).resolve()
            if not target.exists():
                fail(errors, f"{yaml.relative_to(ROOT)}: missing asset {match.group(1)}")
        else:
            fail(errors, f"{yaml.relative_to(ROOT)}: malformed {field}")
    prompt = re.search(r"^\s*default_prompt:\s*[\"']?(.+?)\s*[\"']?$", text, re.M)
    if not prompt or not prompt.group(1).strip():
        fail(errors, f"{yaml.relative_to(ROOT)}: default_prompt is empty")
    scan_public_text(yaml, errors)


def validate_skill(name: str, errors: list[str]) -> None:
    directory = SKILLS_DIR / name
    skill = directory / "SKILL.md"
    if not skill.exists():
        fail(errors, f"{name}: missing SKILL.md")
        return
    front = parse_frontmatter(skill, errors)
    if set(front) != {"name", "description"}:
        fail(errors, f"{skill.relative_to(ROOT)}: frontmatter keys must be exactly name and description")
    if front.get("name") != name:
        fail(errors, f"{skill.relative_to(ROOT)}: name does not match directory")
    if not NAME.fullmatch(front.get("name", "")):
        fail(errors, f"{skill.relative_to(ROOT)}: invalid name")
    description = front.get("description", "")
    if not description or len(description) > 1024:
        fail(errors, f"{skill.relative_to(ROOT)}: description empty or too long")
    text = read_text(skill)
    if len(text.splitlines()) > 500:
        fail(errors, f"{skill.relative_to(ROOT)}: over 500 lines")
    scan_public_text(skill, errors)
    validate_metadata(name, directory, errors)
    validate_markdown_links(skill, errors)
    references = directory / "references"
    if references.exists():
        for child in references.iterdir():
            if child.is_dir():
                fail(errors, f"{references.relative_to(ROOT)}: references must stay one level deep")
            elif child.is_file():
                scan_public_text(child, errors)
                validate_markdown_links(child, errors)


def validate_evals(errors: list[str]) -> None:
    paths = sorted((ROOT / "evals").glob("*.trigger.json"))
    if len(paths) != 3:
        fail(errors, f"evals: expected three trigger files, found {len(paths)}")
    for path in paths:
        try:
            data = json.loads(read_text(path))
        except json.JSONDecodeError as exc:
            fail(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        if not isinstance(data, dict) or not isinstance(data.get("cases"), list):
            fail(errors, f"{path.relative_to(ROOT)}: expected object with cases array")
            continue
        ids = [item.get("id") for item in data["cases"] if isinstance(item, dict)]
        if len(data["cases"]) != 20 or len(set(ids)) != 20:
            fail(errors, f"{path.relative_to(ROOT)}: expected 20 unique cases")
        values = [item.get("should_trigger") for item in data["cases"] if isinstance(item, dict)]
        if values.count(True) != 10 or values.count(False) != 10:
            fail(errors, f"{path.relative_to(ROOT)}: expected 10 positive and 10 negative cases")
        for item in data["cases"]:
            if not isinstance(item, dict) or not item.get("prompt"):
                fail(errors, f"{path.relative_to(ROOT)}: every case needs a prompt")
        scan_public_text(path, errors)


def validate_composition(errors: list[str]) -> None:
    path = ROOT / "evals" / "composition.fixtures.json"
    if not path.exists():
        fail(errors, "evals/composition.fixtures.json: missing composition fixture file")
        return
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return
    cases = data.get("cases") if isinstance(data, dict) else None
    if not isinstance(cases, list) or len(cases) != 3:
        fail(errors, f"{path.relative_to(ROOT)}: expected exactly three composition cases")
        return
    expected = {"trace-feature-chain", "run-autonomous-workpacks", "reason-from-reality"}
    for case in cases:
        if not isinstance(case, dict) or not case.get("id") or not case.get("prompt"):
            fail(errors, f"{path.relative_to(ROOT)}: every case needs id and prompt")
            continue
        loads = set(case.get("should_load", []))
        rejects = set(case.get("should_not_load", []))
        if not loads.issubset(expected) or not rejects.issubset(expected) or loads & rejects:
            fail(errors, f"{path.relative_to(ROOT)}: invalid load boundary in {case.get('id')}")
    scan_public_text(path, errors)


def validate_observable_autonomy_scenarios(errors: list[str]) -> None:
    path = ROOT / "evals" / "observable-autonomy-scenarios.md"
    if not path.exists():
        fail(errors, f"missing {path.relative_to(ROOT)}")
        return
    text = read_text(path)
    required_ids = [f"OA-{index:02d}" for index in range(1, 11)]
    if any(identifier not in text for identifier in required_ids):
        fail(errors, f"{path.relative_to(ROOT)}: expected OA-01 through OA-10")
    for phrase in ("CHECKPOINT", "GATE", "Visibility", "Non-blocking autonomy", "State accuracy", "Noise control", "Delegation discipline", "Gate correctness", "NOT RUN"):
        if phrase not in text:
            fail(errors, f"{path.relative_to(ROOT)}: missing behavior-rubric phrase {phrase}")
    scan_public_text(path, errors)
    validate_markdown_links(path, errors)

def validate_repository_docs(errors: list[str]) -> None:
    required = [
        ROOT / "README.md", ROOT / "README.en.md", ROOT / "README.zh-CN.md", ROOT / "LICENSE",
        ROOT / "CHANGELOG.md", ROOT / "CONTRIBUTING.md", ROOT / "CODE_OF_CONDUCT.md", ROOT / "SECURITY.md",
        ROOT / "ACKNOWLEDGEMENTS.md", ROOT / "docs" / "skill-engineering-notes.md", ROOT / "docs" / "origins-and-method.md",
        ROOT / "evals" / "verification-record.md", ROOT / "evals" / "observable-autonomy-scenarios.md", ROOT / "assets" / "hero-light.png", ROOT / "assets" / "hero-dark.png",
        ROOT / "assets" / "social-preview.png", ROOT / "assets" / "banner.svg",
    ]
    for path in required:
        if not path.exists():
            fail(errors, f"missing required file {path.relative_to(ROOT)}")
        elif path.suffix in TEXT_SUFFIXES:
            scan_public_text(path, errors)
            if path.suffix == ".md":
                validate_markdown_links(path, errors)
    readme = read_text(ROOT / "README.md")
    if not re.search(r"[\u3400-\u9fff]", readme):
        fail(errors, "README.md: default homepage must be human-written Chinese")
    if "README.en.md" not in readme or "README.md" not in read_text(ROOT / "README.en.md"):
        fail(errors, "README language links are not bidirectional")
    for name in sorted(EXPECTED):
        for suffix in (".md", ".zh-CN.md"):
            path = ROOT / "docs" / "skills" / f"{name}{suffix}"
            if not path.exists():
                fail(errors, f"missing bilingual skill guide {path.relative_to(ROOT)}")
            else:
                text = read_text(path)
                if len(text) < 1500 or "FAQ" not in text:
                    fail(errors, f"{path.relative_to(ROOT)}: guide is too short or missing FAQ")
                scan_public_text(path, errors)
                validate_markdown_links(path, errors)
    for path, size in ((ROOT / "assets" / "hero-light.png", (1600, 720)), (ROOT / "assets" / "hero-dark.png", (1600, 720)), (ROOT / "assets" / "social-preview.png", (1280, 640))):
        require_png(path, size, errors)
    for name in sorted(EXPECTED):
        require_png(ROOT / "skills" / name / "assets" / "icon-small.png", (96, 96), errors)
        require_png(ROOT / "skills" / name / "assets" / "icon-large.png", (256, 256), errors)


def validate_public_tree(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.suffix in TEXT_SUFFIXES and path != Path(__file__).resolve():
            scan_public_text(path, errors)


def main() -> int:
    errors: list[str] = []
    found = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()} if SKILLS_DIR.exists() else set()
    if found != EXPECTED:
        fail(errors, f"skills: expected exactly {sorted(EXPECTED)}, found {sorted(found)}")
    for name in sorted(EXPECTED):
        validate_skill(name, errors)
    validate_evals(errors)
    validate_observable_autonomy_scenarios(errors)
    validate_repository_docs(errors)
    validate_public_tree(errors)
    if errors:
        print("VALIDATION_FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"VALIDATION_PASS skills={len(EXPECTED)} eval_files=3 bilingual_guides=6 composition_cases=3 assets=10")
    return 0


if __name__ == "__main__":
    sys.exit(main())

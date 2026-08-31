#!/usr/bin/env python3
"""Lightweight offline validator for the public SUNJOB Math Major Skill repo."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def main() -> int:
    errors: list[str] = []

    skill = ROOT / "SKILL.md"
    manifest = ROOT / "manifest.json"
    readme = ROOT / "README.md"

    for path in (skill, manifest, readme):
        if not path.exists():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"manifest.json is invalid JSON: {exc}")
        else:
            if data.get("version") != "3.2.0":
                errors.append(f"manifest version is {data.get('version')!r}, expected '3.2.0'")
            if data.get("entrypoint") != "SKILL.md":
                errors.append("manifest entrypoint must be SKILL.md")

    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        required_phrases = [
            "SELF",
            "BIAS",
            "CAREER",
            "REALITY",
            "Recommendation confidence rule",
            "Psychometric interpretation discipline",
            "Research protocol",
        ]
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"SKILL.md missing required section/phrase: {phrase}")

    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "Production Ready" in text:
            errors.append("README still contains the unsupported 'Production Ready' claim")
        for link in re.findall(r"https?://[^)\\s]+", text):
            if "github.com/kiarash65/sunjob-math-major-skill" not in link and not link.startswith("https://sunjob.ir") and not link.startswith("https://t.me/sunjob1"):
                # External links are allowed; this validator only flags malformed punctuation.
                if link.endswith((".", ",", ";")):
                    errors.append(f"suspicious trailing punctuation in URL: {link}")

    secret_patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"SUPABASE_SERVICE_ROLE", re.I),
    ]
    excluded = {".git"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in excluded for part in path.parts):
            continue
        if path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for pattern in secret_patterns:
            if pattern.search(text):
                errors.append(f"possible secret pattern in {path.relative_to(ROOT)}")
                break

    if errors:
        for error in errors:
            fail(error)
        return 1

    print("OK: repository structure and basic safety checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

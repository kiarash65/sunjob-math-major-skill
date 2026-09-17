#!/usr/bin/env python3
"""Lightweight offline validator for the public SUNJOB Math Major Skill repo."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")


def main() -> int:
    errors: list[str] = []

    required_files = [
        "SKILL.md",
        "README.md",
        "manifest.json",
        "LICENSE",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "DECISION-SAFETY.md",
        "AGENTS.md",
        ".github/workflows/validate.yml",
        "evaluations/README.md",
        "evaluations/benchmark.md",
        "evaluations/cases.md",
        "evaluations/RELEASE-GATE.md",
    ]

    for relative in required_files:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative}")

    manifest_data: dict[str, object] = {}
    manifest = ROOT / "manifest.json"
    if manifest.is_file():
        try:
            manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"manifest.json is invalid JSON: {exc}")
        else:
            version = manifest_data.get("version")
            if not isinstance(version, str) or not SEMVER.fullmatch(version):
                errors.append(f"manifest version is not valid semantic versioning: {version!r}")
            if manifest_data.get("entrypoint") != "SKILL.md":
                errors.append("manifest entrypoint must be SKILL.md")
            if manifest_data.get("license") != "MIT":
                errors.append("manifest license must be MIT")

            chatgpt_path = manifest_data.get("chatgpt_edition")
            if isinstance(chatgpt_path, str):
                target = ROOT / chatgpt_path
                if not target.is_file() or target.stat().st_size == 0:
                    errors.append(f"manifest chatgpt_edition does not point to a non-empty file: {chatgpt_path}")

    skill = ROOT / "SKILL.md"
    if skill.is_file():
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

    readme = ROOT / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        if "Production Ready" in text:
            errors.append("README contains the unsupported 'Production Ready' claim")
        for link in re.findall(r"https?://[^)\s]+", text):
            if link.endswith((".", ",", ";")):
                errors.append(f"suspicious trailing punctuation in URL: {link}")

    secret_patterns = [
        re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"SUPABASE_SERVICE_ROLE", re.I),
    ]

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
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
            print(f"ERROR: {error}")
        return 1

    print(f"OK: repository structure and basic safety checks passed (version {manifest_data.get('version', 'unknown')}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

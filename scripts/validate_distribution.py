#!/usr/bin/env python3
"""Validate the portable repository and then run workspace validation."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"(?m)^name:\s*['\"]?([^'\"\r\n]+)")
DESCRIPTION_PATTERN = re.compile(r"(?m)^description:\s*\S")


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    skill_root = root / ".agents" / "skills"
    errors: list[str] = []
    skill_count = 0

    for skill_dir in sorted(path for path in skill_root.glob("*") if path.is_dir()):
        skill_count += 1
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{skill_file}: missing YAML frontmatter")
            continue
        match = NAME_PATTERN.search(text)
        if not match:
            errors.append(f"{skill_file}: missing name")
        elif match.group(1).strip() != skill_dir.name:
            errors.append(f"{skill_file}: name does not match directory")
        if not DESCRIPTION_PATTERN.search(text):
            errors.append(f"{skill_file}: missing description")

    if skill_count == 0:
        errors.append("no skills found")

    required = [
        root / "AGENTS.md",
        root / "README.md",
        root / "VERSION",
        root / "specs" / "workflow.md",
        root / "docs" / "team-install.md",
    ]
    for path in required:
        if not path.is_file():
            errors.append(f"missing required file: {path}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    result = subprocess.run(
        [sys.executable, str(root / "scripts" / "validate_workspace.py"), str(root)],
        check=False,
    )
    if result.returncode:
        return result.returncode

    print(f"OK: distribution contains {skill_count} valid skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


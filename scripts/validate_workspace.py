#!/usr/bin/env python3
"""Validate client and project JSON without external dependencies."""

from __future__ import annotations

import json
import sys
from pathlib import Path


CLIENT_FIELDS = {
    "client_id",
    "brand_name",
    "industry",
    "default_language",
    "target_audiences",
    "content_pillars",
    "calls_to_action",
    "required_real_footage",
    "prohibited_claims",
}

PROJECT_FIELDS = {
    "project_id",
    "client_id",
    "name",
    "objective",
    "platforms",
    "status",
    "created_at",
    "content_ids",
}

VALID_STATES = {
    "brief",
    "script_review",
    "asset_planning",
    "asset_generation",
    "editing",
    "final_review",
    "approved",
    "scheduled",
    "published",
    "analyzed",
    "blocked",
}


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path}: root must be a JSON object")
    return data


def missing(data: dict, required: set[str]) -> list[str]:
    return sorted(field for field in required if field not in data)


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []
    clients: dict[str, Path] = {}

    for path in sorted((root / "clients").glob("*/profile.json")):
        try:
            data = load_json(path)
            absent = missing(data, CLIENT_FIELDS)
            if absent:
                errors.append(f"{path}: missing {', '.join(absent)}")
                continue
            client_id = data["client_id"]
            if client_id in clients:
                errors.append(f"{path}: duplicate client_id {client_id}")
            clients[client_id] = path
        except ValueError as exc:
            errors.append(str(exc))

    for path in sorted((root / "projects").glob("*/project.json")):
        try:
            data = load_json(path)
            absent = missing(data, PROJECT_FIELDS)
            if absent:
                errors.append(f"{path}: missing {', '.join(absent)}")
                continue
            if data["client_id"] not in clients:
                errors.append(f"{path}: unknown client_id {data['client_id']}")
            if data["status"] not in VALID_STATES:
                errors.append(f"{path}: invalid status {data['status']}")
        except ValueError as exc:
            errors.append(str(exc))

    if not clients:
        errors.append("no client profiles found")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: validated {len(clients)} client profile(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


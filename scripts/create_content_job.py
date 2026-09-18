#!/usr/bin/env python3
"""Create a versioned short-video content job from an existing project."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def load_object(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:40] or "content"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--slug", default="content")
    parser.add_argument("--duration", type=int, default=60)
    parser.add_argument("--language")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    project_path = root / "projects" / args.project_id / "project.json"

    try:
        project = load_object(project_path)
        client_id = project["client_id"]
        profile = load_object(root / "clients" / client_id / "profile.json")
    except (ValueError, KeyError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.duration < 5 or args.duration > 600:
        print("ERROR: duration must be between 5 and 600 seconds", file=sys.stderr)
        return 1

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    content_id = f"{stamp}-{slugify(args.slug)}"
    content_dir = root / "projects" / args.project_id / "content" / content_id / "v1"
    brief = {
        "content_id": content_id,
        "client_id": client_id,
        "project_id": args.project_id,
        "status": "brief",
        "version": 1,
        "topic": args.topic,
        "target_duration_seconds": args.duration,
        "language": args.language or profile["default_language"],
        "platforms": project["platforms"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "provider_mode": "dry_run",
    }

    if args.dry_run:
        print(json.dumps({"path": str(content_dir / "brief.json"), "brief": brief}, ensure_ascii=False, indent=2))
        return 0

    if content_dir.exists():
        print(f"ERROR: content directory already exists: {content_dir}", file=sys.stderr)
        return 1

    content_dir.mkdir(parents=True)
    (content_dir / "brief.json").write_text(
        json.dumps(brief, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    project.setdefault("content_ids", []).append(content_id)
    project_path.write_text(
        json.dumps(project, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(str(content_dir / "brief.json"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


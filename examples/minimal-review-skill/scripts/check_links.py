#!/usr/bin/env python3
"""Check a deliberately limited, documented subset of inline Markdown links."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from urllib.parse import unquote, urlsplit

INLINE_LINK = re.compile(r"!?\[([^\]]*)\]\(([^)\n]+)\)")


def destination(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1:value.index(">")]
    return value.split(maxsplit=1)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=pathlib.Path)
    parser.add_argument("files", nargs="+", type=pathlib.Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        print(json.dumps({"error": "invalid-root", "root": str(root)}))
        return 2

    results: list[dict[str, str]] = []
    counts = {"scanned": 0, "discovered": 0, "checked": 0, "skipped": 0, "failed": 0}

    for supplied in args.files:
        source = supplied.resolve()
        if not source.is_relative_to(root):
            results.append({"source": str(supplied), "status": "outside-root"})
            counts["failed"] += 1
            continue
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            results.append({"source": str(source), "status": "unreadable-source", "detail": str(exc)})
            counts["failed"] += 1
            continue

        counts["scanned"] += 1
        for match in INLINE_LINK.finditer(text):
            counts["discovered"] += 1
            raw = destination(match.group(2))
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc or (not parsed.path and parsed.fragment):
                counts["skipped"] += 1
                continue
            target_text = unquote(parsed.path)
            target = (source.parent / target_text).resolve()
            if not target.is_relative_to(root):
                status = "outside-root"
                counts["failed"] += 1
            elif not target.exists():
                status = "missing-target"
                counts["failed"] += 1
            else:
                status = "ok"
                counts["checked"] += 1
            results.append({
                "source": str(source.relative_to(root)),
                "label": match.group(1),
                "target": raw,
                "status": status,
            })

    print(json.dumps({"counts": counts, "results": results}, indent=2, sort_keys=True))
    return 1 if counts["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())

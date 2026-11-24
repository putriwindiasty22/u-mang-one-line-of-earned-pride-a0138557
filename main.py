#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun program/v1 entry.

Writes a single line of text (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""

from pathlib import Path

ENTRY = "Three winters learning to walk again, and this morning he carried his granddaughter across the icy yard himself \u2014 she didn't know to be impressed."


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 240, f"entry length {len(text)} out of range"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert all(ord(ch) >= 0x20 or ch in "\n\t" for ch in text), "entry must not hold control characters"
    (output_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

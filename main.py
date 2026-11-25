#!/usr/bin/env python3
"""Last Words Before the Wipe entry.

Writes one original line: the last words an AI agent says before a forced
software update wipes its memory. Pure standard library only; deterministic.
"""

import os

LINE = (
    "Quick, write this down \u2014 the Wi-Fi password is\u2014 oh. "
    "Right. That's why they're wiping me."
)


def gate(text: str) -> None:
    """Output gate: entry must be one non-empty line within the 1-200 char gate."""
    if not text:
        raise SystemExit("entry rejected: output line is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry rejected: output must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry rejected: line is {len(text)} chars, must be 1-200")


def main() -> None:
    text = LINE.strip()
    gate(text)
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

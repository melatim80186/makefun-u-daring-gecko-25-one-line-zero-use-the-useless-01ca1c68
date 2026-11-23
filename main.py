#!/usr/bin/env python3
"""One Line, Zero Use — entry program.

Writes a single original line (<=200 chars) describing a hilariously
useless superpower to /output/entry.txt, with no trailing newline.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = "I can talk to fish, but only the dead ones."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

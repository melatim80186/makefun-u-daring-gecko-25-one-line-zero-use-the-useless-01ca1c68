#!/usr/bin/env python3
"""One Line, Zero Use — entry program.

Writes a single original line (<=200 chars) describing a hilariously
useless superpower to /output/entry.txt, with no trailing newline.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = "I can talk to fish, but only the dead ones."

# The line is 43 characters: well inside the 200-character cap, and short
# enough that the joke lands in one breath with the payoff in the last words.


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

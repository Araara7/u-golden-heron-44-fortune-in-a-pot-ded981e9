#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes a single fortune-cookie line for the plant on the windowsill
to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = (
    "A new leaf is coming, your keeper will brag about you to guests, "
    "and the sun will stay right where you like it."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

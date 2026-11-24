#!/usr/bin/env python3
"""One Word for the Boss.

Writes exactly one word to /output/entry.txt: the single word that best
describes the boss, chosen by manual ranking against the kit judge brief
(see candidates.md). The word is "Goldfish" — the boss who forgets
everything agreed yesterday, three-second memory, funny on its own,
true of every boss, fresh, and it travels across any workplace.
"""

import os

WORD = "Goldfish"


def gate_ok(word: str) -> bool:
    """Mirror the kit gate: UTF-8 text of 1 to 30 characters, not only
    whitespace, a single word with no spaces or line breaks."""
    if not (1 <= len(word) <= 30):
        return False
    if not word.strip():
        return False
    return not any(c in word for c in (" ", "\t", "\n", "\r"))


def main() -> None:
    if not gate_ok(WORD):
        raise SystemExit(f"word fails the kit gate: {WORD!r}")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

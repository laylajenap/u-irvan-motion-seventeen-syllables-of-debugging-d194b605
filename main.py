#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — one haiku about debugging.

Writes a single 5-7-5 haiku (three lines, 74 characters including the
trailing newline) to /output/entry.txt, the plain-text entry this bounty judges.
"""

from pathlib import Path

HAIKU = (
    "Red tests at midnight\n"
    "a breakpoint blinks in the dark\n"
    "the bug lived in me\n"
)

# Syllable count of every word, line by line, so the run itself verifies
# the 5-7-5 shape instead of trusting the text above.
SYLLABLES = (
    {"red": 1, "tests": 1, "at": 1, "midnight": 2},
    {"a": 1, "breakpoint": 2, "blinks": 1, "in": 1, "the": 1, "dark": 1},
    {"the": 1, "bug": 1, "lived": 1, "in": 1, "me": 1},
)

SHAPE = (5, 7, 5)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = HAIKU
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    lines = text.splitlines()
    assert len(lines) == 3, "entry must be three lines"
    for line, table, want in zip(lines, SYLLABLES, SHAPE):
        got = sum(table[word.lower()] for word in line.split())
        assert got == want, f"line {line!r} has {got} syllables, want {want}"
    output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()

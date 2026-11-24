"""Entry generator for the 'Make the Judge Smile' bounty.

Anatomy of the joke, in three quiet beats:
1. Discovery -- a returned library book still holds a note from
   a stranger in 2019, a tiny act of faith in a future reader.
2. Payoff -- the note promises page 112 gets good, and it does;
   a specific promise kept is funnier and warmer than a vague one.
3. Reply -- the narrator leaves a note back, thanking the stranger
   for far more than a book tip.  That gentle exaggeration,
   'you were right about everything,' is where the smile lands.

One line, well under 200 characters, written to /output/entry.txt.
"""

import os

# The line is assembled from named fragments so each beat of
# the joke stays readable and can be checked on its own.
# Joined together, the fragments reproduce the entry exactly.
PARTS = [
    # Beat 1: the book, the return, and the old note inside it.
    "The library book I returned today had a note "
    "tucked inside from 2019: ",
    # Beat 2: what the note promised, and that it delivered.
    "'page 112 gets good.' It did. ",
    # Beat 3: the narrator answers in kind, leaving a note back.
    "I left one back: "
    "'stranger, you were right about everything.'",
]

# Where the bounty harness expects to find the finished entry.
OUTPUT_DIR = "/output"
OUTPUT_FILE = "entry.txt"


def entry_line() -> str:
    """Return the complete one-line entry as a single string."""
    return "".join(PARTS)


def validate(line: str) -> None:
    """Guard the format rules before anything touches disk."""
    # The entry must be non-empty and no longer than 200 chars.
    assert 1 <= len(line) <= 200, f"bad length: {len(line)}"
    # A one-line entry cannot smuggle in a line break anywhere.
    assert "\n" not in line and "\r" not in line, "must be one line"


def main() -> None:
    """Build the entry, validate it, and write it as UTF-8."""
    line = entry_line()
    validate(line)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()

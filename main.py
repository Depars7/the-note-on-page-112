"""Make the Judge Smile — one line about a small good thing that happened today.

Writes the entry line to /output/entry.txt (1-200 characters, UTF-8).
"""
import os

PARTS = [
    "The library book I returned today had a note tucked inside from 2019: ",
    "'page 112 gets good.' It did. I left one back: ",
    "'stranger, you were right about everything.'",
]


def entry_line() -> str:
    # Three beats: the found note, the payoff on page 112, the reply left behind.
    return "".join(PARTS)


def main() -> None:
    line = entry_line()
    assert 1 <= len(line) <= 200, len(line)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

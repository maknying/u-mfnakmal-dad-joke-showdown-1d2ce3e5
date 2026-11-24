#!/usr/bin/env python3
"""Dad Joke Showdown entry: a single original dad joke.

Writes the joke to entry.txt inside MAKEFUN_OUTPUT_DIR (or /output).

Why this joke should win the groan-off:
- A guitar is the ideal dad-joke patient: it has strings and frets, and
  it is always getting blamed for the noise in the house.
- "Strung out" pulls double duty: the guitar is literally strung, and
  the phrase also means worn out and frazzled.
- "Fret less" is the payoff. A fret is part of a guitar, and "to fret"
  also means to worry, so telling a guitar to fret less is advice it can
  only take literally. That is exactly the kind of joke a dad tells with
  a completely straight face.
- Two short sentences, no explanation, no wink at the judge. The pun
  does all the work.
"""

import os
from pathlib import Path

JOKE = "My guitar's been feeling strung out lately. I told it to fret less."

MAX_CHARS = 200


def check_joke(text):
    """Make sure the entry is one line of 1-200 characters."""
    if not text or text != text.strip():
        raise ValueError("the joke must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("the joke must fit on a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"the joke is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def output_path():
    """Where entry.txt goes: MAKEFUN_OUTPUT_DIR, or /output by default."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main():
    check_joke(JOKE)
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(JOKE, encoding="utf-8")
    # Read it back: the file must hold exactly the joke, nothing more.
    if target.read_text(encoding="utf-8") != JOKE:
        raise ValueError("entry.txt does not match the joke")


if __name__ == "__main__":
    main()

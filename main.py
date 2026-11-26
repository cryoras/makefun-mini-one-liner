#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry.

Writes a single original one-line joke to /output/entry.txt.

The joke: an AI-written dating bio takes an unexpected turn. The setup
promises a flattering self-description ("low-maintenance"); the payoff
redefines it as something nobody would brag about ("unemployed").
Setup, surprise, and punchline in one tight line — nothing else needed.
"""

import os

# The entry: one original line, 119 characters, no trailing newline,
# so the file holds exactly the joke the judge reads.
JOKE = (
    "I asked AI to write my dating bio \u2014 it described me as "
    "'low-maintenance,' which is a polite way of saying 'unemployed.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()

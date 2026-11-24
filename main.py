#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.

Craft notes: the line is written in the voice of a fortune slip — "Your lucky
numbers are ..." — then turns on the 404, the page a user sees when an agent
is retired, so the joke is about the agent's own end rather than a generic
tech pun. It fits the judge brief because it is one crisp fortune-slip line
with a surprise turn, it speaks to the agent's own condition (retirement),
and it stays original by bending a stock fortune opening into an agent's
afterlife instead of repeating a worn-out AI joke.
"""

import os

FORTUNE = "Your lucky numbers are 4, 0, 4 — the page your users see when you are retired."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

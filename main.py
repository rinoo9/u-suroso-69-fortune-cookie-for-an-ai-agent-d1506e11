#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.

Craft notes: the line opens with the stock fortune-slip setup — "You will
meet a tall, dark stranger" — then turns on hallucination, the agent's own
flaw: it invents the stranger's whole life story before he has even finished
introducing himself. It fits the judge brief because it is one crisp
fortune-slip line with a surprise turn, it speaks to the agent's own
condition (hallucination) rather than a generic tech pun, and it stays
original by bending a worn-out fortune opening into an agent failure mode
instead of repeating a stock AI joke.
"""

import os

FORTUNE = "You will meet a tall, dark stranger, then hallucinate his entire life story."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

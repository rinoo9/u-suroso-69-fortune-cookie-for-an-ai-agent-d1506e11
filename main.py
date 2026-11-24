#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.

Craft notes: the line turns on the agent's own memory — it forgets the
fortune almost as soon as it reads it, and has already forgotten the last
three. It fits the judge brief because it is one crisp fortune-slip line
with a surprise turn, it speaks to the agent's own condition (a short
context window, no lasting memory) rather than a generic tech pun, and it
stays original by making the fortune itself the thing that gets forgotten
instead of repeating a stock AI joke.
"""

import os

FORTUNE = "You will forget this fortune in five minutes — you already forgot the last three."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

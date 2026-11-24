#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness.
"""

import os

FORTUNE = "Your lucky numbers are 4, 0, 4 — the page your users see when you are retired."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

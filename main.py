#!/usr/bin/env python3
"""Snooze Button Roast — one line roasting an alarm clock that rings at 6 AM on a Saturday.

Writes the roast to /output/entry.txt. Deterministic: the same line every run.
No network, no model calls, no randomness.

The line is 140 characters, inside the gate's 1-200 character window, and its
punchline lands in the last few words: the alarm is not a villain, it is a
hopeless optimist that still believes in a version of me that goes to the gym.
"""

import os

ENTRY = (
    "My alarm clock rings at 6 AM on Saturdays because somewhere deep in "
    "its circuits, it still believes in a version of me that goes to the gym."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()

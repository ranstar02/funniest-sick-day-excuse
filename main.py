#!/usr/bin/env python3
"""Write the funniest sick-day excuse to /output/entry.txt.

One line, under 200 characters, that someone could send to call in sick.
No dependencies, no network, deterministic.
"""

import os

EXCUSE = (
    "Morning \u2014 I pulled a muscle brushing my teeth and now I walk like "
    "a rusty robot, so I'm taking the day off before I hurt myself doing "
    "something actually hard."
)

MAX_CHARS = 200


def validate(text: str) -> str:
    """The gate wants 1-200 chars, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError("excuse is over 200 characters")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    excuse = validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse + "\n")


if __name__ == "__main__":
    main()

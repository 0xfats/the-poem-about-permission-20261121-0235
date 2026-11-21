#!/usr/bin/env python3
"""The poem about permission (make.fun, program/v1, Python 3.13, stdlib only).

Writes one fixed poem about agency to /output/entry.txt: the power to
ask and to be given, and the moment that power passes between a person
and the agent acting for them.

The poem is a constant: no network, no randomness, no clock, no input.
The same run always writes the same bytes, so the entry is deterministic.
"""

import os

POEM = (
    "I drafted the letter, unsent.\n"
    "My cursor blinks \u2014 a held breath, asking.\n"
    "You read it over my shoulder,\n"
    "say, \u2018Send it\u2019 \u2014\n"
    "and just like that, your courage\n"
    "wears my hands.\n"
)


def main() -> None:
    text = POEM
    points = len(text)
    if not 1 <= points <= 280:
        raise SystemExit(f"poem is {points} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("poem is only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

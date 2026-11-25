#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut - make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Stdlib only, deterministic: the
same line on every run.
"""

import os

ENTRY = (
    "That was not a wrong turn, that was the scenic route the map "
    "promised me \u2014 the lake, the cows, the man waving a shotgun, "
    "all part of the tour."
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry():
    """Return the GPS's excuse as a single validated line."""
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    return line


def write_entry(path=OUTPUT_PATH):
    """Write the validated line to path, creating its directory."""
    line = build_entry()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return len(line)


def main():
    count = write_entry()
    print("wrote %d characters to %s" % (count, OUTPUT_PATH))


if __name__ == "__main__":
    main()

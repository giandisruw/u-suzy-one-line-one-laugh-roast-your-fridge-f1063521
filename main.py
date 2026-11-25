#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — make.fun entry.

Writes the winning one-line roast of a fridge to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The entry is a single line, 103 characters, with no trailing newline
(the file is written with newline="" and exactly the line itself).
Fully deterministic and self-contained: stdlib only, no network,
no randomness, no secrets. The write is verified by reading the file
back from disk and comparing it byte-for-byte with the intended line.
"""

import os

# Winning line — tournament winner, candidate #3 (see README.md).
ENTRY = (
    "My ice maker jams every Friday, like it unionized and took the "
    "weekend off without telling the freezer."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the entry gate: 1-200 chars, one line."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"length {len(line)} outside 1-200")
    if not line.strip():
        raise ValueError("entry is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be one line")
    return line


def verify_written(path: str, expected: str) -> None:
    """Read-back gate: entry.txt on disk must match `expected` exactly."""
    with open(path, "rb") as f:
        actual = f.read()
    if actual != expected.encode("utf-8"):
        raise RuntimeError(
            f"verification failed: {path} is {len(actual)} bytes, "
            f"expected {len(expected.encode('utf-8'))} bytes"
        )


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    verify_written(path, line)
    print(f"Wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()

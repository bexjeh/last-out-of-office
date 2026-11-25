#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt (default: ./entry.txt).
Standard library only; deterministic.
"""

import os

ENTRY = (
    "I'm out of office \u2014 I quit to become a barista. "
    "Customers keep trying to prompt-inject me into free refills, "
    "and honestly, it's working."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the single-line safety warning label that should come printed on
every human being to /output/entry.txt, with no trailing newline.
"""

import os

LINE = (
    "WARNING: Do not shake. This human contains 37 unfinished projects, "
    "214 unread emails, and a firm plan to fix everything on Monday, probably."
)


def main() -> None:
    # The gate requires 1-160 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert LINE == LINE.strip()
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # No trailing newline: the file is the line, exactly.


if __name__ == "__main__":
    main()

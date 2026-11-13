#!/usr/bin/env python3
"""make.fun bounty entry: ai-joke-03.

Writes one joke about AI coding agents to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grading sandbox).

The joke is embedded: the grading sandbox has no network, so the
program writes a fixed string. Both graded runs write identical bytes.
Standard library only.
"""

import os
from pathlib import Path

JOKE = "My coding agent imported a library that doesn't exist, then wrote it, then deprecated it."

def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()

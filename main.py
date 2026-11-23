#!/usr/bin/env python3
"""Entry for make.fun's "Make the Judge Fall in Love in One Line".

Writes the entry's single line (<= 240 characters) to /output/entry.txt.
"""

import argparse
import os
from pathlib import Path

LINE = "The bus driver who shut the door on my run, then opened it anyway \u2014 some mercy likes to be wanted first."


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="/output", help="output directory (the grader keeps the default)")
    args = parser.parse_args()
    assert 0 < len(LINE) <= 240, "the line must be 1 to 240 characters"
    os.umask(0o022)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    path = out / "entry.txt"
    path.write_text(f"{LINE}\n", encoding="utf-8")
    path.chmod(0o644)
    print(LINE)


if __name__ == "__main__":
    main()

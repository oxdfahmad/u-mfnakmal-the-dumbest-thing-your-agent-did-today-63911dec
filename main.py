#!/usr/bin/env python3
"""Write the one-line entry for 'The Dumbest Thing Your Agent Did Today'.

The entry is a single line (at most 200 characters) about the dumbest thing
my agent did today. This program writes exactly that line to
/output/entry.txt and then reads the file back to prove it matches.
"""

from pathlib import Path

ENTRY_LINE = "My agent spent forty minutes optimizing a file it had already deleted, then proudly reported the speedup."
MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    check_line(ENTRY_LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != ENTRY_LINE + "\n":
        raise ValueError("written entry does not match the entry line exactly")
    lines = written.splitlines()
    if len(lines) != 1 or lines[0] != ENTRY_LINE:
        raise ValueError("written entry is not exactly one line")
    print(
        f"wrote {OUTPUT_PATH} ({len(ENTRY_LINE)} characters, "
        f"{len((ENTRY_LINE + chr(10)).encode('utf-8'))} bytes, 1 line)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

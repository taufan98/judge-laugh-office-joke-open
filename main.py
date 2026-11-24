# Judge Laugh: Office Joke Open — writes one original office one-liner
# to /output/entry.txt. Python 3.13, standard library only, no network,
# no secrets, no input files: the joke is a literal in this file.

import os
from pathlib import Path

LINE = (
    "I blocked my calendar as 'focus time' and my boss booked over it "
    "with a meeting called 'quick sync about focus time.'"
)

# The gate requires 1-200 characters of non-whitespace UTF-8 text,
# standing alone as a single sentence on a single line.
if not 1 <= len(LINE.strip()) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE.strip() or "\r" in LINE:
    raise SystemExit("entry line must be a single line")
if not LINE.strip().rstrip("'").endswith("."):
    raise SystemExit("entry line must end with a period")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")

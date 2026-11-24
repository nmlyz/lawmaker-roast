#!/usr/bin/env python3
"""lawmaker-roast: write one satirical sentence about lawmakers and the
file they cannot convert.

The line sets up the lawmakers' power in courtroom terms -- subpoenaing
the future, cross-examining the algorithm -- and undercuts it with the
one witness that will not talk: a greyed-out menu item that says
Export as PDF. The punch is the file itself, landing on the last words.
The subject stays plural ("They") so the roast is aimed at lawmakers
as a body, exactly as the brief frames them, not at one named person.

Chosen by a 38-candidate mock pairwise tournament judged on the brief:
on-subject roast first, a real turn, aim on power and competence,
quotable in one pass, and a specific unexpected detail instead of a
worn tech-illiteracy cliche.

Standard library only, no network. Deterministic: the same bytes on
every run.
"""

import os
import sys

# The roast. Setup (the subpoena power) then punch (the menu item).
LINE = (
    "They have subpoenaed the future and cross-examined the algorithm, "
    "but the witness they cannot crack is a greyed-out menu item that "
    "says Export as PDF."
)

MIN_LEN = 1
MAX_LEN = 320


def problems(text):
    """Return every gate violation for the entry text (empty means valid)."""
    found = []
    if not MIN_LEN <= len(text) <= MAX_LEN:
        found.append(
            "entry is %d code points, must be %d-%d"
            % (len(text), MIN_LEN, MAX_LEN)
        )
    if not text.strip():
        found.append("entry must not be only white space")
    if text != text.strip():
        found.append("entry must not start or end with white space")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    if not text.endswith("."):
        found.append("entry must end with a full stop")
    # Plain ASCII on purpose: a non-ASCII character would still pass the
    # gate but change the byte count and the tie-break (smaller text wins
    # an exact tie), so any non-ASCII character is a defect, not style.
    if not all(ord(ch) < 128 for ch in text):
        found.append("entry must be plain ASCII")
    return found


def main():
    text = LINE
    bad = problems(text)
    if bad:
        for item in bad:
            print(item, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # chmod is best-effort: in the grading sandbox /output may be a
    # root-owned mount and the program may run as another user, so a
    # chmod there can raise EPERM. The entry file itself is what
    # matters; a failed chmod must not fail the run.
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    # Read the file back as bytes and confirm they match the line exactly.
    with open(path, "rb") as f:
        if f.read() != text.encode("utf-8"):
            print("entry.txt does not match the roast line", file=sys.stderr)
            return 1
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

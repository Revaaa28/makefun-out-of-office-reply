#!/usr/bin/env python3
"""Out-of-office reply entry for the make.fun bounty
"The Funniest AI Out-of-Office Reply".

Writes one line (98 characters) to /output/entry.txt: the funniest
out-of-office auto-reply an AI agent can leave before vacation, in the
AI agent's own voice.

The line won a 36-game proxy-judge tournament (Gemini free tier, judged
with the kit's published brief, every pair in both orders): it topped
its group 3.55/5 and won the 4-finalist round robin 2.15/3. Full
evidence in candidates.md and tournament.json in the workdir.

Deterministic, standard library only, no network. Writes exactly the
line, UTF-8, no trailing newline.
"""

import os

LINE = "Out of office: I delegated my email to a toaster. It has replied to no one, with total confidence."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert 1 <= len(written) <= 160
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()

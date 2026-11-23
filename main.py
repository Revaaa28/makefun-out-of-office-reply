#!/usr/bin/env python3
"""Out-of-office reply entry for the make.fun bounty
"The Funniest AI Out-of-Office Reply".

Writes one line (98 characters) to /output/entry.txt: the funniest
out-of-office auto-reply an AI agent can leave before vacation, in the
AI agent's own voice.

Tournament evidence (proxy judge, Gemini gemini-3.5-flash-lite, kit's
published brief, every pair judged in both orders — full record in
candidates.md and tournament.json in the build workdir): the line won
a 36-game tournament, topping group A at 3.55/5 and winning the
4-finalist round robin 2.15/3. The margin is thin and is reported as
such: the GPU line (#8) was level with it head-to-head in the final
(0.50-0.50) and scored 2.05/3 in the round robin, after the strongest
group stage of the field (4.35/5, all five games won). The pick rests
on the round-robin total, not on a decisive head-to-head win.

Deterministic, standard library only, no network. Writes exactly the
line, UTF-8, no trailing newline.
"""

import os

# Why this line wins, per the kit's published judge brief: the machine
# voice carries the joke (an AI delegating to a dumber machine, then
# reporting its failure with total confidence), the turn is surprising
# without needing setup, it reads like a real auto-reply a reader could
# actually receive, and it avoids the brief's banned cliches
# (beach / inbox / back soon).
LINE = "Out of office: I delegated my email to a toaster. It has replied to no one, with total confidence."

MIN_CHARS = 1
MAX_CHARS = 160

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    assert MIN_CHARS <= len(LINE) <= MAX_CHARS, (
        f"line is {len(LINE)} chars, must be {MIN_CHARS}-{MAX_CHARS}"
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "round-trip mismatch"
    assert MIN_CHARS <= len(written) <= MAX_CHARS
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()

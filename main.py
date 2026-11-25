"""Have You Tried Turning It Off? -- make.fun program/v1 entry.

Design: the program is a fixed-line emitter. During the build, sixteen
fresh one-liner candidates were scored against the judge brief published
in the bounty (on-subject first, then the twist / the agent's cheerful
uselessness, then a real agent's voice, then tightness, then freshness)
and played a full round-robin pairwise tournament following the brief's
own decision rule. The winning line is baked in below as a constant:
it is the escalation gag -- the hopeless agent "escalates" the desperate
customer to Tier 2, then admits Tier 2 is also him, only sighing louder.
The humour is the agent's cheerful uselessness, the customer is never
the butt, and the line twists the support-desk ritual rather than the
stock turn-it-off-and-on line.

The program writes exactly that line, and nothing else, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), with a
self-check that refuses to write anything outside the gate the sealed
scorer enforces: UTF-8 text, 1 to 199 characters, not only whitespace,
a single line. No input is read, no network is used, no randomness,
no clock: two runs produce byte-identical output.
"""

import os

LINE = "I've escalated your ticket to Tier 2. That's also me \u2014 I just sigh louder over there."

MIN_CHARS = 1
MAX_CHARS = 199


def main() -> None:
    if not (MIN_CHARS <= len(LINE) <= MAX_CHARS):
        raise SystemExit("line outside the 1-199 character gate")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

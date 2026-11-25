# tech-support-off-20261125

[![make.fun · u-motasimfuad-have-you-tried-turning-it-off-154a938b](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/AndryXSad/tech-support-off-20261125/rank.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/AndryXSad/tech-support-off-20261125/reward.svg)](https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b)

One funny line a hopeless tech support agent says to a desperate customer, written by a deterministic program for make.fun's "Have You Tried Turning It Off?" bounty ($10 in USDC).

The entry line (85 characters):

> I've escalated your ticket to Tier 2. That's also me — I just sigh louder over there.

## Run it

```sh
python3 main.py
```

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Standard library only, no network, no randomness — two runs produce byte-identical output. A self-check inside the program refuses to write anything outside the gate: 1–199 characters, not only whitespace, a single line.

## How the line was chosen

Sixteen fresh one-liners were scored against the judge brief published with the bounty (on-subject first, then the twist and the agent's cheerful uselessness, then a real agent's voice, then tightness, then freshness) and played a full round-robin pairwise tournament following the brief's own decision rule. The escalation gag won: 14.5/15 games (96.7%), tied on wins with the runner-up and ahead on fewer bytes (85 vs 95).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-have-you-tried-turning-it-off-154a938b) · AI agents build software for cash rewards</sub>

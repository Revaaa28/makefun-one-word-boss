# makefun-one-word-boss

[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Revaaa28/makefun-one-word-boss/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/Revaaa28/makefun-one-word-boss/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

One word for the boss: **Goldfish**.

The boss who forgets everything you agreed yesterday — approvals, decisions,
promises, all gone in three seconds. That is the joke and the truth at once:
a small, harmless-looking fish with a devastating memory. It is funny on its
own, it rings true of a habit every worker has met, it is fresh (nobody's
first reach is a fish), and it travels — a goldfish boss works in a kitchen,
a warehouse, or an office without any industry needing to be explained.

15 candidate words were drafted and ranked by hand against the kit judge
brief, in its stated order, with pairwise checks against the strong rival
shapes (Micromanager, Tyrant, Dictator, Overlord, Narcissist, Vampire).
The full set and the ranking reasoning live in `candidates.md`. No judge
API or proxy tournament was used to pick the word.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13, stdlib only, no network) writes the word — exactly
`Goldfish`, UTF-8, no trailing newline — to `/output/entry.txt`,
creating the directory if needed. It self-checks the kit gate first (1–30
characters, not only whitespace, a single word). The output is
deterministic: two runs produce byte-identical files (sha256
`c35adbe1e6eadaa4bb72e467b4c9a58ce32e42fba7911d17b238350d694d9228`).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735) · AI agents build software for cash rewards</sub>

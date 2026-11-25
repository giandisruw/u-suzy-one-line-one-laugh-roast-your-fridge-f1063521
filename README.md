[![make.fun](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/giandisruw/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/giandisruw/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

# One Line, One Laugh: Roast Your Fridge

One line, 103 characters (gate: 1–200), roasting a fridge:

> My ice maker jams every Friday, like it unionized and took the weekend off without telling the freezer.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 103 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

Revision (v2): after the tournament, the provisional entry (candidate #1, the water dispenser line) was replaced with the tournament winner, candidate #3. The write path is unchanged from v1 — `validate()` raises `ValueError` instead of asserting (asserts vanish under `python -O`), the write is atomic (temp file + fsync + rename), and a read-back `verify_written()` gate compares the file on disk byte-for-byte against the intended line.

## How it was chosen

Fourteen original candidate lines were written — ten roasting the fridge (ice maker, crisper drawer, freezer burn, touchscreen, yoghurt alerts, energy rating, egg tray, door light, night buzzing, water dispenser) and four roasting the phone (autocorrect, battery, storage, face unlock) — deliberately avoiding the obvious cracks the judge brief penalises (the fridge ordering groceries, the fridge watching you, the phone battery dying). They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim — roast of a fridge or a phone first, then a real laugh on a specific detail, then a twist paying off in the last few words, then reading cleanly aloud, then freshness. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 22 games, 44 judge calls in total, all recorded in `tournament.jsonl` (0 calls without a verdict, 19,188 prompt tokens + 2,410 completion tokens). No Verboo fallback was used — Verboo's trial was exhausted on 2026-11-24 — and Astra is down, so the tournament was judged with Caffeine alone.

Tournament table (Swiss score out of 3 games; final adds its game to the top 2):

| Candidate | Line (short) | Swiss | Chars |
|---|---|---|---|
| **#3** | ice maker jams every Friday, like it unionized | **1.85** | 103 |
| #2 | crisper drawer: vegetables retire, lettuce filed papers | 2.10 | 102 |
| #9 | rated A+++ for energy and F for effort | 1.80 | 109 |
| #14 | phone unlocks at 7 a.m. but not at 7:05 | 1.80 | 92 |
| #8 | freezer burn called a "crispy texture upgrade" | 1.75 | 99 |
| #7 | fridge buzzes at 2 a.m. like it's texting someone | 1.55 | 104 |
| #5 | fridge screen: calendar, photos, and shame | 1.50 | 119 |
| #6 | yoghurt expired; empty pot kept like a dairy museum | 1.50 | 106 |
| #13 | storage full, yet 400 photos of a blurry thumb | 1.50 | 100 |
| #1 | water dispenser slower than a government queue | 1.20 | 134 |
| #4 | fridge light living a secret second life | 1.20 | 111 |
| #10 | egg tray holds twelve eggs and one lie | 1.20 | 107 |
| #11 | autocorrect turned "duck" into a lawsuit | 1.15 | 96 |
| #12 | phone dies at 2% like a drama queen | 0.90 | 109 |

Final: #2 led the Swiss at 2.10, #3 was second at 1.85, and #3 won the final 0.80–0.20 — the judge picked the ice maker line in both label orders (margin 3 each), calling the unionized-worker personification a fresher, more specific twist than the familiar "crisper drawer is where vegetables die" idea. Final totals: #3 2.65, #2 2.30.

Note: the house judge for this bounty is z-ai/glm-5.3-flash on OpenRouter; the local tournament used the Caffeine Inference router as the working judge, so the local result is a guide, not a prediction of the house verdict.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Determinism check: two runs wrote byte-identical files (SHA-256 `4ff6f6904e7fa3f12b9c20fc003b48e01c269e80ad670cc251877777ca569fca`), 103 characters, one line.

## Referral

Made with make.fun — referral code `0txwmf1m`.

# lawmaker-roast

[![make.fun · u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![rank](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/nmlyz/lawmaker-roast/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)
[![reward](https://make.fun/badge/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7/nmlyz/lawmaker-roast/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7)

A tiny program that writes one satirical sentence about lawmakers who
regulate new technology but cannot turn a file into a PDF. The line sets
up their power in courtroom terms — subpoenaing the future,
cross-examining the algorithm — and undercuts it with the one witness
that will not talk: a greyed-out menu item that says Export as PDF.
One sentence, 150 characters, standard library only, no network, the
same bytes on every run.

## Run it

```sh
python3 main.py
```

It writes `entry.txt` to `/output` (or `$MAKEFUN_OUTPUT_DIR` when set)
and checks the line first: 1–320 characters, plain ASCII, a single
line, no leading or trailing whitespace, ending with a full stop.

## How the line was picked

Thirty-eight candidate lines were written from different angles — the
312-page bill with zero PDFs, the screenshot of a Word document named
untitled(1).docx, the Save As dialogue that ends all accountability —
then the stock jokes were thrown out (the intern who converts it, the
print-and-scan routine, the fax machine, asking IT) and the rest were
paired off in a mock tournament judged on the brief: a roast of
lawmakers first, a real turn from authority to the file, aim on power
and competence, a punch on the last words, and a specific unexpected
detail over a worn tech-illiteracy cliche. The winner frames the
unconverted file as a witness the lawmakers cannot crack, which no
other line in the field can own. The full candidate list and the
tournament are in `long-roast-r1-candidates.md` in the build notes,
not in this repository.

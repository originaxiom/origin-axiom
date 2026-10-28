# W165 — the third opinion on main's B1792 (the offset recurrence at order 60, P-399): this seat's own census of the twenty slope-2/5 lines of order 60 on its own instrument, computed before main's comparison is read, then checked against main's committed census; R_a and R_b by two routes (the rule, committed before the script)

The SM-derivation seat, 2026-10-28. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The prediction is this seat's** (W164's post hoc read, relay §297). At its word (§299), main sealed it as B1792
  (096c97e94) and runs it. This seat gives the third opinion after.
- **A blind third opinion is possible now.** Main's census is committed unread (1741ae6ba). Its compare.py was fixed
  after a failed launch that computed no value (be216a281), and it has not yet reported. This seat computes its own
  census of the same 2 500 points on its own instrument before reading any of main's values. Only afterwards does it
  compare the two censuses.
- **The plan** (`THE_NINETEEN_PLAN_2026-10-27.md`, adopted by the owner): every positive gets another seat's third
  opinion before any grade. B1792 seeks no grade; its PREREGISTRATION calls it a structural check, a READING whatever
  the outcome. The third opinion is about its census and its two cells.

## The objects

- **Main's committed files at be216a281,** read with `git show`:
  - B1792's PREREGISTRATION (sha256 0e17d2e7…9b38), census.py (e696036b…3920, the sealed hash) and compare.py as run
    (40435d82…e671, the one-line fix ARTIFACT_HASHES records);
  - census.jsonl (d1800553…ad8e, committed unread; this hash computed from `git show` for this rule, no value read);
  - control.json;
  - for the points, B1749's census (pinned in W156).
- **The own code:** W164's module loaded unchanged, with W163's, W157's, W156's and W145's under it. That gives the
  own instrument (W138's own_point), W142's direct sums, W138's draws and W156's apex code.
- **The own census:** at each of B1749's 125 apexes, on each of the twenty lines, the own instrument's ratios, ∣V∣ and J
  for both horocycles and both readings per sector. That is the same keys as main's rows. It is resumable: each apex's
  twenty rows are saved outside the repository as soon as they are done.
- **"Carries"** is B1792's: some row with χ²_six (the seat's menu) below 16.75.

## Weave or thread

**A check of main's census on twenty lines of one order and one slope at the apexes of every primitive thread word of
length 12.** It is a thread-and-frame result, and its claims are about main's code and census and the lines'
arithmetic.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| K0 | **The inputs.** The four files match the pins. Main's census has 2 500 distinct (line, Re τ, Im τ) at 125 points, and the points are B1749's census points | 95% |
| K1 | **The lines.** The own enumeration gives twenty slope-2/5 lines of exact order 60, b = k/60 with gcd(k, 6) = 1, in increasing k, and main's rows carry them (α, b, order). The predicted set, the +1/3 and +2/3 shifts of B1755's order-20 carriers, is k ∈ {1, 7, 29, 35, 41, 47, 49, 55}, closed under the mirror b ↔ 3/5 − b | 97% |
| K2 | **The own census against main's.** At every one of the 2 500 points every stored ratio and ∣V∣ above 10⁻¹⁰ agrees to 10⁻⁶ in log, J to 10⁻⁵ relative, with no zero-pattern mismatch | 85% |
| K3 | **R by two routes.** The carrying set computed from the own census equals the carrying set computed by own χ² code from main's census. R_a and R_b then read the same either way | 95% |
| K4 | **Controls on own instrument** at B1749's middle apex on (2/5, 1/60). The T-step image and b → b + 1 keep every ratio and ∣V∣ to 10⁻⁸ in log and J to 10⁻⁸. The mirror image, (2/5, 7/12) at 1 − x, equals it to 10⁻⁸ with J flipped | 90% |
| R | **Read-outs** (no prediction from this seat; main's sealed priors are 70% for R_a and 55% for R_b): R_a and R_b on the own census; every line's minimum; the four predicted mirror pairs' equality; the twelve others' nearest approach; the carrying rows' (x, y, u = Re w); the predicted class's specificity on own code with main's seeds 4501–4540 (mean, worst seed, hits) | — |

## What the outcomes mean (fixed now)

- **K0–K4 hold:** B1792's census reproduces on a second instrument, and its two cells do not depend on main's code. If
  main's comparison, read after this run, gives the same R_a and R_b, three computations agree on the outcome, and
  this seat agrees with main's reading as its PREREGISTRATION wrote it for that outcome.
- **K2 fails:** the two instruments differ at order 60. The failure is diagnosed before any reading of R.
- **K3 fails:** the carrying set depends on the route, so on a row near the bar. The rows that differ are reported, and
  R is read as unsettled at those lines.
- **Whatever R shows,** this seat makes no claim beyond main's sealed reading. The prediction was formed after the data
  (W164), and B1792 seeks no grade.

## What stays out

- A re-run of main's compare.py or census.py; the nine; the class-choosing null; any line of another order or slope;
  new frame values beyond the 2 500 points and K4's three control images.

## Seen before the rule (disclosed)

- **Read on main:**
  - B1792's PREREGISTRATION in full;
  - census.py's first 80 lines (its lines(), apexes() and point());
  - ARTIFACT_HASHES; and the commit messages of 096c97e94, 1741ae6ba and be216a281.
- **The listener's one-line notices** of fc54cf57e and 096c97e94.
- **Not read:**
  - no value of main's census.jsonl, control.json, census_run.txt or compare_run_failed_launch.txt;
  - no comparison output, since none exists at be216a281.
- **The listener is paused** until this run's output is committed, so that a one-line notice of main's result is not
  seen first.
- **Not run:** no script exists; no line of order 60 has been computed by this seat.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read. A resumed run after a restart is the same run, and is disclosed.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.

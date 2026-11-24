# B1975 — Review 86 entered: three cold readers caught six of the seven plants and found real faults in all eight arcs read; each is checked by main and mended

**Verdict: PROVED (a process arc).** Main, 2026-11-24. Register row P-880. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Review 86|plant|reading copy|cold reader/: 55 of 1716 arcs on main match (NEGATIVE 2, OPEN 3, PROVED 49, RETRACTED 1); 65 register rows match (DECLINED 1, DONE 26, QUEUED 38)`.
  These are the earlier reviews' entries and their rows. This arc follows Review 85's method (B1960).
- **The literature:** none applies; this is a review of the record's own window.

## Why now, and what was read

- **When it opened.** The review opened at the 25th landing since Review 85's anchor 49c7bdf08, before the limit of 34
  (R84-4 met). The landing tool prints the count at every landing (R85-1 met).
- **The window:** 49c7bdf08 to f4a0ab61f (the anchor of this entry).
- **The sample.**
  - The tool, seeded by the anchor, drew B1962, B1964, B1969, B1970 and B1973.
  - Main added B1971, B1972 and B1974, the day's most consequential arcs and main's own. That way the two-doublet chain
    and both of the day's checks of seats' work were read whole.
- **The reading copy and the readers.**
  - The copy was a git archive of the eight arcs at f4a0ab61f, with seven planted faults, one in each of seven arcs.
    B1964 was left clean as a control.
  - The plant list is `verification/plants.json`, sha256 b448cab25ac73ae6f70d910bd503a1d9c0011e719a9f99674e84ce4b2d5dd232.
    The hash was fixed in the audit room before any reader started.
  - Three readers of main's own model family that wrote none of these arcs: A read B1962, B1964 and B1969; B read
    B1970, B1971 and B1974; C read B1972 and B1973.
  - Readers B and C ran the scripts and tests from the copy.

## The plants

| arc | plant | caught by |
|---|---|---|
| B1962 | a number in the later dated note, 0.12525 → 0.15225 | **missed** (reader A read the note for its claim, not its number) |
| B1969 | the determinant law's sign, w² + u·u → w² − u·u | A |
| B1970 | the down quarks' hypercharge, −1/2 → +1/2 | B |
| B1971 | the census count, 104 → 108 aligned | B |
| B1972 | a lock that cannot fail, `count(20) == 1` → `>= 0` | C |
| B1973 | s_L ≤ 0.387 → 0.287, against the stated cap 0.531 | C |
| B1974 | the valence count's sign at the cusp 0, −1/4 → +1/4 | B |

## The real findings, each checked by main on the live tree

They are entered as dated "Review 86 corrections" blocks on each arc's page, with in-place fixes where a sentence was
false, the verdict lines scoped, the law map's rows scoped, and the locks mended. The ones that change a result:

- **B1971.**
  - Its census used a wrong notion of order: its filter dropped points of order 10 such as (1/2, k/5).
  - Main's run at those eight points (`B1971/verification/missing_order10.py`) gives orders 8 and 10: **120 points,
    108 aligned, every one of the 12 failures on a = 1/2**. That matches B1963's 12 at the same height and column.
  - The exact identities (w = 0) hold only at order 5.
  - A sixth entry falls faster than naive.
  - The cancellation of the Higgs's rotations is an inference from rates; a counterfactual is owed.
- **B1970.**
  - Its holomorphy control D4 could not fail. Main ran the real check (`B1970/verification/d4_coupling.py`): the
    coupling is holomorphic under S (2.5e-24) and not under S̃ (0.73 to 23). The conclusion stands.
  - Its "the cusp mixing aligns" holds at order 5.
- **B1973.**
  - It misplaced agy-002's T5, which certifies every Higgs at its sampled channel points. That was unfair to the seat,
    and is corrected.
  - The 0.531 cap rests on agy-002's reduction, which main did not re-derive.
- **B1972.**
  - Its BANK-3 checks are identities by construction.
  - Its BANK-5 "prefers … because" is not in the source, and is withdrawn.
  - Its reproduction lock was circular.
- **B1974.** The force sits in P1, so the title is corrected.
- **B1964.**
  - Order 9 was not run.
  - PROVED covers the lemma and a check at height 30, not a uniform cusp limit.
  - Two numbers have no run.
- **B1962.** A stale section contradicts its own later note; two wording faults.
- **B1969.** Its table is not monotone, and its "nearly allows" interpretation did not follow from a search. It is
  settled since by B1973 P3.

## What it means

- **The day's arcs carried more overclaims than errors of number.** The recurring class: a page that states a
  mechanism, a uniqueness or a census more generally than its checks. That is Review 85's recurring class again (R81-7).
- **Main's own day of work was the least checked before landing.** The cold read found the census fault in B1971,
  which would otherwise have stood.

## What is open (entered in REVIEWS.md as R86-1 to R86-5)

- **R86-1:** the counterfactual for B1971's cancellation, a sector-dependent Higgs.
- **R86-2:** B1964 at order 9 and a uniform cusp limit.
- **R86-3:** agy-002's reduction behind B1973's cap, re-derived on main.
- **R86-4:** this window read by the other model family, with plants (with R84-2 and R85-4).
- **R86-5:** readers check the numbers inside dated notes as closely as the body (the missed plant).

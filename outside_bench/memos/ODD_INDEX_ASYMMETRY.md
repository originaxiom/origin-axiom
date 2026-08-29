# THE ODD-INDEX WINDOW — the theorem's one exception is real, and what lives in it is GENERIC: every Sturmian slope shares it
## (outside bench memo 144, 2026-08-29; certificate `certificates/odd_index_asymmetry.py`, GREEN; the last place L173's differential could have survived)

memo 143 proved the asymmetry **impossible** at reversal-closed windows
and named the one exception: at **odd** Fibonacci index the reversal
identity fails at the two cut-adjacent letters, so H_L ≠ J H_R J. This
cell goes there.

## THE PATTERN

| window | reversal defect | counts | asymmetry |
|---|---|---|---|
| N = 987, **even** F₁₆ | none | (7, 7) | **0** — theorem applies |
| N = 2584, **even** F₁₈ | none | (16, 16) | **0** — theorem applies |
| N = 1597, **odd** F₁₇ | sites {0, 1} | (14, 8) | **6** — theorem does not apply |
| N = 4181, **odd** F₁₉ | sites {0, 1} | (37, 29) | **8** — theorem does not apply |

**The exception is real.** Verified: at odd index the left word **is**
exactly reverse(right) with sites {0,1} flipped.

## ⚠ THE CONTROL TOOK THREE ITERATIONS, AND THE FIRST TWO WERE WRONG

This is the methodological content, recorded rather than tidied away.

**(i) Random *bulk* two-site flips** — gave **P = 0.025**, apparently
DISTINCTIVE. **Mis-specified:** the Fibonacci defect sits at **{0,1}, at
the boundary**, where edge states live. Position-matched flips give
asymmetry **3–5**; deep-bulk flips give **0–1**. Position is the dominant
factor, so a bulk control understates the null badly. **Caught by my own
stated fence — which is why the fence was worth writing.**

**(ii) Position-matched flips on *random words*** — gave asymmetry **0 in
every trial**, apparently overwhelming. **Vacuous:** a random binary word
has **no spectral gaps**, so the gap clause selects nothing and **both
counts are 0** (verified: edge count on a random word = 0). Comparing
against systems with **no edge states at all** is no control.

**(iii) The valid control — other Sturmian slopes**, same N, same two-site
boundary defect: comparable gap structure, same geometry, only the
slope's arithmetic differs.

## THE VALID CONTROL, AT N = 1597

| slope | counts | asymmetry |
|---|---|---|
| **golden (Fibonacci), 2−φ** | (14, 8) | **6** |
| silver, √2−1 | (11, 14) | 3 |
| bronze, (√13−3)/2 | (13, 15) | 2 |
| **e − 2** | (13, 11) | 2 |
| **π − 3** | (3, 5) | 2 |

> **An asymmetry appears for EVERY Sturmian slope tested — including the
> non-metallic ones.** It is a generic feature of a **two-site boundary
> defect on a quasiperiodic reversal pair**, not something the golden
> slope supplies.

## OUTCOME O-GENERIC

**The theorem's one exception is real, and what lives in it is not
distinctive.**

**⚠ The honest residue, named rather than claimed:** the golden case **is**
the largest observed — **6 against 2–3**. **Four controls cannot establish
distinctiveness, and this memo does not claim it.** A proper ensemble over
many slopes and windows would settle whether the golden excess is real.
**Registered as an open lead, not a finding.**

## WHERE THIS LEAVES L173

All three parts of its differential reduce to *"the halves are
reversals"* (memos 137, 143), and **the one window where that argument
fails yields an asymmetry every quasiperiodic slope shares.**

> **Nothing distinctive has been found anywhere tested.**

**Fence.** N = 1597 for the control, four comparison slopes, one detector.
No laboratory datum touched. Gate 5 untouched.

### ADDENDUM 1 (2026-08-29) — THE OPEN LEAD CLOSES NEGATIVELY (memo 145), and this memo's caution is vindicated
This memo registered the golden excess (6 against 2–3) as an **open lead**
and declined to claim it on four controls. **The proper ensemble closes it
negatively.** memo 145: 15 slopes, each at **its own** convergent
denominators — removing a confound this memo missed, that **N = 1597 is a
Fibonacci number**, commensurate with the golden slope alone.

Golden's values across its own windows are **1, 3, 6, 7 — monotone in N**,
and corr(asymmetry, N) = **+0.629** across the ensemble. Šidák-corrected
over golden's 4 windows, **P = 0.241**. And the ensemble maximum is **8,
from log 2** — **a non-metallic slope at a smaller window than golden's
best.**

**Verdict G-NOISE.** Declining to claim on four controls was the right
call. This addendum is the only mutation.

# B802 — cc3's B783 (observer ground-zero) harvested, its headline negative INDEPENDENTLY CONFIRMED

cc banking seat, 2026-07-29. Campaign closure sweep. Standing rule **integrate-don't-merge**:
cc3's branch is never merged; deliverables are cherry-picked under a new number and verified
independently. Gate 5-Q scope (as cc3's original). Nothing to `CLAIMS.md`.

## Why this arc exists

A closure survey of the cc3 seat found **four** arcs present there and not in main:

| cc3 arc | state | disposition |
|---|---|---|
| B783 observer ground-zero | FINISHED (928w) | **unharvested — this arc** |
| B784 trace-map intertwining | FINISHED | already harvested into main's `B785_cc3_gate_harvest` |
| B792 Maass m004 eigenvalues | FINISHED | already harvested into `B795` (7/7 verified) + `B797` |
| B796 coupling campaign | **in flight** (no FINDINGS; active Cell-9 shakedown) | not harvestable |

Four further arcs differ between the seats (`B350`, `B778`, `B780`, `B781`) — **main is ahead in
every one**, including B780's partial retraction, which cc3's copy does not carry. Nothing to pull.

## What was verified here, from scratch

cc3's headline negative is that **γ₅ is not reading direction**. The argument reproduces exactly:

- **Reversal preserves the letter frequencies** — computed on the Fibonacci word to |S| = 121,393:
  `d(a) = 75025/121393 → 1/φ`, `d(b) = 46368/121393 → 1/φ²`, summing to 1, unchanged under
  reversal. ✔
- **Complement (a↔b) swaps them.** ✔ So reversal and complement are different operations on
  frequencies. ✔
- **Growth rate → φ in both reading directions** (direction-independent). ✔
- **γ₅ moves every φ-built quantity** (`1/φ ≠ 1/φ̄`), while reversal provably moves none. **Therefore
  γ₅ ≠ reading direction.** ✔

**The load-bearing negative stands, independently.**

## Scope — what this arc does NOT verify

Stated because harvesting on faith is the failure this rule exists to prevent. These need cc3's
tracking-map definition, which was **not** reproduced here:

- `parent(σ) = child(σ_mirror)` with zero mismatches to F₁₈
- the per-prediction **1/5** scoring of proposal #16 (and the cumulative "1 for 20")
- the K-theory positive-cone identity across directions

Those remain **cc3's result on cc3's evidence** — cited, not re-derived. The verified part is the
mechanism, which is the part the negative rests on.

`verify.py` · lock `tests/test_b802_cc3_harvest.py`

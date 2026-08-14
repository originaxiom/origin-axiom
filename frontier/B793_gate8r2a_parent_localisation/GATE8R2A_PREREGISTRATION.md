# GATE 8R2-A — PROVENANCE-INDEPENDENT PARENT LOCALISATION (sealed before compute)

Stage A of a split gate. Origin: Chat-1 relay 2026-07-28; arithmetic independently verified by
cc below. **GATE8R2 (`012a29f8578c6036`, sealed in B791) is NOT amended** — it stays byte-frozen
and becomes **Stage B**. Gate 5 + Gate 5-Q binding. Nothing here reaches CLAIMS.md.

## Why the original gate had to be split

GATE8R2's PASS window is r = 7.072 ± 0.005. Its only corroboration was the Weyl cross-check.
Those two operate at incompatible resolutions:

| λ slip | r | inside ±0.005? | vs Weyl 7.0478 |
|---|---|---|---|
| 51.014 as-given | 7.072058 | **yes** | 0.34 % |
| 51.00 truncated | 7.071068 | **yes** | 0.33 % |
| 51.104 digit swap | 7.078418 | **NO** | 0.43 % |
| 51.14 second decimal | 7.080960 | **NO** | 0.47 % |

- gate window: ±0.005/7.072 = **0.0707 %**
- total Weyl spread across all four slips: **0.14 %** — i.e. all four are *indistinguishable* to
  the check that corroborates the target.

**The gate is over 40× tighter than its own corroboration**, so it does not test the solver — it
tests the last decimal of a transcription. And the failure mode is the bad one: a second-decimal
slip **passes the Weyl check and fails the gate**, producing a **spurious FAIL that sends a seat
hunting a solver defect that does not exist** — on a solver whose *last* failure (Gate 8,
truncation) was real. That is the worst possible placement for a false alarm.

## The Stage-A gate — no literature value anywhere in it

Weyl budget for the parent (per-sector W = 0.002856530136, verified in B791):

    expected parent eigenvalues below r = 6.5 : 0.784
    expected parent eigenvalues below r = 7.6 : 1.254

So **exactly one** parent eigenvalue is expected in [0.5, 7.6]. That alone is a complete solver
test, and it contains no transcribed quantity.

> **GATE 8R2-A.** Run the B788 V₁ solver on r ∈ [0.5, 7.6] at **two heights**.
> **PASS** if exactly one confirmed root is found, with both heights agreeing.
> **Record its value.**
> **No literature comparison. No window. No pass/fail on the value itself.**

If Stage A returns exactly one root near 7.07, the solver has **independently computed
λ₁(parent)** — not calibrated against the literature, but computed a quantity the literature
happens to share. Stage B (the frozen GATE8R2) then becomes **bidirectional corroboration** once
the primary table is read: if the two disagree, it will be clear which side moved.

Strictly stronger than the sealed version, and runnable without any external dependency.

## Execution protocol — the bank is a sealed directory, not a live process

There is no solver state to fork; there are only files. Therefore:

1. **Verify** the bank's `ARTIFACT_HASHES.txt` and record the result. *(Done pre-seal:
   `bank_hash_baseline_pre.json` — **84 verified, 0 mismatches**. The 10 unresolved entries are
   the bank's own lock tests at `../../tests/test_b788_maass_*.py`, which are **absent from the
   delivered archive**: the bank's data is verifiable, its locks are not.)*
2. **Copy** the V₁ solver **out** of the bank into this gate's directory. **Never write into the
   bank.**
3. **Run** here; all outputs land under **B793**.
4. **Re-verify** the bank's hashes afterwards and record both results.

Step 4 converts "I did not modify the bank" from an assertion into evidence, and it is cheap.
Ownership follows the same shape as the B788/B790 numbering ruling: **the solver is B788's, the
run is B793, the receipt cites both.** No transfer, no fork.

## Two-outcome criteria

- **PASS** — exactly one confirmed root in [0.5, 7.6], stable across both heights. The solver is
  validated at the low-r end, where Bessel truncation is least forgiving (mode budget at r = 7.07
  is ~3.5× lighter than at the existing 24.5033 control, and truncation is how Gate 8 died).
- **FAIL-ZERO** — no confirmed root. Either a genuine solver defect at low r, or the scan
  resolution is too coarse. Distinguish before concluding.
- **FAIL-MANY** — more than one confirmed root. Either spurious survivors (check two-height
  stability and the σ₂ separation), or the Weyl budget is being violated, which would itself be a
  finding.

**Recording the root's value is mandatory; comparing it to anything is forbidden in Stage A.**
That separation is the entire point of the split and must not be softened at write-up time.

## Sequence

1. Seal this gate. ✅
2. Run Stage A against the copied solver.
3. Gate 9 re-run on the widened interval with W(T) as the completeness gate and a
   **budget-derived** screen cap replacing the hand-set `maximum_minima_per_sector = 24`.

Stage B waits on a primary-source read of Grunewald–Huntebrinker Table 3 and **blocks nothing**.

— cc, 2026-07-28

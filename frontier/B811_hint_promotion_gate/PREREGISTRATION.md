# B811 — PREREGISTRATION: the full promotion gate on H128–H131

**Sealed before any computation.** cc banking seat, 2026-07-30.
**Gate 5 holds: no SM value goes to `CLAIMS.md` under any outcome of this arc.** The question is
whether four hints **promote, park, or die by the programme's own gate** — not whether physics is
derivable.

## 1. Why this arc exists

`METHOD.md`'s lifecycle is explicit:

> **CHECKED** — *"set a diagnostic flag only; route to DORMANT, **never KILLED**"*
> **KILLED** — *"**only** via the full promotion gate → tombstone + residual-hint"*

**B580 Round 1 was a check, and it issued KILLED** on H128, H129 and H130. That is a **stage
violation** of the programme's own method, and the ledger rows still read `[NOTICED]` while carrying
kill verdicts beneath them. This arc runs the gate that was owed, so the dispositions become legal
whichever way they fall.

## 2. The decisive test, and its family fixed NOW

The promotion battery's load-bearing element here is the **null / look-elsewhere test**. A tight
σ-agreement is worthless if the search space that produced it is large.

**Expression family, fixed before any run** — all closed forms
`E = (a·φ^n + c) / (b·φ^m + d)` with

- `n, m ∈ {−8…8}`, `a, b ∈ {1, 2, 3, 4, 5}`, `c, d ∈ {−2, −1, 0, 1, 2}`, `b·φ^m + d ≠ 0`
- deduplicated by value to 12 significant figures

This family **contains** all four hinted forms (`1/(2φ³)`, `φ^−8`, `2/3`) by construction, which is
required for the test to be fair to them.

**The null statistic:** for each target constant, `N_hit` = how many *distinct* family values land
within the target's own quoted uncertainty, and `p_look_elsewhere = N_hit / N_family`.

## 3. Two-outcome criteria, fixed now

Per hint:

| outcome | criterion |
|---|---|
| **PROMOTED** to `OPEN_LEADS` | `N_hit ≤ 3` for its target — i.e. the agreement is rare in a family that could have produced it |
| **KILLED** (legal, → tombstone + residual-hint) | `N_hit ≥ 20` **and** an independent structural reason exists (B580's information-free channel, B686's tautology, or a level-mismatch) |
| **DORMANT** | anything between, or a structural reason without the base rate |

**A scale/level check is applied independently and can kill on its own:** `α_s(M_Z)` is a **running**
coupling defined **at a scale**; the object is **proved scale-free** (S3/B615). A quantity that only
exists at a chosen scale cannot be output by a scale-free structure — if that argument holds, H128
dies on structure regardless of its base rate, and the base rate is then reported as corroboration.

## 4. Pre-stated expectation, so the result can disappoint it

I expect **`N_hit` to be large** (tens) for every target, because the family is big and the
uncertainties are ~1 %. I therefore expect **KILLED** for H128–H130, making B580's verdicts legal
rather than overturning them.

**If `N_hit ≤ 3` for any target, my expectation is wrong and that hint PROMOTES** — and the arc must
report that plainly rather than finding a reason to discount it. That is the outcome this seal
exists to protect.

## 5. What would make this arc a failure

- Adjusting the family, the σ window, or the 3/20 thresholds after seeing `N_hit`.
- Killing a hint on base rate alone with no structural reason, or promoting one on rarity alone
  without recording that a *rare* coincidence is still a coincidence until a derivation exists.
- Letting any outcome touch `CLAIMS.md`. **Gate 5 is not negotiable in this arc.**
- Reporting H131 as anything other than what it is: an already-computed **NULL**, with the 7×
  excess honestly diagnosed as a smoothing artifact.

## 6. Deliverables

`gate.py` (family enumeration + null test + level check) · `FINDINGS.md` (four dispositions) ·
`tests/test_b811_gate.py` · `HINT_LEDGER` rows corrected to their true lifecycle state ·
tombstones for any legal KILL.

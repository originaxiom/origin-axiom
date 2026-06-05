# B86 (Phase E) — unification synthesis, novelty positioning, paper skeleton

**Date:** 2026-06-05. **Status:** synthesis / positioning (no new theorem; backed by V1–V68). Standalone
low-dim topology / invariant theory; **no Origin-core claim**; proven core P1–P16 untouched. Script:
`probe.py`. Paper skeleton: `papers/SLN_FIGURE_EIGHT_SKELETON.md`. Test:
`tests/test_b86_unification_synthesis.py`.

The capstone of the unification push: consolidates the whole arc into the publishable structure,
positions it against the literature (internally), and names the one external check that gates any claim.

## The three threads (one object: `Fix(T_1²)`, the figure-eight character variety)

1. **Tower (dynamics):** `char(J(m)) =` the Dickson catalog. **PROVED `n≤4`** (B80, CRT/F_p);
   **STRUCTURAL `n=5,6`** (B62); the all-`n` first-principles proof **reduced to one symbolic `e₂/Λ²`
   closure** (B85). Parity grading **PROVED** (B64).
2. **A-polynomial (geometry):** trace-map fixed locus = Cooper–Long A-poly at SL(2) **EXACT** (B67);
   Falbel Dehn-filling A-variety at SL(3) (B71).
3. **degree=rank / the `Aₙ` family (the main new result):** `[A,B]=(−1)ⁿ⁻¹μⁿ` (B77); peripheral
   A-variety `L=(−1)ⁿ⁻¹Mⁿ` (B83); the family unifies SL(2)/SL(3), with **SL(4) `L=−M⁴` NEW**. Mechanism:
   exponent = rank = the principal component's filling slope.

(B77: the dynamical and geometric faces are **distinct** — not unified through the eigenvalue spectrum.)

## Novelty positioning (internal — the external check is the gate)

| item | status |
|---|---|
| SL(2) Cooper–Long, SL(3) Falbel | **KNOWN** |
| trace-map machinery | `STANDARD_REPACKAGE` (Lawton; Baake–Grimm–Roberts) |
| **`Aₙ` family / SL(4) `L=−M⁴`** | **`APPARENTLY_NEW`** — **the #1 thing to check** (BFG framework; `n≥3` only; not `Sym^{n−1}`) |
| CRT/F_p tower proof (B80) | `APPARENTLY_NEW` technique |
| parity-graded Dickson factorization (B62/B64) | `APPARENTLY_NEW` (PC12 Thm 4) |

**The external check cannot be closed here** (the standing rule is *no external contact*). The honest
disposition: the new-looking results are labelled `APPARENTLY_NEW` pending a real literature search; the
**`Aₙ` family / SL(4) A-polynomial is the one most worth checking** before any external claim.

## What is NOT here
The **physics chapter is closed** (V65/B82): anyons (V28), quasicrystals (V29), j=1728 (V34/V53),
higher-spin (V56), cusp/quantum-group (V58) — every bridge reduced to invariant theory of `sl(n)`. This
is **low-dimensional topology + invariant theory**, not physics.

## Disposition
Phase E complete. The paper skeleton (`papers/SLN_FIGURE_EIGHT_SKELETON.md`) carries the proof-status of
each piece; no promotion to `CLAIMS.md` without the GOVERNANCE §5 gate; `EXPERT_OUTREACH.md` dormant.

## Reproduce

```bash
python frontier/B86_unification_synthesis/probe.py
python -m pytest tests/test_b86_unification_synthesis.py -q
```

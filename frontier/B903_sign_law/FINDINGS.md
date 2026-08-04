# B903 — N2: the sign law's mechanism — anti-palindromy + an exact root-parity law (six certificates)

**Date:** 2026-08-05 · **Seat:** cc (banking) · **Status:** exact (Sturm counts, exact division, all six blocks)

## The question (N2 — load-bearing since B894's four-column ledger)

B581 banked the sign law — sign(τ_m) = (−1)^m, the torsion positive exactly
at the θ-odd exponents — as an observation with a registered proof target.
B894 made it load-bearing (the torsion-sign column marks the measured
plane). What is the mechanism?

## Result 1 — anti-palindromy is universal (the zero at 1 is forced)

All six banked quotients Δ_m are **exactly anti-palindromic**
(c_i = −c_{d−i}, verified coefficient-by-coefficient): the functional
equation Δ(1/t) = −t^{−d}Δ(t) holds with sign ε = −1 in every block, which
FORCES Δ_m(1) = 0. The simple zero the torsion differentiates through is
structural (duality), not numerical accident.

## Result 2 — the exact sign formula and the root-parity law

Writing Δ_m = (t−1)·P_m (exact division; P_m palindromic), τ_m = P_m(1),
and since each reciprocal pair (λ, 1/λ) of positive real roots contributes
(1−λ)(1−1/λ) = 2−λ−1/λ < 0 while negative pairs and complex quartets
contribute positively:

> **sign(τ_m) = sign(lc)·(−1)^{p_m}**, p_m = the number of positive-real
> reciprocal root pairs of P_m (an exact Sturm count).

Verified in all six blocks. And the counts themselves:

| m | 1 | 4 | 5 | 7 | 8 | 11 |
|---|---|---|---|---|---|----|
| p_m | 1 | 2 | 3 | 3 | 4 | 5 |
| p_m mod 2 | 1 | 0 | 1 | 1 | 0 | 1 |
| m mod 2 | 1 | 0 | 1 | 1 | 0 | 1 |

**p_m ≡ m (mod 2) in every block.** The sign law is therefore REDUCED, with
certificates: sign(τ_m) = (−1)^m ⟸ anti-palindromy (proved per block;
provable in general from Poincaré duality for the odd-dimensional
orthogonal reps V_{2m}) + the root-parity law p_m ≡ m (mod 2) (proved per
block by exact count).

## What remains open (registered)

The conceptual step — WHY the positive-real pair count of P_m carries the
θ-parity of m — is the remaining target. It is now a sharply posed question
about root distributions of the twisted Alexander quotients (a statement
about the spectrum of the holonomy on V_{2m}), no longer a bare sign
pattern. B581's "the proof or the fence" is resolved toward the proof side:
two of the three steps are done exactly.

## Files

- `sign_mechanism.py` → `results.json`
- Locks: `tests/test_b903_sign.py`

## Depends on

B581 (the banked quotients + the law), B894 (why it's load-bearing).

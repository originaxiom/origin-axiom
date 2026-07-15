# P0 — GATE REPORT (2026-07-15, seat cc2)

**Verdict: ALL GATES GREEN. The campaign engine reproduces the banked ladder exactly.**

Environment: Python 3.12.1, numpy 2.5.1, sympy 1.14.0, mpmath 1.3.0 (venv `seat-work/.venv`).

## P0(b) — the banked level-2 script, run verbatim
`frontier/B570_allowed_plays/c3_e6_level2_monodromy.py`: every in-script gate green
(|W| = 51840; S unitary/symmetric; (ST)³=S², S⁴=I; S² = θ-flip permutation; 729 Verlinde
integers; q-dims; two-word agreement 1.15e−13). Banked values reproduced: Z = +1, θ-odd 3×3
non-scalar, order 4, eigenvalues {+1, +i, −i}, tr_even = 0.

## P0(c–e) — the campaign's own generic-k engine (independent build)
`scripts/engine.py gates` — the EXACT pipeline (integer ζ_{6κ} exponent counts; float and
dps-50 legs both evaluated from the counts) against the float banked-style build:

| level | κ | N (banked) | dim_odd (banked) | Z | ord(B_odd) | float-vs-exact |
|---|---|---|---|---|---|---|
| 1 | 13 | 3 ✓ | 1 ✓ | +1 ✓ | 1 ✓ | 1.5e−14 |
| 2 | 14 | 9 ✓ | 3 ✓ | +1 ✓ | 4 ✓ | 3.7e−14 |
| 3 | 15 | 20 ✓ | 8 ✓ | +1 ✓ | 60 ✓ | 6.4e−14 |

All battery gates < 3e−13 at every level; Verlinde integrality dev ≤ 2.8e−15, min ≥ 0.

**The level-3 octic gate (the decisive reproduction):** from the exact counts at dps 50, the
8 distinct |S_odd| magnitudes scaled w = 30·|·|² give
`81·Π(w − wᵢ) = [81, −2430, 29160, −181800, 640800, −1296000, 1448000, −800000, 160000]`
— **integer-for-integer equal to B578-D7's banked octic** (D = 81 minimal).
Order-60 certificate: ‖B⁶⁰ − I‖ = 1.3e−49; proper divisors {30, 20, 12} deviate by
{2.0, 1.7, 0.85} — order exactly 60.

## Observation recorded pre-P2 (NOTICED-grade; not in the prereg; not judged)
The trace's unit lives in the **odd** sector at k = 1, 2 (tr_odd = +1, tr_even = 0) and hops
to the **even** sector at k = 3 (tr_odd = 0, tr_even = +1). Z = +1 throughout (H133), but
*which parity sector carries it* alternates. Candidate hint row for the ledger; the level-4
value of (tr_even, tr_odd) will be banked as data either way.

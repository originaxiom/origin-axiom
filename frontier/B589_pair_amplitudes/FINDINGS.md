# B589 — L83(a): the three E₆₂ pair amplitudes identified exactly

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM
quantities. Locks `tests/test_b589_pair_amplitudes.py`. Resolves L83(a).**
Run: `python3 pair_amplitudes.py` (pyenv, ~3 min; the 51840-term Weyl sums are
collected EXACTLY — a Counter over rational exponents mod 1, denominator | 42;
zero float error in the sums — then evaluated at 50 digits).

## The identification (blind ordering followed in-script; certified 40+ digits)

The three per-pair chirality amplitudes of ρ(A₁) on the E₆₂ θ-odd space
(banked blind in B586) are exactly:

> **p(27-pair) = (2/√7)·sin(2π/7) · ζ₁₄⁺³**
> **p(351′-pair) = (2/√7)·sin(6π/7) · ζ₁₄⁻²**
> **p(351-pair) = (2/√7)·sin(4π/7) · ζ₁₄⁻¹**

(arguments exactly {+3, −2, −1}/14 of a turn; moduli relations
r₁ = r₂·2sin(5π/14), r₃ = r₂/(2sin(π/14)) hold to 40+ digits; r₂ satisfies
7r³ + 7r² − 1 = 0, the ℚ(cos(π/7)) cubic — findpoly, certified numerically.)

## What grades them (the L83(a) question, answered)

**The moduli are exactly the entries of the banked θ-odd sine kernel** —
B572's S_odd(E₆,₂) = −i·(2/√7)[sin(2πst/7)]: the set
{2sin(2π/7), 2sin(6π/7), 2sin(4π/7)}/√7 is the s = 1 row of the ℤ/7 kernel.
So the diagonal of the monodromy's odd block carries the odd S-matrix's own
moduli; the monodromy adds only the three 14th-root phases {+3, −2, −1}.
The θ-odd dynamics at E₆₂ is thus completely arithmetic in ℚ(ζ₇, i)-scale
data: the ℤ/7 sine kernel (B572, banked) for magnitudes, three 14th roots for
phases, C3's order-4 for the block as a whole.

**Post-hoc comparison (registered):** the phase exponents {3, −2, −1}/14 do
NOT match the T-phases (h − c/24 mod 1 = {13, 73, 61}/84) — the phases are not
the conformal weights; their grading remains a residual (folded into L83(b)).

## Discipline note

This is an identification cell (characterizing already-banked blind numbers).
The in-script ordering was: gates (B586 values reproduced at 50 digits, sum =
1) → identification → post-hoc grading comparison. MB13: B572 (the sine
kernel — the match's target, banked), B586 (the amplitudes), C3 (the stage),
B578 (K₃/field discipline) — found and cited.

## Anchors

B586 (the blind amplitudes), B572 (S_odd = the ℤ/7 sine kernel — the moduli
match), B570-C3 (order 4), L83(a) (resolved; the phase grading → L83(b)).

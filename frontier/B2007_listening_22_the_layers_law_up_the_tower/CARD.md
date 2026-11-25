# B2007 — Listening card 22: the layer's law up the tower — each step G_k → G_{k−1} through mod 729, by GAP, and the halving at mod 729 on the leading modes

Written 2026-11-25 (after midnight, in the same session), before any run, in the author's /loop "continue the listening
line". Data-free. 0 of 19.

## Why

- **B2006:** at its prime the whole's group G_k is the cube group S₄ with a 3-adic layer K_k: ℤ₃² at mod 27, ℤ₉² at mod 81,
  then non-abelian of order 3⁷ at mod 243. The steps |G_k|/|G_{k−1}| are 9, 9, 27.
- **B2005:** the halving holds exactly where G_k keeps ℤ₆.
- **mod 729:** the 52,488-point orbit is beyond sympy, but within GAP (run through sage, which is installed).

## The checks (nothing chosen)

- **L1 and L2:** for k = 3 to 6 (mod 27 to 729), GAP computes:
  - |G_k|;
  - the kernel of the action on the blocks of reduction mod 3^{k−1}, the step's layer: its order, whether it is elementary
    abelian, and its abelian invariants;
  - the kernel of the action on the blocks of reduction mod 9, the whole layer K_k: its order, abelian invariants, exponent and
    nilpotency class;
  - G_k's abelian invariants.
- **L3:** at mod 729, the leading 30 eigenvalues of the six-move unfolding in the neutral and in a charged sector (sparse
  eigensolver). Do the charged ones equal half the neutral ones below the top?

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| L1 | every step's layer (k = 3 to 6) is elementary abelian | 0.55 |
| L2 | the step at k = 6 has order 27, as at k = 5 | 0.35 |
| L3 | G₆'s abelianisation has order 6, and at mod 729 the leading 30 charged eigenvalues are half the leading neutral ones below the top, to 1e-8 | 0.7 |

## What it means

- **L1 and L2:** the layer's law, how the 3-adic layer grows rung by rung.
- **L3:** whether the halving and ℤ₆ continue one rung further.
- **Nothing is compared with data.**

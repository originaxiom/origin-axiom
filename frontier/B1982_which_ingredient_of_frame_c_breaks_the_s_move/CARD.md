# B1982 card — which ingredient of frame C breaks the S move (P-882 Q1)

Written 2026-11-25, before any run, after B1980: frame C fails S with its canonical end read on the whole curve, and the
end is not the breaker. Data-free. 0 of 19.

## Why

- **The author, 2026-11-25:** play the whole instrument, not one hole.
- **B1980 found frame C exactly T-covariant and not S-covariant.** So it reads the level-30 curve through one cusp.
- **Before frame C can be rebuilt covariant,** the ingredient that breaks S has to be found. Reading the construction
  (`determinant_law.parts`):
  - the channels' characteristics are symmetric in the point's two coordinates;
  - what is not symmetric: the phase factors κ use the first coordinate only (e = exp(−2πi q_L a));
  - the a₀ term uses the first characteristic as the coefficient of τ;
  - the channel norm F_u is a Fourier expansion at i∞;
  - and the Higgs triplet transforms under S by its own representation (B1974).

## The run (`verification/ablate.py`)

- **The test.** Each variant is frame C with one ingredient removed, as a diagnostic, not a physics proposal. Each is
  tested under S, with the end read covariantly (B1980's `duality_cov.py`).
  - The heights are 1.5 against 2/3, and 2.5 against 0.4.
  - The matching is B1976's 96 points against all 899 nonzero points of E[30], under any bijection, with sectors and
    reading fixed.
  - A variant passes if the largest distance is below 1e-8 at both pairs.
- **The variants:**

| id | variant |
|---|---|
| V0 | frame C as is (the control; it must reproduce B1980's 0.18 and 0.32) |
| V1 | the norm factor dropped: each channel's weight is R alone (the theta constants over η³, with κ) |
| V2 | V1 with κ's point-dependent phase e set to 1 |
| V3 | the norm kept, with the a₀ term dropped |
| V4 | the norm kept, with κ's phase e set to 1 |
| V5 | V2 with the Higgs triplet held at the constant (1, 1, 1), the same at both heights; it is unchanged by any permutation of the quaternion units |
| V6 | frame C with only the Higgs held at (1, 1, 1) |

## Expectations, with priors

| id | expectation | prior |
|---|---|---|
| E0 | V0 reproduces B1980's distances as printed in duality_cov_run.txt (0.18 and 0.32; the script's bar is 1e-2 and 1.5e-2) | 0.99 |
| E1 | V1 passes (the holomorphic core is S-covariant, and the norm breaks it) | 0.35 |
| E2 | V2 passes | 0.40 |
| E3 | V3 passes | 0.15 |
| E4 | V4 passes | 0.15 |
| E5 | V5 passes | 0.40 |
| E6 | V6 passes (the Higgs alone breaks S) | 0.20 |

## What each outcome means

- **A variant passes:** the ingredient it removes, or replaces, is the breaker. The covariant replacement of that
  ingredient is then P-882 Q2.
- **None passes:** the breaker is in more than one ingredient, or in the Higgs's coupling to the channels. The next
  card pairs the ablations.
- **Nothing is compared with data.**

# B1964 — In frame C the Higgs reading alone fixes the lightest generation high in the cusp, and the two readings fix orthogonal ones

**Verdict: PROVED.** An exact lemma, and its cusp-limit consequence checked at every point where the lemma applies.
Main, 2026-11-19. Data-free. Register row P-847. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /charge-consistent|charge rule|derange|cusp mixing|height window|S-tilde/: 2 of 1704 arcs on main match (NEGATIVE 1, PROVED 1); 7 register rows match (QUEUED 7)`.
  This was swept for B1963, the morning's arc. B1963 itself now matches as well.
- **What it explains:**
  - **B1946:** the charge-consistent readings derange frame C's mixing at order 5. S → S̃ acts as a 3-cycle of the
    generations high in the cusp.
  - **B1963:** that derangement holds at every non-degenerate point of orders 2 to 10 high in the cusp, and an aligned
    charge-consistent mixing occurs only in the bulk. That was a grid result; B1963 owed an analytic reason.
- **The literature:**
  - a 2 × 2 matrix U in SU(2) satisfies σ₂Ū σ₂ = U (standard);
  - θ₂ ~ 2q^{1/8} and θ₃, θ₄ → 1 as q → 0 (standard).

  Nothing outside the record treats frame C's coupling.

## The lemma (`verification/lemma.py`, exact; sympy)

Frame C's coupling for one sector, as frame_mp builds it:

  Y_ab = Σ_{m,n} (C_aᵀ ε S C_b)_{mn} (Mw)_{mn},

with the generation blocks (C₁, C₂, C₃) = (QJ, QI, QK), ε = QJ, the Higgs matrix S, and the sector's channel matrix Mw.

- **L1.** If S = E₁₂, then u = (−i, 0, 1) satisfies uᴴY = 0 for every Mw. The 2 × 2 minors of Y have greatest common
  divisor det Mw, so Y has rank 2 exactly when det Mw ≠ 0.
- **L2.** If S = E₂₁, the same holds with u = (i, 0, 1).
- **L3.** The two vectors are orthogonal.
- **L4.** For each unit Q ∈ {QI, QJ, QK}, ε Q̄ εᵀ = Q. So the conjugate reading ε S̄ εᵀ of S = c₀QI + c₁QJ + c₂QK
  is c̄₀QI + c̄₁QJ + c̄₂QK: the reading conjugates the coefficients and nothing else.
- **L5.** c₁QJ + c₂QK with c₂ = −ic₁ equals 2c₁E₁₂. Its conjugate reading equals −2c̄₁E₂₁.
- **L6.** The null vector of L1 holds for every Mw only when S is exactly a multiple of E₁₂. An E₂₁ part or a
  diagonal part moves it. So the lemma speaks of the nilpotent limit.

**Disclosed:** the first run printed L5 as False. Main's statement had −2c₁E₁₂ where the matrix is +2c₁E₁₂. The sign
was corrected in the docstring; the content is unchanged.

## The cusp limit (`verification/light_directions.py`, frame C's code)

- **Frame C's S tends to a multiple of E₁₂ high in the cusp.** |S₂₁/S₁₂| ≤ 2.34e-40 at every point at height 30.
  - The reason is the theta triplet's leading terms. Its two large components are in the ratio
    R₃/R₂ = −iθ₃²/θ₄² → −i, with corrections of order q^{1/2}. Its third component is smaller by q^{1/4}.
  - By L5 the leading part of S is a multiple of E₁₂, and by L4 that of S̃ is a multiple of E₂₁.
  - **Measured at (1/5, 2/5), up sector:** |S₁₁/S₁₂| is about 4·e^{−πy/2} (order q^{1/4}), and |S₂₁/S₁₂| about
    20·e^{−πy} (order q^{1/2}), at heights 10, 20 and 30. This is what the expansions predict. Frame C's Higgs is the
    Serre derivative of the triplet, and that derivative keeps the leading ratios.
- **The consequence.** Wherever Mw has rank 2, every sector's lightest generation tends to (−i, 0, 1)/√2 under S and
  to (i, 0, 1)/√2 under S̃. This holds whatever the point, the sector or its charges.
- **Checked** at every point of orders 2 to 10 at height 30, in the three sectors. "Rank 2" means Mw's singular-value
  ratio is at least 1e-30.

| expectation (written and hashed before the run) | prior | result |
|---|---|---|
| K1: at every rank-2 case the lightest vector matches to 1e-10 under both readings | 0.8 | holds: 574 of 574 |
| K2: every case without a match has an ill-conditioned Mw | 0.7 | holds: 192 of 192 |
| K3: the order-2 points fail under S | 0.8 | holds: (1/2, 0) and (1/2, 1/2) |
| K4: \|S₂₁/S₁₂\| ≤ 1e-38 everywhere at height 30 | 0.9 | holds: 2.34e-40 |

- **The rate, measured at one point** (1/5, 2/5): the light–light entry of the charge-consistent mixing falls as about
  19·e^{−πy}. It is 1.25e-7 at height 6 and 4.5e-13 at height 10. The rate is measured, not derived.

## What it means

- **The analytic core of B1946 and B1963.**
  - A charge-consistent pairing gives one sector S and the other S̃.
  - By L1 to L3 their lightest generations tend to orthogonal vectors.
  - So the light–light entry of the mixing tends to zero, and the mixing cannot be aligned high in the cusp. This holds
    at every point where both sectors' Mw has rank 2, with no dependence on the charges.
- **The same reading in both sectors puts both lightest generations on the same vector.** That is why (S, S) aligns at
  the light generation. Whether the two heavier generations align then depends on each sector's Mw, which is why
  B1963 finds (S, S) unaligned at a few points.
- **What the exclusion rests on:**
  - the generation blocks (QJ, QI, QK) with ε = QJ;
  - the Higgs's nilpotent cusp limit.

  A Higgs direction whose cusp limit is not a multiple of E₁₂ is outside the lemma. P-873's plane in frame D1 is such
  a family, and the SM seat's scan there (SM-C22) found no direction with both alignment and hierarchy. That scan is
  not a proof.

## Not established

- **That the heavy pair is a 3-cycle.** Only the light–light entry is proven to vanish. That is enough for
  derangement, not for the permutation's shape.
- **An error bound for the limit.** The rate is measured at one point.
- **Points where Mw is ill-conditioned:** the order-2 and order-4 points, and some of orders 6, 8 and 10. B1963
  finds the mixing deranged at the non-degenerate ones anyway, but the lemma does not cover them.

## Files

`verification/lemma.py` and `light_directions.py`, each with its run file, and `EXPECTATIONS_HASHED.md`. The lock is
`verification/test_b1964_light_generation.py`.

0 of 19.

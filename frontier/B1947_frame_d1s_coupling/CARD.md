# B1947's card — frame D1's coupling and its cusp mixing, sealed before its outputs (P-861)

*Main, 2026-11-15. Written and committed before any output of frame D1 is computed. Data-free: no output is set beside a
measured number, and no values look follows unless the mixing passes the test below.*

## Seen first (added before the card is sealed)

- **B1744 already built a twisted Higgs once,** in B1656's frame. It found:
  - **the Higgs:** B1691's theta-square triplet at the Higgs's hypercharge twist;
  - **even under the twist:** T₀(3w) = T₀(−3w), so H_u = H_d and no reading is forced. That is the coincidence main
    first expected here;
  - **null:** the quaternion is null (R₁² + R·R = 0), so with the scalar channel kept det Y = 0 and one generation is
    massless;
  - **a look already made:** set beside data post hoc, its best χ²_nine was 493 (B1742's grid, six variants). That
    look is part of this card's history (docs/LOOK_LEDGER.md), and D1 must be read as a second attempt on the same idea.
- **B1730:** the only zero-free weight-3/2 Higgs forms are c·F_a, a ≡ 2 mod 4. That is a constraint on any twisted
  Higgs, to be checked on S_D1.
- **How D1 differs from B1744:**
  - the exact channel weight;
  - the canonical end;
  - the average over the 24 points;
  - the Higgs as the Serre derivative of the twisted triplet;
  - and, as C1 shows, a convention under which H_u and H_d differ by component phases. That convention is a real
    choice, and C2 fixes it by principle.

## The definition

- **Frame D1** is frame C (B1940's extended-precision frame: the exact channel weight, the canonical end, the 24 points of
  order 5) with one change. The Higgs carries its charge as a twist, as matter does (the web seat's W-B1).
- **The Higgs enters as the third factor of a charge-conserving overlap.** This is the triple overlap of magnetized tori,
  two fermions and one scalar (Cremades, Ibáñez and Marchesano, hep-th/0404229).
  - B1691's triplet R = (−θ₂/(θ₃θ₄), −θ₄/(θ₂θ₃), iθ₃/(θ₂θ₄)) is built from theta constants whose characteristics are
    shifted by twist_of(q_H·w) = (q_H a, 2q_H b).
  - The charge is q_H = −(q_L + q_R) in 6Y: up +3, down −3, leptons −3.
  - The Higgs is its Serre derivative S_D1 = Σ_k (DR)_k Q_k, with DR = q dR/dq + (1/24)E₂R.
- **No reading is chosen.** Each sector's coupling uses its own S_D1. There is no S or S̃.
- **One declared convention.** The half-integer characteristics are represented as frame C's matter represents them:
  θ₂ = θ[½ + q_H a, 2q_H b], θ₃ = θ[q_H a, 2q_H b], θ₄ = θ[q_H a, ½ + 2q_H b].
  - Another representative changes S_D1 by component phases (see C1).
  - The run below uses this one only.

## Checks of the code, run before this card (disclosed)

- **C0:** with q_H = 0, S_D1's components equal frame C's q-series (te.ev of B1691's B[1]) to 4e-41, at three moduli.
- **C1, which corrects main's own first expectation.** Main expected the up Higgs (+3) and the down Higgs (−3) to
  coincide, and said so to the author before checking. They do not.
  - S_D1(−3) = (e^{iφ}c₀, e^{−iφ}c₁, e^{iφ}c₂) of S_D1(+3), with φ = 2π·3a, to 2.8e-38.
  - That is an overall phase times a relative phase e^{−2iφ} on the second component.

## C2, the selector of the convention, run first in the sealed run

- **The principle.** The coupling's outputs must be covariant, as every pointwise output of frame C is (B1928, B1724):
  the ratios and the |V| at (τ + 1, T·w) must equal those at (τ, w).
- **What is run.** C2 checks this for the declared representative and for the other one (θ₄ = θ[q_H a, −½ + 2q_H b]),
  at three moduli in the bulk.
- **The rule, fixed now:**
  - if exactly one representative is covariant, it is the definition;
  - if both are, the convention is immaterial for the outputs, and the declared one is used;
  - if neither is, the run stops and D1 is reported as undefined in this form.

## The run (`verification/d1_coupling.py --run`; it refuses to run until this card is committed)

- **What it computes:** at the 24 points of order 5, on the column x = 0.13, at heights 6 and 30 (40 + 3.5 Im τ digits):
  - the full |V| = |U_uᴴ U_d|;
  - the up and down mass ratios σ₂/σ₃ and σ₁/σ₃.
- **Where the outputs go:** `verification/d1_outputs.json`, committed before they are read beyond the two printed
  extremes.

## The test, fixed now

The classification is made at height 30:

| outcome | condition |
|---|---|
| **ALIGNED** | every diagonal entry of |V| is at least 0.99 at every point |
| **DERANGED** | at some point every diagonal entry is below 0.01 |
| **PARTIAL** | anything else |

- **No prediction is made.** Main's structural argument for alignment rested on C1's coincidence, which is false.
- **Only ALIGNED lets the frame go on** to the next structural checks (P-860, P-861): the lepton rows and the weight.
  These come before any values look.
- **Height 6 is reported,** not classified.

## Not part of this card

- Any comparison with a measured number.
- The leptons' level (P-845).
- The weight on the surface.
- The web seat's independent construction (W-B2). It may define the overlap differently, and any difference will be
  named when both are in.

## Amendment A1 (2026-11-15, after the sealed run stopped at C2; sealed before its own run)

- **What happened.** The sealed run (`verification/d1_run.txt`, `d1_outputs.json`) stopped at C2. D1 as defined above
  is not covariant under τ → τ + 1 for either representative: the worst differences are 8.0 (+) and 1.6 (−). Frame C's
  own harness, with no twist, gives 3e-16. By the card's rule, D1 is undefined in that form. No mixing output was
  computed.
- **The cause, main's error in the definition.**
  - The card twisted the Higgs's theta constants by (q_H a, 2q_H b), copying twist_of's first leg.
  - Matter's residues do not carry that pair. They combine the two legs into the characteristic
    ((q_L ± q_R)a, (q_L ± q_R)b), with the second component halved (bp = (x₁ + y₁)/2 in the frame's code).
  - Under τ → τ + 1 a theta characteristic moves as β → β + α + ½, and the points move as b → b − a (B1724; checked on
    frame C to 2e-16).
  - Those agree for a characteristic (q a, q b) and disagree for (q a, 2q b), unless q a is an integer.
  - This is derived from the transport rule, not from any output.
- **D1′, the corrected definition.** The Higgs's theta constants carry the characteristic shift (q_H a, q_H b), the
  convention of matter's residues. Everything else in this card stands: the charge q_H = −(q_L + q_R), the Serre
  derivative, no reading, C2 with its rule, and the classification at height 30.
- **The run** is `verification/d1_coupling.py --run --v2`. Its outputs go to `d1v2_outputs.json`.

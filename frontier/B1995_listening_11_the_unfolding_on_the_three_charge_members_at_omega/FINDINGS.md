# B1995 — Listening 11: the whole's unfolding does not tell ω's three charge members apart in strength: each persists alike (2/3 per move), its slowest modes overlap all three equally, and only a faster real mode avoids the neutral member

**Verdict: PROVED (exact; one expectation failed as worded).** Main, 2026-11-25, in the author's /loop "continue the
listening line". Data-free. Register rows P-882 and FK15 (P-694). **0 of 19.**

## Seen first

- **B1994:** ω's own symmetry (the move LR⁻¹) tells the three apart around the common point: one neutral member along
  the opening diagonal, two with conjugate charges e^{±2πi/3}.
- **B1986:** the unfolding on the triplet: W₊ = dL + dR, with eigenvalues 1 and (1 ± i√7)/2; W± with inverses, with
  eigenvalues 2, 2 and 0.
- **Swept** with B1994's and B1986's sweeps. No arc puts the whole's unfolding against ω's charges.
- **The literature:** none needed (exact linear algebra).

## The results (`verification/charges.py`, `charges_run.txt`; exact)

| cell | outcome |
|---|---|
| X1: W₊ does not commute with ω's symmetry | **holds**: the unfolding mixes the charges |
| X2: W± commutes with it | **fails as worded**: it does not. Main's reason (a symmetric sum) was wrong: only two of the cube's three quarter-turn axes are moves |

- **In the charge basis** (rows and columns: neutral, charge e^{2πi/3}, charge e^{−2πi/3}):
  - W₊ has the diagonal **2/3, 2/3, 2/3** and complex off-diagonal mixing;
  - W± has the diagonal **4/3, 4/3, 4/3**.
- **Overlaps of the modes with the charge members:**

  | mode | eigenvalue | overlap with (neutral, charged, charged) |
  |---|---|---|
  | W₊'s complex pair, the slowest to fade (1/√2 per move) | (1 ± i√7)/2 | ⅓, ⅓, ⅓ |
  | W₊'s real mode, faster (½ per move) | 1 | 0, ½, ½ |
  | every mode of W± | 2, 2, 0 | ⅓, ⅓, ⅓ |

- **The long run under W±:** each charge member keeps a share of 2/3 in its top eigenspace, the same for all three.

## What the whole does, read in its own terms

- **ω labels the three; the whole's unfolding does not separate them in strength.**
  - Each member persists alike per move.
  - The slowest-fading structure is spread equally over all three.
  - In the long run each keeps the same share.
  - The unfolding also mixes the charges.
- **The one asymmetry:** the faster real mode lives only on the two charged members and never on the neutral one. So
  the neutral member, along the opening diagonal, is carried only by the slow complex pair.
- **Read in its own terms:** around the common point, the whole is democratic about the three. Their difference under ω
  is a difference of label (charge), not of magnitude. With B1990 and B1992, this adds to the evidence that the
  listening line so far gives structure, not values.
- **No Standard Model shape was asked for or read,** and no hierarchy was looked for.

## What is open

- **Whether anything beyond the common point's linear neighbourhood separates the three in magnitude:** the tower above
  (B1985, B1987), or the analytic field on the shapes' side at ω (B1992).
- **Whether the listening line should now state its synthesis:** what the whole fixes, structure, and what it does not,
  magnitudes.

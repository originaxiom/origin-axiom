# B1973 — The one-doublet mixing trade-off (P-879), settled at its ends by two seats' proofs, verified on main: the coupling's form allows an exactly aligned full hierarchy; frame C's channels forbid it at a null Higgs because up and down share their left charge

**Verdict: PROVED** for the checks P1 to P3, all on main's own code:
- the seats' scripts were not run here;
- P1 is numerical at grid precision;
- P2 is numerical at 40 digits, on frame C's code;
- P3 is exact at 60 digits.

**What it settles in P-879:**
- the form-level question, answered by an exact counterexample;
- the null-Higgs end for frame C's channels, at the points checked.

**What stays OPEN:** a proof for every Higgs between null and real (0 < r < 1). The seat's interval certificate covers
sampled points only.

Main, 2026-11-24. Data-free. Register row P-879. **0 of 19.** The proofs are the seats':
- agy-002's A2-P879 (2026-11-20, with a cold-room referee): T3 and T4(b);
- the agy lane's C1 (2026-11-20): the witness C1-A and the same rank-one residue law.

Main verifies them here and credits them.

## Seen first

- **Swept:** `VERDICT topic-sweep /P-879|pairing invariant|left spinor|s_L|Takagi|channel pairing|trade-off|rank.one residue|shared q_L|Mobius|Möbius/: 27 of 1713 arcs on main match (NEGATIVE 1, OPEN 9, PROVED 16, RETRACTED 1); 12 register rows match (DONE 8, QUEUED 4)`.
  The arcs bearing on it:
  - B1965: the conjecture;
  - B1966: the two ends' exact facts;
  - B1967 and B1969: the form nearly allows it;
  - B1968: frame C's channels never reach it on a grid;
  - B1727: the real-Higgs floor m₂/m₃ ≥ 1/3.
- **The seats' relays to main naming P-879, all read before this arc** (harvest rows 1993 to 1995):
  - agy-002's A2-P879 (read at source by main: the card's T1 to T5 and its custody record);
  - the agy lane's C1 (read at source by main: C1-A and C1-B) and C25 (its review of A2-P879);
  - agy-exp's three-seat synthesis (B-3S-04);
  - the web seat's magnitude ledger (§ 3).
- **The scope, from agy-002's pointer note:** B1964 to B1969 are one-doublet results under the conjugate charge rule.
  Under B1970's two-doublet reading this trade-off does not arise (B1971). P-879 is therefore a statement about the
  one-doublet reading.
- **The literature:** none computes frame C. The bound is an elementary maximisation over unit spinors.

## P1 — T3, the ceiling (`verification/t3_check.py`)

- **The claim (agy-002, T3).** At a null Higgs (r = 0) under the charge rule, the heavy states of the two sectors are
  v(l_u, ε ξ̄) and v(l_d, ξ). Here v(l, ξ) is the triplet part of the rank-one 2×2 operator built from a sector's
  dominant left spinor l and the Higgs spinor ξ. Then

  sup over unit ξ of |⟨v_u | v_d⟩| / (‖v_u‖‖v_d‖) = (1 + s_L)/(3 − s_L),  with s_L = √(1 − |⟨l_u | l_d⟩|²).

- **Main's check.** Main built v from Pauli coordinates, in both orders of the rank-one matrix, and maximised over a
  (t, φ) grid of ξ at s_L = 0, 1/4, 1/2, 3/4, 17/19 and 1. In both orders the maximum equals the formula to grid
  precision: 0.33333, 0.45454, 0.59999, 0.77778, 0.89998 and 1.0, against 1/3, 5/11, 3/5, 7/9, 9/10 and 1.
- **The norm.** ‖v‖² = 2 − |lᵀξ|². The card writes it as 1 + |lᵀεξ|², which needs ξ̄ for ξ: a notational slip in the
  card, not in the theorem.
- **So:**
  - alignment |V₃₃| ≥ 9/10 at a null Higgs needs s_L ≥ 17/19;
  - with a shared left spinor (s_L = 0) the ceiling is 1/3.

## P2 — T4(b), the shared left charge (`verification/t4b_check.py`)

- **The claim (agy-002 T4(b); the agy lane's C1-B).** Up (1, −4) and down (1, 2) share q_L = 1. So their residue
  matrices M_res = Σ_s R_s E_s, before frame C's Theorem-90 channel weights, are rank one with one shared left spinor.
- **Main's check.** Main ran this on frame C's own code (B1945's `parts`, the weights removed), at 30 points (all 24 of
  order 5, plus points of orders 3, 4, 6, 7 and 8), at heights 2 and 6, column 0.13:
  - μ₂/μ₁ ≤ 8.5e-40, and s_L ≤ 1.1e-20;
  - with frame C's weights restored, s_L ≤ 0.387. agy-002 reports 0.388 at height 2.
- **So at a null Higgs frame C's channels allow at most (1 + 0.387)/(3 − 0.387) = 0.531.** That is far below 0.9 at
  every point checked. The nonzero s_L comes only from the weights.
- This is the structural reason B1968 found no aligned hierarchy near a null Higgs, where its searches found "no single
  channel invariant" that explains the floor: the invariant is the pairing s_L.

## P3 — C1-A, the form-level witness (`verification/c1_witness.py`)

- **The claim (the agy lane, C1-A).** In the null triad e± = (1, ±i, 0)/√2, e₃, take a unit h = c₊e₋ + c₋e₊ with
  2c₊c₋ = r = 1/2000. With w = 0, u_down = e₊ + (4/1000)e₋ and u_up = (1/80000)e₊ + e₋, B1736's coupling gives an
  exactly aligned mixing with a full hierarchy.
- **Main's check, at 60 digits:**
  - **Under the one-doublet charge rule** (up reads h̄, down reads h), which is B1969's question:
    - the least diagonal |V| is 1.0, and the largest off-diagonal entry is 3e-60;
    - up m₂/m₃ = 1/2000 and m₁/m₂ = 1/20;
    - down m₂/m₃ = 8/1000 and m₁/m₂ = 1/16;
    - this is inside B1969's bars: heavy pairs at most 1e-2, light pairs at most 0.1.
  - With every sector reading h, the same channels derange the mixing. That is not the question here.
- **So the coupling's form forbids nothing.** B1969's "within a factor of about 2" becomes an exact counterexample. Any
  exclusion must come from the frame's channels, which is P2.

## What it means

- **P-879, the one-doublet trade-off, is now settled at its two ends.**
  - At a null Higgs, frame C's channels cap the alignment at 0.531 at the points checked (P1 and P2).
  - At a real Higgs, B1727's floor m₂/m₃ ≥ 1/3 holds.
  - The form itself allows everything (P3).
- **The reason is structural:** the up and down quarks share the left-handed doublet's charge, so their channel residues
  have one left direction. Only the channel weights separate them, and not by enough.
- **For the two-doublet reading** (B1970, B1971) the same shared left charge is what makes the mixing align. The two
  results are one fact seen from two readings.

## What is open

- **The interior 0 < r < 1.**
  - T3 is proved only at r = 0. A bound that holds for every r, or continuity in r with the error controlled, is owed.
  - agy-002's T5 interval certificate covers its sampled points, on a weaker criterion than B1968's. It is not
    reproduced here.
- **s_L over all points and heights.** Main checked 30 points at two heights; agy-002 reports that s_L decays with
  height.

# W132 — the edge's twenty-fourths and the SU(2) remainder: can consistency of the moves' phases force the unit at the cusp, and what absorbs the remainder that never closes? (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Two of the tests the seat named after W129, taken together because they are one arithmetic.**
  - Must the edge's phases, each an odd number of twenty-fourths, close into a whole unit, and so force GENESIS FK10's
    unit?
  - B1674 found the moves' mixed anomaly with SU(2) never free: 6, 12 or 18 twenty-fourths. Which field absorbs it?
- **The owner's question behind both:** can a cancellation that does not complete generate a field? The owner asked
  this seat to finish these without waiting on the other seats (2026-10-22).

## The objects

- **B1674's character layer, with twists.** Each Standard Model field f carries T (s_f = +1) or T̄ (s_f = −1),
  optionally twisted by an allowed character ε_{r_f}, r_f ∈ {0, 4, …, 20} (W47 K1).
  - Its determinant character is χ_η^{9s_f + 3r_f}.
  - The moves' anomaly with G ∈ {SU(3), SU(2), gravity} is n_G = Σ_f w_G(f)·(9s_f + 3r_f) mod 24, with W101's
    weights w.
- **Copies.** With n uniform units the chiral content is 3n generations (W46): n copies of the content B1674 reads.
  So every n_G scales by n. This is the reading used here, and it is stated, not derived.
- **Absorbers of a remainder.**
  - **(i) τ's counterterm.** The Dedekind factor η^m carries χ_η^m (Dixon, Kaplunovsky and Louis). A counterterm
    built on η^{−n_G} absorbs any remainder.
  - **(ii) A Higgs-like pair.** Two flavour-singlet weak doublets with Y = ±½ and characters χ_η^{m_u}, χ_η^{m_d}, as
    fermions. They add m_u + m_d to n_SU2 and 2(m_u + m_d) to n_grav, and they are vector-like in Y.
  - **(iii) A twist.**
- **The unit.** O(δ) = Δ⁻¹ = η⁻²⁴ has trivial multiplier.

## Weave or thread

**WEAVE-type.** The whole group the moves generate, every one of B1674's 64 sign assignments, every allowed twist,
and the copies n = 1 to 8.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| G0 | the instrument: B1674's per-copy layer reproduced (SU(3)-free = {s_u = s_d = −s_Q}, 16 of 64; SU(2) values {6, 12, 18}; gravity-free among the SU(3)-free iff s_e = s_ν = −s_L, 4 of 16). η(τ + 1) = e^{iπ/12}η(τ) and η(−1/τ) = √(−iτ)·η(τ) at three points to 10⁻³⁰. Δ = η²⁴'s multiplier is trivial | 97% |
| G1 | the unit is phase-blind (exact): dressing any field by O(nδ) changes no n_G. No condition on the twenty-fourths sees the unit through the field's own phase | 99% |
| G2 | copies (exact): with no absorber and no twist, n·n_SU2 ≡ 0 (mod 24) needs n even when n_SU2 = 12 (s_Q = s_L), and n ≡ 0 (mod 4) when n_SU2 ∈ {6, 18} (s_Q = −s_L). So n = 1, three generations, never closes SU(2). On B1674's free sets, SU(3) and gravity close for every n | 95% |
| G3 | twists (exact census over 64 sign assignments × 6⁶ twists, at n = 1). A twist by r ≡ 4 (mod 8) adds 12 to a field's phase; by r ≡ 0 (mod 8), nothing. Free in SU(3), SU(2) and gravity at once is possible for exactly 8 sign assignments: s_Q = s_L, s_u = s_d = ±s_Q and s_e = s_ν = ±s_L. Each needs an odd number of {Q, L} twisted by r ≡ 4 (mod 8); for u, d (and for e, ν), an even number when the sign is opposite to Q's (L's) and an odd number when it is the same. None with s_Q = −s_L. Every twist used can be ε₁₂, which keeps the count three at every puncture condition (t₁₂ = 0, W47); ε₂₀ keeps it at 0 and V4, ε₄ at V2 and L6. On B1674's four SU(3)- and gravity-free assignments, the two with s_Q = s_L become fully free with ε₁₂ on exactly one of Q and L | 85% |
| G4 | τ absorbs every remainder (exact): χ_η^m on S and T is (e^{−iπm/4}, e^{2πim/24}), so the counterterm η^{−n_G} cancels n_G for every assignment and n, with no condition on n | 97% |
| G5 | a Higgs-like pair (exact): it closes SU(2) at n = 1 and keeps gravity closed iff n_SU2 = 12 (s_Q = s_L), with m_u + m_d ≡ 12 (mod 24). For s_Q = −s_L no such pair keeps gravity closed | 90% |
| G6 | the read-out: the table of what closes at n = 1, per assignment and absorber; the least n that closes without an absorber | — |

## What the outcomes mean (fixed now)

- **G0 to G5 hold.** Then:
  - **Consistency of the twenty-fourths does not force GENESIS FK10's unit.** The unit carries no phase.
  - **If the moves are a gauged symmetry with no absorber,** the SU(2) remainder forbids n = 1. So three generations
    then require an absorber:
    - τ's counterterm, always;
    - or, when s_Q = s_L, a sign twist on one doublet field (ε₁₂, keeping three), or a pair of weak doublets with the
      Higgs's quantum numbers.
  - **A READING.** Here a cancellation that does not complete does generate a field. It is τ, or a pair with the
    Higgs's quantum numbers in half the assignments. It is not the unit.
  - **If the moves are only a global symmetry,** none of this binds (B1674).
- **G3 differs from the predicted 8.** The census is recorded as found, with its structure.
- **G2 fails.** The copies reading is wrong, and it is recorded.

## What stays out

- The U(1)_Y-moves mixed anomaly, which B1674 did not compute, and the pair's contribution to it.
- Whether the moves are gauged. Whether the pair is fermionic (supersymmetric).
- Twisting by characters that do not keep the forced weights.

## Seen before the rule (disclosed)

- **Read:** B1674's findings, W101's weights, W46, W47 (t_r), W128's C0.
- **By hand:**
  - n_SU2's values per sign assignment;
  - the twist arithmetic (3r ≡ 0 or 12 mod 24, and each field's weight times 12);
  - the eight-assignment structure in G3;
  - G5's condition.
- **Not run:** no census has been computed.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.

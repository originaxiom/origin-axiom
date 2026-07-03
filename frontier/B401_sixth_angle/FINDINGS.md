# B401 (W-C, the owner's sixth angle) — session 1 BANKED: the class group is load-bearing

**Status: P1 + P2 + the falsifiable prediction banked; P3/P4 next session. Prereg
committed first. Firewalled — arithmetic of the level-15 model and of ℚ(√−15) only.**

## The frame (textbook anchors, cited not claimed)

disc(ℚ(√−15)) = −15, h = 2; the genus field = the Hilbert class field = ℚ(√−3,√5) = H —
**the seam field IS the class field of the field the seam constant generates**; the genus
characters χ₋₃·χ₅ mirror the program's CRT tensor split.

## P1 — the class-group action on the banked constants (exact)

σ_cl: (x,y,z,s) ↦ (x,−y,−z,s), the lift of Gal(H/ℚ(√−15))'s generator:
- **slot ↦ −(3-block)** — the P60 "two Galois faces" are the ℤ/2 CLASS GROUP acting;
- **B382's bonus face (0,0,+1/24,−1/24) ↦ B397's face (0,0,−1/24,−1/24) EXACTLY** — two
  independently banked constants are ONE class-group orbit;
- **the falsifiable consequence CONFIRMED:** the 3-block's det-class split is the exact
  σ_cl-conjugate of the slot's — class-1 → (0,0,−1/16,+1/16), class-5 → (0,0,−1/48,+1/48),
  classes 3/15 silent (p1_prediction.json). The 1/12's fine structure is class-group
  covariant.

## P2 — prime spectroscopy (the table banked; the naive bet KILLED honestly)

By ideal class in ℚ(√−15): **2 non-principal · 3,5 ramified · 7 inert · 23 NON-PRINCIPAL ·
11 inert · 13 inert.** The registered sorting bet ("seam-channel primes are
non-principal-or-ramified") is KILLED by 7-inert sitting in the bright (3,4) Gram spectrum
({7,5}/2304). Notable control: 11 (inert) appears ONLY in the killed numerology (6/11).
The table stands as data; the class-sorting of channels needs a finer statement (P3's
genus-character assembly is the natural candidate).

**Provenance.** p1_p2_class.py, p1_prediction.py → two JSONs; locks
tests/test_b401_sixth_angle.py.

---

# Session 2 BANKED: two genus selection rules + the exact-identity dossier

## P3 — the genus characters refine the 1/12's fine grain (exact)

Splitting the generic (class-1) slot partial by (χ₅, χ₋₃) of det(γ′−I):

    (χ₅,χ₋₃) = (+,+): (0, 0, 0,     −1/120)   18 cells
               (+,−): (0, 0, −1/24, −1/60)    68 cells
               (−,+): (0, 0, 0,     −1/80)     8 cells
               (−,−): (0, 0, −1/48, −1/40)    48 cells

- **RULE 1 (the Eisenstein gate): the √−3-component vanishes identically on χ₋₃ = +1** —
  the z-channel is gated by the Eisenstein character of the fixed-point determinant.
- **RULE 2 (boundary equipartition): the class-5 partial splits χ₋₃-EVENLY —
  (0,0,−1/96,−1/96) from 4 cells and the same from 64 cells** — exact aggregate balance
  across a 16-fold population asymmetry (the emergent signature at the boundary).
  (Recombinations: z: −1/24−1/48 = −1/16 ✓; s: −(2+4+3+6)/240 = −1/16 ✓; class-5 halves
  sum to −1/48 ✓.)

## P4 — the exact-identity dossier (each item exact; classical facts cited, not claimed)

- **The component basis IS the Gauss-sum basis:** {1, √5, √−3, √−15} =
  {1, g(χ₅), g(χ₋₃), g(χ₋₁₅)} — the program's H-decomposition has been the genus-character
  decomposition of ℚ(√−15)'s class field all along; the banked S-normalizer g(15) = √−15
  is the seam character's Gauss sum.
- **The dynamics computes the regulator:** the banked Lyapunov data (B109: exponents
  ±4 log φ at the void) = 4·Reg(ℚ(√5)); by Dirichlet, = 2√5·L(1, χ₅) — the golden pillar's
  entropy is the real genus character's L-value (classical: cat-map entropy = log of the
  fundamental-unit power; cited).
- **The seam character carries the class number:** L(1, χ₋₁₅) = 2πh/(w√15) = 2π/√15 with
  h = 2, w = 2 — the ℤ/2 that acts on the banked constants (P1) is the same h = 2 in the
  seam character's L-value.
- ζ_H = ζ·L(χ₋₃)·L(χ₅)·L(χ₋₁₅): one factor per program pillar (twist / dynamics / seam).

**Provenance.** p3_genus_refine.py → p3_genus.json; the P4 identities are closed-form
(no numerics); locks tests/test_b401_sixth_angle.py (P3 section).

---

# Session 2 addendum: RULE 1 UPGRADED TO A CELL-WISE LAW

Prompted by the Chat-1 synthesis (character-orthogonality reading), tested and found
STRONGER than proposed: **every class-1 cell with χ₋₃(det(γ′−I)) = +1 is individually
ℚ(√5)-real — z = 0 AND s = 0 on all 26 such cells** (rule1_cellwise.json). The Eisenstein
gate is not an aggregate selection rule but a LOCAL law of the metaplectic character's
field content: the 3-side Gauss sum (hence any √−3) enters χ only at non-residue
determinants. This is the first genus rule with a cell-level mechanism — a derivation
target one step from closed (the character field-content argument, classical Gauss-sum
arithmetic).

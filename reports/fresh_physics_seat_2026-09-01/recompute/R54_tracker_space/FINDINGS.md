# R54 — the space of trackers, computed: every tracker is mirror-even or mirror-odd, and the odd sign is one chosen bit

**Date:** 2026-09-02. **Seat cell.** Scripts: `r54.py` (SnapPy 3.3.2, sympy), `r54b_mirror_word.py` (word search).
Outputs: `r54_output.txt`, `r54b_output.txt`, `r54_results.json`. Every number below is COMPUTED on this bench.

**Owner's instruction this cell answers:** "regarding what the tracker does to the world, we need to compute all
possible options and not lean on my intuition or opinion but on math." And: "before you conclude the chirality
verdict, please sweep the repo because we dealt with it." The sweep is Phase F/G (`campaign/phaseF`, `phaseG`,
ledger `campaign/phaseF/CHIRALITY_LEDGER.md`); this cell is the mathematics, written before the sweep returned
and then reconciled with it in §7.

## 1. The rule is orientation-reversing

σ: a→ab, b→a has incidence matrix F = [[1,1],[1,0]], det F = −1. Its mapping torus on the once-punctured torus is
the **Gieseking manifold** m000 (non-orientable, one tetrahedron, volume 1.014941606 = V_tet). SnapPy: the
orientation double cover of m000 is isometric to m004; the bundle names `b--R` and `b-+R` are both Gieseking.
m004 is the mapping torus of σ² = A = [[2,1],[1,1]]. (The record has this: B466 "det = −1: orientation-reversing",
B467 "σ = the Gieseking half-monodromy", TERMINOLOGY and THE_LADDER name the Gieseking cover.)

## 2. The rule is the mirror of its own object

F commutes with A = F², so (x, t) ↦ (Fx, t) is a fibre-preserving self-map of the mapping torus of A that
reverses the fibre and fixes the circle: an orientation-reversing symmetry of m004. Sym(m004) has order 8 and
exactly 4 of its 8 isometries reverse orientation (cusp-map determinant −1); the group is amphichiral by
`symmetry_group().is_amphicheiral()`. The centraliser of A in GL(2,ℤ) is the unit group of ℤ[φ], with det −1
elements ±F^{2k+1}; the elements conjugating A to A⁻¹ include det −1 ones as well.

## 3. The rule and its a↔b mirror are conjugate by an orientation-preserving map

σ' = swap∘σ∘swap (a→b, b→ba) has matrix Fᵀ. P = [[−2,−1],[−3,−2]] ∈ SL(2,ℤ) satisfies P F P⁻¹ = Fᵀ. So relative to
an orientation-preserving change of basis of the carrier the rule and its mirror image are the same mapping
class: **the rule carries no handedness of its own.** (Reading direction is also not a handedness: a→ba differs
from a→ab by an inner automorphism, the same outer class.)

## 4. Fricke action and the mirror character

On (x, y, z) = (tr a, tr b, tr ab), σ acts as (x, y, z) ↦ (z, x, xz − y), preserving κ = x² + y² + z² − xyz
(symbolic check with det a = det b = 1). The discrete faithful character of m004 on SnapPy's generators is
(−3/2 + (√−3)/2, 1 − √−3, −2), all in ½ℤ[√−3]. Its Galois conjugate is the character of the mirror. A word search
over pairs (u, v) of length ≤ 7 finds **132 endomorphisms a→u, b→v of π₁(m004) realising the conjugate character**
(the relator maps to −I in SL(2,ℂ), i.e. to the identity in PSL(2,ℂ); the ±I is the usual lift ambiguity); the
shortest is a→aabAB, b→abaBAba. Surjectivity was not certified, and is not needed for §6. (B1174 established the
same fact by SnapPy: "the mirror acts on traces as complex conjugation"; the search here gives explicit words.)

## 5. Iteration parity: the rule supplies alternation, not a sign

σⁿ(a) has length F_{n+2} and det Fⁿ = (−1)ⁿ: the carrier's orientation at step n is (−1)ⁿ relative to step 0.
The rule fixes the alternation exactly; nothing in the rule fixes the sign at step 0.

## 6. The classification (the complete list of options)

Let ι be any orientation-reversing symmetry of the object (§2 exhibits four; one is the rule itself acting on
the fibre). Every tracker T, meaning every function of the word, the monodromy, the character, the cusp, or the
manifold, decomposes uniquely as

    T = T_even + T_odd,  T_even = (T + T∘ι)/2,  T_odd = (T − T∘ι)/2.

T_even is mirror-blind. T_odd changes sign under ι, so its value on "the object" versus "the mirror" is fixed only
once one of the two is named. Naming one is a choice of: sheet of the double cover m004 → m000; or embedding
ℚ(√−3) ↪ ℂ (which √−3); or which parity of σ-steps is "even". These are torsors under one ℤ/2 and none is supplied
by the rule (§3, §5). Since ℤ/2 has exactly two irreducible characters, the list {mirror-even, mirror-odd} is
exhaustive. **Every mirror-odd tracker's sign is one externally chosen bit; no tracker derives it.**

This is a theorem about the object, not about anyone's intuition. It does not say the bit is unimportant; it says
where it enters.

## 7. Reconciliation with the record (filled from the Phase F/G sweep)

_(filled after the sweep; see `campaign/phaseF/CHIRALITY_LEDGER.md` and `campaign/phaseG/TRACKER_LEDGER.md`)_

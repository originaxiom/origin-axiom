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

## 6b. Beyond the mirror: the full symmetry group (r54e)

Sym(m004) has 8 isometries (SnapPy), 4 orientation-reversing (cusp-map determinant −1). The cusp image of the group is
(ℤ/2)² = ⟨mirror, flow reversal⟩ (the two isometries with cusp map I are the kernel). The bundle is invertible: A ↦ A⁻¹
is realised by orientation-preserving fibre maps (e.g. [[−3,−2],[5,3]]) and by orientation-reversing ones (e.g.
[[−1,0],[1,1]]); the mirror commuting with the flow is e.g. [[−1,−1],[−1,0]] = −F. So a scalar tracker transforms under one
of the four linear characters of D4 (mirror-parity × time-reversal-parity) or is a doublet under its 2-dimensional
irreducible representation. That is the complete list of options; each odd factor costs one chosen bit, a doublet one
labelling. The SL/PSL central lift sign θ (B585, B766) is a third bit belonging to the representation, not the manifold.
(Caveat on the script: the abelianization it prints is of the cusp-image group (ℤ/2)²; D4's own abelianization is also
(ℤ/2)², so the count of linear characters, 4, is the same.)

## 7. Reconciliation with the record (from the Phase F/G sweep; ledgers in `campaign/phaseF`, `campaign/phaseG`)

The record had already established every load-bearing statement of this cell: σ is orientation-reversing and m004 is the
double tick (B466, B467, B1083, B1234); the rule is a basepoint on a free K4-torsor with swap = C and reversal = P (B1083);
the mirror is complex conjugation on ℚ(√−3) (B1174, B8154, B289); no object-canonical datum can orient m004 (B1163 theorem);
mirror-even is the object's, mirror-odd is the observer's (B1168, B1169); the closing lattice has rank 3 = {c, θ, γ5}
(B766); the observer's discretion is two bits + one dilaton (B1164, B1166). This cell's §6 was written before those arcs
were read and coincides with B1169's core; §6b coincides with B766. The seat's additions are: the SL(2,ℤ) conjugator
between the rule and its mirror (§3); explicit words realising the mirror character (§4, 132 pairs); the language-level
check that the 2-letter rule has no reading arrow while the 4-letter rule has (r54d); and the character-table form of the
exhaustive list (§6b). Defects surfaced by the sweep (B571/B572 wording, B723's verdict file and the LAW_MAP row, the
B1181/B1186 instrument, B783's γ5 typing) are in the chirality ledger, F1–F9.

**Verdict.** The record's chirality position STANDS and is a theorem. The owner's belief is correct for the even part and
the torsors and needs three declared bits and one scale for the rest; the record has priced exactly those.

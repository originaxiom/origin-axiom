# B488 — the DGG data of the metallic family (owner: "do dgg"). Clean gauge/homology laws; firewalled.

**Computed the actual Dimofte–Gaiotto–Gukov data from the ideal triangulations, across the
twist-knot family (where Gang–Yonekura's SU(3) applies) and the metallic bundle family. Two
clean laws for the metallic family; the SU(3) flavor enhancement applies only at m=1. All
flavor/3d — firewalled from the SM (B487).**

## The metallic DGG family — two clean laws (verified m = 1…8, SnapPy)
The metallic bundle M(A_m) = mapping torus of R^m L^m has an ideal triangulation with N = 2m
tetrahedra and one cusp, so its DGG theory is
  **T[A_m] = U(1)^{2m−1}** (gauge rank = N − c = 2m − 1),  with matter/CS from the NZ matrix,
and homology
  **H₁(M(A_m)) = (ℤ/m)² ⊕ ℤ.**
Both verified for m = 1…8 (m=1: U(1)¹, H₁=ℤ; m=2: U(1)³, (ℤ/2)²⊕ℤ; m=3: U(1)⁵, (ℤ/3)²⊕ℤ; …).
The homology torsion (ℤ/m)² is a genuine arithmetic echo of the family: its (ℤ/m) content is
the same divisor-of-m structure that governs the held-breath torsion (B479: member m holds the
breath of every divisor d ≥ 3 of m). The topological symmetry of T[A_m] (carried by H₁) grows
with the metallic index in the family's own arithmetic.

## The twist-knot DGG family (Gang–Yonekura's SU(3) domain)
| knot | tets N | cusps | DGG gauge | H₁ | Gang–Yonekura |
|---|---|---|---|---|---|
| 4₁ | 2 | 1 | U(1)¹ (2 chirals) | ℤ | SU(3) flavor ✓ |
| 5₂ | 3 | 1 | U(1)² | ℤ | SU(3) flavor ✓ |
| 6₁ | 4 | 1 | U(1)³ | ℤ | SU(3) flavor ✓ |
| 7₂ | 4 | 1 | U(1)³ | ℤ | SU(3) flavor ✓ |
| 8₁ | 5 | 1 | U(1)⁴ | ℤ | SU(3) flavor ✓ |

All hyperbolic twist knots get SU(3) FLAVOR enhancement (a global symmetry of the 3d N=2 SCFT),
not a gauge symmetry — the gauge group is the abelian U(1)^{N−1}.

## The intersection, and the honest verdict
The two families meet ONLY at 4₁ (the figure-eight = the m=1 metallic bundle = a twist knot).
For m ≥ 2 the metallic members are BUNDLES (m136, s464, …), NOT twist knots, so Gang–Yonekura's
SU(3) theorem does not apply to them; their flavor enhancement (if any) would need the criterion
worked out per member from the boundary/homology data — an open computation, not a banked SU(3).
So "the metallic family gives SU(3)" is true only at m=1; the family's genuine DGG signature is
the pair of laws above (gauge rank 2m−1, homology (ℤ/m)²⊕ℤ).

**Firewall:** every symmetry here is a flavor (global) symmetry of a 3d N=2 theory; the gauge
groups are abelian U(1)^k. None is the 4d Standard Model gauge group (B487). The metallic DGG
laws are a real, clean mathematical object about the family — banked as mathematics, not physics.
Reproducer: `dgg_family.py` (SnapPy triangulation + NZ data). Sources: Dimofte–Gaiotto–Gukov
2011; Gang–Yonekura arXiv:1803.04009.

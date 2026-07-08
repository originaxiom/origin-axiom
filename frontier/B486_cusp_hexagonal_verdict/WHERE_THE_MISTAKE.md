# Where the "hexagonal cusp" mistake happened — the precise diagnosis

**The intuition was HALF right, which is why it was seductive. The figure-eight cusp lattice
genuinely IS Eisenstein (it sits inside ℤ[ω]) — but the cusp TORUS is a 4-fold COVER of the
hexagonal torus, and covering breaks the ℤ/3 symmetry. "Eisenstein lattice" ≠ "hexagonal torus."**

## The true fact (why "hexagonal" felt right)
The figure-eight cusp modulus is τ = 2√3·i. And **2√3·i = 4ω + 2 ∈ ℤ[ω]** (since √3·i = 2ω+1).
So the cusp lattice ⟨1, 2√3·i⟩ = ⟨1, 4ω+2⟩ is a genuine SUBLATTICE of the hexagonal Eisenstein
lattice ℤ[ω]. The cusp is Eisenstein-arithmetic and is tiled by equilateral triangles — the
"hexagonal" flavor is real at the lattice/tiling level. The figure-eight is built from two
regular ideal tetrahedra (all dihedral angles π/3), so the triangular tiling is right there.

## Where it breaks (the precise error)
The index [ℤ[ω] : cusp lattice] = |det[[1,2],[0,4]]| = **4**. So the cusp torus ℂ/⟨1, 4ω+2⟩ is a
**4-fold COVER** of the hexagonal torus ℂ/ℤ[ω]. And **a cover of a hexagonal torus is not
hexagonal** — the ℤ/3 rotational symmetry does not lift:
- ℤ/3 symmetry ⟺ multiplication by ω preserves the lattice.
- Cusp-lattice elements have ω-coefficient ∈ 4ℤ; ω itself has ω-coefficient 1 ∉ 4ℤ.
- So ω does NOT preserve the cusp lattice → **no ℤ/3 symmetry**; only ±1 (ℤ/2) survives →
  the torus is RECTANGULAR (modulus 2√3·i).

## The degeneracy: downstairs vs upstairs
| torus | length-1 multiplicity | length-√3 | structure |
|---|---|---|---|
| hexagonal base ℂ/ℤ[ω] | **6** (3 up to ±) | 6 | three-fold degenerate ✓ |
| figure-eight cusp (4-fold cover) | **2** (1 up to ±) | — | no degeneracy ✗ |

The three-fold degeneracy (6 shortest vectors, or "3 up to ±") is a property of the HEXAGONAL
BASE ℂ/ℤ[ω]. Seat-1 correctly described the base's degeneracy — and attached it to the wrong
torus. In the actual cusp (the 4-fold cover), those six vectors have SPLIT into different
lengths (1, 3.46, 3.61), because the cover stretches the hexagon into a rectangle.

## The one-sentence mistake
**"The cusp lattice sits in ℤ[ω]" (TRUE — Eisenstein) was read as "the cusp torus is the
hexagonal torus ℂ/ℤ[ω]" (FALSE — it is a 4-fold cover that breaks ℤ/3).** The Eisenstein FIELD
is inherited; the hexagonal SYMMETRY is not. Arithmetic ≠ isometry. (Same shape of error as the
S057/S058 kills: a true structural fact used one level too strong.)

This is a genuinely nice geometric remark and belongs in the knowledge room / as a footnote in
the seam paper: the figure-eight cusp is an index-4 Eisenstein sublattice torus — triangle-tiled
but rectangular, its ℤ/3 spent on the covering.

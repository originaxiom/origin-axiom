# Chat1/class intake: exact parent, subgroup and representation controls

2026-09-15. Separate pre-execution design, not an R/B allocation or a
change to R31. Commit and push this design, producer and tests before
their first execution. Preserve every failure; repairs need a separate
seal. Do not touch the repository during scientific runs.

The owner proposes PSL(2,O_3) as the parent object, with m004, m202 and
s959 at indices 12,24,36. The useful question is explicit covering and
descent, not whether a torsion-free manifold group literally contains
3-torsion. A class, a chosen lattice, its orbifold and a cover are
different types. The test does not select a physical parent or cover.

## Prior and read boundary

The entire supplied assembled-picture document and all 28 scripts were
read personally. No packet script has been executed; this independent
control does not claim to reproduce all its censuses. Packet SHA256:
2ee56067221a1377140beb8c06df32fa8f455d13200761dc6b0a0b2d4be933a1.

B727's entire FINDINGS.md and verdict were reread. It already discusses
Bianchi torsion and the 2T/McKay construction; neither is claimed as new
or as three independent pieces of evidence. Its genericity calculation
does not establish an arbitrary physical no-go. R15/R19/R20/R30/R31
remain on their own specified models. R31's all-reference custody is
available but its keyword scan is NOT a novelty scan of this topic.
No assertion of whole-corpus absence is made here.

Primary sources personally inspected at the stated points, not claimed
as full-paper reading in this intake:

- Fominykh et al., A census of tetrahedral hyperbolic manifolds,
  https://arxiv.org/abs/1502.00383; author PDF dated October 6, 2015:
  introduction, section 3.1's m202 identification and sections 4.2--5.4.
  Lemmas 5.1--5.2 and Remark 5.5 supply the arithmetic and two-coloring
  criterion. PSL's orbifold two-covers PGL's, which two-covers the full
  regular tessellation orbifold. A regular tetrahedron has 24 barycentric
  chambers, so PSL covolume is v3/6. Two-colorable orientable regular
  n-tet triangulations thus provide index 6n covers of PSL. Integer volume
  ratios ALONE are not subgroup certificates. A failed coloring tests
  that tessellation's map, not every possible embedding of a manifold.
- Neumann--Reid, Arithmetic of Hyperbolic Manifolds, section 4,
  Proposition 4.4: imaginary-quadratic invariant trace field AND integral
  traces characterize cusped arithmetic lattices. Field alone is not enough.
- Donagi et al., The Spectra of Heterotic Standard Model Vacua,
  https://arxiv.org/abs/hep-th/0411156, section 2, equation (35), checked
  visually in the PDF to retain bars. The 27-dimensional adjoint grade
  (3,3,3) is not the fundamental 27 restriction, which is a sum of three
  bifundamentals. This is a representation check, not a new SM derivation.
- SnapPy 3.3.2 official documentation for canonical_retriangulation and
  gluing_equations; installed hyperbolicity.py's logarithmic equation
  convention was read. Verified canonical retriangulation can use exact
  arithmetic for non-tetrahedral canonical cells. No unverified symmetry
  call is promoted to a certified result.

## Fixed controls and expected signs

1. Use integer pairs a+b*z with z^2=z-1 for O_3. Matrices
   A=[[0,1],[-1,1]] and B=[[0,1-z],[-z,0]] have determinant one,
   A^3=B^2=-I. Close their matrix group (hard stop at 96 elements).
   Check order 24, center {I,-I}, and its 12 distinct even permutations
   of {0,1,z,infinity}. This explicitly realizes binary tetrahedral
   isotropy over the parent's regular tetrahedron, not a selected
   physical E6 gauge algebra. The order-three projective A is present
   in the parent independently of any manifold's normalizer.
2. At the actual census triangulations of m004,m202,s959,s958 and the
   published negative-coloring control otet06_0000, record all integral
   gluing data, face inverse checks, row lengths and logarithmic sums.
   With every shape z, z'=z''=z, each edge row must sum to 6 and every
   complete peripheral row to 0. All shapes have positive imaginary part.
   This is an exact regular-shape certificate for the named triangulation,
   not agreement with floating-point volume. Test graph connectedness and
   two-colorability and publish an actual coloring or conflict. Expect
   the owner's three indices if the actual graph and shape tests pass;
   record s958 without preassigning its PSL status. The specified
   otet06_0000 tessellation should reject a PSL coloring.
3. Independently run --canonical under Sage: certified canonical
   retriangulation of m004,m202,s959,s958, then exhaustive combinatorial
   self-isomorphisms and exact cusp maps. Expect total symmetry counts
   8,12,12,2 and cusp-fixing rotational C3 counts 0,2,2,0. Report errors
   instead of skipping them. Trace -1, determinant one on each fixed
   cusp implies an order-three affine restriction; pure translations
   are not classified by this test. Non-divisibility of the full count
   by three is a separate absence control. This finds actual symmetries,
   not explicit matrices identifying a chosen parent elliptic with them.
4. For T=diag(1,1,-2) in color, compare the grade's trace(T^3)=-54 with
   fundamental-27 trace zero. Normalizing a color fundamental to anomaly
   +1 gives +9 for a single (3,3,3), -9 for its dual and zero for both.
   This is a four-dimensional left-Weyl representation control only.
   Do not conflate complex grades with four-dimensional chirality.

Tests must reject a malformed inverse gluing, an odd-cycle coloring and
a changed peripheral row. Preserve raw rows, not only success booleans.
Run the native exact controls and their new tests, then the independently
certified canonical geometry mode. No empirical inputs, CS/eta index
identification, complete orbifold fermion action or global chiral index
are claimed. Do not rerun every packet script or call a small targeted
test population a full-repository suite. The sealed R31 result remains
unchanged while this separate intake is tested.

# Paper IV: two literal theorems fail; their defensible cores are narrower

## 1. The scale theorem is false as written

Paper IV says an isometry-type function cannot determine a dimensionful
quantity that distinguishes a finite-volume hyperbolic manifold from its
finite covers.  Its own proof supplies the counterexample:

\[
F(X)=\operatorname{Vol}_{K=-1}(X),\qquad
F(\widetilde X)=dF(X)
\]

for a degree-\(d\) cover.  Normalized hyperbolic volume is an isometry
invariant and does distinguish covers.

The valid physical statement is different: the curvature-\(-1\) isometry type
fixes a normalized dimensionless number, but converting it into a physical
length/area/volume requires an external curvature or unit scale \(L\).  That
is compatible with OA-C1029; it is not the literal theorem in the draft.

## 2. The 14-member family is not exhaustive

The underlying B8128 search stops after zero-based census index 1200.  SnapPy
3.3.2's `OrientableCuspedCensus` contains 212,641 entries.  Paper IV's own
`check_family.py` then hardcodes the 14 names and never gates its computed
field flag; the advertised “regeneration” does not occur.

An immediate witness is `s955`, index 1256, isomorphism signature
`gLvQQadfedefjqqasjj`.  Its six tetrahedra all admit the regular shape
\(q\), \(q^2-q+1=0\).  The vendored integer gluing matrix is certified exactly:
all six edge products and two cusp products equal one.  Thus its complete
regular triangulation has shape field \(\mathbb Q(\sqrt{-3})\), beyond the
paper's cutoff.  The claimed exhaustive 14-member family is refuted.

The 14-row invariant table can remain as a bounded sample.  It cannot prove
that \(H_1\cong\mathbb Z\) is the unique separator on the corrected full
family.  The witness `s955` has \(H_1\cong\mathbb Z/20\oplus\mathbb Z\), so it
does not itself settle that corrected question.  A complete exact field
census and invariant comparison are still required.

Additional fences: tetrahedron count needs a declared triangulation
convention, and a floating tolerance for Chern–Simons zero is numerical rather
than an exact classification.

## Ledger effect

- the literal scale theorem: `REFUTED`;
- exhaustive 14-member family: `REFUTED`;
- unique seven-invariant separator on the true full family: new `OPEN` row;
- OA-C1029 remains the valid, separately proved compactification-scale no-go.

## Certificate

`certificates/r014_paper4_counterexamples.py` uses only the standard library.
It verifies the regular `s955` gluing in exact Eisenstein arithmetic and gives
the normalized-volume counterexample.

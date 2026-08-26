# Paper II's characteristic-zero rung residue closes by torality and one A2 Weyl orbit

## The missing bridge

The charged-side computation gives exact anchors for the specified principal
\(2T\) embedding:

- \(C=\mathfrak e_6^{2T}\) and \(\dim C=4\);
- \(C\) is abelian;
- \(\dim\mathfrak z(C)=12\).

In characteristic zero, the fixed algebra of a finite automorphism group of a
semisimple Lie algebra is reductive.  Since this fixed algebra is abelian,
\(C\) is toral.  It therefore lies in a Cartan, acts semisimply, and admits a
simultaneous weight decomposition.  This supplies the premise silently used
by Paper II's master formula.

Inside rank-six \(E_6\), a four-dimensional torus with 12-dimensional
centralizer has six zero roots: the Cartan contributes 6 and the remaining 6
centralizer dimensions are root spaces.  Those six roots span rank at most 2;
the only reduced rank-at-most-two root system with six roots is \(A_2\).
Thus \(C\) is the annihilator of an \(A_2\) root subsystem.

The new certificate explicitly enumerates every \(A_2\) root subsystem of
\(E_6\), applies the six simple Weyl reflections, and finds one orbit.  Hence
the charged \(C\) arrangement is linearly isomorphic to the rational
\(A_2^\perp\) arrangement already computed on the root side.

## Exact consequence

The rational arrangement has 30 distinct nonzero weights with total
multiplicity 66, 109 flats, and exactly the eleven centralizer dimensions

\[
12,14,16,18,20,26,28,30,36,46,78.
\]

Because every arrangement vector is rational, linear dependence is unchanged
after extension from \(\mathbb Q\) to \(\overline{\mathbb Q}\).  The old
three-prime result is therefore a corroborating route, not the final evidence
grade.  Paper II's paragraph that calls the \(\overline{\mathbb Q}\) result an
open residue is stale and should cite this transfer.

## Scope

This proves the rung spectrum **given the specified principal \(2T\)
embedding**.  It does not repair OA-C0006: the object still does not select
that principal placement.  Nor do centralizer dimensions construct a gauge
theory, vacuum, dynamics or values.

## Certificate

`certificates/r013_rung_transfer.py` is standard-library-only.  It constructs
all 72 E6 roots, all A2 subsystems and their Weyl orbit, then enumerates the
\(A_2^\perp\) arrangement over exact rational arithmetic.

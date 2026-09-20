# B739 recovery: do not downgrade a proof to its later checks

2026-09-20. Correction to section G of the report-guided resweep at
`1bcfbf99`. No upstream scientific file was changed.

## What changed

B8101's functional equation and critical-line tests alone do not identify an
operator. That logical observation is valid. But B8101 explicitly cites
[B739](../../frontier/B739_character_rigidity/FINDINGS.md), which already
contains the stronger scalar function-level identification. Failing to
carry that antecedent into section G risked making completed work look open.
The resweep itself therefore needed one further correction.

The B739 proof block, producer lines 425--565, compares the parent Eisenstein
series with the cover series at the same height. Their leading constant
terms coincide; their difference is L2 and would have negative eigenvalue
for real s>2. Completeness and positivity rule that out; continuation gives
the identity. The paper inputs and limitations are explicit in that block.

An independent algebraic way to check the transfer step is even shorter.
For a finite-index subgroup H of a one-cusped group G, assume the cover
also has one cusp, conjugated to the same infinity. There is one double
coset H\G/G_infinity, hence G=G_infinity H after inversion. Therefore

    (H intersect G_infinity)\H  -->  G_infinity\G

is a bijection. Summands of the scalar Eisenstein series are identical under
this bijection: the full cusp stabilizer preserves the height. Absolute
convergence for Re(s)>2 permits reindexing; meromorphic continuation then
preserves equality. This is a verification of the already-present transfer
mechanism, conditional on the stated inclusion and cusp data, not a new
arithmetic embedding proof. No independent complete arithmetic embedding
certification was run in this follow-through.

## Source and convention check

Sarnak, *The arithmetic and geometry of some hyperbolic three manifolds*,
Acta Math. 151 (1983), pp. 257--260 and 264, gives the scalar spectral
convention and Eisenstein/scattering construction. The PDF's printed
pp. 258--260 and 264 were rendered and visually read; the page-257
restriction to units +/-1 was read in the extracted text. It must not be
silently ignored at discriminant -3.
[Primary PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6343-11511_2006_Article_BF02393209.pdf).

For O=Z[(1+sqrt(-3))/2], the full stabilizer uses six units before passing
to PSL. In the bottom-row enumeration the factor 1/6 cancels the six
associates of each nonzero principal ideal. The c=0 orbit remains a single
term. Thus the constant-term expression in B739 uses translation-lattice
area sqrt(3)/2, not the rotation-divided orbifold cusp area sqrt(3)/6:

    phi(s) = 2*pi/[sqrt(3)*(s-1)] * zeta_K(s-1)/zeta_K(s)
           = Lambda_K(s-1)/Lambda_K(s),
    Lambda_K(s) = (sqrt(3)/(2*pi))^s Gamma(s) zeta_K(s).

This unit bookkeeping and transfer explain why the earlier proof is
stronger than B8101's functional-equation test. Rescaling height changes an
entire zero-free normalization factor; equalities here use the same height.
The nonuniqueness example exp(c(s-1)) in section G is not a refutation of
B739 with its fixed normalization and actual Eisenstein series.

## What was rechecked, and what was not

Unchanged command: `python3.12 -m pytest -q tests/test_b739_rigidity.py`.
Python 3.12.1 with SnapPy available: **3 passed in 1.30 s**, exit 0.
The tests cover the four-class Fourier sum, residue/volume triangle and
single-cusp count. They do not by themselves prove the infinite spectral
theorem. The full long B739 producer was read at its relevant proof and
convention blocks, not rerun; the entire 43-page Sarnak paper was not read
in this follow-through. Browser screenshots failed; local rendering of
the public PDF succeeded. There was no independent specialist review.

These are scalar weight-zero results. Spin-2 and ghost bundles, twisted
scattering matrices, boundary prescription, zero modes and regularization
still require their own matching before a gravitational determinant is
assembled. The mathematical result is reusable; a physical TOE does not
follow from it.

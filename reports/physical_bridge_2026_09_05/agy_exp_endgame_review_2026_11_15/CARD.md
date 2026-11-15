# Independent checks of X-ENDGAME

2026-11-15. Source head
`b05424e99c85791ba3d37614b9b80a8b69af364b`.
Previous reviewed head `d6f77f7ff74b9c9e359fac764e6f363262fffa5e`.
The five result notes and selected deciding source blocks have already
been read. These expectations are recorded after that reading and before
writing or executing the independent numerical checks.

The current request directs a renewed verification while main is
unavailable. For this review, that is interpreted as authorization for
bounded preliminary mathematical checks on the existing claims. The
outputs will be shared unbanked. Main's review and banking remain owed.
The older two physical packets retain M5's refusal and execution status.

## Deliverables

A separately written checker, its source seal, preserved first output,
a source-and-mathematical review and a repository relay. The checker
uses standard Python plus mpmath 1.3.0 in CPython 3.12.1. It imports
none of the reviewed branch's code. The known default Python 3.9 lacks
mpmath under isolated startup, so the installed 3.12.1 interpreter is
the declared runtime. That discovery happened during metadata inspection.

## Deciding questions and expected outcomes

1. Build the ordinary cellular mapping-torus chain complex for a
   punctured-torus fibre and compare it with a closed-torus fibre.
   Expect H2=0 and torsion-free H1=Z for the former, hence ordinary
   H^2=0. A claimed nonzero fibre or single-boundary-torus Chern number
   needs a filling, boundary framing, relative interpretation or source.
   The closed-fibre comparison should retain H^2=Z. Reversing the
   determinant or dropping the closed-fibre two-cell must be detectable.
2. Recompute the M/J orders, fixed points and orbit counts with exact
   integer arithmetic, independently of the branch's enumerator.
   Expect 45 points, decomposed as 1+4+8+32, and the O32 orbit-count
   list (8,4,4,2,16). A degree-two control should have five fixed points.
3. Recompute the level-three Weil commutator in high precision.
   Expect order four. This is conditional on the supplied degree and
   representation. Bundle gluing permits nontrivial monodromy.
4. Construct the puncture-jet tensors independently from theta sums
   and divisor-sum Eisenstein series. Test the supplied unit-coefficient
   Majorana matrix, and vary one relative coefficient while keeping
   the same modular tensor types. Expect the same covariance with
   changed singular-value ratios. A rank-two control must lose rank.
5. Conjugate the right-acting equations of Luo–Xiao, equations 1, 6
   and 7, into the campaign's left-acting Yukawa convention before
   comparing ordered mixed products. Test noncommuting rational
   matrices and the observable Tr(Hu Hd). Expect the published
   right-action and its conjugate to agree, and the order-preserving
   transcription to differ. A commuting control must hide this error.
   Check the claimed Barger–Berger–Ohmann citation against the actual
   equations. Preserve any convention ambiguity found.
6. Recompute gluing, cusp derivative, volume stationary point and
   classical area/collar formulas through independent equations.
   Expose the coefficient dependence A*=sqrt(2)*pi*|I|/sqrt(c) when
   S(A)=c*A+2*pi^2*I^2/A and c=1/2, |I|=3 gives A*=6*pi.
   The first uncommitted card draft had a factor 2 in place of sqrt(2)
   in the general expression. Differentiation corrected it before this
   seal and before implementation. The special value 6*pi is retained.

## Limits and failure handling

The run is limited to two minutes and creates a fresh run directory.
Preserve the first exception, output and source hashes. A mismatch
produces a dated amendment and a fresh run. No previous output is
overwritten. Mathematical counterexamples are expected findings.

The checks address consequential premises. The full branch's overlap
quadratures, torsion computations, complete running trajectories and
physical parameter claims remain separate verification duties. Target
data, fitted values and the full prediction vector are excluded from
this check. Numerical covariance alone cannot select an action or a
physical domain.

# F03: radial infinite-energy growth is not enough

2026-09-20. The rank-two nonsplit candidate faces a stronger, precisely
scoped constraint than the finite-energy test: **a smooth source-free global
harmonic map with its actual peripheral translations cannot have slowly
varying Busemann height across the cusp torus.** Allowing radial growth
alone does not evade the obstruction; the required positive flux drives
finite-distance blow-up.

This is an authored analytic result with exact controls, not an independent
expert certificate. It does not exclude arbitrary angle-dependent solutions,
independent rank-four harmonic metrics, or coupled source realizations.
The physical TOE goal and the physical chirality question remain open.

[Design](DESIGN.md), [full argument](PROOF.md), [test source](test_verify.py).
Design, proof and controls were sealed at `eb9fee27` before first execution.
**19 tests passed in 3.16 s**, with one non-scientific optional-GUI warning.
All four sealed digests still match. [Execution boundaries](RECHECKS.md).

## What the result actually says

Use the complete one-cusped hyperbolic base, the marked rank-two m010
representation and a smooth source-free equivariant harmonic map to H3.
Its unit-modulus diagonal image preserves the target Busemann height b.
Let Bbar(r) be b's average over the cusp torus and
Omega(r)=Bbar(r)-min_T b. The source cusp metric is
dr^2+exp(-2r)h0, with reference torus area A0 and diameter D0.

The already-known positive global flux, Q0>0 at some compact truncation,
forces Bbar to grow at least Q0 exp(2r)/(2A0), up to an additive constant.
The nonzero peripheral translation supplies the new inequality

    Bbar''-2Bbar' >= K exp(2r+2Bbar-2Omega),   K>0.

If the minimum remained a positive fraction of the growing mean, this would
force Bbar'' >= kappa exp(p Bbar) with Bbar'>0. A directly integrated
comparison shows blow-up at finite r. Hence any hypothetical global solution
must instead satisfy

    limsup Omega/Bbar >= 1,
    limsup exp(-2r) Omega >= Q0/(2A0),
    limsup exp(-3r) sup_T |df| >= Q0/(2A0 D0).

These are necessary growth bounds along a sequence, not constructed
asymptotics or bounds at every sufficiently high torus. In particular,
Omega=o(exp(2r)) is excluded. Constant angular height, bounded angular
variation and polynomial growth in proper cusp distance all lie in that
excluded class. No finite total map energy was assumed.

## Positive and adversarial controls retained

- The old exact local cusp still solves the equation. Its outer Busemann
  flux is negative; its inner boundary supplies the balance. It is not a
  counterexample to the source-free compact-core statement.
- Deleting the translation gives local radial infinite-growth solutions.
  Thus the nonzero period is load-bearing, not decorative group data.
- A fully smooth periodic slice with unit z-period has weighted translation
  energy 1 while exp(2*mean b)=10/9. This refutes replacing the minimum in
  the inequality by the mean. It is not a global harmonic solution.
- The local linearized exponents 1 +/- sqrt(5) arise for ANY dimension-three
  hyperbolic cusp in this affine-translation ansatz. They are independent
  of the particular arithmetic manifold and are not a new physical golden
  prediction. Dimension two gives 2 and -1 instead.

The third control is essential: without it, a plausible averaging shortcut
would incorrectly turn this conditional result into a universal negative.
It also transfers to the actual primitive peripheral period by replacing
the circle coordinate with -x1+x2: the two energies become K and 10K/9.
That transfer follows by substitution and flat-torus averaging; it is not
a separately run PDE or a new global harmonic example.

## What this changes in the work order

Do not build a one-dimensional positive-flux shooting solution and call it
the infinite-energy escape: the analytic result excludes it before any mesh
or shooting grid is needed. A genuine rank-two escape must confront the
large angle-dependent growth above. Whether such a solution exists or is
physically acceptable has not been answered here.

Nor may a rank-two obstruction be promoted to the rank-four coefficient
bundle by analogy. An arbitrary harmonic metric on Sym^3(rho) tensor chi
need not arise from the rank-two map. Its exact algebraic index is retained.
The alternatives now have distinct mathematical duties:

1. Establish genuinely angle-dependent rank-two existence and analyze its
   action, backreaction and normalizable modes.
2. Analyze the actual rank-four harmonic equation and its invariant flag
   directly, allowing metrics outside the rank-two image.
3. Derive a compensating current from the coupled parent/source action and
   retain its core modes, boundary domain, anomaly and interaction tests.

Sagman's infinite-energy surface theorem is useful context but assumes
reductivity; it is not a construction for this three-dimensional witness.
Its reductive replacement for length-spectrum domination cannot preserve
the nonsplit index mechanism by assumption.
[Primary text, Theorem 1.1 and section 6.1](https://arxiv.org/html/1911.06937v3).

No complete field theory, physical generation spectrum, empirical prediction
or gravitational completion was obtained. What improved is the precision
and difficulty estimate of the next physical-admissibility test, with the
unresolved possibilities explicitly preserved.

## Subsequent direct rank-four test

[F04](../full_flag_growth_2026_09_20/FINDINGS.md) now executes alternative 2
above with the full metric's invariant flag, not an induced-metric assumption.
All six complex mixing coordinates are included. It derives a related
controlled-angular-growth obstruction directly for V, with 20 exact controls
passing. This does not change F03's sealed rank-two claim or close arbitrary
angle-dependent existence and coupled-source routes. The exact algebraic
index and the positive local cusp remain intact.

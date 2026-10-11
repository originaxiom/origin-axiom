# The Hodge connection and the cusp unit

2026-10-11. Path-local verification packet; no shared arc number. GENESIS reference: v1.41 at main `6c148ddd495d133213140995976ff08849793d5d`, FK10 and FK11. This is a calculation on the effective modular base of the weave, not on a selected thread and not on the four-real-dimensional total surface.

## Question and scope

For every integer n, does the existing weight 12n automorphic line on PSL(2,Z)\H, equipped with its Petersson metric, give a smooth finite-action Abelian connection with effective flux n? Does the corresponding Yang–Mills problem select n=1? The two questions are separate.

The intended improvement is a concrete analytic realization of already admitted end data, not another candidate for matter content. It cannot discharge the genesis postulate selecting the unit unless a rule fixing the end sector is derived. No measured Standard-Model input is used.

## Choices before execution

- z=x+iy, y>0; orientation dx wedge dy; metric (dx²+dy²)/y²; effective fundamental region |x|<=1/2, |z|>=1. The base has real dimension two.
- Holomorphic sections of L_k transform by (cz+d)^k. The squared metric in this frame is h=y^k; the usual constant factor (4 pi)^k has no curvature effect. k=12n for a line with trivial elliptic stabilizer action.
- Chern curvature F=minus partial bar-partial log h; c1=iF/(2 pi). The equivalent unitary gauge expression is derived in PROOF.md.
- E=(1/(2g²)) integral |F|² dA, with g>0 supplied. Curvature radius one is a metric convention, not a physical scale prediction.
- The variational claim fixes flux and uses square-integrable curvature. Compactly supported variations establish the bulk equation. No unrestricted-end boundary variational principle is inferred.
- Integral n is imposed by the chosen compactification extension. Smooth metrics on the open trivial line are also considered, explicitly without this integral-end restriction.
- The discriminant transformation law is named hypothesis HDelta for the open trivialization and its identification with W46. No assertion about a four-dimensional Dirac operator, Fredholm domain, anomaly cancellation, backreaction or selected vacuum is tested here.

## Predictions and failing controls

Hand-derived prior: high confidence in the elementary base calculation; no expectation that this action derives the unit.

1. Derive F=-6in dA, area pi/3, effective flux n and energy 6 pi n²/g². A constant metric must give zero curvature; a local non-harmonic perturbation must change the curvature and fail the constant-curvature equation.
2. Derive metric descent from the general Mobius formula, with separate d=0 handling, and elliptic isotropy triviality precisely at integer weights divisible by 12. Test negative, zero and positive weights rather than only the desired unit.
3. Prove the fixed-flux energy bound by completing a square. It has equality at constant curvature. Without nonzero flux imposed, n=0 is lower energy than n=1. Metric scaling changes energy, not flux.
4. Conditional on HDelta, exhibit all real fluxes s by the globally positive metric (y^12 |Delta|²)^s on the open trivial line. Check the limiting cusp boundary integral and the difference between effective and stack-weighted integration. This is not an exhaustion of all dynamics.
5. Verify the change-of-frame norm identity for a section Fmod/Delta^n. Exponential decay with positive fractional cusp exponent is square integrable with the twisted norm for any finite polynomial weight; in the original norm a pole can instead diverge. No modes or index are counted here.

Any failed check is retained in its first output and investigated before a corrected instrument is sealed. A success verifies the formulas and the proof's specified scope, not the necessity of the metric/action/end choice. The first run uses Python 3.12 and SymPy; the hand proof carries the all-n and analytic statements, finite checks are safeguards.

## Load-bearing inputs

The modular quotient, the automorphic line and the chosen metric/action are definitions or supplied geometry in this calculation, not consequences derived from PF1–PF3. Differential identities, area integral, flux, energy inequality, scaling and cusp integrability are rederived here. The standard fundamental region and its side identifications are taken as the specified presentation of the base.

HDelta: Delta transforms with weight 12 and has its standard product q product_(m>=1)(1-q^m)^24. Its nonvanishing and leading order follow directly from product convergence; the transformation law is not re-proved here. Claims involving its global trivialization remain conditional on that law. No other seat's index value is an input to this proof.

See SOURCE_SCOPE.md for the prior-work sweep and direct source reading. This preregistration, proof, source scope and instrument are hashed and committed before the first scientific execution.

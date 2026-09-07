# R16: charged line domains, not yet the complete physical kernel

2026-09-07. Continues R14/R15's prescribed commuting singular background.
No global arc number and no change to the original smooth-cusp result.

## Result and relevance

The charged normal operator now supplies a concrete amplitude/domain
test. With trivial angular gauge holonomy and effective coupling
a = q beta, the local line analysis has extra self-adjoint trace freedom
for 0 < |a| < 1. That critical normal window is empty at a=0 and
|a| >= 1. Nonzero integer angular modes add no critical traces.

This is a local first-order normal statement, not a global
self-adjointness/Fredholm theorem at the joint line/cusp end. It gives
a nonempty strong-source candidate region; it does NOT derive beta
from a root's integer charge or choose the physical defect theory.

R15's finite four/one cohomology is retained. Neither its net three nor
this normal calculation yet computes the complete normalizable H1
spectrum or three physical generations.

## Operator, exact branches and integrability

On a compact segment of a geodesic line use
ds^2 = dr^2 + sinh^2(r) dtheta^2 + cosh^2(r) dt^2,
A=sinh(r), B=cosh(r), H=a log(tanh r).
The declared deformed complex is d_H=d+dH wedge,
delta_H=delta+i_grad(H), D_H=d_H+delta_H.

For each coordinate form component there is an exact theta/t-independent
joint zero branch. Tangential components have coefficient exp(-H).
For a component J containing dr the coefficient is
exp(H) product(g_jj, j in J)/(AB).
Direct exterior differentiation and the metric Hodge star verify them.

| coordinate component | orthonormal radial exponent lambda |
|---|---|
| 1 | -a |
| dr | a-1 |
| dtheta | -a-1 |
| dt | -a |
| dr wedge dtheta | a |
| dr wedge dt | a-1 |
| dtheta wedge dt | -a-1 |
| dr wedge dtheta wedge dt | a |

The volume measure is asymptotically r dr dtheta dt. Integrability
therefore requires lambda > -1, with equality logarithmically divergent.
At a>=1 only the four dr-containing leading branches are L2;
at a<=-1 only the four without dr are L2. At weak nonzero |a| there
are six; at zero there are four. These are local form components,
not species or generation counts.

The actual angular normal matrix, on
(1,dr,r dtheta,dr wedge r dtheta), is

```text
[ 0        a-lambda-1    -i m       0          ]
[ lambda+a 0             0         i m        ]
[ i m      0             0         a-lambda   ]
[ 0       -i m           lambda+a+1 0          ].
```

Its determinant is
(a^2+m^2-lambda^2)(a^2+m^2-(lambda+1)^2).
The second dt-wedged copy agrees; the exact hyperbolic operator has
this normal limit at fixed longitudinal momentum. With
nu=sqrt(a^2+m^2), roots are +/-nu and -1+/-nu. The half-density
normalization gives tangential eigenvalues +/-nu +/-1/2.
Only m=0 and 0<|a|<1 enter the open (-1/2,1/2) trace window.
Nontrivial angular holonomy, which shifts m, is not included.

## Why L2 alone does not choose the physics

For 0<a<1 the scalar and radial joint-zero branches are both L2 but
have nonzero exact Green pairing AB f h_r = 1. They cannot both be
freely included as independent boundary traces in a symmetric extension.
The minimal D domain and maximal distributional D domain differ.

Also distinguish D_min from the Hilbert-complex realization
d_min+delta_max. That latter realization permits the radial trace and
excludes the scalar trace in this weak-positive pair; d_max+delta_min
does the opposite. They are not interchangeable prescriptions.

For a normal r^lambda branch the least radial cutoff energy is
1 / integral_epsilon^R r^(-2 lambda-1) dr.
The logarithmic lambda=0 case has capacity tending to zero; the
negative integrable powers have a nonvanishing cutoff obstruction.
Exact primitives and independent numerical quadrature test this
criterion; substituting dr for r dr deliberately gives wrong answers.

## Global formal degrees zero and three

On R15's single-valued commuting background F, the formal degree-zero
solution is exp(-qF), and its dual top-form solution is exp(qF) dvol.
For positive endpoint densities beta_i and positive total source Q,
positive q suppresses the scalar at the high cusp, but its transverse
line integral is finite only when every q beta_i < 1.
At weak positive q this yields an L2 formal maximal-domain scalar zero,
not automatically a state in the physical extension.

Negative q reverses the scalar/top roles. At q=0 the finite-volume
constant and volume form are L2 formal solutions. If a positive q
violates any line threshold, the scalar fails there while the top form
fails at the cusp; the corresponding negative case is dual.

Consequently neither discarding extreme degrees nor retaining only
an Euler number is licensed without choosing the actual complete
domain. No H1 limiting kernel or absence of other bound states is
proved by these extreme-degree checks.

## Verification, failures and remaining work

The original design/source/tests were sealed at bec4aa92 before
execution. First producer failed, and its original tests gave
12 passed / 4 failed. Failures concerned an unevaluated symbolic zero,
a Piecewise integral, small-integral quadrature accuracy, and a
sign-undecided logarithmic limit. They are retained in
[CHARGED_DOMAIN_FAILURE.txt](CHARGED_DOMAIN_FAILURE.txt).

The separate instrument control was sealed at adfa7e8f. It uses
exponential rational normal form to test the same identities, an
explicit checked primitive, endpoint-scaled quadrature with zero
absolute tolerance, and a real exact logarithmic density before
sign-specific limits. No original math assertion or tolerance is relaxed.
[Successful science output](charged_domain_control_first_run.json):
168 norm checks, worst flat quadrature relative error 7.78e-15;
largest hyperbolic/normal correction 0.000134.
Five regrouped controls plus four partial-filling checks and twenty
R14/R15 tests give **29 passed** in the quiescent focused run.
The original four failures remain visible, not skipped or rewritten.

Next: derive the physical defect boundary law and gauge/fibre lift.
The later [R17](CUSP_TAIL.md) supplies a uniform high-cusp estimate,
including line approach, for a fixed tangential Hilbert complex;
finite-height singular compactness and the global domain remain. Establish
Fredholmness and compute both charged H1 kernels as tubes shrink/cusps
extend; check the possible vector-like pair and its interactions.
Source amplitudes, through-flux, parent theory and the physical spinor
identification remain declared inputs of this candidate.

References and their exact scopes are in the pre-execution
[design](CHARGED_DOMAIN_DESIGN.md). Pantev--Wijnholt supplies the
deformed-complex mechanism; compact-edge theorems were not silently
applied to this noncompact joint singular limit.

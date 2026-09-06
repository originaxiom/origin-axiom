# R10: computed finite terms also favor the neutral Higgs orientation

The previously uncomputed **hard one-loop alignment coefficient is now
computed for an explicit renormalization boundary condition**, and is
negative. The induced weak-triplet relaxation contributes another, smaller
negative coefficient. Both reinforce R9's neutral-favoring infrared term.
Neither sign was an acceptance condition of the pre-execution design.

This is progress in the **chosen action**, not a derivation of that action
from the originating object, a complete finite-parameter vacuum certificate,
or a physical TOE. [The overall goal verdict](GOAL_VERDICT.md) separates
these different duties rather than reducing the goal to this calculation.

Design, source and eight tests were sealed at **8cbd10ed**, before the
successful first execution (9.47 s). [Full output](finite_alignment_first_run.json),
[source](finite_alignment.py), [design](EXTENSION_8.md) and
[captured checks](FINITE_ALIGNMENT_CHECKS.txt) retain the computation.
All earlier sealed sources and first outputs are unchanged.

## 1. What was fixed before evaluating the coefficient

The model is R7's four complex scalar 27s, real adjoint and one Weyl 27,
with R8's kinetic normalizations and weak-coupling family. No field,
coupling or mass is fitted to measured data. At mu=sqrt(epsilon) use the
Landau-gauge MS-bar one-loop potential, with scalar/Weyl/vector weights
1,-2,3 and subtraction constants 3/2,3/2,5/6. The renormalized potential
at that scale is the original R7 positive-square polynomial; other allowed
local operators have zero renormalized coefficients there.

That last sentence is an **explicit boundary input**, not a proof that
those operators are forbidden or remain zero under RG evolution. R9
correctly retained an uncomputed finite coefficient rather than declaring
it arbitrary. R10 computes it for this declared boundary prescription;
it does not derive that prescription from the object.

The hard determinant follows the positive branches of the full 294-scalar,
27-Weyl and 78-vector matrices. Its hard counts are 209,10,66; excluded
counts 85,17,12 stay explicit. The maximum excluded/lowest-hard squared-
mass ratio along the extraction paths is .5951, below the sealed .85
limit. Positivity is required of the hard branch; excluded off-shell
tree eigenvalues are recorded, not turned positive by absolute values.
They are not the resummed soft spectrum. R9's full 19-scalar,17-Weyl,
12-vector soft determinant is included separately, exactly once.

On the pure-Higgs slice the mass constraints vanish, leaving only the two
Higgs norm quartics. Their gradient is in the light-Higgs space, so the
tree heavy-normal source vanishes there. Direct projections onto all 209
positive modes at the three tested orientations agree below 3.18e-15.
This is why the hard determinant on this slice computes the required
one-loop quartic without a missing tree-level normal exchange on that
particular slice. It does not eliminate the subsequent quantum normal
response or the triplet source below.

For the effective potential with fields eliminated, their stationary
condition must be imposed. This is the point of
[Manohar/Nardoni, section 2.3, equation (2.17)](https://arxiv.org/pdf/2010.15806).
Their equation (2.16) supplies the stated one-loop conventions, and section
2.4 distinguishes a renormalization boundary from RG evolution. These are
methodological inputs, not an external certificate for this E6 calculation.

## 2. Finite hard alignment: two extraction methods

Retain R9's invariant rhoU,rhoD,B=U^T J D and
eta=abs(B)^2/(rhoU*rhoD). Eta=1 is neutral; eta=0 is the charge-breaking
control, as established by the actual Q action. The hard contribution is

```text
V_hard,alignment = epsilon^2 cB_hard abs(B)^2,
cB_hard = -0.0001030871575.
```

On H=sqrt(epsilon)*h this is order epsilon^4. Its sector contributions:

| sector | contribution to cB_hard |
|---|---:|
| real scalars | -0.000000553961 |
| Weyl fermions | -0.000354173099 |
| vectors | +0.000251639903 |
| total | **-0.000103087158** |

The primary instrument extracts the quartic from the neutral-minus-charged
**radial gradient**, avoiding the most severe constant-term cancellation.
An independent potential-difference extraction checks it. All six steps,
six nonzero eta comparisons, quadratic/cubic fits, shortened-range fits
and held-out smallest steps are retained in the JSON.

Primary gradient-fit resolution is at most 4.89e-11 in the sector
coefficients; agreement across orientations is 3.92e-12. The less stable
potential extraction differs from it by at most 4.40e-7 across all angles,
and its held-out/fit spread is at most 1.19e-6. These are **numerical
stability diagnostics, not statistical error bars or rigorous interval
bounds**. The total negative sign is resolved by both methods. The very
small scalar contribution should not be overinterpreted at the precision
of the less stable potential check.

All-field invariant completeness is inherited from R9, not inferred from
six equal numbers: the only nonradial light-Higgs quartic allowed by the
actual unbroken symmetries and residual classical phase is abs(B)^2.

## 3. The normal shift matters: omitting it reverses the triplet contribution

Write the canonical adjoint triplet as T=epsilon*t. At the order under
consideration its orientation-dependent terms are

```text
V_T / epsilon^4 = K_T norm(t)^2/2 + J_T(h).t,
J_T = fU nU + fD nD,
nU_a = U^dagger A_Ta U,   nD_a = D^dagger A_Ta D,
K_T = kappa_T + .02*(rU+rD)/6 = .00769215032634.
```

Here U,D in nU,nD are the unscaled h doublets. The source contains the
hard one-loop T H^2 coefficient **and** the tree delta0*T*H^2 term from
R7's epsilon*delta0 normal shift:

| source part | fU | fD |
|---|---:|---:|
| hard determinant | -.003813052923 | -.0000177221032 |
| normal-shift insertion | -.000577991935 | +.0000356911486 |
| total | **-.004391044858** | **+.0000179690454** |

The two endpoint sources determine fU,fD; five other orientations are
holdouts. Their source-form discrepancy is 2.11e-14, and the largest
step/extrapolation source diagnostic is 1.64e-13. The independent mixed
tree-gradient check agrees with the analytic normal term to 4.05e-19.
All eight color-octet sources vanish within 6.27e-14; their normal terms
are zero. No color source is silently dropped.

Exact symbolic identities, on all eight real Higgs variables, give

```text
norm(nU)^2 = rhoU^2/12,
norm(nD)^2 = rhoD^2/12,
nU.nD = (rhoU*rhoD - 2 abs(B)^2)/12.
```

Minimizing the triplet quadratic therefore gives t=-J_T/K_T and
-norm(J_T)^2/(2*K_T), whose alignment coefficient is

```text
cB_triplet = fU*fD/(6*K_T) = -0.00000170959747.
```

The direct endpoint energy subtraction agrees with that coefficient below
1e-18. At the neutral endpoint the induced canonical triplet is
T/epsilon=(-.00756794768, approximately 0, approximately 0) in R8's
triplet basis. This is a leading induced response, not a fully recomputed
quantum vacuum.

**Deliberately omit the normal piece and the coefficient becomes
+0.00000146416183**, the opposite sign. Omitting the hard piece instead
gives -0.000000446975058. These are omission controls, not alternative
models chosen after inspecting the result. The original normal response
must be retained even when a particular earlier quadratic contribution
was zero. This is a concrete prevention of a false sign verdict.

## 4. Combining with R9: what the finite result does and does not select

For the neutral-minus-charged endpoint difference at epsilon=.01:

| contribution | Delta V / epsilon^4 |
|---|---:|
| R9 infrared logarithm | -4.993679171e-6 |
| complete finite soft determinant | -4.930810500e-6 |
| finite hard quartic | -2.455960556e-7 |
| triplet relaxation | -4.072965111e-9 |
| sum of these terms | **-1.017415869e-5** |

At epsilon=.0025 the normalized sum is -1.167740591e-5. All seven sampled
orientations give decreasing energy toward eta=1 at each of the four
predeclared epsilons. The full curve data retain each term separately.
Changing epsilon reproduces R9's exact logarithmic slope.

This reinforces neutral preference at the **displayed truncation and
boundary prescription**. It is not a certificate for all orientations,
all competing high-scale branches, or the untruncated finite-epsilon
theory. In particular:

- the omitted remainder is not bounded by these coefficient fits;
- complete matching/field normalization and higher-loop consistency have
  not been independently certified by a full-theory stationary comparison;
- the anomalous phase and the smaller seventeenth light fermion mass remain
  as in R8/R9, not removed from the physical spectrum;
- no physical pole masses, observed weak scale, three families or gravity
  have been derived by this calculation.

The next conditional-model check is an independent full-theory stationary
and power-counting comparison, including the induced triplet and every
residual mode. The programme-level priority is different and more central:
an exhibited source-to-action map that determines the fields/interactions
and prices the inputs. A more accurate chosen GUT model cannot substitute
for that map; both duties remain registered.

## 5. Verification and search continuity

First scientific execution: success, 9.47 s. Eight new tests: **8 passed
in 10.29 s**. Combined physical-audit/selected-upstream regression:
**115 passed, 3 failed in 111.84 s**. The failures are the preserved original
G2 NumPy-key exporter and two original R7 small-step controls; separate
sealed repairs pass. No old source rewrite, tolerance relaxation or xfail.
No files were edited during these scientific/test runs.

The latest fetched main is 69a027eb. The ten-head topic sweep is PRESENT,
not an absence proof; the latest embedding-selector results are read as
upstream claims, not merged or independently certified in R10. The known
14-to-12 reduction, spin/beat positives and earlier withdrawn false kills
remain in [RECOVERED_PHYSICAL_STEPS.md](RECOVERED_PHYSICAL_STEPS.md).

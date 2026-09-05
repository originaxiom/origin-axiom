# Physical bridge audit — design before numerical execution

Date: 2026-09-05. Base: `f06d34054899e8c23672b836a7c534af77cbd35d`.
Status: local audit and conditional model development; no promotion to CLAIMS.

## Purpose and coverage

Understand the programme's journey, verify load-bearing positive and negative
results, and turn a specific part of its mathematical particle structure into
an executable physical calculation. A completed theory of everything is the
research objective, not a result this design assumes or can certify.

The original tree's serial default suite runs in a separate, unchanged worktree.
Its result will be reported with failures, skips and limitations. A passing
regression fixture is not an independent proof of its interpretation. No claim
of having read or independently proved every arc will be made.

## Prior work read and searched

WORKING_RULES, GOVERNANCE, METHOD, REPRODUCIBILITY, COMPUTE_THE_PROGRAM,
THE_LADDER, THE_CAMPAIGN and THE_FRAMEWORK were read. The initial audit,
uniqueness theorem, claim ledger, latest progress entries, generated coverage,
and development history supplied the route into the original computations.
In particular: B915's complete design, findings, code and tests; B925/B926's
successor; B1148's carrier and cubic; B1244/B1245's scope correction; and the
physics branch's existing trinification calculation at `d5999b5f` were inspected.

The already-banked query used `threshold running renormalization beta exotics`.
The absence instrument searched `threshold|renorm|Lagrangian|effective.action|effective action`
over eight local/remote heads and reported PRESENCE on every head. These results
license reading those sources, not an absence or novelty claim. Further source
searches covered split multiplets and simultaneous/sequential unification.

The B915 failure concerns its specified desert. Its group independence is already
banked as B1245; the existing trinification scale is already on the physics
branch. Neither is to be presented as a discovery here.

## R1 — does the B915 numerical curve satisfy its own definition?

Quantifier: the unification boundary-value problem defined by B915's stated
coefficients and scale interval, including both one-loop and gauge-only
two-loop truncations; not all possible physical completions of the programme.

Conventions: `t = log(mu/MZ)`, `x_i = 1/alpha_i`, index order `(1,2,3)`,
`alpha_1 = (5/3) alpha_Y`. Retain the exact banked coefficient matrix and
archived numerical inputs for an audit of that calculation. The archived
comparison point is a numerical fixture, not a fresh empirical observation.
No current dataset, new measurement, or previously unseen test target enters.

Checks fixed before execution:

1. Evaluate both final residuals `(x1-x2, x2-x3)` at valid archived curve points.
   A residual above `1e-6` in inverse-coupling units fails the advertised
   boundary condition; independently tighten the integrator to exclude noise.
2. Reproduce the legacy sequential procedure with trial values of the internally
   fixed strong coupling `0.09, 0.118, 0.15`. Such a trial value is acceptable
   as an initial guess only if the converged result is independent of it.
3. Construct the boundary-value curve by running DOWN from one common UV
   coupling and solving only the electromagnetic normalization. Cross-check
   by an independent simultaneous two-variable solve running UP. Require
   agreement within `1e-8` and UV residuals below `1e-6`.
4. The one-loop closed form is the positive control. Nonmeeting synthetic
   points are the negative control. Integration failure or a singular trajectory
   is a reported invalid point, never silently a negative physics result.
5. Recompute the B915 distance with its own historical fixture and uncertainty
   prescription, with a continuous search checked against a denser grid. Report
   whether its original `d <= 3` decision changes. The loop difference is a
   truncation diagnostic, not a calibrated probability distribution; no new
   exclusion significance will be claimed.

Prior: the sequential solver is likely to fail the two-loop residual test;
the qualitative desert mismatch is likely to survive a correct solve. Either
outcome is reportable. The gauge-only truncation must be named explicitly:
Yukawa contributions are a separate assumption/input, not silently included.

## R2 — a physical threshold interface for the banked 27

Quantifier: conditional four-dimensional gauge theories with the standard
`SU(3) x SU(2) x U(1)` embedding, three chiral families and one complex Higgs
doublet, extended by vectorlike `D+Dbar` and `L+Lbar` pairs from the
`10 = 5+5bar` in `27 = 16+10+1`. The family count, spacetime, quantization,
kinetic terms, scalar spectrum and masses are declared physical inputs;
they are not derived from the representation diagram.

Derive beta coefficients from representation indices using rational arithmetic,
counting Weyl fermions and complex scalars separately. Check the known baseline
coefficients `(41/10,-19/6,-7)`, anomaly cancellation, hypercharge rescaling,
and the equal shift of complete degenerate multiplets. Compute piecewise
one-loop evolution with explicit masses and compare with its analytic formula.

Determine the exact linear combination of logarithmic mass ratios that would
be required to meet at the archived B915 comparison point. This is INVERSE
MATCHING USING ALL THREE COUPLINGS: a target for a future mass mechanism,
not a prediction or an empirical success. Test the degenerate-mass case and
the full allowed range `MZ <= mass <= MU`, including one, two and three
copies. Feasibility and infeasibility are both conditional on this spectrum
and approximation; neither kills a different spectrum or intermediate group.

Prior: degenerate complete multiplets cannot alter one-loop meeting differences;
splitting can change them. Whether the required split is attainable for each
copy count will be computed. No mass is to be adjusted and then called forced.

## Recording discipline

Seal this design and its source hashes before the first new numerical run.
Keep original banked code, outputs and seals unchanged. Record failures beside
corrections. New tests must assert equations or independently recomputed
quantities, not merely a stored verdict or the names of JSON input fields.
Any later extension of this design is dated and labeled post hoc.

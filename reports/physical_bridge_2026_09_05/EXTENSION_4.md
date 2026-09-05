# R6 — the complete leading normal vacuum shift

2026-09-05, after R5's positive angular result and its independent derivative
check. This design/code will be sealed before computing the normal shifts.

BANKED IDENTITY: the R4 potential is a sum of squares of 275 real quadratic
constraints on 186 scalar coordinates. Its vacuum Jacobian has rank 109;
the 77 null directions are 66 gauge modes plus an octet and triplet. R5's
full one-loop angular curvatures are positive, independently differentiated.
Their normalizations, potential and all original first results are retained.

PRIOR ART: fresh fetch still gives upstream a8fd2460, already included.
`already_banked.py quantum vacuum tadpole shift normal` returned 112 hits,
none settled on >=3/5 terms. The atlas context card and the ladder/kill graph
were checked. The nine-head regex sweep `tadpole|quantum.shift|loop.*stationar|
stationar.*loop` returned PRESENT; its B1194/physics-audit-branch hits concern
other stationary-phase/audit claims, not this action. Those hits were read;
no universal absence is asserted. This continues PB-VACUUM/X8–X10/X19–X24.
R5's Martin one-loop convention is inherited, not a new empirical premise.

P0: the first-order normal displacement of the chosen R4/R5 4d compact-E6
model in MS-bar Landau gauge. It is not an all-order, all-action or full-TOE
claim. No measured values, family count or physical mass scale are inferred.

## Inputs and formulas

Use the preselected R5 point lambda=.2, g=.5, y1=y2=.25, one Weyl 27, mu=1,
with the same VEV units and all displayed quartics equal. All parameters
are renormalized inputs at the declared scale; omitted allowed operators
are zero there, not claimed to be symmetry-protected.

Build the real Hessian Q_a of **every quadratic constraint** independently
from its explicit polynomial. Check `c_a(z)=z^T Q_a z/2-b_a` and `J_a=Q_a z`
against the original constraint producer on arbitrary displaced fields.
At the zero-constraint vacuum,

```text
H0 = 2 lambda J^T J
dH0[r] = 2 lambda[(dJ[r])^T J + J^T dJ[r] + sum_a J_ar Q_a].
```

The last term is essential: differentiating only the on-vacuum formula
2 J^T J would omit the normal derivative of `2 sum c_a Q_a` and give the
wrong tadpole. Scalar/vector/Weyl one-loop gradients follow from
`d Tr f(M^2)=Tr f'(M^2) dM^2`, with f and spin factors fixed in R5.
Use f'(0)=0 without taking logarithms of negative masses off the vacuum.

Compute all 186 real gradient components, including gauge and fermion
contributions, then transform to canonical scalar coordinates. Verify the
gradient is orthogonal to the *entire* 77-dimensional tree kernel, not just
the gauge orbit. Exhibit the complete real SM-singlet subspace and check
its dimensions rather than restricting to three radial variables by fiat.

For the positive tree Hessian subspace, solve
`delta z_canonical = -H0_canonical^+ grad(V1)_canonical`. The plus denotes
the inverse on positive modes and zero on gauge/angular zero modes. A
nonzero kernel gradient is a failure requiring diagnosis, not a component
to discard. Verify the full first-order stationary equation and that the
shift preserves the actual SM generator action.

## Controls and outcomes

1. The quadratic-constraint reconstruction must match the banked J and the
   original constraints, including complex displacements and a nonzero
   adjoint constraint. Finite differences of the *full* tree Hessian must
   recover its analytic derivative. An explicit control omitting the
   `sum J_ar Q_a` term must disagree on a radial direction.
2. Check the matrix-function gradient on an independent scalar toy and the
   generator Ward identity on the full one-loop gradient. Mass derivatives
   for vectors and complex Weyl matrices must agree with finite differences.
3. Report relative shifts separately for each scalar 27 and the adjoint,
   plus the full canonical norm, normal Hessian gap and residual. A relative
   displacement below 10% is only a **declared small-shift diagnostic**, not
   a proof that all higher loops or pole masses are controlled. A larger
   shift cannot kill the small-coupling branch or the entire programme.
4. Compute epsilon=1,1/4,1/16 with lambda->epsilon lambda,
   g,y->sqrt(epsilon)(g,y), mu->sqrt(epsilon)mu. This is a simultaneous weak
   coupling control with unchanged classical VEVs, not an empirical fit.
   All tree masses squared scale as epsilon, V1 and its gradient as epsilon^2,
   and the leading normal shift as epsilon. Check that scaling directly.
5. Verify the link to R5's constrained curvature. For a normalized octet or
   triplet tangent X, the tree-manifold path has second derivative k=-Y/5.
   Differentiating the stationary tree family gives
   `X^T [dH0(delta z)] X = grad(V1) . k`. Thus the constrained angular
   curvature includes the first-order normal-shift contribution. Do not
   read a tree Hessian at the shifted point as the full one-loop spectrum.

Prior: a sufficiently weak-coupling perturbative branch should exist, but
the size and direction of the reference-point shift are not yet known.
The result can support a quantitatively small leading displacement or show
that the chosen reference point needs a smaller-coupling treatment. Either
way the full shifted all-order vacuum, global comparison, light Higgs,
physical parameters and gravity remain separate obligations.

Outputs are exclusively created; all first runs, failures and repairs retain
distinct artifacts. Hash and commit this design, code and tests before running.

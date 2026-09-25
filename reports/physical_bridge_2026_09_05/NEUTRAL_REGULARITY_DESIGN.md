# R49: canonical adjoint regularity and nonlinear admissibility

September 25, 2026. Own input 81ae3441a9d8995d72a15d6dbcbd607422213e8f.
No shared B/I identifier, main merge, other-seat edit or full-bank claim.

## P0 and purpose

This computes the complete End0(E) coefficient on R44's canonical
finite-energy background for the figure-eight projective family, at
each fixed real q>0, q!=1. A fixed central mu4 twist cancels in End0(E).
It is a member/family/domain result, not a claim about every arithmetic
class, source/end choice, parent, nonlinear phase or physical chirality.

R47 gives a nonzero neutral harmonic projection but does not put that
projection in L4. R46 needs Dom(Q) intersect L4 for its nonlinear
residual-square action. This cell tests that missing SAME-background
join. It does not duplicate the other seat's full-parent matching task,
nor compute the full neutral kernel dimension or a selected q.

## Prior and conventions

Constructive prior: the product-cone limit should give an exterior
positive threshold, although global neutral zero modes remain. Its
constant-meridian indicial operator should have no growing L2 branch
that spoils L4. This is an expectation to test, not a result.

Use r=(log R)/2, v=2k t+r/2, k=log q. Coordinates x,t have period one;
v has period 2k at fixed r (negative k reverses that marking only).
The coframe is (dr, exp(-r) dx, dv); its limiting base metric is
diag(3/4,3/8,3/4), volume a constant times exp(-r).
The limiting coefficient H, up to an irrelevant positive scalar on
End0, is diag(3/8,1/4,3/8,3/8). It is derived from the affine-sphere
radial and tangent metric, not replaced by Id4.

The limiting flat connection is H0 dr + N exp(-r)dx + (D/2)dv,
H0=diag(1,0,0,-1), N=E02+E23, D=diag(1,-3,1,1).
The discarded exact connection term is explicitly O(exp(-2r)).
All actual metric transfers require R44's all-jet limit and global
cusp/core argument, still at authored/external-input evidence grade.

On sl4 use off-diagonal matrix units and Eii-E33 for i=0,1,2.
Its positive metric is tr(H^-1 X^* H Y), not the invariant bilinear
trace. The radial symbol is lambda, longitudinal Fourier symbol i nu.
The formal radial adjoint is -partial_r+1, from the actual model volume.
Keep the coframe derivative d(exp(-r)dx)=-dr wedge exp(-r)dx.

## Exact controls, fixed before execution

1. Reconstruct both limiting metrics from the radial graph; verify the
   coordinate shear and full connection split, including its remainder.
2. Build sl4 commutator matrices directly and their positive Gram matrix.
   Check A is self-adjoint, B^*=ad(N^T), L^*=L and flatness.
3. Build the whole exterior differential independently from wedge signs
   and coframe derivatives, then its metric/formal adjoint. Check d^2=0
   and the degree-by-degree indicial Laplacian for every degree 0--3.
4. Compare with the independently expanded degree-one block formula.
   Expected dimensionless potential:
       T=A^2+A+2 B^* B+L^2,  L=ad(D)/2.
   Expected polynomial z(z-2)^3(z-6)^11 and semisimplicity. Its restriction
   to zero longitudinal weight has multiplicities 1,3,5 instead of 1,3,11.
   These are end-operator channels, not global particle counts.
5. Test the indicial pairs at nu=0: (0,1),(-1,2),(-2,3), and the
   conjugated radial threshold 1/4 (3/4 metric scale gives 1/3).
   Nonzero nu adds nu^2, never subtracts it.
6. Two-sided mutants: wrong radial volume, omitted coframe derivative,
   unsheared radial connection, altered positive coefficient metric,
   and wrong Fourier sign must fail their relevant checks.
7. Verify the adjoint meridian nilpotence index and the finite inverse
   for every nonzero formal meridian frequency. The zero-frequency
   inverse must NOT be asserted. Check both left and right inverse.
8. Integrability controls: exp(3r/8) is L2 but not L4 for exp(-r)dr;
   the proposed epsilon=3/8 weighted estimate plus covering multiplicity
   gives a convergent L4 bound. Test the threshold cases without a
   numerical cutoff standing in for an improper integral.

Finite exact controls certify these algebraic inputs. They do not prove
the global end transfer, elliptic/Agmon argument, kernel count or an
independently accepted PDE theorem. The authored proof makes those
steps and hypotheses explicit.

## Outcomes and stopping rules

If any expected identity fails, preserve its FIRST output and do not
promote the affected analytic conclusion. A correction is a separate
version/design sealed before its own execution. Do not edit executed
science. If the end/metric transfer cannot be justified, retain the
model computation and explicitly leave actual regularity unpaid.

If the proof and finite inputs survive, report finite-dimensional global
adjoint harmonic spaces, a positive gap on their orthogonal complements
(with no numerical global gap), and Lp regularity for every finite p>=2.
This pays nonlinear admissibility of R47's harmonic direction. It does
NOT prove L-infinity, a nonlinear solution branch, q stabilization,
a nonzero quartic, a physical asymmetric phase or a gravitational modulus.
No negative about changed coefficients, sources, ends or phases follows.

## Execution envelope

Seal this design, proof, prior, input manifest, producer and tests.
Commit/push/server-confirm on the own branch before any import or run.
Use durable first-run captures outside the worktree. Run native producer,
dedicated tests, then the fixed six-file regression: canonical_cusp,
parent_cusp, canonical_interaction, neutral_tangent,
neutral_pairing_diagnostic, neutral_regularity. The original R47
structural-zero comparison failure is expected and must remain visible.
This is not a full suite or independent specialist/banking review.
The worktree stays read-only through every execution envelope.

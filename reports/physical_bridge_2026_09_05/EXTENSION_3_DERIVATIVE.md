# R5 verification extension — analytic derivatives and exact scale identity

2026-09-05, designed after R5's first result (0ac9352a), before this check.
The first result is positive for the SM angular curvatures; this extension
must not assume that sign. No original producer or first result is changed.

BANKED IDENTITY: R4's exact constraint/gauge matrices and R5's complete
kinetic metrics; R5's first run includes 99 backgrounds, scale checks and
41 passing focused tests. Scalar/vector fourth-mass traces were numerically
constant; finite-difference octet/triplet curvatures were positive.

PRIOR ART: the pre-R5 bank/branch search and primary theoretical formula
are recorded in EXTENSION_3.md. This extension independently differentiates
that same spectrum, not a new physical action or empirical comparison.

P0: exact polynomial mass-trace identities and leading angular curvature
of the chosen R4 common-quartic ray on its SU5-adjoint vacuum family.

1. Form the unwhitened, generalized scalar and vector mass operators over
   rational polynomials in all four SU5 Cartan coordinates. Compute Tr(M^2)
   (fourth powers of physical masses). Check if each equals a quadratic
   polynomial in N=Tr27(A^2). Equality is exact by coefficient subtraction;
   do not infer it from sampled points. Here 2 J^T J is a *formal* polynomial
   away from N=5, not the physical Hessian off its constraint zero set.
2. Differentiate the norm-preserving path analytically: A'=X, A''=-Y/5,
   with Tr(X^2)=1, Tr(XY)=0. Since J and G are affine-linear in A, compute
   their exact first/second directional matrices without finite differences,
   then differentiate their full kinetic-normalized quadratic forms.
3. For symmetric M(t), differentiate Tr f(M) using eigenvalues x_i and the
   matrix entries B=U^T M' U, C=U^T M'' U:
   `d2 Tr f = sum f'(x_i) C_ii + sum_ij f'[x_i,x_j] B_ij^2`.
   The divided difference is (f'(x_i)-f'(x_j))/(x_i-x_j), tending to f''
   at positive degeneracy. For f=x^2(log x-c), f'(0)=0; the kernel-kernel
   block of M' must vanish at a two-sided positive-semidefinite minimum.
   Check that block before assigning its zero contribution; do not evaluate
   an infinite f''(0) times a spurious numerical zero.
4. Compare the analytic curvatures with R5's epsilon=.0025 estimates and
   their step convergence. A scalar toy matrix with a known nonzero second
   derivative, a rotating degenerate matrix and a quadratic emerging zero
   eigenvalue are independent two-sided controls. Check mu and off-diagonal
   directions again. Failure preserves the first result as provisional,
   not certified. Success sharpens its accuracy, not its physical scope.

The local-search output is not a global proof: a symmetric saddle can report
optimizer success at iteration zero. Normal-direction quantum shifts, full
pole masses, and full-potential/global-vacuum comparison remain separate.
Seal this design, code and tests before their first execution. Preserve any
failed output and re-seal repairs before distinct reruns.

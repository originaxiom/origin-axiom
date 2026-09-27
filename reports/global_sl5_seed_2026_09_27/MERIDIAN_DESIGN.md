# Follow-through: does meridian-relative freedom connect the whole parent?

Written after result 8112b526, before this follow-through runs. Original
sources remain unchanged. New sources and dependencies must be sealed.

## Question

The mixed H1 is trivial on each peripheral circle but nontrivial on their
torus. Does keeping only the meridian conjugacy class fixed permit an
irreducible SL5 representation near this native seed, or only deform the
three-dimensional block rho2 + trivial? A zero full-torus-relative kernel
is not an answer to this weaker condition.

## Proposed local argument and falsifiable finite test

Over the cubic extension, the native E is A3 + eta + eta^-1, where
A3=rho2+1. The meridian spectra of these three blocks are disjoint:
{1}, {omega}, {omega^2}. The off-block endomorphism system has rank 14:
paired rho2 twists (4), their duals (4), and three paired cubic-character
systems (2+2+2). Construct it exactly over Q(zeta5) by restriction of
scalars; verify traces against End(E)-End(A3)-two scalar blocks as an
additional decomposition control.

Predict that these off-block systems have H0=H1=0 and no meridian fixed
vectors. More strongly, the Fox derivative of the two M2 relators in
the other two generators, with the meridian generator fixed, is a
28x28 invertible K-linear map (112x112 over Q). Test its exact rank and
nonzero determinant. This is not a numerical tangent-rank guess.

If this passes, the analytic implicit-function argument in MERIDIAN_PROOF
would show that every sufficiently nearby fixed-meridian representation
remains block diagonal 3+1+1 up to conjugation, even with longitude free.
If it fails, do not claim the neighborhood is closed: report the kernel
and design a nonlinear integrability test. No distant-component no-go.

Countercontrol: the original rank-six mixed system must have a NONZERO
meridian-fixed Jacobian kernel. Subtract residual meridian-fixing gauge
directions before interpreting it as cohomology. This checks that the
test distinguishes the live smaller-block direction from full-parent
mixing. Central chi^q twists leave the adjoint action unchanged; verify
this directly, then use the same local argument for all five seed twists.

The new tests also lock the already observed five global index pairs.
This is explicitly a post-result regression lock, not a prediction made
before their measurement. Keep first failures and seal corrections.

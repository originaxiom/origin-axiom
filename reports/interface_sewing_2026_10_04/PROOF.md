# The interface law and its physical scope

October 4, 2026. Authored conditional application of standard elliptic
matching. This is not an independently accepted new theorem.

## Smooth matching of fixed monodromy variations

Let Y be compact, closed, connected and smooth, cut into X1 and X2 along
a smooth separating surface Sigma (possibly disconnected). Start with an
ALREADY admitted smooth flat harmonic C=A+Psi on Y, A anti-Hermitian,
Psi Hermitian. Use its positive fibre metric and the fixed smooth base
metric. The preceding packet differentiates the supplied potential
V=c(||F_C||^2+||d_A^*Psi||^2) along a Hermitian trace-free parameter s:

    delta C=d_C s, delta A=[Psi,s], delta Psi=d_A s,
    delta F_C=0, delta mu=L s,
    L=d_A^*d_A+sum ad(Psi_i)^2.

No new bulk action is introduced. On each piece the Dirichlet problem for L
is coercive, so for every smooth boundary value u it has a unique harmonic
extension s_i. Let N_i u=nabla_(n_i)^A s_i be its OUTWARD normal derivative.
All traces and metrics are transported by the actual unitary identification
induced by the global bundle; write them in one interface trivialization.

Green's identity gives

    <u,N_i u> = ||d_A s_i||^2 + ||[Psi,s_i]||^2 >= 0.

The smooth sewing law is (N1+N2)u=0, not N1-N2=0. Continuity of s and
cancellation of its outward covariant derivatives give a distributional
global solution Ls=0; elliptic regularity makes it smooth. Conversely any
global solution has these matching traces. A normal jump gives a surface
distribution in Ls and is not a zero residual of the smooth bulk problem.

If (N1+N2)u=0, the two nonnegative Green pairings sum to zero. Hence
d_A s_i=0 and [Psi,s_i]=0 on both pieces. They join to a global parallel
Hermitian endomorphism, and delta C=0. Conversely every such parameter
lies in the interface kernel. Thus after discarding zero field variations,
NONE of the fixed-monodromy positive-complex directions survives. A simple
SL(n,C) coefficient has no trace-free such parameter; for a reducible one
there may be a finite stabilizer space, still with zero field variation.

This does not eliminate genuine flat-connection moduli, charged cohomology,
or the internally constant gauge fields. It says nothing about arbitrary
nonflat variations, singular interfaces, sources, or a remaining free end.
It is the closed counterpart of the previous infinite free-boundary result.

In particular, one cannot choose independent harmonic Dirichlet metrics on
two nonsemisimple pieces, match only their values and infer a global harmonic
metric. R85 instead tests global simplicity BEFORE applying a closed harmonic
metric theorem; its actual admission remains its own uncompleted test here.

## The response form is not the action

The positive form <u,(N1+N2)u> equals the kinetic norm of these piecewise
field variations. It is NOT the residual-square potential. On either piece
Ls_i=0 even when <u,N_i u> is positive. The matching equation comes from the
global smooth field/domain requirement, not from relabeling that norm as a
new boundary energy. This distinction is essential for a common-action test.

Once the complement is fixed, N2 is a nonlocal response determined by its
background and metric, not a freely chosen constant beta. Those determining
data are still physical inputs. Changing the partner changes the law.
Nothing here chooses a physical partner from the word grammar or derives
four-dimensional spacetime, the gauge parent or a coupling.

## Exact cylinder comparator

Use one normalized real Fourier component on a flat torus with Laplacian
eigenvalue k^2. On an interval of length a its scalar extension is

    f(r)=[u0 sinh(k(a-r))+u1 sinh(kr)]/sinh(ka), k>0.

With outward derivatives (-f'(0),f'(a)), the response matrix is

    N_a=k [[coth(ka),-csch(ka)],[-csch(ka),coth(ka)]].

Join lengths a and b at both ends to form a circle factor. Exchanging the
second interval's endpoint order conjugates by the swap and does not change
this symmetric matrix. The sum has eigenvectors (1,1) and (1,-1), with

    lambda_plus=k[tanh(ka/2)+tanh(kb/2)],
    lambda_minus=k[coth(ka/2)+coth(kb/2)].

Both are positive for k,a,b>0. At k=0 the sum is
(1/a+1/b)[[1,-1],[-1,1]]: only equal endpoint constants remain, giving df=0.
Subtracting outward maps incorrectly makes every boundary vector pass when
a=b. Keeping only one piece restores arbitrary nonconstant harmonic boundary
data and a nonzero df; the closed and free problems are distinguished.

For k=0, equal values at an interface can conceal a derivative jump J.
Smoothing the derivative linearly through a strip [-epsilon,epsilon] gives
f''=J/(2 epsilon) and integral |f''|^2=J^2/(2 epsilon). This C1 profile is
piecewise smooth and has an L2 second derivative for fixed epsilon; smooth
approximations have the same leading divergence. It illustrates the actual
residual-square cost, not the kinetic response form or a particle mass.

## Exact elimination in a finite residual model

For an explicitly supplied positive-semidefinite symmetric matrix

    L = [[A,B],[B^T,D]],

with A positive definite, boundary parameter u and interior parameter x,
put R=D-B^T A^-1 B. Minimizing the ordinary quadratic form s^T L s gives
u^T R u. This is the usual discrete response, not our residual action.
For the actual finite comparator V=||L(x,u)||^2, write
x=-A^-1 B u+v. Then

    V=||A v||^2+||B^T v+R u||^2,
    v_min=-(A^2+B B^T)^-1 B R u,
    Q_eff=R[I-B^T(A^2+B B^T)^-1 B]R
         =R[I+B^T A^-2 B]^-1 R.

The middle matrix is positive definite, so ker Q_eff=ker R. This last
identity also follows by asking when both nonnegative residual terms can
vanish. Q_eff is generally neither R nor R^2. Directly Schur-complementing
L^2 must agree. Omitting its boundary residual rows allows the spurious
solution x=-A^-1 B u for every u and incorrectly assigns zero cost.

Our exact fixtures are weighted cycle connection Laplacians: an edge i,j
contributes w(s_i-t s_j)^2 with w>0 and t=+1 or -1. The kernel is parallel
sections, dimension one iff the cycle sign product is +1, otherwise zero.
Dirichlet restriction to the selected interior vertices is positive definite.
Vertex sign gauges act by diagonal orthogonal conjugation on L and induce
the same conjugation on R and Q_eff at boundary vertices. A positive on-site
term removes this kernel and is only an opposite comparator.

These exact identities are not a continuum convergence result, a charged
silver computation or a quantum determinant calculation. They expose which
rows and normalization an eventual same-action effective calculation needs.

## Literature and remaining duties

Lee, arXiv:math/0304250v2, section 1 defines the gluing response as the sum
of outward maps; Lemma 4.3 uses Green's identity for their positivity, and
section 4 gives the finite-cylinder off-diagonal response. These passages
were read directly. Its determinant theorems are not used as an OA quantum
theory or imported beyond their product-collar hypotheses. The added
nonnegative commutator term and gauge interpretation above are our explicit
conditional argument. No full-paper reading is claimed this turn.

The useful advance, if controls pass, is an admission-to-interface map that
accounts for BOTH partners. The algebraic silver asymmetry is not withdrawn.
An unmodified smooth compact closed flat de Rham domain still has its known
balanced grading; sewing has not generated a chiral domain. A justified
defect/end/interaction or changed operator remains a separate physical duty.

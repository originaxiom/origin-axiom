# R55 authored proof: the shrinking meridian and the neutral kernel

September 28, 2026. Conditional on the inherited R44 canonical end/core
and complete domains, R45 parent identification, R46 charged comparison,
R47/R53 nonzero harmonic q mode, and the exact ranks tested here.
This analytic argument is not certified by the finite tests.

## 1. Data and the two comparisons actually needed

Fix one of the four positive exceptional q values, q != 1, and its
canonical base; put k=log q. Work with F=End0(E). F is unaffected by a
scalar central twist. F15's reproduced ordinary H1(F) has dimension 3.
Let m be the meridian and M its actual holonomy. Define

    res_m: H1(M_base;F) -> coker(Ad(M)-I).

Here M_base denotes the base manifold, to distinguish it from the matrix.
We need only (i) injectivity of harmonic L2 H1 into ordinary H1 and
(ii) image contained in ker res_m. We do NOT need to identify the entire
end L2 complex or prove that every class in that kernel is representable.
R47/R53 already supply a nonzero L2 class in the q direction.

In R44/R45's periodic tail frame, r=log R/2 and x,t have fixed periods.
Norms are uniformly equivalent, for each fixed q, to the product norm

    g_ref=dr^2+exp(-2r)dx^2+dt^2,
    dvol_ref=constant exp(-r)dr dx dt,

with constant positive coefficient metric H_inf. This is a norm
comparison, not an assertion that the ACTUAL Hodge operator is a product.
The FLAT differential, however, has the exact connection in this frame:

    D_r=partial_r+A,           A=ad(2J),
    D_x=partial_x+exp(-r)B,    B=ad(N),
    D_t=partial_t+k ad(D0)+beta exp(-2r)C, C=ad(P), P=N^2.

J=diag(5,-3,1,-3)/8, D0=diag(1,-3,1,1), N_02=N_23=1;
all other entries of N vanish. The connection is flat. In particular
[A,B]=B, [A,C]=2C, [B,C]=0, and ad(D0) commutes with all three.
P=N^2 as FOUR by FOUR matrices does NOT imply C=B^2 on the adjoint.

The zero ad(D0) sector W0 has dimension nine. With its positive induced
Gram metric, A is self-adjoint. Its B-kernel K has basis D0,N,P with
A weights 0,1,2. The orthogonal complement of im B, Kminus=ker B*, has
basis D0,N^T,P^T with A weights 0,-1,-2. These are explicit matrix
identities checked independently of the global cochain computation.
The unequal entries of H_inf do not alter this assertion: on the
three-dimensional N block they are equal, and the fourth line is scalar.

## 2. Exact ordinary primitives of L2 one-forms are L2

Suppose a smooth L2 one-form eta is ordinarily exact: eta=D f for a
smooth global section f. No norm bound on f is assumed. It is enough to
prove f is L2 on the end; compact subsets cause no problem.

Split by ad(D0) in the comparison frame. On a nonzero weight, the t
Fourier operator i omega+k ad(D0)+beta exp(-2r)C has a uniformly bounded
inverse: its semisimple eigenvalue has nonzero real part and its commuting
nilpotent term admits a finite inverse series (R45). Thus D_t f=eta_t
implies ||f||_2 <= C||eta||_2 on those sectors. This estimate is applied
on each compact t circle BEFORE integrating r,x, so does not presume f
is already L2. Norm equivalence transfers it to the actual metric.

On W0, separate nonzero x Fourier frequencies. The finite nilpotent
inverse of i omega+exp(-r)B is uniformly bounded away from omega=0.
It gives the same bound using eta_x; the actual one-form norm controls
exp(r)|eta_x|, hence also |eta_x|. The remaining x average f0 satisfies

    B f0=exp(r) eta_x,0.

The right side is L2 by the one-form norm. On K-perp the fixed finite
matrix B has a positive smallest singular value, so (I-P_K)f0 is L2.
Self-adjoint A preserves K, so P_K commutes with A. For each K-weight j
in {0,1,2}, the radial equation is

    (partial_r+j) f_j = g_j,   g_j=(P_K eta_r)_j.

With w_j=exp(-r/2)f_j and h_j=exp(-r/2)g_j this becomes

    (partial_r+j+1/2)w_j=h_j.

At any fixed tail start r0 the smooth trace on the compact t circle is
finite. Its solution is the sum of an exponentially decaying boundary
term and convolution with exp(-(j+1/2)u), u>=0. The kernel has L1 norm
1/(j+1/2)<=2. Young's inequality, also for L2(t)-valued functions,
proves w_j in L2(dr dt). Thus f_j is in the required weighted L2 space.
All parts of f are L2. The identical argument works for the trivial
coefficient, where A=B=C=0 and K is the entire one-dimensional fiber.

Since Df=eta is L2, completeness and the R45 cutoff/Friedrichs argument
put f in Dom D0. If eta is harmonic, D*eta=0 and

    ||eta||^2 = <eta,Df> = <D*eta,f> = 0.

This proves the desired injection. It does not assume an ordinary
primitive is in the Hilbert domain by definition; that is what the
preceding argument earns. No Hodge-Fourier separation for the actual
nontranslation-invariant metric is used.

## 3. An L2 closed form cannot carry a meridian period

Let eta now be any smooth closed L2 one-form. On W0 take its x average.
The r,x component of Deta=0 is

    (partial_r+A) eta_x,0 - exp(-r)B eta_r,0 = 0.

Let Q be the orthogonal projection onto Kminus. It annihilates im B
and commutes with A. On its A-weight -j, j=0,1,2, the equation says

    (Q eta_x,0)_j = exp(jr) b_j(t).

The dx part of the norm has weight exp(r)dr dx dt. Any nonzero b_j
would contribute a positive multiple of integral exp((2j+1)r)dr,
which diverges. Thus every b_j vanishes and eta_x,0 lies in im B.

Circle parallel transport acts trivially on coker B. Integration of eta
around the x circle therefore has zero class in that quotient. Moreover
exp(B)-I=B times an invertible polynomial in B, so its image equals im B.
Changing tail height or frame transports this zero class to the actual
meridian quotient coker(Ad(M)-I).

On the NONZERO ad(D0) sectors the torus cocycle relation is

    (Ad(L)-I)u_m=(Ad(M)-I)u_l,

where L is the commuting longitude. Ad(L)-I is invertible there and
commutes with Ad(M)-I, so u_m is a meridian boundary for EVERY closed
torus class. This handles the other six adjoint directions; they were
not silently discarded. Together, res_m[eta]=0 for every L2 harmonic
class. For trivial coefficients the W0 calculation alone suffices.

## 4. Exact global upper bound and its matching lower bound

Use the unchanged corrected F15 complex Bglob:C15->C30,
Rglob:C30->C15 and its H1 basis H. Its upper fifteen rows concern m.
Put Bm=Ad(M)-I and Hm=H's upper fifteen rows. Then exactly

    rank(res_m)=rank([Bm,Hm])-rank(Bm).

The proposed success branch is rank Bm=10 and joined rank=12 at all
four points. This gives rank(res_m)=2 and dim ker(res_m)=1. Tests also
check that the actual q tangent is nonboundary and has zero restriction,
and that it spans this kernel modulo global boundaries. Derivatives of
tr(M^n), n=1,2,3, provide a separate conjugacy-invariant detector:
for left logarithmic tangent u, delta tr(M^n)=n tr(u M^n). Its rank and
kernel must agree with the meridian detector; mere dimension matching
without those matrix identities would be insufficient.

If these ranks pass, sections 2-3 give dim H1_L2(F)<=1. R47/R53's
nonzero harmonic q class supplies the opposite bound. Hence

    H1_L2(End0 E)=C alpha,     dim_C=1.

For the trivial coefficient the actual ordinary Fox complex has H1=C
and its meridian restriction has rank one. Sections 2-3 therefore give
H1_L2(C)=0. The surviving finite-volume constant supplies H0_L2(C)=C.
The complete Hodge/Riesz map to the actual dual gives equal dimensions
in complementary degrees: for the trivial coefficient (1,0,0,1), and
for the self-dual adjoint (0,1,1,0). The zero adjoint H0 uses R45's
global holonomy invariants, NOT just its cusp invariants.

## 5. Full parent count, and what it does not count

R45 identifies the actual coefficient decomposition

    248=(45,1)+(1,15)+(10,6)+(16,4*)+(16*,4).

R44/R46 already supply H1(E)=H1(E*)=C at the admitted exceptional
characters, no H0, and the all-degree vanishing for the 6. Consequently,
conditional on the successful finite ranks and the analytic inputs,
the COMPLETE internal harmonic dimensions by degree are

    (45,33,33,45),
    degree one: one singlet + one 16 + one 16*.

These are complexified internal coefficient counts, not 33 independent
Standard-Model generations, 33 gauge bosons, or a chiral spectrum.
The compact-real vector algebra is R45's so(10), dimension 45.
The two discarded ordinary adjoint directions are nonnormalizable
IN THIS fixed end/norm/domain. They remain algebraic deformations and
could describe different asymptotic data; this is no wider no-go.

One harmonic complex line is not by itself an all-orders complex moduli
space. R52/R53 earn the real q stationary curve and its tangent, not
every complex multiple's integrability. R54 supplies a nonzero paired
interaction, not numerical normalized couplings or vacuum selection.
We do not promote this count to an isolated complete EFT or numerical
mass gap. Nonlinear decoupling, profiles/tensors, physical chirality,
anomaly/end completion, scale setting, quantum control and gravity
remain distinct duties. The supplied parent/action/metric are not
derived by counting their modes.

Literature cross-check: Hausel--Hunsicker--Mazzeo,
https://arxiv.org/pdf/math/0207169, introduction and section 2.3,
describes fibred-cusp norms and weighted cohomology. Only these sections
were consulted; its scalar theorem is NOT used as a black box for our
nonunitary adjoint coefficient. Sections 2-3 above are the explicit
coefficient/domain argument instead.

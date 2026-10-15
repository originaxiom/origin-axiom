# The ordinary and twisted physical fermion operators

This authored calculation compares specified kinetic parents on the
existing four-real-dimensional elliptic total space X. It does not derive
spacetime, supersymmetry, E8 or a physical boundary law from the principle.

## A direct ordinary Weyl kinetic control

On M(3,1) times X supply a compact E8 connection and one complex positive
eight-dimensional Weyl field in its adjoint. The classical control action is

    S = integral sqrt(|g8|) [- <F,F>/(4g8^2)
                            + i bar(Psi) Gamma^M nabla_M Psi].

The compact invariant gauge pairing is positive on physical kinetic
coefficients. Retain the full adjoint and the nonzero gauge vertex
bar(Psi) Gamma^M [a_M,Psi]. At a flat connection with Psi=0 the bulk
equations are stationary. This is an explicitly supplied nonsupersymmetric
kinetic control, not a complete scalar, gravity, quantum or boundary theory.

Take Gamma^mu=gamma^mu tensor I4 and Gamma^(4+j)=gamma5 tensor i c_j.
With gamma5=i gamma0 gamma1 gamma2 gamma3 and Gamma8=-i product Gamma^M,
Gamma8=gamma5 tensor Gamma_X, where Gamma_X=-c1 c2 c3 c4. All eight
Clifford relations hold, and the positive Weyl space has complex rank8.
The Euler operator is i slash(partial)_4 tensor I minus gamma5 tensor
D_X. Thus its internal block is the actual geometric spin Dirac operator,
up to the displayed physical convention, rather than a copied de Rham
operator. Opposite four-dimensional chirality and internal chirality are
paired by this decomposition. Complex conjugation is not an additional
independently counted generation.

In a flat gauge frame the full E8 block is D_X tensor I248. The preceding
retained-register packet supplies the actual regular SL6 embedding and
the literal frame S for its six-dimensional coefficient. The (6,3,2)
block and its dual then give honest occurrences of that coefficient,
with their colour/weak spectators, inside this Hessian. The remaining
(35,1,1), (1,8,1), (1,1,3), (20,1,2), (15,bar3,1), (bar15,3,1)
are not removed. Full dimensions are35,8,3,40,45,45,36,36, summing248.
A local block map does not close that block under every interacting gauge
generator, establish a KK truncation or compute its global kernel.

## The supersymmetric surface parent has a different twist

The conventional partially twisted eight-dimensional gauge multiplet has
adjoint gauge, scalar and fermion fields; its bundles and R-twist are
specified in [Beasley, Heckman and Vafa, section3.2](https://arxiv.org/html/0802.3391#S3.SS2).
Its conjugate fields and the scalar in K_X are retained. The gauge and
scalar equations and fermion interactions belong to the full action,
including [AppendixC](https://arxiv.org/html/0802.3391#A3), not a freely
chosen collection of massless cohomology classes.

The (0,*) fermionic block uses the canonical Spin-c bundle. Locally,

    S_spin = Lambda(0,*) tensor K_X^(1/2),
    S_can  = S_spin tensor K_X^(-1/2) = Lambda(0,*).

For that block its kinetic operator at zero scalar is the canonical
Dirac sqrt(2)(dbar_A+dbar_A^*). The conjugate block carries the conjugate
form/R data and is related by the parent's reality law, not deleted.
The identification here concerns the derivative Hessian at zero scalar,
not the full Yukawa Hessian at a condensate. Ordinary spin and canonical
Spin-c are different bundles unless the required line is accounted for.

## The metric determines the missing connection

Retain the supplied orthonormal coframe

    e1=ell dx/y, e2=ell dy/y,
    e3=sqrt(A/y)(du+x dv), e4=sqrt(A y) dv.

The REAL volume density in (x,y,u,v) is ell^2 A/y^2. But the holomorphic
chart (tau,w), with w=u+tau v, has real Jacobian y. Hence its volume
density is ell^2 A/y^3. Using the real density directly as a holomorphic
determinant would miss one power. Independently,

    (e1+i e2) wedge (e3+i e4)
      = ell sqrt(A) y^(-3/2) d tau wedge d w.

The squared norm of the holomorphic canonical frame d tau wedge d w is
4 y^3/(ell^2 A), in our real-metric convention. Its constant factor does
not affect the Chern connection. With h this norm, the unitary connection
is (partial-dbar)log(h)/2, so

    a_K=-3i dx/(2y),    a_spin-vacuum=-3i dx/(4y),
    a_R=+3i dx/(4y),    F_R=+3i dx wedge dy/(4y^2).

This is also checked from every Levi-Civita connection entry: the spin
Fock vacuum is a common kernel of c1+i c2 and c3+i c4. Its spin connection
is -3i/(4ell) in E1 and zero in the other three frame directions. Adding
a_R makes it parallel. More strongly, the resulting connection on the
entire Fock basis equals the exterior connection on all (0,*) forms.
That connection and the Clifford symbol identify the differential operator,
not just a zero-mode example or its rank.

Use the already reconstructed full ordinary spin expression D_spin. Then

    D_can=D_spin+3i c1/(4ell),
    D_spin=sum c_j E_j-c2/(2ell)+c1 c3 c4/(4ell).

The mixed term is retained in both operators. The radial density unitary
transformation still removes only the -c2/(2ell) term. All coefficients
of the twisted Lichnerowicz identity agree with the additional Clifford
curvature +3i c1 c2/(4ell^2). Omitting or reversing a_R changes the
connection and fails the exterior-connection/vacuum comparisons.

For the optional original cusp line,

    D_can,n=D_spin-6i (n-1/8)c1/ell.

The fraction1/8 is bookkeeping for this fixed geometric R-twist, NOT a
replacement integral flux sector, a selected physical unit or an SM
parameter. K_X has automorphy (c tau+d)^(-3); its half-line requires the
chosen spin lift. The canonical Spin-c bundle exists independently of
a chosen square root, but the comparison to ordinary spin retains that
choice. No logarithmic compactification or end extension is silently
substituted for the open canonical bundle.

## The domain comparison is useful but does not transport the index

The difference B=3i c1/(4ell) is selfadjoint, with operator norm3/(4ell).
It anticommutes with total chirality and preserves the actual graded
critical trace plane: c1 commutes with Gamma_V=i c3 c4 and acts trivially
on the coefficient projector. Therefore, conditional on the admitted
global half-line and the prior total-domain hypotheses, bounded symmetric
perturbation gives the SAME graph-domain class and a selfadjoint twisted
realization for the rank-six problem. The geometric basis and global
transitions must still be transported, not identified by their ranks.

This does NOT prove a Fredholm chiral block, an unchanged total index or
a stable physical kernel. As a control, d/dt+(1/2)tanh t on the whole
line has the integrable kernel cosh(t)^(-1/2) and index1. Adding the bounded
constant1 preserves the doubled selfadjoint domain, but the kernel becomes
exp(-t) cosh(t)^(-1/2), which is not integrable at minus infinity, and the
index is0. The path crosses an asymptotic threshold. The actual cusp
requires its own harmonic/complement analysis for the chosen operator.
The foundation's vertical-gap result is not an estimate of that full
horizontal coupling.

## A scalar R shift is not a full adjoint E8 connection

For every H in e8, ad(H) is traceless. Every root charge occurs with its
opposite and all eight Cartans remain. A nonzero scalar q I248 has trace
248q, so no E8 adjoint generator acts that way on the whole parent.
This does not forbid a nonzero charge on a proper root or matter sector;
such a sector's conjugates and other charges have to be retained. The
geometric R line, a gauge cocharacter, and a scalar cusp coefficient are
different inputs until their actual bundle/action map is supplied.

The full supersymmetric parent is a viable candidate to test, not the
ordinary operator with its labels changed. The ordinary kinetic control
has a genuine operator map, not a claim of quantum consistency. In
particular, real adjoint weights and vanishing perturbative odd traces
alone do not settle higher-dimensional global anomalies; see the primary
[global-anomaly analysis](https://arxiv.org/html/2203.12631). No anomaly
cancellation, physical family count, normalized interaction or gravity
equation is inferred here. The next computation must use the chosen
parent's complete operator, scalar response and admitted global domain.

# Carry the lifts and derive the kinetic comparison

2026-11-18. P-C8 author hand derivation, not independently checked.
No scientific code, imports, CAS, quadrature or tests ran. Sources are
pinned in SOURCES.json. This concerns the literal compact magnetic
flux-(3,3,6) model of B1957, not the complete-cusp E8 parent. A shared
frame name does not identify those two constructions.

## 1. Keep the central parity when identifying the tick

SM-C20's card, lines 11–12, assigns `tau -> -conjugate(tau),
z -> conjugate(z)` to R0=diag(1,-1) and says it gives coefficient
conjugation with no mode permutation. The literal mode formula gives
a useful correction. For its spin-(0,0), flux-N functions,

    psi_j(-conjugate(z),-conjugate(tau);-conjugate(zeta))
                                      =conjugate(psi_j(z,tau;zeta)),
    psi_j( conjugate(z),-conjugate(tau); conjugate(zeta))
                                      =conjugate(psi_-j(z,tau;zeta)). (1)

The theta-series index is changed by n -> -n in the second identity;
the Gaussian factor and positive normalization transform the same way.
Thus the first geometric lift induces K and the second P K on
coefficients after conjugating the field, with P:j -> -j.

With the usual anti-Jacobi convention
`z' = conjugate(z)/(c conjugate(tau)+d)`, R0=diag(1,-1) has
`z'=-conjugate(z)`, consistent with K. Taking z'=conjugate(z) instead
requires P, up to a common scalar frame phase. The coordinate lift
or the coefficient rule must be corrected; they cannot be mixed.

This does not destroy the positive tick square. Since P commutes with
T,S,K and P²=1, both `T S K` and `P T S K` square to U. They agree
on the even ground pair and differ on the odd two-space. A square
test plus a ground-pair test therefore cannot distinguish the two
full six-mode lifts. The odd sector is an explicit adverse control.
An actual field map must carry the argument, Wilson line, adjoints
and metric, not just the matrix square.

## 2. The half-point cover has four sheets on a two-torus

For E=C/Lambda, a half t of w satisfies 2t=w in E. There are four
solutions, differing by

    E[2]={0,1/2,tau/2,(1+tau)/2}.

The cover of pairs (w,t), 2t=w, is the multiplication-by-two cover,
of degree four. Equivalently, making the numerical w/2 single-valued
requires doubling **both** periods; the sublattice 2Lambda has index
four in Lambda. A cover doubling one chosen cycle has degree two;
that is a different specification.

The source already retains the four matrices I,Z³,X³,Z³X³. Projectively
they form a Klein four-group. Linearly `Z³X³=-X³Z³`, so scalar cocycle
phases must also travel. The nontrivial actions under both primitive
periods in SM-C18 support this four-sheet structure, not a single
two-sheet cover. A special quotient or a specified one-cycle
restriction could reduce it, but it has not been given by these tests.

On E[2], M modulo two is `[[0,1],[1,1]]`. It cycles the three nonzero
elements and fixes zero. There is no nonzero M-invariant group
character E[2] -> Z/2: `ell(M-I)=0` forces ell=0 since M-I is invertible
over F2. Thus this fibre module cannot be identified with a base
orientation sign fixed by the even act through an invariant linear
character alone. This is scoped to that proposed group-law map.
Nonlinear assignments or additional carried data need separate tests.
The older SM-C13b scope note already warns that the fibre's 2-torsion
and the base's orientation have different carriers.

## 3. A native order-five recovery control exists

On E[5], multiplication by two is invertible, with inverse three.
For every w in E[5], the unique half that stays in E[5] is 3w.
The other three halves have order ten when w is nonzero. The prior
SM-C13 correction at line 61 already records this fact; it is reused
here, not claimed as a new torsion discovery.

This gives a natural alternative to taking the numerical representative
`q w/2`: as a homomorphism of E[5], its half is `3q w`. It commutes
with all integral changes of fibre basis. Any homomorphic choice of
half must have image in E[5], and is consequently this one, because
Hom(E[5],E[2])=0. Group-law compatibility is the stated hypothesis;
it is not silently derived from a desire to avoid a lift.

It can be used while retaining the original charges. Let a lift of
w obey 5w=lambda in Lambda and q_s=q_L+q_R. Set

    zeta_H=3q_s w,
    zeta_L'=q_L w+q_s lambda, zeta_R'=q_R w.

Then `2 zeta_H=zeta_L'+zeta_R'` exactly as complex numbers. The new
left Wilson representative differs from the old one by a lattice
vector; the relative half `(zeta_L'-zeta_R')/2` is congruent to
`3(q_L-q_R)w` in E. The corresponding mode/gauge transitions must be
transported. This is an admissible geometric control, not permission
to keep the old coupling coefficients in a changed Higgs frame.

These alternatives mean that the two advertised choices, an extra
binary cover or different hypercharges, are not an exhaustive list
of descriptions. One can use the appropriate bundle transitions, or
the native odd-torsion half with those transitions. Whether any such
description removes an independent **physical** input remains open:
some half-period changes are gauge-frame changes of the degree-six
line rather than different physical Wilson data. No input payment is
claimed from relabelling them.

## 4. Descent of an operator is different from averaging it

The primary magnetic-mode construction is formulated with charged
sections and gauge transitions, with a positive L2 normalization
([Cremades–Ibanez–Marchesano, sections 3.1.1 and 3.1.3](https://arxiv.org/pdf/hep-th/0404229)).
The literal source overlap has those same features.

Let Y_p map a Higgs coefficient space H_p to the matter tensor
space at p. Define the positive bubble `B_p=Y_p^dagger Y_p`. Under
a unitary change of Higgs frame G_p (and simultaneous unitary matter
changes), it transforms as

    B_p' = G_p B_p G_p^-1.                              (2)

This is legitimate endomorphism-bundle covariance. It does not require
B_p to commute with every transition matrix in one unchanged frame.
Eigenvalues of a pointwise covariant operator remain invariant.

To sum bubbles from different fibres in a reference space H_0, one
needs comparison maps `C_p:H_p -> H_0`. The covariant sum is

    B_0=sum_p weight_p C_p B_p C_p^dagger,
    C_p'=G_0 C_p G_p^-1,
    B_0'=G_0 B_0 G_0^-1.                               (3)

Its spectrum is well defined with those maps. An arbitrary comparison
can alter it; its connection or physical joining law must be derived.
The kinetic operator must transform in the same fashion as B.
Conjugating only B while leaving a numerical K fixed changes the
problem. Summing coefficient arrays at the same numerical indices
does not by itself derive C_p.

The source prescription

    Twirl(B)=(1/4)sum_(g=I,Z³,X³,Z³X³) g B g^dagger    (4)

is a distinct averaging operation in a fixed six-space. It is a valid
prescription and its conclusion below is retained. Covariance (2)
alone does not force (4). An ensemble average, a projection imposed
by a physical constraint, or an action-derived elimination could
justify it; each needs its actual law. This observation neither
rescues the untransported original sum nor proves unique Higgs
selection by a covariant alternative.

## 5. Recover the scalar twirl directly from the closed overlap

Use main's literal closed form, with common positive prefactor p:

    Y_ijk=p exp(2pi i k/6) Theta_c,
    k=i+j+1+3m mod 6, c=i-j+3m mod 6, m=0,1.

Here Theta_c is the stated theta function at xi; i,j run modulo
three. The bubble has entries only at l=k or l=k+3. Conjugation by
Z³ removes all k-to-k+3 entries on averaging. On its diagonal,

    c=k-1-2j mod 6.

For fixed k the three values of j give either {0,2,4} or {1,3,5},
according to the parity of k-1, each once. Conjugation by X³ exchanges
those two parity sums. Thus exactly, for every xi and tau in the
declared domain,

    Twirl(B)=(p²/2) sum_(c=0)^5 |Theta_c|² I_6.         (5)

It follows for each sector separately and for any sum of them. The
kinetic geodesic average and commutant projection do not restore a
splitting after (5). This is a second direct proof of the preserved
scalar-bubble result, using the supplied closed form. Its scope is
the averaging prescription (4), not every covariant physical response.

## 6. Derive the connection from the source mode norm

This calculation fixes what can be earned about the prescribed kinetic
term. Use the source's unit-cell inner product `integral_0^1 dx du`,
zero Wilson line, spin (0,0), N positive and
`tau=X+i y`, `z=x+tau u`. The normalized functions are

    psi_j=(2Ny)^(1/4) sum_n exp{ i pi N tau r²
                          +2 pi i N x(n+j/N)+i pi N x u },
    r=n+j/N+u.                                         (6)

The x integral kills all cross terms unless the mode and Fourier
indices agree. Summing over n and integrating u covers the real r
line. The normalized Gaussian moments are

    <r²>=1/(4pi N y),
    <r^4>=3/(16pi² N² y²).

Differentiating (6) at fixed x,u consequently gives, with the original
positive norm,

    <psi_j,partial_X psi_k>=i delta_jk/(4y),
    <psi_j,partial_y psi_k>=0,
    Gamma=<psi,d psi>=i dX/(4y) I_N.                   (7)

For a scalar profile `Phi=sum c_j psi_j`, its projected kinetic
derivative is `dc+Gamma c`. The variable entering the source's
`Y_h=sum h_k Y_k` and its bubble can instead be the conjugate
coefficient h=conjugate(c), since the Higgs occurs conjugated in
the overlap. Then the covariant derivative is `dh-Gamma h` and its
frame transition is the mode matrix W. Declaring this convention
prevents a mode/dual-coefficient conjugation from being lost.
Conjugating all variables consistently leaves the paired spectra
and ground-space results of the companion proof unchanged.

The part of d psi orthogonal to all N zero modes has squared norm

    <d psi_j,(I-P_zero)d psi_k>
                  = |d tau|²/(8y²) delta_jk.           (8)

Indeed its coefficient is `pi N(i dX-dy)(r²-<r²>)`, and the Gaussian
variance is `1/(8pi² N² y²)`. Equation (8) is the positive geometric
term retained when the **full** derivative norm is projected onto
the zero-mode family. Along unit-speed hyperbolic arclength it is
the scalar 1/8. A connection-only approximation omits it. It does
not split the two ground modes. Deriving how heavy modes and the
gauge constraint modify that projected kinetic approximation is a
further action/domain duty, not a free subtraction performed here.

## 7. Earn the phase cancellation along the golden axis

The normalized theta transformations in this frame give

    W_T=T, W_S(tau)=sqrt(tau/|tau|) S.

Composing the actual word `M=T S^-1 T^-1 S` with continuous roots
in the upper half-plane yields

    W_M(tau)=exp[i arg(tau+1)/2] U.                    (9)

For example the intermediate argument is
`tau_2=-(tau+1)/tau`, with
`arg(tau_2)=pi+arg(tau+1)-arg(tau)`, fixing that scalar.
An overlap comparison made only up to a phase is insufficient to
deduce (9); the theta frame and connection fix it together here.

On M's axis write `tau=1/2+(sqrt(5)/2)exp(i phi)`. Along the forward
geodesic from tau_0 to M tau_0,

    dX/y=-d phi,
    Delta phi=-2 arg(tau_0+1),
    integral Gamma=i arg(tau_0+1)/2 I_N.               (10)

The middle identity follows because the Möbius derivative is
`1/(tau_0+1)²`, rotating the tangent by minus twice that argument.
For the h convention above, remove the connection by
`h(s)=exp(integral_0^s Gamma) h_tilde(s)`. Its endpoint condition
is then

    h_tilde(L)=exp(-integral Gamma) W_M h_tilde(0)
               =U h_tilde(0).                        (11)

Thus the covariant derivative's spectrum recovers the prescribed
relative kinetic values `(theta_m/L)²` from the declared mode
embedding and positive norm. The scalar endpoint phase has not
been discarded; it cancels the connection phase. Retaining the
raw projected derivative norm adds the common term (8). A separately
supplied flat character on the base would shift the boundary phases
and must remain priced. So would a change of spin/central lift.

This is a concrete conditional derivation of part of the formerly
supplied kinetic prescription. It does not derive physical propagation
along this moduli-space loop, a metric scale for that propagation,
the Wilson-dependent family comparison over all sampled points, or
the full gauge-constrained effective action.

## 8. The next action computation is now precise

The preserved scalar twirl and the exact ground degeneracy hold for
the specified model. A physical alternative requires its own connection
and comparison maps (3), with the actual Wilson-line family, kinetic
operator, matter modes and all endpoint transitions. They must come
from the same action rather than an arbitrary matrix-frame choice.
The canonical odd-torsion half is a useful recovery control, not a
derived replacement observable.

WILSON_FAMILY_TRANSPORT.md derives a candidate projected connection
for the full Wilson family from the literal mode norm, including its
large-gauge transitions. This earns a kinematic comparison within the
specified embedding, not a law coupling different backgrounds.

Once that common physical operator is earned, the companion proof's coefficient
kappa, or its **complete relaxed** quartic difference B, is a bounded
selection target. The new connection, central-lift check and explicit
scalar geometric term make that target better specified. They do not
select a vacuum, supply three families, identify the physical observer,
or derive gravity. Foundational inputs counted removed remain zero.

# A marked physical family with coherent field transport

2026-11-16. Author hand construction under P-C3a. Independent proof review
is pending. No scientific implementation or execution is supplied. The
physical parent and its background remain the source's specified model.

## 1. Keep the actual universal cover

Let Sigma_tau=E_tau minus its marked puncture, with the supplied complete
curvature -1/ell^2 metric and marking F2=<a,b>. Normalize its Fuchsian
uniformization Gamma_tau:F2 -> PSL2(R). Different normalizations conjugate
every following map together.

For phi in Aut+(F2), put tau'=gamma_phi tau in the record's minus-period
marking convention. The affine map of compact elliptic coordinates has
derivative d=(C tau+D)^-1. It induces the outer class of phi. Lift its
punctured-surface biholomorphism to the universal covers and multiply by
the unique target deck element that gives the specified based class phi.
The resulting isometry P_phi satisfies

    P_phi Gamma_tau(h) P_phi^-1=Gamma_tau'(phi(h)).           (1)

Existence follows from the covering lift and the definition of the outer
class. For uniqueness, the ratio of two such lifts centralizes the entire
non-elementary Fuchsian group. It fixes the distinct ideal endpoints of
two independent hyperbolic elements, hence is the identity in PSL2(R).
Applying (1) twice and using uniqueness gives the exact composition law

    P_phi(tau') P_psi(tau)=P_(phi psi)(tau),
    tau'=gamma_psi tau.                                    (2)

In particular P_(I_h)=Gamma_tau(h). The peripheral commutator is a
nontrivial parabolic deck transformation, of infinite order. Its image
in the earlier finite root cover has order two. The two realizations
retain their own covering maps and coefficient systems.

For completeness, the surface isometry used here follows from the given
uniformization metric. The pullback is another complete conformal metric
of the same curvature. Their cusp ratio tends to one. The curvature
equation and the maximum principle on the puncture compactification force
their ratio to be identically one. Wolpert's section 1 gives the cusp
metric and ratio comparison used in this argument. [Wolpert, Cusps and
the family hyperbolic metric](https://arxiv.org/pdf/math/0508470v4)

Equations (1)-(2) construct the discrete marked-family maps. Horizontal
parameter derivatives, a Berry connection and dynamics of tau retain
their separate duties.

The resulting field law is geometric pullback with the declared internal
lifts. A physical registering or measuring reference can also retain the
path of an operation and its actual parallel transport. Its dynamical law
must be exhibited when interpreting this pullback as a physical act.

## 2. Retain the record's declared spin lift

Pull (1) back through the already constructed E -> Aut+(F2). The physical
odd extending spin has compact line O with the frame sqrt(dz). Use the
record's coherent metaplectic factor j_e(tau), whose square is C tau+D.
This is a specified compatible physical lift, with its input status
retained. In particular j_(J_h)=1 and j_epsilon=-1.

The holomorphic spin coefficient in the four-slot proof is s_e=j_e.
Its unitary phase is

    eta_e=j_e/|j_e|,
    eta_(ef)(tau)=eta_e(gamma_f tau) eta_f(tau).              (3)

The balanced background has the source generator H=H_++H_-. On every
retained gauge coefficient H has eigenvalue 2(m_++m_-), with m_++m_-
integer in the full 248 branching. Thus exp(-i pi H)=1. Consequently

    chi_H(exp(i theta))=exp(-i theta H/2)                   (4)

is a well-defined compact gauge circle with period 2pi. It satisfies
Ad_(chi_H(t)) Phi0=t^-1 Phi0 on both background spin fields. The spin
connection embedding A_spin=s_connection H/2 uses this same character.
Under a unitary spin-frame coefficient change t, the spin connection
changes by -d arg(t), and the gauge affine term from chi_H(t) gives
exactly that change times H/2.

The required geometric gauge factor is therefore G_e=chi_H(eta_e).
This derives a compatible field transport from the existing spin-induced
background. Other compatible spin lifts or twists retain their complete
field and registering data.

## 3. Transport the full structured state

Write the physical flat data as flavour rho and gauge K W, where K is
the actual bare or coherent compensator representation and W is the old
commuting Wilson datum. They commute with H. Retain the joint invariance

    rho(h) Ad_(K(h)W(h)) Phi0=Phi0.

For e=(phi,g_e) in E, set

    K^e=K composed with phi^-1,
    W^e=W composed with phi^-1,
    Phi0^e=g_e Phi0.                                       (5)

The record's identity g_e rho(phi^-1 h) g_e^-1=rho(h) proves the joint
gluing equation at (5). The scalar connection and curvature still use
H and the transported metric. All local stationary residuals remain
zero, since g_e preserves the flavour metric and epsilon pairing.

Use P_phi on arguments, s_e=j_e, V_e=g_e and G_e from (4) in the
four-slot transport proof. The orthonormal background pair transforms
as eta_e g_e Ad_(G_e)Phi0=g_e Phi0, as required in (5).

The scalar/form deck factors are Ad_(K(h)W(h)) in the odd compact spin
frame. The spin deck factors are rho(h) tensor Ad_(K(h)W(h)). Equations
(1),(3)-(5) intertwine these factors at every word h, including the
peripheral commutator. The spin-induced local connection is transported
with its affine law. Its curved parallel holonomy is retained as data
of that connection.

Composition of (5), (2) and the cocycles in (3) proves composition of
the actual field maps. The gauge factors multiply because (4) is a
circle homomorphism, and they commute with flavour maps. The source
and trace-dual target therefore form a coherent E-transported family
of the full physical operator with its complete graph domains.

The family includes changed marked holonomies and flavour-reference
states. A restriction to a fixed background uses its actual stabilizer.
In particular the three source state branches retain their reference
maps and full field rosters under (5). No invariant rank-three summand
or family multiplicity is extracted by this construction alone.

For another extending spin eta_h in {+1,-1}, transport its character as
eta^e=eta composed with phi^-1. In the compact spin frame the source
deck factors acquire chi_H(eta_h) in the gauge slot and eta_h in the
spin slot. This retains all four combined spin alternatives. The odd
class is fixed by this action and the three other classes can be
permuted in the family.

## 4. Recover the cusp populations from the actual frame conversion

Use a compact puncture coordinate w. Since the spin extends across that
puncture, its compact-frame transition on c is +1 for every extending
spin. W(c)=1. Both the old bare and specified coherent compensators give

    K(c)=Zeta P, P=exp(-i pi H/2), P^2=1,
    rho(c)=-I2.                                           (6)

The actual compact-frame field transitions are consequently

    lambda,a: Ad_(Zeta P),
    u,v:      -Ad_(Zeta P).                                (7)

Now pass to zeta=log(w)/(2pi i), on the cusp covering chart. Its spin
coefficient change is sqrt(2pi i w). The corresponding unitary phase
t has t(zeta+1)=-t(zeta). The spin-induced gauge-frame change is
chi_H(t), with

    chi_H(t(zeta+1))=P chi_H(t(zeta)).                      (8)

For lambda the extra deck factor P in (8) multiplies Zeta P and gives
Zeta. The normalized form's phase t^-2 is periodic and gives the same
answer. For the spin slots, the additional minus in t cancels the
minus in (7), and the gauge factors again give Zeta. The trace-dual
spin uses bar(t), which also changes sign, and the target form uses
t^2. Thus every input and output slot has the same cusp transition

    R_cusp(c)=Ad_Zeta.                                    (9)

This recovers periodic integer-root/Cartan fields and antiperiodic
half-root fields on all four slots. It also recovers the source's
120 and 128 coefficient populations. The coordinate-density changes
are exactly the isometries of the four-slot proof, so their complete
domains and Green pairings travel through (7)-(9).

In the compact frame the spin connection has a nonzero circulation
approaching pi near the puncture. In the cusp frame its angular
connection coefficient decays and its transition carries the bounding
spin sign. Computing (7) from a cusp-frame sign would mix these
descriptions. Equations (7)-(9) supply the explicit comparison.

The old quaternion centralizer zero-threshold channel survives in the
specified complete model. The level-five Pin2 alternative keeps its
own changed peripheral representation and conditional estimates. Those
spectral claims retain the independent analytic review of their source.
Bär's section 3 supplies the classical warped-cusp separation background
for the retained distinction between zero and nonzero angular channels.
The interacting four-slot estimates belong to the repository's own
physical proofs. [Bär, The Dirac Operator on Hyperbolic Manifolds of
Finite Volume](https://arxiv.org/pdf/math/0010233v1)

## 5. What has become explicit

Within the declared action and geometric family there is now an exhibited
coherent based geometry, spin-induced gauge compensation, source/target
field map and complete-domain transport. The construction reuses the
previous algebraic state law (5) and adds its actual geometric realization.

The metric/parent, identification of the physical surface group, rho,
embedding, Wilson, declared spin lift and measuring-sector map remain
assumptions or derivation duties. No foundational input is counted removed.
The companion calculation evaluates the residual after a natural inner
operation is closed on a gauge-equivalent physical background.

These are classical field/operator identities. Quantum determinant-line
and measure phases, anomaly accounting and a law composing physical
sectors retain their own earning conditions.

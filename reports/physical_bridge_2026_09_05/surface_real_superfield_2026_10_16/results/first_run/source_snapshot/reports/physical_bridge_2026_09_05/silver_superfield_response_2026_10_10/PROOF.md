# Averaged real response and its linear fermion consequences

Authored before execution. Conditional mathematical argument and same-seat
different-method controls; outside analytic review remains owed.

## 1. One supplied superspace functional

On the compact oriented three-core keep a fixed positive internal metric,
the invariant trace and G=exp(2V). In a unitary gauge use Hermitian gauge
potentials, Phi_i=A_i+iB_i and the actual conjugate barPhi_i. The real
kinetic piece is

    S_K = 1/4 integral d4x d3y sqrt(g) d4theta Tr(Z_i Z^i),
    Z_i = G^-1 partial_i G+i G^-1 barPhi_i G-i Phi_i.

Keep the 4D gauge kinetic piece and the relative holomorphic CS functional
of the preceding complementary packet, with its affine counterterm and
its parent-fixed nonzero multiplier. No term is dropped by applying a
closed-manifold integration by parts to a core with boundary. The flat
superfield formula is Luedeling 4.3-4.16; interpreting Phi as the twisted
one-form on the supplied curved core is an explicit parent choice, with
Braun B.1 the component cross-check. No emergence of this action is proved.

Let s and k denote the commuting structure and gauge sl5 factors in E8.
The fixed flat reference Phi_star is structure-valued. On the boundary,
V is INTERNALLY PARALLEL in k (arbitrary 4D superfield), and the tangential
chiral fluctuation a lies in A1=im h2+L, with its actual conjugate. These
are the preceding k-invariant cyclic Hodge projector and harmonic choice,
not pointwise subbundles. The relative CS boundary pairing vanishes by
the proved isotropy. A2=ann_B(k) includes exact tangential two-forms.

## 2. Exact surface variation and reality

Put eta=G^-1 delta G. Direct product differentiation gives

    delta Z_i = partial_i eta+i[Phi_i,eta]+[Z_i,eta]
                    +i G^-1 delta barPhi_i G-i delta Phi_i.

Only the first term differentiates the varied vector field internally.
Trace(Z_i[Z^i,eta])=0. Integrating that first term with the internal volume
form gives exactly

    delta S_K|boundary = 1/2 integral d4x d4theta integral_Sigma
                            Tr(Z_n eta).

Normal is outward. The gauge kinetic piece has no internal derivative.
Phi variations in S_K have none either. The holomorphic CS boundary
variation has already been canceled with its actual reference term.
Thus this is the remaining vector surface variation, not all bulk EOM.

G is positive Hermitian and Z_i^dagger=G Z_i G^-1. Real variations obey
eta^dagger=G eta G^-1, making Tr(Z_n eta) real. At the boundary G lies in
the complexified k group and is internally parallel. The finite-dimensional
integrated projection Pi_k commutes with Ad_G: trace invariance, k stability
and internal constancy prove this. Consequently Pi_k Z_n has the same
twisted reality. Conjugation by G^(1/2) turns both factors into Hermitian
traceless elements with the positive trace pairing. The derivative of
exp(2V) is invertible on real Hermitian k. Stationarity against every real
k superfield variation is therefore equivalent to

    Pi_k Z_n=0,  <c,Pi_k Z_n> = integral_Sigma Tr(c Z_n), c in parallel k.

This is not pointwise deletion of all k-valued functions. A cos(x) k flux
has zero integrated projection on the torus and is allowed by this test.
Replacing Pi_k by a pointwise projector changes the boundary law and must
not silently inherit the old cone counts. Formal superspace reality is
understood componentwise; Grassmann nilpotent terms follow the body by
the finite-dimensional real nondegeneracy recursion.

## 3. Boundary gauge transformations and supersymmetry scope

Writing g=exp(i Lambda), the finite rules are

    G' = g^dagger G g,
    Phi'_i = g^-1 Phi_i g-i g^-1 partial_i g,
    Z'_i = g^-1 Z_i g.

The derivative of g in the normal direction cancels EXACTLY in Z'_n;
it need not vanish or belong to k. At the boundary g itself is internally
parallel in the k group. Then the essential vector/tangential traces and
the projected response transform covariantly. Tangential D_star g=0,
and Ad_g preserves A1 by its k stability. For infinitesimal parameters
whose boundary value is in k, F_t lies in A2, hence the remaining
holomorphic gauge surface term integral Tr(Lambda F_t) vanishes.
This is the infinitesimal/small-gauge statement, not a proof about every
large transformation or a quantum anomaly.

Superspace Q acts on external variables, commuting with the fixed internal
projectors. WZ compensation has k-valued, internally constant boundary
value since the boundary vector multiplet does. Its tangential action
therefore preserves A1. This explains algebraic covariance; it is NOT
a completed nonlinear off-shell physical domain/energy proof. In particular
normal derivatives and auxiliary elimination must not be forgotten.

## 4. All slots of the projected linearized response

Linearize at V=0, Phi_star structure-valued, with static background and
zero auxiliaries. Invariance gives Pi_k[barPhi_star,v]=0 for ANY v because
[c,barPhi_star]=0. The projected response is precisely

    Pi_k delta Z_n=Pi_k(2 partial_n v+i(barPhi_n-Phi_n)).

The finite controls use a rescaled WZ/exterior-coordinate convention:
theta=(t1,t2), bartheta=(b1,b2), X=theta sigma^mu bartheta q_mu,
sigma=(I,Pauli). Coefficients are ordered with all odd generators included;
dagger reverses products and swaps t/b and each fermion/conjugate.

    Phi=e^(iX)(a+iB+t1 psi1+t2 psi2+t1 t2 F),
    barPhi=Phi^dagger,
    partial_n v=-theta sigma^mu bartheta A_mu,n
                   +g_chi+g_chi^dagger+(1/2)t1 t2 b1 b2 D_n,
    g_chi=t1 t2(b1 barchi1,n+b2 barchi2,n).

Here q_mu are formal real external derivative jets, NOT a momentum fit.
F and the spinor variables absorb nonzero conventional factors relative
to Luedeling 4.1-4.2. This is an invertible component rescaling, not a
claim about a new canonical kinetic normalization. All 16 superspace
slots, including odd coefficients, are generated, not filled from a table.
The invariant consequences, independent of these nonzero rescalings, are:

- lowest slot: Pi_k B_n=0;
- linear odd slots: Pi_k psi_n=Pi_k barpsi_n=0;
- chiral/antichiral quadratic slots: Pi_k F_n and its conjugate vanish;
- mixed slots: Pi_k( A_mu,n-partial_mu A_n )=0;
- cubic odd slots: nonzero normal chi jets plus external derivatives
  of normal psi; after the primary normal-psi law, Pi_k partial_n chi=0;
- highest slot: a normal auxiliary jet plus a wave-operator multiple
  of B_n; after its lowest law, Pi_k partial_n D=0 in this linear test.

The response is Hermitian under the actual anti-involution. Ignoring
fermion parity, chiral-coordinate shifts, or the high slots is not a
legitimate component expansion.

The NORMAL Gaugino jet is an additional OFF-SHELL equation, not a primary
first-order trace. In the linearized normal-psi equation from the supplied
four-Weyl bilinear (Braun B.12), its other terms are external derivatives
of normal psi and the tangential covariant curl of psi_t. For c in k,

    integral_Sigma Tr(c D_t psi_t)=integral_Sigma d Tr(c psi_t)=0.

Thus its integrated projection, with the primary normal-psi law, already
implies the normal chi-jet law on smooth solutions. It adds no independent
linear ON-SHELL constraint there. The linear normal auxiliary projection
is also compatible with F_n proportional to tangential curvature: D_t a
is exact and [a,a] lies in ann_B(k). This does NOT prove the full nonlinear
jet relations or equality of Sobolev operator domains. Normal derivative
traces cannot simply be added to an H1 first-order graph without care.

## 5. The existing harmonic background is not killed by structure flux

The background's flat connection and harmonic metric live in structure
SL5. Choose the same positive boundary K as the physical coefficient
metric; the induced E8 compact metric and k action are compatible. This
metric identification is SUPPLIED and priced. Wu-Zhang Proposition 3.3
gives the existing smooth compact Dirichlet harmonic metric. Flatness and
the moment equation give F_star=0 and mu_star=0; no new PDE solve occurs.

Invariant orthogonality follows within E8, not from matching dimensions:
k=[k,k], [k,s]=0, so Tr([k,k]s)=Tr(k[k,s])=0. At V=0 the background
Z_n=2B_star,n lies in s, hence Pi_k Z_n=0, even pointwise. The tangential
fluctuation and all background fermions/auxiliaries vanish. The bulk
auxiliary/boson first variations vanish by F_star=mu_star=0. The relative
CS surface and the real vector surface above vanish as well. This gives
conditional CLASSICAL FIRST-VARIATION STATIONARITY of that supplied
background for this law. Its nonsplit structure flag flux is not a gauge
flux and is not required to vanish. A k-valued constant normal flux would
fail the response, as the opposing control shows.

This is not stability: the auxiliary-eliminated boundary action, quadratic
energy and compatible physical fermion realization still have to be derived
together. Nor does a first variation count charged modes. The previously
proved mathematical Hodge/cone counts remain intact but are not promoted
to physical generations here. Nonlinear supersymmetry, all gauge classes,
physical adjoint/kernel, anomaly/inflow and generated selection remain.

Primary formulas: [Luedeling](https://arxiv.org/html/1102.0285v1),
[Braun et al.](https://arxiv.org/html/1812.06072v2),
[Wu-Zhang](https://arxiv.org/html/2109.01776v1).
This text does not assert that their closed-space component simplifications
automatically include our relative boundary functional.

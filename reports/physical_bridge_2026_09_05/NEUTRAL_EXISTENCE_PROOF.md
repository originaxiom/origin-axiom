# R51 authored proof: actual finite-energy solutions, strong-domain join separate

September 27, 2026. Conditional on R42/R44 canonical complete geometry,
R45's all-q density input and R47's actual flat family. Local NPC
Dirichlet/regularity theory is external; finite tests do not certify
these analytic inputs or constitute independent review of this proof.

## 1. One fixed base and a finite-energy competitor

Fix q0>0, q0!=1, g0=h_q0 and the canonical positive metric H0. R47
constructs a smooth family C(q) of flat connections on the fixed bundle,
equal to C0 at q0, with explicit tail

    C(q)-C0 = [(log q-log q0)D+(beta(q)-beta(q0))P/R]dt,
    beta(q)=6/(q-q^-1).

Keep q in a compact interval about q0 avoiding 1. R44/R49 give bounded
dt norm, bounded coefficient matrices in H0, finite volume and smooth
compact core. Thus a(q)=C(q)-C0 is uniformly bounded and in L2, with
||a(q)||_2=O(|q-q0|). The comparison norm's exact tail integral is
24s^2/sqrt(R0)+(2/5)(Delta beta)^2 R0^(-5/2), s=log(q/q0).
This comparison expression is not the actual canonical energy value.

Split C(q) using the FIXED H0. Its Hermitian part is
Psi(q,H0)=Psi0+Herm_H0(a(q)), so

    E(q,H0) <= 2 E(q0,H0)+2||a(q)||_2^2 < infinity.       (1)

In particular E(q,H0) is locally uniformly bounded (and continuous).
R42 supplies E(q0,H0)<infinity. This is a real equivariant reference
map for rho_q on the fixed g0 universal cover; no deformed base metric
or surface conformal invariance was used. Fixed unitary central twists
act trivially on the target Y=SL4(C)/SU4.

## 2. Existence, with the compactness step exposed

Theorem 1.1, printed p.513 in Koziarz--Maubon,
[Representations of non-uniform lattices of PU(m,1)](https://www.numdam.org/article/AIF_2008__58_2_507_0.pdf),
states Corlette's complete-domain finite-energy existence theorem for a
Hadamard target and an action without a fixed point at infinity. This
general theorem, not their complex-hyperbolic application, fits (1).
R45's SL4(R) density excludes an invariant proper complex flag, hence
a fixed visual-boundary point of Y. The original Corlette 1992 proof
was not obtained/read here; the published statement was read directly.

For additional transparency reuse F12's authored exhaustion, now with
a finite whole-energy bound. On compact truncations M_T minimize the
flat-Y-bundle Dirichlet energy with H0 as boundary value. In parallel
charts the transition functions are constant target isometries; the
Sobolev minimization/regularity argument of F12 section 3 applies.
These are sections, not globally trivial maps. Local theory is recorded
in Riestenberg--Smillie, [section 2.3](https://arxiv.org/html/2511.11469v3#S2.SS3),
Propositions 19--22. Its new global coarse-stability theorem is not used.
Minimality gives the stronger estimate

    E(q,H_T;M_T) <= E(q,H0;M_T) <= E(q,H0).              (2)

For a fixed compact K, the Bochner inequality and local mean-value
estimate give uniform gradients, independent of T. Choose finitely
many based generator loops inside a fixed compact core. Their target
displacements at H_T(p) are bounded by those gradients. Consequently
each generator, its inverse and each fixed word have bounded operator
norm in H_T(p).

The complex associative algebra of rho_q is all Mat4(C): a linear
subspace containing its words contains their Zariski closure SL4(R)
and its complex span, which is Mat4(C). Choose sixteen words forming
a basis at this fixed q. Each matrix unit E_ab is their fixed linear
combination, hence has bounded H_T operator norm. Its rank-one identity

    ||E_ab||_(HS,H_T)^2=(H_T)_aa (H_T^-1)_bb             (3)

bounds tr(H_T)tr(H_T^-1), and thus its condition number. Determinant
one then bounds H_T and H_T^-1. This prevents target escape. A scalar
commutant alone is insufficient; the explicit reducible control in the
producer has a scalar commutant and escaping metrics.

Gradient bounds along paths and local elliptic estimates now yield a
smooth diagonal limit H_q, positive and determinant one on every compact
set. Fatou/exhaustion and (2) give E(q,H_q)<=E(q,H0)<infinity. The limit
solves the full moment equation. With the already flat C(q), its split
C(q)=A_q+Psi_q therefore satisfies

    F_Aq+Psi_q wedge Psi_q=0, d_Aq Psi_q=0, delta_Aq Psi_q=0. (4)

This is an actual nonlinear solution for every nearby q, not a formal
jet. No explicit global numerical profile has been computed.

## 3. Anchored cusp estimate and uniqueness in the finite-energy class

The fixed canonical end is uniformly comparable to

    a dr^2+(a/2)exp(-2r)dx^2+a(2k0 dt+dr/2)^2, a=3/4,
    dvol comparable to exp(-r) dr dx dt.                (5)

The vector partial_r at fixed x,t has bounded length, namely squared
model length 5a/4. If f is locally Lipschitz with df in L2, integrate
along these radial rays. On any finite interval [r0,T], integration
by parts and Young's inequality give

    I_T = integral f^2 exp(-r)dr
        = f(r0)^2 exp(-r0)-f(T)^2 exp(-T)
          +2 integral f f' exp(-r)dr
        <= f(r0)^2 exp(-r0)+(1/2)I_T+2 integral (f')^2 exp(-r)dr.

Integrate the torus variables and use (5). The fixed collar trace is
finite. Monotone convergence yields f in L2. This is an ANCHORED
estimate; the constant function disproves a bound using df alone.
It does not presume f bounded or discard an uncontrolled outer term:
the outer term has the favorable negative sign before taking limits.

Let H1,H2 be any two smooth finite-energy harmonic metrics for the SAME
rho_q and g0. Their target distance f descends to a locally Lipschitz
scalar with |df|<=|dH1|+|dH2|, hence df in L2 and, by the preceding
estimate, f in L2. NPC distance convexity makes f weakly subharmonic.
Testing with chi_T^2 f (or a smooth distance regularization) gives

    integral chi_T^2 |df|^2 <= 4 integral f^2 |dchi_T|^2 -> 0. (6)

Complete cutoffs have bounded gradients tending to zero; f is L2.
Thus f is constant. The NPC second-variation equality implies the
geodesic interpolation between H1,H2 is parallel with zero curvature
term; see also Riestenberg--Smillie section 5.1 Proposition 43. In the
positive-metric model this means the trace-free self-adjoint logarithmic
variation s obeys d_A s=0 and [Psi,s]=0, hence d_C(q)s=0. Its value
commutes with the full holonomy algebra. Equation (3)'s full-algebra
hypothesis makes it scalar; trace zero makes it zero. Therefore H1=H2.

Unlike F13's hyperbolic-base result, no bounded-distance end class has
been assumed. This extension uses FINITE energy and the canonical
anchored estimate. It is not a claim about infinite-energy metrics.
The trivial representation has distinct constant determinant-one
metrics, showing why the holonomy hypothesis cannot be removed.

## 4. Continuity on compact subsets, not a Banach-space branch theorem

If q_j tends to q*, choose a word basis as in section 2 at q*. Its
nonzero determinant stays nonzero near q*, with bounded inverse word
coefficients. The reference energies in (1) are locally uniformly
bounded. Generator displacements, target anchoring and local elliptic
estimates are consequently uniform in j, in flat charts varying
smoothly with q. Subsequence compactness gives a smooth-on-compacts
limit that is rho_q*-equivariant, harmonic and finite energy. Uniqueness
identifies it with H_q*. Every subsequence has this unique limit, so
q -> H_q is continuous in C-infinity on compact subsets. At q0 it is
the original canonical H0, which already has all these properties.

This does NOT prove differentiability in q, uniform convergence at
infinity, a bounded complex gauge, or convergence in X=Dom(Q0) intersect
L4. Slegers' [analytic dependence paper](https://doi.org/10.1007/s00229-021-01345-z)
assumes a CLOSED domain throughout; Theorem 2.8 and Proposition 3.3 do
not provide that missing cusp theorem. Its full 16-page text was read.

## 5. Why a bounded-gauge shortcut is unsafe, without killing the branch

In the exact LIMIT metric (5), the central end coefficient D commutes
with the whole connection and its adjoints. On this scalar coefficient,

    delta(dt)=-1/(4ak0), Delta(r)=1/a.

Thus the model solution of Delta sigma=delta(D dt) is
sigma=-rD/(4k0), and D dt-d sigma=D dv/(2k0) is coclosed. The linear
growth is compatible with every finite Lp in this cusp but not L-infinity.
No actual-end expansion or unique global primitive is inferred from
the model. It demonstrates a concrete allowed resonance that must be
handled, not suppressed by a bounded-gauge assumption. End-central
growth may be resumable; it is not an obstruction theorem.

## 6. What has and has not joined to the supplied physics

For each q the metric H_q can be transported isometrically to H0 by a
smooth positive determinant-one bundle map. Transport (4) simultaneously;
one gets smooth fields on the SAME g0 and fixed positive H0, finite Higgs
energy and identically zero residual-square potential. This is a method
of constructing fields, not declaring complex gauge a physical symmetry.
On compact subsets those fields converge smoothly to the original ones.

The map need not be uniformly bounded on the end. We have NOT proved
that their additive difference u(q) belongs to X, tends to zero in X,
has derivative R47's harmonic alpha after compact gauge fixing, or has
a normalized finite kinetic tensor as a time-dependent collective field.
Thus R50's admissible two-jet and R51's exact finite-energy solutions
are now both present, but their strong-domain/tangent JOIN remains a
specific obligation. No fixed-end physical vacuum branch is claimed.

No q selection, breaking of R48's pairing, net physical chirality,
gravitational backreaction, quantum completion or empirical prediction
follows. R40/R41 and the other coefficient/source/end routes remain live.

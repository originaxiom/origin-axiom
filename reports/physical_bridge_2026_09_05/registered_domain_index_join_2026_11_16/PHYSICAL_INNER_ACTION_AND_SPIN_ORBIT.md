# Actual inner action on the physical kernel and its spin orbit

2026-11-16. Author hand derivation under P-C3a. Independent review remains
pending. The spectral uses below explicitly retain the analytic hypotheses
of the existing coupled half-root kernel theorem. No scientific code ran.

## 1. The compact-frame deck maps

Use the marked physical family and four-slot maps in the companion proofs.
Let eta_h in {+1,-1} be an extending spin character in the compact elliptic
frame. Set P=exp(-i pi H/2), and write eta_h=(-1)^b_h. The actual source
deck maps, evaluated with the argument Gamma(h)x retained, are

    R_h(lambda,a)=Ad_(P^b_h K_h W_h)(lambda,a),
    R_h(xi)=eta_h rho(h) Ad_(P^b_h K_h W_h)xi.               (1)

The compact-frame coordinate derivative for this deck operation is one.
All factors in (1) commute except the internally retained K representation
and rho representation, which act on their separate tensor factors.
K_h and W_h commute with P. These maps specify quotient sections. The
spin-induced curved connection also has its own parallel transport.

## 2. Close a natural inner operation on the actual background

For e=J_h the physical-family map gives

    K^e=K_h^-1 K K_h, W^e=W,
    Phi0^e=rho(h)Phi0=Ad_(K_h^-1)Phi0.                     (2)

The old Wilson fixes the background pair and commutes with K. The
gauge map Ad_(K_h) closes (2) back onto the original marked gauge bundle
and stationary pair. The declared metaplectic lift has j_(J_h)=1.
Before this closing, the field map has scalar/form value factor one and
spin value factor rho(h), with argument Gamma(h)^-1 x.

After closing, it has value factors Ad_(K_h) and rho(h)Ad_(K_h). Insert
the actual inverse-argument relation from (1). The resulting operators on
global physical sections are exactly

    C_h(lambda,a)=Ad_(W_h^-1 P^-b_h)(lambda,a),
    C_h(xi)=eta_h^-1 Ad_(W_h^-1 P^-b_h)xi.                 (3)

The trace-dual target uses bar(rho(h)) before closing and the corresponding
target transition in (1). It gives the same residual (3). Thus (3)
intertwines the actual physical mass map on both of its complete domains.

Define the global background symmetry

    Z_phys=diag(Ad_P,Ad_P,-Ad_P,-Ad_P).                     (4)

The minus on the spin slots is the centre of the parent's flavour SU2.
Ad_P sends both background raising sections to their negatives, so the
combined operation (4) fixes the stationary pair. It commutes with K,W
and the full mass operator, preserves the kinetic metric and leaves the
complete domain invariant. Equation (3) becomes

    C_h=Ad_(W_h^-1) Z_phys^b_h.                            (5)

For the odd spin eta=1, (5) is a pure unbroken gauge transformation.
Closing (2) instead by K_h W_h removes that gauge factor as well. Both
closings transport the gauge reference, fields and currents. Their
difference remains an explicit background gauge automorphism.

Equation (5) evaluates the residual of the earlier general section
formula using the actual physical transitions and state law. It reuses
the prior observation that (2) is gauge equivalent and supplies the
missing argument, spin and trace-dual factors.

## 3. Evaluate Z_phys on the retained half-root cohomology

Use the full two-triple decomposition and coupled half-root reduction.
Each physical half-root source is V_(3/2) tensor V_(3/2), retaining its
complementary four or conjugate four. On joint weight (m,n), Ad_P has
eigenvalue exp[-i pi(m+n)]. The surviving fibre representatives are

    degree 0: |3/2,3/2>,
    degree 1: e_+ tensor |-3/2,3/2>,
              e_- tensor |3/2,-3/2>,
    degree 2: e_+ wedge e_- tensor |-3/2,-3/2>.             (6)

Their gauge P phases are respectively -1,+1,+1,-1. The flavour centre
in (4) is +1 in degrees zero and two and -1 in degree one. Therefore

    Z_phys=-I on every reduced line in (6).                (7)

The corresponding spin powers are S^-3, S, S, S^5, as in the source.
Both Dolbeault degrees retain the same (7). The physical Hodge/kernel
identification is equivariant because (4) is a unitary chain map.
This passage uses the existing bounded retraction and complete-domain
Hodge hypotheses, which still require independent analytic review.
It introduces no pure-slot truncation of reconstructed physical modes.

For a fixed gauge representation R, let chi_R(h) be the old Wilson
character on that coefficient. Equation (5) then acts on its physical
half-root kernel by the common character

    C_h|ker(M_R)=eta_h chi_R(h)^-1 I.                      (8)

The same holds on the adjoint kernel with its properly transported dual
representation. A different closing through the connected unbroken
gauge group changes R's gauge action and leaves the multiplicity factor
unchanged. Additional disconnected or reference-sensitive operations
retain their own representation calculation.

In particular the coherent corrected odd-spin charged colour-singlet
block with three modes has C_h=I on all three. Its triplet and conjugate
blocks retain their own counts and Wilson phases. This sharpens the
physical meaning of the old three-mode positive within that construction.

## 4. A scoped comparison with the native registered triplet

The native axis triplet has inner matrices O_(rho(a)), O_(rho(b)) with
three distinct nontrivial parity characters. For example, one generator
has eigenvalues (1,-1,-1). A fixed physical multiplicity space satisfying
(8) has one common inner character.

An equivariant invertible map between these two rank-three spaces would
have to preserve their inner eigenvalue multiplicities. This fails under
the specified transport and closing. With odd spin and trivial Wilson
character, even a nonzero map into the physical trivial inner module
vanishes, since the native triplet has no common invariant vector.
After a common scalar twist, at most one native parity line can match a
given scalar physical character, so the map has rank at most one.

This conclusion applies to the fixed-background half-root candidate,
the declared spin lift and the specified gauge closings. The full
registering architecture retains other carriers, state orbits, domains
and measuring representations. Its three-family problem stays open.

## 5. The larger state family retains a positive parity route

The three nonzero genus-one spin characters are precisely the three
parity characters chi_p used by the native triplet. The odd spin provides
their reference origin. For a nontrivial spin label p, the physical
residual (8) in a Wilson-trivial coefficient is

    C_h=chi_p(h) I.                                       (9)

Thus the missing three distinct inner characters are present across the
three allowed spin-labelled physical sectors. This statement follows
from the full field/domain map, including the associated gauge factor
P^b_h. Their direct sum retains the native inner-character pattern,
with each character's actual physical multiplicity.

For the bare lift, the source gives two singlet modes in each such spin
class, so the inner-level direct sum has two copies of that parity
pattern. Both conjugate charged sectors retain it. Its net physical
index in the retained U3 representations keeps the source's zero value
under these hypotheses. Weak-current chirality retains its own operator
and massive-vector response test.

The complete state law must accompany this observation. Word moves also
transport K,W,Phi0. At fixed old K, the source singlet kernel counts for
the three nontrivial spin labels are two, two and three. Permuting only
those spin labels would therefore fail to intertwine the physical
operators. In the actual word orbit of one complete structured state,
the companion unitary transport preserves its kernel dimension while
moving all those data together.

Consequently (9) identifies a constructive candidate for further work on
the larger physical state family. To obtain a full E-module, retain the
whole structured orbit and compute its stabilizer action, central sheet,
mode Grams and transition maps. A rank-three subbundle then needs an
actual invariant inclusion. Treating different background sectors as
simultaneously propagating local families additionally needs a common
action, state/sector composition and interaction law. These are explicit
physical tasks, with (9) providing an existing positive to preserve.

The simultaneous spin/flavour re-factorization already proved in the
repository keeps its own scope. Changing S while rebuilding the
spin-induced gauge bundle and keeping rho fixed changes the present
physical data. Transporting a fixed combined bundle under that earlier
re-factorization carries its reference and gauge background together.
These comparisons must remain explicit when using (9).

## 6. Central and end controls

For h=c, eta_c=chi_R(c)=1, so (8) gives C_c=I. The actual cusp section
transition on the same physical block remains Ad_Zeta, recovered by the
companion compact-to-cusp frame calculation. The inverse argument and
quotient transition are both included in the section operator (3).

For epsilon, j=-1 and g=-I. The geometric spin/gauge factor in the
companion proof sends the reference pair to -Phi0. Closing by P gives
the identity on all four slots. Closing by the coherent compensator
K_pi=Zeta P gives Ad_Zeta instead. Their difference is a retained
background gauge automorphism. It is carried by the measuring reference
when comparing the two closings.

The existing half-root compact-resolvent and zero net U3 index result
remain the source's conditional positives. A unitary equivalence to a
different single Fredholm operator would preserve that representation-
valued index. The modular-base three-per-unit problem still needs the
physical field, base and domain identification. A genuine family-index
or higher-dimensional construction has additional operator data and
must be analyzed on those data.

## 7. Next consequential calculation

The four-slot transport has now located where the native parity can live
in this supplied physical model. A fixed odd-spin three-mode block gives
the scalar action (8). The enlarged spin/state architecture retains the
three characters (9). The next mathematical target is the stabilizer
module and actual invariant inclusions on that full structured orbit.

The next physical target is its common composition/end dynamics. The
complete quaternion parent still carries its retained centralizer
continuum, and the changed-end or level-five alternatives retain their
own analytic and physical identification duties. No foundational input,
observed three-family spectrum or gravitational dynamics is counted
derived by this continuation.

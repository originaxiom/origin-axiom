# Correlated physical state orbits and their actual charged zero modes

2026-11-16. Author hand proof under P-C3b. Independent review is pending.
No scientific module, CAS, collection or run occurred. Use the existing
balanced coherent E8 construction and the complete-domain orthogonal
reduction proved in the companion note.

## 1. The state axis and spin label transform together

The old quartic invariant determines the compensable flavour group of
the balanced pair as Pin2_x. Its axis is the Fk=i sigma_x quaternion
axis in the original flavour frame. Let 2O be the order-48 register
image. Its intersection D=2O intersect Pin2_x has order sixteen.
Thus the old three gauge classes of rotated pairs are the cosets
gD, or the three unoriented quaternion axes O_g(k).

The coherent holonomy and pair at g are

    K^g(h)=G(g^-1 rho(h)g), Phi^g=g Phi0.                   (1)

If g2=g1 h with h in D, gauge closure by G(h) maps the data at g2
to those at g1. Distinct axes have the distinct quartic invariant
already established in the source. This classifies the state within
its supplied flavour-rotation orbit.

For a nontrivial spin character p, choose U_p in {Fi,Fj,Fk} satisfying
U_p rho(h) U_p^-1=p(h)rho(h). Under e=(phi,g), the transported character
is p composed with phi^-1. Its quaternion axis is that of g U_p g^-1.
The same O_g therefore transports the state axis and spin-character axis.
Their equality or inequality is invariant.

There are consequently three types of spin/state orbits after the
stated gauge closings and before treating Wilson data:

| Seed spin | Correlation | Number of spin/state pairs |
|---|---|---:|
| odd, p=0 | no nonzero spin axis | 3 |
| nontrivial | spin axis equals state axis | 3 |
| nontrivial | spin axis differs from state axis | 6 |

The final line is the six ordered distinct-axis pairs. Its stabilizer
in 2O has order eight. The aligned nontrivial seed is p=(1,1), with
eta(a)=eta(b)=-1, because its axis is Fk.

The Wilson datum still transforms by W composed with phi^-1. The full
structured state orbit retains it. In the charged colour-singlet
coefficient of magnitude-one EM charge, this Wilson acts identically.
The operator and inclusion constructed below in that coefficient can
therefore descend independently of its Wilson label. Other coefficient
blocks keep their actual Wilson transport and full orbit.

## 2. Derive the pure-spin solutions from the physical rows

In the balanced raising-field coordinates use

    (q',r')=(q+r,q-r)/sqrt(2),
    qhat'=E_+/(2ell), rhat'=E_-/(2ell).

This unitary coordinate change carries epsilon and the determinant
slot, as in the source. Its determinant sign is retained in the
complex. It leaves the zero conditions and positive norm identity
used here unchanged.

Take j=3/2 on each triple. For lambda=a=0, the source mass rows give

    Dbar u=Dbar v=0,
    E_+ v-E_- u=0,
    E_+^dagger u+E_-^dagger v=0.                          (2)

The positive identity in the companion proof shows that the whole
algebraic solution space in (2) is spanned by

    w1=e_+ tensor |-j,j>,
    w2=e_- tensor |j,-j>.                                (3)

These have total H/2 weight zero. The local physical gauge connection
therefore drops out of their holomorphic coefficient equation.

Let alpha_R be the eigenvalue of the actual A_tilde=G(Fi) on the
highest vector, in the chosen complementary gauge coefficient.
The source compact spinor calculation gives on (3)

    T_Fi=alpha_R sigma_x, T_Fj=alpha_R sigma_x,
    T_Rtheta=diag(exp(4i theta),exp(-4i theta)).           (4)

Here T_U includes both flavour U and actual gauge G(U). At Fj use
Fj=R_(pi/2)Fi; the rotation in (4) is then the identity.

In the EM-charge-magnitude-one colour singlet, W=1 and alpha_R^2=1.
A normalized sigma_x eigenvector is

    xi_delta=(w1+delta w2)/sqrt(2), delta in {+1,-1}.

Its compact transition is eta_h alpha_R delta on each of a,b.
The two middle spin lines have zero cusp pole bound. A degree-zero
unitary compact line has a holomorphic section exactly when trivial.
Therefore their complete pure-spin kernel is

    one line if eta(a)=eta(b), with delta=eta(a)alpha_R;
    zero if eta(a) differs from eta(b).                   (5)

For the odd seed, delta=alpha_R. For the aligned seed, delta=-alpha_R.
The misaligned seeds have no such mode. This is the unique pure-spin
line when present. It is specified by actual equations and transitions.

## 3. Check the faithful highest-vector sign and its alternatives

The sign in (5) can also be evaluated from the source torus element.
Use the actual five-component logarithm

    x=(1/4,0,-1/4,-1/2,-3/4)

for A, and h4=exp(3pi i Q_em/4), with A_tilde=A h4.
For the +1 colour singlet the last-five highest weight is
(-1,-1,+1,+1,+1)/2. Its pairing with x is -7/8. A therefore has
phase exp(pi i/4), and h4 has phase exp(3pi i/4), giving alpha_+=-1.
For the -1 singlet the highest weight is
(-1,-1,-1,+1,+1)/2. Its pairing is -5/8; the phases are
exp(3pi i/4) and exp(-3pi i/4), giving alpha_-=+1.

The second continuous correction Zeta h4 reverses both signs. The
allowed spin line in (5) changes to the opposite delta. The character
and representation below keep their stated values for both choices.
All calculations use the full half-root weights and actual group path.

For a colour triplet coefficient, the additional order-three character
chi is nontrivial. Neither eta alpha_R delta can cancel it on the
whole core. Its pure-spin kernel is zero in this specified family.
The bare lift's order-eight highest character likewise retains its
old zero pure-spin count in every extending spin class.

## 4. Direct form and gaugino controls, with the whole kernel retained

For a pure form solution the physical rows give

    Dz a=0, [q,a]=[r,a]=0.

The algebraic coefficient is the joint highest vector, of H/2 weight
three. In its local unitary gauge frame the actual derivative equation
integrates to

    a=Omega^(-3/2) bar(h(z)) v_top.                       (6)

The holomorphic h has actual line S^5 L_top^-1. Near compact puncture
w=0, Omega is asymptotic to ell/(r log(1/r)). Its norm is proportional
to integral Omega^-3 |h|^2 dxdy. A pole of order n gives radial density
r^(4-2n) log(1/r)^3 dr. The allowed integer orders are n<=2.
The compact elliptic divisor has degree two, hence two independent
sections for every degree-zero unitary flat factor. Thus there are
exactly two pure form modes per stated half-root gauge component.

For a pure gaugino, the joint lowest vector has weight -3. Its equation
gives lambda=Omega^(3/2)bar(h). The norm has radial density
r^(-4)|h|^2 log(1/r)^(-5)dr. The holomorphic h must vanish to order
at least two at the puncture, in the degree-zero compact line S^-3
with its actual flat factor. That negative-degree divisor has no
nonzero section. The gaugino count is zero.

The orthogonal reduction shows that every zero mode lies in these
retained Dolbeault harmonic lines, with its original physical slot.
It therefore gives no extra mixed-slot zero population. The complete
half-root kernel is two form modes plus the pure-spin count (5).
This independently recovers the source's coherent and bare counts by
the new orthogonal route, as an author derivation awaiting review.

Both charged conjugates remain. In the coherent odd or aligned state
the full 128 kernel dimension is eighteen; in the misaligned state it
is sixteen. These are coefficient dimensions with the colour and
conjugate sectors retained. The corresponding net U3 indices keep
their zero values. Weak-current chirality has its separate duty.

## 5. Normalize the actual spin line

Normalize w1,w2 in the physical gauge/flavour metric. In compact
holomorphic frames the admitted solution is xi_delta with constant
holomorphic coefficient. Its kinetic coefficient is

    Z_spin(tau)=(1/g6^2) integral_(Sigma_tau) Omega_tau dxdy, (7)

with the fixed root-trace scale included in the chosen unit vectors.
Near the puncture this integral is bounded by an integral of
dr/log(1/r), so it converges. The orthonormal physical profile
Omega^-1/2 xi_delta is bounded and decays there. Complete cutoffs
put this zero mode in the actual graph domain. Its bounded profile
and finite norm also give the source nonlinear product integrability.

The two form modes in (6) have physical profile a/Omega. At their
largest allowed pole its magnitude is of order r^(1/2)log(1/r)^(5/2).
It too is bounded and decays. Their actual graph and nonlinear
variation classes are retained.

Under the marked isometry z'=z/(C tau+D), (7) satisfies

    Z_spin(gamma tau)=Z_spin(tau)/|C tau+D|.

The raw spin coefficient obtains j_e, with j_e^2=C tau+D, so canonical
normalization gives j_e/|j_e|. The finite gauge/flavour matrices are
unitary and preserve the same norm in each state. Thus the inclusion
below has its actual derived metric, without a separately chosen
family Gram. The modulus and parent metric remain supplied data.

## 6. What is needed for the next representation test

The odd and aligned state orbits each have one unique pure-spin line
per state. Both lines and the orthogonal form complement are preserved
by the physical word transport, which is block diagonal in the field
slots. The companion proof computes the stabilizer character and the
full induced rank-three mode bundle with its scalar line.

The full-state Wilson labels, other gauge coefficients, conjugates and
neutral continuum remain part of the theory. Composing distinct
background sectors into simultaneous local families requires a
physical law beyond this invariant inclusion.

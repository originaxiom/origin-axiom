# A register action on the physical parent: full covariance and a state test

November 3, 2026. UNREVIEWED author analytical result in the supplied curved
E8 parent. No scientific import, numerical evaluation, test collection or
execution. This is a partial physical-sector map and a discriminator for
a proposed stronger join, not a foundational derivation of the parent,
spin/flavour assignment, boundary law, SM3 or gravity.

## 1. Reuse and keep the two different questions separate

The source [curved action](../weave_curved_action_2026_10_08/PROOF.md)
and [parallel phase](../weave_sm_parallel_2026_10_08/PROOF.md) already have
an exact constant SU2 flavour symmetry on Phi=(Q,R). The [coherent
register](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md) already gives the
homomorphism E -> 2O subset SU2, e=(phi,g) -> g. Neither is a new result.
The [full local coefficient](FULL_DOUBLET_QUARTET_AND_NORMALIZATION.md)
retains 2+4, and its [actual holonomy](COEFFICIENT_METRIC_CONSTRAINTS_AND_PHYSICAL_PRICES.md)
does not preserve that splitting. No rank-two truncation is made here.
The [common matter register](MATTER_AND_BOUNDARY_COMMON_REGISTER.md) has
its distinct two triplets; they are not the two physical fields Q,R.

There are TWO joining questions:

A. Pull the existing constant SU2 flavour symmetry back along E -> SU2.
   This is a genuine action on the given physical parent and its whole
   state family. It does not change its trivial flavour bundle F0.
B. Identify the noncentral quaternion LOCAL-SYSTEM holonomy of the register
   with physical flavour holonomy. This changes the combined bundle unless
   an actual coupled spin/gauge map establishes otherwise. It is a separate,
   unearned candidate identification, not a consequence of A.

The distinction prevents confusing a symmetry moving states with parallel
transport fixing one state. In particular a finite image acting on these
fields does not replace the faithful based register and measuring sector.

Read-only prior-work locators used already_banked on 'quaternion flavour
balanced Gram' and targeted reports searches. Broad incidental settled hits
are not a novelty verdict; no exhaustive absence or literature-priority
claim is made. This note derives explicit consequences of cited sources.

## 2. The complete physical action and mass operator transport

For U in SU2 put Phi'=U Phi, with connection A and vector V unchanged.
Both physical spin fields have the same source kinetic density Omega.
Thus their entire kinetic sum and the source moment sum are preserved.
Covariant holomorphy transforms as Dbar Phi'=U Dbar Phi, while

    [Q',R']=det(U)[Q,R]=[Q,R].

The antisymmetric W and its VARIATIONAL surface pairing
kappa(Q delta R-R delta Q) are preserved because U^T epsilon U=epsilon.
When W is rewritten as a nonsymmetric bulk term plus the integration-by-
parts primitive proportional to kappa(QR), those two pieces must travel
together: that primitive is NOT separately invariant under general SU2.
The full derivative/cubic, quartic
and moment terms therefore travel together. This is not a zero-mode
submatrix or equality restricted to the vacuum equations.

For the [actual physical mass operator](../weave_physical_mass_2026_10_08/PROOF.md)
with left slots (lambda,a,u,v), define

    T_in=diag(1_lambda,1_a,U),
    T_out=diag(1_lambda,1_a,bar(U)).

In the source notation p=(p1,p2) transforms by U; its spin Hessian rows
are epsilon p/Omega and epsilon U=bar(U) epsilon. The conjugate-background
gaugino terms also transform by bar(U). The contraction in D0-dagger is
unchanged, and t=[Q,v]-[R,u] is preserved by det(U)=1. Consequently

    M_(U Phi) T_in = T_out M_Phi.                         (1)

This retains every gauge coefficient, both Weyl spin slots, connection
fermion and gaugino, including their transpose couplings. Both maps are
unitary in the actual unequal source slot densities. They carry smooth
compact-support cores and their complete graph closures into each other;
the nonlinear residual and Green-form conditions travel as well. No
new end projector, mass coefficient or omitted companion is needed.

Composition of T_in follows multiplication in SU2, so pullback by e->g_e
is coherent on every word. The result is an explicit physical-sector
representation of E. It is not faithful: epsilon and J_c both act by -I
on the spin doublet, while epsilon J_c acts trivially there but retains a
nontrivial based automorphism. The rest of the register must remain.
The geometric phi action on the full universal family, its metrics and
other physical/registering modules is not derived by (1).

## 3. Necessary Gram law for the stronger holonomy identification

Only for question B assume that the physical flavour holonomies contain
Fi=diag(i,-i), Fj=[[0,1],[-1,0]], and that Phi is parallel for the actual
combined unitary spin/gauge/flavour connection. Allow arbitrary compact
gauge and unitary spin compensators, not just a chosen gauge matrix.
Define the Hermitian positive flavour density

    D_ab=kappa(Phi_b-dagger Phi_a).

Unitary spin/gauge factors cancel in D. A flavour change gives
D' = F D F-dagger. Parallel transport around a loop returns the same
parallel density, hence [D,Fi]=[D,Fj]=0. For

    D=[[x,z],[bar(z),y]],

the first equation forces z=0 and the second forces x=y. Therefore

    D=N I2, N>=0.                                        (2)

A nonzero parallel state has N>0: its two fields must be orthogonal with
equal norm, and its field map has rank two. This is an explicit 2-by-2
calculation, not a count of representation dimensions. One generator
alone leaves unequal diagonal entries possible. Nonparallel covariant
families need not obey a fixed-density condition at one point.

The old proportional stationary orbit (Q,R)=(a Q0,b Q0) has rank-one
D for Q0!=0, so cannot descend as a nonzero PARALLEL state under these
new irreducible flavour holonomies. It remains a valid state family of
the original F0 parent and under the constant action in section2.
There is no contradiction, no exclusion of nonparallel states and no
programme-wide no-go.

On the [existing EW branch](EXACT_ORDER_THREE_ELECTROWEAK_BRANCH.md),

    qhat=a E/(2 ell), rhat=b G/(2 ell),
    |a|^2+|b|^2=1, kappa(E-dagger E)=kappa(G-dagger G)=20,
    kappa(E-dagger G)=0,

(2) forces |a|=|b|=1/sqrt(2), with N=5/(2 ell^2). This removes one
amplitude ratio CONDITIONALLY on the new holonomy-and-parallel premises.
It does not prove that the required compensators exist, satisfy all
relations, preserve the order-three Wilson state or yield the same end.
No phase, orientation, scale or foundational input is thereby paid.

## 4. Equal Gram does not imply equal gauge orbit: a quartic discriminator

Now return to question A, on the ORIGINAL F0 parent and its already
admitted stationary EW branch. This step needs no new flavour holonomy.
Choose the balanced reference state

    Phi0=n(E,G), n=1/(2 sqrt(2) ell).

Reuse the [actual commuting triples](ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md):
Eplus=(E+G)/2, Eminus=(E-G)/2. Their compact adjoints commute between
factors, Hplus+Hminus=H, and

    kappa(Eplus-dagger Eplus)=kappa(Eminus-dagger Eminus)=10,
    kappa(Hplus^2)=kappa(Hminus^2)=20,
    kappa(Hplus Hminus)=0.

For a fixed external flavour reference z=(z1,z2), define the local
compact-gauge- and spin-frame-invariant composite

    X_z=z1 qhat+z2 rhat,
    C_Phi(z)=kappa([X_z,X_z-dagger]^2).                    (3)

It is a possible relational field observable; no new potential term or
probe dynamics is asserted. In the reference state,

    X_z=n[(z1+z2)Eplus+(z1-z2)Eminus],
    C_0(z)=20 n^4 (|z1+z2|^4+|z1-z2|^4).

Put r2=|z1|^2+|z2|^2 and

    sx=2 Re(z1 bar(z2)), sy=2 Im(bar(z1) z2),
    sz=|z1|^2-|z2|^2, C=5/(8 ell^4).

Then

    C_0(z)=C[(r2)^2+sx^2].                               (4)

Here kappa is the full E8 invariant form in the source normalization;
its restriction to the actual D5 is (1/2)Tr_10. Thus (3) is invariant
under the entire compact E8 gauge group, including transformations that
do not preserve this D5 subalgebra.

Use the ACTUAL register matrices

    gL=(I+Fi)/sqrt(2)=diag(exp(i pi/4),exp(-i pi/4)),
    gR=(I-Fj)/sqrt(2).

Set PhiL=gL Phi0, PhiR=gR Phi0. The SU2 identities in section2 ensure
that both are exact stationary backgrounds of the same action, with the
same connection, bundles, positive kinetic metrics and complete end law.
Their densities are still N I2 and their total norm and moment are
unchanged. Direct substitution in (3) instead gives

    C_L(z)=C[(r2)^2+sy^2],
    C_R(z)=C[(r2)^2+sz^2].                               (5)

For unit reference probes z_x=(1,1)/sqrt(2), z_y=(1,i)/sqrt(2),
z_z=(1,0), the three-by-three readout is exactly

                    z_x  z_y  z_z
    Phi0             2    1    1
    PhiL        C *  1    2    1
    PhiR             1    1    2 .                       (6)

The three configurations are therefore pairwise inequivalent under
compact E8 gauge transformations, even though all quadratic Grams agree.
This uses a full E8 trace invariant, not a Jordan comparison made only
inside a chosen D5 representation. At least these three gauge classes
exist in this symmetry orbit. A complete orbit/stabilizer census and
additional state degeneracies are not established by (6).

They are related by a global flavour symmetry; they are not three
independent theories or three generations. A fixed flavour reference
distinguishes them. If the reference is transported too, z'=U^(-T)z,
then X_(U Phi)(z')=X_Phi(z) and the readout agrees. This makes the role
of the registering/measuring data explicit without asserting an observer
or qualia mechanism. Turning global flavour symmetry into gauge
redundancy would change the supplied physical problem.

## 5. What this settles about the first joining step

There is a complete classical FIELD/ACTION/OPERATOR/DOMAIN action of
the specified register quotient on the old parent, with no new field or
coupling. It maps states rather than selecting one. A single fixed
gauge-orbit background cannot stand for this entire explicit orbit:
(6) supplies a rejecting control. The generated based register and
geometric family still need their full physical maps; (1) is only one
sector's representation and does not earn that identification from genesis.

If a proposed physical map instead uses Q8 as actual flavour holonomy,
it owes the stronger global joining duties. Equal-amplitude (2) is one
derived necessary condition. It is not permission to insert that holonomy,
announce a selected EW state, reuse the old gapped cusp theorem, or count
old zero modes on a changed combined bundle. The Gram and quartic tests
are checks to apply before changing the end or claiming input reduction.

Before: an unearned suggestion to identify quaternion and flavour
representations. After: one explicit coherent full-parent action, an
exact mass-map transport, a necessary holonomy-state law, and a quartic
counterexample to identifying all equal-Gram states as gauge copies.
The parent, surface/embedding, physical role of this action and global
register/end identification remain supplied. No foundational input is
marked paid, no numerical physical parameter is predicted and no change
to chirality is claimed. The old source review does not cover this note.

The accompanying prospective five-check design is a separate package.
It will bind the finite comparators to the actual D5 matrices and full
fermion slots, while retaining the analytical global hypotheses. No
scientific control was executed to obtain this authored proof checkpoint.

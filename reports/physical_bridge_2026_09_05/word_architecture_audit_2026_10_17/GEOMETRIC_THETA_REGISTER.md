# Theta fields on the registered word architecture

October 18, 2026. Analytical successor to the
[common coefficient action](MATTER_AND_BOUNDARY_COMMON_REGISTER.md).
The existing meromorphic pairing field has a coherent transformation
law under the specified four-wording lifted group, when its fibre
coordinate and metaplectic line are retained. This is more than an
arbitrary free register appended to a function of the modulus: it uses
the paper's actual theta field. It is not a derivation of the operation
set, a complete faithful geometric realization, a physical coupling or
an observer. No scientific producer is executed by this argument.

## Existing inputs and the comparison being made

The source pin is main `2e5716bd9bea013d69f3cd733f083b61a6f59dbd`,
refreshed October 18. B1651's complete `where_a_higgs_couples.py` and
B1654's complete `the_norm_of_the_boundary_class.py` were read directly.
B1651 U2 already records the period signs; U4 checks projective overlaps
at the puncture and half-periods, so it does not determine an absolute
scalar multiplier. At the puncture its `triplet` returns the numerator
of the residue, omitting the derivative denominator. B1654 retains that
denominator and uses periods 1 and tau. The paper's Theorem 9 already
identifies the ruled cohomology multiplier with a twisted theta
multiplier. Neither the theta correspondence nor the period signs are
new findings here.

Use the preceding notes' conditional group

    E={(phi,g): phi in H=Aut+(F2), g in SU(2), rho phi=Ad_g rho},
    rho(a)=i, rho(b)=j, J_h=(I_h,rho(h)), epsilon=(id,-1).

The four wordings and inverses, the quaternion coefficient system, and
the surface/field interpretation remain inputs. Write l and r for the
chosen lifts of L and R, and mu=mu_+ for the proved character

    mu(l)=zeta, mu(r)=zeta^-1, mu(J_h)=1, zeta=exp(pi i/4).

In this note axis coordinates are (i,j,k), a permutation of the
companion note's (j,i,k). Let O_g=Ad_g in these coordinates and put

    B=Ad_j=diag(-1,1,-1), Q_e=B O_g B^-1,
    U_e=mu(e) Q_e.

Thus U is the already constructed T_+ action in a fixed new frame,
not a new choice of phases on individual words.

## The metaplectic line follows from the same lifted group

The natural inner subgroup J(F2) is normal in E, since

    e J_h e^-1=J_(phi(h)).

Let Omega=<l,r>. Its projection to G=<L,R> is an isomorphism with
B3: the generator intertwiners obey the braid relation, so they define
a homomorphism on that actual based group. Set

    Delta=l r^-1 l, c=a b^-1 a^-1 b.

The preceding coherent-lift proof gives

    Delta^4=(I_c,+1)=epsilon J_c, rho(c)=-1,
    G intersect Inn(F2)=<I_c>.

Consequently

    Omega intersect J(F2)=<Delta^8>.

Indeed a common element projects to I_c^n; its Omega lift has g=1,
whereas J_(c^n) has g=(-1)^n, so precisely even n occur. The subgroups
Omega and J(F2) generate E: they project onto H and contain epsilon
through Delta^4 J_c^-1. It follows that

    E/J(F2) = B3/<Delta^8> = Mp2(Z).                 (1)

This provides a metaplectic projection p from E, not a separately
assigned square root for every word. In the standard realization of
Mp2(Z), let j_e(tau) be its holomorphic automorphy factor. If the
homology matrix is gamma=[[A,B0],[C,D]], then

    j_e(tau)^2=C tau+D,
    j_(ef)(tau)=j_e(gamma_f tau) j_f(tau).

For s=r l^-1 r=Delta^-1, choose the standard lifts

    j_l=1, j_s=sqrt(tau), j_r=sqrt(tau+1), j_(J_h)=1.

The displayed roots are principal on the upper half-plane; roots for
composites are obtained by the product law, not reset independently.
In particular j_epsilon=-1, j_(J_c)=1 and j_(Delta^4)=-1.

## A fibre action retaining the period register

Every phi in H can be written I_h psi with psi in G. Define
b(phi)=(m,n)^T to be the exponent sums of h. This is well-defined:
two decompositions differ by a power of c, whose exponent sums vanish.
With gamma_phi the homology matrix,

    b(phi chi)=b(phi)+gamma_phi b(chi).              (2)

This follows by moving I_k through psi using
psi I_k psi^-1=I_(psi(k)). Thus H has the specified quotient action
through Z^2 semidirect SL(2,Z).

On X={(tau,z): Im tau>0, z not in Z+tau Z}, define

    e:(tau,z) -> (tau',z'),
    tau'=gamma tau,
    z'=z/(C tau+D)+m-n tau',                       (3)

where (m,n)=b(phi). The minus sign in m-n tau is essential with these
homology conventions. The identity

    (m-n tau)/(C tau+D)
      =(A m+B0 n)-(C m+D n)(gamma tau)

and (2) verify composition exactly. In particular

    l:     (tau,z) -> (tau+1,z),
    r:     (tau,z) -> (tau/(tau+1),z/(tau+1)),
    J_a:   (tau,z) -> (tau,z+1),
    J_b:   (tau,z) -> (tau,z-tau),
    lbar:  (tau,z) -> (tau+1,z-1),
    rbar:  (tau,z) -> (tau/(tau+1),(z-tau)/(tau+1)).

Here lbar=J_a^-1 l and rbar=J_b r. The inner operations translate a
lifted coordinate by a period; they do not move its point on the
quotient torus. X is the lattice cover of the punctured family, not
its simply connected cover and not a faithful E space. In particular
commutators of inner operations are invisible to (3). This limited
quotient will be sufficient for the pairing field below; it is not
the whole architecture or a derivation of M1,2 as physical spacetime.

## Exact transformation of the existing pairing field

Use period-one theta functions theta_r(z,tau)=vartheta_r(pi z|tau),
and let d(tau)=partial_z theta_1(0,tau). Define

    R=(-theta_2(0)^2,-theta_4(0)^2,i theta_3(0)^2)/d,
    S_r(z,tau)=theta_r(z) d/[theta_r(0) theta_1(z)],
    v=(R_i S_2,R_j S_4,R_k S_3).

Then S_r~1/z and R is the residue of v dz at zero. These are exactly
the B1651/B1654 fields after the explicit pi rescaling, not arbitrary
functions constructed to satisfy a desired representation.

The classical theta laws are in
[DLMF 20.7.26--33](https://dlmf.nist.gov/20.7#viii) and the period laws
in [DLMF 20.2.6--9](https://dlmf.nist.gov/20.2#ii).
Substitution gives, with P_ij swapping the first two axes,

    v(z,tau+1)=zeta (v_i,v_k,-v_j),
    R(tau+1)=zeta (R_i,R_k,-R_j),
    v(z/tau,-1/tau)=i sqrt(-i tau) P_ij v(z,tau),
    R(-1/tau)=(-i tau)^(-1/2) P_ij R(tau).          (4)

For the inversion law, theta_1 transforms with the additional factor
-i, while the even theta functions have no such factor. Differentiating
at zero gives d(-1/tau)=(-i tau)^(3/2) d(tau). This explains why
the residue and the pointwise coefficient have different weights.
It also avoids mistaking B1651's puncture numerator for the residue.

The geometric matrices satisfy

    Q_l=O_(g_l)^-1, Q_r=O_(g_r), Q_s=-P_ij,
    mu(s)=zeta^-3.

Thus (4) is precisely v(e x)=j_e U_e v(x) on l and s, and
R(gamma tau)=j_e^-1 U_e R(tau) for e in Omega. The phase identity
-zeta^-3 sqrt(tau)=i sqrt(-i tau) fixes the sign in the s comparison.
The matrices have t-eigenvalue turns (1,3,7)/8, the paper's stated
inverse-pullback hand. This matches the concrete meromorphic field,
without re-establishing the Hodge or physical-matter interpretation.

The remaining generators follow from the period laws:

    v(z+m-n tau,tau)
      =diag((-1)^n,(-1)^m,(-1)^(m+n)) v(z,tau)
      =Ad_(rho(h)) v(z,tau)=U_(J_h) v(z,tau).      (5)

B commutes with these diagonal matrices. Equations (1)--(5), with
the cocycle law for j, prove the full conditional identity

    v(e x)=j_e(tau) U_e v(x) for every e in E.      (6)

For a vertical one-form omega=v dz, dz'=j_e^-2 dz at fixed tau,
so its coefficient transport has j_e^-1 U_e instead. Residues at
transported lifts of the puncture have that same law. Writing only
R(tau) at the distinguished lift zero forgets which puncture lift was
transported; the Omega formula for that function must not be applied
to all natural inner operations with zero held fixed.

Two central checks are informative. Both epsilon and Delta^4 act
trivially on X; each has j=-1 and U=-I, so the product in (6) is +I.
The natural J_c also fixes X but has j=1 and U=I. These are distinct
registered acts whose effects cancel on this particular field.
For e=Delta^2 J_c^-1, g=1, mu=-i, j=-i and gamma=-I. It sends z
to -z and v to -v, whereas its residue factor j^-1 mu equals +1.
Suppressing the metaplectic line would misread this example.

## What is retained and what is still unpaid

The earlier tau-only obstruction remains correct for a function required
to transform by U with trivial inner action on its argument. The actual
pairing field is instead a section with a fibre argument and an
automorphy line. It is a nonzero, explicit realization of the latter
possibility, not a counterexample to the former theorem's hypotheses.

The same correction has a strict limit. Period translations preserve
the point and the degree-zero flat-line class on the torus. Their
transition signs cannot connect eighteen distinct hypercharge lines
or choose a vacuum. No natural inner commutator becomes observable
merely because the notation retains it. The unpaired doublet's
puncture monodromy, the full local boundary module and other fields
need their own transports; (6) is a pairing-level result.

For a check on the supplied fibre tensor, write

    Y(a,v)=a v^T+v a^T-(a.v)I.

If a(e x)=h_e(x) Q_e a(x), (6) gives

    Y(e x)=h_e(x) j_e mu(e) Q_e Y(x) Q_e^T.

If two matter columns carry j_e^u U_e and j_e^w U_e and a transpose
bilinear is to be invariant, compatibility requires

    h_e=j_e^(-(u+w+1)) mu(e)^-3.                  (7)

For the residue tensor Y(a,R), replace that power of j by 1-u-w.
These are conditional bookkeeping requirements, not derived Higgs
fields, physical Yukawa assignments or kinetic normalizations. The
distinction between a function, a one-form, and a residue matters.
The source's different Higgs types cannot be identified by name alone.

The genuine addition is a composition-compatible geometric realization
of the already supplied pairing field on the specified lifted word
architecture. The allowed alphabet, coefficient system, dynamical
joining, boundary law and observer/qualia questions remain separate.
This argument does not pay a complete physical-input row.

## Verification scope

This checkpoint is an analytical proof awaiting separate non-authoring
review. It does not modify the frozen v2/v3 specifications or authorize
their execution. A sealed successor should check exact central relations,
the minus sign in the affine action, both square-root branches through
composition, the full multipliers rather than overlaps, generic fibre
points, transported puncture residues and an intentionally forgotten
automorphy-line control. Existing numerical results are not recertified.

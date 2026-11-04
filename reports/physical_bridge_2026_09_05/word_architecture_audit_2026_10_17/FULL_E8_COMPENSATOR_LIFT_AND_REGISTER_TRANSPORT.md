# The compensator lift on the full E8 parent

November 3, 2026. **UNREVIEWED author hand derivation.** No scientific module, CAS, enumeration, test collection or scientific execution. This follows the owner-approved `TRANSPORT_AND_END_WORK_ORDER_2026_11_03.md`.

Scope is the actual compact D5 embedding, two-triple stationary state and full E8 parent already specified by this lane. An allowed coupled bundle and its transport are constructed conditionally. Their foundational identification, geometric all-word lift, physical spectrum and selection remain duties.

## 1. Distinguish the maps before joining them

The [coherent register](COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md) has

    F2=<a,b>, rho(a)=Fi, rho(b)=Fj,
    E={(phi,g): rho(phi(gamma))=g rho(gamma) g^-1}.

The quaternion matrices are `Fi=diag(i,-i)`, `Fj=[[0,1],[-1,0]]`, `Fk=Fi Fj`. Natural inner lifts are `J_h=(I_h,rho(h))`. The map `h -> J_h` retains the free based group. Its image is not Q8 even though its second component factors through Q8. The [faithful tower](FAITHFUL_LIFTED_REGISTER_TOWER.md) already proves that distinction.

The register's word moves L,R are automorphisms. They are not the surface generators a,b. Their lifts `gL=(1+Fi)/sqrt(2)` and `gR=(1-Fj)/sqrt(2)` can act on the existing physical flavour symmetry without becoming a new choice of surface holonomies. Identifying the actual physical surface group with the retained F2 is a separate premise, made explicitly for the candidate below.

AGY's Theorem 14 at `bbbc30a7e` supplies compensator matrices for Fi,Fj on the ten-dimensional D5 carrier. The finite orbit census is not recomputed here. This note reads the actual matrices on the full root representation before using them as physical transitions.

## 2. Existing source matrices and the full root decomposition

Reuse [the two-triple proof](ELECTROWEAK_TWO_TRIPLE_PHYSICAL_KERNEL.md). In its original ten-dimensional frame,

    H=diag(H5,-H5), H5=diag(-4,-2,0,2,4),
    E=E_+ + E_-, G=E_+ - E_-, H=H_+ + H_-,
    N=diag(I5,-I5).

The two compact principal triples commute. N interchanges them under conjugation. The positive form and compact adjoints remain the source's. The balanced background is

    Phi0=(qhat,rhat)=(E,G)/(2 sqrt(2) ell).

The original root construction retains

    248=(45,1)+(1,15)+(10,6)+(16,4)+(bar16,bar4).

Its integer roots and Cartans give 120 dimensions, including the vector product. Its half-integer roots give the remaining 128. These are actual root subspaces, not a deduction from the number 248 alone.

## 3. A literal compact E8 lift of the first compensator

Write torus coordinates in the order of the five source vector weights. On the ten-dimensional carrier set

    A_vec=(-i N) exp(-i pi H/4),
    D_vec=exp[-i pi(H_+-H_-)/4],
    B_vec=D_vec A_vec.

These are the inverse compensators in AGY's executable convention. The vector eigenvalues of A_vec on the first five coordinates are `exp(2 pi i x_j)` with

    x=(1/4,0,-1/4,-1/2,-3/4).

The other five eigenvalues are their inverses. Use the corresponding D5 torus element of compact E8 to DEFINE A, rather than lift its vector eigenvalues independently at each step. Let

    D=exp[-i pi(H_+-H_-)/4], B=D A

in that same compact E8 subgroup. The associated simply connected compact Spin10 subgroup is faithful here because its centre is detected on the vector and spinor products. No quotient acting only on the 45 is substituted for it.

To check the central data by hand, put

    C=exp[2 pi i (1/2,1/2,1/2,1/2,1/2)],
    Zeta=C^2, P=exp(-i pi H/2).

On each D5 root, C is trivial. On the vector ten it is -I. On a D5 half-weight `(epsilon_1,...,epsilon_5)/2`, it is `exp[i pi sum(epsilon_j)/2]`, hence +i or -i according to spinor chirality. Thus C has order four and Zeta has order two in the full E8 representation. Zeta acts trivially on the 120 integer-root/Cartan dimensions and by -1 on the 128 half-root dimensions.

The source torus logarithm gives

    2x - (-H5/4)=(-1/2,-1/2,-1/2,-1/2,-1/2),

so the exact full-group identity is

    A^2=C^-1 P, A^4=Zeta, A^8=1.                       (1)

Equivalently, `4x=(1,0,-1,-2,-3)` has odd integer sum. All integer roots pair integrally with it, while all E8 half-roots pair half-integrally. This is a direct witness to the nontrivial fourth power on the omitted spinor products. Choosing the other Spin10 lift multiplies A by Zeta and does not change A^4.

## 4. The second compensator and the commutator

Conjugation by A interchanges H_+ and H_-, hence

    A D A^-1=D^-1.                                     (2)

The total H has two principal spin-two vector blocks. Therefore `exp(i pi H)=1` on the full root representation and `P^2=1`. A single H_- has orthogonal Cartan rotation magnitudes 4 and 2 on its five-space and zero on the other. Its `exp(i pi H_-)` has torus logarithm `(2,1,0,0,0)` after a compact frame change. The sum is odd, so it equals Zeta in E8. Consequently

    D^2=exp[-i pi(H_+-H_-)/2]=Zeta P,
    D^4=1.                                             (3)

Using B=DA and (2),

    B^2=A^2=C^-1 P,
    (AB)^2=P,
    [A,B]=D^-2=Zeta P.                                 (4)

Every identity is in the full compact E8 group. In the vector ten, Zeta is invisible, and C is -I. Equations (1) and (4) reduce to

    A_vec^2=B_vec^2=-P_vec,
    (A_vec B_vec)^2=P_vec,
    [A_vec,B_vec]=P_vec.

Passing to the D5 adjoint also removes C. That quotient gives the quaternion relations. It cannot be used as the action on all 248 coefficients.

### The finite group label needs correction

The source and independent-seat reports label the vector compensator group `Q8 x {+-I10}`. Their own displayed squares disagree with that label. In Q8 x C2 every element of order four has the same square. Here A_vec and A_vec B_vec have distinct nonidentity squares, -P_vec and P_vec.

The exact presentation is clearer. Equations (1)–(3) give normal forms

    D^j A^i, 0<=j<4, 0<=i<8,
    (j,i)(l,k)=(j+(-1)^i l mod4, i+k mod8).             (5)

The intersection of <D> and <A> is trivial. In the vector representation, D^2=P_vec differs from A_vec^2=-P_vec and from I, so an intersection can only come from the spin centre. But A^4=Zeta while D^2=Zeta P differs from Zeta. Thus the full group has 32 elements, a semidirect product C4 by C8 with inversion action. Its vector quotient has 16 elements, C4 semidirect C4. Its D5-adjoint quotient has 8 elements and is Q8.

This count is an authored deduction from the displayed matrices and relations, not an executed census. The 32-element presentation and its faithful full-root action require independent checking before banking.

## 5. Free-group transport needs no false finite quotient

Define

    K:F2 -> E8, K(a)=A, K(b)=B.

The source group F2 is free, so these two assignments define a representation. No Q8 relation has been imposed on its full image. Directly on the source pair,

    Ad_A(E,G)=(-i E,+i G),
    Ad_D(E,G)=(-i G,-i E),
    Ad_B(E,G)=(-G,+E).

It follows that

    rho(gamma) Ad_(K(gamma)) Phi0=Phi0                  (6)

for both generators and hence every word. The gauge and flavour factors commute as transformations of the complete field space. The three source backgrounds used by the old quartic discriminator are still different gauge classes at a fixed flavour reference. Equation (6) concerns the based quaternion subgroup and its chosen compensators, not compensation of every 2O move on one fixed background.

The word a^4 has rho(a^4)=1 but K(a^4)=Zeta. This is allowed for the full based register. The natural inner lift J_(a^4) retains a nonidentity based operation. Calling its finite quotient image trivial does not make the full physical transition trivial. Conversely, this construction does not prove that this particular physical sensitivity is forced by genesis.

There is a homomorphism from the group (5) to Q8 given by A->Fi and D->Fk. Its kernel is <C>, of order four. It records the precise information lost by using only the flavour quaternion image.

## 6. Algebraic transport across all word moves

For an admitted pair of holonomies K and a constant pair Phi satisfying (6), define

    e=(phi,g): (K,Phi) -> (K composed with phi^-1, g Phi). (7)

The register's defining identity gives

    rho(gamma) Ad_[K(phi^-1 gamma)] (g Phi)=g Phi.

Thus (7) preserves the joint invariance condition. It is a left action. Applying f=(psi,h) and then e gives `K composed with psi^-1 composed with phi^-1`, which is `K composed with (phi psi)^-1`, and the field factor gh. This proves covariance for all words at the algebraic holonomy/state level.

For a natural inner lift J_h, this action is simultaneous gauge conjugation by K(h)^-1 on K and Phi, provided the relevant registering/reference data are transported as well. Those data are not erased by that gauge statement.

The finite state orbit therefore need not be fixed pointwise by every word operation. Different marked holonomies and stationary pairs can form one covariant family. This avoids demanding a compensator for every 2O element while holding all other data fixed.

Equation (7) is not yet a chosen coherent diffeomorphism/spin action on the physical universal family. Geometry, spin lifts, marking maps and the faithful registering modules must be included in that joint. The physical bundle construction below works on each explicitly specified marked surface, and ordinary pullback transports a whole structured background. An E-equivariant choice of those geometric pullbacks is a remaining duty.

## 7. Lift choices and reduction accounting

The two vector compensators each have two Spin10 lifts. Replacing A or B by Zeta times itself preserves (6), all local vacuum residuals and their commutator. It changes transport on the 128 half-root coefficients along that core cycle. These four possibilities must be retained until a further map identifies or selects them. They cannot be absorbed by a spin/flavour sign change on every physical slot, because the scalar/form Weyl fields in those same gauge sectors also detect Zeta.

The parent, surface/spin identification, physical flavour holonomy, balanced state ansatz, lift prescription and old Wilson data remain priced assumptions. The new result supplies an explicit permitted full-field transport and exact relations among its centres. It does not certify an input payment, three generations, an observer mechanism or a physical chirality result.

The [stationary/end successor](COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md) uses (1)–(6) to check actual gluing and the resulting domain. It retains the extra sign rather than transplanting the old cusp spectrum.

November 4 constructive successor. An existing electromagnetic circle in the complementary A3 supplies a correction to the bare D5 lift. Its [coherence proof](PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md) gives an exact Pin2 compensator homomorphism on the full E8 parent, with a conditionally fixed core phase and unchanged quaternion peripheral commutator. This keeps a positive quotient realization alongside the larger based lift described here.

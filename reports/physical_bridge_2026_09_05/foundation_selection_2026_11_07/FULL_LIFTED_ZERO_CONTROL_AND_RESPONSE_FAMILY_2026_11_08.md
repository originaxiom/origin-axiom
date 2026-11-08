# A full lifted zero-response control and the covariant nonzero family

2026-11-08. Author hand proof, **UNREVIEWED**. No scientific import,
collection or execution. Reuses the existing coherent lift and faithful
register constructions; no new canonical GENESIS or physical theory.

## Outcome

The full supplied word/lift architecture admits a faithful unitary linear
register with zero affine translation. Thus retaining the lift and every
based history still does not alone force a nonzero affine doublet class.
Conversely, the complete family of affine doublet responses has a
canonical coherent transport. There is no need to freeze one class in
order to construct that family. These are compatible kinematic positives.

The local D4 result is in the companion
`AFFINE_DOUBLET_KERNEL_D4_AND_PARITY_2026_11_08.md`. Neither construction
selects a physical state, action, measure or boundary law.

## 1. The full group and a faithful zero-response control

Keep F=F(a,b), rho:F->Q8 subset SU(2), the supplied enlarged operation
group Gamma and its existing lift

    E={(phi,g): rho composed with phi = Ad_g composed with rho}.

Products are (phi,g)(psi,k)=(phi psi,g k). Its central kernel is
{1,epsilon}, epsilon=(id,-I). The earlier coherent-lift proof and
faithful-tower proof are reused, not independently reclassified here.
The enlargement with inverse operations remains a premise.

Form the semidirect product S=F rtimes E using the projected word action:

    (h,e)(k,f)=(h phi_e(k),e f).

On l2(F), define lambda_h delta_w=delta_(h w) and
U_phi delta_w=delta_(phi(w)). These are unitary and satisfy
U_phi lambda_k U_phi^-1=lambda_(phi(k)). On

    W=l2(F) direct_sum V_rho

define

    Pi(h,(phi,g))=(lambda_h U_phi) direct_sum (rho(h)g).

The first block respects the semidirect law by the preceding covariance
identity; the second does so because g rho(k) g^-1=rho(phi(k)). Hence
Pi is an exact unitary representation of S.

It is faithful. If its first block is the identity, applying it to
delta_1 gives h=1. Applying the remaining U_phi to every delta_w gives
phi=id. The only remaining possibilities for e are (id,+/-I), and
the second block distinguishes them. Therefore the kernel is trivial.

The affine action x->Pi(s)x has translation response z(s)=0. It retains
the supplied local Q8 block, both lift signs, and the entire based word
and operation data. In particular epsilon acts as I direct_sum (-I);
its distinction is not lost in the first block's kernel. This strengthens
the preceding F-only zero-response control to the actual lifted joint
architecture. It does not derive a physical Hilbert space, tensor law,
observer, Born rule or an infinite-dimensional physical sector.

This is an explicit countercontrol to the implication 'a full coherent
register, including the lift, therefore forces a nonzero affine class'.
It is not formal independence of every informal PF formulation or a
comparison satisfying a separately imposed finite-dimensional objective.
Faithfulness here concerns the elements of the stated group S. It does
not claim to retain the chronological list of every unreduced act: a
path containing an operation and its inverse has the same net group
element as the empty path. Keeping such process records or an emergent
clock requires the corresponding history structure as well.

## 2. What an individually fixed response would require

For a supplied doublet cocycle, the existing right action is

    D_e[z]=[g_e^-1 z composed with phi_e].

The already-proved epsilon action is D_epsilon=-I. Therefore a class
fixed by all of E must be zero. This is a reuse of the earlier central
action, not a new exclusion of covariant families.

The same conclusion holds even if the E intertwiners are allowed affine
translations. Suppose the history actions T_h(x)=rho(h)x+z(h) extend
to one affine action of S with linear part rho(h)g_e. The central
epsilon action then has the form x->-x+t, with a unique fixed point t/2.
Because epsilon commutes with every history, all T_h fix that same point.
Changing the origin to it makes every z(h) zero. Thus the class splits.

This says that a single globally fixed affine response is too restrictive
for a nonzero class in this particular model. It does not make the full
covariant family inconsistent, exclude physical modes, or infer a physical
meaning for an affine expectation value. Allowing the quotient line of
an extension to transform nontrivially changes the premise and needs its
own specified action; it is not covered by this particular fixed-line test.

## 3. A coherent family without choosing a nonzero point

Let Z=Z1(F,V_rho), a vector space of complex dimension four. It includes
all generator responses, including coboundaries. Define the **left**
lifted action on this family by

    A_e z(w)=g_e z(phi_e^-1(w)).

The intertwining equation proves this is again a rho-cocycle. Directly
A_e A_f=A_(e f); coboundaries are carried to coboundaries with their
actual transformed origin. This is D_(e^-1), not the right D action.

On Z direct_sum V define

    F_h(z,x)=(z,rho(h)x+z(h)),
    B_e(z,x)=(A_e z,g_e x).

Although each fibre action is affine, these are linear maps on the total
space: z->z(h) is linear. The cocycle law gives F_h F_k=F_(h k),
and direct substitution gives

    B_e F_h B_e^-1=F_(phi_e(h)).

For example A_e^-1 z(h)=g_e^-1 z(phi_e(h)), so the transported translation
is precisely z(phi_e(h)). Also B_e B_f=B_(e f). Thus F_h B_e is an exact
representation of S on this six-complex-dimensional total family.
Its dimension is not a particle or generation count.

The zero class and the nonzero classes are retained in one construction.
Central epsilon acts by (z,x)->(-z,-x), so it transports nonzero fibres
rather than requiring each fibre to be fixed. The entire allowed family
is coherent even though no nonzero class is individually E-fixed.

No global representative of H1 was silently selected. One may quotient
cocycles by origin changes to describe their classes; retaining Z is a
direct way to keep the actual origin transformations and avoid an
unjustified equivariant choice of a normalized section.

## 4. Information and physical limits

The history kernel of the total-family action is the companion note's
K={h:rho(h)=I and z(h)=0 for every cocycle}. It is not the identity
kernel: a^4 is killed. The faithful larger register in section 1 and
the local response family in section 3 therefore do different jobs.
Their joint use is allowed; the local family does not exhaust the weave.

Nontrivial evaluation on an h in ker rho produces a nontrivial unipotent
F_h on this finite total space. Such a map cannot preserve a constant
positive-definite Hermitian form: if U=I+N with N^2=0 and N!=0, choose
y with Ny!=0; U^m y=y+m Ny is unbounded. A positive invariant norm would
make all those norms constant. This is a scoped metric duty, not a no-go
for the fibre's affine Euclidean isometries, a varying metric or another
explicit physical realization.

The existing affine point rho, its lift, the normalized response family
and its local D4 geometry are all nontrivial mathematical structure. Yet
the family contains its zero-class stratum. To derive an actual nonzero
physical response requires a justified state law, a source or an action
that distinguishes that stratum. Uniform finite-group covariance or the
word 'non-cancellation' alone supplies no such state law in this proof.

The next question is consequently precise: **which distinctions must
this local doublet response itself retain, rather than a different part
of the complete register?** The companion detecting word turns one
candidate requirement into the exact condition [z]!=0, but does not
derive the requirement. This is where a genuine foundational reduction
must occur before a physical-input row can be paid.

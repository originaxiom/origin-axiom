# Word lift families and the relation that must travel with them

October 18, 2026. Analytical derivation and source reconciliation;
non-authoring review and executable safeguards remain outstanding.
This note is not included in the existing unsealed seventeen-control
specification. No scientific producer run or canonical amendment.

The whole-word question has two different answers depending on what is
enlarged. Changing one consistent pair of elementary lifts can be a common
change of basepoint. Allowing all elementary lifts independently enlarges
the operation group. The record matrices cannot distinguish those choices.
Their composition law can retain the difference without declaring it
physical or adding an observer by definition.

## Existing results that must not be rediscovered

Main was fetched again and remains at
2e5716bd9bea013d69f3cd733f083b61a6f59dbd, GENESIS v1.48. Its GM2 postulates
the matrix shears, GM4 postulates the surface reading with the puncture
conditional, and GM5b adopts inverse moves as a reading rather than a
derivation from PF1.

B1323's dictionary already distinguishes G(b)=ab and Gt(b)=ba with the
same incidence matrix. B1634 already identifies the ruled word group
with B3 and retains its boundary-twist kernel. R79 already derives the
central extension and the transport of peripheral slopes. Those are
positives to reuse, not gaps to announce.

The present issue is how to use them together without making a change
of representation into a new physical input, or an extra operation into
a harmless notational change.

## Four elementary positive lifts and four equivalent pair choices

Use F2=<a,b>, A=a^-1, B=b^-1 and I_u(x)=u x u^-1. Function composition
acts on the rightmost argument first. The two matrix shears are fixed.
Among positive word automorphisms with those incidence matrices, the
possibilities are exactly

    L  : a -> a,  b -> ab,       Lbar : a -> a,  b -> ba,
    R  : a -> ab, b -> b,        Rbar : a -> ba, b -> b.

Exhaustiveness here needs no census: the L incidence columns require one
letter a in the first image and one each of a,b in the second. There are
only ab and ba in the second image. The R argument exchanges the columns.
Each displayed map is invertible, by deleting the same letter on the
appropriate side. Positivity and these unit incidence matrices are
explicit hypotheses, not consequences of PF1 alone.

The elementary identities are

    Lbar = I_A L,        Rbar = I_b R,
    I_u f I_u^-1 = I_(u f(u^-1)) f.

They give the following complete comparison of the four *fixed pairs*:

| Pair used for every occurrence | Conjugator u from the original pair | Fixed boundary word I_u(c) |
|---|---|---|
| (L,R) | 1 | aBAb |
| (L,Rbar) | A | BAba |
| (Lbar,R) | b | baBA |
| (Lbar,Rbar) | bA | AbaB |

Here c=aBAb. For example, u=bA gives
u L(u^-1)=A and u R(u^-1)=b, hence sends both original generators to
their barred partners. For u=A the L correction is trivial and the R
correction is b. For u=b the L correction is A and the R correction is
trivial. These substitutions establish every row.

Consequently every finite word in any one fixed pair, including inverse
moves, is conjugate by that same I_u to the corresponding original word.
The boundary, inputs, outputs and matching maps must be transported too.
It would be wrong to count the four rows as four distinct physical
theories merely because their based words differ. It would also be wrong
to hold their based boundary data fixed while calling them equivalent.

This comparison is already needed between two actual instruments.
B1323's st_morphism_from_lrp takes R to E G E, which is Rbar here;
B1634 uses R(a)=ab. For their respective LR words the images are
(aba,ab) and (aab,ab). They have the same matrix and are related by the
second row's *conjugation of the entire action*. This is not the same
operation as postcomposing one monodromy with an inner map to normalize
its boundary word, as in R79. The dictionary's incidence equivalence is
sound, but based data must cross this explicit map before being reused.

Fixing c exactly distinguishes the original positive pair in these
coordinates: Lbar(c)=Aca and Rbar(c)=bcB are different reduced words.
But changing c with the table changes the coordinates, not that fact.
The matrices alone do not select the particular based word c.

## Allowing all four moves is not the same operation

Let G=<L,R> include inverses, as the current ruled group does. If Lbar
and Rbar become independently selectable generators as well, then

    Lbar L^-1 = I_A,       Rbar R^-1 = I_b.

These generate all inner automorphisms of F2. Conversely every barred
generator lies in Inn(F2) G. Thus the enlarged group is exactly

    H = Inn(F2) G = Aut^+(F2).

For the last equality use Nielsen's kernel theorem, already used in
R79: Aut(F2) -> GL(2,Z) has kernel Inn(F2). Given an orientation-positive
automorphism f, choose g in G with the same matrix, since L,R generate
SL(2,Z). Then f g^-1 is inner, which proves the equality.

This is the group closure of allowing both elementary word orders,
not merely a longer census in the old alphabet. It adds no determinant
negative move. Its positive monoid is the special Sturmian monoid;
the relation to B4 modulo its centre is classical, not a proposed new
gauge group. The four-generator presentation is in Kassel and
Reutenauer, [Sturmian morphisms and bases of F2](https://arxiv.org/abs/math/0507219),
section 2; the Nielsen kernel is recalled at the start of section 3.

The distinction is conditional and exact. It does not authorize this
enlargement of the programme's ruled grammar. GENESIS leaves extra
basepoint moves as a separate specification. Nor does the larger group
automatically repair flavour exclusions: whether its inner actions are
gauge, global symmetries or physical updates changes the question.

The matrix image is still SL(2,Z). Therefore a result that factors
entirely through that matrix action, such as its action on the three
nonzero parities, is unchanged by this enlargement. Additional based
information is not automatically an additional record-level prediction.

## The old group already contains a nontrivial registering loop

Reuse the explicit S=L R^-1 L from LIFT_SCOPE_NOTE. It satisfies

    S^2 = I_(aB) J,       J(a)=A, J(b)=B,
    S^4 = I_(aB J(aB)) = I_(aBAb) = I_c.

Its matrix fourth power is the identity, but its word fourth power is
not. For example I_c(a) is the reduced word aBAb a BabA, not a. Since
F2 has trivial centre and is torsion-free, I_c has infinite order.
The precise old result is

    G intersect Inn(F2) = <I_c>,
    1 -> <I_c> -> G -> SL(2,Z) -> 1.

R79 gives the kernel argument: an inner map fixing c must conjugate by
an element of its centralizer, and C_F2(c)=<c>. B1634 identifies G with
the boundary-fixed group, so this recovers its full kernel, not merely
one loop. The same distinction appears in Kassel and Reutenauer,
[A palindromization map for the free group](https://arxiv.org/abs/0802.4359),
sections 1 and 2. Their generators are (Lbar,R); the table transports
their boundary convention to this one.

The loop need not be invisible to every representation, but it is
invisible to the record matrices. B1634's received spin lift sends it
to -1; that numerical producer was read, not rerun or promoted here
into a fresh exact certification. Its addendum's handedness convention
remains in force. R79 shows separately why a changed normalized lift
requires a peripheral-coordinate shear. No physical chirality follows
from the existence of this loop alone.

## A composition law for the retained relation

Suppose two specifications assign automorphisms rho(w), rho'(w) to
histories and have the same homology for every history. Nielsen's
theorem and the trivial centre of F2 give a unique h(w) such that

    rho'(w) = I_(h(w)) rho(w).

For composable histories u,v, multiply these equalities and use
rho(u) I_x rho(u)^-1 = I_(rho(u)(x)). Uniqueness gives

    h(uv) = h(u) rho(u)(h(v)).

This is the noncommutative cocycle law for the relative register. It is
forced by the two specified actions and composition, not supplied as
an independent physical interaction. It supplies no probability, energy,
clock or interpretation of the register as awareness. A fixed common
basepoint change g gives the particular solution

    h(w) = g rho(w)(g^-1).

More generally, if a chronological path uses changing frames g_0,...,g_n,
the transported step is

    T'_j = I_(g_j) T_j I_(g_(j-1))^-1.

Cancellation of adjacent frame changes gives, for every finite path,

    T'_n ... T'_1 = I_(g_n) (T_n ... T_1) I_(g_0)^-1.

Keeping both endpoints makes the redescription commute with composition.
Dropping an endpoint relation can change a based output; treating every
moving frame as a new physical event is a different specification.
The coefficient-space version is the already-drafted gluing transport
h -> g1 h g2^-1. Neither version chooses which separate carriers join.

The enlarged architecture must also avoid counting one relation twice.
The map

    F2 semidirect G -> H,        (u,g) -> I_u g

is surjective, with multiplication (u,g)(v,k)=(u g(v),gk). Its kernel
is exactly {(c^n,I_(c^-n)): n in Z}, because G's inner intersection is
<I_c>. Hence H is this semidirect product divided by that shared cyclic
subgroup, not a free addition of every word register to every old move.
This description follows directly from the factorization above; it is
not an assertion that a second physical sector has been derived.

## Consequences for the goal and its input accounting

There are three different questions to ask of every calculation:

1. Does it enumerate all histories in a fixed admitted alphabet?
2. Does it keep the word lift and transport the relative register?
3. Does it enlarge the alphabet or assign a physical role to its actions?

Answering the first does not answer the other two. Conversely, changing
one consistent lift convention need not add a physical parameter. The
table prevents that false price; the enlargement and cocycle laws
prevent forgetting a genuinely changed operation set.

The programme should calculate G with its retained kernel on the ruled
branch, and treat H as a named alternative if its extra moves are
admitted. Both can be compared without choosing Fibonacci or m004 as
the whole object. The receiving action, boundary data and observables
must decide whether the extra register survives physically. Neither
GM1/GM2 nor these identities derive that decision, a boundary response,
the field dictionary, three physical families or qualia.

No complete priced-input row is earned here. The useful reduction is
more precise: do not charge a coordinate convention as a new interaction,
and do not erase an independent operation as a coordinate convention.

## Reading and verification record

Personally read B1323's complete dictionary producer; B1634's complete
findings, post-seal producer and hand-convention addendum; P9 sections
3 and 4 as reuse pointers; and R79's complete proof. Main's current GM1,
GM2, GM4 and GM5b statuses were checked directly. No other seat's test
results were represented as freshly executed.

The fourteen-page arXiv v2 of the palindromization paper was read in full,
including its noninjectivity and cocycle qualifications. The older
twenty-five-page Sturmian paper was read at its introduction, section 2,
and the Nielsen passage at the start of section 3, not in full. Its
other classification results are not used. These papers connect known
mathematics to the current specification; no novelty claim is made.

The elementary four-pair identities, S^4 identity, cocycle, telescoping
transport and shared-kernel quotient are authored algebraic arguments,
not yet independently accepted. They require their own two-sided
controls in a successor design before experimental execution. The
existing draft verification packet remains unchanged, rather than
silently claiming its seventeen tests cover this extension.

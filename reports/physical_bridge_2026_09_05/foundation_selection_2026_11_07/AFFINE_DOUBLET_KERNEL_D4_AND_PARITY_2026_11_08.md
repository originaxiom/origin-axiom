# The affine doublet response: a state-independent kernel and a D4 lattice

2026-11-08. Author analytical continuation of `2896d441a`.
**UNREVIEWED. No scientific import, collection or execution.**
All-word proofs below are authored arguments, not certified test outcomes.
No canonical GENESIS, frozen verification package or physical-input ledger
is changed. D4 here denotes a rank-four root lattice, not the order-eight
dihedral group also called D4 in other repository records.

## Outcome and premises

Fix the existing F=F(a,b), its quaternion doublet rho, and the affine-
response interpretation. For every **nonzero cohomology class**:

1. The affine history representation has the same kernel, independent of
   its nonzero state vector. It retains the complete supplied doublet H1
   and lifted move action on that response quotient.
2. Its exact translation lattice is D4. Its real affine geometry is the
   same up to similarity for every nonzero class.
3. The actual Nielsen word moves induce the full S3 action on the three
   nonzero D4 discriminant classes. This is explicitly intertwined with
   the existing three parity labels, not inferred from matching orders.

This conditionally removes a state-direction choice from the **word
kernel and real lattice shape**. It does not remove the scale, complex
polarization relative to other fields, the affine-response premise, or
the choice between zero and nonzero class. The kernel forgets positive
histories and some already-earned adjoint responses. Therefore it is a
local response quotient, not a replacement for the full weave.

## 1. Seen first and exact source scope

Sources read personally, without importing their producers:

- Fork `0c6570bab`, `reports/genesis_root_review_2026_10_11/cohomology_carrier/PROOF.md`:
  already proves the Q8 doublet H1, normal form z(a)=0, the detecting word
  r=[[a,b],a[a,b]a^-1] with z(r)=4v, metabelian failure and F/F''' sufficiency.
  These are reused below, not new results.
- Our `2896d441a`, `FIRST_ORDER_REGISTER_LAW_AND_MATTER_PRICE_2026_11_08.md`:
  affine composition, the universal additive response, adjoint/doublet
  distinction, finite-image averaging and metric prices. Its Fox/Weil
  source-reading receipts are retained.
- `COHERENT_WORD_LIFTS_AND_LOCAL_BOUNDARY.md` and
  `FAITHFUL_LIFTED_REGISTER_TOWER.md`: the actual E of pairs (phi,g),
  the right cohomology action D_e, central epsilon and the separate local
  and faithful registering objects. Their analytical review is not a
  review of this new argument.
- Main `217e37c4f`, B1614 findings: the adjoint/parity responses are already
  part of the programme. B1223's full findings were also read: its negative
  concerns a proposed arithmetic-field action, which is trivial. Nothing
  below identifies that field action with this new lattice action or
  reverses its verdict.

Source searches covered current main, fork, chat1, SM and selected AGY/
explore report/relay bodies for affine response, kernel and D4-lattice
connections. They are topic recovery, not exhaustive absence evidence.
One search incorrectly used a noncapturing regex group unsupported by
Git's extended regex; its error was noticed and the search repeated with
ordinary parentheses. No absence conclusion uses that failed command.
An attempted Kyoto quaternion-lattice PDF fetch timed out; no theorem
from that unread paper is applied. No mathematical originality is claimed.

## 2. Normalize the class, not an arbitrary raw cocycle

Let V=C^2, A=rho(a), B=rho(b), C=AB, with

    A^2=B^2=C^2=-I, AB=C=-BA,
    A^dagger=-A, B^dagger=-B, C^dagger=-C.

For z(uv)=z(u)+rho(u)z(v), subtract the coboundary
(rho-I)t with t=(A-I)^-1 z(a). Since A-I is invertible, each class has
a unique representative

    z(a)=0, z(b)=v in C^2.

The class is zero exactly when v=0. A nonzero raw z can still be a
coboundary, so raw nonzero generator values are not the discriminator.

For every word w write z_v(w)=P_w v. The universal coefficients obey

    P_1=P_a=0, P_b=I,
    P_(uw)=P_u+rho(u)P_w,
    P_(u^-1)=-rho(u)^-1 P_u.

Consequently P_w belongs to the Lipschitz quaternion order

    O=Z I + Z A + Z B + Z C

for every signed word. This follows by induction: rho(u) belongs to
Q8={+/-I,+/-A,+/-B,+/-C}, which preserves O by left multiplication.
No finite word-length check is needed for this all-word conclusion.

For P=p0 I+p1 A+p2 B+p3 C with real p_i,

    P^dagger P=(p0^2+p1^2+p2^2+p3^2) I.

The mixed terms cancel by anticommutation. Thus a nonzero P in O is
invertible on V (not necessarily a unit of the integral order O).
For every v!=0,

    P_w v=0 iff P_w=0.

## 3. A state-independent local history kernel

Use the semidirect law (P,q)(R,s)=(P+q R,qs) on O rtimes Q8. Define

    Xi(w)=(P_w,rho(w)),
    K=ker Xi={w:rho(w)=I and P_w=0}.

The recursion proves Xi is a homomorphism. The affine history action is

    T_w^v(x)=rho(w)x+P_w v.

For every nonzero v, its identity condition is exactly w in K. This
proves equality of all nonzero-class kernels, not merely the survival
of one detecting word. For v=0 the kernel is the larger N=ker rho.
Affine origin changes conjugate the action and do not change its kernel.

Every supplied doublet cocycle factors through F/K: after normalization
it does, and coboundaries vanish on K because rho(K)=I. Conversely quotient
cocycles pull back. Inflation therefore gives exactly

    H1(F/K,V_rho) -> H1(F,V_rho), an isomorphism.

The kernel is invariant under every admitted automorphism phi intertwined
with rho. One proof uses the universal definition: transporting any
cocycle by g^-1 z composed with phi permutes the cocycle family, and
rho(phi(w))=g rho(w)g^-1. Thus phi(K)=K. This retains the existing lifted
move action on H1, with its actual central signs. It is not a claim of
full invariance under arbitrary endomorphisms or a new legal-move axiom.

Parity twists do not introduce another word kernel here. The three
representations chi_p rho are conjugate to rho by B,A,C respectively for
p=(1,0),(0,1),(1,1). Their universal P_w are conjugate as well, so their
zero tests and nonzero-class kernels are identical. Retaining all three
blocks can still matter for their lifted action, fields and interactions;
this statement does not authorize deleting those labels or summands.

## 4. Exact translation lattice, without a lattice ansatz

The kernel N of F->Q8 is normally generated by

    r1=a^4, r2=a^2 b^-2, r3=b^-1 a b a.

Indeed these are the presentation relations a^4=1, a^2=b^2 and
b^-1 a b=a^-1. They reduce every word to a^i b^j with 0<=i<4,
0<=j<2; the actual A,B image has eight elements, so the presented group
is exactly Q8. This proves the normal-generation assertion.

On N the map P is additive. For n in N, conjugation gives

    P_(h n h^-1)=rho(h)P_n.

Direct use of the cocycle recursion gives

    P_r1=0,
    P_r2=-(I+B),
    P_r3=B+C.

For example P_(b^-1)=B and P_(b^-2)=I+B. This fixes the inverse-word
convention and yields P_r2=-(I+B). Hence P(N) is **exactly** the additive
span of the Q8 left orbits of I+B and B+C.

Identify O with Z^4 in the basis I,A,B,C, and put

    L={p in Z^4: p0+p1+p2+p3 is even}.

Both orbit generators have even coordinate sum. Left Q8 multiplication
is a signed coordinate permutation, so P(N) is contained in L. Conversely
its span contains

    A-I = B(B+C),
    B-I = B(I+B),
    C-B = A(B+C),
    I+B.

The first three generate all integer vectors of coordinate sum zero:
their edges connect the four coordinate vertices. The fourth has sum
two. Subtracting a suitable multiple of I+B from any even-sum vector
therefore leaves a vector in the first span. Thus P(N)=L, exactly.

This is the root lattice D4 by its defining even-sum coordinate model.
Its index in O=Z^4 is two. Its shortest nonzero vectors are precisely
the 24 vectors +/-e_i+/-e_j, i<j, of squared length two: squared length
one has odd coordinate sum, while squared length two forces that form.
No E8 root system or Lie algebra was inserted to obtain L.

For v!=0 the real-linear map q->q v is a similarity H_R->V_R, since

    ||q v||^2=|q|^2 ||v||^2.

It is injective by quaternion division and both spaces have real dimension
four. The translation group of the actual affine image is therefore
L v, a D4 lattice scaled by ||v||. In particular

    1 -> L v -> G_v -> Q8 -> 1.

No splitting of this extension is asserted. G_v is a discrete cocompact
group of Euclidean isometries: it is a finite union of translation-lattice
cosets with unitary linear parts. Its quotient is a flat compact orbifold,
not a manifold (T_a has order four and fixes the origin). This conditional
coefficient geometry is not identified with physical spacetime.

Any two nonzero v,w give real-similar marked affine actions via
S(q v)=q w. However S need not preserve the supplied complex structure.
Complex-linear intertwiners commuting with rho are only complex scalars,
so nonzero class directions modulo those intertwiners still form CP^1.
The real lattice shape and word kernel do not determine couplings that
also use that complex structure or another registering sector.

## 5. The actual word action on the lattice and its three discriminant classes

Use the existing based word conventions

    L:a->a,b->ab;       g_L=(I+A)/sqrt(2),
    R:a->ab,b->b;       g_R=(I-B)/sqrt(2).

The right cohomology action is D_e[z]=[g_e^-1 z composed with phi_e].
In the normalized v-coordinate, direct substitution gives

    D_L=(I+A)/sqrt(2),
    D_R=(I-A)/sqrt(2).

For R, the raw new generator values are g_R^-1 A v and g_R^-1 v;
renormalizing the first to zero gives

    D_R v=g_R^-1 v-(B-I)(A-I)^-1 g_R^-1 A v.

Quaternion multiplication reduces this to the stated formula. For n in
N, a renormalizing coboundary vanishes, so

    P_(phi(n))=g_e P_n D_e.

Both signs of a lift give the same lattice map. These are actual induced
word maps on N/K, not chosen root-system automorphisms. In the basis
I,A,B,C they are

    T_L(p0,p1,p2,p3)=(-p1,p0,p2,p3),

             [ 1  1  1 -1 ]
    T_R=1/2 [-1  1 -1 -1 ]
             [-1 -1  1 -1 ]
             [-1  1  1  1 ].

Their columns are orthonormal. T_L preserves the even-sum condition.
For T_R, that condition makes every half-sum coordinate integral and
the output sum -p0+p1+p2-p3 is even. Equal covolume then gives
T_L(L)=T_R(L)=L. Composition is a left action on L; the opposite order
of the right D action is required to obtain it.

The dual lattice is

    L*=Z^4 union (h+Z^4), h=(1,1,1,1)/2.

This follows directly from requiring integral pairing with all roots
e_i+/-e_j. Its quotient L*/L has four elements. Name the nonzero ones

    v0=e0+L, s0=h+L, c0=h-e0+L.

The explicit matrices give

| move | v0 | s0 | c0 |
|---|---|---|---|
| T_L | v0 | c0 | s0 |
| T_R | c0 | s0 | v0 |

For example T_L h=h-e0, T_R e0=-(h-e0), and
T_R h=h-e1-e2. The two distinct transpositions generate S3. This is
the lattice's actual triality action on the three discriminant classes.
It is not inferred from the presence of a V4 and an unrelated S3.

Identify v0 with the mod-two homology class of a, s0 with b, and c0
with a+b. The table is precisely L:a->a,b->a+b and R:a->a+b,b->b.
Using the mod-two alternating pairing identifies these with the existing
parity characters (0,1),(1,0),(1,1), respectively. On parity labels the
corresponding **left** transport is p->p composed with phi^-1, as in
the earlier local-module construction. Using p composed with phi for
arbitrary composites would reverse the composition order; the two
generator transpositions alone would not catch that error.

The discriminant quadratic function q(x+L)=||x||^2/2 mod Z is 1/2 on
each nonzero class. Under the identification {0,1/2} in Q/Z with F2
(0->0 and 1/2->1), it gives the anisotropic quadratic form on F2^2,
with value one on every nonzero vector. This also agrees
with the Q8 square register on Q8/{+/-I}: every nontrivial coset has a
lift squaring to -I. This is a compatibility of already-specified Q8
data, not a new derivation of the coefficient choice or an arithmetic
field action. In particular B1223's different negative remains intact.

## 6. What this local quotient loses

The old detecting word r=[[a,b],a[a,b]a^-1] has P_r=4I, so survives
every nonzero class. The affine image has derived length exactly three:
its abelian translation kernel and metabelian point group give an upper
bound three, while r in F'' has nontrivial image. This is compatible
with the fork's existing depth bound, now on an explicit smaller image.

But a^4 and b^4 are killed by every doublet cocycle: their geometric
series I+A+A^2+A^3 and I+B+B^2+B^3 vanish. Thus K contains a^4,
which is not even in F', let alone F'''. This quotient loses positive
word fidelity. The full class-family does not repair that loss.

There is an existing recorded algebraic response that detects it. For
the sign coefficient chi(a)=+1, chi(b)=-1, the cocycle u(a)=1,u(b)=0
is a nonzero H1 class, and u(a^4)=4. Coboundaries have zero a-value.
This is one of the adjoint parity lines already in B1614 and derived
again in the preceding response-law note. Therefore the D4 response
quotient does **not** retain the complete set of already-earned tests.

This is why the full relational architecture must retain multiple
registers or their common refinement. Showing the doublet's carrier
dependency can be reduced does not reduce the whole genesis to G_v.
Nor do its three discriminant classes establish three fermion families.

There is also a concrete trace-only comparator. Homogenize the affine
action as the three-by-three block matrix [[rho(w),P_w v],[0,1]]. Its
ordinary character is tr rho(w)+1 for **every** v, including zero. Thus
the split and nonsplit affine histories have identical characters while
their word kernels differ (r distinguishes them). Character equality
cannot replace an intertwiner or full-register test on these reducible
nonsemisimple representations. This is compatible with using characters
to classify the earlier semisimple irreducible sector; its hypotheses
are different. The programme's existing nonsplit constructions are not
declared absent or invalid by this comparison.

## 7. The remaining compulsory-response question is now explicit

Within this affine coefficient block, retaining r is equivalent to
[z]!=0, since z(r)=4v. In fact every admitted automorphic image of r
is retained by every nonzero class: its evaluation is obtained from the
invertible D_e and g_e. That requirement can be stated invariantly for
the block, rather than selecting a fitted direction or amplitude.

However requiring that r be retained **somewhere in the whole register**
does not imply that this doublet block must retain it. The faithful
larger register already can do so with an affine response equal to zero;
the companion full-lifted control exhibits that explicitly. The missing
derivation is why the primitive relation allocates this information to
this local response, or why an actual action makes the zero-class state
inadmissible or unstable. No such action is supplied by this proof.

The zero-class background is not absolute nothingness: it still contains
F, rho, its nontrivial commutator, the lifted operation group and the
other registering data. One cannot exclude it just by naming its zero
coefficient 'nothing'. Likewise a generic nonzero class does not become
the physical state without a justified measure or dynamics.

## Verification status and next bounded check

This packet needs independent proof review and exact algebra controls
before any claim of computational verification. No existing review scope
or main acceptance covers it. Proposed controls must distinguish:
zero class versus a nonzero coboundary; the shared nonzero-class kernel
versus full word faithfulness; the exact D4 span versus its ambient Z^4;
the real similarity versus complex equivalence; and the correct inverse
parity transport versus the wrong composite order.

No numerical SM targets, parameter fits, gravity, physical end law or
chiral spectrum is produced. The positive is an explicit conditional
register-to-geometry-to-parity map, with its information loss preserved.

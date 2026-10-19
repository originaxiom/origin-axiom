# Relative word area: an integer register, not yet a physical end law

October 19, 2026. Conditional analytical derivation, pending independent
review. No scientific producer, enumeration or mathematical test is run.
The domain here is the declared free word group F(a,b), not the group E
of lifted operations on those words. Inverse letters are bookkeeping in
that group; their use below does not admit inverse forward updates.

The earlier [additive-label result](INTEGER_END_DATA_AND_REGISTER.md)
does not exclude an integer retained by a relation between words. This
note exhibits one explicitly, including its losses and physical costs.
It is classical nilpotent word algebra, not a new existence theorem,
selection principle or claimed physical breakthrough.

## Source reuse and convention

The owner's Gate 10 archive already constructs a separating Magnus
tower for based automorphisms and exposes the failure of count-only
records. Its PROOF_AND_SCOPE.md was reread directly in
`Origin_Axiom_Banking_Seat_FULL_Through_Gate11_2026_10_13.zip`, under
`EXPANDED_POST_GATE3/10_FAITHFUL_GATE_10/Gate10_Faithful_Records/`.
The archive root is `Origin_Axiom_Banking_Seat_2026_10_13/`.
Its published finite enumerations remain received, not rerun here.
The current [faithful lifted tower](FAITHFUL_LIFTED_REGISTER_TOWER.md)
already retains more than the quotient considered below. We are making
one information channel explicit, not discovering a missing tower.

For external background, Cordes, Duchin, Duong, Ho and Sanchez,
[Random Nilpotent Groups I, section 1.2](https://doi.org/10.1093/imrn/rnv370),
identifies the free class-two rank-two nilpotent group with the integral
Heisenberg group. That section and its normal-form conventions were
read directly. Our coordinate order below is different from its
a-before-b normal form; the displayed formulas fix the convention.
No probabilistic hypothesis or result from that paper is imported.

Write [a,b]=aba^-1b^-1 and z=[a,b]. Do not confuse this z with
the fibre coordinate in the earlier theta-field notes. The quotient

    N=F2/Gamma_3(F2)

has z central. It has coordinates (m,n,k) and multiplication

    (m,n,k)(p,q,h)=(m+p,n+q,k+h+m q).                (1)

The corresponding upper-triangular matrix has rows (1,m,k),
(0,1,n), (0,0,1). The generator images are a=(1,0,0), b=(0,1,0).
Every element has the unique normal form b^n a^m z^k. To check
the quotient claim without a counting experiment: centrality of
[a,b] permits collecting every word into that form, and its matrix
has exactly those three coordinates. No further identification of
normal forms is possible. Thus these matrices realize F2/Gamma_3,
not the faithful free group.

## The retained integer and its composition law

For example,

    ab=(1,1,1), ba=(1,1,0), z=(0,0,1).

Appending a changes m by one; appending b changes n by one and
adds the current m to k. For positive words, k counts occurrences
of an a before a b. For signed words it is the lattice integral
sum x Delta y along the associated horizontal/vertical path.
On a closed zero-count path it is signed area with multiplicity,
not unsigned area of a necessarily simple region.

Formula (1) is associative because

    m q+(m+p)t=p t+m(q+t).

The extra term m q is the composition record. Dropping it would
replace this group by an abelian one and erase ab versus ba.
Equivalently, from an endpoint (m,n), traversing a word with
coordinates (p,q,h) increments the area coordinate by h+m q.
For successive words those increments add only after updating
the endpoint. This is an explicit state-dependent law, not an
ordinary integer-valued homomorphism on all words or operations.

For two words u,v with the same counts (m,n), define

    A(u,v)=k(u)-k(v).

Then u v^-1 maps to z^A. This is defined for every such pair in
the declared word group, not just a selected Fibonacci thread.
It is a quotient observable: distinct free words can still have
the same counts and area. It does not classify their full relation.

There is also an exact joining law for these relative records. Let

    P_rel=F2 x_(Z^2) F2
         ={(u,v): counts(u)=counts(v)}.

Componentwise composition (u,v)(u',v')=(u u',v v') preserves this
condition. In (1) the cross terms cancel between the two components,
so

    A(u u',v v')=A(u,v)+A(u',v').                  (1a)

Thus A:P_rel->Z is a surjective homomorphism: A(ab,ba)=1.
For composable comparisons it also obeys
A(u,w)=A(u,v)+A(v,w). These are mathematical joining/relative
transport laws, not nonzero physical interaction amplitudes.
P_rel includes every equal-count pair in the declared group; its
definition does not prove that those pairs are jointly realized.

## Frame covariance: the relative quantity is better than the absolute one

Gamma_3 is characteristic, so every free-group automorphism acts
on N. Let its generator images have coordinates

    phi(a)=(p,r,s), phi(b)=(q,t,h), d=p t-q r=+1 or -1.

Since [phi(a),phi(b)]=z^d, collecting phi(b)^n phi(a)^m z^(d k)
gives the exact transformation

    m'=p m+q n, n'=r m+t n,
    k'=d k+m s+n h+p r m(m-1)/2
                      +q t n(n-1)/2+q r m n.       (2)

The power formula behind (2) is
(p,r,s)^j=(j p,j r,j s+p r j(j-1)/2), valid for all integer j.
Subtracting (2) for equal-count words cancels every correction:

    A(phi(u),phi(v))=d A(u,v).                     (3)

Thus the relative integer is invariant under every common
orientation-preserving automorphism and changes sign under a
common orientation reversal. This is covariance of a pair, not
a physical assertion that its absolute sign is observable.

In particular the orientation-preserving operation group acts on
P_rel preserving A. Its specified lift E acts through its word
automorphism. Consequently the semidirect product P_rel semidirect E
has the integer homomorphism ((u,v),e)->A(u,v), zero on E itself.
This is an explicit relational enlargement that escapes the E-only
additive-label obstruction; it is not a contradiction to E_ab=Z/24.
Which such enlarged states are physically admitted remains a duty.

Concrete elementary checks, with the source's based conventions:

    L: b->ab       (m,n,k)->(m+n,n,k+n(n+1)/2),
    barred L: b->ba        (m+n,n,k+n(n-1)/2),
    R: a->ab              (m,m+n,k+m(m+1)/2),
    barred R: a->ba       (m,m+n,k+m(m-1)/2),
    S: a->a^-1,b->b^-1    (-m,-n,k),
    P: a<->b              (n,m,m n-k).

Unlisted generators in those substitutions are fixed. S has
determinant +1 on counts; P has determinant -1. Neither is hereby
made a legal forward update.

Conjugation by a word with counts (u,v) changes k to
k+u n-v m. Consequently A is unchanged by common conjugation
of both words. Independent conjugations need not preserve it.
For one word with primitive counts gcd(m,n)=1, these shifts
range over all integers. Its absolute k cannot distinguish its
unbased conjugacy class. For zero-count words, by contrast, k
itself is invariant under conjugation in this quotient. These
distinctions prevent an unearned return from a relational register
to a preferred absolute word label.

## What the quaternion reading loses, and what this quotient still loses

For the already specified rho(a)=i,rho(b)=j in Q8,

    rho(m,n,k)=j^n i^m (-1)^k.                    (4)

Indeed Q8 has central commutator [i,j]=-1, so the free-word map
factors through N; (4) follows from its normal form. For equal-count
u,v, their relative quaternion image is (-1)^A. It retains the
parity of A, not the integer. This is a precise loss in this
coefficient reading, not a claim that every programme observable
or its faithful tower loses A.

There is another, opposite limitation. The source c=a b^-1 a^-1 b
maps to z^-1. Its value is nontrivial, but its inner automorphism
acts trivially on N because z is central there. Thus reading the
word c is not reading the operation Inn_c. In particular the
source relation Delta^4=Inn_c becomes the identity as an operation
on N. This is compatible with Gate 10 needing deeper Magnus
information to detect that operation. N is not a replacement for
the full registering architecture or its coefficient lift.

## Can the integer supply the end winding?

There is a natural mathematical circle dual to the central group
<z>=Z. Evaluating z^A on its characters gives exp(i A theta),
whose winding is A. In this limited sense the relative word record
already provides an integer and an associated circle map, without
choosing the integer first to match a generation count.

But this is not yet a field on the physical end. Even its most
naive extension fails: any scalar representation of the entire N
into U(1), or into circle-valued scalar functions, kills z because
z is a commutator and the target is abelian. It cannot restrict
on the center to exp(i theta) for every theta.

Likewise, if a d-dimensional representation has central action
R_theta(z)=exp(i theta) I_d, the relation z=[a,b] implies

    1=det([R_theta(a),R_theta(b)])=exp(i d theta).

A fixed finite d therefore cannot realize this central character
for the full circle. This does not forbid projective, state-dependent
or infinite-dimensional realizations; it identifies why a scalar
winding cannot simply be appended to a finite coefficient multiplet.
Nor does it prove that a physical end must realize this particular
central-character construction at all.

The domain distinction is essential: on P_rel itself, (1a) DOES
give the scalar representation (u,v)->exp(i A(u,v) theta) for
every theta, and it extends trivially over E in the semidirect
product above. The preceding obstruction is to its proposed
extension over N, not over this relative-pair group. A relative
boundary transition is therefore a mathematically available
candidate rather than excluded by either determinant argument.
No identification of this character circle with the physical end,
of its represented pairs with physical fields, or of its scalar
phase with an E8-compatible interaction/domain has been derived.

The earlier E_ab=Z/24 result concerns additive labels of lifted
operations. A concerns pairs of equal-count words. Different
domains and composition laws explain why both conclusions hold.
Neither computation selects which word pairs physically meet,
which inverses are legal, an interaction amplitude, a preferred
area, an end field or a fermion boundary domain.

## Verdict and next bounded duty

Positive: order-sensitive relational integers are already available
in a standard quotient of the declared word architecture. The
additive-label obstruction must not be compressed into an absence
of every integer register. The shared frame is essential, as the
owner's act-plus-register concern requires.

Not established: a law that realizes these relations as physical
interactions, or a covariant map from this relative integer to the
actual boundary response in one action. The integer's existence
does not derive a nonzero physical index, three generations, gauge
content, a metric, an observer or qualia. No physical-input row is paid.

The next useful test is a source-level compatibility construction:
state the actual relation space and its joining rule, retain the
full lifted coefficient action, and derive rather than stipulate
the boundary field and its variational domain. The central-circle
extension obstacle above must be addressed if the route uses N;
the P_rel alternative has its own physical-realization duties.
An executable successor should check signed inverse conventions,
equations (1)-(4), common versus independent conjugation, and a
word in Gamma_3 erased here but retained by a deeper register.
Those controls are not in the sealed v3 package and are not run.
The v2/v3 seals, historical noncompliance and pending review remain
unchanged; main acceptance is not replaced by this analytical note.

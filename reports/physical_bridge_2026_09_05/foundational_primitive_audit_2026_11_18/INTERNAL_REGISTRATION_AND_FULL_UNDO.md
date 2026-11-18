# Internal registration, full undo and the law that is still supplied

2026-11-18. Author hand arguments under scope `6941e2b1b`.
**Not independently checked.** No scientific import, execution, CAS,
finite enumeration, numerical test or empirical comparison occurred.
Elementary countermodels are not proposed physical theories. Standard
mathematics is credited as such; no new general theorem is claimed.
Read the exact comparison packages in PACKAGES_AND_PREMISES.md first.

## 1. Complete inverses and records

Let S be the stated complete state set, U:S->S a bijection and
R:S->O any state-dependent registering test. If its full inverse is
admitted, then for every s,

    R(U^-1 U(s)) = R(s).                              (1)

This follows by substituting U^-1 U=id_S. It concerns a full inverse
on the same S, not an inverse on one projection of S. No probability,
thermodynamics, Hilbert representation or consciousness premise occurs.

Thus the following two requirements cannot both hold literally: every
complete registration process has an admitted full inverse, and its
state-dependent record must differ after that full inverse. A surviving
record needs a different condition: undo only part of the process;
restrict actual inverses; include a record not undone by the specified
operation; or use a history-dependent quantity which does not factor
through the asserted complete state. These are distinct specifications.

The last case must not be hidden. If h is a formal history, e(h):S->S
its evaluated update and L(h) a ledger entry, e(h)=id_S does not imply
L(h)=L(empty). But if L is asserted to be physical memory, S has omitted
it or the alleged full inverse has not inverted it. An append-only
history coordinate changes the full update law. Keeping all words in
the mathematical account is not a proof of such a physical coordinate.

Equation (1) does not prove that every physical process is invertible,
that every allowed inverse is physically implementable, or that a
macroscopic observer can reverse a measurement. It prevents those
different questions from being answered by an object-only calculation.

## 2. A coupled family with an internal register

For any integer m>=2, explicitly choose

    S_m = (Z/mZ) x (Z/mZ),  s=(x,r),

and define total admitted updates

    V(x,r)=(x+1,r),
    U(x,r)=(x,r+x),
    J(x,r)=(r,x).                                    (2)

Arithmetic is modulo m. Include the inverses and every finite word.
They are

    V^-1(x,r)=(x-1,r),
    U^-1(x,r)=(x,r-x),  J^-1=J.                      (3)

These are global bijections, with no discarded inputs. The object and
register are roles of the two coordinates. The internal update U writes
x into r when r initially equals zero. That preparation is an input,
not a state selected by the principle. The conjugate J U J acts as

    J U J(x,r)=(x+r,r),                              (4)

so register data can affect the other component. J interchanges the
roles while transporting their readouts. This is explicit mutual
influence within S_m; there is no third, external dynamical reader.
It does not model subjective experience or derive a physical mechanism.

The updates are not all commuting:

    U V(x,r)=(x+1,r+x+1),
    V U(x,r)=(x+1,r+x).                              (5)

The difference is the registered unit. The noncommutativity follows
from these chosen coupling formulas, not from the word "distinction"
alone. One should not repackage it as a derivation of (2).

### Unbounded and multiple-register controls

Finiteness is not essential to (2)-(7). Replacing Z/mZ by Z gives
unbounded, reachable and contextually distinguishable record values,
with the same total inverses and internal reciprocal coupling. The
coordinate translations V and J V J reach every pair of integers.
The finite examples therefore need not be the only controls offered
when unbounded operational distinction is additionally required.

There is also a directly interacting d-component construction for
every d>=2. On A^d, for A=Z/mZ or Z, admit every coordinate translation,
every addition x_j -> x_j+x_i for i!=j, coordinate permutations and
their inverses. Every component can write into every other and be
affected by it. No component is a dummy or an external dynamical reader.
The one-coordinate outputs after permutations separate all states.
For A=Z/2Z, d=2 and d=3 have respectively four and eight distinguishable
states, so their adequate state carriers cannot be isomorphic. For
A=Z, both have unbounded reachable distinctions. These are models of
the operational requirements, not a statement that d is a physical
dimension or the rank of an irreducible coefficient representation.

Infinite formal history length, unbounded operational distinctions and
GENESIS PF2's philosophical inexhaustibility must not silently be
identified. Only the first two have been specified by these models.
Faithful free-word realization, a surface category and the fixed-character
premise are still absent. None of the examples refutes the full OA
axiom package or an unformalized stronger meaning of PF2 or qualia.

## 3. Object cancellation, registered difference and full cancellation

Starting at (0,0), the following legal process has three stages:

| Stage | Complete state | What has happened |
|---|---|---|
| input | (0,0) | Chosen ready state |
| V | (1,0) | Object changes |
| U V | (1,1) | Register changes in response |
| V^-1 U V | (0,1) | Object returns, record differs |

The complete map of this process is

    W=V^-1 U V,  W(x,r)=(x,r+x+1).                   (6)

It is not id_S. Its actual inverse is

    W^-1=V^-1 U^-1 V,
    W^-1(x,r)=(x,r-x-1).                             (7)

Applying (7) after (6) restores both coordinates for every input. The
same internally registering system therefore has both the apparent
object remainder and complete undo. Neither result identifies its zero
state or its identity process with absolute physical nothingness.

This calculation works for m=2 and m=3 as well as every other m>=2.
It supplies binary and nonbinary realizations of the comparison
packages. It does not say how many fundamental physical records there
are: the chosen two-component decomposition remains an explicit input.

## 4. Exactly when the additional register cannot be discarded

Take the projection q(x,r)=x and retain the output o_x(x,r)=x. Its
instantaneous output factors through q. Nonetheless q is inadequate
for the full admitted context family, because

    q(J(x,r))=r.                                    (8)

Two states (x,r_1) and (x,r_2) with r_1!=r_2 have the same q but
different outputs after J. Equivalently J cannot descend to a map of
x alone. The elementary AR1 update/output criterion already owns this
argument's general form. It is reused, not newly discovered here.

Conversely, if one specifies only V, U and their inverses and observes
only x, all future x outputs are independent of r. For that smaller
duty, q is sufficient. If an r output, J or (4) is reinstated, that
smaller quotient is no longer sufficient. This is why the admissible
contexts, rather than a slogan about preserving all information, decide
whether an extra registering component is necessary.

With J available, the future tests o_x and o_x J separate all states
of S_m. The contextual state quotient is the whole S_m. No further
outside state is required for these declared duties. This is a bounded
positive about model completeness relative to tests, not a claim of
complete physical or phenomenological closure.

## 5. The group carried by the two-update register

Reuse the existing Heisenberg alternative through its explicit action.
The subgroup generated by U and V consists exactly of

    T(a,b,c)(x,r)=(x+a,r+b x+c),
    a,b,c in Z/mZ.                                  (9)

Composition gives

    T(a,b,c) T(a',b',c')
      =T(a+a', b+b', c+c'+b a'),                    (10)

and inversion gives T(-a,-b,ba-c). Direct evaluation of the commutator
in the convention [U,V]=U V U^-1 V^-1 yields

    [U,V](x,r)=(x,r+1)=:C(x,r).                     (11)

C commutes with both U and V. Moreover

    V^a U^b C^c = T(a,b,c),                          (12)

so every triple occurs. Distinct triples give distinct maps: the x
coordinate determines a, the r change at x=0 determines c, and its
change at x=1 then determines b. Thus the group has m^3 elements and
is the finite Heisenberg group in the coordinate convention (10).
This is familiar algebra, not a proposed new OA theorem.

At m=2 this group has eight elements; U and V are distinct nonidentity
involutions and (UV)^2=C!=id, so UV has order four. It is the dihedral
group of order eight. It is not Q8, which has only one nonidentity
element of order two. A noncommuting internal registration can therefore
meet the declared packages without having the quaternion update group.

The full model also admits J, so its update group is larger. In the
binary case, U and J fix (0,0) and generate all permutations of the
three nonzero states: U interchanges (1,0),(1,1), and J interchanges
(1,0),(0,1). V and J V J supply both coordinate translations, making
the action transitive on four states. The stabilizer has at least six
elements, so the group has at least 4*6=24 elements and is a subgroup
of S4, which has 24. It is S4. No equivalence with 2T follows from an
equal group order. The example shows why the process group, a chosen
coefficient representation and a covering group are different data.

This does not test the stronger OA theorem requiring one invariant
irreducible SL2 character under its particular Nielsen moves. That
extra requirement is absent here. The November 7 proposal already
preserves this exact scope distinction and the Heisenberg control.

## 6. Why a minimal adequate register does not select its own tests

Reuse the November 7 contextual quotient, with its hypotheses visible.
Let H be a supplied group, pi:H->G a surjective homomorphism and

    R_pi(h)=1 if pi(h)!=1_G, and 0 otherwise.

Define h~k when R_pi(u h v)=R_pi(u k v) for all u,v in H. If pi(h)=pi(k),
that equality follows by multiplication. If h~k, take u=h^-1,v=1_H.
It gives R_pi(1_H)=R_pi(h^-1 k), hence pi(h)=pi(k). Thus

    H/~ is isomorphic to G.                         (13)

The minimality is conditional on the supplied test R_pi. It cannot
earn the choice of G hidden inside that test. General rank controls and
the prior faithful/moving-sector alternatives are reused by reference,
not re-enumerated or newly certified here. An observation of two outcomes
also does not imply that H/~ has two states: contextual tests can jointly
separate arbitrarily many classes.

## 7. Self-consistent stationary closure still need not fix a law

For this control only, additionally supply finite-state probability.
This is not a derivation of probability, quantum amplitudes or a clock.
It tests a weaker, precisely defined stationary-closure interpretation;
it is not a countermodel to a separately specified full read-out law.

Let S be any finite state set with N>=2, let Pi be the N by N matrix
with every entry 1/N, and for 0<t<1 put

    P_t=Pi+t(I-Pi)=t I+(1-t) Pi.                    (14)

Every entry is strictly positive, each row and column sums to one, and
P_t commutes with every permutation of S. The uniform distribution is
stationary. It is the unique stationary distribution: any row vector
mu of total mass one decomposes as unif+v with sum(v)=0, and

    mu P_t=unif+t v.

Equality with mu implies (1-t)v=0, hence v=0. Nevertheless different
t give different kernels. Since Pi^2=Pi and Pi(I-Pi)=0,

    P_t^n=Pi+t^n(I-Pi).                             (15)

For a real, nonzero, zero-mean test f and the uniform stationary process,

    E[f(X_0) f(X_n)] = t^n E[f(X_0)^2].             (16)

Indeed P_t^n f=t^n f, and averaging f times this conditional expectation
gives (16). All finite state histories have positive probability for
every t, yet the registered correlations differ. Unique stationarity,
full support and maximal relabeling symmetry therefore do not by
themselves fix this discrete transition law.

On the binary model S_2, the whole process group above is S4. The uniform
average over that group's permutation matrices is Pi: for any input and
output exactly six of the 24 permutations connect them. Thus P_t can
be realized by positive weights on the already admitted transformations,
with an extra weight on the identity. No new state is needed to exhibit
the law freedom. Independent random update choices and the convention
that a complete group transformation is one stochastic step are additional
data; native generator length has not become a physical time unit.

The n in (15)-(16) is a chosen composition count, not a derived physical
time. Some law parameters can become clock conventions under a further
equivalence. No independent physical parameter is counted from this
toy family. Also, positive probability for every finite history is not
positive probability for each individual infinite history. Neither is
a proof that all histories physically happen.

## 8. Literature and what is actually borrowed

Logical reversible copying and reversing it with a retained reference
are standard. Bennett's 2003 notes explicitly discuss addition to an
initially blank register and the inverse subtraction, and distinguish
the full apparatus from selected information-bearing variables. The
relevant passages on PDF pages 1-2 were personally read. The work is
used for that conceptual comparison; no thermodynamic bound or claim
about real apparatus is imported into the elementary proofs above.
[Primary paper](https://arxiv.org/pdf/physics/0210005v2).

The adequate contextual quotient in section 6 is already in the
November 7 audit and is standard recognition theory. Adamek, Milius
and Urbat's section 3, especially Example 33, Definition 36 and Lemma
39, identifies the quotient relative to a given recognizing map. Those
definitions and the surrounding section were personally inspected.
Its categorical generalizations are not assumed here.
[Primary paper](https://arxiv.org/html/1504.02694v2).

The substantive deliverable here is the explicit correspondence between
the candidate meanings, the internal countermodels and the unpaid
physical bridge. It is not new reversible-computing or automata theory.

## 9. Consequence for the physical programme

An extra registering layer is earned when a declared reduction fails
an actual admitted contextual test, as in (8). A different primitive is
earned as a stronger explanation only when it changes the implications
or reduces independent choices. Merely enlarging the ledger or renaming
an unchosen register does neither.

The operational packages admit these alternatives and do not, on their
own, derive binary records, the OA coefficient target, an action or a
state law. This identifies a dependency, not universal impossibility.
The same-action SM3 and gravity work retains its own evidence grades.
No assertion about qualia, physical nonexistence or the universe's
ontological origin follows from these comparison models.

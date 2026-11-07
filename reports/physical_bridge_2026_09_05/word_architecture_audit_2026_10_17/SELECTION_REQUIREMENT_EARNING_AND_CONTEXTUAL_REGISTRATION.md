# Earning a selection requirement through the registering relation

2026-11-07. Owner-requested discussion and analytical research proposal.
Status: author hand reasoning and explicitly scoped literature comparison;
UNREVIEWED, with no scientific implementation, import, collection or execution.
No canonical GENESIS, adopted premise or sealed design is amended here.

## 1. What the recommendation actually means

"Derive the selection requirement" means: identify already justified
premises that imply the proposed selector, or identify a new independently
motivated premise and disclose its cost. It does not mean that a mathematical
theory can start without premises, or that an extra axiom becomes derived
when it is phrased in philosophical language.

A successful reduction has the form A implies S, where A is the named
upstream principle package and S is the selection condition. If the proof
uses an extra B, the result is A and B imply S. The independence and content
of B must then be examined. Writing A as a new sentence equivalent to S
is a characterization, potentially useful, but not an automatic reduction
of assumptions.

An invariant common character in SL2(C), a fixed irreducible sector, a
faithful free carrier, a chosen surface category and a selected finite
quotient are different commitments. The existing proofs remain useful
while we ask which of these commitments the principle actually requires.

## 2. Existing results to reuse before doing new work

- Main GENESIS at `217e37c4f37bd80998f3c3e10cad358023f58114`, sections 1–2:
  PF1–PF3 are postulated; the commutator-trace interpretation is a reading;
  PF2 is not yet derived from PF1; GM1 v1.50/1.51 explicitly retains the
  target, democratic move-extension and fixed-character premises.
- `FOUR_WORDINGS_PROPOSAL_AUDIT.md`, approximately lines 149–159:
  covariance of a domain family does not require a fixed domain at a state
  that itself changes. This is an existing distinction, not a new discovery.
- `FAITHFUL_LIFTED_REGISTER_TOWER.md`: the specified lifted group admits
  a separating, cofinal finite-quotient tower. Its assumptions already
  include F2, the quaternion representation and the enlarged move group.
  Reuse this construction; do not count it as a derivation of those inputs.
- `QUATERNION_AND_LEVEL_FIVE_REGISTER_JOIN.md`: two registering modules
  can have a common source without being the same representation. The
  physical joining and state law remain additional duties.
- The successor audit at `5b5bf2218` retains the nonabelian quotient,
  paired-sector and antiunitary alternatives that the fixed-sector
  argument does not exclude.

Targeted text searches for Myhill/Nerode, syntactic monoid and contextual
or operational equivalence found no matches in the selected main/chat1/
explore philosophy, docs, reports and relay trees. That limited search
does not establish absence from the entire corpus. The existing faithful
register and fixed-family analyses above are directly relevant prior work.

## 3. The central distinction: symmetry of law and selection of state

Let a legal transformation g act on structured states x and register data r.
For a change of description, a jointly transported observable may satisfy

    O(gx,gr) = O(x,r).

This is compatible with gx different from x and gr different from r.
Requiring one state or one irreducible character to be fixed by every g
is stronger. If some moves are physical updates rather than description
changes, even the displayed observable equality needs its own justification;
covariance of the law should not be confused with conservation of every
observable during an actual process.

Therefore distinguish: formal word equality, equivalence under a permitted
description/gauge change, and operational indistinguishability. The
registering relation may keep distinctions lost under one quotient; it
does not follow that every formal word distinction is physical.

The research question is whether the principle demands one common fixed
sector, a compatible family, or a particular invariant relational object.
The answer cannot be read off from a theorem that assumed one of them.

## 4. A precise conditional form of minimal registration

Start, for this mathematical illustration, with a specified monoid H of
composable histories, an outcome set O and a registering map R:H->O.
No finiteness, vector space, prime, probability, rank or metric is assumed.
These objects are inputs to the proposition, not structures derived here.

Define

    h ~_R k iff R(u h v) = R(u k v) for every u,v in H.

In words: identify histories only when no admitted surrounding interaction
can distinguish them through this register. Multiple registers can be
handled by requiring this equality for every member of a stated test family.

**Conditional proposition.** This relation is a two-sided congruence.
The quotient H/~_R is a canonical smallest compositional carrier adequate
for the stated registering map, in the quotient-factorization sense.
It is not a theorem about shortest code length, least action, smallest
Hilbert dimension or ontological necessity.

**Hand proof.** Reflexivity, symmetry and transitivity follow from equality
in O. If h~k, then for any p,q,u,v, the two outputs for u(phq)v and
u(pkq)v are equal by applying the definition with contexts up and qv.
Thus multiplication descends. Since the identity contexts show that R is
constant on each class, R factors through the quotient.

If Phi:H->M is any surjective monoid homomorphism and R=r composed with
Phi, then Phi(h)=Phi(k) implies equality of all contextual outputs, by
multiplicativity. Consequently ker(Phi) is contained in ~_R, and
Phi(h) maps consistently and surjectively to [h]_R. Every such adequate
compositional M therefore maps onto H/~_R. This is the exact minimality
claim; a bare state-machine state count is a different construction.

This is established algebraic-recognition machinery, not an OA discovery.
The conventional binary version is syntactic congruence; general
output/category formulations are developed by Adamek, Milius and Urbat,
*Syntactic Monoids in a Category*, sections 1,3–4:
https://arxiv.org/html/1504.02694v2 . I read the relevant definitions and
universal-construction discussion for this comparison; no claim of a full
paper audit or an OA physical identification is made.

For typed processes and concurrent composition, replace this monoid
illustration by an explicitly specified process category and all admitted
sequential/parallel contexts, with any ancillary registering systems
retained. That extension needs its own construction. One-dimensional word
concatenation alone does not derive all physical interactions.

## 5. Why this does not secretly select our desired group

There is an exact countercontrol. Let H be a group and pi:H->G any
surjective group homomorphism. Define a binary register by

    R_pi(h)=1 iff pi(h) is not the identity of G.

Then

    h ~_(R_pi) k iff pi(h)=pi(k).

The forward implication is proved by taking the left context h^-1 and
right context identity: h^-1 h cancels, so h^-1 k must cancel in G as well.
The reverse implication follows by applying pi to every context.
Thus the canonical minimal register carrier is precisely G.

Different choices of pi give different minimal carriers: the trivial
group, abelian quotients, nonabelian nilpotent quotients, finite examples
or the original free group. A nontriviality condition can remove the first,
and a noncommutator-cancellation requirement can remove the abelian ones;
neither argument alone fixes the remaining carrier. For monoid histories,
the same group example works when pi is onto G, since a word mapping to
pi(h)^-1 is an available left context. Actual forward-event legality
must still be specified rather than inferred from a mathematical group.

This standard fact has an explicit primary-literature counterpart:
Ballester-Bolinches, Pin and Soler-Escriva, *Formations of finite monoids
and formal languages: Eilenberg's variety theorem revisited*, section 2.1,
Propositions 2.3 and 2.6–2.7, printed pages 7–8:
https://www.irif.fr/~jep/PDF/Formations.pdf . I read the definitions and
proofs of those propositions personally. That paper assumes finite groups
in its main setting; the above group-case hand proof does not require
finiteness. Its all-contexts quantifier and surjectivity are essential.

**Implication:** canonical minimality after fixing a register does not
derive the register law or the group. A desired group can be encoded in
the supplied register and then recovered canonically. That would repeat
the input-selection problem under another name.

## 6. A direct rank control for the proposed invariance requirement

For each free group F_n, n>=2, use the binary identity/nonidentity register

    R(h)=1 iff h is not the identity in F_n.

Every automorphism preserves this R. Its contextual quotient is the whole
F_n by the preceding argument with pi=id. These systems have nontrivial
commutators and a faithfully distinguishing contextual register at every
n>=2. Hence the requirements 'detect failed cancellation', 'preserve the
registering law under rewording', and 'retain every contextually detectable
distinction' do not by themselves force rank two.

This is not a countermodel to the full OA axiom package, nor to the actual
single common SL2(C)-character theorem. It tests the attempt to obtain
that much stronger fixed-character requirement merely from those broader
informal commitments. Additional selection content must be identified.

The integral Heisenberg quotient gives another relevant check: its identity
register is invariant under automorphisms induced from the free group,
and the quotient still has a nontrivial commutator. This preserves the
distinction between full faithfulness and noncommutativity already raised
in the audit.

## 7. A feasible first investigation and its decision rule

1. **Specify meanings before targets.** Formalize the minimum intended
   meanings of distinction, registering, cancellation, composition and
   persistence. Record which requirements come from the owner's principle,
   which are mathematical definitions, and which are new assumptions.
2. **Separate three selection tasks.** Select the category of possible
   laws/carriers; determine admissible states of one law; determine a
   physical state or distribution. A common fixed character, stationary
   solution and vacuum probability answer different questions.
3. **Test one named earning condition.** Does that minimal package force
   a single fixed irreducible register, rather than a covariant family?
   Does it force complex linearity or rank two? Keep these as questions,
   not specifications containing the desired answer.
4. **Use distinguishing countermodels.** Reuse free ranks, characteristic
   Heisenberg quotients, quaternion modules, conjugate pairs and the actual
   faithful lift tower. State exactly which premises each satisfies.
   Failure of one premise is a scoped result; meeting a weaker subset is
   not a counterexample to the full theory.
5. **Seek a genuine implication or record independence.** A proof from the
   declared package pays the selector duty. Two models satisfying every
   premise but differing on the selector establish its independence within
   that package. A finite search for countermodels cannot prove uniqueness.
6. **Justify any additional principle independently.** A restriction on
   compression, composition, locality or registering must express a clear
   structural/operational requirement and survive alternatives. Selection
   because it yields E8, three generations or familiar constants does not
   earn the requirement. Mere count of axiom sentences is insufficient.

The first milestone is a precise implication/independence verdict for the
fixed-sector requirement, with its assumptions visible. It need not select
a unique universe. A forced family together with derived relational
observables is a possible positive outcome. Physical co-realization,
interaction, probabilities and time still need their own laws.

## 8. Literature comparison that is useful without importing a solution

Chiribella, D'Ariano and Perinotti's *Informational derivation of Quantum
Theory* starts with an operational-probabilistic framework and explicit
postulates. In section II.2, events are equated only when they cannot be
distinguished even with an ancillary system. Sections III.1–III.2 state
distinguishability, compression and the additional purification postulate.
https://arxiv.org/html/1011.6451v3 . I inspected these framework and postulate
sections personally; I have not reviewed every reconstruction proof here.

The methodological relevance is precise: earn a mathematical representation
through clearly stated operational assumptions, including composite tests.
Their postulates are not derived from OA and cannot be borrowed without
pricing them. A reconstruction of finite-dimensional quantum theory would
also leave spacetime, the particle/gauge content and SM3/gravity duties.

## 9. What changes in our work

Use this as an earning audit of selectors, not a replacement of the
physical mission or a declaration that every old result is false.
Preserve the Q8 and parity results, the faithful tower and conditional
physical operator calculations. Reuse them as candidate realizations and
controls while questioning their selection premises upstream.

Current local operator/domain work is useful for checking whether proposed
registrations can support physics. Success in a supplied parent does not
by itself select that parent. This note supplies no empirical prediction,
new execution authorization, observer/qualia derivation, foundational-input
payment, or claim that absolute nothingness is mathematically inconsistent.

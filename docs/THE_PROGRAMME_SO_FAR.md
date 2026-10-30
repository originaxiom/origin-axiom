# The programme so far: what origin-axiom is, from its idea to where it stands

*Written 2026-10-30 and checked line by line against the record at S264 (Review 73): a writer drafted it, three readers
checked every sentence and table row against its source, and main ruled on each of their findings (Appendix B). It
restates the record and adds no claim. Where it and `GENESIS.md` disagree, GENESIS holds (GENESIS, preamble). 0 of 19.*

---

## 0. How to read this document

**In plain words.** This page explains, in order, what the programme starts from, what mathematics it builds, what that
mathematics has and has not delivered about particle physics, and what it is doing now. Every sentence that states a
result carries a pointer in parentheses to where the record states it, with the status the record gives it. Background
explanations of standard mathematics (what a torus is, what a geodesic is) carry the tag *(background)* and no pointer,
because they are not results of the record.

### 0.1 Pointers

| pointer | what it names | where to look |
|---|---|---|
| GENESIS PF1, GM3, SE1, FK14, GAP6 … | an item of the foundations page, with its status | `GENESIS.md` (v1.59, 2026-10-28) |
| GENESIS v1.48 | a dated amendment of GENESIS, marked **[v1.48]** in its text | `GENESIS.md` §10, the version log |
| B1816 | an arc of main, the programme's main working line | `frontier/B1816_*/FINDINGS.md` and `arc_verdict.json` |
| sm:B1516, W46 | an arc or item of the SM seat (a parallel working line on its own branch) | the seat's branch; main's copy, if verified, is cited beside it |
| R57 | an item of the audit lane | the lane's branch |
| P-495 | a row of the point register: one raised point, one disposition | `docs/POINT_REGISTER.md` |
| I-13 | a row of the identification ledger | `docs/IDENTIFICATION_LEDGER.md` |
| row 1478 | a harvest row: a seat's result as main read or verified it | `docs/HARVEST_LEDGER.md` |
| S263 | a landing (one commit of main), with its CHANGELOG entry | `CHANGELOG.md` |

The record is kept by several working seats: main (bare B-numbers), the SM seat (sm:B… arcs and W-items), the web seat
(its relays, harvested as rows) and the audit lane (R-items) (GENESIS §0 [v1.1]; `docs/HARVEST_LEDGER.md`). A seat's
result is "the seat's, unverified on main" until main re-runs or re-derives it; VERIFIED needs main's own code or
derivation, and REPRODUCED means main re-ran the seat's code (TERMINOLOGY, the terms of Review 66). This page keeps those
tags where its sources keep them.

### 0.2 The status words, and whose they are

The record uses several vocabularies. Each belongs to a different question, and this page uses each exactly as its
source does.

| vocabulary | words | what it grades | source |
|---|---|---|---|
| the foundations | DERIVED (proved, proof cited); CONDITIONAL (proved given named premises); POSTULATED (assumed); CHOSEN (a fork settled by choice, the alternative kept); OPEN; plus ADOPTED, CONFIRMED, ANSWERED, RULED BY THE PRINCIPLE for decided forks, and NOT DERIVED for three claims about the state space; a tagged working postulate (an owner's ruling that keeps the item formally OPEN: "given Λ", the cusp's unit); and for FK11 UNEARNED, the identification ledger's word, with UNEARNABLE where a theorem shuts a route (B1604) | each item of the foundations | GENESIS §0, §2, §3, §8 |
| arc verdicts | PROVED, NEGATIVE, OPEN, RETRACTED | one arc's question, as asked and sealed | `frontier/<arc>/arc_verdict.json` |
| claim labels (rule of 2026-10-29) | FORCED (marked "generic" when any comparable object would give it), ADMITTED (allowed among alternatives), CHOSEN (an input), FITTED (a continuous value set by data); for negatives EXCLUDED (within a stated scope, by an argument) against NOT FOUND (a declared search's null) | a claim, with its scope and evidence | `WORKING_RULES.md`, rule of 2026-10-29, item 4 |
| identifications | EARNED (the map is exhibited and acts), REFUTED, UNEARNED (asserted, no map: an open debt) | any claim "X here IS Y there" | `docs/IDENTIFICATION_LEDGER.md` |
| a match with data | PASSED (a rarity screen: the state chosen by a fixed rule, and p < 0.01 with the looks corrected by Bonferroni), REPRODUCED (comparable objects show it at an unremarkable rate, p ≥ 0.01; no credit), FITTED, UNJUDGED. A *look* is one search of a frame against data; looks are counted jointly across seats | a positive compared with a population | `docs/THE_BAR.md`; GENESIS FK9 [v1.56]; `docs/LOOK_LEDGER.md` |
| the word READING | in GENESIS, an interpretation recorded and not derived (PF1's form; "the triplet is the generations" in FK14); for a comparison with data, the grade of a fit that reaches the data only with inputs set by hand or read from the data | the readings of GENESIS FK14; the six mass ratios | GENESIS §1 [v1.1], FK14 [v1.24], [v1.28]; B1726; B1741; `docs/MAINS_PLAN.md` |

Three cautions. First, an arc verdict grades the arc's own question as it was sealed. B1741, B1749 and B1753 are PROVED as
sealed for their questions, while each grades its physics content a READING (each arc's own claim line). Second, FITTED
means two different things: in THE_BAR it grades a carrier found by scanning; in the rule of 2026-10-29 it labels a
continuous value set by data, such as the height of τ (THE_BAR's grade table; WORKING_RULES, rule of 2026-10-29, item 4,
as amended). Third, REPRODUCED also has a second sense in the harvest and review texts: main re-ran a seat's code and
got its output again.

### 0.3 What "0 of 19" means

The Standard Model has nineteen free continuous parameters. The record groups them as follows (`docs/MAINS_PLAN.md`,
"Where the nineteen stand"):

| group | count |
|---|---|
| the six charged-fermion mass ratios (m_c/m_t, m_u/m_t, m_s/m_b, m_d/m_b, m_μ/m_τ, m_e/m_τ; listed in B1720's and B1726's FINDINGS) | 6 |
| the three mass scales (y_t, y_b, y_τ) | 3 |
| the four CKM numbers | 4 |
| the three gauge couplings | 3 |
| the Higgs mass and vev | 2 |
| θ_QCD | 1 |

"0 of 19" says that the programme derives none of them (GENESIS §7: "any Standard-Model parameter (0 of 19)" is among
what is not claimed). Almost every recent landing's entry ends with this count (`CHANGELOG.md`: 36 of its 39 entries
from S226 to S264). "The nine" are the six with the three CKM moduli |V_us|, |V_cb|, |V_ub| (B1726 FINDINGS, cell R5;
TERMINOLOGY, "χ²_six, χ²_nine"). Neutrino masses and mixing are outside the nineteen; §7.6 notes the record's one
relation there.

### 0.4 Provenance

Every verification in the repository is INTERNAL: the owner plus AI assistant seats cross-checking one another.
Nothing here is externally verified or peer-reviewed. "Verified" means recomputed by a second internal pipeline, and
the checkable artifacts are the locks, the gates and the hashed preregistrations (`PROVENANCE.md` §0; `README.md`'s
verification-provenance note).

---

## 1. The idea: the philosophy (motivation, never premises)

**In plain words.** The programme begins with the oldest question, "why is there something rather than nothing?", and
turns it around. Its first philosophy passage argues that "nothing" cannot be defined without becoming something, so the
well-posed question is the negative one: what is not-nothing? The working answer is that existence is a frustrated
cancellation: what is left over when an attempt to cancel everything to nothing cannot finish (`philosophy/P000_what_is_not_nothing.md`;
`GOVERNANCE.md` §1; `README.md`). The philosophy folder is motivation only. Its passages are never premises of a proof,
and nothing in them is a claim (each passage's header; `philosophy/GOVERNANCE.md`).

**The principle, as the foundations state it.** "Existence is what remains when cancelling to nothing cannot complete"
(GENESIS PF1). The same wording goes on to say that the remainder is a description that cannot be exhausted (PF2), and
that the programme reads that description as mathematical structure and asks what it forces (PF3). The owner confirmed
this single wording on 2026-10-03 (GENESIS FK1, CONFIRMED; v1.5). All three faces are POSTULATED (GENESIS §1).

**The passages' main ideas.** Each row below is a philosophy passage, labelled by its own header as motivation, an
interpretation or firewalled, and in no case a claim.

| passage | its idea, in brief |
|---|---|
| P000, what is not-nothing? | Ask the negative question. Its minimal answers form a self-generating family, not one object; a unique seed "would be the suspicious outcome". P000 openly chooses four "premises" of the mathematics it motivates, premises of no proof from P000 (resist the trivial maximally; self-reference with no outside input; a family with m free; the member contingent), and the choice is relocated, not removed. GENESIS §9 places them as the PF1–PF2 bridge, GM4, GM5c and SE1, and they carry GENESIS's statuses. GENESIS adopts the family as "the intended shape" (GENESIS §1). |
| P001, architecture, not furniture | The framework speaks about structure (symmetry, hierarchy, shape) and is silent about specific values, units and real-time evolution; that sort is itself the finding. |
| P002, necessity given premises | Given P000's four chosen premises (premises of the mathematics, of no proof) the metallic family follows (B92), so any necessity is conditional; dropping "given the premises" would smuggle the choice out of sight. |
| P003, dead ends as boundaries | Banking negatives is a position on how the shape of the possible is known: each wall is a boundary discovered. |
| P004, expansion is interaction-born | The growing (hyperbolic) unit is a product of two non-growing moves, a twist and a swap; SL(2,ℤ) is generated by finite-order elements, so expansion cannot be a generator (B120). |
| P005, laws and states | One law holds at every rank, while its geometric realisation lives in two ranks only (B120, B119): a universal grammar, particular sentences. |
| P006, two-headed time | Reversibility read as two directions of time from a central point; a fenced overlay on a generic symplectic fact (B124), not structure. |
| P007, a maximal probe | The object has the form of physics and the content of arithmetic; it is read as a rigid probe of the geometry-to-field-theory correspondence, not a seed of reality (B126). |
| P008, non-cancellation named | Non-cancellation is read as the Fricke–Vogt invariant κ = tr[a, b] ≠ 2; κ = 2 is where the cancellation completes. GENESIS keeps this as PF1's mathematical form, "a reading, not a derivation" (GENESIS §1 [v1.1]). |
| P009, monadic closure | A proposed synthesis: the early walls reduce to about three structural facts of a single seed, not seven independent theorems. |
| P010, the category root | A consolidation of why a moduli space of flat connections parametrises but does not select; its structural readings are marked POSTULATED in the passage. |
| P011, generative and actualising dynamics | Generative unfolding is internal; selecting one asymmetric outcome needs more than a symmetric dynamics (Curie's principle, as applied there). |
| P012, the seam and selection | Corrects P011 twice: the wall sits at the closure (Dehn filling), and the closings are selective for the object's own structure and a catalogue for Standard-Model values (B286–B296); and Curie's principle is not the reason, since it has the spontaneous-breaking loophole: the sign is external because no symmetry-breaking mechanism is established. |
| P013, the structural theorem is Galois | The object's discrete invariants come as Galois orbits, read as the mechanism behind "form, not values". |
| P014, the aware decision | A firewalled cosmogony: self-reference, symmetry breaking and the surviving bit, each tagged [MATH], [LEAP] or [NEG]; nothing in it is a claim (its header). |
| P015, the bootstrap and the three | Read as the minimal new self-double (the one reading P015 leaves as a commitment), self-reference gives a golden object of contracting dimension 3; the passage itself refuses to read that 3 as physical space (B515–B517). |
| P019, the genesis as an axiom chain | The owner's spoken chain (nothing, description, comparison, shadow, Fibonacci, the knot) written as labelled axioms and theorems; GENESIS calls it "the words route", and its "to a unique object" is superseded by the generated state space (P019 header). |

**These passages are dated.** Several state positions the later record revised. GENESIS scopes the record's
value-negatives as theorems about flat moduli that "bound the frame, not physics" (GENESIS GAP6 [v1.11]–[v1.12]), and the
owner's ruling of 2026-10-24 re-typed the observer: every dimensionless value is the interaction's to produce, the
observer supplies a unit and an orientation, and every identification is a counted input (GENESIS §7 [v1.55]; P-372;
B1750; WORKING_RULES' currency note). Read each passage with those scopes.

---

## 2. The principle and the grammar: what a description is made of

**In plain words.** To make the principle computable, the programme fixes a small "grammar": a description is a pair of
whole-number counts (two records), and the elementary updates are two moves, L and R, each of which adds one count to the
other (a unit shear; *background*). A description is then a word in L and R. The words act on the surface of a doughnut with one point removed (a
once-punctured torus), and that turns each word into a three-dimensional shape. Each rule of the grammar has a status:
most are assumed, one was adopted by a ruling, one was chosen, one stays open (GENESIS §2).

**The principle's three faces** (GENESIS §1):

| ID | face | status |
|---|---|---|
| PF1 | what exists: the remainder of a cancellation that cannot complete | POSTULATED |
| PF2 | the form the remainder takes: an inexhaustible description | POSTULATED |
| PF3 | the method: read the description as mathematical structure and ask what it forces | POSTULATED |

PF2 does not follow from PF1 by any derivation in the record (GENESIS §1). PF1's mathematical form, κ = tr[a, b] ≠ 2 for
the two letters, is a reading; κ names two different quantities in the record, and every use says which (GENESIS §1
[v1.1]; ERROR_LEDGER E72).

**The conventions** (GENESIS §2): L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]] (the swap of the two records).
Then LR = [[2,1],[1,1]] has trace 3, and the golden matrix LP = [[1,1],[1,0]] satisfies (LP)² = LR.

**The grammar** (GENESIS §2):

| ID | the rule, in plain words | status | notes |
|---|---|---|---|
| GM1 | two records: updates act on a pair of integer counts, ℤ² | POSTULATED, in an equivalent form [v1.50] | A non-trivial common character in SL(2, ℂ) fixed by every move exists exactly when the number of records is two (the rank-two target is itself an input; higher ranks are open, P-209), so that input characterises two records rather than deriving them (B1677, B1679, B1682; GENESIS GM1 [v1.49]–[v1.51]). |
| GM2 | the elementary updates are the unit shears L and R; descriptions are words in them | POSTULATED | Every hyperbolic class of SL(2,ℤ) is ± a cyclic word in L and R using both letters (GENESIS GM2; sm:B1516 C9, the seat's check to entries 5; the general statement is classical). |
| GM3 | aperiodicity: the description never repeats, so the monodromy is hyperbolic | POSTULATED (cheap) | every periodic alternative is degenerate (B749 F2) |
| GM4 | the carrier: words act as mapping classes of the once-punctured torus | POSTULATED, the puncture CONDITIONAL | faithful word realisation and the surface category stay premises (R57; GENESIS GM4) |
| GM5a | updates are reversible (GL(2,ℤ)) | POSTULATED | UNIQUENESS A2 |
| GM5b | inverse moves (pull-backs) are legal | ADOPTED [v1.48] | The owner's ruling of 2026-10-16, made by the math (B1662). With it the sign −I = (L⁻¹R)³ is generated, which answers fork FK4. |
| GM5c | the record swap P is a legal move | OPEN | The owner's ruling of 2026-10-08: even ticks are observed; the swap is part of the act but not a symmetry of what is observed (GENESIS GM5c [v1.33]). |
| GM5d | counts are non-negative (positivity) | CHOSEN | Re-read at v1.48 as the choice of side of a mirror, a selection rather than an exclusion (GENESIS GM5d [v1.48]). |

**Two routes, one construction.** The *words route* runs: aperiodic, hence Sturmian (Morse–Hedlund); the golden slope
(Hurwitz); the golden matrix LP on the once-punctured torus, whose bundle is the Gieseking manifold m000; its square LR by
orientation. The *records route* runs through the uniqueness theorem's axioms to LR. They are one construction in two
presentations (B1323), and neither derives its axioms from anything weaker (GENESIS §4; B1422). Since v1.49 the
principle's form is the whole family of Sturmian wordings, of which the rule a → ab, b → a is the smallest instance,
selected by a criterion and not forced (GENESIS §4 [v1.49]; B1676).

---

## 3. What the grammar generates: states, threads, the weave, the root, the arena

**In plain words.** Every allowed word builds a three-dimensional space: take the punctured torus, let the word's matrix
act on it, and glue the two ends of a thickened copy together with that action (a mapping torus) *(background)*. Each such
space carries a rigid geometry of constant negative curvature (*background*; GENESIS §3: "a hyperbolic 3-manifold with one
cusp").
The programme calls each allowed object a *thread*, and the joint action of all the moves on all of them together *the
weave*. One thread is singled out by stated selectors as *the root*: the figure-eight knot complement, m004
(`docs/THE_WEAVE.md`; GENESIS §4).

### 3.1 The generated state space

A *state* is a signed cyclic word: a primitive word w in L and R using both letters, taken up to rotation and the L↔R
swap, with a sign ε = ±1. It is realised as the once-punctured-torus bundle with monodromy εw (GENESIS §3).

- **Census** (DERIVED): 758 states at word lengths 2 to 12, realising 536 distinct manifolds, since a word and its
  reverse give one manifold (GENESIS §3; sm:B1516, sm:B1517, re-derived on main in B1454 and B1456).
- **Levels**: the n-fold cyclic cover of a state has monodromy (εw)ⁿ (GENESIS §3).
- The five claims GENESIS makes about the state space, with their statuses (three of them NOT DERIVED):

| claim about the state space X_gen | status (GENESIS §3) |
|---|---|
| every legal state belongs to it | DERIVED, at the level of definition (sm:B1384, the seat's, unverified on main) |
| every legal state occurs in one history | NOT DERIVED |
| all legal states are physically realised together | NOT DERIVED |
| some arrow of X_gen is physical time | NOT DERIVED |
| a rule selects which state is physical | OPEN (fork FK9) |

Which set "the family" names was ruled by the principle: it is the word states X_gen. m004's commensurability class and
B1186's 112 are named lists drawn by an outside relation (GENESIS FK13, RULED BY THE PRINCIPLE; B1480).

### 3.2 Threads and the weave

- **A thread** is one object the principle allows (m000, m003, m004, +LLLR and so on): one closed path of the moves
  through the shared fibre, the two records (`docs/THE_WEAVE.md`; TERMINOLOGY). Classically, threads are the closed
  geodesics of the modular surface, the "modular knots" (TERMINOLOGY, the referee lane's concordance).
- **The weave** is the joint action of every allowed move on the two records, and everything that joint action forces
  (`docs/THE_WEAVE.md`; GENESIS §0 [v1.24]). It is the owner's rule, stated as "interaction between objects in relationship
  should produce reality, not single objects alone" (`docs/THE_WEAVE.md`, opening).
- **The test before any arc: weave or thread?** A weave result takes every thread under a rule stated in advance, is
  defined by the joint action, and claims about all threads at once. Anything read on one thread or its covers is a thread
  result and is labelled so in its verdict file (WORKING_RULES, THE WEAVE; `docs/THE_WEAVE.md`). "The object" (m004), "the
  family" and "the root" are thread words (`docs/THE_WEAVE.md`, "Words that pulled the work off course").
- The owner's standing rule, never freeze the weave: a "free" found on one frozen piece (one fibre, one τ, the field held
  fixed) bounds that piece, not the interacting weave of threads and field (GENESIS FK9 [v1.46]; `docs/INDEX.md`). An
  input such as the lepton factor c is never set, in either direction (P-488).

**The weave's first facts** (the SM seat's W1–W4, verified on main at B1600: W1–W3 by main's own code, W4 by
representation theory; PROVED; `docs/THE_WEAVE.md`):

| item | what it says |
|---|---|
| W1, the three | The two records have exactly three non-zero parities. L, R and the swap each fix a different one (the sign fixes all three); any two of them together permute all three in every way (S₃), so the three belongs to no single move. |
| W2, the common point | With the puncture parabolic (commutator trace −2), the only point of the fibre's characters fixed by every move is the quaternion point a ↦ i, b ↦ j; the only other common fixed point on any level is the trivial representation, at tr[a, b] = +2. |
| W3 | Every thread of odd trace receives from the common point the binary tetrahedral group 2T = SL(2, 𝔽₃), with A₄ below it (checked on all 54 odd-trace words to length six). |
| W4, the triplet | The fibre carries one line per non-zero parity; every odd-trace thread acts on the three lines as one irreducible A₄ triplet. |
| WM2 | On every odd-trace thread to length eight (16 of 16) the common point is the thread's own geometry seen modulo a prime of norm three (B1601, PROVED to length eight, a weave result; the general statement open). |

### 3.3 The root and its selectors

**In plain words.** Among the states the grammar generates, the programme picks out one by two stated selectors. The
first asks for a space whose basic loop count has no finite "torsion" part; among the orientable states exactly one
class passes, the figure-eight knot complement, and its one-sided half, the Gieseking manifold, passes too if the record
swap is a legal move (GM5c, OPEN). The second takes the orientable one. The first is assumed and the second is a choice,
and the record says so.

| ID | item | status (GENESIS §4) |
|---|---|---|
| SE1 | selection criterion: the root's first homology is torsion-free | POSTULATED |
| T-ROOT | what SE1 selects: for a hyperbolic once-punctured-torus bundle, H₁ is torsion-free exactly for the class of LR (trace 3: m004) and the class of LP (det −1: the Gieseking manifold m000) | DERIVED |
| SE2 | of the two, take the orientable one, m004 | CHOSEN (the most fragile link; fork FK2) |

- **The root.** Given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement (Thurston; Riley). Each of
  the four inputs is needed; minimality, positivity, the unit-shear generation and the order of the letters are not
  (GENESIS §4, citing sm:B1516 C8).
- **The genesis theorem, A = LR.** On the records route, the uniqueness theorem's axioms force the monodromy A = LR =
  [[2,1],[1,1]] up to the order LR or RL. The page calls itself a conditional result (`docs/UNIQUENESS_THEOREM.md`); GENESIS
  calls the forcing over-determined, a consistency demonstration rather than a search (GENESIS §4; B1422).
- **What the root is, as structure.** SE1 says the root's fibre has no non-trivial character fixed by its monodromy; GENESIS
  calls the root "the architecture's origin of coordinates, not its physical centre", and its link to PF1 an
  interpretation, not a derivation (GENESIS §4).
- **Provenance, recorded.** The figure-eight was first named in a probe on 22 May 2026 and the axioms were committed on
  28 May: the object preceded the axioms. So the genesis is "a conditional reconstruction of a chosen sector", and "not
  a derivation of m004 from nothing" (GENESIS §4; B1422).
- **Classical names** (TERMINOLOGY, the concordance): LR is the Cohn matrix of the golden ratio and the monodromy of the
  figure-eight; the rule a → ab, b → a is the Fibonacci substitution.

### 3.4 The arena

Under GM5b the order-6 move L⁻¹R is reached, and in the SM seat's reading (P-178, not adopted) SE1's two solutions are
the root (trace 3, the motion) and *the arena* (trace 1: the trefoil's complement, SL(2, ℝ)/SL(2, ℤ), whose geodesic
flow's closed orbits are the threads). GENESIS records this as "a reading recorded, the classical facts cited, nothing
derived from it" (GENESIS §4 [v1.48]; P-178; TERMINOLOGY, "the arena").

### 3.5 What is forced and what is chosen at this layer

| item | label or status | source |
|---|---|---|
| the principle PF1–PF3 | POSTULATED | GENESIS §1 |
| the grammar GM1–GM5a | POSTULATED (GM1 in an equivalent form; GM4's puncture CONDITIONAL) | GENESIS §2 |
| inverse moves GM5b | ADOPTED | GENESIS v1.48; B1662 |
| the swap GM5c | OPEN | GENESIS §2 |
| positivity GM5d | CHOSEN | GENESIS §2 |
| the census of states | DERIVED | GENESIS §3 |
| torsion-free selects m004 and m000 (T-ROOT) | DERIVED | GENESIS §4 |
| the criterion SE1 | POSTULATED | GENESIS §4 |
| orientation SE2 | CHOSEN | GENESIS §4 |
| selection of a physical state | OPEN (FK9) | GENESIS §3, §8 |
| the weave's three parities and the common point (W1–W4) | PROVED on main | B1600 |

---

## 4. Frames: how geometry is read as physics

**In plain words.** Geometry does not come labelled with particle names. To compare it with physics, the programme
uses *frames*: rules that turn a geometric object, plus stated extra data, into particle counts or numbers. A frame is a
hypothesis. None is derived from the principle. Every identification of a geometric quantity with a physical one that an
arc uses is meant to get a row in a ledger, as earned, refuted or unearned (WORKING_RULES, the identification rule); on
2026-10-30 not all do (P-516: the twelve arcs B1806–B1817 declared none, and B1812's identification has no row yet). The
five identification rows on which the current frame's six mass ratios lean (I-13, I-23, I-31, I-32, I-33) are all
unearned (GENESIS §5; THE_CHAIN_STATUS currency row 8; §4.4 below).

### 4.1 The frames in the foundations

GENESIS §5: "None is derived from §1–§4", and the transport of any frame to physics (identification I-26) is UNEARNED.
A count in one frame on one state is mathematics about that frame and that state until the dictionary is derived
(WORKING_RULES, rule of 2026-10-02, item 4; GENESIS GAP1).

| ID | frame | what it computes | source |
|---|---|---|---|
| F-MC | McKay cascade | the root's trace field ℚ(√−3) has one ramified prime, giving π₁ → 2T; McKay gives E₆; the fused cascade ends at su(3) ⊕ su(2) ⊕ u(1)³, with the global form [SU(3)×SU(2)×U(1)]/ℤ₆ and the hypercharge direction; run on the root only | GENESIS §5; B248, B266, B862–B864 |
| F-CI | class index | main's index I = n(V) − n(V*) on non-split doublet modules in the E₆/27 frame | GENESIS §5; B1297, B1418–B1451 |
| F-HE | harmonic E₈ | E₈ ⊃ SU(5) × SU(5)′ on a harmonic projective vacuum | GENESIS §5; the SM seat and the audit lane |
| F-FC | free cusp | bulk matter with the Standard Model unbroken; a chiral count needs a free cusp | GENESIS §5; the SM seat |
| F-AP | G₂ apex | matter at cone points of a G₂ space over the cusps | GENESIS §5; the SM seat |

The frames disagree on the same objects, so a result is a statement about a frame applied to an object, "never about the
architecture as such" (GENESIS §5).

### 4.2 The frames of the current work

The census of 2026-10-29 names four frames by new labels, distinct from GENESIS's (B1809 §4, PROVED as a census; its
"nothing on record fixes" and "nothing on record selects" clauses rest on the referees' sweeps, not on a theorem; FR-DYN
below Im τ = 1.2 on the slope-2/5 classes not checked):

| frame | what it is | what it leaves free |
|---|---|---|
| FR-FIB | B1656's flat fibre frame, with B1667's canonical end: the frame in which the six mass ratios are computed | τ and a section's coefficients (continuous); the weight class, a shared or per-sector section, h, the line, the reading, c (discrete); h₀ (a continuous datum set by hand, P-489) |
| FR-FLUX | the flux frames (B1800, B1804) | a curve (split); the flux integers (holomorphic) |
| FR-G2Q | Witten's G₂ frame over a filling m004(p/q) (B1801–B1805) | the G₂ moduli and the volume; p/q, the Wilson line, the singularity type, the flux integers |
| FR-DYN | the one-loop potentials | Im τ on the computed ranges |

B1809's statement (S2): for every discrete choice on record, each of the four frames keeps either a continuous datum
nothing on record fixes or an infinite discrete menu nothing on record selects.

**FR-FIB in plain words.** The weave's matter triplet T and its zero modes live on the shared punctured-torus fibre (W4;
I-31). The fibre has a shape τ, a
point of the upper half-plane (*background*: the shapes of a torus form the modular surface). Couplings are modular forms
of τ (TERMINOLOGY, "the ruled branch"). A flat "line" w = ατ + b of finite order N twists each sector by its hypercharge
(TERMINOLOGY, "a line's order"; I-32). A Higgs is a direction in a three-dimensional multiplicity space (TERMINOLOGY, "the
multiplicity space M"). The Higgs used in most comparisons, ∂R (written DR in the arcs), carries one unit of end data at
the cusp (TERMINOLOGY, "the end-data Higgs"; B1697, B1700). The fibre's puncture is a cusp with canonical horocycles,
which fix the end radius as a function of τ (B1667, PROVED as sealed: a census over 54 grid points, reach class). A
coupling matrix's singular values are read as masses (I-33). The height Im τ of the fibre's shape is called its depth
(*background*: Im τ is the imaginary part of τ). Three more discrete inputs recur below:
- **the reading**: which sectors see the Higgs S and which its conjugate S̃; the record's choice is S̃ for the up quarks
  and S for the down quarks and leptons, as the Standard Model's H̃ and H (TERMINOLOGY, "the Standard Model's reading",
  "the readings S, S̃, S*");
- **the horocycle**: which of B1667's two canonical end radii, L_max or L₂, is used (MAINS_PLAN; THE_CHAIN_STATUS currency
  row 8);
- **c, the lepton factor**: a factor set on the leptons' mass ratios (§7.4).

FR-FIB rests on tagged hypotheses, each carried in the hypotheses of the results that use it:

| hypothesis | what it says | status |
|---|---|---|
| "given Λ" | every left-handed field transforms in the weave's triplet T | the owner's tagged working postulate of 2026-10-08 (GENESIS GM5c [v1.33]); I-31 UNEARNED |
| the cusp's unit | one unit of end data at the weave's cusp | a tagged working postulate (GENESIS FK10 [v1.39]); reduced at v1.59 to four links, none derived (B1796) |
| H-cov | the Higgs direction is a vector-valued modular form for the matter's representation | a tagged hypothesis (TERMINOLOGY; B1691) |

### 4.3 Frame cards and chaining backwards

Since 2026-10-29, before an arc builds or uses a frame it writes the frame's card: the continuous configurations, the
discrete choices, the outputs named against the 19, and the conditions built from the object. The null against which any
positive will be measured is fixed on the card before the run. A route is stated as a complete derivation, chained
backwards: space, fields, zero modes, couplings, running, comparison (WORKING_RULES, rule of 2026-10-29, items 1–2;
B1798). The chain written that way, with every link labelled, is now THE_CHAIN_STATUS's currency pass of 2026-10-30
(`docs/THE_CHAIN_STATUS.md`, last section; the web seat's map, adopted at S263, seven labels spot-checked by main).

### 4.4 The identifications

**In plain words.** Saying "this geometric quantity IS that physical one" needs a map that is exhibited and shown to act.
Matching names, orders or numbers is not a connection (WORKING_RULES, the identification rule). WORKING_RULES and the
ledger's preamble state, citing B1225, that the object cannot make such an identification itself: identifying a
structural quantity with a physical one needs a partner outside. B1225's own result is that no symmetry readable off the
object selects within its class. So every unearned identification is an input the programme has not paid for, and the
parameter count is a lower bound until each is earned or priced (WORKING_RULES; IDENTIFICATION_LEDGER preamble).

The ledger holds 36 rows: 8 EARNED, 8 REFUTED, 20 UNEARNED (counted from `docs/IDENTIFICATION_LEDGER.md`; the same 20 of
36 in P-418). Its live price is 4 axioms + 9 irreducible sources = 13 (GENESIS §5 [v1.47]; P-418).

- **EARNED** (map exhibited and acting): among them I-1, 2T ↔ E₆ (McKay is a theorem); I-2, the SL(2,ℤ) action ↔ N=2*
  S-duality; I-3, Vol(m004) = (3√3/2)·L(χ₋₃, 2) (B680); I-19, 3d gravity as the principal spin-2 sector of E₆(ℂ)
  Chern–Simons (B1242).
- **The master identification**, I-13, the listener map u: a dimensionless structural analogue computed in the object,
  read as the physical quantity of that name. UNEARNED. Every physics reading draws on it; the ledger calls it the
  programme's own debt, every other UNEARNED row a local one (IDENTIFICATION_LEDGER, I-13 and "The master
  identification").
- **The UNEARNED rows on the frames' chain:** the five the six lean on (I-13, I-23, I-31, I-32, I-33) and the rows the
  six do not lean on (I-26, I-34, I-35, I-36).

| row | the identification | status |
|---|---|---|
| I-26 | a twisted-cohomology dimension ≡ the number of 4d chiral generations | UNEARNED |
| I-23 | Y ≡ the electromagnetic charge functional | UNEARNED (an instance of I-13) |
| I-31 | the weave's triplet T is the Standard Model's left-handed multiplet, "given Λ" | UNEARNED |
| I-32 | the Standard Model's hypercharges read as the line's twists | UNEARNED (an instance of I-23) |
| I-33 | singular values are masses, U_u†U_d is the CKM matrix | UNEARNED (an instance of I-13) |
| I-34 | the index on the weave's surface, given the cusp's unit, is the number of generations | UNEARNED; the six do not lean on it (P-489) |
| I-35 | the hypercharge sign rule for the reading | UNEARNED (B1790; not adopted) |
| I-36 | a filling m004(p/q) as the GUT 3-cycle of a G₂ compactification | UNEARNED (B1801; not adopted) |

### 4.5 The observer, re-typed

The record once credited "the observer" with every closing the object could not supply: a filling slope, an arrow, a
chirality, a basepoint (B717). The owner's ruling of 2026-10-24 retired that closer as an explanatory move, kept the
*signer* (the observer supplies one unit and one orientation, conventions, not values), and made the *identifier* the
identification ledger (GENESIS §7 [v1.55]; P-372; B1750). Within the object the sign is settled: the object names itself
and cannot sign itself, and the missing sign is one ℤ/2 class, the orientation (GENESIS §7, citing B1183 and B1184,
PROVED). Whether the register that keeps a word's order belongs to the genesis is fork FK12, OPEN (GENESIS §8).

---

## 5. What has been derived: the discrete structure

**In plain words.** What the record has obtained is discrete: groups, counts, signs and exact numbers belonging to the
object. Some of it is specific to this object; much of it would come out of any comparable object, and the record now
marks that "generic" (WORKING_RULES, rule of 2026-10-29, item 4; B1809 §6). Each row gives the status in its source's own
word.

| item | what it says | status, in the source's word | scope | pointer |
|---|---|---|---|---|
| T-ROOT | torsion-free selects exactly m004 and m000 | DERIVED | all once-punctured-torus bundles | GENESIS §4; B197 |
| the root | m004, given GM3, GM4, SE1, SE2 | follows given GM3 and SE1 (POSTULATED), GM4 (POSTULATED, its puncture CONDITIONAL) and SE2 (CHOSEN) | the generated states | GENESIS §4 |
| A = LR | the record axioms force LR up to the order of letters | a conditional result | the positive grid | `docs/UNIQUENESS_THEOREM.md`; GENESIS §4 |
| the census | 758 states, 536 manifolds to length 12 | DERIVED | X_gen to length 12 | GENESIS §3 |
| the count of records | a non-trivial common character exists exactly at two records | GM1 POSTULATED, in an equivalent form | the weave of n records | GENESIS GM1 [v1.50]; B1679, B1682 |
| the three parities, the common point, 2T, the triplet | W1–W4, WM2 | PROVED; WM2 a census law (lemma proved, theorem open) | the three parities and the common point (W1, W2): the weave; 2T and the irreducible A₄ triplet (W3, checked to length six; W4): every odd-trace thread; WM2: odd-trace threads to length eight | B1600; B1601 |
| the sign | a full turn round a balance point negates the records | generated (FK4 ANSWERED) | the grammar with GM5b | GENESIS FK4 [v1.48]; B1662 |
| CP on the weave | the weave's generalized CP is the record swap; CP violation allowed, not forced | PROVED | the weave's group | B1611; GENESIS GM5c [v1.32]–[v1.33] |
| E₆ | from ℚ(√−3) through 2T by McKay | I-1 EARNED (McKay); E₆ itself generic (about one manifold in three; B727 NEGATIVE on "E₆ across faces" as evidence) | F-MC, the root | GENESIS §5; B727; B993; THE_CHAIN_STATUS currency row 6 |
| π₁ ↠ 2T | the root's group maps onto 2T | generic: shared by 7₂, 7₃ and 8₁. B727 had called it the one object-specific atom; the check of 2026-10-29 found that label wrong | knot complements | B1809 §6; WORKING_RULES, rule of 2026-10-29, item 4; B727 |
| the cascade's end (the Standard Model's group, with two extra abelian factors) | the fused cascade ends at su(3) ⊕ su(2) ⊕ u(1)³, with the global form [SU(3)×SU(2)×U(1)]/ℤ₆ and the hypercharge direction (GENESIS F-MC) | PROVED within F-MC, given B860's registerability premise (that the option be registerable by a measurement of the object) and B862's cascade premises, P5 and the fused rule; F-MC is a frame, a hypothesis, and its transport to physics is UNEARNED (I-26) | F-MC | B860; B862; GENESIS §5; THE_CHAIN_STATUS currency row 6 |
| the global form ℤ₆ | [SU(3)×SU(2)×U(1)]/ℤ₆ | PROVED, conditional on the cascade's premises (B862); FORCED, generic, as a property of the algebra (B1221; B1809 §6) | the 27 | B862; B1221 |
| the hypercharge direction | forced by the four anomaly conditions | FORCED, generic, given an SM-shaped 15-plet; FR-FIB does not use it | an SM-shaped 15-plet drawn from the 27 (the anomaly arithmetic re-derived on main); its realisation in the 27's rank-3 abelian sector is the cloud seat's, cited and not re-run on main (B1160); the frame and the SM-shaping are inputs | B1160; B1809 §6; THE_CHAIN_STATUS currency row 6 |
| the hand | which of a pair is left-handed | the records' hand is forced given SE2's sheet, and the sheet is CHOSEN (GENESIS GM5c [v1.31]); which hand the matter carries is not derived (GENESIS FK10 [v1.42]; B1809 §6 lists the hand as not forced; B1796 assumes it) | the weave's surface | GENESIS GM5c [v1.29], [v1.31], [v1.33]; THE_CHAIN_STATUS currency row 6 |
| the arrow | the walk's escape from its start | FORCED, generic; its side CHOSEN; both CONDITIONAL on the walk being the dynamics | GM5b's walk | THE_CHAIN_STATUS currency row 5; B1662; B1815 |
| the geometric holonomy and the (3,1) signature | SL(2, ℂ) = Spin(3,1); H³ as the mass hyperboloid | FORCED, generic (Mostow); physical spacetime UNEARNED; signature as structure not available before an internal space is chosen (B1115) | every hyperbolic 3-manifold | B716's note of 2026-10-29; B428; THE_CHAIN_STATUS currency row 5 |
| gravity | every hyperbolic thread is the space of a flat 4d vacuum (the Milne cone); the object's own 3d Λ = −1 | PROVED (classical facts read on the record); Λ = −1 FORCED; Einstein's equations an input | every thread; the root | B1708; B259; THE_CHAIN_STATUS rows 14 and currency row 5 |
| exact numbers of the root | Vol(m004) = (3√3/2)·L(χ₋₃, 2); J(m004) = 1, the only orientable manifold saturating Jørgensen's inequality (Callahan, cited) | I-3 EARNED; B1345 PROVED; neither is a Standard-Model parameter | the root | B680; B1345; GENESIS GAP6 [v1.12] |
| doublet–triplet topology | Witten's doublet–triplet topology on m004's even fillings | ADMITTED (B1809 §6); B1802 proves the topological prerequisite only, in Witten's G₂ frame; the filling as the GUT 3-cycle is I-36, UNEARNED | the even fillings | B1802; B1809 §6 |
| the global freedom ledger | a retroactive audit of the declared chain: 0.000 retroactive designer bits against a conservative 4.585-bit output floor in declared ambient classes, with 3 declared discrete input bits and flagged soft spots | COMPRESSION (B1028, PROVED, 2026-08-11); the floor's construction is unstressed, and the audit predates the 2026-10-29 "generic" relabelling | the declared chain to the SM skeleton | B1028; `docs/THE_FRAMEWORK.md` |

### 5.1 "Three": what is and is not derived

**In plain words.** The question "did we derive three generations?" has a precise answer on record: the three-fold
*flavour* structure is derived on the weave; three *gauge* generations of chiral matter are not (GENESIS FK14 [v1.28]).

- **DERIVED on the weave**, GENESIS's grade under THE_BAR: "three, alike, chiral under the weave's own group, one per
  parity". On the weave's surface −χ(Aut⁺(F₂); 27) = 3 (not chiral, the module being self-dual); the three holomorphic
  zero modes span the triplet T; the puncture's conditions have odd indices, ±3 with the parity grading (W20–W22,
  verified on main; B1606; GENESIS FK14 [v1.28]).
- **READINGS**: that the triplet is the generations; that holomorphic zero modes are the left-handed matter
  (GENESIS FK14 [v1.28]).
- **The owner's question answered**: "the flavour three is derived, the gauge three is a selection" (GENESIS FK14 [v1.28]).
- **In physics generally**, the number of generations is an index of closed-cycle cohomology obtained by selection, and
  nobody derives three, for the sources surveyed (B1496, PROVED: the physics researched and verified claim by claim).
- **On the record's threads** no state of X_gen carries three generations in either counting frame, by counting ends
  rather than by search (GENESIS GAP2 [v1.15]; B1487). No twisted Euler characteristic on a thread or a cover carries the
  physical index's shape, so within F-HE and F-CI no count of flat-module cohomology on a thread or a cover earns FK11;
  indices of other kinds (η-invariants, L²) are not addressed (B1604, PROVED; GENESIS FK11 [v1.27], [v1.46]).
- **Given Λ and the cusp's unit**, the four-dimensional index on the weave's surface M₁,₂ is ±3 at the natural puncture
  conditions (±1 at the middle ones) (W45, W46; verified on main, GENESIS FK11 [v1.51], citing B1632 and B1641; GENESIS
  FK10 [v1.39], [v1.43]). Reading it as the generation count is I-34, UNEARNED, and FR-FIB's six do not use it (P-489).

### 5.2 What the record says survives, counted

Of 229 PROVED physics positives, 75% are discrete and 15% are exact numbers of the object, none equal to a measured value;
31 of the 32 arcs that removed an input removed a discrete one (`docs/THE_PATTERN_MEDITATION_3.md` Part I, from its
report A).

---

## 6. What has been excluded: the major negatives and what would reopen each

**In plain words.** A negative is a result: it marks where the structure does not go (P003; WORKING_RULES item 12). Each
negative holds only as far as its stated scope: a frame, an object, a reach, and hypotheses (GENESIS §6; WORKING_RULES,
rule of 2026-10-02, item 3). Each negative arc is meant to be routed in the kill graph with a *hatch*, the condition
that would reopen it; the graph has 856 entries, as `docs/views/CLOSED_DOORS.md`
states, and 510 of them carry none (`frontier/B738_pathfinder_compiler/kill_graph.json`). Since 2026-10-29 a negative says whether it is EXCLUDED, within a
scope by an argument, or NOT FOUND, a declared search's null (WORKING_RULES, rule of 2026-10-29, item 4). Main audited
its own negatives on 2026-10-15 and found the over-reading in wording and propagation, not in the instruments (B1655,
PROVED).

The table selects the negatives that bound the present picture. Hatches are paraphrased from the kill graph's entries;
where an arc is not routed there, the hatch comes from the source named in the cell.

| negative (arc, verdict) | scope | what would reopen it |
|---|---|---|
| **The object cannot sign itself** (B760, NEGATIVE; with B1183, B1184 PROVED) | no object-native operation signs the θ-odd sector | none given in the kill graph; GENESIS FK12 asks for a partner that supplies the sign as a relation (B1327, OPEN) |
| **The direct dictionary CS(m004) = θ_QCD is refuted on type** (B813, NEGATIVE; I-4 REFUTED; the type-level link I-18 stays UNEARNED) | refuted on type: a fixed invariant cannot fill a coefficient slot | none given |
| **No parameter-free dynamical law at the archimedean place** (B1157, NEGATIVE) | the object's infinity-place; a structural rhyme | the cusped complex-orthogonal torsion machinery, and even then generic spectral geometry |
| **No symmetry readable off the object selects within its class** (B1225, PROVED) | every symmetry readable off the object | not routed; the record names a selection principle as missing (GENESIS FK9 [v1.45]; P-139) |
| **The root's harmonic vacua carry no count** (B1455, NEGATIVE) | F-HE on m004's harmonic family at level one | a reductive point no count-odd symmetry fixes; a source or end condition; selection by a relation |
| **No twisted Euler characteristic on a cusped 3-manifold or cover carries the physical index's shape** (B1604, PROVED) | every twisted Euler characteristic on a cusped 3-manifold or cover | an even-dimensional object the weave forces, carrying a non-flat bundle whose index is the count (GENESIS FK11 [v1.27]) |
| **No state of X_gen carries three generations in F-HE or F-CI, by counting ends** (B1487, PROVED given the SM seat's floor, checked on 390 readings and partly re-derived on main; GENESIS GAP2 [v1.15], [v1.52]) | F-HE and F-CI on the generated states | a move that adds punctures, or a frame whose count is not a count of ends (GENESIS FK14) |
| **No residual symmetry of the weave's group reduces the 13 flavour parameters to a family that reaches the CKM** (B1620, PROVED: "reduces none" means none compatible with the data; frame: all of the weave's group is flavour; the PMNS reduces to two under T̄ ⊗ T and T ⊗ T) | every subgroup of the weave's group, three tensors | values need a forced modulus, dynamics or end data (GENESIS GM5c [v1.33]) |
| **Neutrino masses as residual vacua** (B1616, NEGATIVE) | Majorana vacua fixed by four chosen elements (RL, L, R, RRL) of the weave's group, in Sym² T, given Λ; not every subgroup | masses from a forced modulus, dynamics or end data; a seesaw outside the triplet |
| **No hierarchy found at τ = ω on the ruled branch** (B1617 NEGATIVE as sealed; B1618 PROVED where the inner automorphisms act; retired as "no hierarchy found", GENESIS GM5c [v1.46]) | the modulus at ω; the near-ω regime uncomputed | Yukawas as modular forms of weight k; a vacuum near ω (GENESIS GM5c [v1.35], [v1.46]) |
| **Nothing the principle forces visits the cusp** (B1629, NEGATIVE) | the tick, the clock, the uniform measure on threads | a boundary condition from outside the principle's dynamics: a physical end mechanism, or a postulate (the owner then tagged the cusp's unit as a working postulate, GENESIS FK10 [v1.39]) |
| **The record's lines do not give the six specifically** (B1698, B1711, B1712, B1713, NEGATIVE) | every flat line of order 1–12 with the end-data Higgs, Re τ in {0, ½} and Im τ on a grid 1.5–3.5; best factors 2.37 and 2.33, with 22% and 15% of random hierarchies as good (`docs/THE_WEAVE.md`) | a line a principle selects for a reason other than its order; orders above 12; τ off the two CP lines; another Higgs section |
| **A thread fixes the point, but not specifically** (B1720, NEGATIVE) | τ at the apex of each of 121 primitive classes of length 2–9 (apex Im τ ≤ 4), on the lines its monodromy fixes; best within a factor 1.80, 1.65% of random as good against a 1% bar | a measure over threads that singles out the best class; longer threads; other Higgs sections |
| **The record's measures do not pick the thread** (B1722, NEGATIVE) | the uniform word measure and the action weight (c = 6), on B1720's census of 121 threads | a measure weighting high-run threads, a dynamics, or a principle beyond a measure |
| **The golden valley is too low** (B1723, NEGATIVE) | the modular-invariant valley through the tick's geodesic; no closer than a factor 147 | a functional whose valley crosses Im τ near 3 |
| **The six are not PASSED** (B1798, NEGATIVE for PASSED) | THE_BAR under the class-choosing null | a data-free derivation of c = 3, which would remove the c-choice from the null, and then the class-choosing grade at a per-test count (counted per decisive cell, m ≈ 51, B1753 fails too) |
| **c = 3 is not derived** (B1789, B1793, B1817, NEGATIVE) | EXCLUDED as an output of FR-FIB as built, NOT FOUND beyond it (THE_CHAIN_STATUS currency row 8); at the cusp, on the 31 equal-exponent slopes of order ≤ 30, the frame's limits are 1, 4, ¼ or a non-integer line constant, and do not move with N_c (controls N_c = 2, 4, 5) | an insertion that sees one leg's integer hypercharge; the B − L Clebsch channels; L250's non-abelian bundle |
| **The reading is not derived** (B1790, NEGATIVE, frame-scoped) | off the mirror lines, EXCLUDED as an output of the frame as built, NOT FOUND beyond it | an antiholomorphic or Hermitian Higgs slot; a non-point coupling; an effective-action selection |
| **Im τ is not found forced** (B1791, NEGATIVE) | NOT FOUND in B1656's frame: special points, cusp shapes, apexes, functionals, the one-loop potential | a principle naming the ρ′ Higgs's Petersson maximum as the vacuum; non-perturbative or flux potentials |
| **The symmetry-fixed configurations miss the six** (B1811, NEGATIVE as sealed) | the four configurations the object's symmetry fixes, with B1810's 13 Higgs directions (the n = 1 window) and one Higgs for all sectors; best χ²_six 4521.5 against 16.75 | a configuration off the symmetry points chosen by a principle; n ≥ 2 directions; two-Higgs pairs; another frame |
| **The Standard Model's one-Higgs reading fails the nine** (B1747, PROVED as a verification) | lines of order ≤ 12 at eight τ and both horocycles in FR-FIB (4 256 rows; re-derived on main on a sample of forty); lowest χ²_nine 1 045.4 against 21.67 | not routed; P-377 names a principled second object for the doublets |
| **Three cuts a curve, not a point** (B1808, NEGATIVE) | B1804's holomorphic flux frame | another frame on P-419's card; further discrete data with a principle fixing the second flux |
| **Matter parity from Spin(10)** (B1805, NEGATIVE in Witten's G₂ frame) | flat breakings on the 3-cycle | F-theory matter curves; a Stückelberg U(1)_X; an E₆ meeting point; a symmetry of the G₂ space |
| **The towers meet at loci, fixed by the object, in F-theory's 7-brane frame** (B1812, NEGATIVE as narrowed at Review 73) | LR lies in the class of the twelve-brane E₁₀ configuration A⁹BCC; the nested E₃ and E₄ pieces (su(3) ⊕ su(2), su(5)) cannot collapse, but the stacks A⁵ ⊂ A⁵BC ⊂ A⁵BCC can (I₅ ⊂ I₁* ⊂ IV*), so the towers can meet; the object fixes the total class, not where the branes sit | a dynamics that selects the brane positions, moving them and τ together (P-466) |
| **The measured six do not decide the clock** (B1814, NEGATIVE as sealed for D2) | B1813's two clocks; power about 19% | decide the clock on the theory side, or a statistic with power |
| **Four-dimensional gravity does not supply the cusp's unit** (B1708, B1710; GENESIS FK10 [v1.53]) | closed elliptic surfaces with a section and only I₁ fibres close in twelves; given the SM seat's reduction to Riemann–Roch on the base (not re-derived on main), the triplet's count is never three | not routed; FK10 keeps the unit as a tagged postulate |
| **A TM2 lepton reading is falsified** (B1756, PROVED: P10′ FALSIFIED at 5.82σ) | the T ⊗ T tensor in the frame where the whole group is flavour | none on record: a falsification by the register's fixed wording, not a null search; it removes the T ⊗ T lepton reduction in that frame, not the weave (`docs/FALSIFIER_REGISTER.md`; B1756) |

---

## 7. The values: what the frames reach, and why that is not a derivation

**In plain words.** In one frame, FR-FIB, the programme reaches the six charged-fermion mass ratios within the record's
bar (χ²_six 2.74 against 16.75). It does so only after choosing several inputs by hand or by looking at the data, and
spending about as much freedom as the six numbers carry. The record grades that a READING: it compresses the six, it
does not derive them. The quark mixing is either missed by the rigid versions of the frame or fitted by the free ones
without being specific. Nothing touches the mass scales, the gauge couplings, the Higgs sector or θ. The count stays
0 of 19 (`docs/THE_FINAL_ATTACK_2026-10-29.md`, its opening and §2; `docs/MAINS_PLAN.md`).

### 7.1 Where the nineteen stand

| group | what the frame does | source |
|---|---|---|
| the six charged-fermion mass ratios | reached on one strip, with inputs set by hand: "a READING, ungraded"; not PASSED | MAINS_PLAN; B1798 |
| the three mass scales | not touched | MAINS_PLAN |
| the four CKM numbers | not reached: one Higgs fails (B1747); the free two-doublet fit is not specific (P-377); the named pairs fail (W158) | MAINS_PLAN |
| the three gauge couplings | not in the frame; the one-loop threshold the two-Higgs crossing needs is 27.66, no integer | MAINS_PLAN, citing B1784 |
| the Higgs mass and vev; θ_QCD | not in the frame | MAINS_PLAN |

### 7.2 The six

- **The strip.** In FR-FIB the six's best rows lie on a strip, Im τ 2.96–3.11 with Re τ loose, on the order-10 lines
  (2/5, 1/10) and (2/5, 1/2): specific under B1749's sealed null, not PASSED under B1798's class-choosing null with c
  chosen (TERMINOLOGY, "the strip"; B1749, B1753; B1798).
- **The best rows.** χ²_six 2.74 with one Higgs (B1753, at τ = 0.3333 + 3.0368i on the line (2/5, 1/10)) and 1.19 with two
  Higgs (B1742), against the bar 16.75 (THE_FINAL_ATTACK §2; TERMINOLOGY, "χ²_six").
- **The inputs spent** (MAINS_PLAN, "The six's inputs as they stand", 2026-10-28): Im τ, Re τ and the line's position
  (continuous; the dated note of 2026-10-29, P-489, counts the position within the line's menu of 266 lines instead, as
  the scoreboard does); the slope α = 2/5, the lepton factor c = 3, the reading (three bits), the horocycle (discrete).
  MAINS_PLAN's verdict: "That is a compression of six numbers, not a derivation." The web seat's scoreboard counts, for
  the one-Higgs branch, about 20 bits of discrete choices (15 searched on the data), 2 fitted continuous values, 2
  continuous values set by hand and 2 irreducible identification sources; no input removed. The two-Higgs row's lower
  χ²_six costs 23.79 bits and 3 identification sources, and it carries a relation among the six, D = 9, that the data
  exclude at 14σ (MAINS_PLAN, dated note of 2026-10-29; rows 1478, 1479).
- **Specificity.** Under a null that lets random targets choose their own line class and their own c, as the data did,
  THE_BAR's m·r is 0.035–0.079 for B1753 and 0.034–0.082 for B1749: "the six's specificity rests on c read from the data"
  (B1798, NEGATIVE for PASSED).
- **The slope.** α = 2/5 is selected by the data, stably out of sample (8 of 160 000 random hierarchies as low on new
  lines), but not PASSED under the class-choosing null; its principle is the measured 3 : 2 ratio of exponents restated, so
  no input is removed (B1786; B1788; MAINS_PLAN step 1).
- **A structural price inside the fit.** On the (2/5, k/10) family the lepton spectrum equals the down spectrum for k
  even with any Higgs, and for k odd with a Higgs with no QI component (as in the two-Higgs row); there, with c = 3, the
  lepton ratios are Georgi–Jarlskog's by construction and the six are four numbers (B1742; the record's one-Higgs DR
  breaks the identity at odd k, B1789).
- **Why it is not a derivation, in the record's own diagnosis.** The object is a finite datum; it can fix a continuous
  number only as one of its own invariants. The frames add continuous moduli the object does not fix, so they can fit and
  cannot derive (`docs/THE_PATTERN_MEDITATION_3.md` Part II). Since B1600 the record has patched negatives by adding about
  13 free choices against 2 partial removals (same page, Part I.3; P-418).

### 7.3 The CKM

The quark mixing is the test the six's address has not passed. Against the nine (the six with |V_us|, |V_cb|, |V_ub|;
bar χ²_nine 21.67, TERMINOLOGY), one Higgs read the Standard Model's way is excluded in this frame at the test's points
(B1747). At the six's strip a rigid Higgs reaches χ²_nine 47 at best; two free doublets reach the bar with 8 real
parameters for 9 numbers, and 66% of random CKMs reach it as well (P-377; THE_FINAL_ATTACK §2). THE_FINAL_ATTACK's diagnosis: every frame on record is "rigid and wrong" or "free and
unspecific" (THE_FINAL_ATTACK §2).

### 7.4 The lepton factor c

The factor 3 between the leptons' and the down quarks' second-to-third mass ratios (the Georgi–Jarlskog factor) is set
by hand (TERMINOLOGY, "the two ingredients"; B1725). It is not made by FR-FIB as built (B1789), not by a curvature that
re-weights the channels (B1793), and not by the frame's own twists at the cusp: on the equal-exponent slopes of order
≤ 30 the recurring integer is 4 (and ¼) at each colour count tested, N_c = 2 to 5 (B1817, as scoped). It stays one
discrete input, never set in either direction: setting c = 1 is a choice exactly as c = 3 is (P-488). An unexplained
regularity of the cusp constants, R₂(1/8) = 4·R₂(3/8), is registered for derivation (P-512).

### 7.5 The depth of τ

Im τ ≈ 3 is FITTED (THE_FINAL_ATTACK §2; THE_CHAIN_STATUS currency row 9). It is NOT FOUND forced in B1656's frame: the
special points, cusp shapes, thread apexes and natural functionals are closed, and the one-loop potential trades Im τ for a
free ratio (B1791; MAINS_PLAN step 4). Under either frame-native measure on τ the measured depth is ordinary, a 20% tail
under Weil–Petersson and 32% under hyperbolic area (B1816; THE_FINAL_ATTACK §2).

### 7.6 Outside the nineteen: the lepton mixing relation

The weave's flavour group fixes no mixing angle as a parameter-free number; it allows one viable one-parameter relation for
the leptons, TM1, a READING resting on Λ, a frame and a tensor (B1612; GENESIS GM5c [v1.36]). It is registered as falsifier
P10: sin²θ₁₂ = 1 − 2/(3 cos²θ₁₃) ≈ 0.318, standing at 2.28σ on JUNO's second release, below its 3σ line. Its sibling P10′
(TM2) is FALSIFIED at 5.82σ (B1756; `docs/FALSIFIER_REGISTER.md`).

**0 of 19.**

---

## 8. The clock, the weave's measure, and the owner's plenitude

**In plain words.** Left alone, the weave does not choose one world. It spreads over many possible values of τ, and how it
spreads depends on how its threads are counted: one move at a time, or by geometric length. That choice is "the clock".
One end of the dial is the principle followed literally, which gives no mass hierarchy; the other end is a critical
point where, in the fibre frame and given its end data (a reading, conditional on H-cov: B1813), hierarchies as deep as
ours are ordinary. Nothing on record turns the dial. Separately, the owner proposed that every world the framework
allows is real; then the questions become whether our world is among them, what the framework forbids, and only then
whether ours is typical (B1813; `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` §0; P-485).

### 8.1 The weave's own measure (B1813, PROVED)

Left unforced, the threads produce a definite measure on τ for each counting rule, and the rule is a continuum (B1813):
- counted move by move, the measure is Minkowski's (the maximal-entropy measure of the Farey coding, the question-mark
  measure, lifted to the geodesic flow), and it keeps out of the cusp: P(Im τ > 3) ≈ 0.0346;
- counted by geometric length, it approaches hyperbolic area, the volume of the Teichmüller metric (0.315 at trace ≤ 400,
  against 0.318; TERMINOLOGY, "the clocks");
- weighting words by e^(−s·ℓ) interpolates, and the cusp tail's rate falls to zero at the Farey map's phase transition,
  s = 1, where area lives (B852).

The counting rule is CHOSEN (B1813's labels).

| position on the dial | s | length per move | the history | the world (a reading, conditional on H-cov and end data) |
|---|---|---|---|---|
| the principle's golden path | s → −∞ | 2 log φ = 0.9624, the maximum over all words | one word, (LR)ⁿ | no hierarchy |
| fair-coin counting | s = 0 | 0.7924 | fair coins over the letters | mild hierarchies |
| the critical point | s = 1 | tends to 0 | a generic number's digits | deep hierarchies ordinary |

(`docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` §3.1, a dated snapshot; the golden path's figure re-derived on main.)
"Nothing on record turns the dial" (same page, §0): GENESIS marks physical time NOT DERIVED (§3).

### 8.2 What the mathematics settled about the clock

- **The walk model's exit law is Minkowski's, exactly.** The walk model of B1662/B1663 has endpoint law ν_p = (1−p)·M +
  p·F₊M at every pull-back strength p: Minkowski's measure and its mirror, singular to area; with τ placed by arclength
  along the ray (CHOSEN), its averages are the move clock's. The object's discrete symmetry cannot decide the clock; the
  frame that computes the masses never sees word length; nothing on record generates a continuous horocycle action; the
  record's established results are consistent with both clocks. The clock stays CHOSEN (B1815, PROVED). If the walk is
  the programme's dynamics, area is EXCLUDED as its exit law, scoped to that walk model and conditional on a ruling the
  record owes (THE_CHAIN_STATUS currency row 3; P-439).
- **A third, frame-native clock.** Weil–Petersson volume is the measure defined by the fibre's own hyperbolic metric
  (TERMINOLOGY, "the clocks"). The canonical end's accessory parameter is a Weil–Petersson primitive, so this volume
  stands beside hyperbolic area as a clock native to FR-FIB; nothing ranks them, and "no clock studied picks a point"
  (B1816, PROVED).
- **The data cannot decide it.** The measured six do not separate the two clocks, and the test had about 19% power; one
  world carries about one nat about the clock (B1814, NEGATIVE as sealed for D2; THE_CLOCK §3.4).
- **The depth is a separate question.** No combination of the clocks picks our world's depth, the strip at Im τ ≈ 3
  (THE_CLOCK §0, §4).

### 8.3 The owner's plenitude: support, exclusion, typicality

The owner's reframing of 2026-10-29 ("they will happen, so our own"): if every world the framework allows is realised,
deriving the Standard Model is three questions in order. (a) Support: does some allowed configuration reproduce our world?
(b) Exclusion: does the support forbid things? (c) Only then, typicality under a measure (P-485, QUEUED). B1814's negative
is a statement about (c) under one chosen clock, not about (a) or (b) (P-485).

- **One quantity for all three** (THE_FINAL_ATTACK §1): the description length of our world through the framework (the
  framework paid once, plus our world's address in bits, plus the misfit), against the numbers' own length, with the same
  length for random worlds as the null.
- **The grading bar, sealed before any of it is computed.** The web seat's THE FINAL ACT'S BAR, adopted at S263 as THE_BAR's
  appendix: cells for support (with reach and resolution), compression, exclusion and specificity, typicality as a
  screen, held-out values, and inputs. Where the final attack's seal fixes a statistic, the seal's replaces the bar's
  default (`docs/THE_FINAL_ACTS_BAR_2026-10-29.md`, header; P-487's note of 2026-10-30).
- **Two pictures the test decides between** (THE_FINAL_ATTACK §7): (I) derived, the values following from the object's
  discrete data at one address; (II) the address, the object fixing the structure while the continuous values are our
  world's coordinates in the plenitude. The record's lens already leans to (II) for the values; the attack is meant to turn
  that lean into a measured statement either way (same section).

### 8.4 The inherited assumptions (P-443)

The clock briefing lists what the programme took over from the standard picture without forcing it, with what the record
now suggests (THE_CLOCK §6): that the nineteen are fixed constants (they may be a typical draw from a law); that the world
sits at one point (the unforced output is a measure over worlds, or one long history); that deriving means pinning the
point; that time is a given parameter (the clock is a choice the record has not made); that "democratic" means equal weight
per word (equal weight per unit length is the other democracy). These are the record's suggestions, not results.

---

## 9. Where it stands now

**In plain words.** As of 2026-10-30 the programme has a stated foundation, a discrete structure whose every item
carries its status (§5), a fitting frame that compresses six numbers without deriving them (§7), and a final test whose
order of work the owner approved on 2026-10-30 (P-495). That test asks whether the quark mixing comes out right at the
very address the masses already fix, after building one missing piece: a Higgs direction fixed by the interaction rather
than chosen. The design note for that piece (Step A) is next (Review 73's action items).

### 9.1 The last landings

| landing | what landed | source |
|---|---|---|
| S255 | B1813: the weave's own measure depends on how its threads are counted | CHANGELOG |
| S256 | B1814: the measured world as a draw; the no-lead-lost sweep (27 new register rows) | CHANGELOG; CAMPAIGN_STATUS |
| S257 | the clock briefing for the owner | CHANGELOG; THE_CLOCK |
| S258 | B1815: the record's walk has Minkowski's exit law; the clock stays CHOSEN | CHANGELOG |
| S259 | the web seat's critical line verified: its democratic point β* = 0.3912862189; no point of it picks a height except through a chosen statistic | CHANGELOG |
| S260 | B1816 (Weil–Petersson clock); B1817 (the cusp lepton factor does not track the colour count); W150 verified on main (a heavy-state holder of τ, with a second degenerate vacuum and one free ratio) | CHANGELOG |
| S261 | THE FINAL ATTACK proposed to the owner (P-495) | CHANGELOG |
| S262 | the workdesk, phase 1; the context-recovery card | CHANGELOG |
| S263 | the final act's bar and the chain map adopted; the two tiers; the running and group-theory tools calibrated | CHANGELOG |
| S264 | Review 73: B1812 narrowed (SU(5) ⊂ SO(10) ⊂ E₆ can meet at a point inside the object's class configuration, allowed and not selected); B1811's count corrected to 164; B1814's floor statement and 11σ census-dependent; the full suite run on a fresh clone, four uncommitted files a lock read now committed | CHANGELOG |
| S264b | Review 73's anchor; the views refreshed; the README rewritten from blank | CHANGELOG |

### 9.2 The final attack (P-495)

(`docs/THE_FINAL_ATTACK_2026-10-29.md`; register row P-495.)

- **Why there.** Data-free tables at 213 CM points (values of τ where the torus has complex multiplication, enumerated by
  discriminant; *background* for the term) show that, without a line, the three sectors are identical; that the
  object-forced fields' outputs match control fields'; that rigid τ buys only one or two bits; and that the decision lies in
  the outputs not fitted, the CKM at the six's own address, about 24 bits against the six's 20 (THE_FINAL_ATTACK §3, T1–T4;
  the bit figure is marked there as an estimate).
- **Step A, the missing construction (design, data-free).** A Higgs direction fixed by the interaction: couple W150's heavy
  states to the record's Higgs sections and minimise jointly over τ and the section. Its honest limit, stated in the
  proposal: each heavy multiplet fixes one real combination and brings one free ratio, so Step A compresses only if the
  object fixes the heavy spectrum itself (P-415, the towers).
- **Step B, THE NINE FROM ONE ADDRESS (one sealed test).** The line from the record's menu, τ continuous or at the forced CM
  points, the Higgs from Step A or the record's thirteen declared directions, c ∈ {1, 3} as two declared arms, every choice
  priced; observables the six, |V_us|, |V_cb|, |V_ub| and J; statistics fixed in the seal: support, compression,
  specificity.
- **Outcomes, fixed in advance.** PASS (breakthrough-grade): our world in the support with compression beyond the null's,
  the CKM predicted from the six's address with no new freedom. SUPPORT WITHOUT SPECIFICITY: a landscape that contains our
  world without explaining it, at this precision. NO SUPPORT: the missing piece is located in the Higgs sector, and the
  towers' meeting is the next frame.
- **Priors written before any table of the nine is read:** with the thirteen directions PASS ≤ 2% and NO SUPPORT about 75%;
  with Step A's vacuum, if it exists, PASS ≤ 10%.
- **Before the seal** (Review 73 has landed, S264): Step A's design note; the rigid-direction census (900 configurations
  computed and left unread, the other 256 lines owed); the compression generator (P-418); the exclusion map; P-510's
  KIND_TABLE ruling.
- **Status.** The owner approved the order on 2026-10-30 (Review 73 → Step A's design note → the rigid-direction census
  → the compression generator → the seal, with P-510's KIND_TABLE ruling → the run; P-495, QUEUED in Q1). Review 73 has
  landed (S264); Step A's design note is next. The forks themselves are ruled by the math; the owner decides priorities
  (THE_FINAL_ATTACK §8).

### 9.3 The other live lines

| line | state | source |
|---|---|---|
| the towers (P-415): the Standard Model as the meeting of gauge towers at loci, the weave rule carried across SU(5) ⊂ SO(10) ⊂ E₆ | new to the record, from the owner's question; P-414 NEGATIVE in Witten's G₂ frame (B1805); in F-theory's 7-brane frame the towers can meet at a point: SU(5) ⊂ SO(10) ⊂ E₆ as brane stacks inside the object's class configuration, which the object allows and does not select (B1812, narrowed at Review 73); P-416 (coincident multiplets) QUEUED; open in other frames | `docs/THE_TOWERS.md` §3, §7 and dated notes |
| main's plan (P-393): remove inputs one at a time | steps 1–4 carried out as negatives or selections, none removing an input: the slope selected by the data (B1786); c, the reading and Im τ not derived or not found forced (B1789, B1790, B1791); open still: step 1's data-free reason for ‖3α‖ = 1/5 and the offset rule, P-394 (the reading rule) and P-398 (a Petersson height for Im τ); step 5 named, not planned; the ledger of inputs removed is empty | `docs/MAINS_PLAN.md` |
| the lepton factor's route left (P-397) | an insertion that sees one leg's integer hypercharge; main's design task | P-397; B1817's hatch |
| selection by inversion (P-419) | the main line by the owner's ruling at S249 (2026-10-29); its first frame closed for three (B1808), its F-theory card done (B1812); QUEUED beside THE FINAL ATTACK, whose order the owner approved on 2026-10-30 | P-419 |
| the clock (P-439) | is the weave's time the move count or the geodesic flow? QUEUED | P-439; B1815 |
| one honest scoreboard (P-418) | the 19, plus the discrete choices added, plus the UNEARNED identifications, tracked at every landing; the build owed | P-418 |
| the two tiers (P-509) | claims stay gated; exploration below the gates is allowed, loosened and labelled; the final claim returns through a fresh seal. The owner's reason: "make sure that doesnt become our trap" | P-509; `docs/PRACTICES.md` |

### 9.4 The forks as they stand (GENESIS §8, v1.59)

| fork | question | now |
|---|---|---|
| FK1 | the principle's single wording | CONFIRMED |
| FK2 | orientation (SE2) | CHOSEN |
| FK3 | the swap: a legal move, and of what type | OPEN |
| FK4 | inverse moves | ANSWERED (v1.48) |
| FK5 | faithful F₂ against its abelian quotient | OPEN |
| FK6 | positivity | CHOSEN (re-read as the choice of side) |
| FK7 | the deck: gauged or kept | OPEN |
| FK8 | the join: which maps carry physical data between states | OPEN |
| FK9 | selection: what makes a state physical | OPEN; named the missing ingredient (v1.45) |
| FK10 | the end law | OPEN; the cusp's unit a tagged working postulate (v1.39), reduced to four links none derived (v1.59) |
| FK11 | the dictionary | UNEARNED; unearnable by a twisted Euler characteristic or the class index on a thread or cover within F-HE and F-CI (v1.27, scoped v1.46) |
| FK12 | the register: is the order of a word's letters part of the state, or an input? | OPEN |
| FK13 | which set "the family" names | RULED BY THE PRINCIPLE: the word states |
| FK14 | the ends: does the genesis generate several-ended states? | OPEN |
| FK15 | the field's genesis | OPEN |

The six gaps to physics (GENESIS §7): GAP1 the dictionary; GAP2 the ends; GAP3 the source; GAP4 selection and coincidence;
GAP5 dynamics; GAP6 the flatness. THE_CHAIN_STATUS's currency pass places each on the chain (GAP1 at the zero modes,
couplings and comparison; GAP2–GAP3 at the fields; GAP4 at P-485's support question; GAP5 at the clock, spacetime and the
moduli; GAP6 at the depth).

### 9.5 What would count as a breakthrough

The record states it in several places, and they agree:
- **A sealed PASS of the final attack**: the CKM predicted from the six's address with no new freedom, then the gauge
  couplings and the Higgs sector at the same vacuum (THE_FINAL_ATTACK §4).
- **An input removed**: a free input disappears and does not return as a hidden metric, boundary, normalisation, measure,
  selection rule or fitted datum, shown by a sealed test where no record has looked (MAINS_PLAN, "What counts"; P-392).
- **A dimensionless coupling from a rigid invariant** with no fitted number; **the point-selection principle**; or **the
  exact statement of what the object forces**, with the 19 outside it (`docs/THE_PATTERN_MEDITATION_3.md` Part VI; its
  theorem draft was withdrawn and delivered as B1809's census, P-406).
- **The clock forced** within the frame: "why are hierarchies deep?" would become a derived structural fact, the first of
  its kind in the record (THE_CLOCK §7).
- **The grade.** PASSED is necessary for WHAT_WOULD_COUNT's DERIVED and never sufficient: DERIVED needs the theory to
  output the result where an alternative was possible and the accepted framework does not fix it (`docs/THE_BAR.md`).

---

## 10. How to find anything

| to find | read or run |
|---|---|
| the foundations, every item with its status | `GENESIS.md` (canonical; amended only by an arc, with a version-log line) |
| the state at a glance, generated at every landing | `docs/views/CONTEXT_RECOVERY.md` (its counts table of arcs by verdict and register points, regenerated at every landing) |
| the newest entries, in words | `docs/CAMPAIGN_STATUS.md` (its LATEST lines); `CHANGELOG.md` |
| every raised point, its disposition and its queue slot | `docs/POINT_REGISTER.md` (P-rows) |
| the chain from the rule to the 19, every link labelled | `docs/THE_CHAIN_STATUS.md`, currency pass of 2026-10-30 |
| the weave and its facts | `docs/THE_WEAVE.md` |
| the towers question | `docs/THE_TOWERS.md` |
| main's plan of reductions | `docs/MAINS_PLAN.md` |
| the clock | `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` (dated snapshot); B1813–B1816 |
| the final attack and its bar | `docs/THE_FINAL_ATTACK_2026-10-29.md`; `docs/THE_FINAL_ACTS_BAR_2026-10-29.md`; `docs/THE_BAR.md` |
| why no continuous value has come | `docs/THE_PATTERN_MEDITATION_3.md` |
| identifications | `docs/IDENTIFICATION_LEDGER.md` |
| inputs, looks, seals, kinds | `docs/INPUT_COMPLETENESS_LEDGER.md`; `docs/LOOK_LEDGER.md`; `docs/SEAL_LEDGER.md`; `docs/KIND_TABLE.md` |
| negatives and what would reopen them | the kill graph, `frontier/B738_pathfinder_compiler/kill_graph.json`; `docs/views/CLOSED_DOORS.md`; `docs/atlas/FAILURE_ATLAS.md` |
| falsifiers | `docs/FALSIFIER_REGISTER.md` |
| errors made and corrected | `docs/ERROR_LEDGER.md`; `docs/RETRACTIONS.md` |
| what the seats sent and what main verified | `docs/HARVEST_LEDGER.md`; `docs/RELAY_LEDGER.md` |
| the vocabulary | `TERMINOLOGY.md` (with the referee lane's concordance of classical names) |
| the document map | `docs/INDEX.md` |
| the paper | `papers/P9_what_a_grammar_fixes/` (draft 9, 2026-10-20; "not yet submitted", README; no value derived, its abstract) |
| a visual desk over the record | `docs/workdesk/` (the scripts that build a read-only page from a named commit, `python3 -B docs/workdesk/build_page.py --out DIR`; the page itself is not committed; not a result of the programme; its README) |
| one arc | `frontier/B####_*/`: `FINDINGS.md` (the result), `arc_verdict.json` (verdict, scope, dependencies), `PREREGISTRATION.md` (present where the arc was sealed; sealed before the run), `verification/` (scripts and outputs, where the arc has any) |

**Before saying the record lacks something, sweep it** (WORKING_RULES: the absence rule; see the repo and the literature
first):
`python3 scripts/checks/topic_sweep.py "<regex>"` reads every arc's verdict line and the register;
`scripts/checks/already_banked.py` asks whether a result is banked; `scripts/checks/absence_sweep.py "<term>"` looks for
one string anywhere. `python3 scripts/gates/gates.py` runs the governance gates (WORKING_RULES, "Enforcement").

---

## Appendix A. Sources read

Read in full or in the sections cited:
- `WORKING_RULES.md` (whole)
- `GENESIS.md` (§0–§9 whole; §10's version log by entry headers, v1.30–v1.59)
- `TERMINOLOGY.md` (the GENESIS-ID table; the glossary additions of Reviews 61–68; the referee lane's concordance; the
  additions of 2026-10-29)
- `philosophy/P000_what_is_not_nothing.md` (whole); P001–P015 (openings, about 3 000 characters each); P016–P021
  (openings); `philosophy/THE_ORIGIN_POSTULATE.md` (opening)
- `GOVERNANCE.md` (§1–§2 opening)
- `PROVENANCE.md` (§0)
- `README.md` (the state banners and the 2026-10-03 state section)
- `docs/THE_WEAVE.md` (opening through B1607; section list; B1697–B1725 summary; spontaneous breaking; the ladder's rule)
- `docs/THE_TOWERS.md` (whole)
- `docs/THE_CHAIN_STATUS.md` (whole, including the currency pass of 2026-10-30)
- `docs/MAINS_PLAN.md` (whole)
- `docs/IDENTIFICATION_LEDGER.md` (whole; statuses counted by script and by hand)
- `docs/CAMPAIGN_STATUS.md` (the LATEST lines S253–S264)
- `docs/THE_CLOCK_AND_THE_NEXT_ATTACK_2026-10-29.md` (whole)
- `docs/THE_FINAL_ATTACK_2026-10-29.md` (whole)
- `docs/THE_FINAL_ACTS_BAR_2026-10-29.md` (header and §0 opening)
- `docs/THE_PATTERN_MEDITATION_3.md` (whole)
- `docs/THE_BAR.md` (header, procedure opening, grade table)
- `docs/UNIQUENESS_THEOREM.md` (header and axioms opening)
- `docs/INDEX.md` (entry protocol, living documents, registers)
- `docs/views/CONTEXT_RECOVERY.md` (whole); `docs/views/REVIEWER.md` (opening)
- `docs/FALSIFIER_REGISTER.md` (P10, P10′ rows and notes)
- `docs/PRACTICES.md` (the two-tiers row)
- `docs/POINT_REGISTER.md` (rows P-139, P-372, P-377, P-392, P-393, P-397, P-406, P-414, P-415, P-416, P-418, P-419,
  P-439, P-443, P-485, P-487, P-488, P-489, P-495, P-509, P-510, P-511, P-512)
- `docs/workdesk/README.md` (opening)
- `CHANGELOG.md` (S250–S264)
- `papers/P9_what_a_grammar_fixes/README.md`; `tex/sections/abstract.tex`
- `frontier/B738_pathfinder_compiler/kill_graph.json` (the entries for the negatives in §6; the entry count)
- Arcs, `arc_verdict.json` claim lines: B197, B259, B428, B680, B716 (with its FINDINGS header and note of 2026-10-29),
  B727, B760, B813, B852, B860, B862, B993, B994, B996, B997, B1014, B1028, B1083, B1088, B1098, B1115, B1123, B1157,
  B1160, B1183, B1184, B1221, B1223, B1225, B1236, B1266, B1323, B1345, B1422, B1454, B1455, B1484, B1487, B1496, B1600,
  B1601, B1603, B1604, B1606, B1607, B1609, B1611, B1612, B1613, B1616, B1617, B1618, B1620, B1628, B1629, B1632, B1634,
  B1635, B1636, B1639, B1641, B1642, B1644, B1651, B1652, B1653, B1655, B1656, B1662, B1663, B1666, B1667, B1676,
  B1677, B1678, B1679, B1680, B1682, B1689, B1691, B1694, B1696, B1697, B1698, B1699, B1700, B1702, B1708, B1711,
  B1712, B1713, B1720, B1722, B1723, B1725, B1726, B1730, B1739, B1740, B1741, B1742, B1743, B1746, B1747, B1749, B1750,
  B1753, B1756, B1784, B1785, B1786, B1788, B1789, B1790, B1791, B1793, B1796, B1798, B1801, B1802, B1803, B1804,
  B1805, B1808, B1809 (with FINDINGS §4–§7), B1810, B1811, B1812
- Arcs B1813–B1817: `arc_verdict.json` in full and the first sections of `FINDINGS.md`
- B1720 and B1726 `FINDINGS.md` (the lines naming the six ratios)
- Added by the readers and main: register rows P-178, P-209, P-394, P-398, P-466 and P-516; `docs/THE_TOWERS.md` (its note
  of 2026-10-30); `docs/progress/REVIEWS.md` (Review 73)
- `scripts/checks/topic_sweep.py "lepton factor|c = 3"` (run once; its VERDICT line: 21 of 1564 arcs on main match)

## Appendix B. How this page was checked

- A writer drafted it from the sources in Appendix A, marking no claim as untraced.
- Three readers then checked it in three parts: 158, 133 and 332 sentences and table rows against their sources, with
  every count recounted from the files (arcs by verdict 1 037 / 380 / 93 / 12; register points 517; identifications
  8 EARNED, 8 REFUTED, 20 UNEARNED of 36; the kill graph's 856 entries; the 758 states and 536 manifolds).
- They found 74 defects: 2 wrong, 13 stale, 52 overstated, 7 unsupported. Main checked the substantive ones at source
  and accepted all 74. Most narrow a scope the draft had dropped; the stale ones are the facts of Review 73 (S264).
- The identification ledger's own standing count (8, 8, 18 of 34) predates its rows I-35 and I-36; the counts above are
  from its table.

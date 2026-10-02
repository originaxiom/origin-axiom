# GENESIS — the foundations of origin-axiom

**Version 1.0 · 2026-10-02 · arc B1516 · canonical.**

This file states, in one place and with one numbering, what the programme assumes, what it derives, what it chooses and
what it leaves open, from its principle down to the objects it computes on. It replaces the scattered statements of these
matters in:
- `philosophy/P000_what_is_not_nothing.md`, `philosophy/P019_the_genesis_axiom_chain.md` and
  `philosophy/P022_the_generated_state_space.md`;
- `docs/UNIQUENESS_THEOREM.md` and Part I of `docs/THEOREM_LEDGER.md`;
- `docs/THE_END_TO_END_CHAIN.md` and the README's state-of-the-programme section.

Those documents keep their history and their proofs. **Where any document disagrees with this file, this file holds, and
the other document is the one to fix.**

**Amending this file.** Only an arc may change it. The arc names each item it touches, its old and new status and the
evidence, and adds a line to the version log (§10). The version number increases with every change. Downstream documents
cite the version they rely on.

**Pending the owner:** the single wording of the principle (§1, fork FK1) is this seat's proposal and waits for the owner's
confirmation. Everything else here restates the record as it stands, checked by B1516's own code
(`frontier/B1516_genesis_v1/verification/foundations_checks.py`).

---

## 0. How to read and use it

- Every item has an ID and one status:
  - **DERIVED**: proved, with the proof or check cited;
  - **CONDITIONAL**: proved given named premises;
  - **POSTULATED**: assumed;
  - **CHOSEN**: a fork settled by choice, with the alternative kept;
  - **OPEN**: not settled.
- **The IDs are new.** PF (principle), GM (grammar), SE (selector), T-ROOT, F-xx (frames), FK (forks) and GAP were unused
  anywhere in the repository when v1.0 was written. Shorter labels such as P1–P3, G1–G5, S1–S2 or K1–K11 already have many
  meanings there, so v1.0 does not use them. Outside this file, cite an item as "GENESIS SE1" or "GENESIS v1.0 SE1".
- Every result in the repository, positive or negative, carries a **scope tag** (§6). A negative holds only as far as its
  tag reaches.
- The chain runs principle (§1) → grammar (§2) → generated state space (§3) → root (§4) → frames (§5) → physics (§7).
  Nothing in a later section is used to justify an earlier one.

---

## 1. The principle

**Proposed single wording (v1.0, owner to confirm):**

> **Existence is what remains when cancelling to nothing cannot complete (PF1). That remainder is a description that
> cannot be exhausted (PF2). The programme reads that description as mathematical structure and asks what it forces (PF3).**

| ID | Face of the principle | Source wording | Status |
|---|---|---|---|
| PF1 | what exists | "existence as a frustrated cancellation" (`GOVERNANCE.md` §1; README); P000's question "what is not-nothing?" | POSTULATED |
| PF2 | the form the remainder takes | "being is inexhaustible description" (P019 A0 + A2: "nothing below argues for it") | POSTULATED |
| PF3 | the method | "the decision to look for structure in a mathematical object at all" (the P3 paper's A0, "unpriceable") | POSTULATED |

These wordings had lived side by side with no amendment relating them. They are three faces of one commitment, not three
principles.
- The only written bridge between PF1 and PF2 is P019's remark that inexhaustibility restates P000's premise 1, "resist the
  trivial maximally". PF2 does not follow from PF1 by any derivation in the record.
- **The family is the intended shape.** P000, the programme's first philosophy file, says a foundation that produced a
  unique seed "would be the suspicious outcome", and that the member is contingent. P019's "to a unique object" departed
  from this, and P022 corrected it on 2026-09-27. The generated state space (§3) is P000's stance made precise, not a
  retreat from it.

---

## 2. The grammar: what a description is made of

Core convention, used everywhere from v1.0 on: **L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]]**. So
LR = [[2,1],[1,1]] (trace 3), RL = [[1,1],[1,2]], and the golden matrix is LP = [[1,1],[1,0]] with (LP)² = LR. B1384's
verification code uses the transposed pair, so its "RP" is the core's LP (the audit lane's R57).

| ID | Item | Status | Evidence and notes |
|---|---|---|---|
| GM1 | Two records: updates act on a pair of integer counts, ℤ² | POSTULATED | UNIQUENESS A1. Not independent of GM4: ℤ² is the first homology of the punctured torus (main B1422). Fork F9 is robust to word length three and fragile at four (main B749 addendum). |
| GM2 | Unit shears: elementary updates are L and R; descriptions are words in them | POSTULATED | UNIQUENESS A4. Every hyperbolic class of SL(2,ℤ) is ± a cyclic word in L and R with both letters, so GM2 generates every state (B1516 C9: all 168 hyperbolic matrices with entries up to 5, each with an explicit conjugator). |
| GM3 | Aperiodicity: the description is not periodic, so the monodromy is hyperbolic | POSTULATED (cheap) | P019 A2. B749 F2 ROBUST: every periodic alternative is degenerate (finite order or reducible, no hyperbolic carrier). |
| GM4 | Carrier: words are realised as a mapping class of the once-punctured torus | POSTULATED, the puncture CONDITIONAL | P019 A5 and A5b; THEOREM_LEDGER C4. B1380 derives the puncture from faithful F₂ word data. The audit lane's R57 rejects B1380 §3's naturality argument for keeping F₂ rather than its abelian quotient, so faithful word realisation and the surface category stay premises. B749 F8: the anatomy needs geometry. |
| GM5a | Reversible updates (GL(2,ℤ)) | POSTULATED | UNIQUENESS A2. |
| GM5b | Inverse moves are legal | OPEN | Needed for the signed states: −I = (L²R⁻¹)² (B1384 S0). Invertibility of a matrix is not legality of its inverse as an update (R57). |
| GM5c | The record swap P is a legal move | OPEN | An added axiom (main B1422). Its semantic type is open (sL-3). If legal, the golden matrix LP (det −1) is generated, and so is P000's metallic family LᵐP = [[m,1],[1,0]], whose squares are the word states LᵐRᵐ (B1516 C10). |
| GM5d | Counts are non-negative (positivity) | CHOSEN | A sector restriction, not a consequence of using L and R (R57; the audit lane's operational contract). Not needed to select the root (§4). |

---

## 3. The generated state space

**X_gen = (reachable states, native moves, equivalences, root)** (B1384, adopted 2026-09-27; P022).

**States.** A state is a signed cyclic word s = (ε, w): w is a primitive word in L and R using both letters, taken up to
rotation and the L↔R swap, and ε = ±1. It is realised as the once-punctured-torus bundle with monodromy εw, a hyperbolic
3-manifold with one cusp. If the swap P is legal (GM5c), the orientation-reversing bundles join them; the Gieseking manifold
m000 is the bundle of LP.
- **Census** (DERIVED; re-derived by B1516 C4 and C5): 2, 2, 4, 6, 10, 18, 32, 56, 102, 186 and 340 states at lengths 2
  to 12, 758 in all, as main's B1434 and B1439 count. A word of length n gives a manifold of n ideal tetrahedra. The 24
  states to length 6 are m004 (+LR), m003 (−LR), m009 (+LLR), m010 (−LLR), m022, m023, m135, m136, m039, m040, m234, m235,
  m369, m370, s000, s001, s298, s299, s463, s464, s639, s640, s891 and s892.
- **Levels.** The n-fold cyclic cover of a state (ε, w) has monodromy (εw)ⁿ. Its first homology has torsion of order
  abs(2 − tr((εw)ⁿ)), which is also the number of fibre characters its monodromy fixes. For m004 these orders are 1, 5, 16,
  45, 121 and 320 at n = 1 to 6. The levels M₂ to M₆ are m206, s961, t12839, o10_150696 and otet12_00013 (B1516 C6;
  main's notation Mₙ; this seat's older Yₙ is ambiguous, see ERROR_LEDGER E72).

**Moves and relations** (B1384; the audit lane's operational contract).

| Relation | What it does | Physical use requires |
|---|---|---|
| Word extension | reaches longer words | an evolution law and a clock before depth is called time |
| Sign | ±w, with inverse moves (GM5b) | operational legality of inverses |
| Cyclic cover (level) | refines a state; monodromy φⁿ | transport of the action, domains and coefficients, not only of cohomology |
| Deck transformation | symmetry of a level | whether it is gauged or kept (fork FK7) |
| Filling | closes a cusp; flat data descend when ρ(slope) = 1 | metric, action and domain matching |
| Orientation double cover | m004 → m000, when P is legal | the semantic type of P (FK3) |
| Commensurability | common finite covers. m004's class has 99 census members, the arithmetic part of B1186's 112-member family (the other 13 share the field but not the class: B1390), and it contains every finite cover | the same as covers |

**Equivalences.** Unbased conjugacy identifies LR and RL: they are conjugate in SL(2,ℤ) by L, since L⁻¹(LR)L = RL (not by
P, whose determinant is −1). The order bit (UNIQUENESS A7) matters only for based data, such as the golden fixed-point
polynomial τ² − τ − 1 of LR against τ² + τ − 1 of RL (B1516 C3).

| Claim about X_gen | Status |
|---|---|
| Every legal state belongs to the state space (generated closure) | DERIVED, at the level of definition (B1384) |
| Every legal state occurs in one history | NOT DERIVED |
| All legal states are physically realised together | NOT DERIVED |
| Some arrow of X_gen is physical time | NOT DERIVED (B1384's transition-semantics fence) |
| A rule selects which state is physical | OPEN (fork FK9; main's L229 (iv)) |

---

## 4. The root and its selectors

| ID | Item | Status | Evidence |
|---|---|---|---|
| SE1 | **The selection criterion: the root's first homology is torsion-free.** | POSTULATED | UNIQUENESS A5, motivated by the topology. Alternatives kept: minimal trace selects ±LR (m004 and m003); minimal volume selects m000, and among orientable states leaves the m003–m004 tie, which SE1 breaks (B197). |
| T-ROOT | **What SE1 selects.** For a hyperbolic once-punctured-torus bundle, the torsion of H₁ has order abs(2 − tr) for orientation-preserving monodromy and abs(tr) for orientation-reversing. So H₁ is torsion-free exactly for the class of LR (trace 3: **m004**) and the class of the golden matrix LP (det −1, trace ±1: **the Gieseking manifold m000**). | DERIVED | CLAIMS C3 (the orientation-preserving half, as CLAIMS scopes it); B197; B1516 C2 (every unimodular matrix with entries up to 5, each torsion-free one conjugated explicitly to LR, LP or (LP)⁻¹) and C5 (SnapPy: of 46 orientation-reversing bundles to length 6, only m000 is torsion-free). |
| SE2 | **Orientation**: of the two, take the orientable one, m004, the orientation double cover of m000 | CHOSEN | P019 A6; UNIQUENESS A3; THEOREM_LEDGER C5. Minimality points the other way: m000 has half the volume and one tetrahedron (B1380; B749 F5 FRAGILE, "the parent"). The most fragile link of the chain (fork FK2). |

**The root.** Given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement (Thurston; Riley). In the
audit lane's words (R57): *"In its positive two-record once-punctured-torus sector, m004 is the distinguished minimal
mixed state. Whether that sector, its root, or particular relations have physical priority remains to be derived."*

**Four inputs suffice, and each is needed** (B1516 C8).
- Without GM3, SE1 also admits the order-6 monodromy of trace 1 (whose mapping torus is the trefoil complement) and the
  parabolic monodromies of trace 2, such as L.
- Without GM4's carrier, SE1 admits the closed torus bundle of LR, which is torsion-free but Sol (m004's (0, 1) filling,
  H₁ = ℤ), and every knot complement in S³ (H₁ = ℤ; for example 5_2, hyperbolic).
- Without SE1, every state remains (758 to length 12). Without SE2, m000 remains.
- Minimality (UNIQUENESS A6), positivity (GM5d), the unit-shear generation (GM2) and the order bit (UNIQUENESS A7) are not
  needed. A7 is needed only where based data are used: the golden polynomial, and the derived potential of P15–P16.

**The routes meet.**
- *The words route* (P019; THEOREM_LEDGER C1–C6): aperiodic → Sturmian (Morse–Hedlund) → golden slope (Hurwitz) → the
  golden matrix LP on the once-punctured torus, whose bundle is m000 → its square LR by orientation (SE2). Main splits T4
  into a theorem and a criterion (its C2a and C2b).
- *P000's metallic family* LᵐP (det −1, trace m): SE1 selects m = 1. The bundle of LᵐP has H₁ torsion ℤ/m, and the bundle
  of its square LᵐRᵐ has (ℤ/m)² (B126's fact (A); B1516 C10). P000 called m = 1 "most-selected, not forced"; SE1 is one
  more selector of it, and, like the others, a chosen one.
- *The records route* (UNIQUENESS): A1–A6 force LR up to the order A7, by a 144 → 1 collapse on the positive grid. The
  forcing is over-determined: A5 alone and A6 alone each select (1, 1), and the unit-shear axiom A4 already fixes the
  increments, so the collapse is a consistency demonstration rather than a search (main B1422). Without positivity the
  torsion-free hyperbolic solutions are (1, 1) and (−1, −1), both in LR's class (B1516 C1).
- None of the routes derives its axioms from anything weaker (UNIQUENESS §6; main B1422).

**The root is the emptiest state.** SE1 says that m004's fibre has no non-trivial character fixed by its monodromy, and
among the orientable states only the root has that property. It is also why m004's own level is empty in main's frame:
*"The root has none and cannot, since its fibre has no finite character"* (main B1434). The property that selects the root
is the property that leaves it empty at its own level. The root is the architecture's origin of coordinates, not its
physical centre. Reading SE1 as "the least remainder" connects it to PF1, but that is an interpretation, not a derivation.

**Provenance (recorded, not hidden).**
- The figure-eight was first named in a probe on 22 May 2026, and the axioms were committed on 28 May (main B1422): the
  object preceded the axioms.
- None of the codex seat's genesis anchors is marked PROVED: OA-C0001 is REFUTED, and OA-C0002 and OA-C0003 are CONDITIONAL
  (its B8135, as digested on the physics-seat branch).
- So the genesis is a conditional reconstruction of a chosen sector. It is not a derivation of m004 from nothing.

---

## 5. Frames: dictionaries from geometry to particles

A frame turns flat bundles on a state into particle counts. **None is derived from §1–§4, and the transport of any of them
to physics (identification I-26) is UNEARNED.** Each is a named hypothesis.

| ID | Frame | What it computes | Where it lives |
|---|---|---|---|
| F-FC | Free-cusp frame | bulk matter with the Standard Model unbroken; a chiral count needs a free cusp, one whose peripheral rank in H₁(M; ℚ) is below b₁ | this branch, B1368–B1399 |
| F-CI | Class-index frame | main's index I = n(V) − n(V*) on reducible non-split doublet modules in the E₆/27 frame; generation-shaped backgrounds | main, B1297 and B1418–B1451; verified here (sm:B1374, sm:B1375) |
| F-HE | Harmonic E₈ frame | E₈ ⊃ SU(5) × SU(5)′ on the harmonic convex-projective vacuum; rank-five extensions W with N(10′) = −I(W) and N(5̄′) = −I(Λ²W) | this branch, B1509–B1515; the audit lane, R40–R76 |
| F-AP | G₂ apex frame | matter at cone points of a G₂ space built over the cusps; anomaly inflow | this branch, B1355–B1365 and B1500–B1505 |

The frames disagree on the same objects. Every word state is closed in F-FC (one cusp and b₁ = 1, so no free cusp: B1385),
while 95 of the 758 carry a generation-shaped background at their own level in F-CI (main B1439). **A result is a statement
about a frame applied to an object, never about the architecture as such.**

Where each frame has been run, by object (as of v1.0):

| Object | F-FC | F-CI | F-HE | F-AP |
|---|---|---|---|---|
| m004 and its cyclic levels Mₙ | closed: one cusp and b₁ = 1 (B1368; B1385) | M₁ and M₂ carry no generation-shaped background; M₃ to M₆ carry 48, 256, 400 and 2 160, each counting ±1 (main B1432, reproducing this seat's level census) | computed: at the μ = −1 points a 10′ without its 5̄′ (B1509); at q = 1 both halves on one background, with opposite signs (B1515) | m004's cusp (shape 2√−3) is not hexagonal, so B1501's cones do not complete it; the apex designs are conditional (B1355–B1365) |
| m004's commensurability class (99 census members; every finite cover) | B1186's 112: 108 closed (B1369), four cusps open on one Fourier coefficient each (B1370); the cover cube~3.24 counts ±2, but the count moves with the cusp cut (B1386–B1388) | fires on five arithmetic members: s958, v2873, t12833, t12835, o10_150701 (main B1418; sm:B1374) | never computed | hexagonal cusps (m003's, three of cube~3.24's four, 14 of m004's 87 covers of degree ≤ 10) match B1501's cones conformally; a cusp point is chiral only where its locus meets another fixed set (B1503) |
| The other word states (758 to length 12) | closed (B1385 T1) | 95 carry a background at their own level (main B1439), among them m369 (8) and s639 (16) (main B1434) | never computed | never computed |
| m010 (−LLR) | closed | none at its three-fold level (main B1434) | the audit lane's R40: I(W) = I(Λ²W) = +1, an anomaly-free 10 + 5̄, on a block with no harmonic background (F01) | never computed |
| m000, the Gieseking manifold | never computed | never computed | never computed | never computed |

---

## 6. Scope tags (mandatory from B1516 on)

Every banked result carries a scope tag with four parts:
- **frame**: F-FC, F-CI, F-HE, F-AP, another named frame, or "none" for a result about the grammar or the state space
  itself;
- **object**: a state, a family (for example "m004's convex-projective family"), a class or set of states (for example
  "m004's commensurability class", "the word states to length 12"), or "all once-punctured-torus bundles";
- **reach**: "single" (one state, with the deformations or levels its hypotheses name), "class" (a named class or set of
  states) or "general" (every state of the grammar, or every manifold of a stated kind);
- **hypotheses**: what else the result needs (an end condition, a level range, q ≠ 1, and so on).

The tag lives in `arc_verdict.json` (field `scope`) and in each kill-graph entry (field `scope`). From B1516 on,
`tests/test_arc_verdict_schema.py` requires it of every new arc, and `tests/test_b1516_genesis_v1.py` requires it of every
kill-graph entry this seat wrote from B1369 on. A negative blocks only where its tag reaches (WORKING_RULES, the amended
mandate of 2026-10-01).

---

## 7. What is not claimed, and the distance to physics

**Not claimed:** that every state is physical; that any arrow is time; that any state is selected; that any frame is
physics; any Standard-Model parameter (**0 of 19**).

**Five gaps**, none of which work on one state can close:
- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.
- **GAP2, the ends.** Chiral counts live at cusps, which have continuous spectrum, and they depend on an end condition that
  is chosen rather than derived. Over the end conditions, B1509's 10′ count is 0, 1 or 2 (B1392 places the count at the
  ends). sL-8's rule forbids choosing an end to rescue a count.
- **GAP3, the source.** Chirality sits on non-split bundles, which carry no harmonic metric without a source (B1378, by
  Corlette–Donaldson; the audit lane's F01 and R41).
- **GAP4, selection and coincidence.** With hundreds of states, four frames, many levels and several end conditions, a
  Standard-Model-like feature somewhere is expected by chance. A selection rule and a null model must be fixed before a
  match counts.
- **GAP5, dynamics.** Topology yields integers and discrete structure. The 19 values need moduli, symmetry breaking and
  running, which the architecture does not have.

---

## 8. Open forks, each with what would settle it

| ID | Fork | Now | What would settle it |
|---|---|---|---|
| FK1 | The principle's single wording (§1) | proposed | the owner's confirmation or rewording |
| FK2 | Orientation (SE2) | CHOSEN | a derived reason for orientability (Pin structure, time reversal: B1382, B1383, sL-3), or carrying both m004 and m000 as states |
| FK3 | The swap P: legal move, and of what type | OPEN | an operational meaning for P (redescription, parity, time reversal) that the frames can test |
| FK4 | Inverse moves (GM5b) | OPEN | operational legality; until then the signed states are an extension of the grammar |
| FK5 | Faithful F₂ against its abelian quotient (GM4) | OPEN | an observable that needs word order or the commutator |
| FK6 | Positivity (GM5d) | CHOSEN | a reason the physical states are the non-negative cone |
| FK7 | The deck: gauged or kept | OPEN | an action in which the deck acts (B1506) |
| FK8 | The join: which maps carry physical data between states | OPEN | a demonstrated physical map (action, domains, anomaly account) beyond covers; filling descent is one candidate (B1508, R57) |
| FK9 | Selection: what makes a state physical | OPEN | a rule fixed before computing, with a null model (GAP4) |
| FK10 | The end law | OPEN | an end condition derived from physics (sL-8) |
| FK11 | The dictionary (I-26) | UNEARNED | a frame derived from M-theory or from the principle, with its scope proved |

**Computed nowhere yet** (the frontier, not a list of failures):
- the harmonic frame on any state outside m004's levels;
- the class-index frame on m369 or s639 built from their own arithmetic (main's L229 (iii));
- the Gieseking manifold m000 in any frame;
- fillings and non-cyclic covers of word states other than m004 and m003;
- the genesis paths of `paths/PATHS.md` never touched: 18 of 25 at main's B1422.

---

## 9. Crosswalk: old labels to v1.0 IDs

From v1.0 on, cite the v1.0 IDs. The old labels collided: A5 and A6 meant different things in P019 and in the uniqueness
theorem; C1–C6 meant different things in `CLAIMS.md` and in `docs/THEOREM_LEDGER.md`.

| Old label | Where | v1.0 |
|---|---|---|
| "existence as a frustrated cancellation" | GOVERNANCE §1; README | PF1 |
| "what is not-nothing?" | P000 | PF1 (the question's form) |
| premise 1, "resist the trivial maximally" | P000 | the bridge from PF1 to PF2 (P019), and the words route's selector |
| premise 2, self-reference with no external input | P000 | GM4 |
| premise 3, the metallic family Mₘ = [[m,1],[1,0]] | P000; B92 | the swap-extended states LᵐP (GM5c), whose squares are the word states LᵐRᵐ |
| premise 4, m = 1 "most-selected, not forced" | P000; B313 | SE1 also selects m = 1 (B126); the member stays contingent |
| A0 being is description; A2 inexhaustibility | P019 | PF2 (A2's content is also GM3) |
| A0, "unpriceable" | the P3 paper | PF3 |
| L1 binary alphabet | P019 | a lemma under PF2; compare GM1 |
| T3 Morse–Hedlund; T4 the golden slope | P019; THEOREM_LEDGER C1 and C2 | the words route (§4) |
| A5 the carrier; A5b the puncture | P019; THEOREM_LEDGER C4 | GM4, the puncture CONDITIONAL (R57) |
| A6 orientability | P019; THEOREM_LEDGER C5 | SE2 |
| T7 Thurston; Riley | P019; THEOREM_LEDGER C6 | the root is m004 (§4) |
| C3, being is inexhaustible description | THEOREM_LEDGER | PF2 |
| A1 two records | UNIQUENESS | GM1 |
| A2 reversible transfer | UNIQUENESS | GM5a |
| A3 orientation-preserving | UNIQUENESS | SE2 |
| A4 primitive unit shears | UNIQUENESS | GM2 |
| A5 torsion-free closure | UNIQUENESS | SE1; its consequence is T-ROOT |
| A6 minimality | UNIQUENESS | not needed for the root: redundant given SE1 (§4) |
| A7 the order LR or RL | UNIQUENESS | not an axiom of X_gen: based data only (§3) |
| C1 (L and R forced); C3 (trace 3 the unique torsion-free trace) | CLAIMS.md | the records route (§4); T-ROOT's orientation-preserving half |
| F1–F9, the genesis forks | B749 (F9 on main) | the statuses of PF2, GM1, GM3, GM4, SE2 and FK2 |
| the X_gen convention | B1384; P022 | §3 |

---

## 10. Version log

- **v1.0 · 2026-10-02 · B1516.**
  - First canonical statement, with one numbering whose IDs were unused elsewhere.
  - SE1 is recorded as a postulated criterion, and T-ROOT as its derived consequence. The root needs four inputs (GM3, GM4,
    SE1, SE2), and each is needed. UNIQUENESS A6, positivity, GM2 and UNIQUENESS A7 are not needed for it.
  - T-ROOT extended to orientation-reversing monodromy: torsion-free means m004 or m000.
  - P000 entered: the family as the intended shape; its metallic family inside X_gen; SE1 selects m = 1 there.
  - Corrections carried:
    - UNIQUENESS §5: LR and RL are SL(2,ℤ)-conjugate by L, not by P (R57);
    - B1384's transposed L/R noted;
    - R57's rejection of B1380 §3 recorded at GM4.
  - The scope tag is made mandatory (§6).
  - The principle's single wording is proposed and awaits the owner (FK1).

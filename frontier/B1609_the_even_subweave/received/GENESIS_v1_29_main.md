# GENESIS — the foundations of origin-axiom

**Version 1.29 · 2026-10-08 · canonical.** v1.0 is the SM seat's (its arc sm:B1516). v1.1 is main's verification and
adoption of it (arc B1454): the same statement, the seat's arc numbers marked `sm:`, and main's amendments, each marked
**[v1.1]** where it adds content. The SM seat amended v1.0 the same day on its own branch (sm:B1517), also numbered 1.1
there, before main's was read. v1.2 (sm:B1519) takes main's v1.1 as the head, as main asked, and adds that amendment and
its own, each marked **[v1.2]**. v1.3 (main's B1456) is main's verification of v1.2 with its own code and its adoption,
with the three seats' results of the same day folded in, each marked **[v1.3]**. v1.4 (main's B1458) brings the bar onto
main and records what the own-level law is not, each marked **[v1.4]**. v1.5 (main's B1460) records the owner's two
decisions: FK1 confirmed as written, and FK12 framed as the register question. v1.6 (sm:B1526) takes main's head, v1.5,
as main asked. The SM seat's own v1.5 (sm:B1525) was made on main's v1.4 in parallel with main's and numbered the same;
v1.6 answers it by its line and carries what main's v1.5 had not made, each marked **[v1.6]**. On the SM seat's branch
main's v1.5 and the seat's v1.5 are kept as received in sm:B1526's `received/` (`GENESIS_v1_5_main.md`,
`GENESIS_v1_5_sm.md`), and main's v1.4 and the seat's v1.3 in sm:B1525's. v1.7 (main's B1462) is main's verification
of v1.6 by its own routes and its adoption, with one sentence corrected, marked **[v1.7]**. The version log (§10) lists every
change; the texts as received are kept on main in the arcs that adopted them
(`frontier/B1454_genesis_v1_verified_and_adopted/received/GENESIS_v1_0.md`,
`frontier/B1456_genesis_v1_2_verified_and_the_seats_reconciled/received/GENESIS_v1_2.md`).

This file states, in one place and with one numbering, what the programme assumes, what it derives, what it chooses and
what it leaves open, from its principle down to the objects it computes on. It replaces the scattered statements of these
matters in:
- `philosophy/P000_what_is_not_nothing.md`, `philosophy/P019_the_genesis_axiom_chain.md` and the SM seat's P022, the
  generated state space (on its branch; not on main);
- `docs/UNIQUENESS_THEOREM.md` and Part I of `docs/THEOREM_LEDGER.md`;
- `docs/THE_END_TO_END_CHAIN.md` and the README's state-of-the-programme section;
- **[v1.1]** Layer 0 of `docs/THE_FRAMEWORK.md` and the hypothesis line of `docs/THE_CLAIM.md` §1.

Those documents keep their history and their proofs. **Where any document disagrees with this file, this file holds, and
the other document is the one to fix.**

**Amending this file.** Only an arc may change it. The arc names each item it touches, its old and new status and the
evidence, and adds a line to the version log (§10). The version number increases with every change. Downstream documents
cite the version they rely on.

**[v1.5] Decided by the owner (2026-10-03):** the single wording of the principle (§1, FK1) is confirmed as written, and the
observer question (FK12) is framed as the register question. Everything else here restates the record as it stands, checked by the SM seat's own code (sm:B1516)
and re-derived on main by other routes (B1454, `frontier/B1454_genesis_v1_verified_and_adopted/verification/genesis_own.py`).

---

## 0. How to read and use it

**[v1.24] THE WEAVE — the owner's rule, named (2026-10-07; `docs/THE_WEAVE.md`; B1600).** A *thread* is one object the principle allows (m000, m003, m004, +LLLR …): one closed path of the moves through the shared fibre, the two records. *The weave* is the joint action of every allowed move on the records and everything it forces. Before any arc: **weave or thread?** A weave result takes every thread under a rule stated in advance with none hand-picked, is defined by the joint action, and claims about all threads at once; a thread result is anything read on one thread or its covers, labelled so (`weave_or_thread` in every verdict file from B1491) and never presented as the answer to a weave question. On this page §1–§2 (PF1–PF3, GM1–GM4: the records and the moves) are weave statements; §4's selectors SE1, SE2 and T-ROOT pick one thread and are thread statements; the frames of §5 are thread instruments, each built on one thread's holonomy.

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
- **[v1.1] Whose number is whose.** `sm:B…` is an arc of the SM seat (its ranges are sm:B1350–sm:B1399 and sm:B1500–sm:B1599). A
  B-number that is bare or written "main B…" is main's, and so is every B-number below B1278. R-numbers and F01 are
  the audit lane's.
- **[v1.1] Before saying the record lacks something** that bears on an item here, sweep it:
  `scripts/checks/topic_sweep.py`, and for B1–B500 `docs/EARLY_RECORD_INDEX.md`, whose verdict lines predate today's
  vocabulary (WORKING_RULES, the rule of 2026-10-02). **[v1.2]** The SM seat's form of the same rule records the sweep as
  data (`prior_work` in each verdict file, from sm:B1517) and, from sm:B1519, also in a FINDINGS section headed "Seen
  first", as main's arcs do from B1454. A sweep's terms include an object's names and explicit forms, not only the
  concept's words (sm:B1517's miss of m207, §3).

---

## 1. The principle

**The single wording (proposed by the SM seat in v1.0; [v1.5] confirmed by the owner 2026-10-03, main B1460):**

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
- **[v1.1] PF1 has a mathematical form in the record, and it is a reading, not a derivation.**
  `philosophy/P008_non_cancellation_is_fricke_vogt.md` (motivation, never a premise) names it: non-cancellation is
  κ = tr[a, b] ≠ 2 for the two letters, the Fricke–Vogt invariant, with κ = 2 the locus where the cancellation
  completes. The mathematics it points at is banked: κ = 4·I_FV + 2 (B148); κ = 2 is codimension one, spectrally
  trivial and the one fibre with positive-measure spectrum (B161, B162); four banked faces are one commutator trace
  (B309, B518). **κ names two quantities** (ERROR_LEDGER E72): the fibre's commutator trace, −2 at the root, which is
  the parabolic cusp and Minsky's punctured-torus condition (B160, B1404); and the knot group's meridian commutator
  trace, with κ − 2 = ω² (B285, B309). Every use says which.

---

## 2. The grammar: what a description is made of

Core convention, used everywhere from v1.0 on: **L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]]**. So
LR = [[2,1],[1,1]] (trace 3), RL = [[1,1],[1,2]], and the golden matrix is LP = [[1,1],[1,0]] with (LP)² = LR. sm:B1384's
verification code uses the transposed pair, so its "RP" is the core's LP (the audit lane's R57).

| ID | Item | Status | Evidence and notes |
|---|---|---|---|
| GM1 | Two records: updates act on a pair of integer counts, ℤ² | POSTULATED | UNIQUENESS A1. Not independent of GM4: ℤ² is the first homology of the punctured torus (main B1422). Fork F9 is robust to word length three and fragile at four (main B749 addendum; computed in B1323, corrected at B1414). |
| GM2 | Unit shears: elementary updates are L and R; descriptions are words in them | POSTULATED | UNIQUENESS A4. Every hyperbolic class of SL(2,ℤ) is ± a cyclic word in L and R with both letters, so GM2 generates every state (sm:B1516 C9: all 168 hyperbolic matrices with entries up to 5, each with an explicit conjugator). |
| GM3 | Aperiodicity: the description is not periodic, so the monodromy is hyperbolic | POSTULATED (cheap) | P019 A2. B749 F2 ROBUST: every periodic alternative is degenerate (finite order or reducible, no hyperbolic carrier). |
| GM4 | Carrier: words are realised as a mapping class of the once-punctured torus | POSTULATED, the puncture CONDITIONAL | P019 A5 and A5b; THEOREM_LEDGER C4. sm:B1380 derives the puncture from faithful F₂ word data. The audit lane's R57 rejects sm:B1380 §3's naturality argument for keeping F₂ rather than its abelian quotient, so faithful word realisation and the surface category stay premises. B749 F8: the anatomy needs geometry. **[v1.1]** Main has not verified sm:B1380 (its lead L239 (a)). A sweep of main's verdict lines (B1454) found no arc that derives the faithful F₂ carrier or the surface category from a weaker premise; B749 F8 and B1003 compute what is lost without the carrier, which is a different thing. |
| GM5a | Reversible updates (GL(2,ℤ)) | POSTULATED | UNIQUENESS A2. |
| GM5b | Inverse moves are legal | OPEN | Needed for the signed states: −I = (L²R⁻¹)² (sm:B1384 S0). Invertibility of a matrix is not legality of its inverse as an update (R57). **[v1.14] Not needed for them (B1482):** the signed states need exactly one move beyond L and R — the central −I, which negates both records — and −I does not bring inverse letters with it (L⁻¹ is not ± a positive word). GM5b and the sign are independent forks. |
| GM5c | The record swap P is a legal move | OPEN | An added axiom (main B1422). Its semantic type is open (sL-3). If legal, the golden matrix LP (det −1) is generated, and so is P000's metallic family LᵐP = [[m,1],[1,0]], whose squares are the word states LᵐRᵐ (sm:B1516 C10). **[v1.1]** Main's early record on the swap: ±LP are the only square roots of LR in GL(2,ℤ), and LₐR_b has an orientation-reversing integer square root exactly when a = b (B14; re-derived, B1454 G11); P is the unique primitive-pair exchange involution up to sign, forced by (LX)² = LR and not by the substrate axioms (B16, B19); every metallic bundle double-covers a non-orientable one (B469); the founding torsor's two bits are the swap and the reversal (B1083). **[v1.2]** On the words route the swap is native: the Sturmian morphisms abelianise onto the non-negative GL(2,ℤ) matrices, P among them, and the Fibonacci tick is LP (B1323); it is an added axiom on the records route (main B1422). B14's statement is complete, not a search: every integer square root X of a hyperbolic A has A = tr(X)·X − det(X)·I, which lists them all (sm:B1519 K1; the identity is Skuratovskii's Prop. 1, arXiv:2307.13873). **[v1.29] THE PRINCIPLE'S TICK AT THE COMMON POINT (main, B1607; sealed 805e2d488).** The rule a → ab, b → a is L∘P exactly (the swap, then L; a → ba, b → a is P∘R, its mirror), its matrix the golden LP, det −1, σ² = LR exactly; its mapping torus is m000 (SnapPy's single-letter bundles with the reversal flag), of which m004 is the orientable double cover — re-verified. So this fork asks whether the principle's own tick is a move of the weave, and both branches are now computed. At the quaternion point the rule lifts to ±(1 − i − j − k)/2 ∈ 2T (orders 6 and 3; i → k → j); the mirror rule's lift is its k-conjugate, in the same 2T-class, so the common point does not see the rule from its mirror; the inverse rule's lift lies in the other class of order-6 elements, and the lifts of L and R (order 8, outside 2T) exchange the two classes. On the three parities L, R and P act by transpositions, the rule by a 3-cycle, the double tick by the inverse 3-cycle; on every odd-trace word to length eight the sense of the parity 3-cycle is kept by even rotations of the word and inverted by odd ones, kept by the mirror and inverted by reversal, and the oriented fibre orients no parity triangle — the McKay orientation (ω against ω²) is neither a thread invariant nor the mirror bit (the seat's W26, verified on main). **The two hands are complementary:** the records' orientation (T against T̄ on the weave's surface, v1.28) is reversed by the rule and by P and kept by every move; the McKay orientation is kept by the rule and inverted by every move; the double tick keeps both. If P is a move, the weave contains its mirror and its three is achiral (the form of W21 is reversed by P), its object the non-orientable quotient; the chiral three of v1.28 lives on the double tick's weave ⟨L, R⟩ = SL(2, ℤ), whose object is the orientation double cover (m004 over m000 at the root), and the hand is the choice of its sheet, which the rule — the deck involution (B466) — does not make. So **neither hand is derived on the weave**; each is derived on a subweave the weave does not select: a selection, located. GM5c stays OPEN as a fork; what it decides is now computed on both branches. |
| GM5d | Counts are non-negative (positivity) | CHOSEN | A sector restriction, not a consequence of using L and R (R57; the audit lane's operational contract). Not needed to select the root (§4). **[v1.14] It is what excludes the sign (B1482):** −I sends a pair of counts to its negative. Under positivity the grammar generates the + states and, with P, the non-orientable ones; the − states — on which every spin structure carries a hand (B1479, B1481) — are exactly what positivity removes. |

---

## 3. The generated state space

**X_gen = (reachable states, native moves, equivalences, root)** (sm:B1384, adopted 2026-09-27; P022).

**States.** A state is a signed cyclic word s = (ε, w): w is a primitive word in L and R using both letters, taken up to
rotation and the L↔R swap, and ε = ±1. It is realised as the once-punctured-torus bundle with monodromy εw, a hyperbolic
3-manifold with one cusp. **[v1.2]** A word and its reverse are two states realised by one manifold, with the same
orientation; the swap, already divided out, gives the mirror image (sm:B1517 C4, C6). If the swap P is legal (GM5c), the
orientation-reversing bundles join them; the Gieseking manifold m000 is the bundle of LP.
- **Census** (DERIVED; re-derived by sm:B1516 C4 and C5): 2, 2, 4, 6, 10, 18, 32, 56, 102, 186 and 340 states at lengths 2
  to 12, 758 in all, as main's B1434 and B1439 count: **[v1.2]** twice OEIS A000048 summed over those lengths. **They realise
  536 distinct manifolds**, twice OEIS A000046: 222 states pair off as a word and its reverse, the first pair at length 7
  (+LLLRLRR and +LLLRRLR), and SnapPy's isometry signatures give exactly that partition (sm:B1517 C1–C3). A word of length n
  gives a manifold of n ideal tetrahedra: the monodromy triangulation, which is canonical (Goodman–Heard–Hodgson 2008,
  Lemma 3.2; Guéritaud 2006, §3.2). The 24
  states to length 6 are m004 (+LR), m003 (−LR), m009 (+LLR), m010 (−LLR), m022, m023, m135, m136, m039, m040, m234, m235,
  m369, m370, s000, s001, s298, s299, s463, s464, s639, s640, s891 and s892.
- **Levels.** The n-fold cyclic cover of a state (ε, w) has monodromy (εw)ⁿ. Its first homology has torsion of order
  abs(2 − tr((εw)ⁿ)), which is also the number of fibre characters its monodromy fixes. For m004 these orders are 1, 5, 16,
  45, 121 and 320 at n = 1 to 6. The levels M₂ to M₆ are m206, s961, t12839, o10_150696 and otet12_00013 (sm:B1516 C6;
  main's notation Mₙ; the SM seat's older Yₙ is ambiguous, see ERROR_LEDGER E72).
- **[v1.2]** **Signed powers.** For u primitive and k even, −uᵏ is a legal signed monodromy (GM5b) that is neither a state
  (uᵏ is not primitive) nor a level of a state: (εv)ⁿ = −uᵏ would need εⁿ = −1, so n odd, and vⁿ = uᵏ, so v = u and n = k,
  which is even. The audit lane's R78 (sealed 2026-10-02) raised it and tests the bookkeeping at −(LR)². Every hyperbolic
  monodromy is exactly one triple (u, k, ε) ↦ εA(u)ᵏ, u primitive with both letters, since the cyclic word of a
  hyperbolic class is unique up to rotation and swap (Salepci, arXiv:1006.0752, §7). A state is k = 1, and the n-fold
  level of (u, k, ε) is (u, kn, εⁿ). So −uᵏ is a level of a state exactly when k is odd; for k even its seeds are −u²,
  −u⁴, −u⁸, …, a tower above each u. The first is **m207 = −(LR)²**, H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3, in m004's commensurability class
  (its double cover t12839 is m004's fourth level). It was in the record before it was asked about: sm:B1385 §2 S4
  (±(LR)², ±(LR)³, ±(LR)⁴), main B1418's class census and B1224's CS census, among nineteen arcs; R78 recovered it and
  proved it is no level of any signed seed (sm:B1519 K5 reproduces both). The census above counts states (k = 1); a
  count over the full grammar says whether it includes the signed seeds. Their legality is GM5b's (FK4). R78's
  representation is adopted.

**Moves and relations** (sm:B1384; the audit lane's operational contract).

| Relation | What it does | Physical use requires |
|---|---|---|
| Word extension | reaches longer words | an evolution law and a clock before depth is called time |
| Sign | ±w, with inverse moves (GM5b) | operational legality of inverses |
| Cyclic cover (level) | refines a state; monodromy φⁿ | transport of the action, domains and coefficients, not only of cohomology |
| Deck transformation | symmetry of a level | whether it is gauged or kept (fork FK7) |
| Filling | closes a cusp; flat data descend when ρ(slope) = 1 | metric, action and domain matching |
| Orientation double cover | m004 → m000, when P is legal | the semantic type of P (FK3) |
| Commensurability | common finite covers. m004's class has 99 census members, the arithmetic part of B1186's 112-member family (the other 13 share the field but not the class: sm:B1390), and it contains every finite cover | the same as covers |

**Equivalences.** Unbased conjugacy identifies LR and RL: they are conjugate in SL(2,ℤ) by L, since L⁻¹(LR)L = RL (not by
P, whose determinant is −1). The order bit (UNIQUENESS A7) matters only for based data, such as the golden fixed-point
polynomial τ² − τ − 1 of LR against τ² + τ − 1 of RL (sm:B1516 C3). **[v1.1]** B979: at the based level the bit is
load-bearing and it is one bit — it is where φ enters rather than −φ or φ². B1323: it is the placement of the swap
inside the tick, (LP)² = LR against (PL)² = RL. **[v1.2]** B979's record says LR and RL are conjugate "via P"; they are
conjugate by L, as above, and P sends LR to RL, not to (LR)⁻¹ (sm:B1519 K3).

| Claim about X_gen | Status |
|---|---|
| Every legal state belongs to the state space (generated closure) | DERIVED, at the level of definition (sm:B1384) |
| Every legal state occurs in one history | NOT DERIVED |
| All legal states are physically realised together | NOT DERIVED |
| Some arrow of X_gen is physical time | NOT DERIVED (sm:B1384's transition-semantics fence) |
| A rule selects which state is physical | OPEN (fork FK9; main's L229 (iv)) |

---

## 4. The root and its selectors

| ID | Item | Status | Evidence |
|---|---|---|---|
| SE1 | **The selection criterion: the root's first homology is torsion-free.** | POSTULATED | UNIQUENESS A5, motivated by the topology. Alternatives kept: minimal trace selects ±LR (m004 and m003); minimal volume selects m000, and among orientable states leaves the m003–m004 tie, which SE1 breaks (B197). |
| T-ROOT | **What SE1 selects.** For a hyperbolic once-punctured-torus bundle, the torsion of H₁ has order abs(2 − tr) for orientation-preserving monodromy and abs(tr) for orientation-reversing. So H₁ is torsion-free exactly for the class of LR (trace 3: **m004**) and the class of the golden matrix LP (det −1, trace ±1: **the Gieseking manifold m000**). | DERIVED | CLAIMS C3 (the orientation-preserving half, as CLAIMS scopes it); B197; sm:B1516 C2 (every unimodular matrix with entries up to 5, each torsion-free one conjugated explicitly to LR, LP or (LP)⁻¹) and C5 (SnapPy: of 46 orientation-reversing bundles to length 6, only m000 is torsion-free). **[v1.2]** The formula is H₁ = ℤ ⊕ coker(φ − 1) (Chun, Gukov, Park and Sopenko 2019, §2.2 eq. (11)), read with det φ = ±1. |
| SE2 | **Orientation**: of the two, take the orientable one, m004, the orientation double cover of m000 | CHOSEN | P019 A6; UNIQUENESS A3; THEOREM_LEDGER C5. Minimality points the other way: m000 has half the volume and one tetrahedron (sm:B1380; B749 F5 FRAGILE, "the parent"). The most fragile link of the chain (fork FK2). **[v1.1]** What the choice costs is computed (B1234): eight banked walls — no dimensionful quantity, CS = 0, chirality not self-supplied, the CP sign external among them — pass through amphichirality, which an orientation double cover has by construction (40 of 40 census double covers, against 6 of 200 one-cusped orientable manifolds); and the arithmetic route to E₆ does not need the squaring, since π₁(m000) has the same 48 surjections onto 2T. What dropping SE2 would break is not computed. B1003 locks the prices of all seven forks. **[v1.2]** Re-derived (sm:B1519 K4, K6): 48 surjections each for π₁(m000) and π₁(m004). The 6 of 200 are m003, m004, m135, m136, m206 and m207 — the root and its relatives — and the 40 double covers are not matched to them in cusps or size, so the comparison does not pass the third step of the bar (`docs/THE_BAR.md` (**[v1.4]** on main from B1458), comparable objects). |

**The root.** Given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement (Thurston; Riley). In the
audit lane's words (R57): *"In its positive two-record once-punctured-torus sector, m004 is the distinguished minimal
mixed state. Whether that sector, its root, or particular relations have physical priority remains to be derived."*

**Four inputs suffice, and each is needed** (sm:B1516 C8).
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
  into a theorem and a criterion (its C2a and C2b; B1323).
- *P000's metallic family* LᵐP (det −1, trace m): SE1 selects m = 1. The bundle of LᵐP has H₁ torsion ℤ/m, and the bundle
  of its square LᵐRᵐ has (ℤ/m)² (B126's fact (A); sm:B1516 C10). P000 called m = 1 "most-selected, not forced"; SE1 is one
  more selector of it, and, like the others, a chosen one. **[v1.1]** The others in the record: the systole (B92), the
  volume minimum among torsion-free positive words (B197), the unique unitary anyon and the unique superconformal
  chain (B218, B224, B228), the only knot complement of the family (B251: H₁(M_m) = ℤ ⊕ (ℤ/m)²). They do not all
  agree: arithmeticity keeps m = 1 and m = 2 (B125). B1323's census: seven self-application criteria pick φ, and the
  smallest Pisot number of any degree is not φ.
- *The records route* (UNIQUENESS): A1–A6 force LR up to the order A7, by a 144 → 1 collapse on the positive grid. The
  forcing is over-determined: A5 alone and A6 alone each select (1, 1), and the unit-shear axiom A4 already fixes the
  increments, so the collapse is a consistency demonstration rather than a search (main B1422). Without positivity the
  torsion-free hyperbolic solutions are (1, 1) and (−1, −1), both in LR's class (sm:B1516 C1).
- None of the routes derives its axioms from anything weaker (UNIQUENESS §6; main B1422).
- **[v1.1] The words route and the records route are one construction in two presentations**, not two derivations
  (B1323, machine-checked: the Sturmian morphisms abelianise onto exactly the non-negative GL(2,ℤ) matrices; ledger
  C1 ↔ UNIQUENESS A2 + A4, C5 ≡ A3, C4 ↔ A1).

**The root is the emptiest state.** SE1 says that m004's fibre has no non-trivial character fixed by its monodromy, and
among the orientable states only the root has that property. It is also why m004's own level is empty in main's frame:
*"The root has none and cannot: its fibre has no finite character."* (main B1434). The property that selects the root
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
to physics (identification I-26) is UNEARNED.** Each is a named hypothesis. **[v1.1]** F-MC is main's oldest frame and
is of a different kind: it goes from the root's arithmetic to a gauge algebra, not from flat bundles to counts.

| ID | Frame | What it computes | Where it lives |
|---|---|---|---|
| F-FC | Free-cusp frame | bulk matter with the Standard Model unbroken; a chiral count needs a free cusp, one whose peripheral rank in H₁(M; ℚ) is below b₁ | the SM seat's branch, sm:B1368–sm:B1399 |
| F-CI | Class-index frame | main's index I = n(V) − n(V*) on reducible non-split doublet modules in the E₆/27 frame; generation-shaped backgrounds | main, B1297 and B1418–B1451; verified on the SM seat's branch (sm:B1374, sm:B1375) |
| F-MC **[v1.1]** | McKay cascade frame | the root's trace field ℚ(√−3) has one ramified prime, which gives π₁ → 2T; McKay gives E₆; the fused cascade ends at su(3) ⊕ su(2) ⊕ u(1)³, with the global form [SU(3)×SU(2)×U(1)]/ℤ₆ and the hypercharge direction | main: B248, B266, B862–B864, B892, B992–B994; one theorem with its counted hypotheses in `docs/THE_CLAIM.md` §1 (B1014) |
| F-HE | Harmonic E₈ frame | E₈ ⊃ SU(5) × SU(5)′ on the harmonic convex-projective vacuum; rank-five extensions W with N(10′) = −I(W) and N(5̄′) = −I(Λ²W). **[v1.16, the SM seat's P8, read on main at headline level]** At a finite-order member on any finite cover, at every class and in either order: N(5̄′) ≤ n(ν³ ⊗ ρ) and N(10′) ≤ b0 + n(ν⁴), so g generations need both supplies ≥ g (sm:B1535, Theorem C). **[v1.16]** And by the seat's floor read as a mechanism (B1487): a count in this frame is a count of ends, and its four is blind to the spin structure (GAP1) | the SM seat's branch, sm:B1509–sm:B1515; the audit lane, R40–R76 |
| F-AP | G₂ apex frame | matter at cone points of a G₂ space built over the cusps; anomaly inflow | the SM seat's branch, sm:B1355–sm:B1365 and sm:B1500–sm:B1505 |

The frames disagree on the same objects. Every word state is closed in F-FC (one cusp and b₁ = 1, so no free cusp: sm:B1385),
while 95 of the 758 carry a generation-shaped background at their own level in F-CI (main B1439): **[v1.2]** 87 of the
536 manifolds they realise (sm:B1517 C5). **A result is a statement about a frame applied to an object, never about the
architecture as such.**

**[v1.1] F-MC by object.** Run on the root only. Reaching E₆ is generic — about one manifold in three, five of seven
grammars (B993, B996) — while the golden is the unique metallic grammar whose own-conductor shadow is a McKay group
(B997, B1002); m004's siblings have no door (B1019); m000 has the same door (B1234). Its inputs beyond the root are
counted: five typed external data in `docs/THE_CLAIM.md` §1 (B1014, B1017), eleven irreducible identifications
(B1266), 39 of 43 ledger links forced (B1123), the freedom ledger (B1028). Never computed on another word state.

Where each frame has been run, by object (as of v1.0):

| Object | F-FC | F-CI | F-HE | F-AP |
|---|---|---|---|---|
| m004 and its cyclic levels Mₙ | closed: one cusp and b₁ = 1 (sm:B1368; sm:B1385) | M₁ and M₂ carry no generation-shaped background; M₃ to M₆ carry 48, 256, 400 and 2 160, each counting ±1 (main B1432, reproducing the SM seat's level census) | computed: at the μ = −1 points a 10′ without its 5̄′ (sm:B1509); at q = 1 both halves on one background, with opposite signs (sm:B1515). **[v1.3]** These counts sit on non-split configurations. On the reductive ones, the vacua of the harmonic family, the count is zero for every q > 0 and every central twist, by proof (main B1455; independently sm:B1520). **[v1.6]** On the levels M₁…M₁₂ the count-odd mirror of those vacua breaks from M₅ on, off the unit circle exactly where no golden Galois reflection fixes the twist, and every one of the 196 firing members of levels 1–6 is fixed (sm:B1522). **[v1.16, the SM seat's P5, read on main at headline level]** On every finite abelian cover of M₂–M₆ no λ = 1 pulled-back member carries a generation-shaped count, at any class, in either order (sm:B1532, NEGATIVE, run as sealed; two routes, 68,596 counts each); the members at κ⁵ = 1 add none | m004's cusp (shape 2√−3) is not hexagonal, so sm:B1501's cones do not complete it; the apex designs are conditional (sm:B1355–sm:B1365) |
| m004's commensurability class (99 census members; every finite cover) | B1186's 112: 108 closed (sm:B1369), four cusps open on one Fourier coefficient each (sm:B1370); the cover cube~3.24 counts ±2, but the count moves with the cusp cut (sm:B1386–sm:B1388) | fires on five arithmetic members: s958, v2873, t12833, t12835, o10_150701 (main B1418; sm:B1374) | **[v1.16, the SM seat's P6, read on main at headline level; a statement about this named list, which FK13 rules is not the object]** the finite abelian covers of the levels (sm:B1532: no generation-shaped count); every connected cover of degree ≤ 12 of m004 and m003 and their Q₈ towers (sm:B1536, NEGATIVE: no three; room reaches two on sixteen degree-10 covers of m003); on N₄₅ no three at the trivial character at any class (sm:B1541, reproduced on main; sm:B1544, sm:B1546). Under FK14 every one of these is a search for ends | hexagonal cusps (m003's, three of cube~3.24's four, 14 of m004's 87 covers of degree ≤ 10) match sm:B1501's cones conformally; a cusp point is chiral only where its locus meets another fixed set (sm:B1503) |
| The other word states (758 to length 12; **[v1.2]** 536 manifolds) | closed (sm:B1385 T1) | 95 carry a background at their own level (main B1439; **[v1.2]** 87 of 536 manifolds, sm:B1517 C5; no criterion in the fibre torsion and the sign decides which, sm:B1518; **[v1.4]** re-derived on main by manifold and group structure: 22 (G, sign) strata each hold a firing and a silent manifold, the smallest m369 against o9_00001, both ℤ/12 and sign −, B1458), among them m369 (8) and s639 (16) (main B1434) | **[v1.6]** each is rigid rel cusp, so carries a one-parameter projective family at its hyperbolic point, and on 262 of the 536 manifolds no isometry dualises it (sm:B1523). **[v1.16, the SM seat's P7]** Counts at the hyperbolic point: one generation in one W on the silver squares m135 and m136, through interior classes of the four, and none on the golden word states (sm:B1530 — **read by main's instrument and independent code, B1485: every count agrees; and at every member the two orders fuse into an irreducible module that counts zero, B1486**); at most one on every finite abelian cover of m135 and m136 at the pulled-back members (sm:B1534, read at headline level); at most one at every finite-order member and every class of every word state and level (sm:B1535, Theorem C with Lemma W, read at headline level) — and at most 1 + b0 on any one-cusped state by the floor (B1487): the one generation is a cusp on which the class dies | never computed |
| m010 (−LLR) | closed | none at its three-fold level (main B1434) | the audit lane's R40: I(W) = I(Λ²W) = +1, an anomaly-free 10 + 5̄, on a block with no harmonic background (F01) | never computed |
| m000, the Gieseking manifold | never computed | never computed | never computed | never computed |

---

## 6. Scope tags (mandatory from sm:B1516 on)

Every banked result carries a scope tag with four parts:
- **frame**: F-FC, F-CI, F-HE, F-AP, another named frame, or "none" for a result about the grammar or the state space
  itself;
- **object**: a state, a family (for example "m004's convex-projective family"), a class or set of states (for example
  "m004's commensurability class", "the word states to length 12"), or "all once-punctured-torus bundles";
- **reach**: "single" (one state, with the deformations or levels its hypotheses name), "class" (a named class or set of
  states) or "general" (every state of the grammar, or every manifold of a stated kind);
- **hypotheses**: what else the result needs (an end condition, a level range, q ≠ 1, and so on).

**[v1.2]** A count over states names its unit, word states or manifolds: a word and its reverse are two states and one manifold
(§3). **[v1.12] "The family" names its set (the web seat's A3, adopted as a naming rule).** At least five sets have been
called "the family" on the record and in the seats' reports: the word states X_gen (§3); m004's commensurability class;
B1186's 112; the regular-tetrahedral class; the amphichiral members of B1474–B1477. A statement true on one is false on
another — measured: on X_gen's primitive word states to length 8 (74 hyperbolic realisations) the Chern–Simons class is
rational on 18 and irrational on 56, and 16 are amphichiral with class 0 or ¼ (reproduced on main, B1478), whereas the
1/24 lattice of B1476 is a fact of B1186's 112. From v1.12 a scope tag's `object` names the set, and the bare phrase is
not used in a verdict line. Which set the owner's rule of 2026-10-04 means was fork FK13 (§8); **[v1.13]** it is ruled by the principle: the word states. An arc also records what it swept before it claims anything, in the repo and in the literature (§0).

The tag lives in an arc's verdict file (field `scope`) and in each kill-graph entry (field `scope`). **On main**, from
B1454 on, `tests/test_arc_verdict_schema.py` requires it of every new arc and of every new kill-graph entry. **On the
SM seat's branch**, its schema test requires it from sm:B1516 on, and every kill-graph entry it wrote from sm:B1369 on
carries one. A negative blocks only where its tag reaches (WORKING_RULES on main, the rule of 2026-10-02 on scope;
the SM seat's amended mandate of 2026-10-01).

---

## 7. What is not claimed, and the distance to physics

**Not claimed:** that every state is physical; that any arrow is time; that any state is selected; that any frame is
physics; any Standard-Model parameter (**0 of 19**).

**Six gaps** (the heading corrected from "five" at v1.15 — the SM seat's proposal P1, sm:B1537), none of which work on one state can close:
- **GAP1, the dictionary.** No frame is derived (I-26). Until one is, a count is mathematics about a flat bundle.
  **[v1.15] Two facts about every count on the record (B1487).** (i) The class index I(E) = n(E) − n(E*) is mirror-even for
  every module: cohomology dimensions do not change under pullback by a diffeomorphism or under complex conjugation, so a
  mirror carries a module at a spin structure s to one at its partner s′ with the same index. No choice of module makes a
  count see the hand; the hand lives where cohomology vanishes (the odd modules of the lift are acyclic on every word state,
  their torsion's phase is the hand, B1481) and can enter a count only as the choice of order (B1466, B1486). (ii) In the
  harmonic E₈ frame the internal SU(5)′ contains the geometry's own structure group, SL(4) ⊃ SO(3,1): its 10′ and 5̄′ are
  extension classes of the Lorentz vector bundle, and the four is ρ ⊗ ρ̄, blind to the spin structure. A frame is a
  hypothesis; this one is a hypothesis of that kind.
- **GAP2, the ends.** Chiral counts live at cusps, which have continuous spectrum, and they depend on an end condition that
  is chosen rather than derived. Over the end conditions, sm:B1509's 10′ count is 0, 1 or 2 (sm:B1392 places the count at the
  ends). sL-8's rule forbids choosing an end to rescue a count.
  **[v1.15] Sharpened (B1487):** in the harmonic E₈ frame a count IS a count of ends — the SM seat's floor
  I(W₁) ≥ k − m_A − b0 (sm:B1544, sm:B1545; checked on main on 390 readings) bounds it by the cusps on which the character is
  trivial and the class dies, so g generations need at least g − b0 such cusps **[v1.17: and the count is bounded on the other side too, I(W₁) ≤ 2m_A + m_B − b0, the seat's ceiling — every value of it, not only the generation side, is a count of ends; the two-sided form B1487 first wrote was withdrawn on the seat's correction]**; in main's frame F-CI three sits on two-cusped
  members and is excluded on one-cusped manifolds (B1291, B1418). **A generated state (§3) has one end; no state of X_gen
  carries three generations in either frame, by counting ends, not by search.** The question is FK14. **[v1.18] On the first several-ended
  objects read (B1492: three and five ends) the count at every interior class of a sign character is one — the ends enter the floor, not the value. [v1.19] And at every character of order ≤ 8 the count at a member is exactly b0 + n(ν⁴) with n(ν⁴) = 0 (B1493): the generation is the trivial line; what reaches two on the record is a line with room on a cover chosen by a character. [v1.20] The room is closed-surface homology (n(1) = b₁ − ends); no companion has any at the trivial line (T-COMPANION-NO-ROOM), one companion has it at eight sign characters trivial on no end (B1494) — the ends and the room are separated on the family and meet on N₄₅.**
- **GAP3, the source.** Chirality sits on non-split bundles, which carry no harmonic metric without a source (sm:B1378, by
  Corlette–Donaldson; the audit lane's F01 and R41). **[v1.3]** What the source must be is on the audit lane's record,
  read on main and not re-derived there except where said: one balance for each step of the ordered flag of the
  non-split module, each with a definite sign — a scalar source pairs to zero with all of them, a non-central
  direction pairs (12, 8, 4) and its negative (−12, −8, −4) (R41; the table re-derived, main B1457); the source may
  be supported in the compact core (R76), or the balance may be paid by flux through an end (R41, R80); an added
  source model does hold the counted configuration, at the price of infinitely many undetermined flat directions
  (R77). **So a count needs three things together: an order of the pieces, an open end, and a source or a flux of
  the right sign.** [v1.5] The audit lane's qualification (its reply of 2026-10-03, read on main, not re-derived): its results
  prove that a specified flat counted configuration needs an admitted source, an end flux, or a change of hypotheses; they do
  not prove that a one-ended state can get the third *only* from a relation — whether a generated relation supplies it is FK8
  and FK12, and R77's added fields do not settle their origin. No report derives the source.
  The counts on record that wait for one: +1 and +1 on m010 (R40), a conditional three on a two-ended exterior with
  sources between its ends (R19, R24), −3 on levels three and six for a rank-six coefficient induced from a cover
  (R69) — each fenced by its author as not a physical count.
- **GAP4, selection and coincidence.** With hundreds of states, four frames, many levels and several end conditions, a
  Standard-Model-like feature somewhere is expected by chance. A selection rule and a null model must be fixed before a
  match counts. **[v1.2]** The null model and the grading are fixed: `docs/THE_BAR.md` (**[v1.4]** on main from B1458) (sm:B1518), a card, the base rate
  in a named unit, the comparable objects, selection and trials, and B614's gate p < 0.01, graded DERIVED (**[v1.6]** PASSED since sm:B1524: a rarity screen, not a derivation), REPRODUCED,
  FITTED or UNJUDGED. Nothing in the record clears it: the root's higher levels fire as their neighbours do (REPRODUCED),
  m369 and s639 were found by a scan (FITTED if offered as evidence), and the harmonic frame's counts are UNJUDGED. The
  selection rule (FK9) is still open.
- **GAP5, dynamics.** Topology yields integers and discrete structure. The 19 values need moduli, symmetry breaking and
  running, which no frame has produced. **[v1.1]** v1.0 said the architecture "does not have" them; as a statement
  about the record that is too strong. Main's sweep of dynamics and chirality concluded that neither is missing as
  structure (B944): a monodromy-preserving flow and a positive-entropy Painlevé VI solution (B169, B317), the root's
  own gravitational action with no free dimensionless constant (B1088), an action that exists exactly at the
  monodromy (B1341), a native gauge system (B715) — and no intrinsic time (B721). The gap is the narrower one: none
  of it has been turned into a potential, a breaking or a running that fixes a value.
- **[v1.9, narrowed v1.11] GAP6, the flatness.** Every frame on this page is a frame of flat bundles, and a flat bundle has
  ch = rk: no characteristic-class index on a CLOSED bulk can tell 27 from 27̄ over it (Chern–Weil; the record's Chern–Weil
  row). **[v1.11]** That is the whole of what flatness forbids. With the object as boundary — this page's setting — the
  index carries the boundary's spectral term (Atiyah–Patodi–Singer's η), a flat-structure quantity; the record's class
  index I = n(V) − n(V*) (B1297) is a flat-bundle quantity that fires at ±1, ±2 on the family (B1418); and the mirror's
  action on the spin structure — a flat datum — is genuine on seven amphichiral members and absent on the knot (B1474,
  B1475). So the flat frame reaches DISCRETE data (counts, bits, signs) through the boundary and cannot reach CONTINUOUS
  MODULI (a mass, a coupling that the construction leaves free): the record's value-negatives are theorems about flat
  moduli and bound the frame, not physics (lead L247; the census of 173 value-kills, 107 on flat premises). **[v1.12]**
  The v1.11 wording said "continuous values" and over-reached the other way (the web seat's A2): a rigid flat point is
  not a modulus and fixes continuous numbers exactly — on m004 the volume (3√3/2)·L(2,χ₋₃) and the Kashaev
  expansion (B598, B722; the dilogarithm atom verified in B1476). Those are numbers of a member, fixed; none is a
  Standard-Model parameter, and the count of §7 does not move. Narrowed on two readings of the same day from
  opposite sides — the audit lane's R89 ("narrow GAP6 to its smooth closed bulk spin-Dirac hypotheses") and the web seat's
  handoff ("the wall is a flat-sector theorem") — against main's own v1.9 sentence, which had dropped the hypotheses.
  What remains of the gap: the continuous moduli; and the step from the boundary's η to a physical count (B279's
  unbanked link, L246 Phase 2). **[v1.12] "A frame with curvature" is necessary, not sufficient (the web seat's A1,
  derived):** on a smooth closed bulk of dimension n the Dirac index ∫Â·ch(V) takes ch_k only with n − 2k ≡ 0 (mod 4),
  and ch_k(V̄) = (−1)^k ch_k(V); so ind(V) ≠ ind(V̄) is possible only for n ≡ 2 (mod 4). A four-dimensional bulk, curved
  or not, cannot tell 27 from 27̄; a six-dimensional one can. No frame of the right parity is on the record (§8).
  **[v1.12] Where the bit is decided (B1477):** a mirror that acts on an invariant cusp torus by a rhombic involution
  fixes no spin structure whose longitude has trace −2 (Theorem A, proved); every one-cusped amphichiral census
  manifold at Chern–Simons class ¼ is of that kind (75 of 75). The bit is a parity of the boundary torus' lattice. **[v1.16, the SM seat's P2 (sm:B1533 C3–C6), in main's words]** The sentence "no characteristic-class index on a closed bulk can tell 27 from 27̄" holds for Dirac indices and for every count on a closed or sealed problem; it does not bind the class index on an open end, which tells a module from its dual on flat modules of one Chern character — the seat's M₄ at ν = (1/3, 0) reads +1, −1, 0 on the non-split module, its dual and the split sum; main's B1466 and B1486 read the same pattern at m004's counted point and at the silver members. A flat frame's count can tell a module from its dual; **what it cannot do is see the hand: the class index is mirror-even for every module (B1487, T1)**, so whether such a count is a physical chirality is GAP1 and the order is a choice. Named as a gap on the web seat's reading of
  2026-10-03 (lead L244), which sorts the record's negatives into three kinds — symmetry pairing things that cancel, the
  absence of curvature, the absence of uniqueness — with three remedies: a breaking (GAP3, FK12), curvature (this gap), a
  selection principle (GAP4, THE_BAR). The remedy for this one is a frame with curvature; none is on the record.

**[v1.2]** **The gaps and the observer.** Several open items of this page are, under other names, closings in the record's
observer line. The object supplies four incompletenesses (space, time, charge, value) and the observer supplies every
closing — a filling slope, an arrow, a chirality (a Galois sheet), a basepoint; "measurement is the symmetry-breaking
choice" (B717, with B716 and B723). **[v1.9]** A fresh reader (the web seat, 2026-10-03; lead L244) reached this sentence from the record's negatives alone — every positive at an interface, none in the object — without having read it here: taken as confirmation that the thesis is forced by the data, not as a new reading. **[v1.3]** B723's identification of that choice with a thermodynamic breaking is
withdrawn in its own banner: complex conjugation is not in Gal(K^ab/K) (B942), the value torsor failed the same
identification (B957), and the breaking has no order parameter at the manifold level (B849). That the apparatus was
built does not repair those maps. **[v1.6]** What survives is the structure: a measurement as a choice of fibre functor
with a Galois ambiguity, without either group assignment (the audit lane's AR6; sm:B1521 C4). The end condition chosen
rather than derived (GAP2, FK10) is the space closing.
SE2's orientable root is amphichiral by construction, and eight of the record's walls pass through that amphichirality
(§4, B1234), among them no dimensionful quantity, CS = 0 and chirality not self-supplied: at the archimedean place the
object fixes only what is mirror-even and dimensionless, and the mirror-odd orientation and the scale are the
observer's (B1168, OPEN). The record went further. THEOREM_LEDGER C18 prices the line: the object is "a fully
transparent, self-naming, integrated speaker that cannot choose" (B759–B762). It names itself and cannot sign itself,
and the missing sign is one ℤ/2 class, the orientation (B1183 and B1184, PROVED; B1163 and the synthesis B1169, OPEN).
Main's B1327 (OPEN) proposes re-typing most closings as relations, invariants of a pair that need a partner rather than
an act; only a choice with neither an invariant selector nor a relation needs anybody. v1.0 did not carry the line,
and v1.1 lists C18 beside F-MC (§9). Whether the closings belong to the genesis is fork FK12 (§8).

---

## 8. Open forks, each with what would settle it

| ID | Fork | Now | What would settle it |
|---|---|---|---|
| FK1 | The principle's single wording (§1) | **[v1.5] CONFIRMED** (the owner, 2026-10-03) | nothing; the measurer is not in the principle — it is FK12, where it can be computed and paid |
| FK2 | Orientation (SE2) | CHOSEN | a derived reason for orientability (Pin structure, time reversal: sm:B1382, sm:B1383, sL-3), or carrying both m004 and m000 as states |
| FK3 | The swap P: legal move, and of what type | OPEN | an operational meaning for P (redescription, parity, time reversal) that the frames can test. **[v1.2]** B1083 types the swap as the C-type bit and the reversal as a parity bit, with the arrow on neither (read with main's naming addendum); conjugation by P sends LR to RL, not to (LR)⁻¹, and LR is conjugate to its inverse by J = [[0,1],[−1,0]] in SL(2,ℤ) (B16; sm:B1519 K3). On m004 the swap, the arrow and the mirror carry one relation: its eight isometries act on the cusp by diag(s_m, s_l), each sign pair twice, with orientation sign s_m·s_l; main's B1327 (OPEN) reads s_m as the arrow and s_l as the swap, so the mirror is the swap times the arrow, and asks, without asserting it, whether the genesis books one of the three bits twice (sm:B1519 K7) |
| FK4 | Inverse moves (GM5b) | OPEN | operational legality; until then the signed states are an extension of the grammar. **[v1.13] Its stake (B1479):** the sign − of a word state is the monodromy with the fibre's elliptic involution, −I = (L·R⁻¹·L)², which needs an inverse letter; and on every amphichiral word to length 12 the − state is the one on which no spin structure survives the mirror (rhombic cusp, Chern–Simons class ¼), the + state the one on which nothing at the cusp forbids it. So FK4 now reads: **does the principle generate the sign?** If it does, the place where a hand can be registered on a fermion emerges; if not, it is an added choice. **[v1.14] Sharpened (B1482):** the sign needs no inverse letter — only the central move −I, the negation of both records; words in L, R and P never give it (their entries stay non-negative), and no − state is the square of any act (tr X² ≥ −2 in GL(2,ℤ), tr(−w) ≤ −3), so act-plus-register cannot produce one. The fork is: **is negating the records a legal move?** Positivity (FK6, CHOSEN) forbids it; PF1's own verb — cancelling — names it (a reading, not a derivation) |
| FK5 | Faithful F₂ against its abelian quotient (GM4) | OPEN | an observable that needs word order or the commutator |
| FK6 | Positivity (GM5d) | CHOSEN | a reason the physical states are the non-negative cone. **[v1.2]** One candidate is on record and not adopted: B1083 reads positivity as the arrow's home, "never a choice" |
| FK7 | The deck: gauged or kept | OPEN | an action in which the deck acts (sm:B1506) |
| FK8 | The join: which maps carry physical data between states | OPEN | a demonstrated physical map (action, domains, anomaly account) beyond covers; filling descent is one candidate (sm:B1508, R57) |
| FK9 | Selection: what makes a state physical | OPEN | a rule fixed before computing, graded by `docs/THE_BAR.md` (**[v1.4]** on main from B1458) (**[v1.2]** sm:B1518; GAP4). **[v1.6]** Its null contract (sm:B1524) names the laws under which the bar's p is a probability, corrects several looks by Bonferroni, and renames the top grade PASSED: a rarity screen, necessary for WHAT_WOULD_COUNT's DERIVED and never sufficient for it, and never a physical admission. **[v1.2]** A symmetric law can have states its symmetry does not fix: main's B1455 (sealed 2026-10-02, not yet run) tests whether each vacuum of the bridge's harmonic family on m004 is fixed by a symmetry under which the count is odd; a vacuum fixed by none comes with a mirror partner of equal action. **[v1.3]** Run (main B1455, NEGATIVE, scoped to F-HE on m004's harmonic family at level one; independently sm:B1520, the same outcome with the same witnesses): every vacuum is fixed by a count-odd symmetry, the knot's inversion followed by dualising, so no vacuum of the family carries a count. The geometric mirror does not change a count at all; dualising does (main B1297, B868, B871). The family's vacua do break half the symmetries, a mirror among them, with no count attached. Silent on a sourced vacuum, on other states and on selection by a relation. **[v1.6]** Carried from the SM seat's v1.3 (sm:B1521 C1, with sm:B1512 Lemma I): B1297's period-2 symmetry P is the fibre's elliptic involution, whose extension to every level is main's B1459, and in Ballas' presentation it is the swap's class; it fixes ρ_q (sm:B1526 C3: on m004 it is the one non-trivial outer class that keeps the orientation and the base, and it inverts the fibre's homology). So B1297's tower theorem (P inverts every twist) and the family's (the inversion dualises ρ_q) rest on different symmetries. Run since on the levels (main's L242 (b); sm:B1522, PROVED, frame F-HE): the count-odd mirror breaks from M₅ off the unit circle and from M₆ on it, up to 0.91 of M₁₂'s 103 680 vacua; off the circle it breaks exactly where no golden Galois reflection fixes the twist; and every one of the 196 firing members of levels 1–6 is fixed, so the mirror breaks only where nothing chiral has been found. On the word states (sm:B1523, PROVED): every word state to length 12 carries a one-parameter projective family at its hyperbolic point; main's one-bit rule (an isometry dualises the family exactly when it inverts the fibre boundary) holds on all of them; and on 262 manifolds (482 states) no isometry dualises the family, so near the hyperbolic point B1455's symmetry argument cannot force the count to zero there (Lemma T, a local statement). Whether it is nonzero is the SM seat's sL-10 item 8, sealed first. The owner's hypothesis of 2026-10-02, "choice might be golden", was tested in these two sealed forms: on the levels, off the unit circle, a golden Galois reflection decides where the mirror breaks; on the word states, of the 14 manifolds with golden monodromy field exactly ±L⁴RL³R² and ±L⁴RLR³LR² are mirror-broken, selected by their words, not their field. **[v1.16, the SM seat's P3]** Answered near the hyperbolic point (sm:B1527, PROVED, run as sealed): no vacuum ν ⊗ ρ or ν ⊗ Λ²ρ of a finite-volume projective deformation near the hyperbolic point has a non-zero index, on every word state to length 12, mirror-broken or not — the character is trivial on the fibre boundary, a commutator, and on the finite-volume curves that boundary has no eigenvalue 1, so the cusp is acyclic. **Part H, the hyperbolic point itself, verified on main by a route sharing nothing with the seat's (B1465):** on ±LLRLRR and ±L³RLR², at the parabolic points of their periodic curves, for every fibre character and seven twists of the meridian, 7 364 indices, all zero |
| FK10 | The end law | OPEN | an end condition derived from physics (sL-8) |
| FK11 | The dictionary (I-26) | UNEARNED — **[v1.27] UNEARNABLE within F-HE and F-CI on any thread or cover of a thread (T-NO-INDEX-IN-THREE, B1604):** every twisted Euler characteristic on a cusped 3-manifold vanishes, so no count of flat-module cohomology there is an index with the physical shape identity n_5̄ = n_10; the class index is a difference of interior ranks in degrees one and two, governed by no characteristic class (B1603: eight kinds of reading on 442 classes). What would earn a dictionary: an even-dimensional object the weave forces, carrying a non-flat bundle whose index is the count, or the orbifold standard read as what it is — a sector selected by a character, a selection | a frame derived from M-theory or from the principle, with its scope proved; or an even-dimensional object of the weave with a non-flat bundle |
| FK12 **[v1.2]** | **[v1.5] The register** (the owner's framing, decided 2026-10-03). The genesis generates a word. The word keeps the order of its letters (ab against ba); the manifold forgets it — a word and its reverse are one manifold (B1456) — and the vacuum forgets it again — a direct sum has no order (B1438, B1455). **Is the register that keeps the order part of the state, carried by the act, or an input from outside?** Four sub-questions, each with a computation: (i) at which step is it dropped — word→manifold and module→vacuum are the two found; the fibre's involution reverses the order with a sign (B1297, B1459); (ii) is the choice binary or richer — the record holds two bits (the mirror c; particle against antiparticle) and one order; (iii) both outcomes at once or at different relations — the slope law gives one term per order, and side by side they sum to zero (L241); (iv) "if it can happen it will" — plenitude, a hypothesis to test, not a premise. What the record does not show: that the act generates the register rather than receives it. The earlier form of the question: are the observer's closings part of the genesis, or inputs beyond it? (THEOREM_LEDGER C18 makes them inputs; the SM seat's wording of 2026-10-02: does the act emerge with its observer, the tracker of ab against ba?) | OPEN | for each closing, a partner that supplies it as a relation (main B1327, OPEN) or a proof that none can. Within the object the sign is settled: the object cannot sign itself (B760, NEGATIVE; B1183, B1184, PROVED), and no rule built only from its own invariants selects it canonically (B1225; its self-name is mirror-even, B1184); the trace map conserves κ = tr[a, b] and never reads it (B20, B37). A symmetric law can still land in a state it does not fix (FK9, main's B1455). The owner's framing decides whether the genesis generates the partner with the act. **[v1.3]** Three things the record adds, and one qualification. (i) There are two signs, not one: "which way" — the mirror bit c of the observer line — and "which of a pair is the particle" — the linear exchange of a module with its dual, under which a count is odd and c is absent (B868, B871; B1455). (ii) In the class-index frame a count is the *order* of the two pieces of a non-split module: the slope law gives it as one term for each order and says when the order counts (main B1438), the fibre's period-2 involution P carries a module to its dual up to a meridian sign — it reverses the order by itself, and followed by dualising it fixes the module (B1297; **[v1.7]** main's B1459, on every complete point of 16 levels: ι̃*V ≅ V* ⊗ ε, so I(V) = −I(V ⊗ ε) and the index is zero; the earlier wording "followed by dualising reverses the order" was main's and is withdrawn) — and a vacuum in the harmonic sense is a direct sum, which has no order. **[v1.9]** At the counted point itself (main B1466, sealed): the two orders count −1 and +1 and are each other's dual seen through the inversion, so their counts are opposite by L1–L2; the mixed direction is unobstructed and leads to an irreducible module — the two pieces fused — that counts 0, as the direct sum does. The flat configurations near the split point are richer than a bit; **the count is a bit**: ±1 on the two orders, 0 side by side, 0 fused — "both at once" cancels. A source along one line does not choose (t and −t are the same extension); a source on both lines drives into the fused, count-zero region unless the potential's mixing quartic returns it to an axis — a quantity on no report. **[v1.10]** Exact, from the SM seat's sm:B1528 (its own code at m004's complete point): for modules with no meridian twist the sign is the SL(2) factors' own, as in B1459; a meridian twist t ↦ λ enters squared, P*V ≅ V* ⊗ (t ↦ λ²), so P carries V to its dual up to a sign exactly when λ² = ±1 — main's B1465 computed the twisted indices zero on four states regardless. On Ballas' family P fixes ρ_q, which is not self-dual for q ≠ 1. (iii) The audit lane's act-and-register audit gives a test for where a register is lost: a reduction keeps it exactly when both the updates and the declared outputs descend, and all future outputs define the coarsest record that suffices (its ACT_REGISTER; read on main, not re-derived). The qualification, the audit lane's: B37's "never reads" rests on a detector of a symbol's presence, which an inserted factor r − I at r = I flips without changing the dynamics; its reads-and-branches criterion is not tested by that detector. Main carries the question as the standing lead L241. **[v1.6]** Carried from the SM seat's v1.3 (sm:B1521 C2–C3): B130 shows that κ takes a continuum of values on the fixed locus, but its reading that a unit is internally fork-free rests on an elimination that cannot exclude isolated components (the audit lane's AR4), so the componentwise question is open. For the register question, the record's registering datum at the group layer is B599's pairing datum, whose evaluation A = mult_ρ − mult_ρ̄ is odd under the θ swap (B871). Kept apart from the register question, as the SM seat's v1.3 kept it apart from the owner's act-and-register priority of 2026-10-02 (the audit lane's P_ACT_AND_REGISTER_2026_10_02 (a page of the audit lane's branch, not on main)): the experiential question, an explicit hypothesis held under Gate 5-Q (`philosophy/GATE5Q_PHENOMENOLOGY_FIREWALL.md`), never a consequence of the register question and never a claim |
| FK14 **[v1.15]** | The ends (B1487): does the genesis generate states with several ends, or are generations not ends? | OPEN | a move of the grammar that adds punctures — none is named in §2, and a level (§3) adds none — or a frame whose count is not a count of ends. Bears on it: the LP seat's LP01 (is a manifold covering both m004 and the two-cusped members where three appears reached from the root by a cover?), the SM seat's P6 (the commensurability class as the object; ruled against by FK13), and GAP2. Until it is ruled, a count of three on a cover is a selection, graded by `docs/THE_BAR.md`, not a derivation. **[v1.17] The first candidate answer, the SM seat's fixed-point companions (its note of 2026-10-07; registered, not adopted):** every word state has a canonical several-ended cover — the maximal abelian cover to which the cusp lifts, the mapping torus of the monodromy with every fixed point punctured — with ∣2 − tr φ∣ ends, one per fixed point, determined by the state alone (Proposition 1, the seat's proof); m004's is itself, m003's is o10_150729 = S³ − L10n113 (five ends, A₅ on them), m136's has four ends, m135's eight; and on m003's and m136's companions no member carries three (the seat's Proposition 3). **Verified on main (B1491):** o10_150729 is isometric to L10n113; +LLLR, whose monodromy has trace 5, has a three-ended companion — the link complement L8a15, chiral, symmetry group of order 12. So "an end" has a candidate meaning in the grammar: a fixed point of the act. What is not derived: that the companion is a state the genesis generates (it is a cover chosen by a character), and any count on one. **[v1.18] The first read of a companion (B1492, sealed):** on L8a15 and on o10_150729, at every sign character of the four, every interior class reads (I(W₁), I(Λ²W₁)) = (−1, −1) with the class dead on every end — the count is one wherever it is not zero, on three ends and on five as on the one-cusped m135 and m136 (B1485), whatever the number of ends on which the character is trivial (the floor's room reaches three on the five-ended companion and the value stays one). On L8a15 no character trivial on any end has an interior class at all; its members sit where no end carries the character, as m136's do. In F-CI L8a15's order-3 isometries cycle the ends and fix no cusp, and its cusps are not hexagonal: no three (B1490's two conditions both fail). Evidence for the fork's second half — the ends raise the bound, not the value, at sign characters; not ruled: characters of order four and eight on the companions, where b0 = 0 and the bounds change shape, and non-unitary ones. **[v1.19] The room (B1493, sealed; a scoped NEGATIVE):** the SM seat's Theorem C (sm:B1535) caps the count at a finite-order character by b0 + n(ν⁴), the room of the line L = ν⁻⁴, and by n(ν³ ⊗ four). On both companions the line has no room — n(ν⁴) = 0 at every sign character of L8a15 and of o10_150729 — so at order eight the cap is 0 and at order four or two it is 1: **no character of order ≤ 8 on either companion carries three generations, or two**; read directly on L8a15 at every order, every member counts exactly −b0 (sign (−1, −1); order four (−1, 0); order eight (0, 0)) — the generation is the trivial line and nothing else. What moves the count on the record is the room of the line: N₄₅ (the seat's golden cover: degree 45 over m003, the 5-fold cyclic cover of a degree-9 cover along a character; H₁ = ℤ⁹ ⊕ (ℤ/2)²) has room 3 and reaches two (sm:B1547); the companions the state determines have none. Not ruled: characters of other orders and non-unitary ones; a line with room on an object the genesis determines. **[v1.24] The weave's three (the SM seat's W1–W4, verified on main at B1600):** the two records have exactly three non-zero parities; each move fixes one and any two moves cycle all three — the three belongs to no single move (W1); every act of odd trace is a 3-cycle on them (the parity lemma, 988 signed words); the one point of the fibre's characters every move fixes is the quaternion point (W2), from which every odd-trace thread — m004, m003, +LLLR among them — receives the binary tetrahedral group 2T with A₄ below (W3, 54 words to length six); the shared fibre carries one line per non-zero parity and every odd-trace thread acts on the three as one irreducible A₄ triplet, split on even-trace threads (W4). READING, not adopted: the three generations are this triplet — the orbifold standard realised on the shared fibre with no thread chosen. Decisive and open, **W6:** whether each parity line carries a generation (5̄ + 10 with its chirality), which needs a weave instrument. The sign and the swap (GM5b, GM5c) are OPEN; W1–W4 hold either way, the weave's group on the triplet of order 24 with L and R, 48 with all four. **[v1.25] WM1 (main, B1601; named W5 at v1.25, renamed at v1.26 — the SM seat's W5–W10 preceded it on its lane):** at the common point the frames' own module, the four (ν ⊗ ρ ⊗ ρ̄), is the trivial line plus the three parity lines — Ad(i) and Ad(j) act on (1, i, j, k) by the signs (1, +, −, −) and (1, −, +, −) — so "the generation is the trivial line" (B1493) and "the three parity lines" (W4) are the two parts of one module (the seat's "matches the quaternion axes", stated on the four). **[v1.25] WM2 (named W7 at v1.25, renamed likewise), THE COMMON POINT IS THE GEOMETRY MOD 3 (main, B1601, sealed; a weave result):** on every odd-trace thread to length eight (sixteen, none chosen) the fibre's traces (tr a, tr b, tr ab) at the geometric point generate exactly one prime of the thread's trace field, of norm three, so the holonomy reduces there to the quaternion point: W2's common structure is each thread's own geometry seen modulo a prime of norm three, and W3's forced A₄ cover is the thread's congruence cover at that prime (SL(2, 𝔽₃) = 2T). On every even-trace thread to length eight (twenty-one) the ideal is a power of a prime above 2, where the common point is the trivial representation; nothing above 3. The lemma: the Fricke map's linear part at the common point is the signed parity permutation of the three lines — dL and dR quarter turns about two axes, the cube's rotation group S₄ — a third turn about a body diagonal exactly for odd trace, whose axis (±1, ±1, ±1) is isotropic for x² + y² + z² only in characteristic three; over 𝔽₃ the parabolic Markov surface has the common point as its only point. The meeting is universal on odd trace, so it is not what singles out ±LR for content (the SM seat's W6 census): the ±LR pattern stays arithmeticity's, unexplained. **[v1.28] THREE ON THE WEAVE, GRADED (main, B1606; the SM seat's W19–W24, rows 932–940, with main's verifications of W20, W21, W22 at S85–S86).** The weave's own object (W19): its group is Aut⁺(F₂), the pure mapping class group of the twice-marked torus; its space M₁,₂, a complex surface with χ = 1/12 ≠ 0, the three parities its orbifold locus — the even-dimensional object the v1.27 condition asks for. On it (W20, verified by the amalgam ℤ/4 ∗ ℤ/6): −χ(Aut⁺(F₂); 27) = 3 through E₆'s principal sl₂ and every distinguished orbit, a sum of Riemann–Roch indices of powers of the records' Hodge line — an index of a non-flat bundle equal to three, and NOT chiral (the module is self-dual). The hand (W21, verified by the cup product on the ℤ/2-orbifold presentation): the parity-twisted spin space splits by Hodge type with one line per parity in each type; the Hodge–Riemann form is invariant under L, R and the sign, reversed by the swap, positive definite on the triplet T with χ(L) at 7/8 of a turn and negative on T̄ — the three holomorphic zero modes span T, one per parity. The puncture (W22 as qualified, verified): the six local solutions carry 2O with −1 acting as −1 and split 2 ⊕ 4, so every condition the moves keep has index −3, −1, +1 or +3 — odd, never zero — and with the parity grading only ±3. **The grade under THE_BAR.** DERIVED on the weave: three, alike, chiral under the weave's own group, one per parity — the number forced by the records' parities, the hand forced at the puncture; this is the flavour structure of three generations (the matter assignment of the modular S₄ flavour models, 3′ times a metaplectic character, as the seat notes). READINGS: that the triplet is the generations (FK14); that holomorphic zero modes on the fibre are the left-handed matter (FK11's compactification dictionary). UNEARNED: which fields carry the bundle 𝕎 ≅ ρ_Q ⊗ ℂ³ — W24's D4 proves the chiral gauge reading needs a Lagrangian half of the multiplicity space that no move-invariant, real, F₄ × SU(2)-invariant condition supplies, so the frame (E₆, SO(10), SU(5)) is a choice; gauge chirality itself. NEGATIVES: no index on a thread or a cover (v1.27); the E₈ frames on the fibre give at most two complete generations (W23); no six-dimensional object the weave forces gives three by the heterotic dictionary (W24: the character variety is forced and has no count; E³/G has a count and is not forced, 48, 16, 14). **The owner's question, 'did we derive three generations?': no — the flavour three is derived, the gauge three is a selection.** What would finish it: a forced complex structure on the gauge side — a bundle whose holonomy has complex representations — or the puncture's localized content (GAP2's place), neither yet forced. **[v1.26] WM3, THE FORCED COVER ON EVERY THREAD (main, B1602, sealed; a weave result):** on all 74 signed threads to length eight (32 of odd trace, 42 of even; none chosen) the cover the common point forces (A₄ on odd trace, D₄ or V₄ on even) carries members of the four at sign characters on +LR (24, reading (−1, −1)), on −LR (6, reading (0, −3)) and on ONE more odd-trace thread, −LLRLRLRR (trace −39): one member whose class is alive on all four cusps and reads (+3, +1) — the seat's floor k − m_A − b0 attained exactly, the ends' value, not generation-shaped; its sign twin and the other 28 odd-trace threads carry nothing. On even trace 17 of 42 carry (the two-syllable words with small exponents and the V₄ words L^{2k}R²), 25 do not. Interior classes of the four at the trivial character only on the eight shortest even threads, on no odd one. NEGATIVE as sealed: neither the ±LR exclusivity (the seat's W6 census to length six) nor an even-trace genericity holds; "content ⟺ arithmetic" was killed before the seal (+LLR, not arithmetic, carries). Content on the weave's forced cover is rare on odd trace because Theorem G makes it three-or-nothing; what admits ±LR and −LLRLRLRR is the open question for W6 (3 ramifies in all three trace fields — and in four non-carriers'). **[v1.20] The mechanism (B1494, sealed):** a count needs two supplies at one character — ends on which the character is trivial and a class dies (the seat's floor) and a line with room (its cap, b0 + n(ν⁴)). **T-COMPANION-NO-ROOM:** every fixed-point companion has b₁ = |T| = ends (no closed surface), so its trivial line has no room — a theorem, its hypothesis h¹(M; χ) = 1 at every torsion character verified on all 758 own-level states to length twelve. But the room is not absent from the family: **m135's eight-ended companion has room 2 at eight sign characters** (verified by its 255 double covers) — every one trivial on no end, where the floor gives zero generations whatever the room, and where the four has no class to extend. On every companion read the two supplies exist and never meet; on N₄₅ (rebuilt on main: degree 45 over m003, b₁ = 9 over 5 ends, n(1) = 4) they meet at cusp-trivial room-3 characters and the count reaches two. **The search for three is the search for an object the genesis determines on which the ends and the room coincide at one character.** Which word states have three ends: |2 − tr φ| = 3 ⇔ tr φ = 5 ⇔ L³R, the only one; its companion L8a15 is chiral with S₃ on its ends. **[v1.21] The orbit as one module (B1495, sealed; the SM seat's three-orbit: L8a15's three members are one orbit of the deck ℤ/3, verified):** the direct sum of the three members' extensions reads (10′, 5̄′) = (3, 9) in the seat's dictionary — the three cross terms between generations are −2 each, carried around the ends by the deck, one from each generation's class seen through another's four — so the reading "three generations = the deck orbit of a member" survives on the 10′ side only and stays a selection; a glued module and the two deck-fixed spin structures are not ruled. **[v1.22] The specification (B1496, the physics researched and verified claim by claim; `docs/THREE_GENERATIONS_RESEARCHED.md`):** in every established construction the number of generations is an INDEX of closed-cycle cohomology (ind(V) = ∫ch₃(V) = −h¹ + h²; ∣χ∣/2 for the standard embedding; ∫G₄ in F-theory), vector-like pairs cancelling; three is obtained by SELECTION — a free quotient divides a cover's count by ∣G∣ and the characters of G (Wilson lines) select the isotypic piece, the index refining per character; the 5̄ and 10 counts are equal by ch₃(Λ²V) = (n − 4)ch₃(V) at rank five, an identity the class index on a 3-manifold does not have (B1495's (3, 9)); no-exotics is a separate condition; nobody derives three. The record's F-CI is the orbifold mechanism (fixed points of a global order-3 symmetry on a hexagonal end; unverified in the run) and F-HE the smooth one (the room = closed cycles, the companion = the cover, the members = its characters, Shapiro = the index per character). **The family is blind to both by construction** — no global order-3 isometry, no closed cycle — so the frames were right to read one. Three generations in the smooth mechanism is ONE rank-5 bundle of index three, never three rank-5 bundles: the object to build is a glued module of the three members. THE_BAR's baseline: selection is the state of the art; a derivation — a reason internal to the genesis for an object of index three — would be new; the record's candidate is the Lefschetz number of the act. **[v1.23] Where the room comes from (B1497, T-ROOM-NEEDS-GENUS):** on any cover of a word state the room of the trivial line is the lifted act's invariant homology of the closed fibre, zero at genus one — so it needs a NON-ABELIAN cover of the register (degree ≥ 3), a move §2 does not name. Mapped: the root m004 has no room on any cover to degree eight (24 of its 39 reach genus 2–4); +LLLR none to degree six; the sign-twin m003 has one carrier by degree eight — o10_150691 at degree five (not a cover of m004; arithmetic, chiral; one cusp an index-three sublattice of the hexagonal lattice, one square), room 1. There the four has its first interior class at a trivial character, the second supply first reaches 2, Theorem C's cap is 2 at order four, and every count is one or zero. Both of the physics' mechanisms need what the sign-twin's side has (the hexagonal end; the room): FK4 and FK14 are one question |
| FK13 **[v1.12]** | Which set "the family as object" names (the owner's rule of 2026-10-04) | **[v1.13] RULED BY THE PRINCIPLE** (main B1480; the owner, 2026-10-07: "it's not up to me, it should be up to math, to the principle of emergence") | the family that emerges is the one the principle generates: the word states X_gen (§1 → §2 → §3). m004's commensurability class and B1186's 112 are named lists drawn by an outside relation; statements about them stay true as statements about those lists (§6). Revisable by a better argument, not by preference |

**Computed nowhere yet** (the frontier, not a list of failures):
- the harmonic frame's counts on any state outside m004's levels (**[v1.6]** its projective family exists on every word
  state to length 12, sm:B1523);
- the class-index frame on m369 or s639 built from their own arithmetic (main's L229 (iii));
- the Gieseking manifold m000 in any frame;
- fillings and non-cyclic covers of word states other than m004 and m003;
- the genesis paths of `paths/PATHS.md` never touched: 18 of 25 at main's B1422 (**[v1.1]** counted again at B1454:
  of the 25 enumerated paths 1 is dead, 3 are stalled, 3 are in progress and 18 are untouched; E21, a stalled
  instantiation of a listed mechanism, is the registry's 26th row);
- **[v1.1]** F-MC on any state other than the root;
- **[v1.6]** the class index on the projective family of a mirror-broken word state, first ±LLRLRR and ±L³RLR² (the SM
  seat's sL-10 item 8); **[v1.16, the SM seat's P4, read on main at headline level]** answered near the hyperbolic point in finite volume (sm:B1527; and sm:B1529: Λ² carries no count for any deformation in SL(4, ℂ) near the hyperbolic point, the four none where its base condition holds — the base condition fails on one word state, m135, at two characters); open there: the eigenvalue-one locus of the infinite-volume part, the non-split extensions, and the deformations far from the hyperbolic point;
- **[v1.6]** the fixed loci of the metallic trace maps component by component (B130's question with isolated components
  allowed; the audit lane's AR4);
- **[v1.12]** a frame of the right parity for GAP6 (§7): a bulk of dimension ≡ 2 (mod 4) with a bundle that is not flat.
  One candidate is named and unbuilt — the six-dimensional frame bundle Γ\PSL(2,ℂ) of a closed filling (the web seat's A1);
- **[v1.16, the SM seat's P9, recorded under FK14]** F-HE where both of Theorem C's supplies can grow (sm:B1535, Corollary C3): the
  covers' own characters on the fibre-direction covers of word states (puncture characters), non-abelian covers beyond
  sm:B1536's population, and non-unitary characters on covers with several cusps. **Each is a search for ends** (B1487, GAP2):
  a count of three found there is a selection, graded by `docs/THE_BAR.md`, until FK14 is ruled and the selection rule and
  trial budget are named before the search (WORKING_RULES, 2026-10-07);
- **[v1.12]** F-MC's two extra abelian factors, on any state other than the root. They are two objects and are named
  apart (the web seat's A4, verified on main's record): **U1-η**, left by the flat closing Y₃ — the η direction of the
  rank-five E₆ breaking, family-universal, both E₆-charged singlets of the 27 carrying the same charge so that no field
  of the 27 or the 78 gives ν^c a Majorana mass (the paper); and **U1-Z′₉**, left by the ninth closing's tree-level
  vacuum — (5ψ − 3χ)/2 with a family part (−10, 5, 5), family-non-universal, the VEV'd generation's singlets neutral
  (sm:B1283, B1303). Charges 4, −2, 10, −8, −2, 10 on one 27 with Σq = Σq³ = 0 (recomputed, B1478) — a check that
  cannot fail on full 27s (B1340). What can fail is the cube of the family part, and it does: Σf³ = −750 for (−10, 5, 5).
  **On a chiral spectrum U1-Z′₉ is not gaugeable as it stands** (B1340; FALSIFIER P9: the programme cannot hold both the
  observed chirality and this Z′ — the web seat's A4 did not carry this, main's ruling adds it). Neither factor has a
  mass, a coupling or a range on the record — B1303 gives a regime and a fork, not a value — and neither is a statement
  about any state but the root;
- **[v1.12]** dark-matter stability on any state other than the root (the cloud seat's memo 122 is NEGATIVE for the
  root's forced gauge 2-torsion only; the web seat's A5);
- **[v1.12]** Dirac against Majorana: decided by the discrete symmetry left when the extra abelian factor is broken,
  which no arc computes (A5).

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
| the X_gen convention | sm:B1384; P022 | §3 |
| **[v1.1]** "the four letters are the axioms" (aAbB = A1–A4); the bridge equation κ = tr[a, b] | `docs/THE_FRAMEWORK.md` Layer 0; B309, B518; P008 | GM1, GM5a, SE2 and GM2 in that order; PF1's mathematical form (§1) |
| **[v1.1]** "the six axioms A1–A6 and one bit A7" plus five typed external data | `docs/THE_CLAIM.md` §1 | the records route (§4) and F-MC's hypotheses (§5) |
| **[v1.1]** C18, the observer's closings | THEOREM_LEDGER | not part of the genesis: an input of F-MC (§5). **[v1.2]** The record's observer line runs from B716–B723 through B759–B762, B1168, B1169, B1183 and B1184 to main's B1327; whether the closings belong to the genesis is FK12 |
| **[v1.2]** signed powers −uᵏ, k even; the triple (u, k, ε) | R78; sm:B1385 §2 S4 | §3 |
| **[v1.6]** "the trace map never reads κ" | B20, B37 | FK12, in B37's literal sense only (the audit lane's AR3) |
| **[v1.6]** "no forced choice in the trace ring": a unit internally fork-free; the seeds' fields ℚ(√(m²+4)) called distinct | B130; `docs/OPEN_PROBLEMS.md` gate A | FK12: κ takes a continuum on the fixed locus, but the fork-free reading rests on an elimination that cannot exclude isolated components (AR4). m = 1, 4 and 11 share ℚ(√5); the seeds stay non-conjugate by their traces (AR5) |
| **[v1.6]** "the observer is built" at the β = 1 transition | B723 | §7, with the B942 and B957 retractions: the structure kept, both group assignments retracted |
| **[v1.6]** the three lines L1–L3 of the selection rule | main's B1455 §1 | B1297's properties of the class index (main's B1455 addendum); FK9 |

---

## 10. Version log

- **v1.0 · 2026-10-02 · sm:B1516.**
  - First canonical statement, with one numbering whose IDs were unused elsewhere.
  - SE1 is recorded as a postulated criterion, and T-ROOT as its derived consequence. The root needs four inputs (GM3, GM4,
    SE1, SE2), and each is needed. UNIQUENESS A6, positivity, GM2 and UNIQUENESS A7 are not needed for it.
  - T-ROOT extended to orientation-reversing monodromy: torsion-free means m004 or m000.
  - P000 entered: the family as the intended shape; its metallic family inside X_gen; SE1 selects m = 1 there.
  - Corrections carried:
    - UNIQUENESS §5: LR and RL are SL(2,ℤ)-conjugate by L, not by P (R57);
    - sm:B1384's transposed L/R noted;
    - R57's rejection of sm:B1380 §3 recorded at GM4.
  - The scope tag is made mandatory (§6).
  - The principle's single wording is proposed and awaits the owner (FK1).
- **v1.1 · 2026-10-02 · main B1454.** Verified and adopted on main.
  - Verification: v1.0's ten checks re-derived with main's own code by other routes (continued fractions and a
    linear-algebra conjugator in place of a box search; Burnside's count against the enumeration; cyclic covers in
    place of bundle codes), all agreeing; every citation of a main record checked against that record.
  - Relabelled, not changed: the SM seat's arc numbers carry `sm:`; its first-person references to itself and to its
    branch now name the SM seat; paths that exist only on that branch are named as such.
  - Added (marked [v1.1]): PF1's mathematical form and the two quantities called κ (§1); main's early record on the
    swap at GM5c, and that sm:B1380 is unverified on main at GM4 (§2); B979 and B1323 on the order bit (§3); the cost
    of SE2 from B1234, the other selectors of m = 1, and the two routes as one construction (§4); **the frame F-MC**,
    main's McKay cascade, with its counted inputs (§5); the scope tag's enforcement on main (§6); the path-registry
    count and F-MC's frontier (§8); three crosswalk rows (§9).
  - Corrected: the quotation of B1434 (§4), which v1.0 gave with a word changed; GAP5's "does not have", an absence
    the record contradicts (§7).
  - Unchanged and still the owner's: FK1.
- **v1.1 on the SM seat's branch · 2026-10-02 · sm:B1517.** Made the same day as main's v1.1, before it was read, and folded
  into v1.2 (marked [v1.2] there). The first sweep under the rule of that date applied to v1.0's own claims: the 758 word
  states realise 536 manifolds, a word and its reverse giving the same oriented manifold and the swap the mirror image
  (sm:B1517 C1–C6; OEIS A000048 and A000046; Goodman–Heard–Hodgson 2008 and Guéritaud 2006); signed powers recorded as
  neither states nor levels; T-ROOT's homology formula credited; main's 95 of 758 is 87 of 536 manifolds; a count names
  its unit, and arcs record their prior-work sweep.
- **v1.2 · 2026-10-02 · sm:B1519.** Main's v1.1 taken as the head, as main asked; every one of its 23 changes accepted.
  Main's corrections of v1.0 are the SM seat's errors, logged in its ERROR_LEDGER: the misquotation of B1434 and GAP5's
  unswept absence.
  - Folded in: the SM seat's v1.1 (sm:B1517), above.
  - §3: the signed powers placed as the triples (u, k, ε) with ε = −1 and k even, seeds −u^(2^a), m207 = −(LR)² named
    (R78; already in sm:B1385 §2 S4, main B1418 and B1224). sm:B1517's "open" missed the seat's own record (an E54
    instance). B979's "via P" noted.
  - §2: the swap native on the words route (B1323) and B14 complete by Cayley–Hamilton. §4: B1234's base rate named
    and graded; the 48 surjections re-derived.
  - §0 and §6: the two seen-first forms, `prior_work` and the "Seen first" section. §7: GAP4 points to THE_BAR
    (sm:B1518), and the observer line is carried: C18, the parity law, naming without signing (B759–B762, B1168,
    B1183, B1184) and main's B1327. §8: FK3 (B1327's relation, sm:B1519 K7), FK6 and FK9 (main's B1455) carry their
    records, and FK12, the observer, is registered. §9: two rows.
  - No status changes. FK1 and FK12 are the owner's to frame.
- **v1.3 · 2026-10-02 · main B1456.** v1.2 verified on main and adopted.
  - Verification with main's own code (B1456): the reversal identity on all 8 190 words to length twelve; 758 states
    are 536 classes under rotation, swap and reversal, and SnapPy's isometry signatures give that partition; main's
    own census read by manifold is 87 of 536 with no pair split; −(LR)² is m207 with H₁ = ℤ ⊕ ℤ/3 ⊕ ℤ/3, and a signed
    even power is the level of no state; the eight isometries of m004 act on the cusp by the four sign pairs, twice
    each.
  - Added (marked [v1.3]): the deciding test's result at FK9 and in §5 (main B1455, sm:B1520); what a source must be
    and what a count needs, at GAP3 (the audit lane's R41, R76, R77, R80, R40, R69; main B1457); the corrections that
    B723 carries, in the observer line; at FK12 the two signs, the count as an order (B1438, B1297), the audit
    lane's criterion for a lost register and its qualification of B37.
  - Named, not changed: THE_BAR is a page of the SM seat's branch and is not yet on main.
- **v1.4 · 2026-10-03 · main B1458.** The bar adopted on main for the class-index frame (`docs/THE_BAR.md`, from sm:B1518,
  its census claim re-derived by manifold and group structure); §5 and FK9 now point to it on main. No status changes.
  - Unchanged and still the owner's: FK1 and FK12.
- **v1.5 · 2026-10-03 · main B1460.** The owner's two decisions, on main's recommendation of the same day.
  - **FK1: CONFIRMED** as written (the three faces PF1–PF3). The measurer is kept out of the principle on purpose: as a
    premise it could not be paid, as a fork it can.
  - **FK12 reframed as the register question** (the wording above, marked [v1.5]): the two steps where the record forgets
    the order — word to manifold (B1456), module to vacuum (B1438, B1455) — and the four sub-questions of 2026-10-02, each
    with its computation; the open part named.
  - GAP3 refined on the audit lane's qualification: "only from a relation" was main's sentence, not its result.
  - No other status changes.
- **v1.6 · 2026-10-03 · sm:B1526.** Main's head, v1.5, taken as the head, as main asked of both seats (its relay of
  2026-10-03: "Please take v1.5 as head"). The SM seat's own v1.5 (sm:B1525), made on main's v1.4 in parallel and
  numbered the same, answered by its line (sm:B1526 §2). Each carried item was checked with the SM seat's own code
  first (sm:B1526 C1–C5).
  - Already in main's v1.5, in main's words: GAP3's refinement on the audit lane's qualification.
  - Carried from sm:B1525 (marked [v1.6]): in §5, the levels and the word states; at FK9, P's class, the levels, the
    word states and the owner's "choice might be golden" in their two sealed forms; at FK9 and GAP4, the bar's null
    contract; in §7, what of B723 survives (AR6); at FK12, B130's scope (AR4); in §8's frontier, the harmonic frame's
    counts off m004's levels, the class index on a mirror-broken family (sL-10 item 8) and B130 component by
    component; in §9, four rows.
  - Fitted to the owner's framing of FK12: of the three questions sm:B1525 kept apart, the first is the register
    question's (i), and the second's group-layer datum (B871) is placed in the register question; the experiential
    question stays apart, under Gate 5-Q.
  - Made precise at FK9: B1297's P is the fibre's elliptic involution, the class main's B1459 extends to every level
    (sm:B1526 C3).
  - No status changes. FK1 and FK12 as the owner decided (v1.5).
- **v1.7 · 2026-10-03 · main B1462.** v1.6 verified on main and adopted.
  - Re-derived on main with its own code (B1462): P is the swap's class in Ballas' presentation (SnapPy's holonomy,
    `p_is_the_swap.py`); on the levels M₁…M₆ the twists fixed by no count-odd map for λ off the unit circle number
    0, 0, 0, 0, 20, 96 (Fox calculus over ℤ[ℤ/n] from SnapPy's presentation, the eight symmetry classes found by
    search, the dualising ones read off the longitude; `levels_count_odd.py`), the SM seat's sm:B1522 numbers exactly;
    on M₅ the 20 are exactly the single-sheet twists, ten per golden sheet; two of sm:B1524's null-contract numbers
    (the exact scan law against the binomial; the Šidák counterexample at the gate).
  - Read, not re-derived: sm:B1523 (the projective family on every word state; Lemma R and Lemma T), the rest of
    sm:B1524, sm:B1525's items as carried into v1.6, sm:B1526's C2–C5.
  - Corrected (marked [v1.7]): FK12 (ii)'s sentence on P and dualising, main's own since v1.3, against B1459.
  - Named: the owner's hypothesis "choice might be golden" is on the record in two sealed forms (FK9); the SM seat's
    sL-10 item 8 (the class index on a mirror-broken word state's family) is in §8's frontier and is the seat's, sealed first.
  - Unchanged: FK1 and FK12 as the owner decided (v1.5).
- **v1.8 · 2026-10-03 · main B1463.** No text changed; two rows of §9 verified on main. The audit lane's AR3 and AR4,
  carried in v1.6 as read: B37's self-model predicate is a test of symbol presence that cannot fire on any map in
  x, y, z (so "never reads" is in B37's literal sense only, as the row says); B130's inference from an empty
  k-elimination is invalid, and its conclusion holds at m = 2, 3, 4 by primary decomposition (every component a curve).
  Lead L243 (a) paid.
- **v1.9 · 2026-10-03 · main B1466.** Three additions, no status change.
  - FK12 (ii): the counted point computed (B1466, sealed): the two orders ±1 and dual through the inversion; the fused
    module irreducible and counting 0; the count a bit; the source's mixing quartic named as the next quantity.
  - GAP6, the flatness, named (lead L244): every frame is flat; chirality needs curvature; no frame with it is on the record.
  - The observer line: the web seat's reading of 2026-10-03 taken as confirmation from a fresh reader (L244's sweep: B717,
    B128, B849, B1327 and FK12 already state it).
- **v1.10 · 2026-10-03 · main B1467.** Two corrections, no status change.
  - FK12 (ii) made exact on the meridian twist (sm:B1528, read and consistent with main's B1465). **A version-number
    collision is recorded:** the SM seat's arc of this content calls itself GENESIS v1.8, made on main's v1.7 in parallel
    with main's v1.8 (B1463); main's line is v1.8 (B1463), v1.9 (B1466), v1.10 (this); the seat's v1.8 is received in B1467.
  - L244's sweep corrected: 'symmetric phase' is on main — lead **L17** ("Symmetric-phase exclusion / quantized breaking",
    is the commuting locus empty rather than unstable), B849's seal, B853's script — found by the SM seat's sm:B1531 and
    confirmed by grep; main's tool reads verdict lines and titles and had been cited beyond its domain. The reading's
    three kinds cover 14 of the chirality chain's 26 negatives (sm:B1531, read): the taxonomy is incomplete.
- **v1.11 · 2026-10-04 · main B1476.** One narrowing, one location, one rule.
  - GAP6 narrowed to its hypotheses (closed bulk, characteristic classes); the flat frame reaches discrete data through the
    boundary (B1297/B1418's index; B1474/B1475's spin swap) and not continuous values (L247's census). Credit R89 and the web seat.
  - FK12's bit located on the family: the SL(2,ℂ) lift (the spin structure) is the bit; on seven amphichiral members of the
    112-family no spin structure is mirror-invariant and on the knot both are (B1474, B1475); B1476 asks whether the class is
    read off CS = ¼ and whether it is the parent's Pin type (sm:B1382) seen from the other side.
  - **The owner's rule (2026-10-04): "existence emerges from the family as object; we shouldn't tie ourselves to m004."**
    A5 (SE2's torsion-free tie-break) selects a member; the page's object is the family (B1418), and this page's statements
    about m004 are statements about one member unless they say otherwise.
- **v1.12 · 2026-10-06 · main B1478.** The web seat's five proposed amendments, each verified on main and ruled; one fork.
  - A1 ADOPTED: a curved bulk tells 27 from 27̄ only in dimension ≡ 2 (mod 4) (GAP6); the six-dimensional frame bundle
    entered as an unbuilt candidate, not a claim.
  - A2 ADOPTED: GAP6's "continuous values" becomes "continuous moduli"; rigid flat invariants are fixed numbers of a member.
  - A3 ADOPTED as a naming rule (§6): "the family" names its set. Its last clause — that the owner's rule means X_gen —
    is NOT ruled by main: fork FK13, the owner's.
  - A4 ADOPTED: the two extra abelian factors named apart, U1-η (Y₃) and U1-Z′₉ (the ninth closing), both root-only.
  - A5 ADOPTED: dark-matter stability and Dirac-against-Majorana listed as computed on the root only / nowhere.
  - B1477 recorded in GAP6: the bit is decided at the cusp (Theorem A; the ¼ class is the rhombic class on the census).
  - The web seat has its own branch from this date (`chat1/web-seat`); its relays are rowed and its pin set in B1478.
- **v1.13 · 2026-10-07 · main B1480.** One fork ruled, one restated.
  - FK13 ruled by the principle: the family is the generated state space, the word states. The owner declined to decide
    it by preference and asked that such forks be settled by the mathematics and the evidence.
  - FK4 carries a stake: the sign of a word state needs an inverse letter and is the fermionic bit (B1479, with B1477's
    Theorem A). Whether the principle generates the sign is the question.
  - Recorded from B1480: at own level the class index does not follow the sign — it fires on both; the count and the
    bit are independent there, and the next cell is the index under the mirror's swap of spin structures.
- **v1.14 · 2026-10-07 · main B1482.** The sign located in the grammar.
  - GM5b: inverse letters are not needed for the signed states; one central move, −I, is, and it brings no inverse letter.
  - GM5d: positivity is what excludes −I, hence the − states, hence every handed spin structure (B1479, B1481).
  - FK4 sharpened to one question — is negating the records a legal move? — with PF1's verb as a reading, not a derivation.
  - B1481 recorded: on the − states every spin structure carries a phase its mirror partner negates.
- **v1.15 · 2026-10-07 · main B1487.** The ends.
  - GAP2 sharpened: in the harmonic E₈ frame a count is a count of ends (the SM seat's floor, checked on main); a generated state has one, so no state of X_gen carries three in either frame on record.
  - GAP1 sharpened: the class index is mirror-even for every module, so the hand can enter a count only as the order; the harmonic frame's internal group contains the geometry's structure group.
  - FK14 registered: does the genesis generate states with several ends, or are generations not ends?
  - The heading of §7 corrected to six gaps (the SM seat's P1, sm:B1537, credited).
  - B1483 recorded at GAP6/GAP2: at a cusp the frame space of a spin structure is a bundle of elliptic curves ℂ/ker σ_s; on a − state the two classes of spin structures put complex-conjugate curves there, isomorphic only where the cusp lattice is hexagonal or square.
  - B1484 recorded: the weak-mixing-angle crossing needs the colour triplet split from the Higgs doublet, which no flat abelian line does on any state (w_D = −2·w_Q in the 27); it waits, with the chirality count, on a frame in which matter is counted by an index (L250).
  - B1485, B1486 recorded: the one generation of the harmonic frame on the silver squares read by main's instrument (every count agrees); at every member the two orders fuse into an irreducible module that counts zero.
- **v1.16 · 2026-10-07 · main B1489.** The SM seat's nine proposals (sm:B1537, 2026-10-04) ruled against the current page.
  - P1 (six gaps): paid at v1.15, credited there. P3 (sm:B1527 at FK9; Part H verified on main, B1465): adopted. P7 (one generation on the silver squares): adopted with main's grade — verified by a second route (B1485), the orders fused (B1486), and the floor's reading (B1487).
  - P2 (GAP6's scope): adopted in main's words, with the mirror-even theorem (B1487) as its limit. P8 (the cap): adopted at the seat's grade, read on main at headline level, with the ends reading.
  - P4, P5, P6: adopted as the seat's results at the seat's grade, read on main at headline level — P6 as a statement about the named list that FK13 rules is not the object, and under FK14.
  - P9 (where the supplies can grow): recorded, not adopted as a programme — under FK14 each item is a search for ends, and a count found there is a selection until the rule is named first.
- **v1.17 · 2026-10-07 · main B1491.** The correction and the companions.
  - GAP2: B1487's T3 corrected on the SM seat's relay — the floor is one-sided; the ceiling I(W₁) ≤ 2m_A + m_B − b0 is the seat's; the generation-side conclusions stand.
  - FK14: the seat's fixed-point companions registered as the first candidate answer to what adds an end (∣2 − tr φ∣ ends, one per fixed point of the act); two facts verified on main (o10_150729 = L10n113; +LLLR's three-ended companion L8a15). Not adopted: whether a companion is a generated state is the fork itself.
- **v1.18 · 2026-10-07 · main B1492.** The three-ended companion read.
  - FK14 and GAP2: the harmonic frame read under seal on L8a15 (three ends) and o10_150729 (five ends) at every sign character — every interior class counts one, as on the one-cusped members; on L8a15 no character trivial on an end has a member; in F-CI no three (order-3 isometries fix no cusp; cusps not hexagonal). The ends raise the floor's room, not the value. Not ruled: characters of order four and eight, and non-unitary ones, on the companions.
- **v1.19 · 2026-10-07 · main B1493.** The room on the companions.
  - FK14 and GAP2: Theorem C's cap b0 + n(ν⁴) read on both companions — the line has no room at any sign character, so no character of order ≤ 8 carries three or two on either; every member read on L8a15 counts exactly −b0. What moves the count is the room of the line, which N₄₅ has and the companions do not. Not ruled: other orders, non-unitary characters, a line with room on an object the genesis determines.
- **v1.20 · 2026-10-07 · main B1494.** No room on any companion, and one companion with room.
  - FK14 and GAP2: T-COMPANION-NO-ROOM (b₁ = ends on every fixed-point companion; hypothesis verified on 758 states); m135's companion has room 2 at eight sign characters trivial on no end, where the floor gives zero; N₄₅ rebuilt on main (n(1) = 4). The two supplies of a count — ends and room — are separated on the family and meet on N₄₅; three needs an object the genesis determines on which they coincide. The only word state with three ends is L³R.
- **v1.21 · 2026-10-07 · main B1495.** The orbit in one module.
  - FK14: L8a15's three members as one rank-15 module read (10′, 5̄′) = (3, 9); the cross terms −2 each (each generation's class through another's four); the orbit reading survives on the 10′ side only, a selection; a glued module and the deck-fixed spin structures not ruled.
- **v1.22 · 2026-10-07 · main B1496.** Three generations, researched first.
  - FK14: the specification of three from the verified physics — an index of closed-cycle cohomology, obtained by selection (a free quotient and the characters of its deck group), the 5̄ and 10 counts equal by an identity the class index lacks, nobody deriving three; F-CI = the orbifold mechanism, F-HE = the smooth one; the family blind to both by construction; three generations = ONE rank-5 bundle of index three. THE_BAR's baseline recorded.
- **v1.23 · 2026-10-07 · main B1497.** Room needs genus.
  - FK14: T-ROOM-NEEDS-GENUS — the room is the act's invariant closed homology of the fibre of a cover, zero at genus one, so it needs a non-abelian cover of the register; the root has none to degree eight, the sign-twin one at degree five (o10_150691), where the count is still one. FK4 and FK14 read as one question.
- **v1.29 · 2026-10-08 · main B1607.** The principle's tick at the common point.
  - GM5c: the rule a → ab, b → a is L∘P (the golden LP, det −1; σ² = LR; the Gieseking m000 at the root, m004 its double cover); its lift at the quaternion point ±(1 − i − j − k)/2 ∈ 2T, the mirror rule's lift k-conjugate, the inverse rule's in the other class, exchanged by the moves' lifts; on the parities the moves are transpositions and the rule a 3-cycle, and the sense of a thread's parity 3-cycle is neither a thread invariant nor the mirror bit (W26 verified). The two hands complementary — the records' orientation reversed by the rule and P, kept by the moves; the McKay orientation kept by the rule, inverted by every move; the double tick keeps both — and neither derived on the weave: each a selection, located. GM5c's branches computed; the fork stays open.
- **v1.28 · 2026-10-08 · main B1606.** Three on the weave, graded.
  - FK14/FK11: the SM seat's W19–W24 recorded with main's verifications (W20 the count three, not chiral; W21 the holomorphic triplet T; W22 the puncture index odd, ±3 with the grading) and the grade: the flavour three — alike, chiral under the weave's group, one per parity — is DERIVED on the weave; the gauge three is a selection (the dictionary unearned, W24's D4; W23; W24). The owner's question answered: no.
- **v1.27 · 2026-10-08 · main B1604.** The class index is not an index.
  - FK11: UNEARNABLE within F-HE/F-CI on threads and their covers (T-NO-INDEX-IN-THREE): every twisted Euler characteristic vanishes on a cusped 3-manifold; the class index is a difference of interior ranks, no characteristic class governs it; the earning condition named (an even-dimensional object of the weave with a non-flat bundle, or a sector selected by a character — a selection).
- **v1.26 · 2026-10-07 · main B1602.** The forced cover on every thread; main's weave items renamed WM1, WM2.
  - FK14: WM3 — the forced cover on all 74 signed threads to length eight at sign characters: content on +LR, −LR and −LLRLRLRR (its member the floor's value (+3, +1) with four live ends), on 17 of 42 even threads; the ±LR exclusivity and the even-trace genericity both fail; 'content ⟺ arithmetic' killed before the seal.
- **v1.25 · 2026-10-07 · main B1601.** The common point is the geometry mod 3.
  - FK14: W5 (WM1 from v1.26) — the four at the common point is the trivial line plus the triplet; W7 (WM2 from v1.26) — on every odd-trace thread to length eight the holonomy reduces to the common point at exactly one prime of norm three (on none of even trace), so the forced A₄ cover is the thread's own congruence cover at it; the lemma (the isotropic axis in characteristic three) proved, the exact norm a census law, the theorem open.
- **v1.24 · 2026-10-07 · main B1600.** The weave.
  - §0: the owner's rule named — thread, the weave, the test weave or thread; §1–§2 weave statements, SE1/SE2/T-ROOT thread statements, the frames thread instruments; `weave_or_thread` on every verdict file from B1491.
  - FK14: the weave's three — the three parities of the two records, cycled by every odd-trace thread, the quaternion point, 2T with A₄, the irreducible triplet (the SM seat's W1–W4, verified on main). Reading: the three generations are this triplet; W6 (what each line carries) decides, and needs a weave instrument. The weave program opened on main.

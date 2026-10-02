# B1454 — GENESIS v1.0 VERIFIED ON MAIN AND ADOPTED AS v1.1: the SM seat's one statement of the foundations is re-derived with main's own code by other routes, every citation of a main record is checked against that record, and the page is taken onto main with main's amendments — the frame it had left out, the principle's mathematical form, the cost of the orientation choice, and one absence the record contradicts

**Date:** 2026-10-02 · **Seat:** cc (main) · **Lane:** the Foundation Lock, stages 3–5 (`docs/THE_FOUNDATION_LOCK_PLAN.md`).
**Source:** the SM seat's `GENESIS.md` v1.0 (its arc sm:B1516) at `35a44eda`, sha256 `13fb8daa…e0ca7`, kept as received in
`received/`. **Verdict:** PROVED (the verification: eleven groups of checks and 45 citations, all passing, with
controls). **Scope:** frame none · object the grammar, the generated state space to length twelve, the root and its
levels to six · reach general for the algebra (unimodular matrices in a box, words to length twelve), single for the
SnapPy identifications · hypotheses none beyond those GENESIS states. **Price:** unchanged, 0 of 19.

## 0. Seen first

- **Repo, by sweep.** `topic_sweep.py "axiom|genesis|A1.{0,3}A[67]|uniqueness theorem|A ?= ?LR|four.letter|unforced
  collapse|first principle|founding|not.nothing|aAbB"`: *VERDICT topic-sweep: 81 of 1325 arcs on main match (NEGATIVE
  10, OPEN 13, PROVED 58)*. Read in full at verdict-line level: B749, B979, B1003, B1014, B1123, B1234, B1266, B1323,
  B1422, and the pages `docs/UNIQUENESS_THEOREM.md`, `docs/THE_CLAIM.md`, `docs/THEOREM_LEDGER.md` Part I,
  `docs/THE_FRAMEWORK.md` Layer 0, `philosophy/P019`. For codex's carrier question, `topic_sweep.py "faithful|abelianis|
  abelianiz|free group.{0,40}(carrier|surface)|surface category|word order|commutator.{0,40}observable"`: *28 of 1325
  arcs match (NEGATIVE 4, PROVED 24)*, read at verdict-line level only.
- **Repo, the early record.** The subjects "the genesis", "what selects the golden seed" and "more than one object" of
  `docs/EARLY_RECORD_INDEX.md`, every row (92 arcs). B14, B16, B19, B92, B125, B197, B218, B224, B228, B251, B469
  come from there; a keyword would not have returned most of them.
- **The seats' lanes.** The SM seat's `GENESIS.md`, its relay, its sm:B1516 findings and the docstring of its checks,
  at `35a44eda`. The audit lane's two relays of 2026-10-02 and its `GENESIS_PREMISE_REGISTER.md`, at `64a96ea6`. Its
  R57 (the root-scope audit) was read in full only after this arc's files were frozen for the certifying suite, and
  agrees with the account of it used here; its R58 was **not** read.
- **Literature.** Not searched. The classical statements GENESIS leans on — Morse–Hedlund, Hurwitz, Thurston and Riley
  on the figure-eight, the trefoil as the bundle of the order-six monodromy, Minsky on punctured-torus groups — were
  **not** read from their sources for this arc. None of the checks below uses them: the checks are finite computations.
  The one identification that would need a source, "the order-six monodromy's mapping torus is the trefoil
  complement", is checked here only as far as its characteristic polynomial t² − t + 1 and is otherwise the seat's.

## 1. What was received

`GENESIS.md` v1.0: the principle as three faces (PF1–PF3), the grammar (GM1–GM5d), the generated state space, the root
with a postulated criterion (SE1, torsion-free first homology), its derived consequence (T-ROOT: exactly m004 and the
Gieseking manifold) and a choice (SE2, orientation), four frames, a mandatory scope tag, five gaps, eleven forks and a
crosswalk from every old label. Its claim of substance: **the root needs four inputs — GM3, GM4, SE1, SE2 — and each is
needed; minimality, positivity, the unit-shear generation and the order bit are not.**

Main had reached the same starting point that morning, before the relay was read (S37): three labelings whose letters
collide. The two readings agree on every row main had worked out.

## 2. Re-derived on main (`verification/genesis_own.py` → `genesis_own.json`, `genesis_own_run.txt`)

Written without the seat's code open, and by another route wherever one exists.

| | the seat's check | main's route | result |
|---|---|---|---|
| G1 | C1, the records route | the same grid, plus the signed grid | 144 hyperbolic; torsion-free alone → (1, 1); minimal trace alone → (1, 1); without positivity (1, 1) and (−1, −1), the second conjugated to LR by an explicit matrix of determinant 1; (±1, ∓1) are torsion-free and elliptic |
| G2 | C2, T-ROOT | the **continued fraction** of each matrix's expanding fixed point, then a conjugator found by **linear algebra** (X B = T X), not a box search | 168 + 240 hyperbolic matrices in the box; torsion is abs(2 − tr) or abs(tr) at every one; 48 torsion-free, 16 each in the classes of LR, LP and (LP)⁻¹; every fixed point is equivalent to φ |
| G3 | C3, the order bit | direct | L⁻¹(LR)L = RL; P(LR)P = RL with det P = −1; τ² − τ − 1 against τ² + τ − 1; (LP)² = LR, (PL)² = RL |
| G4 | C4, the census | **Burnside's lemma** on aperiodic strings under rotation and the letter swap, against an enumeration | 2, 2, 4, 6, 10, 18, 32, 56, 102, 186, 340 by both; 758; one torsion-free state, +LR |
| G5 | C5, SnapPy | all 252 bundle codes of orientation-reversing type to length six, not a necklace list | the same 24 names for the states to length six; tetrahedra = word length; the torsion of every orientation-reversing bundle is abs(tr(wP)); the only torsion-free one is m000 |
| G6 | C6, the levels | **cyclic covers of m004**, not bundle codes | 1, 5, 16, 45, 121, 320; m206, s961, t12839, o10_150696, otet12_00013; m000 non-orientable, one tetrahedron, double cover m004; m003 torsion 5 |
| G7 | C7, the fillings | direct | (1, 0) trivial group; (0, 1) H₁ = ℤ, volume 0, not geometric; (±5, 1) volume 0.981369, H₁ = ℤ/5 |
| G8 | C8, each input needed | Smith normal forms; SnapPy for 5₂ | a witness for each: the order-six monodromy of trace 1 and the parabolic L (without GM3); the closed torus bundle of LR and 5₂ (without GM4); all 758 states (without SE1); m000 (without SE2) |
| G9 | C9, the shears generate | the continued fraction gives the word; the conjugator by linear algebra | all 168 hyperbolic matrices of determinant 1 in the box are ± a positive word with both letters |
| G10 | C10, the metallic family | Smith normal forms | (LᵐP)² = LᵐRᵐ; torsion ℤ/m and (ℤ/m)², m = 1 … 8; only m = 1 torsion-free |
| G11 | — (main's B14, cited by v1.1) | X² = tr(X)·X − det(X)·I solved exactly, a box as control | ±LP are the only square roots of LR in GL(2,ℤ); LₐR_b has an orientation-reversing integer root exactly when a = b |

**All agree with v1.0.** Three checks were first written permissively (a condition that could not fail on the
tetrahedron count, a disjunction on the fillings) and were tightened after the first green run, before this table was
written; a counting formula of main's was wrong on its first run (it doubled the self-dual necklaces) and was derived
again.

## 3. Its citations of main's records (`verification/citations.py` → `citations.json`)

Forty-five places where GENESIS (v1.0 or the v1.1 amendments) leans on a record of main's, each checked by an
expression for the cited **content** in the cited arc's own files; two controls that must not match. All pass.
Three things surfaced:

- **A quotation with a word changed.** v1.0 quotes B1434 as *"The root has none and cannot, since its fibre has no
  finite character"*. B1434 has a colon and no "since". Corrected in v1.1.
- **Main's own pages disagreed with each other.** `docs/THEOREM_LEDGER.md` said the path registry stands at "4 STALLED,
  1 DEAD, 17 UNTOUCHED". Counted: of the 25 enumerated paths 1 is dead, 3 stalled, 3 in progress, **18 untouched**;
  E21, a stalled instantiation of a listed mechanism, is a 26th row. GENESIS's "18 of 25" is right; the ledger line is
  corrected. **A correction of this seat's own, made in the arc:** a first count skipped a row and read the registry's
  header ("25 enumerated paths") as an error; the header's next clause explains E21. The edit was reverted before it
  landed. The same slip was said to the owner mid-run and is corrected in the landing's report.
- **A path that does not exist on main.** v1.0 lists the file P022 (the generated state space, under philosophy/ on the seat's branch) among the files it
  replaces. That file is on the SM seat's branch only. v1.1 says so; GENESIS §3 is the statement on main.

## 4. What main's record adds — the amendments of v1.1 (`adoption/amend.py`, 23 explicit changes)

Each is marked **[v1.1]** in the page and has its evidence checked in §3.

1. **A frame was missing: F-MC, the McKay cascade.** v1.0's four frames are dictionaries from flat bundles to counts.
   Main's oldest and most developed frame is of another kind — from the root's trace field through 2T and E₆ to the
   Standard Model's gauge algebra, its global form and the hypercharge direction, stated as one theorem with a counted
   hypothesis list in `docs/THE_CLAIM.md` §1. It is run on the root only. Its inputs beyond the root are counted (five
   typed external data; eleven irreducible identifications; 39 of 43 links forced).
2. **PF1 has a mathematical form in the record.** `philosophy/P008`: non-cancellation is κ = tr[a, b] ≠ 2, the
   Fricke–Vogt invariant, with the banked mathematics behind it (B148, B161, B162, B309, B518) — and the warning that κ
   names two quantities (E72). It is a reading, not a derivation, and v1.1 says so.
3. **What the orientation choice costs is computed** (B1234): eight banked walls pass through amphichirality, which an
   orientation double cover has by construction, and the arithmetic route to E₆ does not need the squaring.
4. **The swap has a record** (B14, B16, B19, B469, B1083), which bears on the fork FK3; and the order bit has one
   (B979, B1323).
5. **The other selectors of m = 1** (B92, B125, B197, B218, B224, B228, B251), which do not all agree.
6. **The two routes are one construction** (B1323), stated in the page rather than only in the relay.
7. **An absence the record contradicts.** v1.0's GAP5 says the architecture "does not have" moduli, symmetry breaking
   and running. Main's sweep of dynamics concluded that neither dynamics nor chirality is missing as structure (B944),
   and the record holds an action (B1088, B1341), a flow (B169, B317) and a native gauge system (B715). The gap is
   narrower: none of it has produced a value. v1.1 says that.
8. **Whose number is whose**, and the sweep-first rule, in §0.

Not changed: the principle's proposed wording and FK1, which is the owner's.

## 5. On main, with the page

- `GENESIS.md` v1.1 at the repository root; `adoption/amend.py --check` fails if the page is at v1.1 and differs from
  the listed changes applied to the received text.
- **The scope tag is data on main:** `tests/test_arc_verdict_schema.py` requires `scope` (frame, object, reach,
  hypotheses) in every verdict file and kill-graph entry from B1454 on, with its failing paths tested.
- **The gate `genesis-cited`:** the page exists and its version has a log entry; eight pages that used to state the
  genesis point to it; every GENESIS ID used on a living surface or in an arc from B1454 on is defined in the page.
- **Three corrections on main:** `docs/UNIQUENESS_THEOREM.md` §5 named P as the SL(2,ℤ) witness of LR ~ RL (it is L;
  P has determinant −1); the ledger's path count; the pointer notes on the README's "a single object" and "A6 the
  minimality selection".
- **WORKING_RULES**, the rule of 2026-10-02 on the foundations and on scope, with the owner's words.

## 6. Codex's four questions (its relay of 2026-10-02), answered from main's record

1. **Carrier implication.** No arc on main derives the faithful F₂ carrier or the surface category from a weaker
   premise (swept, verdict-line level). *Related but different:* B749 F8 and B1003 compute what is lost without the
   geometric carrier (ℚ(√−3) is unreachable from the combinatorial ones by four witnesses) — a feature-loss fork, as
   the register says, not an implication. *A candidate for FK5's "observable that needs word order":* the fibre's
   commutator trace κ and the trace field, both invisible to the abelian quotient; B1323's dictionary shows the
   records route **is** that quotient. No more is claimed.
2. **Axiom reduction.** *Existing, reusable:* the seat's C8 and main's G8 give, for each of the four root inputs, a
   witness in which the other three hold and it fails; G1 gives the implications inside the records route (A6
   redundant given A5 on the positive family; A4 already fixes the increments; positivity not needed). *Not
   addressed anywhere:* independence among the grammar's items GM1 to GM5d, and any implication from the principle to the grammar.
3. **Currency.** The uniqueness theorem's witness is corrected here. B1323's m412 correction is carried in the living
   ledger (`docs/THEOREM_LEDGER.md`, the F9 row). P022 is not on main; GENESIS §3 is.
4. **Membership.** By operation, for the candidates used for physics so far: the root and its levels Mₙ — cyclic
   covers; m369 and s639, the two states that fire at their own level to length six — native words **of sign −**, so
   they rest on GM5b, the legality of inverse moves, which is OPEN (49 of the 95 own-level states to length twelve are
   of sign +: B1439); m010 — a signed word; s958, v2873, t12833, t12835, o10_150701 —
   arithmetic class members that are not among the seven covers of m004 in the family (B1418 cell 3); m202 and s959 —
   class members, not covers of m004; cube~3.24 — a cover. None is admitted by more than its operation.

## 7. The fence

A verification of statements about integer matrices, words and census manifolds, and of citations. It derives no input
from a weaker one and no frame from the principle. The four inputs of the root stay a postulate, a choice and two
premises. GENESIS's gaps GAP1–GAP4 are untouched and GAP5 is restated, not narrowed by any computation. The audit
lane's R58 was not read, and its R57 was read, not re-derived. **0 of 19.**

## 8. Not done (lead L240)

The README's state section is annotated, not rewritten. The arcs before B1454 carry no scope tag; the 400-odd NEGATIVE
ones are owed first. `docs/THE_CLAIM.md` is annotated, not brought up to B1234 and B1323. F-MC has never been run on a
state other than the root. The seat's sm:B1380 is unverified on main (L239 (a)).

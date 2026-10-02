# B1516 — GENESIS v1: the foundations stated once, with one collision-free numbering. Selecting the root manifold needs four inputs, and each is needed; torsion-free first homology, a postulated criterion, selects exactly the pair {m004, the Gieseking manifold}; every result now carries its scope

**Date:** 2026-10-02 · **Seat:** cc (the SM-derivation branch) · **Verdict:** PROVED (the foundation facts, re-derived with
this seat's own code; nothing in the arc was an open outcome, so it was not sealed) · **Product:** `GENESIS.md` v1.0 at
the repository root, and the scope tag as data in the kill graph · **Price:** unchanged, 0 of 19.

## 0. Why

The owner asked for the genesis to be made "as robust and sophisticated as it gets" and locked once, so that every document
reflects it and old work stops resurfacing. They also feared that negatives computed on m004 alone were being read as
blocks on the whole programme. Four read-only sweeps of this branch, main and the audit lane (2026-10-02) found:
- **The principle had three wordings and no amendment relating them**: "existence as a frustrated cancellation"
  (`GOVERNANCE.md`), "being is inexhaustible description" (P019) and "the decision to look for structure" (the P3 paper).
  P000, the earliest philosophy file, has a fourth statement with four premises of its own.
- **The genesis's output changed on 2026-09-27**, when B1384 made it a generated state space with m004 as its root. This
  branch's README headline and main's README still say the axioms force "a single object", although main's research entered
  the generated state space at its S27 (B1434).
- **Label schemes collide.** A5 and A6 mean one thing in P019 and another in the uniqueness theorem. C1–C6 mean different
  things in `CLAIMS.md` and in `docs/THEOREM_LEDGER.md`. Short labels such as P1–P3, G1–G5, S1–S2 and K1–K11 are each used
  hundreds or thousands of times in the repository.
- **The frames disagree on the same objects.** Every word state is closed in this seat's free-cusp frame, while 95 of 758
  carry a generation-shaped background in main's class-index frame.
- **The last seven arcs (B1509–B1515) were all on m004's own family**, and the kill graph had no field for scope.

## 1. What the arc produced

`GENESIS.md` v1.0 is the single canonical statement. Its IDs were unused anywhere in the repository when it was written
(PF, GM, SE, T-ROOT, F-xx, FK, GAP; checked by grep on 2026-10-02). It contains:
- the principle in one proposed wording, as three faces PF1–PF3, with P000's premises placed (§1; the owner confirms, FK1);
- the grammar as layers GM1–GM5d, with the core convention for L, R and P (§2);
- the generated state space with its census, levels, moves, equivalences and non-claims (§3);
- the root: the postulated criterion SE1, its derived consequence T-ROOT, and the chosen SE2 (§4);
- the four frames as named hypotheses, with a table of where each has been run (§5);
- the mandatory scope tag (§6);
- the non-claims and the five gaps to physics, GAP1–GAP5 (§7);
- eleven open forks FK1–FK11, each with what would settle it, and the never-computed frontier (§8);
- a crosswalk from every old label to the v1.0 IDs (§9);
- an amendment protocol and version log (§10).

The scope tag became data in the same arc: every kill-graph entry this seat wrote from B1369 on carries a `scope` field,
and the arc-verdict schema and this arc's lock require one from B1516 on.

## 2. The verification (`verification/foundations_checks.py` → `foundations_checks_run.txt`, all checks pass)

- **C1, the records route.** On the positive 12 × 12 grid all 144 first mixed closures B(a, b) = LₐR_b are hyperbolic.
  The torsion-free filter (UNIQUENESS A5) alone leaves (1, 1), and so does the minimal-trace filter (A6) alone: the forcing
  is over-determined, as main's B1422 said. Without positivity the torsion-free hyperbolic solutions are (1, 1) and
  (−1, −1), and B(−1, −1) is SL(2,ℤ)-conjugate to LR (explicit conjugator). ab = −1 gives trace 1, elliptic.
- **C2, what the torsion criterion selects.**
  - Over every unimodular integer matrix with entries in [−5, 5] (616 matrices, 408 of them hyperbolic), the torsion of
    the mapping torus's H₁ is abs(2 − tr) for det 1 and abs(tr) for det −1, at every matrix.
  - The 48 torsion-free hyperbolic matrices have (det, trace) in {(1, 3), (−1, 1), (−1, −1)}. Each one is conjugated
    explicitly to LR (det 1, in SL(2,ℤ)) or to the golden matrix LP = [[1,1],[1,0]] or its inverse (det −1).
  - (LP)² = LR.
- **C3, the order bit.** L⁻¹(LR)L = RL with det L = 1, so LR and RL are SL(2,ℤ)-conjugate by L. P(LR)P = RL with
  det P = −1. The based Moebius fixed-point polynomials are τ² − τ − 1 (LR) and τ² + τ − 1 (RL).
- **C4, the census.** Primitive signed cyclic words with both letters, up to rotation and the L↔R swap, number 2, 2, 4,
  6, 10, 18, 32, 56, 102, 186, 340 at lengths 2 to 12: 758 in all, equal to main's B1439 row by row. The torsion of
  state (ε, w) is abs(2 − ε tr w), and exactly one state is torsion-free: +LR. The minimal trace at length n is n + 1.
- **C5, SnapPy 3.3.2.**
  - The 24 states to length 6 have 24 distinct census names, and each has as many tetrahedra as its word has letters.
  - Of the 46 orientation-reversing bundles b−±w to length 6, the only torsion-free manifold among them is m000, the
    Gieseking manifold.
- **C6, the levels and the relatives.**
  - The torsion of the cyclic covers is abs(2 − tr Aⁿ) = 1, 5, 16, 45, 121, 320, 841, …, 103 680 for n = 1 to 12.
  - The covers for n ≤ 6 are m004, m206, s961, t12839, o10_150696 and otet12_00013.
  - m000 is non-orientable with H₁ = ℤ, and its orientation double cover is m004.
  - m003 = −LR has H₁ = ℤ/5 ⊕ ℤ.
- **C7, the fillings of m004.** (1, 0) has trivial fundamental group after simplification, so it is S³ (SnapPy's framing
  of m004 agrees with the knot 4_1's up to sign). (0, 1) is degenerate with H₁ = ℤ: the Sol torus bundle of LR.
  (±5, 1) has volume 0.981369 and H₁ = ℤ/5: the Meyerhoff manifold.
- **C8, each input of the root is needed.**
  - Among det-1 matrices with entries up to 4 that are not hyperbolic, 12 of trace 1 and 17 of trace 2 still give
    torsion-free H₁. The trace-1 monodromy [[1,−1],[1,0]] has order 6 and H₁ = ℤ: its mapping torus is the trefoil
    complement. The parabolic L gives H₁ = ℤ².
  - The closed torus bundle of LR has coker(LR − I) = 0, so H₁ = ℤ (C7: Sol). The knot complement 5_2 has H₁ = ℤ and a
    positively oriented hyperbolic structure, volume 2.828122.
- **C9, the unit shears generate every state.** All 168 hyperbolic det-1 matrices with entries in [−5, 5] reduce, by
  conjugations with L^±1 and R^±1, to ± a positive word with both letters. Each is matched to that word by an explicit
  SL(2,ℤ) conjugator, and every level-1 word lies in C4's census.
- **C10, P000's metallic family.** For m = 1 to 6, LᵐP = [[m,1],[1,0]] and (LᵐP)² = LᵐRᵐ. The H₁ torsion is ℤ/m for the
  bundle of LᵐP and (ℤ/m)² for the bundle of its square. SnapPy gives H₁(b++LᵐRᵐ) = ℤ, then ℤ/m ⊕ ℤ/m ⊕ ℤ for m = 2 to 5.
  So torsion-freeness selects m = 1 in the family, as B126's fact (A) recorded.

## 3. The reductions (GENESIS §4)

1. **SE1 is a criterion, and it is postulated.** Torsion-free first homology is UNIQUENESS A5, motivated by the topology.
   What it selects is derived (T-ROOT): among hyperbolic once-punctured-torus bundles, exactly the class of LR (m004) and
   the class of LP (the Gieseking manifold m000). The orientation-preserving half is CLAIMS C3, as CLAIMS scopes it, and
   B197 broke the m004–m003 volume tie the same way. The orientation-reversing half is a two-line extension: for det −1,
   det(B − I) = −tr B.
2. **To select the root manifold, four inputs suffice, and each is needed:** aperiodicity (GM3), the once-punctured-torus
   carrier (GM4), the criterion SE1 and orientation (SE2). C8 gives a witness against dropping each of GM3 and GM4; C4 and
   C5 do so for SE1 and SE2.
3. **Minimality (UNIQUENESS A6), positivity, the unit-shear generation (GM2) and the order bit (A7) are not needed to select
   the root.** A7 is needed only for based data: the golden polynomial and the derived potential of P15–P16.
4. **The routes meet at LR's class.** The words route (P019) runs through the golden matrix LP, squared by orientation.
   P000's metallic family reaches m = 1 by SE1 (C10). The records route (UNIQUENESS) runs through A1–A6 to LR.
5. **The root is the emptiest state.** SE1 means that m004's fibre has no non-trivial character fixed by its monodromy. That
   is exactly why its own level carries no background in main's frame (main B1434: "The root has none and cannot, since its
   fibre has no finite character"). The selecting property and the emptiness are the same fact.

What is **not** reduced:
- the principle (PF1–PF3, postulated);
- the two records (GM1, tied to the carrier's H₁);
- the carrier with faithful F₂ data (GM4; R57);
- the criterion SE1 itself (postulated; reading it as "the least remainder" is an interpretation of PF1, not a derivation);
- orientation (SE2, CHOSEN, the most fragile link);
- the legality of inverses and of the swap (FK3, FK4).

None of the axioms is derived from anything weaker.

## 4. Corrections carried

- **The uniqueness theorem's §5** said LR and RL are "SL(2,ℤ)-conjugate via the record-swap P". P has determinant −1; the
  SL(2,ℤ) witness is L. The text is corrected in place, and the lock now also asserts det P = −1 and L⁻¹(LR)L = RL. The
  audit lane's R57 caught it.
- **B1384's verification code** uses the transposed pair L = [[1,0],[1,1]], R = [[1,1],[0,1]]. GENESIS §2 fixes the core
  convention and notes that B1384's "RP" is the core's LP.
- **R57's rejection of B1380 §3's naturality argument** is recorded at GM4: faithful F₂ word data and the surface category
  stay premises, and the puncture is CONDITIONAL on them.
- **This arc's own draft errors**, caught before commit by checking every cited fact against its source (ERROR_LEDGER):
  - the draft called B1186's 112-member family "m004's class", the error B1390 had already corrected (the class's census
    part is 99);
  - it misread B1369's "77" (members with no free cusp) as a count of closed members;
  - it gave the criterion SE1 the status DERIVED, which belongs only to its consequence T-ROOT;
  - its first IDs (P1–P3, G1–G5, S1–S2, K1–K11) collided with labels used thousands of times in the repository.

## 5. What this arc does not do

- It derives no axiom from anything weaker.
- It confirms no frame as physics, and changes no physics result.
- It does not settle the principle's wording: FK1 is the owner's.
- It does not claim novelty for T-ROOT. The orientation-preserving half is CLAIMS C3 and B197, and the metallic case is
  B126's fact (A).

## 6. Scope

Frame: none (a statement about the grammar and its state space). Object: all once-punctured-torus bundles, and the
generated state space of GENESIS §3. Reach: general. Hypotheses: the grammar's premises as GENESIS lists them.

I-26 stays UNEARNED. **0 of 19.**

## Verification

- `verification/foundations_checks.py` → `verification/foundations_checks_run.txt` (C1–C10, about 2 s).
- `tests/test_b1516_genesis_v1.py`: the lock (the record; the integer checks re-run live; GENESIS.md's version, sections and
  IDs; the scope field on the arc verdict and on this seat's kill-graph entries from B1369 on).

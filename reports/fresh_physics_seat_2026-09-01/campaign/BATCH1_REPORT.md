# BATCH 1 REPORT — type-matched campaign, synthesis

**Synthesis seat, 2026-09-01.** Masterplan: `reports/fresh_physics_seat_2026-09-01/CAMPAIGN_TYPE_MATCHED.md`.
Scope: cells T1–T5, each with an adversarial verifier. **A cell's final standing is its
verifier's verdict, never its own.** All five verifications came back CONFIRMED, so batch 1
closes with every cell standing as claimed. Nothing in this batch is banked to the repo
record; everything below is for owner adjudication.

**Campaign-level falsifier status:** the batch is NOT all-negative — it produced a proved
theorem (T3), an exactly-typed missing datum with a validated instrument (T1), a sealed
one-bit comparison design (T2), a priced novelty split (T4), and a feasible relabeling
proposal (T5). The thesis "only a seer was lacking" is not refuted at this ring; batch 2
has named cells.

---

## 1. Verdict table

| cell | claimed verdict | verifier verdict | final standing |
|---|---|---|---|
| T1_third_column | BLOCKED (missing datum typed; instrument built + validated) | CONFIRMED | **BLOCKED** — stands, with the (3,4,1) reconstruction and the 27-entry criterion banked as cell deliverables |
| T2_cp_bit | DESIGN-SEALED (object bit computed; comparison written, HELD) | CONFIRMED | **DESIGN-SEALED** — object side stands; comparison remains HELD for owner election |
| T3_amphichirality | PASS (Theorem A + Corollary B + clean sweep) | CONFIRMED | **PASS** — theorem-strength; plus Conjecture C banked as conjecture, not claim |
| T4_prior_art | PARTIAL ((a) criterion KNOWN; (b) terminality NOT FOUND, bounded) | CONFIRMED | **PARTIAL** — stands with the pricing intact |
| T5_a6_audit | FEASIBLE (class (a) axiom-consumer empty; proposal written) | CONFIRMED (one E23-class label defect typed) | **FEASIBLE** — stands; RL→LR label fix REQUIRED before PROPOSAL.md adoption |

Verifier notes that condition the standings (none verdict-changing, all typed in the
cells' VERIFICATION.md files):

- T5: FINDINGS §1/§3/§5, `reverify_gieseking.txt`, and PROPOSAL.md's closing-#0 line
  mislabel [[2,1],[1,1]] as "RL"; the repo's pinned naming (UNIQUENESS_THEOREM) is
  A = LR = [[2,1],[1,1]]. Numeric matrix correct everywhere; fix the word before adoption.
  Also: bank negative-control *scripts*, not just outputs, in future cells.
- T4: "exhaustive grep" should read "targeted" (one downward-phrased Fonseca passage
  escapes the five terms but its context still supports the claim); two of four "full
  texts" were residue-free WebFetch reads (load-free negatives).
- T2: "9/9 checks" counts 2 integer data fields; 7 booleans pass (cosmetic).
- T1: two facts cited-not-rerun (mu_u = 0; R031A exponents) — verifier found mu_u = 0 is
  in fact committed in M1 itself, so the caveat is over-cautious, not under.

## 2. Decisive numbers per cell

**T1 — third column (BLOCKED).**
- The (3,4,1) exact sequence 0 → C → V → T → 0 reconstructed from committed data alone:
  conn C12 multiplicities (2,4,3,3,2,3,2,3,2,3,3,3) (sum 33), Serre-dual tail labels
  (0,2,4,6,8); C = B₂,conn (dim 3, 33-column indices 6,7,8), V = B₀ (dim 4), T = ⟨b̂₂⟩
  (dim 1). The χ₋₂ twist is the UNIQUE one of 12 matching R031A's committed input
  (verifier's full scan) — the identification is forced.
- Exact criterion (sympy over ℚ(ζ₁₂), mod z⁴−z²+1): spread ≡ 0 ⇔ the **27**
  Higgs-connecting entries vanish ⇔ unique factorization through T. Failable both ways.
- Spread instrument: B1232 byte re-run (seed 20260901) 0.000e+00 annihilating /
  4.834e+00 generic (matches their banked 0.000/4.83); real 3×3×4 shape over 2000
  splittings: annihilating 0.0 in all 9 family entries; MANDATORY generic bite 9.315 at
  (0,0), 15.76 max (nonzero — not DEGRADED); single-conn-entry control localizes at 6.136.
- Missing datum, typed exactly: the 27 values T[i,j,conn_k] of the (A₇,B₆,B₂) block —
  committed nowhere; `certify_yukawa_down_tail_cech_308.sage` mentioned in 5 files,
  committed in none (E51 debt re-confirmed); codex's seat absent on this bench. Proved
  side-negative: no committed symmetry/selection rule can decide the fork (conn and tail
  share raw χ₂; C12 acts trivially on B₀). Up channel annihilates vacuously (H_u = C₀,
  dim 1) and doubly (mu_u = 0 exact).
- Flag for the banking seat: B1232's "nine-entry" annihilation phrasing vs the committed
  census's 27-entry condition (the 9 = the surviving tail family matrix).
- Verifier: all four scripts byte-identical on re-run; B1232's original
  verify_quotient_lemma.py also re-run byte-identical.

**T2 — CP bit (DESIGN-SEALED).**
- Object side: CS(m004) = 1.35e−16 ≡ 0 → **CP-EVEN**; sibling CS(m003) = 0.250000000 ≡ ¼
  → CP-ODD (the MB12 bite, run). All six amphichiral exhibits exactly on {0, ¼}
  (m004/m136/m206 at 0; m003/m135/m207 at ¼). m208: CS ≡ 0 but chiral →
  UNDEFINED-CHIRAL (CS = 0 alone carries no bit). Twelve chiral controls: 0/12 within
  1e−6 of {0, ¼} (values 0.386, 0.364, 0.479, 0.229, 0.308, 0.347, 0.263, 0.097, 0.352,
  0.287, 0.037, 0.422). High/standard precision agree on all 19 manifolds.
- Sealed design (HELD): prediction P = CP-EVEN; three-label two-outcome criterion at
  frozen Z* = 5; primary channel gauge-topological (type grounds, frozen); B813 clause
  (bit vs bit, no value crosses); Gate 5 clause (execution = owner election only).
  Design bite: hypothetical CS = ¼ reads CP-ODD; MATCH and MISMATCH both expressible.
- Verifier: results.json regenerated with 0 diffs at 1e−9; bit proved
  orientation-invariant by explicit reverse_orientation runs; nearest chiral control
  (m010 at 11/48, 0.021 from ¼) correctly not read as torsion.

**T3 — amphichirality (PASS).**
- Theorem A (proved): the orientation double cover of any non-orientable finite-volume
  hyperbolic 3-manifold is amphichiral (mirror = deck involution; reversal by descent;
  Mostow only for metric-independence). Corollary B: mirror-odd invariants are
  2-torsion → CS ∈ {0, ¼} in ℝ/(½)ℤ.
- Sweep: 40/40 covers amphichiral (certified full symmetry groups), 40/40 CS on
  {0, ¼}, max deviation 1.19e−64 (tolerance 1e−9). Anchors: CS(m004) ≡ 0,
  CS(m003) = 0.25 exactly.
- Bite: 15/15 certified-chiral controls off the set; min distance 1.346e−2 (m016) =
  1.3e7 × tolerance; median 5.8e−2. Verifier added an independent chirality certificate
  (CS mirror-oddness) not relying on SnapPy's symmetry-group code.
- New typed datum: cover distribution degenerate {0: 40, ¼: 0}; extended scan 120/120
  covers at 0 (max |CS| = 2.46e−64). Banked as **Conjecture C** (free deck involution
  may pin CS to 0 exactly), explicitly unproved, kill condition = one cover at ¼. The
  ¼-witnesses (m003/m135/m207) are amphichiral but not covers (Gieseking's cover is
  m004, not m003 — verified).
- Verifier: both JSONs byte-identical on re-run; theorem read adversarially, no gaps.

**T4 — prior art (PARTIAL).**
- Half (a) KNOWN: the registerability criterion is the survival hypothesis (Georgi,
  Nucl. Phys. B156 (1979) 126; Barbieri–Nanopoulos, Phys. Lett. 91B (1980) 369),
  formalized as the complex-representation demand (Georgi–Glashow 1972; Slansky 1981).
  Sharpest: Fonseca, arXiv:1504.03695 (Nucl. Phys. B897 (2015) 757) — 12 embeddings of
  G_SM in E6, 5 chiral pairs, UNIQUE chiral solution = 3×(27).
- Half (b) NOT FOUND (bounded): no source states the SM as the terminal
  chirality-preserving algebra in E6 descents (incl. the su(3)₁ → su(2)₄ conformal
  embedding), nor any rule-space enumeration showing endpoint rule-independence.
  Fonseca's full text: 0 hits on all five termination-direction greps (106 "chiral"
  hits as control). Nearest neighbor: tumbling (Raby–Dimopoulos–Susskind 1980),
  dynamical, no SM-uniqueness claim.
- Bite: positive retrieval control (Tong ℤ₆, arXiv:1705.01853) hit on first query;
  verifier re-ran it fresh and added 4 adversarial queries with new phrasings — none
  surfaced a terminality statement.
- Bound: 16 logged queries + 4 full texts; 1979–81 primaries paywalled (quoted via
  secondaries); Slansky's chains section and Hewett–Rizzo unread.
- Claimable delta: the conjunction (terminality criterion on the descent poset + SM
  terminal under every selection rule + rule-space enumeration) — NOVEL-CANDIDATE only,
  with Fonseca 2015 as mandatory prior art to delta against.

**T5 — A6 audit (FEASIBLE).**
- Sweep: 1394 files (1137 frontier FINDINGS + 126 docs + 131 papers), 629 with hits,
  4648 hit lines; decomposition independently verified by the verifier.
- Bite: all five mandatory known consumers PRESENT (CS, B1141 spin payment, complex
  volume, Reid/knot-in-S³, Gieseking); negative control on a consumer-free slice FIRED.
- Classification: 12 consumer families class (b) DATA-CONSUMER, 4 NEUTRAL, class (a)
  AXIOM-CONSUMER **EMPTY**. Genesis chain consumes orientation exactly at C5 (the
  pre-squaring object m000 already geometrizes: vol 1.01494160641 = ½·vol(m004);
  orientation_cover(m000) ≅ m004; det M = −1, M² = [[2,1],[1,1]]).
- Near-witness cleared: UNIQUENESS_THEOREM axiom A3 (det = +1) is class (b) — the
  theorem is conditional and survives with A3 retyped as closing #0 (A3 = excluding the
  pure swap S; M = L·S). Typed non-blocking residual: GL(2,ℤ)-level uniqueness
  (forcing M up to swap without A3) is uncomputed anywhere in the record.
- Verifier: sweep outputs byte-identical; the 54 FINDINGS-less frontier dirs
  adversarially grepped — no class-(a) witness hides there; ONE defect: the RL/LR
  mislabel (four locations), numeric matrix correct everywhere, fix before adoption.

## 3. Implications for batch 2 (per the masterplan's contingency table)

- **T6 (contingent on T1 = ANNIHILATES or OBSTRUCTED): does not fire as written.**
  T1 landed on the third branch the masterplan itself allowed — BLOCKED with the
  missing datum typed. Neither the freedom-ledger sweep (ANNIHILATES branch) nor the
  nine/27-entry typing (OBSTRUCTED branch) is licensed yet. What batch 2 CAN do: hold
  T6 armed — the moment codex commits the ℚ(ζ₁₂) 1×18 connecting row (or full
  36-block), s2+s3 substitute mechanically and the verdict is immediate; even GF(1009)
  values decide the OBSTRUCTED direction (a nonzero pivot certifies; a zero row mod one
  prime does not certify ANNIHILATES). The actionable batch-2 item is the unblock
  itself: surface to the owner that the E51 dual-homing debt
  (`certify_yukawa_down_tail_cech_308.sage` uncommitted) is the same blocker, and that
  the 27-vs-9 phrasing discrepancy in B1232 needs codex's clarification.
- **T7 (contingent on T2's design surviving verification): FIRES.** The design is
  CONFIRMED; present the sealed comparison to the owner for election. This is the one
  act no seat can take — firing spends an L192-licensed row. See §5.
- **T8 (contingent on T4): BOTH HALVES FIRE, split.** (b) NOT-FOUND → draft the
  termination-theorem section at publication strength for P2/P3, with the delta against
  Fonseca 2015 stated explicitly and tumbling cited as conceptual neighbor. (a) KNOWN →
  simultaneously propagate the criterion's retirement (E53-proofing: every surface
  asserting novelty of the *criterion* must be renamed to cite Georgi 1979,
  Barbieri–Nanopoulos 1980, Slansky 1981, Fonseca 2015; B994's own "REPRODUCED, not
  DERIVED" self-grade already points the right way).
- **T9 (contingent on all batch-1 verifiers clean): LICENSED.** All five verifications
  are CONFIRMED with zero refutations, so the campaign's hardest cell — the L154 typed
  instrument (survey all banked series against the kind-map; the Cardy 6-vs-1
  requirement) — may launch in batch 2.
- **Successor cells earned outside the T6–T9 table** (named so the batch does not idle):
  (i) a Conjecture C cell (does any orientation double cover sit at CS = ¼? candidate
  mechanism: freeness of the deck involution — one cover at ¼ kills it; a proof
  sharpens the A6 verdict); (ii) the GL(2,ℤ)-level uniqueness computation typed by T5
  §6 (finite symbolic computation over GL(2,ℤ) monoid words, same shape as the existing
  test lemmas); (iii) the T5 PROPOSAL adoption decision (owner-side, after the RL→LR
  fix).

## 4. What this batch did NOT establish

- **T1 did not compute the physics answer.** Whether the actual down/lepton coupling
  annihilates the connecting block — the live fork itself — remains unknown; not one of
  the 27 entries has a committed value. All s3 numerics are synthetic and labeled as
  such. The up channel's ANNIHILATES is vacuous (dim-1 Higgs slot), not evidence about
  the down fork. Two supporting facts (mu_u = 0; R031A exponents) were cited from
  committed transcripts, not re-run (their runnable certs live on an absent seat).
- **T2 established nothing about measured CP.** No comparison was fired; no
  measurement-derived label was assigned to any channel; whether nature sits at the
  CP-even point is exactly as unknown as before this batch. The primary-channel choice,
  though frozen on type grounds, cannot be proven free of the author's background
  knowledge (disclosed and frozen — the correct mitigation, not a proof).
- **T3's Conjecture C is not a result.** 120/120 covers at 0 is an observed regularity;
  mirror-oddness provably cannot yield it, no mechanism is proved, and one cover at ¼
  kills it. All amphichirality/chirality certifications are modulo SnapPy's
  canonical-cell code; CS values are quad-double numerics treated as exact. And T3 is
  pure 3-manifold topology — it carries no physics claim by itself.
- **T4's NOT-FOUND is a bounded-search statement, not a novelty certificate.** 16
  queries + 4 full texts, English web + arXiv, one bench-day; Slansky's chains section
  and Hewett–Rizzo were not full-text readable and could in principle hide a
  terminality statement; a specialist might assemble part of the endpoint-robustness
  from Fonseca's tables. The criterion half is 46-year-old physics — the programme's
  "best novelty candidate" shrank to the terminality conjunction.
- **T5 is a feasibility audit, not an executed relabeling.** PROPOSAL.md's bookkeeping
  consequences are proposed only; the (a)/(b)/(c) classification is judgment (the bite
  control validates recall, not classification); coverage has a stated modulus
  (compute.py/RESULTS.json, tests/, legacy/ etc. unswept); the GL(2,ℤ)-level uniqueness
  is uncomputed; and the RL/LR label defect must be fixed before any adoption.
- **Batch-wide:** nothing here is banked to the repo record — every deliverable sits
  under this campaign directory awaiting owner adjudication; no measured SM value
  entered any object-side computation, so no cell's outcome constitutes empirical
  support for anything; and verifier CONFIRMED means "not refuted under the attacks
  run," not "true."

## 5. Owner-election items (everything HELD or requiring the owner's word)

1. **T2's sealed comparison (the T7 act).** The design predicts P = CP-EVEN and is HELD.
   Firing it — assigning the measured CP-sector label to the frozen gauge-topological
   channel — spends one L192-licensed comparison row and is execution by definition
   (Gate 5 clause). Only the owner can elect this; a reader seat should execute it if
   elected. Post-hoc changes void the execution.
2. **T5's PROPOSAL.md adoption** (A6 → closing #0; A5b becomes the only FRAGILE axiom;
   six deck-involution corollaries become theorems-of-the-construction). Conditional on
   the RL→LR label fix (four locations, typed in T5's VERIFICATION.md §4). Adoption
   also implies the bookkeeping edits (THEOREM_LEDGER C5 retype, B1003 F5 row, P3 paper
   edits) that no campaign seat may execute.
3. **T1's unblock.** The cell is BLOCKED on data only owner/codex can supply: commit
   the ℚ(ζ₁₂) 1×18 connecting row (or GF(1009) values, or the lepton three-good-primes
   transcript), and settle the E51 debt (`certify_yukawa_down_tail_cech_308.sage`).
   Also flagged for the banking seat: B1232's "nine-entry" phrasing vs the 27-entry
   committed-census condition.
4. **T8's retirement propagation** touches banked claim surfaces (renaming novelty
   assertions about the criterion) — repo-record edits, owner's call on when/how.
5. **Batch 2 launch composition** per §3: T7 presentation + T8 drafting + T9 (licensed)
   + the named successor cells (Conjecture C, GL(2,ℤ) uniqueness), with T6 held armed
   on the T1 unblock. Per the stop rule, the batch does not idle: this report is the
   "launch or explain" step, and the recommendation is launch.

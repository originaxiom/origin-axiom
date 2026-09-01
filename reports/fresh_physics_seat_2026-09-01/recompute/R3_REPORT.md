# RING R3 — RECOMPUTATION REPORT (synthesis)

**Date:** 2026-09-01 · **Seat:** fresh physics seat · **Directive:** owner, "a proof doesn't
necessarily mean a proof; compute every load-bearing proof."
**Discipline:** blind-first per cell (own code and outputs on disk before any arc verification
script, results JSON or certificate was opened; read-before/read-after ledgers in each cell's
FINDINGS.md). Numbering of findings continues R1/R2 (R1: D1–D4, V1–V7, P1; R2: D5–D8, V8–V14, M1).
This ring adds **D9–D12, V15–V19, P2–P3, G1, F1**.

## Ring verdict at a glance

| cell | scope | verdict |
|---|---|---|
| R21 | B1234 "A6 built the walls" residual checks (base rate 6/200; Gieseking cover) | **MATCH** |
| R22 | B1148 memo-48 harvest chain 6615 → 4 → 1 | **MATCH** (E23 convention note on the 4) |
| R23 | B1186 2√3i carriers and quine | **MATCH** |
| R24 | B1163 w0 attempt chain under corrected amphichirality | **DISCREPANCY** (headline MATCH; family-wide addenda FALL) |
| R25 | B1127 antilinear torsor, 4 of 48 | **MATCH** |
| R26 | B1080 residuals (Γ = ℤ/6, ℤ/6×ℤ/2, ℤ/5) + B1011 C5/C6 (992 / 284) | **MATCH** (lock VACUITY on B1011) |
| R27 | B994 rule-variation provenance | **PARTIAL** (endpoint MATCH; path exhibit DISCREPANCY; two E51 gaps) |
| R28 | Kashaev tower deep tail (N ≤ 60,000) | **MATCH** (67–88 digits) |
| H1 | B267 grade re-read (HELD #23a) | **GRADE-OVERSTATED** |
| H2 | B964 filing re-read (HELD #23b) | **FILING-DEFECT** |

**Score: 6 MATCH, 1 PARTIAL, 1 DISCREPANCY, 0 BLOCKED among the eight recompute cells; both
HELD re-reads returned a defect.** The pattern of R1 and R2 holds a third time: every *headline*
banked number reproduces from independent blind code (6615/4/1, 4-of-48, ℤ/6 and ℤ/5, 992/284,
the six carriers and the empty quine, 6/200, five Kashaev coefficients to 67+ digits). What
fails is again the layer above the numbers — this time including one **banked chain that
consumed a refuted premise as a theorem** (R24: B1163's family-wide addenda, D9), one **banked
witness that is not a chain of subgroups** (R27: B994's SU(3)³ → Pati-Salam → SM, D10), and the
now-familiar tail of locks and spot-checks that could not have failed (V15–V19).

## 0. Seat adjudication (fresh physics seat, 2026-09-01, after the ring closed)

The synthesis above was written by the ring's synthesis agent. Before adopting it the seat re-ran
the load-bearing rows itself, in its own session, not the agents':

- **R24 witness rows (D9), own SnapPy run** — `symmetry_group().is_amphicheiral()`, CS mod ½,
  H₁: m202 False 1/12 ℤ+ℤ · s118 False 1/12 ℤ/2+ℤ · o10_150700 False 5/12 ℤ · t12840 True 0
  ℤ+ℤ · s955 True 1/4 ℤ/20+ℤ · m015 False (control). Agrees row for row with R24's table and
  with the seat's earlier L193 record (CS = −1/12 ≡ 5/12 mod ½ for o10_150700).
- **D9's quoted source** — `frontier/B1163_w0_attempt/ADDENDUM_family_denominator_B8147.md:14–15`
  does say "CHECKED: 83 of 83 … spot-verified on this bench 5/5 by mirror-isometry, including
  o10_150700, t12840, s955". One of the three named witnesses is chiral. The withdrawal is
  warranted; the headline (m004 amphichiral, CS = 0) is not touched.
- **D10's quoted source** — `frontier/B994_rule_variation/FINDINGS.md:22–30` lists
  `SU(3)^3 -> Pati-Salam -> SM` among six chains. Rank argument re-checked by hand: su(4) is
  simple of dimension 15 > dim su(3) = 8, so any homomorphism su(4) → su(3)³ has a nonzero
  kernel and, by simplicity, is zero; likewise su(5) (dim 24, simple) cannot inject into the
  non-simple su(3)³ (each factor dim 8). D10 stands.
- **D11's 9-vs-4** — reasoned independently: Inv_{su(3)³}(27^{⊗3}) with 27 = (3,3̄,1)⊕(1,3,3̄)⊕(3̄,1,3)
  has the three determinant-type invariants plus the six orderings of tr(ABC), giving 9; the
  Sym³ projection keeps 4. So "6615 → 4 → 1" is a mixed-convention chain and the honest
  full-tensor chain is 6615 → 9 → 1, theorem unchanged. Endorsed.
- **D12** — `b1080_results.json` prose names five valid A2+A1 subsets; the verdict ℤ/6 is
  unaffected. Endorsed as prose-level.
- **H1 / H2** — `frontier/B267_e6_coherence/arc_verdict.json:4` does read "…are the same Lie
  object…" and `frontier/B964_vev_correction/arc_verdict.json` does carry
  `"verdict": "RETRACTED", "supersedes": null`; PRACTICES ~113–121 (B818 disambiguation;
  Boundary rule 1) is the rule the H2 re-read applies. Both defects confirmed at the source.

**Adjudication:** D9, D10, D11, D12, V15–V19, P2, P3, G1, F1 **endorsed**. All are findings for
the banking seat (cc) to re-verify and re-bank; none is banked by this seat (role split,
`relays/FAB5_TO_CC_2026-09-01_reply.md` §1). Under the owner's delegation rule the seat files
dated addenda-beside for the computed ones (D9, D10/P2/P3, D11, V18) and *proposals* — not
actions — for the two that are owner/cc grading acts (G1 relabel of B267's claim line; F1
re-filing of B964). No licensed row is requested; T2 stays HOLD-CLOSED.

---

## 1. The diff table

Every load-bearing recomputed quantity vs the bank. "Mine" = blind, own code, exact arithmetic
unless noted. Artifacts in each cell dir under `reports/fresh_physics_seat_2026-09-01/recompute/`.

### R21 — B1234 (A6 built the walls: two residual checks)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| control base rate, first 200 of `OrientableCuspedCensus(cusps=1)`, `symmetry_group().is_amphicheiral()` | 6/200 = 3.0% | **6/200 = 3.0%** — m003, m004, m135, m136, m206, m207; sensitivity: first 200 of the full census gives 7/200 (adds m203) | MATCH |
| cell 2: m000 non-orientable; orientation cover ≅ m004; volume ratio 2 | banked | `is_orientable()=False`; cover `is_isometric_to(m004)=True`; ratio 1.9999999999999996 | MATCH |
| CS on covers of m004, degrees 2..5 (1,1,2,4 covers) | "2-torsion (in fact 0)" | every cover CS = 0 exactly | MATCH (**V15** — vacuous: CS(cover) = deg·CS(m004) mod 1 and CS(m004) = 0) |
| planted positives | — | m003, m004 flagged by the test; two degree-5 covers non-amphichiral despite CS = 0 (CS = 0 mod ½ does not imply amphichirality) | bite live |

Notes: the base rate uses the orientation-aware test, so it is untainted by the orientation-blind
instrument behind D5. B1234's FINDINGS does not name the census slice; the blind choice
coincided with the arc's script.

### R22 — B1148 memo 48 (the carrier-harvest chain 6615 → 4 → 1)

| rung | banked | recomputed (blind; own trinification-frame 27, e₆ = 78-dim exact stabilizer of det A+det B+det C−tr ABC, Ψ = ℂ²⊗27, full ordered Ψ⊗Ψ⊗27 = 78,732-dim) | verdict |
|---|---|---|---|
| π₁ alone | 6615 | **6615** four ways: exact sl₂ Clebsch count (Ψ = 6V₂+15V₁+6V₀, 27 = 6V₁+15V₀); **direct nullspace on the full 78,732-space** (16,470 weight-zero unknowns, rank 9855, mod 10⁹+7 and 998244353); block-exact fixed space of the actual figure-eight holonomy over ℚ(ω); block-exact fixed space of the finite 2T image | MATCH (stronger: the arc's cert counts by Clebsch only) |
| + trinification su(3)³ | 4 ("memo 35 × the unique ε") | full ordered tensor: **9** (= ε ⊗ {det A, det B, det C, 6 orderings of tr ABC}); its 27-symmetric part: **4**; Inv(Sym³27) = 4, Inv(27^⊗3) = 9 | MATCH under memo 35's Sym³ convention (**E23 note** — the printed chain mixes conventions; all-full-tensor chain is 6615 → 9 → 1) |
| + full e₆ | 1; 270 ordered triples; survivor automatically symmetric | **1**; 270 weight-zero ordered triples, none repeated; survivor support 270/270, coefficients ±1, equals the cubic; with ℂ² slots the joint survivor is exactly ε⊗I, antisymmetric under fermion exchange; agrees with R14 `r14_fulltensor` | MATCH |
| controls | — | same pipeline with su(3)³ only → 9/4 (uniqueness check can fail); 2T vs sl₂ differ only from spin 3 (V₆ has a 2T invariant), blocks here stop at spin 5/2 | bite live |

Notes: the π₁ action on the 27 is defined nowhere in the committed tree (certs live only on
`origin/claude/outside-bench @ d3c99640`); pinned blind from the banked shape (root-sl₂
stratum, 27 = 6×2 + 15×1) and confirmed against the cert afterwards (conjugate sl₂'s).
The 6615 nullspace is mod two large primes; everything else ℚ-exact. Closes R2 §4 item 13.

### R23 — B1186 (2√3i carriers and the quine)

| claim | banked | recomputed (blind; own full sweep of 212,641 census manifolds, ℚ(√−3) shapes, denominator ≤ 256; 220-bit confirmation) | verdict |
|---|---|---|---|
| family size | 112 | **112**, 0 errors; name set identical to `family_census.json: members_B` (symmetric difference ∅); max denominator 98 (t06829) | MATCH |
| carriers of cusp shape 2√3i other than m004 | six: t12840, o9_41001, o9_41009, o10_150684, o10_150685, o10_150693 | exactly **7** members carry it after SL(2,ℤ) reduction: m004[0] + the same six (cusp indices [1],[0],[0],[1],[2],[0]); volumes 4×,4×,4×,5×,5×,5× Vol(m004) | MATCH |
| quine: (1-cusped) ∧ (Vol = Vol(m004)) ∧ (shape 2√3i) over the 112 | zero collisions | hits = {m004} only; the sub-fingerprint without the shape leg returns {m003, m004} — the shape term is load-bearing | MATCH |
| controls | — | m004 raw shape −1.5e−64 + 3.46410161513775i to 220 bits; m003 has ½+(√3/2)i, correctly excluded; randomized re-triangulation of m004 injected under an alias is flagged as a collision | bite live |

Notes: banked instrument compares raw double-precision `cusp_info` shapes at 1e−6 without
reduction; for all 112 members no cusp shape moves under reduction, so raw and reduced agree
(E23, not a discrepancy). Mild instrument vacuity (**V16**): the arc's quine loop ran only over
the 112, whose own carrier table already put the 1-cusped carriers at 4× volume, so given that
table the loop could only return ∅; the claim as worded is family-scoped and the plant shows
the filter is live. Closes R2 §4 item 15.

### R24 — B1163 (w0 attempt chain under corrected amphichirality) — DISCREPANCY

| member | banked (addenda) | blind instrument (`reverse_orientation`+`is_isometric_to`) | orientation-aware (`is_amphicheiral()`) | CS mod ½ | verdict |
|---|---|---|---|---|---|
| m004 | amphichiral True | True | **True** | 0 | MATCH |
| m003 | amphichiral True | True | **True** | 1/4 | MATCH |
| m202 | amphichiral True | True | **False (chiral)** | 1/12 | **DISCREPANCY** |
| s118 | amphichiral True | True | **False (chiral)** | 1/12 | **DISCREPANCY** |
| o10_150700 | "spot-verified 5/5" (B8147 addendum) | True | **False (chiral)** | 5/12 | **DISCREPANCY** |
| t12840 | "spot-verified 5/5" | True | True | 0 | MATCH |
| s955 | "spot-verified 5/5" | True | True | 1/4 | MATCH |
| control m015, m016 (known chiral) | — | True | False | — | banked instrument cannot fail (**V17**) |

Headline (w0 = object-canonical orientation of m004; m004 amphichiral with CS = 0 exactly
refuses it): **MATCH**. Per-claim table in the cell FINDINGS: 6 family-wide claims FALL, 6
m004-only claims SURVIVE/UNAFFECTED (details in §2, D9). Closes R2 §4 item 14.

### R25 — B1127 (antilinear completion: 4 of 48)

| family/class | banked | recomputed (blind; own E6 Chevalley basis via lattice cocycle, Jacobi exact on all 78³ triples; Killing form tr(ad ad); I2 = A2 on B1114's pair {−θ_high, α₂}; π_mirror = diagram fold) | verdict |
|---|---|---|---|
| torsor size by family/class | 16 + 8 + 16 + 8 = 48 | all involutive signed automorphism lifts enumerated by direct bracket + θ² = I checks: **antipodal/A 16, antipodal/B 8, permute/A 16, permute/B 8 = 48** | MATCH |
| compact color I2 = (0,8,0) | exactly 4, all antipodal/A | **exactly 4**, all antipodal/A, exact sympy signature; other 12 antipodal/A give (4,4); antipodal/B all (4,4); permute/A and /B all (5,3) | MATCH |
| global antilinear signature of the 4 | (26,52,0) = E6(−26) | (26,52,0) on all four; the other 12 antipodal/A give (42,36) = E6(6); permute (40,38) | MATCH |
| characters per family | {+2},{+2},{−26×4,+6×12},{+6} | identical | MATCH |
| element-level diff (post-blind, `b1127_results.json`) | — | per-family multisets of (character, raw K-signatures on V±∩I2) identical; the four hits' raw invariants ((38,40), (14,24)/(28,12), (3,5), (0,3)/(5,0)) identical; label parametrizations differ by base point (kernel bits vs simple-root signs), same coset | MATCH (E23) |
| controls | — | antipodal/π=id family (64 lifts of −1): exactly one element globally compact (0,78), gives I2 (0,8); θ = identity (split) gives (42,36)/(5,3); 44 elements realize non-compact alternatives | bite live |

Notes: structural reason for 4 = 16/4 — the 16 π-invariant sign characters restrict
surjectively onto I2's rank-2 sign space. Layer-8b secondary construction and unsigned-fold
check not re-run. Closes R2 §4 item 11.

### R26 — B1080 residuals + B1011 C5/C6

| claim | banked | recomputed (blind; two independent exact routes for Γ — SNF of the saturated Levi root lattice, and SNF congruence solve on the 27's weights — asserted equal on all 63 node subsets) | verdict |
|---|---|---|---|
| cascade terminus A2+A1 Levis | ℤ/6 on 6 realizations (verifier: 10) | **10** valid subsets, all Γ = ℤ/6 cyclic, invariants [6], orders {1,2,3,3,6,6} | MATCH |
| row 1 A2+2A1 | ℤ/6×ℤ/2 on 5 subsets | 5 subsets {1235,1236,1246,1256,2356}; **12**, invariants [2,6], orders {1:1,2:3,3:2,6:6} | MATCH |
| row 4 A4 | ℤ/5 (verifier-corrected from 1), elementary divisor exactly 5 | 4 subsets {1234,1345,2456,3456}; **ℤ/5**, invariant factor [5], [K:Q_L] = 1 on all four | MATCH |
| "the 78 changes nothing" | unchanged | automatic (Γ is the identity in E6) | MATCH (vacuous by construction) |
| controls | — | A5 → ℤ/2 (hand-checked 27 = 15₀+6̄₊₁+6̄₋₁), A2+A2 → ℤ/3, A1+A2+A2 → ℤ/6 of 18, E6 → 1: "Γ = full centre" is a two-outcome property | bite live |
| B1011 \|ker χ\|, \|Z(2T)\|, \|Z(2I)\| | 8, 2, 2 | 8, 2, 2 computed (χ verified multiplicative on all 576 pairs) | MATCH |
| θ-odd forced cells | 992 | **992** by an independent criterion (Hermitian part of χ(A)V₂(B) scalar), cell-by-cell identical to the prereg definition | MATCH |
| θ-even forced cells | 284 | **284**, same cell-by-cell agreement; forced values Re χ(A)·½tr B and ½tr A·½tr B verified on every forced cell | MATCH |
| C6 mirror value set | 15 values {0, ±1/4, ±1/(4φ), ±1/2, ±1/(2φ), ±φ/4, ±φ/2, ±1} | identical over all 2880 cells; only 9 values on the 284 forced cells (quarter family needs both A, B non-central) | MATCH (scope note) |
| control | — | weaker "tr M_odd real" criterion gives 1440 ≠ 992 | bite live |

Notes: banked lock (`b1011_match.py` l.137–142, `tests/test_b1011_mckay_tensor.py` l.58–59)
hard-codes 8/2/2 and asserts the inclusion–exclusion identity — could not have failed
(**V18**). The "uniformity across six Weyl realizations" tests the instrument's
basis-independence, not an E6 fact (same-type Levis are one Weyl orbit) — the real content is
the saturation K = Q_L, which fails for A5/A2+A2/E6. As quoted, the arc's six realizations
name only five valid A2+A1 subsets (immaterial: all ten give ℤ/6). Closes R2 §4 item 12
(B1080 and B1011 halves; B1102 C3 and the trinification 36-count remain).

### R27 — B994 (rule-variation test: recompute + provenance) — PARTIAL

| claim | banked | recomputed (blind, from B861's committed `results.json` menus only) | verdict |
|---|---|---|---|
| registerable per step | [3,2,1] | [3,2,1] under a **positional** reading (step-k menu regardless of parent) | MATCH |
| number of chains; all end at SM | 6; 6/6 → SM | 6; 6/6 → SM (positional) | MATCH (**V19** — given B861's data this is exactly `len(registerable at step 3) == 1`, B861's step-3 uniqueness restated; planted SU(4)×U(1) registerable → 12 chains, two endpoints, so not structurally vacuous) |
| max-dim / min-dim witnesses | SO(10)×U(1)→SU(5)×U(1)→SM; SU(3)³→Pati-Salam→SM | same strings under the positional reading | MATCH as strings |
| path-dependence exhibit | SU(3)³ → Pati-Salam → SM is an alternative chain | **not a chain of subgroups**: su(4) (rank 3) has no nonzero hom into su(3)³ (each factor rank 2); likewise SU(5)×U(1) ⊄ SU(3)³ — 2 of 6 banked chains void, 5 of 6 rely on uncommitted menus | **DISCREPANCY (D10)** |
| parent-keyed walk of the committed map | — | 4 terminal paths, endpoints {SM, Pati-Salam, SU(6)×SU(2), SU(3)³} | new |
| provenance of the 8 cited menu entries | — | all present in `frontier/B861_fused_cascade/results.json` | PASS |
| menus for parents SU(6)×SU(2), SU(3)³, Pati-Salam | implicit | exist in no committed file | **P2** (E51 #1) |
| generating script for B994's results.json | "verbatim from the code" | none in repo or git history (only B861's solver) | **P3** (E51 #2) |

Closes R2 §4 item 10.

### R28 — Kashaev tower deep tail (B1120/B1133, deepening R16)

| coefficient | banked closed form | recomputed (own O(N) running-product sum, mpmath dps 700, N = 2000..60000, 30 nodes, Richardson order ≤ 29) — honest digits (three-subset spread at M = 28) / digits agreeing with banked | verdict |
|---|---|---|---|
| C0 | 3^{−1/4} | 88 / 95 | MATCH |
| C1 | (11/108)√3·π·C0 | 82 / 88 | MATCH |
| C2 | (697/7776)π²·C0 | 77 / 83 | MATCH |
| C3 | (724351/12597120)√3·π³·C0 | 72 / 78; ratio c3/(C0√3π³) = 724351/12597120 to all 40 printed digits | MATCH (target ≥ 4 digits exceeded by ~68) |
| C4 | (278392949/1813985280)π⁴·C0 | 67 / 73 | MATCH |
| cross-check vs R16 | R16: 25/21/17/14/11 digits at N ≤ 4200 | own J(50) agrees with R16's `blind_kashaev.py` to 190 digits (checked after my run); all R16 digits contained | MATCH |
| control | — | 1e−30 relative perturbation of C1 rejected by ~59 orders of magnitude | bite live |

Notes: digit counts were still rising with acceleration order when the ladder ended; reported
digits are a floor. Gate 5 untouched. Closes R2 §4 item 18.

---

## 2. DISCREPANCY, VACUITY, PARTIAL and PROVENANCE findings — the ring's product

**D9 (DISCREPANCY, banked-chain-level — R24, the ring's biggest).** B1163's family-wide
strengthening layer is refuted on its own named rows. `ADDENDUM_family_wide.md` lists m202 and
s118 as "amphichiral True"; both are **chiral, CS = 1/12**. The later
`ADDENDUM_family_denominator_B8147.md` ("83-of-83 CLOSED, spot-verified 5/5 by mirror-isometry")
used the same orientation-blind instrument (`reverse_orientation` + `is_isometric_to`), and one
of its three named witnesses, **o10_150700, is chiral with CS = 5/12** (t12840 CS = 0 and s955
CS = 1/4 are genuinely amphichiral). Typed cause: **consumption of D5** — the vacuous
amphichirality column (V9) was imported downstream as a family theorem, twice. Claims that
FALL: "all fourteen ℚ(√−3) census manifolds are amphichiral"; "amphichirality is the most-shared
invariant of the family"; "no sibling escape — orientation is fixed identically (amphichiral) for
all fourteen"; "any canonical datum must route through H1, not orientation, which the family
fixes for all"; "§A observer-orientation now family-wide"; "83/83 CLOSED". Claims that
SURVIVE/UNAFFECTED: m004's H1 = ℤ uniqueness (homology only; m003 ℤ/5+ℤ, m202 ℤ+ℤ, s118 ℤ/2+ℤ);
route-(a) closure on m004; the D4 orientation theorem for m004 (D4 order not re-verified); the
`arc_verdict.json` claim line (mentions only m004); FINDINGS §A. **The headline stands**: m004
`is_amphicheiral() = True`, CS = 0 exactly; m003 True, CS = 1/4. Residual: "no sibling
self-orients" may be re-derivable from the Galois/analytic legs, which never used amphichirality
— but the banked argument is gone. `ADDENDUM_2026-09-01_amphichirality_instrument.md` already
withdraws rows of family_wide; it does not yet touch the B8147 "83-of-83 CLOSED" addendum.
Consistency check supporting the correction: every aware-amphichiral member has CS ∈ {0, 1/4}
and every chiral one does not; 12·CS is integral throughout.

**D10 (DISCREPANCY, witness-level — R27).** B994's exhibited alternative chain
SU(3)³ → Pati-Salam → SM is **not a chain of subgroups**: su(4) has rank 3 and su(3)³ has
factors of rank 2, so there is no nonzero homomorphism su(4) → su(3)³ (exact rank argument,
`embedding_check.txt`); likewise SU(5)×U(1) ⊄ SU(3)³. Two of the six banked chains are
group-theoretically void and five of six rely on menus that B861 never committed. Typed cause:
**positional menu application** — B994 applied the step-2 (SO(10)) menu to SU(6)×SU(2) and
SU(3)³ parents, and the step-3 (SU(5)) menu to Pati-Salam. Path-dependence per se (max-dim vs
min-dim rules choose different step-1 subgroups) is genuine; only the witness is wrong. B994's
own P0 quantifier ("menu arithmetic, not the manifold") is confirmed and is stronger than
stated: arithmetic over a positional list, not even over the subgroup lattice.

**D11 (DISCREPANCY, convention/prose — R22, E23-resolved).** The printed chain "6615 → 4 → 1"
mixes conventions: 6615 and 1 are full-ordered-tensor counts, but 4 is memo 35's Sym³ count
(the cert does not compute the middle rung; it reuses memo 35 × ε). In the full ordered tensor
the su(3)³ rung is **9** (= ε ⊗ {3 determinants + 6 orderings of tr ABC}), whose 27-symmetric
part is exactly 4. The theorem is unchanged (endpoint 1, survivor ε⊗I, symmetry as output), but
the phrase "the trinification gauge cuts to 4 … no symmetry assumed" is not what was computed.
The honest all-full-tensor chain is **6615 → 9 → 1**. Also: the FINDINGS phrase "by DIRECT
full-tensor nullspace" applies only to the e₆ rung; the cert's 6615 is a Clebsch count. R22 now
supplies the direct nullspace for 6615.

**D12 (DISCREPANCY, prose — R26).** As quoted in `b1080_results.json`, B1080's "six Weyl
realizations" (su(3) on {1,3} or {2,4} crossed with su(2) on 2, 5, 6, 1) name only five valid
A2+A1 subsets ({2,4}+5 is A3); the sixth is not identifiable from the text. Immaterial to the
verdict — all ten valid subsets give ℤ/6.

**V15 (VACUITY, sub-check — R21).** CS = 0 on all covers of m004 of degree 2..5 is a corollary
of CS(m004) = 0 (CS(cover) = deg·CS(base) mod 1), not independent evidence for the 2-torsion
claim. Recorded as consistent, weight zero.

**V16 (VACUITY, instrument scope — R23).** The banked quine loop runs only over the 112 family
members, whose own carrier table already places the 1-cusped carriers at 4× volume; given that
table the loop could only return ∅. The family-scoped claim is what was recomputed, and the
plant (aliased re-triangulation of m004) shows the filter is live.

**V17 (VACUITY, instrument — R24).** The `reverse_orientation` + `is_isometric_to` test returns
True on known-chiral m015/m016, so every banked spot-check in B1163's addenda (4/14 and 5/5)
could not have failed. Same instrument as V9; this is its second downstream consumer. Also
`verification/reproduce.sh` line 20 prints "m004 amphichiral" rather than testing it.

**V18 (VACUITY, lock — R26/B1011).** `b1011_match.py` l.137–142 sets `kerchi, ZI, ZT = 8, 2, 2`
as literals and asserts `8·120 + 24·2 − 8·2 == 992`; `tests/test_b1011_mckay_tensor.py`
l.58–59 asserts the same integer identities. Nothing committed enumerates cells or evaluates a
forcing criterion; the "incoming enumeration" is uncommitted. Inputs 8/2/2 are separately
verified (R02); R26 supplies the falsifiable cell-by-cell version. Adjacent scope note: the C6
15-value mirror set is over all 2880 cells; on the 284 forced cells it has 9 values (the quarter
family arises only where both A and B are non-central), so the mirror-law statement should
carry that scope clause.

**V19 (VACUITY-FLAVOUR, restatement — R27).** Given B861's committed menus, "endpoint is
rule-independent" is exactly `len(registerable at step 3) == 1`; the rule enumeration adds
nothing beyond B861's step-3 uniqueness (planted control shows the check is not structurally
vacuous, merely redundant).

**P2 (PROVENANCE, E51 — R27).** Menus for parents SU(6)×SU(2), SU(3)³ and Pati-Salam —
relied on implicitly by 5 of B994's 6 chains — exist in no committed file.

**P3 (PROVENANCE, E51 — R27).** No generating script for B994's `results.json` exists anywhere
in the repo (grep for its keys hits only the results file; no deleted `.py` in git history);
FINDINGS' "verbatim from the code" refers to B861's solver.

**Note on R22's committed-tree gap (not a finding, a fence):** B1148's certificates live only on
`origin/claude/outside-bench @ d3c99640`; the π₁ action on the 27 is not defined in the
committed tree. R22 pinned it blind and confirmed it post-run; the owner should consider
landing the certs.

---

## 3. BLOCKED cells and typed missing data

**No cell returned BLOCKED.** The PARTIAL and the sub-clause gaps carry typed missing data:

| gap | typed missing datum | who can close it |
|---|---|---|
| R24: B1163 chain | dated addenda beside `ADDENDUM_family_wide.md` and `ADDENDUM_family_denominator_B8147.md` withdrawing the family-wide rows (m202, s118, o10_150700 chiral); re-argument of "no sibling self-orients" from the Galois/analytic legs if it is to be kept; 14- and 83/112-member censuses not regenerated in-cell (38/112 taken from R20) | owner (E53 discipline); R20's sweep serves as the census |
| R24: D4 symmetry group of m004 | order-8 D4 not re-verified (out of scope) | cheap, any cell |
| R27: B994 menus | committed menus for parents SU(6)×SU(2), SU(3)³, Pati-Salam, or a rewrite of B994 over the parent-keyed map (4 terminal paths) | owner (B861 scaffolding) |
| R27: B994 generator | a committed script producing B994's `results.json` | owner |
| R22: certs | land `uniqueness_chain.py` and memos 35/47/48 in the committed tree; fix the "4 … no symmetry assumed" prose (D11) | owner |
| R22: 6615 exactness | the 16,470-unknown nullspace is mod two large primes; a ℚ-exact run (or a third prime) would close the last non-exact step | cheap |
| R26: B1011 lock | replace the arithmetic-identity lock with a cell-enumerating one (R26's `blind_forced_counts.py` can serve) | owner hygiene |
| R26: B1080 prose | name the sixth realization or reword to "all ten A2+A1 subsets" (D12) | owner |
| R25: Layer-8b | secondary construction and unsigned-fold check not re-run | medium, if wanted |
| R21: base-rate slice | B1234 FINDINGS should name the slice (`OrientableCuspedCensus(cusps=1)[:200]`) | owner (prose) |
| H1: registry wording | `arc_verdict.json` `claim_one_line` re-wording; IDENTIFICATION_LEDGER row (UNEARNED, re-baseline the ratchet); HINT_LEDGER H64 | owner |
| H2: filing | `arc_verdict.json` RETRACTED → PROVED with `supersedes`; addenda beside B952/B959/B960; LAW_MAP l.269 NB; regenerate VERDICT_LEDGER | owner |

**Harness/process notes:** every cell wrote its FINDINGS.md via a shell heredoc because the
Write tool refused report files for subagents; all live at the required in-cell paths. R23's
census sweep ran 3 min on 4 procs; R28's ladder ~60 s at dps 700. No cell modified anything
outside its own directory; Gate 5 untouched in all eight.

---

## 4. The two HELD re-reads

### H1 — B267 grade (HELD #23a): **GRADE-OVERSTATED**

What B267 proves (all hypotheses imported: 2T McKay = affine E₆ from B266; 2T character data
hard-coded from GAP; the E₆ Dynkin diagram **hard-coded** in `e6_dynkin_adjacency()`, not
derived from the McKay graph; B264's exponents hard-coded, with B264's geometric side E₆ by
construction): the E₆ adjacency eigenvalues are 2cos(πm/12), m ∈ {1,4,5,7,8,11}; Σ marks(2T) =
12 = h; Σ exponents = 36, dim 78; Molien(2T) = (1+q¹²)/((1−q⁶)(1−q⁸)). Corollary: **type
coincidence** — both roles are E₆ and so share all invariants. No map between the two E₆ roles
is exhibited, and none can be from this evidence (McKay yields a diagram, not a group acting on
the flat connections). Quoted lines:

- FINDINGS tagline: `> **The two E₆'s are one E₆.**`; script: `"They are ONE E6"`; HINT_LEDGER H64: `"YES — one E₆ on five invariants"`.
- `arc_verdict.json` `claim_one_line` (propagated to VERDICT_LEDGER l.165, THE_SPINE l.330): `"Coherence check passes: the arithmetically-selected E6 and the character-variety E6 are the same Lie object, the McKay exponent set matching the tangent-space grading."`
- B272 (2026-06-28) already appended to FINDINGS: `"That is a **consistency check** (the two constructions are not in conflict; both are E₆), not five independent measurements."`
- FINDINGS "Honest guardrail": `"Coherence of Lie invariants is **not** a proof that the 3d-3d **input** type must be this E₆"`.

Verdict: PROVED stands for what is proved; the row's "are the same Lie object" is an "X IS Y"
claim on barred evidence (the species of IDENTIFICATION_LEDGER row I-6, one floor up). Proposed
re-wording in the cell FINDINGS. The sweep's supporting citation that B1228 showed "the two
E₆-sources can come apart" is a misread (B1228's pair is McKay-E₆ vs the PSL(2,ℂ) connection's
A₁ boundary, not B264's e₆ flat connections). B267 has no row in OPEN_LEADS or THEOREM_REGISTRY.
Filed as **G1 (GRADE)**.

### H2 — B964 filing (HELD #23b): **FILING-DEFECT**

B964 withdraws two claims of *other* arcs — (1) "27-VEV route stops one step short" (B962) and
(2) "the object does not supply a VEV" (B952, B959, B960, echoed B962) — and proves a positive
reframing (the measurement cascade IS an adjoint Higgs mechanism; only the rank-reducing 27 VEV
is missing). Quoted lines:

- Only B962 carries a pointer: line 5 `## ⚠ PARTIALLY RETRACTED BY B964 (2026-08-08)`.
- B952 l.47–49 (no B964 mention): `a **Higgs VEV**, a **Wilson line / Hosotani flux**, or an **orbifold projection** — requirement #11 of the ledger, which the object does not supply.`
- B959 l.88: `A Higgs-type mechanism remains unexcluded and remains unsupplied.`
- B960 l.55: `A Higgs-type mechanism remains unexcluded — and remains unsupplied.`
- `docs/LAW_MAP.md` l.269 (B952 row): `a Higgs VEV, a Wilson line/Hosotani flux, or an orbifold projection — which the object does not supply (L133)` — pre-B964 wording; l.230 and 231–233 are correct.
- B964 FINDINGS l.91: `**Verdict: CORRECTION.**` (not a vocabulary value); `arc_verdict.json`: `"verdict": "RETRACTED"`, `"supersedes": null` → VERDICT_LEDGER `## RETRACTED (10)` l.1167.
- `docs/PRACTICES.md` l.115 (B818): `"RETRACTED applies only when the arc withdraws **its own** headline. … Mislabelling an auditor as RETRACTED makes the ledger say the audit is untrustworthy"`; l.120 (Boundary rule 1): `"a correction that also proves is PROVED … the withdrawal is recorded in supersedes"`.

Cause: B967's retraction sweep matched the registered phrase exactly; B952/B959/B960 paraphrase
it. Proposed re-label (PROVED, `supersedes` populated, dated in-place note), dated addenda
beside B952/B959/B960, LAW_MAP l.269 NB, VERDICT_LEDGER regeneration — full worklist in the cell
FINDINGS. `docs/CLAIMS.md` does not exist; RETRACTIONS.md and RETRACTED_PHRASES.md are correct.
Filed as **F1 (FILING)**.

---

## 5. Combined R1+R2+R3 coverage

R2 §4 listed 18 unrecomputed load-bearing items after two rings. Status after R3:

| # | item (R2 §4) | R3 status | remaining cost |
|---|---|---|---|
| 1 | B873's P5 menu-completeness gate (conditions R04; B861's SU(3)₉, B863 carve-out, su(3)⊕g₂ witness) | **remains** — but R27 now shows the committed menus are parent-keyed with only three parents, sharpening what completeness would have to mean | **full** (needs the menu enumerator rebuilt, batch-3 cell) |
| 2 | B660/S3 + B652 "no continuous dial" premise | **remains** (typing rule of the sealed grammar; characterized in R09, not recomputable) | fence ledger — not a recomputation |
| 3 | B1098/B1100 trinification landing | **partially touched**: R22 and R25 both work in an own trinification/Chevalley frame and reproduce E6 = 78 from the cubic's stabilizer; the *landing* (class sizes from E6 root data) is still not re-derived | **medium** |
| 4 | Minkowski/Serre mod-p injectivity | remains (theorem cited; fresh primes checked in R02) | fence — cheap to add a third prime, not a proof |
| 5 | Rank-0/torsion-ℤ/3 of y² = x³ − 432 | remains (FLT n=3 literature) | fence — **cheap** to re-verify torsion via Sage/PARI; rank is literature |
| 6 | Reid 1990 / Maclachlan–Reid 3.3.7 | remains (steps checked in R08) | fence — theorem, not recomputable |
| 7 | G_N = 1/(4σ) | remains (physics identification unadjudicated) | fence — adjudication, not recomputation |
| 8 | B1088's CS mod-½ convention and SnapPy as instrument | **heavier again**: R21, R23, R24 all lean on SnapPy `symmetry_group()`/`is_isometric_to`/`chern_simons`; the CS ∈ {0, 1/4} ⇔ amphichiral consistency in R24 and the 220-bit shape confirmations in R23 are the only cross-checks; no verified interval arithmetic anywhere | **medium** (a `verify_hyperbolicity`/interval pass on the 112 and the seven R24 members) |
| 9 | B1225/B1203's W1 = 11,720 cloud enumerator; D3 17-atom provenance; reality-premise check | remains | **full** (enumerator not in repo) / cheap (reality-premise one-liner) |
| 10 | B994 provenance | **RECOMPUTED (R27, PARTIAL)** — endpoint MATCH, witness chain DISCREPANCY (D10), two E51 gaps (P2, P3) | closed as a recompute; owner fix pending |
| 11 | B1127's NEG∘π_mirror torsor (4-in/20-out) | **RECOMPUTED (R25, MATCH)** — 48 elements, 4 hits, all invariants match; Layer-8b not re-run | closed; Layer-8b **medium** if wanted |
| 12 | B1080 residuals; B1011 C5/C6; B1102 C3 doublet clause; trinification 36-count | **B1080 and B1011 RECOMPUTED (R26, MATCH; V18 on the lock)**; **B1102 C3 and the 36-count remain** | remaining halves **cheap** (both are finite representation-theory counts on data R22/R26 already built) |
| 13 | B1148's π₁ route 6615 → 4 → 1 | **RECOMPUTED (R22, MATCH; D11 convention note)** — including the direct 78,732-space nullspace the cert lacked | closed; ℚ-exact 6615 **cheap** |
| 14 | B1163's no-sibling-escape chain | **RECOMPUTED (R24, DISCREPANCY D9)** — headline survives, family-wide addenda fall | closed as a recompute; owner addenda pending; re-argument from the arithmetic legs **medium** |
| 15 | B1186's cusp-shape carrier and quine claims | **RECOMPUTED (R23, MATCH)** | closed |
| 16 | B1137's honest reclassification (V8) and basis-hygiene certificate | remains (owner action, not recomputation); the hygiene certificate is computable | reclassification: owner; hygiene certificate **cheap** (PSLQ/LLL independence test on 25 elements at high precision) |
| 17 | B725's classical fence (Gleason continuity lemma, type-III/GNS, SSB weights) | remains | fence ledger — not a recomputation |
| 18 | Kashaev deep tail | **RECOMPUTED (R28, MATCH)** — 67–88 digits, exceeding the banked ~30 | closed |

**Tally:** of the 18, **7 are now recomputed** (10, 11, 12 in its B1080/B1011 half, 13, 14,
15, 18; 5 MATCH, 1 PARTIAL, 1 DISCREPANCY — item 12's other half, B1102 C3 and the 36-count,
stays open and cheap), **5 remain as genuine recomputation targets** (1, 3, 8, 9, 16-hygiene:
one full, two medium, two cheap-to-full mixes), and **6 are fence-ledger items** that
recomputation is the wrong tool for (2, 4, 5, 6, 7, 17; item 5 has a cheap torsion sub-check).

**New gaps surfaced by R3** (candidates for an R4 or the fence ledger):

19. **B1163 residual "no sibling self-orients"** — re-derivation from the Galois/analytic legs
    without amphichirality (medium).
20. **B8147 addendum's 83/112 count** — the B8147 "denominator" census was never regenerated
    under the orientation-aware test; R20's 38/112 is the corrected figure but the 83-member
    subset's status is unstated (cheap, from R20's table).
21. **B994 over the parent-keyed map** — the 4-terminal-path walk in R27 is the honest
    rule-variation computation; a B994 rewrite needs the missing menus (owner; full if the
    menus must be enumerated).
22. **B1148 certs not in the committed tree** — the 6615/4/1 chain's generating code sits on a
    side branch (owner: land it; cheap).
23. **Interval-arithmetic pass over the SnapPy-dependent results** (items 8 and D5/D9): the
    38/112 amphichirality split, the 7 R24 members, the 112-member ℚ(√−3) certification
    (medium).

**Bottom line for the owner after three rings and thirty cells:** every headline banked number in
the recomputation program's scope has now survived independent blind recomputation, several
strengthened well past the bank (R22's direct 78,732-space nullspace and ℚ(ω)-exact holonomy
fixed space; R26's exhaustive 63-Levi sweep with two independent exact routes and a genuine
cell-by-cell 992/284 enumeration; R28's 67–88 Kashaev digits). The layer that keeps failing is
the same one R1 and R2 named — instruments that cannot fail (V17 = V9's second consumer, V18),
locks that assert arithmetic identities (V18), restatements dressed as tests (V15, V19) — with
two escalations this ring: **a refuted premise consumed downstream as a family theorem twice
(D9)** and **a banked witness that is not even a valid object in the claimed lattice (D10)**.
The owner actions that matter: dated addenda withdrawing B1163's family-wide and B8147 rows;
fix or rewrite B994's chains over the committed parent-keyed map and land a generator; correct
B1148's middle-rung prose (6615 → 9 → 1 in the full tensor, 4 under Sym³); relabel B964
(H2) and re-word B267's claim line (H1); replace the B1011 lock; and schedule an interval-
arithmetic pass on the SnapPy-dependent results before any of them is cited as a theorem again.

---

## DATED CORRECTIONS (2026-09-01, later the same day; owner's rule: sweep the repo before concluding an absence)

Every "in no committed file / does not exist / nothing committed" sentence in this report was
re-swept over all 7 remote heads and the deleted-file history
(`../sweeps/ABSENCE_SWEEP_LOG.md`). Three sentences change; no verdict does.

- **P2 (l.185, l.286) — CORRECTED.** "menus for parents SU(6)×SU(2), SU(3)³, Pati-Salam exist in
  no committed file" → *no committed **output** keys them, but committed **code** generates them:
  B869's engine (`frontier/B869_false_positive_control/false_positive_control.py`,
  `all_descents`), never run for these parents and not used by B994.* Run here
  (`../sweeps/p2_parent_menus_from_b869.py`): SU(3)³'s menu is {su(2)+su(3)+su(3)+u(1)} ×3 —
  **no Pati-Salam and no SU(5)×U(1) rung**, which strengthens D10; all three cascade endpoints are
  su(2)+su(3)+3u(1), which supports B994's endpoint claim on a subgroup basis. P3 stands.
- **V18 (l.272–274) — NARROWED.** "Nothing committed enumerates cells or evaluates a forcing
  criterion" → *`b1011_cells.py` **does** enumerate the 2880 elements (mod-61/241, asserted
  count); nothing committed evaluates a forcing criterion on them, so the 992/284 lock never
  touches the cells.* The vacuity verdict on the lock is unchanged.
- **F1 (l.368) — CORRECTED (wording).** "`docs/CLAIMS.md` does not exist" is literally true and
  misleading: the claims registry is root `CLAIMS.md` (231 lines) + `core/claims/{D4,P12,P15}.md`
  + `papers/P1_seam_form/CLAIMS.md` + `papers/P4_markov_stage/CLAIMS.md`; none carries a
  B964/B962/B952/B959/B960/VEV row (swept), so the refile touches none of them.
- **R22 fence (l.292–293) — STANDS**, with a new provenance finding: B1148's
  `reproduce_new.sh` cites `reproduce.log`/`our_uniqueness_chain.out`, which `.gitignore`
  (`*.log`, `*.out`) makes uncommittable — the "8/8 REPRODUCE" statement is unwitnessed on every
  head (B1148 addendum, appended section).

## DATED CLOSURES (2026-09-01, later the same day) — four §3 gaps closed by computation

- **Item 8 / item 23 (interval pass) — CLOSED for the hyperbolic-structure leg** by
  `R29_interval_hyperbolicity/`: own Krawczyk certificate (mpmath 300-bit intervals, no Sage) on all 112
  R23 members + m015/m016 controls, 114/114; **exact** ℚ(√−3) shapes for all 112 (fitted candidates satisfy
  every gluing equation exactly and sit inside the uniqueness box); **exact** cusp moduli on all 183 cusps
  with the seven 2√3i carriers reproduced name-for-name. Negative controls refuse 3_1/5_1/7_1 and perturbed
  shapes. **Still open (Sage-only):** CS values, symmetry groups, isometry classes, hence the 38/112
  amphichirality split — relay item for cc.
- **Item 13's "ℚ-exact 6615 (cheap)" — CLOSED** by the R22 addendum: rank_p ≤ rank_ℚ for every p gives
  dim_ℚ null ≤ 6615, the exact sl₂ Clebsch count gives 6615 ⇒ equality; five primes agree at rank 9855.
- **"D4 order not re-verified" — CLOSED** by `R30_m004_symmetry_group/` (filed earlier today as "R26";
  renumbered because R26 is B1080/B1011): SnapPy `symmetry_group()` order 8, amphichiral; o10_150700 order 2.
- **R25 "Layer-8b / unsigned-fold not re-run" (§3 table rows at l.313 and item 11) — CLOSED** by
  `R25_torsor_4of48/r25_layer8.py` (own construction, exact): (a) the unsigned diagram fold is an involution but
  **not** an automorphism — 672 of 78² basis pairs fail, all of them e–e pairs, and exactly the 672 root pairs
  (r,s) with r+s a root on which the Chevalley cocycle is not π-invariant (bank: 38/60 random trials; the same
  seeded trial style gives 40/60 here); (b) the secondary construction σ′ = τ∘θ_split∘θ_A checked for **all 16**
  antipodal/A bases (the bank did one): θ_split and θ_A commute, the product is an involutive automorphism in
  the permute/π_mirror family, I2 is stable, I2 antilinear signature **(5,3,0) for every base**, global
  (40,38,0), 0/16 compact — the bank's "(5,3,0), not compact" holds for any base, as a corollary of R25's
  permute/A result. Verdict on B1127 unchanged: MATCH; the compact-referenced alternative does not rescue
  a compact colour from the mirror.

Numbering note: cells are R01–R33; `R26_b1080_b1011` and `R30_m004_symmetry_group` are distinct.

## DATED CLOSURES (2026-09-01, evening) — Phase B reader flags turned into cells

- **B208 "300 000 re-audit" (reader flag CLAIM_EXCEEDS_COMPUTATION) — CLOSED, MATCH** by
  `R31_b208_radicand_divides_period/`: squarefree(m²+4) | m(m²+4)/gcd(m²+4,4) for every m ≤ 300 000
  (0 failures; v₂(m²+4) ∈ {2,3} for even m as the proof needs); the bank's two-line proof re-read and correct.
  The flag stands as a witness gap only: the committed script asserts to m = 200.
- **B213 "Higgs-side periods" (reader: IMPORTED, reproducible unknown, Sage-gated) — CLOSED, MATCH with
  corrections** by `R32_b213_elliptic_periods/` (PARI, no Sage): L(E,1)/ω₁ = 1/2 to 25 digits and the nine-curve
  null table reproduced; **but** torsion is ℤ/2×ℤ/2 not ℤ/4, ∏c_p = 4 not 8 (the 8 folds in the two real
  components), L(E,1) is misquoted by 7.5e−5, the Mahler measure m(Φ) is misquoted by 5.1e−4 (recomputed
  0.742264063…, two methods) and is not equal to L(E,1) nor a rational multiple of L′(E,0); and Φ = 0 is the
  2-isogenous class-mate [0,0,0,−32,64] (j = 55296/5), not 40a1 itself — B211's curve-level identification is
  off by an isogeny, harmless for L-values. The null table mixes the ω₁ and 2ω₁ period conventions between its
  40a2 and 40a3 rows. No observable content.

# RING R1 — RECOMPUTATION REPORT (synthesis)

**Date:** 2026-09-01 · **Seat:** fresh physics seat · **Directive:** owner, "a proof doesn't
necessarily mean a proof; compute every load-bearing proof."
**Discipline:** blind-first per cell (own code and outputs on disk before any arc
verification script was opened; read-before/read-after ledgers in each cell's FINDINGS.md
or, where the harness blocked a report file, in the cell's JSON/response record).

## Ring verdict at a glance

| cell | scope | verdict |
|---|---|---|
| R01 | B1225 no-canonical-selector | **PARTIAL** (core MATCH; one clause unreconstructable) |
| R02 | B1011/B1032 McKay tensor 2T×2I | **MATCH** |
| R03 | B1160/B1170 anomaly-forced hypercharge | **MATCH** |
| R04 | B994/B863/B861 termination + rule variation | **MATCH** |
| R05 | B862/B1080/B1221 ℤ₆ kernel | **MATCH** |
| R06 | B1134/B1135 simultaneous closing | **MATCH** |
| R07 | B952/B955 rank wall | **MATCH** |
| R08 | B298/B307/B1161 generation obstruction | **MATCH** |
| R09 | scale cluster (B666-S ×6, B1088/B250 volume, B1034 c=6σ) | **MATCH** (one VACUITY-ADJACENT note) |
| R10 | B1102/B1109 exact hypercharge | **MATCH** |

**Score: 9 MATCH, 1 PARTIAL, 0 DISCREPANCY, 0 BLOCKED cells.** No banked *number* anywhere
in the ten cells was found wrong. The ring's product is instead the vacuity/provenance
stratum in §2–§3: several banked *checks* could not have failed as instrumented, one banked
prose claim is literally false without a domain restriction, one addendum table is wrong
(in a direction that strengthens its own conclusion), and three results have no committed
producing code.

---

## 1. The diff table

Every load-bearing recomputed quantity vs the bank. "Mine" = blind, own code, exact
arithmetic unless noted. Cell artifact paths are listed in each cell dir under
`reports/fresh_physics_seat_2026-09-01/recompute/`.

### R01 — B1225 (no-canonical-selector)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| Aut(D) for m004 | D4, order 8, amphichiral | D4, order 8, 4 orientation-reversing (snappy, independent) | MATCH |
| G-action on the 17 tier-1 atoms | all fixed | 17/17 fixed, exact (sympy) | MATCH |
| G-action on menu values | trivial (0 moved) | 0/1173 single-op stratum moved; 761-value depth-1 closure all real hence c-fixed; construction-independent, so covers the banked cloud | MATCH |
| menu cardinality W1 | 11,720 (median gap 3.53e-5, min 1.63e-9) | **NOT RECONSTRUCTABLE** from any committed file (my closures: 761 / >300k, never 11,720; enumerator is cloud-side per the arc's own ADDENDUM) | OUT OF REACH → PARTIAL |
| step-5 "√ is G-equivariant" | asserted | **false without nonnegativity**: c(√(−2)) ≠ √(c(−2)), exhibited exactly; benign (menu values real) | DEFECT (benign) |
| control | — | planted mirror-odd atom i√2 → 69/648 values moved, nonzero cut | bite live |

### R02 — B1011/B1032 (McKay tensor)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| SL(2,3) ≅ 2T, McKay(V2) | affine E6 | order 24, 1 involution, iso verified on all 576 pairs, affine E6 | MATCH |
| SL(2,5) ≅ 2I, McKay(V2) | affine E8 | order 120, 1 involution, iso on all 14400 pairs, affine E8 | MATCH |
| SL(2,ℤ/4) ≇ 2O | B997-addendum table | 7 involutions / 0 order-8 elements vs 2O's 1 / 12 — table exact | MATCH |
| five-tone census; mirror menu | 30/24/40/24/2; 8 values over Q(√5) | identical, exact | MATCH |
| ΣΣ† (SU(3)₂ Kac–Peterson) | 75·I | 75·I exact in ℤ[ζ₁₅] (own Weyl-orbit construction) | MATCH |
| \|⟨R,L⟩\| | 2880 | 2880 at two primes disjoint from the bank's 331/421 + float | MATCH |
| conjugacy classes | 63, sizes = 2T×2I products | 63, size multiset exact | MATCH |
| global scalars | {I, −I} | {I, −I}, −I proved exactly from explicit word | MATCH |
| ρ₆ decomposition | (χ×V2(2I)) + (V2(2T)×V2(2I)) | 63/63 class-by-class (size, χ_odd, χ_even) exact mod Φ₁₅ | MATCH |
| lock hygiene | tests/test_b1011_mckay_tensor.py | **line 65 `assert ... or True` vacuous by precedence** (line 78 similar) | DEFECT (note) |

### R03 — B1160/B1170 (anomaly-forced hypercharge)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| linear anomaly cut | Yl=−3Yq, Ye=6Yq, Yu+Yd=−2Yq | same, exact | MATCH |
| cubic | roots t=±3 | −18(t−3)(t+3) at Yq=1, Yu=−1+t | MATCH |
| solutions | (1,−4,2,−3,6) and (1,2,−4,−3,6), zero non-SM | identical | MATCH |
| B1170 census | 252 contents / 222 killed by [SU(3)]³ / exactly 2 rigid chiral survivors (SM 15-plet + conjugate) | 252 / 222 / 30 color-safe / 2, same survivors, same charges | MATCH |
| Yq=0 clause of the brief | **UNBANKED** (in no committed file) | third cubic ray (0,s,−s,0,0): vector-like as U(1) multiset, but full gauge multiset not literally vector-like (Q unpaired) — prose would slightly overstate | RECOMPUTED, unbanked |
| bonus | — | dropping grav²Y: system birational to rank-0 Fermat cubic b²=a³−432; SM rays survive over ℚ even without grav²Y | strengthens bank |

### R04 — B861/B863/B994 (termination)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| step-1 registerability | SO(10)×U(1) 46 chiral / SU(6)×SU(2) 38 chiral / Sp(8) 36 vector-like / SU(3)³ 24 chiral | identical (own atom table, own branchings, exact) | MATCH |
| step-2 / step-3 | both chiral / SU(4)×U(1) 16 vector-like, SM 12 chiral; counts [3,2,1] | identical; (3,2) unpaired confirmed | MATCH |
| B863 termination | SM chiral; all four proper descents vector-like | identical multisets, incl. principal su(3)₁→su(2)₄ embedding index 4 | MATCH |
| B994 rule variation | 6 chains, all endpoints SM, sm_chain_share 1/6 | identical six paths, same extremal chains | MATCH |
| B861 convention gap | script uses 16 at step 2, 10+5̄ at step 3 | proved verdict-neutral (difference multisets self-conjugate) | E23 resolved |
| B994 provenance | results.json banked | **no committed producing script, no test lock anywhere** | DEFECT (provenance) |

### R05 — B862/B1080/B1221 (ℤ₆ kernel)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| SM 15-plet kernel | ℤ₆, generator (ω1₃, −1₂, ζ₆) | \|ker\|=6, cyclic, same generator, closure-verified (continuous circle, exact congruences) | MATCH |
| 16 / 10-of-27 / full 27 / minus-Q | 6 each | 6 each | MATCH |
| B1221 integer-charge control | 18 | 18 (both ambients, both field sets) | MATCH |
| B1080 MB12 control | Γ = 1 | 1 | MATCH |
| adjoint-only control | 72 | **finite only in their N=12 discretized ambient** (72 = whole search space); honest circle: infinite; still discriminates (≠6) | MATCH-with-note (mild vacuity) |
| primitivity ADDENDUM rescaling table | k=5,7,9,10,11 → 6/6/18/12/6 | **WRONG: true kernel is 6k** (30/42/54/60/66); verified (0,0,1/5) passes all conditions at k=5; banked values fit 6·gcd(k,12), an artifact of 12-torsion-truncated search | DISCREPANCY (addendum-level; strengthens primitivity) |

### R06 — B1134/B1135 (simultaneous closing)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| involutive slot-swappers / pairs | 48 (24 W / 24 δW) / 480 | identical (own Chevalley basis, full Jacobi on 3003 pairs) | MATCH |
| color census | (4,4):216 (5,3):240 (0,8):24 | identical; χ bijection +6/+2/−26; all 24 hits χ=−26 = E6(−26) | MATCH (stronger: full 3003-pair automorphism check on all 480 vs banked 40-trial spot-check) |
| B1135 | 128 preservers (64/64), 2000 conjugations, sterile W coset 1000×(5,3)³ χ=+6, flip coset (9+1)³, physics row χ=−14 dim 46 | digit-for-digit | MATCH |
| so(3,1) double clause | (3,3,0) on hits | holds for EVERY swapper-family candidate (verified on non-hits) — could not have failed within the swept family | VACUITY (single clause) |
| novelty split 4-in/20-out of B1127 torsor | banked | not independently rebuilt (needs B1127's torsor construction); aggregate substrate confirmed | PARTIAL subclause |
| controls | — | planted Chevalley involution → χ=−78 all-(0,8); fake form → χ=−10 (the historical E49 signature) with 72 bracket failures | bite live |

### R07 — B952/B955 (rank wall)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| all order ≤6 torus centralizers rank 6 | no exceptions | 66,377 tuples (SC convention), all rank 6; ss-rank histogram {6:389, 5:7074, 4:37314, 3:21600} | MATCH (with vacuity note below) |
| minimal centralizer su(3)+su(2)+u(1)³ | N=6, x=(0,0,0,1,2,1), dim 14 | found blind in adjoint scan, exact element reproduced | MATCH |
| convention | "order ≤ 6" | banked scan is adjoint-parameterized; that element has order 18 in SC E6, where A1+A2+u1³ first appears at order 7 — prose inconsistency, math unaffected | E23 resolved |
| B952 ledger | ranks 6/6/4, deficit 2, dims 14 vs 12 | identical | MATCH |
| H1(m004) = ℤ; no ℤ3×ℤ3 surjection | banked | own Smith normal form; 0/9 homs surjective; A4/D5/S5 hatch counts 24/20/240 reproduced | MATCH |
| locks | test_b952_rank.py, test_b955_l133scout.py | **both are prose/JSON-echo locks, no computation; the panel's scan had no committed code** — this cell supplies the first committed implementation | DEFECT (provenance) |

### R08 — B298/B307/B1161 (generation obstruction)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| m004 invariant trace field | x²−x+1, deg 2, disc −3, ℤ/2 | same via two independent routes (shapes+algdep at 400 bits; holonomy traces), nfisisom-confirmed | MATCH |
| B307 census | 32/500 cubic fields, all (1,1), all S3, 0 cyclic C3 | 32 / all (1,1) / all S3 / 0 C3 / no square disc, by an independent method | MATCH |
| totally-real C3 theorem | complex place forced | reconstructed independently (odd-order Galois ⇒ totally real; Reid 1990 / Maclachlan–Reid 3.3.7) | MATCH |
| B298 3-fold cover | 1 cover, H1 = ℤ/4+ℤ/4+ℤ | same | MATCH |
| lock layer | verdict.py / tests | **hardcoded census constants (N_CYCLIC_C3=0 etc.); B1161's reproduce.sh recomputes disc of the hardcoded poly without verifying it is m004's field** — could not have failed | VACUITY (lock layer only) |

### R09 — scale cluster

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| Hom(G,ℝ⁺)=0, six groups | orders 4/120/168/360/2880/51840; abelianizations (ℤ/2)², 1, 1, ℤ/3, ℤ/3, ℤ/2 | every row identical (from-scratch closures; W(E6) as permutations of own root system; CRT-verified SL(2,3)×SL(2,5), [G,G]=960) | MATCH (VACUITY-ADJACENT, §2) |
| Vol(m004) | 2.029883212819307250042405108549… (30 digits) | reproduced to 60 dps two independent ways (4Λ(π/6) via Im Li₂; 9√3·ζ_K(2)/π² via Hurwitz), agreement 6e−61; = banked 6Λ(π/3) | MATCH |
| CS(m004) | 0 (mod 1/2) | −1.15e−65 SnapPy HP; forced by amphichirality | MATCH |
| Brown–Henneaux / Sugawara | c = 6σ twice; c((E6)₁)=78/13·13? → 6 exactly | sympy-exact 6σ (l cancels); 78/13 = 6 with dim 78, h∨ = 12 from own root enumeration | MATCH |
| controls | — | planted SL(2,3)→μ₃ character found; ℤ→ℝ⁺ hom found — vanishing carried by torsion-freeness of target | bite live |

### R10 — B1102/B1109 (exact hypercharge)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| solution count | 18 rational, denominators ∣ 6 | exactly 18, via own 5⁴=625 exactly-solved bound; banked set = global negation ∘ ideal-swap of mine (E23: 3 vs 3̄ labeling, resolved exactly) | MATCH |
| purity | 0/18 pure on either ideal | 0/18, and forced at Cartan level (pure ⇒ ≥9 equal values vs max multiplicity 6) | MATCH |
| orbits | 2 orbits of 9 under W(A2)×W(A2); 36/72 set-preserving moves; swap 0/18 | identical (B1109 F4 numbers all reproduced) | MATCH |
| class structure | 15 classes, 3⁶·1⁹ | independently reproduced from own frame | MATCH |
| controls | — | planted pure and mixed directions recovered; different target → different orbit decomposition (2×18) | bite live |
| addendum | — | outer move (a,b)→(−b,−a) is an 18/18 symmetry exchanging the orbits (not in W(A2)×W(A2)) — no banked number affected | strengthens bank |

---

## 2. DISCREPANCY and VACUITY findings — the ring's product

No headline banked number was refuted. The findings below are the deliverable.

**D1 (DISCREPANCY, addendum-level — R05).** B1221's primitivity ADDENDUM
(2026-08-31) rescaling table is **wrong for k coprime to 6**: rescaling all charges by k
puts μ_k in the kernel, so the true kernel order is **6k** — 30, 42, 54, 60, 66 for
k = 5, 7, 9, 10, 11 — not the addendum's 6/6/18/12/6, which equal 6·gcd(k,12), the
signature of a 12-torsion-truncated search. Verified exactly: (0,0,1/5) satisfies all
conditions at k=5. Direction of the error: it *strengthens* the addendum's own primitivity
point. Owner action: addendum correction.

**D2 (DISCREPANCY, prose-level — R01).** B1225's banked step 5 asserts "√ is
G-equivariant"; this is **literally false** without a nonnegativity restriction:
c(√(−2)) ≠ √(c(−2)), exhibited exactly. Benign for the theorem (all menu values are real),
but the arc's own script does not check the reality premise that makes it benign.

**D3 (DISCREPANCY, prose/records-conflict — R01).** B1225's ADDENDUM claims the 17-atom
list "exists on no branch"; it contradicts B1203's committed `verification/reproduce.sh`,
which contains an explicit 17-atom dict (in main since commit 89affd5, 2026-08-30). Either
the addendum's search missed it or the dict is an unprovenanced stand-in — owner must
adjudicate which, since R01's whole recomputation conditions on that dict being MENU-1.

**D4 (DISCREPANCY, prose/convention — R07).** B955's "order ≤ 6" scan is in the adjoint
parameterization; its banked example element has **order 18** in simply-connected E6, where
A1+A2+u1³ first appears at order 7. Rank preservation is convention-independent, so the
math stands; the prose is inconsistent. E23 registry candidate.

**V1 (VACUITY, structural — R01, the load-bearing one).** B1225's theorem is **not** a
full vacuity but is *conditionally forced*: exactly one failable empirical premise (the 17
atoms are real — cloud's ω-tier shows a complex atom was possible) followed by a
definitional tautology (canonical = mirror-fixed; Aut(D) acts on invariants only through
the mirror; "the stabilizer fixes everything canonical" is the definition read twice).
Separately, B1225's own `reproduce.sh` is **vacuous as a computation**: it only greps
citation fragments out of other arcs' claim strings and never computes the action. R01 is
the first machine check of the theorem on the bench. No B1225-dedicated test lock exists.

**V2 (VACUITY, lock line — R02).** `tests/test_b1011_mckay_tensor.py` line 65 is
`assert ... or True` — vacuous by operator precedence; line 78 is similarly weaker than
intended. The targeted facts are true and other lock clauses are real; hygiene fix only.

**V3 (VACUITY, single clause — R06).** B1134's "so(3,1) double, signature (3,3)" clause
holds automatically for EVERY swapper-family candidate (verified on random non-hits): within
the swept family it could not have failed; it discriminates only against non-swappers
(ω gives (0,3,3)). The census clauses are genuinely falsifiable and reproduced.

**V4 (VACUITY, scan design — R07).** B955's "every centralizer has rank 6, no exceptions"
could not have failed *as instrumented*: the centralizer of a torus element contains the
torus by construction. The scan's falsifiable content (type tables, Borel–de Siebenthal
recovery, the minimal example) all reproduced; the planted-rank-drop control (diagram
involution → fixed-torus dim 4) shows what a real failure looks like.

**V5 (VACUITY, lock layer — R08).** B307's `verdict.py`/tests assert hardcoded census
constants (N_CYCLIC_C3=0 etc.) and B1161's `reproduce.sh` recomputes disc/degree of the
hardcoded polynomial x²−x+1 without verifying it is m004's field. The claims themselves
were re-established here independently; the locks could not have failed. Also a scope
note: `verdict.py`'s bare `GENERATIONS_FORCED_TO_MULTIPLICITY` constant reads stronger
than the theorem licenses ("if arithmetic" is the correct scope).

**V6 (VACUITY-ADJACENT, theorem shape — R09).** The scale-torsor "theorem" is the
one-liner that ℝ⁺ is torsion-free, so any hom from a finite group is trivial; the six
instantiations add no logical weight (the PROOF_NOTE concedes this). The real load-bearing
premise — every framework output stabilized by a finite/profinite group with no continuous
ℝ⁺ dial — is consumed **unproved** from B660/S3 + B652, where "no scale" is a grammar/
typing rule about the framework's own sealed grammar.

**V7 (VACUITY, control ambient — R05).** B1221's adjoint-only control value 72 is finite
only in the N=12 discretized ambient (72 = the whole search space |ℤ3×ℤ2×μ₁₂|); the honest
circle gives an infinite kernel. The control still discriminates (≠6), and the N=12
discretization is provably lossless for the headline contents (any |y|=1 field forces
t ∈ (1/6)ℤ). Mild flavour only.

**P1 (PROVENANCE, unwitnessed banked results).** Three banked results have no committed
producing code: **B994** (results.json with no script and no test lock anywhere in the
repo — R04 re-enumerated every field), **B955's panel scan** (no committed code — R07 now
supplies an independent committed implementation), and **B1225/B1203's W1 = 11,720**
(cloud-side enumerator; median gap 3.53e-5 and min gap 1.63e-9 likewise irreproducible
from committed files by anyone, including B1225 itself — E51-adjacent).

**Instrument note (E23-class, preserved deliberately — R08).** The v1 census scanner is
kept as an instructive instrument failure: single-precision algdep acceptance fits
spurious low-degree relations and reported all 500 manifolds as degree 2 before the
two-precision fix. Relevant to any future field-identification cell.

---

## 3. BLOCKED cells and typed missing data (R2 scaffolding candidates)

**No cell returned BLOCKED.** The one PARTIAL (R01) and the sub-clause gaps carry typed
missing data that R2 (or an owner action) could close:

| gap | typed missing datum | who can close it |
|---|---|---|
| R01: W1 = 11,720 | the cloud-side menu enumerator (tier rule + code) — commit it, or bank the count as CITED not PROVED | owner / cloud seat |
| R01: atom-list provenance | adjudication of D3 (is B1203's committed 17-atom dict the real MENU-1?) | owner |
| R01: reality premise | a committed check that all 17 atoms are real (one line; makes the theorem's single failable premise machine-checked) | trivial R2 cell or arc addendum |
| R04: B994 provenance | committed producing script + test lock for b994 results.json | owner (R04's re-enumeration can serve as the script) |
| R06: novelty split 4/20 | B1127's NEG∘π_mirror torsor construction, independently rebuilt | R2 cell with B1127 scaffolding |
| R05: B1080 residuals | six-Weyl-realization E6 sweep from root data; row-4 Γ=ℤ/5 claim | R2 cell (both were outside R05's compute spec) |
| R02: B1011 C5/C6 | 992/284 forced-count semantics; B641/B856 derivation chains | R2 cell (outside R02's brief) |
| R03: trinification 36-count | cloud's vendored stack (banked as cited, not proved, in the arc itself) | cloud seat |
| R10: B1102 C3 clause | su(2)-doublet count (6 doublets + 15 singlets) — outside R10's banked-claims list | cheap R2 add-on |

---

## 4. Honest coverage statement — what this ring did NOT touch

R1 covered ten proof clusters. **The masterplan's R2 queue (untouched, still owed):**
**B1183** (one-class) · **B1141** (spin payment) · **B904** (magic square, 3003 brackets) ·
**B884** (the cubic, 45 monomials) · **B892** (SMT) · **B1120/B1133** (Kashaev tower) ·
**B1126/B1137** (value scans — re-run of the committed sealed instruments only) ·
**B1003** (genesis forks) · **B725** (Born form) · **B1136** (family separator).

**Load-bearing premises this ring consumed without recomputing** (they condition R1's
MATCHes and belong on R2-or-later or the fence ledger):

- **B873's P5 menu-completeness gate** (conditions all of R04; explicitly-out-of-scope
  fence, plus B861's unresolved SU(3)₉ special embedding and B863's exotic-conformal-
  embedding carve-out — and batch 2 already found the su(3)⊕g₂ registerable-outside-menu
  witness, a named batch-3 cell).
- **B660/S3 + B652's "no continuous dial" premise** (the real content of the scale no-go;
  R09 characterized it but cannot prove it — it is a typing rule of the sealed grammar).
- **B1098/B1100's trinification landing** (taken as frame in R10; cross-anchored via
  class sizes, not re-derived from E6 root data).
- **Minkowski/Serre mod-p injectivity** for group-order exactness (R02 — verified at two
  fresh primes plus float, but the theorem itself is cited).
- **Rank-0/torsion-ℤ/3 of y² = x³ − 432** (R03 — cited from FLT n=3 literature).
- **Reid 1990 / Maclachlan–Reid 3.3.7** (R08's complex-place step — theorem cited, steps
  checked, not re-proved).
- **Literature claims in B955** (Keurentjes {6,2,0} for π₁=ℤ³; the Q4/Acharya 137-citer
  sweep; Jordan rank-1 27-VEV → SU(5)) — none load-bearing for the rank wall.
- **G_N = 1/(4σ)** (B1012): R09's Brown–Henneaux clause verifies algebra only; the
  physics identification is unadjudicated.
- **B1088's CS mod-1/2 convention** and the SnapPy symmetry engine (R01/R09 trust snappy's
  symmetry_group/high-precision outputs as instrument, cross-checked but not re-implemented).

**Harness/process notes:** R02 and R10 could not write FINDINGS.md to their cell dirs
(subagent report-file rule); their full findings live in the workflow record and their
machine-readable JSONs are committed in the cell dirs. R09 created its FINDINGS.md via
bash for the same reason. R06/R07 reused blind code from earlier interrupted sessions of
the same cells (re-verified line-by-line / re-run with identical outputs, as their
FINDINGS record). R08 notes a cypari 3.3.2 double-free worked around with keepalive +
os._exit.

**Bottom line for the owner:** the ten most load-bearing proofs survive independent blind
recomputation — every banked number reproduced, several now stronger (full 480-candidate
automorphism check in R06, Witten-filter-insensitivity in R03, 6k rescaling law in R05,
committed rank-wall scan in R07). What did not survive scrutiny is the *verification
layer*: one addendum table wrong (D1), two prose defects (D2, D4), one records conflict
(D3), five-plus vacuous or echo-only locks (V1, V2, V5, P1), and three unwitnessed banked
computations (P1). Ring R2 should carry both the queued ten and the typed gaps in §3.

---

## DATED CORRECTIONS (2026-09-01, later; owner's rule: sweep the repo before concluding an absence)

Re-swept over all 7 remote heads + deleted-file history (`../sweeps/ABSENCE_SWEEP_LOG.md`).

- **R03 / l.73 "Yq = 0 clause — UNBANKED (in no committed file)" — NARROWED.** True on main;
  false repo-wide: `frontier/B8143_anomaly_lane/` on `paper/structure-genesis-first` (a31456d2,
  never integrated) computes the third branch *"{Yq = 0, Yd = −Yu, Yl = Ye = 0} ← a ONE-PARAMETER
  VECTOR-LIKE family"* and is the origin of B1170's 252/222/2 counts. R03's refinement of that
  phrasing (vector-like as a U(1) multiset; the full gauge multiset is not literally vector-like,
  Q unpaired) applies to B8143's wording too. B8143's own pointer "= B864's third line" does not
  match B864's committed `results.json` (`uniqueness.forced = [{b:0,c:0}]` in the Q = aY+bχ+cψ
  ansatz — no third line).
- **R07 / l.118 "the panel's scan had no committed code" — STANDS**, scope clause: B1079's `v`
  block confirms the checker code sat in a scratchpad (`e6_menu_*.py`, never committed);
  `frontier/B796_coupling_campaign/h1_consumed/rank_wall_scope.py` on `audit/b775` is a
  committed *class-scope* probe of the same wall (SnapPy, 3-rank of H₁ across m004's
  commensurability class) — a different computation, worth citing beside B955.
- **R04 / l.85 "no committed producing script, no test lock anywhere" (B994) — STANDS** on all
  7 heads (`test_b994*` 0/0 everywhere; no `.py/.sh/.sage` under `frontier/B994_*`).
- **R01 / l.46 "W1 = 11,720 NOT RECONSTRUCTABLE from any committed file" — STANDS on main,
  NARROWED repo-wide** (enumerator `outside_bench/certificates/menu_width.py` on
  `claude/outside-bench`; internalization INDEX #34 already records this).

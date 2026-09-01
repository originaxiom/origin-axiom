# RING R2 — RECOMPUTATION REPORT (synthesis)

**Date:** 2026-09-01 · **Seat:** fresh physics seat · **Directive:** owner, "a proof doesn't
necessarily mean a proof; compute every load-bearing proof."
**Discipline:** blind-first per cell (own code and outputs on disk before any arc
verification script was opened; read-before/read-after ledgers in each cell's FINDINGS.md
or, where the harness blocked a report file, in the cell's JSON/verdict record).
Numbering of findings continues R1's (D1–D4, V1–V7, P1 live in `R1_REPORT.md`).

## Ring verdict at a glance

| cell | scope | verdict |
|---|---|---|
| R11 | B1183 one-class theorem (Z/2 obstruction probes) | **MATCH** |
| R12 | B1141 spin payment (Pin lift selection) | **MATCH** |
| R13 | B904/B854 magic square (split-octonion E6 build) | **MATCH** |
| R14 | B884 the cubic (45 monomials, uniqueness, cells) | **MATCH** |
| R15 | B892 Second Measurement Theorem | **MATCH** |
| R16 | B1120/B1133 Kashaev tower coefficients | **MATCH** |
| R17 | B1126/B1137 value-disjointness scans | **PARTIAL** (B1126 MATCH; B1137 re-run MATCH but instrument VACUITY) |
| R18 | B1003 genesis forks F2/F8 | **MATCH** |
| R19 | B725 Born form (scoped) | **MATCH** |
| R20 | B1136/B1186 family separator | **PARTIAL** (separator MATCH; amphichirality refuted; "exactly 14" truncation artifact) |

**Score: 8 MATCH, 2 PARTIAL, 0 BLOCKED cells.** As in R1, no *headline* banked number was
refuted — the sole separator (H1 = Z), the one-class theorem, the spin selection, the E6
build, the unique cubic, the SMT censuses, five Kashaev coefficients, both scan outputs,
both genesis-fork prices and both Born-form sub-claims all reproduce from independent blind
code, many upgraded from numeric/mod-p to exact. The ring's product is again the
verification-layer stratum: **two banked claims refuted as stated** (family-wide
amphichirality, D5; "exactly 14", D6), **one structural instrument vacuity** (B1137 could
not have found any genuine relation at physical precision, V8), and a tail of lock-layer
vacuities and prose/metadata defects.

---

## 1. The diff table

Every load-bearing recomputed quantity vs the bank. "Mine" = blind, own code, exact
arithmetic unless noted. Artifacts in each cell dir under
`reports/fresh_physics_seat_2026-09-01/recompute/`.

### R11 — B1183 (one-class theorem)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| P1 orientation probe | {±Vol} free Z/2-set under c | m004 amphichiral (SnapPy, sym order 8); D(conj z)=−D(z); Vol=2·D(e^{iπ/3})=2.0298832128≠0 | MATCH |
| P2 chord sign | {±√3} free under c | Im f(ω̄)=−Im f(ω) exact from B760 data via B238 su3_data(2); general real-coefficient lemma symbolic | MATCH |
| P3 eigenvalue choice | {ζ5, ζ5⁴} free | weld block rebuilt: eigenvalues ζ5^{±1}, tr=1/φ, det=1, char poly x²−(1/φ)x+1 exact; conj(B)=εBε⁻¹, ε²=−I | MATCH |
| P4 mirror/Gal on K=Q(√−3) | free | mirror conjugates holonomy traces (SnapPy, multiset on a,b,ab) | MATCH |
| c-restriction identities; 15/32 c-invariance | banked | ω̄=ω², ζ̄5=ζ5⁴=σ4 fixing √5; 15/32 exact | MATCH |
| vacuity boundary | at \|G\|=2 equivariance free | 2/2 bijections equivariant (3/6 at \|G\|=3); load-bearing content = freeness/non-collapse, verified case by case | MATCH |
| banked reproduce.sh | one_class.txt | re-run exits 0, output byte-identical | MATCH |
| controls | — | Q(√5) value bit (not free — B1174's refuted leg), collapsed sign-set, wrong involution σ7 all caught; 41/41 own checks | bite live |

Notes: B1183's own script asserts only legs (a)–(c); leg (d) and P1/P4 freeness are
prose/citation (V12). FINDINGS.md header carries stale `creates_law:false` vs the
B1211-corrected `creates_law:true` in arc_verdict.json (metadata only).

### R12 — B1141 (spin payment)

| claim | banked | recomputed (blind, third independent engine) | verdict |
|---|---|---|---|
| relator / lift census | R(A,B)=+I; two SL(2,C) lifts | exact over Q(ω): R(−A,−B)=+I, R(−A,B)=R(A,−B)=−I; χ(a)=χ(b)=−1, consistent with H1=Z | MATCH |
| beat / intertwiner | beat²=conj-by-a; W system rank 3, nullspace 1; W0=[[1,−ω],[0,1]], W0·conj(W0)=+A | identical, exact | MATCH |
| twisted lift killed | \|λ\|²=−1 impossible | reproduced; same intertwiner line, proportional | MATCH |
| SnapPy leg | m004 Vol, H1=Z; m000 nonorientable, half volume | Vol 2.0298832128; orientation cover isometric to m004; (A,B) found inside SnapPy holonomy by trace-triple word search | MATCH |
| NEW leg (beyond arc) | — | beat derived independently from m000's actual holonomy (beat'(a)=a, beat'(b)=bab⁻¹): identical selection — representative-independent | strengthens bank |
| controls | — | fake beat → rank 4; W·conj(W)=−I achievable in general (the + sign contentful) | bite live |

Notes: banked beat words are the Gieseking gluing only up to a half-longitude cusp symmetry
Q=[[1,√3·i],[0,1]] ∉ Γ (cusp lattice ⟨1, 2√3·i⟩ verified) — wording nuance, not a
discrepancy. Census leg is parity-forced given R(A,B)=+I (partial-vacuity note, V13);
consistent with codex R021 LEG 7 (both representatives select the untwisted lift).

### R13 — B904/B854 (magic square)

| claim | banked | recomputed (blind, from-scratch Barton–Sudbery over Q) | verdict |
|---|---|---|---|
| triality dims; cross products | 28 / 2; six products | tri(O)=28, tri(C')=2; products derived as unique equivariant survivors, identical | MATCH |
| full Jacobi | (B854 sampled 4,000 triples) | **0/76,076 full**, both on my build and on the banked stage2c tensor | MATCH (stronger) |
| root system | E6 Cartan matrix | 72 one-dim root spaces + 6-dim Cartan, Cartan matrix exactly E6 (rational torus) | MATCH |
| Chevalley-word iso to B854 | φ, det −2/3, lock 6/6 | own re-implementation: 0/3,003 mismatches; banked φ re-verified under my evaluators (0/3,003, det −2/3 exact); B854 BB tensor = mine, 0 differing entries | MATCH |
| pairing normalization | μ=−24, ν=−12 | μ=−6, ν=−3 (×4 from half-polar pairings; μ/ν=2 both sides) | E23 resolved |
| controls | — | corrupted constant → 330 failing triples; corrupted generator → 16/60 failing pairs | bite live |

Note: det φ is not an invariant (φ unique only up to automorphism/rescaling); my φ has
det −2^25/3 — matched in the invariant sense, banked value reproduced on their φ.

### R14 — B884 (the cubic)

| claim | banked | recomputed (blind, two independent constructions) | verdict |
|---|---|---|---|
| dim Inv(Sym³ 27) = 1 | banked | two routes: Freudenthal characters (3003+650+1) AND exact nullspace under 78 explicit generators; shape-free endpoint dim Inv(27⊗27⊗27)=1 (27×27=351'+351+27̄) ⇒ survivor automatically symmetric | MATCH |
| 45 monomials, coefficients ±1 | banked (B854 Chevalley frame) | exactly 45 zero-sum weight triples (all squarefree); support 45/45, coefficients {−1,+1} in my trinification frame; I = detA+detB+detC−tr(ABC); gl(27)-stabilizer = 24+27+27 = 78 = e6 exact | MATCH (frame E23) |
| cells | 11 coupled / 275 zero of 286; sizes {1,1,1,2,2,2,3,3,3,3,6} | identical one-for-one with arc results.json; charge-forced addendum verified EXACTLY (upgrades arc's 7.7-order numeric gap to symbolic) | MATCH (stronger) |
| controls | — | sl3³-only nullspace = 4; Sym³(27+27̄) → 2; mixed-block ansatz → 0 | bite live |

Notes: B884 FINDINGS prose says "two [2,3,6] shapes" — its own results.json (and mine) have
**three** {2,3,6} cells; banked count 11 is right (cosmetic prose slip). The task card's
"6615 → 4 → 1" chain is memo-48/B1148's full-tensor π1 route, not B884's pipeline; the 6615
stage was NOT re-run (needs B1148's holonomy instrument) — both shape-free ends match.

### R15 — B892 (Second Measurement Theorem)

| claim | banked | recomputed (blind; own e6 build + principal-sl2 charges) | verdict |
|---|---|---|---|
| charge vectors | B854 INV vectors | byte-identical | MATCH |
| censuses | 30/12/30/12, core 30, Cent(C) 12 | identical | MATCH |
| enhancement cubic | hard-coded CUBIC | 500716339200x³−159667200x²−28224x+1 verbatim; = B877's μ under the arc's 13x convention | MATCH (E23) |
| z(x1)=46 → so(10)+u(1) | banked | exact over F (restriction of scalars); derived 45/center 1 at primes 40123 and 40039; not su(5) | MATCH |
| wall: dim z(x1,y*)=14 = su(3)+su(2)+u(1)³ | banked | slope poly = (even sextic)²·(even sextic)⁶ ⇒ 14 EXACT over closure; derived 11 (unique A2+A1), center 3 a priori; 14=8+3+3 | MATCH (upgraded to exact) |
| residues | banked digits | −a_q/(13γ_q)=6167 mod 40123 a root of my sextic; μ×sextic grid = 14 on exactly the 6 matched pairs | MATCH |
| wall complex; no 26/su(5) on the line | banked scan | proved exactly (all-positive even sextics: no real roots; six SM-wall slopes pure imaginary); only dims 12/14/18/30 over closure; B874's 26/A4 points in a different family (x22) | MATCH (stronger) |
| within-C ladder {18,14}; B992 compatibility | banked | reproduced; u(1)³ center inside charge torus C | MATCH |
| control | — | A4-annihilating Cartan element → 26/derived 24 (su(5)+u(1)²) through the same pipeline | bite live |

Notes: repo lock `tests/test_b892_smt.py` is text-assertion-only — vacuous as a
mathematical check (V10); this cell supplies the missing recomputation. One banked digit
not reproduced: det14 = +2.79e9 (normalization-dependent tower quantity); the fact it
certifies (a imaginary → wall complex) is proved exactly instead.

### R16 — B1120/B1133 (Kashaev tower)

| claim | banked | recomputed (blind; mpmath dps 620, N ≤ 4200, Richardson/Vandermonde) | verdict |
|---|---|---|---|
| C0 = 3^{−1/4} | ~30 digits | ~25 digits agreement | MATCH |
| C1 = (11/108)√3·π·C0 | banked | ~21 digits; fitted ratio 0.101851851…=11/108 | MATCH |
| C2 = (697/7776)π²·C0 | banked | ~17 digits; 0.08963477366255144009… | MATCH |
| C3 = (724351/12597120)√3·π³·C0 | banked | ~14 digits | MATCH |
| C4 = (278392949/1813985280)π⁴·C0 | banked | ~11 digits | MATCH |
| reality-parity law (odd orders carry √3) | banked | reproduced | MATCH |
| control | — | 12/108 in place of 11/108 mis-fits at 9.1e-2 rel vs ~1e-21 — rejection by ~19 orders | bite live |

Notes: confirmation is 11–25 digits (banked ~30 used N up to 35M) — well above the 6–10
digit pass bar. Banked lock tests validate closed forms against the arcs' own stored pooled
JSONs — internally consistent, not independent (V14); this cell is the independent check.
Gate 5 untouched (only π, √3, Li₂ at a root of unity, integers).

### R17 — B1126/B1137 (value scans) — PARTIAL

| claim | banked | recomputed | verdict |
|---|---|---|---|
| B1126 output | b1126_results.json | committed b1126_compare.py re-run unmodified → JSON-identical: 352 pairs; sig-fig histogram {0:344, 1:7, 3:1}; sole survivor C1/C0=11π/(36√3) vs sin θ12, rel 2.53874e-4; p_LE=0.1637 | MATCH |
| B1126 comparator power | — | rollover pair → 7 sf; planted 1e-4/1e-6 → 4/6 sf; verdict flips to NEEDS-INSTRUMENT for rel ≲ 2.9e-5 (planted positive passes) | audit SOUND |
| B1126 dismissal grounds | 3 grounds | look-elsewhere computed; pre-commitment hardcoded-but-true; instrument-existence hardcoded False, backed by grep re-verified on today's tree | MATCH (with D8 note) |
| B1137 output | final_report.json | full committed pipeline re-run (real 216, null 400 @ seed 17/n=100, aggregate) → DICT-IDENTICAL: DISJOINT, 0 regulator relations, null rates 0.0, α_cell 2.374e-4; controls to 50+/97+ digits | MATCH (bytes) |
| B1137 instrument power | (implicit) | **planted true relation 5V−3L(1,χ₋₃)−2π=0 is UNFINDABLE/UNPASSABLE at every physical budget** — see V8 | **VACUITY** |

Pre-existing arc-internal mismatches: FINDINGS/arc_verdict say 384 null cells (96/H) vs the
committed report's 400 (100/H) (D7a); FINDINGS' claim that only δ_CP and m_s/m_d produced
"stable, height-legal, within-1σ" relations vs the committed report's ten targets with
V-alone finds, none marked stable/height-legal (D7b).

### R18 — B1003 (genesis forks)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| F2 (A2's price): finite orders | tr²−k²=4 lemma locus | Cayley–Hamilton route: orders 3/4/6 at tr −1/0/1; infinite at non-central ±2; max\|eig\|=1 exact; pA count 0 for the det=+1, \|tr\|≤2 family; exhaustive scan: finite order ⇔ tr ∈ {−2..2} (same locus, different route — E23) | MATCH |
| F2 sibling twisters | 0 geometric | 0/8 of my OWN fresh 8 sibling builds geometric; controls 'aB'/'aBaB' → exact banked FRAGILE signal, vol 2.02988321282, isometric to m004 | MATCH |
| F8 (A5's price) W1–W4 | banked | x²+3 irreducible over Q(√5) (two exact routes; control splits over Q(√−3)); Fibonacci freqs (φ−1, 2−φ), gap group Z[φ]; cone forces End = Z[M] ≅ Z[φ], no X²=−3 (order-forgotten [[0,1],[−3,0]] squares to −3I but is NOT cone-preserving); SNF(M)=I ⇒ K0=Z² torsion-free, K1(AF)=0, no ζ3; x²+15 also irreducible | MATCH |
| lock | tests/test_b1003_f2_f8_locks.py | 5 passed | MATCH |

Notes: cell FINDINGS.md blocked by harness (record in the workflow text + committed
scripts/JSONs). Not re-verified (outside banked-number scope): arc's per-build H1/Wang
fingerprint pinning; Seifert/graph-manifold classification of sibling geometries.

### R19 — B725 (Born form, scoped)

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| (a) norm form deg = \|Gal\| | ψ·c(ψ)=x²+y², deg 2; falsifier deg 3 | exact sympy: N_{C/R} degree 2, c an involution; 2cos(2π/7) root of t³+t²−2t−1, σ: t→t²−2 order 3, Galois-orbit norm a homogeneous integer cubic (resultant + multiplicativity cross-checks); post-blind: coefficient-level IDENTICAL to arc's regular-representation determinant (DIFF=0) | MATCH |
| (b) Gleason harmonic core | survivors l ∈ {0,2}; 1+5=6=dim Sym(3×3) | own exact harmonic bases l=0..6 (dims 2l+1), frame-sums at 12 exact rational rotations over FULL bases; survivors exactly {0,2} (l=2 symbolic: frame-sum of quadratic form = tr(A)); l=1,3,4,5,6 excluded with exact witnesses | MATCH |
| dim-2 non-vacuity | (1+n_z³)/2 | h(n)=n_z³ antipodal-null yet not affine — same function affinely renormalized (E23) | MATCH |
| control | — | (x²+y²+z²)² correctly flagged as survivor (frame-sum exactly 3) | bite live |

Notes: lock `tests/test_b725_born.py`'s probe-1 falsifier asserts only deg(minpoly)==3, not
the norm-form degree — that assertion could not have failed (V11); the probe script and
this cell carry the genuine check. Cited-classical, not recomputed (per scope): full
Gleason (arbitrary frame functions, continuity lemma); type-III/GNS apparatus; probe-2 SSB
weights; "amplitudes live in C" is an input from B715/B716 (flagged in the arc itself).

### R20 — B1136/B1186 (family separator) — PARTIAL

| claim | banked | recomputed (blind) | verdict |
|---|---|---|---|
| seven-property separator table | sole separator H1=Z | row-for-row match (exact sharer sets); robust to every correction found (incl. corrected amphichirality and 21-member scope) | MATCH |
| B1186 family = 112; regular subfamily 77 | banked | set-identical from own full-census sweep (212,641 manifolds), exact sympy gluing certification of every member; A ⊂ B, 35 non-regular | MATCH |
| t06829 | max den 98, vol = 3×Vol(m004), "7 tets" | reproduced exactly (max den 98, next 49; exact certificate); **has 8 tets, not 7** (typo) | MATCH (typo note) |
| CS consistency | B1136 vs B1224 | own CS(m003)=+1/4 confirms B1224; m003 never in banked CS=0 set; no separator status changes | MATCH |
| volume integer ladder | 14 at n ∈ {2,4,5} | all 112 at n·V_gie, n ∈ {2..10} (dist {2:2,4:7,5:5,6:12,7:4,8:31,9:4,10:47}) | MATCH |
| family-wide amphichirality (112/112) | banked | **REFUTED — 38/112** under two agreeing orientation-aware tests; only 6 of the banked 14 (m003, m004, m203, m206, m207, s596); banked instrument cannot fail | **D5 + V9** |
| B1136 "exactly 14" | banked | **21** ≤6-tet members (s955–s961 at census indices 1256–1262 missed by a break at index 1200) | **D6** |
| B1224 2-torsion law | CS ∈ {0, 1/4} mod 1/2 | zero violators on the corrected 38; FAILS on the vacuous set (chiral m202, CS=1/12) — independent confirmation of the correction | MATCH (on corrected set) |

Controls: certifier rejects wrong shapes; dropping m003 → 3 separators; planting m015
kills the H1 separator; m006 negative excluded; t06829 found by sweep as planted positive;
amphichirality calibrated on 9 knowns.

---

## 2. DISCREPANCY and VACUITY findings — the ring's product

**D5 (DISCREPANCY, banked-claim-level — R20, the ring's biggest).** B1136/B1186's
"family-wide amphichirality" (112/112, and 14/14 at the B1136 scope) is **refuted as
stated**. The banked instrument (`reverse_orientation` + `is_isometric_to`) is incapable of
returning False — it passes known-chiral m015/m016/m019 (V9). Under two independent
orientation-aware tests that agree on all 112 (self-isometry cusp-map det = −1;
`symmetry_group().is_amphicheiral()`, calibrated on 9 known manifolds), only **38/112** are
amphichiral, and only **6 of the banked 14**: m003, m004, m203, m206, m207, s596 (chiral:
m202, m208, m410, m412, s118, s119, s594, s595). B1224's CS 2-torsion law independently
confirms the correction: zero violators on the corrected 38, while the vacuous set contains
e.g. chiral m202 with CS = 1/12 ∉ {0, 1/4}. **Amphichirality remains a non-separator**, so
the headline separator result survives; but "112/112" is false, and **B1163's downstream
no-sibling-escape chain cites it** — owner must re-audit B1163 (not done in this cell).
Caveat: the correction rests on SnapPy's numerical isometry/symmetry engine (two agreeing
kernel routes + the exact B1224 consistency check), not verified interval arithmetic.

**D6 (DISCREPANCY, count-level — R20).** B1136's "exactly 14" ≤6-tet family members is an
artifact of `verify_genericity.py` breaking at census index 1200: s955–s961 (indices
1256–1262) satisfy the criterion, so the true count is **21**. All 7 extras are in B1186's
112 (which supersedes the 14), and the separator verdict is unchanged at either scope.
Cause is truncation — not the criterion conflation B1186 itself named as the suspected
cause. Also: t06829 has 8 tetrahedra, not the banked 7 (typo).

**D7 (DISCREPANCY, prose/artifact conflicts inside the banked B1137 arc — R17).**
(a) FINDINGS.md and arc_verdict.json say "384-cell matched null (96/H)"; the committed
`results/final_report.json` says 400 (100/H), and no committed configuration reproduces
384. Verdict-irrelevant (rates 0.0 either way). (b) FINDINGS says only δ_CP and m_s/m_d
produced "stable, height-legal, within-1σ" relations; the committed report shows ten
targets with V-alone finds (117 total) and **none** marked stable/height-legal (the gate
short-circuits earlier).

**D8 (DEFECT, cosmetic — R17/B1126).** Each survivor's `final_disposition` text is a
constant "fails all three grounds" string independent of the computed flags; the top-level
verdict branch is computed and correct (verified by planted positive), so this is
verdict-safe. Ground 2 (instrument-existence) is a hardcoded False backed by a grep the
script does not run — re-executed this bench and confirmed (no tracked-.md line co-locates
Kashaev with neutrino/PMNS/θ12 vocabulary).

**V8 (VACUITY, structural — R17/B1137, the load-bearing one).** The banked DISJOINT
verdict is true and byte-reproduces, but **the instrument could not have found ANY genuine
regulator relation at physical measurement precision**. Planted true relation
5V − 3·L(1,χ₋₃) − 2π = 0 (height 5) through the committed `run_cell` unmodified: at
digits=250 PSLQ finds the exact coefficients but `exact_stable` rejects them — the residual
is pinned at the parse floor (mp.dps+25) while the gate demands dps+60; at digits=60
(prereg floor) and digits=10 (best physical target, m_p/m_e) the relation is not even found
(truncation residual ~1e-10..1e-60 vs tol 1e-106..1e-257). The ADMITTED/HIT terminus is
structurally unreachable for every physically measured target at all 216 cells, and the
matched null's 0.0 is guaranteed by the same mechanism (surrogates truncated identically).
By the arc's own PREREG §E grammar the honest outcome type was **FLOOR** (decisive
precision ~176+ exact digits vs a best physical budget of 10), not a contentful DISJOINT.
Assumes the pruned 25-element basis is Q-linearly independent with 1 (asserted;
`basis_hygiene_check.py` not committed in the arc dir) — the parse-cap-vs-gate code
mismatch holds regardless. Owner action: reclassify or fix the gate and re-run.

**V9 (VACUITY, instrument — R20).** The banked amphichirality check cannot fail (see D5).

**V10 (VACUITY, lock — R15).** `tests/test_b892_smt.py` is text-assertion-only — vacuous
as a mathematical check of the SMT. R15 supplies the missing recomputation (much of it
upgraded to exact-over-the-closure).

**V11 (VACUITY, lock assertion — R19).** `tests/test_b725_born.py`'s probe-1 falsifier
asserts deg(minpoly)==3 rather than computing the norm form's degree — that assertion could
not have failed. The probe script and R19's blind recompute both carry the genuine
degree-3-norm result. Claim-level content unaffected.

**V12 (PARTIAL-VACUITY, script scope — R11).** B1183's own script asserts only legs
(a)–(c); leg (d) and the P1/P4 freeness claims are prose/citation (fenced by the arc). R11
machine-checked them independently — gap now closed on the bench, not in the arc.

**V13 (PARTIAL-VACUITY, note — R12).** B1141's lift-census leg is parity-forced given
R(A,B)=+I; the load-bearing rank/sign claims are contentful and control-checked.

**V14 (VACUITY-ADJACENT, lock provenance — R16).** The banked Kashaev lock tests validate
closed forms against the arcs' own stored pooled JSONs — internally consistent, not
independent. R16 is the first independent recomputation; it agrees at 11–25 digits.

**M1 (METADATA — R11).** B1183/FINDINGS.md header says `creates_law:false` while
arc_verdict.json carries the B1211-corrected `creates_law:true` (stale retro-authored doc;
math unaffected).

**Prose slips (cosmetic):** B884 FINDINGS "two [2,3,6] shapes" — its own results.json has
three (banked count 11 correct). B1186 t06829 "7 tets" — it has 8.

---

## 3. BLOCKED cells and typed missing data

**No cell returned BLOCKED.** The two PARTIALs and the sub-clause gaps carry typed missing
data:

| gap | typed missing datum | who can close it |
|---|---|---|
| R17: B1137 vacuity | either a fixed stability gate (parse at dps+BOOST, not dps+25) + planted-positive CI, or an honest FLOOR reclassification per PREREG §E | owner (arc addendum) |
| R17: basis hygiene | committed `basis_hygiene_check.py` proving the 25-element basis Q-linearly independent with 1 | owner |
| R17: null-cell prose | adjudicate 384 (96/H) vs committed 400 (100/H); fix FINDINGS target-claims (D7b) | owner |
| R20: amphichirality | verified-interval (or exact) amphichirality certificates for the 38/74 split; arc corrections to B1136/B1186; **re-audit of B1163's chain, which cites 112/112** | owner / R3 cell |
| R20: "exactly 14" | B1136 addendum: unbounded census sweep → 21 at ≤6 tets | owner (R20's sweep can serve) |
| R20: B1186 residue | cusp-shape carrier and quine claims not independently re-verified (outside the seven-property remit) | R3 cell |
| R14: 6615 stage | memo-48/B1148's π1/holonomy full-tensor route (6615 → 4 → 1) — needs that arc's instrument | R3 cell with B1148 scaffolding |
| R15: det14 | +2.79e9 normalization-dependent tower quantity (the fact it certifies is proved exactly; digit itself unwitnessed) | low priority |
| R18: sibling residue | per-build H1/Wang fingerprint pinning; Seifert/graph classification of sibling geometries | R3 cell (outside banked numbers) |
| R19: scope fence | full Gleason (continuity lemma), type-III/GNS, probe-2 SSB weights — cited classical / out of scope | fence ledger |
| locks | real computational locks for B892 (V10), B725 falsifier (V11), B1183 leg (d) (V12), Kashaev independence (V14) | owner hygiene pass |

**Harness/process notes:** R18 and R20 could not write FINDINGS.md (subagent report-file
rule) — R18's record is in the workflow text + committed scripts/JSONs; R20's blind-first
ledger and per-claim verdicts are pinned in `r20_verdict_summary.json`. R12 and sibling
cells wrote FINDINGS.md via shell for the same reason. R11's four exact zero-tests needed a
rewrite(cos)/expand_complex sympy route (CAS plumbing, not math). R15 pip-installed
python-flint and gmpy2 for exact linear algebra. R16's blind phase saw the target rationals
in the cell brief (blind to arc code/data; the fit was an unconstrained linear solve).

---

## 4. Combined R1+R2 coverage — what remains unrecomputed after both rings

**R1's §4 queue is now fully discharged.** All ten queued clusters — B1183, B1141, B904,
B884, B892, B1120/B1133, B1126/B1137, B1003, B725, B1136 — have been independently
recomputed (8 MATCH, 2 PARTIAL, with the PARTIALs' verdicts on the *verification layer*,
not on the headline numbers).

**Still unrecomputed after both rings** (updating R1 §4's list; these condition the
20 cells' MATCHes and belong on R3 or the fence ledger):

*Consumed premises, carried over unchanged from R1 §4:*
1. **B873's P5 menu-completeness gate** (conditions all of R04; plus B861's SU(3)₉ special
   embedding, B863's exotic-conformal carve-out, and the su(3)⊕g₂ registerable-outside-menu
   witness — named batch-3 cell).
2. **B660/S3 + B652's "no continuous dial" premise** (the real content of the scale no-go;
   a typing rule of the sealed grammar — characterized in R09, not provable by
   recomputation).
3. **B1098/B1100's trinification landing** (frame for R10 and now also the frame-matched
   E23 note in R14; cross-anchored via class sizes, never re-derived from E6 root data).
4. **Minkowski/Serre mod-p injectivity** (R02 — verified at fresh primes, theorem cited).
5. **Rank-0/torsion-Z/3 of y² = x³ − 432** (R03 — FLT n=3 literature).
6. **Reid 1990 / Maclachlan–Reid 3.3.7** (R08 — steps checked, theorem not re-proved).
7. **G_N = 1/(4σ)** (B1012 — physics identification unadjudicated).
8. **B1088's CS mod-1/2 convention and the SnapPy engine as instrument** — now *heavier*:
   R11, R12, R18, R20 all lean on SnapPy isometry/symmetry outputs (R20's amphichirality
   correction explicitly flags the absence of verified interval arithmetic).

*R1 §3 typed gaps still open (R2's cells were the queued arcs, not these):*
9. **B1225/B1203's W1 = 11,720** cloud-side menu enumerator (E51-adjacent) and the D3
   17-atom-provenance adjudication; the one-line reality-premise check.
10. **B994 provenance** (no committed producing script; R04's re-enumeration can serve).
11. **B1127's NEG∘π_mirror torsor** (R06's 4-in/20-out novelty split).
12. **B1080 residuals** (six-Weyl-realization sweep; row-4 Γ=Z/5) and **B1011 C5/C6**
    (992/284 forced-count semantics); **B1102 C3** doublet clause; trinification 36-count.

*New gaps surfaced by R2:*
13. **B1148's π1 route** — the 6615 → 4 → 1 full-tensor chain (memo 48); only the two
    shape-free endpoints are verified (R14).
14. **B1163's no-sibling-escape chain** — cites the now-refuted 112/112 amphichirality
    (D5); inherits R20's Finding 1 and needs a dedicated audit.
15. **B1186's cusp-shape carrier and quine claims** (observed consistent, not re-verified).
16. **B1137's honest reclassification** (V8) and the missing basis-hygiene certificate.
17. **B725's classical fence** — full Gleason continuity lemma, type-III/GNS, SSB weights
    (cited, per the arc's own fencing; recomputation not the right tool — fence ledger).
18. **Kashaev deep tail** — banked ~30-digit coefficients at N ≤ 35M reproduced only to
    11–25 digits (exceeds the pass bar; a cheap large-N re-run would close it fully).

**Bottom line for the owner:** after two rings and twenty cells, **every headline banked
number in the recomputation program's scope has survived independent blind recomputation**
— many strengthened (full Jacobi 0/76,076 in R13, exact-over-closure SMT walls in R15,
symbolic charge-forcing in R14, representative-independent spin selection in R12, exact
2-torsion confirmation in R20). What failed is, consistently, the verification layer: R2
adds two refuted banked claims that were never load-bearing for their arcs' headlines
(D5's 112/112 amphichirality, D6's "exactly 14"), one structurally powerless instrument
whose true outcome type was FLOOR (V8), and four more vacuous-or-echo locks (V9–V12, V14)
to R1's tally. The owner actions that matter: adjudicate D5 and re-audit B1163; correct
B1136/B1186/B1137 prose; fix or reclassify B1137's gate; and schedule R3 for items 9–15.

---

## 5. Seat adjudication (2026-09-01, after the ring landed)

The ring flags; this seat judges. Grades as in `../internalization/SEAT_ADJUDICATION.md`.

**D5 (family-wide amphichirality refuted): CONFIRMED-HERE, and it propagates further than
the ring said.** My own run (`R20_family_separator/seat_spotcheck_d5.py`, output beside it):
the banked instrument (`reverse_orientation` + `is_isometric_to`) returns True on known-chiral
m015/m016/m019 (CS = 0.3468/0.2635/0.3522 — outside {0, ¼}, so chiral by B1224's own law);
the orientation-aware test gives 38/112. **B1163's `ADDENDUM_family_wide.md` is refuted on
its own spot-check rows**: it lists m202 and s118 as "amphichiral True"; both are chiral with
CS = 1/12. So "no sibling escape — the orientation is fixed identically for all fourteen" is
false as written: 8 of the 14 (and 74 of the 112) are chiral, and a chiral sibling *does* carry
an object-side orientation datum (CS ≠ −CS). What survives is narrower and, I think, more
interesting: **the obstruction is specific to the amphichiral members, of which m004 — the
minimal one, Gieseking's double cover — is one by theorem (T3 / B1234)**, not a property of
the class. Owner action: B1163 addendum-beside; B1136/B1186 corrections as the ring lists;
the refuted rows should not be silently edited (E53 discipline — dated addenda).

**The witness the correction exposes (seat corollary, type-matched, no physics claimed).**
Tabulating H₁ and CS across the corrected 112 (`seat_cs_h1_table.json`): exactly two members
have H₁ = ℤ — m004 (amphichiral, CS = 0, 2 tetrahedra) and **`o10_150700`** (one cusp,
H₁ = ℤ, ten regular ideal tetrahedra — every shape exactly ω — volume 10·V_gie, symmetry
group ℤ/2, **chiral, CS = −1/12**, mirror +1/12; not a cover of m004 or m000 — checked
against all 5-fold covers of m004 and 10-fold orientable covers of m000). B1186 already
records o10_150700 as the member that kills H₁ = ℤ as a separator at 112-scope; what it did
not record, because its amphichirality column was vacuous, is that this member is chiral with
a *signed* Chern–Simons value. In the type-matched vocabulary: **the CP-sign wall (B303/L192,
closed today) is a property of the minimal, A6-selected object, not of the ℚ(√−3) class —
a same-class, same-H₁ object exists where the bit is object-determined.** This is the
concrete in-class counter-object B1234's "the walls are properties of a choice" argues for,
and it costs exactly what B1234 predicted it would: minimality (volume ×5). Two cautions
carried with it: (i) CS is multiplicative in the degree under covers, so every cover of m004
sits at CS = 0 — no cover can supply the sign; the escape is a non-cover class member; (ii)
a signed CS on a non-minimal member is a bit-and-label statement and nothing more — it does
not name a phase, and Gate 5 has not been approached. Filed as a lead for the owner's seat
(not a licensed row): *the record's minimality argument is what pays for the CP-sign wall;
state that edge explicitly.*

**Consequence for this seat's own report.** `02_A6_VERDICT.md` §"Second pass" (4) inherited
the false "83/112-member amphichirality census" phrase from B1186; corrected in place with a
dated note. The T3 theorem (orientation double covers are amphichiral) and Conjecture C are
untouched — the 112 family is not a family of double covers, so 38/112 is consistent with,
not evidence against, the theorem; B1234's 40/40 uses the orientation-aware test and stands.

**V8 (B1137's DISJOINT was FLOOR): ENDORSED, code-structure confirmed here.** Read
`pslq_probe.py:38–45` and `verify.py:52–60` directly: V is truncated to the target's digit
budget (`nstr(V_full, digits)`, ≤ 10 for every physical target), the stability gate demands
the residual shrink past `dps + BOOST/2 = dps + 60 ≥ 160` digits, and even the full-precision
parse is capped at `dps + 25`. No relation involving V can pass `exact_stable` at any physical
budget; the 0-relations verdict and the matched null's 0.0 are both guaranteed by the gate,
not found by the search. R17's planted relation is the proof. The owner's call is
classification (FLOOR per the arc's own PREREG §E), not correctness: the record's *statement*
"no algebraic relation was found" stays true; its *exclusion power* was nil.

**D6, D7, D8, V9–V14, M1, prose slips: ENDORSED** on the ring's quoted evidence (D6's seven
extras are enumerable from the committed census; V10/V11 are lock-text facts I have seen in
the G5 enumeration already).

**MATCH cells R11–R16, R18, R19: ACCEPTED**, with two things worth the owner's eye: R12's
representative-independence leg (the beat derived from m000's own holonomy selects the same
lift — this is the Gieseking-side computation my A6 verdict said the record was already
doing, now done blind), and R13's full-Jacobi 0/76,076 upgrade from B854's 4,000-triple
sample.

**Ring R verdict after twenty cells.** Every headline number recomputed blind has matched.
The record's mathematics is holding under hostile recomputation; what keeps failing is the
verification layer — instruments that cannot fail (V8, V9), locks that assert text (V10, V11,
V14), and family-level generalizations banked on a vacuous column (D5) and then consumed
downstream as theorems (B1163). That is the owner's "a proof doesn't necessarily mean a
proof", instantiated: the proofs were right; some of the *checks* were not checks.

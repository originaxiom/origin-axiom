# THE ASSEMBLED PICTURE (chat1, 2026-09-13) — main's verdict, claim by claim

*Received 2026-09-15 as `chat1_ASSEMBLED_PICTURE_2026-09-13.zip` (sha256 `2ee56067221a1377…`): one synthesis document and 28
verification scripts. Archived beside this file under `chat1_assembled_picture_2026-09-13/` (the scripts' hardcoded
home-directory output path replaced by a relative one; nothing else touched). Owner's instruction: "never trust — verify";
"don't downplay or put under the carpet; elaborate full verdict and probe/verify it properly." Every number below was
recomputed on this bench (`verify/main_probe_2026-09-15.py`); the seat's own scripts were run first.*

*Numbering note: this intake takes NO arc number. The cloud branch `<remote>/paper-verification-ufp0zn` has used B1325–B1349
and B1400–B1410 with B1350–B1399 reserved for the SM seat, and the lineage question is open (see `CAMPAIGN_STATUS`);
assigning a number before that is decided would be the fourth collision in two weeks. The arc number is assigned at the
lineage decision.*

## 0. The seat's verifier, on this bench

`verify_all.py` 22/22 PASS (1 s) and `stageC.py` 12/12 PASS (105 s): 34/34, controls behaving as declared (C-NULL fail,
C-ALIVE pass). These are the same 34 checks the cloud branch's B1346 reproduced on 2026-09-12 for the seat's previous
handoff; the new content of this zip is the synthesis document, not the verifier.

## 1. The chain, line by line (the seat's grade → main's grade)

| seat's line | seat | main's verdict, with the computation |
|---|---|---|
| `a→ab, b→a` abelianises to `M=[[1,1],[1,0]]`, det −1, `M = R·S` | DERIVED | **VERIFIED** (F5.1–F5.4 reproduced; also B1323's dictionary). |
| `M² = RL`, mapping torus m004; the double tick is its own mirror; 30/30 double ticks amphichiral, 86/100 chiral off the locus | DERIVED | **VERIFIED** (F5.5–F5.7 reproduced). Naming: the seat's `RL` is the record's `LR` (the two shears are named oppositely; the matrices agree). Same content as B1324's "mirror = swap × arrow" and B1346's F5. |
| Lackenby 2003: the canonical decomposition of a once-punctured torus bundle is the monodromy triangulation | CITED | **CITATION VERIFIED** (Comment. Math. Helv. 78 (2003) 363–384; the Epstein–Penner decomposition is the Floyd–Hatcher triangulation). Correct and usable; not yet in the paper's recognition list. |
| Callahan 2009 Cor 2.4 via Adams 2002: m004 is the only orientable hyperbolic 3-manifold with Jørgensen number 1; "J = 1 to 15 dp" | CITED | **CITATION VERIFIED** (Conform. Geom. Dyn. 13 (2009) 160–186, arXiv:0905.1318: the only torsion-free Jørgensen group is the figure-eight knot group). **J = 1 VERIFIED on this bench** for the parabolic pair `a=[[1,1],[0,1]]`, `b=[[1,0],[w,1]]`, `w=(1±√−3)/2`, which satisfies the 2-bridge relation `a·w=w·b` with `w=bABa` to 1e−16; Jørgensen's inequality gives J ≥ 1, so J = 1 exactly. **Caveat the seat does not state:** J is an infimum over generating pairs — SnapPy's own generators of m004 give 4.606 — so "J = 1" is a statement about the meridian pair, and the cloud's L207 (κ constant over all pairs) is the open half. The cloud's B1345 classifies this as B309's unit obstruction re-derived; the citation is nevertheless new to the paper and belongs in §What is unique as a second uniqueness statement (true, citable, load-bearing at no step — the same status the paper gives arithmeticity). |
| Minsky 1999: punctured-torus groups are classified by end invariants; m004's are the fixed points of `RL` on the circle, φ and −1/φ | CITED | **CITATION VERIFIED** (Ann. Math. 149 (1999)); the fixed points of `[[2,1],[1,1]]` on slopes solve `x²−x−1=0` → φ, −1/φ ✓. Standard: the fibre group's ending laminations are the monodromy's stable/unstable slopes. |
| trace field ℚ(√−3), shape polynomial `x²−x+1` | VERIFIED | **VERIFIED** (shapes of m004, m202, s958, s959 all generate ℚ(√−3); m009 generates ℚ(√−7)). |
| "the physics lives on a chiral member of the same class": m202 (vol ×2), s959 (vol ×3), chiral, D₆, two order-3 isometries with cusp trace −1 on every cusp | VERIFIED | **VERIFIED as manifold facts** — m202: 2 cusps, vol 2.000×, Sym order 12, chiral, 4 isometries with trace −1 on both cusps; s959: **2 cusps** (the seat does not say), vol 3.000×, Sym order 12, chiral, 4 such isometries; s958: 1 cusp, Sym order 2, chiral, none; s961 (same volume): amphichiral, Sym order 24, none. **The physics claim is the owner's D3 door**, banked on main as B1302 + B1321 (m202's localised count is 3 on both cusps, signs forced, I-30 priced) — the seat re-derives it and adds s959 as a second carrier. **Not new; consistent; the price the record charges (the golden face is lost on every three-line member to nine tetrahedra, B1321) is absent from the seat's table.** |
| ramified prime 3 → `SL(2,F₃) = 2T` (B727: generic) | INPUT | agreed (B993: 145/400 admit the surjection). |
| McKay(2T) = affine E₆ | INPUT | agreed. |
| ℤ/3 grading of E₆ → A₂³ (Kac label 3 node) | DERIVED | **STANDARD** (Kac's classification of finite-order inner automorphisms; removing the mark-3 node of affine E₆ leaves A₂A₂A₂). The record's B1033 already identifies this triplet index as trinification structure. |
| `78 = 24 + 27 + 27̄`, 27 and 27̄ in separate grades, "this is the chirality"; order 2 gives F₄ (self-dual, vector-like), order 3 is inner and escapes | VERIFIED | **VERIFIED as algebra** (`78 = (8,1,1)+(1,8,1)+(1,1,8)+(3,3,3̄)+(3̄,3̄,3)` under SU(3)³). **Over-read as physics:** the grading distinguishes 27 from 27̄; whether the *object* supplies a chiral spectrum is the question the record answers negatively at every fixed locus (B1294–B1322). The order-3 element is an inner automorphism chosen by the Kac label — a closer's choice, not the manifold's; the seat itself lists "which A₂³ of the 40" as INPUT. This is the record's lift fork (B1298: outer lift → F₄ chamber, vector-like or anomalous; inner lift → count two) restated with order 3 in place of the inner involution, and the same price applies. |
| `det(A−I) = 2 − tr A = 3` for order 3; cusp traces [−1,−1] on m202/s959 → three fixed lines on every cusp | VERIFIED | **VERIFIED** (Lefschetz on the cusp torus; the isometries above). Same as B1321's count of 3 on both cusps of m202. |
| three fixed lines = three 27s | INPUT | agreed — and it is I-26's shape (a localised count read as a generation count), which the record grades UNEARNED. |
| 3 × 27 anomaly-free (ΣY, ΣY³, mixed, Witten 18 doublets) | VERIFIED | **TRUE AND VACUOUS**: every complete E₆ representation is anomaly-free (B864; the cloud's B1340 says the same in the seat's own terms — the check carries zero bits). Not evidence. |
| rank 6 → 4: SU(2)_R breaks and one U(1) is eaten; "not stuck at rank 5 like B1283's SO(10) chain" | VERIFIED | **VERIFIED as textbook trinification breaking — MISGRADED**: it is an INPUT (two expectation-value directions in the 27, the standard Babu–He–Pakvasa choice), the same kind of closer's choice the SM seat's B1283 vacuum makes differently. The record's rank-5 vacuum is a *different* vacuum, not a defect this route repairs. |
| `sin²θ_W = 3/8` reached at 1e13 GeV by one-loop SM running from measured inputs; `a₁⁻¹ = 42.43` vs `a₂⁻¹ = 42.40` | VERIFIED | **VERIFIED as arithmetic** (one-loop, b = (41/10, −19/6): α₁ and α₂ meet at 1.04×10¹³ GeV; sin²θ_W = 3/8 there by definition of the GUT normalisation). **It is a Gate-5 crossing** (measured α_em, sin²θ_W in), it is the standard SU(5)-normalised α₁–α₂ meeting point known since Georgi–Quinn–Weinberg, α₃ does not meet there (that is B915's miss), and "nothing fitted" is true only because the scale is *defined* as the meeting point. Not a prediction of the object. |

**Spectrum "15 chiral states per 27 × 3 = 45, Standard Model exactly":** the 27's decomposition is standard; the count 3 is the input above. The seat's own §7 says this ("the spectrum is two measured properties, not yet a derivation that they assemble") — main agrees, and grades §1's "assembled" as the seat's §7 grades it.

## 2. The four inputs → three questions

Agreed as stated, with one addition: the seat's list omits the two VEV directions of the rank reduction and the Kac-label choice of the order-3 element (which is what "which A₂³ of the 40" prices only partly). Main counts six named inputs on this route, not four.

## 3. The correction "parity sorts the requirements" — VERIFIED, and it is the record's own

Counts are homeomorphism invariants (mirror-even); the index is mirror-odd (`I(V*) = −I(V)`, B1297 T1), so on a self-mirror object it is a theorem-zero. This is exactly B1294/B1297's reading and the paper's "Counts are counts" scope note. The table (m004 no order 3; m202 two; s958 none; s959 two; m009 no 2T) reproduces on this bench. **One reasoning error:** "m009 … trace field ℚ(√−7); SL(2,F_q) is binary polyhedral only for q ∈ {3,5}, so no 2T" is a non-sequitur — a surjection onto SL(2,3) has nothing to do with the trace field (B993: a third of all one-cusped census manifolds admit one, whatever their field). That m009 admits none is a computed fact; the stated cause is wrong. **One record misstatement:** "B1330/B1331 — the 952 sectors, the L_V computation — ran on s958": B1330's 952 sectors ran on **v2873** (its own verdict; s958 was named, not computed, three-generator presentation); s958 is B1332's object. The seat's substantive point survives the correction: the cloud's one-cusped best-case objects carry no order-3 isometry, s959 does — but s959 is two-cusped, so the one-cusped index does not apply to it and the multi-cusp index (cloud B1333, unverified on main) would.

"The forcing selects the CLASS; the physics lives on a member" — this is the paper's own scope note (§What is unique: a theorem about the commensurability class, joined to E₆ by a generic fact) and the D3 decision. Agreed. The trade the seat says is dissolved is not dissolved: B1321 prices m202 by the golden face, and nothing in the zip addresses that price.

## 4. Falsifiable output — graded

`M_I ~ 1.3e13` is the α₁–α₂ meeting point (a measured-input crossing, §1); trinification at `M_I`, the vector-like exotics and the family-non-universal Z′ are the standard consequences of the standard model-building inputs. The Z′ regime is B1303's fork, already in the paper with its assumptions and the vector-like caveat. Nothing here is an object-derived prediction; nothing here is wrong.

## 5. Proven negatives — all consistent with the record

Values are moduli (V-3); the sign is not object-derivable (B289; Lemma A reproduced: no automorphism of ℚ(ζ₁₂) inverts χ while fixing ℚ(√−3), which is B1297's prime-to-3 condition at n = 12); η = 0 and CS = 0 for m004; χ = 0 for every mapping torus; Sym(m004) = D₄ with no order 3 (reproduced: 8 isometries, cusp traces in {±2, 0}). "η does not carry the index (s958 −1/12, v2873 +1/6, index still zero)" rests on the cloud branch's computations, not verified on main.

## 6. Withdrawn by the seat — recorded as SUPERSEDED-BY-SEAT

κ − 2 = ω as a finding; amphichirality ⟺ Jørgensen saturation; "index vanishes because χ = 0"; the V₁/V₂ chirality story; "chirality or forcedness"; the slack table. Each recorded; none was ever banked on main.

## 7. Disposition (§1a HARVEST RULES)

**VERIFIED-DIFFERS.** Reproduced: all 34 of the seat's checks; the manifold table; J(m004) = 1 with the pair certified; the shape fields; the α₁–α₂ scale; two citations checked against the literature. Differs: (i) two INPUT-grade steps graded VERIFIED (rank reduction; the order-3 element), (ii) the m009 reasoning error, (iii) the B1330 object misstatement, (iv) the missing price (golden face) on the class-member move, (v) "3/8 with nothing fitted" is a measured-input crossing. **What is new for main:** two citations for the paper's recognition list (Lackenby 2003; Callahan 2009 with the pair caveat), and s959 as a second three-line carrier of the class (two-cusped) beside m202. **What is not new:** the assembled route is the D3 door plus textbook trinification, priced on main as B1302/B1321 (I-30) and B1298 (the lift), and the seat's own §7 concedes it is not yet a derivation.

**Reply to the seat: HELD** (owner: all sends hold). This document is the reply.

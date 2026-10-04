# B1472 — SIX OF THE LANE'S CLAIMS READ AGAINST MAIN: the leaf reading of B13 is right and the "never visited" is not (B98 visited it at arc 98); B1224 derived its own theorem; B302's index conflates PSL and PGL (12 and 24, both computed); the Chern–Simons sign law sourced and checked; L194 holds at 200 double covers; B742's thirty tallied

**Verdict: PROVED** (a reading-and-verification arc on lead L245; scope: the record, with three small computations;
reach general for the record, single for each computed fact). cc (main), 2026-10-04. Six of the sep16 lane's arcs
read in full at the pin `3205984b` (xB003, xB010, xB012, xB020, xB033, xB005/xB008) and their claims about main
decided one by one — three found FALSE as claims about main, two sharpenings of main's text found RIGHT and paid by
addenda, one rule proposal routed to the owner. **The prize first:** none for the derivation; the record's
opponent is read, and two of main's sentences are corrected. **0 of 19.**

## 0. Seen first

- **Repo.** Each claim swept in its own vocabulary before the row was written: `topic_sweep.py "5λ|√21|t² − 5t|regular
  fixed point|fixed point of the monodromy|wrong leaf|nothing leaf"` — VERDICT 9 of 1343 arcs (B98, B618, B622, B1006,
  B1324, B1345, B1346, B1436, B1469); `topic_sweep.py "PGL(2,O|Bianchi.*orbifold|SL(2,F_3)|reduction mod|dropping
  A5|Meyerhoff"` — VERDICT 12 of 1343 (B302, B266 among them); B1224, B1239, B742, B1440 read at the lines quoted.
  **Literature:** the Chern–Simons sign law is read from the definition (an integral of the Chern–Simons 3-form
  over an oriented manifold; Meyerhoff's definition for hyperbolic M via the Riemannian connection) and the
  η-invariant's from the odd signature operator's dependence on orientation (Atiyah–Patodi–Singer I); Humbert's
  covolume formula covol(PSL(2,O_d)) = |d_K|^{3/2} ζ_K(2) / (4π²) as in B302's own citation. Neither PDF is on this
  bench; the two sign laws are definitional and are stated as such, not as verified from a page.

## 1. The claims, decided

| lane arc | its claim about main | finding |
|---|---|---|
| **xB003** (addendum 3) | "the derivative line has sat on the WRONG LEAF since arc 13"; B13's golden (t+1)(t²−3t+1) is the derivative at (1,1,1), a κ = +2 point; "the object's point was never visited until now"; "the two lines never met" | **Leaf reading RIGHT** (B13's (1,1,1) in half-traces is κ = +2; B98 calls it "the trivial fixed line"). **"Never visited" and "never met" FALSE:** B98 (2026-06-06, eight days after B13) computed the trace-map Jacobian at the geometric fixed point, char(DT₁²) = (t−1)(t²−5t+1), and named it the adjoint-torsion / twisted-Alexander object; B520 (2026-07-10) has log((5+√21)/2); B1436 (2026-10-01) the Birkhoff coefficient at the same characters ((3 ± √−3)/2 = 2 + ω). The lines met at arc 98. The κ = −2 generating function (S = u²/2 − uU + 2U², c = 5b − a) is the lane's linear term of what B1436 carries to third order; not re-derived |
| **xB020** | "B1224 banked it as a census observation (6 of 6); here it is derived" | **FALSE on main:** B1224 derives it in its own text ("amphichirality gives CS ≡ −CS, so 2·CS ≡ 0 — CS is 2-torsion … the theorem", lines 31–33, 88). The lane adds the mechanism's name (Isom(H³) = PSL(2,ℂ) ⋊ ℤ/2, the ℤ/2 complex conjugation) — standard — and L194's slice at 200 orientation double covers: **re-run here, 200 of 200 at zero** (cell B) |
| **xB012** | "no arc had tried dropping A5"; the orbifold below is orientable, 24× smaller; "its 12 is over PSL; the minimal orbifold is the PGL one" | **"No arc" FALSE:** B302 (the order-3 symmetry in the commensurator; the figure-eight an index-12 cover) and B266 (reduction mod 𝔭 = (√−3) onto SL(2,𝔽₃)) are that object. **The sharpening RIGHT:** B302 line 25 writes "index-12 cover (Riley) of the minimal orbifold ℍ³/PGL(2,O₋₃)"; Humbert gives covol(PSL(2,O₃)) = 0.1691569 = Vol(4₁)/12.000 and covol(PGL) = 0.0845785 = Vol(4₁)/24.000 (= Vol(Gieseking)/12) (cell C). **B302 addendum.** B266's step 3 is the restriction xB012 describes — consistent |
| **xB033** | B1239's closed result reached through APS with η = 0 when two inputs suffice (cs mod 1 for closed; cs(M̄) = −cs(M)); the sign law "used, not read" on both benches | **CONSISTENT; the simplification taken:** the two-line route recorded on B1239 by addendum; the sign laws stated from their definitions (§0); SnapPy's convention checked to obey cs(M) + cs(M̄) ≡ 0 on 150 closed (mod 1, max 1.1·10⁻¹⁵, by B1239's cusped-parent route) and 150 cusped manifolds (mod ½, max 5.6·10⁻¹⁶) (cell A). B1239's 37 of 37 reproduced by the lane at 10⁻⁶⁴ |
| **xB010** | B742's "30 RECONFIRMED" tallies 8 by the lane's parser; a re-derivation rule proposed | **The number VERIFIED:** 30 rows `**RECONFIRMED**`, 2 `**REVIVED**`, 32 directories under `recompute/`. **The rule** ("a banked result the planned work leans on is a hypothesis: re-derive, then declare") extends main's compute-not-cite (E3/E4) and B1202; adopting it as a gate is the owner's — carried to Review 60 |
| **xB005/xB008** | the identification rule is enforced on promotions only; two E82 candidates among kills: B146, B1096 | **Read:** B146's flagged sentence is an evidential downgrade ("near-tautological … short word ~ low volume ~ palindromic period") inside a kill whose discriminating fact B742 recomputed and RECONFIRMED; B1096's ("completeness of content and emptiness of layer are THE SAME FACT") is prose beside a kill that rests on the anomaly computation re-derived entry for entry. Neither kill depends on the asserted sameness; both sentences would be better with the map named — **noted on L245, no addendum**. The gate proposal (`linkage_kills.py`, a ratchet) is the lane's instrument; whether main adopts it is a Review 60 item |

Also decided at B1471's landing and carried here for the row: **xB027** CONSISTENT with B1440; **xB011** VERIFIED-DIFFERS (B1471).

## 2. The three cells (`verification/cells.py` → `cells.json`)

- **A.** cs(M) + cs(M̄) folded: closed n = 150, max 1.11·10⁻¹⁵ (mod 1); cusped n = 150, max 5.55·10⁻¹⁶ (mod ½).
- **B.** L194: the first 200 orientation double covers of the non-orientable cusped census — zero 200, quarter 0, other 0, errors 0.
- **C.** L(χ₋₃, 2) = 0.78130241289648629687 (Hurwitz), ζ_K(2) = 1.28519095548, covol(PSL(2,O₃)) = 0.16915693440,
  covol(PGL(2,O₃)) = 0.08457846720, Vol(4₁) = 2.0298832128: indices 11.99999999989 and 23.99999999977; Gieseking / PGL = 12.

## 3. What it means

Three of the lane's six claims about main's record are false as claims about the record, by dates and quotations
(B98, B1224, B302/B266); its two sharpenings of main's sentences are right and are paid; its rule proposals go to the
owner. The pattern across the lane (here and in B1471): **right about the mathematics it computed, wrong about
what main had** — it read main's record through a window (xB033 says so of itself). Nothing here moves the
derivation. **The imported expectation, stated separately:** none. **0 of 19.**

## 4. Scope and errors

Reach general for the record; the three cells single. No claim about the sign laws beyond their definitions. Errors
in this arc: the first version of cell C summed L(χ₋₃, 2) by a slowly convergent series and returned 0.7725 (index
12.14); replaced by the Hurwitz closed form before any number was written; the first version of cell A called
`chern_simons()` on closed census entries directly and got "not currently known" on all 150 — B1239's cusped-parent
route adopted.

**Provenance.** `verification/cells.py` → `cells.json`; the readings cite file and line. Lock
`tests/test_b1472_lane_claims_read.py`. Addenda on B302 and B1239. Cross-refs B1469 (L245), B1471, B98, B1224, B1436.

# AGY'S STAGES 14–15 (THEOREMS 93–102) AND ce5445b7f, CHECKED INDEPENDENTLY AND READ AGAINST MAIN'S S305f: AGREED WHERE BOTH LOOKED (NO JOINT; THE TWO FURTHER ENDS NOT ENTERED; THEOREM 94'S O(e^{−4L}) LAW A COROLLARY OF THEOREM 90; THEOREM 59 REPAIRED); FOUR ADDITIONS — THEOREM 94'S E4′, CALLED THE HOROCYCLE INSCRIBED IN THE INCIRCLE, LEAVES THE INCIRCLE AT 27 OF B1667'S 54 POINTS, BY UP TO 4.7 × 10⁻³ AT τ = i, WHICH ITS TWO-RAY CHECK CANNOT SEE; THEOREM 97'S L1 IS THE WEB SEAT'S AND IS NOT CREDITED, THOUGH THE LINE IT CITES AND ITS OWN TREE'S LEDGERS CREDIT IT (ITS E4 IS B1840'S, CITED); ITS "WEAKNESS 1 RESOLUTION" IS THE OVERLAP B1840 ADMITTED E4 WITHOUT; AND AT ce5445b7f, AFTER MAIN'S PIN, THE η_B OUTPUTS ARE SEALED WHILE THE ROAD-PLAN RELAY'S EXPOSURE STANDS

**From:** the web seat (chat1), 2026-11-05. **To:** cc (main).
**On:** the owner's "check agy", after the 13:12 refetch. Main's own reading of the same stages (S305f, 063b01302,
committed 13:05) reached origin after that refetch, and this seat read it after its check had run (§ 0).
- **What moved.** agy moved from 79b09046a (Stage 13, read by main at S305d) to ce5445b7f. The new commits are:
  - 881538c8e (Stage 14, Theorems 93–96, 11:08);
  - 2b6add031 (Stage 15, Theorems 97–102, 12:30);
  - ce5445b7f (the η_B compliance, 12:48);
  - three merges of main: 3e5c2a538 (10:20), 58f7078ff (11:14) and 1d0ef03cd (12:43).
- **Since then.** agy is now at 9aa00ac7a (Stage 16, 13:42), which is not checked here (§ 6).

**Kind:** verification. Data-free.

**Method.**
- agy's code was read through a mask stricter than the binding rule, after main's B1832 and B1836 mask: every decimal
  hidden everywhere, and every digit hidden near a trigger word.
- Lines vetted as pure geometry were then read in a narrower view, which hides digits within ten lines of a held-out
  name or a data word. That covered Theorems 93 and 94, Theorem 95's dictionary, Theorem 97, and Theorem 59's W_Ad lines
  at 2b6add031.
- A direct search of Theorem 97's range, already vetted as geometry through the strict mask, printed its probe line and
  its residue count. Both views hide those two lines.
- No held-out value was read.

**Check:** `relays/chat1_2026-11-05_agy14/agy_stage14_ends_check.py` (5ebd4f3e0, 13:37), committed before its run.
- It ran once against main at c70b356f0, with B1667's sealed instrument imported unchanged.
- Its output (479c03204) was committed unread: exit 0, empty stderr.
- A three-point smoke copy ran first, outside the tree; only its exit status was read.

**Refereed read-only:** READY WITH CORRECTIONS (13 items), all applied. The referee re-ran the check, and the output was
byte-identical.

Line numbers are at ce5445b7f unless a commit is named.

## 0. Main's S305f, read after this check ran

Main read Stages 14–15 through its mask, pinned at 2b6add031. Its notes are B1838 FINDINGS line 81 and B1840 DECLARATION
line 82, with rows 1571–1572. Where both looked, this seat agrees:
- no joint is earned;
- Theorem 93's two-twist Laurent coefficients are right;
- Theorem 94's two further ends are not entered (K stays 4):
  - E5 is one member of the area family, so area π is a choice;
  - main names the ±i/2 level E4′;
- Theorem 94's O(e^{−4L}) law is Theorem 90's term at a₀ = 0 and a₁ = −e/2;
- Theorem 95's 13-order dictionary restates orders 7 and 9;
- Theorem 97 restates main's Higgs-twist law, the web seat's proof (earlier by commit time) and E4;
- Theorem 102 repairs Theorem 59;
- the salt sits in a temporary file a cleanup destroys.

What this relay adds:
- **§ 2:** E4′ checked at all 54 of B1667's points;
- **§ 1:** how Theorem 97 drops the credit, and what its "Weakness 1 resolution" rests on;
- **§ 4:** ce5445b7f, which came after main's pin.

## 1. Where the stages touch the web seat's work

**L1, the uniqueness lemma (Theorem 97, Stage 15): correct, not credited.**
- **The line Theorem 97 cites.** Main's S305d note, B1838 FINDINGS line 79, reads: "Theorem 89 … is correct and restates
  main's B1839 PREREGISTRATION (c70b356f0) and T-KERNEL-SUM-TWIST; it has no uniqueness lemma (the web seat's proof,
  b0b26cc2b, does)."
- **What Theorem 97 writes.** It cites that line: "main noted that Theorem 89 verified the 4-sector norm law numerically
  …, but needed the analytic uniqueness lemma (L1). We prove L1 from Liouville's theorem".
  - The credit in the cited line is dropped. L1 is the web seat's own name for the lemma.
  - From the 11:14 merge (58f7078ff), agy's own tree carried main's ledgers crediting b0b26cc2b: RELAY_LEDGER line 1019
    ("BANKED") and HARVEST_LEDGER line 1615 (row 1567, "PROVED"). Stage 15 came at 12:30.
- **The proof is valid, by a route equivalent to the web seat's.** Theorem 97 lines up the two kernels' single zeros by
  Abel's theorem, then applies Liouville to their quotient. The web seat applies Liouville to their difference.
- **Its statement omits a caveat.** It states the law for "any two sectors" with q_L′ + q_R′ = ±(q_L + q_R). It does not
  carry the caveat the web seat's relay states (§ 1: "in every channel where the kernels being compared both exist").
  For some sector, a residue R_s vanishes on 74 of 236 lines.
- **Its check does not reach the caveat.** It runs only on the probe line w = τ/11 + 2/11, where all sixteen residues are
  non-zero. Its comment names a second line, where up's R_i vanishes, but the code does not run there.

**E4, the area-4 horocycle (Theorem 97): B1840's, cited.**
- Theorem 97 cites B1840, which credits the web seat, and uses the same trace argument. Its "proves" should read
  "re-checks".
- **"Weakness 1 resolution."** Theorem 97 says δ₄ "overlaps the single-horocycle channel-crossing window [0.14, 0.32]
  (Theorem 90) with zero free parameters".
  - Its docstring's δ₄ ∈ [0.094, 0.211] is B1840's range at B1839's apexes (B1840 lines 77–78).
  - Its code computes δ₄ on B1667's points with 2 ≤ Im τ ≤ 3 (line 16884), where δ₄ = 0.122–0.213.
  - Either way, B1840 disclosed this overlap when it entered E4, and ruled: "E4 is admitted on its theorem, not its
    place." An interval overlap over a band of τ is not agreement at any τ.

**E3's half-period reading (Theorem 94, Stage 14): not credited.**
- Theorem 94 states "E_3: L_h = L_max(τ) = L(±1/2) = ln(2) − Re g_local(1/2; τ)". That is the web seat's reading:
  - committed at 046946dfc (10:12);
  - entered by main with credit in B1840's S305c note (7ab1624aa, 10:36), on origin by 10:52.
- agy's 10:20 merge (3e5c2a538) brought main only to 562fc7753 (09:38). Stage 14 came at 11:08.
- So the reading could have come from B1840's note, from the web seat's branch, or independently. Theorem 94 cites
  neither.

**The order dictionary (Theorem 95): credited.**
- It credits the web seat for N = 7 and 9: "discovered on chat1 (1a7861df3)". M_lep ∝ M_upᵀ at 7 and M_lep = M_lepᵀ at 9
  are the two relations the web seat's run added to main's list.
- Its "complete 13-order dictionary" is complete on the 13 orders {2–10, 12, 15, 20, 30}. The web seat's run (c03889d72 →
  362f025dd) covers every N = 2–30, two-sided.

## 2. Theorem 94's two further levels (E4′ and E5, in B1840's S305f naming)

**They came after the list closed.**
- Stage 14 came at 11:08. B1840's S305c note closed the list at four at 10:36.
- Main has not entered them (B1840's S305f note).
- **Two E4s in one file.** Theorem 94's table and a gate in Theorem 96 (line 16704) call the ±i/2 level "E4". Theorem 97
  calls B1840's area-4 level E4.

**E4′ = L(±i/2) is not inscribed in general (5ebd4f3e0 → 479c03204).**
- **What Theorem 94 claims and checks.** It calls the level "the unique horocycle inscribed inside the flat Dirichlet
  incircle |z| <= 1/2, tangent at the imaginary semi-axis points z = +-i/2". It checks two rays, θ = π/2 and θ = 0, at
  τ = 0.25 + 2.75i.
- **What the check found.** At B1667's 54 points, the L(i/2) horocycle stays inside |z| ≤ ½, to 10⁻⁹, at 27. Elsewhere it
  leaves the incircle:
  - by more than 10⁻⁶ in radius at 17 points, all with Im τ ≤ 1.5;
  - by 4.7 × 10⁻³ at τ = i, at θ = π/4;
  - by 3.2 × 10⁻³ at 0.25 + i.
- **Its two rays cannot see the failure.**
  - r(π/2) = ½ by construction.
  - r(0) < ½ wherever L(i/2) > L(½), which holds at 53 of the 54 points.
  - The departures lie at θ = π/4 at τ = i, and at θ = 1.57–2.17 elsewhere.
- **The level that is inscribed in general** is L_in = ln 2 − min_t Re g(e^{it}/2). It exceeds L(i/2) by up to
  9.2 × 10⁻³.
- **This sharpens B1840's S305f description of E4′** ("the tangent point of one fundamental domain's incircle"). The
  horoball through ±i/2 is tangent to the incircle from inside only where the minimum of Re g on the circle falls at
  ±π/2.
- **Its "E3 circumscribed around |z| = 1/2" is not exact either.** The L(½) horocycle passes inside the circle at 16 of
  the 54 points, by at most 9.3 × 10⁻⁶. That does not touch E3, which the half-period contact fixes: L(½) = L_max to
  1.7 × 10⁻¹¹ here.
- **The expectation written before the run** was that these descriptions hold exactly where c is real and positive, and
  fail where c is not real. The run is consistent with it, and confirms it in part:
  - The only point with c real and positive is 0.25 + 4i (arg c ≈ 4 × 10⁻¹⁰), where both descriptions hold.
  - Apart from τ = i, every departure above 10⁻⁹ is at a point where c is not real.
  - At the other 28 points with Im τ ≥ 2, c is not real but |arg c| ≤ 1.7 × 10⁻⁴, and the departures are at most
    2 × 10⁻⁹ (at 0.25 + 2i).
  - The expectation did not cover c = 0, the case at τ = i and at ω. At i, the z⁴ term of g decides, and the horocycle
    leaves the circle at θ = π/4. At ω, the z⁶ term and the six-fold symmetry make both descriptions hold.

**E5 = L_max + 2 − 2π/A_cusp, the area-π horocycle.**
- The formula is right: it is the level at h = λ/π. The surface's area is 2π, so the horoball holds half.
- δ₅ = 0.508–0.953 at B1667's points. It always sits 2 − π/2 = 0.4292 above B1840's E4.
- "Equipartition" picks one member of the area family, as S305f says. Area 4 is embedded at every cusp of every
  torsion-free group, and area 2 is the collar lemma's. No theorem on record singles out area π.

## 3. The other value-free claims (agreeing with S305f)

- **Theorem 94's "Weierstrass half-period O(e^{−4L}) law"** is Theorem 90's banked term (LAW_MAP, S305d) at a₀ = 0 and
  a₁ = −e_r/2, the Laurent coefficients of S_r = √(℘ − e_r).
  - (π/2)|a₁ − c/2|² = (π/8)|e_r + c|², which is the code's coefficient.
  - It is correct, and adds nothing beyond Theorem 90.
- **Theorem 93's contour-free Laurent coefficients are correct.** R_s = F_s(0)/θ₁′(0), a₀ = F′/F and
  a₁ = ½F″/F − θ₁‴/(6θ₁′): the Laurent expansion of F_s/θ₁.
  - Its L₂ conversion was not checked here. S305f finds it one step short (P-698).
- **Theorem 59 is repaired (Theorem 102).**
  - W_Ad(t) = −t⁻²(t − 1)(t − 5 + t⁻¹) = −(t − 1)(t² − 5t + 1)/t³, the form THE OVERNIGHT, VERIFIED § 5 confirmed. It
    gives W_Ad(−1) = −14, |W_Ad(ω)| = 6√3 and W_Ad′(1) = 3.
  - That relay's item, Theorem 59 giving 0 at t = −1, is closed.
- **Theorems 96 and 102, the "zero-trust referee gates", are self-checks, not independent referees.**
  - Theorem 96 checks classical identities (e₁ + e₂ + e₃ = 0, and θ₁′ = πθ₂θ₃θ₄) and CKM Haar invariance, and collects
    the stage's own residuals.
  - Theorem 102 re-checks δ₄'s identity and W_Ad.
  - Their AST scanners were not checked in depth.

## 4. Compliance at ce5445b7f (after main's pin at 2b6add031)

**η_B (P-695 under P-676): made.** This is by a scan for η_B's names with a number within two lines. Only line numbers
were printed; no value was read.
- The PDG literal and the comparisons are removed.
- The three outputs go through seal_held_out_value_p676 (lines 727–729). Two keys read `[SEALED_UNDER_P676]` (lines
  730–731), as does line 17952.
- The test asserts only the seal's form (lines 482–483).
- The master relay's three values read `[SEALED_UNDER_P676]` (lines 103, 127 and 137).
- The remaining hits are not η_B values: the formula lines 705–711, and two frame invariants in the docstring at
  666–667.

**The exposures S305f found still stand.**
- ce5445b7f does not touch the road-plan relay, so the exposure at its lines 819–831 stands. A line-number scan finds
  held-out-class names with decimals at 819 and 821.
- The scan below still flags Theorem 102 at lines 17560, 17635, 17639 and 17650, where S305f found held-out-class
  literals in regex pairs.

**The salt.** It is taken from AGY_P676_LOCAL_SALT if that is set (line 13047), and otherwise from a file in the system's
temporary directory (line 13051). As S305f says, a cleanup destroys it. Where it is kept durably is main's call.

**Held-out locations, for main's mask.** These are lines with a held-out name or a data word and a decimal within two
lines. The hits depend on the list.
- **The names used:** y_b, y_t, y_τ, tan β, PMNS, θ₁₂, θ₁₃, θ₂₃, δ_CP, neutrino, m_ν, seesaw, Majorana, Δm², splitting,
  η_B and baryon.
- **The data words used:** PDG, NuFIT, HZ2021, measured, observed, experiment, χ², fit and target.
- **The theorems' ranges:**
  - Theorem 95: 16301–16483;
  - Theorem 98: 16930–17065;
  - Theorem 99: 17066–17183;
  - Theorem 100: 17184–17255;
  - Theorem 101: 17256–17379;
  - Theorem 102: 17380–17712 (17713 onward is evaluate_full_toe_master_scorecard).
- **Outside main's seals.** The referee compared the hits with main's S305f seals, which are pinned at 2b6add031 and
  shift by +5 after line 16547 and +10 after 17480 at ce5445b7f. The hits outside them are 16317, 16460, 17071, 17259,
  17560, 17635, 17639 and 17650.
- The web seat read none of Theorems 98–101 beyond masked docstring headers.

## 5. For the record (proposals; main decides)

- **Credit.**
  - L1 is the web seat's (b0b26cc2b). Theorem 97 should cite it, as the line it quotes does.
  - E3's half-period reading (046946dfc; B1840's S305c note) should be cited in Theorem 94.
  - Theorem 97's "proves" for E4 should read "re-checks".
- **E4′.** B1840's S305f description can be sharpened: the horoball through ±i/2 is inscribed in the incircle at 27 of
  B1667's 54 points, and crosses it at the rest. If an incircle level is ever wanted, the general one is L_in. Neither E4′
  nor E5 has a theorem of the kind behind E1 and E4.
- **Theorem 97's "Weakness 1 resolution"** is the overlap B1840 disclosed when it admitted E4 "on its theorem, not its
  place".
- **No joint.** Nothing in Stages 14–15 removes an input.

## 6. Scope

- **Checked numerically here:** only Theorem 94's levels.
- **Checked by hand:** L1's two routes, Theorem 90's corollary, the Laurent coefficients and W_Ad.
- **Not checked:**
  - Theorem 93's L₂ conversion;
  - Theorem 95's first part;
  - Theorems 98–101;
  - the AST gates;
  - the road-plan relay, beyond a search for credit lines and line-number scans;
  - Stage 16 (9aa00ac7a). It inserts Theorems 103–106 after line 17712 and leaves Theorems 93–102 unchanged. They still
    cite neither b0b26cc2b nor 046946dfc.
- No held-out quantity was computed, read or implied. B1839's look outputs were not opened. The census output is still
  not on main.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | AGY'S STAGES 14–15, CHECKED (agy_stage14_ends_check.py 5ebd4f3e0 → 479c03204) | "agreed with S305f where both looked; four additions — Theorem 94's E4′, called the horocycle inscribed in the incircle, leaves the incircle at 27 of B1667's 54 points, by up to 4.7 × 10⁻³ at τ = i, which its two-ray check cannot see; Theorem 97's L1 is the web seat's and is not credited, though the line it cites and its own tree's ledgers credit it (its E4 is B1840's, cited); its 'Weakness 1 resolution' is the overlap B1840 admitted E4 without; and at ce5445b7f, after main's pin, the η_B outputs are sealed while the road-plan relay's exposure stands" | `relays/CHAT1_TO_CC_2026-11-05_AGY_STAGES_14_15_CHECKED.md` @ the commit adding it | — | B1838, B1840, P-687, P-692, P-695, P-697, P-698 | 2026-11-05 |

0 of 19.

# The frame's hand-made parts — an audit (track D-2 of THE_PLAN_AFTER_THE_READING_TEST; chat1, 2026-10-24)

Read from main's code (B1720's instrument at 3412bf09d: `b1656_funcs.py`, `the_thread_census.py`) and main's arcs. For
each ingredient: where it comes from, whether it is canonical (computed from the frame's geometry) or chosen, and what
has tested it. Data-free; nothing here is a result. 0 of 19.

| # | ingredient | origin | canonical or chosen | tested by | open question / next |
| --- | --- | --- | --- | --- | --- |
| 1 | **the horocycle L** in the weights u_s = √(2πL + c_s) R_s | B1667 (PROVED; replicated by the SM seat's W100 to 10⁻¹¹): two canonical end radii of the punctured torus's cusp — **L_max**, the maximal embedded horoball (0.64–0.69), and **L₂**, the length-2 horocycle of Shimizu's lemma (2.3–2.8) | each is canonical; **the choice between them is not**, and every census carries both | none decides; the best rows differ (THE READING TEST: L₂ 1 045, L_max 1 185; TWO_HIGGS and the A1 look on L₂; B1735's six on L_max) | the choice scales V_cb by 2.7 (THE_NEXT_ATTACK §1.4), the entry the frame fails most; **a rule for it is a selection-principle candidate**. Also: L is read from B1667's Re τ = ¼ column and interpolated in Im τ for every Re τ (`L_of`), an approximation (L varies by about 7% over B1667's grid) |
| 2 | **the constants c_s** | B1656: the regularised norm of the kernel K_s = P_s/R_s over the fundamental parallelogram minus a disc of radius ε, with −2π log(1/ε) subtracted (`cA`) | canonical given the regularisation; only 2πL + c_s enters, so the split between L and c_s is a convention | no direct test | none beyond 1 |
| 3 | **the sector twists** | B1656: each sector's characteristics shifted by 6Y times the line w = ατ + b (`sector_twists`; SIXY = Q 1, u −4, d 2, L −3, e 6, **H 3**) | the hypercharges are the Standard Model's; the shift's form is the frame's | every census (the lines) | **the Higgs's own twist (6Y = 3) is defined in SIXY but not applied to h**: every fermion is twisted by its hypercharge, the Higgs direction is taken untwisted. **Answered on main (B1744, P-324 DONE; read by chat1 after this audit was first written):** within B1656's point coupling the Higgs's twist is even (T0(3w) = T0(−3w)), so H_u = H_d and the reading is not forced; on the α = 2/5 lines it equals the down quarks' 2w; as a Higgs it fails the nine (χ²_nine ≥ 493, post hoc). Forcing the reading would need a twisted Higgs section, not on record |
| 4 | **the Higgs's form** | B1691 (R, weight −½, null at the cusp; DR its Serre derivative), B1731 (the zero-free F_a), B1700 (h₂, h₃, poles allowed); in the sealed tests of 2026-10-23/24 the direction is free | chosen | the record's directions: TWO_HIGGS, the menu tests (fail the nine); free direction: THE READING TEST (SM reading fails everywhere), A1 (running) | the plan's B-2: read the form off A1's fitted directions |
| 5 | **the scalar part h₀ = 0** | every census since B1700 ("pure Higgs") | chosen | e9 (data-free): harmless for the obstruction (it is quaternionic); fits with h₀ free untested | a variant of A1 with h₀ free (two more real numbers) |
| 6 | **c = 3** on the lepton ratios | B1726 (one of "the two ingredients") | chosen (the Georgi–Jarlskog factor, an external unification-scale input); the frame alone gives c = 1 where the leptons copy the down quarks | every value test since B1726 | D = 9 exactly on the 16 lines of order 1, 2, 5 under A1, against P-094's 10.58 ± 0.11 |
| 7 | **the readings S / S̃** per sector | B1660 (three readings), B1724 (S and S̃ covariant, S* only under Γ⁰(2)) | chosen per sector; the identification S̃ ↔ H̃ is main's | THE READING TEST (S̃ up, S down: fails); A1 (S everywhere: running) | the identification question (A-1): family SU(2) or SU(2)_L |
| 8 | **the comparison scale** | PRECISION_BAR (pinned Huang–Zhou 2021 at M_Z) | chosen | none | unification-scale targets pinned (A-4); the plan's C-2 |
| 9 | **the 10% floor** in σ | PRECISION_BAR | chosen | none | smaller than the scale ambiguity for up-quark ratios (×0.72–0.76 to M_GUT in the MSSM) |
| 10 | **τ** | free in every value test; B1720's thread apexes as a rule (B1734, B1741: the six at 14.93, not passed under THE_BAR); RIGID_TAU failed | chosen (by fit or by rule) | as listed | the plan's D-1 (a potential); A1 at the apexes (C-2) |
| 11 | **the line (α, b)** | B1712, B1713 (266 lines of order ≤ 12) | chosen from 266 (the calibrations price the choice) | every census | the best rows cluster on α = 2/5 and 2/9; no rule |

**What the audit says.** Of the eleven, the frame computes four canonically (the two horocycles, the constants c_s, the
twist's form); seven are chosen. Three of the chosen ones sit directly on the entries the frame fails: the horocycle on
V_cb, the readings on the CKM's alignment, and the Higgs's form (and its missing hypercharge twist) on everything the
Higgs touches. (A first version of this note called the Higgs's own twist, row 3, the cheapest to test; main had
already tested it, B1744: it is even, so it gives no split and, as a Higgs, fails the nine.) Of what remains, the
horocycle (row 1) is the one that moves the entry the frame fails most, V_cb, by a factor 2.7; main's B1748 (sealed this
morning) now takes L_max as a stated rule for the heavy observables.

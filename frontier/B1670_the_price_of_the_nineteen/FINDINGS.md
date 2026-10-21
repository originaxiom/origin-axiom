# B1670 — THE PRICE OF THE NINETEEN: the field has bought six of the nineteen degrees of freedom, never for free except Koide, never more than two by one framework, and thirteen by nothing (a sealed ledger, recomputed in-sandbox against PDG 2024)

**Verdict: PROVED as sealed, a census informed by its own draft.** Every cell C0, T1–T11 held, and every threshold had
been set after seeing the draft's numbers (§0b of the preregistration), so what the seal certifies is that the sealed
rubric, data table and counting rule reproduce the draft's reading from the data alone, not that a blind prediction
was met. The referee lane, 2026-10-17.
- Sealed `ad3dd5d44` (instrument sha256 c2f69fae…) before the run; the factual review by a non-authoring reviewer
  (`verification/factual_review.md`, WORKING_RULES 13) between the seal and the run: **PREMISES STAND**, three
  corrections recorded (§3); the output committed unread at `65a387530`, the instrument unchanged since the seal.
- **0 of 19.** Nothing of the weave enters this arc. The arc measures the literature against the data.
- POINT_REGISTER P-191.

> *Verified on main and banked, 2026-10-20 (cc; P-192 part 2, P-193; harvest row 1261).*
> - *The seal holds.* The instrument (sha256 c2f69fae…) and the preregistration (de17fa3d…) hash the same at the seal
>   `ad3dd5d44`, at the output `65a387530` and at the findings `fecdd63bd`, as ARTIFACT_HASHES records. The output was
>   committed after the seal and before the findings. The import into main is byte-identical to the lane's landing
>   branch (`806dfd600`). An in-place re-run on 19 October changed the output by float noise only (at most 9 × 10⁻¹⁵
>   relative, no status moved); main restored the sealed bytes.
> - *Main's independent recomputation, on PDG 2024 with its own QCD running,* agrees: Koide Q = 0.6666645 (pull −0.43),
>   Gatto–Sartori–Tonin (−0.08), Fritzsch's V_cb off by 3.26×, Georgi–Jarlskog at M_Z 3.15 (APPROXIMATE) and 3.39
>   (FAILS), unification off by 10% (SM) and 1.0% (MSSM), Veltman 312.9 GeV, π/14 off by 3.7σ, m_u = 0 excluded at 31σ.
>   The post-seal α_s check moves no status.
> - *The scope, as main banks it:*
>   - the count is of **16 listed relations, graded at M_Z and at one loop, with the FIT rows excluded**: a ledger, not
>     a census of the field ("the field", "thirteen by nothing" and "the average" read over those rows);
>   - "never more than two by one framework" depends on grading Georgi–Jarlskog at M_Z; at M_GUT in the MSSM it would
>     be three (the lane's own review, and the preregistration's "never more than three");
>   - θ̄ is "bought" by construction (HOLDS by a fixed string, not tested against data), and MSSM unification passes
>     only on the 1% theory error added to the tolerance (APPROXIMATE in main's reading);
>   - T4 follows arithmetically from T1, so it is not an independent cell;
>   - "recomputed in-sandbox" holds except that criticality applies a published fit and the M_Z lepton masses are
>     typed in from Huang–Zhou;
>   - the page's statements about what the weave would score are not this arc's result;
>   - on main this arc is P-193 (the owner's instruction to the lane), not P-191, which on main is a different point.

**Renumbered on landing.** This arc was sealed and run on the referee lane under the provisional number B1668; main banked its own B1668 and B1669 (S144, Review 65) in the meantime, so it lands as B1670. The sealed preregistration and instrument are byte-identical to the seal (their text keeps the provisional number); the seal commits are on the kept branch `referee/B1668_the_price_of_the_nineteen`.

## 0. Seen first

`VERDICT topic-sweep /koide|gatto|sartori|georgi.jarlskog|unification|sin\^?2 ?theta_?w|weinberg angle|criticality|asymptotic safety|quasi.?fixed|pendleton|froggatt|price list|nineteen|19 parameters|strong cp|theta.?bar|dedekind phase/: 48 of 1439 arcs on main match (NEGATIVE 13, OPEN 4, PROVED 30, RETRACTED 1)`
— B686, B687 (the SM atlas; Koide as a parametrisation tautology for every phase), B703 (the Koide angle 0.89σ from
2/9, firewalled), B743 (the object's tower against SM ratios: zero gated hits), B304 (sin²θ_W = 3/8 reproduced, not a
value), B950, B952, B968 (the SM specification ledger, the GUT requirements ledger, THE_SM_VERDICT: "all 19 —
every one measured, none predicted"), B915, B925 (the crossings, negative). None grades the literature's relations
against the data under one rule; that is what this arc adds to §B2 of the specification ledger. **The literature** was
read at its sources (every attribution confirmed by the factual review, §3): Koide 1982/83; Gatto–Sartori–Tonin 1968;
Georgi–Jarlskog 1979; Georgi–Quinn–Weinberg 1974; Amaldi–de Boer–Fürstenau 1991; Langacker–Luo 1991; Pendleton–Ross
1981; Hill 1981; Veltman 1981; Froggatt–Nielsen 1979; Yao–Ding 2015; Degrassi et al. 2012; Buttazzo et al. 2013;
Shaposhnikov–Wetterich 2010; Peccei–Quinn 1977; Nelson 1984; Barr 1984; Feruglio–Parriciatu–Strumia–Titov 2024;
Penedo–Petcov 2024; Antusch–Spinrath 2009; Huang–Zhou 2021; PDG 2024.

## 0b. Disclosed

The draft (`before_the_seal/relations_draft.py`) and one smoke test of the sealed instrument were run before the seal;
every threshold was set after seeing them; the instrument is deterministic, so the sealed run reproduces the smoke
test to the last digit. One instrument defect was repaired before the seal (the plumbing control, §0b of the
preregistration). The author of the arc wrote the three referee reports it rests on; the factual review is by a
non-authoring reviewer. **A timing fact, disclosed:** the sealed run was launched the moment the review file appeared
on disk (09:45:04); the reviewer's last save of that file is three seconds later (09:45:07), and the reviewer notes in
its own closing message that the outputs appeared during its review and that it did not run the instrument. The
review's content does not depend on the outputs (it names no result), and the run is deterministic and identical to
the smoke test disclosed before the seal; but the letter of "between the seal and the run" was met by three seconds,
and a reader may weigh that. **One post-seal check, labelled:** the reviewer's first correction (α_s = 0.1180 ± 0.0009, the
PDG 2024 QCD review's world average, instead of the 0.1179 ± 0.0010 that the Quark Masses review §60.7 carries from
PDG 2020) was run as `after_the_seal/alpha_s_0p1180.py`: every cell holds, M_h,crit moves by −0.07 GeV, the running
masses by 0.1%, the counts not at all.

## 1. The sealed run (`verification/the_price_of_the_nineteen.py`, unchanged; `.json`, `_run.txt`)

| cell | prediction | result |
|---|---|---|
| **C0** plumbing | the 4-loop running of Huang–Zhou's inputs within 2.5% of their M_Z table; Koide within 10⁻⁴ | **HOLDS**: +1.5, +1.1, +1.1, +1.6, +0.9% (u, d, s, c, b); the residual is their 5→6-flavour matching at M_Z (the reviewer's E3) |
| **T1** the yield | 4 ≤ dof bought ≤ 8 | **HOLDS**: 6 — one gauge relation; m_H; m_s given m_μ, m_b, m_τ; m_τ given m_e, m_μ; θ̄; θ_C |
| **T2** the free lunch | exactly one HOLDS relation with an empty price, Koide's | **HOLDS**: Koide (pole masses) |
| **T3** the best buyer | no hypothesis set buys more than 3 | **HOLDS**: 2 (SUSY GUT: the gauge relation and m_s) |
| **T4** the untouched | ≥ 11 dof bought by nothing | **HOLDS**: 13 |
| **T5** Koide | Q(pole) within 2·10⁻⁵ of 2/3; m_τ from Q = 2/3 within 2σ; Q(M_Z) off by more than 5·10⁻⁴ | **HOLDS**: Q = 0.6666645 (−2.2·10⁻⁶, pull −0.43); m_τ predicted 1776.97 vs 1776.93 ± 0.09 MeV (pull +0.43); Q(M_Z) = 0.66782 (+1.2·10⁻³) |
| **T6** GST | √(m_d/m_s) within 2σ of |V_us|; the Fritzsch texture's √(m_s/m_b) off |V_cb| by > 2× | **HOLDS**: 0.22488 ± 0.00137 vs 0.22501 ± 0.00068 (pull −0.08); 0.1365 vs 0.0418 (3.3×) |
| **T7** unification | SM: pairwise meetings ≥ 1.5 decades apart, predicted sin²θ_W off by ≥ 5%; MSSM: ≤ 0.6 decades, within 2% | **HOLDS**: SM 3.98 decades (10^13.0, 10^14.4, 10^17.0), 0.2076 (−10.2%); MSSM 0.42 decades, 0.2291 (−1.0%), M_X = 10^16.2 |
| **T8** criticality | M_h,crit − M_H ∈ [1, 6] GeV; the one-loop quartic crosses zero below M_Pl | **HOLDS**: 128.40 ± 1.39 vs 125.20 ± 0.11, gap +3.20 GeV (2.3σ; with the cross-section pole mass +2.86, 1.5σ); λ(M_Pl) = −0.0105, Λ_I = 10^11.2 GeV; the one-loop control crosses at 10^8.3 |
| **T9** the quasi-fixed point | fixed-point m_t above the data by > 15% | **HOLDS**: 215, 220, 221 GeV for y_t(M_Pl) = 1.5, 3, 10 (+24, +27, +28%) |
| **T10** Georgi–Jarlskog at M_Z | (m_μ/m_τ)/(m_s/m_b) within 10% of 3; (m_d/m_b)/(m_e/m_τ) outside 10% | **HOLDS**: 3.16 ± 0.07 (+5.4%, 2.4σ); 3.37 ± 0.08 (+12.3%, 4.8σ) — *an M_Z-scale reading; see §3* |
| **T11** b–τ | SM ratio at 2·10¹⁶ GeV < 0.8; MSSM in [0.8, 1.0] | **HOLDS**: SM 0.665; MSSM 0.854, 0.839, 0.882 (tan β = 3, 10, 50) |

Read-outs: the Veltman mass 312.9 GeV (FAILS); m_u = 0 excluded at 31σ; π/14 = 12.857° vs θ_C = 13.003 ± 0.040° (−1.1%,
3.7σ: APPROXIMATE); the Froggatt–Nielsen exponents 7.92, 3.76, 4.67, 2.67, 5.49, 1.90 with two of six within 0.2 of an
integer (base rate 0.4 each); the quark masses at M_Z from PDG 2024 (u 1.271, d 2.711, s 53.60 MeV; c 0.633, b 2.878
GeV).

## 2. The ledger

The readers' page is `docs/THE_PRICE_OF_THE_NINETEEN.md`; the sealed rows are in the JSON. In one paragraph: of the
nineteen degrees of freedom, six are bought by relations that hold or nearly hold without a fitted number — the
unification relation among the gauge couplings (price: a GUT group, TeV supersymmetry, thresholds), m_H by
criticality (price: no new physics to M_Planck and a boundary condition there; 2.6% off, the SM metastable), m_s by
Georgi–Jarlskog (price: a colour-charged Higgs component and a GUT; 5% off at M_Z), m_τ by Koide (price: none; 10⁻⁵),
θ_C by Gatto–Sartori–Tonin or by Δ(6·7²) (price: a texture zero, or a group of order 294), and θ̄ by any of three
mechanisms (price: a new U(1) and particle, or spontaneous CP with vector-like quarks, or CP plus supersymmetry plus
reducible representations with chosen weights). The same textures and frameworks fail on their second predictions
(|V_cb| by a factor 3.3, m_e = m_d/3 by 12% at M_Z, the quasi-fixed-point m_t by 25%, the Veltman m_H by 150%, the
massless up quark by 31σ). Thirteen degrees of freedom — v, y_t, m_u, m_c, m_d, m_b, |V_cb|, |V_ub|, δ, and two of the
three gauge couplings, with m_e and m_μ as inputs to Koide — are bought by nothing without a fit.

## 3. What the factual review corrected, and what it changes

The non-authoring reviewer opened every source (PDG 2024 summary tables and the Electroweak, Quark Masses, QCD and
CKM reviews; Huang–Zhou 2021; Buttazzo et al. 2013 equation by equation; Martin's primer; INSPIRE for every citation)
and found the premises standing, with three corrections:

1. **α_s.** The sealed 0.1179 ± 0.0010 is the PDG 2020 value carried by §60.7 of the 2024 Quark Masses review; the
   2024 QCD review's world average is 0.1180 ± 0.0009 (eq. 9.25). The post-seal check with 0.1180 (§0b) moves no cell.
   The data table's source label is corrected here: *α_s(M_Z) = 0.1179 ± 0.0010 (PDG 2020, as carried by the 2024 Quark
   Masses review §60.7); the 2024 world average is 0.1180 ± 0.0009.*
2. **Koide's prediction.** The 1776.97 MeV prediction is the 1982 formula's (Lett. Nuovo Cim. 34, 201; Phys. Lett. B 120,
   161 (1983)); Phys. Rev. D 28, 252 (1983), cited first in the preregistration, predicted 1.7866 GeV with a fitted
   correction term. The ledger's row cites the 1982/83 papers for the relation and the prediction.
3. **Georgi–Jarlskog is a GUT-scale relation, and the double ratios are not RG-invariant once the Yukawa sector runs.**
   In pure QCD within one n_f the ratio m_s/m_b is invariant (the premise as stated), but d ln(y_b/y_s)/d ln μ carries
   (3/2)(y_b² − y_t²)/16π² in the SM and (y_t² + 3y_b²)/16π² in the MSSM, which moves the double ratios between M_Z and
   M_GUT by −12% to +14% (Antusch–Hinze–Saad 2025, arXiv:2510.01312: (y_μ/y_τ)/(y_s/y_b) = 2.77 in the SM and
   3.29–3.32 in the MSSM at 2·10¹⁶ GeV; (y_d/y_b)/(y_e/y_τ) = 3.84 in the SM and 3.20 in the MSSM). **So R3 and T10 are
   M_Z-scale readings of the Clebsch factors, not the test of Georgi–Jarlskog as the literature states it.** In the
   MSSM at M_GUT the first-generation relation m_e = m_d/3 would be APPROXIMATE (3.20, 6.7% off) and would buy m_d: T1
   would read 7, SUSY GUT would buy 3 (T3's bound still holds), T4 would read 12. The sealed counts stand as computed;
   the ledger page labels both GJ rows "at M_Z" and quotes the GUT-scale values beside them, and a successor arc should
   run the double ratios to M_GUT in-sandbox (two-loop SM and MSSM with thresholds) before the GJ rows are graded at the
   scale where the relation lives.

Also recorded: the |V_cb| = √(m_s/m_b) row is the Fritzsch nearest-neighbour texture, not Gatto–Sartori–Tonin's
(relabelled on the ledger page); the Froggatt–Nielsen exponents mix m_u(M_Z), m_c(M_Z) with the pole m_t (a STRUCTURE
row; shifts of 0.02); the plumbing residual is mostly Huang–Zhou's 5→6-flavour matching at M_Z rather than running.

## 4. What it means, and what it does not

- The measured state of the parameter problem, under one rule: about six degrees of freedom bought by the whole
  field, none free but one, none explained. That is the comparison class for any claim about the nineteen — the
  weave's structure would enter this ledger with zero rows bought (B1671), which is the honest reading of "0 of 19":
  average for a structure without dynamics is zero; the best in the field is two.
- A HOLDS at a price is not an explanation: unification holds given a group and a content nobody has seen; Koide holds
  given nothing and is understood by nobody; θ̄ = 0 holds by construction in each mechanism.
- **What it cannot show:** that any relation is explained; which price is worth paying; anything about the weave. A
  ledger of sixteen rows is a first page, not the literature; extending it is §4 of the readers' page.
- **Falsifiers.** If a later arc, grading at M_GUT with the running done in-sandbox, finds both Georgi–Jarlskog
  relations HOLD in the MSSM, T1 becomes 7 and SUSY GUT the only framework at three; if a second price-free relation is
  ever found to HOLD at Koide's precision, T2 fails and the relation deserves its own arc.

## 5. Files

`verification/the_price_of_the_nineteen.py` (sealed ad3dd5d44), `.json`, `_run.txt`; `verification/factual_review.md`;
`verification/before_the_seal/` (the draft, its run, the smoke test); `verification/after_the_seal/alpha_s_0p1180.py`
(labelled post-seal check, with its outputs); the lock `tests/test_b1670_the_price_of_the_nineteen.py`; the readers'
page `docs/THE_PRICE_OF_THE_NINETEEN.md`.

## Addendum (2026-10-21, Review 66's premise audit)

> *Scoped 2026-10-21.* The claim line's last sentence, "the comparison class for any claim about the nineteen: a structure without dynamics buys zero rows", is a reading of this census, not a theorem: in the ledger priced here no framework without dynamics bought a row. The web seat's map (P-220) says the price of 13 undercounts the route the paper uses; that is checked when its map is committed. The ledger and its numbers are unchanged.

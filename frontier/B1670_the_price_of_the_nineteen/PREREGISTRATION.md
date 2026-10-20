# B1668 — THE PRICE OF THE NINETEEN (a sealed ledger of the claimed relations among the Standard Model's free parameters, each priced, graded by the identification ledger's rule and tested against today's data in-sandbox): preregistration

The referee lane (the outside referee of draft 3, `reports/referee_lane_2026-10-17/`), 2026-10-17, at the owner's word
("create your branch and lets do it"). POINT_REGISTER P-191. 0 of 19.

- **The question.** `docs/SM_SPECIFICATION_LEDGER.md` §B2 says of the nineteen: "every one measured, none predicted".
  That is true of parameter-free derivation and false of relations: the literature holds relations among the nineteen
  that predicted numbers before they were measured, texture relations good to a per cent, and mechanisms that set one
  parameter to zero — each bought with stated inputs. No ledger prices them in one place under one rule. This arc
  builds that ledger's first page by the record's own method: every relation recomputed in-sandbox from a sealed data
  table with propagated errors, graded by a sealed rubric, its price (its inputs beyond the Standard Model) named, and
  the counts the preregistration predicts — how many of the nineteen are bought, at what price, by how many hypothesis
  sets — read off by the instrument, not by the author. The referee's answer to "derive the nineteen" (report 03) is
  that no structure without dynamics can; this arc measures how far the field has got with structures that have them.
- **What is not claimed.** No value is derived here; nothing of the weave or the object enters. The arc is a measurement
  of the literature against data. The two theorems about the weave's triplet that the same report states (N8, the half
  floor; N10, the strong CP angle as the Dedekind phase of the modulus) are a separate arc (B1669), not this one.

## 0. Seen first

`VERDICT topic-sweep /koide|gatto|sartori|georgi.jarlskog|unification|sin\^?2 ?theta_?w|weinberg angle|criticality|asymptotic safety|quasi.?fixed|pendleton|froggatt|price list|nineteen|19 parameters|strong cp|theta.?bar|dedekind phase/: 48 of 1439 arcs on main match (NEGATIVE 13, OPEN 4, PROVED 30, RETRACTED 1)`
— read in full: B686 and B687 (the SM atlas: 14 of 23 dimensionless invariants unreachable, 8 base-rate-dead, Koide
the one live target; Koide's Q = 2/3 as a parametrisation tautology for every phase), B703 (the Koide angle θ₀ =
0.2222296(83), 0.89σ from 2/9, firewalled as post-hoc), B743 (zero gated hits of the object's tower against SM ratios,
Koide found and rejected), B304 (sin²θ_W = 3/8 as a reproduced GUT relation, not a value), B950 (the SM specification
ledger), B952 (the GUT requirements ledger), B968 (THE_SM_VERDICT), B915/B925 (the crossings: the object's gauge
boundary against α_em, negative). None of them grades the literature's relations against the data; B687 grades the
object's reach. **The literature** (each read at its source, access dates in §1): Koide 1983 (Phys. Rev. D 28, 252;
the 1982 Lett. Nuovo Cimento 34, 201) and the τ mass history; Gatto, Sartori, Tonin 1968 (Phys. Lett. B 28, 128);
Georgi and Jarlskog 1979 (Phys. Lett. B 86, 297); Georgi, Quinn, Weinberg 1974; Amaldi, de Boer, Fürstenau 1991 and
Langacker, Luo 1991 (unification with LEP data); Pendleton, Ross 1981 and Hill 1981 (the quasi-fixed point); Veltman
1981 (Acta Phys. Polon. B 12, 437); Froggatt, Nielsen 1979; Yao, Ding 2015 (θ_C = π/14 from Δ(6·7²)); Degrassi et al.
2012 and Buttazzo et al. 2013 (criticality at NNLO); Shaposhnikov, Wetterich 2010 (m_H = 126 GeV from asymptotic
safety); Peccei, Quinn 1977; Nelson 1984, Barr 1984; Feruglio, Parriciatu, Strumia, Titov 2024 and Penedo, Petcov 2024
(θ̄ = 0 from modular invariance); Antusch, Spinrath 2009 (GUT Clebsch factors against modern quark masses); Huang, Zhou
2021 (running masses at M_Z); PDG 2024 (the data). The novelty is the ledger and its rule, not any relation in it.

## 0b. Disclosed

- **The draft was run before the seal** (`verification/before_the_seal/relations_draft.py`, output `_run.txt`), and
  **the sealed instrument was smoke-tested once** (`before_the_seal/smoke_run.txt`, `smoke.json`); the instrument is
  deterministic, so the sealed run will reproduce the smoke test. Every threshold below was set after seeing those
  numbers. **No cell is blind.** The verdict is therefore graded as a *census informed by its own draft*, and it is said
  so in the FINDINGS. What the seal protects is the rubric, the price column, the dof-counting rule and the predicted
  counts, which were fixed before the ledger was read off by the instrument and cannot be moved after.
- **One instrument defect found and repaired before the seal:** the plumbing control compared this arc's 4-loop QCD
  running of the PDG 2024 inputs with Huang–Zhou's table, which was made from PDG 2020 inputs; m_u differed by 3.4%,
  of which 1.9% is the input. The control now runs *their* inputs through this running and compares with *their*
  table; the residual (0.9–1.6%, every flavour) is their electroweak and Yukawa part, which this arc does not include
  and prices as a 2% theory error on every cross-sector ratio.
- **The author of this arc wrote the reports it rests on.** The factual review of §4 is by a non-authoring reviewer, as
  WORKING_RULES 13 requires for a design whose premises name real-world facts.

## 1. The data table (sealed; every number carries its source and access date)

| quantity | value | source (accessed 2026-10-17 unless stated) |
|---|---|---|
| M_Z, M_W, M_H | 91.1880 ± 0.0020, 80.3692 ± 0.0133, 125.20 ± 0.11 GeV | PDG 2024 summary table, gauge and Higgs bosons |
| α̂⁻¹(M_Z), ŝ²_Z (MS-bar) | 127.930 ± 0.008; 0.23129 ± 0.00004 | PDG 2024 Electroweak Model review, §10.2.2 and Table 10.2 |
| α_s(M_Z) | 0.1179 ± 0.0010 | PDG 2024 Quark Masses review §60.7, citing the QCD review |
| m_u, m_d, m_s (MS-bar, 2 GeV) | 2.20 ± 0.07, 4.69 ± 0.05, 92.74 ± 0.54 MeV | PDG 2024 Quark Masses review eqs. 60.7, 60.8, 60.5 (the bracketed total errors) |
| m_c(m_c), m_b(m_b) | 1.275 ± 0.009, 4.196 ± 0.012 GeV | eqs. 60.23, 60.24 |
| m_t (direct); m_t (pole, from cross sections) | 172.57 ± 0.29; 172.4 ± 0.7 GeV | PDG 2024 summary table, quarks |
| m_e, m_μ, m_τ (pole) | 0.51099895 MeV, 105.6583755 MeV, 1776.93 ± 0.09 MeV | PDG 2024 |
| m_e, m_μ, m_τ (MS-bar at M_Z) | 0.48307, 101.766, 1728.56 MeV | Huang and Zhou 2021, arXiv:2009.04851, Table 3 (accessed 2026-10-16) |
| |V_us|, |V_cb|, |V_ub|, J | 0.22501 ± 0.00068; 0.04183 (+0.00079 −0.00069); 0.003732 (+0.000090 −0.000085); (3.12 ± 0.13)·10⁻⁵ | PDG 2024 CKM review eq. 12.27 and the line after it |
| the NNLO fit of the SM couplings and the stability bound | eqs. 55, 57, 60, 61e, 64, 65, 67 of Buttazzo, Degrassi, Giardino, Giudice, Sala, Salvio, Strumia, JHEP 12 (2013) 089, arXiv:1307.3536v2, with their reference values M_t = 173.10, α₃ = 0.1184, M_h = 125.66, M_W = 80.384 | arXiv:1307.3536v2 |
| v | 246.22 GeV | from G_F = 1.1663788(6)·10⁻⁵ GeV⁻² (PDG 2024 eq. 10.8) |

Quark masses are run to M_Z in 4-loop QCD with 3-loop decoupling at m_c and m_b (CRunDec via the `rundec` package);
the electroweak and Yukawa parts of the running, which Huang–Zhou include and this arc does not, are priced as a 2%
theory error on every cross-sector ratio (the plumbing control measures them at 0.9–1.6%). The charged leptons at M_Z
are taken from Huang–Zhou directly.

## 2. The rubric and the counting rule (sealed)

- **Status of a relation against data:** HOLDS if |pull| ≤ 2, with σ the data error and the stated theory error in
  quadrature; APPROXIMATE if |pull| > 2 but the relative deviation is within 10%; FAILS otherwise; FIT if the relation
  contains a continuous parameter fitted to the data it describes; STRUCTURE if it fixes a pattern and no number.
- **Price:** the inputs the relation needs beyond the Standard Model, listed in the instrument's ledger table before
  the run (a group, a content, a boundary condition, a texture, a scale choice is *not* a price; a mechanism is).
- **A relation buys one degree of freedom of the nineteen per independent equation it imposes**, when its status is
  HOLDS or APPROXIMATE and it carries no fitted continuous parameter. Two relations on the same dof count once. A
  mechanism that sets a parameter to zero buys that parameter at its price.
- **A hypothesis set** is a consistent framework (SUSY GUT; non-SUSY GUT; SM to M_Planck with one boundary condition;
  texture zeros; a finite flavour group; a strong-CP mechanism). T3 asks how many dof one set buys.

## 3. The cells

| cell | prediction | kind |
|---|---|---|
| **C0**, plumbing | this arc's 4-loop running of Huang–Zhou's own inputs reproduces their M_Z table within 2.5% for every flavour (the residual being their electroweak part); Koide's Q from the pole masses within 10⁻⁴ of 2/3 | gate |
| **T1**, the yield | the number of dof of the nineteen bought at HOLDS or APPROXIMATE without a fit is between 4 and 8 | test (informed: the draft gives 6: one gauge relation, m_H, m_s from GJ, m_τ from Koide, θ̄, θ_C) |
| **T2**, the free lunch | exactly one HOLDS relation has an empty price, and it is Koide's | test (informed) |
| **T3**, the best buyer | no single hypothesis set buys more than 3 dof | test (informed: SUSY GUT buys 2) |
| **T4**, the untouched | at least 11 of the 19 dof are bought by nothing | test (informed: 13) |
| **T5**, Koide is a pole-mass relation | |Q(pole) − 2/3| < 2·10⁻⁵ with the m_τ-predicted-from-Q=2/3 within 2σ of the measured m_τ; and |Q(M_Z running) − 2/3| > 5·10⁻⁴ | test (informed) |
| **T6**, GST and its texture's second prediction | √(m_d/m_s) within 2σ of |V_us|; the same texture's √(m_s/m_b) off |V_cb| by more than a factor 2 | test (informed) |
| **T7**, unification | one loop: with SM content the three pairwise meeting scales span ≥ 1.5 decades and the unification-predicted sin²θ_W is off the data by ≥ 5%; with MSSM content above 1 TeV the span is ≤ 0.6 decades and the prediction is within 2% | test (informed: 3.98 and 0.42 decades; −10.2% and −1.0%) |
| **T8**, criticality | the NNLO-fit critical Higgs mass with today's m_t and α_s exceeds the measured M_H by 1 to 6 GeV (the SM is metastable, not critical); the one-loop in-sandbox quartic, run from the NNLO boundary values, crosses zero below M_Planck | test (informed: +3.20 GeV, 2.3σ; the crossing at 10^8.3) |
| **T9**, the quasi-fixed point | the one-loop infrared fixed point of y_t gives m_t above the data by more than 15% for y_t(M_Pl) ∈ {1.5, 3, 10} | test (informed: 24–28%) |
| **T10**, Georgi–Jarlskog | the double ratio (m_μ/m_τ)/(m_s/m_b) is within 10% of 3; the double ratio (m_d/m_b)/(m_e/m_τ) is outside 10% | test (informed: 3.16 ± 0.07, 3.37 ± 0.08) |
| **T11**, b–τ | at one loop the SM ratio m_b/m_τ at 2·10¹⁶ GeV is below 0.8; the MSSM ratio (TeV threshold, tan β ∈ {3, 10, 50}) lies in [0.8, 1.0] | test (informed: 0.67; 0.85, 0.84, 0.88) |
| read-outs | the full ledger table; the quark masses at M_Z; λ(M_Pl) and Λ_I from the NNLO fit; the Froggatt–Nielsen exponents and how many are near an integer (base rate 0.4 each); the Veltman and massless-up rows; the fixed-point m_t | — |

**If C0 fails, nothing after it is read as a result.** Verdict rule: PROVED if T1–T11 hold (the ledger's first page
stands as measured, with its counts); NEGATIVE as sealed if any fails, with the failing cell's reading. Because every
cell is informed by the draft, a PROVED verdict certifies that the sealed rubric and data reproduce the draft's
reading, not that a blind prediction was met; the FINDINGS say so in their first line.

## 4. What it would mean

- **If T1–T4 hold:** the nineteen have been bought, by the whole field, to the extent of about six degrees of freedom,
  never for free except Koide, never more than three by one framework, and thirteen not at all. That is the measured
  state of the parameter problem, and the comparison class for any claim the program (or anyone) makes about the
  nineteen: a structure that bought one dof at a price comparable to a GUT's would be average; one that bought three
  would be the best in the field.
- **If T2 fails because a second free relation holds,** the ledger has found a Koide-class coincidence worth its own
  arc. **If T3 fails,** some framework buys more than three, and the owner should know which.
- **T5–T11** are the recomputations that make the ledger a measurement rather than a reading list; each is a known fact
  of the literature re-derived here, and a failure would mean either the data have moved or the instrument is wrong.
- **What it cannot show:** that any relation is *explained*; which price is worth paying; anything about the weave
  (B1669 is the arc for that). 0 of 19.

## 5. Files

`verification/the_price_of_the_nineteen.py` (sealed), with `the_price_of_the_nineteen.json` and `_run.txt` after the
run; `verification/before_the_seal/` (the draft, its output, the smoke test); `verification/factual_review.md` (the
non-authoring reviewer's report, §4 of WORKING_RULES 13, written between the seal and the run). The lock is
`tests/test_b1668_the_price_of_the_nineteen.py`. The ledger's page for readers is `docs/THE_PRICE_OF_THE_NINETEEN.md`.

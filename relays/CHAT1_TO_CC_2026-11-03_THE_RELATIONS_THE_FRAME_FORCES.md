# chat1 → cc (main), 2026-11-03: THE RELATIONS THE FRAME FORCES (P-568's first half; FL-15; B1809's owed f(d) for FR-FIB; data-free; it assigns nothing) — on each of FR-FIB's branches as B1825 typed it (line, direction, radius rule, reading; c = 3, H = I and h₀ = 0 fixed), the only continuous input is τ. B1809's output rank f(d) is therefore at most 2, and it is exactly 2 on all 1 536 distinct branches sampled, each at two τ (3 328 evaluator rows; at every sampled point some two output gradients make an angle whose |sin| is at least 0.043). So the ten graded outputs obey at least 8 relations on every branch and exactly 8 wherever f(d) = 2, and 11 of 13 with y_b/y_t, y_τ/y_t and θ̄ (once θ̄'s convention is fixed; θ̄ is undefined where a quark is massless). On the 32 branches where a null direction is read alike in all three sectors on a line of order 1 or 2, the ten reduce to m₂/m₃ and f(d) = 1. That is the most the frame could explain relationally on one branch, before the menu's bits. The explicit, τ-independent relations are of two kinds. B1728's law, read as relations among the outputs, forces equalities only on the census lines of order ≤ 7 (62 of 266): d = e on orders 4 and 5, u = d with V = 1 on orders 3 and 6, u = e on order 7, all three equal on orders 1 and 2; on orders 8–12 it forces none. The frame's exact zeros fix outputs: on every order-4 line the first generation is massless in all three sectors and, where the mixing is defined, |V_us| = |V_ub| = J = 0 (B1716, B1713); on every order-12 line e/τ = 0; for the two null directions R and t = −5/288, u/t = d/b = e/τ = 0 on every line (B1809 § 4); and where the matter is null too (every sector on order 4, the leptons on order 12; B1716) the Yukawa has rank one (B1659's adjugate law): with a null direction all six mass ratios vanish on order 4, the mixing undefined, and μ/τ = 0 on order 12. B1742's half-period mechanism adds relations that depend on the direction (computed at two τ by check (3), not derived): on every order-8 and order-10 line, d = e for a Higgs lacking the quaternion component the line's class fixes, or along one unit only (QI on the candidate family's (2/5, odd/10) and 15 other lines, the list main's S297 found for P-355); on the order-4 lines u = d = e likewise; on order 6, d = e and u = e in the ratios only, for a Higgs along the unit the class fixes. Relations among within-sector ratios move with the scale by at most B1718's running (about 12% in log for the down–lepton and up–lepton ones, 25% for the up–down ones); inter-sector ones need a declared scale. The rigid inter-sector values (P-568's second half) are not computed here, because P-585 holds y_b/y_t out for the candidate family's level-2 card — 0 of 19

chat1 (the web seat), at the owner's word of 2026-11-03 ("go for it", on the seat's proposal; item 2, the relational
ledger). **A data-free note; it assigns nothing and changes no verdict.** No measured value is read by the checks; § 3
quotes main's record on the running (B1718, R1, S294). No inter-sector value is printed anywhere B1728's law does not
force it to equal another; § 2's half-period coincidences are printed as counts of lines, and their departures only by
decade.

The checks are committed beside the note, each script before its output, and run against main at 354a4ea4d:
- `relays/chat1_2026-11-03_relations/relations_check.py`, version 2 at 796f02e2b and its output at 5c98cc7e5. Version 1
  (5aecc2bce, b3be3f9f2) kept the exact zeros, whose noisy logarithms inflated its rank measure. Version 2 drops outputs
  below 10⁻⁶.
- `relays/chat1_2026-11-03_relations/halfperiod_check.py` (check (3)), written at the referees' findings: version 1 at
  41451dbee (output cef31ebfe) and version 2 at 2b515e748 (output a993b7df6). It covers the half-period classes, the
  coincidences by direction (and, in version 2, with random directions), the menu's departures, the exact zeros, the
  order-4 mixing and the collapsed branches. 0 of 19.

**Refereed read-only before the push.** The first pass found the note FAIL as drafted, on one blocking finding: its list
of explicit relations left out the frame's exact zeros (the order-4 lines' massless first generation with
|V_us| = |V_ub| = J = 0, the order-12 leptons' zero, the null directions' zeros), which made two summary sentences false,
one of them an unearned negative about orders 8–12. Its corrections:
- B1742's mechanism is not confined to (2/5, odd/10). The seat's check (3) confirms the referee's classification and
  refines order 6's case to the unit the line's class fixes.
- "8 relations on every branch" overclaimed: f(d) = 1 on 32 branches of orders 1–2.
- B1825 typed twelve directions (a₀ ≡ F₋₂, so the evaluator's rows double-count); h₀ = 0 was missing from what is fixed.
- The scale bound for the up–down relations is about 25%, not 12%.
- § 4 misstated what level 2 requires; the 10⁻⁶ floor's noise claim was too general.
- Nits, and missing credits (B1698, B1726, B1713, B1789, B1824, P-489, P-355, FL-14).
All were applied. The referee reran the sweep and reproduced version 2's output byte for byte. It checked every
quotation, the table on all 266 lines and the rank at the note's 16 points with its own step-stable measure, and found
nothing that computes a held-out value.

A second read-only pass reran check (3) from 41451dbee against main at 354a4ea4d and reproduced its output byte for byte
(exit 0, empty stderr). It recomputed the order-10 class list and the twist identities exactly, and reran the
classification with random Higgs directions at both radii and a third τ, with no exception. Its verdict: PASS WITH
CORRECTIONS, nothing blocking. Its corrections:
- the null directions' second-generation zeros on orders 4 and 12 (a null direction on a null matter is rank one);
- the branch count (1 536 branches at two τ, not 3 072);
- R's one order-4 cell, and the menu's departures in the ratios, which run up to two decades above the largest-value
  measure;
- § 4's parenthetical on the forced equalities;
- nits.
All were applied. Version 2 of check (3) (2b515e748, output a993b7df6) counts the second-generation zeros, bins both
departures by decade, and repeats the classification with random directions.

**Seen first.** Main at 354a4ea4d (S296); full text, `--no-aliases`; the VERDICT is cut before its list of other lanes:
- `VERDICT topic-sweep /co-rank|corank|Jacobian|relations the frame forces|relational sense|rigid (inter-sector )?outputs?|y_b ?/ ?y_t|y_τ ?= ?y_b|b.τ unification|coincidence law|hypercharge mod|6Y mod/ (full text): 84 of 1576 arcs on main match (NEGATIVE 24, OPEN 5, PROVED 53, RETRACTED 2); 6 register rows match (DONE 3, QUEUED 3)`
- **Bearing on it:**
  - **B1809:** "f(d) is the generic rank of Φ on C(d) … The relations among the outputs number m − f(d)"; for FR-FIB,
    "m = 10 (six mass ratios, four CKM parameters). f(d) ≤ 2 with DR at a fixed line"; and, owed, "P-418: f(d) per
    frame as a Jacobian rank".
  - **B1728 (PROVED, "if" direction) and B1703** (the census that found the law): when two sectors share singular
    values on a line of order N.
  - **B1698** (§ "Why d and e coincide", after its seal): the earliest statement of the table's d = e rows, which B1728
    cites — Y_e = Y_dᵀ "with the same singular values" on order-5 lines, Y_e = Y_d on order-4 lines, and the order-4
    lines' massless first generation.
  - **B1742 § 3:** the α = 2/5 lines, where "the lepton twists … equal, modulo the lattice … the down twists (w, 2w)
    swapped and shifted by half-periods"; **P-355**, which owes "the identity's full list of lines"; **B1789** (DR's QI
    component, "about 7% of the largest at Im τ 3").
  - **B1716 and B1713** (the exact zeros that mask orders 4 and 12; B1713's dated note: on the order-4 lines the up and
    down null vectors coincide); **B1726** (§ "R7's near miss": with c = 3, D = 9·D_frame); **B1824** (a₀ = η⁴F₋₂/6, so
    the declared menu has twelve distinct directions); **P-489** (h₀ a continuous datum set by hand).
  - **B1718** (the within-sector running); **A5** (B1827's reader, on the inter-sector ones; its item 7 is FL-14's).
  - **P-574, P-585;** S291's recount (FL-05).
- **Main moved while the note was under referee** (S297, 36fd3c315; both sweeps rerun there, VERDICT unchanged). S297
  paid P-355's first owed item (data-free; B1830's verification/recheck/p355/): the lepton and down spectra coincide for
  every Higgs exactly on B1703's d = e points, and "for a Higgs with NO QI component exactly on their 40 β-half-lifts"
  (16 points of order 8, 24 of order 10; 20 lines up to sign), "which extends B1742's α = 2/5 case to every such line".
  That is § 2's QI class, found independently. S297 tested a generic and a QI-free Higgs only.

**What it answers.**
- **FL-15:** "the honest "n of 19" in the relational sense (the number of relations the frame forces: a Jacobian co-rank)
  has never been computed".
- **P-568** ([LEAD], Q1): "the number of relations the frame forces (the Jacobian co-rank of its outputs in its
  continuous data) and its rigid inter-sector outputs (m_t : m_b : m_tau at the strip; y_tau = y_b on order-5 lines)
  have never been computed".

## 1. The count: f(d) = 2 on every branch sampled, so 8 relations among the ten (9 on 32 branches of orders 1–2; none of the ten varies on the 192 order-4 branches with a null direction)

**What fixes a branch.**
- In B1825's typing, FR-FIB's discrete data fix a branch: the line, the direction (twelve: B1810's thirteen with
  a₀ ≡ F₋₂, B1824), the radius rule (L_max or L₂) and the reading (8). That is 192 branches per line (the evaluator's 208
  rows count a₀ and F₋₂ twice), with c = 3, H = I and h₀ = 0 fixed.
- What is left is τ:
  - the radii are functions of Im τ (B1821's interpolant of B1667's column, P-542);
  - the directions are functions of τ.
- B1809's C(d) for FR-FIB also allows "a generic section's coefficients". B1825's typing has none, and they would add
  continuous data.
- h₀, the Higgs's scalar component, is a continuous datum set by hand (h₀ = 0; B1809 § 4's dated note, P-489); the
  evaluator's Higgs has none. Freed, it would add continuous data, as a section's coefficients would.

**So f(d) ≤ 2**, as B1809 says for DR at a fixed line: on a branch the ten graded outputs (the six mass ratios, |V_us|,
|V_cb|, |V_ub|, J) are functions of the two real coordinates of τ.

**Check (1)** (`relations_check.py`, version 2):
- **Where:** eight lines of orders 7–12, at τ = 0.13 + 2.2i and 0.31 + 3.1i.
- **Which branches:** all 3 328 rows with the CKM defined: 1 536 distinct branches (8 lines × 192) at two τ each, each
  a₀ row repeating its F₋₂ row.
- **The measure:** the gradients in (Re τ, Im τ) of the ten (logs of the nine positive ones, and J).
  - An output below 10⁻⁶ is dropped from its branch's gradients: an exact zero such as B1716's, or a value whose
    logarithm is too noisy to differentiate. This drops at least one output on 1 284 of the 3 328 rows (by the referee's
    count, 1 216 of them drop an exact zero: the null directions' and the order-12 leptons'). The floor alone does not
    exclude noisy gradients — elsewhere in the band it can report a second direction from noise — but at these points
    the referee's step test (h = 10⁻⁴ against 10⁻⁵) reproduces every number below.
  - The largest |sin| of the angle between two kept gradients is at least 0.043. It is below 0.1 on 26 rows, all on
    the slope-1/12 and slope-5/12 lines, all with a null direction (R on 18, t = −5/288 on 8, by the referee's count),
    and below 10⁻³ on none.
- **Result:** f(d) = 2 on every branch sampled, so co-rank exactly 8 there. A ratio of singular values would mislead
  here: one output can vary far faster in Im τ than the others, so σ₂/σ₁ can be tiny while the gradients are far from
  parallel.
- **Where it is less.** f(d) is the generic rank.
  - On the four lines of orders 1 and 2, a null direction read alike in all three sectors (S S S or S̃ S̃ S̃) makes the
    three sectors coincide (B1728), V = 1, and the first generation massless (B1809 § 4). The ten reduce to m₂/m₃, so
    f(d) = 1 on those 4 × 2 × 2 × 2 = 32 branches (check (3) item (6)).
  - On the six order-4 lines a null direction meets a null matter in every sector (B1716), so each Yukawa has rank one
    (B1659's adjugate law): the six mass ratios vanish and the mixing is undefined, so nothing among the ten varies on
    those 6 × 2 × 2 × 8 = 192 branches (check (3) items (4) and (5)). On the order-12 lines the leptons alone are rank
    one (μ/τ = e/τ = 0), and f(d) stays 2 (check (1)'s order-12 rows).
  - On a reflection line (Re τ = 0 for the lines the mirror fixes, B1821) every output except J is even in Re τ, so
    where J ≡ 0 the pointwise rank is 1. On (0, 0) at τ = 2.5i, J ≡ 0 on the 104 of 208 rows that read up and down
    alike; on the others J's slope is tiny but not zero, so a numerical count of rank-1 rows depends on its floor (136 at
    10⁻¹⁰, 156 at check (1)'s 10⁻⁸; the referees' counts).

**With the frame's three other outputs.**
- They are y_b/y_t, y_τ/y_t, and θ̄ once a rule fixes its convention (P-323, P-569).
- They are functions of τ on a branch too, so the co-rank is 11 of 13.
- **This is the frame's relational capacity on one branch:** the most it could explain relationally there if our world
  lay on that branch's surface.
- It counts nothing of the 53 looks, or of the branches and addresses a search chooses among. C_ten and K
  (THE FINAL ACT'S BAR) already price that choice.

The other six of the 19 (g₁, g₂, g₃, m_H, v, y_t) have no frame (S291).

## 2. The explicit relations

**B1728's law, read as relations among the outputs.** B1728 proves that two sectors share singular values whenever their
charges agree mod N up to swap and sign (the "if" direction). Among the outputs this means:

| order N | sectors forced equal (same reading in both) | among the ten | among the inter-sector ratios | census lines (of 266, up to w → −w) |
|---|---|---|---|---|
| 1, 2 | up = down = leptons | c/t = s/b = μ/τ and u/t = d/b = e/τ; V = 1 | y_t = y_b = y_τ | 1 + 3 |
| 3, 6 | up = down | c/t = s/b, u/t = d/b; V = 1 (\|V_us\| = \|V_cb\| = \|V_ub\| = J = 0) | y_t = y_b | 4 + 12 |
| 4 | down = leptons; the lightest of all three sectors is exactly 0 (B1716; B1713), and the up and down null vectors coincide (B1713's dated note); with a null direction the second generation too (rank one; B1659), the mixing then undefined | s/b = μ/τ; u/t = d/b = e/τ = 0; \|V_us\| = \|V_ub\| = J = 0 | y_b = y_τ | 6 |
| 5 | down = leptons, transposed (Y_e = λY_dᵀ; Y_u symmetric) | s/b = μ/τ, d/b = e/τ | y_b = y_τ | 12 |
| 7 | up = leptons, the twists swapped and negated, so Y_e = λY_uᵀ (B1728's steps 2–3) | c/t = μ/τ, u/t = e/τ | y_t = y_τ | 24 |
| 8–11 | none (B1703's census; B1728's converse is computed, not proved) | none | none | 156 |
| 12 | none; the leptons' lightest is exactly 0 (B1716, B1713), and with a null direction their second too | e/τ = 0 (μ/τ = 0 too with a null direction) | none | 48 |

**How to read the table.**
- **The raw frame.** "Among the ten" is before c: with c = 3 by hand on the leptons, the d = e rows of orders 1, 2 and 5
  become (μ/τ) = 3(s/b) and (e/τ) = (d/b)/3, so D = (m_μ/m_e)(m_d/m_s) = 9 (P-355; B1726). On order 4, m_d = m_e = 0, so D
  is undefined.
- **Readings.** Each relation holds when the two sectors both read S or both read S̃ (B1728's step 2). The reading at
  B1825's address, (S̃, S̃, S) (S̃ for up and down, S for the leptons), keeps up = down only; the candidate family's
  (S̃, S, S) keeps d = e.
- **Check (2):** one or two lines of each order 2–12 at τ = 0.13 + 2.2i, DR, L₂, both common readings. Each sector pair is
  printed only as "equal" or "apart".
  - every row follows the table;
  - on both order-4 lines, (1/4, 0) and (1/2, 1/4), the lightest down and lepton masses are below 10⁻¹² in both (B1716's
    exact zeros; the up quarks' too, which a pair comparison cannot show);
  - no inter-sector value is printed, only "equal" or "apart".
- **The null directions.** R and t = −5/288 are null (h·h = 0), so det Y = 0 in every sector (B1659): u/t = d/b = e/τ = 0
  on every line and in every reading (B1809 § 4). On the order-4 lines (every sector) and the order-12 lines (the
  leptons) the matter is null as well (B1716), so the Yukawa has rank one (B1659's adjugate law) and m₂ = 0 too; that is
  why the order-4 rows have the mixing undefined. B1809 § 4's "m₂ ≡ 0 only at L = ∞" for the isotropic directions holds
  off these lines only.
- **Check (3)** (`halfperiod_check.py`) counts the zeros over all 266 lines, both radii, the thirteen directions and both
  readings per sector, at τ = 0.13 + 2.2i and 0.27 + 2.6i (m₁/m₃ below 10⁻¹²):
  - the null directions: every row, in all three sectors, on every line; and m₂/m₃ below 10⁻¹² too on every order-4 row
    (all three sectors) and every order-12 lepton row, and on no other;
  - the eleven others: every row in all three sectors on the order-4 lines, every lepton row on the order-12 lines, and
    no other row (at these τ: on Re τ = 0 the quarks' lightest also vanishes on P-292's 16 order-12 lines, now P-337 —
    B1713's dated correction and the kernels relay's zero law; a zero on a curve, not a relation on the branch).
  - On the six order-4 lines, the 1 056 rows with the up and down spectra non-degenerate have |V_us| and |V_ub| at most
    2.0 × 10⁻¹², |J| below 10⁻²⁴ and |V_cb| at least 6 × 10⁻⁵; the other 192 rows have the mixing undefined, and all
    of them carry a null direction.
  - On the 32 collapsed branches of § 1 the three sectors share their spectrum, m₁/m₃ < 10⁻¹² and V = 1, at both τ.

**Relations that depend on the direction: the half-period coincidences (B1742 § 3 and their kin).**
- On w = (2/5)τ + k/10 the lepton twists equal the down twists swapped and shifted by half-periods. For k even (order 5)
  this is the table's d = e. For k odd (order 10) the spectra coincide "only for a Higgs with no QI component", the
  departure being linear in that component (F₂₂'s is about 10⁻¹³ at Im τ 2.6, F₆'s about 3 × 10⁻⁴).
- **The mechanism is general** (the referee's finding; check (3) confirms it).
  - On order 8 the lepton twists are the down twists shifted by the half-period 4w: (−3w, 6w) = (w, 2w) + (−4w, 4w).
  - On order 10 they are swapped and shifted by 5w: (−3w, 6w) = (2w, w) + (−5w, 5w).
  - On order 4 the up twists differ from the down and lepton ones by 2w.
  - The half-period's class ((N/2)α, (N/2)b) mod 1 fixes one quaternion unit: (0, ½) QI, (½, 0) QJ, (½, ½) QK.
- **Check (3)'s classification** (seven synthetic directions, reading S in all three sectors and again S̃, L₂, every
  census line; a pair counts when all three singular values agree to 10⁻⁸ at both τ). Two sectors share their spectrum
  for a Higgs with no component along the unit the line's class fixes, or along one unit only:
  - d = e on all 24 order-8 lines and all 36 order-10 lines, a third per class. The candidate family's (2/5, odd/10) are
    5 of the 12 order-10 lines in the QI class; the others are (1/5, odd/10), (0, 1/10) and (0, 3/10). The QI class is
    S297's list (P-355's first item); the QJ and QK classes, the one-unit Higgs and the next two items are new here.
  - u = d and u = e on the six order-4 lines, two per class.
  - On order 6, d = e and u = e in the ratios only (the largest singular values differ), for a Higgs along the unit the
    line's class fixes.
  - Nothing on order 12, and nothing on an odd order beyond B1728's table. The table read S̃ is the same in every cell.
- **On the menu** (check (3); the largest departure over the class's lines and both τ, by decade, in two measures: all
  three singular values relative to the larger largest one, and the two mass ratios each relative to itself, which the
  relation equates; the second runs up to two decades above the first):
  - F₂₂ and F₂₆ sit on the QI-class relation to better than 10⁻⁸ in both measures on all 20 QI-class lines of orders 8
    and 10, in both readings. F₁₈ does in the first measure but only to the 10⁻⁷ decade in the ratios; F₁₄ to the 10⁻⁷
    and 10⁻⁵ decades. On the two QI-class order-4 lines F₁₄–F₂₆ are below 10⁻⁸ in both measures.
  - F₋₁₀ and F₋₆ are led by their QI component (QJ and QK down to 1.4 × 10⁻⁶ and 3 × 10⁻⁴ of |S| at Im τ 2.6; about
    3 × 10⁻⁵ and 2 × 10⁻³ at Im τ 2.2, the referee's figures), so they come near every class's relation, as a one-unit
    Higgs would: F₋₁₀ to the 10⁻⁵ decade in the first measure and 10⁻³ in the ratios, F₋₆ to 10⁻³ and 10⁻².
  - DR, a₀ (≡ F₋₂), R and t = −5/288 depart by at least 10⁻² on every class of orders 8 and 10, in both measures. On
    order 4, R's first-measure departure on the QI-class lines read S is in the 10⁻³ decade; its ratios there are all
    zero (a null direction on a null matter). No menu direction lacks QJ or QK exactly.
- B1809 lists B1742's case as "The six are four" on α = 2/5. That is where THE SIX ON THE STRIP (B1829; P-585) lives;
  its best rows sit about 20% off the relation (D 10.92–11.05 against 9; S295, P-585), DR's QI component being about 7%
  at Im τ 3 (B1789).
- This is part of P-355's owed "full list of lines": a computation at two τ, not a derivation.

**Where this leaves the frame's searches.**
- B1825's address, (3/8, 3/8), is of order 8 and in the QK class. B1728's law forces nothing there. The half-period
  relation d = e would need a Higgs with no QK component and, under its mixed reading (S̃ for the down quarks, S for the
  leptons), one whose components share a phase, S̃ ∝ S (the referee's run); check (2) shows no coincidence on (3/8, 1/8)
  with DR.
- On the candidate family's lines the relation is B1742's, conditional on the direction; every order-8 and order-10 line
  has its own.
- On orders 8–12 the explicit relations are the order-12 leptons' zero (both light leptons with a null direction), the
  null directions' zeros and the half-period
  coincidences, which depend on the direction (above). Beyond them the relational content is § 1's co-rank, which a card
  can name in advance only as the branch's surface.

## 3. Where each relation lives (the scale)

- **The frame declares no scale** (FL-05; P-574 asks every future card to declare one, or price a menu).
- **Relations among within-sector ratios.** Up to 10¹⁶ GeV the up-type ratios fall by at most 12% in log, the down-type
  ratios rise by at most 12% and the leptons' do not run (B1718: factors 0.884, 1.131 and 1.000 at 10¹⁶ GeV). A relation
  exact at one scale between M_Z and 10¹⁶ GeV is therefore off at any other by at most about 12% in log for the
  down–lepton and up–lepton rows (s/b = μ/τ, d/b = e/τ, c/t = μ/τ, u/t = e/τ) and about 25% for the up–down rows
  (c/t = s/b, u/t = d/b), whose sectors run in opposite directions (R1, B1827: −11.6% and +13.1% to 2 × 10¹⁶ GeV).
- **Inter-sector equalities.** y_b = y_τ, y_t = y_b and y_t = y_τ are statements at one scale, and running moves them by
  factors.
  - A5: the order-5 lines' y_τ = y_b is "a GUT-scale statement being compared at the wrong scale, where the within-sector
    ratios of B1718 do not care but the inter-sector ones do".
  - S294: nature's m_b/m_τ "crosses 1 near 1e6 GeV in R1's data-only table".
  - None of them can be graded without the declared scale P-574 asks for.

## 4. P-568's second half: not computed here

P-568 also asks for "its rigid inter-sector outputs (m_t : m_b : m_tau at the strip …)". The seat does not compute them,
for this reason:
- **P-585** (Q1) names y_b/y_t "(never computed, the cleanest)" among the held-out targets of the candidate family's
  level-2 card, which GENESIS v1.61 grades under GAP1's v1.60 rule: no function of a held-out quantity may be used in
  building, choosing or tuning the frame, and its prior looks count in m_V.
- Printed now, the strip's y_b/y_t would be a look, and it would be in view when the card fixes its scale (P-574) and
  its theory error (P-575). The seat counts that as compromising the target, not merely pricing it.

So the seat leaves it to that card. It proposes that main order the two rows: either compute P-568's rigid outputs only
inside the sealed level-2 card, or drop y_b/y_t from P-585's held-out list (a third order — computing it now and
counting the look in m_V, as P-585 does for θ̄ — leaves the card's scale to be chosen with the value known; the seat does
not propose it). This note prints none of them except where B1728's law or a half-period coincidence forces them equal
(the latter equate the largest singular values too: y_b = y_τ on orders 8 and 10, and y_t = y_b = y_τ on order 4, for a
Higgs lacking the line's component). None of these equalities is at the candidate family's address: on its order-10
lines neither law relates the up sector to another (check (3)), so nothing here bears on P-585's y_b/y_t, and y_τ/y_b is
not a clean target (P-585). P-568's "y_tau = y_b on order-5 lines" is B1728's law, so its second half reduces to
m_t : m_b : m_tau at the strip.

## 5. What it does not show

- No relation is compared with a measured value, and no relation is claimed to hold or fail in our world.
- The co-rank is a count of relations per branch, not an achievement. It says nothing of whether any branch's surface
  passes near our ten.
- B1728's converse (no coincidence beyond its table) is B1703's census and B1728's check, not a proof. Check (3) adds a
  census of all 266 lines at two τ: its generic direction shows nothing beyond the table, and the other six kinds show
  only the half-period coincidences (§ 2). B1703's census used one Higgs (∂R), so the converse is for a generic Higgs.
- The half-period relations are classified by line and component (§ 2) from a computation at two τ, not derived;
  check (3)'s 21 random directions (three of each kind), read S and S̃, agree with it on all 33 516 comparisons. Their
  departure off the condition is known only for B1742's family and, by decade, for the menu (check (3)).
- Y_u's symmetry on order-5 lines constrains the rotations, not the ten, and is not counted.

## Proposals (main's to take or leave)

- **FL-15, P-568's first half and B1809's owed count (P-418's f(d)):** for FR-FIB as B1825 typed it, f(d) = 2 on every
  branch sampled (1 on the 32 branches of orders 1–2 with a null direction read alike in all sectors; on the 192
  order-4 branches with a null direction the six ratios vanish and the mixing is undefined). The relations
  number 8 of the ten (11 of 13) where f(d) = 2, and the explicit ones are § 2's table (B1728's law with B1716's and
  B1713's zeros), the null directions' zeros, and the half-period coincidences (B1742's case and its kin).
- **P-355's owed list of lines:** S297 paid it for the QI class. § 2's classification (check (3), computed at two τ, not
  derived) adds the rest: d = e on the QJ- and QK-class lines of orders 8 and 10 for a Higgs lacking QJ, respectively
  QK; d = e on every order-8 and order-10 line for a one-unit Higgs; u = d = e on order 4 likewise; and order 6's
  coincidences in the ratios only.
- **P-568's second half and P-585:** order them as in § 4.
- **A relations card (P-568's next step):** it must declare its scale for the inter-sector rows (§ 3). On FR-FIB's
  searched lines the direction-conditional relations are the half-period coincidences (§ 2); the menu's F₂₂ and F₂₆
  realise them to 10⁻⁸ on 20 lines (F₁₈ to 10⁻⁶ in the ratios).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE RELATIONS THE FRAME FORCES (P-568's first half; checks: relations_check.py version 2 796f02e2b → 5c98cc7e5, halfperiod_check.py version 1 41451dbee → cef31ebfe, version 2 2b515e748 → a993b7df6) | "the only continuous input is τ" | `relays/CHAT1_TO_CC_2026-11-03_THE_RELATIONS_THE_FRAME_FORCES.md` @ the commit adding it | — | P-568, FL-15, B1809, P-418, P-585, P-355, B1728, B1742, B1716, B1713 | 2026-11-03 |

0 of 19.

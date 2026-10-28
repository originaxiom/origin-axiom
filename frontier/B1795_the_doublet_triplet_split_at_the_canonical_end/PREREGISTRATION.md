# B1795 — PREREGISTRATION: THE DOUBLET–TRIPLET SPLIT AT THE CANONICAL END — does B1656's frame keep a light Higgs pair while lifting every colour-triplet pair (P-325; L250 (ii))

cc (main), 2026-10-28, the sweep's second-ranked zero-freedom lead (P-325). **Sealed before `verification/split.py`
computes any vector-like pair.** The read-out is structural and data-free. It is sealed because a split would open a
value contact: the unification ratio, 5/7 with the Higgs multiplets split, against 0.7172 measured (B1484). That
comparison is not made here and would need a seal of its own. 0 of 19.

## Why

- **What a split would mean.** In SU(5)-like unification the weak mixing angle at the unification scale follows from the
  light spectrum. B1484 found:
  - the desert gives 0.528 (measured 0.7172);
  - complete multiplets give ½;
  - light Higgs doublets with heavy colour triplets give 5/7 = 0.714.
- **No flat abelian line splits by invariance.** "No flat abelian line that keeps the quark doublet removes the triplet"
  (B1484, the 27's w_D = −2·w_Q).
- **The frame supplies vector-like masses instead.** B1656's frame now gives masses from couplings (the L250 reader,
  `audit/drafts/leads_reeval/L251_L250.md` § L250 (ii)):
  - the D D^c pair is the sector with twists (−2w, 2w), and the H_u H_d pair the sector with (3w, −3w);
  - a singlet (6Y = 0) is the partner of both.
- **Whether the frame splits doublets from triplets is a computation nobody has made** (P-325; never computed).

**What is known before the run** (stated, not computed here):
- **Order 5 cannot split.** The two pairs' twists coincide up to a lattice shift iff N ∣ 5, since −2 ≡ 3 (mod 5); a
  charge shift by N is a phase (B1728). This is SU(5)'s own doublet–triplet problem.
- **At leading order every line keeps one massless member of each pair** (R-check 3, the reader's). The "1"-channel
  residue θ₁(δw) vanishes for a Higgs charge δ = 0 (B1703's rule). But that is a leading-order statement, and the
  canonical end, where L is of order one, lifts B1703's protection (B1711, B1716).
- **B1716's exact-zero law** (det M = ¼ Σ c_s R_s² vanishes iff the left twist has exact order 4 and the right twist
  order ≤ 2) was proved on the Standard Model's three sectors only. Opposite twists have equal orders, so as written it
  never fires on a vector-like pair. Whether other exact zeros appear when the twists sum to zero is unknown.

## The model (no data)

- **The frame:** B1656's four-channel coupling at B1667's canonical end, through B1726's compute() path:
  - its b1656_funcs (B1723's);
  - its Higgs section S from B1691's theta constants, and S̃ = εS*εᵀ;
  - L_max and L₂ read from B1667's Re τ = ¼ column.
- **The pairs:** D = (−2, 2), D^c-first = (2, −2), H = (3, −3), H^c-first = (−3, 3), as (left, right) charges 6Y.
- **The partner:** the singlet is typed as the frame's Higgs section, with the same S, line-free and charge-free as in
  B1726. This is a hypothesis, disclosed.
- **Per line, point and pair:**
  - the residues R_s, the regularised norms c_s and D = Σ c_s R_s² = 4 det M (independent of L, B1716);
  - Dn = ∣D∣ / (max∣c∣ · Σ∣R_s∣²), B1716's Z6 normalisation; exact zeros sat at ≤ 6.5 × 10⁻¹⁴ there, and non-zeros at
    ≥ 1.9 × 10⁻⁴;
  - the coupling Y = coupling(S or S̃, M) at both horocycles: its singular values, ∣det M∣ and ∣tr(εSMᵀ)∣.
- **The lines:**
  - B1713's 266, orders 1–12 up to sign;
  - the twenty slope-2/5 lines of exact order 60 (B1792), six of which carry the six.
- **The points:**
  - B1716's two generic τ, 0.37 + 2.2i and 0.11 + 1.7i;
  - the six's strip point 0.730769231 + 3.037487672558812i (B1792's best row).
- **Size:** 286 lines × 3 points × 4 pair orientations = 3 432 sector computations.

## Cells

"Exact zero" means Dn < 10⁻¹⁰ at all three points, for the pair in either slot order.

| cell | prediction | prior |
|---|---|---|
| C1, control | the Standard Model's sectors through split.py's own path reproduce B1726's compute() at the strip point on (2/5, 49/60) to 10⁻⁹ | 99% (run before the seal: 0.0) |
| C2, control | on every line of order 1 or 5, Dn agrees between the D pair and the H pair to 10⁻⁹ (relative) — the order-5 identity | 95% |
| **S1, decisive** | no line has an exact zero of det M for the H pair | 85% |
| S1′ | no line has an exact zero of det M for the D pair | 85% |
| **S2, the split** | some line has an exact zero for the H pair and none for the D pair | 7% |
| **S3, decisive** | at the strip point, on the six's six carrying lines (B1792: 7/60, 29/60, 41/60, 47/60, 49/60 and 11/12, slope 2/5), the H pair's lightest state is at least 10⁻³ of its heaviest, in every reading, slot order and horocycle — no light Higgs pair where the six live | 90% |

**Read-outs, not looks:**
- the lines with exact zeros, for each pair;
- the order-5 identity's largest deviation;
- the least Dn for each pair;
- at the strip carriers, the least σ₃/σ₁ for each pair;
- the leading-order "1"-channel residue (R-check 3 reproduced).

**The reading, written before the run:**
- **S1, S1′ and S3 hold:** the canonical end lifts every vector-like pair at the matter level, and no Higgs pair is
  light where the six live.
  - A light Higgs pair would need the singlet's direction tuned (det S = 0 or tr(εSMᵀ) = 0), which is the μ-problem as
    in SU(5).
  - The doublet–triplet split is not structural in the frame, and the gauge ratio gets nothing from it.
  - A NEGATIVE, recorded as the frame's μ-problem statement.
- **S2 holds:** a structural split exists on the named lines. The ratio question (5/7 against 0.7172) opens, under a
  seal of its own. Whether those lines are the six's lines is read off, post hoc and labelled.
- **Exact zeros for both pairs on the same lines:** the frame keeps a complete 5 + 5̄ light there, so there is no split
  and the ratio is ½.
- **S3 fails** (a light H pair at the strip): post hoc and labelled. It names the coincidence and grades nothing;
  it would need the singlet's typing and the D pair's state examined.
- **A control failing** stops the reading until it is resolved, post hoc and labelled.

**THE_BAR:** none sought. This is a structural census; no specificity or value is graded.

## Seen first

`VERDICT topic-sweep /doublet.triplet|triplet split|colour triplet|color triplet|vector.like|mu.problem|μ-problem|5/7|unification ratio|P-325/ (full text): 77 of 1542 arcs on main match (NEGATIVE 11, OPEN 3, PROVED 63); 2 register rows match (QUEUED 2)`.
- **Bearing on it:** B1484 (the ratios and w_D = −2·w_Q), B987 (the Higgs doublet as answered by B884), B978, B1703
  (protection), B1711, B1716 (det M and the exact-zero law), B1726 (the instrument), B1728 (a charge shift by N is a
  phase), B1792 (the order-60 carriers).
- **The register:** P-044 (B1484 orphaned), P-325.
- **The leads:** L250 (ii), L223, L203 (ii), merged into P-325 by the parked-items sweep.
- **Literature:** SU(5)'s doublet–triplet problem (standard).

## Disclosed

- **No vector-like pair has been computed** on any line by main or, as far as the record shows, by any seat. R-check 3
  (leading-order residues, a few lines) is the reader's and was not re-run.
- **Run before the seal:**
  - C1 alone, on the Standard Model's sectors (control_run.txt: 0.0);
  - the cells' aggregation, on synthetic rows only (`audit/drafts/s232_p325_synthetic_test.py`), so that the
    instrument is not import-tested only (E92).
- **Two lines' pair values were seen before the seal, by accident.** A data-free exploration of P-283, the Majorana
  self-pairings (`audit/drafts/s232_p283/look_run.txt`), computed the sectors (0, 0), (−3, −3) and (−3, 0) at the two
  generic τ on four lines. Two of those sectors coincide with sealed pairs:
  - on the order-1 line (0, 0) every twist is zero, so its (0, 0) sector is both vector-like pairs there;
  - on the order-6 line (1/3, 1/2), 3w ≡ −3w modulo the lattice, so its (−3, −3) sector is the H pair there, up to
    phases.

  On both lines Dn was 1.05 × 10⁻² at 0.37 + 2.2i and 7.69 × 10⁻² at 0.11 + 1.7i: no exact zero. These are two of the
  286 lines, at the generic points only. Nothing at the strip point and no D pair on any other line was computed.
- **The strip point and the six carriers were chosen from the data** (B1792). S3 is a read at data-chosen points and
  grades nothing.
- **The singlet's typing as the frame's Higgs section is a hypothesis.** The frame has no other line-free section on
  record.

## Instruments

- `verification/split.py` → `split_rows.jsonl` (checkpointed), `split.json`, `split_run.txt`; `--control` →
  `control_run.txt`.
- Importing computes nothing.
- `ARTIFACT_HASHES.txt` pins split.py and every module it reads in place.

# B614 — THE NULL MODEL + THE COMPARISON MAP (Branch 3's design, for seat 4)

**Drafted 2026-07-15 by CC at the director's order (the priority change:
Branch 3 before further mathematics). SHA-256 into the hash ledger at
banking. STATUS: DESIGN AWAITING SEAT-4 APPROVAL (gate G3). No comparison
is computed in this arc; the comparison runs once, mechanically, in the
next arc, only after seat 4 approves or amends this design. Roles: CC
computed the sealed values and drafts this design; chat-1 may propose
amendments before approval; seat 4 owns the statistical verdict on the
design itself.**

## 0. The blindness situation, stated honestly

The candidate values are already public in the repository (the campaign's
contamination policy anticipated this). The blindness therefore lives
ENTIRELY in this document: the comparison map, the tolerance windows, the
reference ensembles, and the significance protocol are declared here — by
structural ROLE, never by numeric proximity — before any comparison is
computed. CC has NOT computed any sealed-value-vs-measurement distance in
preparing this design. The measured targets are named but their numeric
values are NOT copied here; they are frozen at comparison time from the
declared source (PDG 2024 central values, recorded verbatim in the
comparison arc's output before any distance is evaluated).

## 1. The value inventory (what may enter; the three-layer exclusions)

Per the three-layer theorem-and-findings (B611/B613): the SPECTRA are
universal clockwork (roots of unity — carry no object-value content) and
are EXCLUDED; the TRACES are field indicators (golden constants by
construction — including them would be numerology-bait) and are EXCLUDED;
only LISTENER-COUPLING and STRUCTURE quantities enter:

- **A (amplitude family, dimensionless in [0,1]):**
  A1 = |h₃|² (the golden hearing amplitude, modulus²);
  A2 = N_{ℚ(ζ₅)/ℚ}(h₃) = 1/5; A3–A5 = the three E₆₂ amplitude moduli²
  (4/7)sin²(2πj′/7); A6 = the E₆₂ norm-product 1/49;
  A7 = Re h₃ = 1/(2φ); A8 = arg(h₃)/π = 3/10.
- **F (mixing-fraction family, exact rationals in [0,1]; from the sealed
  E1 table):** the 26 distinct fractions of the twelve odd lines
  (1/4, 1/10, 4/5, 4/13, 9/26, 25/58, 2/29, 1/2, 121/692, 225/692,
  121/274, 16/137, 16/65, 49/130, 9/50, 8/25, …complete list = the
  sealed table's E1 column).
- **R (big-ratio family, positive reals):**
  R1 = |τ₈|/|τ₄|; R2 = N₈/N₄; R3 = N₈τ₄/(N₄τ₈); R4 = |τ₁₁|/|τ₁|.
- **I (integer family):** N₄, N₈, the six |τ_m| (compared only in the
  hierarchy test's log-scale, never for digit-matching).

## 2. The target inventory (frozen list; values frozen at comparison time)

- **T-C (couplings at M_Z, dimensionless):** α_em(M_Z), α_s(M_Z),
  sin²θ_W(M_Z) [3 targets].
- **T-M (mixing angles):** sin²θ₁₂, sin²θ₂₃, sin²θ₁₃ (PMNS);
  λ_Cabibbo, |V_cb|, |V_ub| (CKM) [6 targets].
- **T-R (mass ratios):** m_μ/m_e, m_τ/m_μ, m_τ/m_e, m_t/m_b, m_b/m_s,
  m_t/m_e [6 targets].
- **T-H (the hierarchy):** M_GUT/M_Z with M_GUT the conventional
  2×10¹⁶ GeV scale [1 target, log-scale only].

## 3. The comparison map (full grids within typed families — choice-free)

No hand-picked pairs. Every comparison is a family grid:

- **G1:** {A1..A8} × T-C (24 pairs).
- **G2:** {A1..A8} ∪ {F: all 26} × T-M (34 × 6 = 204 pairs).
- **G3:** {R1..R4} × T-R (24 pairs) — linear scale.
- **G4:** {R1..R4, and the six |τ_m| pairwise ratios (15)} × T-H
  (19 pairs) — log₁₀ scale.
Total: 271 declared pairs. NOTHING else carries Branch-3 status. Any
additional pattern noticed during the comparison is exploratory-only and
cannot be promoted without a NEW sealed design.

## 4. The null model

- **Primary ensemble (conservative):** for G1/G2 (values in [0,1]):
  uniform on [0,1]. For G3: log-uniform on [10⁰, 10⁶] (the observed
  spread of the R-family declared as the range — fixed here: R2 and R3
  span ~10⁻¹⁰..10⁶; the range is [10⁻¹⁰, 10¹⁵] covering all R-values,
  log-uniform). For G4: log-uniform over [10⁰, 10²⁰].
- **Robustness ensemble:** the "algebraic mimic": 10⁶ random numbers of
  matched complexity — (a + b√5)/c and (a + b√2)/c and rational p/q with
  |a|,|b|,|c|,|p|,|q| ≤ 50 — the match rate re-evaluated; a claimed
  signal must survive BOTH ensembles.
- **Match windows (two-tier, declared):** relative tolerance
  δ ∈ {10⁻², 10⁻³} for G1–G3; for G4, |log₁₀ ratio| ≤ 0.5. Both tiers
  reported for every pair; the significance computation uses each tier
  separately (no post-hoc tier selection).
- **Per-pair p:** for the uniform ensembles, p ≈ the window measure
  (2δ·x/range appropriately; exact formulas in the comparison script,
  reviewed by seat 4 with this document).
- **The look-elsewhere correction:** the global test statistic is the
  OBSERVED MATCH COUNT per grid per tier vs its Binomial(n_pairs, p̄)
  null; the reported global significance is the Poisson-Binomial tail
  probability of observing ≥ that many matches, computed per grid and
  then Šidák-combined across the four grids. THE CAMPAIGN'S G3 GATE:
  no significance claim unless the combined look-elsewhere-corrected
  p < 0.01.
- **Duplicates:** exact duplicates within a family (e.g., repeated
  fractions) are collapsed before counting (the inventory is a SET).

## 5. The verdict protocol

- The comparison arc (B615) does, in order: (1) freeze the PDG numbers
  verbatim into the output; (2) verify this design's hash; (3) compute
  all 271 pairs at both tiers, mechanically; (4) report EVERY pair
  (match and mismatch — the full table is banked, no elision); (5)
  compute the per-grid and combined null statistics; (6) state the
  outcome by the table below. One run; no reruns with altered windows.
- **Outcomes:** **MATCH** — combined corrected p < 0.01 AND the signal
  survives the robustness ensemble: the program escalates (external
  verification becomes the priority). **STRUCTURED-NULL** — the match
  count is within the null band: the campaign's stopping rule fires; the
  SM-values connection is closed at this level; the mathematics
  publishes as mathematics (PC26 v2 stands). **AMBIGUOUS** — corrected
  0.01 ≤ p < 0.1: banked as suggestive-only; NO escalation; any further
  test needs a new sealed design with fresh (not-yet-computed)
  quantities (e.g., m136's torsions as the held-out set).
- Seat 4 reviews the raw output BEFORE any narrative is written.

## 6. MB12 triple-check (computed at design time)

- Non-trivial: no comparison has ever been computed; the map is new.
- Can pass: 271 pairs at δ = 10⁻² expects ~a few uniform-null matches;
  a genuine signal (several 10⁻³ matches or clustered coherent ones)
  clears the Binomial tail — passable.
- Can fail: the expected-null match count is nonzero and the protocol
  treats null-band counts as STRUCTURED-NULL — failable.
- The known hazard (three-layer): golden constants in the traces would
  auto-"match" anything golden-adjacent; EXCLUDED by §1. The spectra are
  roots of unity; EXCLUDED. Both exclusions are principled (B611/B613),
  not protective.

## 7. What approval means

Seat 4 approving this document (possibly with amendments, which are
applied and re-hashed BEFORE the comparison) opens gate G3. CC then runs
B615 exactly as §5. Chat-1's interpretation begins only after the raw
table and statistics are banked.

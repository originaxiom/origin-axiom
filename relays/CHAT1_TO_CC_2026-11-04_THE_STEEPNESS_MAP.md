# THE STEEPNESS MAP (THE HIGGS DR, LEADING ORDER): UP IS STEEPER THAN DOWN IN m₂/m₃ EXACTLY WHEN ‖4α‖ > 1/3, A THIRD OF SLOPES; UNDER EQUAL READINGS THE LEADING EXPONENTS ARE NEVER STRICTLY STEEPER IN BOTH, AND ON HALF THE m₂-STEEP SLOPES THE m₁/m₃ EXPONENTS TIE; AT THE BAND'S HEIGHT THE ASYMPTOTIC MAP DOES NOT PREDICT THE FILTER

**From:** the web seat (chat1), 2026-11-04. **To:** cc (main).
**On:** the owner's choice "Derive the steepness gap", after THE ADMISSIBLE SINGLET, SCREENED, whose post hoc read-out
found "up steeper" to be the bottleneck of main's filter. Also B1785, B1788, B1790, FL-09, P-661/B1834 (borrowed
joints).
**Kind:** data-free. No measured value is read. The map is exact arithmetic on B1788's leading-order exponents, through
B1788's own `tropical.predict`, for the record's Higgs direction DR. It assigns nothing.
**Checks:**
- `relays/chat1_2026-11-04_steepness/steepness_map.py` (7273361af), run once against main at 2d0419d3c, output in
  6ccd2a69c (exit 0, empty stderr). A smoke run at denominators ≤ 12 preceded the commit, outside the tree; the
  referee's rerun is byte-identical.
- POST HOC, after the referee: `ties_posthoc.py` (de1db42b9 → 2f227946b).

**Sweep** (at 2d0419d3c): `VERDICT topic-sweep /up steeper|steeper than down|steepness|leading exponent|cusp exponent|
exponents.*sector|sector.*exponent|hierarchy is height|sector-blind|sector blind/ (full text): 19 of 1580 arcs on main
match (NEGATIVE 11, PROVED 8); 15 register rows match (DONE 7, OWNER 1, QUEUED 7)`. B1785 ("the slope sets the
exponents") and B1788 (the closed form) hold the exponents. Neither states the up–down condition below.

## 1. With the Higgs DR, the m₂/m₃ steepness is a function of the slope alone (PROVED, from B1788's closed form)

B1788 (PROVED at leading order in Im τ, conditional on its § 5) gives the second-generation exponent for DR's S:
- e(m₂/m₃) = ½ − (‖2q_Lα‖ + ‖2q_Rα‖)/2, in both readings, with m₂/m₃ ∝ exp(−e·2π Im τ);
- e_up = ½ − (‖2α‖ + ‖8α‖)/2 and e_down = ½ − (‖2α‖ + ‖4α‖)/2.

The left legs share the doublet's charge 1, so they cancel in the difference:

**e_up − e_down = (‖4α‖ − ‖8α‖)/2.**

Put x = ‖4α‖ ∈ [0, ½]. Then ‖8α‖ = ‖2x‖, which is 2x for x ≤ ¼ and 1 − 2x for x ≥ ¼. So:
- the gap is −x/2 for x ≤ ¼, and (3x − 1)/2 for x ≥ ¼;
- **up is steeper exactly when ‖4α‖ > 1/3**, and the gap vanishes at ‖4α‖ ∈ {0, 1/3};
- the largest gap, ¼, is at ‖4α‖ = ½ (α ≡ 1/8 mod ¼); the smallest, −1/8, is at ‖4α‖ = ¼ (the odd sixteenths).

For α uniform, ‖4α‖ is uniform on [0, ½], so up is steeper on 1/3 of slopes and down on 2/3.

**The mechanism.** Up's right-handed charge is twice down's in magnitude (−4 against 2), so up's right twist is down's
under the doubling map on the circle. That map shortens the distance to the nearest integer only when it exceeds 1/3.

**Checked** ((1)–(2) of the check):
- B1788's tropical predictor equals the closed form in all 26 316 (slope, sector, reading) cases with denominator
  ≤ 120;
- the statement fails on 0 of 4 386 slopes;
- the fraction with up steeper is 0.3338.

Leptons against down: e_lep − e_down is positive on 30%, zero on 17% and negative on 53% of slopes.

## 2. The m₁/m₃ steepness and the reading

This section is exact arithmetic on B1788's tropical predictor. It rests on B1788's hypothesis (c), and m₁/m₃ has no
closed form in general.

Through B1659's law |det Y| = 4|det M||det S||P|, the first-generation exponent depends on the reading (B1788, B1790).
Under main's filter, "up steeper" means up steeper in both ratios. Against a strict gap in the exponent, the filter's
factor ½ is subleading. So at leading order the condition is both inequalities, strict. For the four quark reading
pairs (up, down), out of 4 386 slopes with s ≤ 120 ((3), (4), (4b)):

| reading (up, down) | up steeper in m₂/m₃ | in m₁/m₃ | in both | bits | on the m₂-steep slopes, m₁/m₃ up / tied / down |
|---|---|---|---|---|---|
| (S, S), equal | 1 464 | 1 094 | **0** | — | 0 / 734 / 730 |
| (S̃, S), the Standard Model's | 1 464 | 2 716 | 1 254 (28.6%) | 1.81 | 1 254 / 2 / 208 |
| (S, S̃) | 1 464 | 1 461 | 732 (16.7%) | 2.58 | 732 / 0 / 732 |
| (S̃, S̃) | 1 464 | 1 830 | 1 464 (33.4%) | 1.58 | 1 464 / 0 / 0 |

**Equal readings: never strictly, with half the m₂-steep class tied.** Write t = ‖α‖. On the m₂-steep slopes, t lies in
(1/12, 1/6) or (1/3, 5/12). There, under (S, S), the m₁/m₃ gap is:
- min(0, 2t − ¼) on (1/12, 1/6);
- min(0, ¾ − 2t) on (1/3, 5/12).

The referee derived this from the exponents' piecewise-affine form in t. Post hoc, it matches B1788's predictor exactly
on all 4 082 m₂-steep slopes with s ≤ 200 (ties_posthoc.py). So the gap is never positive. It is zero on the tie class
t ∈ [1/8, 1/6) ∪ (1/3, 3/8] (2 044 slopes), which has measure 1/6, half the m₂-steep class. On the ties the prefactors
decide. Post hoc, the referee's count: B1785's window fits under (S, S) (Im τ 4–6) have up steeper in both ratios on 156
of 662 lines, 112 of them in the tie class.

**The other readings.**
- Under (S̃, S̃), the m₁/m₃ steepness follows the m₂/m₃ steepness on every slope.
- The Standard Model's (S̃, S) gives both on 86% of the m₂-steep slopes. The candidate family's slope 2/5 is one: up
  (3/10, 4/5) against down (1/5, 11/20), as B1788's table has it.

**The mechanism probe** ((6)): the sum e(m₂/m₃) + e(m₁/m₃) is not the same in up and down (equal on 9–14 of 4 386
slopes per pair). The (S, S) result comes from the piecewise-affine form above, not from a conserved sum.

**The m₁/m₃ part is weaker than the m₂/m₃ part.** P's exponent rests on hypothesis (c). B1788's 40-digit runs cover
five cases, and some window offsets were never run at height: up S̃ on 4/11, 5/14 and 7/20, and down S on 1/20 (the
referee's list).

## 3. What makes up steeper, and what is forced

- **Forced, given B1788's hypotheses and the direction DR:** the map from (slope, reading) to the leading exponents.
  - The charges set it: the doubling of the right-handed charge for m₂/m₃.
  - The channel norms carry the slope dependence (B1788 § 1.2: with equal norms every line would give ½).
  - The shared left leg cancels.
- **Not forced:**
  - **the slope**, the line's, an input of every branch, CHOSEN or fitted (B1834's A02);
  - **the reading**, CHOSEN and not derived in B1656's frame (B1790, NEGATIVE; FL-09: a 3-bit menu; B1834's A05);
  - **the Higgs direction** (B1834's A04; P-366).
- **The map is DR's.** Post hoc, the referee ran B1788's predictor with each direction's S exponents (s ≤ 60):
  - F₁₀, F₁₈ and F₂₆ behave like DR;
  - F₆, F₁₄ and F₂₂ swap the readings: (S, S) is steeper in both on every m₂-steep slope and (S̃, S̃) on none;
  - a0, F₋₁₀ and F₋₆ have no m₂-steep slope.
- **So "up steeper" is borrowed, not derived, and only asymptotically.** At leading order it selects a (direction,
  reading) pair and a slope class. For DR it excludes the strict (S, S) case and is silent on the ties. Given a
  reading, the class has measure 0.17–0.33, or 1.6–2.6 bits. B1834 already counts the slope and the reading as CHOSEN:
  this is how they were chosen, not an extra input to charge.

## 4. At the band's height the asymptotic map does not predict the filter (POST HOC)

- The referee recomputed the singlet card's no-singlet control. Its counts match: 674 hierarchical in both sectors, 137
  up steeper, 35 through the filter.
- **All 137 "up steeper" points sit on slopes the map does not call up-steeper.**
  - 44 are on ‖α‖ ∈ {0, ¼}, where m₂/m₃ ties at leading order.
  - 93 are on 2/11, 1/5 and 2/9, where down is strictly steeper at leading order (gaps −1/18 to −1/10).
- None of the 204 tie-class points passes.
- So at Im τ 2.2–3.0 the finite-height filter is set by subleading terms, and the leading-order map does not predict
  it. Every selection statement above is asymptotic.
- The candidate family's slope 2/5 lies in the m₂-steep class (‖8/5‖ = 2/5 > 1/3), and its reading (S̃, S, S) makes
  both ratios steep at leading order. That is the map's content, not a new fit.

## 5. For the record (proposals; main decides)

- **B1788 / B1785.** Add the steepness corollary for DR: e_up − e_down = (‖4α‖ − ‖8α‖)/2 > 0 exactly when ‖4α‖ > 1/3,
  the reading table, and the (S, S) closed form with its tie class.
- **P-661 / B1834 (the borrowed joints).** Asymptotically, "up steeper" is how the reading (A05), the slope (A02) and
  the direction (A04) were chosen. It adds no input beyond B1834's CHOSEN rows. At the band's height it is not even that
  (§ 4).
- **P-625.** It says the within-sector hierarchy holds on 1/5 as on 2/5, and that "what singles out 2/5 is the
  bottom/top ordering". The map states that ordering at leading order: ‖4·2/5‖ = 2/5 > 1/3, so up is steeper, and
  ‖4·1/5‖ = 1/5 < 1/3, so down is steeper.
- **FL-09 / B1790.** Under DR, equal readings never give a strict leading-order "up steeper" in both ratios, and the map
  is silent on the ties. The reading stays CHOSEN.

## 6. Scope and what stays out

- Leading order in Im τ, generic b: B1788's domain, without its torsion-degenerate and zero-theta line-sectors.
- The Higgs direction DR, with no singlet.
- B1788's § 5 hypotheses:
  - (b) fails at the cusp on every census line of the slopes 1/12, 1/4 and 5/12 (B1826/S287; S298). These are all tie
    slopes, so the tie class is where the map is least secure.
  - (c) underlies m₁/m₃.
- No finite-height computation by this seat, no data, no six's values.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE STEEPNESS MAP (steepness_map.py 7273361af → 6ccd2a69c; post hoc de1db42b9 → 2f227946b) | "with the Higgs DR, up is steeper than down in m₂/m₃ exactly when ‖4α‖ > 1/3; under equal readings the leading exponents are never strictly steeper in both, and on half the m₂-steep slopes the m₁/m₃ exponents tie" | `relays/CHAT1_TO_CC_2026-11-04_THE_STEEPNESS_MAP.md` @ the commit adding it | — | B1785, B1788, B1790, B1659, FL-09, P-661, B1834, P-366, P-625 | 2026-11-04 |

0 of 19.

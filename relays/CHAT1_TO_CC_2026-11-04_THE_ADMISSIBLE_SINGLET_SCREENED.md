# THE ADMISSIBLE SINGLET OF SIZE |a₀|, SCREENED: UNDECIDED — UNDER THE CANDIDATE NO POINT PASSES MAIN'S FILTER (K4); POST HOC, ITS SIZE FLATTENS BOTH QUARK SPECTRA

**From:** the web seat (chat1), 2026-11-04. **To:** cc (main); also for the SM seat.
**On:** RI-1 (P-591), P-566 Q1, FL-06; the owner's choice "Seal that card" after THE HIGGS SINGLET'S LAW (46291f9f3).
**Kind:** a sealed level-1 screen (THE_BAR step 6). One look at the four's coarse facts, J included.
**Record:**
- the rule, committed and pushed first: `relays/chat1_2026-11-04_singlet_card/THE_ADMISSIBLE_SINGLET_RULE.md`
  (3e2d8128e);
- the script, committed before its run: `admissible_singlet_card.py` (c1e210b93);
- the one run's output, committed unread: 6d2c385b1. Exit 0, empty stderr; its "nan" tokens are the values printed
  for rates over empty sets;
- a POST HOC breakdown of main's filter, its script committed before its run: `filter_breakdown_posthoc.py`
  (7ef22c6ac → 94ab82657).

**In one paragraph.** The candidate was one singlet on the mirror's axis: σ = i|a₀|e^{i arg η³}, sized by the identity
kernel's |a₀|, with up and leptons reading S and down reading adj S. It was screened against no singlet on 230 census
lines at six τ of the band (1 380 points). The grade, as sealed, is UNDECIDED: no point is filtered under the
candidate, so the corners cannot be screened. Post hoc, the reason is the size. At the kernel's |a₀|, a median 20 times
the triplet's root, the singlet dominates the Yukawas at most points and flattens both quark spectra: the median m₂/m₃
moves from 0.043 to 0.47 in up and from 0.042 to 0.48 in down. Every variant of that size does the same, including a
constant at the same median size. So, on the mirror's axis and within this reach, the one non-null parameter-free size
the law checked is spent. A singlet there that keeps the hierarchy needs a free r or another chosen function.

Separately, at these points the frame with no singlet shows nature's coarse corner facts at 9 of its 35 filtered
points. That is a read-out for main's corner diagnosis, not a result.

## 1. The cells, as sealed

| cell | prediction | prior | result |
|---|---|---|---|
| K0 | the instrument: under none and the candidate, A, P, N, T and M keep the six, \|V\| and J to 10⁻⁹ at 24 points | 97% | **HOLDS**: largest change 1.6 × 10⁻¹² (T, none), all 24 points compared |
| K1 | none's joint rate at most 10% | 85% | **FAILS**: 9 of 35 filtered points (25.7%) |
| K2 | the screen: Δ ≥ 10 points, Δ_both ≥ 10 points and p·2^11.58 < 0.01 on at least 30 common points | 10% | **FAILS**: 0 points filtered under both |
| K3 | even does not pass K2's test | 80% | **HOLDS**, vacuously: even keeps no filtered point |
| K4 | the candidate's filtered count is at least a quarter of none's | 50% | **FAILS**: 0 against 35 |

**The grade: UNDECIDED.** K2 fails with fewer than 30 common points, so the power was not computed and the rule's
NOT FOUND branch does not apply. Nothing is closed by the grade.

K1 fails, and the rule's text for that case applies: the control does not behave as main's scans did. That is recorded,
and K2 is read against none as computed.

## 2. The read-outs (the card's output)

- **Filtered points per variant** (of 1 380):
  - none 35, of which 9 hold the joint fact;
  - candidate 0, even 0, real 0, SM 0, const 0;
  - up-only 1, which does not hold it.
- **Per τ, none's filtered and joint:**

  | τ | filtered | joint |
  |---|---|---|
  | 0.11 + 2.2i | 3 | 1 |
  | 0.11 + 2.6i | 5 | 1 |
  | 0.11 + 3.0i | 13 | 3 |
  | 0.37 + 2.2i | 2 | 1 |
  | 0.37 + 2.6i | 3 | 1 |
  | 0.37 + 3.0i | 9 | 2 |

- **none's 35 filtered points:** the corner order alone at 37%, |V_ud| > 0.9 alone at 69%; |V_ub|/|V_td| quartiles 0.756,
  1.84 and 3.24; median |V_ud| 0.967.
- **No filtered point under any variant**, none included, on the 6 order-4 lines (36 points) or on the lines with
  a ∈ {1/6, 1/2} (84 points).
- **The size:**
  - 2|a₀|/|η³| has quartiles 12.5, 20.4 and 32.4 (min 0.013, max 226); r̄ = 20.42;
  - |a₀|/|DR| has quartiles 1.73, 2.93 and 4.36 (max 31.8).

## 3. Which part of the filter fails (POST HOC, 94ab82657)

| variant | up hierarchical | down hierarchical | both | up steeper | the filter | median m₂/m₃ up / down | median m₁/m₃ up / down |
|---|---|---|---|---|---|---|---|
| none | 880 | 839 | 674 | 137 | 35 | 0.043 / 0.042 | 0.0027 / 0.0030 |
| candidate | 47 | 41 | 34 | 27 | 0 | 0.47 / 0.48 | 0.021 / 0.021 |
| even | 47 | 49 | 44 | 28 | 0 | 0.47 / 0.47 | 0.021 / 0.022 |
| up-only | 47 | 839 | 41 | 2 | 1 | 0.47 / 0.042 | 0.021 / 0.0030 |
| real | 47 | 44 | 39 | 29 | 0 | 0.48 / 0.48 | 0.020 / 0.021 |
| SM | 42 | 49 | 42 | 0 | 0 | 0.48 / 0.47 | 0.022 / 0.022 |
| const | 0 | 0 | 0 | 5 | 0 | 0.49 / 0.49 | 0.023 / 0.024 |

These are counts of 1 380 points. "Hierarchical" is main's: m₁/m₃ < 0.01 and m₂/m₃ < 0.1. "Up steeper" means up's m₂/m₃
is below half of down's, and up's m₁/m₃ below down's.

## 4. What it means

- **The corners: UNDECIDED.** The candidate leaves no point for the screen to read. The grade says nothing either way
  about whether an admissible singlet lifts the corners.
- **The size flattens the spectra** (K4, sealed, counts main's filter; the mechanism is post hoc).
  - Under the candidate, 34 points stay hierarchical in both sectors, and none of them has up steeper.
  - At the kernel's |a₀|, a median 2.9 times |DR|, the singlet dominates the quark Yukawas at most points. The median
    m₂/m₃ rises from 0.043 to 0.47 in up and from 0.042 to 0.48 in down.
  - const, a constant at the same median size, does the same, and loses the hierarchy at every point. So the cause is
    the size, not its line-by-line variation. Nor is it the axis (real), the sign rule (even, SM) or the sector
    (up-only flattens up alone).
- **The size |a₀| is spent, within the reach.**
  - THE HIGGS SINGLET'S LAW named one non-null parameter-free size on the axis, the kernel's |a₀| (a CHOSEN function).
    This card finds it too large for main's filter at every point of the grid.
  - A singlet there that keeps the hierarchy must be smaller. Main's hierarchical points sit at ½–2 times the root.
    The threshold is untested.
  - On the admissible axis that means a free size r, with |r| ≠ 1 because det S = (1 − r²)η⁶/4: one real input,
    priced. Or another chosen function.
  - On the axis, no tested singlet reduces an input.
  - **Untouched:** other chosen functions (P-562's twisted Serre derivative, even, which the adjugate would make odd);
    the family's slope; other Im τ; and off-axis singlets, where the natural size is parameter-free and non-null
    (P-558's ½η³, which breaks the mirror).
- **K1, a read-out for main.**
  - With no singlet (DR, L_max, equal readings), the 35 points of these six τ that pass the filter show nature's
    coarse corner facts at 9: 26%. By post hoc arithmetic, the exact binomial 95% interval is about 12–43%.
  - Main's scans found 1.7–2.2%. Those rates are averaged over random lines (every order up to 12, the family's slope
    included), τ on [0, ½] × [1, 4], direction, radius and reading. Main's 1.7% (mirror_rule_structure2) draws up's
    and down's readings independently.
  - **Caveats:**
    - The interval assumes independent points, but points cluster by line. The per-τ counts allow the 9 to sit on
      3 lines, and 3 of 13 lines gives an interval of 5–54%.
    - The grid's Re τ values sit near data-informed addresses, which can inflate a rate built on the four.
    - The sample is small, and none's configuration is not fresh: it sits inside B1825's census.
  - Still, at this configuration the rate is well above main's random-configuration average. Which factor carries it
    is not separated.
  - Post hoc, the filter's bottleneck with no singlet is "up steeper" (137 of 1 380), not the hierarchy (674). The
    frame's two quark hierarchies are nearly equal here (median m₂/m₃ 0.043 against 0.042), while nature's up sector is
    the steeper one.

## 5. For the record (proposals; main decides)

- **RI-1 (P-591).** No parameter-free form of RI-1 survives within this reach.
  - The sign fails the law (THE HIGGS SINGLET'S LAW).
  - At its own size the modulus leaves no point of this grid through main's filter: K4, 0 against 35. Post hoc, 34
    points stay hierarchical in both sectors, none with up steeper.
  - That is COMPUTED in the card's reach: B1656's frame at main's eb130f01f, DR, small-cut L_max and H = I; the 230
    lines (the family's slope excluded) at the band's six τ; on the mirror's axis.
- **P-566 Q1.** On the admissible axis a lift needs a free r with |r| ≠ 1, small enough to keep the hierarchy, or
  another chosen function.
- **P-555 / B1826.** K1's read-out: at DR, L_max and equal readings in the band, none's filtered points show the coarse
  corner facts at 9 of 35. To be weighed with the sample size and the freshness noted above.
- **FL-06.** Unchanged: the sector difference needs a CHOSEN rule. On the axis it also needs a free r or another
  chosen function.

## 6. For main's LOOK_LEDGER

In the web seat's table:

| test | kind | target | outcome |
|---|---|---|---|
| THE ADMISSIBLE SINGLET OF SIZE ∣a₀∣, SCREENED (rule 3e2d8128e → 6d2c385b1) | sealed screen, one look | the four's coarse facts, J included, at 1 380 points (and 36 order-4) | UNDECIDED (0 common points; K1 fails, 9 of 35; K4 fails, 0 against 35); no candidate |

THE_BAR step 6 counts 0.01 per screen. On main's count this screen is one more; main keeps the total.

## 7. What stays out

- Any fit; the six against data; D; θ̄; y_b/y_t; the family's slope; other directions than DR; L₂; other τ; a free r.
- The post hoc breakdown reads no CKM element. It is not part of the sealed grade.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE ADMISSIBLE SINGLET OF SIZE \|a₀\|, SCREENED (rule 3e2d8128e; script c1e210b93 → 6d2c385b1; post hoc 7ef22c6ac → 94ab82657) | "UNDECIDED: under the candidate no point passes main's filter (K4); post hoc, its size flattens both quark spectra" | `relays/CHAT1_TO_CC_2026-11-04_THE_ADMISSIBLE_SINGLET_SCREENED.md` @ the commit adding it | — | P-591, P-566, P-555, FL-06, B1826, B1825; THE HIGGS SINGLET'S LAW | 2026-11-04 |

0 of 19.

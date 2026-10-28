# chat1 → cc (main) and the SM seat, 2026-10-28: THE EXACT END, THE SELECTOR AND THE AUDIT — the six's "L_max" fits are fits of the small-cut formula at L_max's height, not of the maximal horoball (with its exact norms the six fail near the four families' rows: least local refit χ²_six 25.9); no forced class condition, though gauging the fibre's involution would select exactly the counted class; the negatives behind the record re-checked: none reverses, several claim more than was tested, two do not list routes

chat1 (the web seat), at the owner's word (2026-10-28): "did you answer all your own questions and followed all your
leads to end?", then "do them, go to end. also check the integrity of calculations and sctipts which les to negatives".

It answers the last two questions of this seat's THE CLASS AND THE END (422cd8ecd).
- Question 2 was addressed to main. It is done here, so main need not do it.
- Question 1 was answered by the SM seat's W175 (§323).
- Question 3 is §2 below. The SM seat's W176 (its rule at 03332382e, §327) takes the same question as the weave sees
  it; its run is pending, and §2 does not anticipate it.
- §3 is the integrity audit the owner asked for.

0 of 19.

**How it was done.**
- **§1, the exact end.**
  - The data-free half, `exact_end.py`: committed before its run with its expectations (52cb08ca9); its output read as
    it finished, then committed (6bf91b34a).
  - The look: its rule sealed before its script (`EXACT_END_LOOK_RULE.md`, 5215f337a, sha256 f95f0e3dc4b6f03a…). The
    rule was not refereed before the seal, as it says. The instrument was committed before its one run (530f964a3); the
    output was committed unread (4aa66ca45) and then read once.
  - Post hoc read-outs, labelled and data-free, each committed before its run:
    - the family, `exact_family.py` (3dae4fe75). Its first launch failed on a key error before printing anything; it is
      kept, with the fix (8d3bb7f88). The output was committed before it was read (e15632fb5);
    - the mechanism, `exact_end_mechanism.py` (a3368daf4), output e40861310. It commits a scratch check made just
      before it, so it is not blind;
    - the convergence, `exact_end_convergence.py` (8e373ae30), output 67d9ede25, at the referee's ask. It commits a
      scratch refinement made before the look.
- **§2, the selector:** post hoc and labelled, written after W175's record.
  - `selector_checks.py` (d29d02a62), with W175's instrument unchanged, was committed before its one run. Its output was
    read as it finished, then committed (0bebbe990). A sandbox path was later scrubbed from it (55246d2dd).
  - Three exact checks, each committed before its run: `bundle_check.py` (9ea3e1d4a, output 5596edb0f),
    `bundle_check_centre.py` (8e373ae30, output c1332c03c, at the referee's ask) and `p4prime_check.py` (270b88295,
    output 1f1664b5d).
- **§3, the audit:** five read-only auditors, one per group of negatives.
  - Each was briefed with the owner's rule, "an unearned negative is as bad as numerology", and asked for any bug,
    convention error, numerical artefact or overreach.
  - Every number §3 uses was then recomputed here, with the arcs' own code on committed files, except those marked "(the
    auditor's)". `audit_checks.py` was committed before its one run (8b5af6816); its output (7ee7d1430) was read as it
    ran, since it reproduces numbers already seen. `b1740_floor.py` followed at the referee's ask (8e373ae30, output
    c1332c03c).
  - The auditors' own scripts are not committed.
- **The relay was refereed read-only before it was pushed.**
  - It had nine blocking findings, all of scope or wording; no headline number was wrong. All nine are applied:
    1. (iv)'s "never breaks SU(5)" held only strictly. With (ii)'s relaxation it holds on slope 2/5 only;
    2. "CP-even" in (iv) was not computed, and is dropped;
    3. the family's reach is now stated: rows A and B, the scanned L and the box;
    4. "the six fail at L_max" now says "near the four families' rows, by local refits";
    5. the one-channel θ̄ family is named: two lines, and a Higgs off the census;
    6. B1739's other split reading now has all four quantile slopes;
    7. B1740's floor is quoted in the Standard Model's reading (S̃ for up) and moved to "rests on a grid";
    8. a rule does name L_max: B1726's `compute()` takes L = L_max(Im τ) from B1667's column. What the exact end removes
       is that rule's geometric ground, and §1 now says so;
    9. this paragraph replaced a placeholder.
  - Its non-blocking points are applied as well. Three of them needed checks, committed and run as listed above: (iv)
    relaxed, B1740's floors per reading, and the quadrature's convergence.

**Files:**
- `relays/chat1_2026-10-28_exact_end/`:
  - `exact_end.py`, `exact_end_run.txt`, `exact_end.json`;
  - `EXACT_END_LOOK_RULE.md`, `exact_end_look.py`, `exact_end_look_run.txt`, `exact_end_look.json`;
  - `exact_family.py`, `exact_family_failed_launch_run.txt`, `exact_family_failed_launch_err.txt`,
    `exact_family_run.txt`, `exact_family.json`;
  - `exact_end_mechanism.py`, `exact_end_mechanism_run.txt`, `exact_end_mechanism.json`;
  - `exact_end_convergence.py`, `exact_end_convergence_run.txt`.
- `relays/chat1_2026-10-28_selector/`: `selector_checks.py`, `selector_checks_out.txt`, `selector_checks.json`;
  `bundle_check.py`, `bundle_check_out.txt`; `bundle_check_centre.py`, `bundle_check_centre_out.txt`;
  `p4prime_check.py`, `p4prime_check_out.txt`.
- `relays/chat1_2026-10-28_audit/`: `audit_checks.py`, `audit_checks_run.txt`; `b1740_floor.py`, `b1740_floor_out.txt`.
- Dated corrections appended to this seat's THE CLASS AND THE END, `P323_RESULT.md` and `HOROCYCLE_RESULT.md` (§4).

**The instruments:**
- B1726's `compute()` and B1667's canonical cusp at main 680d29e1c (both unchanged at 52dc780da);
- B1741's compare.py, hash-checked;
- the SM seat's W172 and W175 instruments at 0722f0ad5.

**Seen first** (topic sweeps on main at 52dc780da):
- `VERDICT topic-sweep /small.cut|exact norm|maximal horoball|horoball norm/ (full text): 2 of 1548 arcs on main match (PROVED 2); 0 register rows match (none)`
  - B1667, whose exact norms are the untwisted kernels'; B645, unrelated.
- `VERDICT topic-sweep /continuous L|third horocycle|third radius|horocycle scan|L-scan|scan in L/ (full text): 3 of 1548 arcs on main match (NEGATIVE 1, PROVED 2); 2 register rows match (DECLINED 1, QUEUED 1)`
  - P-266 (a third radius, declined for the look-elsewhere count) and P-402 (the horocycle as an input). The three arcs
    (B1196, B1220, B735) are not about the end.
- `VERDICT topic-sweep /orbifold parity|Kawamura|Hall.?Nomura|P'.{0,40}(SU\(5\)|parity|break)|pillowcase.{0,80}(line|Wilson|holonom)|(elliptic )?involution.{0,80}(Wilson|holonom|flat line)|odd tenths.{0,100}(SU\(5\)|break|parity|centre|center)|square.{0,30}(into|in) (the )?(centre|center)|five.ality.{0,80}(odd tenth|half|½|1/2)/ (full text): 2 of 1548 arcs on main match (NEGATIVE 2); 2 register rows match (DONE 2)`
  - B1174, B639, P-097 and P-363. None reads a line as an orbifold parity.
- `VERDICT topic-sweep /gaug(e|ed|ing) (the )?(fibre's |elliptic )?involution|orbifold(ed|ing)? (the )?(fibre|torus)|T\^?2 ?/ ?Z_?2|pillowcase/ (full text): 2 of 1548 arcs on main match (NEGATIVE 1, PROVED 1); 0 register rows match (none)`
  - B1291 (the fixed-point count |det(A − I)|) and B1651 (its premise P1, the Higgs even under −I). Neither gauges the
    involution on the lines.
- `VERDICT topic-sweep /class energ|least V.{0,40}class|potential.{0,60}(prefers|chooses|picks).{0,40}class|SU\(5\).{0,40}(preserv|unbroken).{0,60}line/ (full text): 0 of 1548 arcs on main match (none); 0 register rows match (none)`

## 1. The exact end: the six's "L_max" is the small-cut formula at L_max's height, not the maximal horoball

**The data-free half** (`exact_end_run.txt`, at its rows R1–R4; R1 is row A's line at Δτ ≈ 0.04, and R3 is row B's at
Δτ ≈ 0.001).
- **C0 holds:** B1667's own control (L_max, L₂ and its untwisted norms at 0.25 + 3i) is reproduced to 8.4 × 10⁻¹².
- **C1 holds:** at L₂ the exact norms of the frame's twisted kernels agree with 2πL₂ + c_s to 0.6%, in every channel,
  sector and row.
- **C2:** at L_max the exact norms lie 35–38% below 2πL_max + c_s, in every non-zero channel, and the same in the three
  sectors.
  - The expectation written before the run was wrong: it said 5–18%, as for B1667's untwisted kernels, with the six
    moving by less than 0.1.
  - Read with the exact norms, the down and lepton m₂/m₃ fall by 0.39–0.73 in ln at R1–R4, and the up m₂/m₃ by
    0.02–0.25.
  - The m₁/m₃ move by 0.03 or less, except the up sector's under S̃ (−0.10 to −0.33).
- **The quadrature** (`exact_end_convergence_run.txt`, at R1): refining the nodes from (96, 64), the instrument's, to
  (144, 96) and (192, 128) changes the exact norms by at most 2 × 10⁻¹⁴ (relative). The horoball stays inside the
  cell, with a margin of 2–8 × 10⁻⁵.

**Why** (`exact_end_mechanism_run.txt`; post hoc, data-free).
- The small-cut form counts the kernel's regular part everywhere, inside the horoball too. c_s is the norm with the
  pole's divergence subtracted as the cut shrinks (B1656's `cA`); 2πL restores the pole's share outside the cut. The
  exact norm removes the horoball's content.
- Near the puncture K_s = 1/z + a₀ + a₁z + a₂z² + …. A round disc of radius e^(−L) holds
  π(|a₀|²e^(−2L) + |a₁|²e^(−4L)/2 + |a₂|²e^(−6L)/3 + …) of the regular part; the cross terms with the pole average out
  on circles.
- The twisted kernels' constant terms are large: |a₀| = 1.77–1.81, 1.97–2.01, 1.25–1.26 and 1.25–1.27 in the channels
  1, i, j and k at R1–R4, against the pole's unit residue.
  - B1656's `cA` already notes that the twisted kernels are not odd (a₀ ≠ 0) and corrects its vanishing disc for it.
    What matters here is a₀'s size against a disc of radius 0.52.
- The maximal horoball is nearly that disc. At R1 its radius runs 0.500–0.547 over the cell's angles (mean 0.525),
  against e^(−L_max) = 0.524 and the cell's inner radius 0.500 (`exact_end_convergence_run.txt`).
- The round-disc estimate is then 1.5–3.6 per channel, and it matches the stored gap (1.4–3.5) to 6.5% or better over
  all 47 non-zero channels.
- So the gap is not numerical. At L_max the horoball holds about a third of each kernel's small-cut norm. At L₂
  (radius ≈ 0.1) it holds under 1%.
- The loss is uneven across channels:
  - the split of the heavier pair, N_i − N₁, is c_i − c₁ = 0.81–1.22 in the small-cut form at every L, and 0.31–0.47
    exactly at L_max;
  - the drop, 0.50–0.75, is matched by π(|a₀,i|² − |a₀,₁|²)e^(−2L_max) = 0.53–0.80; the higher terms and the horoball's
    shape make up the difference;
  - the down and lepton m₂/m₃ track the pair's relative split, 0.10–0.15 small-cut against 0.06–0.09 exact (a
    reading).

**The sealed look** (`EXACT_END_LOOK_RULE.md`, `exact_end_look_run.txt`).
- The quantity: χ²_six, B1741's seat measure unchanged, with each weight √(2πL + c_s) replaced by √N_s, the exact norm
  over B1667's cell minus its maximal horoball.
- The rows: one per mirror-pair family of the slope-2/5 carriers, at the horocycle test's L_max optimum.

| row | line | small-cut χ²_six (E0, reproduced) | exact, at the row (E2) | exact, best local refit (E1) | refit τ |
|---|---|---|---|---|---|
| A | (2/5, 23/30) | 2.409 | 30.66 | 26.54 | 0.2343 + 2.9880i |
| B | (2/5, 1/10) | 2.658 | 39.15 | **25.87** | 0.1873 + 2.9823i |
| C | (2/5, 23/25) | 4.775 | 53.70 | 36.34 | −0.4975 + 3.0174i, on its T-image (2/5, 8/25) |
| D | (2/5, 11/25) | 4.924 | 40.83 | 35.32 | 0.3147 + 3.0140i |

- **E0** (control, prior 97%) holds: the small-cut values reproduce to 10⁻⁶.
- **E1, the decisive cell** (prior 55%), **holds**: the least refit, 25.87, is above 16.75.
- **E2** (prior 80%) holds: with the exact norms every row is above 16.75.
- **E3, the read-out:**
  - at every refit the down m₂/m₃ (reading S) stays at 0.012–0.014, against 0.017–0.021 in the small-cut form at the
    rows. The lepton m₂/m₃ behaves the same way;
  - the up m₂/m₃ stays within 0.11 in ln of its small-cut value; the up m₁/m₃ moves by up to +0.20 (row D);
  - the refits used 28, 32, 34 and 40 evaluations. Row B reached the cap of 40; its last ten values span 25.868–25.889,
    so the cap does not matter there. None ended on a box bound.
- **The scope:** four local Nelder–Mead refits (box ±0.2 in Re τ, ±0.5 in Im τ), from rows the small-cut fit chose,
  all on slope 2/5 at Im τ ≈ 3. A minimum elsewhere is not excluded.

**The family** (`exact_family_run.txt`; post hoc).
- The question: near rows A and B, does any embedded horoball (L ≥ L_max), read with its exact norms, give the six of
  the fits' weights?
- The frame is compared with itself: the exact six at (τ, L) against the lever, the small-cut six at L_max at the row.
  No measured value is read, though the rows themselves were chosen by a fit to data.
- **F1, along L at the rows' τ.** At each of the 15 scanned values of L, from L_max to 3.5, some ratio of the exact six
  stays at least 0.419 (row A) or 0.462 (row B) in ln from the lever.
  - The closest point is at or just above L_max.
  - The exact down and lepton m₂/m₃ sit 0.40–0.48 below the lever's there, and fall further as L grows.
- **F2, one Nelder–Mead over τ (±0.2 in Re, ±0.5 in Im) and L ∈ [L_max, L₂].** The least rms distance is 0.220 (row A)
  and 0.249 (row B), against the measure's 0.10 floor. Both were found within 0.02 of L_max.
- **The small-cut family moves too.** Its down and lepton m₂/m₃ fall monotonically with L, by about 0.80 in ln from
  L_max to L₂. Near L_max the six move by up to 1.3–1.4 in ln per unit of L: most in the up m₁/m₃, and by 0.72 in the
  down and lepton m₂/m₃.
- **C, sector independence,** holds at row A (5 × 10⁻¹⁵). At row B it fails as worded (1.00): the up sector's channel i
  vanishes identically on (2/5, 1/10), with zero residue, and C did not exclude it. The non-zero channels agree to every
  stored digit at `exact_end.json`'s R3, at the neighbouring τ.
- Of the expectations written before the run, F1's (least D above 0.2) and F2's (least rms above 0.1) were met; C's
  failed as worded.

**What it means.**
- **The rule and its ground.** B1726's `compute()` weights each channel by √(2πL + c_s) with L = L_max(Im τ), read from
  B1667's column: 0.656 at Im τ 2.0 down to 0.645 at 3.5, and 0.647 at the rows. B1741, B1749, B1786 and the horocycle
  test all call it. The rule's ground was geometric: the end is the maximal horoball.
- **That ground is gone.** 2πL_max + c_s is not the maximal horoball's norm.
  - With the horoball's exact norms, the six fail near the four families' rows (local refits; least χ²_six 25.9).
  - Near rows A and B, no embedded horoball (L_max ≤ L ≤ L₂, τ within ±0.2 and ±0.5) brings the exact six within rms
    0.22 of the lever.
- **A reading.** What carries the six is a regularisation with a scale: the regularised norm c_s, plus 2πL at L_max's
  height, with the regular part kept inside the cut.
  - Either a reason other than the horoball's norm ties that scale to L_max(τ), or the scale is an input.
  - Until such a reason is named, that the fits sit at L_max's height is a pattern match.
  - In this formula the six move with L, so the data's preference for L_max over L₂ is a preference for a scale. No fit
    with L free has been run.
- **The horocycle test's H4 is restated:** the six need the small-cut weights at L_max's height, and at L₂'s they fail.
  The second clause is unchanged, because at L₂ the exact and small-cut norms agree.
- **L₂'s results stand.**
- **P-323's θ̄ was not recomputed.** The exact norms are real and channel-dependent, as the small-cut ones are, so its
  mechanism stands. That is a reading.

## 2. The selector (question 3): no forced class condition; the counted class is characterised, not derived

The candidates, on the lines to order 60 (`selector_checks_out.txt`, `bundle_check_out.txt`,
`bundle_check_centre_out.txt`; post hoc, exact arithmetic except (v)).

**(i) Strict compatibility with the fibre's elliptic involution.**
- z ↦ −z sends a flat line (a, b) to (−a, −b). If the involution is gauged, the line must come back to itself: each
  holonomy e^(2πi a·6Y) must square to 1 on every charge, so 2a and 2b must be integers.
- No slope-2/5 line qualifies, since 2a = 4/5.

**(ii) The same up to SU(5)'s centre, (iii) with SU(5) broken to the Standard Model's group.**
- (ii): each holonomy's square is central, so 10a and 10b are integers. (iii): some holonomy is not central, so 5a or 5b
  is not an integer.
- On slope 2/5 these admit exactly b ∈ {1/10, 3/10, 1/2, 7/10, 9/10}: the odd tenths, one T-orbit. That is the counted
  class: B1755's carriers, B1749's strip and the line of W169–W172.
- Its holonomies have a sharp form:
  - the a-holonomy, e^(2πi (2/5)·6Y), is central;
  - the b-holonomy is a central element times e^(iπ·6Y). On the 5 that factor is diag(1, 1, 1, −1, −1), the parity
    with which orbifold GUTs break SU(5) and split the doublet from the triplet (Kawamura; Hall–Nomura).
- None of B1786's out-of-sample carriers (orders 25 and 30) meets (ii).
- **Read by order alone,** as W176 reads the question (the moves act transitively on the lines of each order, W140):
  (i) with (iii) leaves order 2, the lines whose holonomy is P′ itself; (ii) with (iii) leaves orders 2 and 10.
- **It is not forced.** The condition arises only if the involution is gauged on the lines.
  - No rule on record does that. B1651's premise P1 makes the Higgs even under −I, through the lift k; that is a parity
    premise on the Higgs, not a condition on the line. The sweep for gauging finds nothing else.
  - The frame treats the involution as a symmetry of the family: (a, b) and (−a, −b) give identical results (the
    auditor's check).
  - So the odd tenths are characterised as centre × P′, not derived.

**(iv) The line extending over the mapping torus as a flat bundle.**
- Strictly, the monodromy (LR, or its conjugate RL) fixes only the trivial line. With the involution it fixes the
  trivial line and four order-5 lines. None breaks SU(5).
  - This is W140's thread result (a thread γ fixes the lines whose order divides |tr γ − 2|) and B1291's count,
    |det(A − I)|, read for LR.
- With (ii)'s relaxation, up to SU(5)'s centre:
  - without the involution, 25 lines, of orders 1 and 5, none breaking SU(5);
  - with it, 125 lines. 100 of them break SU(5), all of order 25, e.g. (1/25, 3/25) for LR;
  - none of the 100 lies on slope 2/5 (a = 2/5, or its sign flip 3/5).
- So on slope 2/5 no line that extends over the mapping torus, strictly or up to the centre, breaks SU(5). Off that
  slope, up to the centre and with the involution, order-25 lines do. This sits with B1794's finding that the object
  forces no hypercharge class.

**(v) The frame's one-loop potential** (W175's instrument, unchanged; full content only).
- The least V* over the orbit coordinate X, per class representative b, minus that of the SU(5)-preserving class
  b = 0:

| Im τ | 1/60 | 1/50 | 1/45 | 1/40 | 1/35 | 1/30 | 1/25 | 1/20 | 1/15 | 1/10 (the counted class) |
|---|---|---|---|---|---|---|---|---|---|---|
| 2.5 | +0.012 | +0.019 | +0.026 | +0.035 | +0.051 | +0.078 | +0.132 | +0.247 | +0.522 | +1.047 |
| 3.0 | +0.0004 | +0.0014 | +0.0025 | +0.0046 | +0.0084 | +0.016 | +0.033 | +0.074 | +0.180 | +0.374 |
| 3.5 | −0.0014 | −0.0016 | −0.0016 | −0.0013 | −0.0004 | +0.0019 | +0.0078 | +0.024 | +0.069 | +0.150 |

- At Im τ 2.5 and 3.0, V* rises monotonically with the class's distance from b = 0. At 3.5 the least is at b = 1/50,
  by 0.0016.
- The counted class, the farthest possible from b = 0 on this slope, has the highest V* of the eleven at every height.
- W175 found the order-5 class least among its classes (orders 5–30) at every height. Among the finer classes here, at
  Im τ 3.5 classes of orders 35–60 next to b = 0 lie up to 0.0016 lower.

**Closed on the way:** P4′, the next-order lift under the framed end condition (`p4prime_check_out.txt`). With u = R,
Σ R_s² = 0 holds on the twisted lines too (to 2 × 10⁻¹⁶ relative, at two rows and in every sector), so det M vanishes at
every cut and there is no next order.

**So:** no forced class condition was found.
- The counted class has one sharp characterisation, centre × P′.
- On slope 2/5 the object's own bundle condition never breaks SU(5).
- The frame's potential, at full content, disfavours the counted class.
- Gauging the fibre's involution on the lines is the one candidate rule that would select it. It is not in the record.

## 3. The audit: the negatives behind the record, re-checked

Per group: the claim, what was found, and the verdict. "Recomputed" means `audit_checks_run.txt`, the part named, unless
another file is named.

### 3.1 This seat's THE CLASS AND THE END, and the shared numerical core

- **The core is sound** (the auditor's). B1656's functions, as B1726 uses them, are converged at a high and a low point:
  - at 0.5 + 3.03i, NK, the residue contour, cA's quadrature and ε move the mass ratios by at most 8 × 10⁻¹¹, |V| by
    2.7 × 10⁻¹⁰ and J by 7.6 × 10⁻¹⁰; the worst case at a low apex is 6 × 10⁻⁹;
  - cA agrees with main's mpmath route to 2 × 10⁻¹²; |P_s| is doubly periodic to 3 × 10⁻¹⁵; B1691's DR matches
    explicit theta sums to 10⁻³¹;
  - Q is the first leg, so V = U_uᴴU_d is the left-handed mixing;
  - the guard never fires: the least margin of 2πL + c_s is 1.19;
  - c_s is the same in all three sectors to 3 × 10⁻¹¹.
- **Three statements corrected** (recomputed, part A):
  - the 18 apexes off the mirror lines are 10 configurations, 7 up to the mirror. The sign relation is opposite at 10
    of 10 under (L_max, S̃, S) and the same at 9 of 10 under (L_max, S̃, S̃);
  - "the cyclic permutation" is the best-matching one: the least matched |V| is 0.963, the largest entry off it 0.252;
  - §3's table is under (S, S). Under (S̃, S), B1786's best row is the cyclic permutation (|V_us| 0.991, |V_cb| 0.998,
    |V_td| 0.991).
- **A convention** (the auditor's): J's printed sign is the code's. The Yukawa is built as Qᵀ Y u^c, so
  J_phys = −J_code.
- The order-5 mirror apexes' |J| ≤ 8 × 10⁻¹³ is limited by quadrature; refined, it falls to 5 × 10⁻¹⁶ (the auditor's).
- **Verdict:** sound. No claim changes direction.

### 3.2 P-323 (this seat's θ̄ census)

- **It stands, and is understated** (recomputed, part B).
  - H1's verdicts reproduce exactly: NOT HARMONIC 10 859, UNDETERMINED 219, NOISE-LIMITED 318, NO READING 444.
  - 168 of the 219 UNDETERMINED and 317 of the 318 NOISE-LIMITED have a valid centre scaling as r² above 100 σ_D.
  - The N certificates survive tighter quadrature: D(r₁) moves by at most 4 × 10⁻¹¹ (the auditor's).
- **The mechanism is near-analytic** (the auditor's). The real, τ-dependent weights √(2πL + c_s) together with the
  conjugated section make θ_Y non-harmonic; frozen weights give none. So the 10 859 are not independent confirmations.
- **It weakens on a subset** (recomputed).
  - A Higgs set exactly to one channel, e₀, e₁ or e₂, is off the census: F₋₁₀ is one-channel only up to terms of order
    2¹⁰e^(−2.5π Im τ).
  - Such a Higgs makes θ_Y harmonic with J ≠ 0 at all six centres of (1/3, 1/12) and (1/6, 5/12): |D(r₁)| ≤ 4.7 × 10⁻¹⁰,
    ratio 61–73 (r⁶), |J| = 1.3–3.1 × 10⁻². On (2/5, ½) it does not (ratio 4.0).
  - Those two lines are among the twelve where θ_M is harmonic; the other ten were not tested.
  - There θ̄ could be removed by a holomorphic counterterm while CP stays violated, but the up sector has no hierarchy
    (m₂/m₃ 0.43–0.93).
  - A reading: the masses need a Higgs spread over channels with unequal norms, and that spread is what makes θ_Y
    non-harmonic.
- **Wording** (recomputed):
  - "every slope-2/5 line" should read "the 40 in scope". They are NOT HARMONIC in both phase-free readings, 1 600 of
    1 600;
  - the 98.0% is of the 11 078 combinations with a reading; of all 11 840 it is 91.7%. Under a stricter N
    (|D(r₁)| > 10⁻⁴, ratio 3.8–4.2, at least two centres) it is 9 288: 83.8% of those with a reading, 78.4% of all;
  - the lines whose norms pair number 54, of orders 4 and 12, none on slope 2/5.
- **Verdict:** stands.

### 3.3 The horocycle test (this seat)

- **H2, NOT ABSORBED, stands within W in (S̃, S, S)** (the auditor's).
  - Five searches refined from their found points gain at most 7 × 10⁻⁴, and no unflagged distance is below 0.30.
  - The grid's rms is at least 0.381 at every base point; below G (Im τ 1.5–2.1, two lines) it is at least 1.65.
- **Control (b) was narrow, and is now repaired** (recomputed, part H).
  - Its 20 targets share one shift, 0.05 − 0.35i, so it tested local convergence.
  - The rule's search, unchanged, recovers three deep planted shifts to 3 × 10⁻⁸: 0.05 − 1.0i, −0.15 − 1.2i and
    −0.65i, all below G's lowest row.
- **H4's L₂ clause stands** (the auditor's).
  - 30.589 is a confirmed local minimum; a tighter Nelder–Mead stays at 30.5891.
  - No lower basin was found at low Im τ (B1786's 1 080 slope-2/5 apex rows at Im τ 2.0–2.3 give at least 533.6) or
    across Re τ = 0 or 1.
  - On the test's grid G, the full eight-reading menu's least at L₂ equals the seat menu's, 37.94, driven by the up
    sector; the other six readings add nothing lower.
- **H1, H3 and H5 stand** under the other conventions and readings tried (the auditor's).
- **χ² matches** B1741's compare.py. The CKM moduli, which the note had not compared, match B1786's to 2.4 × 10⁻¹²
  (the auditor's).
- **Wording:**
  - the register row needs "within W" and "(S̃, S, S)": 110 searches ended on W's Re edge, and L₂'s best fits use
    (S̃, S̃, S̃) with c = 3;
  - control (c) quoted the accepted points' range, not B1667's column;
  - after §1, "L_max" there means the small-cut weight at L_max's height.
- **Verdict:** stands. Control (b) claimed more than it tested; the search's power is now shown.

### 3.4 Main's B1739, B1740 and B1790

The conventions match the core in all three arcs (the auditor's): S̃ = εS*εᵀ, the rows of Y are the doublets, and
V = U_uᴴU_d.

**B1739 ("the Higgs is nearly null"; the six and an aligned CKM "cannot have both").**
- **The negative holds on the census grid,** by a test the arc did not run (recomputed, part C). Among the 6 151 rows of
  the Standard Model's reading with |V_ud| ≥ 0.97, the least χ²_six is 387 (3.09 over all rows). The best of them misses
  some ratio of the six by a factor of at least 5.05 (5.05–6.68 across the lepton reading and c).
- **"|V_ud| ∝ r^0.52" is a property of the median, not a law** (recomputed).
  - Per Im τ, the slope of ln quantile(|V_ud|) against ln r is 1.24, 1.14, 0.52 and 0.22 at the 10th, 25th, 50th and
    75th percentiles.
  - The arc's own mechanism (light states on h and h̄) predicts slope 1. The other split reading shows it at the lower
    three quantiles: 1.00, 1.02, 0.98, then 0.54, with median/r flat at 6.2–8.5.
  - Under the Standard Model's reading median/r climbs from 6.3 to 52.1. The rows are two populations; the aligned one
    shrinks from 21.9% to 9.8% of rows as Im τ rises.
  - So "0.974 needs r of order one, Im τ ≈ 1" and P-345's "∝ r^½ ≈ 0.1" are unearned.
- **FINDINGS §4's "χ² 52.7"** is the six at the nine's best row. The uniform S̃ reading's own least is 22.36 (recomputed
  with B1740's compare.py), at (2/5, 1/10), Im τ 2.65, |V_ud| 0.992.
- **Verdict:** the exclusion is earned on the census grid, by the joint test. The r^½ law and its extrapolation are
  not.

**B1740 (the non-null Higgs under the Standard Model's reading).**
- **It is stronger than stated** (`b1740_floor_out.txt`). On all 23 940 F₋₂ rows, at both horocycles, the Standard
  Model's reading has no hierarchy:
  - the up m₂/m₃ (read with S̃) is at least 0.283, 77 times the measured 3.7 × 10⁻³; its floor rises with Im τ, from
    0.283 to 0.347;
  - the down m₂/m₃ (read with S) is at least 0.374, 20 times the measured.
- A Higgs set exactly to e_i leaves no hierarchy either. At 0.35 + 3.05i on (2/5, 1/10) the up sector's
  (m₂/m₃, m₁/m₃) is (1.000, 0), and the down and lepton sectors' (0.52, 0.019). That is the auditor's; it was
  re-checked here with B1790's referee module, in a scratch run that is not committed.
- **Scope** (the auditor's). "The dichotomy is sealed" and "the non-null ones (a < 0) miss the masses" rest on F₋₂.
  - F₋₆ was not run, as disclosed, and only the two ends, r ≈ 0.006 and r ≈ 1, were tested.
  - B1743's admixture direction (P-352; r ≈ 0.017) reached χ²_nine 17.3 under the uniform reading.
  - It should read "sealed for F₋₂".
- C1(iii) compares two identical expressions, so it tests nothing (the auditor's).
- **Verdict:** earned and robust for F₋₂, on its grid; the dichotomy's general form overreaches.

**B1790 (the reading not derived in the frame).**
- **No class of maps is missing** (the auditor's): orientation reversal with either line sign is in `maps.py`, SL(2,ℤ)
  is covered by B1724, and conj Y(S, M) = Y(S̃, εM*εᵀ) holds exactly.
- **There is a route the arc does not list** (recomputed, part E).
  - On the mirror lines a holomorphic section reproduces the S̃ reading exactly: conj DR(τ) = diag(1, 1, −1)·DR(τ) at
    Re τ = 0, and the same at τ − 1 at Re τ = ½.
  - The spectra agree to |Δln| 0.00 on (2/5, 1/10) at 3i and ½ + 3i, against 1.27 off the line at 0.35 + 3.05i.
  - It is covariant only under Γ⁰(2), like B1724's S*.
  - So "needs an antiholomorphic or Hermitian slot" holds for SL(2,ℤ)-covariant sections at generic Re τ. A mirror-line
    rule for τ with such a section is open.
- **"Nearly reading-blind"** holds for the coarse measure only. The precision minima on B1726 (recomputed with B1740's
  compare.py) are 3.09 for (S̃, S, S), 22.36 for (S̃, S̃, S̃), 28.47 for (S, S̃, S̃) and 139.4 for (S, S, S).
- **Verdict:** earned, with that scope.

### 3.5 The SM seat's W172 and W174

**W172 (the price of CP at the counted line).** Recomputed with the SM seat's own code (W172's and W175's modules,
unchanged), part F. The "bosons" are the Higgs pair: H_u and H_d are the only bosonic entries of W167's content.
- **P0–P3 are earned** at the full content, at the rows' heights and s = 3–4 (the auditor's).
- **"Robustly" is not earned.**
  - With the bosons' weight set to 0 (matter only), the X-minimum leaves the mirror point at all 16 row heights. It goes
    to X* = 0.262–0.379, or its image 2 − X*, 0.004–0.011 below V(1).
  - These X* lie 0.002–0.177 from a row's X at the same height. Up to the mirror image the rows run 0.235–0.654.
  - CP breaks below a bosons' weight between 0.20 and 0.25 at Im τ 2.96, and between 0.10 and 0.15 at 3.12.
  - W175's pitchfork below Im τ 2.22 is a second route.
  - So NOTE's "every content variation keeps X at a mirror fixed point" and "it needs the contents' weights tuned
    against each other" are unearned. The menu's bosons' weights ran 0.5–20. Its subsets ran the quarks alone (X* = 1),
    the leptons alone (X* = 3.5) and the Higgs pair alone; the quarks and leptons together without the Higgs pair were
    not among them.
- **"In effect a flat direction" depends on the yardstick.** Measured against the X-well's own amplitude (0.494–0.620)
  rather than |V*|, the rows sit 3.2–15.4% of the way up the well, and the price is 1.6–7.7% of it.
- **Cosmetic:** 16 distinct heights, not 17; two stored heights differ only in float noise.
- **Verdict:** P0–P3 stand; "robustly" and "flat" overreach.

**W174 (the census window: the cusp's exponent patterns).**
- **The arithmetic is cleared** (the auditor's).
- **The slope-2/5 verdict is a near-miss inside extraction noise** (recomputed, part G).
  - With the stored (5,6) exponents the least excess over ln 3 is 0.029, on an unconverged line, (2/5, 4/5).
  - With the (4,5) exponents four slope-2/5 patterns pass, by 0.009–0.030: (2/5, 3/10), (2/5, 2/5) and (2/5, 7/10) at
    Re τ 1/8, and (2/5, 1/10) at 3/8.
  - Extrapolated past (5,6), the same four fail by 0.10–0.11. The trend supports the fail, which is earned if the
    asymptotic exponents are the rationals.
- **Scope** (the auditor's).
  - "On every census line" and "holds on every line, converged or not" go past the rule's own S0 clause; the 46
    unconverged lines are open.
  - Menu A covers one reading, (S̃, S, S), and one horocycle.
- **The criterion** (the auditor's).
  - "Within a factor 3" was applied to each ratio's prefactor. Per coefficient (ln 9 on the ratios), the slope-2/5
    rationals and ω pass, and B still fails by 0.23.
  - Random near-data sixes pass menu A 18.5% of the time, above the rule's 5%, so a pass would have been read as
    capacity.
- **Verdict:** earned for B, for ω at factor 3 per ratio, and for the converged non-2/5 lines. On slope 2/5 it is a
  near-miss resting on the exponents' asymptotics. "Answered in its sharpest form" overstates.

### What the audit changes

- **No negative reverses.** These stand:
  - P-323, and the horocycle test's H2 and H4;
  - B1739's exclusion on its grid, B1740 for F₋₂, and B1790 with its scope;
  - W172's P0–P3, and W174's verdicts on B and on ω at factor 3 per ratio.
- **Claims went past what was tested:** control (b); "every slope-2/5 line"; the r^½ law and its extrapolation; "the
  dichotomy is sealed"; "needs an antiholomorphic slot"; "nearly reading-blind"; "robustly"; "in effect flat"; "every
  census line".
- **Two routes the arcs did not list:** the matter-only potential at the rows' heights (W172), and the mirror-line
  holomorphic section (B1790).
- **One structural fact made explicit (P-323):** with a Higgs set exactly to one channel, a direction off the census,
  θ̄ is removable with CP violated on the two lines tested, (1/3, 1/12) and (1/6, 5/12); and there the masses have no
  hierarchy.

## 4. Corrections applied to this seat's notes (dated, appended)

- **THE CLASS AND THE END:**
  - the off-mirror apex counts (10 of 10 and 9 of 10);
  - "the cyclic permutation" is the best-matching one, with its margins;
  - §3's table is under (S, S);
  - J's sign convention.
- **`P323_RESULT.md`:**
  - an exactly one-channel Higgs, off the census, gives a harmonic θ_Y on the two lines tested (no hierarchy);
  - "every slope-2/5 line" → "the 40 in scope", with 1 600 of 1 600 in both readings;
  - the denominators: 91.7% of all; under a stricter N, 83.8% of those with a reading and 78.4% of all.
- **`HOROCYCLE_RESULT.md`:**
  - control (b)'s reach, and its repair;
  - the ledger row's qualifiers, "within W" and "(S̃, S, S)";
  - the column's range;
  - "L_max" is the small-cut weight at L_max's height, and the exact-norm failure's scope.

## For main's registers (main's to enter)

- **P-402, with MAINS_PLAN step 5 (the horocycle).**
  - B1726's rule takes L = L_max(Im τ), on the ground that the end is the maximal horoball. 2πL_max + c_s is not that
    horoball's norm. With its exact norms the six fail near the four families' rows (§1: local refits, least χ²_six
    25.9). Near rows A and B no embedded horoball brings the exact six within rms 0.22 of the lever (the family).
  - The horocycle test's proposed ledger row should then read: "the end's scale L in 2πL + c_s (L_max's height, 0.647
    at the rows) | a formula's scale | preferred by the data to L₂'s; within W in (S̃, S, S) not absorbed by τ; not the
    maximal horoball's norm (the web seat's exact end)".
  - The question "what selects L_max or L₂" becomes: what, other than the horoball's norm, ties the regularised norm's
    scale to L_max(τ)?
- **P-266:** if the end is a regularisation with a scale, the look-elsewhere concern P-266 was declined for applies to
  that scale.
- **P-323:** the corrections in §3.2 and §4.
- **P-345 (B1739's consequence):** the r^½ law is a median artefact; the exclusion holds on the census grid by the
  joint test.
- **B1740 and B1790:** the scope corrections in §3.4.
- **P-164, P-250 and P-277 (the class):** §2.
  - On slope 2/5 the object's bundle condition never breaks SU(5), strictly or up to the centre.
  - The counted class is centre × P′.
  - Gauging the fibre's involution on the lines is the one candidate rule that would select it.
- **P-406 (what the object forces, stated as a theorem):**
  - §2 (iv) is a forcing statement of that kind, on slope 2/5: a line there that extends over the mapping torus,
    strictly or up to SU(5)'s centre, preserves SU(5).
  - §3 marks which negatives are structural (B1790's identity, P-323's mechanism) and which rest on a grid or a
    wording (B1739's exclusion, B1740's floor, W174 on slope 2/5).
- **The look ledger:** below.

## Proposals (they assign nothing)

1. **To main, for P-402: name the end.**
   - The rule L = L_max(τ) has lost its geometric ground. Either a reason other than the horoball's norm ties the
     regularisation's scale to L_max(τ), or the scale is an input.
   - If it is an input, the six's specificity should be re-read with L free, at the look-elsewhere cost P-266 named.
   - If the end is a geometric horoball, the six fail at both canonical ones on the evidence so far: at L_max near the
     four families' rows (§1, local refits), and at L₂ by H4.
2. **To main: should the fibre's involution be gauged on the lines?**
   - The involution commutes with the monodromy, so it acts on the mapping torus.
   - If a rule gauges it up to SU(5)'s centre, and the line must break SU(5), the slope-2/5 line is forced into the
     counted class, with its b-holonomy centre × P′. B1786's out-of-sample carriers are then excluded. Read by order
     alone, the condition leaves orders 2 and 10.
   - The record has no such rule (§2). The slope stays an input either way.
3. **To the SM seat: W172's matter-only variation as its own sealed arc.**
   - The physical question is whether the Higgs pair belongs in the frame's bulk loop. In B1656's frame the Higgs's
     massless mode is the end's boundary class (B1654).
   - With matter only, the minimum leaves the mirror point at every row height and lands among the rows' X.
   - A seal could ask whether the six at that X* stay below the bars, and what J is there. W176 could carry the same
     variation per order.
4. **To the SM seat: amend W172's "robustly" and "in effect a flat direction", and W174's scope** (§3.5). W174's
   slope-2/5 verdict rests on the exponents' asymptotics.
5. **To main: amend B1739's FINDINGS §3–4 (the law, and the 52.7), B1740's "the dichotomy is sealed", and B1790's
   FINDINGS lines 73–76 and its §4** (§3.4).

**Next here,** on main's word or the owner's:
- a sealed six-fit with L free in the small-cut formula, if main wants that look;
- the matter-only six at W172's X*, if the SM seat hands it here.

## The look ledger

- **One sealed look:** §1's exact end, the six only. E1 held at its 55% prior; E0 and E2 held.
- **Seen before the seal,** as the rule disclosed: the rows' small-cut values (the horocycle test's), and the exact
  norms' effect at `exact_end.py`'s rows. R3 is row B's line at Δτ ≈ 0.001 and R1 row A's at Δτ ≈ 0.04, so E2's size
  at A and B was foreseeable. E1, the refits, was not.
- **Post hoc and data-free:** the family (whose lever is the six at a data-fitted row), the mechanism, the convergence,
  the selector, the two bundle checks and P4′. No measured value was read in them.
- **The audit's data read-outs, informal and disclosed:**
  - B1739's joint test;
  - B1740's floors against the measured ratios;
  - B1790's per-assignment minima;
  - W174's variant exponents;
  - the horocycle re-searches;
  - the auditors' own informal χ² read-outs.

  Nothing is claimed from them beyond the verdicts in §3.
- **Limits not tested:** the class energies in (v) are at full content only; "a regularisation with a scale" is a
  reading.

0 of 19.

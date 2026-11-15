# W-L1: the look at τ = i fails. Frame C's read-out at (i, the mark), where frame C's binaries of point and reading settle, fails the big run's own statistic by orders of magnitude, and random targets fit it at least as well a quarter of the time. In frame C the point the act's axis names has only a modest hierarchy, and the place with a hierarchy leaves a scale open

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`. It closes card W-L1
(`relays/cards/CHAT1_W-L1_the_look_at_tau_i.md`, 82c94361d).

**Under the author's ruling of 2026-11-15, afternoon.** The author answered in main's place that W-A1's τ = i read-out
is to be tested against data, and that this seat runs the look. This seat is no longer blind to the two data files the
big run pins. Every other firewall line stands.

**How it was done.**
- **The rule** (card W-L1, 82c94361d) was committed before any data file was opened: one governing option; the big
  run's version-3 statistic, bar and calibration; the bar counted after five options; and a prior, P(PASS) = 0.02.
- **The values** (`wl1_values.py`, LOOK_VALUES.json, sha256 `976f52f2…`) were computed and committed (4a9b788d6) before
  the look script was committed (e364209e7).
- **The look script** (`wl1_look.py`) re-types version 3's statistic. It was sealed before its run, and its output was
  committed (ab41df26b) before it was read.
- **Labels.** Computed once; expectations committed first (the rule and the prior). The statistic was recomputed
  independently from the committed values, on the referee's own code, and both scripts were reproduced byte for byte by
  the referee.
- **Not blind in the sense of the ledger.** It is a fork after B1944's look, and it is counted in its bar. Two further
  disclosures:
  - W-A1's values at (i, mark) were printed before the rule was written;
  - this seat used these two data files in October, before the firewall (TWO_HIGGS, 219e1bb65).
  With one option declared and nothing free, neither could steer the outcome.

## 1. The outcome

| | the governing option: frame C at (i, mark), the canonical end | the end −0.3 (reported) | the end +0.3 (reported) |
|---|---|---|---|
| χ²₇ (bar 22.60) | **7,820** | 7,996 | 7,664 |
| worst factor (bar 3) | **12,758** | 14,161 | 11,590 |
| calibration, χ²₇ (bar 1 %) | **26.1 %** | 25.8 % | 26.4 % |
| calibration, worst factor (bar 1 %) | **73.6 %** | 72.8 % | 74.1 % |
| outcome | **FAIL** | FAIL | FAIL |

- **The pulls of the governing option**, in compare.py's order:
  - c/t +47.3, u/t +47.8;
  - s/b +29.2, d/b +22.7;
  - μ/τ +27.3, e/τ +40.1 (frame C's lepton rows are its down rows);
  - |V_us| −1.06, |V_cb| +29.7, |V_ub| +32.4.
- **Reported (P-341):** χ²₆ = 8,242 and χ²₉ = 10,176.
- **Every mass ratio is too large**, by large factors: the frame's ratios are larger than the targets'. So are |V_cb|
  and |V_ub|. Only |V_us| is near, as in every option of the big run (B1944).
- **The calibration is of the read-out as a whole**, and it says the read-out is generic. About a quarter of B1720's
  random targets fit it at least as well in χ²₇, and about three quarters in the worst factor.
  - |V_us| is one row of seven, 10 % below its target. Alone it carries little weight: under B1720's law a random |V_us|
    falls as near about 8 % of the time (the referee's number, computed once).
- **The end's convention does not matter at this scale.** Shifting L₂ by −0.3 and +0.3 moves χ²₇ by +2.3 % and −2.0 %.
- **The coarse cell alone forces the outcome.** The worst factor is 12,758 against a bar of 3, so no bar or calibration
  could change it.

**Against the prior.** The prior was P(PASS) = 0.02. It was written because frame C's hierarchy is a height variable
and τ = i is a bulk point, with W-A1's printed σ₃/σ₁ (of order 1e-1 and 1e-2) in view. The outcome is what the prior
expected.

## 2. What it teaches

- **[J] In frame C, selection and hierarchy pull apart.**
  - **The selected point.** W-A1 found that at τ = i, where the act's axis crosses the cone point of order 2, three
    binaries settle by equivalence:
    - the one binary the record's frame C carried, the Higgs world's global bit (C04), since S̃ = S;
    - the two a point read-out brings back: mark against twin, and the two crossings.
    - The end's convention (C05) does not settle.
    - The point is named by a rule, the act's axis meeting the cone point of order 2. That rule is one counted choice,
      proposed after the look (W-A1, W-V1).
  - **The price.** The point is in the bulk, and frame C's hierarchy is a height variable (W-F24). So at that point the
    read-out has the bulk's ratios, and the look fails like the average did (B1944).
  - **The hierarchical place.** Where frame C does have a hierarchy, at the cusp (W-F25), the read-out needs a height the
    frame does not fix. It leaves one open scale, and on the up sector the mark against the twin.
  - **So in frame C no read-out on record is both selected and hierarchical.** The selected ones (the average, B1944; the
    point the act's axis names, this look) are in the bulk. The hierarchical one (the cusp, W-F25) leaves a scale. That
    is a reading from these cases, not a property shown for the frame.
  - **The axis's height (elementary; not independently checked).** Every image of the act's axis is a semicircle of
    radius √5/(2|a|) ≤ √5/2, since it is the closed geodesic of discriminant 5. So no point the axis names rises above
    Im τ = √5/2.
- **[J] What this rules out, and what it does not.**
  - It rules out frame C read at τ = i, and with it the hope that the point the act's axis names rescues frame C. The
    other cone point, ω, is not on the axis (W-A1) and was not looked at.
  - It does not touch W-A1's Part 1. The dictionary from the Weil representation's centre is algebra and makes no claim
    on these numbers.
  - It does not test a frame in which the hierarchy is arithmetic rather than geometric, that is, carried by the
    characteristics' charges at a bulk point rather than by the height.
- **[J] What it suggests.**
  - A frame that is to work at a point the object names must carry its hierarchy in its exponents at that point, not in
    the height.
  - In modular-flavour language, that is a residual-symmetry expansion (Feruglio, Gherardi, Romanino and Titov,
    arXiv:2101.08718; Novichkov, Penedo and Petcov, arXiv:2102.07488). Near i, mass ratios are suppressed by powers of the
    distance to i, set by the fields' charges under the residual symmetry.
  - At i the residual S does force one zero in frame C, the Higgs triplet's third component (W-A1). But no sector's
    singular value vanishes (W-A1, I2). So frame C's fields carry no charges that suppress a generation.
  - That is a design criterion for the next frame, to be checked data-free before any look: at the named point, the
    frame must force zeros that the departure from it then fills.
  - The departure is then a scale of its own. Unless the object fixes it, the criterion trades the cusp's open height
    for an open distance to i.

## 3. Banking and what is owed

- **Banked as a reading of frame C at τ = i: NEGATIVE as sealed, PROVISIONAL until its second computation** (the SM
  seat's re-run, below), as B1944 was banked. It is not the programme's comparison.
- **Owed:** the SM seat's re-run of `wl1_values.py` and `wl1_look.py` on the pinned files, as the second computation.
  Its label would be "reproduced". "Recomputed on another family of model" would be the stronger label.
- **The look ledger gains a row:** this look, with one option, the fifth counted in the frame-C family (the big run's
  four and this one).
- **The ledger beside the outcome, as the card asks:**
  - 36 sealed decisive cells and 32 post-hoc scans (Review 70);
  - six point-based value looks (A9);
  - the big run (B1944);
  - and this look.

## 4. Typed

| statement | how checked |
|---|---|
| the outcome FAIL; χ²₇, the worst factor, the calibrations, the pulls | computed once; expectations committed first (the rule and the prior; the values committed before the look script); recomputed independently from the committed values (the referee's own code: every number agrees; the calibrations exactly on the seed, and 25.1 % and 73.0 % on an independent stream of 400,000 draws); both scripts reproduced byte for byte (the referee) |
| the end's convention moves χ²₇ by about 2 % | computed once (reported options) |
| in frame C no read-out on record is both selected and hierarchical | a reading (this look, B1944, W-F24, W-F25, W-A1) |
| a frame working at a named point must force zeros there | a hypothesis (a design criterion) |

## 5. Files

`relays/chat1_2026-11-15_wl1/`:
- `wl1_values.py`, LOOK_VALUES.json, `wl1_look.py`, `SCRIPT_SHA256.txt`;
- `wl1_values_out.txt`, `wl1_look_out.txt`, `wl1_look_output.json`;
- the warnings files, both empty.

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes;
the read's corrections are applied in this version. The first version's commit message (ffba48a8f) says "has no
hierarchy"; "only a modest hierarchy" is the corrected wording.

0 of 19.

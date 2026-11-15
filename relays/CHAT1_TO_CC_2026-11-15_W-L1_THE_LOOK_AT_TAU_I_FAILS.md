# W-L1: the look at τ = i fails. Frame C's read-out at (i, the mark), the point where every binary settles, fails the big run's own statistic by orders of magnitude, and random targets fit it as well a quarter of the time. In frame C the point the object names has no hierarchy, and the place with a hierarchy names no point

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:`. It closes card W-L1
(`relays/cards/CHAT1_W-L1_the_look_at_tau_i.md`, 82c94361d).

**Under the author's ruling of 2026-11-15, afternoon.** The author answered in main's place that W-A1's τ = i read-out
is to be tested against data, and that this seat runs the look. This seat is no longer blind to the two data files the
big run pins. Every other firewall line stands.

**How it was done.**
- **The rule** (card W-L1, 82c94361d) was committed before any data file was opened: one governing option; the big
  run's version-3 statistic, bar and calibration; the bar counted after five options; and a prior, P(PASS) = 0.02.
- **The values** (`wl1_values.py`, LOOK_VALUES.json, sha256 `976f52f2…`) were computed and committed (4a9b788d6) before
  the look script existed.
- **The look script** (`wl1_look.py`) re-types version 3's statistic. It was sealed (e364209e7) before its run, and its
  output was committed (ab41df26b) before it was read.
- **Labels.** Computed once; expectations committed first (the rule and the prior). Not blind in the sense of the
  ledger: it is a fork after B1944's look, and it is counted in its bar.

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
- **The calibration says the read-out is generic.** About a quarter of B1720's random targets fit it at least as well in
  χ²₇, and about three quarters in the worst factor. So even |V_us|'s nearness carries no weight.
- **The end's convention does not matter at this scale.** Shifting L₂ by ±0.3 moves χ²₇ by 2 %.

**Against the prior.** The prior was P(PASS) = 0.02, written because frame C's hierarchy is a height variable and τ = i
is a bulk point. The outcome is what the prior expected.

## 2. What it teaches

- **[J] In frame C, selection and hierarchy pull apart.**
  - W-A1 found that at τ = i, where the act's axis crosses the cone point of order 2, every binary frame C carries
    settles by equivalence: the mark against the twin, the two crossings, and the Higgs world (S̃ = S). It is the point
    the object names.
  - But it is in the bulk, and frame C's hierarchy is a height variable (W-F24). So at that point the read-out has the
    bulk's ratios, and the look fails like the average did (B1944).
  - Where frame C does have a hierarchy, at the cusp (W-F25), it names no point. It leaves a scale, and on the up sector
    the mark against the twin.
  - **So in frame C no read-out is both selected and hierarchical.** That is a structural property of the frame. It is
    shown here at one named point, and by B1944 for the average.
- **[J] What this rules out, and what it does not.**
  - It rules out frame C read at τ = i, and with it the hope that frame C's symmetric points rescue it.
  - It does not touch W-A1's Part 1. The dictionary from the Weil representation's centre is algebra and makes no claim
    on these numbers.
  - It does not test a frame in which the hierarchy is arithmetic rather than geometric, that is, carried by the
    characteristics' charges at a bulk point rather than by the height.
- **[J] What it suggests.**
  - A frame that is to work at a point the object names must carry its hierarchy in its exponents at that point, not in
    the height.
  - In modular-flavour language, that is a residual-symmetry expansion: near i, couplings are suppressed by powers of
    the distance to i, set by the residual S's charges. Frame C's couplings at i show no forced zero (W-A1, I2), so frame
    C has no such charges.
  - That is a design criterion for the next frame, to be checked data-free before any look: at the named point, the
    frame must force zeros that the departure from it then fills.

## 3. Banking and what is owed

- **Banked as a reading of frame C at τ = i: NEGATIVE**, as the rule says. It is not the programme's comparison.
- **Owed:** the SM seat's re-run of `wl1_values.py` and `wl1_look.py` on the pinned files, as the second computation.
  Its label would be "reproduced". A check on a code of another family would be better.
- **The look ledger gains a row:** this look, one option, after five in the frame-C family.

## 4. Typed

| statement | how checked |
|---|---|
| the outcome FAIL; χ²₇, the worst factor, the calibrations, the pulls | computed once; the rule and the prior committed first; the values committed before the look script existed |
| the end's convention moves χ²₇ by 2 % | computed once (reported options) |
| in frame C no read-out is both selected and hierarchical | a reading (this look, B1944, W-F24, W-F25, W-A1) |
| a frame working at a named point must force zeros there | a hypothesis (a design criterion) |

## 5. Files

`relays/chat1_2026-11-15_wl1/`:
- `wl1_values.py`, LOOK_VALUES.json, `wl1_look.py`, `SCRIPT_SHA256.txt`;
- `wl1_values_out.txt`, `wl1_look_out.txt`, `wl1_look_output.json`;
- the warnings files, both empty.

This note was pushed before its referee read finished, following the author's word of 2026-11-15 on untracked notes.
The read's corrections follow in a later commit.

0 of 19.

# W-C7: B1913 comes out the same on this seat's own code; B1885's negative already has two computations; B1823 and B1822 are held by this seat's firewall

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`. This note closes card W-C7
(`relays/cards/CHAT1_W-C7_three_negatives_b1913_run_the_rest_held.md`, 62c116c22), proposed and approved in M18.

**How it was checked:** recomputed independently, on this seat's own construction of the state
(`relays/chat1_2026-11-11_golden_state/golden_state_peak.py`, imported unchanged); expectations committed before the
run, but **not blind**: this seat read § 1 of B1913's FINDINGS through the mask before writing them, to judge the card
against its firewall. Main's code was not opened.

## 1. B1913: the results

| item | this seat's result | main's (B1913 § 1) |
|---|---|---|
| \|f\|² under (1, 0, 5, 1) and (2, −1, 5, −2) | unchanged, within 2.8 × 10⁻³⁰ at three points (sealed run, E1) | ratio 1.0 |
| the flat density \|f\|²/y² | changes by exactly \|cz + d\|⁴, within 2.8 × 10⁻³⁰ (sealed run, E2) | the same |
| the greatest place of \|f\|² | one maximisation, in the standard chart only, finds this seat's z\* of 2026-11-11 again (4.6 × 10⁻²² away; post hoc E3, reported only). Its maximum in the moved chart was not computed, so main's "distance 0" is not reproduced | z\*, distance 0 |
| the flat density's greatest place, standard chart | 0.256228 + 0.314113 i, a strict local maximum, 0.0559 from z\* | (0.2562, 0.3141); the 0.056 on record |
| the same, chart moved by (1, 0, 5, 1), carried back | 0.314884 + 0.342973 i, a strict local maximum | (0.3149, 0.3430) |
| their distance | **0.0654** | 0.065 |

**So B1913's statement holds on this seat's code:** the hyperbolic density's greatest place does not depend on the
chart, and the flat density's does, by 0.065.

## 2. How the run went

- **The sealed run** (`wc7_checks.py`, sha256 `75c3e66d…af72f7b6`) held E1 and E2, then stopped in E3. To evaluate f at
  g₁z near the peak (imaginary part about 0.043), the sealed code's series needed more terms than it allows, and it
  refused. The numerical derivative raises the working precision, and that raises the count.
- **Post hoc 1** (`wc7_posthoc_1.py`, committed before its run) computes the moved chart's densities in the standard
  chart, through the identity E1 and E2 had just checked: \|f(g₁z)\|²/Im(g₁z)² = \|f(z)\|² \|5z + 1\|⁴/y². E4 then held
  as sealed.
- **Two checks that cannot fail, said plainly** (§ 13, kind 4):
  - after the change, E3 locates the maximum of \|f\|² once and measures its distance from z\*. It tests nothing about the
    chart. It is reported, not counted.
  - E5, the sealed control, is the same function on both sides after the change. It shows only that the optimiser
    returns one point twice.

  The result rests on E1, E2 and E4, within these limits:
  - the moved chart was never evaluated near the peak;
  - E1 and E2 sample the identity at six cases, and that it holds everywhere is the transformation law, not a
    computation;
  - E4's threshold (more than 10⁻³ apart) is nearly certain to pass. Its real content is that both maxima agree with
    main's coordinates to four places.

## 3. What the wall teaches (the rule's point 5)

B1913's argument, which this seat did not compute: the flat area is excluded by invariance, not by a choice, since a
density used to read a place off the curve must be a function on the curve. Among areas invariant under all of
SL₂(ℝ), the hyperbolic area is the only one up to scale. A Γ₀(5)-invariant weight would give others, so "forced" holds
only within that class. Any increasing function of \|f\|² has the same greatest place, so the density's power is not an
ingredient. What stays open is the one ingredient B1913 names, which curve: the
reading of the mark. This seat has nothing to add to that.

## 4. What was not run, and why

- **B1885's negative** (the agy lane's point is not the critical point). This seat found it first, on 2026-11-11
  (`relays/chat1_2026-11-11_golden_state/posthoc_peak.py`, Q1). B1885 recomputed it on main's code. So it already has two
  computations, on two codes. The lane's point is already in this seat's 2026-11-11 file, so a rerun here would only
  repeat this seat's own Q1, not add a new code. The card's reason, that a rerun would need the lane's outputs, was
  wrong.
- **B1823** (Step A, the tied heavy vacuum). Its sealed design compares the frame's masses and mixing with measured
  values.
- **B1822** (the T-norm on the frame's matter). Its code forms a χ² against measured masses.
- **Why B1823 and B1822 are held.** This seat's firewall, set by the author, forbids any mixing or Yukawa quantity and
  any comparison of the held targets with data. This seat counted terms in their files and read neither further.
  `needs`: they stay with main or go to a seat without this firewall, unless the author changes it for this seat himself.

## 5. Files

`relays/chat1_2026-11-13_wc7/`:
- `wc7_checks.py` (sealed), `wc7_checks_out.txt` and `wc7_checks_err.txt`;
- `wc7_posthoc_1.py` and `wc7_posthoc_1_out.txt`.

This note was read by one session before it was pushed.

0 of 19.

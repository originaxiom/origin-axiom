# W142 — the third opinion on main's B1735 (P-342), and an audit of its scripts and arithmetic: the re-run, the χ² calibration on own code, the definitions checked, the sensitivity, the row on own code, and FINDINGS' statements (the rule, committed before the script)

The SM-derivation seat, 2026-10-23. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **Main's B1735** (post hoc, labelled) put the precision bar on the two-ingredient censuses. On B1726's grid, with τ
  fitted, the seat's menu reaches χ²_six = 3.09, below the bar 16.75. That is at the line (2/5, 1/10), τ = 0.35 +
  3.05i, L_max, up S̃, c = 3, with every pull within 1.32σ. Only 0.03% of random hierarchies do as well over the same
  rows and menu. It is the first row on main below the bar. The nine fail (χ² 109), and the thread rule reaches only
  31–42.
- **The owner's rule of 2026-08-21:** a positive value match is not banked as more than a reading without a third
  opinion.
- **Main's P-342 asks the seats** to re-run calib_chi2.py and control.py, recompute the row on their own instruments,
  and look for any uncounted look. The calibration was written after the minimum was seen.
- **The owner asked (2026-10-23)** for the third opinion, and added: "see if main did anything wrong, check integrity
  of script and math". So this arc audits B1735's code, definitions and statements as well as reproducing them.

## The objects

- **Main's committed files at bf0a9a330**, read with `git show`:
  - B1735: check.py, calib_chi2.py and control.py; calib_chi2.json, check.json and control.json; FINDINGS;
  - B1726's census.jsonl (sha256 d67432f0…, pinned by B1726's lock test and W138) and compare.py;
  - B1734's census.json (b29ac3e3…, recorded by W141) and compare.py;
  - for control.py, B1726's census.py and the files its compute() reads;
  - the mass and CKM data, pinned;
  - B1720's compare.py, for the χ² definition.
- **The own code:**
  - From W138's committed script: the census arrays of B1726, the draws, and the own instrument (W93's residues ×
    κ, W89's norms, the Higgs DR from theta sums), its circle residues of main's bilinear, and its point comparison.
  - From W141's: the census arrays of B1734.
  - Written fresh here:
    - σ from the pinned files;
    - χ² by direct summation of squared differences, not main's |X|² − 2X·t + |t|² expansion, over the four menus
      (seat, cov, free, covfree, the lepton factor in the last two by its closed-form optimum);
    - χ²_nine;
    - the sensitivity runs;
    - the checks of FINDINGS' statements.
  - It imports nothing of B1735's or B1726's or B1734's code.
- **The points for B:** the χ²-best point, (2/5, 1/10) at 0.35 + 3.05i, and its four grid neighbours on the same line
  (0.2 + 3.05i, 0.55 + 3.05i, 0.35 + 2.95i, 0.35 + 3.15i).

## Weave or thread

**Neither, strictly: a check and an audit of main's census of one frame** (B1656's coupling on the shared fibre), with
τ on B1726's grid. The claims are about main's code, definitions and stored numbers.

## The audit by reading (stated now, before any run)

- **check.py, calib_chi2.py and control.py read line by line. No error was found in their logic.**
  - σ is B1720's: σ² = (relative error of each mass)² summed, plus 0.10², with the pairs (c, t), (u, t), (s, b),
    (d, b), (μ, τ), (e, τ).
  - The free menus' single lepton coordinate (E_μ + E_e)/√(σ_μ² + σ_e²) is exactly the χ² minimised over the lepton
    factor. Its closed form k = (w_e d_e − w_μ d_μ)/(w_μ + w_e) is right.
  - The expansion |X|² − 2X·t + |t|² is exact algebra. Its rounding (|X|² ~ 10⁴) is far below the 10⁻⁹ tie tolerance.
  - Ties count against the claim. Data and random targets get the same rows, menus and σ.
  - χ²_nine's tuple unpacking binds as intended.
  - control.py's six, pulls, D (μ·d over s·e) and CKM ratios are formed correctly.
- **The bar.** 16.75 comes from B1698's and B1720's sealed χ² cells. The 99% point for six degrees of freedom is
  16.81, so the bar is slightly stricter than "99%"; 21.67 is the 99% point for nine (21.666). This changes nothing
  at 3.09.
- **FINDINGS' wording, two slips found by reading (by hand):**
  1. "a grid of step 0.15 × 0.1": B1726's Re τ values are 0.05, 0.2, 0.35, 0.55, 0.7, 0.85, so one step is 0.2.
  2. "every earlier χ² cell failed by a factor 5 or more (79 at best)": 79.4/16.75 = 4.7.
- **Integrity of the record:** B1735 pins nothing; it has no ARTIFACT_HASHES. Its inputs are pinned elsewhere (B1726's
  lock test; W141's NOTE for B1734's census).
- **Looks not counted in B1735's calibration:**
  1. **Post hoc.** The cell was applied to censuses already known to hold good coarse rows, and the calibration was
     written after the minimum was seen, as main disclosed. The χ² definition and the allowance were fixed by B1720,
     which was sealed earlier, so they were not tuned to this row.
  2. **The count.** B1735 reports eight χ² fractions (two censuses × four menus): 8 × 0.0003125 = 0.0025. Counting
     every fraction on B1726's census from any seat (six coarse, W138's covfree, four χ²): 11 × 0.0003125 = 0.0034.
     The seat's χ² specificity survives any count up to 32 looks.
  3. **The ingredients** were chosen with the data in view, and the null ignores the Georgi–Jarlskog relations
     (W138's looks). Under the most permissive menu (every covariant reading, the factor free) the χ² fraction is
     0.96%, at the bar, as main says.
  4. **The ratios' correlations** through the shared t, b and τ masses are ignored. That is negligible under the 10%
     allowance (t's error 0.45%, b's 0.9%, τ's 0.02%).
  5. **D** = 10.76 at the row is a ratio of the six, not an independent check, as main says.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| A0 | **The inputs.** The two censuses match their recorded sha256 values and the data files their pins | 95% |
| A1 | **The re-run.** Main's calib_chi2.py and control.py run once in a temporary tree and exit 0. calib_chi2.json is reproduced: every per-seed fraction exactly, every minimum to 10⁻¹² relative. control.json is reproduced to 10⁻¹² (its fresh-against-stored 0.0). check.json's covariant-free per-seed fractions equal W138's and W141's committed ones exactly | 90% |
| A2 | **The χ² calibration on own code** (direct sums; each arc's 20 seeds; four menus; both censuses). Every per-seed fraction equals calib_chi2.json's exactly, the minima agree to 10⁻¹⁰ relative at the same rows, and χ²_nine (seat) is 109.12 and 440.8 to 10⁻¹⁰ relative | 85% |
| A3 | **The definitions.** σ re-derived from the pinned files equals B1720's to 10⁻¹⁵. The bar 16.75 lies below χ²₆'s 99% point (16.81), and 21.67 equals χ²₉'s (21.666) to 10⁻² | 95% |
| A4 | **Sensitivity (labelled; B1726, seat's menu, seeds 1726–1730).** With the allowance 0.05 the χ² minimum stays below 16.75 (by hand ≤ 6.6 at the same row). With the lepton factor removed (c = 1 only) it is above 16.75. With the allowance 0.20, and all the fractions: read-outs | 75% |
| B0 | **The own instrument's controls** at the χ²-best point: residues against the re-implemented bilinear to 10⁻¹⁰ relative; J1 to 10⁻¹⁰‖Y‖³ | 75% |
| B1 | **The five points.** Every stored ratio and \|V\| above 10⁻¹⁰ is reproduced to 10⁻⁶ in log, and J to 10⁻⁵ relative where \|J\| > 10⁻¹⁰. The same values fall below 10⁻¹⁰ | 70% |
| B2 | **The row from the own values:** χ²_six 3.0945633, every pull to 10⁻⁵, D 10.7647 to 10⁻⁶ relative, the CKM over data (4.4117, 23.842, 10.611) to 10⁻⁶, and J 2.468 × 10⁻⁴ to 10⁻⁵ | 70% |
| C1 | **FINDINGS' statements, computed.** The two slips hold as read (a Re step of 0.2; the factor 4.7, not 5). Every other number checked holds: pulls within 1.32σ, D within 1.7σ, J eight times PDG's, the eight fractions and minima of §2's table as printed | 90% |

## What the outcomes mean (fixed now)

- **A1 and A2 hold.** B1735's χ² minimum and its calibration are reproduced by its own code and by a second code
  written differently (direct sums). 3.09 and 0.03% stand.
- **A1 fails, A2 holds:** an environment difference, recorded. **A2 fails, A1 holds:** this seat's code or main's
  departs from the stated definition; diagnosed post hoc and labelled.
- **A3 holds:** the definitions are what main says, and the bar is slightly strict.
- **A4:** if the allowance 0.05 keeps the minimum below the bar, the result does not hang on the 10% allowance. If
  c = 1 is above the bar, the value-level match needs the lepton factor.
- **B1 and B2 hold:** the row is reproduced by a second instrument, which shares with main only B1667's column.
- **C1 holds:** main's statements are right apart from two wording slips, which change no number. A dated note on B1735
  is proposed to main.
- **On "did main do anything wrong" (fixed now).**
  - If A1, A2, A3, B1 and C1 hold: no error in code or arithmetic. Two wording slips; nothing pinned in B1735 itself;
    and the post hoc status main already discloses.
  - If any fails, the failure is the finding, and it is diagnosed before anything else is said.
- **This seat's opinion on banking (fixed now).** If A1, A2 and B1 hold, B1735 is a value-level READING:
  - τ fitted (two continuous numbers on a grid);
  - a line chosen from 266;
  - two hand-put ingredients;
  - post hoc.
  It can be banked as that and no more. It is not a derivation, and the nine fail at value level.

## What stays out

- B1735's part A coarse covfree run, which is not re-run here. Its fractions are W138's and W141's, compared in A1.
- The frame itself; B1740 (sealed by main, running; no expectation stated); P-343 (what places τ).

## Seen before the rule (disclosed)

- **The preparation** was a read-only pass in this seat's session.
  - **On main:**
    - B1735's FINDINGS, check.py, calib_chi2.py, control.py, calib_chi2_run.txt, control_run.txt and the lock test;
    - check.json's B1726 χ² rows and covfree values, and calib_chi2.json's B1726 entries;
    - P-341 to P-343;
    - B1720's compare.py (its σ and bar);
    - B1740's seal message.
  - **On the web seat's branch:** PRECISION_BAR.md.
  - **Looked at in the data:** the HZ2021 masses and errors; W138's committed covfree per-seed values (the first five
    seeds, against check.json's).
- **By hand:**
  - the σ values (0.1036, 0.198, 0.133, 0.123, 0.100, 0.100) and the row's pulls from them;
  - the χ² ≤ 6.6 estimate at allowance 0.05;
  - the quantiles, by scipy, one call;
  - the look counts;
  - the two slips.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed part is a failed launch of that part: kept, disclosed, fixed, and only that part relaunched.
- Any later check is labelled post hoc.

0 of 19.

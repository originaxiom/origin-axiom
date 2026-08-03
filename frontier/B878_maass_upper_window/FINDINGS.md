# B878 — the cc3 Wave-1 harvest: the 43-eigenvalue Maass dataset lands on main — B845's missing dataset found, verified, banked

cc banking seat, 2026-08-03, late night. Harvest from the cc3 seat's branch
`audit/b775-braver-questions` @ `cd1447b6` under the standing **integrate-don't-merge** rule
(the branch is never merged; deliverables are cherry-picked under fresh numbers and verified
here). The relay is preserved verbatim (`RELAY_AS_RECEIVED.md`). Mathematics scope; nothing to
`CLAIMS.md`; Gate 5-Q respected throughout, as on the branch.

## 1. What main was waiting for, now here

**B845's inventory flagged "43 eigenvalue parameters to r = 13.5" as described-but-not-found**
(main carried 17 to r = 9.84, completed by B846). The dataset exists and its arithmetic closes
exactly against main's own banked table:

| | distinct | with multiplicity |
|---|---|---|
| lower window (main's banked B797/B846 table, r ≤ 9.84) | 17 | 27 |
| **upper window (this harvest, r ∈ [10.0, 13.5])** | **26** | **45** |
| **combined** | **43** ✓ | **72** ✓ |

## 2. Verification legs (this seat's, independent)

- **Two-Y stability**: 26/26 upper-window entries pass (|r_Y1 − r_Y2| within 100σ, sigmas
  ~10⁻¹⁰, all flagged stable).
- **The four parent forms**: all present at ≤ 5×10⁻¹⁰ — 7.072004187 in main's own banked
  table (3.3×10⁻¹⁰), the other three in the upper window.
- **The relay's §5 correction is real and was hit here first**: the branch's
  `eigenvalues_final.json` is the stale 6-entry version (the same defect shape B846 fixed on
  main) — the canonical lower window is main's table; the upper window is `scanE_refined.json`.
- **Both flagged entries verified in the data**: the restored 10.9965 double ("patch tolerance
  had wrongly removed it") and the 11.008 parent's tight-bracket note — the relay's instrument
  lesson (brackets narrower than local spacing) is recorded in the dataset itself.
- **S_invariance_dev range [5.7×10⁻¹⁰, 1.3]** — reported, not interpreted; the branch FINDINGS
  (preserved as `branch_FINDINGS.md`) owns that diagnostic's semantics.

## 3. What else this harvest carries

- **The scalar Hejhal solver** (`branch_hejhal_m004.py`) and the arb-certified Cell-9 rung
  driver (`branch_cell9_rung1_v2.py`) — **B804's named missing machinery base** ("Dirac
  eigenvalues need the spinor-Hejhal solver"). B804's class-level verdict and the branch's
  independent Cell-3 spin fork agree at the class level; the spinor extension is now priced
  work, not missing machinery.
- **The ladder alignment**: the branch's rung (i) at 25 digits is the sealed *validation* rung
  under prereg 169e9042; main's B798 box (d ≤ 10, H ≤ 1e7 ⟹ N ≥ 100 digits) is the falsifier
  terminus. 25 → 50 → 100, exactly as designed.
- **In flight on the branch's side**: the λ₂ 27-digit run (relaunched detached, ~24–30 h;
  restart recipe in the relay). Its landing + the PSLQ stage bank later under their own number.

## 4. Honest boundaries

- The **arb certification of the 26 upper values is the branch's** (three §16 review passes,
  verdicts banked in-arc there); this seat verified the dataset's internal stability,
  cross-table consistency, and claim arithmetic — not a re-run of the certification.
  The λ₂ landing will provide the deepest independent check of the pipeline.
- **No completeness claim for the 43** (the branch's own scope limit, adopted: sub-leading Weyl
  terms are 43–60% of leading below r = 13.5 — the budget is a screen).
- Main's banked `B797` table is **not** extended here (its locks stand); the combined view is
  this arc's `results.json`. The paper (cc3's priced item 2) cites both windows.

`tests/test_b878_maass_harvest.py`

# B1954 — The physical lane's work of 2026-11-15 to 17, read and checked: its fifteen defects in X-APEX are exactly quoted, four of its exact claims are recomputed, and none of its own model is banked

**Verdict: PROVED** (a process arc: a harvest, with main's checks of what could be checked). Main, 2026-11-17, at the
author's word to fetch every seat, verify and harvest, this lane first. No measured number is used. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /physical lane|physical-bridge|X-APEX|X-SYNTHESIS|complete cusp|E8 parent|P-C3/: 15 of 1695 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 13); 17 register rows match (DONE 6, QUEUED 11)`. The harvest ledger's rows for this lane end at row 1725 and its pin stood at `1aa76251` (2026-11-12). The
  72 commits since had no row. Main's notes of the top-layer read (2026-11-17) are superseded by this reading.
- **The literature:** none is used by main here. Where the lane cites primary equations (Buttazzo et al. 2013 for the
  quartic's two-loop term; Luo and Xiao, and Bednyakov, Pikelner and Velizhanin, for the Yukawa terms), main has not
  re-read them.

## What was read

Every relay note of the lane since the pin, in full (20 notes), its status page, its packet for main (the checklist
and findings F01 to F17), its one-page premise list for C7, and its fifteen defects in agy-exp's X-APEX. The proof
files under its report folders (about 25,000 lines) were not read: the lane itself labels them author hand
derivations, not independently checked, with no scientific execution.

| delivery | what it is | row |
|---|---|---|
| reviews of agy-exp's X-FUNNEL and X-ENDGAME, and six recommended derivations | eight source findings; independent counterchecks in exact integers; the next steps it recommends | 1853, 1854 |
| the relative-register boundary law; a harmonic-transport draft withdrawn by its author | author derivations with author checks | 1855 |
| its review of every seat | corrections addressed to agy-exp, the web seat, the SM seat and agy-002 | 1856 |
| P-C3 and P-C3a to P-C3f | its own model, an E₈ parent on the complete cusp: field and domain maps, state orbit, protected quartic, neutral response, the light system, a retained massless pair | 1857 to 1860 |
| C4, the packet for main | a dependency-ordered checklist and findings F01 to F17 on the other seats' newest work | 1861 |
| C5, C6, C7 | reviews of X-FRONTIER and X-SYNTHESIS with repairs requested; a four-form quotient and its connection | 1862 to 1864 |
| its answer to the author's word of 2026-11-17 | campaigns paused; one page of premises for C7; X-APEX read in full, fifteen defects | 1864, 1865 |

## What main checked (`verification/codex_checks.py`)

| claim of the lane | main's check | result |
|---|---|---|
| its 36 quotations from agy-exp's X-APEX, at the cited files and lines | each excerpt looked up at its line in agy-exp's branch at the pinned head | **36 of 36 exact**, covering all fifteen findings |
| XA-07: the element agy-exp calls a Weyl involution has order four | the order of the written permutation | **4**. (Main's own witness in its notes, the swap of coordinates 1–3 with 4–6, has order 2) |
| XA-08 and F05: the normalised Fourier square carries a central scalar, −1 at levels 3 and 15 | S and T with (ST)³ = S² at p = 3 and p = 5 | **−1 at 3, +1 at 5** |
| its X-ENDGAME countercheck: the fourth cyclic cover of the punctured-torus bundle has torsion ℤ/3 ⊕ ℤ/15; 45 points of period 4 | SnapPy, and ∣det(LR⁴ − 1)∣ | **ℤ/3 + ℤ/15 + ℤ; 45** |
| C7: E₆ = 45₀ + 1₀ + 16₊₁ + 16̄₋₁ inside E₈ under Q = (2/3)(e₁ + e₂ + e₃); the Q circle has period 6π on E₈ and 2π on the singlets | the charges of all 240 roots | the colour singlets are 40 + 16 + 16 roots of charges 0, +1, −1; the periods hold. The coloured roots have charges ±1/3, ±2/3 **and ±4/3**; the lane's page lists the first two |
| F13: a dimension count cannot count two scales of one dimension | the rank of [1, 1] | 1, with one free ratio: the finding stands |

**Not checked by main:** F12's coefficient (−48 against −24) and the mixed Yukawa terms. They agree with the standard
two-loop equations as main recalls them, which is not a check.

## What main takes from it

- **A scope correction to main's own wording** (its review of agy-002's A2-AMP, which main had verified): that τ → τ + 5
  changes the up sector's sum rules out phases on the points. It does not show that no flat unitary connection exists.
  B1953 and B1945 § 6 claim only the first; a dated note there now says so.
- **A third check of B1951.** The lane checked the web seat's W-A1, Part 1, by hand: the centraliser, the exterior
  algebra and the anomaly counts.
- **The carrier's cohomology.** For the punctured-torus bundle, ordinary H² vanishes and the relative group is ℤ. A
  degree on the fibre can survive only as relative data with a boundary trivialisation. Any use of "flux on the fibre"
  (B1952's flux bit; P-866) has to say which.
- **Its fifteen defects in X-APEX stand as source findings.** Among them: the cusp-contraction check uses a flat massive
  operator, not the punctured hyperbolic one; the wall's gradient omits normal equations; a Dirichlet tail value is used
  as a full gap; the "zero-bit" infrared vector imports a selected vacuum's scales; the precision certificates are
  attached to a different state. They are the checklist for main's own reading of agy-exp's campaigns (P-865 (b)).
- **Its findings F01 to F17** order what main recomputes in the other seats' work. F04 (two different Higgs operators),
  F13 (the scale count) and F03 (the strong-CP benchmark supplies its own premises) bear directly on any count of
  inputs.

## What is not banked, and what the lane asks first

- **Nothing of the lane's own model is banked.** P-C3 to C7 are hand derivations inside a supplied E₈ parent with a
  supplied carrier, metric, background and action. The lane says so on every page, and counts no foundational input
  removed.
- **The step it asks main to recompute first** is one analytic estimate: the bounded inverse on the complete cusp in
  P-C3e, equation (3), with its nonlinear map. Main has not done it. It is entered in P-865.
- **Its twelve-method verification package** (sealed at `ca02b5d8d`) is unrun and stays unrun: main's refusal of the
  earlier sealed packets (M5) stands until a reseal.

## Not claimed

- That any of the lane's proofs is correct. Main read its notes, not its proofs.
- That agy-exp's X-APEX is wrong where the lane found a scope defect. Each finding is about what a named artifact
  tests.
- Any comparison with data.

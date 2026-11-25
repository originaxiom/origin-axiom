# B1977 — At order 30 on the act's line frame C has points with an aligned mixing, a mass hierarchy in both quark sectors, the leptons split from the down quarks in the exponent, and a 2–3 mixing falling at a rate of 1/30; every rate lies on a grid of 1/60, in 17 classes [CORRECTED 2026-11-25, B1979: the converged classes are 12]

**Verdict: PROVED** for G1 to G5, as sealed: all five held.
- The rates are read between heights 20 and 30 at column 0.13.
- The card and the script were hashed before the run (`EXPECTATIONS_HASHED.md`).

Main, 2026-11-24, at the author's word ("dig deeper"). Data-free. Register rows P-860 (d) and P-845. **0 of 19.**

*Dated note (2026-11-25, B1979).* The rates are limits on the grid of 1/60. On 30–40 and 40–50 all 864 are on it, with
largest residuals of 4.2e-4 and 5.1e-5. The four off-grid rates of G3 are finite-height effects. **The 17 classes were
partly an artefact of keying 20–30 rates at three decimals: the converged classes are 12.** Every statement below that
says 17 now reads 12. The web seat's CHK-1 reproduced this arc with two assemblies of its own (credit: the web seat).

*Dated relabel (2026-11-25, P-883, at the author's word):* by THE_WEAVE's test (all threads, none chosen; defined by the joint
action; about all threads at once), this is a **thread** result, not a weave result: frame C at B1976's 96 points, fixed by m004's act. It was first labelled "the weave (the points of a level)".

## Seen first

- **Swept:** `VERDICT topic-sweep /order 30|1/30|exponent grid|Wolfenstein|slow mixing|level 30/: 1 of 1718 arcs on main match (PROVED 1); 4 register rows match (DONE 1, QUEUED 3)`. The one arc matched is B1976.
- **The record:**
  - B1976: the level as a lens, order 30 on the act's line;
  - B1971, B1975: the order-5 rates and the census;
  - B1945: the mass exponents' tropical rule;
  - B1949: the lepton exponents.
- **The seats:**
  - the agy lane's C8 gives the all-S mixing exponents at order 5, with e₁₂ + e₂₃ = e₁₃ at some points;
  - its C9 gives the trade-off between cover degree and the mixing.
- **The literature:** in Froggatt–Nielsen language, rates are charges and ε is the flavon. Additive mixing exponents (V₁₃ ~ V₁₂V₂₃) are the Wolfenstein pattern. Nothing here is read against data.

## The results (`verification/rates30.py`, `rates30_run.txt`, `rates30_run.json`)

**The five slow-mixing points of B1976** are (4/15, 1/30), (4/15, 11/30), (4/15, 7/10), (11/15, 3/10) and (11/15, 19/30). They share one set of rates, in ε = e^{−π Im τ}:

| | m₂/m₃ | m₁/m₃ |
|---|---|---|
| up | 0.399 (2/5) | 1.366 (41/30) |
| down | 0.466 (7/15) | 0.999 (1) |
| lepton | 0.400 (2/5) | 1.100 (11/10) |

| | V₁₂ | V₂₃ | V₁₃ |
|---|---|---|---|
| rate | 0.600 (3/5) | 0.0325 (1/30) | 0.633 (19/30) |

V₁₃ = V₁₂ + V₂₃, and the least diagonal is 0.9998.

| id | expectation | result |
|---|---|---|
| G1 | a hierarchy in both quark sectors at the five points | **holds, 5 of 5** |
| G2 | the slow 2–3 rate is 1/30 to within 2e-3 | **holds, 5 of 5** (0.0325) |
| G3 | every rate within 3e-3 of a multiple of 1/60 | **holds at 860 of 864** (the four outside are near 1.80, at 3e-3 to 4e-3) |
| G4 | the lepton m₂/m₃ rate differs from the down quarks' | **holds, 5 of 5** (0.400 against 0.466) |
| G5 | some point is aligned, hierarchical in both quark sectors, and has a mixing rate below 1/10 | **holds at 30 points** |

**The 96 points fall into 17 classes of rates.** Two classes, of 12 and 6 points, carry the 2–3 rate of 1/30. The largest
class is (up 0.4, 1.4; down 0.466, 1.033; lepton 0.4, 1.0; V 0.633, 0.033, 0.667). The classes are printed in this arc's
verification.

**Disclosed.** The script imports B1976's module, which runs its own computation at import. The first lines of
`rates30_run.txt` repeat B1976's summaries and are not this arc's results.

## What it means

- **The first viable configuration.** Frame C, with two doublets reading S, at points of order 30 on the act's line, is
  the first configuration on record that passes every structural test at once:
  - the mixing is aligned;
  - both quark sectors are hierarchical;
  - the leptons separate from the down quarks in the exponent;
  - a mixing entry stays sizeable deep in the cusp.

  Level 5 could not give these together (B1971, B1976).
- **The scale-free content is the rational rates on the grid of 1/60.** A card that compares their ratios with data
  would read the frame without fitting anything but the scale.
- **The menu is the 17 classes,** a trials factor to be declared, unless a principle picks the class.
- **What remains free:** the height (one number), the column (subleading), and the choice of level 30 itself (P-845).

## What is open

- **A principle for level 30 and for the class:** the act's line fixes the 5-part, and the 6-part is not fixed.
- **Rates at other heights and columns,** and the order-one coefficients.
- **The rates in closed form,** from the characteristics: why 1/30 appears in V₂₃.
- **The sealed card (route d):** the scale-free ratios of the rates, the 17 classes as the declared menu, and the
  random-hierarchy null computed before any look.

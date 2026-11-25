# B1992 — What the whole can select is algebraic: every point or level its moves single out is an algebraic number, so ε at an algebraic height is never one of its selections; a transcendental value needs a map the whole would have to force

**Verdict: PROVED (T1 and T3 are standard theorems; T2 is an exact check on every word to length 4 and on every number
the listening line found).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register
rows P-882, P-629 and P-845. **0 of 19.**

## Seen first

- **B1983 to B1991,** the listening line, and the numbers it found:
  - the fixed points 0 and 2;
  - the bound-state levels −2 and 2cos(2πk/n);
  - the rates ½, 1/√2 and (±1 ± i√7)/2;
  - the counts' coefficients 0, ±2, ±3, ±4;
  - the groups S₃ and S₄.
- **B1980:** the ε question as asked at the author's word.
- **B1791:** Im τ not found forced in an older frame.
- **Swept:** `VERDICT topic-sweep /transcendental|Gelfond|algebraic number|periods?\b|zero-dimensional/: 86 of 1733 arcs on main match (NEGATIVE 18, OPEN 5, PROVED 62, RETRACTED 1); 48 register rows match (DONE 26, QUEUED 22)`. The record uses "algebraic" and "transcendental" in other senses. None types what the whole can
  select.
- **The literature (standard):**
  - a zero-dimensional ideal over ℚ has only algebraic solutions;
  - e^π is transcendental (Gelfond, 1929);
  - the Gelfond–Schneider theorem (1934).

## Custody

- The card and the check were hashed before the run.
- **The check was disclosed twice in EXPECTATIONS_HASHED.md:**
  - its first name, `select.py`, shadowed Python's `select` module and crashed at import before computing anything;
  - its first full run was stopped after 34 minutes with no output (sympy's `solve` on large Gröbner bases), and the
    script was reduced to the zero-dimensionality test that T1 needs.

## The results

- **T1, standard.** The moves are polynomial maps with integer coefficients. A point or level the whole singles out by
  finitely many conditions built from them is a zero-dimensional set defined over ℚ, so its coordinates are algebraic.
  A condition that defines a positive-dimensional set singles out nothing.
- **T2** (`verification/select_check.py`, `select_check_run.txt`):
  - Of the 30 positive words of length 1 to 4, **26** fix a zero-dimensional set of readings on the cusp's leaf, so
    algebraic points.
  - The four exceptions are L³, R³, L⁴ and R⁴, powers of one letter, which fix curves and single out nothing.
  - Every word with both letters (a thread) singles out finitely many algebraic readings.
  - Every number the listening line found is algebraic (T2b).
  - (The run's "all algebraic False" on the four exceptions is a label: a curve contains non-algebraic points and
    singles out none.)
- **T3, standard.** For algebraic y ≠ 0, ε = e^{−πy} is transcendental:
  - y rational: e^π is transcendental, and so are its rational powers;
  - y irrational: e^{πy} = (−1)^{−iy}, and Gelfond–Schneider applies.
- **T4, consequence.** At any algebraic height, ε is not a selection of the whole. It can only arise as an analytic
  function of the whole's algebraic data, through a map the whole would itself have to force.

## What the whole does, read in its own terms

- **The family of selection examined** is a finite classification with a test of membership: the words to length 4,
  classified by whether their fixed set on the cusp's leaf is zero-dimensional.

- **By its own moves the whole can fix only algebraic numbers.** Everything heard so far is of that kind: structure,
  levels and rates.
- **A transcendental value cannot be one of its direct selections.** This covers ε, a mass ratio of the form ε^E·C, and a
  hyperbolic length. Such a value needs a forced analytic map from the whole's algebraic data.
- **The cusp's leaf carries such a map canonically:** its real Fuchsian component is the punctured torus's Teichmüller
  space, the upper half-plane of τ, with readings x = 2cosh(ℓ/2) (Fricke). That map is the geometry the whole already
  has, not a frame chosen by hand. But on that component the moves act as the mapping class group, and the record has
  found there that no point of τ carries weight (B1868, B1923). The selections there are the elliptic points i and ω,
  which have no hierarchy (B1691).
- **This is a type constraint, not a no-go.** It tells the listening line where values could come from:
  - the forced analytic geometry of the cusp's leaf;
  - its connection to the common point. Mod 3 every integral reading of the leaf collapses onto the common point
    (B1601, B1983).
- **No Standard Model shape was asked for or read.**

## What is open

- **Whether the connection between the cusp's two parts forces a value.** The two parts are the isolated common point
  (unitary, algebraic, the one outcome) and the Fuchsian component (analytic, where τ lives, no point weighted). They
  meet only arithmetically, mod 3.

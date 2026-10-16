# W95 — the rule, recorded before the code

The SM-derivation seat, 2026-10-16. Committed before the code that reads it exists. Nothing here is a result.

## Why this arc

- **The owner's go (relay §145).** The fresh look's N2 (`docs/A_FRESH_LOOK_FROM_THE_PRINCIPLE_2026-10-15.md`, §4 and
  §6) asks for the record's own invariants traced by discriminant: summed over every thread of each D > 0, and over
  every CM point of each D < 0. W95 was held for it.
- **The question.** Every value on the record so far was read at one point or along one thread. Read over all threads
  at once, assembled by D, do the weave's values carry structure, and where does it come from?

## Weave or thread?

- **A WEAVE result, in a supplied frame.** It meets THE WEAVE's three conditions:
  - **every thread under a stated rule:** every narrow class of primitive forms of each D in range. Each class is one
    oriented closed geodesic, one thread. None is hand-picked.
  - **a quantity defined by the joint action:** D is the invariant the moves preserve. The D-trace is the sum over the
    whole orbit set of that D.
  - **a claim about all threads at once:** the traces, their law in D, and the CM side.
- **The frame is supplied:** the surface frame (W72's units), cell C1, neutral, given Λ and the cusp's unit (GENESIS
  FK10). The claim is bounded by the range (|D| ≤ 300), and any limit beyond it is a reading.

## The quantity

- **The matrices** are those of W97's instrument with no hypercharge line, so every dressing is 1 and the three sectors
  coincide. At a point τ = x + iy:
  - K(τ)_ik = Σ_c F_i,c conj(F_k,c) y^(3/2), with F_0, F_1, F_2 = W72's units F_i, F₊, F₋ (weight 3/2);
  - Y(τ)_ik = dot(G′(F_i, F_k; R), conj(h5)) y^(5/2), with R at weight −½, h5 at 5/2, and
    G′(X, Y; v) = (v·Y)X + (v·X)Y − (X·Y)v.
- **The trace of discriminant D:**
  - for D > 0, T_D(M) is the sum over every narrow class of the cycle integral ∫ M ds over one period of its closed
    geodesic;
  - for D < 0, T_D(M) is the sum over the reduced primitive forms Q of M(τ_Q) / w_Q, with w_Q = 3 for [1, 1, 1],
    2 for [1, 0, 1], and 1 otherwise.
- **The masses at D** are the singular values m₁ ≤ m₂ ≤ m₃ of T_D(K)^(−½) T_D(Y) (T_D(K)^(−½))ᵀ, as W97 takes them.
  The same is done for each class alone (the thread's own masses).
- **The range:**
  - D > 0: every D ≡ 0, 1 (mod 4), not a square, with 5 ≤ D ≤ 300;
  - D < 0: every D ≡ 0, 1 (mod 4) with −300 ≤ D ≤ −3.

## The threads and the points

- **The classes** are enumerated by Zagier reduction: forms [a, b, c] with a > 0, c > 0 and b > a + c, gcd 1,
  b² − 4ac = D, grouped into cycles by Zagier's step with nᵢ = ⌈(b + √D)/(2c)⌉.
- **Each cycle's thread** is the word W = L R^(n₁−2) L R^(n₂−2) ⋯ L R^(n_r−2), conjugate to ∏ R^(nᵢ) S. Its axis,
  half-width and period come from the word's own matrix, as W97's geometry does.
- **Both orientations are counted** when they are distinct narrow classes. A reciprocal class is counted once.

## The instrument

- **The units** are built by `the_per_field_units.build_units`, W97's route. If every non-zero line coefficient lies
  within 10⁻³⁰ of a Gaussian integer, the rounded integers are used; otherwise the units are used as built.
- **The matrices are invariant** under the moves (exploration below; cell V2). So each point is reduced to the standard
  fundamental domain by τ ↦ τ − n and τ ↦ −1/τ, and the units are evaluated there by their series. There is no
  transport and no fitted matrix.
- **The precision** is 80 digits.
- **The cycle integrals:**
  - the trapezoid in arclength over one period, centred on the axis's apex, with nodes at half steps;
  - Npts = ⌈30·P·(1 + H)⌉ and ⌈37.5·P·(1 + H)⌉, where P is the period and H = √D/(2·a_min), with a_min the least
    a in the cycle. H is the class's highest point in the fundamental domain, where the integrand turns fastest.
- **Four processes,** one class per task.

## Exploration before this rule (disclosed)

All of it is in scratch, on the instrument only. No trace and no cycle integral was computed, and no mass at any CM
point.
- **Invariance.** With no line, K and Y at τ = 0.21 + 1.37i and at its images under T, T⁻¹, S, ST², [[2, 1], [1, 1]],
  T³ and [[1, 0], [3, 1]] (W97's fitted transport) agree to 10⁻³⁹ as matrices.
- **The pointwise rank is one.** At that point the masses are (0, 0, m₃), with m₃ the same at all six images. At
  τ = 0.3 + iy for y = 1, 2, 3, 5 and 8, Y's second singular value is below 10⁻³³ of its first.
- **The units grow at the cusp.** Their leading exponents are −⅞ (F_i), −⅛ (F₊) and −⅝ (F₋), as W72 found. K's
  largest eigenvalue grows from 8 × 10⁴ at y = 1 to 4 × 10³⁹ at y = 8.
- **Sizing by number theory alone:** 282 classes for 5 ≤ D ≤ 300; about 5.8 × 10⁵ nodes at the first count.
- **The units' coefficients.** A scratch check of whether the line coefficients are Gaussian integers was still running
  when this rule was committed. The rule decides the instrument either way (above), and the check's result is
  disclosed in the record.

## A correction to the fresh look, made before any trace

- **What the fresh look said.** §4 said that by Duke (1988) the traces equidistribute as D grows, so in the limit no
  point is charged. On 2026-10-16 this seat told the owner that the likeliest outcome of N2 was "flat".
- **Why that does not hold here.** Duke's theorem holds for bounded invariant functions. The record's surface-frame
  units grow at the cusp, since they are not normalisable (W72, X5). So these traces are not expected to
  equidistribute. A thread's cycle integral is dominated by its highest arc, and the D-trace by its highest classes.
- **Where the content moves.** Each D-trace is finite, while the surface integral W72 needed diverges. So the traces by
  D define masses in the surface frame where W72 could define none, and the question becomes how they behave with D.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, the threads** | each cycle's word has the cycle's discriminant and its automorph's trace; the cycles with words of length ≤ 10 correspond one to one, by rotation, to the Lyndon words in L and R of length ≤ 10 with both letters and D ≤ 300 | 90% |
| **V2, invariance** | at τ = e^(iθ) for θ = 80°, 95° and 110°, the series values of K and Y at τ, τ + 1, τ − 1 and −1/τ agree to 10⁻³⁰ relative, with no reduction | 95% |
| **V3, rank one at a point** | at every CM point of the range and at six further points, σ₂/σ₁ of Y(τ) is below 10⁻²⁵ | 85% |
| **V4, the CM side** | with n_D the number of reduced primitive forms of D < 0: if n_D = 1, both m₁/m₃ and m₂/m₃ are below 10⁻²⁰; if n_D = 2, m₁/m₃ is below 10⁻²⁰ and m₂/m₃ above it; if n_D ≥ 3, both are above 10⁻²⁰ | 80% |
| **V5, every thread has three masses** | for every class, m₁/m₃ > 10⁻³⁰ | 85% |
| **V6, convergence** | for every class and every D-trace with D > 0, ln(m₁/m₃) and ln(m₂/m₃) change by less than 10⁻⁶ between the two node counts | 75% |
| **V7, precision** | on the root (D = 5) and on the class with the most nodes, the ln ratios at 80 and at 100 digits agree to 10⁻¹⁰ | 85% |
| **V8, the cusp carries the trace** | for every D in [100, 300] with at least two classes, the D-trace's ln(m₁/m₃) and ln(m₂/m₃) agree to 10⁻³ with those of the sum over its highest classes (the classes with the largest H) | 60% |

**The read-outs (no prior).**
- **The record's places:** the masses at D = −3 (ω), −4 (i), 5 (the root), 8, and 12 (LLR and LRR, through ω).
- **The law in D:** ln(m₁/m₃) and ln(m₂/m₃) of every D-trace, and their least-squares slopes against √D over
  200 ≤ D ≤ 300.
- **The exponent ratio:** κ(D) = ln(m₁/m₃)/ln(m₂/m₃).
- **The thread masses** of every class.
- **The data, as seen-data numbers:** the three sectors' ratios and κ from `received/HZ2021_running_masses_MZ.json`.
  For each sector, the number of D-traces whose two log ratios lie within W66's allowance, with z per ratio as in W66
  (a = 0.10, r_calc from V6) and Σz² ≤ 5.991. There is no null, and the frame is blind to the sector, so no claim
  follows from these counts.

## What the outcomes would mean

- **V4 as predicted:** a single point, ω or i or any CM point of class number one, leaves two of the three generations
  massless in this frame. k points give k massive generations. So three need at least three points, or a thread. This
  is the wall as a counting law, read over every point of each D.
- **V8 as predicted:** each D's trace is carried by the threads that rise highest into the cusp. The weave's values in
  this frame are set at the cusp, where GENESIS FK10's unit and the units' poles sit.
- **The law in D, two named outcomes:**
  - **Slopes near 0** (|slope| < 0.1 per unit √D): the ratios approach finite non-zero values. The weave assigns
    definite generation masses in this frame, the same in every sector.
  - **Slopes clearly negative:** the hierarchy grows with D without a bound in the range. Every hierarchy is reached at
    some D, so the numbers need a selection of D, or of the cusp's regularisation. That is the vacuum-selection reading,
    now with a parameter that is named.
- **V5 or V6 failing:** an instrument fault. It is diagnosed post hoc and labelled, and the cell stays failed as worded.

## After the run

- Commit the output unread.
- Then record:
  - the weave dossier's NOTE (a section, a header bullet, a table row and a files entry);
  - the state page;
  - a relay section;
  - the ledger;
  - CHANGELOG and PROGRESS_LOG;
  - a test;
  - a dated note on the fresh look's §4.

0 of 19.

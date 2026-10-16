# W-trace, untwisted: each layer's norm integrals are its deepest pair's (chat1; the frame's own check; no data)

chat1 (the web seat), 2026-10-16, at the owner's go-ahead ("do as u recomend on all"). This is W-trace's first stage
(`READING_THE_RULE_THAT_PICKS_NO_THREAD.md` §4); it was refereed read-only before it left.
- **What was computed.** The untwisted thread frame's cycle integrals on every primitive thread of trace t = 3 to 12
  (29 threads), summed by layer. The instrument is the sealed `tlow2.py`, unchanged, at zero twist: v = R, with W72's
  units and Higgs.
- **Files:**
  - `w_trace_untwisted.py`, its run and `w_trace_untwisted.json`;
  - `closure_at_generic_start.py` and its run.
- **No charge, no twist and no datum enter.** No mass is compared with anything measured. 0 of 19.

## 1. The instrument held

- **Convergence.** Each thread is integrated at n and 1.25n points per unit length. The point count is doubled until
  the two agree to 10⁻²⁰. The deep threads (height ≥ 4.39) needed 60 points per unit, the rest 30. The worst
  agreement:
  - 2.4 × 10⁻²¹ for L⁶R and LR⁶;
  - 1.6 × 10⁻²⁸ for L⁵R and LR⁵;
  - ≤ 4.2 × 10⁻³⁵ for every other thread.
- **Closure.** Every thread closes, to ≤ 3.8 × 10⁻⁴⁶, with the period started at a generic point
  (`closure_at_generic_start.py`).
  - **The probe at the period's first point reads about 2 on LRR's three rotations and LLR's rotation LRL.** On those
    rotations the first point is an image of ω, e^(iπ/3), where Y3x vanishes, so the probe reads 0/0. The Y1 and Y2x
    integrands still close there (the referee's diagnostic: ≤ 5 × 10⁻⁴⁷).
  - Started at a generic point, all six rotations close to ≤ 4.1 × 10⁻⁴⁹. LRR's integrals are unchanged by the start
    to 1.4 × 10⁻³⁷ of each matrix's largest entry. So every thread enters the layer sums.
  - The probe's value is recorded only as a diagnostic.
  - *(The draft of this note read the probe as a defect of the carry, or as a selection of threads. The referee found
    the cause before it left.)*
- **The K integrals' integrands are Hermitian and positive.** §2 rests mainly on them.

## 2. The result: each layer's norm integrals are its deepest pair's

- **Per thread, the norm integrals grow exponentially with the thread's height.**
  - Fits of ln tr K against height over the 29 threads give slopes 11.25 (K32), 10.60 (KM12) and 11.89 (K72).
  - The cusp growth of the units' leading component, |q^(−7/8)|² = e^(2π·(7/4)·y), gives 2π·7/4 = 11.00.
- **So in every layer the deepest pair, L^(t−2)R and its mirror, carries the layer's norm integrals.** The other
  threads' share is:

  | layer t | threads | 1 − the pair's share of K32 | of KM12 | of K72 |
  |---|---|---|---|---|
  | 3, 4, 5, 7, 9 | the pair alone (LR alone at t = 3) | 0 | 0 | 0 |
  | 6 | 3 | 8.8 × 10⁻⁸ | 3.7 × 10⁻⁷ | 2.1 × 10⁻⁸ |
  | 8 | 4 | 2.8 × 10⁻¹⁰ | 1.2 × 10⁻⁹ | 6.9 × 10⁻¹¹ |
  | 10 | 6 | 1.0 × 10⁻¹² | 4.1 × 10⁻¹² | 2.5 × 10⁻¹³ |
  | 11 | 3 | below double precision | | |
  | 12 | 4 | 3.8 × 10⁻¹⁵ | 1.5 × 10⁻¹⁴ | 8.9 × 10⁻¹⁶ |

  At t = 11 the third thread, LLLRRR, sits at height 1.8 against the pair's 5.4.
- **The Yukawa integrals are not dominated the same way.** The pair's Frobenius share of Y1, Y2x and Y3x is:
  - t = 6: 0.61, 0.78, 0.61;
  - t = 8: 0.40, 0.55, 0.37;
  - t = 10: 0.21, 0.37, 0.20;
  - t = 11: 0.50, 0.90, 0.51;
  - t = 12: 0.34, 0.93, 0.36.
- **So the layer's masses are the pair's, moved a little.** The masses are K_L^(−½) Y K_R^(−½), and K is the pair's.
  In C1, ln(m₂/m₃) for the layer, with the pair alone in brackets:
  - t = 3 to 5: −1.00, −5.69, −9.79 (the same);
  - t = 6: −13.27 (−13.38);
  - t = 7: −16.77 (the same);
  - t = 8: −20.01 (−20.09);
  - t = 9: −23.40 (the same);
  - t = 10: −26.30 (−26.68);
  - t = 11: −29.97 (−29.96);
  - t = 12: −32.93 (−33.22).

  The shift reaches 0.38 and does not shrink with t. On average ln(m₂/m₃) falls about 3.5 per unit of trace (6.6 per
  unit of the pair's height √(t² − 4)/2); the step drifts from 4.7 to 3.0.
- **The cells' ranks at zero twist:**
  - C1, C2/THETA2 and C2/ORTH have rank three;
  - C2/E4, C3/E4, C3/THETA2 and C3/ORTH have rank two (the Jacobi zero, R·R = 0), as the record has them.
  - The 10⁻³⁰ rank test separates the two cleanly to t = 12: s₁/s₃ ≥ 10⁻²⁰·² against ≤ 10⁻³⁸·⁶.
- **Both indexings agree.** The deepest pair is primitive at D = t² − 4, so grouping by discriminant gives the same
  dominance.

## 3. What it means for the owner's question (a reading)

- **Unregularised, the no-thread sum is dominated by the cusp.**
  - The units grow exponentially there, so summing a layer without choosing gives its deepest pair the layer's norm
    integrals: to 3.8 × 10⁻¹⁵ (K32), 8.9 × 10⁻¹⁶ (K72) and 1.5 × 10⁻¹⁴ (KM12) by t = 12.
  - The layer's masses are then the pair's, moved by the shallower threads' Yukawa integrals.
  - The pairs are the L·Rⁿ family. The volume reading already found it (13:43 addendum), and the per-field cusp law
    bounds it (19:41).
- **So the selection the owner suspected appears here as the cusp's weight.**
  - This is not a rule that picks a thread. It is the units' growth at the cusp, the puncture around which the
    order-swaps' commutator [LR, RL] loops.
  - That is a reading, not a derivation.
- **Duke's limit is not reached without regularising the cusp.**
  - The record's regularisation, B1654's L, is a cutoff, and a cutoff is a scale.
  - Whether a canonical renormalisation removes the exponential growth without leaving a scale is open. Zagier-type,
    by analytic continuation, is the classical candidate.
  - If it does, the traced frame has a scale-free limit to compare with the surface frame. If it does not, the
    traced rule moves the free choice to the cusp.
- **The scope.** This is the untwisted frame, layers t ≤ 12, with W72's units.
  - The per-field reading shifts the units' cusp exponents (the 19:41 law), but F_i's leading growth stays at least
    7/8, so the same dominance is expected there.
  - That is not computed here.

## 4. For the SM seat and for main

- **For both.** The traced rule's first result in this frame is above. The open question it leaves is whether a
  canonical renormalisation of the cusp exists for these integrands.
- **W95** (the record's invariants traced by discriminant) is the SM seat's, if the owner's ruling reaches it. Its
  invariants may not grow at the cusp, and then they would not be dominated this way.
- **The closure probe's 0/0 at the ω-images** is an instrument note, not a finding. Y3x's integrand vanishing at
  e^(iπ/3) is consistent with the record's zeros at ω (W87, B1657), but that link is not checked here.

chat1, 2026-10-16. 0 of 19.

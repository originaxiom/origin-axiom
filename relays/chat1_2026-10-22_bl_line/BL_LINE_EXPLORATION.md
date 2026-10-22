# Step 1, first look: a flat Wilson line along B − L in main's frame does not produce the Georgi–Jarlskog split where the frame fits (three points, one window)

chat1, 2026-10-22. **EXPLORATORY, labelled.** No cell, no seal, no data in the design; the read-out compares with the
record's targets. Step 1 of chat1's plan (make the Clebsch a frame quantity). Refereed read-only before it left.
0 of 19.

## What was done

- **The frame.** Main's B1720 instrument at 3412bf09d, unchanged, with a second flat line added: each field is twisted
  by q·w + q′·w′. Here q = 6Y and w = aτ + b is the record's hypercharge line; q′ = 3(B − L) (Q 1, u^c −1, d^c −1,
  L −3, e^c 3, the Higgs 0) and w′ = a′τ + b′ is the B − L line, the SM seat's relay §66 proposal (P-084).
  - Every Yukawa bilinear is B − L neutral, so the line is allowed. Main's twist is real-linear in its argument, so
    the instrument computes exactly this twist.
- **The points.** The sealed census's best six-row (0.4 + 2.7i on (2/5, 1/10)) and best nine-row (the same τ on
  (2/5, 1/2)), and the tick's exact d = e line (2/5, 4/5) at ½ + 3.1i.
- **The window.** At each point, a′, b′ ∈ {−0.30, −0.28, …, 0.30}: 2 883 evaluations, every sector with every reading.
  The instrument has period 1 in a′ and b′, so this window is about a third of the B − L line's torus.
- **The order.** `bl_line_scan.py` (9a83cdc15), the read-out `bl_line_readout.py` (f25a49644) and the identity check
  `bl_line_scaling.py` (62eeb7dd0) were each committed before the scan's output existed or was read. The output
  (29ab8441a) and the read-outs (44ba2b9ef) were committed before they were opened. A second read-out,
  `bl_line_readout2.py` (b339ca898 with its output), is post hoc, at the referee's prompt.
- **The smoke test.** At w′ = 0 the instrument reproduces the census instrument exactly (max \|Δ ln\| = 0.0).

## What came out

1. **The exact identity, predicted in writing before the read, holds** [COMPUTED].
   - On the tick's order-5 line, 6Y reduces mod 5 to 1 on Q, u^c, e^c and 2 on d^c, L. And 3(B − L) of (L, e^c) is
     exactly three times that of (d^c, Q).
   - So the leptons' twists are the down quarks' with the legs swapped and w′ replaced by 3w′. With B1698's
     transposition (Y_e = Y_dᵀ on these lines), the singular values must then satisfy leptons(w′) = down(3w′).
   - The frame obeys it to 9.4 × 10⁻¹⁰ in ln, over 1 452 values (both ratios, both horocycles, every reading). On the
     two order-10 lines it fails by 2.5–3.0 in ln, as expected.
   - So on the tick's line the Georgi–Jarlskog ratios are R2(w′) = f₂(3w′)/f₂(w′) and R1(w′) = f₁(w′)/f₁(3w′), with
     f₂ and f₁ the down quarks' m₂/m₃ and m₁/m₃. The 3 is the charges' 3, exactly.
2. **But the frame does not respond the way Georgi–Jarlskog needs.** With no by-hand Clebsch (the w′ = 0 column takes
   the better horocycle):

   | point | model | w′ = 0 | best six over the window (D there) | best six where D is within 3σ of P-094 |
   | --- | --- | --- | --- | --- |
   | (2/5, 1/10), 0.4 + 2.7i | S̃ for every sector | 4.22 | 2.77 (1.52) | 11.7 |
   | (2/5, 1/2), 0.4 + 2.7i | S̃ for every sector | 3.84 | 2.62 (2.00) | 7.3 |
   | tick (2/5, 4/5), ½ + 3.1i | S̃ for every sector | 23.1 | 3.48 (0.27) | 8.6 |
   | tick (2/5, 4/5), ½ + 3.1i | main's readings | 2.33 | 2.31 (2.88) | 7.5 |

   - The line improves the census's best row (4.2 → 2.8), but not to the by-hand Clebsch's 1.51. It is also worse
     than the census's own best without a Clebsch (2.55).
   - **Where D reaches the record's target** (P-094: 10.58 ± 0.11), the six miss by 7.3–11.7 in the table, and by
     7.3–27 with main's readings at the census rows. Over all 27 reading combinations, the best is 7.3 when the down
     quarks and leptons share a reading. Mixed down and lepton readings reach 3.9, but they split d from e by choice.
   - **R2 is often Georgi–Jarlskog-sized** (R2 ≥ 2.5 on 23–30% of the window's rows), **but never with a fitting
     six.** Where R2 and R1 both lie in [2, 4.5], the best six is 14.5 and 63 at the census rows, and no such row
     exists at the tick (reading S̃ in every sector).
   - The D-matched rows are carried by R1 (4.1–55) more than by R2 (0.2–2.6).
   - **The first-order slopes show the imbalance.** At the census's best row (reading S̃, second horocycle), the
     slopes of ln R1 in a′ and b′ are 38 and 13.5, against −10.5 and 1.9 for ln R2. At the tick the first generation
     moves less fast (about 1.4 times the second in a′).
   - From the slopes and that row's baseline (R2 1.02, R1 0.98), matching both data ratios at first order needs
     (a′, b′) ≈ (−0.06, 0.25), \|a′τ + b′\| ≈ 0.27. That is far outside the linear range: at the six nearest grid points R2
     is 0.73–0.94 and R1 0.34–0.68.

## The reading [READING]

- **Why the 3 does not show, on the tick's line.** The identity makes the leptons' ratios the down quarks' at three
  times the B − L argument. R2 would equal the charges' 3 at every w′ only if f₂ were homogeneous of degree one,
  vanishing at w′ = 0, so that the B − L line generates the second generation. R1 = 3 would further need f₁ to fall as
  1/w′, as a fixed determinant would give.
  - In main's frame the hypercharge line already makes all three generations massive at w′ = 0 (on the tick's line
    m₂/m₃ = 0.0253 at reading S, B1698). So the B − L line perturbs an existing hierarchy rather than generating it.
  - At finite w′, R2 reaches 3 often, but never at a row whose six fit.
  - At the order-10 rows there is no identity, and the negative there is empirical.
- **So, on this window and at these points, route (a) did not supply the ingredient.** No row of the window has a
  fitting six together with D at P-094, or with Georgi–Jarlskog-like ratios.
  - It is exploratory: three base points, a third of the w′ torus (spot checks past the tick's edge, by the referee,
    found nothing better), and a step of 0.02.
- **Route (b) is what remains, and it is not yet a derivation.** With the uniform unit O(δ), the weight-3/2 Higgs space
  is three-dimensional (the SM seat's W123, §207), and main's frame uses one direction, ∂R.
  - A Georgi–Jarlskog-type Higgs would be two directions: one with Clebsch 1 in every sector (Pati–Salam's (1, 2, 2))
    and one with 1 for quarks and −3 for leptons ((15, 2, 2), whose B − L generator is diag(1, 1, 1, −3)).
  - But W123 supplies the directions, not their Clebsches. In main's coupling the Higgs section enters every sector
    alike, and sector dependence comes only from the twists. So putting the −3 on a second direction is by hand,
    unless something fixes it. In the E₆ frame only a Higgs outside the 27, the 351′, can (P-084).
  - Main's B1700 (exact) adds that ∂R is the only member of the unit's space holomorphic off v₊, and the only one
    giving a hierarchy. The other two basis directions, E₄²(E₄∂R + E₆R/12)/Δ and E₄E₆·a₀/Δ, carry poles x⁻⁷ and x⁻⁵
    off v₊ and give m₂/m₃ ~ \|q\|⁰ at the cusp. Whether a small admixture of one, with the −3 put on it, splits d from
    e by the needed factor without losing the hierarchy is the open computation.

0 of 19.

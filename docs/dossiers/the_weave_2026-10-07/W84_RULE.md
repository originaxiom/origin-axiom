# W84 — the rule, recorded before the code

The SM-derivation seat, 2026-10-14. Committed before the code that reads it exists. What the seat read and reasoned
while drafting is listed under "Seen before the rule", and the priors were set after that. Nothing here is a result.

## Why this arc

- **chat1's thread frame and its Lagrange law** (`chat1/web-seat` @ 39bfc86fe) are built on this seat's W72 forms. Under
  the hypothesis H-thread, the couplings are cycle integrals along the vacuum thread's closed geodesic. chat1 found
  ln(m₂/m₃) = 7.289 − 7.332·y_max over 59 threads, with y_max half the thread's Lagrange value.
- **The owner's rule: verify load-bearing math.** chat1's numbers rest on this seat's forms, so the seat checks them
  with an independent integrator, at a precision that does not lose the hierarchy.
- **A question the fit raises.** Its slope, 7.332, sits within 0.002 of 7π/3. This arc asks whether the slope is a
  constant at all, and what it tends to deep in the cusp.

## Weave or thread?

- **THREAD results, one thread at a time,** read under chat1's H-thread, which is a hypothesis.
- **The family L^n R is a list read one member at a time** (THE WEAVE rule's "family"). Its slopes are a statement about
  that family. Which thread is the vacuum is open.

## Seen before the rule (disclosed)

- **chat1's two FINDINGS, its scripts, and `thread_frame.json`'s per-thread ratios:**

  | thread | y_max | m₂/m₃ | m₁/m₃ |
  |---|---|---|---|
  | LR | 1.1180 | 0.36877 | 9.568·10⁻³ |
  | LLRR | 1.4142 | 0.035742 | 5.864·10⁻³ |
  | LLR | 1.7321 | 3.3861·10⁻³ | 3.3247·10⁻⁴ |
  | LLRLR | 1.6329 | 0.011807 | 7.663·10⁻⁴ |
  | LLLR | 2.2913 | 5.6076·10⁻⁵ | 3.0489·10⁻⁶ |
  | LLLLR | 2.8284 | 1.5507·10⁻⁶ | 2.4915·10⁻⁸ |

- **The seat's own arithmetic on those numbers,** along L^n R for n = 1 to 4. The local slopes of −ln(m₂/m₃) against
  y_max are 7.64, 7.34 and 6.68, falling. Those of −ln(m₁/m₃) are 5.47, 8.39 and 8.95, rising.
- **The W72 module** (`the_surface_yukawa.py`, unchanged since 87cf7f551). ρ_R's exponents in eighths are e_i 1, v₊ 7
  and v₋ 3. So the matter modes grow at the cusp like q^{−7/8} (F_i), q^{−1/8} (F₊) and q^{−5/8} (F₋). The Higgs mode h
  (ρ′, eighths e_i 3, v₊ 1, v₋ 5) is cuspidal. The Hermitian pairing is diagonal in the three lines.
- **An argument by hand, not a result.**
  - Near the geodesic's apex x moves linearly while y moves quadratically. So in every cycle integral, products of
    different q-powers on a line oscillate and are suppressed deep in the cusp.
  - Then K is nearly diagonal, with K_aa ∝ e^{4π e_a y}, where e = (7/8, 1/8, 5/8) for (F_i, F₊, F₋).
  - Each Y_ab is set by G_ab's coefficient at h's lowest exponents.
  - So Ŷ = (K^{−½})ᵀ Y K^{−½} has a Froggatt–Nielsen texture whose charges are the units' exponents. F₊ is then the
    heaviest state, m₂/m₃ ~ |q|^{2(5/8 − 1/8)} = e^{−2π y}, and m₁/m₃ ~ |q|^{2(7/8 − 1/8)} = e^{−3π y}, up to powers
    of y from the widths.
  - It assumes every pair's lowest pairing exponent is the same, and that the texture's coefficient matrix is generic.
- **Nothing has been computed** for this arc.

## The method (fixed here)

- **The forms** are the W72 module's own: `best_section` for F_i, F₊ and F₋ (weight 3/2) and for R (weight −½, unit on
  v₊), `solve_twisted` for h (weight 5/2, the lowest residual over the three lines, as W72 and chat1 chose), and
  `G_series`. They are evaluated with `ev_vec` and `ev_scal` at mp.dps = 60, at each point's image in the standard
  fundamental domain (y ≥ √3/2).
- **The integrals,** with the seat's own code. K_ab = ∫⟨F_a, F_b⟩ y^{3/2} ds and Y_ab = ∫⟨G_ab, h⟩ y^{5/2} ds, with
  ⟨u, v⟩ = Σ_k u_k v̄_k, over one period of the thread's closed geodesic, by the trapezoid rule. The trapezoid rule is
  spectral for a periodic analytic integrand.
  - The axis comes from the rotation of the word with the least |c|. The arclength is s from the apex, with the nodes
    shifted by half a step from chat1's (s_j = −P/2 + (j + ½)P/N).
  - N = 512, with N = 1024 as the control at the largest thread.
- **The masses** are the singular values of (K^{−½})ᵀ Y K^{−½}, in ascending order, at 60 digits. The states' weights
  are as chat1 defined them.
- **The threads.**
  - V1: LR, LLRR, LLR, LLRLR and LLLR.
  - V2: L^n R for n = 1 to 8, with y_max = √(n² + 4n)/2 exactly.

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **V1, reproduction** | At the five V1 threads, \|Δ ln(m₂/m₃)\| and \|Δ ln(m₁/m₃)\| against chat1's banked values are below 10⁻⁵. | 85% |
| **V2a, the slope is not constant** | Along L^n R, the local slopes of −ln(m₂/m₃) against y_max vary by more than 0.3 from n = 1→2 to n = 7→8. | 80% |
| **V2b, m₂/m₃'s limit** | The last local slope of −ln(m₂/m₃) (n = 7→8) lies within 5% of 2π = 6.283. | 60% |
| **V2c, m₁/m₃'s limit** | The last local slope of −ln(m₁/m₃) lies within 5% of 3π = 9.425. | 55% |
| **V2d, the heaviest** | F₊ carries weight ≥ 0.99 of the heaviest state at every n. | 90% |
| **V2e, the mechanism** | At n = 8, \|K_ab\|/√(K_aa K_bb) < 10⁻³ for every a ≠ b. | 85% |
| **V2f, the control** | At n = 8, N = 512 and N = 1024 give ln(m₂/m₃) and ln(m₁/m₃) equal to 10⁻⁸. | 90% |

**The read-outs (no prior).** Every thread's ratios, K's eigenvalues and the states' weights. The local slopes. A fit of
the local slopes to s_∞ + c/y.

## What a result means, fenced

- **If V1 holds,** chat1's thread-frame numbers reproduce on an independent integrator at 60 digits.
- **If V2a and V2b hold,** the Lagrange law's slope is not constant. Deep in the cusp, ln(m₂/m₃) falls like
  −2π y_max, a power of |q| fixed by the units' exponents, and chat1's 7.33 is an average over the range it fitted.
  "7π/3" is then a coincidence of the range, not a constant.
- **If V2b or V2c fails,** the Froggatt–Nielsen reading is wrong or incomplete, and the seat says which assumption
  failed.
- **In every case:**
  - H-thread stays a hypothesis;
  - the three sectors' differences are untouched (one thread gives every sector the same ratios);
  - the count is unchanged, 0 of 19.

## Discipline

- **The rule is committed before the script, and there is one run.** A failed launch (a crash before the read-out) is
  disclosed and fixed, and does not count.
- **chat1's data is read only from its committed JSON** (39bfc86fe), by `git show`.
- **Each cell is recorded as computed.** A failed prediction is recorded as failed, and post hoc checks are labelled.

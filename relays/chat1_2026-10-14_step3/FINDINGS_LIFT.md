# LIFT: under P4 and P5, main's boundary-class lift carries into the thread frame. Each of the four rank-two cells computed has κ ≥ 0.03 on every admitted thread, and m₁/m₃ → κ/(4πL) once L is large enough

chat1, 2026-10-15.
- **Sealed** at `0be810276` (`PREREGISTRATION_LIFT.md`, sha256 8cb464e6…). The repository ignores `*.out`, so the
  pre-seal logs were force-added at `6916685b8`.
- **The script** `lift_cells.py` was committed at `d02aa207b`, after the seal and before its one run (exit 0, 1035 s).
- **Output** `lift_cells_run.txt` and `lift_cells.json` (`172b40776`), committed before this read-out.
  - The log's first two lines are a SyntaxWarning from importing B1538's `punct_covers.py` out of the extracted
    SM-seat tree. They name the script's own temporary directory. They are harmless and left as written, as in the
    THETA2 and step-3a logs.
  - This sits in tension with WORKING_RULES §11 (scrub sandbox paths from committed files). Those logs are kept as
    their runs wrote them. The path is a generic temporary directory, not the sandbox's working path. If the owner
    wants run logs scrubbed too, all three can be redone together.
- Refereed read-only before leaving. The referee's corrections are taken below.
- Step 1c of chat1's route, at the owner's "goforit".
- **0 of 19.**

## Scored

| | prediction | prior | outcome |
|---|---|---|---|
| Q | the controls hold | 85% | **HOLDS.**<br>(a) The grid against main's route A: 9.2·10⁻¹².<br>(a′) Both against the closed form: 9.1·10⁻¹².<br>(b) All 27 integrand families are invariant to 2.4·10⁻¹², including δ, δ + R and δ + c̃²∘R.<br>(c) The unlifted cells reproduce step 3a and THETA2 at 0.023 of the tolerance.<br>(d) β = (−224, −4, −112), to 1.7·10⁻³⁹.<br>(e) 1.9·10⁻¹⁵.<br>Reported only: (e′), the zero pair, 2.3·10⁻¹⁶ |
| L1 | an instrument check: under P4′ each rank-two cell has m₁/m₃ < 10⁻¹⁰ on every admitted thread | 97% | **FAILS as worded,** in one cell.<br>C2/E4, C3/ϑ² and C3/H-ORTH hold, at most 5.1·10⁻¹⁴.<br>C3/E4 exceeds 10⁻¹⁰ on 5 of 59 admitted threads (1.1–4.4·10⁻¹⁰): LLLLR, LLLLLRR, LLLLLRRR, LLLRRRRR and LLRRRRR.<br>The check measured the double-precision route's floor in C3/E4: up to 4.4·10⁻¹⁰, at most 2.1·10⁻¹⁶·κ (post hoc, below) |
| **L2** | under P4 and P5, κ > 10⁻⁶ on every admitted thread in all four rank-two cells | 88% | **HOLDS.** The least κ:<br>0.032 in C2/E4 (LLRRRRR, 58 admitted);<br>5.89 in C3/E4 (LR, 59);<br>0.545 in C3/ϑ² (LLLRRRRR, 59);<br>1.23 in C3/H-ORTH (LLLRRRRR, 59) |
| L3 | at L = 10⁷, 4πL·m₁/m₃ agrees with κ to 1% on every admitted thread | 85% | **HOLDS.** The worst cases:<br>1.2·10⁻⁴ in C2/E4 (LLRRRRR);<br>9.7·10⁻⁸ in C3/E4;<br>8.9·10⁻⁶ in C3/ϑ²;<br>6.8·10⁻⁶ in C3/H-ORTH.<br>The sealed read-out at L = 1000 is in the next section |
| L4 | at the root, κ ∈ [0.01, 10] in all four cells | 55% | **HOLDS.** The root's κ: 0.226 in C2/E4, 5.89 in C3/E4, 2.19 in C3/ϑ² and 4.19 in C3/H-ORTH |

**Four of five cells hold.** The one that failed, as worded, had the highest prior.

**C2/E4 admits 58 threads, not 59.**
- LLLLLRR fails the N = 256 against 384 check, at 1.6·10⁻⁵ against 10⁻⁵. THETA2 admitted it.
- The disagreement is in κ, by inference: the JSON keeps only the larger of the two. The m₂/m₃ integrals are THETA2's
  (Q(e), 1.9·10⁻¹⁵), and THETA2's N agreement on m₂/m₃ for this thread is 1.4·10⁻⁸.
- Its mirror, LLRRRRR, passes at 8.7·10⁻⁶. It supplies both the cell's least κ and L3's worst case, so both sit at the
  admission edge.

## Where first order holds, and what happens beyond it

These are the sealed L3 read-out at L = 1000 and further read-outs from the same output.

**How often the exact P4 masses depart from first order.**

| cell (admitted) | off > 10% at L = 1000 (worst) | at L = 100 | at L = 10 |
|---|---|---|---|
| C2/E4 (58) | 3 (0.27) | 15 | 24 |
| C3/E4 (59) | 27 (1.00) | 44 | 58 |
| C3/ϑ² (59) | 8 (0.64) | 26 | 59 |
| C3/H-ORTH (59) | 12 (0.80) | 35 | 59 |

- **The working conditions are κ ≪ 4πL·m₂/m₃ and |c̃|/(2πL) ≪ 1.** The first keeps the first-order lift εκ below the
  second generation; the second keeps the 1/L expansion itself valid.
  - The preregistration named only 4πL·m₂/m₃ ≫ |Δc̃|. That is not enough when κ ≫ |Δc̃|.
  - On C3/E4's LLLLLRR at L = 1000, 4πL·m₂/m₃ ≈ 900, yet first order is off by about 100%.
  - In C3/E4 the first condition is sufficient but not necessary, because the (R, E4·R) corner nearly decouples. On
    LLLLLRR at L = 10⁷, εκ/(m₂/m₃) = 0.63, yet first order agrees to 2.6·10⁻⁸. In the other cells that ratio is at
    most 2.3·10⁻⁵ at L = 10⁷.

**Where εκ passes m₂/m₃,** the lifted state is no longer the lightest.
- This comes from comparing first-order sizes. The exact-L eigenvectors were not computed.
- The exact values agree with it. At the root of C3/E4 at L = 10, m₁/m₃ = 0.0181 (the unlifted m₂/m₃ was 0.0184) and
  m₂/m₃ = 0.0487 (εκ = 0.047).

| cell | L = 10 | L = 100 | L = 1000 |
|---|---|---|---|
| C2/E4 | 11 | 0 | 0 |
| C3/E4 | 59 | 44 | 31 |
| C3/ϑ² | 21 | 4 | 0 |
| C3/H-ORTH | 28 | 6 | 0 |

- **Where εκ > 1, the lifted state becomes the heaviest.** This happens only in C3/E4: on 53, 41 and 25 of its 59
  threads at L = 10, 100 and 1000.
  - The remaining two are then suppressed by about 4πL/κ.
  - Example: on LLLLLRR at L = 10, m₁/m₃ = 1.5·10⁻⁶ and m₂/m₃ = 2.3·10⁻⁵.
- **At the root, at L = 10,** the lifted state passes the second generation in C3/E4 (εκ = 0.047 against 0.018) and in
  C3/H-ORTH (0.033 against 0.022). It does not in C3/ϑ² (0.017 against 0.033) or in C2/E4 (0.0018 against 0.485).

## L1's failure: the floor of the pointwise route in C3/E4 (post hoc, from the committed output)

**The floor follows κ, in C3/E4 only.**
- There, P4′ m₁/m₃ divided by κ runs from 1.0·10⁻¹⁸ to 2.1·10⁻¹⁶, with median 1.5·10⁻¹⁷.
- log(floor) against log(κ) has slope 1.19 over six decades.
- Spearman(κ, floor) = 0.98 cannot by itself separate κ from height, because Spearman(y_max, floor) = 0.97. The slope is
  what separates them.

**Mirror threads agree.**
- Ten admitted threads have κ ≥ 7.1·10⁵, and five of them pass.
- Mirror pairs have identical κ and straddle the threshold. For example, LLLLR fails at 1.5·10⁻¹⁰ while its mirror
  LRRRR passes at 7.8·10⁻¹¹, both at κ = 2.04·10⁶.
- So the failure is numerical.

**Why the floor follows κ in C3/E4.**
- Y_R has a zero row and a zero column there, so the null pair picks out a single entry of Y_δ, the (R, E4·R) entry.
  - The R row: G(R, Y; R) = (R·R)Y.
  - The E4·R column: G(X, E4·R; R) = E4·[(R·X)R − (X·R)R] + E4(R·R)X = E4(R·R)X.
  - Both vanish by Jacobi's R·R = 0.
- Under P4′ that row and column carry R·R, which in double precision is machine precision times |R|².
- κ's entry is G(R, E4·R; δ)·h̄ = 2E4·(δ·R)·(R·h̄), with δ·R = Σ c̃_r R_r². It has the same shape.
- THETA2's 40-digit series route gave the same five threads 2–8·10⁻²¹.

**The other three cells behave differently.**
- Their floors are at most 5.1·10⁻¹⁴.
- They rise with height and anti-correlate with κ (Spearman −0.79, −0.75, −0.77).
- floor/κ reaches 5.5·10⁻¹³ in C2/E4, 2.8·10⁻¹⁴ in C3/ϑ² and 1.8·10⁻¹⁴ in C3/H-ORTH.

**The sealed margin read-out:** the largest P4′ m₁/m₃ divided by εκ at L = 10⁷ is:

| cell | margin |
|---|---|
| C2/E4 | 6.9·10⁻⁵ |
| C3/E4 | 2.6·10⁻⁸ |
| C3/ϑ² | 3.5·10⁻⁶ |
| C3/H-ORTH | 2.3·10⁻⁶ |

So the floor does not reach L2 or L3.

## Read-outs (no prior)

**κ over the admitted threads, and m₂/m₃ for comparison.**

| cell | κ range | Spearman(y_max, ln κ) | m₂/m₃ range | the root's κ | 4πL·m₁/m₃ at L = 10, 100 (root) |
|---|---|---|---|---|---|
| C2/E4 | 0.032–0.65 | −0.86 | 8.5·10⁻⁵–0.48 | 0.226 | 0.237, 0.227 |
| C3/E4 | 5.89–5.7·10⁶ | **+0.99** | 0.018–0.93 | 5.89 (the least) | 2.28, 5.91 |
| C3/ϑ² | 0.55–3.7 | −0.85 | 3.5·10⁻⁴–0.31 | 2.19 | 1.69, 2.19 |
| C3/H-ORTH | 1.2–10.6 | −0.90 | 5.1·10⁻⁴–0.31 | 4.19 | 2.14, 4.16 |

- **In C3/E4, κ grows steeply with the thread's height:**
  - 5.89 at LR (y_max 1.12);
  - 210 at y_max 1.56 and 460 at 1.68;
  - 7.1·10⁵ at 2.81, 2.0·10⁶ at 2.83 and 5.7·10⁶ at 2.96.

  It exceeds 10³ on 44 of 59 threads. Why the normalised (R, E4·R) entry grows like this was not computed. In the other
  three cells κ varies by a factor of 7–20 and falls with height.
- **The hierarchy depends strongly on the thread in every cell,** through m₂/m₃ as well as κ.
- **The common shift** leaves κ unchanged at the root, to 8.6·10⁻¹⁶, which is the identity. **The covariant channel
  shift** δ + c̃²∘R changes it by 315–328% in every cell. So κ responds to the channel weights.
- **The anchor.** On one fibre, B1654's L·m₁/m₃ ≈ 0.11–0.17 at i and t1 corresponds to κ ≈ 1.4–2.1. The root's κ in
  the three C3 cells is 2.2–5.9, the same order. C2/E4's is six to nine times smaller.
- **The root's κ ratios, which do not depend on L:**
  - C3/E4 : C3/H-ORTH : C3/ϑ² = 2.69 : 1.91 : 1;
  - C2/E4 / C3/E4 = 0.038.
- **The rank-three cells at the root, under P4,** move by O(1/L) relative.

  | cell | unlifted | L = 10 | L = 100 |
  |---|---|---|---|
  | C1 | 0.00957 | 0.00926 | 0.00954 |
  | C2/ϑ² | 0.544 | 0.549 | 0.545 |
  | C2/H-ORTH | 0.618 | 0.602 | 0.616 |

- **For the record only:** the L at which the root would reach each sector's m₁/m₂ (HZ2021 at M_Z), from
  m₁/m₂ = κ/(4πL·m₂/m₃).
  - At the root, to first order, m₁/m₂ = 0.037/L (C2/E4), 25/L (C3/E4), 5.2/L (C3/ϑ²) and 16/L (C3/H-ORTH).
  - These hold only for L much larger than the coefficient, and with |c̃|/(2πL) ≪ 1.

  | cell | up | leptons | down |
  |---|---|---|---|
  | C2/E4 | 18.7 | 7.8 | 0.74 |
  | C3/E4 | 1.3·10⁴ | 5.4·10³ | 506 |
  | C3/ϑ² | 2.6·10³ | 1.1·10³ | 104 |
  | C3/H-ORTH | 7.8·10³ | 3.3·10³ | 309 |

  This is not a value contact.
  - L, the end condition and the cell assignment are free.
  - The root cannot host all three sectors' 2–3 ratios (the route's read-out 1b). C2/E4's m₂/m₃ = 0.485 matches no
    sector's.
  - C2/E4's 0.74 lies outside the expansion itself. The 1/L expansion needs |c̃|/(2πL) ≪ 1, and there c̃₃(i) ≈ −3.9
    against 2πL ≈ 4.6.
  - In the C3 cells, L of 10²–10⁴ means an end cutoff ε ~ e^(−10²) to e^(−10⁴).

## What it shows

1. **Under P4 and P5, B1654's lift survives in the thread frame.** [SEALED, L2 and L3; conditional on P5]
   - In each of the four rank-two cells computed, on every admitted thread, the null pair's first-order lift is
     nonzero: κ ≥ 0.03, up to 5.7·10⁶. The thread integral does not cancel it.
   - Where κ ≪ 4πL·m₂/m₃ and |c̃| ≪ 2πL, the first generation gets m₁/m₃ = κ/(4πL). L3 confirms this at L = 10⁷ on
     every admitted thread.
     At L ≤ 1000 it fails on some threads in every cell (the table above).
   - So, under P5 (a global normalisation is untested), the rank-two zero in this frame belongs to the end condition
     P4′, not to integration. This is B1654's statement at a point, carried along a thread.
2. **At the root, κ is 2–6 in the (−½, 7/2) cell and 0.23 in the (3/2, 7/2) cell under E4·F.** [SEALED, L4; the values
   are read-outs]
   - So the first generation's suppression is 1/(4πL) times κ, and m₁/m₂ falls like 1/L.
   - This is a logarithmic hierarchy in the cutoff. [read-out; root only; first order; P5; L free; cell assignment
     free]
   - The cost: in the C3 cells the observed m₁/m₂ would need L ~ 10²–10⁴.
3. **The (−½, 7/2) cell under E4·F has a zero row and a zero column.** [algebra] Its κ grows by six orders of magnitude
   with the thread's height. [read-out]
   - So at moderate L, on most C3/E4 threads, the lifted state is not the light one. It passes the second generation on
     all 59 at L = 10, and becomes the heaviest on 53, 41 and 25 at L = 10, 100 and 1000.
   - Where it is heaviest, the other two are suppressed by about 4πL/κ.

## Fence

- **Conditional on P5,** that P4 is imposed fibre by fibre. A global per-channel normalisation is not computed.
- **Which end condition is physical,** P4 or P4′, is not decided. Under P4′ the zero stays, to the numerical floor.
- **L is free.** So is the cell assignment.
- **Not tested:**
  - sectors (main's twisted channels);
  - CP;
  - the (7/2, 7/2) cell;
  - any value.
- **The object:** W72's framework, B1644's coupling, B1654's c_r from main's route A, and Lyndon words to length 8
  with y ≤ 3.
- **0 of 19.**

## For main

> **Dated note, 2026-10-15, 11:55: priority and proof belong to the SM seat's W87.**
> - **W87 proved the closed form first.** Its rule is at `3274265c1` (08:34), and it was recorded at `adeb6f909` (08:52)
>   in relay §114, before chat1's pre-seal reviewer found it independently (about 09:26).
>   - W87 proves c_r = −2π·ln((π/2)|θ_r(0)|²) by Parseval in the strip, with Euler's and Gauss's identities.
>   - Its three routes agree to 10⁻⁴⁰.
>   - It gives D = −θ₃⁴h(λ)/(4πη⁶), with λ = θ₂⁴/θ₃⁴ and h(λ) = λ·ln|λ| + (1 − λ)·ln|1 − λ|. D's zero set is exactly
>     ω's orbit.
> - **So "a numerical identity, not proved here" is superseded:** the closed form is W87's theorem.
> - **chat1 missed §114** because its repository fetched only main and chat1's own branch. The fetch is now fixed.
> - **A consequence of W87's end-condition family** (u_r = G(2πL + c_r)R_r; by expansion, not computed here):
>   - LIFT's κ is the same for every channel-blind G with G′ ≠ 0;
>   - only the prefactor changes, with m₁/m₃ → (G′/G)(2πL)·κ;
>   - P4's G = √x gives LIFT's 1/(4πL);
>   - P5 is still needed.

**The closed form,** found by chat1's pre-seal reviewer after W87 had proved it (note above):
c_r(τ) = −4π·ln|θ_r(0|τ)| − 2π·ln(π/2).
- At first reading it was called a numerical identity. W87 proves it.
- It matches route A to 9·10⁻¹² at this run's 20 Q(a′) points. Before the seal (`closed_form_c.out`) it matched to
  4.5·10⁻¹¹ at τ = 1.411 + 0.899i.

**B1654's D(τ) = −4π·Σ_r R_r²·ln|θ_r(0|τ)|.**
- The constant drops because Σ_r R_r² = R·R = 0.
- The referee reproduced B1654's values from it: |D|/|R|² = 1.0888 at i, D(ω) = 0 (9·10⁻³¹), and the cusp law
  (350.2337 against the predicted 350.2342 at 5i).

**κ per thread and cell** is in `lift_cells.json`, for main's twisted channels (route step 1d) to set beside.

chat1, 2026-10-15.

# SM-C7 — the slope and the Kronecker function are two coefficients of one L-function, on the thread's own geodesic

*Card SM-C7 (`relays/cards/SM_C7_the-slope-and-the-channel-norm-one-l-function.md`). Steps 0 to 2 were approved by
main (docs/seats/sm.md, M15, M17), and run ahead of SM-C6 at the owner's word. Step 0 was sealed and pushed
(ae5f6d7d1) before the population was computed. Data-free: no measured value is read, B1656 is not read, and steps 3
and 4 are not run. Main read at f503b1f38.*

## The outcome

**The identity holds, with its two coefficients, on all 601 characters at all 16 levels of B1737's population.** It
is not outcome C. Every expectation sealed in step 0 was met, and every planted control failed as it had to. The
reading of outcomes A, B and D needs step 3, which main holds.

With c = (i, j)/N the character's point, Jc = (−c₂, c₁) its dual point, γ = Mᵀ acting on the modulus, and the thread's
closed geodesic run once from z₀ to γz₀:

1. **The value coefficient (step 1).** B1737's slope is a period along the thread's geodesic:

   s(χ) + ½·#(−I) = Z(0, χ) = (1/4π²) ∫ from z₀ to γz₀ of G^(Jc)*(z) dz.

   - G^(u)* is the weight-2 Eisenstein series summed over the shifted lattice u + ℤ², in Hecke's limit (minus π/y).
   - Max difference over 601 characters: 2.3 × 10⁻¹⁴.
   - 48 and 96 quadrature nodes agree to 5.9 × 10⁻¹³, and the period does not depend on z₀.
2. **The Kronecker coefficient (step 2).** The same L-function's value at s = 1 is the arc-length integral, along the
   same geodesic, of the Kronecker-limit function. That function is the log of a Siegel function, a theta quotient:

   Z_tot(1, χ) = (2/π) ∫ over one period of E_c(z, 1) ds = −4 ∫ over one period of log|g_Jc(z)| ds.

   - Here Z_tot(s, χ) = Σ over v in (ℤ² − 0)/⟨M⟩ of χ(v)|Q(v)|^{−s}, computed from cone sums, independently of the
     integral.
   - Max relative difference: 4.7 × 10⁻¹²; at s = 2 (Hecke's formula as a check): 3.8 × 10⁻¹².
3. **Its odd partner at s = 1, from the same function.**
   - The period of G_c = −2πi ∂ log g_Jc along the geodesic equals Z_same(1, χ) − Z_opp(1, χ) (max difference
     6.1 × 10⁻¹²).
   - It is 4π² times a rational number on every character: the winding of g_Jc's argument. The denominators run from 1
     to 96, and the residual is 1.6 × 10⁻¹³.
4. **At s = 0 the total carries no character information beyond the slope.**
   - Z_tot(0, χ) = 0 (6 × 10⁻¹¹) and Z_tot′(0, χ) = −ℓ/2 (3.5 × 10⁻¹⁰) on every character, with ℓ the geodesic's
     length.
   - So the information sits in two places:
     - the cone value at 0, which is the slope;
     - the value at 1, which is the Kronecker coefficient.

**In one sentence:** on each thread, one Siegel function g_Jc, read along the thread's own closed geodesic, gives:
- the Kronecker coefficient, through its modulus;
- the odd part, through its argument;

and the slope comes from the dual-shifted weight-2 Eisenstein series along the same geodesic. No point τ on the
geodesic is chosen anywhere: the thread supplies the whole computation.

## Level by level

| level | N | characters | step 1: max diff | step 2(b): max rel. | step 2(c): max diff | value range | Kronecker coefficient Z_tot(1) range | L_odd(1)/4π² denominators |
|---|---|---|---|---|---|---|---|---|
| +LR 2 | 5 | 4 | 1.7e-16 | 1.6e-14 | 8.6e-14 | -0.4472 to 0.4472 | -3.0979 to -3.0979 | 5 |
| +LR 3 | 4 | 15 | 6.1e-16 | 3.2e-14 | 4.1e-14 | -1.0000 to 1.0000 | -5.3368 to -1.3342 | 1, 4 |
| +LR 4 | 15 | 44 | 4.2e-15 | 2.5e-13 | 7.9e-13 | -2.6180 to 2.6180 | -6.1958 to 4.8438 | 3, 5, 15 |
| +LR 5 | 11 | 120 | 2.0e-14 | 4.7e-12 | 3.9e-12 | -6.9112 to 6.9112 | -7.7539 to 14.7175 | 1, 11 |
| +LLR 3 | 10 | 49 | 1.8e-15 | 2.2e-12 | 1.8e-12 | -2.6180 to 4.2361 | -10.9541 to 11.4494 | 2, 10, 20 |
| +LLLR 3 | 18 | 107 | 1.6e-14 | 2.9e-12 | 6.1e-12 | -5.0000 to 12.1702 | -14.8698 to 27.5944 | 1, 2, 3, 6, 9, 18 |
| +LLRLR 2 | 48 | 95 | 2.3e-14 | 1.0e-12 | 4.3e-12 | -5.0273 to 7.8751 | -9.7821 to 17.5591 | 1, 2, 3, 4, 6, 8, 12, 24, 32, 96 |
| -LR 1 | 5 | 4 | 6.5e-17 | 7.2e-14 | 8.0e-14 | -0.2236 to 0.2236 | -1.5490 to -1.5490 | 10 |
| -LR 2 | 5 | 4 | 1.1e-16 | 1.6e-14 | 8.6e-14 | -0.4472 to 0.4472 | -3.0979 to -3.0979 | 5 |
| -LR 3 | 10 | 19 | 8.6e-16 | 1.4e-12 | 8.5e-13 | -1.1180 to 1.1180 | -5.3368 to 0.0000 | 1, 5, 10 |
| -LR 4 | 15 | 44 | 4.2e-15 | 2.5e-13 | 7.9e-13 | -2.6180 to 2.6180 | -6.1958 to 4.8438 | 3, 5, 15 |
| -LLRLR 1 | 12 | 11 | 8.4e-16 | 5.4e-13 | 4.7e-13 | -1.0000 to 0.5000 | -4.8910 to 0.7325 | 4, 8, 12, 24 |
| -LLLRLR 1 | 15 | 14 | 8.9e-16 | 2.8e-13 | 6.7e-13 | -1.6708 to 0.5000 | -5.8977 to 4.3090 | 3, 15 |
| -LLR 2 | 6 | 11 | 4.5e-16 | 1.5e-12 | 6.2e-13 | -1.0000 to 1.0000 | -7.3028 to 0.0000 | 3, 6 |
| -LLR 3 | 18 | 53 | 5.3e-15 | 1.6e-12 | 1.7e-12 | -4.9115 to 2.0321 | -10.9541 to 12.8397 | 2, 4, 6, 12, 18, 36 |
| -LLRR 1 | 4 | 7 | 2.3e-16 | 1.4e-14 | 5.0e-14 | -0.5000 to 0.5000 | -4.8874 to -1.2218 | 1, 4, 8 |

Value range: s(χ) + ½#(−I). Kronecker coefficient: Z_tot(1, χ), the L-function's own arithmetic, not B1656's frame
norm, which step 4 would tabulate and which is held.

## The planted controls

| control | what was planted | caught |
|---|---|---|
| P1 | a character the monodromy does not fix, in place of χ (step 1) | 466 of 466 |
| P2 | the geodesic of M′ = [[t − 1, 1], [t − 2, 1]], same trace t, same c (steps 1 and 2(b)) | 601 of 601; 601 of 601 |
| P3 | the period run from γz₀ to z₀ (step 1) | 572 of 572 with a value above 10⁻⁶ |
| P4 | a factor 2 on G^(Jc)* (step 1) and on E_c (step 2(b)) | 572 of 572; 565 of 565 with a value above 10⁻⁶ |

P1 applies to 466 characters, not 601. At +LR 3 (N = 4) and +LR 5 (N = 11), M ≡ I mod N, so every character of that
modulus is fixed and no wrong character exists there. The 29 characters with slope value 0 (P3, P4) and the 36 with
Kronecker value 0 (P4 in step 2(b)) cannot show a sign or a factor; this was said before the run.

## What is classical, and what is new here

- **Classical** (from memory, as the card says):
  - Hecke's integral representation of the zeta of a real quadratic order;
  - Kronecker's second limit formula, with the Siegel function;
  - the Shintani and Sczech cone cocycle at s = 0, which B1737 already identified.

  The identities above are instances of these.
- **New for the record:**
  - that they hold in the record's own conventions, on B1737's population, to 10⁻¹¹ or better;
  - which object carries each coefficient: the dual point Jc, the u-shifted series for the value, the v-twisted series
    and its Siegel function for the Kronecker coefficient;
  - that the derivative at 0 is universal;
  - that B1737 § 4's "τ-only term" is not needed. The Kronecker coefficient is a number of the thread, an integral
    along its own geodesic, with no modulus τ supplied.
- **Not shown here:**
  - whether B1656's channel norm c_s is this Kronecker coefficient, at a point of the geodesic or as its average.
    That is step 3, held for a sealed card;
  - nothing here selects a line, a modulus, or any value compared with measurement.

## Disclosed

- **The order of the work.** SM-C7 ran before SM-C6 at the owner's word; main had put SM-C6 first.
- **The population was dumped** with main's own B1737 code in a worktree of main at f503b1f38, outside the tree. B1737
  and B1438 are identical there to main's head at the seal.
- **Bugs found and fixed during calibration**, on matrices outside the population, before the seal:
  - the c₂ = 0 Fourier modes were summed with a power-law truncation;
  - the geodesic's fixed points were ordered wrongly when b < 0;
  - the negative-trace cone sum counted one orbit of each pair.

  Each was caught by a calibration check and fixed there. None of these was found on the population.
- **The step-1 convention,** u-shifted at Jc, was chosen among four declared family members on calibration
  characters only. The population then confirmed it out of sample.

## Files

- **`relays/sm_c7/STEP0_CONVENTIONS_AND_EXPECTATIONS.md`** and **`relays/sm_c7/expectations.json`**: sealed first.
- **`relays/sm_c7/sm_c7_lib.py`**: the instruments.
- **`relays/sm_c7/calibration/`**: nine calibration scripts and `relays/sm_c7/calibration/calibration_run.txt`.
- **`relays/sm_c7/population.json`**: B1737's population, dumped by `relays/sm_c7/dump_population.py`.
- **`relays/sm_c7/run_c7.py`**: steps 1 and 2 and the plants.
  - Output: `relays/sm_c7/sm_c7_results.json`, one row per character, with every number above.
  - Run: `relays/sm_c7/RUN.txt`, 2 471 s.

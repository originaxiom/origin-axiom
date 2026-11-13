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

## Steps 3 and 4 (released by main, M19), sealed first at 664c04531

*B1656 was read only for its kernel and its regularised norm, in `relays/sm_c7/b1656_kernel.py`, its definitions
copied unchanged. No value was set beside a measured number. The step-4 table is committed and compared with nothing.
Conventions and expectations: `relays/sm_c7/STEPS34_CONVENTIONS_AND_EXPECTATIONS.md`.*

### The outcome: A, for the thread's shifted partial zeta. The channel norm matches only as the average, never at the apex

1. **What B1656's channel norm is.**
   - At every thread's apex, for all 601 lines and all four channels (2 383 entries with a frame value):

     c_s(τ, ū) = F_{u_s}(τ) + π log Im τ − 2π(γ + log π),

     with a largest residual of 4.2 × 10⁻¹¹.
   - F_u is the Kronecker limit, at s = 1, of the lattice sum shifted by u.
   - u_s is the real coordinates of the summed twist ū, plus the channel's half-period: 1: 0; i: (0, ½); j: (½, 0);
     k: (½, ½).
   - The remaining τ-dependence, π log Im τ − 2π(γ + log π), is one function, the same for every line and channel.
2. **That τ-only part is not modular.** It moves by −π log|τ|² under τ → −1/τ (calibration). Along a thread, the
   frame's own c_s averaged over one period depends on where the period starts: it moved by 0.56 to 3.9 between two
   windows, on all 16 levels. The line part F_u does not move (3 × 10⁻¹²).
3. **The line part's average is the thread's partial zeta.**
   - By the shifted Hecke formula (checked at s = 2 to 2.3 × 10⁻⁸ on every level), the line part's average along the
     thread's closed geodesic is the Kronecker limit, at s = 1, of the thread's shifted partial zeta
     Σ over v in (u + ℤ²)/⟨M⟩ of |Q(v)|^{−s}.
   - For channel 1, u = Jc: that is the same partial zeta whose odd part at s = 1 is 4π² times the slope (step 1).
   - **So the slope and the channel norm are two coefficients of one L-function, the shifted partial zeta at Jc.** The
     slope is its odd value at s = 1; the norm's line part, averaged along the thread, is its even Kronecker limit.
4. **Not at the apex.** On all 1 476 closed entries the line part at the apex differs from its average (by more than
   10⁻⁶). The apex is not a point where the norm equals the L-function's coefficient: not outcome B.
5. **Not the twisted coefficient of step 2.**
   - On every level with at least three distinct values, the line part is not an affine function of step 2's
     (π/2ℓ)Z_tot(1, χ_c): the residual runs from 0.17 to 23. On −LLR 2 and −LLR 3, two characters share Z_tot(1)
     but differ in the norm.
   - The norm is the finite Fourier transform of the twisted coefficients: a shift, not a character.

### Level by level (channel 1; every entry is in `relays/sm_c7/sm_c7_steps34_results.json`)

| level | apex τ | characters | closed entries | max identity resid. | line part ⟨F⟩, channel 1 (range) | frame c₁ at the apex (range) | frame average moves by |
|---|---|---|---|---|---|---|---|
| +LR 2 | 0.5000+1.1180i | 4 | 4 | 1.4e-12 | 8.9068 to 8.9068 | -1.6870 to -1.4339 | 1.45e+00 |
| +LR 3 | 0.5000+1.1180i | 15 | 60 | 8.1e-13 | 8.3934 to 12.7486 | -2.8597 to 10.5214 | 2.29e+00 |
| +LR 4 | 0.5000+1.1180i | 44 | 44 | 9.5e-12 | 8.9068 to 23.3016 | -2.9827 to 42.5073 | 3.10e+00 |
| +LR 5 | 0.5000+1.1180i | 120 | 120 | 4.2e-11 | 8.9561 to 46.8594 | -3.0170 to 127.4640 | 3.90e+00 |
| +LLR 3 | -0.0000+1.7321i | 49 | 98 | 5.0e-12 | 7.2144 to 36.7833 | -2.9458 to 37.9316 | 3.19e+00 |
| +LLLR 3 | 0.5000+2.2913i | 107 | 428 | 6.0e-12 | 6.9308 to 85.2354 | -2.8374 to 95.0174 | 3.80e+00 |
| +LLRLR 2 | 0.0000+1.6330i | 95 | 380 | 8.0e-12 | 8.0651 to 56.0352 | -2.9852 to 150.5856 | 3.71e+00 |
| -LR 1 | 0.5000+1.1180i | 4 | 4 | 6.3e-13 | 8.9068 to 8.9068 | -1.6870 to -1.4339 | 5.62e-01 |
| -LR 2 | 0.5000+1.1180i | 4 | 4 | 1.4e-12 | 8.9068 to 8.9068 | -1.6870 to -1.4339 | 1.45e+00 |
| -LR 3 | 0.5000+1.1180i | 19 | 76 | 1.2e-12 | 8.3934 to 14.7137 | -3.0225 to 14.6590 | 2.29e+00 |
| -LR 4 | 0.5000+1.1180i | 44 | 44 | 9.5e-12 | 8.9068 to 23.3016 | -2.9827 to 42.5073 | 3.10e+00 |
| -LLRLR 1 | 0.0000+1.6330i | 11 | 22 | 4.4e-12 | 8.0651 to 15.0997 | -2.9121 to 9.9414 | 1.78e+00 |
| -LLLRLR 1 | -0.5000+2.1409i | 14 | 14 | 5.0e-12 | 8.1823 to 21.2117 | -2.3223 to 16.6250 | 2.01e+00 |
| -LLR 2 | 0.0000+1.7321i | 11 | 44 | 1.0e-12 | 7.2144 to 14.5691 | -2.9458 to 14.8611 | 2.08e+00 |
| -LLR 3 | -0.0000+1.7321i | 53 | 106 | 8.2e-12 | 7.2144 to 39.5528 | -2.9458 to 41.2218 | 3.19e+00 |
| -LLRR 1 | -0.0000+1.4142i | 7 | 28 | 7.6e-13 | 7.0656 to 11.4208 | -3.1296 to 4.5859 | 1.30e+00 |

### The step-4 table

- **`relays/sm_c7/sm_c7_steps34_results.json`**, one row per character, with for each channel:
  - **canonical, when u_s is closed:** ⟨F_u⟩, the line part averaged along the thread;
  - F_u at the apex;
  - B1656's c_s at the apex;
  - the frame's c_s averaged on the representative's semicircle, for both windows, stated as not canonical;
  - whether u_s is closed.
- 1 476 of the 2 404 channel entries are closed. Of the 2 404, 21 have no frame value, because R_s = 0 there.
- Nothing in it is compared with anything.

### Expectations: seven held as sealed, two did not

- **Held:** 3a, 3b (both parts), 3c, 3d, P6 (2 383 of 2 383) and P7 (2 362 of 2 383).
  - P7's 21 misses are characters with c ≡ ±Jc, where the plant changes nothing.
- **3e did not hold as sealed.**
  - It asked for a residual above 10⁻³ on every level with at least four characters. On +LR 2, −LR 1 and −LR 2 the
    four characters take one value, and on +LR 3 the fifteen take two; an affine fit through one or two points is
    exact.
  - The sealed criterion counted characters where it should have counted distinct values. On all twelve levels with
    three or more distinct values it holds.
- **P5 did not hold as sealed: 2 129 of 2 383, not 99%.**
  - Of the 254 misses, 16 are exactly zero: the wrong shift equals ∓ the right one, and F_u = F_{−u}.
  - The other 238 are real differences of 1.6 × 10⁻⁷ to 7.3 × 10⁻⁷. That is about 4 000 times the identity's
    residual, but under the sealed 10⁻⁶. They lie on the threads whose apex has Re τ = ±½, where channels j and k
    nearly coincide.
  - The threshold was set too coarse. The identity distinguishes the channels at its own precision.
- No conclusion above rests on 3e or P5. Nothing was adjusted after the run.

### What this does and does not do

- **It does:**
  - B1737 § 4's follow-on is answered, in corrected form. The channel norm and the slope are coefficients of one
    L-function, the thread's partial zeta shifted by the line, and only as an average along the thread's own
    geodesic. No point of the modulus is singled out.
  - The frame's norm carries one universal, non-modular τ-term. Its absolute values depend on the representative τ
    used; differences between lines and channels at one τ do not.
- **It does not:**
  - choose a line;
  - compare anything with a measured value. That is the comparison step, for later (M19).

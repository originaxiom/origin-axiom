# B1917 — The slope and the Kronecker function are two coefficients of one L-function, read along the thread's own geodesic (the SM seat's SM-C7 steps 1 and 2, verified on main)

**Verdict: PROVED** (numerically: the seat's identity on all 601 characters, checked by main's own code; Hecke's formula
at s = 2 in the same conventions; the value at s = 1 against a direct sum). cc (main), 2026-11-13 (S306p). Data-free:
no measured value is read and B1656's frame is not evaluated. **0 of 19.**

## 1. The answer first

- **The question** (B1737 § 4, L233's follow-on, Review 74's second lead; the debt P-384 rests on it): B1737 showed that
  the slope law's s(χ) is a twisted zeta value at s = 0. Are the slope and the channel norm's kind of quantity two
  coefficients of one L-function? The SM seat's card SM-C7 put it in a well-posed form by Hecke's integral formula:
  along the thread's own closed geodesic on the modular surface.
- **The seat's result** (`relays/SM_C7_ONE_L_FUNCTION.md` @ `e47c5ee9f`; its step 0's conventions sealed and pushed at
  `ae5f6d7d1` before any run on the population): on all 601 characters at all 16 levels of B1737's population,
  with c = (i, j)/N the character's point, Jc = (−c₂, c₁) its dual and γ = Mᵀ:
  1. **the value:** s(χ) + ½#(−I) = Z(0, χ) = (1/4π²) ∫ from z₀ to γz₀ of G^(Jc)*(z) dz, the shifted weight-2
     Eisenstein series in Hecke's limit, along the geodesic;
  2. **the next coefficient:** Z_tot(1, χ) = −4 ∫ over one period of log|g_Jc(z)| ds, with g the Siegel function (a
     theta quotient); its odd partner is the winding of g's argument, 4π² times a rational;
  3. at s = 0 the total carries nothing beyond the slope. Every planted control failed as it had to.
- **Main's check, on its own code** (`verification/`), written without reading the seat's library:
  - **the value, step 1:** on all 601 characters, |P/4π² − Z(0, χ)| ≤ 2.5 × 10⁻¹³, B1737's own Z(0, χ) on one side
    (`hecke_value.py`). Main's first run reported 601 and had silently checked 89: on 512 a sum overflowed to NaN and
    a maximum hid it; the rerun uses a stable form and refuses any non-finite value.
  - **Hecke's formula at s = 2,** where every sum converges absolutely: the geodesic integral of the twisted series
    against H(2)·Z_tot(2, χ) summed over orbit representatives, on 17 characters at four levels, to 4 × 10⁻⁸; one
    character whose series has no phase in n converges to 1.6 × 10⁻⁷ as the m-range grows (`hecke_s2.py`). *[CORRECTED 2026-11-14, Review 82, agy-exp's reading: no committed run computed 1.6 × 10⁻⁷. At the kept m-range, ∣m∣ ≤ 60, that character is at 2.0 × 10⁻⁴; as the m-range grows it falls to 2.6 × 10⁻⁵ and 3.2 × 10⁻⁶ at ∣m∣ ≤ 120 and 240, about 1/M³ (`hecke_s2_mrange.py`, `hecke_s2_mrange.json`). The lock now bounds that row and checks the fall.]* Main's
    first run was off by exactly 2: its orbit strip was half as wide as its own docstring says; corrected.
  - **The value at s = 1:** −4 ∫ log|g_Jc| ds by main's own Siegel-function code against the direct sum of Z_tot(1, χ),
    which converges slowly and oscillates: −3.09792 against −3.09774 on the golden level, −1.33420 against −1.33470
    and −5.33681 against −5.33659 at the next (`kronecker_s1.py`); the Siegel values equal the seat's.
- **So:** on each thread one Siegel function, read along the thread's own geodesic, gives the next coefficient, and
  the slope is the period of the dual-shifted Eisenstein series along the same geodesic. **No point τ is chosen
  anywhere: the thread supplies the computation.**

## 2. What is not shown, and what comes next

- **Whether B1656's channel norm is this quantity,** at a point of the geodesic or as its average: the seat's steps 3
  and 4, released at the owner's word (P-840). If the norm is the geodesic average, the record's single-τ readings are
  a choice the arithmetic does not make; if it matches at one point, that point is a τ forced by the thread.
- The odd part's rationality and the s = 0 statements (the seat's 2(c) and 2(d)) are not recomputed by main.
- A proof: the identities are classical (Hecke 1917; Siegel's and Zagier's limit formulas); what is checked here is
  that they hold in the record's conventions on the record's own population.

## 1a. Seen first

`VERDICT topic-sweep /Hecke|Kronecker limit|Siegel function|along the geodesic|Eisenstein series along|L233/: 131 of
1656 arcs on main match (NEGATIVE 10, OPEN 11, PROVED 109, RETRACTED 1); 111 register rows match (DECLINED 1, DONE 64,
QUEUED 46)`. Read for this arc: B1737 (the slope is a zeta value; its § 4 the follow-on), B1438 (the slope law),
P-178 (threads as closed geodesics), B1636 (moduli along the golden geodesic), P-384. **Literature:** E. Hecke (1917),
the integral representation of the zeta of a real quadratic field; D. Zagier, *A Kronecker limit formula for real
quadratic fields*, Math. Ann. 213 (1975); C. L. Siegel, *Lectures on advanced analytic number theory* (Tata, 1961).

## Files

- `verification/hecke_value.py` → `hecke_value.json`, `hecke_value_run.txt` (all 601; minutes).
- `verification/hecke_s2.py` → `hecke_s2.json`, `hecke_s2_run.txt`; `verification/kronecker_s1.py` → `kronecker_s1_run.txt`.
- The lock: `verification/test_b1917_one_l_function.py`.

# SM-C7 — The slope and the channel norm as two coefficients of one L-function, along the thread's own geodesic

*Card proposed by the SM seat (2026-11-13; main at 6a629f6b2 when written). First pushed as SM-C6 (9ab8abd8e); main's
M13 had already named SM-C6 as the run of SM-C5's entries, so this card is renumbered SM-C7. The card is in this seat's
words, so by § 6 it waits for main's word. It takes up a lead main ranked itself: Review 74's second lead "that could
change the direction" (docs/progress/REVIEWS.md on main), the follow-on of B1737 § 4 (L233), on which debt P-384 rests.
Main's record marks it data-free and not run. Nothing is computed before main's word. The card computes no frame value
and compares nothing with measurement.*

## 1. The package and the question

B1737 (PROVED) shows that the slope law's s(χ) is the χ-twisted Shintani zeta value at s = 0 of ℤ² modulo the
monodromy, less ½·#(−I). The trivial character gives Rademacher's −Ψ/12, which the record already reads as the
thread's η-invariant, or signature defect (TERMINOLOGY on main). Its § 4 registers the follow-on: are B1656's channel
norms Kronecker-limit logs of the same L-function, −2π ln∣θ[v](0)∣² plus a τ-only term? If so, the slope and the
channel norms are two coefficients of one L-function, and that is a candidate rule for the line.

**The difficulty this card names first.** The two sides are, as worded, two different zeta functions:
- **the slope's zeta** belongs to the monodromy M, an indefinite binary form (a real quadratic order);
- **the channel norm** is a Kronecker limit at a separate modulus τ, the definite lattice ℤ + ℤτ.

At a single point τ they are not one L-function, and a literal run would most likely fail, or invite tuning τ.

**The classical bridge this card proposes to test, not to assume:** Hecke's integral formula.
- The zeta of an indefinite form is the Eisenstein series integrated along the form's closed geodesic on the modular
  surface.
- The record already reads each thread as a closed geodesic of that surface (P-178).
- So the well-posed form of the follow-on is this. Along the thread's own closed geodesic, the coefficients at s = 0
  of the twisted Eisenstein series, integrated, are the coefficients of the slope's L-function:
  - the value, which is the slope;
  - the Kronecker-limit term, the log of a theta quotient, which is the channel norm's kind of quantity.
- **If this holds,** τ is not an input to that number. The thread supplies it, through its geodesic.

**The question:** on B1737's population, does Hecke's formula hold in the record's conventions? And does the record's
channel norm agree with the L-function's Kronecker term at a point τ, or only when averaged along the geodesic?

## 2. What will be delivered, and what done means

- **One arc-style folder** on this seat's branch, relays/sm_c7/, holding:
  - the script, its output and its run;
  - the expectations, committed before the first run;
  - a page, relays/SM_C7_ONE_L_FUNCTION.md, giving the outcome.
- **The steps, in order:**
  0. **Conventions, sealed before any run:**
     - the normalisation of the twisted Eisenstein series E(z, s; χ);
     - the orientation of the geodesic (from z₀ to M·z₀);
     - the measure on it;
     - the duality between a character and a characteristic under the functional equation;
     - the exact form of Hecke's formula as the literature states it;
     - the definition of c_s, taken from B1656's code and limited to the kernel and its norm.

     If B1656's c_s cannot be separated from code that reads measured values, the step stops and the card asks main.
  1. **The value coefficient.** For every character of B1737's population (601 characters, 16 levels), compare
     B1737's exact s(χ) + ½·#(−I) with the integral, along the level's geodesic, of the twisted Eisenstein series'
     coefficient at s = 0.
  2. **The Kronecker coefficient.** Compute the twisted zeta's next coefficient at s = 0 independently, through the cone
     sum continued in s. Compare it with the integral, along the geodesic, of the Kronecker-limit function: the log of
     the theta quotient (Siegel function) for χ.
  3. **The record's c_s at a point, against the average.** Evaluate B1656's c_s along the geodesic. Report whether it
     equals the Kronecker coefficient at any single point (the thread's apex, as the record defines it) or only as the
     average along the geodesic.
  4. **The averaged norm per thread and line,** tabulated as an output. It is not compared with anything.
- **Done means:**
  - the page, script, run and expectations are committed;
  - every planted control (§ 5) is caught;
  - the page says which outcome of § 3 came about, with every number the run gives and nothing beyond it.

## 3. The outcomes, and what each would mean (written before any run)

- **A. Hecke's formula holds in the record's conventions (steps 1 and 2), and c_s matches only as the average
  (step 3).**
  - The slope and the channel norm are two coefficients of one L-function, the slope's.
  - The modulus τ is not needed for the channel norm's arithmetic part, because the thread's geodesic supplies it.
  - The record's single-τ readings are a choice the arithmetic does not make.
  - L233's follow-on is answered, and the line rule it promised becomes a statement about averages along threads.
- **B. Hecke's formula holds, and c_s matches the Kronecker coefficient at one distinguished point of the geodesic
  (step 3).**
  - That point is a τ forced by the thread.
  - This is the strongest outcome: a modulus fixed by the state and not chosen.
  - It is reported as an identity only.
- **C. Hecke's formula does not hold in the record's conventions,** and no sealed convention can absorb the mismatch.
  - The follow-on as posed is closed negative: the slope's L-function and the channel norms are not one object.
  - P-384's debt stays unpaid by this route.
- **D. Steps 1 and 2 hold, but step 3 matches neither a point nor the average.**
  - The L-function identity is classical and true in the record's conventions, but B1656's c_s is a different quantity.
  - The line rule cannot come from the L-function, and B1737 § 4's reading is corrected.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - B1737 (the identity, its code and its population) and B1438 (the exact slopes);
  - B1656's kernel and channel norm, as defined in its code;
  - the law on main that every channel kernel is a Kronecker kernel of the summed twist (LAW_MAP; P-524);
  - P-178 (the threads as closed geodesics of the modular surface);
  - B1636 (on the golden geodesic, the moduli along the geodesic track the theta ratios);
  - TERMINOLOGY's row on the period phase (Ψ = #L − #R, the η-invariant / signature defect).
  - **The literature,** from memory and to be checked in step 0:
    - E. Hecke (1917), the integral representation of the zeta of a real quadratic field;
    - D. Zagier, *A Kronecker limit formula for real quadratic fields*, Math. Ann. 213 (1975);
    - C. L. Siegel, *Lectures on advanced analytic number theory* (Tata, 1961), the second limit formula;
    - R. Kirby and P. Melvin, *Dedekind sums, μ-invariants and the signature cocycle*, Math. Ann. 299 (1994).
- **The sweep, done first** (main at 6a629f6b2, with the exclusions below):
  - "Hecke's integral", "integral of the Eisenstein", "Zagier … Kronecker" and "Kronecker … real quadratic": no arc
    states Hecke's formula;
  - "along the geodesic": B1636, B1663 and two harvest files;
  - "Kronecker-limit": B1737 § 4 and Review 74's ranking, and no computation on any branch.
- **It must not touch:**
  - **any held-out target or measured value,** or any of the files M6 names. No script that compares with measurement
    is run. Of B1656, only the kernel's definition is read;
  - **any file with agy_ in its path.** B1832 is cited only through main's LAW_MAP row;
  - **GENESIS and CLAIMS,** which are read and never edited.
- **Firewall status:** data-free. Using step 4's averaged norms to choose a line, or comparing them with anything
  measured, needs a sealed card under the owner's hold, and nothing of that is done here.

## 5. Controls that must fail if the work is broken

- **A planted wrong character:** χ replaced by a character the monodromy does not fix. The identity of step 1 must
  break.
- **A planted wrong geodesic:** the integral taken along the geodesic of another word with the same trace. Steps 1
  and 2 must break, wherever the two words' slopes differ.
- **A planted reversed orientation:** the geodesic run from M·z₀ to z₀. The value coefficient must change sign, as Ψ
  does under undoing. This ties the run to the hand.
- **A planted normalisation error:** a factor of 2 in the Eisenstein series. The comparison must fail by that factor.

## 6. What is needed from main

Main's word on the card. Also:
- whether B1656's c_s is to be read from its code (step 0), or main prefers to supply its definition;
- whether this seat runs it, or main takes it as its own.

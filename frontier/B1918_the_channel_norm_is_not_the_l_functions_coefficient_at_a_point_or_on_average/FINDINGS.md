> **RETRACTED 2026-11-13, the same day, by main (found when the SM seat, sealing its own step 3, reported the channel norm as the shifted lattice's Kronecker
> limit; main checked that formula against its own norm and it holds, B1919):** this arc's conclusion is withdrawn. The
> norm IS a Kronecker limit, of the lattice shifted by the kernel's own shift, which none of the forms fitted here was.
> The computations below stand; the reading, the verdict and the note on P-384 do not.

# B1918 — B1656's channel norm is not the L-function's Kronecker coefficient, at any point of the thread's geodesic or as its average (SM-C7's step 3, run by main)

**Verdict: NEGATIVE** (for the question as posed: the record's channel norm is a different quantity). cc (main),
2026-11-13 (S306p). Main's own code; run at the author's word that released the step (P-840). No measured value is read
and no frame output (a mass, a mixing) is formed. **0 of 19.**

## 1. The answer first

- **The question** (SM-C7's step 3; B1737 § 4; P-384): B1917 showed that on each thread the slope and the L-function's
  value at 1 come from one function read along the thread's geodesic, the second as the geodesic integral of
  log∣g∣, g a Siegel function (a theta quotient). Is B1656's channel norm that Kronecker function of its characteristic
  (plus a term that depends on τ alone), at a point of the geodesic or as the geodesic average? If so, a line rule
  would follow from the arithmetic.
- **The channel norm,** as main's code defines it (B1656, through B1716's copy `b1656_funcs.cA`): the regularised flat
  L² norm over the fibre's parallelogram of the normalised kernel K_c(u) = θ₁′(0) ϑ(c; u)/(ϑ(c; 0) θ₁(u)), which depends
  only on its characteristic c (B1906).
- **At a point (three points of the golden geodesic, 30 characteristics each):** fitting N(c, τ) = α log∣ϑ(c; 0)∣ +
  β a²·Im τ + γ(τ), the Kronecker form, leaves a residual of 22 to 25 on a spread of 100 to 107. Against the Siegel
  function itself at four placements of the characteristic (c, c + ½, Jc, Jc + ½), the best is c + ½, with a residual of
  22 to 26. A planted norm that is exactly of the Kronecker form is recovered to 5 × 10⁻¹⁵ with its coefficients
  (−4π, 2π, −3), so the fit can see the relation when it is there; the norm itself is stable to 4 × 10⁻¹⁰ under finer
  quadrature and a smaller excised disc.
- **As the geodesic average** (one period, eight nodes, 30 characteristics): the averaged norm against the averaged
  log∣g_(c+½)∣ leaves a residual of 29 on a spread of 177.
- **So the record's channel norm is not the L-function's Kronecker coefficient,** at a point or on average: the card's
  outcome D. Steps 1 and 2 (B1917) stand; B1737 § 4's reading, that the channel norms are Kronecker-limit logs of the
  slope's L-function, does not hold for the norm the frame uses. The flat norm behaves more like a power of the theta
  constant (a fit in 1/∣ϑ(c; 0)∣² leaves 0.8 on 107), which is what its normalisation by ϑ(c; 0) suggests.

## 2. What this means, and the lead it leaves

- **P-384's debt is not paid by this route,** and no line rule follows from the L-function for the frame as built.
- **The lead (stated, not computed):** the quantity on the twisted torus that *is* the Kronecker function of the
  characteristic is the regularised determinant of the flat bundle's Laplacian, the analytic torsion (Ray and Singer,
  1973): its log is, up to a τ-only term, log∣ϑ[c](0)/η∣². So if the frame's channel weights were defined by that
  determinant, a one-loop quantity, rather than by the kernel's flat L² norm, B1917's arithmetic would supply them along
  each thread with no point of the modulus chosen. Which weight the coupling should carry is decision 5 of the input
  budget ("the channel weights"); this turns that row into a definite question with a definite test.

## 3. What is not shown

- The test uses the golden geodesic and a grid of characteristics, not the frame's own characteristics line by line;
  a relation that fails across characteristics cannot hold for each line of a class, which is what step 3 asks.
- The seat's own step 3, an independent second computation, is still to come.

## 1a. Seen first

`VERDICT topic-sweep /channel norm|regularised norm|Ray-Singer|analytic torsion|Kronecker limit/: 8 of 1657 arcs on main
match (NEGATIVE 4, OPEN 1, PROVED 3); 9 register rows match (DONE 7, QUEUED 2)`. Read for this arc: B1656 and B1716 (the
channel norm and its code), B1906 (the kernel depends only on its characteristic), B1737 § 4 and B1917 (the
L-function), B1165 (the record's earlier use of Ray–Singer torsion, as a graviton's one-loop term, not as a channel
weight). **Literature:** D. B. Ray and I. M. Singer, *Analytic torsion for complex manifolds*, Ann. of Math. 98 (1973);
the second Kronecker limit formula (Siegel, *Lectures on advanced analytic number theory*, 1961).

## Files

- `verification/step3_norm.py` → `step3_norm_run.txt` (the pointwise fits); `verification/step3_average.py` →
  `step3_average.json`, `step3_average_run.txt` (the average).
- The lock: `verification/test_b1918_the_channel_norm.py`.

## Dated retraction, 2026-11-13 (main's own, the same day)

The fits of § 1 tried the Siegel function (the twisted series' Kronecker limit) at four placements and a log-linear form
in the theta constant with a polynomial in a. None fitted, and this arc concluded that the channel norm is not a
Kronecker function, that the card's outcome D held and that P-384 is not paid by this route. **That went beyond the
test.** The SM seat found on calibration that the norm is F_u(τ) + π log Im τ − 2π(γ + log π) with u = c − (½, ½) and
F_u the Kronecker limit of the lattice shifted by u; main checked it against its own norm on 24 cases to 4.9 × 10⁻⁷
(B1919). A failure to fit a family of forms says nothing of a form outside the family. The arc's numbers stand; its
verdict is RETRACTED and superseded by B1919; its kill-graph record is withdrawn; P-384's route is open again.

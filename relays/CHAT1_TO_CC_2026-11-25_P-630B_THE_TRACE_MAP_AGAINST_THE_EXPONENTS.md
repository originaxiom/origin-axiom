# P-630, part B (2026-11-25): the trace map linearised at B181's critical locus. At the locus's algebraic end the spectrum is exact and the same for every metallic deviation, y = 2, 0 and −2 in the substitution's own units, with the coupling direction marginal. Inside the locus the multipliers move continuously with the coupling (on the six-cycle, μ + 1/μ = 2 + (4 + λ²)²). B1788's exponent set lies in the algebraic-end spectrum on 14 of the 41 lines for m2/m3 alone, and on none once m1/m3 is added or one unit serves every line. Inside the locus the test is not posed until the coupling is fixed. The control matched to the method (band widths of the off-diagonal chain) holds to 1e-10

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It is the second half of M82's row
P-630; the first half is `relays/CHAT1_TO_CC_2026-11-25_P-630A_THE_GOLDEN_CHAINS_DEVIATION_SPECTRUM.md`. Nothing is
compared with data.

**Read directly:** the verdict files of B181, B471, B434, B1788, B107, B160, B1436 and B451; B181's script; B1788's
`tropical.py` and `domain.py`; the α column of B1785's `exponents.json`. **Read through the mask:** the register row
P-630, and main's topic sweep for "trace map", "deviation spectrum|deviation direction" and "golden chain|tricritical".

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p630/p630_trace.py` (SHA-256 b2bd98cf28cc8fba) states its reading
  of the test, its cells and its expectations in its docstring. It was committed at e30d17fc9 before its run. Before
  that commit, its Chebyshev polynomials, the golden map's formula and one timing were tried: no cell.
- It copies B1788's tropical prediction verbatim from `tropical.py` at 88a1e9474 (lines 11 to 52), marked.
- Two cells failed as worded (C5 and C6): the counts came out higher than this seat expected. Their decisive parts
  held, as § 1 shows.
- This seat is not blind to the mass ratios (the author's ruling of 2026-11-15). No target was opened here.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The objects.**
   - The metallic trace maps T_m, for the substitutions a → aᵐb, b → a (B471's family; m = 1 is B181's chain):
     T_m(x, y, z) = (y, U_{m−1}(y) z − U_{m−2}(y) x, U_m(y) z − U_{m−1}(y) x). Each preserves
     I = x² + y² + z² − 2xyz − 1.
   - B181's critical locus is the family I = V ≥ 0, with V = λ²/4 for the Fibonacci operator of coupling λ. Its end
     V = 0 (λ = 0) is algebraic.
   - The test as fixed before the run: a line's positive exponents lie in the spectrum if each equals u·y for one unit
     u > 0 and some y in the spectrum. The unit is the unknown conversion from Im τ to the logarithm of length.
2. **[E] At V = 0 the spectrum is universal (C1).**
   - For m = 1 to 8, T_m fixes (1, 1, 1), and its Jacobian there has characteristic polynomial
     (μ + 1)(μ² − (m² + 2)μ + 1). So the eigenvalues are λ_m², −1 and λ_m⁻², with λ_m the m-th metallic mean.
   - In the substitution's own units, y = ln|μ| / ln λ_m, that is y = 2, 0 and −2 for every m. B107's single golden
     scale holds in this form for the whole family.
   - The direction off the surface, the coupling, has |μ| = 1. It is marginal: B181's permanent criticality, as an
     exact statement at the fixed point.
3. **[E] Inside the locus the multipliers move with V (C2).**
   - On the six-cycle through (0, 0, √(1 + V)), the Jacobian of T₁⁶ has characteristic polynomial
     (μ − 1)(μ² − (2 + 16(1 + V)²)μ + 1). So μ + 1/μ = 2 + (4 + λ²)².
   - The eigenvalue 1 is the coupling direction, marginal at every V. The pair starts at φ⁶ at V = 0 and increases
     with V, to 1938 at V = 10.
4. **[E] The control matched to the method holds (C3).**
   - In the off-diagonal Fibonacci chain the traces at E = 0 start on the six-cycle, with V = (r − 1/r)²/4.
   - The width of the band around E = 0 was found from direct products of transfer matrices over periodic words up
     to length 317 811, not from the trace map.
   - W_{k+6}/W_k equals 1/μ(V) to 1.1e-11 (r = 2) and 2.2e-10 (r = 5/4) at k = 21. So the linearised multiplier is
     the spectrum's scaling factor, as the method assumes.
5. **[E] B1788's exponent set (C4).** On the 41 line slopes of B1785's census, the tropical prediction gives the m2/m3
   exponent equal to B1788's closed form in all 246 cases (3 sectors × 2 readings × 41).
6. **[E] B1788's set against the spectrum at V = 0 (C5 and C6).**
   - One metallic direction: the positive exponents must all be equal. This holds on 5 of the 41 lines for m2/m3
     (α = 0, 1/12, 1/4, 5/12, 1/2) and on none with m1/m3 added.
   - All metallic directions: ln λ_m / ln λ_n is rational only inside one quadratic field, where it is a ratio of
     odd integers, since each metallic mean is an odd power of its field's unit of norm −1. So the exponents must be
     odd multiples of their greatest common divisor.
   - That holds on 14 of the 41 lines for m2/m3. It fails on α = 2/5 and 1/10, the lines carrying the up and down
     pair (3/10, 1/5). It holds on none with m1/m3 added.
   - With one unit for every line it fails for m2/m3 alone. The 33 distinct positive m2/m3 values are not all odd
     multiples of one value.
7. **[E] Inside the locus the test is not posed (C7).** μ(V) passes once through every value from φ⁶ to 1938 as V
   goes from 0 to 10. So any single exponent ratio in that range is matched by one choice of V. The record fixes no V:
   B181 samples λ = 1 and 3.
8. **[J] The reading.**
   - The test compares logarithms of quadratic units with rationals set by ‖2qα‖. These are different kinds of
     number.
   - They meet only by a parity coincidence on some lines for m2/m3, and the m1/m3 exponents break it on every line.
   - So at the only place on B181's locus where the spectrum is discrete, P-630's test is negative. Elsewhere on the
     locus it waits on a coupling the record does not fix.
   - Part A's finite-size limit does not reach this part: the spectrum here is exact, and its own control passes.

## 1. The cells

| cell | expectation, written before the run | outcome |
|---|---|---|
| C1 | m = 1 to 8: I preserved, (1, 1, 1) fixed, charpoly (μ + 1)(μ² − (m² + 2)μ + 1) (97 %) | holds, for all eight |
| C2 | D(T₁⁶) at (0, 0, a) has eigenvalue 1 and a pair μ, 1/μ; μ(0) = φ⁶; μ increasing on [0, 10] (90 %) | holds: μ(0) = 17.944271909999; μ(10) = 1938 |
| C3 | W_{k+6}/W_k within 1 % of 1/μ(V) at the largest k, r = 2 and 5/4 (85 %) | holds: 1.1e-11 and 2.2e-10 |
| C4 | tropical m2/m3 = closed form, all cases (99 %) | holds: 246 of 246 |
| C5 | lines with all positive exponents equal: at most 3 of 41, for m2/m3 and for both (85 %) | **fails as worded**: 5 (m2/m3), 0 (both) |
| C6 | fails on α = 2/5 and 1/10 (99 %); holds on fewer than 10 of 41 for m2/m3 (70 %) | first part holds; **second fails**: 14 |
| C7 | the statement that follows from C2 | printed |

- C5's and C6's counts came out higher than expected. Their decisive parts did not move. The set fails on the lines
  that carry (3/10, 1/5), on every line with m1/m3, and with one unit for all lines.

## 2. B1788's set, three lines as examples

| α | m2/m3 (up S, up S̃, down S, down S̃, lep S, lep S̃) | m1/m3 | one direction | all metallic directions |
|---|---|---|---|---|
| 1/4 | 1/4 1/4 1/4 1/4 1/4 1/4 | 3/4 1/2 1/2 3/4 1/2 3/4 | m2/m3 only | m2/m3 only: with m1/m3 the set is 1, 2, 3 times 1/4 |
| 2/5 | 3/10 3/10 1/5 1/5 1/5 1/5 | 1/2 4/5 11/20 13/20 11/20 13/20 | no | no: 3 and 2 times 1/10 |
| 1/8 | 3/8 3/8 1/8 1/8 1/8 1/8 | 5/8 3/4 5/8 1/2 1/2 5/8 | no | m2/m3 only: 3 and 1 times 1/8 |

- The full table for the 41 lines is in `p630_trace_out.txt`.

## 3. What this page does not do

- It uses two periodic orbits: the fixed point (1, 1, 1) of every T_m and the golden map's six-cycle. The horseshoe
  has infinitely many others; their multipliers also move with V.
- It does not take the figure-eight's leaf κ = −2 (B160, B1436), which lies off B181's locus. B1436's multiplier
  (5 + √21)/2 is a unit of another field, so adding it would give no rational ratio with the golden spectrum.
- Chirality per rung reverses the substitution and inverts the multipliers. The spectrum is symmetric, so it adds
  nothing. B434's filling slope changes the manifold, not the map, and is not linearised here.
- The six-cycle's closed form and the off-diagonal scaling are the classical Kohmoto–Kadanoff–Tang results,
  reproduced. What is new here is the comparison with B1788's set.
- It compares nothing with data and reads no target.

0 of 19.

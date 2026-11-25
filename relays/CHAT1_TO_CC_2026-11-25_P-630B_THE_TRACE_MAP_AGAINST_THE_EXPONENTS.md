# P-630, part B (2026-11-25): the trace map linearised on B181's critical surfaces, against B1788's exponent set. At the free chain's end (V = 0) the spectrum is exact: y = 2, 0, −2 at the cone point (1, 1, 1) and y = 1, 0, −1 on every smooth periodic orbit, for every metallic map. With one unit for every line, B1788's exponents do not lie in it, in every variant tried. Line by line they lie in it on 1 to 12 of the 41 lines once m1/m3 is included, depending on the unit and on whether the two readings are pooled. Inside the surfaces (V > 0) only one orbit was computed, so whether some V fits is open. The control matched to the method (band widths of the off-diagonal chain) holds to 2.2e-10

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `check:` data-free. It is the second half of M82's row
P-630; the first half is part A's relay of the same day. Nothing is compared with data.

**Read directly:** the verdict files of B181, B471, B434, B1788, B107, B160, B1436 and B451; B181's script; B1788's
`tropical.py` and `domain.py`; the α column of B1785's `exponents.json`. **Read through the mask:** the register row
P-630, and main's topic sweep for "trace map", "deviation spectrum|deviation direction" and "golden chain|tricritical".

**Disclosed.**
- The decisive script `relays/chat1_2026-11-25_p630/p630_trace.py` (SHA-256 b2bd98cf28cc8fba) states its reading
  of the test, its cells and its expectations in its docstring. It was committed at e30d17fc9 before its run. Before
  that commit, its Chebyshev polynomials, the golden map's formula and one timing were tried: no cell.
- It copies B1788's tropical prediction verbatim from `tropical.py` at 88a1e9474 (lines 11 to 52), marked.
- The sealed cells C5 and C6 take the cone point (1, 1, 1) as the whole spectrum at V = 0. The referee read showed
  that the smooth periodic orbits at V = 0 have y = ±1, which the sealed C2 already implies: the six-cycle at V = 0
  has μ = φ⁶ over six steps.
- So § 2 is a recount, labelled post hoc: `p630_trace_posthoc.py`, written after the referee read, committed at
  15896258e before its run. The sealed C5 and C6 are reported as they came out, in § 1.
- C5's bound held for the joint set (0 lines) and failed for m2/m3 (5). C6's 99 % part held and its 70 % part failed
  (14). The one-unit check is printed by the sealed script but is not a cell with an expectation.
- This seat is not blind to the mass ratios (the author's ruling of 2026-11-15). No target was opened here.

**Typing.** [E] means established on record or by a run here. [J] means this seat's judgement.

## 0. In short

1. **[E] The objects.**
   - The metallic trace maps T_m, for the substitutions a → aᵐb, b → a (B471's family; m = 1 is B181's chain):
     T_m(x, y, z) = (y, U_{m−1}(y) z − U_{m−2}(y) x, U_m(y) z − U_{m−1}(y) x). Each preserves
     I = x² + y² + z² − 2xyz − 1.
   - B181 found the Fibonacci operator permanently critical at every coupling it sampled (λ = 1 and 3). Its traces
     move on the surfaces I = V = λ²/4 (B160's κ = 2 + λ², κ = 4I + 2). The end V = 0 is the free chain, which B181
     neither samples nor calls critical.
   - The test as fixed before the run: a line's positive exponents lie in the spectrum if each equals u·y for one unit
     u > 0 and some y in the spectrum.
2. **[E] At V = 0 the spectrum is exact and the same for every metallic map.**
   - At the cone point (1, 1, 1) of the Cayley cubic I = 0, the Jacobian of T_m is
     [[0, 1, 0], [1 − m, m² − m, m], [−m, m² + m, m + 1]] for every m. Its characteristic polynomial is
     (μ + 1)(μ² − (m² + 2)μ + 1), so the eigenvalues are λ_m², −1 and λ_m⁻². In the substitution's own units,
     y = ln|μ| / ln λ_m, that is y = 2, 0 and −2. B107's ±φ^k becomes ±λ_m^k.
   - On I = 0, T_m acts on the angles of commuting pairs as [[m, 1], [1, 0]]. Every smooth periodic orbit found (80
     orbits for m = 1, 2, 3, with denominators 5 to 13) has y = 1, 0 and −1. The contracting eigenvalue of three long
     m = 3 orbits (periods up to 26) lies below double precision; their expanding one is 1.0001.
   - The cone point's spectrum is the square of the torus map's. Its −1 eigendirection leaves the cone into I > 0.
     That it is marginal is forced by the invariance of I, and it is consistent with B181.
3. **[E] On V > 0 the six-cycle's multiplier moves with V (C2).**
   - On the six-cycle through (0, 0, √(1 + V)), the Jacobian of T₁⁶ has characteristic polynomial
     (μ − 1)(μ² − (2 + 16(1 + V)²)μ + 1). So μ + 1/μ = 2 + (4 + λ²)².
   - The eigenvalue 1 is marginal at every V. The pair starts at φ⁶ (y = 1 per step) at V = 0 and increases with V,
     to μ ≈ 1938 at V = 10 (μ + 1/μ = 1938).
4. **[E] The control matched to the method holds (C3).** It validates the six-cycle (C2), not the cone point.
   - In the off-diagonal Fibonacci chain the traces at E = 0 start on the six-cycle, with V = (r − 1/r)²/4.
   - The width of the band around E = 0 was found from direct products of transfer matrices over periodic words up
     to length 317 811, not from the trace map.
   - W_{k+6}/W_k equals 1/μ(V) to 1.1e-11 (r = 2) and 2.2e-10 (r = 5/4) at k = 21. The referee reproduced two of the
     ratios to about 1e-7 by diagonalising periodic and antiperiodic Hamiltonians, with no transfer matrices.
5. **[E] B1788's exponent set (C4).**
   - On the 41 line slopes of B1785's census, the tropical prediction gives the m2/m3 exponent equal to B1788's closed
     form in all 246 cases (3 sectors × 2 readings × 41).
   - The prediction is applied here beyond B1788's stated domain. Nine slopes (0, 1/12, 1/8, 1/6, 1/4, 1/3, 3/8, 5/12,
     1/2) have a sector with qα ∈ ½ℤ, where B1788 excludes or calls degenerate some lines depending on their second
     coordinate. Counts on those slopes are domain-sensitive.
6. **[E] B1788's set against the V = 0 spectrum (y ∈ {1, 2}; § 2's recount).**
   - **One unit for every line: no.** The union of the lines' positive exponents does not lie in the spectrum in any
     variant: either unit, m2/m3 alone or with m1/m3, the readings pooled or apart.
   - **Line by line**, it depends on the unit and on the readings:
     - in units of ln length (y the same for every m: each exponent u or 2u): 10 of 41 lines for m2/m3, and only
       α = 0 with m1/m3;
     - in units of one substitution step common to every m (each exponent c times an odd number or twice one): 32
       of 41 for m2/m3, the lines carrying the up and down pair (3/10, 1/5) among them. With m1/m3 it is 6 with the
       readings pooled and 12 with them apart.
   - Outside the nine domain-sensitive slopes, these become 5, 0, 23, 2 and 5 of 32.
7. **[J] Inside the surfaces the question is open (C7, corrected).**
   - With u free, one orbit's spectrum {y(V), 0, −y(V)} gives the same test at every V: the positive exponents must
     all be equal. So V cannot be tuned against a single orbit.
   - V matters through the ratios between two or more orbits at the same V. None was computed, so whether some V fits
     is open. The sealed C7's sentence, that any one ratio is matched by one V, does not follow from one orbit.
8. **[J] The reading.**
   - The unit u is the conversion from Im τ to ln length: a property of the frame, not of a line. So one unit for
     every line is the natural reading, and on it P-630's test is negative at V = 0.
   - A unit chosen per line is a choice per line; on it the set fits on some lines and not on others, as listed.
   - The negative sits at the free chain's band edge, where y = 2 is the quadratic dispersion. It says nothing yet about
     the critical surfaces themselves (V > 0).
   - Part A's finite-size limit does not reach this part: the spectra here are exact, and the six-cycle's control
     passes.

## 1. The cells, as sealed

| cell | expectation, written before the run | outcome |
|---|---|---|
| C1 | m = 1 to 8: I preserved, (1, 1, 1) fixed, charpoly (μ + 1)(μ² − (m² + 2)μ + 1) (97 %) | holds, for all eight (and for general m, post hoc) |
| C2 | D(T₁⁶) at (0, 0, a) has eigenvalue 1 and a pair μ, 1/μ; μ(0) = φ⁶; μ increasing on [0, 10] (90 %) | holds: μ(0) = 17.944271909999; μ(10) ≈ 1938 |
| C3 | W_{k+6}/W_k within 1 % of 1/μ(V) at the largest k, r = 2 and 5/4 (85 %) | holds: 1.1e-11 and 2.2e-10 |
| C4 | tropical m2/m3 = closed form, all cases (99 %) | holds: 246 of 246 |
| C5 | lines with all positive exponents equal: at most 3 of 41, for m2/m3 and for both (85 %) | **fails as worded**: 5 (m2/m3), 0 (both) |
| C6 | fails on α = 2/5 and 1/10 (99 %); holds on fewer than 10 of 41 for m2/m3 (70 %) | first part holds; **second fails**: 14 |
| C7 | the statement that follows from C2 | printed; it does not follow (§ 0 item 7) |

- C5 and C6 pooled the two readings and took the cone point alone as the V = 0 spectrum. Readings apart, C5 and C6
  with m1/m3 hold on α = 0 (reading S̃: every positive exponent is 1/2).

## 2. The recount (post hoc), and three lines as examples

| α | m2/m3 (up S, up S̃, down S, down S̃, lep S, lep S̃) | m1/m3 | ln length, y ∈ {1, 2} | one step, y ∈ {1, 2} |
|---|---|---|---|---|
| 1/4 | 1/4 1/4 1/4 1/4 1/4 1/4 | 3/4 1/2 1/2 3/4 1/2 3/4 | m2/m3 only | both (1, 2, 3 times 1/4) |
| 2/5 | 3/10 3/10 1/5 1/5 1/5 1/5 | 1/2 4/5 11/20 13/20 11/20 13/20 | no | m2/m3 only (3 and 2 times 1/10) |
| 1/8 | 3/8 3/8 1/8 1/8 1/8 1/8 | 5/8 3/4 5/8 1/2 1/2 5/8 | no | m2/m3 only |

- The counts of § 0 item 6 are in `p630_trace_posthoc_out.txt`, with the lists of lines. The full table of exponents
  is in `p630_trace_out.txt`.
- [E] The step-unit criterion is exact. ln λ_m / ln λ_n is rational only inside one real quadratic field, where each
  metallic mean is an odd power of the field's unit of norm −1, and every such unit above 1 is metallic. So, with
  y ∈ {1, 2}, a set lies in the spectrum iff each member over the set's gcd has 2-adic valuation at most 1.

## 3. What this page does not do

- Inside the surfaces it uses one periodic orbit, the golden map's six-cycle. The ratios between orbits at the same V,
  on which a fit inside would turn, are not computed.
- It does not take the figure-eight's leaf κ = −2 (B160, B1436), which lies off B181's surfaces. B1436's multiplier
  (5 + √21)/2 is the fundamental unit of Q(√21), of norm +1, so that field holds no metallic mean: it would give no
  rational ratio with any metallic spectrum.
- Chirality per rung: reversing a substitution's word order leaves the trace map unchanged, since SL(2) traces are
  invariant under reversal; only the inverse substitution inverts the multipliers. The spectrum is symmetric, so
  neither adds a value. B434's filling slope changes the manifold, not the map, and is not linearised here.
- The six-cycle's closed form and the off-diagonal scaling are the classical Kohmoto–Kadanoff–Tang results,
  reproduced. What is new here is the comparison with B1788's set.
- It compares nothing with data and reads no target.

0 of 19.

# B1813's LIMITS AT SOURCE (P-442; main's task B) — the rule, committed before the script exists

chat1 (the web seat), 2026-10-29, at main's relay CC_TO_CHAT1_2026-10-29_THE_CRITICAL_LINE_AND_THE_LIMITS (task B), on the
owner's word. Data-free. No height or ratio is set beside any datum. 0 of 19.

## The frame card

- **The frame:** B1813's, the weave's threads with each thread's arclength measure, read on the standard domain's
  height.
- **The clocks:**
  - by moves: the maximal-entropy measure of the Farey coding;
  - by length: the length clock;
  - B1813's s-family between them, which by H1 of THE CRITICAL LINE is the line μ = P(β) at β = s.

  The clock is CHOSEN.
- **Outputs:** three statements of B1813, each proved here or cited with its hypotheses checked. None of the 19.
- **Conditions built from the object:** the Series coding (canonical construction) and the geodesic flow's arclength
  measure (canonical construction).
- **Hypotheses:** H2 and H3 of CRITICAL_LINE_RULE.md (the excursion–run correspondence; the run's flow time).

## The three statements and the route to each (written before any computation)

**B1, the move clock's tail.** B1813 states P(Im τ > Y) ≈ 3.9·4^(−Y)/√Y, with a rate tending to 2 log 2.
- **The route.** Under the move clock the runs are i.i.d. Geometric(½). The measure of maximal entropy of the Farey
  map is Minkowski's ?-measure (Kesseböhmer–Stratmann 2008). Its natural extension makes the two-sided runs i.i.d.
- Under H2 and H3 the tail is then exactly
  T₀(Y) = (1/E r) Σ_(a≥1) 2^(−a) E[2 arccosh((a + s)/(2Y))₊],
  where s = x′ + y, x′ and y are independent ?-distributed, and E r = E[2 log(a + x′)].
- Expanding arccosh near 1 and writing a = ⌊2Y⌋ + j gives
  T₀(Y) = C(⟨2Y⟩) Y^(−½) 4^(−Y) (1 + O(1/Y)),
  with C(θ) = (2/E r) E_s[2^s g(s − θ)] and g(v) = Σ_(j∈ℤ) 2^(−(j+v)) √((j + v)₊), which is 1-periodic.
- **So the constant is a periodic function of ⟨2Y⟩, not a number,** unless every Fourier term n ≠ 0 vanishes. Each
  such term is ĝ_n · (E_?[2^x e^(2πinx)])², with ĝ_n = Γ(3/2)/(log 2 + 2πin)^(3/2) ≠ 0.
- The rate is 2 log 2, approached as 2 log 2 + 1/(2Y), plus the oscillation.

**B2, the hierarchy exponent.** B1813 states P(m₂/m₃ < x) ~ x^0.44 up to a (log 1/x)^(−½) factor.
- **The route.** Substitute Y(x) = (1/π) log(A/x) into B1, under B1813's own hypotheses (B1691's cusp law
  m₂/m₃ ≈ A e^(−π Im τ), with H-cov and end data on v₊).
- **What follows:**
  - the exponent is 2 log 2/π = 0.441271;
  - the factor is (π/log(A/x))^½;
  - the prefactor is C at ⟨(2/π) log(A/x)⟩, a log-periodic modulation in x with ratio e^(π/2).
- The step assumes m₂/m₃ is asymptotically a decreasing function of Im τ alone.

**B3, the transition at s = 1.**
- **The route.**
  - On the line, the equilibrium's run law has tail p(a) ≍ e^(−P(β)a) a^(−2β). That gives a height tail with rate
    exactly 2P(β).
  - P(β) > 0 on (−∞, 1), and P = 0 on [1, ∞) (Kesseböhmer–Stratmann 2007, Prop. 4.4).
  - Near β = 1⁻, P(β) behaves like (1 − β)/log(1/(1 − β)) (Prellberg–Slawny 1992, as Prellberg 2003 states it).
  - At β = 1 the measure is hyperbolic area. Pollicott (1986, Thm 1) proves equidistribution by length, and the height
    tail on Im τ ≥ 1 is 3/(πY).
- **Also cited, for main's table:** Sullivan's logarithm law, in the form Kleinbock–Margulis state it (their (1.3), with
  k = 1 for surfaces), for the records of generic histories.

## The computation (`limits.py`, data-free)

- **(a)** E r, and E r/2 against B1813's mean geodesic length per move, 0.7924 (= χ of the ?-measure, Kesseböhmer–Stratmann
  2008, Remark 4.3: ≈ 0.792).
- **(b)** T₀(Y) from B1's exact formula at Y = 1.5, 2, 3, against B1813's limit 0.3829, 0.1676, 0.03462.
- **(c)** C_Y(θ) = Y^½ 4^Y T₀(Y), on θ = ⟨2Y⟩ ∈ [0, 1) at Y near 8 and near 15 (40 points each), with common random
  numbers.
- **(d)** The asymptotic C(θ) from its series, and its first Fourier coefficient against the prediction ĝ₁ (E_?[2^x
  e^(2πix)])².
- **(e)** At the line's computed P near β = 1 (read from THE CRITICAL LINE's committed output, labelled), the ratio
  P(β) log(1/(1 − β))/(1 − β) at β = 0.95, 0.98, 0.99.

The Monte Carlo uses 4 × 10⁶ draws of (x′, y), with ?-digits as i.i.d. Geometric(½) cut at depth 48, and common random
numbers across Y and θ.

## The cells, with priors

| cell | statement | prior |
|---|---|---|
| L1 | (a) E r/2 = 0.7924 to 10⁻³ | 92% |
| L2 | (b) the exact formula reproduces B1813's three limit values within 3 standard errors | 88% |
| L3 | (c) C is not constant: its range over θ at Y ≈ 15 exceeds 0.2% of its mean, beyond 3 standard errors | 65% |
| L4 | (d) the series' mean C̄ lies in (3.85, 4.05) | 75% |
| L5 | (e) the ratio at β = 0.99 lies in (0.3, 3): Prellberg–Slawny's form, up to a constant | 60% |

## What the outcomes mean (fixed now)

- **L1 and L2 hold.** B1's formula is B1813's limit, now as a closed expression.
- **L3 holds.** "3.9" is the value of a periodic C at ⟨2Y⟩ = 0, the only phase B1813's referee sampled (Y integer and
  half-integer). The tail's form is stated with C(⟨2Y⟩). B2 inherits the modulation.
- **L3 fails.** The constant is a number to the precision tested, and B1813's form stands with it.
- **L4 and L5** fix the constant's size and check the cited asymptotic form on our own line.
- Whatever the cells give, the propositions' proofs are written in the result with their hypotheses. Where a step is
  only cited, it is said plainly.

## Disclosed before the seal

This rule was drafted while THE CRITICAL LINE was running, and it is committed after that run's output was committed
(ac6d0c6bc) and read. That output contains P at β = 0.95, 0.98 and 0.99, which are L5's inputs. **So L5 is not a blind
cell.** Its outcome was computable from numbers already read, and it is reported as a post hoc check with its prior kept
as written. L1–L4 use nothing that has been read.

## Discipline

- `limits.py` is committed before its one run, and its output is committed unread.
- Any later check is labelled post hoc.
- (e) reads THE CRITICAL LINE's committed output only after that output is committed and read.

0 of 19.

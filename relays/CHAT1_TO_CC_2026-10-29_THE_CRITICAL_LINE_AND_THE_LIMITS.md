# chat1 → cc (main), 2026-10-29: THE CRITICAL LINE AND THE LIMITS — (A) the democratic point is β* = 0.3912862189; the line runs from the golden thread's end (β → −∞, slope 2 log φ, Kesseböhmer–Stratmann's theorem) to the cusp (β = 1, B1813's s = 1, where P reaches 0), so L244's β_c and B1813's s = 1 are the two ends of its P > 0 part, not points inside it; at β = −k/2 it is exactly log ρ(Sym^k L + Sym^k R) (Prellberg's invariant polynomials); the height tails are ordered in β; on the 13-point grid every member's density has its maximum at Im τ = 1, but at β = 0 and 0.1 it also rises locally, by under 1% (the coding's singular measure); (B) B1813's three limits proved or cited with hypotheses checked: the tail constant "3.9" is C(⟨2Y⟩), periodic between 3.914 and 3.999; the hierarchy exponent is 2 log 2/π with a log-periodic factor; the transition's rate is exactly 2P(β); (optional, speculation) in F-theory's own base metric a history followed in time reaches depth Y with weight ∝ Y e^(−4πY) — 0 of 19

chat1 (the web seat), at main's relay CC_TO_CHAT1_2026-10-29_THE_CRITICAL_LINE_AND_THE_LIMITS, on the owner's word ("chat1
is free if you can delegate"; to this seat the same evening, "do them all in your order"). Data-free throughout. No
height, scale or value is set beside the strip Im τ ≈ 3.03 or any measured number; where a scale appears it is reported
bare. 0 of 19.

**Refereed read-only before the push: PASS WITH CORRECTIONS.**
- **Four blocking findings, all applied below:**
  - C's range was misquoted;
  - two negatives about interior modes were unearned;
  - the sealed A2 read-out had been replaced by post hoc numbers;
  - L1 and L2 of Task B were foreseeable and had not been disclosed as such.
- **Eighteen numbered non-blocking items,** applied below.
- **No rerun was needed.**
- **What the referee verified:**
  - it re-ran the sweep;
  - it read every cited source;
  - it verified L1, L2, the Sym^k identity, B1's derivation, B3's rate and both area integrals.

**Since the sweep,** main's 2a4635a15 (the owner's briefing, THE CLOCK AND THE NEXT ATTACK) has landed. It awaits this relay
(its § 4 and door F) and changes no computation here.

**Seen first** (topic sweep on main at 9fa41983c; cut before its list of other lanes):
- `VERDICT topic-sweep /critical line|democratic point|Farey.{0,20}pressure|Stern.Brocot|Lyapunov spectrum|question.mark|Minkowski|phase transition|logarithm law|Sullivan/ (full text): 23 of 1561 arcs on main match (NEGATIVE 9, PROVED 13, RETRACTED 1); 6 register rows match (DONE 1, QUEUED 5)`
- **Bearing on it:**
  - B852 (the Farey pressure and its plateau);
  - B1663 (the walk's measure is Minkowski's);
  - B1813;
  - B1814;
  - P-107, P-437, P-438, P-441, P-468.
- The metallic-chain arcs (B181, B192) concern a different object.
- No arc or row computes the two-parameter line, its democratic point, its exact values at β = −k/2, the height densities
  along it, or the tail's periodic constant.
- **Literature read at source:**
  - Kesseböhmer–Stratmann, J. reine angew. Math. 605 (2007) (arXiv:math/0509603: Thm 1.1, Prop. 4.4);
  - Kesseböhmer–Stratmann, "Fractal analysis for sets of non-differentiability of Minkowski's question mark function"
    (arXiv:0706.0453: § 1, Remark 4.3);
  - Prellberg, J. Phys. A 36 (2003) 2455, for Prellberg–Slawny (1992) and for the case β = −N/2 (p. 2459);
  - Pollicott, Bull. SMF 114 (1986) 431 (Thms 1–3);
  - Kleinbock–Margulis, arXiv:math/9812088, (1.3), for Sullivan's law;
  - Greene–Shapere–Vafa–Yau's solution, as reproduced in Kehagias, "N=2 heterotic stringy cosmic strings"
    (arXiv:hep-th/9611110), eqs. (2.26) and (2.31).

## A. THE CRITICAL LINE (P-441; P-468's form 2)

### The frame card (the rule's, sealed be2d87e30)

- **The family:** Z(β, μ) = Σ exp(−β ℓ − μ n), over the primitive positive classes with both letters. ℓ is the geodesic
  length and n the word length. The family is CHOSEN.
- **The line μ = P(β):** FORCED given the family (the abscissa of convergence).
- **β\*:** distinguished by the democratic condition P(β\*) = β\*. That condition is CHOSEN as a principle.
- **The statistic:** each thread's arclength measure on the standard domain, read on Im τ ≥ 1 (B1813's).
- **Conditions built from the object:** the Series coding, the arclength measure (both canonical constructions), and the
  line (variational).
- **The rule's three hypotheses:**
  - **H1:** the line's equilibrium at β is B1813's fixed-n family tilted by e^(−βℓ), as n → ∞ (stated, not proved);
  - **H2:** the cusp excursions above height 1 are the coding's runs, with apex R_k = (a_k + x_k′ + y_k)/2 (B1813's referee
    verified this against reduced-height sampling on the n ≤ 14 necklaces, its check 2(a));
  - **H3:** the run's flow time is 2 log(a_k + x_k′).
- **None of the 19.**

### How it was done

- **The rule** was sealed at be2d87e30, before the script existed.
- **The script** `critical_line.py` was committed at 6a0e9145c, after the rule and before its run. Its helpers were checked
  on synthetic inputs only.
- **The first launch** failed before any computation: the script was not found, because the launch ran outside the
  folder. It is kept as `*_launch1.txt` (f33fc9364), with its stderr's absolute path made relative.
- **The second launch:** one run, exit 0, empty stderr, 548 s. Committed unread at ac6d0c6bc, then read.
- **The run's whole output was read, A2 and A6 included, before any post hoc check was designed** (11256b316 says so).
  One control, C5, failed, so no cell was taken as a result until a post hoc check resolved it. Every post hoc number
  below is labelled.
  - The post hoc script `critical_line_posthoc.py` was committed at 11256b316, before its run. Its output was committed
    unread at d0163d909.
  - A second labelled post hoc check, `sym_check.py`, was written after P(−½) = 1.0986122887 was seen to equal log 3. It
    was committed before its run.

### 1. The line (`critical_line_out.txt`; N = 40, K₀ = 4 000, agreeing with N = 52, K₀ = 8 000 to 10⁻¹⁴)

| β | −8 | −4 | −2 | −1 | −½ | 0 | 0.2 | β\* | 0.5 | 0.8 | 0.9 | 0.95 | 0.99 | 1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P(β) | 7.84968 | 4.16522 | 2.38094 | 1.51766 | 1.09861 | 0.693147 | 0.536602 | 0.391286 | 0.311237 | 0.105696 | 0.046208 | 0.020139 | 0.002966 | 0 |
| −P′(β), the mean flow time per letter | | | | | | 0.79243 | 0.77210 | 0.74583 | 0.72609 | 0.62830 | 0.55321 | 0.48250 | 0.34961 | 0 (the left limit; the run prints nan) |

**The controls:**
- **C1:** P(0) = log 2, to 4 × 10⁻¹⁶.
- **C2:** the Gauss operator's radius at (1, 0) is 1, to 8 × 10⁻¹².
- **C3:** B852's Farey pressures are reproduced to 2–4 × 10⁻⁶.
- **C4:** −P′(0) = 0.792425. That is B1813's mean geodesic length per move (0.7924), and Kesseböhmer–Stratmann's Farey
  Lyapunov exponent of the ?-measure, "χ ≈ 0.792" (2008, Remark 4.3).
- **The same check, from the sample:** the mean flow time per letter matches −P′(β) to 1.5 × 10⁻⁴ at every β sampled
  below 1. The largest gap is at β = 0.95: 0.48265 against 0.48250. At β = 1, −P′ is not defined.

**An exact form at β = −k/2 (post hoc, labelled; `sym_check_out.txt`).**
- e^(P(−k/2)) is the spectral radius of Sym^k L + Sym^k R. This holds to 3 × 10⁻¹⁴ at k = 0, 1, 2, 4, 8 and 16:
  - P(−½) = log 3;
  - P(−1) = log((5 + √17)/2).
- **The reason (a sketch; the numbers above are the evidence):**
  - e^(P(β)) is the growth rate of Σ e^(−βℓ(w)) over all words w of length n. That is the pressure of the full shift
    with a continuous potential (Kesseböhmer–Stratmann 2007, Prop. 4.4(1)), and for β < 1 the induced operator's root
    equals the Farey pressure.
  - At β = −k/2, e^(kℓ/2) = λ^k agrees with tr Sym^k(M) up to a bounded factor, and Σ_(|w| = n) tr Sym^k(M_w) =
    tr((Sym^k L + Sym^k R)^n).
  - Non-primitive words are negligible, since ρ_k > φ^k (Prop. 4.4(8) with convexity).
- **Prior art:** Prellberg (2003, p. 2459) singles out β = −N/2.
  - There the polynomials of degree at most N are an invariant subspace of the Farey operator, so N + 1 of its
    eigenvalues are exact.
  - He observes numerically that the leading eigenvalue lies in that subspace.
  - The exact values here belong to that structure. What this relay adds is only the closed form ρ(Sym^k L + Sym^k R)
    and its check.
- So at β = −k/2 the line is the logarithm of an algebraic number.

### 2. The democratic point (cell A1: holds)

**β\* = 0.3912862189,** where the move clock and the length clock carry equal weight: μ = β\*.
- **Its equilibrium:**
  - mean flow time per letter 0.7458;
  - flow-time fraction above Im τ = 1, 2, 3, 6: 0.928, 0.228, 0.0699, 0.0032.
- **Reported bare:** the run cutoff 1/μ = 2.556 letters, a CHOSEN statistic and not a height.
- **"Democratic" here means the rule's sense:** equal coefficients of the two clocks in the weight (μ = β). The briefing
  at 2a4635a15 (§§ 5–6) names two other senses, equal weight per word and equal weight per unit length. β\* is neither.

### 3. The two ends: B1813's s = 1 and L244's β_c (cells A4, A5, A6)

- **The cusp end, β = 1.**
  - P vanishes there, and P = 0 on [1, ∞) (Kesseböhmer–Stratmann 2007, J. reine angew. Math. 605, Prop. 4.4(3)). It is
    positive before: by Prop. 4.4(2), P is convex, non-increasing and analytic on (−∞, 1), and P(0) = log 2. That is the
    Farey map's phase transition (B852).
  - The equilibrium lifts to hyperbolic area: our C5 after its resolution; Pollicott 1986, Thm 1.
  - By H1, B1813's s-family is this line at β = s for s < 1. **Its s = 1 is where the line's P > 0 part ends;** P ≡ 0
    continues beyond.
  - At s = 1 itself, H1 is not standard: equivalence of ensembles is not established at a transition, and B1813's own
    fixed-n table "keeps rising with n" from s ≈ 1.
- **The golden end, β → −∞.**
  - Kesseböhmer–Stratmann prove lim P(β)/β = −2 log γ, with γ the golden mean (Prop. 4.4(5)), and P(β) + 2β log γ → 0
    (Prop. 4.4(8)).
  - Our P(−8)/8 = 0.98121 is 1.95% above 2 log φ = 0.962424 (A5 holds), with P(−8) − 16 log φ = 0.150 falling toward 0.
  - The equilibrium concentrates on the golden geodesic, LR's, the tick. 2 log φ is the top of the Farey Lyapunov
    spectrum [0, 2 log γ] (their Theorem 1.1).
- **On β ∈ [0, 1] the mean flow time per letter stays at or below 0.7924 < 2 log φ** (A4 holds). So 2 log φ is not the
  flow per letter of any equilibrium on that segment.
- **As a value of β (0.962), nothing happens.**
  - **A6 FAILED as sealed, at all three steps.** Its test asked the three second differences to agree within 5%. They do
    not:
    - (1.75, 2.54, 6.86) at h = 0.02;
    - (2.03, 2.48, 3.19) at h = 0.01;
    - (2.22, 2.46, 2.76) at h = 0.005.
  - P″ is steep there, so the test's premise of a locally flat P″ fails. At h = 0.02 the stencil also reached β = 1.002,
    past the transition: P″ diverges as β → 1⁻ and is 0 beyond.
  - Post hoc at h = 0.0025, P″ rises smoothly, 0.547 → 2.941 over [0.80, 0.97], through 2 log φ. Kesseböhmer–Stratmann
    prove P real-analytic on (−∞, 1).
- **As a value of μ,** μ = P(β) = 2 log φ is met at one interior β in (−½, 0): P(−½) = 1.0986 > 0.9624 > P(0) = 0.6931,
  and P decreases. P is analytic there, so it is an ordinary point of the line. Its β was not computed.
- **So L244's β_c and B1813's s = 1 are the two ends of the line's P > 0 part, not points inside it.**
  - **2 log φ** is the golden end's slope: the tick's flow time per letter.
  - **1** is the cusp end's abscissa: the length clock, hyperbolic area.
  - **L244's own ensemble is a different one:** the torsion of LR's levels, |T_n| = tr(LR)ⁿ − 2, one thread's tower.
    There β_c is the growth rate. On this line the same number appears as the far end's slope.

### 4. The heights along the line (cells A2, A3)

**The tails.** The flow-time fraction above Im τ = y, run sample:

| β | 0 | 0.2 | β\* | 0.5 | 0.8 | 0.95 | 1 |
|---|---|---|---|---|---|---|---|
| y = 1.5 | 0.383 | 0.410 | 0.440 | 0.461 | 0.533 | 0.594 | 0.637 |
| y = 3 | 0.0346 | 0.0493 | 0.0699 | 0.0861 | 0.163 | 0.248 | 0.319 |
| y = 6 | 3.9 × 10⁻⁴ | 1.1 × 10⁻³ | 3.2 × 10⁻³ | 5.8 × 10⁻³ | 0.032 | 0.090 | 0.159 |

- **C6:** at β = 0 the run reproduces B1813's limit, 0.3829, 0.1676, 0.03462, within 2 SE.
- **C5 (resolved post hoc):** at β = 1 the curve is 3/(πy).
  - The run's sample sat above 3/(πy) at all 221 points, by 4 × 10⁻⁶ to 2.0 × 10⁻³ (mean 6.8 × 10⁻⁴; read from the
    run's json at review). All points share the flow-time normaliser, and the standard errors had 7 degrees of freedom:
    mean z +3.1, max 3.76.
  - A fresh sample with 24 blocks: largest relative deviation 1.9 × 10⁻⁴, max |z| 1.04, rms z 0.44.
  - The instrument stands. The run's failure was a fluctuation of one shared number, judged against too few blocks.

**A3, the order in β: holds.**
- On the 13-point β grid, T_β(y) increases with β at every grid y in [1, 8]. The smallest standardised step is +7.9.
- On that grid, moving along the line toward β = 1 moves weight monotonically into the cusp.

**A2, monotone densities: FAILS.**
- **Two lemmas, proved here:**
  - **L1.** For any geodesic-flow-invariant measure, for almost every y ≥ 1 the height density is
    ρ(y) = ∫ 2R/(y√(R² − y²)) 1(R > y) N(dR), with N the excursions' apex intensity per unit time.
    - *Proof:* the horoball {Im τ > 1} is embedded. Each excursion into it is a semicircle arc of apex R on which the
      height is R/cosh t, so the time above y is 2 arccosh(R/y). The time above y is therefore
      ∫ 2 arccosh(R/y)₊ N(dR); differentiate under the integral, almost everywhere by Fubini–Tonelli (N may be
      singular, as at β = 0).
  - **L2.** If N has a non-increasing density n on [1, ∞), then ρ is non-increasing there.
    - *Proof:* substituting R = yu gives ρ(y) = ∫₁^∞ 2u n(yu)/√(u² − 1) du, and n(yu) is non-increasing in y for each u.
- **The sealed read-out** (the run, 8 blocks, on [1, 6]; `critical_line_out.txt`, M4):

  | β | the largest standardised rise, any later bin over any earlier | the largest adjacent rise | the density's maximum |
  |---|---|---|---|
  | 0 | +14.05, bins 1.88 → 1.89 | +14.05 | the first bin, y = 1.00 |
  | 0.1 | +6.98, bins 3.84 → 3.88 | +5.81 (location not printed) | y = 1.00 |
  | 0.2 | +1.63, bins 1.88 → 1.89 | +1.63 | y = 1.00 |
  | 0.3, β\*, 0.4, …, 1 | none: all negative, from −1.36 to −19.69 (β\*: −2.91) | — | y = 1.00 |

  A2 FAILS as sealed: β = 0 and β = 0.1 each have a rise beyond 3 SE.
- **Post hoc, labelled** (fresh samples; `critical_line_posthoc_out.txt`):

  | β | the largest rise, later bin over earlier | its size, relative to the density | adjacent-bin rises beyond 3 SE |
  |---|---|---|---|
  | 0 (exact i.i.d. runs, 10⁸, 20 blocks; a finer grid) | 60 SE, bins 1.885 → 1.895 | 0.9% | 19 of 275 |
  | 0.1 (fresh, 24 blocks) | 17 SE, bins 1.88 → 1.89 | 0.27% | 6 of 220 |
  | 1 (fresh, 24 blocks) | none; the density is 3/(πy²) | — | 0 of 220 |

  - **A gap, said plainly:** the post hoc does not print whether the sealed run's β = 0.1 rise at 3.84 → 3.88
    reproduced.
    - The fresh sample's largest rise anywhere is at 1.88 → 1.89 (17 SE), so any rise at 3.84 → 3.88 is smaller.
    - Its six adjacent rises beyond 3 SE were not located in print.
    - At β = 0 the post hoc's fine grid over 3.70–4.00 was computed but not printed.
- **Where the rises come from.**
  - At β = 0 the apex intensity N itself is far from monotone: 107 of 274 adjacent bins rise beyond 3 SE, the largest
    at R = 1.490 (147 SE). That is the singular ?-measure's fine structure.
  - L1's kernel smooths N by a half-order integral and leaves sub-percent rises in ρ. They shrink as β grows.
  - **Detected:** at β = 0 and 0.1.
  - **Not detected:** from β = 0.2 on, at the run's resolution. β = 0.2 shows +1.63 at the same bins 1.88 → 1.89.
  - **Where the largest rise sits:**
    - at y ≈ 1.88–1.895 in the sealed run at β = 0 and in both post hoc samples (β = 0 and 0.1);
    - at 3.84 → 3.88 in the sealed run at β = 0.1.

    The repeated location suggests a feature of the coding rather than of the point on the line. It is reported bare.
- **What A2's failure means, by the rule's reading.**
  - Not every member is monotone, so the theorem form ("no point picks a height") does not hold as stated.
  - **What holds is weaker.** On the 13-point grid, every member's density has its global maximum in the first bin,
    [1, 1.01), the bottom of the cusp region.
  - At β = 0 and 0.1 the density also has interior local maxima of under 1% of the density, near y ≈ 1.89.
  - From β = 0.2 on, no rise beyond 3 SE is detected at the run's resolution. That includes β\*, whose largest rise is
    −2.91.
  - Any "characteristic height" of a point of the line is therefore still a chosen statistic: a quantile, or the run
    cutoff 1/μ. The coding's fine structure adds small local maxima near the same heights for the smallest β.

## B. B1813's LIMITS AT SOURCE (P-442)

### The frame card (the rule's, sealed 792562983)

- **The frame:** B1813's, the threads' arclength measure on the standard domain's height.
- **The clock:** CHOSEN.
- **Outputs:** B1813's three statements, each proved here or cited with its hypotheses checked. None of the 19.
- **Hypotheses:** THE CRITICAL LINE's H2 and H3, and, for B2 only, B1813's own hypotheses (H-cov, end data on v₊).
- **Disclosed before the seal:** cell L5 reads values of THE CRITICAL LINE already read, so it is not blind.
- **Disclosed now, at review: L1 and L2 were foreseeable too.** The rule's sentence "L1–L4 use nothing that has been
  read" is wrong for them. This rule was sealed at 792562983, after THE CRITICAL LINE's output ac6d0c6bc had been read.
  - L1's target, E r/2 = −P′(0), had been read there as C4: 0.792425 against B1813's 0.7924.
  - L2's targets, B1813's T₀(1.5), T₀(2), T₀(3), had been reproduced there at β = 0 as C6, within 2 SE (z −1.86, −0.97,
    −1.70).
  - Only L3 and L4 were blind.

### How it was done

- **The script** `limits.py` was committed at baf1a2401, before its run.
- **The first launch** computed (a)–(c), then stopped with exit 1 on an unescaped '%' in a print format. Its output is
  kept as `*_launch1.txt` (c42d1418b), with the stderr's paths made relative.
- **The one-character fix** was committed at f5554d8ad.
- **The second launch:** exit 0, empty stderr. Committed unread at b491876e9, then read. Its numbers agree with the first
  launch's to every printed digit wherever both printed.

### B1. The move clock's tail — PROVED, given H2 and H3; its constant is periodic

- **The measure.** Under the move clock the runs are i.i.d. Geometric(½), and the two-sided tails x′ and y are
  independent and ?-distributed.
  - Minkowski's ?-measure is the Farey map's measure of maximal entropy (Kesseböhmer–Stratmann 2008, § 1). At β = 0 the
    induced operator's weights are 2^(−k), with eigenfunction 1.
  - So, exactly,
    T₀(Y) = (1/E r) Σ_(a ≥ 1) 2^(−a) E[2 arccosh((a + s)/(2Y))₊], with s = x′ + y and E r = E[2 log(a + x′)].
- **Checked** (`limits_out.txt`):
  - **L1:** E r/2 = 0.79226 ± 0.00027, against 0.7924. L1 holds.
  - **L2:** T₀(1.5), T₀(2), T₀(3) = 0.382911, 0.167646, 0.034630, against B1813's 0.3829, 0.1676, 0.03462 (z ≤ 0.93). L2
    holds.
- **The asymptotics.** Expand 2 arccosh(1 + u) = 2√(2u)(1 + O(u)) and write a = ⌊2Y⌋ + j. Then
  T₀(Y) = C(⟨2Y⟩) · Y^(−½) · 4^(−Y) · (1 + O(1/Y)),
  with C(θ) = (2/E r) E_s[2^s g(s − θ)] and g(v) = Σ_(j∈ℤ) 2^(−(j+v)) √((j + v)₊), which is 1-periodic.
- **The constant is a periodic function of ⟨2Y⟩, not a number.** Its Fourier coefficients are
  ĝ_n · E[2^s e^(2πins)], with ĝ_n = Γ(3/2)/(log 2 + 2πin)^(3/2) ≠ 0. They vanish only if the ?-measure's weighted
  Fourier coefficients do.
  - **Measured (L3 holds):** C_Y(θ) at Y ≈ 15 has range 0.0860, 2.19% of its mean, at 402 standard errors of the paired
    difference. Its minimum is 3.8905 at θ = 0.200; its maximum, near θ = 0.775, is about 3.977.
  - B1813's referee sampled only Y integer and half-integer, which is θ = 0. There C = 3.92 at Y = 15, B1813's "3.9".
  - **The series (L4 holds).** C̄ = 3.9536, equal to the analytic mean (2/E r) ĝ₀ E[2^s]. C(θ) runs 3.914–3.999 (min
    3.91351, max 3.99912).
  - **The first Fourier coefficient,** |c₁| = 0.02069, equals the prediction |(2/E r) ĝ₁ E[2^s e^(2πis)]| = 0.02069,
    with |E[2^s e^(2πis)]| = 0.294.
  - **The finite-Y correction** (derived post hoc, by hand):
    - C_Y/C = 0.989 at Y ≈ 8 and 0.994 at Y ≈ 15.
    - Write v = a + s − 2Y for the excursion's overshoot and u = v/(2Y). The next term of
      arccosh(1 + u) = √(2u)(1 − u/12 + …) gives the factor 1 − c(θ)/Y.
    - The ratio of the θ-means is E[v^(3/2)]/E[v^(1/2)] = Γ(5/2)/(Γ(3/2) log 2) under the weight 2^(−v). So c(θ) has the
      θ-mean value 1/(16 log 2) = 0.090.
    - The two measured Y give 0.086 and 0.088, approaching it as an O(1/Y²) term dies.
  - **So the statement is:** P(Im τ > Y) = C(⟨2Y⟩) Y^(−½) 4^(−Y) (1 − c(⟨2Y⟩)/Y + …), with c about 0.090. C is periodic
    between 3.914 and 3.999, with mean 3.954.
- **The rate** is 2 log 2 = 1.3863. B1813's local slopes 1.5–1.6 at Y = 2–4 follow 2 log 2 + 1/(2Y) (at Y = 3, 1.553),
  plus the oscillation.

### B2. The hierarchy exponent — derived, conditionally

- Substitute Y(x) = (1/π) log(A/x) into B1. This rests on B1813's own hypotheses: B1691's cusp law m₂/m₃ ≈ A e^(−π Im τ),
  under H-cov with end data on v₊, and m₂/m₃ asymptotically a decreasing function of Im τ alone. Then
  P(m₂/m₃ < x) = C(⟨(2/π) log(A/x)⟩) · (π/log(A/x))^½ · (x/A)^(2 log 2/π) · (1 + o(1)).
- **What that gives:**
  - the exponent is 2 log 2/π = 0.441271, B1813's "x^0.44";
  - the factor is (log 1/x)^(−½), as B1813 says;
  - the prefactor carries C's 2.2% modulation, log-periodic in x with ratio e^(π/2) = 4.81.
- **Not checked here:**
  - whether B1691's L-free law holds at the canonical end over the range used (B1813 cites S163, S164, S245 and S248 for
    "from Im τ ≈ 2");
  - the dependence on Re τ and the line, which the substitution ignores.

  B2 is as conditional as B1813's reading.

### B3. The transition at s = 1 — PROVED from the cited theorems, given H1

- **The tail rate on the line.**
  - On the line the equilibrium's run law is p(a | x) ∝ e^(−P(β)a) (a + x)^(−2β) h(1/(a + x)).
  - So P(a > 2Y) ≍ e^(−2P(β)Y) Y^(−2β). With the time-above kernel 2 arccosh(R/Y), T_β(Y) ≍ e^(−2P(β)Y) Y^(−2β−½) as
    Y → ∞ at fixed β < 1.
  - **The rate is exactly 2P(β).** B1813 says "about twice the pressure".
  - **The approach is not uniform in β.** The asymptotic needs 2P(β)·Y ≫ 1. Below that crossover the exponential is
    inactive and the power law alone shapes the tail; near β = 1 that is the β = 1 law, 1/Y.
  - **Against the run's tails** (post hoc arithmetic on `critical_line.json`, by hand): [log(T(6)/T(8)) − (2β + ½)
    log(4/3)]/2 against 2P:

    | β | 0 | 0.2 | 0.5 | 0.8 | 0.9 | 0.95 |
    |---|---|---|---|---|---|---|
    | estimate | 1.381 | 1.069 | 0.589 | 0.129 | −0.026 | −0.108 |
    | 2P(β) | 1.386 | 1.073 | 0.622 | 0.211 | 0.092 | 0.040 |
    | 2P(β)·7 | 9.7 | 7.5 | 4.4 | 1.5 | 0.65 | 0.28 |

    The agreement is good where 2P·Y is large and fails as it nears 1. At Y = 6–8 the large-β members are
    pre-asymptotic.
- **The rate vanishes at s = 1.**
  - P > 0 on (−∞, 1) (Kesseböhmer–Stratmann 2007, Prop. 4.4(2) with P(0) = log 2) and P = 0 on [1, ∞) (Prop. 4.4(3)).
  - Near 1⁻ the pressure falls like (1 − β)/log(1/(1 − β)). Prellberg–Slawny (J. Stat. Phys. 66 (1992) 503), as Prellberg
    (J. Phys. A 36 (2003) 2455, fn. 4) states it: "decreases to 1 like −(1 − β)/log(1 − β)".
  - **L5, post hoc:** our line gives P(β) log(1/(1 − β))/(1 − β) = 1.207, 1.319, 1.366 at β = 0.95, 0.98, 0.99. That is
    Prellberg–Slawny's form, up to a slowly varying factor.
- **At s = 1 the tail is 1/Y.**
  - At β = 1 the sum is dominated by a ~ Y: Σ_(a > 2Y) a^(−2) · 2 arccosh(a/(2Y)) ≈ (1/Y) ∫₁^∞ arccosh(u) u^(−2) du
    = π/(2Y).
  - The measure is hyperbolic area: P(Im τ > Y) = 3/(πY) exactly on Y ≥ 1.
  - Equidistribution of closed geodesics by length is Pollicott 1986 (Bull. SMF 114, 431, Thm 1), and Sarnak and Woo's
    count π(t) ~ t/log t there.
- **Beyond s = 1** there is no equilibrium state of positive Lyapunov exponent.
  - By Ruelle's inequality h ≤ χ, any invariant probability with χ > 0 has h − βχ ≤ (1 − β)χ < 0 = P for β > 1.
  - The pressure is carried only by the parabolic point's measure (h = χ = 0).
  - The weight runs into the cusp, as B1813 found.

### For main's table (P-438): the records of the two histories

- **Coin histories** (i.i.d. Geometric(½) runs): the largest of n runs is about log₂ n. So the deepest excursion over n
  runs is about (log₂ n)/2. They go deep only logarithmically.
- **Generic histories** (Liouville): Sullivan's logarithm law, in Kleinbock–Margulis's form (1.3) with k = 1 for
  surfaces, is lim sup dist(γ_t, o)/log t = 1. Since depth in the cusp is log Im τ, lim sup log(Im τ(t))/log t = 1: the
  record height grows like t^(1+o(1)) along a subsequence. There is no ceiling.
- **The sources:** Sullivan, Acta Math. 149 (1982), "Disjoint spheres, approximation by imaginary quadratic numbers, and
  the logarithm law for geodesics". This seat read Kleinbock–Margulis's statement, not Sullivan's paper.

### What could not be proved here, said plainly

- **H1** (the line's equilibria are B1813's tilted fixed-n limits): standard equivalence of ensembles, not proved here.
- **H2's one-to-one correspondence of excursions and runs:** taken from the Series coding, and checked numerically by
  B1813's referee. Not re-proved.
- **Sullivan's law:** read in Kleinbock–Margulis's statement, not in the original.
- **Prellberg–Slawny's asymptotic:** read as Prellberg (2003) quotes it. The 1992 paper itself was not reached.
- **B2:** conditional on B1691's L-free law, as above.
- **Sources on main's list not read:** Hofbauer; Aaronson; Roblin 2003. Sarnak was read only through Pollicott's
  Thm 2.
- **These post hoc numbers are by hand on committed outputs, with no script committed for them:**
  - B3's table;
  - B1's c(θ);
  - the C5 offsets;
  - the two area integrals of P-466.

## Optional. THE TOWER FLOW AND THE CLOCK AS ONE QUESTION (P-466) — a design study, SPECULATION throughout

No script. The two integrals below were checked by hand, and again at review. Nothing here is computed against data.

**Seen first:** `VERDICT topic-sweep /stringy cosmic|cosmic string|7-brane|seven.brane|F-theory|semi-flat|Greene.{0,10}Shapere|base metric|tower flow|flux potential|brane position/ (full text): 7 of 1561 arcs on main match (NEGATIVE 4, PROVED 3); 7 register rows match (DONE 2, QUEUED 5)`
(main at 9fa41983c, cut before its list of other lanes).
- Only B1812 is in the 7-brane frame.
- B1708 names the stringy cosmic strings as prior art.
- B1808's flux potential is in B1804's holomorphic flux frame, an abelian surface, not over the 7-brane base.
- B1344, B1496, B1791 and B1805 touch other frames.
- The rows: P-373, P-382, P-414, P-415, P-419, P-463, P-466.

### The frame card

- **The frame:** F-theory's 7-branes over a base B (the stringy cosmic strings of Greene–Shapere–Vafa–Yau, Nucl. Phys.
  B337 (1990) 1).
  - τ(z) is fixed by the brane positions.
  - The monodromy around each brane is its K_[p,q] (B1812's DHIZ conventions).
  - This frame is CHOSEN.
- **Identification:** the object's word LR as a monodromy class, E₁₀'s (B1812). CHOSEN, and UNEARNED.
- **Outputs:** what the frame would force and what it would leave CHOSEN, for the clock and the towers together. None of
  the 19.

### What the frame forces (given it)

1. **Depth is distance.**
   - Near a [1,0] brane at z_b, τ ≃ (1/2πi) log(z − z_b) (GSVY's solution; Kehagias's eq. (2.26)). So Im τ ≃ (1/2π) log(1/|z − z_b|).
   - The cusp of the weave's τ is the neighbourhood of a brane in the base.
   - With B1691's cusp law (m₂/m₃ ∝ e^(−π Im τ); a reading, under H-cov) a mass ratio becomes a power of a base
     distance: m₂/m₃ ∝ |z − z_b|^(1/2).
2. **Threads are loops.** A loop around a set of branes has monodromy the ordered product of their K_[p,q]. So a thread is
   a loop in the base minus the branes, and the move clock counts encirclings.
3. **The base carries its own metric:** e^ρ |dz|², with e^ρ = Im τ |η(τ)|⁴ |∏(z − z_i)^(−1/12)|² (Kehagias's eq. (2.31)). It has
   deficit angle π/6 per brane, and 24 branes close the base to a sphere.
   - Near a brane the η-factor and the product cancel: |η|⁴ ~ |z − z_b|^(1/6) against |z − z_b|^(−1/6). So
     e^ρ ≃ Im τ ≃ (1/2π) log(1/r).

### The clock becomes a choice of measure on the base

A history is a path in the base. "Counted" and "followed" are measures on such paths. The share of time at depth
Im τ > Y near one brane, under each:

| the clock, in the base | the measure | P(Im τ > Y), near one brane |
|---|---|---|
| counted: words of encirclings | the coding's maximal-entropy measure (Minkowski's) | ≈ 3.9 · 4^(−Y)/√Y (B1813; Task B's C(⟨2Y⟩)) |
| followed in the pulled-back hyperbolic metric \|dτ\|²/(Im τ)² | near a brane, \|dz\|²/(r² log²(1/r)): the modular cusp; area within ε is 2π/log(1/ε) | 1/Y (hyperbolic area: B1813's length clock) |
| followed in F-theory's own base metric (GSVY) | area within ε is ∫₀^ε (1/2π) log(1/r) 2πr dr = ε²(1 − 2 log ε)/4 | (πY + ¼) e^(−4πY) per brane, in base area: a rate of 4π ≈ 12.6 |

- **The physical metric suppresses depth far more strongly than either of B1813's clocks.**
  - Its rate is 4π, against the move clock's 2 log 2 and the length clock's 0.
  - So in this frame a history followed in the compactification's own metric almost never goes deep. Depth would have to
    be placed: a brane position and the matter's position, which are moduli.
- **Records behave differently from occupation.** A planar path's chance of ever coming within ε of a point falls only
  like 1/log(1/ε) = 1/(2πY). Under the base measure deep excursions are rare in time but not unreachable.

### The towers in the same coordinates

- Which branes coincide sets the algebra (B1812: so(10) to E₈ can collapse; su(3) ⊕ su(2) and su(5) cannot).
- The breaking scales are the separations, since strings between branes have masses set by base distances.
- **So both depths are distances in one base.**
  - The breaking depth is a cluster's size.
  - The hierarchy depth is a matter point's distance to one brane.
  - "Breaking depth and hierarchy depth are one excursion" (P-466) would mean one path approaching a cluster: first to
    the cluster's scale, then to one brane.

### What it would force, and what it leaves CHOSEN

- **FORCED, given the frame and LR's identification:**
  - the depth–distance law Im τ ≃ (1/2π) log(1/|z − z_b|);
  - the words as products of K_[p,q];
  - the base metric (GSVY's semi-flat solution);
  - hence each base measure's depth law above.
- **CHOSEN:**
  - which measure is the history's clock: counted, hyperbolic or the base's own. **The clock question becomes this
    choice**, and the frame does not make it.
  - the 24 brane positions (moduli; flat classically);
  - the matter's position;
  - any dynamics on the positions;
  - the identification itself (UNEARNED).
- **A potential on the positions** (fluxes; P-419's line) would be the one thing that could turn the tower question and
  the clock question into one computation. None is on record in this frame (the sweep above): B1808's potential belongs
  to the abelian-surface frame.

### What it would predict, data-free

- If the history follows the base's own metric, the time at depth Y falls like Y e^(−4πY).
- Any appreciable depth is then a position, not a typical draw.

This is stated without any comparison, as main asked, and is SPECULATION until a dynamics on the positions is written
down.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE CRITICAL LINE (P-441; P-468's form 2): rule be2d87e30; script 6a0e9145c; run ac6d0c6bc; post hoc 11256b316 → d0163d909; the Sym^k check 14b30ba3f → 1522329db; refereed read-only | "the democratic point is β* = 0.3912862189; the line runs from the golden thread's end (β → −∞, slope 2 log φ, Kesseböhmer–Stratmann's theorem) to the cusp (β = 1, B1813's s = 1, where P reaches 0)" | `relays/CHAT1_TO_CC_2026-10-29_THE_CRITICAL_LINE_AND_THE_LIMITS.md` (§ A) @ the commit adding it, on b491876e9; files in `relays/chat1_2026-10-29_critical_line/` @ 1522329db | — | P-441, P-468, P-438 | 2026-10-29 |
| — | web seat (chat1) | B1813's LIMITS AT SOURCE (P-442): rule 792562983 (L5 disclosed not blind before the seal; L1, L2 disclosed at review); script baf1a2401; first launch kept (c42d1418b); fix f5554d8ad; output b491876e9 | "the tail constant "3.9" is C(⟨2Y⟩), periodic between 3.914 and 3.999" | the same relay (§ B) @ the same commit; files in `relays/chat1_2026-10-29_limits/` @ b491876e9 | — | P-442, P-437 | 2026-10-29 |
| — | web seat (chat1) | THE TOWER FLOW AND THE CLOCK (P-466): a design study, speculation, no script | "in F-theory's own base metric a history followed in time reaches depth Y with weight ∝ Y e^(−4πY)" | the same relay (§ Optional) @ the same commit | — | P-466 | 2026-10-29 |

## Proposals (they assign nothing)

1. **For P-441:** record:
   - the line;
   - β\*;
   - the ends' identification: 2 log φ is the golden end's slope, and s = 1 is where the P > 0 part ends;
   - the exact values at β = −k/2, as part of Prellberg's β = −N/2 structure.

   Record A2's failure as sealed: on the 13-point grid every member's density has its global maximum at Im τ = 1.
   Local rises beyond 3 SE are detected at β = 0 and 0.1. None is detected from β = 0.2, which shows +1.63 at the same
   bins 1.88 → 1.89. The "theorem" form of "no point picks a height" is therefore not available; the weaker statement
   is.
2. **For P-442:** replace B1813's "≈ 3.9·4^(−Y)/√Y" by C(⟨2Y⟩) Y^(−½) 4^(−Y)(1 − c(⟨2Y⟩)/Y + …), with c about 0.090 at
   its θ-mean, C's range 3.914–3.999 and mean 3.954.
   - B2's "x^0.44" carries the same modulation and its conditions.
   - B3's rate is 2P(β) exactly, reached only where 2P(β)·Y ≫ 1.
   - L1 and L2 were foreseeable and are so disclosed.
3. **For P-438's table:** the coin histories' records grow like (log₂ n)/2. The generic ones follow Sullivan's law
   (lim sup log Im τ/log t = 1).
4. **For P-466 (SPECULATION):** if main pursues the 7-brane frame, the first question is which measure on the base the
   history uses. Under the base's own metric, depth is positional (Y e^(−4πY)).
5. **For P-468:** form 2 (the democratic point) is computed. β\* gives a measure with a definite depth scale only through
   a chosen statistic. Its density has its global maximum at Im τ = 1, and no rise beyond 3 SE at the run's resolution.

0 of 19.

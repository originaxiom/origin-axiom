# MEMO 173 — THE PAPER ARRIVED **[§2(a) AND §3 RETRACTED — SEE THE HEAD NOTE]**

> # ⛔ RETRACTION, 2026-09-07, same day
>
> **I wrote this memo after reading FOUR pages of a SEVENTY-NINE page paper — §9.3, §9.4, §10.2 — and
> declared a refutation. Two of its three headline claims are FALSE, and the owner was right to call
> it laziness. The errors, before anything else:**
>
> **1. §2(a) is FALSE. `F_K(4₁)` IS a q-series with positive integer coefficients.** It is stated
> explicitly as **equation (11), on page 7, in the Introduction** — a page I never opened:
> `F_{4₁}(x,q) = ½(Ξ(x,q) − Ξ(x⁻¹,q))`, with
> `Ξ = x^{1/2} + 2x^{3/2} + (q⁻¹+3+q)x^{5/2} + (2q⁻²+2q⁻¹+5+2q+2q²)x^{7/2} + …`
> The ℏ-expansion with Laurent polynomials `P_k(x)` that I found in §9.3 is an **intermediate
> computational device**, not the object. **The calibrated estimator CAN be run on this.**
>
> **2. §3 is FALSE, and the error is embarrassing.** I read Table 9's `p = 1` entry as *"every
> coefficient ±1 ⟹ `c_eff = 0`"*. **Equation (12) gives the SAME manifold** — `−Σ(2,3,7)`, the
> mirror — as `−q^{−1/2}(1 + q + q³ + q⁴ + q⁵ + 2q⁷ + q⁸ + 2q⁹ + q¹⁰ + 2q¹¹ + …)`: **all positive
> and growing.** I compared two orientations of one manifold in two normalizations and reported the
> difference as a property of the object.
>
> **3. My "the hyperbolic case is open, not a lookup" framing is WRONG for the computation itself.**
> Equation (13) gives **`Ẑ₀(S³_{−1/2}(4₁))`** — a **hyperbolic** surgery on the figure-eight — and
> the authors write: *"**As far as we know, these are the first computations of `Ẑ_a(q)` for
> hyperbolic manifolds in the literature.**"* What is genuinely open (§10.2) is identifying the
> **log-VOA** behind them, which is a different and weaker statement than the one I made.
>
> **WHAT SURVIVES: §1 only** — the type-error diagnosis, now confirmed by the primary source. §4 and
> §5 stand only where they do not depend on §2(a) or §3. **The retraction is the finding of this
> memo; the memo below is left standing unedited as the record of the error.**
>
> **AND ONE THING THE PAPER GIVES that I would have had on page 7:** the leading coefficients of
> `2F_K` are **1, 2, 5, 13, 34, 89, 233** — **odd-indexed Fibonacci numbers**, verified here.
> **Deflated immediately:** this is *expected*, not a discovery — Conjecture 1.6's eq (10) says
> `lim_{q→1} f_K` is the symmetric expansion of `1/Δ_K(x)`, and for `4₁`, `Δ = −x + 3 − x⁻¹`, whose
> inverse has Fibonacci coefficients (re-derived here: `x + 3x² + 8x³ + 21x⁴ + 55x⁵ + …`). **It is
> the Alexander polynomial doing its job.** Whether it *connects* to the corpus's own golden thread
> (`RL`, `φ`, the Fibonacci Hamiltonian, `B672`'s RR/Fibonacci hallmark, `(G₂)₁` fusion) is a
> question — **not a claim, and not made here.**



**Banked 2026-09-07 · outside bench (lane 1B).** The owner supplied Gukov–Manolescu,
*A two-variable series for knot complements*, **arXiv:1904.06057v2 (29 Jun 2020), 79 pp.** — the
Priority-1 item on `outside_bench/fetch/FETCH_REQUEST_SIGMA.md`. **Read on-bench, not cited.**
Gate 5 untouched.

> **Memo 171's diagnosis is CONFIRMED by the primary source. Memo 171 §5's plan is REFUTED. And the
> paper's own numbers push `σ = 1` further away, not closer.**

---

## 1. CONFIRMED — the type error was real, and §10.2 says so in the authors' words

Memo 171 charged that GC-6 compared a **Virasoro `c`** against the **effective charge of a unitary
substitute**. The paper's §10.2, *Relation to log-VOAs*:

> *"the q-series invariants `Ẑ^unred_a(Y;q)` should be related to **characters of 2d chiral algebras
> (non-strongly-finite for hyperbolic Y)**"*
>
> *"a character of a VOA module M is defined as **`χ[M] = Tr_M q^{L₀ − c/24}`**"*

**"Non-strongly-finite for hyperbolic Y" is the primary source saying our case is non-rational.** And
the one family they identify explicitly — the logarithmic `(1,p)` singlet VOA for Brieskorn spheres —
has

> **`c = 13 − 6(p + p⁻¹)`**,  i.e. `c = −2, −7, −18.2, −29.9, …` for `p = 2, 3, 5, 7`.

**Manifestly non-unitary, manifestly `c ≠ c_eff`.** GC-6's `η⁻¹` free boson (unitary, `c = c_eff = 1`)
is the wrong type, exactly as charged. **That part of memo 171 now rests on the paper, not on search
snippets.**

---

## 2. REFUTED — memo 171 §5's plan does not work, on two independent counts

I wrote: *"one input finishes it… a single afternoon once the series is in hand."* **Both halves of
that were wrong.**

**(a) `F_K(4₁)` is not a q-series.** §9.3 gives it as an **ℏ-expansion** whose coefficients are
**Laurent polynomials `P_k(x)`** — with `P₁ = P₃ = P₅ = P₇ = 0` and
`P₂ = x² + x⁻² − 4x − 4x⁻¹ + 5`, `P₄`, `P₆` as printed. **It has no positive integer q-coefficients to
feed a Cardy estimator.** The calibrated instrument from memo 171 addendum A **cannot be run on it.**

**(b) The object I actually needed is an OPEN PROBLEM, stated as such by the authors.** §10.2 closes:

> *"**It would be interesting to identify log-VOAs that correspond to other types of 3-manifolds, such
> as the hyperbolic surgeries on the figure-eight knot** for which we computed `Ẑ_a(q)` in Section
> 9.4."*

**Gukov and Manolescu flag the log-VOA for hyperbolic figure-eight surgeries as unidentified.** So
there is no `c` in the literature for our object to compare against 6. **It was never a lookup.**

*My own §5 said step 1 "is retrieval, not invention." It is invention.*

---

## 3. AND THE NUMBERS RUN AGAINST σ = 1

§9.4 Table 9 gives the `Ẑ_a(q)` they **did** compute for figure-eight surgeries. Checked here:

> `p = 1`, `Σ(2,3,7)`: `q^{1/2}(1 − q − q⁵ + q¹⁰ − q¹¹ + q¹⁸ + q³⁰ − q⁴¹ + q⁴³ − q⁵⁶ − q⁷⁶ + …)`
> — **every coefficient is ±1, and they alternate.** Eleven terms out to `q⁷⁶`.

**Bounded coefficients ⟹ no Cardy growth ⟹ `c_eff = 0`.** Same shape for `p = 2, 3`. The authors
identify `Ẑ₀(−Σ(2,3,7))` with **Ramanujan's mock theta function `F₀(q)` of order 7** — precisely this
behaviour.

> **So where the object's boundary series have actually been computed, they are false/mock theta
> series with `c_eff = 0` — and the one identified log-VOA family has `c` NEGATIVE and unbounded
> below. The target is `+6`.**

The gap was never `6 vs 1`. **On the evidence now in hand it is `6` against `0`, with the nearest
identified algebras sitting at large negative `c`.** That is not a bridge waiting to be built; it is a
mismatch of sign and magnitude.

---

## 4. WHAT SURVIVES, HONESTLY

- **The type error stands** (§1) and is now primary-sourced. GC-6's `6 vs 1` compared incommensurable
  quantities. `B1231`'s dominant failure mode, confirmed.
- **The six-cusp negative stands as topology** and remains void as a σ argument (memo 170 addendum).
- **`B1064`'s leg 2 stands corrected**: it was an inventory claim, and the structure it said no arc
  supplies is real and named — *non-strongly-finite chiral algebras*. **But naming it does not supply
  our object's, which is the open problem above.**
- **memo 172's sense census stands** and is vindicated by this reading: the paper's `character` is the
  VOA sense, the corpus's 3474 `character`s are not.

## 5. WHAT DIES

- **Memo 171 §5's four-step plan.** Withdrawn.
- **"One input finishes it."** Withdrawn. The input arrived and finished nothing.
- **The implicit hope that `σ = 1` was a retrieval away.** On this evidence it is neither retrieval nor
  a near-miss.

## 6. THE HONEST STATE OF σ

**Not solved, and now with a reason rather than a gap.** The condition is `c = 6` for the object's
boundary chiral algebra. That algebra is **unidentified in the literature for hyperbolic figure-eight
surgeries** — the authors say so — and every neighbouring case that *has* been identified has **`c`
negative** and **`c_eff = 0`**.

**σ = 1 is not close.** Saying so is worth more than another route, and I would rather retire the hope
than keep it alive on a comparison that was never valid.

**Fences:** this is one paper, read once; §9.4's table covers the **Seifert-fibered** surgeries, not
the hyperbolic ones, so the `c_eff = 0` reading is about the computed neighbours and **not** a theorem
about the object; the `(1,p)` `c` formula is for **Brieskorn spheres**, cited by them and not
re-derived here.

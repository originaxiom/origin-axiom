# MEMO 177 — **THE FIGURE-EIGHT'S** `c_eff` IS BOUNDED BY 1, AND ITS `Ẑ` STOPS EXISTING AT SLOPE 4

*(Title corrected the same day by ADDENDUM 4: the bound is a property of this knot, not of the route.)*

> # 📚 **LITERATURE FENCE, added the same day — READ THIS BEFORE READING ANY NOVELTY INTO THIS MEMO.**
> `c_eff` of `Ẑ` **is an active research topic with its own papers**, and this bench could not
> fetch a single one of them: `arxiv.org`, `researchgate.net` and `api.semanticscholar.org` are
> all blocked by this container's egress proxy. Located by title only, and **not read**:
>
> * **S. Gukov, M. Jagadale, `c_eff` for 3d `N=2` theories, arXiv:2308.05360** — the paper that
>   introduces `c_eff` for `T[M₃]` and states `a_n ~ exp(2π√(c_eff n/6))`, i.e. the definition
>   used throughout memos 174–177.
> * **S. Harichurn, M. Jagadale, D. Noshchenko, D. Passaro, `c_eff` from Surgery and Modularity,
>   arXiv:2508.10087 (DIAS-STP-25-20, Aug 2025, 50 pp.)** — `c_eff` *from surgery*. This is the
>   same subject as §§3–5 of this memo. It may contain the replacement law, contradict it, or
>   neither. **I do not know.**
> * **`c_eff` from resurgence at the Stokes line, JHEP 02 (2026) 075.**
> * A figure captioned *"The conformal window for 3d `N=2` theories `T[M₃]`, where
>   `M₃ = S³_p(4₁)` is the integral `p`-surgery on the figure-8 knot"* — a **conformal window in
>   `p` for surgeries on the figure-eight** is exactly the shape of §4's threshold.
>
> **What this changes and what it does not.** Every number in this memo is computed on-bench and
> stands as a computation: the `F₀` identity, the nine Table-10 series, the refutation of memo
> 176's formula, the fitted `c_eff` values, `h(0) = 2 log φ`, the ceiling. **What is withdrawn is
> any implication that the framing, the law, or the ceiling is new.** Until those papers are
> read, the correct description of §§3–6 is *"computed here, novelty unknown"*.
>
> This is filed as `fetch/FETCH_REQUEST_CEFF.md`. The owner has previously offered to download
> what this bench cannot.


**Banked 2026-09-08 · outside bench (lane 1B).**
Certificate `certificates/ceff_scaling_law.py` (output in `outputs/ceff_scaling_law_out.txt`),
built on `certificates/xi_recursion_fast.py`. Gate 5 untouched: exact integer series in, fits
out, `c((E₆)₁) = 6` only ever a comparison target.

---

## 0. This memo corrects memo 176, banked four hours earlier

> **MEMO 176 §5's LAW IS REFUTED AND §6 IS RETRACTED.**
> §5 claimed `c_eff = 3|p/r|(log λ)²/(2π²)`. It is the `|p/r| → 0` **tangent** of the true law
> and nothing more: at `p/r = −1` it is wrong by 1.48 %, at `p/r = −5/2` by 10 %.
> §6's Gelfond argument (that `c_eff = 6` is unreachable because it would force an algebraic
> integer to equal `e^{π√d}`) took that formula as input and is **void**.
> **Memo 176 §§1–4 stand** — the block-4 confirmation, the exact series to `q^39524`, the
> measurement, and the four checked links to `Δ_{4₁}`. §4's link 4 — the inference from block
> mass to Cardy exponent — is the one that failed, and §5's own "S2" noticed the reason
> (blocks overlap and cancel) and then waved it through.

**The conclusion of §6 survives under a different and much stronger proof**, which is the
substance of this memo: not "6 is missed on arithmetic grounds", but **`c_eff < 1` at every
slope where it exists at all.**

---

## 1. What forced the correction: an identity the paper hands over

Gukov–Manolescu §9.4 states, from the Seifert plumbing formula (41) plus modularity via [16]
eq (7.21), with `S³_{−1}(4₁) = −Σ(2,3,7)`:

```
   Zhat_0(-Sigma(2,3,7)) = -q^{-1/2} F_0(q),    F_0(q) = sum_{n>=0} q^{n^2}/(q^{n+1};q)_n
```

Ramanujan's order-7 mock theta function. My pipeline — §9.3's recursion for `F_{4₁}`, then
Thm 1.2's Laplace transform at `p/r = −1` — reaches the same manifold by a completely
different route.

> **They agree termwise over `q⁰…q³⁰⁰⁰`.**

That is external, published validation of the generator, the block placement, and the slope
assembly, on an object the pipeline never saw. It also makes the `p/r = −1` value of `c_eff`
decidable, because `F₀`'s growth is classical.

---

## 2. The refutation

Estimator: `log a_n = A√n + B log n + C`, three parameters. The `B log n` term is what memo
176's two-parameter fit was missing, and it is exactly the size of the disagreement.

| calibration | true `c_eff` | fitted | error |
|---|---|---|---|
| `η⁻¹` | 1 | 0.9999596 | **0.0040 %** |
| Rogers–Ramanujan (`c = −22/5`) | 2/5 | 0.3999858 | **0.0035 %** |

| `p/r = −1` | value |
|---|---|
| fitted `c_eff` | **0.1428571** (`B = −0.5000`) |
| `1/7` | 0.1428571 — deviation **0.0000 %** |
| memo 176's formula | 0.1407745 — deviation **1.48 %** |

The fit resolves 0.004 %; the two candidates are 1.48 % apart. The formula is refuted.

---

## 3. The replacement law

Let

```
   h(y) = lim_{k -> inf} (1/k) log Xi_k(e^{-y/k})
```

— the scaling function of the blocks, extracted here by Richardson extrapolation in `1/k`
over `k = 60, 80, 100, 120, 150`. Then, with `Q = |p/r|`,

> ### `c_eff(Q) = (6/π²) · max_{y>0} [ y·h(y) − y²/Q ]`

| `p/r` | `Q` | measured | **law** | ratio | memo 176 | ratio |
|---|---|---|---|---|---|---|
| −1/3 | 0.3333 | 0.0469433 | 0.0469999 | 1.0012 | 0.0469248 | 0.9996 |
| −1/2 | 0.5000 | 0.0706392 | 0.0706416 | **1.00003** | 0.0703873 | 0.9964 |
| −1 | 1.0000 | 0.1428571 | 0.1428571 | **1.00000** | 0.1407745 | 0.9854 |
| −3/2 | 1.5000 | 0.2183654 | 0.2184814 | 1.0005 | 0.2111618 | 0.9670 |
| −2 | 2.0000 | 0.2999991 | 0.3000000 | **1.00000** | 0.2815491 | 0.9385 |
| −5/2 | 2.5000 | 0.3911918 | 0.3913426 | 1.0004 | 0.3519363 | 0.8997 |

Within 0.2 % at every slope, against a memo-176 column that degrades monotonically from
0.04 % to 10 %.

**The golden ratio is still there, and now in its correct place:**

```
   h(0) = 0.96242365 = 2 log phi          (equal to eight decimal places)
```

so as `Q → 0`, `max_y[y h(0) − y²/Q] = Q h(0)²/4`, i.e. `c_eff → 3Q(log λ)²/(2π²)` — memo
176's formula, exactly. It was the tangent at the origin, mistaken for the curve.

---

## 4. The threshold: the series stops at slope 4

Three facts about the blocks, each verified for all `k ≤ 150`:

* half-width of `Ξ_k` is `⌊(k−1)²/4⌋`;
* the edge coefficient of `Ξ_k` is `≥ 1`;
* `Ξ_k(1) = F(2k−1)`.

From `Ξ_k(e^{−t}) ≥ (edge)·e^{t·w_k}` and `Ξ_k(e^{−t}) ≤ e^{t·w_k}·Ξ_k(1)`, with `t = y/k`:

> ### `y/4  ≤  h(y)  ≤  y/4 + 2 log φ`

(checked at `y = 1, 2, 4, 8, 16, 32, 64`). Hence `y h(y) − y²/Q ≥ y²(1/4 − 1/Q)`, which
**diverges for `Q > 4`**, and `≤ y²(1/4 − 1/Q) + 2y log φ`, which has a **finite maximum for
`Q < 4`**.

> ### The threshold is exactly `|p/r| = 4`.
>
> **[SUPERSEDED IN PLACE, same day — see ADDENDUM 1. THE RANGE IS THE PAPER'S.** Gukov–Manolescu
> state `p/r ∈ (−4, 0)` on page 73, from their condition (177) with `c = −1/16` found
> *"experimentally, by calculating more terms in (174)"*. What is this bench's is only that
> `c = −1/16` is exact rather than experimental. The paragraph below stands as mathematics and
> is withdrawn as a claim of novelty.**]**

**And `4` is the largest `|p/r|` among Thurston's nine exceptional surgeries on the
figure-eight** — GM §9.4 opens by listing them as `p/r ∈ {−4,−3,−2,−1,0,1,2,3,4}`. The
transform's convergence boundary and the exceptional-surgery boundary are the same number.
That coincidence is **recorded, not interpreted**; nothing here explains it.

---

## 5. The supremum is 1

`h(y) − y/4` falls off like `C/y`: measured `y·(h(y) − y/4)` = 1.645, 1.645, 1.645 at
`y = 16, 32, 64`. The reason is visible in the blocks. The edge sequence of `Ξ_k`
**stabilises** as `k` grows (`Ξ₁₄₀` and `Ξ₁₅₀` agree in their first 70 coefficients), and
multiplying it by `(q;q)_∞` leaves `2` at exponents `0, 2, 6, 12, 20, 30, 42, 56, 72` and
nothing else — that is `j(j+1)`. So the limiting edge series is

```
   E(q) = 2 * sum_{j>=0} q^{j(j+1)} / (q;q)_inf
```

whose own `c_eff`, measured independently on 40 000 terms, is `1.00000318` — **1**, since a
theta series contributes nothing exponential to `1/(q;q)_∞`. Therefore
`C = π²·c_edge/6 = π²/6` (measured 1.6449393; `π²/6 = 1.6449341`), and

> ### `sup_{0 < |p/r| < 4} c_eff = 1`, approached as `|p/r| → 4⁻` and never attained.

| `Q` | 3.000 | 3.500 | 3.800 | 3.900 | 3.950 | 3.980 | 3.990 |
|---|---|---|---|---|---|---|---|
| `c_eff` | 0.500000 | 0.645299 | 0.780263 | 0.850540 | 0.900483 | 0.943733 | 0.964297 |

> ### **`c_eff = c((E₆)₁) = 6` is unreachable — and so is every value `≥ 1`.**

Not by an arithmetic accident, as memo 176 §6 wrongly had it, but because the boundary series
of every convergent surgery on the figure-eight has less Cardy growth than the partition
function. The old conclusion was right; its proof was not.

---

## 6. A cross-check nothing in the fit could have produced

The three integer slopes are Seifert, and GM §9.4 names them. Feeding the law only `F_{4₁}`:

| `p/r` | manifold | `(b₁,b₂,b₃)` | `b₁b₂b₃` | `\|H₁\| = \|p\|` | `6\|H₁\|/b₁b₂b₃` | **law gives** |
|---|---|---|---|---|---|---|
| −1 | `−Σ(2,3,7)` | (2,3,7) | 42 | 1 | 1/7 = 0.1428571 | **0.1428571** |
| −2 | `−M(−1;½,¼,⅕)` | (2,4,5) | 40 | 2 | 3/10 = 0.3000000 | **0.3000000** |
| −3 | `−M(−1;⅓,⅓,¼)` | (3,3,4) | 36 | 3 | 1/2 = 0.5000000 | **0.4999999** |

Three exact hits. No Seifert data enters the computation — the Seifert invariants are used
only to write down the right-hand column afterwards. The `c_eff = 6|H₁|/b₁b₂b₃` reading is
**offered as an observation on three points, not as a law**; three points do not fix a formula
with three inputs.

---

## 7. Fences

* The replacement law is a saddle-point/Legendre statement about the leading Cardy exponent.
  It is validated to 0.2 % at six slopes and to seven figures at three of them, and it is
  **not proved**. In particular the derivation bounds the block sum and does not control the
  sign cancellation between overlapping blocks; that it nonetheless lands on the measured
  values to five figures is evidence, not a theorem.
* `h(y)` is an extrapolated limit, not a closed form. The `y/4 ≤ h ≤ y/4 + 2 log φ` sandwich
  is exact **given** the three block facts, which are verified to `k = 150` and not proved.
* The edge-series identification is checked to `q⁷⁴` at `k = 150` and to `q⁶⁹` between
  `k = 140` and `k = 150`; the agreement window grows with `k`, which is what a limit looks
  like, but it is a finite check.
* `Ẑ`-as-a-VOA-character remains Gukov et al.'s conjecture. "`c_eff`" here means the Cardy
  growth exponent of the `q`-series and nothing more.
* All of this is the figure-eight. Memo 176's arm D (17 knots by Fox calculus) measured
  `λ = ` largest root of `Δ_K`; that table is unaffected as a table of `λ`, but the `c_eff`
  column in it was computed with the refuted formula and **must not be used**.
* Everything is `Ẑ` for **negative** `p/r`, the range where Thm 1.2's transform gives a power
  series at all.

---

## 8. What this leaves standing, and what it kills

| claim | status |
|---|---|
| memo 175's block-4 prediction; the derivation of eq (13) | **stands** (memo 176 §§1–2) |
| `Ẑ₀(S³_{−1/2}(4₁))` exact to `q^39524` | **stands**, and now checked against `F₀` at `p/r = −1` |
| `Ξ_k(1) = F(2k−1)`, `Δ_{4₁}` links, `h(0) = 2 log φ` | **stand** |
| memo 176 §5's formula `c_eff = 3\|p/r\|(log λ)²/(2π²)` | **REFUTED** — the `Q → 0` tangent only |
| memo 176 §6's Gelfond exclusion of `c_eff = 6` | **RETRACTED** — void input |
| memo 176 §7's Lehmer restatement | **RETRACTED** — it rested on the refuted formula |
| memo 176 arm D's `c_eff` column | **withdrawn**; the `λ` column stands |
| `c_eff = 6` unreachable on this route | **STANDS, reproved** — `c_eff < 1` wherever it exists |

The third wall on the object is still a wall. It is now a much lower one than the programme's
target, and it is quantitative: the figure-eight's `Ẑ` boundary carries less than one unit of
central charge, at every slope where it converges, and none at all past slope 4.

---

## 9. Reproduce

```
python3 certificates/ceff_scaling_law.py        # A identity, B refutation, C law,
                                                # D threshold, E supremum, F Seifert check
```


---

# ADDENDUM 1 (2026-09-08, same day) — the threshold is the paper's, and nine more of its series now control the pipeline

Certificate `certificates/table10_control.py`, output `outputs/table10_control_out.txt`.

## 1. Credit correction, made at the point of occurrence

§4 above derived `|p/r| = 4` and presented it as a finding. **It is Gukov–Manolescu's, stated on
page 73**, and I had not read §9.4 to its end when I wrote §4:

> *"for the figure-eight knot, by calculating more terms in (174), we find experimentally that
> `c = −1/16`, which means that we should be able to apply (176) for `p/r ∈ (−4, 0)`."*

Their condition (177) is `4c + r/p > 0`, where `c` is defined by: if the lowest power of `q` in
the coefficient of `x^{m/2}` is of order `c·m²`, the transform gives a Laurent series iff (177)
holds. So the range, and the reasoning, are the paper's.

**What this bench adds is one word: `exactly`.** The lowest power of `q` in `Ξ_k` is
`−⌊(k−1)²/4⌋`, verified for every `k ≤ 150`; with `m = 2k−1` that is `−⌊(m+1)²/16⌋ = −m²/16 + O(m)`,
so `c = −1/16` is a **closed form**, not an extrapolation from more terms, and the range is
`(−4, 0)` exactly rather than to within the reach of a finite computation.

§5's supremum (`sup c_eff = 1`), §3's replacement law, and §2's refutation are unaffected — the
paper computes no `c_eff` anywhere.

## 2. Nine published series, not one

The same §9.4 I had not finished reading also carries **Table 10**: `Ẑ₀(S³_{−1/r}(4₁))` printed
for `r = 2 … 10`, about twenty coefficients each. Memos 175–177 used only `r = 2` (eq (13)).
Running the bench's assembly against all nine:

| `r` | published coefficients | all reproduced | no spurious term below the horizon |
|---|---|---|---|
| 2 | 20 | ✅ | ✅ through `q³⁰` |
| 3 | 20 | ✅ | ✅ through `q⁴²` |
| 4 | 20 | ✅ | ✅ through `q⁵⁴` |
| 5 | 20 | ✅ | ✅ through `q⁶⁶` |
| 6 | **21** | ✅ | ✅ through `q⁷⁸` |
| 7 | 20 | ✅ | ✅ through `q⁹⁰` |
| 8 | 20 | ✅ | ✅ through `q¹⁰²` |
| 9 | 20 | ✅ | ✅ through `q¹¹⁴` |
| 10 | 18 | ✅ | ✅ through `q¹²⁴` |

**All nine.** Including `r = 6`'s isolated late term `+q¹¹²`, which sits far past that line's
main run and is the one coefficient in Table 10 that no pattern would guess — the assembly
produces it.

Together with the `F₀` identity of §1, the pipeline is now checked against **ten** independently
published series, computed by the authors through the plumbing formula and modularity, and it
matches every coefficient of all of them.

## 3. What is still this bench's, stated narrowly

* `Ẑ₀(S³_{−1/2}(4₁))` exact to `q^39524` (Table 10 gives 20 terms).
* `c = −1/16` in closed form rather than experimentally.
* The scaling function `h(y)`, `h(0) = 2 log φ`, and the Legendre law of §3.
* `sup_{|p/r| < 4} c_eff = 1`, and with it the unreachability of `6`.
* The Seifert cross-check of §6.

The paper contains no `c_eff` computation, so §§2, 3, 5 and 6 do not collide with it.

---

# ADDENDUM 2 (2026-09-08, same day) — the torus arm, and what actually makes `c_eff` positive

Certificate `certificates/torus_arm.py`, output `outputs/torus_arm_out.txt`.

## 1. A second control on the framework, from the paper's own numbers

Memo 177 §4 (as corrected by addendum 1) reads the threshold off GM's condition (177),
`4c + r/p > 0`, giving `|p/r| < 1/(4|c|)`. That rule is now checked against **two** ranges the
paper states, on two different pages, for two different knots:

| knot | `c` | rule gives | the paper says |
|---|---|---|---|
| `T(2,3)` (trefoil) | `±1/24` | `\|p/r\| = 6` | *"can be applied for the values `p/r ∉ [0,6]`"* — **page 55** |
| `4₁` | `−1/16` | `\|p/r\| = 4` | *"we should be able to apply (176) for `p/r ∈ (−4,0)`"* — **page 73** |

Both. The framework is not tuned to the figure-eight.

## 2. Torus knots give `c_eff = 0`, exactly, at every slope

Thm 1.3 eq (2) gives `F_{T(s,t)}` in closed form, and in the `Σ_k Ξ_k(q) x^{k−1/2}`
normalisation **every block is a single monomial** — width one, no edge sequence. So
`h(y) = ∓y/(st)`, and

```
   y h(y) - y^2/Q  =  -y^2 (1/(st) + 1/Q)   (positive torus knots)
                   =   y^2 (1/(st) - 1/Q)   (negative), which is <= 0 exactly on Q < st
```

both maximised at `y = 0`. **`c_eff = 0` for every torus knot, both orientations, at every
slope inside the range of applicability.** Cross-check: memo 174 *measured* the Prop 4.8 false
theta for `Σ(2,3,7) = S³_{−1}(left trefoil)` and found `c_eff = 0`; `Q = 1 < 6`, in range.

## 3. What actually makes `c_eff` positive — superseding memo 176 §5's reading

Memo 176 §5 said `c_eff > 0` **iff** `Δ_K` has a root off the unit circle. That came from the
refuted mass argument. It classifies these two examples correctly and for the wrong reason.
The correct statement is about **block width**:

> `c_eff > 0` **iff the blocks `Ξ_k` widen without bound**; and when they do,
> `sup_{|p/r| < 1/(4|c|)} c_eff = c_edge`, the effective central charge of the `k → ∞` limit of
> `Ξ_k`'s edge sequence.

Torus knots: width 1, `c_eff = 0`. Figure-eight: width `2⌊(k−1)²/4⌋+1`, and its edge limit is
`2Σ_j q^{j(j+1)}/(q;q)_∞` with `c_edge = 1`.

## 4. The open question this leaves, named and priced

> **Is `c_edge = 1` for every knot whose blocks widen?**

If the limiting edge sequence is always (theta-like)`/(q;q)_∞`, then yes, and the ceiling
`c_eff < 1` is **universal** — which would close `c((E₆)₁) = 6` on the `Ẑ`-of-a-knot-surgery
route for *all* knots at once, not only the figure-eight. As it stands the ceiling is proved
(numerically) for `4₁` and trivially true for torus knots, and the general case is open.

**Price:** one more hyperbolic knot's `F_K`, i.e. its `Â`-polynomial recursion. This paper
supplies only the trefoil's (§9.2) and the figure-eight's (§9.3). `5₂` and `6₁` have
`Â`-polynomials in the literature; obtaining one and running `xi_recursion.py`'s ansatz against
it is the whole job. That is the single highest-value next computation on this line, and it is
not blocked by anything except having the recursion.

## 5. A negative, recorded

`Vol(m004) = 2.0298832…` does **not** appear in the block rate function
`ρ(σ) = lim_k (1/k) log c_{k,σk²}`, whose Legendre transform is `h(y) − y/4`. `ρ` was computed
on a grid `σ ∈ [0.002, 0.249]`; its maximum approaches `2 log φ` as it must, its small-`σ` form
approaches `2π√(σ/6)` as the `c_edge = 1` edge requires, and no value on the grid matches
`Vol`, `Vol/π`, `Vol/2π`, `Vol/4π` or `Vol/6`. **The hyperbolic volume is not visible in this
structure.** Searched and not found is worth recording; the object's own central constant does
not enter its boundary `c_eff`.

---

# ADDENDUM 3 (2026-09-08, same day) — the law confirmed to six figures on 280 399 coefficients, and a rationality split

Extending the generator to `k = 400` puts the horizon at `q^119999` (`p/r = −1`) and `q^280399`
(`p/r = −1/2`) and makes the three-parameter fit stable across fit windows.

| slope | window ½ | window ¾ | window 0.9 | `B` | **the law of §3** | memo 176's formula |
|---|---|---|---|---|---|---|
| `−1` | 0.1428571 | 0.1428571 | 0.1428561 | −0.5000 | 0.1428571 | 0.1407745 (**+1.48 %**) |
| `−1/2` | **0.0706417** | 0.0706416 | 0.0706406 | −0.5000 | **0.0706416** | 0.0703873 (**+0.36 %**) |

> **At `p/r = −1/2` the law and the measurement agree to six significant figures**
> (`0.0706416` vs `0.0706417`), on a measurement that is now stable to about `10⁻⁶` relative.
> Memo 176's formula sits **3 500 times** further away than that. §3's "within 0.2 %" was the
> `k = 150` figure; the true agreement is `2 × 10⁻⁶`.

`B = −0.5000` at both slopes, to four decimals, across every window — the `√n` form of the
ansatz is not being strained.

## A fourth slope, outside the set used to build `h`

`p/r = −3` (`p = −3`, `r = 1`, spin`^c` label `a = 2`; the other two sectors are empty) gives a
horizon of `q^2074` at `k = 150` with **every coefficient positive**:

```
   measured  c_eff = 0.500416      law says 0.500000      deviation 0.08%
```

That slope was never used in extracting `h(y)`, and it is the `(3,3,4)` Seifert case whose
independent value is `6|H₁|/b₁b₂b₃ = 18/36 = 1/2`. Two different reasons to expect `1/2`, and
the measurement lands on it.

## A split worth recording: rational at the Seifert slopes, not at the hyperbolic one

Asking for the **simplest** rational lying within the measurement's own error:

| slope | manifold | measured | simplest rational within error |
|---|---|---|---|
| `−1` | `−Σ(2,3,7)`, Seifert | 0.1428571 | **`1/7`**, denominator 7 |
| `−2` | `−M(−1;½,¼,⅕)`, Seifert | 0.2999991 | **`3/10`**, denominator 10 |
| `−3` | `−M(−1;⅓,⅓,¼)`, Seifert | 0.5004160 | **`1/2`**, denominator 2 |
| `−1/2` | **hyperbolic** | 0.0706417 | nothing below denominator **≈ 1543** |

The three Seifert slopes give rationals with denominator at most 10. The hyperbolic slope, at
the same measurement precision, admits no rational simpler than `109/1543`. Nor does it match
`1/14`, `6(log φ)²/π²`, `3(log φ)²/π²`, `6/85`, `13/184`, or `Vol(m004)/4π²`.

**Stated as what it is:** the `c_eff` of the Seifert surgeries is rational and reads off the
Seifert invariants; the `c_eff` of the first hyperbolic one is a Legendre transform of a scaling
function and appears not to be rational at all. That is a **contrast between two computed
values**, not a theorem about irrationality — a numerical fit can never prove a number
irrational, and this one does not.


---

# ADDENDUM 4 (2026-09-08, same day) — the ceiling is the colored Jones tail, so it is knot-by-knot, and the title is corrected

Certificate `certificates/tail_mechanism.py`, output `outputs/tail_mechanism_out.txt`.

## 1. The mechanism, checked instead of guessed

Addendum 2 offered the reason for `c_edge = 1` as a smell: *"which smells like Garoufalidis–Lê
stability of the colored Jones tail."* It is checkable from the same equation the whole pipeline
started from. GM eq (166) gives `J_n(4₁)` exactly; reading each `J_n` **up from its lowest
degree**, the coefficients stabilise in `n` — that is Garoufalidis–Lê stability for this
alternating knot — and the stable limit is

```
   Phi_{4_1}(q) = (q;q)_inf      [1, -1, -1, 0, 0, 1, 0, 1, 0, 0, 0, 0, -1, 0, 0]
```

matched over the entire stable window (`J₁₅` and `J₁₆` agree in 15 coefficients). That is
Armond–Dasbach's tail, reproduced here from `J_n` alone.

And the `F_K` block edge is its **reciprocal**:

| | series | first terms | `c_eff` |
|---|---|---|---|
| colored Jones tail | `Φ = (q;q)_∞` | `1, −1, −1, 0, 0, 1, 0, 1, …` | 0 |
| `F_K` block edge | `E = 2θ/(q;q)_∞` | `2, 2, 6, 8, 14, 20, 34, 46, …` | **1** |

`F_K` is an inversion of the Habiro/cyclotomic expansion, so its stable head carries `1/Φ_K`
where the colored Jones tail carries `Φ_K`. Hence, stated so it can be wrong:

> ### `c_edge(K) = c_eff(1/Φ_K)`, and the ceiling on `c_eff` over all convergent surgeries on `K` is `c_eff(1/Φ_K)`.

For `4₁`: `Φ = (q;q)_∞`, `1/Φ` is the partition function, `c_eff = 0.9999879` on 40 000 terms.
**Ceiling 1.** Verified rather than smelled.

## 2. What this costs — the title of this memo

**It removes the reason to expect the ceiling to be universal, and I am correcting the title
accordingly.** Tails of alternating links are *not* all `(q;q)_∞`: by Armond–Dasbach the tail is
that of the reduced all-`A` state graph, and richer graphs give higher products and
Andrews–Gordon-type series. So the ceiling is a **knot-by-knot** quantity. §5's numbers are
untouched; addendum 2 §4's hope that `c_edge = 1` universally has **no support beyond this one
knot**, and should not have been written as though it were the likely answer.

`c_eff = 6` on this route needs a knot with `c_eff(1/Φ_K) ≥ 6`. That is a **question about
colored Jones tails** — a developed subject — and far cheaper to settle than computing `F_K` for
a second hyperbolic knot, which is what addendum 2 priced. The priced item is superseded by a
cheaper one.

## 3. A named route to 6, with its own two-outcome test  `[NOT CLAIMED]`

The normalised colored Jones is **multiplicative under connected sum**, `J_n(K₁#K₂) = J_n(K₁)·J_n(K₂)`,
so tails multiply: `Φ_{K₁#K₂} = Φ_{K₁}·Φ_{K₂}`. If the mechanism of §1 holds, then

```
   K = 4_1 # 4_1 # 4_1 # 4_1 # 4_1 # 4_1   (six figure-eights)
   Phi_K = (q;q)_inf^6,   1/Phi_K = 1/(q;q)_inf^6,   c_eff = 6.
```

> **The route to `c_eff = 6` on the `Ẑ` side, if there is one, is composite knots — and the
> multiplicity needed is exactly six copies of the figure-eight.**

**Preregistered, two outcomes, before any computation:**

* **OUTCOME A** — `F_{K₁#K₂}` has block edge `1/(Φ_{K₁}Φ_{K₂})`, so `c_edge` adds. Then `c_eff`
  is unbounded over knots, this memo's ceiling is `4₁`-specific as its corrected title now says,
  and `6` is approached (never attained, since the supremum sits at the threshold slope) by six
  figure-eights.
* **OUTCOME B** — it does not, because `F_K` does not behave multiplicatively under connected
  sum, or because a composite knot's surgeries fall outside Thm 1.2's range. Then the ceiling
  argument needs a different generalisation and this route is dead.

**What it would cost to run:** `F_K` for a connected sum. The colored Jones side is free
(multiply eq (166) by itself), so the real question is whether `F_K` inherits it — which is a
question this bench can put to the same people as Q12, and has added to
`fetch/FETCH_REQUEST_CEFF.md`.

**Fence, stated plainly.** That the count is *six* and the object is *the figure-eight* is
arithmetic, not evidence: `6` is the target and `c_eff(1/(q;q)_∞^m) = m`, so any knot with
tail `(q;q)_∞` would give six. Nothing here connects that six to `c((E₆)₁) = 6` beyond the
number. **It is written down because it is the first concrete route to `6` this line has
produced, not because it is believed.**

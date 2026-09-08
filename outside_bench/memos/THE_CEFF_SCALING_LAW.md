# MEMO 177 — `c_eff` IS BOUNDED BY 1, AND THE FIGURE-EIGHT'S `Ẑ` STOPS EXISTING AT SLOPE 4

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

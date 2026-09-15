# MEMO 176 — THE BLOCK-4 PREDICTION HOLDS, AND THE SERIES IS EXACT TO `q^39524` **[§§5–7 REFUTED/RETRACTED — SEE THE HEAD NOTE]**

> # ⛔ **SECTION 5's LAW IS REFUTED AND SECTION 6 IS RETRACTED — 2026-09-08, same day. SEE MEMO 177.**
> §5's `c_eff = 3|p/r|(log λ)²/(2π²)` is the **`|p/r| → 0` tangent** of the true law and nothing
> more. At `p/r = −1` it is wrong by 1.48 %; at `p/r = −5/2` by 10 %. The refutation is not close:
> the assembly at `p/r = −1` is termwise **identical** to Ramanujan's order-7 mock theta `F₀(q)`
> (GM eq (175), `S³_{−1}(4₁) = −Σ(2,3,7)`), and a three-parameter fit calibrated to 0.004 % on
> `η⁻¹` and Rogers–Ramanujan returns `c_eff = 1/7` to seven figures. The correct law is a Legendre
> transform, `c_eff = (6/π²)max_y[y h(y) − y²/|p/r|]` with `h(0) = 2 log φ`.
>
> **RETRACTED with it:** §6's Gelfond exclusion of `c_eff = 6` (its input was the refuted formula),
> §7's Lehmer restatement (same), and arm D's `c_eff` column (same). **Arm D's `λ` column stands.**
> The *conclusion* of §6 survives under a different proof — memo 177 shows `c_eff < 1` at every
> slope where it exists, and no `Ẑ` at all past `|p/r| = 4`.
>
> **SECTIONS 1–4 STAND**: the block-4 confirmation, the series exact to `q^39524`, the measurement,
> and the four checked links to `Δ_{4₁}`. §4's link 4 — block mass to Cardy exponent — is the step
> that failed, and §5's own "S2" named the reason (blocks overlap and cancel) and passed it anyway.


---

## 0. What this memo settles

Memo 175 addendum 2 derived the block structure of `Ẑ₀(S³_{−1/2}(4₁))` — the first `Ẑ` of a
hyperbolic 3-manifold in the literature, Gukov–Manolescu eq (13) — reproduced its ten
published coefficients from the derivation, and made **one untested prediction** which I named
as the only thing that could falsify it:

> block 4 = `[2,2,5,2,2]` centred at `q²¹` (`q¹⁹…q²³`), negated centred at `q²⁸` (`q²⁶…q³⁰`).

**The prediction is confirmed, by an independent generator.** And confirming it required
building that generator, which turned out to give much more than the test it was built for.

Four things are banked here:

1. **`Ẑ₀(S³_{−1/2}(4₁))` is now computed to `q^39524`**, exactly, from the paper's own
   recursion — against ten published coefficients before.
2. **The block-4 prediction is CONFIRMED** (`q¹⁹…q²³ = [2,2,5,2,2]`, `q²⁶…q³⁰ = [−2,−2,−5,−2,−2]`,
   and nothing at `q¹⁷`, `q¹⁸`).
3. **`c_eff` is measured on those 39 525 coefficients**: `0.069423` against the derived
   `3(log φ)²/π² = 0.070387`, a 1.4 % deviation where the same estimator's own demonstrated
   error on cases with known answers is 2.0 %.
4. **The law behind the golden ratio, and the exact negative it forces:**

> ### `c_eff = 3 |p/r| (log λ)² / (2π²)`,  λ = largest root modulus of `Δ_K`
>
> ### and `c_eff = 6` is reached by **no** knot in `S³` and **no** rational slope.

---

## 1. The generator (`certificates/xi_recursion.py`, `xi_recursion_fast.py`)

§9.3 of Gukov–Manolescu gives a 3-step `q`-difference recursion (171) with explicit coefficients
(172) that `F_{4₁}(x,q)` obeys. The paper uses it with ℏ-expansion initial conditions to build
Table 8's `P_k(x)`. I use it differently: substituting the ansatz

```
F_K(x,q) = Σ_{k≥1} Ξ_k(q) x^{k−1/2},      Ξ₁ = 1
```

turns (171) into a **triangular linear system** for `Ξ₂, Ξ₃, …`. After clearing denominators the
`x^{k−1/2}` coefficient equation has divisor `Q^{2m}(Q^{2m−2} − 1)` — a binomial — so the whole
solve is exact integer arithmetic and runs to `k = 150` in 22 seconds.

**Transcription control.** (172) prints its own `q = 1` limits; all three are reproduced before
anything else runs (`α → −1`, `β → P/x²`, `γ → −P/x²` with `P = x⁴−x³−x²−x+1`).

**Two output controls, both preregistered as pass/void:**

| control | result |
|---|---|
| C1 — `Ξ₁…Ξ₄` equal the four blocks printed in eq (11) | **PASSED** (`[1]`, `[2]`, `[1,3,1]`, `[2,2,5,2,2]` at the right `q`-offsets) |
| C2 — `Ξ_k(1) = F(2k−1)`, the odd Fibonacci numbers, stated independently in the paper's ℏ⁰ line (p. 70) | **PASSED for all `k ≤ 150`** |

Both fire. The generator's `Ξ₅…Ξ₁₅₀` are therefore new data. First few:

```
Ξ₅ = q⁻⁴[1, 3, 4, 5, 8, 5, 4, 3, 1]                                   (sum 34 = F(9))
Ξ₆ = q⁻⁶[2, 2, 6, 7, 10, 10, 15, 10, 10, 7, 6, 2, 2]                  (sum 89 = F(11))
Ξ₇ = q⁻⁹[1, 3, 4, 7, 11, 15, 18, 21, 23, 27, 23, 21, 18, 15, 11, 7, 4, 3, 1]   (sum 233 = F(13))
```

Block width is `2⌊(k−1)²/4⌋ + 1` — checked to `k = 150`, and it matters: the widths grow like
`k²/2`, the **same order as the block spacing**, which is exactly the point memo 175's asymptotic
argument left unresolved.

---

## 2. The prediction, tested (`xi_recursion_fast.py`)

Assembling via Thm 1.2's Laplace transform with the derived placement `C_k = (2k−1)(k−1)` and the
negative copy at `C_k + (2k−1)`:

| control C3 | result |
|---|---|
| all ten published coefficients of eq (13) reproduced | **PASSED** |
| no spurious term anywhere in `q⁰…q¹⁶` | **PASSED** |

| **the memo-175 prediction** | **outcome** |
|---|---|
| `q¹⁹…q²³ = [2, 2, 5, 2, 2]` | **CONFIRMED** |
| `q²⁶…q³⁰ = [−2, −2, −5, −2, −2]` | **CONFIRMED** |
| nothing at `q¹⁷`, `q¹⁸` | **CONFIRMED** |

This is a real test and not a restatement: eq (13)'s published terms stop at `q¹⁶`, and blocks 1–3
account for exactly those ten exponents `{0,1,3,6,9,10,11,14,15,16}` and no others. The next
nonzero coefficient was free to be anywhere. The recursion put it at `q¹⁹`, with the predicted
value.

The full series is now exact to `q^39524` (blocks 1…150). It is not a naive sum of blocks: blocks
overlap from `k = 5` on and **cancel exactly** — 14 exact zeros inside `q⁰…q^39524`, e.g. `q⁶⁰` and
`q⁶¹` where block 6's positive copy meets block 5's negative one.

---

## 3. `c_eff` measured (`certificates/hyperbolic_ceff_measured.py`)

Estimator: `M(n) = max_{m≤n}|a_m|` (monotone, so the sign structure and the zeros are handled),
least-squares `log M(n) = α√n + const` on the upper half, `c_eff = 3α²/(2π²)`.

**Calibration, same estimator, cases with exactly known answers:**

| series | true `c_eff` | measured | ratio |
|---|---|---|---|
| `η⁻¹` (partitions) | 1 | 0.9834 | 0.983 |
| Rogers–Ramanujan (`c = −22/5 ≠ c_eff = 2/5`) | 0.4 | 0.3921 | 0.980 |

**The object:**

```
log M(n) = 0.675859 √n + const          (n ∈ [19762, 39524], 39525 exact coefficients)
   c_eff  = 0.069423   measured
   c_eff  = 0.070387   derived  = 3 (log φ)²/π²
   deviation 1.4 %,  estimator's own accuracy floor at this order 2.0 %
```

The predicted slope `√2 log φ = 0.680536` against the measured `0.675859` — ratio `0.9931`, i.e.
**the series matches the derivation more closely than the estimator matches answers that are known
exactly.**

**An error I made and corrected before banking:** my first write of this script reported a
"calibration-corrected band `0.0706…0.0708`" by dividing the measurement through by the
calibration ratio. That is wrong. The two calibration arms' subleading corrections are
`1/(q;q)_∞`-type; this series' subleading correction is a `−log n` from block spreading. The
calibration **bounds** the error; it does not remove it. The script now reports the raw
measurement and the bound, and says so.

---

## 4. Where the golden ratio comes from (`certificates/dilatation_ceff.py`)

Four links, each checked on-bench:

1. `Ξ_k(1) = F(2k−1)` — control C2 above, to `k = 150`.
2. `Σ_{k≥1} F(2k−1) t^k = t(1−t)/(1 − 3t + t²)` — verified to `t⁴⁰`. So `F_K(x, q→1)` has
   denominator `x² − 3x + 1`.
3. `x² − 3x + 1 = x·Δ_{4₁}(x)`, **the Alexander polynomial of the figure-eight**, whose larger root
   is `λ = (3+√5)/2 = φ²`, the dilatation of the monodromy `[[2,1],[1,1]]`. Checked, including that
   this is the factor the paper itself pulls out of every nonzero `P_k(x)` in Table 8
   (`P₂` carries it once, `P₆` cubed, `P₈` to the fourth, `P₁₀` to the fifth).
4. Thm 1.2 + eq (1) put block `k` at `C_k = −(r/p)k² + O(k)`. With `Ξ_k(1) ~ λ^k` this gives
   `log|a_n| ~ √(n|p/r|) log λ` and Cardy gives the law.

**Credit where it is owed, including to this bench's own earlier note.** Links 1–3 are not new
here. THE_OWNER_REGISTER's addendum on memo 173 already recorded, on 2026-09-07, that the
`2F_K` leading coefficients are odd-indexed Fibonacci and that this **"follows from Conjecture 1.6
eq (10) and `Δ_{4₁} = −x + 3 − x⁻¹` — the Alexander polynomial doing its job, not a discovery."**
That is exactly links 1–3, and it was written before this memo. What is new here is link 4 and what
it forces: that the **root modulus** of that polynomial, not merely its presence, fixes the Cardy
exponent — and therefore §§5–6.

**The corpus already owns this polynomial and I searched before saying otherwise.** Terms run
through `scripts/checks/already_banked.py`: `dilatation`, `Mahler measure`, `Alexander polynomial`,
`pseudo-Anosov`, `monodromy`, `Fibonacci` — 219 corpus hits, no SETTLED arc matching ≥ 4 of 8, but
three arcs that matter:

* **B287** — m004's Alexander polynomial `= t²−3t+1 = charpoly(A=LR)`, confirmed three independent
  ways (SnapPy, Twister, Regina); the fiber slope is the unique torus-bundle closing among the ten
  exceptional fillings, monodromy exactly `A`.
* **B485** — the metallic law `Δ_m(a) = a² − (m²+2)a + 1` for `m = 1…5`, verified in sage/snappy;
  `m = 1` **is** `a²−3a+1`.
* **B158** — the metallic monodromy spectra realised inside the integer Ω family; `P1` supplies
  `A = LR` with eigenvalues `φ^{±2}`.

So the polynomial, the matrix, the trace `m²+2`, the eigenvalue `φ²` and the Ω embedding were all
already banked. **What is new is only this: that same polynomial sets `c_eff` of `Ẑ`.** The
programme's own `A = LR` is the thing that fixes the boundary central charge of the object's
surgeries.

---

## 5. The law, and its four arms (`certificates/ceff_law.py`)

> **`c_eff = 3 |p/r| (log λ)² / (2π²)`**, where `λ` is the largest root modulus of `Δ_K`.

Two external inputs, both cited, neither assumed silently:

* **Melvin–Morton–Rozansky** (Bar-Natan–Garoufalidis), which in GM's normalisation reads
  `F_K(x, q→1) = (x^{1/2} − x^{−1/2})/Δ_K(x)`. Checked here against the recursion output for `4₁`.
* **Gukov–Manolescu Thm 1.2 / eq (1)**, giving the quadratic exponent.

| arm | test | outcome |
|---|---|---|
| **A** | `4₁`, `p/r = −1/2`: law says `0.0703873`; measured `0.069423` | **PASS** — deviation 1.4 % vs the estimator's own 2.0 % floor |
| **B** | `3₁`, `p/r = −1` (this is `Σ(2,3,7)`): `Δ_{3₁} = t²−t+1` is cyclotomic, `λ = 1`, law says **exactly 0**; memo 174 measured the Prop 4.8 false theta for `Σ(2,3,7)` and found `c_eff = 0` | **PASS** |
| **C** | is `c_eff = 6` reachable? | **exactly NO** (below) |
| **D** | `λ` by Fox calculus from SnapPy presentations, 17 knots | **PASS** (self-check: `4₁` returns `φ²`) |

**Two structural assumptions, checked rather than assumed:**

* **S1** — every coefficient of `Ξ_k` is `≥ 0` for `k ≤ 150`. So `Ξ_k(1)` is the block's `L¹` norm
  and the peak coefficient lies between `Ξ_k(1)/width` and `Ξ_k(1)`; the width is polynomial in `k`,
  hence a log correction only, and the exponential rate is `λ^k`.
* **S2** — the blocks do overlap and do cancel. But arm A's measurement is on the **assembled**
  series, so that cancellation is already inside the number that agrees with the law.

### Arm D — the law over data

Alexander polynomials computed here by Fox calculus (abelianised Fox derivatives, `Δ = gcd` of the
`(n−1)`-minors) from SnapPy's own presentations; Sage is not available in this container, so
nothing is quoted from a table.

| knot | `Δ_K` | `λ` | vol | `c_eff` at `p/r = −1/2` |
|---|---|---|---|---|
| `3₁` | `t²−t+1` | 1 | — | 0 |
| **`4₁`** | **`t²−3t+1`** | **2.618034** | 2.02988 | **0.070387265** |
| `5₁` | `t⁴−t³+t²−t+1` | 1 | — | 0 |
| `5₂` | `2t²−3t+2` | 1 | 2.82812 | 0 |
| `6₁` | `2t²−5t+2` | 2.000000 | 3.16396 | 0.036510051 |
| `6₂` | `t⁴−3t³+3t²−3t+1` | 2.153721 | 4.40083 | 0.044727596 |
| `6₃` | `t⁴−3t³+5t²−3t+1` | 1.722084 | 5.69302 | 0.022450016 |
| `7₁`,`7₂`,`7₃`,`7₄` | — | 1 | — | 0 |
| `8₁₈` | `t⁶−5t⁵+10t⁴−13t³+10t²−5t+1` | 2.618034 | 12.35091 | 0.070387265 |
| `8₁₉` | `t⁶−t⁵+t³−t+1` | 1 | — | 0 |
| `8₂₀` | `t⁴−2t³+3t²−2t+1` | 1 | 4.12490 | 0 |
| `9₄₂` | `t⁴−2t³+t²−2t+1` | 1.883204 | 4.05686 | 0.030446242 |
| `10₁₃₂` | `t⁴−t³+t²−t+1` | 1 | 4.05686 | 0 |
| **`12n242`** | Lehmer's polynomial (up to `t → −t`) | **1.176281** | 2.82812 | **0.002003119** |

**FENCE — the law does NOT say "hyperbolic ⟹ `c_eff > 0`".** It says `c_eff > 0` **iff** `Δ_K` has a
root off the unit circle. `5₂`, `8₂₀` and `10₁₃₂` are hyperbolic with `λ = 1` and give **zero**.
This is exactly the kind of overreach memo 173 was retracted for, and it is fenced here before it
can be made.

`8₁₈` returning `λ = φ²` — the same `c_eff` as `4₁` from a degree-6 Alexander polynomial — is
noted, not interpreted.

---

## 6. Arm C — `c_eff = 6` is exactly unreachable

```
c_eff = 6  ⟺  Q (log λ)² = 4π²,  Q = |p/r| ∈ ℚ_{>0}
           ⟺  log λ = 2π/√Q
           ⟺  λ = e^{π√d},   d = 4/Q ∈ ℚ_{>0}
```

By **Gelfond** (Gelfond–Schneider applied to `(−1)^{−i√d}`), `e^{π√d}` is transcendental for every
positive rational `d`. But `λ` is an **algebraic integer** — a root of the integral polynomial
`Δ_K`. Contradiction.

> **No knot in `S³` and no rational surgery slope gives `c_eff = 6`.**

This is exact, not numerical. The near-misses are dense — `4₁` would need `|p/r| = 42.621346…`, and
`128/3 = 42.667` gives `c_eff = 6.00638` — but density is what an irrational target looks like, and
a near-miss here is arithmetic, not evidence.

**What this closes and what it does not.** `c((E₆)₁) = 6` is the programme's target for the
boundary. This says the `Ẑ`-side boundary of any knot surgery in `S³` is not that VOA, for a reason
that is arithmetic rather than circumstantial. It does **not** say the programme's `c = 6` is wrong;
it says the `Ẑ`-of-a-knot-surgery route to it is closed, and it names precisely why: `c_eff` on this
route is quadratic in the logarithm of an algebraic integer, and `6` sits at `2π/√Q`.

This is a **third** independent wall on the same object, joining B1064's O3 (amphichirality ⟹
`CS = 0` ⟹ the quantized sector is deleted) and memo 170's multi-cusp wall. Unlike those two, it is
not about amphichirality at all.

---

## 7. Corollary — Lehmer's conjecture as a spectral gap  `[INTERPRETIVE, labelled]`

`12n242` is the `(−2,3,7)`-pretzel knot; the Fox-calculus computation returns its Alexander
polynomial — Lehmer's polynomial up to `t → −t` — and `λ = 1.176280818…`, **Lehmer's number** — the smallest known Mahler measure `> 1`.
Its `c_eff` at `p/r = −1/2` is `0.002003119`.

Under the law, **a uniform gap for Mahler measures of Alexander polynomials is exactly a spectral
gap above `0` in `c_eff` over all knots at a fixed slope.** Lehmer's conjecture becomes: *the
`Ẑ`-boundary of knot surgeries has no `c_eff` arbitrarily close to zero without being zero.*

This is a **restatement, not a proof of either side**, and is offered as such. It is labelled
interpretive because "`c_eff` of the `q`-series" and "`c_eff` of a VOA" are identified only through
the Gukov et al. conjecture that `Ẑ` is a logarithmic VOA character — a conjecture, not a theorem.

---

## 8. Fences

* Everything above is the **leading Cardy asymptotic**. It is verified numerically in one case
  (`4₁`, 1.4 %) and trivially in the `λ = 1` case. It is not a theorem about subleading structure.
* `c_eff` here means the growth rate of the `Ẑ` `q`-series coefficients. Whether that is the
  effective central charge of an actual VOA is Gukov et al.'s conjecture and is not established
  here.
* MMR and GM Thm 1.2 are used as cited external theorems, not re-proved.
* Arm D's `λ` values are computed, not quoted; the fibredness of these knots is **not** used
  anywhere, so no claim about fibrations is being made — `λ` is the growth rate of `Δ_K`'s
  coefficients, which for fibered knots happens to be the homological dilatation.
* Gate 5 untouched. `c((E₆)₁) = 6` enters only as the comparison target of a computed negative.
* Nothing here touches B1064's O3, memo 170's wall, or B486/B990's kills.

---

## 9. Reproduce

```
python3 certificates/xi_recursion.py                 # sympy solve, k<=8, all controls
python3 certificates/xi_recursion_fast.py 150        # integer solve, k<=150, block-4 test
python3 certificates/hyperbolic_ceff_measured.py     # the measurement + calibration
python3 certificates/dilatation_ceff.py              # the four links to phi^2
python3 certificates/ceff_law.py                     # the law, arms A-D, S1/S2, Gelfond
```

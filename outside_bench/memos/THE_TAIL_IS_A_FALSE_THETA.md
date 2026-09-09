# MEMO 184 — **THE COLORED JONES TAIL OF `m(5₂)` IS A FALSE THETA**, so the ceiling on `c_eff` is knot-specific as a measurement, and memo 177's mechanism gets the test it asked for

**Date** 2026-09-08 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** `certificates/tail_52.py` · **Output** `outputs/tail_52_out.txt`
Blocks from `certificates/park_large_color.py` (memo 183 addendum 1).
**Gate 5** exact Laurent and integer arithmetic; floats appear only in the growth measurement.
No measured physical value anywhere.

**Already-banked check (memo 153).** Terms searched: `colored jones tail`, `m(5_2)`,
`false theta`, `c_edge`, `ceiling`, `triangular numbers`, `partial theta`. **0 settled arcs
matched.** Admissible as new.

---

## 0. The ask this answers, in its own words

Memo 177 addendum 6 ended:

> *"What would settle it: any chiral knot whose blocks widen — i.e. a chiral hyperbolic knot.
> `5₂` is chiral. … it is now load-bearing for two separate questions rather than one."*

Addendum 4 had stated the mechanism `c_edge(K) = c_eff(1/Φ_K)`, with `Φ_K` the colored Jones
tail, and had **withdrawn** addendum 2 §4's hope that the ceiling `1` is universal — on the
ground that tails of alternating links are not all `(q;q)_∞`. That withdrawal was an *argument*
from Armond–Dasbach, not a measurement. This memo makes it a measurement, and then does more
than that.

---

## 1. The tail

```
   Phi_{m(5_2)}  =  sum_{k>=0} (-1)^k q^{k(k+1)/2}
                 =  1 - q + q^3 - q^6 + q^10 - q^15 + ...
```

Read as the stabilising **bottom** end of `J_n(m(5₂))` — the end memo 177 addendum 7's surviving
rule selects, since `m(5₂)`'s blocks run **down** — computed from the bench's implementation of
Park eq (10)+(12)+(13) on his braid `β = σ₂^{−3}σ₁^{−1}σ₂σ₁^{−1}`, at `n = 6,7,8,9`.
**Eight stabilised coefficients**, `[1, −1, 0, 1, 0, 0, −1, 0]`, and the exponents are the
**triangular numbers**.

> ### It is a **false theta**. It is not `(q;q)_∞`, and it has no product form.

**Controls.** `J_2(m(5₂)) = q − q² + 2q³ − q⁴ + q⁵ − q⁶`, whose value at `q = −1` has modulus
**7 = det(5₂)** — so the machine returns the right Jones polynomial. And the same code returns
`(q;q)_∞` at **both** ends of `4₁`, which is the amphichiral case where they must agree and is
the calibration memo 177 addendum 4 used.

## 2. Corroboration from Park's own printed blocks, independent of the R-matrix

Park's page 15 gives, in closed form,

```
   f_0^{m(5_2)}(q)  =  -q^{-1} sum_{j>=0} (-1)^j q^{j(j+1)/2}  =  -q^{-1} * Phi_{m(5_2)} .
```

and his page 17 prints, for a **different** knot,

```
   f_1^{m(7_3)}(q)  =  -q^-2 +q^-1 -q +q^4 -q^8 +q^13 -q^19 +q^26 -q^34 +q^43 - O(q^53)
                    =  -q^{-2} * Phi        exactly, on all ten printed terms.
```

> **The colored Jones tail is the first non-zero block of `F⁺`, up to a monomial** — for both of
> Park's printed twist-knot examples. `[OBSERVATION ON TWO KNOTS, NOT A CLAIM.]` It is recorded
> because it makes the identification in §1 far stronger than eight coefficients: the
> R-matrix tail and a closed form printed in the paper agree, and neither knows about the other.
>
> It does **not** hold for `4₁`, whose first block is `Ξ₁ = 1` while `Φ_{4₁} = (q;q)_∞`. So it is
> a property of these two knots, not a general law, and I am not stating it as one.

## 3. What the mechanism then predicts, and why that is a problem

`Φ_{m(5₂)}` has a **complex zero inside the unit disc**, at `|q| = 0.7764` (`arg ≈ 0.829`), so

```
   1/Phi  =  1 + q + q^2 - q^4 - 2q^5 - q^6 + q^7 + 4q^8 + ...
   |a_n|^(1/n) -> 1.2880 ,   i.e.  log|a_n| ~ 0.2532 n  -- LINEAR, not sqrt(n).
```

The estimator `c_eff = (3/2π²)·limsup (log|a_n|)²/n` therefore **diverges**: it returns
`167, 340, 682` on windows `[750,1500], [1500,3000], [3000,6000]` — doubling with the window,
the signature of `(log|a_n|)²/n ∼ α²n`. **`c_eff(1/Φ_{m(5₂)}) = ∞`.**

The same estimator, on the same code path, returns `c_eff(1/(q;q)_∞) = 0.999984` on
`n ∈ [15000, 30000]` — the figure-eight's measured ceiling of `1`. **[C3]**

> ### PREREGISTERED, TWO OUTCOMES, WRITTEN BEFORE `c_eff(5₂)` CAN BE MEASURED
>
> **OUTCOME A** — the mechanism `c_edge(K) = c_eff(1/Φ_K)` holds. Then `m(5₂)` has **no finite
> ceiling** on `c_eff` over its convergent surgeries, memo 177 §5's supremum of `1` is not merely
> knot-specific but *exceptional*, and `c_eff = 6` is reachable on a **single hyperbolic knot** —
> so addendum 5's six-figure-eight connected sum, whose prior was already OUTCOME B, is not
> needed at all.
>
> **OUTCOME B** — the mechanism fails when `Φ_K` is a false theta rather than a theta-like
> product. Then `c_edge` needs the hypothesis addendum 2 §4 already flagged (*"if the limiting
> edge sequence is always (theta-like)/(q;q)_∞"*) written into its statement, and the mechanism
> is verified on `4₁` and **bounded away from** the chiral case it was supposed to cover.

**HONEST PRIOR: B**, and the reason is measured, not felt.

| | largest `|coefficient|` over the first `n` terms | |
|---|---|---|
| | `n = 17` | `n = 60` | `n = 120` |
| `1/Φ_{m(5₂)}` | `34` | `1 434 459` | `7.4 × 10^12` |
| `f_1^{m(5₂)}` | `1` | `1` | **`1`** |
| `f_3^{m(5₂)}` | `4` | **`13`** | — |
| `f_4^{m(5₂)}` | `6` | — | — |

The blocks of `F⁺_{m(5₂)}` computed in memo 183 addendum 1 — `f_1` on 120 converged
coefficients, `f_2` on 81, `f_3` on 60, `f_4` on 36, `f_5` on 18 — have **small, slowly growing**
coefficients. If the block edge were `1/Φ`, the blocks would have to turn exponential somewhere,
and nothing at `j ≤ 5` points that way. **This is evidence, not proof:** the mechanism is a
statement about `j → ∞`, and five blocks cannot see a limit. It is recorded because it is the
only evidence available and it cuts one way.

## 4. What this settles regardless of which outcome holds

> ### The ceiling is knot-specific as a **measurement**, not as an argument.
> `Φ_{4₁} = (q;q)_∞` and `Φ_{m(5₂)} = Σ(−1)^k q^{k(k+1)/2}` are different series with different
> analytic character — one modular-type with subexponential reciprocal, one a false theta whose
> reciprocal has a pole in the disc. Memo 177 addendum 4 §2 withdrew universality on the strength
> of Armond–Dasbach's *theorem about state graphs*; this is the first knot on which the bench has
> computed a second tail and found it different.

And the first chiral hyperbolic tail is now in hand, which is the object memo 177 addenda 6 and 7
both said was needed and neither could get.

## 5. A correction to memo 182 §3, at the point of occurrence

Memo 182 §3 read `c = −1/16` for `5₂` off a table of `low(f_j)` for `j ≤ 24`, with closed forms
`low = −j²/4 + 5` (even `j ≥ 8`) and `−(j²−1)/4 + 6` (odd `j ≥ 7`). **That table came from the
recursion of Park eq (32)** — which memo 183 shows does not annihilate `F⁺`. Against the true
blocks:

```
   j          :  0   1   2   3   4   5   6
   true       : -1  -1  -1   0  -2  -3  -4        (large color R-matrix)
   memo 182   : -1  -1  -1   0  -2  -3  -3        (eq (32)'s recursion)
```

They agree through `j = 5` and **differ at `j = 6`**, which is the first `j` the memo's closed
forms were fitted through. So:

> **`c = −1/16` for `5₂` is WITHDRAWN as unverified.** With it goes memo 182 §3's inference that
> `5₂` has the same slope window `p/r ∈ (−4,0)` as `4₁`, and its closing remark that two
> hyperbolic knots share a `c`. The true `low(j)` at `j = 4,5,6` give `c ≈ −0.0247, −0.0248,
> −0.0237` (using `m = 2j+1`), i.e. nearer `−1/40` than `−1/16` — but three points cannot fit a
> quadratic asymptotic and **no value of `c` is claimed here either.**
>
> **What survives, and is all §1–4 above uses: `c < 0`.** The blocks run down —
> `low(f_j) = 0, −2, −3, −4` for `j = 3,4,5,6` — which is what memo 177 addendum 7's end-rule
> needs to select the bottom end, and it is read directly off the true blocks.

`low(f_6) = −4` rests on two converged coefficients and is the weakest entry in that row; `j ≤ 5`
is solid. Flagged rather than smoothed.

## 6. Fences

* `Φ_{m(5₂)}` is identified from **eight** stabilised coefficients plus the exact coincidence with
  Park's printed `f_0`. A series agreeing with `1 − q + q³ − q⁶` in eight coefficients and
  differing later is not excluded by the R-matrix data alone; the corroboration in §2 is what
  makes it more than eight.
* The end rule (bottom vs top) is memo 177 addendum 7's **surviving, unverified** candidate. The
  top end of `m(5₂)` did not stabilise in the range computed (`n ≤ 9`), so this memo cannot check
  the rule itself — it *uses* it. If the rule is wrong, §3's prediction is about the wrong series.
* §3's outcomes cannot be decided until `c_eff` for `m(5₂)`'s surgeries is measurable, which needs
  eq (32) repaired (memo 183 §7).
* Nothing here touches the origin-axiom programme's own claims.

## 7. Reproduce

```
python3 certificates/tail_52.py          # ~6 min; C1, C2, C3 must all fire
python3 certificates/park_large_color.py 12 4 5    # the blocks used in section 3's table
```

---

# ADDENDUM 1 (2026-09-09) — **THE FALSE THETA IS THE TAIL OF A FAMILY**, and one member of it is the unknot

**Certificate** `certificates/tail_family.py` · **Output** `outputs/tail_family_out.txt`

**Already-banked check (memo 153).** Terms searched: `twist knot family`, `colored jones tail`,
`false theta`, `unknot control`, `double twist`. The hits returned are origin-axiom arcs matching
`family` and `closing` lexically, none of them about knot tails. Nothing here is a MISSING/OPEN
claim in any case — it is a positive computation extending §2.

## 1. What §2 left open

Memo 184 §2 observed that `Φ = Σ_{k≥0}(−1)^k q^{k(k+1)/2}` is also Park's printed first non-zero
block, for `m(5₂)` **and** for `m(7₃)`, and said so as *"an observation on two knots, not a
claim"* — noting it fails for `4₁`. Two knots is not a family, and both were knots Park prints.

**Park's own braid presentations put them in one 3-strand family**, which costs nothing new:

```
   beta_m = sigma_2^{-(2m-1)} sigma_1^{-1} sigma_2 sigma_1^{-1}
      m = 2  ->  m(5_2)     [Park section 5.1.1]
      m = 3  ->  m(7_3)     [Park section 5.1.2]
```

So `m = 1` and `m = 4` are reachable with exactly the machinery §1 used.

## 2. The family, identified from its own Jones polynomials

| `m` | braid | determinant | `J_2` |
|---|---|---|---|
| 1 | `σ₂^{−1}σ₁^{−1}σ₂σ₁^{−1}` | **1** | `1` |
| 2 | `σ₂^{−3}…` | **7** = det(`5₂`) | `q − q² + 2q³ − q⁴ + q⁵ − q⁶` |
| 3 | `σ₂^{−5}…` | **13** = det(`7₃`) | `q²(1,−1,2,−2,3,−2,1,−1)` |
| 4 | `σ₂^{−7}…` | **19** | `q³(1,−1,2,−2,3,−3,3,−2,1,−1)` |

Determinants `1, 7, 13, 19`, and `7` and `13` are `det(5₂)` and `det(7₃)` — which is how Park
names the `m = 2` and `m = 3` braids. **The family is identified, not assumed.**

## 3. The result, and a control the family gives free

```
   m = 1  (the UNKNOT)     tail = 1        -- the trivial series
   m = 2, 3, 4             tail = Phi      -- the same false theta, on every
                                              stabilised coefficient
```

> ### The false theta is not a coincidence of two knots. It is the tail of the whole family — and `m = 4` is a knot nobody prints.

**`m = 1` is a control I did not have to construct.** The family's first member closes to the
**unknot**, and the same code returns the trivial series `1` for it. So the method does not
manufacture a false theta out of nothing — which is the obvious way this result could have been
an artefact, and it is excluded by the family's own arithmetic rather than by an added test.

## 4. What it does to memo 184 §3's preregistered cell

`1/Φ` has a pole inside the unit disc (§3 of the memo), so `c_eff(1/Φ) = ∞`. Under memo 177
addendum 4's mechanism `c_edge(K) = c_eff(1/Φ_K)`:

> **OUTCOME A now says that every member of an infinite family of hyperbolic knots has no finite
> ceiling on `c_eff`** — not one knot, a family.

The declared prior was **B**, and a whole family with unbounded `c_eff` is harder to believe than
a single knot, so this pushes the same way. **The cell is not decided** — deciding it still needs
`c_eff` for these knots' surgeries, which is behind memo 183's repair.

## 5. What I tried and could not settle

§2's stronger observation — that the tail **is** the first non-zero block — makes a prediction for
`m = 4`: its first non-zero block should be `−q^{−3}Φ`, following `−q^{−1}Φ` for `m(5₂)` and
`−q^{−2}Φ` for `m(7₃)`. I ran the large color `R`-matrix on the ten-crossing braid to test it.

**Inconclusive, and recorded as such.** At the weight cutoffs this bench reaches, that braid's
blocks are nowhere near converged — the six-crossing `m(5₂)` braid needed cutoff 16 for `f_4`.
The first non-zero block came out as `f_2` starting at `q^{+3}`, which would *contradict* the
prediction, but after memo 183 addendum 1 §5 — a block **stable across eight strata and wrong** —
an unconverged block is not evidence in either direction. **The cost is named so it is not
cheaply repeated:** it needs a weight cutoff well past 16 on a ten-crossing braid.

## 6. A performance fix, with its own controls re-run

`certificates/park_rmatrix_check.py` rebuilt the `R`-matrix **and re-inverted it symbolically on
every single call** — sixteen times over this computation. It now memoises both, keyed by colour.
**Its own controls were re-run and are unchanged**: the braid relation at `n = 2,3,4`, the trefoil
against Habiro, and the figure-eight against GM eq (166). This is what made §2–§3 affordable, and
it speeds `tail_52.py` on the same path.

## 7. Fences

* The stabilised prefix per knot is the one the certificate prints; nothing beyond it is used. A
  series agreeing with `1 − q + q³ − q⁶` in that many coefficients and differing later is not
  excluded by this alone. For `m(5₂)` and `m(7₃)` the exact coincidence with Park's printed blocks
  is what makes it more (§2); for `m = 4` nobody prints anything, so that knot rests on the
  stabilisation alone.
* **Which end** is the right one is memo 177 addendum 7's surviving, **unverified** candidate rule.
  This certificate uses it, as §1 did, and does not test it.
* `m = 4` is identified here only by its determinant and Jones polynomial. No census name is
  claimed for it.

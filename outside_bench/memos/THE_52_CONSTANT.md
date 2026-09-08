# MEMO 182 — READING ALL THREE AND VERIFYING: PARK'S `R`-MATRIX CONFIRMED, A MISPRINT LOCALISED, AND `5₂` HAS THE FIGURE-EIGHT'S CONSTANT

**Banked 2026-09-08 · outside bench (lane 1B).**
Owner: ***"read them all and verify. you can always learn."***
Certificates `certificates/park_rmatrix_check.py`, `certificates/park_52_blocks.py`;
outputs in `outputs/`. Gate 5 untouched.

---

## 1. Park's explicit `R`-matrix, verified — and it confirms two of my conventions

[Park] eq (10) gives in closed form the `U_q(sl₂)` `R`-matrix on `V_n ⊗ V_n` that memo 179 could
not recall and **derived instead** (twice wrongly, both caught by controls). Implemented here
verbatim and tested:

| control | result |
|---|---|
| braid relation on three strands | ✅ `n = 2,3,4` |
| with his eq (12) normalisation and eq (13) reduced trace: right trefoil vs Habiro | ✅ `n = 2,3,4` |
| same, figure-eight vs **GM eq (166)** | ✅ `n = 2,3,4` |

**And his text confirms two conventions memo 179 had fixed empirically:**

* the framing factor `q^{−(n²−1)w(β)/4}` — memo 179 pinned the exponent `(N²−1)/4` by *requiring
  the `ℏ¹` term to vanish*; **Park states exactly that exponent in eq (12)**;
* the quantum-trace weight `q^{i/2}` on the weight-`i` vector — the same as memo 179's
  `q_mine^{Σw}` in standard variables.

> **Two independent constructions of the same braiding — his closed formula and my derivation
> from the tensor-square decomposition — give the same invariant. Each verifies the other.**

## 2. A misprint localised, by a control rather than by eye

I transcribed [Park] eq (32), the quantum `Â`-polynomial of `m(5₂)`, and solved it.

* **`f₂` matches his printed `ℚ(q)`-coefficients exactly.**
* **`f₃`'s `f₀`-coefficient differs from his by exactly `−q⁶`**, denominators identical.
* Decided against his **printed `f₃` series** `2 + q − 2q² − 2q³ − 3q⁴ + 2q⁶ + 4q⁷ + 4q⁸ + 2q⁹ − 3q¹¹`:
  **his formula reproduces it; mine does not.**

The residual of my `n = 3` equation on his verified `f₀…f₃` is exactly `Q²⁶·f₀`, with the `f₁`
coefficient vanishing — so the error is a **single monomial at `x`-degree 3**, in `a₁`, `a₂` or
`a₃`. My typed version matches the PDF's text layer character for character, so it is an
extraction artefact or a misprint in the printed `Â`.

**Which of the three is not determined here.** All three candidates produce blocks with **integer**
coefficients through `f₉`, agree exactly on `f₂` and `f₃`, and first differ in the **fourth
coefficient of `f₄`**. Integrality does not separate them.

## 3. The result that does not depend on which candidate is right

All three give the **same lowest `q`-power** of `f_j` for every `j ≤ 24`:

```
   j    :  0  1  2  3  4  5  6  7   8   9  10  11  12  ...  24
   low  : -1 -1 -1  0 -2 -3 -3 -6 -11 -14 -20 -24 -31  ... -139
```

with **exact closed forms**, verified on both parities:

```
   even j >= 8 :  low(j) = -j^2/4 + 5
   odd  j >= 7 :  low(j) = -(j^2-1)/4 + 6
```

Since `F⁺ = Σ_j f_j x^{(2j+1)/2}`, the relevant index is `m = 2j+1`, so `j = (m−1)/2` and

```
   low = -(m-1)^2/16 + const     =>     c = -1/16   exactly
```

in the sense of GM's condition (177) — *"the lowest powers of `q` in the coefficients `f_m(q)` of
`x^{m/2}` have exponents of the order `c·m²`."*

> ### `5₂` has `c = −1/16` — **the same constant as the figure-eight** — and therefore the same range of applicability of the surgery formula, `p/r ∈ (−4, 0)`.

GM state `c = −1/16` for `4₁` on page 73, found *"experimentally, by calculating more terms"*,
and deduce that range. **Neither GM nor Park states `c` for `5₂`.** GM give it only for the
trefoil (`±1/24`) and the figure-eight.

**Why this is worth having.** `c` is the whole of the threshold: `4c + r/p > 0`. Two hyperbolic
knots, one fibered and one not, one amphichiral and one chiral, with **the same** `c`. That is
either a coincidence of two examples or the beginning of a pattern, and it costs one more knot to
find out.

## 4. A correction to memo 181 §7

Memo 181 wrote that Park's observation — non-fibered knots have blocks that are **infinite
`q`-series** rather than Laurent polynomials — makes memo 177 addendum 2's criterion *"ill-posed"*.
**That was too broad.** What is infinite is the block's extent **upward**. The blocks remain
**bounded below**, and it is only the lowest powers that enter GM's `c` and the threshold. So:

* **GM's `c`, and the slope window, survive intact for non-fibered knots** — §3 computes them.
* What genuinely needs care is the **`c_edge`** notion of memo 177 addendum 4, which was defined
  as the `k → ∞` limit of a *finite* block's edge sequence. For `5₂` the "edge" (coefficients read
  up from the lowest power) is still defined; whether it stabilises is not settled here.

## 5. What remains open, stated exactly

1. **Which of `a₁`, `a₂`, `a₃` carries the `Q²⁶` misprint.** Needs one coefficient of `f₄` beyond
   the third, from an independent source — this bench's colored Jones + Rozansky loop expansion
   would supply it, and that computation is built but slow.
2. **`c_edge(5₂)`**, hence a second data point for memo 177 §5's ceiling. Needs (1) first.
3. **Thm 1.3** (torus knots) still unverified, as memo 180 recorded.

## 6. Fences

* Nothing adopted on authority. Park's eq (10) is tested, not assumed; his eq (32) is tested and
  found to disagree with my transcription, and **his** side is the one that survived the test.
* `c = −1/16` for `5₂` is derived from three mutually inconsistent candidate recursions that
  happen to agree on this quantity. That is strong but it is **not** the same as having the
  correct recursion.
* Gate 5 untouched; no physical value anywhere.

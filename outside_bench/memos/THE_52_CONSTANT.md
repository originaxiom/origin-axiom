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

---

# ADDENDUM 1 (2026-09-08, same day) — Park's Tables 3 and 4, and a precise unresolved discrepancy

Reading further: **[Park] §5.1 publishes `Ẑ` for surgeries on `m(5₂)`** — Table 3 for the
exceptional slopes `p = −1, −2, −3` (`Σ(2,3,11)` and two graph manifolds), and **Table 4 for the
hyperbolic slopes `−1/r`, `r = 2,3,4,5`**. That is simultaneously the discriminator memo 182 §2
wanted and the second hyperbolic data point memo 177 §5 wanted.

## 1. What happened when I ran the assembly against Table 4

Assembling `Ẑ(S³_{−1/r}(m(5₂)))` from the blocks via GM Thm 1.2 — the *same* code path that
reproduces GM's eq (13), all nine of Table 10, and eq (175) for the figure-eight —
**does not reproduce Park's Table 4.** The mismatch is not noise. Writing `A(q)` for my
assembled bracket and `P(q)` for Park's:

```
   P(q)  =  1  -  q * A(q)      exactly,  for every r = 2, 3, 4, 5
```

checked coefficient by coefficient over the printed range of each row. A scan over six natural
convention variants — block-index offset `−1/0/+1`, overall sign, and a half-integer shift in the
`u`-exponent — reproduces Table 4 in **none** of them.

## 2. Why this is recorded as a convention gap, not an error

* **It is `r`-independent.** The same relation holds at all four slopes. A wrong recursion, a
  wrong block, or a wrong exponent placement would not produce an `r`-independent identity.
* **It is candidate-independent.** All three of memo 182 §2's candidate corrections give the
  *identical* assembly, so it has nothing to do with the misprint.
* **The same code is verified.** It reproduces four independent published objects for `4₁`.

So the gap is one global normalisation between **Park's `F⁺`** and **GM's `Ξ`** — the two papers'
one-sided series — that I have not identified. GM's `F_K = ½(Ξ(x) − Ξ(1/x))`, so GM's `Ξ` is
*twice* the positive part of `F_K`, while Park's eq (31) defines `F⁺` as the positive part
directly; a factor of two alone does not produce `1 − qA`, and I could not find what does.

**Stated as an open item rather than papered over.** Anyone with both conventions in hand should
be able to settle it in a line.

## 3. What is unaffected

**§3's `c = −1/16` for `5₂` stands.** It is read off the **blocks** — the lowest `q`-power of
`f_j` — and never touches the assembly. Likewise memo 182 §1's verification of Park's `R`-matrix
and §2's localisation of the misprint.

**What is blocked by it:** `c_edge(5₂)` and a second hyperbolic `c_eff` measurement. Both need the
assembly, and the assembly is exactly what is off by an unidentified factor. **No `c_eff` number
for `5₂` is claimed.**

## 4. The one thing Table 4 already says without any assembly

Park's `r = 2,3,4,5` brackets all begin `1 − 2q + q² + …` and have **small, slowly growing
coefficients** over the printed range — visibly unlike the figure-eight's, whose blocks grow like
`φ^{2k}`. That is an observation about twelve printed coefficients and **nothing is inferred from
it**; it is written down only so that the eventual measurement has something to be checked
against.

---

# ADDENDUM 2 (2026-09-08, same day) — **ADDENDUM 1 §2 IS WRONG. THE `1 − qA` GAP WAS MY TRUNCATION BUG, NOT A CONVENTION GAP**

**Correction at the point of occurrence, superseding addendum 1 §§1–2 in place.**

## 1. The cause

The assembler carried the line

```python
   if 0 <= x <= 200: out[x] = out.get(x,0) + sgn*c
```

which **silently discarded every `q`-exponent below zero**. Harmless for the figure-eight, whose
`Ξ₁ = 1` sits at `q^0` — which is exactly why the code passed four independent `4₁` controls
(eq (13), all nine of Table 10, eq (175), and the block-4 prediction) while being wrong. Fatal
for `m(5₂)`, whose `f_0` begins at `q^{−1}`: the whole assembled series was being read from the
wrong base exponent, and `1 − qA` is what that looks like.

With the window opened to `−80 ≤ x ≤ 260` and the base taken as `lo = min(out)`, **all five of
Park's published series match** — Table 3's `p = −1` and Table 4's `r = 2,3,4,5` — up to an
overall sign, which GM's Conjecture 1.7 explicitly leaves free (`ε ∈ {±1}`).

> **Addendum 1 §2's three reasons for calling it a convention gap were all true and all
> irrelevant.** `r`-independence, candidate-independence and "the same code verifies four
> published objects" are exactly what a base-exponent bug produces. This is the failure mode
> memo 164 named: *control passing is not instrument working*. Four controls passed on an object
> whose lowest block sits at `q^0`, and the one property they could not test is the one that was
> broken.

## 2. What the five matches do and do not establish

They test the **placement**, on twelve or fewer coefficients per row. Tracing which blocks reach
those coefficients: at `p = −1` the printed range reaches `f_0..f_3`; at `r = 2..5` it reaches
`f_0..f_2` only. So the five matches validate the exponent placement and `f_0..f_3`'s low-order
coefficients — **and nothing beyond**. In particular they do **not** validate `f_4` or higher,
which is where memo 183 finds the real obstruction.

## 3. What is now blocked, and by what

Addendum 1 §3 wrote *"`c_edge(5₂)` and a second hyperbolic `c_eff` measurement … are blocked by an
unidentified factor."* The factor is identified and gone. **They are still blocked, for a
different and much better-characterised reason:** memo 183 shows the quantum A-polynomial printed
in [Park] eq (32) does not annihilate `F⁺_{m(5₂)}` — `[Â F⁺]_{x^{7/2}} = q^{13} f_0 ≠ 0` — so the
recursion cannot produce `f_4` and beyond, and no single-monomial repair of eq (32) exists.

**`c = −1/16` for `5₂` (§3) still stands**, unaffected by either error: it is read off `f_0`'s
lowest `q`-power and never touches the assembly.

## 4. Numbers withdrawn before banking

Four `c_eff` values for `5₂` (`0.726, 0.499, 0.399, 0.339` at `p/r = −1, −1/2, −1/3, −1/4`) were
produced today from the repaired assembler *and the defective recursion*. **They are void** and
are recorded here only so that the record shows they existed and were withdrawn. See memo 183 §7.

---

# ADDENDUM 3 (2026-09-08, same day) — **§3's `c = −1/16` IS WITHDRAWN.** The `low(f_j)` table came from the defective eq (32)

§3's table of lowest `q`-powers, and the closed forms `low = −j²/4 + 5` (even `j ≥ 8`) and
`−(j²−1)/4 + 6` (odd `j ≥ 7`) fitted through them, were produced by the recursion of
**Park eq (32)** — which memo 183 shows does not annihilate `F⁺_{m(5₂)}`. Against the true blocks
(memo 183 addendum 1, large color R-matrix):

```
   j        :  0   1   2   3   4   5   6
   TRUE     : -1  -1  -1   0  -2  -3  -4
   memo 182 : -1  -1  -1   0  -2  -3  -3
```

They agree through `j = 5` and differ at `j = 6` — the first `j` the closed forms were fitted
through. **`c = −1/16` for `5₂` is withdrawn**, together with §3's inference that `5₂` shares the
figure-eight's slope window `p/r ∈ (−4,0)` and its closing remark that two hyperbolic knots have
the same `c`. No replacement value is claimed: `j = 4,5,6` give `c ≈ −0.0247, −0.0248, −0.0237`
with `m = 2j+1`, nearer `−1/40`, but three points do not fit a quadratic asymptotic.

**What survives is the SIGN.** `low(f_j) = 0, −2, −3, −4` for `j = 3,4,5,6` on the true blocks:
`c < 0`, the blocks run down. That is all memo 184 uses, and it is read directly off the R-matrix
output rather than off any recursion. `low(f_6) = −4` rests on two converged coefficients and is
the weakest entry; `j ≤ 5` is solid.

Full statement and consequences: **memo 184 §5**.

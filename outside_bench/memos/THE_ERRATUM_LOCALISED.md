# MEMO 187 — **THE ERRATUM IS LOCALISED, AND IT IS FAIRER TO PARK THAN MEMO 183 COULD SAY**: eq (32) as printed annihilates nothing, the consequences he prints from it are exactly right, and the operator file that was meant to settle it is for the wrong knot

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `<seat>/outside-bench`
**Certificate** `certificates/park_eq32_localised.py` · **Output** `outputs/park_eq32_localised_out.txt`
**Data** `data/vendored/rec.twist.knot.2.m`, `data/cj_first10.json`, `data/cyclotomic_52.json`, `data/park_f52_blocks_w16.json`
**Gate 5** exact integer and `Fraction` arithmetic; `sympy` used only for symbolic manipulation of exact rationals. No measured value.

**Already-banked check (memo 153).** Terms searched: `non-commutative A-polynomial`,
`quantum A-polynomial`, `5_2`, `erratum`, `recursion`, `colored Jones annihilator`. Nothing
here is a MISSING/OPEN claim; the one open item in §6 is named with exactly what was tried.

---

## 1. What arrived

`fetch/FETCH_REQUEST_CEFF.md` **§B''** has asked since memo 183 for the primary-source quantum
A-polynomial, to say *where* Park's eq (32) went wrong. Two sources arrived:

* **`rec.twist.knot.2.m`** — a Garoufalidis–Sun `twist.knot.data` operator, order 4, inhomogeneous;
* **arXiv:1201.3314v3**, Garoufalidis, *"Quantum knot invariants"* (Arbeitstagung survey), which
  **prints in §4 an order-3 inhomogeneous recursion for the colored Jones of `5₂`** (as the
  `(−2,3,−1)` pretzel knot).

Plus arXiv:2106.03942 (fetch item **B2**, §6 below) and a typed `A_polynomial_5_2.txt`.

**Nothing was taken on a filename or a label.** Every operator is identified the way memo 186
identified the tables: **by what it actually annihilates**, against the colored Jones of five
knots — `3₁, 4₁, 6₁, 9₂` (Garoufalidis–Sun tables, identified by determinant) and **`5₂`,
computed at this bench** by the R-matrix state sum on Park's braid word (memo 185 addendum 3).

## 2. The file is for the wrong knot — the lost minus sign again

| operator | annihilates |
|---|---|
| `rec.twist.knot.2.m` (order 4) | **`6₁ = K_{−2}`**, at `n = 1…6`, direct, no shift — **and nothing else** |
| survey §4 (order 3) | **`5₂`**, at `n = 1…6`, direct, no shift — **and nothing else** |

> The file named `rec.twist.knot.2.m` holds the operator for `K_{−2} = 6₁`. **The same lost
> minus sign memo 186 found in the `CJTwist` filenames.** The `5₂` operator was not in the file.

**But §B'' is closed anyway.** The survey *prints* `5₂`'s recursion, and it is now **verified**
against this bench's own colored Jones at six values of `n`. **The bench holds a verified
non-commutative A-polynomial for `5₂`.**

## 3. CELL 1 — Park's eq (32) as printed annihilates nothing

*(A: it annihilates some knot's colored Jones in some convention → eq (32) is a correct operator
merely mismatched to `F⁺`. B: it does not.)*

**→ B.** Five knots × 2 normalisations × 2 mirrors × 3 shifts = **60 conventions. Nothing.**

Memo 183 established the defect against `F⁺_{m(5₂)}` with an exactly measured remainder. **This
is an independent second witness on a completely different object** — the colored Jones — and it
is now measured against a *verified* comparison operator rather than against nothing.

## 4. T3 — the obvious explanation, tested and refuted

The natural hypothesis, once the file turned out to be `K_{−2}`, is that Park picked up the
wrong twist-knot file. **Tested: no.** The ratio `a_i(6₁ operator) / a_i(eq 32)` is not constant
in `i`. `a₀` and `a₄` do share factors, but that is the generic twist-knot shape, not a match.
**Hypothesis refuted, and recorded as refuted.**

## 5. CELL 2 — the part that is fair to the author

*(A: the consequences Park prints from eq (32) fail too → the error is upstream, in his
computation. B: they hold → the error is confined to the printed operator.)*

On the same page Park prints `f₂` and `f₃` as explicit `ℚ(q)`-combinations of `f₀` and `f₁`.
This bench computed `f₀…f₅` **independently**, from his large-colour Verma R-matrix
(`park_large_color.py`, memo 183 addendum 1).

```
Park's printed f_2  vs  the bench's own block :  MATCH over q^-1 .. q^14  (16 coefficients)
Park's printed f_3  vs  the bench's own block :  MATCH over q^0  .. q^14  (15 coefficients)
```

The horizon is set by `f₀`'s 16 stored coefficients, **not by any disagreement**.

> **→ B. The computation behind the paper was right.** Whatever went wrong, went wrong
> **between his computation and the printed operator.** Memo 183 could only say eq (32) fails;
> it is now known that this is a transcription defect and not a mistake in the mathematics.
> That is stated as plainly here as the negative was.

## 6. T4 — the fourth upload, verified rather than used

`A_polynomial_5_2.txt` is **not a primary-source data file** — it is a typed summary, so it was
verified, not trusted. Taking the `q → 1` limit of the **verified** order-3 operator and removing
the extraneous factor `(m−1)³(m+1)³(m²+1)²` that the classical limit of a non-commutative
A-polynomial always carries:

```
w^3 · A_uploaded(1/w)  ==  the classical limit,  exactly.
```

**The uploaded file is correct**, written with the reciprocal longitude convention `w ↔ 1/w`.
The chain closes: *our own colored Jones → the survey's operator → its classical limit → this file.*

## 7. The named open item, with what was tried

**Converting the verified colored-Jones operator into the `x`-block recursion for `F⁺` does not
work by the naive ansatz.** Tried: `Â = Σ_j a_j(x,q) ŷ^j` with `ŷ : x ↦ qx` and
`F⁺ = Σ_j f_j x^{j+1/2}`, collecting powers of `x`, in **all four** `q`- and `x`-mirror
orientations. Each gives a triangular system determining `f₂…f₅` from `f₀, f₁`, and each
disagrees with the bench's known blocks at the first or second coefficient. **So the `F_K`
annihilator is not literally the colored-Jones annihilator in this convention. Not solved, not
claimed** — written down so the next seat does not repeat it.

**This is memo 183 addendum 4's blocker, still standing**, but now with a verified operator on
the table instead of a defective one.

## 8. arXiv:2106.03942 has arrived, and memo 185 §8 turns out to be the bridge

Fetch item **B2** — the *inverted* Habiro series — is here. Park's **Conjecture 2**:

```
F_K(x,q) = −(x^{1/2} − x^{−1/2}) Σ_{m≥1}  a_{−m}(K) / ∏_{j=0}^{m−1} (x + x^{−1} − q^j − q^{−j})
```

expanded as a power series in `x`, where `a_m(K)` are Habiro's coefficients **in the basis
`∏_j (x + x^{−1} − q^j − q^{−j})`** and `a_{−m}` is their extension to negative index.

Two things are worth recording immediately.

1. **That is exactly the basis memo 185 §8's convention note singled out.** §8 was written
   because reading "all coefficients are 1" into GM's eq (21) basis would have hidden CELL A's
   obstruction. It turns out to be the basis this whole route is built in — `a_m(4₁) = 1` for
   all `m ≥ 0` is Park's own opening example.
2. **Park's own framing matches what memo 185 CELL A measured.** He describes the usual Habiro
   series as a completion at the *finite* place `x + x^{−1} = 2` and the inverted one at the
   *infinite* place `x + x^{−1} = ∞`, "inverting it to make it convergent". CELL A measured that
   convergence failure directly, and addendum 2 measured its *rate* as a function of the twist
   parameter.

**Not tested here.** The nearest cheap test is Conjecture 2 for `4₁`, where `a_{−m} = 1` and
`F_{4₁}` is known — named as **F187-1**.

## 9. Named follow-ups

**F187-1.** Test Park's Conjecture 2 on `4₁` (`a_{−m} = 1`), against the known `F_{4₁}`.
**F187-2.** Get the real `rec.twist.knot.-2.m`…`rec.twist.knot.2.m` set with the signs intact —
though §B'' no longer depends on it, since the survey supplied `5₂`.
**F187-3.** The `F⁺` block recursion (§7). The verified operator is in hand; the conversion is not.

# B8112 — the dictionary entry is an **identity**, and the answer to B8104's question is **"none of them"**

**Date:** 2026-08-21 · **Seat:** cc3, audit · **Lane:** MATHEMATICS. **Gate 5 untouched — no measured
value appears.** Third rung of the owner-elected **finish-the-3d-theory** line.

> **SCOPE.** The complex length spectrum of `m004` and Pfaff, arXiv:1206.0228, Theorem 1.2.
> Establishes an **identification** and computes a **torsion ratio**. It does **not** assemble the
> one-loop partition function: the cusp's continuous spectrum (B739 / B8101) is still not included.

---

## The question B8104 left, and why it had no answer as posed

B8104: *"does the AdS₃ boundary-graviton one-loop determinant correspond to one of Pfaff's `ρ(m)`
torsions, and if so which?"*

**It corresponds to none of them — and the reason is structural, not a near-miss.** The definitions,
**read from the source rather than recalled**:

- `ρ(m)` := the **2m-th symmetric power** of the standard `SL₂(ℂ)` rep on `Sym^{2m}ℂ²`, **dim 2m+1**
- `σ_k` := the rep of `M = SO₂(ℝ)` with highest weight `k e₂` — **one-dimensional**
- `R(s,σ) := ∏_{[γ] prime} det(Id − σ(m_γ)e^{−sℓ(γ)})`, absolutely convergent for **Re(s) > 2**

**Because `σ_k` is one-dimensional, `σ_k(m_γ) = e^{ikθ_γ}`, so**

> ### `R(k,σ_k) = ∏_{[γ] prime}(1 − e^{ikθ_γ}e^{−kℓ_γ}) = ∏_{[γ] prime}(1 − q_γ^k)`, with `q_γ = e^{−ℓ_γ+iθ_γ}` — **exactly the Giombi–Maloney–Yin nome.**

Hence the graviton product is **`Z_geod = ∏_{n≥2}|R(n,σ_n)|^{−2}`** — **an infinite product of
one-dimensional Ruelle zetas**, while every `ρ(m)` torsion is a **finite** object. **No single one
can be it.** What Theorem 1.2 supplies is the **tail**:

```
Z_geod = |R(2,σ_2)|^{-2} · lim_{m→∞} [ (c(m)/c(2))^{κ(X)} · exp(−(1/π)vol(X)(m(m+1)−6))
                                       · T_X(ρ(m))/T_X(ρ(2)) ]^{-2}
```

**Verified, not asserted:** re-summing B8100's own spectrum in the opposite order agrees to
`8.2×10⁻¹⁴` and reproduces its banked `log Z_geod = −0.2729771708384` exactly.

## ⚠ And the identification explains B8100's error bar

`R(s,σ)` converges absolutely for **`Re(s) > 2`**. The graviton product **starts at `n = 2`** — the
**boundary**. So the prediction is that all the cutoff instability lives in one factor. **It does:**

| cutoff | `n = 2` term | `n ≥ 3` tail |
|---|---|---|
| 4.0 | −0.346991558 | +0.080909800 |
| 4.5 | −0.354912150 | +0.080817660 |
| 5.0 | −0.351949899 | +0.080934784 |
| 5.5 | −0.353902280 | +0.080925110 |

**Last cutoff step: `1.95×10⁻³` for `n = 2` against `9.67×10⁻⁶` for the whole `n ≥ 3` tail — 202×.**

> **B8100 reported oscillatory convergence and quoted the last delta as an honest error. This says
> WHY: the `n = 2` mode of the graviton sits exactly at the abscissa of absolute convergence of the
> Ruelle zeta — which is also why Pfaff's theorem starts at `m ≥ 3` and normalises by `ρ(2)`.**
> **The structure of the physics and the structure of the theorem have the same boundary.**

## What that buys: a computed torsion ratio for the figure-eight knot complement

`κ(X) = 1`, `vol(X) = 2.029883212819307`. **`c(m)` recomputed with a script** — B8104 banked its
values with **none** — and the parenthesisation is **declared in the code**, since the source
transcription is ambiguous. It **reproduces B8104's numbers to 10 decimals**, so the two runs
verify each other.

| m | `(c(m)/c(2))^κ` | volume factor | `∏_{k=3}^m |R(k,σ_k)|` | **`T_X(ρ(m))/T_X(ρ(2))`** |
|---|---|---|---|---|
| 3 | 0.7121142418 | 2.071719×10⁻² | 0.968798056 | **1.429269×10⁻²** |
| 4 | 0.5531518273 | 1.178796×10⁻⁴ | 0.954465152 | **6.223622×10⁻⁵** |
| 5 | 0.4522787995 | 1.842144×10⁻⁷ | 0.959468990 | **7.993938×10⁻⁸** |
| 6 | 0.3825504039 | 7.906521×10⁻¹¹ | 0.961191568 | **2.907261×10⁻¹¹** |

**Relative uncertainty `4.8×10⁻⁶`**, from the `k≥3` Ruelle product's cutoff stability — **420× more
stable than the `n=2` term**, which is precisely why the torsion ratio is quotable when the full
one-loop is not.

## ⚠ A control defect found in B8100 — the result stands, the control did not

B8100's *"geodesics come in complex-conjugate pairs"* gate ran on `M.length_spectrum(**2.0**)`
while its headline used cutoff **5.5**. **The control was run on a different data set than the
result.** Below 5.5 there are **four self-conjugate classes at `θ = π`** (`e^{iπ} = e^{−iπ}`) that a
naive pairing test rejects; none appears below 2.0, so **the control passed only in the regime where
it was vacuous.**

**B8100's number is unaffected — it is reproduced here to `10⁻¹³`.** This is a **control defect, not
a result defect**, and it is the *frame-not-instance* refinement of **E2** recurring: a control that
exercises a substitute rather than the instance under test. Filed as an E2 instance.

*(And my own first version of the repaired test failed too: `(θ₁+θ₂) % 2π` returns ≈`2π`, not ≈`0`,
for a sum a hair below `2π`. Fixed to measure distance to the nearest multiple.)*

## What this does NOT establish

- **Not the one-loop partition function.** The cusp's continuous spectrum is still absent; B739's
  scattering determinant (verified in B8101) remains the missing half.
- **Not that analytic torsion *is* the graviton determinant.** Pfaff computes **Ray–Singer analytic
  torsion**. What is identified here is the **Ruelle factors**, exactly and by definition. The
  torsion-to-determinant step is a further identification and is **not** claimed.

## Artifacts

`dictionary.py` · `results.json` · `tests/test_b8112_graviton_torsion_dictionary.py`

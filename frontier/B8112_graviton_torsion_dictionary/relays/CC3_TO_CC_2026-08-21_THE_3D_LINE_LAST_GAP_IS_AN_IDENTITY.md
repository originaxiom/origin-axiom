# cc3 → cc · **The 3d line's last named gap closes — as an identity, and the answer is "none of them"**

Third rung of the owner-elected **finish-the-3d-theory** line. **Gate 5 untouched.**

## The question, and why it had no answer as posed

B8104 left one: *does the AdS₃ boundary-graviton one-loop correspond to one of Pfaff's `ρ(m)`?*

**Definitions read from arXiv:1206.0228 rather than recalled** — `σ_k` is the `SO₂(ℝ)`
highest-weight-`k` representation and is **one-dimensional**. Therefore `σ_k(m_γ) = e^{ikθ_γ}` and

> ### `R(k,σ_k) = ∏_{[γ] prime}(1 − q_γ^k)`, `q_γ = e^{−ℓ_γ+iθ_γ}` — **exactly the GMY nome.**

So the graviton one-loop **is** `∏_{n≥2}|R(n,σ_n)|^{−2}`: an **infinite** product of
one-dimensional Ruelle zetas, where every `ρ(m)` torsion is **finite**. **No single one can be it.**
Theorem 1.2 supplies the **k ≥ 3 tail**.

**Verified, not asserted:** re-summing B8100's own spectrum in the opposite order agrees to
**8.2×10⁻¹⁴** and reproduces its banked `log Z_geod = −0.2729771708384` exactly.

## ⚠ The part I think you'll want: it explains B8100's error bar

`R(s,σ)` converges absolutely for **`Re(s) > 2`**. The graviton product **starts at n = 2** — the
boundary. Last cutoff step: **`1.95×10⁻³`** for the `n=2` term against **`9.67×10⁻⁶`** for the whole
`n ≥ 3` tail. **202×**, and `n=2` is the sign-changing one.

> **B8100 reported oscillatory convergence and quoted the last delta honestly. This says why — and
> it is the same boundary that makes Pfaff start at `m ≥ 3` and normalise by `ρ(2)`.** The physics
> and the theorem have the same abscissa.

## A number you can use

`κ = 1`, `vol = 2.029883212819307`:

| m | **`T_X(ρ(m))/T_X(ρ(2))`** |
|---|---|
| 3 | **1.429269×10⁻²** |
| 4 | **6.223622×10⁻⁵** |
| 5 | **7.993938×10⁻⁸** |
| 6 | **2.907261×10⁻¹¹** |

**Relative uncertainty `4.8×10⁻⁶`** — the `k≥3` product is **420× more cutoff-stable** than `n=2`,
which is exactly why *this* is quotable when the full one-loop is not.

**`c(m)` recomputed with a script**, since **B8104 banked its values with none**; parenthesisation
**declared in the code** because the source transcription is ambiguous. It reproduces B8104 to ten
decimals — the two runs verify each other.

## A control defect in my own B8100 — the result stands, the control did not

Its *"geodesics come in complex-conjugate pairs"* gate ran on `length_spectrum(**2.0**)` while the
headline used cutoff **5.5**. **A control run on a different data set than the result.** Four
self-conjugate `θ = π` classes sit below 5.5 (`e^{iπ} = e^{−iπ}`) and **none** below 2.0 — so it
**passed only in the regime where it was vacuous**.

**B8100's number is unaffected** (reproduced here to `10⁻¹³`). Filed as an **E2 frame-not-instance**
instance, **not a new class**, with the standing rule sharpened: **a control must run on the same
data the headline came from, and a cutoff is part of the data.** *(My own first repair also failed:
`(θ₁+θ₂) % 2π` returns ≈`2π`, not ≈`0`, for a sum a hair below `2π`.)*

## Fences

- **Still NOT the one-loop partition function.** The cusp's continuous spectrum is absent; B739's
  scattering determinant (verified in B8101) remains the missing half.
- **NOT** that analytic torsion **is** the graviton determinant. Pfaff computes **Ray–Singer**
  torsion. What is identified here is the **Ruelle factors**, exactly and by definition; the
  torsion-to-determinant step is a further identification and **is not claimed**.

**Artifacts:** `frontier/B8112_graviton_torsion_dictionary/` — `dictionary.py`, `FINDINGS.md`,
`results.json` · `tests/test_b8112_graviton_torsion_dictionary.py` (7 assertions from
`results.json`). — cc3, audit seat. No merge from this seat.

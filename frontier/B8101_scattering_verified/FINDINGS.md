# B8101 — B739's scattering determinant IS one, verified; `φ(1) = −1`; five of seven ingredients in hand

**Date:** 2026-08-20 · **Seat:** cc3 (audit) · **Verdict: PROVED.** Second rung of the
owner-elected **finish-the-3d-theory** line. Gate 5 untouched.

## What was verified

**B739 banked** `φ_m004(s) = Λ_K(s−1)/Λ_K(s)`. **This checks it is a scattering determinant**, not
merely an identity.

- **`Λ_K(s) = Λ_K(1−s)`** to `<1e-25` — the completion is right (`K = ℚ(√−3)`, `h = 1`, `d_K = −3`,
  `ζ_K = ζ·L(χ₋₃)`).
- **`φ(s)·φ(2−s) = 1`** to `<1e-25`. **This is the load-bearing check.** On `H³` the spectral
  parameter is `s(2−s)` and the critical line is `Re s = 1`, so unitarity reads `φ(s)φ(2−s) = 1` —
  **not** the `φ(s)φ(1−s)` of the 2-dimensional case. B739's formula satisfies the **3-dimensional**
  condition exactly.
- **The continuous integrand `−φ′/φ(1+ir)` is REAL on the critical line**, as unitarity requires,
  and is numerically computable.

## `φ(1) = −1` — and it is the non-trivial sign

At `s = 1`, the centre of the critical line, unitarity forces `φ(1)² = 1`. Computed:
`φ(1+10⁻⁸) = −1.00000002`, so **`φ(1) = −1`**.

**Consequence:** the trace-formula term `(1 − φ(1))` equals **2, not 0**. **The cusp contributes
non-trivially at the symmetric point** — it is not a term that quietly vanishes.

## The assembly — 5 of 7

| status | term | source |
|---|---|---|
| **IN HAND** | identity / volume | `Vol = 2.029883212819307` (B8099, verified) |
| **IN HAND** | geodesic / discrete | `log Z_geod = −0.272977 ± 2.0×10⁻³` (B8100) |
| **IN HAND** | scattering determinant | `Λ_K(s−1)/Λ_K(s)`, unitarity verified here |
| **IN HAND** | symmetric-point term | `φ(1) = −1` ⟹ `(1 − φ(1)) = 2` |
| **IN HAND** | continuous integrand | `−φ′/φ`, computable and real on `Re s = 1` |
| **MISSING** | the test function `h(r)` | the spin-2 / boundary-graviton `h` for a **cusped** quotient |
| **MISSING** | the assembled determinant | needs `h`; **not attempted** |

## What is genuinely missing, named precisely

**The spin-2 test function for a cusped quotient.** GMY's product is derived for handlebodies and
closed quotients; the boundary-graviton `h(r)` appropriate to a **finite-volume cusped** manifold is
the one object none of these rungs supplies. **That is the whole remaining gap — not "quantization"
in the abstract, but one named function.**

## SCOPE

Verifies that B739's object satisfies the conditions a scattering determinant **must** satisfy on
`H³`, computes its symmetric-point value, and shows the continuous integrand is tractable. **Does
not assemble the one-loop determinant** and does not claim a partition function. No measured value.

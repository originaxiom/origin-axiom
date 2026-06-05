# B83 (Phase A) — the SL(n) figure-eight Dehn-filling A-polynomial family `L = (−1)ⁿ⁻¹ Mⁿ`

**Date:** 2026-06-05. **Status:** high-precision-numerical (the SL(4) A-polynomial is new; the family
unifies B67/B71/B73). Standalone low-dim topology; **no Origin-core claim**; proven core P1–P16
untouched. Script: `probe.py`. Test: `tests/test_b83_sln_apolynomial.py`.

## The result

degree=rank is the matrix law `[A,B]=(−1)ⁿ⁻¹μⁿ` on the principal Dehn-filling component (B73/V54,
B77/V60). Its **peripheral eigenvalue shadow is an A-polynomial.** Co-diagonalizing the commuting
meridian `μ=A⁻¹t` and longitude `λ=[A,B]`, each eigenvalue pair `(M,L)=(eig μ, eig λ)` satisfies the
**eigenvalue A-variety**
```
   L = (−1)ⁿ⁻¹ Mⁿ ,     with   ∏ M = det(μ) = 1 .
```
This is the rank-`n` analogue of the figure-eight A-polynomial, unifying the trace-map results into one
family:

| rank `n` | A-variety | source |
|---|---|---|
| 2 | — (no Dehn-filling component) | A0/B73 — SL(2) is degenerate |
| 3 | `L = +M³` | Falbel `W1=D2` (B71); confirmed here, `~1e-10` |
| **4** | **`L = −M⁴`** | **NEW — the SL(4) figure-eight A-polynomial from the trace map**; confirmed here, `~1e-12` |
| 5 | `L = +M⁵` (predicted) | the principal SL(5) component is not numerically locatable (B78) |

So the family is **`Aₙ: L = (−1)ⁿ⁻¹ Mⁿ` on the principal Dehn-filling component, `n≥3`** — the rank-`n`
generalization of B67 (SL(2) Cooper–Long) and B71 (SL(3) Falbel). The **SL(4) member `L=−M⁴` is new**.

## The mechanism (the "why n", as far as this establishes it)

- **The exponent is the rank `n`** — structurally the **Falbel filling slope** of the *principal*
  Dehn-filling component (the principal component is precisely the one whose A-polynomial degree equals
  the rank; SL(4) has a *second* Dehn-filling component, the `{z⁴+1}` one, with `M³=L` — a different
  slope, V54).
- **The sign `(−1)ⁿ⁻¹`** is fixed by the determinant/orientation: it is the scalar `c` in B77's
  `[A,B]=c·μⁿ`, forced to `cⁿ=1` by `det[A,B]=det(μ)ⁿ=1`, with the observed branch `(−1)ⁿ⁻¹`.
- **The meridian eigenvalues `M` are GENERIC** — they vary across the component (`|M|` spread `O(1)`),
  **not** fixed roots of unity (B77). So the A-variety is the 1-parameter curve `L=(−1)ⁿ⁻¹Mⁿ` (per
  eigenvalue), not a finite point set.

The full *derivation* of why the principal component's slope equals the rank is deferred — it lives in
the Falbel / Bergeron–Falbel–Guilloux SL(n)-figure-eight framework (the external novelty check, Phase E).
This stage establishes the **A-polynomial family + the structural identification of the exponent**.

## On `j=1728`

The `j=1728` link (V53) is a property of the **m-family spectral curve** `y²=M⁴−aM²+1` (the metallic
A-polynomial thread, B69/V53), not of the SL(n) Dehn-filling A-variety `L=(−1)ⁿ⁻¹Mⁿ` — the latter is a
genus-0 monomial curve with no elliptic `j`-invariant. So the `j=1728` test B73 flagged is a
**category mismatch**: it belongs to the m-axis (resolved, V53), not the n-axis. Recorded, not pursued.

## Disposition

The SL(4) figure-eight A-polynomial (`L=−M⁴`) is established, and degree=rank is reframed as the
clean **Aₙ family** `L=(−1)ⁿ⁻¹Mⁿ` (n≥3) — the rank generalization of Cooper–Long/Falbel. The mechanism
(exponent = rank = filling slope) is structurally identified; its full derivation is the external-check
item (Phase E).

## Reproduce

```bash
python frontier/B83_sln_apolynomial/probe.py
python -m pytest tests/test_b83_sln_apolynomial.py -q
```

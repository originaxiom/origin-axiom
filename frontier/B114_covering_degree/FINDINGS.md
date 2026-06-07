# B114 — the covering-degree mechanism for degree=rank's exponent: TESTED-NEGATIVE

**Status: `TESTED-NEGATIVE`.** Tests S022's candidate positive mechanism (CC-web Addition 1 A1d): is the
degree=rank exponent `k` the **Weyl-orbit covering degree** of the meridian→longitude map `M ↦ L = c·Mᵏ`? B111
found it `k`-to-1 at the **single-eigenvalue** level (`μ ↦ μᵏ`); this stage tests the **full-spectrum** version
and finds it **does not** equal `k`. NO physics; no `CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

## The result
The **full covering degree** — the number of distinct meridian spectra `{Mᵢ}` with `det = ∏Mᵢ = 1` (SL(n)),
**mod the Weyl group** (permutations), mapping to the same longitude spectrum `{Lᵢ = c·Mᵢᵏ}` — is **`~ k^{n−1}`,
not `k`**:

| component | `n` | `k` | full covering degree | `= k`? |
|---|---|---|---|---|
| SL(3) W1 | 3 | 3 | **9** `= 3² = k^{n−1}` | ✗ |
| SL(4) secondary | 4 | 3 | **27** `= 3³ = k^{n−1}` | ✗ |
| SL(4) principal | 4 | 4 | **40** (`< 4³`, reduced by the repeated eigenvalue `{1,1,ω,ω²}`) | ✗ |

(Each `Lᵢ/c` has `k` `k`-th roots → `kⁿ` combinations; `det=1` fixes one → `~k^{n−1}`; mod permutation adjusts
for repeated eigenvalues.) So `covering degree = k` holds **only for a single eigenvalue**, not the full spectrum.

## Verdict
The **covering-degree-=-`k` mechanism is not supported** (TESTED-NEGATIVE at the full-spectrum level). The
exponent is **not** a covering degree. The live exponent lead stays the **`Mᵏ`-scalar arithmetic** of B111
(ADDITION 1): `k` is constrained to powers where `Mᵏ` is non-scalar *and* compatible with the bundle relations
(the `M⁴=−1` scalar impossibility forces `k=3` on the secondary). `S022`'s covering-degree candidate is
downgraded; the exponent (the power half of `ρ_n`) stays open, with the scalar-arithmetic — not the covering
degree — as the live lead.

```bash
python frontier/B114_covering_degree/probe.py
python -m pytest tests/test_b114_covering_degree.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.

# B192 — SL(n≥3) higher-rank Lyapunov spectra: the parity law makes V29 a measured property

**Date:** 2026-06-22. **Status:** Masterplan III, **Track D** (L20/B166 deepened). **Computed** the *full* Lyapunov
spectrum (all `n` exponents, QR-flag) of the metallic SL(n) transfer cocycle and read its **symmetry**. **Result: a
clean parity law** — the metallic Lyapunov spectrum is **symmetric (symplectic) iff `n` is even**, **asymmetric
(non-Hermitian) iff `n` is odd** — directly realizing V29 ("a symplectic form on `ℝⁿ` exists iff `n` even"), and the
even-`n` symmetry is **special to the metallic cocycle** (a generic SL(n) is asymmetric for all `n`). **Firewall-side:**
emergent non-Hermitian higher-rank spectral math (`K010` boundary), *not* fundamental; no scale/Λ; **nothing to
`../../CLAIMS.md`**; P1–P16 frozen. Ledger V185. Reproducer `sln_higher_rank.py` (`ALL CHECKS PASS`).

## The setup

The metallic SL(n) transfer companion `M_n(E,V)` (det = 1): first row `[E−V, −1, 0,…,0, (−1)^{n−1}]`, subdiagonal
`1`s (generalizes B166's `M3`); Fibonacci ordering of the on-site potential `V ∈ {λ, 0}`. The **full** Lyapunov
spectrum `γ_1 ≥ … ≥ γ_n` is computed by the QR-flag method (accumulating `log|R_{ii}|` for all `i`). B166 looked only
at the *top* exponent (and recorded that SL(2)-style Cantor thinning doesn't transfer); here the *whole spectrum* and
its symmetry are the object.

## The result

| `n` | parity | spectrum | sum | symmetry defect `Σ|γ_i+γ_{n+1−i}|` |
|---|---|---|---|---|
| 2 | even | `[ 0.13, −0.13]` | 0 | **0.000** (symmetric) |
| 3 | odd | `[ 0.25, 0.11, −0.36]` | 0 | **0.222** (asymmetric) |
| 4 | even | `[ 0.29, 0.28, −0.28, −0.29]` | 0 | **0.003** (symmetric) |
| 5 | odd | `[ 0.29, 0.25, −0.06, −0.21, −0.27]` | 0 | **0.114** (asymmetric) |

- **D1 — SL(n) structure.** The spectrum **sums to 0** (det = 1) for `n=3,4,5` — the SL(n) cocycle constraint.
- **D2 — the parity law (V29 made visible), controlled.** The symmetry defect is `~0` for **even** `n` (n=2: 0.000,
  n=4: 0.003 → a `±`-symmetric, symplectic spectrum) and **large** for **odd** `n` (n=3: 0.22, n=5: 0.11 →
  non-Hermitian). **Control:** a generic random SL(n) cocycle is asymmetric for **all** `n` (n=4 defect `≈0.52`),
  so the even-`n` symmetry is **special to the metallic cocycle** — `163×` smaller defect than generic SL(4). The
  metallic even-`n` transfer cocycle is therefore (conjugate to) a **symplectic** one — it *uses* the symplectic
  form V29 guarantees exists for even `n`; the odd-`n` cocycle cannot (no form) and is genuinely non-Hermitian.
- **D3 — bounded set + tower.** A Cantor-like bounded (top-Lyapunov `≈0`) set persists (nonempty, not full), and the
  band-center linearization carries one golden tower scale `±φᵏ` (B107/B60). B166's recorded negative stands:
  SL(2)-style *clean* Cantor thinning still does not trivially transfer at the top-Lyapunov level.
- **D4 — FIREWALL.** Emergent non-Hermitian higher-rank spectral math; the odd-`n` cocycle is genuinely
  non-Hermitian (asymmetric spectrum); the rigorous higher-rank spectral theory (Hausdorff dimension, a horseshoe,
  the spectral-set topology) stays **NEEDS-SPECIALIST** (no ground truth, B166).

## What this means (L20)

B166 established V29 as an *abstract algebra* fact (the symplectic form exists iff `n` even) and a *negative*
(no clean Cantor thinning). B192 turns the algebra fact into a **measured spectral property**: the metallic
transfer cocycle's Lyapunov spectrum is symplectically symmetric *exactly* when `n` is even — and this is
non-trivial (generic SL(n) is asymmetric for all `n`). So the "intrinsically non-Hermitian for odd `n`" statement is
now directly visible as Lyapunov-spectrum asymmetry, the cleanest possible signature. The rigorous spectral theory
remains the genuine specialist boundary.

## Scope / honesty
- The full Lyapunov spectrum + symmetry are robust (QR-flag, averaged over energies, vs a generic-SL(n) control).
- The even-`n` symmetry is established for `n=2,4`; the metallic cocycle being *literally* symplectic (vs merely
  conjugate to one, giving the symmetric spectrum) is the natural specialist follow-up, not claimed here.
- Emergent condensed-matter / dynamical-systems mathematics (`K010` boundary); no physical-magnitude claim; nothing
  to `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`B166_sln_aperiodic` (V29 / the symplectic obstruction + the top-Lyapunov negative this deepens), `B109` (the
center-manifold / band-center link), `B60`/`B61`/`B107` (the SL(n) tower, the golden scale), `docs/OPEN_LEADS.md`
L20. External: the QR-flag / multiplicative ergodic (Oseledets) Lyapunov spectrum; symplectic cocycles ⟹
`±`-symmetric Lyapunov spectra; non-Hermitian aperiodic / higher-rank spectral theory (the specialist residual).

## Reproduction
`python frontier/B192_sln_higher_rank/sln_higher_rank.py` — D1 the full spectrum sums to 0; D2 the parity law +
the generic-SL(n) control; D3 the bounded set + golden tower scale; D4 the firewall/NEEDS-SPECIALIST residual.
Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b192_sln_higher_rank.py` (2 tests, ~0.5s).

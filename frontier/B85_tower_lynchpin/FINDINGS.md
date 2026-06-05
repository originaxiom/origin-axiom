# B85 (Phase C/D) — the all-n tower lynchpin, precisely reduced

**Date:** 2026-06-05. **Status:** STRUCTURAL — a verified new fact (Λ² functoriality), a closed shortcut
(Λ²V doesn't break the degeneracy), and the precise reduction of the deepest open item. Standalone
Lie/invariant theory; **no Origin-core claim**; proven core P1–P16 untouched. Script: `probe.py`. Test:
`tests/test_b85_tower_lynchpin.py`.

## The lynchpin

The metallic tower `char(J(m)) =` the Dickson catalog is **PROVED at `n≤4`** (B80/V62, CRT/F_p) and
**STRUCTURAL at `n=5,6`** (B62 opposition-involution `θ`-split). The only remaining gap is a
**from-first-principles proof at `n≥5`**. This stage reduces that gap to its irreducible form, ruling
out the numerical and representation-theoretic shortcuts (Phase C "build `σ` / `Fix(σ)`" and Phase D
"general-`n` `a_d`" are the same symbolic object; consolidated here).

## What this establishes

**(1) Λ² functoriality of the figure-eight substitution (verified, ~1e-14).**
The substitution `φ: a→a²b, b→ab` is functorial under the exterior square:
```
   Λ²(A²B) = (Λ²A)²(Λ²B) ,     Λ²(AB) = (Λ²A)(Λ²B) .
```
So the even-`k` sector (tied to `e₂=tr(Λ²A)`) is **the same figure-eight trace map carried on the
`Λ²V` representation** — a clean new structural fact (not previously recorded).

**(2) But `Λ²V` does NOT remove the doubly-degenerate `char(M²)²`.**
The `char(M²)` multiplicity (1 at `n=3,4`; **2 at `n=5,6`**) is the dimension of the height-2 root
space's `θ`-symmetric part (B62) — a **root-system fact**, not a representation artifact. `Λ²V`
(dim `C(n,2)`) re-presents the same root system; the multiplicity persists. So the functoriality, though
real, **does not dissolve the degeneracy** that blocks the numerical proof.

## The irreducible reduction (combining B84 + B70 + B62 + (1)–(2))

- **Numerical routes are DEAD** (B84/V67): the ε-series pinv-limit does not converge canonically at the
  `char(M²)²` sector — even gauge-invariant power sums scatter; no gauge-fix / θ-split / averaging helps.
- The gap is **exactly 2 eigenvalues** — the *second* `char(M²)` (B84); 22/24 SL(5) modes are canonical
  (B66).
- That sector is a **rank-1, bounded-bidegree-≤(3,3)** `e₂/Λ²` closure (B70).
- Λ² functoriality (1) identifies it cleanly, but (2) the multiplicity-2 is intrinsic, so the closure
  must be assembled **symbolically**: the fixed-line Jacobian `Dσ` of the *exact* trace map `σ` is
  canonical **by construction** (no pinv, exact even at the degenerate multiplicity) — but building `σ`
  is the **Procesi-trace-ring problem** (the explicit `(n²−1)`-coordinate substitution with the
  `eⱼ` exterior-power dependency; research-scale).
- **B62 already gives the tower structurally**; the residual is *only* the "from first principles"
  symbolic assembly.

## Verdict

The all-`n` tower lynchpin is reduced to **the symbolic assembly of the bounded rank-1 `e₂/Λ²` closure
into `σ`** — a precise, finite, research-scale continuation. **No numerical or representation shortcut
remains** (B84 killed the numerical; this stage killed the Λ²V representation shortcut). This is the
honest scoping of the deepest open item: `n≤4` proved, `n≥5` structural (B62) with the first-principles
gap reduced to one symbolic construction.

## Reproduce

```bash
python frontier/B85_tower_lynchpin/probe.py
python -m pytest tests/test_b85_tower_lynchpin.py -q
```

# B75 — metallic × degree=rank, the two-parameter (m,n) thread (Path F1)

Is the **degree=rank** law (`Mⁿ=L` on the figure-eight bundle's principal Dehn-filling component,
B73/V54) **m-independent** — does it persist across the **metallic family** of once-punctured-torus
bundles (monodromy `φ_m²`, `φ_m: a→aᵐb, b→a`), or is it special to the figure-eight (`m=1`)?

- **`probe.py`** — realizes metallic-`m` bundle reps (`tAt⁻¹=(AᵐB)ᵐA, tBt⁻¹=AᵐB`) at finite-order
  A-spectra and applies the **convention-independent** eigenvalue test `eig[A,B]=eig(t)ᵏ`.
- **`FINDINGS.md`** — the result + the methodological correction (why the eigenvalue test, not B73's
  convention-specific `μ=A⁻¹t`).

**Result (high-precision-numerical).** The **m-axis is real**: at rank `n=3`, the **odd** metallic
bundles `m=1` *and* `m=3` both give the clean `M³=L` (eigenvalue test ~1e-14) — degree=rank persists to
`m=3` (a different hyperbolic manifold, monodromy trace 11), complementing the `n`-axis (V47/V54). So
degree=rank looks like a **rank/topological invariant**, robust under metallic deformation. **Open:**
the **even-`m`** (m=2) Dehn-filling component wasn't located (no clean hit over 61 spectra — consistent
with the cusp-torsion parity `k≡m mod 2`, B69); and the **rank-4 metallic** corner (the `φ_m²` n=4
spectra differ from B73's `{1,1,ω,ω²}`).

```bash
python frontier/B75_metallic_degree_rank/probe.py
python -m pytest tests/test_b75_metallic_degree_rank.py -q
```

No Origin-core claim; proven core P1–P16 untouched.

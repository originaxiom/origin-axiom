# B85 — the all-n tower lynchpin, precisely reduced (Phase C/D)

The metallic tower is PROVED at `n≤4` (B80) and STRUCTURAL at `n=5,6` (B62). This reduces the
remaining from-first-principles gap to its irreducible form.

- **`probe.py`** — verifies Λ² functoriality of the figure-eight substitution and the persistence of
  the `char(M²)²` multiplicity under Λ²V.
- **`FINDINGS.md`** — the verified fact, the closed shortcut, and the precise reduction.

**Result.** (1) **Λ² functoriality** (new, ~1e-14): the figure-eight substitution is functorial under
the exterior square, so the even-k sector is the same trace map on `Λ²V`. (2) **But Λ²V does not break
the degeneracy** — the `char(M²)²` multiplicity-2 at SL(5) is a root-system fact (B62), intrinsic. So
combined with B84 (numerical routes dead) and B70 (the gap is a rank-1, bounded-bidegree-≤(3,3) e₂
closure), the all-n tower lynchpin reduces to **the symbolic assembly of that bounded closure into the
exact trace map σ** (where `Dσ` is canonical by construction) — a finite, research-scale continuation,
with **no numerical or representation shortcut remaining**. B62 gives the tower structurally; the
residual is only the from-first-principles symbolic step.

```bash
python frontier/B85_tower_lynchpin/probe.py
python -m pytest tests/test_b85_tower_lynchpin.py -q
```

No Origin-core claim; proven core P1–P16 untouched.

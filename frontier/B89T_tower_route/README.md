# B89-T — the metallic tower's cohomological route closed; the explicit Sym reduction (Task T)

Task T aimed to prove the tower `char(J(m)) = ∏ char(±Mᵏ)` for **all n** via the cohomological /
root-height route. Honest outcome: that route is **foreclosed**, but the genuine gap (B85's Procesi
assembly) is sharpened to one explicit closed-form + a single module-isomorphism.

- **`probe.py`** — (1) shows the cohomological route fails: the `H¹(F₂; ad ρ)` action at the
  (trivial-rep) fixed line is `char(M)^{n²−1} ≠ tower`; (2) the explicit two-sequence Sym product
  `∏_{d=2}^n char(Sym^d M_m)·∏_{d=0}^{n-3} char(Sym^d M_m)` equals the proved (n≤4) / structural (n=5)
  tower **symbolically in m**; (3) the n=6 discriminator `a₃=2`.
- **`FINDINGS.md`** — the route-closure, the Sym reduction (T)/(M), the n=6 row, and honest labels.

**Result.** The cohomological route is a third dead shortcut (after B84 numerics, B85 `Λ²V`). The all-n
tower reduces to one **module-isomorphism** `J(m) ≅ M_m on [⊕_{d=2}^n Sym^d]⊕[⊕_{d=0}^{n-3} Sym^d]` —
**PROVED n≤4**, structural n=5; the derivation (the Procesi structure) is the lone open item. The Sym/θ
constructions both predict `a₃(n=6)=2`, overruling B66's gauge-corrupted pinv.

```bash
python frontier/B89T_tower_route/probe.py
python -m pytest tests/test_b89t_tower_route.py -q
```
No Origin-core claim; proven core P1–P16 untouched.

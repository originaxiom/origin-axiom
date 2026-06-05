# B94 — tower universality: catalog universal, parity det=−1-specific (Paper 0, G1)

The decisive G1 gate: does the metallic trace-map tower survive outside the metallic slice?

- **`probe.py`** — squares the **proved** metallic Jacobian (`J(φ²)=J(φ)²`, `M_m²` is det=+1, non-metallic)
  at SL(3) and SL(4); shows `char(J²)` factors **exactly** over the catalog `char(Nᵏ)` (universal) but with
  **no** sign sectors `char(−Nᵏ)` and **no** `(t+1)` (parity det=−1-specific). Plus the G3 note: degree=rank
  is det-agnostic (figure-eight is det=+1, B89).
- **`FINDINGS.md`** — the result, the conclusion, the honest scope.

**Result (`computer-assisted`, exact n=3,4).** **Universal catalog, det=−1 parity.** The Dickson catalog
`∏char(Nᵏ)` survives for any `GL(2,ℤ)` monodromy (Cayley–Hamilton); the parity/sign structure
`char(−Nᵏ)` is det=−1-specific — so `det=−1` (B92) is *structurally distinguished*, not just simplest.
And the tower (parity det=−1-specific) and degree=rank (det-agnostic) answer "universal?" differently:
**two problems**.

```bash
python frontier/B94_tower_universality/probe.py
python -m pytest tests/test_b94_tower_universality.py -q
```
No Origin-core claim; proven core P1–P16 untouched.

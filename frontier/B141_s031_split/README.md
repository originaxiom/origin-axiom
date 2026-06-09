# B141 — split S031: φ-fixed tower REDUCIBLE (Q₈), φ²-geometric tower IRREDUCIBLE (dense fig-8)

Third reconciliation pass on S031, one layer past B140; a substantive correction to B140's reframe. The root of the
φ-vs-φ² distinction is **finiteness vs density of the SL(2) image.** MATH tier; firewalled; B129 preserved.

- **Item 1 (RIGOROUS, all n).** The unique irreducible SL(2) φ-fixed point `(0,0,0)` is the **quaternion group Q₈**
  (`A²=B²=−I`, `AB=−BA`, order 8), finite with max irrep dim 2. So its principal `Sym^{n−1}` (dim n) is **reducible
  for all n≥3** (alg-dim table `{2:4, 3:3, 4:4, 5:4, 6:4, 7:4}`; `χ_{Sym²}=(3,3,−1,−1,−1)=χ_a+χ_b+χ_c`). **No
  irreducible principal φ-fixed point exists at n≥3** — corrects B140's "rigidity of the principal *irreducible*
  fixed point."
- **Item 2 (RIGOROUS, all n).** The φ²-geometric fig-8 holonomy (B129's S1a) is **Zariski-dense**, so `Sym^{n−1}` is
  **irreducible ∀n** (alg dim n², n=2..5), traces in ℚ(√−3).
- **Item 3 (SOLID).** Finite image (Q₈) → reducible tower; dense image (fig-8) → irreducible tower. S031 conflated
  the two objects (irreducibility+ℚ(√−3) from φ², "fixed point" from φ).
- **Item 4 (CONJECTURE, open n≥4).** The SL(3) φ-fixed locus appears **entirely reducible** (intertwiner search:
  60/60 reducible, 0 irreducible). Rigorous path = symbolic elimination (the SL(4) route).

**The split:** **S031a** (φ-fixed) = reducible (reducible × discrete); **S031b** (φ²-geometric) = irreducible in
ℚ(√−3) (B129 S1a, HMP-adjacent). **B129's 0-escape conclusion stands.**

```
python frontier/B141_s031_split/probe.py
python -m pytest tests/test_b141_s031_split.py -q
```

**Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B140 untouched. See `FINDINGS.md`; ledger **V130**.

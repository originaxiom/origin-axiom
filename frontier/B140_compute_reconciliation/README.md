# B140 — compute-session reconciliation (subtractive: close / retract / tighten / record)

A Chat-2 compute session reconciled against the repo. **No new frontier claim** — close one open lead, retract one
(never-banked) over-claim, tighten two framings, record two facts. MATH tier; firewalled.

- **Item 1 — B139-G CLOSED (genus-general).** The chirality firewall has no genus gap: the mirror = orientation-
  reversal theorem (vol invariant, CS flipped, trace field conjugate-isomorphic) is **genus-independent**. The
  genus-1 `M→Mᵀ` is a genus-1 *mechanism*; the conclusion is general. Verified genus-1 bundles + knots; genus-2 CS
  numeric is theorem-backed (twister/Sage absent in-sandbox).
- **Items 2–3 — reframe S031 (rigidity) + sharpen B138 (φ vs φ²).** `N=[[m,1],[1,0]]` has `det=−1` and `N²=RᵐLᵐ`,
  so `φ_m` (det −1) has **discrete** fixed points (S031's object) while `φ_m²` (the bundle) has a **positive-dim**
  fixed locus (B71). The unique irreducible φ-fixed point is the **rational** `Sym²(0,0,0)` (SL(3): `(−1,−1,−1)`,
  commutator 3) — so "sealed in `K_m`" is loose (`K_m` is the `φ²`-bundle field; φ-fixed content is **ℚ**). B129's
  0-escape conclusion **stands** (ℚ ⊂ ℚ(√−3)). S031 reframed as **rigidity/uniqueness**; the "non-principal /
  HMP-route" over-claim **retracted** (no non-principal irreducible φ-fixed points).
- **Item 4 — record:** `[[m,1],[1,0]]² = RᵐLᵐ`; `(m,m)` cyclic palindrome ⟹ every metallic bundle amphichiral (B134).
- **Item 5 — record (≠ S031):** the `φ²`-geometric bundles' trace fields m=1→ℚ(√−3), m=2→ℚ(i), m≥3→higher-degree
  (structural; banked B125/B129) — the `φ²`-bundle object, distinct from S031's φ-fixed points.

```
python frontier/B140_compute_reconciliation/probe.py
python -m pytest tests/test_b140_compute_reconciliation.py -q
```

**Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B139 untouched; B129's conclusion stands. See `FINDINGS.md`;
ledger **V129**.

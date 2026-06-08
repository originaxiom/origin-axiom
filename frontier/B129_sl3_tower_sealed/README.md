# B129 — the SL(3) tower is sealed in ℚ(√−3): the firewall from inside the tower

The arc after B128 (verify-don't-trust, in-sandbox). **Does climbing the SL(n) tower produce new content, or is it the
single SL(2) Fibonacci datum in larger irreps?** The latter — the **sixth** firewall direction, the first from inside
the tower.

`probe.py` verifies:
- **S1a (EXACT, sympy)** — the principal `Sym²` metallic SL(3) rep is **irreducible** (generated algebra = `M₃`, dim 9)
  yet **every trace lies in ℚ(√−3)** (`trA=trB=3`, `trAB=½−(3√3/2)i`, `trA⁻¹B=9/2+(5√3/2)i`, `tr[A,B]=½+(3√3/2)i`).
  SL(2) arithmetic in SL(3) clothing.
- **S1b (scipy)** — off-sublocus root-find `tcoords(A,B)=tcoords(AB,A)` over the 4-dim SL(3) bulk: a 15-seed scan gives
  427 converged fixed points, **max distance-to-ℚ(√−3) = 1.2e-6**, 0 beyond 1e-5 → **0 escapes** (the genuine content
  is the `Sym²` image). Uses the **polished distance** escape test (method bug B2 fix).
- **S2 (SnapPy)** — silver bundle `b++RRLL` degree-2 covers reach `(cusps, free_rank)=(2,2)`: rank grows by covering,
  by **replication** (the covers correction).

```
python frontier/B129_sl3_tower_sealed/probe.py
python -m pytest tests/test_b129_sl3_tower_sealed.py -q
```

S1a + detector regressions always run; S1b (scipy) and S2 (SnapPy) skip when the tool is absent.

**Corrected firewall statement:** the metallic family produces **abelian × discrete**, never an irreducible **simple
non-abelian** factor — *not* "rank is always 1" (rank grows by covering, but only by replication). **Two method bugs**
banked (`inQ3` rejects rationals; finite/central masquerade at the residual floor) → `REPRODUCIBILITY.md` SCAN.

**Tier.** MATH + a firewalled physics reading (POSTULATED). Naming `knowledge/K012`; `S029` strengthened; `P007` sixth
direction; capstone `S031` (open MATH, not a bridge). Nothing to `CLAIMS.md`; P1–P16, B85, B124–B128 untouched. See
`FINDINGS.md`; ledger **V118**.

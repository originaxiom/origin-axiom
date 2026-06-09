# B142 — (A) Klein-4 rigorous principal stratum; (B) magic-manifold cartography + MB10; (C) inventory

Three independent, subtractive items. MATH tier; firewalled. (Sage-gated parts run under `sage-python`.)

- **Item A (RIGOROUS).** The principal φ-fixed stratum of S031a is reducible by a one-line proof: eigenvalues
  `{1,−1,−1}` ⟹ `A²=I`; `A~B~AB` ⟹ `B,AB` involutions; two involutions with involution product **commute**
  (`(AB)²=I ⟹ BAB=A ⟹ BA=AB`) ⟹ Klein-4 ⟹ reducible. Upgrades B141 Item-4's principal case from conjecture;
  reconfirmed 78/78 numerically. Full SL(3) locus stays CONJECTURE.
- **Item B (CARTOGRAPHY).** The "Borromean/SU(3) enhancement" claim fails: (1) `s776` = the **magic manifold**
  (ℚ(√−7), 3-chain link, **not** Brunnian), **not** the Borromean rings (`L6a4`, ℚ(i)) — `is_isometric_to` False;
  (2) SL(2,ℂ) dim = #cusps = **3** (Thurston, generic — MB8 null control across sym 8/12/48), and SL(2,ℂ) dim ≠
  rank(SU(3)) — SU(3) is **SL(3,ℂ)** CS (s776's SL(3,ℂ) Ptolemy: 14 obstruction classes, dim 6); (3) trace field
  not ℚ(√−3) ⟹ **outside the forced chain**. Banked: tombstone **K-I** + guard **MB10** (structure ≠ gauge,
  dimensional form). Firewall-confirming, NOT a result, NOT a crossing.
- **Item C.** Open-threads inventory → `docs/OPEN_LEADS.md`.

```
python -m pytest tests/test_b142_klein4_and_magic_cartography.py -q     # 5 passed, 1 skipped (sage)
~/.local/bin/sage-python frontier/B142_klein4_and_magic_cartography/probe.py
```

**Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B141 untouched. See `FINDINGS.md`; ledger **V131**.

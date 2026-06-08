# B128 — symmetry-breaking landscape: chirality recursion, the order parameter, the torsion firewall

The arc after B127/K010 (verify-don't-trust, in-sandbox, on validated controls). **The metallic structure permits
symmetry breaking but never forces it**; a clean new MATH theorem (the chirality recursion) and the correct order
parameter survive; the torsion→gauge bridge is tombstoned.

`probe.py` verifies:
- **the method bug** — naive `is_isometric_to(mirror)` false-positives on chiral m015/m016/m009; the correct test is
  `symmetry_group().is_amphicheiral()` gated on `is_full_group()` (controls: m004/m003 amphichiral, m015/m016/m009
  chiral).
- **M-A** the chirality recursion: `W=R^{m₁}L^{m₁}…R^{m_k}L^{m_k}` achiral ⟺ the block-sequence `(m₁…m_k)` reversal is
  a cyclic rotation (**15/15** across `k≤4`; combinatorial rule + live SnapPy).
- **M-B** the order parameter is the **ordering**, not the count (balanced `#R=#L=6` triples that are chiral).
- **M-C** the exact `Z₂` mirror: block-reversal negates CS to machine zero.
- **K-F** torsion tracks **periodicity**, not chirality (single torsion in both achiral `RRLLRRRLLL` and chiral
  (1,2,3); doubling = the periodic case) — plus center≠gauge (`S029`/`S030`).

```
python frontier/B128_symmetry_breaking_chirality/probe.py
python -m pytest tests/test_b128_symmetry_breaking_chirality.py -q
```

The live SnapPy recomputations **skip** when SnapPy is absent (the pure-combinatorics facts + records always run).

**Tier.** MATH (low-dim topology) + a firewalled physics *sharpening* (permits-not-forces = the fifth firewall
direction; existence inevitable / specific physics contingent). `K-F` tombstoned; the recursion theorem is
`knowledge/K011`; the method bug is a `REPRODUCIBILITY.md` SCAN note; `P007`/`P008` sharpened. Nothing to `CLAIMS.md`;
P1–P16, B85, B127/K010/P008/S030 untouched. See `FINDINGS.md`; ledger **V117**.

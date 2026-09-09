# Addendum (2026-09-02) — three narrowings from codex R036, each recomputed (B1235)

1. **"Global minimum" → box minimum.** `audit.py`'s `origin_is_global_min` checks K(0) = −4 and Hessian 2I — local.
   K(10,10,10) = −704. On the SU(2) trace box [−2, 2]³ the origin IS the unique minimum:
   a² + b² + c² − abc = (a − b)² + c² + ab(2 − c), every term ≥ 0 on the box, equality only at the origin; the critical
   locus is the origin and the four points (±2, ±2, ±2) with sign product +1. Checked symbolically and on 20 000 box
   points: `frontier/B1235_two_seat_harvest/verification/markoff_box_minimum.py`.
2. **"Arithmetic cannot emit a continuum" is not a principle** — x² + y² = 1 has a real continuum. What the arc had
   was an inventory: no continuum among the corpus's emitted values. The slogan is withdrawn where it appears
   (CAMPAIGN_STATUS, CHANGELOG, PROGRESS_LOG, the relay); the inventory stands.
3. **"Every checkable claim recomputed here"** was fourteen booleans. Scope stated.

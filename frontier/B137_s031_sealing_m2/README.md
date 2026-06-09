# B137 — S031 sealing extended to m=2 (silver, SL(3), ℚ(i)) + the reducible-filter (MB7)

A "push further" increment on **S031** (the SL(n) sealing capstone). B129 verified the SL(3) sealing for m=1
(figure-eight, ℚ(√−3)) and left m≥2 undone. This closes m=2 (silver, ℚ(i)).

**Result.** The SL(3) tower is sealed in `K_m` for both arithmetic metallic members: **m=1 in ℚ(√−3)** (reproduces
B129) and **m=2 in ℚ(i)** (new) — among **irreducible** off-sublocus fixed points, **0 escapes** from the SL(2) trace
field (2 seeds each). Strengthens S031 to {m=1, m=2}; theorem-version (all m,n) stays open.

**Method note (MB7).** A naive search counts reducible degenerate points (algebra dim < 9) as "escapes" — their `κ`
isn't constrained to `K_m`. At m=2 these faked ~15–20 escapes (all reducible, `trA=−1`, well-converged), nearly reading
as "S031 false for m=2." Guard: count escapes only among **irreducible** (algdim=9) fixed points; then m=2 seals.
Sibling of K-G/K-H/MB2.

```
python frontier/B137_s031_sealing_m2/probe.py
python -m pytest tests/test_b137_s031_sealing_m2.py -q
```

scipy-guarded. **Tier.** MATH. Computational evidence (not a proof); m≥3 (non-quadratic `K_m`) and SL(n≥4) are future
work. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B136 untouched. See `FINDINGS.md`; ledger **V126**. Method note **MB7**
→ `REPRODUCIBILITY.md`.

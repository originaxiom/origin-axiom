# B153 — rank-stratified degeneration of degree=rank (figure-eight SL(n))

**Question.** Is the figure-eight degree=rank relation `L=(−1)^{n-1}Mⁿ` a genuine A-polynomial component,
and how does it behave across rank?

**Answer (STRUCTURAL; V142).** It is rank-stratified: a genuine **component at n=3** (`L=+M³`, Falbel),
a measure-zero **slice at n=4** (`L=−M⁴`, exact over ℚ(ω)), and **absent at n=5** (semisimple provably
reducible; non-ss numerically absent). This replaces the deflated PC13 "SL(4) component" claim. No physics;
nothing to `CLAIMS.md`.

**Toolkit (`sln_toolkit.py`, self-tested).** Reusable substrate built during the campaign: the bundle
relation, irreducibility (Burnside), peripheral/relation extraction, the **exact** deformation-theory
tangent (slice-vs-component + spectrum-mover), and branch-aware construction. Seals the bug classes
(finite-difference, sqrt-branch, near-singular `t⁻¹`) that cost the earlier probes.

**Method note.** Random Newton drifts to the vacuous (`det t=0`) stratum; cures: Sage/Singular
decomposition of the `det t`-saturated ideal, or adding `det t=1` to the Newton system. Both validated.

```bash
python frontier/B153_degree_rank_degeneration/probe.py
python -m pytest tests/test_b153_degree_rank_degeneration.py -q
```

Files: `sln_toolkit.py`, `probe.py`, `FINDINGS.md`. Campaign log + Sage scripts: `audit/` (working).

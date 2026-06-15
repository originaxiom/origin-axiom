# B153 — rank-stratified degeneration of degree=rank (figure-eight SL(n))

**Question.** Is the figure-eight degree=rank relation `L=(−1)^{n-1}Mⁿ` a genuine A-polynomial component,
and how does it behave across rank?

**Answer (STRUCTURAL; V142, n=5 corrected V143).** It is rank-stratified: a genuine **component at n=3**
(`L=+M³`, Falbel), a measure-zero **slice at n=4** (`L=−M⁴`, exact over ℚ(ω)), and **not realized on any
irreducible rep at n=5** (semisimple provably reducible; non-ss irreducibles *exist* — corrected — but
degree=rank fails on them). This replaces the deflated PC13 "SL(4) component" claim. No physics; nothing
to `CLAIMS.md`.

> **n=5 correction (2026-06-15, self-audit).** The first cut claimed "n=5 absent: non-ss 0/120, no
> irreducible reps." That was a `det t=0`-drift artifact; with `det t=1` pinned, irreducible SL(5) reps with
> the principal spectrum **do exist** (non-ss). The headline is unchanged (degree=rank still not realized on
> an irreducible rep) but the reason is corrected. Reproduce: `python n5_nonss_irreducible.py`.

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

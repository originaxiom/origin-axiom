# B105 — the n=5 wall (characterized), the unified wall, and the ρ_n convergence

Executes the CC-web "n=5 Resolution + Literature + Final Observations" handoff. No physics (physical readings
POSTULATED + quarantined).

- **`probe.py`**
  - **N5 (decisive):** is the SL(5) tower degeneracy a coordinate artifact or a structural change?
    **Coordinate artifact** — the eps-series resolves **21/24** Dickson factors; the resolved 21 are
    **universally catalog-consistent**, the corrupted 3-dim factor is **gauge noise** (varies across seeds),
    and the eps-series ceiling is 21/24. The strict "all 3" bar is **not met**; the obstruction is the
    gauge-degeneracy at the cusp's repeated `−1`. Three structural routes agree the missing piece is `Sym²`.
  - **H6 (unified wall):** the forced cusp spectra `{1,i,−i}`/`{1,1,ω,ω²}`/`{1,1,1,−1,−1}` — the
    **non-trivial eigenvalues collide first at n=5** (`−1`, mult 2); n≥6 has no finite-order spectrum. One
    collision is the common root cause of the tower / degree=rank / eps-series walls → **natural boundary at
    n=4**, proved.
  - **convergence:** the project converges on one object **`ρ_n`** (the `GL(2,ℤ)`-rep on the SL(n) trace
    ring); the tower **is** `char(ρ_n)`, fully characterized n=3,4, boundary at n=4 proved.
- **`FINDINGS.md`** — the N5 verdict, the unified wall, the convergence thesis, the L1/L4 literature (cited),
  and the H1–H6 observations + C1–C4 corrections (each by proof status).

**Result.** The n=5 degeneracy is a **characterized coordinate artifact, not a structural change** (the n=5
catalog is strongly supported, formally open, obstruction pinned). The project is **complete at n=4** with a
**proved boundary**, and converges on one fully-characterized object. Cite B61/B62/B84/B89-T/B95/B103/B104;
GKLP arXiv:1305.0937; Bonahon–Dreyer 1209.3526; Douglas–Sun 2011.01768.

```bash
python frontier/B105_n5_wall_and_convergence/probe.py
python -m pytest tests/test_b105_n5_wall_and_convergence.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.

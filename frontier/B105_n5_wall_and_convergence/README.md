# B105 — the n=5 wall (characterized), the unified wall, and the ρ_n convergence

Executes the CC-web "n=5 Resolution + Literature + Final Observations" handoff. No physics (physical readings
POSTULATED + quarantined).

> **⚠ V90 audit (Corrections A & B, explicit downgrades).** Two prior inferences are withdrawn: (A) the
> seed-variation does **not** imply "coordinate artifact, not structural change" — it is the eps-series
> rank-deficiency signature (B84), uninformative about the truth there (Appendix A); a structural deviation
> at the unresolved sector is neither ruled in nor out. (B) there is **no proved "natural boundary at n=4"** —
> `char(J(n))=catalog` is a class function for **all `n`** (B103); n=4 is a *methodological ceiling*, not a
> theorem. The 21/24 computation and the `ρ_n` thesis are unchanged.

- **`probe.py`**
  - **N5:** the eps-series resolves **21/24** Dickson factors; the resolved 21 are **universally
    catalog-consistent** (across seeds and monodromies) — the genuine evidence. The 3 unresolved are
    supported as `Sym²` by **structural routes** (B62/B89-T/B103), *not* by the seed-variation (Correction A).
    The strict "all 3" bar is **not met** → the explicit n=5 catalog is **OPEN**.
  - **H6 (structural observation):** the forced cusp spectra `{1,i,−i}`/`{1,1,ω,ω²}`/`{1,1,1,−1,−1}` — the
    non-trivial eigenvalues collide first at n=5 (`−1`, mult 2); n≥6 has no finite-order spectrum. A
    **candidate** common root cause of the tower / degree=rank / eps-series walls (not a proof; Correction B).
  - **convergence + open frontier:** the project converges on one object **`ρ_n`** (the `GL(2,ℤ)`-rep on the
    SL(n) trace ring), fully characterized n=3,4, explicit n≥5 OPEN. **The live target:** prove
    `char(ρ_n)=catalog` directly from `ρ_n` (B103) + B62's multiplicities — around the σ-construction.
- **`FINDINGS.md`** — the corrections banner, the N5 result, the unified wall, the convergence + open
  frontier, the L1/L4 literature (cited), and H1–H6 / C1–C4 (each by proof status).

**Result.** The 21/24 resolution is universally catalog-consistent (strong evidence on the resolved sector);
the explicit **n≥5 catalog is OPEN**, walled from two methods (eps-series + trace-ring non-closure), with a
structural deviation at the unresolved sector neither ruled in nor out. **The structure holds for all `n`**
(B103); the project converges on one fully-characterized object `ρ_n` (exact/constructive at n=3,4). Cite
B61/B62/B84/B89-T/B95/B103/B104; GKLP arXiv:1305.0937; Bonahon–Dreyer 1209.3526; Douglas–Sun 2011.01768.

```bash
python frontier/B105_n5_wall_and_convergence/probe.py
python -m pytest tests/test_b105_n5_wall_and_convergence.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.

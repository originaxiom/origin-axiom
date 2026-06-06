# B100 — literature cross-checks of the SL(3) slice + the twisted-Alexander bridge (Probes 2 + 6)

**Status: `computer-assisted`.** Two independent, **published** frameworks are run against the
B71/B98/B99 SL(3) figure-eight results. Nothing here is our discovery; the methods are **cited**. No
physics claim; no Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b100_literature_crosscheck.py`.

## Probe 2 — the Ptolemy variety (Zickert; Garoufalidis–Goerner–Zickert)
SnapPy's boundary-unipotent SL(3,ℂ) **Ptolemy variety** for the figure-eight `4_1` at `N=3`:

| object | value |
|---|---|
| obstruction classes (`H²(M,∂M; ℤ/3)`) | **2** |
| boundary-unipotent SL(3,ℂ) reps in the trivial class (sympy.solve, 8 coords) | **6** |

This is the **0-dimensional boundary-unipotent slice** of B71's 2-dimensional SL(3) character-variety
components (V0/W1/W2) — a complementary cut through the **same object**, containing the geometric rep.
It cross-validates B71 from an **independent code path** (SnapPy Ptolemy, not our trace-map ideal).
*(The non-trivial obstruction class carries a `1+u+u²=0` cocycle root and is left to SnapPy/Magma's exact
solver; only the stable trivial-class count is banked.)* — Zickert arXiv:1405.0025; GGZ arXiv:1207.6711.

## Probe 6 — character-variety genus + twisted Alexander (Baker–Petersen)
Baker–Petersen (arXiv:1211.4479) computed canonical-component **genera** *and* **twisted Alexander
polynomials** for once-punctured-torus bundles with tunnel number one (the figure-eight is the first;
see also the unbounded-genus family arXiv:2206.14954). The decisive, clean cross-validation is the
**twisted Alexander**, which is exactly the **B98/B99 geometric-rep Jacobian**:

```
   transverse char-factor at the geometric rep  =  t² − 5t + 1     (adjoint torsion τ₁ = −3)
```
recomputed here by reusing the locked B98 probe. The **genus figures are different curves** and must not
be conflated:
- canonical component in **trace** coordinates `{y=z=x/(x−1)}` is rational → **genus 0** (B67/B71);
- the **A-polynomial spectral curve** `w²=disc_L` → **genus 3** (B69/B87).

## Verdict
Two independent published frameworks **agree** with the B71/B98/B99 SL(3) picture: the Ptolemy slice
reproduces the boundary-unipotent reps of the same character variety, and the twisted Alexander **is** our
geometric-rep Jacobian. Methods **cited**, not claimed.

## Scope (honest)
SnapPy Ptolemy at `N=3` for one manifold; the trivial-class count via `sympy.solve` (deterministic, =6);
the twisted-Alexander anchor is a reuse of the locked B98 result; the genus figures are **cited /
prior-banked** (B69/B87 + Baker–Petersen), **not** recomputed here. The connections to Zickert / GGZ /
Baker–Petersen are **citations** — the agreement is *consistent with* the published results, not a new
claim.

```bash
python frontier/B100_literature_crosscheck/probe.py
python -m pytest tests/test_b100_literature_crosscheck.py -q
```
No physics claim; proven core P1–P16 untouched; outreach dormant.

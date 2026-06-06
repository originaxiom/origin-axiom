# B98 — the trace-map Jacobian at the GEOMETRIC representation (Probe 1)

**Status: `computer-assisted` (exact, SL(2)).** Neutral low-dim-topology / Lie theory; **no physics
claim** — the 3d-3d correspondence is **cited** from the literature, not claimed. No Origin-core claim;
proven core P1–P16 untouched. Script `probe.py`; test `tests/test_b98_geometric_jacobian.py`.

## The question (the handoff's #1 priority)
The metallic tower `char(J(m))` = the Dickson catalog is computed at the **trivial fixed line** of the
trace map (all traces = n), where Task T (B89-T) degenerated. The **geometric representation** (the
complete-hyperbolic holonomy) is a *different* fixed point — and the one where the published bridges live:
the **3d-3d correspondence** (Dimofte–Gaiotto–Gukov, arXiv:1108.4389/1112.5179; Terashima–Yamazaki
arXiv:1103.5748; Gang–Koh–Lee–Park arXiv:1305.0937) and **Daly** (arXiv:2411.04431, 2024 — the monodromy
action on the geometric tangent space is the cohomological / twisted-Alexander object). We had never
computed the Jacobian spectrum there.

## The result (figure-eight, SL(2), exact)
The figure-eight trace map is `T₁²` with `T₁(x,y,z)=(z,x,xz−y)` on `(x,y,z)=(tr A,tr B,tr AB)`. On the
geometric component `V0={y=z=x/(x−1)}`,
```
   char(D T₁²)|_{V0} = (t−1)·( t² − c(x) t + 1 ),     c(x) = (2x²−x+1)/(x−1).
```
The **geometric** fixed point has a parabolic puncture (`tr[A,B]=−2`), i.e. on V0: `x²−3x+3=0`, so
```
   x_geom = (3 ± √−3)/2  ∈  ℚ(√−3)   — exactly the figure-eight trace field,
```
where `c(x_geom)=5` and
```
   char(D T₁²)|_geom = (t−1)( t² − 5 t + 1 ).
```
The transverse pair `{μ,1/μ}` (`μ+1/μ=5`) gives the **adjoint Reidemeister torsion**
`τ=(1−μ)(1−1/μ)=2−c=−3`, equal to the figure-eight torsion `τ₁=−3` (`cs_invariant_family`; Porti) — the
object Daly identifies with the geometric tangent-space monodromy action.

## Verdict (decisive)
**The Dickson tower does NOT appear at the geometric rep — it is a trivial-rep phenomenon.** At the
geometric rep the same monodromy's Jacobian gives `t²−5t+1` = the **adjoint-torsion / twisted-Alexander**
object (consistent with Daly arXiv:2411.04431; reproduces `τ₁=−3`). The two fixed points of the trace map
carry **different invariants**: trivial → the Dickson tower; geometric → the torsion. This also explains
why Task T degenerated at the trivial rep — the cohomological/torsion content lives at the **geometric**
rep, exactly as the published framework predicts.

## Probe 5b (a deflation check, negative)
Is the tower the **Kostant principal-sl(2) branching** of `sl(n)`? **No.** Kostant's
`sl(n)=⊕_{k=1}^{n−1} V_{2k}` is even-power `Sym^{2k}` only; the tower's two-sequence
`[Sym²..Sym^n]×[Sym⁰..Sym^{n−3}]` uses consecutive intervals of *both* parities — a different object. So
the tower is **not** "just a known decomposition" (consistent with the V27 even-only kill).

## Scope (honest)
Exact at SL(2). The connection to Daly / the 3d-3d framework is a **citation**, and the match (the
geometric-rep Jacobian reproduces the adjoint torsion `−3`) is *consistent with* the published results,
**not** a new claim of ours. **Open next** (Probe 1c): the SL(3) geometric Jacobian (at `Sym²` of the
geometric rep, on V0) — does it likewise give the SL(3) torsion rather than the tower?

```bash
python frontier/B98_geometric_jacobian/probe.py
python -m pytest tests/test_b98_geometric_jacobian.py -q
```
No physics claim; proven core P1–P16 untouched; outreach dormant.

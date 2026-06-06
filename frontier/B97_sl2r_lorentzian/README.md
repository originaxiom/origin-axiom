# B97 — where Lorentzian structure lives: the SL(2,ℝ)/Teichmüller component

The honest follow-up to B96: B96 found the geometric (SL(2,ℂ)) side is Euclidean `(0,2)`; B97 checks the
real (SL(2,ℝ)/Teichmüller) side, the phase space of 2+1 gravity.

- **`probe.py`** — (1) the gauge-algebra trace-form signatures: `sl(2,ℝ)=so(2,1)→(2,1)` **Lorentzian**
  (2+1 Minkowski), `su(2)=so(3)→(0,3)` Euclidean; (2) an explicit **SL(2,ℝ) Fuchsian** fiber rep
  (`tr[X,Y]=−2`); (3) the holonomy preserves the `(2,1)` form (**SO(2,1) local Lorentz invariance**).
- **`FINDINGS.md`** — the result + the honest deflation.

**Result (`computer-assisted`).** Lorentzian structure **is** present — as the `so(2,1)=sl(2,ℝ)` gauge
algebra on the real/Teichmüller component (the 2+1-gravity phase space) — but it is **structural** (the
gauge group is the Lorentz group), present by construction, **not emergent**. B96 + B97 locate the
Lorentzian form precisely (real side, not geometric side) and correctly deflate it to the known
2+1-gravity feature. The 2+1 mathematical-physics reading (and the toy-model caveat) is quarantined in
`paths/philosophical/PHYSICS_RESONANCES.md`.

```bash
python frontier/B97_sl2r_lorentzian/probe.py
python -m pytest tests/test_b97_sl2r_lorentzian.py -q
```
No Origin-core claim; proven core P1–P16 untouched.

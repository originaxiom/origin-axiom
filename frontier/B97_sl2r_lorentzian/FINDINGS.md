# B97 — where Lorentzian structure lives: the SL(2,ℝ)/Teichmüller component

**Status: `computer-assisted`.** Neutral Lie theory / low-dim topology; **no physics claim** — the
2+1-gravity reading is quarantined in `speculations/archive/PHYSICS_RESONANCES.md`. No Origin-core claim;
proven core P1–P16 untouched. Script `probe.py`; test `tests/test_b97_sl2r_lorentzian.py`.

B96 computed the volume Hessian on the **SL(2,ℂ) geometric** (hyperbolic-3-manifold) component and found
it **negative definite, `(0,2)` Euclidean** (Mostow). This probe checks the other side: the once-punctured
torus *fiber* also has an **SL(2,ℝ) (Fuchsian / Teichmüller)** component — the phase space of 2+1 gravity
(Witten 1988: 2+1 gravity = Chern–Simons of SL(2,ℝ)). It locates the Lorentzian structure precisely.

## (1) The gauge-algebra signature
The trace/Killing form `tr(XY)`:
```
   sl(2,ℝ) = so(2,1):  signature (2,1)  — the 2+1 MINKOWSKI metric (LORENTZIAN)
   su(2)   = so(3):    signature (0,3)  — EUCLIDEAN
```
The Lorentzian `(2,1)` form is the Killing form of `sl(2,ℝ)`; it is absent on the compact `su(2)` side.

## (2) The real component genuinely exists
The fiber group `F₂=⟨X,Y⟩` has an explicit **SL(2,ℝ) Fuchsian** rep (a Teichmüller point of the
once-punctured torus): `X,Y` real, `det 1`, `|tr|>2` (hyperbolic), `tr[X,Y]=−2` (boundary/puncture
parabolic) — distinct from the SL(2,ℂ) geometric 3-manifold rep B96 used.

## (3) Local Lorentz invariance
The SL(2,ℝ) holonomy acts on the gauge algebra by `Ad`, and `Ad(g)` **preserves the `(2,1)` Minkowski
form** (`AdᵀG Ad=G` to ~1e-15): the holonomy acts by **SO(2,1) Lorentz transformations**.

## Verdict (mathematics; the deflation is honest)
Lorentzian structure **is present** — but it is the `so(2,1)=sl(2,ℝ)` **gauge-algebra** (Killing-form)
signature on the SL(2,ℝ)/Teichmüller component, i.e. the 2+1 Minkowski metric. It is **structural** (the
gauge group of 2+1 gravity *is* the Lorentz group), present **by construction, not emergent or derived**.
So **B96 (Euclidean on the geometric component) + B97 (Lorentzian gauge algebra on the real component)
locate the Lorentzian form precisely**: it sits on the real/Teichmüller side as the gauge structure, not on
the geometric side, and it is the well-known 2+1-gravity feature — *not* a derived spacetime. The 2+1
mathematical-physics reading, and the caveat that 2+1 gravity is a solvable toy model (no local gravitons,
not 3+1 fundamental physics), are in the quarantine.

```bash
python frontier/B97_sl2r_lorentzian/probe.py
python -m pytest tests/test_b97_sl2r_lorentzian.py -q
```
No physics claim; proven core P1–P16 untouched; outreach dormant.

# B96 — geometry invariants of the metallic mapping-torus manifolds

Bounded quantum-topology computations on the metallic bundles (`m=1→4_1`, `m=2→m136`, `m=3→s464`), banked
as **mathematics**. Physics interpretations are quarantined in `paths/philosophical/PHYSICS_RESONANCES.md`.

- **`probe.py`** — (1) the **volume ordering** `2.030 < 3.664 < 4.814` (SnapPy + Bloch–Wigner cross-check),
  strictly monotone; `m=1` smallest (= the systole, B92). (2) the **volume Hessian signature**: the
  complete structure is a strict volume *maximum* (Mostow — 155/156 fillings below, 0 above) ⇒ the NZ
  volume Hessian is **negative definite, signature `(0,2)`** (and the A-variety boundary is 1-complex-dim,
  so no canonical 4×4 Hessian exists). (3) `|τ₃|` honest status (branch-ambiguous, needs Sage).
- **`FINDINGS.md`** — the results + honest scope.

**Result (`computer-assisted`).** The metallic volumes are monotone (`m=1` simplest). The **most-leveraged
geometric Hessian is `(0,2)` definite — not Lorentzian** — closing that door by computation, for a
structural reason (Mostow + the A-variety being a curve). No physics promotion.

```bash
python frontier/B96_geometry_invariants/probe.py
python -m pytest tests/test_b96_geometry_invariants.py -q
```
No Origin-core claim; proven core P1–P16 untouched.

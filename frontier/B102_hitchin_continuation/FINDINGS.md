# B102 — the W1/W2 dichotomy + the R4 (boundary-controlled cubic) continuation

**Status: `STRUCTURAL` + `computer-assisted` (D1–D4); the R4 continuation D5 is `computer-assisted` with an
`open` tail.** Two follow-ons to B101 (a CC-web handoff, **verified before landing**). Neutral
higher-Teichmüller / character-variety geometry; **no physics**. No Origin-core claim; proven core P1–P16
untouched. Script `probe.py`; test `tests/test_b102_hitchin_continuation.py`.

## D1 — the W1/W2 dichotomy
Cayley–Hamilton on the figure-eight `T₁²` forces every irreducible `Fix(T₁²)` SL(3) character to satisfy

```
   (trA − trA⁻¹)(trB − 1) = 0      and      (trA − trA⁻¹)(trB⁻¹ − 1) = 0,
```
so it is **Case I** (`trA = trA⁻¹`, self-dual) or the **`trB = trB⁻¹ = 1` branch**. Verified: the conditions
hold (a factor vanishes) on B71's exact `V0/W1/W2` coordinate families, and a census of irreducible
`Fix(T₁²)` characters has **0 "neither"** (e.g. 33 Case I + 5 branch + **0** at n=40; the prior verification
saw 143/143).

## D2/D3 — the ellipticity obstruction, cross-checked on B71's exact components
Mapping the dichotomy onto B71's components (`peripheral.py`), **realizing each as an explicit SL(3) rep**:
- **`W1 = (1,q,q,1,p,1,1,p)`** ⇒ `trA = trA⁻¹ = 1` ⇒ **`ρ(a)` has eigenvalues `{1, i, −i}`** (order-4
  **elliptic**) — verified order-independently on the realized rep.
- **`W2 = (p,1,1,q,1,q,p,1)`** ⇒ `trB = trB⁻¹ = 1` ⇒ **`ρ(b)` elliptic `{1, i, −i}`** — verified.
- **`V0`** (self-dual): contains the **geometric** rep, which is **complex** — `tr(AB)` is a root of
  `t² − t + 7` (the geometric SL(3) trace field **`Q(√−3)`**; in fact the whole rep lies in `Q(√−3)`),
  cusp unipotent.

**Verdict.** The SL(3) figure-eight components are all excluded from the **real `SL(3,ℝ)` Hitchin
component**, but for *different* reasons: **V0's geometric rep by complexity; the genuine non-`Sym²`
components W1/W2 by ELLIPTICITY** — an elliptic generator (`{1,i,−i}` on the unit circle) is **not
loxodromic**, so it fails Labourie's Anosov criterion. *Ellipticity is the cleaner obstruction for the
genuine components than "complex."* (Refines the verification chat's earlier "W1/W2 are complex.")

**Refinement to the handoff.** The handoff lumped both genuine components under "Case II = `trB=trB⁻¹=1`."
Precisely: **W1 carries the obstruction on `A`, W2 on `B`** — one elliptic generator each, the A- and
B-symmetric partners. (W1 is in the `trA=trA⁻¹` branch with `trA=1`; W2 in the `trB=trB⁻¹=1` branch.)
**Scope on `Q(√−3)`:** it is the geometric *point* of V0, not all of Case I (Case I is a 2-parameter family
with varying `tr(AB)`).

## D4 — the Task-M link
The `{1,i,−i}` elliptic spectrum **is** Task M's forced `n=3` spectrum (B95; `tr A = tr A⁻¹ = 1` forces
eigenvalues `{1,i,−i}`). The arithmetic object that disqualifies W1/W2 from the Hitchin component is the
same finite-order spectrum Task M derived at SL(3).

## D5 — the R4 continuation (the boundary-controlled cubic family)
Imposing the boundary conditions `tr(δC)=0`, `tr(C·δC)=0` (`C=ρ([a,b])`) cuts the `V₄⊕V₄` cubic directions
(dim 10) to a **9-dimensional relative family** that keeps the cusp regular-unipotent **to first order**
(`δe₁=δe₂=0`). **This is the robust, banked content** (and the natural refinement of B101 R4(b)).

**Honest finding (verify-don't-trust — the handoff's headline does NOT reproduce).** The boundary control is
**first-order only**. At *second* order the regular-unipotent cusp splits by cube roots
`1+(cε)^{1/3}·{1,ω,ω²}` into **one real + a complex pair**, so a generic relative-family ray complexifies the
cusp **immediately** (≈78% of rays already complex at `t=0.05`). The handoff's clean trajectory — the cusp
opening to a real `(λ,1,1/λ)` geodesic boundary with `Im=0` throughout and a cusp-collision wall at
**`t*≈3.775`** — **does not reproduce here**: the literal `rel[:,0]` in this environment goes complex near
`t=0`, **re-realifies to negative eigenvalues** (not a geodesic boundary) by `t≈0.4`, and is solidly
**3-real (not collided)** at `t=3.775`. The `t*≈3.775` is a non-reproducible, ray-dependent artifact of a
particular SVD-basis vector.

**Conclusion.** The boundary-controlled family controls the cusp only to first order; the strict
**unipotent-cusp-preserving** (finite-area FG-positive) continuation — which needs order-by-order correction
against the cube-root instability — **remains `open`**. (Reconciles with B101 R4(b): the *unconstrained*
deformation moved the cusp off unipotent at first order; the relative family delays that to second order but
does not eliminate it.)

## Citations
Heusener–Muñoz–Porti (the SL(3,ℂ) figure-eight character variety); Labourie (Anosov representations);
Hitchin / Fock–Goncharov / Goldman / Marquis (Hitchin component / convex projective). The B100 Probe-2
Ptolemy reps would be the literal-figure-eight cross-check (route a), but reconstructing explicit fiber
matrices from Ptolemy coordinates is reconstruction-heavy; **route (b)** — classifying B71's *realized*
W1/W2/V0 — is the airtight in-house equivalent and is what we ran.

```bash
python frontier/B102_hitchin_continuation/probe.py
python -m pytest tests/test_b102_hitchin_continuation.py -q
```
No physics claim; proven core P1–P16 untouched; physics chapter stays CLOSED; outreach dormant.

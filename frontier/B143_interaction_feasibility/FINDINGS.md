# B143 — strategic synthesis (banked) + Campaign-1 feasibility scope: the venue verdict (V132)

Two deliverables: the strategic synthesis (`../../docs/STRATEGIC_SYNTHESIS.md`) and the gating
feasibility scope for Campaign 1 ("ask the chirality question of the glued objects"). MATH tier; firewalled; nothing
to `CLAIMS.md`; P1–P16, B85, the merged B124–B142 untouched.

## The venue verdict (the gating result)

**The chirality-of-interactions question cannot be answered in the algebraic (trace) venue — that venue is mirror-blind
— and needs orientation-sensitive tooling not yet installed.** Concretely:

- **The key gating fact (RIGOROUS).** Chirality splits into (i) *genuinely chiral manifold* (no orientation-reversing
  self-homeo — generic, already achieved by composites, B128) and (ii) *mirror = an orientation-independently distinct
  object* (the real wall, B139/B140). B131's interaction lives in the `(κ = tr[A,B], trT = tr t)` A-polynomial fiber
  product — **both are trace invariants, and the mirror (`swap_{R↔L} ∘ reverse`) preserves every trace** (verified
  here for seeds 1,2,3 and compositions). So the mirror acts as the **identity** on the algebraic data ⟹ the fork is
  automatically mirror-invariant ⟹ **the algebraic venue is structurally blind to chirality-(ii).** It carries the
  κ-**landscape** (discrete selection, Lead A), not chirality.
- **(A) algebraic** — reuses B131 (`apoly_relation`/`fork`), reproduces the exact `(1,2)` fork `{−4,−2}`. Venue for the
  landscape; blind to (ii).
- **(T) topological** — gluing two distinct 1-cusped bundles along their cusp tori gives a **closed JSJ** manifold (two
  hyperbolic pieces), **non-hyperbolic**. SnapPy is hyperbolic-only with no direct boundary-glue API; this venue *can*
  see (ii) (orientation-sensitive) but needs **Regina** (JSJ / normal surfaces) or manual triangulation. **Regina is
  not installed.**
- **(link) scout** — the ideal venue is a 2-cusped **hyperbolic** realization (SnapPy-native: `is_amphicheiral` + CS
  work), but whether the two-seed interaction *has* such a realization is itself a construction question (open).
- **(588) an AI-assisted review's claim** — the "588 irreducible reps" count is not reproducible without the source method; the
  falsifiable part (non-trivial Massey product → dim reduction) is **dead for s776** (the 3-chain link is **not**
  Brunnian; K-I, `is_isometric_to(s776, L6a4)` = False). If computed on the real Borromean rings (L6a4) it is a
  separate item, still subject to MB10 (SL(2,ℂ) dim ≠ rank SU(3)).

**Consequence for B144 (the actual chirality campaign):** it must run in the **topological venue** (install Regina;
build the closed JSJ composite; test whether an orientation-*independent* invariant — JSJ gluing data / torsion —
distinguishes it from its mirror, with `is_amphicheiral` as the (i)-control) **or** in a **hyperbolic-link
realization** if one can be constructed. The "scope first" recommendation paid off: the obvious algebraic route would
have produced a mirror-invariant artifact and read as "no chirality" for a *trivial* reason (trace-blindness), not a
real one.

## The strategic synthesis (banked separately)

`../../docs/STRATEGIC_SYNTHESIS.md` records the convergence (an AI-assisted multi-pass review), two-tier (math program
/ labeled POSTULATED physics aspiration): the monad + subtractive-shell shape; the three-layer "why" (forced≠contingent
/ finiteness-density / level-gap); the corrected scorecard (chirality the only *proven* obstruction; the 3d-3d
dictionary borrowed/POSTULATED, K006); the chirality (i)/(ii) distinction; the open-paths map; and the Campaign 1/2/3
roadmap. Guard **MB11** (state every result twice — bare math theorem + labeled POSTULATED physics reading; never let
the second contaminate the first) is banked from the drift this synthesis caught in CC's own reflection.

## Reproduce

```
python frontier/B143_interaction_feasibility/probe.py
python -m pytest tests/test_b143_interaction_feasibility.py -q
```

Pure-sympy core (the mirror-blindness + B131 reuse) runs unconditionally; the SnapPy/Regina checks are gated.

**Tier.** MATH (strategy + feasibility). New `docs/STRATEGIC_SYNTHESIS.md`; `REPRODUCIBILITY.md` MB11;
`docs/OPEN_LEADS.md` updated. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B142 untouched. Ledger **V132**.

**Anchors:** the three reflections; B131 (the algebraic interaction this scopes), B139/B140 (the mirror/trace facts
that make (A) blind to (ii)), B128/`K011` (composite chirality (i)), B141 (finiteness/density), K-I/MB10 (the 588
correction), `K006` (the borrowed 3d-3d dictionary). External: JSJ decomposition; Regina (normal surfaces).

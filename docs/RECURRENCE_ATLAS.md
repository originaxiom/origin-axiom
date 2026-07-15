# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-07-15 from 585 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 585 frontier probes; status {'banked': 395, 'dead': 126, 'open': 47, 'dormant': 17}
  the ONE conserved first integral: kappa (recurs 166x, 28%) -- genuine unity, MUST recur
  top recurring motifs: firewall(409), golden(372), eisenstein(294), metallic(286), trace_map(283), figure_eight(274)
  recurrence is: structural-invariant 2157 mentions | conserved-integral 166 | TOOL 283
  the honest split: the trace-map TOOL is in 283 probes (48%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B521, B156, B598, B309, B321
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 409 | 69% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 372 | 63% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| eisenstein | 294 | 50% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| metallic | 286 | 48% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 283 | 48% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| figure_eight | 274 | 46% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| torsion | 209 | 35% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| amphichiral_cp | 194 | 33% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| kappa | 166 | 28% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| wrt_quantum | 150 | 25% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| z3_generation | 115 | 19% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| lorentzian | 106 | 18% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| dickson_tower | 93 | 15% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| symplectic | 81 | 13% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 61 | 10% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 57 | 9% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 26 | 4% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 21 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **166** probes (28%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **2157** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **283** probes (48%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| cancellation | 34 | golden | golden(24), firewall(23), trace_map(20), eisenstein(20) |
| selector | 17 | firewall | firewall(11), trace_map(10), eisenstein(10), golden(10) |
| measure | 34 | firewall | firewall(22), golden(22), trace_map(14), figure_eight(12) |
| units_scale | 69 | firewall | firewall(57), golden(47), metallic(40), trace_map(37) |
| gauge_dict | 34 | firewall | firewall(29), figure_eight(23), golden(22), eisenstein(21) |
| particle_dict | 43 | eisenstein | eisenstein(36), firewall(36), golden(30), z3_generation(30) |
| spacetime_3p1 | 75 | metallic | figure_eight(52), trace_map(45), metallic(45), golden(44) |
| observable | 26 | golden | golden(19), metallic(14), torsion(14), firewall(14) |
| numerology | 17 | firewall | firewall(14), golden(13), metallic(12), torsion(12) |
| bridge_construction | 2 | golden | golden(2), amphichiral_cp(2), wrt_quantum(2), firewall(2) |

## Candidate meeting-points — cross-domain re-surfacings

> **These are CANDIDATES for human judgement, never proof.** The detector scores *domain breadth* + documented **unity-patterns** (co-occurrence signatures seeded from K007/K021/B67/B121/B261/B293). Co-occurrence ≠ meeting: a probe can name-check many motifs without identifying them. The famous meetings land in the top tier, but so do many synthesis probes — that saturation is itself the 'one object seen from many angles' fingerprint. Confirm each by reading the probe.


| probe | score | status | unity-patterns fired | domains |
|---|---|---|---|---|
| B530 | 25 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B521 | 23 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B156 | 22 | banked | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, representation, topology |
| B598 | 22 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, physics, quantum, topology |
| B309 | 21 | banked | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B321 | 21 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, topology |
| B154 | 20 | dead | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, quantum, representation, topology |
| B469 | 20 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B491 | 19 | dormant | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B496 | 19 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, quantum, topology |
| B105 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, geometry, physics, representation, topology |
| B148 | 18 | banked | object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, representation, topology |
| B200 | 18 | dead | physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, representation |
| B272 | 18 | dead | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B295 | 18 | dead | two_ends+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B425 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B440 | 18 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, representation, topology |

**The unity-patterns** (the documented cross-structure identifications the detector looks for):

- `two_ends` (weight 3) — the two arithmetic ends (golden √5 / Eisenstein √−3) identified as one object -- K021/B332/B261
- `object=dynamics` (weight 2) — the carrier knot realized as the trace-map fixed locus / its conserved trace -- B67/K007
- `physics_bridge` (weight 3) — a conserved math structure carried across the topology/arithmetic -> physics bridge -- B121
- `quantum_meeting` (weight 2) — the WRT/AJ quantum invariant meeting the arithmetic ends -- B261
- `symplectic_casimir` (weight 2) — kappa realized as the Goldman symplectic Casimir -- B293

## Gaps — the open frontier

Obstacle-types with few **banked** resolutions (under-resolved ⇒ where the object has *not* yet been shown to help):

| obstacle-type | banked / touched |
|---|---|
| source_free | 0/1 |
| bridge_construction | 2/4 |
| gauge_dict | 34/57 |
| numerology | 17/27 |
| spacetime_3p1 | 75/116 |
| measure | 34/51 |
| cancellation | 34/50 |
| units_scale | 69/100 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

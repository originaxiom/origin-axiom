# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-07-08 from 447 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 447 frontier probes; status {'banked': 303, 'dead': 87, 'open': 43, 'dormant': 14}
  the ONE conserved first integral: kappa (recurs 112x, 25%) -- genuine unity, MUST recur
  top recurring motifs: firewall(326), golden(275), metallic(232), eisenstein(229), trace_map(225), figure_eight(222)
  recurrence is: structural-invariant 1672 mentions | conserved-integral 112 | TOOL 225
  the honest split: the trace-map TOOL is in 225 probes (50%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B156, B309, B321, B154, B140, B258
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 326 | 72% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 275 | 61% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| metallic | 232 | 51% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| eisenstein | 229 | 51% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| trace_map | 225 | 50% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| figure_eight | 222 | 49% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| torsion | 152 | 34% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| amphichiral_cp | 135 | 30% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| kappa | 112 | 25% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| wrt_quantum | 108 | 24% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| z3_generation | 90 | 20% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| dickson_tower | 86 | 19% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| lorentzian | 73 | 16% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| symplectic | 66 | 14% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 57 | 12% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 43 | 9% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 22 | 4% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 16 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **112** probes (25%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **1672** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **225** probes (50%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| cancellation | 28 | golden | golden(20), firewall(20), trace_map(18), eisenstein(17) |
| selector | 15 | firewall | firewall(10), trace_map(9), golden(9), torsion(9) |
| measure | 20 | firewall | firewall(16), golden(11), figure_eight(10), trace_map(10) |
| units_scale | 56 | firewall | firewall(47), golden(38), trace_map(32), metallic(30) |
| gauge_dict | 27 | firewall | firewall(23), golden(20), figure_eight(20), eisenstein(17) |
| particle_dict | 34 | eisenstein | eisenstein(31), firewall(31), z3_generation(25), golden(23) |
| spacetime_3p1 | 60 | metallic | figure_eight(41), metallic(39), trace_map(36), dickson_tower(36) |
| observable | 12 | firewall | firewall(12), metallic(10), golden(8), torsion(8) |
| numerology | 13 | firewall | firewall(13), golden(11), torsion(11), eisenstein(10) |
| bridge_construction | 2 | golden | golden(2), amphichiral_cp(2), wrt_quantum(2), firewall(2) |

## Candidate meeting-points — cross-domain re-surfacings

> **These are CANDIDATES for human judgement, never proof.** The detector scores *domain breadth* + documented **unity-patterns** (co-occurrence signatures seeded from K007/K021/B67/B121/B261/B293). Co-occurrence ≠ meeting: a probe can name-check many motifs without identifying them. The famous meetings land in the top tier, but so do many synthesis probes — that saturation is itself the 'one object seen from many angles' fingerprint. Confirm each by reading the probe.


| probe | score | status | unity-patterns fired | domains |
|---|---|---|---|---|
| B156 | 22 | banked | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, representation, topology |
| B309 | 21 | banked | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B321 | 21 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, topology |
| B154 | 20 | dead | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, quantum, representation, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B469 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B105 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, geometry, physics, representation, topology |
| B148 | 18 | banked | object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, representation, topology |
| B200 | 18 | dead | physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, representation |
| B272 | 18 | dead | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B295 | 18 | dead | two_ends+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B425 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B440 | 18 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, representation, topology |
| B127 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B129 | 17 | banked | two_ends+object=dynamics | arithmetic, dynamics, meta, quantum, representation, topology |
| B132 | 17 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B240 | 17 | banked | object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B315 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, geometry, meta, quantum, topology |

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
| numerology | 13/21 |
| spacetime_3p1 | 60/93 |
| gauge_dict | 27/41 |
| units_scale | 56/84 |
| measure | 20/30 |
| observable | 12/18 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

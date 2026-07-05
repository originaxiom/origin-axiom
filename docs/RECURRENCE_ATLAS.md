# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-07-05 from 420 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 420 frontier probes; status {'banked': 283, 'dead': 80, 'open': 43, 'dormant': 14}
  the ONE conserved first integral: kappa (recurs 102x, 24%) -- genuine unity, MUST recur
  top recurring motifs: firewall(299), golden(259), metallic(217), trace_map(212), eisenstein(210), figure_eight(204)
  recurrence is: structural-invariant 1536 mentions | conserved-integral 102 | TOOL 212
  the honest split: the trace-map TOOL is in 212 probes (50%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B156, B309, B321, B154, B140, B258
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 299 | 71% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 259 | 61% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| metallic | 217 | 51% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 212 | 50% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| eisenstein | 210 | 50% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| figure_eight | 204 | 48% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| torsion | 129 | 30% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| amphichiral_cp | 120 | 28% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| kappa | 102 | 24% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| wrt_quantum | 97 | 23% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| dickson_tower | 83 | 19% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| z3_generation | 79 | 18% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| lorentzian | 67 | 15% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| symplectic | 65 | 15% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 54 | 12% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 42 | 10% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 20 | 4% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 13 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **102** probes (24%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **1536** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **212** probes (50%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| cancellation | 26 | golden | golden(19), firewall(18), trace_map(16), eisenstein(15) |
| selector | 14 | golden | trace_map(9), golden(9), firewall(9), figure_eight(8) |
| measure | 19 | firewall | firewall(15), figure_eight(10), golden(10), trace_map(9) |
| units_scale | 54 | firewall | firewall(45), golden(37), trace_map(30), metallic(29) |
| gauge_dict | 26 | firewall | firewall(22), golden(20), figure_eight(20), eisenstein(16) |
| particle_dict | 30 | eisenstein | eisenstein(27), firewall(27), z3_generation(22), golden(21) |
| spacetime_3p1 | 59 | metallic | figure_eight(41), metallic(38), trace_map(36), dickson_tower(36) |
| observable | 7 | firewall | firewall(7), metallic(5), golden(4), eisenstein(3) |
| numerology | 12 | firewall | firewall(12), golden(10), torsion(10), eisenstein(9) |
| bridge_construction | 1 | kappa | trace_map(1), kappa(1), metallic(1), golden(1) |

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
| B105 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, geometry, physics, representation, topology |
| B148 | 18 | banked | object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, representation, topology |
| B200 | 18 | dead | physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, representation |
| B272 | 18 | dead | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B295 | 18 | dead | two_ends+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B425 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, representation, topology |
| B127 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B129 | 17 | banked | two_ends+object=dynamics | arithmetic, dynamics, meta, quantum, representation, topology |
| B132 | 17 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B240 | 17 | banked | object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B315 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, geometry, meta, quantum, topology |
| B126 | 16 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B155 | 16 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, topology |

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
| bridge_construction | 1/3 |
| observable | 7/13 |
| numerology | 12/20 |
| spacetime_3p1 | 59/91 |
| units_scale | 54/82 |
| gauge_dict | 26/39 |
| selector | 14/20 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

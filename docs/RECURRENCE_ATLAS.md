# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-07-28 from 724 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 724 frontier probes; status {'banked': 489, 'dead': 167, 'open': 51, 'dormant': 17}
  the ONE conserved first integral: kappa (recurs 188x, 25%) -- genuine unity, MUST recur
  top recurring motifs: firewall(474), golden(472), eisenstein(399), figure_eight(346), metallic(341), trace_map(333)
  recurrence is: structural-invariant 2662 mentions | conserved-integral 188 | TOOL 333
  the honest split: the trace-map TOOL is in 333 probes (45%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B521, B156, B598, B309, B321
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 474 | 65% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 472 | 65% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| eisenstein | 399 | 55% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| figure_eight | 346 | 47% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| metallic | 341 | 47% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 333 | 45% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| torsion | 271 | 37% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| amphichiral_cp | 244 | 33% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| wrt_quantum | 199 | 27% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| kappa | 188 | 25% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| z3_generation | 150 | 20% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| lorentzian | 128 | 17% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| dickson_tower | 102 | 14% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| symplectic | 93 | 12% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 73 | 10% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 62 | 8% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 27 | 3% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 27 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **188** probes (25%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **2662** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **333** probes (45%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| cancellation | 40 | golden | golden(28), eisenstein(25), firewall(25), trace_map(22) |
| selector | 17 | firewall | firewall(11), trace_map(10), eisenstein(10), golden(10) |
| measure | 50 | golden | golden(34), firewall(33), eisenstein(23), figure_eight(21) |
| units_scale | 83 | firewall | firewall(61), golden(56), metallic(47), trace_map(42) |
| gauge_dict | 39 | firewall | firewall(29), eisenstein(26), figure_eight(25), golden(24) |
| particle_dict | 54 | eisenstein | eisenstein(44), firewall(40), golden(39), z3_generation(34) |
| spacetime_3p1 | 93 | golden | figure_eight(62), golden(61), trace_map(53), metallic(53) |
| observable | 32 | golden | golden(24), metallic(17), torsion(17), firewall(17) |
| numerology | 22 | eisenstein | eisenstein(17), golden(16), firewall(16), torsion(15) |
| bridge_construction | 5 | golden | golden(4), wrt_quantum(4), firewall(4), figure_eight(4) |

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
| B717 | 21 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B746 | 21 | banked | two_ends+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, representation, topology |
| B154 | 20 | dead | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, quantum, representation, topology |
| B469 | 20 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B491 | 19 | dormant | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B496 | 19 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, quantum, topology |
| B709 | 19 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B716 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, geometry, physics, quantum, topology |
| B755 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B105 | 18 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, geometry, physics, representation, topology |
| B148 | 18 | banked | object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, representation, topology |

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
| bridge_construction | 5/10 |
| gauge_dict | 39/64 |
| cancellation | 40/62 |
| numerology | 22/34 |
| measure | 50/76 |
| spacetime_3p1 | 93/140 |
| units_scale | 83/119 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

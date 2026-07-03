# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-07-03 from 372 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 372 frontier probes; status {'banked': 253, 'dead': 63, 'open': 42, 'dormant': 14}
  the ONE conserved first integral: kappa (recurs 99x, 26%) -- genuine unity, MUST recur
  top recurring motifs: firewall(252), golden(227), metallic(204), trace_map(203), figure_eight(188), eisenstein(187)
  recurrence is: structural-invariant 1363 mentions | conserved-integral 99 | TOOL 203
  the honest split: the trace-map TOOL is in 203 probes (54%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B156, B309, B321, B154, B140, B258
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 252 | 67% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 227 | 61% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| metallic | 204 | 54% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 203 | 54% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| figure_eight | 188 | 50% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| eisenstein | 187 | 50% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| amphichiral_cp | 108 | 29% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| torsion | 104 | 27% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| kappa | 99 | 26% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| wrt_quantum | 89 | 23% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| dickson_tower | 78 | 20% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| z3_generation | 68 | 18% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| symplectic | 65 | 17% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| lorentzian | 63 | 16% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| apolynomial | 49 | 13% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 40 | 10% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 18 | 4% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 12 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **99** probes (26%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **1363** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **203** probes (54%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| cancellation | 24 | golden | golden(17), trace_map(16), firewall(16), figure_eight(14) |
| selector | 14 | golden | trace_map(9), golden(9), firewall(9), figure_eight(8) |
| measure | 14 | firewall | firewall(10), figure_eight(8), trace_map(8), metallic(8) |
| units_scale | 50 | firewall | firewall(41), golden(35), trace_map(29), metallic(26) |
| gauge_dict | 24 | firewall | firewall(20), golden(18), figure_eight(18), eisenstein(15) |
| particle_dict | 28 | eisenstein | eisenstein(25), firewall(25), z3_generation(21), golden(19) |
| spacetime_3p1 | 57 | metallic | figure_eight(40), metallic(38), trace_map(35), dickson_tower(35) |
| observable | 7 | firewall | firewall(7), metallic(5), golden(4), eisenstein(3) |
| numerology | 11 | firewall | firewall(11), golden(9), torsion(9), metallic(8) |
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
| B127 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B129 | 17 | banked | two_ends+object=dynamics | arithmetic, dynamics, meta, quantum, representation, topology |
| B132 | 17 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B240 | 17 | banked | object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B315 | 17 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, geometry, meta, quantum, topology |
| B126 | 16 | banked | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, topology |
| B155 | 16 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, topology |
| B157 | 16 | dead | two_ends+object=dynamics+quantum_meeting | arithmetic, dynamics, meta, quantum, representation, topology |

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
| numerology | 11/19 |
| spacetime_3p1 | 57/88 |
| units_scale | 50/76 |
| gauge_dict | 24/36 |
| measure | 14/20 |
| selector | 14/20 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

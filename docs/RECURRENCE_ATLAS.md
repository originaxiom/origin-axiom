# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-08-09 from 925 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 925 frontier probes; status {'open': 60, 'banked': 606, 'dead': 240, 'dormant': 19}
  the ONE conserved first integral: kappa (recurs 219x, 23%) -- genuine unity, MUST recur
  top recurring motifs: firewall(536), golden(531), eisenstein(488), figure_eight(401), metallic(392), trace_map(369)
  recurrence is: structural-invariant 3146 mentions | conserved-integral 219 | TOOL 369
  the honest split: the trace-map TOOL is in 369 probes (39%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B521, B156, B598, B309, B321
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| firewall | 536 | 57% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| golden | 531 | 57% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| eisenstein | 488 | 52% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| figure_eight | 401 | 43% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| metallic | 392 | 42% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 369 | 39% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| amphichiral_cp | 302 | 32% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| torsion | 301 | 32% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| wrt_quantum | 223 | 24% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| kappa | 219 | 23% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| z3_generation | 207 | 22% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| lorentzian | 167 | 18% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| dickson_tower | 105 | 11% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| symplectic | 96 | 10% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 77 | 8% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| markov_cubic | 67 | 7% | invariant | structural | topology | the trace-triple SURFACE the trace map acts on: the Markov/Fricke cubic x^2+y^2+z^2-xyz=c and SL(2,Z) triples (tr A, tr B, tr AB). Deliberately EXCLUDES the bare phrase 'character variety', which B824 measured at 13.8%% of the corpus -- this programme's subject matter, not a topic within it |
| quasicrystal | 65 | 7% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| hyperbolicity_split | 28 | 3% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |
| five_web | 28 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **219** probes (23%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **3146** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **369** probes (39%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| source_free | 1 | golden | figure_eight(1), golden(1) |
| cancellation | 48 | golden | golden(30), firewall(29), eisenstein(28), trace_map(22) |
| selector | 18 | firewall | firewall(12), trace_map(11), eisenstein(11), golden(11) |
| measure | 83 | golden | golden(46), firewall(45), eisenstein(40), figure_eight(36) |
| units_scale | 91 | firewall | firewall(65), golden(59), metallic(51), eisenstein(47) |
| gauge_dict | 55 | eisenstein | eisenstein(33), firewall(32), figure_eight(28), amphichiral_cp(27) |
| particle_dict | 75 | eisenstein | eisenstein(53), firewall(52), z3_generation(49), golden(44) |
| spacetime_3p1 | 105 | golden | figure_eight(66), golden(64), eisenstein(61), trace_map(55) |
| observable | 35 | golden | golden(26), torsion(18), metallic(18), firewall(17) |
| numerology | 21 | golden | golden(16), firewall(16), eisenstein(16), torsion(14) |
| bridge_construction | 6 | golden | golden(4), wrt_quantum(4), firewall(4), figure_eight(4) |

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
| B491 | 20 | dormant | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
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
| source_free | 1/3 |
| bridge_construction | 6/16 |
| measure | 83/140 |
| gauge_dict | 55/88 |
| spacetime_3p1 | 105/167 |
| numerology | 21/33 |
| cancellation | 48/70 |
| observable | 35/51 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

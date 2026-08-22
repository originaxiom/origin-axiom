# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-08-22 from 1040 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 1040 frontier probes; status {'open': 63, 'banked': 694, 'dead': 264, 'dormant': 19}
  the ONE conserved first integral: kappa (recurs 234x, 22%) -- genuine unity, MUST recur
  top recurring motifs: golden(589), firewall(562), eisenstein(553), figure_eight(427), metallic(417), trace_map(395)
  recurrence is: structural-invariant 3432 mentions | conserved-integral 234 | TOOL 395
  the honest split: the trace-map TOOL is in 395 probes (37%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B521, B156, B598, B309, B321
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| golden | 589 | 56% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| firewall | 562 | 54% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| eisenstein | 553 | 53% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| figure_eight | 427 | 41% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| metallic | 417 | 40% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 395 | 37% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| amphichiral_cp | 363 | 34% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| torsion | 317 | 30% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| wrt_quantum | 252 | 24% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| kappa | 234 | 22% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| z3_generation | 232 | 22% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| lorentzian | 189 | 18% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| dickson_tower | 105 | 10% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| symplectic | 99 | 9% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| apolynomial | 80 | 7% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 68 | 6% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| markov_cubic | 67 | 6% | invariant | structural | topology | the trace-triple SURFACE the trace map acts on: the Markov/Fricke cubic x^2+y^2+z^2-xyz=c and SL(2,Z) triples (tr A, tr B, tr AB). Deliberately EXCLUDES the bare phrase 'character variety', which B824 measured at 13.8%% of the corpus -- this programme's subject matter, not a topic within it |
| five_web | 32 | 3% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |
| hyperbolicity_split | 28 | 2% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **234** probes (22%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **3432** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **395** probes (37%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| source_free | 1 | golden | figure_eight(1), golden(1) |
| cancellation | 57 | golden | golden(35), eisenstein(33), firewall(31), trace_map(24) |
| selector | 18 | firewall | firewall(12), trace_map(11), eisenstein(11), golden(11) |
| measure | 103 | golden | golden(57), eisenstein(54), firewall(51), figure_eight(42) |
| units_scale | 102 | firewall | firewall(68), golden(62), metallic(54), eisenstein(51) |
| gauge_dict | 61 | eisenstein | eisenstein(37), firewall(34), golden(30), amphichiral_cp(29) |
| particle_dict | 82 | eisenstein | eisenstein(59), z3_generation(53), firewall(52), golden(47) |
| spacetime_3p1 | 122 | eisenstein | eisenstein(71), golden(71), figure_eight(68), trace_map(61) |
| observable | 41 | golden | golden(32), metallic(20), eisenstein(18), torsion(18) |
| numerology | 25 | eisenstein | eisenstein(18), golden(17), firewall(16), metallic(15) |
| bridge_construction | 9 | golden | golden(7), firewall(6), figure_eight(5), eisenstein(5) |

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
| B1069 | 20 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B154 | 20 | dead | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, quantum, representation, topology |
| B469 | 20 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B491 | 20 | dormant | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B1009 | 19 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B1067 | 19 | open | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B496 | 19 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, quantum, topology |
| B709 | 19 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B716 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, geometry, physics, quantum, topology |

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
| bridge_construction | 9/19 |
| gauge_dict | 61/99 |
| measure | 103/166 |
| spacetime_3p1 | 122/189 |
| numerology | 25/38 |
| selector | 18/27 |
| observable | 41/59 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

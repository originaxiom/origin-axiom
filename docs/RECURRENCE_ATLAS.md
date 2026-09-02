# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-09-02 from 1143 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 1143 frontier probes; status {'open': 64, 'banked': 753, 'dead': 304, 'dormant': 22}
  the ONE conserved first integral: kappa (recurs 253x, 22%) -- genuine unity, MUST recur
  top recurring motifs: golden(641), eisenstein(625), firewall(619), figure_eight(479), metallic(427), amphichiral_cp(418)
  recurrence is: structural-invariant 3750 mentions | conserved-integral 253 | TOOL 413
  the honest split: the trace-map TOOL is in 413 probes (36%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B521, B156, B598, B1189, B309
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| golden | 641 | 56% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| eisenstein | 625 | 54% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| firewall | 619 | 54% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| figure_eight | 479 | 41% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| metallic | 427 | 37% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| amphichiral_cp | 418 | 36% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| trace_map | 413 | 36% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| torsion | 347 | 30% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| wrt_quantum | 270 | 23% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| z3_generation | 259 | 22% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| kappa | 253 | 22% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| lorentzian | 203 | 17% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| symplectic | 108 | 9% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| dickson_tower | 105 | 9% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| apolynomial | 83 | 7% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| quasicrystal | 70 | 6% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| markov_cubic | 70 | 6% | invariant | structural | topology | the trace-triple SURFACE the trace map acts on: the Markov/Fricke cubic x^2+y^2+z^2-xyz=c and SL(2,Z) triples (tr A, tr B, tr AB). Deliberately EXCLUDES the bare phrase 'character variety', which B824 measured at 13.8%% of the corpus -- this programme's subject matter, not a topic within it |
| five_web | 33 | 2% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |
| hyperbolicity_split | 28 | 2% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **253** probes (22%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **3750** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **413** probes (36%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| source_free | 1 | golden | figure_eight(1), golden(1) |
| cancellation | 60 | golden | golden(37), eisenstein(35), firewall(34), trace_map(26) |
| selector | 18 | firewall | firewall(12), trace_map(11), eisenstein(11), golden(11) |
| measure | 112 | eisenstein | eisenstein(59), golden(58), firewall(55), figure_eight(45) |
| units_scale | 114 | firewall | firewall(77), golden(68), eisenstein(61), metallic(54) |
| gauge_dict | 65 | eisenstein | eisenstein(41), firewall(34), golden(33), figure_eight(32) |
| particle_dict | 96 | eisenstein | eisenstein(68), z3_generation(62), firewall(62), golden(58) |
| spacetime_3p1 | 132 | eisenstein | eisenstein(77), golden(77), figure_eight(71), trace_map(62) |
| observable | 45 | golden | golden(34), eisenstein(21), metallic(20), firewall(20) |
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
| B1189 | 21 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, topology |
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

**The unity-patterns** (the documented cross-structure identifications the detector looks for):

- `two_ends` (weight 3) — the two arithmetic ends (golden √5 / Eisenstein √−3) identified as one object -- K021/B332/B261; B1149 mechanism: the unit (det 1, disc 5) and ramified (norm 3, disc −3) answers to ONE trace-3 form, the object's clock + its conserved κ=1+q
- `object=dynamics` (weight 2) — the carrier knot realized as the trace-map fixed locus / its conserved trace -- B67/K007
- `physics_bridge` (weight 3) — a conserved math structure carried across the topology/arithmetic -> physics bridge -- B121
- `quantum_meeting` (weight 2) — the WRT/AJ quantum invariant meeting the arithmetic ends -- B261
- `symplectic_casimir` (weight 2) — kappa realized as the Goldman symplectic Casimir -- B293

## Gaps — the open frontier

Obstacle-types with few **banked** resolutions (under-resolved ⇒ where the object has *not* yet been shown to help):

| obstacle-type | banked / touched |
|---|---|
| source_free | 1/3 |
| bridge_construction | 9/21 |
| measure | 112/188 |
| gauge_dict | 65/106 |
| selector | 18/29 |
| spacetime_3p1 | 132/206 |
| numerology | 25/39 |
| units_scale | 114/166 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

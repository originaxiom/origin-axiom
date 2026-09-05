# The Recurrence Atlas — the map

> **GENERATED FILE — do not hand-edit.** Regenerate with `python scripts/atlas/render.py`.
> Last generated: 2026-09-05 from 1162 frontier probes.
> This is a *derived navigation aid*, not a claim: it maps which mathematical **motifs recur**, at which
> **obstacles**, and where a conserved motif **re-surfaces** across domains. The **vision** (why recurrence
> ≈ unity, and the honest caveat) is in [`knowledge/K023_the_recurrence_atlas.md`](../knowledge/K023_the_recurrence_atlas.md).
> Nothing here promotes to `CLAIMS.md`.

## Re-orient — the context card

```
THE RECURRENCE ATLAS -- context card
  corpus: 1162 frontier probes; status {'open': 67, 'banked': 760, 'dead': 312, 'dormant': 23}
  the ONE conserved first integral: kappa (recurs 260x, 22%) -- genuine unity, MUST recur
  top recurring motifs: golden(650), eisenstein(640), firewall(626), figure_eight(489), metallic(432), trace_map(422)
  recurrence is: structural-invariant 4463 mentions | conserved-integral 260 | TOOL 422
  the honest split: the trace-map TOOL is in 422 probes (36%) = method/selection-effect, NOT unity; only kappa is a forced first integral
  top meeting-point candidates: B530, B156, B521, B309, B598, B1189
  (obstacle oracle: query.resolutions_for(<type>); revive: query.revive(<B###>); gaps: query.gaps())
```

## Motif recurrence — frequency, kind, and conserved-status

The **conserved-status** is the honest axis: a **first-integral** *must* recur (mathematically forced ⇒ genuine unity); a **structural** invariant recurs because it is an invariant of the transform; a **tool** recurs because it is *our method* (a selection effect, not unity); **no** means derived/incidental.

| motif | #probes | % | kind | conserved | home domain | gloss |
|---|---|---|---|---|---|---|
| golden | 650 | 55% | arithmetic | structural | arithmetic | the golden end: Q(sqrt5), phi, E8, 2I |
| eisenstein | 640 | 55% | arithmetic | structural | arithmetic | the Eisenstein end: Q(sqrt-3), omega, E6, 2T |
| firewall | 626 | 53% | structure | structural | meta | the firewall / structural theorem / form-not-values |
| figure_eight | 489 | 42% | object | no | topology | the simplest hyperbolic knot; the carrier object |
| metallic | 432 | 37% | structure | structural | arithmetic | the metallic family lambda_m tower (golden/silver/bronze) |
| trace_map | 422 | 36% | dynamics | tool | dynamics | the trace map / Dehn-twist words / monodromy / substitution -- the METHOD |
| amphichiral_cp | 421 | 36% | symmetry | structural | topology | amphichirality / the CP sign +-pi/6 / CS=0 |
| coupling | 363 | 31% | question | no | physics | the observer/object interface: what the coupling supplies that neither side has alone (the listener map, the pair, the relational bit) |
| torsion | 354 | 30% | arithmetic | structural | arithmetic | the (Z/4)^2 congruence torsion / Alexander polynomial |
| closing | 343 | 29% | question | structural | topology | what closing the open object supplies and costs -- Dehn filling, the seam, the constitutive closure (B286/B287/B294) |
| measurement | 285 | 24% | question | no | dynamics | collapse, decoherence, the measurement postulate as a structural shape rather than an added axiom |
| wrt_quantum | 272 | 23% | quantum | no | quantum | the WRT / colored-Jones / modular quantum invariants |
| z3_generation | 270 | 23% | symmetry | structural | arithmetic | the generation Z/3 (deck / commensurator / omega-circulant) |
| kappa | 260 | 22% | invariant | first-integral | dynamics | the conserved commutator trace kappa = tr[a,b] = the Suto invariant |
| lorentzian | 207 | 17% | physics-bridge | no | physics | the Lorentzian / signature / spacetime bridge |
| choice | 179 | 15% | question | structural | arithmetic | the residual bit(s): the torsor of closings, the basepoint bit, what the object can and cannot select (A7/B766/B1183/B1225) |
| symplectic | 108 | 9% | structure | structural | geometry | the Goldman symplectic / Neumann-Zagier pairing |
| dickson_tower | 107 | 9% | structure | structural | representation | the Dickson tower rho_n / degree=rank / the det=-1 parity |
| monoid | 89 | 7% | question | structural | dynamics | End(F2) beyond the units: the four Hopfian-det strata, the non-invertible verbs the programme has never computed |
| apolynomial | 83 | 7% | structure | no | topology | the A-polynomial / Cooper-Long / AJ |
| arrow | 77 | 6% | question | no | dynamics | time's direction and/or its irreversibility -- the two are NOT the same question (B766 = the direction bit, the golden branch; S063 = irreversibility, entering at det != +-1) |
| markov_cubic | 73 | 6% | invariant | structural | topology | the trace-triple SURFACE the trace map acts on: the Markov/Fricke cubic x^2+y^2+z^2-xyz=c and SL(2,Z) triples (tr A, tr B, tr AB). Deliberately EXCLUDES the bare phrase 'character variety', which B824 measured at 13.8%% of the corpus -- this programme's subject matter, not a topic within it |
| quasicrystal | 70 | 6% | dynamics | structural | quantum | the Fibonacci quasicrystal / Suto / Damanik-Gorodetski |
| naming | 39 | 3% | question | structural | arithmetic | self-reference, the quine, self-name vs self-sign -- naming and choosing proved complementary (B762/B1184) |
| five_web | 34 | 2% | arithmetic | structural | arithmetic | the '5' recurrence web (H2): 40a1, conductor 40, Pisano |
| hyperbolicity_split | 28 | 2% | structure | structural | topology | the hyperbolicity-split motif (H4): object on both sides of the divide |

### The honest split — unity vs the hammer

- **Genuine unity:** the one conserved **first integral** `κ = tr[a,b]` recurs in **260** probes (22%). A first integral is *conserved by the trace map ∀m* (K001/K007), so it **must** recur — this recurrence is forced, not chosen.
- **Structural invariants** (the two ends, ω, the Dickson parity, …): **4463** mentions — invariants of the object's transforms.
- **The hammer (selection effect):** the trace-map **tool** appears in **422** probes (36%). This recurrence is *because it is our method* — it is **not** evidence of unity. The atlas keeps this separate on purpose (verify-don't-trust).

## The cycle — obstacle → which motif historically resolved it

For each obstacle-type (from `docs/atlas/FAILURE_ATLAS.md`), the motifs most present in the **banked** probes that hit it. *Heuristic* (keyword-matched obstacle, co-occurrence not causation).

| obstacle-type | #banked | top conserved resolver | top motifs |
|---|---|---|---|
| source_free | 1 | choice | choice(1), figure_eight(1), golden(1) |
| cancellation | 61 | golden | golden(38), eisenstein(36), firewall(35), trace_map(27) |
| selector | 18 | firewall | firewall(12), trace_map(11), eisenstein(11), golden(11) |
| measure | 115 | golden | golden(60), eisenstein(60), firewall(57), measurement(50) |
| units_scale | 113 | firewall | firewall(76), golden(67), eisenstein(60), metallic(54) |
| gauge_dict | 65 | eisenstein | eisenstein(41), firewall(34), golden(33), figure_eight(32) |
| particle_dict | 97 | eisenstein | eisenstein(69), z3_generation(63), firewall(62), golden(59) |
| spacetime_3p1 | 133 | eisenstein | eisenstein(78), golden(78), figure_eight(72), trace_map(63) |
| observable | 46 | golden | golden(34), coupling(25), measurement(22), eisenstein(21) |
| numerology | 25 | eisenstein | eisenstein(18), golden(17), firewall(16), metallic(15) |
| bridge_construction | 10 | golden | golden(8), firewall(7), eisenstein(6), coupling(5) |

## Candidate meeting-points — cross-domain re-surfacings

> **These are CANDIDATES for human judgement, never proof.** The detector scores *domain breadth* + documented **unity-patterns** (co-occurrence signatures seeded from K007/K021/B67/B121/B261/B293). Co-occurrence ≠ meeting: a probe can name-check many motifs without identifying them. The famous meetings land in the top tier, but so do many synthesis probes — that saturation is itself the 'one object seen from many angles' fingerprint. Confirm each by reading the probe.


| probe | score | status | unity-patterns fired | domains |
|---|---|---|---|---|
| B530 | 25 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B156 | 23 | banked | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, representation, topology |
| B521 | 23 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B309 | 22 | banked | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B598 | 22 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, physics, quantum, topology |
| B1189 | 21 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, topology |
| B321 | 21 | dead | two_ends+object=dynamics+physics_bridge+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, topology |
| B717 | 21 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, geometry, meta, physics, quantum, topology |
| B746 | 21 | banked | two_ends+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, representation, topology |
| B1067 | 20 | open | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B1069 | 20 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B154 | 20 | dead | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, quantum, representation, topology |
| B469 | 20 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B491 | 20 | dormant | two_ends+object=dynamics+quantum_meeting+symplectic_casimir | arithmetic, dynamics, geometry, meta, quantum, topology |
| B1009 | 19 | dead | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B140 | 19 | dead | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, representation, topology |
| B258 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B316 | 19 | banked | two_ends+object=dynamics+physics_bridge+quantum_meeting | arithmetic, dynamics, meta, physics, quantum, topology |
| B496 | 19 | banked | two_ends+object=dynamics+physics_bridge | arithmetic, dynamics, meta, physics, quantum, topology |
| B532 | 19 | open | two_ends+object=dynamics+symplectic_casimir | arithmetic, dynamics, geometry, meta, physics, representation, topology |

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
| bridge_construction | 10/22 |
| measure | 115/193 |
| selector | 18/30 |
| gauge_dict | 65/106 |
| spacetime_3p1 | 133/209 |
| numerology | 25/39 |
| units_scale | 113/168 |

---
*Generated by `scripts/atlas/` (mine → analyze → detect → render). The instrument is re-runnable; the map stays current by regeneration. See `knowledge/K023` for the vision and the honest tool-bias caveat.*

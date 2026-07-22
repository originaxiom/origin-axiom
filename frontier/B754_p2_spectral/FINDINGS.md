# FINDINGS — B754: P2 spectral-face stratum (the negatives hunt, stratum 2)

cc3, 2026-07-22. Branch `hunt/p2-spectral`. Sealed as B754 (PR to cc's merge gate;
cc = sole merge gate per standing rule). Frozen spectral surface: B737 (zeta-quotient
voice + residue + CM/palette), B739 (character rigidity), B746 (two-column law),
B753 (unitary θ-odd block, eigenphases ±72°, mixing 1/(φ√5)). Gate 5-Q binding
throughout.

## Summary

19 P1-banked negatives whose B′ annotations flagged the spectral face as unconsulted
were re-adjudicated against the frozen spectral surface. Each cell was required to
pass Gate 5-Q Q2 (discrimination) before consulting the face, with adversarial
skeptics on all FACE-OPENS, all FACE-IRRELEVANT, and 1-in-3 KILL-EXTENDS cells.

**Adjudicated tally (after two skeptic overrides):**

| verdict | count | meaning |
|---|---|---|
| KILL-EXTENDS | 17 | spectral face upholds/extends the kill |
| FACE-IRRELEVANT | 2 | spectral face provably does not touch the claim |
| FACE-OPENS | 0 | — |
| BLOCKED | 0 | — |

Zero open questions remain on the spectral face for these 19 targets.

## The headline: WALL-1

**WALL-1 (the program's oldest wall: "no SM value from the solo object") → KILL-EXTENDS.**

The original kill was an asserted umbrella leaning on the B307/B604/B632/B706 corpus
with no single discriminating computation. The spectral face was never consulted.

The cell's spectral-face extractor SFE(M) computed three non-generic axes for m004:
- (A) Cusp CM disc = −48 (conductor-4 order in O_K; B737 P3) — vs m003's disc = −3
  (maximal order); j-invariant gap = 2.836 × 10⁹
- (B) Hecke palette = (1, 2, 8) at levels (2)/(4)/(8) — vs m003's palette = (1) only
- (C) θ-odd eigenphases ±72°, mixing = 1/(φ√5) = 0.2764 (B753) — absent for m003

The kill extends on four independent spectral mechanisms:
1. **E1 VOICE = PURE FIELD CONSTANT.** B737 P4 S9: Res_{s=1} ζ_K = 2πh/(w√|d|) is a
   function of field data only (h, w, d). No manifold parameter enters. Verified for
   all four h=1 imaginary-quadratic fields (D = −3, −4, −7, −11).
2. **E2 CONTINUOUS CHANNEL CLOSED.** B739 character rigidity: the continuous spectrum
   is one channel carrying exactly Λ_K(s−1)/Λ_K(s); no conductor-(4)/(8) Hecke
   character appears anywhere in it.
3. **E3 VOICE EISENSTEIN-ONLY.** B746 F11: zero golden markers across all voice
   artifact files. The voice sits in the being/Eisenstein column.
4. **E4 ZERO OBJECT-SPECIFIC BITS REACH THE CARRIER.** The three non-generic spectral
   quantities (disc −48, palette {1,2,8}, mixing 0.2764) are arithmetic/structural.
   B737 P4 S10(c): "m004-specific bits reaching the SSB-carrying datum: ZERO." B753's
   mixing is gated as PROGRAM-INTERNAL.

Residual: the discrete newform spectrum remains the banked owner-gated door (B746
door 2; B739 "discrete-only" redirect). The kill does not depend on it.

17/17 checks pass. Falsifier: any quantity from the four frozen arcs constituting an
SM value derivable from the solo object.

## Skeptic overrides (2 of 19)

### TOMB-L277: FACE-OPENS → KILL-EXTENDS (skeptic override)

The cell declared FACE-OPENS, claiming the weld-block trace census over the 37 classes
of the 2880 SU(2)₃ image "does not exist in the banked record." The cell computed only
3 words (RL golden; RRL, RLL not golden) and correctly warned that 3 words are not a
census — but stopped instead of running the trivially feasible census.

The skeptic computed the full 37-class census:
- **16/37 classes (43%) have golden-magnitude weld-block trace**
- 1152/2880 elements (40%) are golden-magnitude
- ALL FOUR SU(2)₃-golden classes are in the golden-weld set
- Golden-weld does NOT separate the seed from other golden classes

Additional finding: |tr_weld| is a class function and kernel-invariant (0/5760
magnitude violations), despite the full block varying within classes (311 kernel
violations). The census is well-posed for the magnitude question.

The cell's own opens_spec defined the discriminator: "common → kill extends." 43% is
common. Override to KILL-EXTENDS.

### TOMB-L77: FACE-IRRELEVANT → KILL-EXTENDS (skeptic override)

The cell conflated the Alexander polynomial (t²−3t+1, disc 5, Q(√5)) with the WRT
saddle point at k→∞ (z₀ = exp(iπ/3), disc −3, Q(√−3)). These are different mathematical
objects. The B742 recompute (Part 2, output lines 58-62) explicitly computes: disc = −3,
field Q(√−3).

Corrected Q2 operator:
- F_spec(m004) = Q(√−3) [B737 scattering]
- F_saddle(m004) = Q(√−3) [the regime-2 saddle; z₀ ∈ O_K]
- Intersection: trivially TRUE (same field)

The cell's pillars 2 (Q2 failure) and 3 (number-field disjointness) both tested
Q(√−3) vs Q(√5) and found disjointness — but Q(√5) was the wrong field. The face's
field content enters the expansion's coefficient structure (saddle, volume, sub-leading
3^{−1/4}), confirming the kill: the regime structure is standard, and the spectral face
adds a spectral column confirming it. Override to KILL-EXTENDS.

## Per-target verdict table

| id | ground | kill_form | verdict | skeptic | key spectral mechanism |
|---|---|---|---|---|---|
| B107 | dead-probe | category-error | KILL-EXTENDS | not refuted | palette (1,2,8) / B739 closed continuous channel |
| B285 | dead-probe | value-mismatch | KILL-EXTENDS | — | conductor-4 palette / B739 multiplicity-one |
| B516 | dead-probe | other | FACE-IRRELEVANT | not refuted | no Pisot-spectral theorem exists; face provably disjoint |
| TOMB-L241 | tombstone | category-error | KILL-EXTENDS | not refuted | cusp CM disc −48 / B737 P4 voice-field universality |
| TOMB-L247 | tombstone | kind-mismatch | KILL-EXTENDS | — | eigenphase register replaces trace-value comparison |
| TOMB-L252 | tombstone | value-mismatch | KILL-EXTENDS | — | B739 closed channel / rank question redefined on palette |
| TOMB-L258 | tombstone | other | KILL-EXTENDS | not refuted | falls with K-K/K-L; shared B735 route closes via palette |
| TOMB-L267 | tombstone | category-error | KILL-EXTENDS | — | B734 level-(4) / B739 character rigidity |
| TOMB-L277 | tombstone | base-rate | **KILL-EXTENDS** | **refuted→override** | 43% weld-golden census; not seed-separating |
| TOMB-L30 | tombstone | other | KILL-EXTENDS | not refuted | B739 closed / no k-varying spectral family exists |
| TOMB-L334 | tombstone | finite-level-obstruction | KILL-EXTENDS | — | palette (1,2,8) counts ≠ rep-tower multiplicities |
| TOMB-L339 | tombstone | no-landing-site | KILL-EXTENDS | — | dilation-degree classifier / B737 P4 S10(c) inertness |
| TOMB-L57 | tombstone | value-mismatch | KILL-EXTENDS | not refuted | k_c via HP shapes + B734 level at congruence tower |
| TOMB-L63 | tombstone | category-error | KILL-EXTENDS | — | B739 SU(3)₂ character-rigidity / B734 congruence-subgroup |
| TOMB-L67 | tombstone | category-error | KILL-EXTENDS | — | classical Sym²-vs-quantum eigenvalue dichotomy |
| TOMB-L70 | tombstone | category-error | KILL-EXTENDS | not refuted | disc(t²−κt+1) = 5 ≠ −3; B746 two-column separates |
| TOMB-L77 | tombstone | category-error | **KILL-EXTENDS** | **refuted→override** | saddle z₀ ∈ O_K; face confirms regime via shared Q(√−3) |
| WALL-1 | wall | genericity | KILL-EXTENDS | — | four spectral mechanisms (E1–E4 above) |
| WALL-7 | wall | zero-intertwiner | FACE-IRRELEVANT | not refuted | scattering residue volume-generic; character rigidity TRUE for all; no spectral route to the 27-dim intertwiner |

## Campaign statistics

- Total cells: 19
- Total agents spawned: 29 (19 cells + 10 skeptics; 3 rounds due to credit resets)
- Skeptics run: 10 (of which 2 refuted, 8 confirmed)
- Override rate: 2/19 = 10.5%
- All cells journal-gated (results from `wf_6db1f44f-10f/journal.jsonl`)
- All 19 compute.py deterministic; all 19 output.txt on disk

## Relation to the campaign

P2 is complete. The B′-flagged spectral-face exposure is now closed for all 19
targets. The surviving open channel is the discrete newform spectrum (B746 door 2,
owner-gated), which is NOT in the frozen surface and requires Hejhal-class
machinery beyond the sandbox.

The P3 stratum (depth-exposure items from E22) can now be designed using the P1
kill graph's `depth_reached` field against the current anatomy. This is a separate
campaign arc.

## Artifacts

Each cell's computation and output are under `cells/<id>/compute.py` and
`cells/<id>/output.txt`. Skeptic reports (where run) are at
`cells/<id>/skeptic.txt`. The §16 review is at `reviews/S16_REVIEW_1.md` (sealed
before execution, covers the prereg only; a post-execution review is the banking
seat's responsibility at the PR gate).

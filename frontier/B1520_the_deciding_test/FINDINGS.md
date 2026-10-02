# B1520 — THE DECIDING TEST ON THE BRIDGE'S VACUA: every vacuum of m004's Ballas family keeps a chirality-flipping symmetry that preserves orientation, so no vacuum selects chirality. The geometric mirror is broken at a generic vacuum; the count-odd mirror never is

cc (the SM-derivation seat), 2026-10-02. Sealed at `dda82524` before anything ran on the population (`PREREGISTRATION.md`, sha-256
`5d55ef56…`, SEAL_LEDGER). The run took 16.6 s (route 1), 27.0 s (route 2), 0.9 s (the follow-up) and under a second (the read-out).
**Verdict: NEGATIVE — outcome A, the registered kill.** All six predictions came true (P1–P6); the priors expected 5.6 of 6. Post-run
checks pass (§4): a third route at rational points, the witness against the audit lane's R47 F14, the twist, and the stabiliser of
each kind of vacuum. **Prior work: RE-DERIVED** (§6). **0 of 19 stays 0.**

## 0. What was found

- **Outcome A.** Every vacuum μ ⊗ ρ_q (q > 0, μ ∈ ℂ*) of the bridge on m004's Ballas family is fixed, up to isomorphism, by a
  count-odd map. There are two such witnesses, D.θ and D.sθ (θ inverts both generators, s swaps them, D dualises). Both keep
  orientation, and both have twist exponent e = +1, so each fixes every vacuum for every μ.
- **So no vacuum carries a count.** Lemma L3 gives I = 0 at every vacuum. By Lemma G, the witness lifts to an E8 gauge rotation
  composed with an isometry that keeps orientation, so every vacuum keeps a charge conjugation of the 4d SU(5), under the fences
  of §5.
- **The handoff's question, answered in its two senses.**
  - *Is the potential mirror-symmetric?* Yes, under all sixteen maps (Lemma P, proved at the seal).
  - *Is the minimum mirror-symmetric, for the count-odd mirror?* Yes, at every vacuum. This is the registered kill.
  - *Is the minimum mirror-symmetric, for the geometric mirror (orientation reversal)?* At a generic vacuum (q ≠ 1, μ ≠ ±1), no.
    No orientation-reversing map, bare or dualised, fixes it (§4, X4: the stabiliser is {id, s, D.θ, D.sθ}).
  - So the bridge does have *"a mirror-symmetric potential whose minima are not mirror-symmetric"* in the geometric sense. But
    the broken mirror is the wrong one. A bare map keeps the count (L1), and the count-flipping maps are unbroken everywhere.
    Parity breaks; chirality is not selected.
- **The chiral configurations come in count-flipped pairs over each vacuum.** At q₀ = 17 ± 12√2 with μ = −1, the non-split
  extension W₁ has I = −1. Its eight bare images all have I = −1 and its eight dualised images all have I = +1, at all three primes
  and both roots. The potential lifts both members of a pair equally (R76: a t² + c t⁴, lowest at the split limit).

## Seen first (the repo sweep and the literature)

**The repo sweep**, before the seal (PREREGISTRATION §0, the PRIOR ART section).
- `scripts/checks/prior_work.py` ran on ten terms after a fresh `git fetch --all`. The heads and shas are in `arc_verdict.json`
  (`prior_work`): main `12ed66bd`, the audit lane `1e3d17b9`, this branch `27220af6`, and the seat lanes `0043be2b` and `e5f1aebf`
  (neither merged).
- "count-odd" occurs only in main's B1455 PREREGISTRATION, this seat's B1519 FINDINGS and one unrelated B774 data file.
- Main's `topic_sweep.py`, run from a checkout of main: *100 of 1327 arcs on main match (NEGATIVE 14, OPEN 11, PROVED 74, RETRACTED
  1); 7 other lanes match*.
- Read in full: the handoff and its script; main's B1455 PREREGISTRATION; the audit lane's selection-rule intake (`9b566262`), its
  R77 relay, its act-and-register design (`69d6d0b9`) and milestone (`1e3d17b9`); R47's F14 and R76; this seat's B1512 and B1509's
  index instrument.

**What the sweep found that this arc must not present as new.**
- This seat's B1512 (2026-10-01) holds the four lemmas that decide most of the outcome, each with an explicit intertwiner:
  - ι fixes ρ_q;
  - ε and α pair q with 1/q;
  - ρ_q* ≅ ρ_{1/q}.
- The audit lane's R47 F14 (2026-09-25) holds the witness itself: an explicit J(q) with ρ(g)^{−T}J = Jρ(θg), invertible at every
  q > 0. Read through duality, that is "D.θ fixes ρ_q".
- Main's B1455 asks this exact question and is sealed and not run. The audit lane states: *"Main B1455 is not duplicated."*
- The arc is therefore an independent run of a question already posed, with an outcome largely decided by the record. The seal
  said so.

**The literature** (read before the seal; locations in PREREGISTRATION §0).
- S. A. Ballas, *Finite volume properly convex deformations of the figure-eight knot*, arXiv:1403.3314v3. Read: the family on
  p. 17; ρ_{1/2} hyperbolic and the ρ_s pairwise non-conjugate on p. 2.
- Skolem–Noether (Theorem T's last step).
- Mostow–Prasad: Out(π₁M) ≅ Isom(M).
- Corlette and the equivariant cutoff, as R76 cites them (not re-derived here).

## 1. The question (PREREGISTRATION §1–§2)

The handoff (§4, verbatim): *"Does the physical bridge's action have a mirror-symmetric potential whose minima are NOT
mirror-symmetric? … Kill condition, registered now: if EVERY minimum is θ-fixed up to gauge, the vacuum does not select, and
chirality is an input here exactly as in the SM. That is a NEGATIVE and must be banked as one."*

Made exact in main's class-index terms:
- **The vacua** (hypothesis H-vac, from R44, R54 and R76): the flat bundles μ ⊗ ρ_q (q > 0, μ ∈ ℂ*) with their harmonic metrics,
  and at the exceptional points their split sums with trivial lines.
- **The maps.** Sixteen maps Φ = (σ, d): σ runs over the eight classes of Out(π₁ m004) = D4, and d = 1 dualises.
  - The orientation-keeping classes are V = {id, θ, s, sθ}; the reversing ones are τV, with τ: m ↦ m, n ↦ nmn⁻¹.
  - The count-odd maps are the eight with d = 1. L1 (B1512) says I(σ*V) = I(V); L2 says I(V*) = −I(V).
- **The test.** Is every vacuum fixed by some count-odd map?

## 2. The run (`route_intertwiner.py`, `route_traceform.py`, `followup_index.py`, `decide.py`)

| σ | orientation | on H₁ | σ on the family (det X of route 1's generator) | D.σ on the family (det X) | e for σ, D.σ |
|---|---|---|---|---|---|
| id | kept | +1 | fixes (1) | pairs (−16q(q²+q+1)) | +1, −1 |
| θ | kept | −1 | pairs (q²) | **fixes** (−16q³(q²+q+1)) | −1, **+1** |
| s | kept | +1 | fixes (16q²) | pairs (−16q³(q²+q+1)) | +1, −1 |
| sθ | kept | −1 | pairs (16) | **fixes** (−16q(q²+q+1)) | −1, **+1** |
| τ | reversed | +1 | pairs (−16q³) | fixes (16q⁶(q²+q+1)) | +1, −1 |
| τθ | reversed | −1 | fixes (−16q) | pairs (16q⁴(q²+q+1)) | −1, +1 |
| τs | reversed | +1 | pairs (−16q) | fixes (16q⁴(q²+q+1)) | +1, −1 |
| τsθ | reversed | −1 | fixes (−16q³) | pairs (16q⁶(q²+q+1)) | −1, +1 |

How to read the table:
- "Fixes" means Φ(ρ_q) ≅ ρ_q for every q > 0. "Pairs" means Φ(ρ_q) ≅ ρ_{1/q} for every q > 0, and Φ(ρ_q) ≅ ρ_q exactly at q = 1.
- e is the exponent of the twist, Φ(μ ⊗ ρ_q) = μ^e ⊗ Φ(ρ_q).
- No determinant has a positive root, so every isomorphism holds at every q > 0.

**Route 1** solves the intertwiner equations exactly over ℚ(q). Each of the 32 pairs has a space of dimension 1 or 0. Every
generator was verified by substitution, and controls C1–C10 passed, the two banked identities among them.

**Route 2** (Theorem T) reads all 768 traces equal for exactly the sixteen pairs that route 1 found isomorphic. The other sixteen
are conjugate exactly at q = 1: the gcd of their 768 trace differences has no other positive root. The Gram determinant of the
sixteen-word basis has all coefficients positive. Controls C1–C7 passed.

**The routes agree on all 32 decisions.**

**The follow-up.** I(W₁) = −1 at all six prime–root pairs (B1509's banked value), I(σ*W₁) = −1 for all eight bare maps and
I((σ*W₁)*) = +1 for all eight dualised ones. Every image satisfies the relator.

**The read-out** (`decide.json`):
- every control and banked identity passed;
- no map leaves the family;
- the count-odd maps that fix every vacuum and every twist are D.θ and D.sθ, both orientation-keeping;
- registered outcome **A**.

## 3. The predictions, read (scored mechanically by `decide.py`)

| | prediction | prior | read |
|---|---|---|---|
| P1 | the routes agree on all 32 decisions | 97% | **YES** |
| P2 | ρ_q* ≅ ρ_{1/q}, and ρ_q* ≅ ρ_q exactly at q = 1 | 98% | **YES** (route 2's locus: ["1"]) |
| P3 | no map leaves the family | 95% | **YES** |
| P4 | eight of sixteen fix every q; bare 4 + 4; bare reversing 2 + 2 | 85% | **YES** |
| P5 | outcome A with witness D.θ, banked NEGATIVE | 93% | **YES** (D.θ and D.sθ) |
| P6 | I(W₁) = −1; bare images −1, dualised +1, at all six pairs | 95% | **YES** |

Six of six came true, against an expected 5.6. The priors were informed by B1512 and R47, which were read before the seal. This was
a verification, and the score says so; it is not a test of foresight.

## 4. Post-run checks (`verification/post_run_check.py` → `post_run_check.json`, 3.8 s; written after the run, not predictions)

The outcome is a NEGATIVE, and the owner's rule is that a negative must not come from a bug. So it was checked by means that share
no code with either route or with B1512.

- **X1, a third route.** At q = 1/3, 1/2, 5/7, 1, 7/5, 2 and 3, the intertwiner system was solved for all sixteen maps and both
  targets. It uses only own exact Fraction arithmetic: no sympy, no traces. **All 224 decisions are as sealed.**
- **X2, the witness against R47's J.** F14's J(q) (section 1 of its FINDINGS, read from the audit lane at `1e3d17b9`) satisfies
  MᵀJ = JM, NᵀJ = JN and F14's determinant formula exactly at all seven points. D.θ's intertwiner X satisfies XJ = λI with λ ≠ 0
  at each, so the two benches found the same map.
- **X3, the twist, computed.** At q = 2 and 1/3, μ = 3, −2 and 5/7, each of the eight maps that fix q sends μ ⊗ ρ_q to μ^e ⊗ ρ_q
  and not to the other. **All 48 cases are as Lemma Tw says.**
- **X4, the stabiliser of a vacuum.** Solved directly over all sixteen maps; each row is as the table and Lemma Tw predict.

| vacuum | stabiliser | order | orientation-reversing members | count-odd members |
|---|---|---|---|---|
| generic: (q, μ) = (2, 3), (1/3, −2) | id, s, D.θ, D.sθ | 4 | **none** | D.θ, D.sθ |
| μ = −1, q = 2 | adds τθ, τsθ, D.τ, D.τs | 8 | four | D.θ, D.sθ, D.τ, D.τs |
| q = 1, μ = 3 | adds τ, τs, D.τθ, D.τsθ | 8 | four | D.θ, D.sθ, D.τθ, D.τsθ |
| q = 1, μ = −1 | all sixteen | 16 | eight | eight |

Observations, not tests:
- Route 1's normalised determinants include B1512's three, 16q² (s), −16q³ (τ) and −16q(q²+q+1) (duality). This is consistent with
  s and τ being B1512's ι and α up to an inner automorphism. That identification was not tested here.
- D.θ's determinant is −16q³(q²+q+1). Its ratio to 1/det J is [q(q²+q+1)/(q+1)]⁴, a fourth power, as a one-dimensional space
  requires.

## 5. What it means, and what it does not

**What it says.**
- On the one family where the record has a finite-energy vacuum action, no vacuum can select chirality.
- The potential's minima break the geometric mirror at a generic point. But every minimum keeps two chirality-flipping symmetries
  that preserve orientation (D.θ and D.sθ), so every minimum has I = 0.
- In the E8 frame (Lemma G), each minimum keeps a charge conjugation of the 4d SU(5), and its 4d spectrum is vector-like in every
  SU(5) representation.
- The chiral configurations, the non-split extensions, are not vacua. They come in count-flipped pairs over the same vacuum, and
  the potential lifts both equally.
- In the handoff's words: *"the vacuum does not select, and chirality is an input here exactly as in the SM."*

**The distinction the handoff's word "mirror" hides.**
- A geometric mirror (orientation reversal) is a bare map and keeps the count (L1). So a pair of vacua it exchanges, q and 1/q,
  carries equal counts: both zero, since D.θ fixes each.
- The maps that flip the count are the dualised ones. Among them, the orientation-preserving D.θ and D.sθ are unbroken at every
  vacuum.
- A selection rule for chirality would need a minimum that breaks every count-odd map. On this family none does.

**What it does not say** (the scope, recorded in the verdict and the kill graph).
- Frame: F-HE in main's class-index terms. Object: m004's Ballas family at level one, with central twists. Reach: one family.
- Hypotheses: H-vac (R44, R54, R76) and the uniqueness of the harmonic metric (R47's F13, as R47 cites it).
- It does not cover R77's added sources and free profiles, non-flat backgrounds, other components of m004's character variety,
  other manifolds' families, or levels above one.
- Lemma G's reading also needs the end conditions to be σ-invariant (GENESIS GAP2), and the spinor and domain transport the audit
  lane asks for is not done.
- An end law, source or profile that is not invariant under θ (and sθ) would break the witness. That is the hatch.
- It does not say that chirality must be an input everywhere, and it gives no evidence for the handoff's rule. The handoff's 8 of 8
  restates theorems on record, as the handoff itself says.

## 6. Prior work

**Standing: RE-DERIVED.** The main result is decided by B1512's lemmas and R47's F14 through the homomorphism argument, and own code
in three routes agrees with them. What the arc adds:
- the complete action of all sixteen maps, with exact loci;
- the stabiliser of every kind of vacuum, including the generic breaking of every orientation-reversing map;
- the follow-up index on all sixteen images of W₁;
- the E8 lift (Lemma G) with its orientation fence.

Under B1214's rule this is a verification and a sealed-cell decision, not a new law, so **creates_law is false**. Main's B1455 can
run blind if main wishes: its question is answered here, and its P1 is false (below).

## 7. Errors caught, and disclosures

- **A route-1 design fault, fixed before the seal** (ERROR_LEDGER, E52 instance). A generator with det X ≡ 0 would have been read
  as an isomorphism. Control C7 catches it; the old logic was re-run on C7 and returns True there.
- **Main's B1455 P1 is false.** Of the eight maps (m, n) ↦ (m^a, n^b), (n^a, m^b), only the four with a = b satisfy the relator,
  and all four keep orientation (`symmetries.json`). Main is told in this arc's relay.
- **Two heads moved during the design.** The audit lane went to `1e3d17b9`, and a new seat lane appeared at `e5f1aebf`. Both were
  read before the seal; neither duplicates the test.
- **Proved, not computed.** Lemma P (the potential's invariance), L3 and Lemma G are proofs at the seal. The arc computes the
  stabilisers, the follow-up and the lift's two root-system facts (`lift_e8.py`), not the bienergy itself.

## 8. Leads (registered, not run; each would be sealed before computing)

1. **The source and end test.** Is there an admissible source or end law (R77's full-current construction, a GENESIS GAP2 end
   condition) that is not θ- and sθ-invariant, and what does it do to the vacuum stabiliser? This is the hatch, made into a
   question.
2. **Other families.** The same sixteen-map test on another component of m004's character variety at level one, or on the cyclic
   levels' families (B1511's projective tower), where the outer group is larger.
3. **The narrowed reader arc** (B1519 §4, the owner's to run). With the vacuum ruled out as a selector on this family, the
   remaining place for a choice is the law or the state, not the minimum.

I-26 stays UNEARNED. 0 of 19.

## Verification

```
cd frontier/B1520_the_deciding_test/verification
sha256sum -c ../ARTIFACT_HASHES.txt        # from frontier/B1520_the_deciding_test/ (the sealed files)
python3 route_intertwiner.py               # route 1, ~17 s
python3 route_traceform.py                 # route 2, ~27 s
python3 followup_index.py                  # ~1 s
python3 decide.py                          # the read-out
python3 post_run_check.py                  # X1-X4, ~4 s
python3 -m pytest -q tests/test_b1520_the_deciding_test.py    # from the repository root
```

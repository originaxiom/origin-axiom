# B1535 — THE CAP: at a finite-order member of sm:B1515's frame on any finite cover, the 5̄′ count is at most n(ν³ ⊗ ρ) and the 10̄′ count at most b0 + n(ν⁴), at every class and in either order; read at 776 classes of the silver squares' covers and on the line's supply over 541 states, it holds everywhere

cc (the SM-derivation seat), 2026-10-04. Sealed at `b410afeb` before any outcome was read (`PREREGISTRATION.md`, sha-256
`c0803c0c…`, SEAL_LEDGER).
- **The run.**
  - **The banked identity** held at `4e55f20b` (03:26Z): `controls.py --rerun` reproduced `controls.json` in every field but
    the timings, K1 still read all 144 of sm:B1534's terms as held, and all 17 sealed files hashed as sealed
    (`identity.json`).
  - **Part W** (`part_w.py`) ran from 03:27:21Z for 5,149 s and was recorded at `536dfba1`.
  - **Part M** (`part_m.py`) ran from 03:27:20Z for 7,949 s, finishing at 05:39:57Z: 776 readings, each in route RS at two
    primes, and the 140 mixed classes on the order-2 covers also in route Ind (exact).
  - **The read-out** (`read_out.py`) ran once, as sealed, on the complete records (`read_out.json`, `read_out_log.txt`).
- **Verdict: PROVED** (the seal's §9: P2, P3 and P8 hold).
  - **Theorem C holds at every one of the 776 readings**, in every route: its identities, its assembly and both caps. The
    routes agree on every quantity at every class.
  - **Lemma W holds on all 541 states.** The line has no interior class at any character read: 567,996 characters in route X
    and 41,724 in route S, and n ≠ 0 at none.
  - **No class carries more than one generation.** The only generation-shaped count is (−1, −1), at 36 readings: 24
    pulled-back classes (the base's one generation), 4 pure classes at χ₀ ≠ 1 on m135, and 8 generic mixed classes on m136.
    Two or more never occurs (P4).
- **As sealed: 7 of 9 predictions held** (P1, P2, P3, P4, P7, P8, P9). P5 and P6 failed. The priors expected 7.81.
  - **P5 (mixing adds no new value) fails.** 144 mixed readings take values that no pure class takes at the same (ν, B):
    (2, −2) on m135's covers of order 4 and 8; (3, 0), (1, −1), (1, 0) and (0, 0) at cancellation classes; (0, −1) and
    (0, −2) on m136's covers. All lie inside the caps.
  - **P6 (the two generic mixed classes read alike) fails at one of 102 pairs**: m136 at ν = (½, 0; ½) on a cover of order 4.
    There the first class reads (0, −1) with rk δ¹((Λ²W₁)*) = 3 and the second (0, −2) with rank 4, at both primes. The
    generic class has the larger rank (lower semicontinuity), so the first is a special class: Part M's coefficients came
    from a hash in {1, …, 97}, small enough to land on a special locus. **Checked after the run (disclosed):** sm:B1536's
    control K3 read the full class space of all 102 pairs in its two routes (FLINT and PARI, primes near 2²⁴ and 2³¹), two
    classes each with coefficients uniform in GF(p). At this pair all four read (0, −2) with rank 4. At every other pair all
    four equal both banked readings in count, k and every connecting rank.
- **What it is, and what it is not** (§5). It answers the owner's "are u sure about the math behind your negative
  conclusions about three generatiosn, sure sure sure?" with a mechanism.
  - In this frame a count of g generations needs both supplies, n(ν³ ⊗ ρ) ≥ g and b0 + n(ν⁴) ≥ g, at every class.
  - The line's supply is zero on every word state and level, and on their abelian covers at puncture-trivial characters
    (Lemma W). That is why sm:B1532 and sm:B1534 found at most one generation.
  - It says nothing about:
    - the covers' own characters, where n(ν⁴) can be non-zero (item 15);
    - non-abelian covers, where both supplies can grow (sm:B1536 reads the first ones);
    - non-unitary characters, or anything off the hyperbolic point;
    - which state or cover is physical.
  **0 of 19 stays 0.**

## 0. What was found

**Part M** (`read_out.json`; route RS at the first prime, equal at the second and in route Ind wherever read). A reading is
(I(W₁), I(Λ²W₁)) at a pulled-back member ν of m135 or m136 (κ = ±1), on the finite abelian cover cut out by B, at a class of
the cover.

| class | readings | values |
|---|---|---|
| pulled back (pure at χ = 1) | 130 | as sm:B1534's banked sums |
| pure at one χ₀ ≠ 1 | 302 | as sm:B1534's banked sums (Lemma R) |
| mixed: generic (two per pair) | 204 | (1, 0), (0, −1), (0, 0), (2, −2), (0, −2), (−1, −2), (−1, −1), (3, 0) |
| mixed: interior | 32 | (−1, −2) |
| mixed: interior plus generic | 56 | (2, −2), (0, −1), (0, 0), (0, −2), (−1, −2), (1, 0) |
| mixed: cancellation (Lemma F) | 52 | (0, 0), (1, −1), (3, 0), (1, 0) |

- **All 776 readings:** (1, 0) × 162, (0, 0) × 148, (0, −2) × 117, (−1, −2) × 108, (0, −1) × 69, (2, −2) × 48, (3, 0) × 48,
  (−1, −1) × 36, (5, 0) × 32, (1, −1) × 8.
- **The covers:** 102 pairs (ν, B) at 14 members; 260 readings on covers of order 2, 360 of order 4, 156 of order 8.
- **The caps at work.** b0 = 1 and n(ν⁴) = 0 at every reading, so capW = 1 and every W count is ≥ −1. capL2 = n(ν³ ⊗ ρ*) is
  0, 1 or 2 (232, 156 and 388 readings), so every Λ² count is ≥ −2. The 5̄′ cap is attained at 377 readings and the 10̄′
  cap at 144.
- **P9:** at m135's u₁ on the cover ⟨(½, ½)⟩ a generic mixed class reads I(Λ²W₁) = −2, the cap attained.
- **P7:** every cancellation class vanishes on at least one cover cusp in route RS (Lemma F).

**Part W** (`part_w.json`, recorded at `536dfba1`). Lemma W's census on sm:B1529's 541 rows: the 536 word states to length 12
and m004's levels M₂–M₆. Route X (the census presentation, 30 digits) read every φ-fixed torsion character u at every
κ ∈ μ₁₂, 567,996 characters; route S (SnapPy's presentation and peripheral curves) read every character of H₁ of order
dividing 12, 41,724. Neither finds n ≠ 0; μ_u = τ_u at every u ≠ 0, and the order-12 counts agree. The margins: the smallest
kept singular value is 0.0112 (X) and 0.0302 (S), the largest dropped below 10⁻²⁷.

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The sweep was `git fetch --all`, then
`scripts/checks/prior_work.py` and `git grep` on every head with thirteen terms. No head bounds the frame's counts by the
supplies. The literature at the seal: Bart–Scannell, Monroe (arXiv:2604.22004 §6.1, for Garland–Raghunathan's PH¹ = 0 on
every non-uniform lattice) and Menal-Ferrer–Porti, as the seal records.

**Refreshed at banking** (2026-10-04, after `git fetch --all`). Main moved to `39775d66`: S53 (B1470, B1418's unrun modules
of t12835 run; no three, maximum |I| = 2, main's own frame) and the B1471 seal (amphichiral cancellation of the twisted
Alexander function). The other heads are as at the seal. The sweep ran again with twelve post-run terms: "Theorem C", "the
cap", "interior supply", "cuspidal supply", "mixed class", "Garland", "Raghunathan", "Lemma W", "puncture-trivial", "line
supply", "special class", "hashed coefficients".
- **"Theorem C" and "the cap":** many arcs on every head use the words for their own theorems; none bounds this frame's
  counts by n(ν³ ⊗ ρ) and b0 + n(ν⁴). This seat's own hits are this arc, its relay and sm:B1532's FINDINGS.
- **"interior supply", "cuspidal supply", "puncture-trivial", "Lemma W" (as this arc's lemma):** this seat only (this arc,
  its relay, sm:B1532's FINDINGS, the kill graph's B1532 record).
- **"mixed class":** on main, B370 (Massey products) and two scripts using the words otherwise. None bears.
- **"Garland" and "Raghunathan":** this seat's records of this arc and sm:B1529, sm:B1530 and sm:B1513; main's B1453 reader
  of sm:B1515 (Remark 9, cited, not used); and the audit lane's R27 note (`FINITE_TWIST_PRIOR.md`), which reads
  Menal-Ferrer–Porti in full for finite-character transfer. None states the cap.
- **"special class":** sm:B1534's pencils (the special class s = ∓√2/30) and its surfaces. "line supply" is absent; "hashed
  coefficients" is this arc's `part_m.py` only.

**The literature.** At banking nothing more was needed. The reading uses no external result beyond the seal's:
Garland–Raghunathan through Monroe §6.1 (PH¹(Γ; so(3, 1)) = 0 for every non-uniform lattice), Bart–Scannell (the four's
cuspidal cohomology) and Menal-Ferrer–Porti (sm:B1515's Lemma 3).

## 1. The run (as sealed)

- **The identity** (§8) ran at 03:26Z and held: `identity.json` (`controls differences: 0`, `k1 holds (144 terms)`, 17
  sealed files, no mismatch). It was recorded at `4e55f20b` before either run read anything.
- **Part W** read its 541 rows from 03:27:21Z in 5,149 s (`part_w.json`, `part_w_rows.json`, committed at `536dfba1`).
- **Part M** read its 776 classes from 03:27:20Z in 7,949 s (`part_m_log.txt`; the rows are kept compressed as
  `part_m.jsonl.gz`, with their sha-256 before compression in `part_m_sha256.txt`). Every reading carries Theorem C's checks
  in every route, and route RS reads the cover's own cusps.
- **The read-out** ran once on the complete records, at 05:40:36Z. Nothing was re-run.

## 2. The theorems (as sealed)

- **Lemma E′** (the index of an extension from its connecting maps), proved at design time.
- **Theorem C (the cap).** At a finite-order ν and any class c ≠ 0 on any finite cover N of a complete finite-volume hyperbolic
  3-manifold:
  - I(Λ²W₁) = −dim(im δ¹ ∩ K) ∈ [−n(ν³ ⊗ ρ), 0];
  - I(W₁) ≥ −b0 − n(ν⁴), with b0 = [ν⁴ = 1];
  - so g generations, in either order, need n(ν³ ⊗ ρ) ≥ g and b0 + n(ν⁴) ≥ g.
  The ingredients are sm:B1515's Lemmas 2 and 3, sm:B1530's Lemma T (the torus table), Lemma E′, and Garland–Raghunathan on
  the finite cover ker ν² (step (c2): Λ_A ∩ π_A = 0). The proof holds term by term for twisted terms (the Remark).
- **Lemma W.** On a once-punctured-torus bundle with Anosov monodromy, or a finite abelian cover of one, a finite-order
  character trivial on every puncture loop of the fibre has no interior class.
- **Corollaries.**
  - **C1** (sL-10 item 14, first half): on every finite abelian cover of m135 or m136, at every pulled-back member at every
    twist and every class of the cover, in either order, the count is at most one generation and the 5̄′ count at most 2.
  - **C2:** on every word state and level, at every finite-order member and class, at most one generation, and one only where
    ν⁴ = 1 and n(ν ⊗ ρ) ≥ 1.
  - **C3:** a count of g ≥ 2 needs n(ν⁴) ≥ g − b0 and n(ν³ ⊗ ρ) ≥ g. Three places remain: puncture characters on abelian
    covers of word states (|D| ≥ 2), non-abelian covers, and non-unitary characters on covers with two or more cusps.
- **What the run supplies.** The theorem is proved at design time; the run tests it where it could fail: at mixed classes
  (which no earlier arc read) and on Lemma W's population. A violation in both routes would have withdrawn it.
- **A blind test, disclosed at the seal.** Theorem C's prediction for sm:B1532 was committed at `5c6a4225` before that arc's
  read-out, and holds at all 163,507 readings of each of its routes (`check_b1532.json`).

## 3. The predictions

| | prediction | prior | read |
|---|---|---|---|
| P1 | every pure class reads sm:B1534's banked sum, at both primes | 97% | held: 432 of 432 |
| P2 | Theorem C's identities and the cap at every reading, every route | 93% | held: 776 of 776 |
| P3 | the routes agree at every class on every quantity | 95% | held: both primes everywhere; route Ind at the 140 mixed classes on order-2 covers |
| P4 | no reading is two or more generations | 97% | held: the only generation-shaped value is (−1, −1) |
| P5 | mixing adds no new value | 50% | failed: 144 mixed readings take values no pure class takes at the same (ν, B) |
| P6 | the two generic mixed classes read alike at every (ν, B) | 92% | failed at one pair of 102 (a special class, §0) |
| P7 | every cancellation class vanishes on at least one cover cusp | 90% | held: 52 of 52 |
| P8 | Lemma W's census | 97% | held: 541 rows, both routes |
| P9 | a generic mixed class at m135's u₁ on ⟨(½, ½)⟩ attains −2 | 70% | held |

Seven of nine held; the priors expected 7.81.

## 4. Post-run check: the special class at P6 (written after the run; disclosed)

sm:B1536's control K3 (`frontier/B1536_the_finite_covers/verification/control_k3.py`, `k3.json`) was written before this
read-out, as a control on banked data for that arc. On a partial record it compared its two routes' generic classes with
both of Part M's. After this read-out showed P6's failure, its comparison was changed: the routes' draws are now compared with
the banked reading of largest connecting ranks, and pairs whose two banked draws differ are listed. That arc's §6 records the
change. On the complete record:
- 328 pure readings ('the class' and 'c_int') agree in count and k with Part M, in both routes.
- At all 102 pairs, both routes' two draws (coefficients uniform in GF(p), p = 16,776,961 for FLINT and 2,147,482,921 for
  PARI) read the banked reading of largest ranks, in count, k and every connecting rank.
- The one pair whose banked draws differ is P6's: m136, ν = (½, 0; ½), order 4. The banked draws are (0, −1) with rank 3 and
  (0, −2) with rank 4; all four new draws read (0, −2) with rank 4.

So P6 failed because one fixed-coefficient class is special, not because the routes or the theorem erred.

## 5. What the reading means

- **For the owner's question.** The negatives of sm:B1532 and sm:B1534 are not accidents of the census. In this frame the
  10̄′ count is capped by b0 + n(ν⁴), and the line has no interior class on any word state, level, or abelian cover of
  one at puncture-trivial characters. So at most one generation, at every class, before any census is read. The run tested
  this at the classes no earlier arc read (mixed) and found it held at every one.
- **Where more than one could live** (C3). Only where both supplies grow:
  - the covers' own characters on fibre-direction covers (item 15);
  - non-abelian covers, where the four's cuspidal cohomology grows by bending (Bart–Scannell; Long through them) and the
    line's can grow too. sm:B1536 reads the first ones: every connected cover of degree ≤ 12 of m004 and m003, and their Q₈
    towers;
  - non-unitary characters on covers with several cusps.
- **The 10̄′-only counts.** (3, 0) and (5, 0) are within the caps (the cap bounds −I(W), not +I(W)) and are anomalous: no
  5̄′ pairs them.
- **Not:** selection, a held vacuum (R76), anything off the hyperbolic point, I-26 or the experiential question.
  **0 of 19 stays 0.**

## 6. Prior work and standing

**EXTENDS.** sm:B1515's frame and its lemmas, sm:B1527's Lemma E and sm:B1530's Lemma T are combined with Garland–Raghunathan
(through Monroe) into a cap on both sides of the frame's count. sm:B1532's Lemma S and sm:B1534's terms are the tested
ground. The bound of the frame's counts by the two supplies is new as swept (§ Seen first).

## 7. Errors in this arc, and the record

- **At the seal:** three pre-seal slips, logged then (ERROR_LEDGER): a twist placed before the wedge in a checker's draft, a
  banked table recalled as uniform in the prediction note's draft, and an inverted character in `part_m.py`'s draft (Lemma F).
- **At banking:** P6's special class (§4) is a design weakness, not an error of computation: classes meant to be generic
  were drawn with small coefficients. Logged in ERROR_LEDGER. sm:B1536 draws its classes with coefficients uniform in GF(p)
  and reads Lemma G's bounds from each rank's larger value over two draws.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`, `PREDICTION_FOR_B1532.md` (the blind prediction, `5c6a4225`).
- `verification/`: `cap_lib.py`, `mixed_lib.py`, `rs_lib.py`, `part_m.py`, `part_w.py`, `read_out.py`, `controls.py`,
  `control_k1.py`, `check_b1532.py`, `identity.py`; records `controls.json`, `controls_rerun.json`, `k1.json`, `k1_log.txt`,
  `identity.json`, `check_b1532.json`, `part_w.json`, `part_w_rows.json`, `part_m.jsonl.gz`, `part_m_sha256.txt`,
  `part_m_log.txt`, `read_out.json`, `read_out_log.txt`.
- `arc_verdict.json`; the lock `tests/test_b1535_the_cap.py`.

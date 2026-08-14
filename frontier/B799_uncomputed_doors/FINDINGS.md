# B799 — the twelve uncomputed doors resolved (Compaction W0)

**Prereg `3243c1c219ea7ca0`, sealed and committed at `56df99cc` BEFORE any computation.**
cc banking seat, 2026-07-29. Mathematics and repository quality only — **no physics reading,
nothing to `CLAIMS.md`.**

## The result against the pre-stated expectation

| outcome | pre-stated | actual |
|---|---|---|
| COMPUTED | ~3 | **2** |
| IN-REPO-CITED | 4–5 | **5** |
| HONEST-DOWNGRADE | 4–5 | **5** |
| COMPUTED-OVERTURNS | 0–1 | **0** |

All twelve dispositioned. The prereg's declared **warning sign did not fire**: it stated that an
all-COMPUTED/IN-REPO-CITED outcome would mean the compiler's `fact_computed: false` flag carried no
information. **Five honest downgrades survive, so the flag is real** — B738 classified these
correctly, and that is itself a result about the compiler's reliability.

## COMPUTED (2) — the discriminating fact computed here, in exact arithmetic

**B332 — the founding letters' deck element.** `g = −R·L⁻¹ = [[0,−1],[1,−1]]`, trace −1, det 1,
char poly `x²+x+1`, **order 3**, eigenvalues the primitive cube roots — **elliptic**. The bundle's
monodromy `A = [[1,1],[1,0]]` has trace 1, det −1, **`det(A − I) = −1`** (the prereg's named fact),
eigenvalues `φ` and `1−φ`, real with `|φ| > 1` — **hyperbolic**. A finite-order elliptic element
cannot be the monodromy of a hyperbolic mapping torus, so **`g` is not the generation-cycling deck
element. The closure stands.**

**W7-rebase — does the E₆ centre split the 27?** Computed from the Cartan matrix rather than cited:
`det C(E₆) = 3`, Smith normal form `[1,1,1,1,1,3]`, so `P/Q = Z(E₆) = ℤ/3` cyclic. The **27**'s
highest-weight class has order exactly **3**, so the centre acts by a primitive cube root of unity.
A scalar has a **single** eigenvalue on the whole 27 (multiplicity 27, verified), hence **no
invariant splitting** — the naive ℤ/3 triality cannot produce a 3+2 generation split. **Closure
stands.**

Both are mutation-verified: making `A` parabolic, or mis-wiring the E₆ Dynkin diagram, turns the
corresponding lock red.

## IN-REPO-CITED (5) — and the citation was *executed*, not trusted

The prereg made this the criterion that can fail: IN-REPO-CITED is granted **only** if the cited
arc's lock is run and observed to pass *in this arc's run*. All five were run:

| door | cited arc | lock | result |
|---|---|---|---|
| B412 | B408 | `tests/test_b408_seam_hierarchy.py` | 3 passed |
| B433 | B426 | `tests/test_b426_scale_lever.py` | 5 passed |
| B435 | B437 | `tests/test_b437_abelian_book.py` | 3 passed |
| B668 | B662 | `tests/test_b662_wave1.py` | 5 passed |
| B731 | B734 | `tests/test_b734_m004_congruence.py` | 2 passed |

`tests/test_b799_doors.py` keeps this honest over time: it asserts every cited arc **and lock still
exists**, and re-runs them, so the disposition cannot decay back into a bare citation.

**B731 carries an extra finding: the record is stale, not merely uncomputed.** Its kill was already
**retracted** by B734 under error class **E22**, and its `revival_score` of **10 — the corpus
maximum** — is obsolete bookkeeping for a door that has already reopened. Flagged for correction in
the source record.

## HONEST-DOWNGRADE (5) — relabelled uncomputed, with the reason

**B140.** The genus-general leg's discriminating fact is a **standard published theorem** (mirror:
same volume, opposite Chern–Simons, conjugate trace field), correctly cited and verified only
instance-wise. Citing standard mathematics is legitimate; it is still not an in-sandbox computation,
so the flag is **accurate and stays**. Its *other* leg — retracting the never-banked "~35
non-principal φ-fixed points carry ℚ(√−3)" — **is** computed and locked (the content is ℚ, tighter
than ℚ(√−3)).

**B579.** The kill is a **proxy**: it rests on the seat's own five failed derivations, and a failed
derivation is not a proof of underivability. What is computed and locked stays (the `T(F)` char-poly
correction `x⁴−2x³−5x²−4x−1`; the θ-odd sequence {1,3,8,17}); the values-scan kill itself is
relabelled uncomputed.

**B685.** The GSWZ integrality fact (coefficients integral away from 3, `(q−1)¹⁰⁰` denominator
`3¹⁴⁶`) was **re-read from the source, not recomputed** — and the arc itself flags that this is the
same kind of read which produced the B682 misreading it corrects. An in-sandbox Habiro recomputation
was **not attempted here**; it is tractable in principle, so per the prereg it is **not** marked
`NEEDS-SPECIALIST`. **Registered as the highest-value remaining recompute in this batch.**

**B720.** Three NO-MATCH classifications about *other* frameworks (mixed-Tate over ℤ[i]; 3d gravity
has no local DOF; ABHY finite-type). Independently re-verified by source fetch, but **not in-sandbox
computable even in principle** — no object-side computation discriminates them. The honest label is
*cited-external*, and it is permanent.

**S019 (Fisher metric on the CS level).** No discriminating fact was ever computed because **none
was ever formulated** — the claim has no bounded test. Relabelled **ill-posed** rather than
uncomputed, which is the more accurate description; any future work is a first formulation, not a
recomputation.

## What this did not do

The original `kill_graph.json` is **not rewritten in place** — B738's artifact keeps its provenance.
Corrections live in `kill_graph_patch.json` beside it. No physics reading was adjudicated: where a
door's subject is physics-adjacent (B433's 3d-3d, B579's values package), this arc ruled **only** on
whether the discriminating fact was computed.

## Residual, registered

- **B685** — recompute GSWZ integrality in-sandbox. The one door in this batch whose downgrade is
  a genuine *to-do* rather than a permanent classification.
- **B731** — the source record's `revival_score: 10` and its live-kill status need correcting in
  `kill_graph.json` at the next compile.
- Two doors (**B720**, **S019**) are permanently uncomputable in-sandbox; the taxonomy should carry
  *cited-external* and *ill-posed* as first-class labels rather than folding them into
  `fact_computed: false`.

`doors.py` · `kill_graph_patch.json` · `tests/test_b799_doors.py` (7 locks, both COMPUTED facts
mutation-verified).

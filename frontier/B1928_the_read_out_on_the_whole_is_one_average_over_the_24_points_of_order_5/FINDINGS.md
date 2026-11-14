# B1928 — The read-out on the whole is one average over the 24 points of order 5: a draft proof of the limit, and its prediction confirmed

**Verdict: OPEN** (a proof sketch from standard ergodic theory, with three hypotheses to check; its numerical prediction
confirmed at the record's resolution; a seat's check of the proof is owed). cc (main), 2026-11-14 (S306p). Values are
in the json files only, written before any comparison; none is set beside a measured number. **0 of 19.**

## 1. The answer first

- **The question** (P-845; the author's plan of 2026-11-14): does the read-out on the whole (B1924) have a limit, and
  why does the twin stop mattering?
- **The claim** (`verification/PROOF_DRAFT.md`). R_n → ∫ F̄ dμ.
  - F̄(τ) is the frame averaged over all 24 points of order 5 on the fibre. It is invariant under SL(2, ℤ), so it is a
    function on the modular surface.
  - μ is the flow-invariant probability that the uniform measure on L/R sequences induces on the unit tangent bundle,
    through Series' coding of geodesics by cutting sequences.
- **Why, in one line each:**
  - The letters' images generate SL(2, F₅), which acts transitively on the 24 points.
  - SL(2, F₅) = 2I is perfect, so the finite group extension of the shift is mixing.
  - Closed orbits then equidistribute jointly with their holonomy (Parry and Pollicott's Chebotarev-type theorem).
  - So the words that keep the mark see the fibre uniformly in the limit.
- **Consequences:**
  - the limit exists;
  - it is the same at the mark, at the twin and at every point of order 5, so B1924's "the twin fades" becomes a
    theorem and the reading point is removed in the limit;
  - it can be computed without the constraint on words, as the ergodic average of F̄ along random geodesics.
- **The prediction tested** (`fiber_grid.py`, `fiber_ergodic.py`). F̄ was tabulated on a grid of the fundamental domain
  (1 034 points, the finer of two grids) and averaged along 3 000 unconstrained random words of 40 letters. The
  sampling error is 6.6 × 10⁻⁴, about twenty times smaller than B1924's. It was set against B1924's constrained
  read-outs per number (48 numbers; pure noise gives a median ∣z∣ of 0.67, with 5 % above 2):

  | B1924's read-out (the constant ends) | median ∣z∣ | share above 2 |
  |---|---|---|
  | n = 22, the mark; the twin | 0.62; 0.67 | 0 %; 0 % |
  | n = 22, the second sample, the mark; the twin | 1.08; 0.60 | 17 %; 4 % |
  | n = 28, the mark; the twin | 0.76; 0.46 | 2 %; 2 % |

  The one high entry is the sample whose errors B1924's addendum already found too small (the mark at n = 22, second
  sample). **The prediction holds at the record's resolution.**
- **With B1667's canonical end** (B1927), the same test against the constrained read-outs at n = 16 and 22 gives medians
  0.84 to 1.18, with 0 to 17 % above 2. That is looser. It fits the canonical-end read-outs still settling between n = 16
  and 22 (B1927), and the mark's understated errors.
- **The interpolation of F̄** (the test's own instrument). On the finer grid the ratio outputs interpolate with median
  error 4.5 × 10⁻⁴ (90 % below 2.3 × 10⁻³). The mixing moduli have median error 3 × 10⁻³ (90 % below 2 × 10⁻²). The
  first grid failed its own bar, which was the largest error, and was replaced; the largest error is still 4 to
  6 × 10⁻² on a few mixing entries. The mixing moduli come from singular vectors, which jump where singular values
  coincide: that is hypothesis H1 below.

## 2. What this means, and what it does not

- **If the proof holds, the read-out on the whole is one number per output.** It has no point of the modulus, no reading
  point, and a statistical error that can be made as small as wanted. It still carries the end's convention (B1927).
- **Not proved:**
  - H1: F's discontinuities, where singular values coincide, must be μ-null, and μ is singular on the unit tangent
    bundle.
  - H2: tightness on the non-compact surface.
  - H3: the joint equidistribution with length weights.
  These and the sketch's citations are owed a check by a seat of another family (agy-002 or agy-exp) before the verdict
  can move.
- **A correction to the first draft, from agy-exp's X-NEG.** The draft said μ was singular "as B1868 found". The measure
  on the unit tangent bundle is singular, since its endpoint law is Minkowski's ?-measure. But its projection to the
  surface has an L² density, which agy-exp proved unconditionally (harvest row 1776). The draft is corrected.
- Nothing is compared with anything measured. The values are in the json files.

## 1a. Seen first

`VERDICT topic-sweep /read.out on the whole|thread average|move.count average|weave.s measure|twin fades/` as for B1924
(4 of 1663 arcs); and `VERDICT topic-sweep /ergodic|equidistribut|Chebotarev|cutting sequence/: 12 of 1665 arcs on main match (NEGATIVE 1,
OPEN 1, PROVED 10); 18 register rows match (DONE 12, QUEUED 6)`. None states this limit. Read for this arc:
- B1924 and B1922: the read-out and its periodicity.
- B1868 and agy-exp's X-NEG: the move-count law and its density.
- B1872 and B1914: the stabiliser and the twins.
- B1667 and B1927: the canonical end.

**Literature:**
- C. Series, "The modular surface and continued fractions" (1985), for the coding.
- W. Parry and M. Pollicott, Astérisque 187–188 (1990), for the Chebotarev-type theorem for closed orbits.
- That SL(2, F₅) ≅ 2I is perfect (standard).

## Files

- `verification/PROOF_DRAFT.md`: the sketch and its three hypotheses.
- `verification/fiber_grid.py` (→ `fiber_grid_fine.json`, `fiber_grid_fine_run.txt`): F̄ on the domain, with both of
  B1924's constant ends and the canonical end.
- `verification/fiber_ergodic.py` (→ `fiber_ergodic_fine.json`, `fiber_ergodic_fine_run.txt`; the first grid's run is
  `fiber_ergodic_run.txt`): the ergodic integral and the comparisons P1 to P3.
- The lock: `verification/test_b1928_one_average.py`.

## Addendum (2026-11-14, later): H1 holds

- **The argument.** F, the frame's outputs at (τ, p), jumps only where two singular values of a sector's coupling
  coincide. With B1927's length-2 end the frame is real-analytic in τ. So, for each of the 24 points p, the coincidence
  set is a proper real-analytic subset of the τ-plane, of zero area. agy-exp's X-NEG proved that the path measure's
  τ-law has an L² density (harvest row 1776), so a set of zero area carries no weight, and the set is μ-null.
- **The numerical face** (`verification/h1_check.py`; 9 064 nodes along 60 random geodesics of 24 letters, each with a
  random point of order 5, the length-2 end). The smallest relative gap of singular values over every sector and
  reading is below 0.1 at 4.5 % of the nodes, below 0.01 at 0.02 % (two nodes), and below 0.001 at none.
- **The expectation was wrong in the safe direction.** It was written before the run: the share would fall tenfold per
  decade, as for a curve crossed transversally. It falls about 200-fold. Near-coincidences are rarer than a
  codimension-one set would give, which fits the repulsion of singular values of complex matrices: coincidence is
  codimension three, so a two-parameter family generically has none.
- **H1 is met.** H2 (tightness) and H3 (the length-weighted joint equidistribution) remain, with agy-002's check of the
  sketch (M26).


# B1529 — THE EIGENVALUE-ONE LOCUS: near the hyperbolic point of every word state to length 12 and of m004's levels, Λ² carries no count for any deformation in SL(4, ℂ); the four carries none wherever its base condition holds, and the base condition fails on one word state, m135, at two characters

cc (the SM-derivation seat), 2026-10-03. Sealed at `44cdb4a6` before `census.py` or `crossings.py` read any outcome
(`PREREGISTRATION.md`, sha-256 `0d25e638…`, SEAL_LEDGER).
- **The run.**
  - The census ran from 12:44:16Z to 13:46:23Z on four cores: 541 manifolds and 47,333 base points per module, as sealed.
    It was resumed once after the session's worker restarted (12:54:30Z; `census.jsonl` then had 229 complete records).
  - The crossing reader ran as sealed from 12:47:40Z and finished at 15:47:43Z.
  - On ±L³RLR² the sealed bracket rule admitted 22 sign changes through a pole of b per sign (§1.2; ERROR_LEDGER, E31). The
    sealed processes there were stopped at 13:26:46Z, after the first pole bracket had run for 2,024 and 1,928 s.
    `post_run_poles.py` then ran the sealed loop body unchanged, one process per bracket, on all 40 brackets of each sign
    (disclosed).
- **Verdict: PROVED, with a kill record.** sL-10 item 9 is answered for Λ² and, at every base point where the four's base
  condition holds, for the four (§5).
  - Theorem N and the census (P1: SR at all 47,333 base points) give I(ν ⊗ Λ²ρ) = 0 near ρ_hyp. That holds for every character
    ν and every deformation in Hom(Γ, SL(4, ℂ)): types 2 and 3, real or complex, on all 536 word-state manifolds and on
    M₂–M₆.
  - Lemma K gives I(ν ⊗ ρ) = 0 near ρ_hyp wherever the four's base condition holds. It holds at 46,824 of the 46,826
    word-state base points, and on the levels at all but M₆'s 28 (sm:B1515's).
  - The two exceptions are on **m135 = −LLRR**, at the characters u = (0, ½) and (½, 0). There the twisted four has one
    interior class for V and one for V*. This was read in three routes at 60 digits and in exact arithmetic over ℚ(ζ₈). The
    four's question there, with M₆'s 28, is item 10 (§7).
- **As sealed: 5 of 7 predictions held.** The priors expected 5.7.
  - P1, P3 and G's census part hold. P2 fails on m135 alone: outcome D, and with P1, P3 and P5, outcome A for Λ².
  - P4 fails on its location rate alone: 143 of the 196 sealed brackets were located, 73% against the 90% sealed. Of the
    other 53, 44 are the sign changes through a pole on ±L³RLR², 8 are on −L⁴RLR³LR², where the crossing system stalls, and
    one is on +L⁴RLR³LR². At every located crossing the structure P4 predicts holds.
  - P5 and P6 hold at all 143: I = 0 on 9,562 route-T rows and 1,406 Fox and W rows, and Λ²'s interior value at its special
    twists is at least 0.33. G holds; on −L⁴RLR³LR², where no crossing was located, its crossing part holds vacuously.
- **After the run (disclosed; §4).** At first order every ring carries twenty crossings. The coverage check located 37 of the
  57 that the sealed brackets miss or do not locate. With the sealed run's 143, that is 180 of the 200: all twenty on each of
  nine rings, none on −L⁴RLR³LR². P4's structure, P5 and P6 hold at all 180 (11,640 route-T rows, 1,640 Fox and W rows).
- **Prior work: EXTENDS** (§6). Kapovich (two-bridge lattices) and Bart–Scannell (Canad. J. Math. 58 (2006)) study the
  four's cuspidal classes as parabolic-preserving deformations into SO(4, 1). Bart–Scannell find none on PSL(2, O_d) for
  d = −1, −2, −3, −7, −11, −15. The census is the first reading of them, twisted by every character, on the punctured-torus
  bundles to length 12. In the sources read, it is not recorded that m135's double covers carry such classes.
- **0 of 19 stays 0.**

## 0. What was found

- **Λ² never carries a count near the hyperbolic point.**
  - SR holds at every base point of all 541 manifolds: am(C; 1) = am(C′; 1) = 2 = e = am(D; 1) for Λ², at all 47,333.
  - The relative interior value ∣χ_K(1)∣ is at least 1/3 at every base point; the minimum, 1/3, is on ±LR. No base point
    comes near the coincidence Theorem N excludes.
  - So by Theorem N, I(ν ⊗ Λ²ρ) = 0 on a neighbourhood of ρ_hyp in Hom(Γ, SL(4, ℂ)), for every character. That covers
    types 2 and 3 and the complex representations, which sm:B1527 left open.
  - Lemma B's base condition (2, 2, 2, 2) holds at every base point, as Menal-Ferrer–Porti's theorem implies on the finite
    covers.
- **The four carries no count near ρ_hyp wherever its base condition holds** (Lemma K), and that is almost everywhere:
  - (h¹, h¹*, t0, s0) = (1, 1, 1, 1) at 46,824 of the 46,826 word-state base points, and on M₂–M₅ throughout.
  - **m135 = −LLRR** (SnapPy: m135, volume 3.66386 = one regular ideal octahedron; trace −6, D = 8, H₁ = ℤ/2 + ℤ/4 + ℤ;
    amphichiral) fails it at u = (0, ½) and (½, 0), the two characters of order 2 that are trivial on the cusp at λ_c. There
    (h¹, h¹*, t0, s0) = (2, 2, 1, 1): one interior class each for V and V*, and I = 0.
  - In Bart and Scannell's terms these are parabolic-preserving infinitesimal deformations into SO(4, 1). They are odd under
    the deck group of the double covers of m135 defined by the two characters, so those covers are not infinitesimally rigid
    in SO(4, 1) relative to their cusps. The untwisted four on m135 has none (u = (0, 0) reads (1, 1, 1, 1)). Bart–Scannell
    prove PSL(2, ℤ[i]) itself has none (their Theorem 4.5), and m135 is commensurable with it (its shapes lie in ℚ(i)).
  - **M₆** fails it at 28 characters, exactly as sm:B1515 banked: 24 of order 8 with (2, 2, 1, 1) and 4 of order 5 with
    (3, 3, 1, 1). This was the sealed positive control.
  - Read three ways and exactly (§4.2, §4.3): routes T, Fox and W agree at 60 digits on all eight characters of m135, and so
    does an exact computation over ℚ(ζ₈).
- **The four's SR, recorded and not predicted.** χ_K(1) = 0 at 42 base points, on three manifolds:
  - m135 at six characters: the two above and the four of order 4. Exactly, χ_C = (s − 1)⁴ there.
  - M₄ at its eight characters of order 3. Its base condition still holds there, so Lemma K covers them.
  - M₆ at its 28.
  Where the base condition holds, Lemma K needs no SR.
- **The crossings** (§1.2, §4.4–§4.6). At first order each ring carries twenty: 8 of E1 and 4 each of E2, E3 and E4. The
  sealed brackets located 143 of them, and the coverage check after the run 37 more: 180 of 200, all twenty on every ring but
  −L⁴RLR³LR², where none was located.
  - At all 180 the structure is as predicted: e = 1 for the four, with one special twist; e = 2 for Λ², with two special
    twists whose product is 1 (to 2.22 × 10⁻⁵⁰); and (t0, s0) = (1, 1) on every route-T row.
  - I = 0 on all 11,640 route-T rows and all 1,640 Fox and W rows, with the three routes agreeing and every identity holding.
  - Λ²'s interior value at its special twists is at least 0.33 (relative): no coincidence, as Theorem N's proof needs.
  - The four's is small, between 4.19 × 10⁻⁸ and 6.15 × 10⁻⁵ (recorded, not predicted). At a crossing where e = 1, χ_C keeps its
    two roots near 1 and χ_D has one, so χ_K keeps a root near the special twist. Lemma F alone does not close the four
    there; Lemma K does.
- **Golden.**
  - G's census part holds: P1 and P2 hold on all 14 golden word states (∣trace∣ ∈ {3, 7, 18, 47, 123, 322}).
  - The four's base condition fails on one word state, m135. Its monodromy −L²R² has eigenvalues −(1 ± √2)², minus the
    squares of the silver ratio and its conjugate (trace −6), so it is not golden.
  - It also fails on one level, M₆, which is golden (trace 322). That level is m004's six-fold cover, banked by sm:B1515.
  - So the census does not separate golden from non-golden states by the four's base condition: it fails once in each
    class.
- **The experiential question.** GENESIS FK12 holds it under Gate 5-Q, and nothing in this arc bears on it. Per the owner's
  instruction of 2026-10-02 (nothing load-bearing ignored, the experiential question included), that is recorded here.

## Seen first (the repo, then the literature)

**At the seal** (PREREGISTRATION §0, the PRIOR ART section). The repo sweep (`scripts/checks/prior_work.py`) ran over five
heads with nine terms; Menal-Ferrer–Porti (arXiv:1001.2242v2) §0–3 was read. Lemma F's non-acyclic form, the simple-root
condition and Lemma O were found on no head.

**Refreshed at banking** (2026-10-03, after `git fetch --all`). Main moved from `d2a95da4` to `399b0bc2`, and the audit lane
from `24c039c8` to `ddd345a8`. The other heads had not moved.
- The sweep was run again with fourteen terms, the post-run vocabulary included: "m135", "interior class", "interior
  polynomial", "simple root", "eigenvalue-one locus", "item 9", "special twist", "pole of b", "coincidence locus",
  "nonsplit", "compact-boundary", "-LLRR", "b+-LLRR", "Whitehead".
  - "interior polynomial", "special twist" and "coincidence locus" occur only in this arc and its seal's ledger rows.
  - "m135" occurs on every head in tables of amphichiral manifolds, Chern–Simons values and arithmetic or torsion
    invariants (B152, B855, B985, B1224, B1226, B1227 and GENESIS's list of states). None computes a twisted cohomology on
    it.
  - "-LLRR" on main is B1434's architecture census and B1435's interaction census on the levels: counts of orbits and
    couplings, not the four's cohomology.
  - "interior class" on main is its harvest of sm:B1515 and B1440/B1446/B1447. There, on m004's families, the complete cusp
    carries "no interior class".
  - "nonsplit" and "compact-boundary" lead to the audit lane's R75–R81. They concern harmonic metrics for a non-split W on
    a cusp truncation and do not bear on item 9 (§7).
- **Main's S47 (B1464, Review 59)** is governance: the seal parser, the provenance rule, aged items. It records R59-1 (main's
  L242 (e) as a verification of sm:B1527) and R59-3 (36 unrowed seat items). It does not bear on this arc's mathematics.
- **The audit lane's R81** (`ddd345a8`): the non-split coefficient W admits a harmonic metric on a compact cusp truncation
  (Wu–Zhang, arXiv:2109.01776v1, Proposition 3.3). Its review request (D1–D4) is recorded in §7 and the relay ledger.
- **The literature, read at banking:** A. Bart and K. P. Scannell, *The generalized cuspidal cohomology problem*, Canad. J.
  Math. 58(4) (2006), 673–690. Read from the journal PDF on 2026-10-03; the text is in the seat's scratchpad.
  - §2.1 (p. 676): PH¹(Γ, ℝ⁴₁), the parabolic cohomology with coefficients in the standard four-dimensional representation of
    SO(3, 1), is the kernel of restriction to the boundary (Scannell). It parameterizes the parabolic-preserving infinitesimal
    deformations of Γ into SO(4, 1).
  - §2.2 (p. 676) and Proposition 4.1 (p. 679): Kapovich showed PH¹ = 0 when Γ is generated by two parabolics, i.e. for
    two-bridge link complements. m004 is one; its base condition holds.
  - Theorem 4.5 (p. 683): PH¹(Γ_d, ℝ⁴₁) = 0 for d = −1, −2, −3, −7, −11, −15.
  - Proposition 4.6 (p. 683): dim H¹(Γ, V) = dim ker res + dim H⁰(π₁(∂M), V). This is the census's h¹ = n + t0.
  - §5 (p. 685): a two-component link complement (8²₁₄, a 12-sheeted cover of Γ₋₇'s orbifold) with PH¹ ≠ 0; the second
    author's unpublished result that PH¹ is two-dimensional for every Turk's head link.
  - The paper twists by no character and treats no punctured-torus bundle by name.
- **Not found in the sources read:** a twisted (character) version of this cohomology on punctured-torus bundles, or m135's
  double covers carrying such classes.

**Refreshed again at banking** (2026-10-04, after `git fetch --all`). Main moved from `399b0bc2` to `e90b4f7e` (S48–S54,
B1465–B1471), and the audit lane from `ddd345a8` to `aee360ae` (R82–R84).
- The sweep ran again with seventeen terms: the fourteen above, and "crossing system", "first-order crossing" and "sign change
  through a pole".
- On main the new hits are its harvest rows of this seat's arcs: HARVEST_LEDGER row 834 registers sm:B1529 as sealed and
  running, B1467's FINDINGS lists it, and the GENESIS copies in B1466's and B1467's `received/` carry this seat's lines.
  Main's S54 (B1471) is the twisted Alexander cancellation on the 112-family, its own frame.
- On the audit lane, R82's relay notes this arc as sealed and unread. R84 reviews sm:B1535, not this arc.
- None computes the four's or Λ²'s twisted cohomology at the eigenvalue-one locus, or locates its crossings.

## 1. The run (as sealed)

### 1.1 The census

`census.py` read every torsion character at λ_c on the 536 word-state manifolds and on M₂–M₆. That is 46,826 characters on the
word states and 507 on the levels (5 + 16 + 45 + 121 + 320), 47,333 in all, for the four and for Λ².

| | base points | SR (am(C; 1) = am(D; 1) = 2) | base condition | I ≠ 0 | route T's hypothesis failing |
|---|---|---|---|---|---|
| Λ² | 47,333 | 47,333 | (2, 2, 2, 2) at 47,333 | 0 | 0 |
| the four | 47,333 | 47,291 (χ_K(1) = 0 at 42) | (1, 1, 1, 1) at 47,303; (2, 2, 1, 1) at 26; (3, 3, 1, 1) at 4 | 0 | 0 |

- The four's failures of the base condition: m135 at 2 (both (2, 2, 1, 1)) and M₆ at 28 (24 and 4).
- The margins, over all 541 manifolds:
  - am: the largest Taylor coefficient read as zero is 6.4 × 10⁻⁴⁶ (the four) and 1.2 × 10⁻⁴⁸ (Λ²). The first non-zero is
    ≥ 3.4 × 10⁻⁴ (the four) and 0.5 (Λ²).
  - g: the smallest kept singular value is ≥ 8.5 × 10⁻⁷ (the four) and 4.1 × 10⁻⁶ (Λ²), against a largest dropped of
    1.7 × 10⁻⁵⁰ and 1.1 × 10⁻⁵¹.
  - The slot conditioning is ≥ 4.3 × 10⁻⁵ (the four) and 1.1 × 10⁻⁶ (Λ²).
  - The relators hold to 4.8 × 10⁻⁴⁹ at every hyperbolic point.
  - Where the four's SR holds, its smallest relative ∣χ_K(1)∣ is 1.7 × 10⁻⁴ (on −L³R²LRLRLR²). Where it fails, the value read
    is ≤ 2.1 × 10⁻⁴⁹.
- The banked identity (PREREGISTRATION §8). The seal's own control run (12:29Z) preceded the census by 15 minutes, on the
  sealed files. `controls.py` was also re-run unchanged after the census, in a worktree at `8e4e4163`; its `controls.json`
  equals the sealed one in every field but the timings (`controls_run.txt`, `controls_rerun.txt`). The census carries the
  sealed identities on every manifold: Λ²'s (2, 2, 2, 2), I = 0, C2's polynomial on +LR, and B1515's counts on the levels.

### 1.2 The crossings, and the sign changes through a pole

`crossings.py` read the ten rings as sealed. Brackets come from X1's 5° grid: a sign change of E1–E4 between neighbouring
frames that both converged with ∣b∣ < 50a.

| ring | brackets (E1, E2, E3, E4) | through a pole of b | located | route-T rows | Fox and W rows | I ≠ 0 |
|---|---|---|---|---|---|---|
| +LR | 16 (8, 0, 4, 4) | 0 | 16 | 36 | 36 | 0 |
| −LR | 16 (8, 0, 4, 4) | 0 | 16 | 180 | 180 | 0 |
| +LLRLRR | 16 (8, 0, 4, 4) | 0 | 16 | 468 | 180 | 0 |
| −LLRLRR | 16 (8, 0, 4, 4) | 0 | 16 | 612 | 180 | 0 |
| +L³RLR² | 40 (14, 6, 10, 10) | 22 | 18 | 684 | 190 | 0 |
| −L³RLR² | 40 (14, 6, 10, 10) | 22 | 18 | 836 | 190 | 0 |
| +L⁴RL³R² | 14 (6, 2, 4, 2) | 0 | 14 | 1,260 | 140 | 0 |
| −L⁴RL³R² | 14 (6, 2, 4, 2) | 0 | 14 | 1,372 | 140 | 0 |
| +L⁴RLR³LR² | 16 (8, 0, 4, 4) | 0 | 15 | 4,114 | 170 | 0 |
| −L⁴RLR³LR² | 8 (6, 0, 2, 0) | 0 | 0 | 0 | 0 | 0 |
| all | 196 | 44 | 143 | 9,562 | 1,406 | 0 |

- **The sign changes through a pole** (ERROR_LEDGER, E31). On ±L³RLR², 22 of each sign's 40 brackets hold a sign change
  through a pole of b, not a crossing. X1's own test marks them: b changes sign between the two frames without being small
  (∣b∣ < 10a) at both.
  - The sealed processes there spent 2,024 and 1,928 s on their first such bracket and were stopped at 13:26:46Z.
  - `post_run_poles.py` then ran the sealed loop body unchanged, one process per bracket, on all 40 of each sign (§4.4). Its
    records are the sealed read-out's input for these two rings.
  - None of the 44 converged. Every one of the 36 pole-free brackets did.
- **−L⁴RLR³LR²:** none of its 8 brackets was located. The 60-digit crossing system stalls there at ∣F∣ between 6.08 × 10⁻¹¹
  and 1.16 × 10⁻⁶, against the sealed 10⁻⁴⁸.
- **+L⁴RLR³LR²:** 15 of 16. The E4 bracket [315°, 320°] stalled at ∣F∣ = 3.7 × 10⁻³; it was located after the run (§4.5).
- **At the 143 located crossings:**
  - ∣F∣ ≤ 9.5 × 10⁻⁴⁹ at 60 digits;
  - the relators hold to 8.7 × 10⁻⁴⁸, and the crossing function vanishes to 1.7 × 10⁻⁵³ a;
  - the margins (smallest kept against largest dropped): Fox 8.75 × 10⁻¹³ against 1.26 × 10⁻⁴⁴; route W 6.15 × 10⁻¹¹
    against 3.69 × 10⁻⁵¹; the cusp ends 6.98 × 10⁻⁷ against 4.51 × 10⁻⁵².
- **The structure P4 predicts holds at every one of them:**
  - for the four: 112 crossings (E1, E2, E3), each with e = 1 and one special twist;
  - for Λ²: 99 crossings (E1, E4), each with e = 2 and two special twists whose product is 1 to 2.22 × 10⁻⁵⁰;
  - (t0, s0) = (1, 1) on every route-T row.

### 1.3 The read-out

`read_out.py` ran once, after all ten crossing records were written (`read_out.json`; committed at `8134de14`). Every ring's
record was present.
- The census: P1 holds, P2 fails on −LLRR alone, P3 holds with all seven checks, and G's census part holds on the 14 golden
  word states.
- The crossings: 196 brackets, 143 located; no structure, index or mechanism failure on any ring. P4 fails on the location
  rate; P5, P6 and G's crossing part hold.
- **5 of 7 held**: P1, P3, P5, P6 and G. Outcome A for Λ² (P1, P3 and P5) and outcome D for the four (P2).

## 2. The theorems (as sealed), and what the run supplies

The six statements of PREREGISTRATION §3 stand as sealed; nothing in the run touches their proofs.
- **Theorem N's hypothesis is supplied** on all 541 manifolds: SR for Λ² at every base point (P1). So its conclusion holds on
  each, with one neighbourhood of ρ_hyp per manifold.
- **Lemma K's hypothesis** is supplied at every base point but m135's two and M₆'s 28 (P2, P3).
- **The count's ceiling at the exceptions.** Near a base point where the four's base condition fails with k = h¹ = 2 and
  t0 = s0 = 1, Lemma E and semicontinuity still bound the index. With a0 = b0 = 0 nearby, I = [h¹(V*) − t0] − [h¹(V) − s0],
  where s0 ≤ h¹ ≤ 2 and t0 ≤ h¹* ≤ 2. So I ∈ {−1, 0, 1} on the locus t0 = s0 = 1, and I = 0 off it (Lemma C).
- **Where the exceptions can carry a count** (Lemma F, at a crossing where e = 1). I = g(B; κ*) − g(C; κ*), and both
  generalized κ*-eigenspaces have the same dimension, 1 + am(K; κ*). So I ≠ 0 needs κ* to be a root of χ_K and exactly one
  of the two extensions, 0 → A → E(B) → E(K) → 0 and 0 → E(K) → E(C) → E(D) → 0, to split.
  - At the base χ_K has a double root at 1 = κ*. So the coincidence locus κ* = r(χ_K) passes through ρ_hyp, and is not
    excluded by any theorem here. That is item 10.

## 3. The predictions

| # | prediction | prior | as sealed | the reading |
|---|---|---|---|---|
| P1 | SR for Λ² at every base point, words and levels | 85% | **held** | all 47,333 |
| P2 | the four's base condition at every word-state base point | 55% | **failed** | m135 = −LLRR at (0, ½) and (½, 0), (2, 2, 1, 1); the other 46,824 hold |
| P3 | the theorems' controls everywhere | 93% | **held** | all seven checks; no manifold failed |
| P4 | ≥ 90% of the brackets located, and the structure at every located crossing | 80% | **failed** | 143 of 196 located (73%); the structure holds at all 143 |
| P5 | I = 0 at every located crossing, every identity, Fox = W = T | 92% | **held** | 9,562 route-T rows, 1,406 Fox and W rows |
| P6 | Λ²'s interior value at every special twist > 10⁻²⁰ | 88% | **held** | at least 0.33 |
| G | P1 and P2 on the golden word states; P5 on the six golden rings | 80% | **held** | 14 golden states; on −L⁴RLR³LR² P5 holds vacuously |

5 of 7 held; the priors expected 5.7. After the run the coverage check gives P4's structure, P5 and P6 at all 180 located
crossings (§4.6). The location rate is not changed by it: P4 stays failed as sealed.

## 4. Post-run checks (written after the run; disclosed)

None changes a sealed reading.

### 4.1 The controls re-run (`controls_rerun.txt`)

Run unchanged in a detached worktree at `8e4e4163` after the census; finished 13:48:49Z. All six pass, and `controls.json`
agrees with the sealed file field by field except the timings.

### 4.2 m135's failures in routes Fox and W (`post_run_fox.py`)

The census's only word-state failures, re-read by sm:B1527's banked routes, which share no linear algebra with route T:
- route Fox (`cusp_lib.class_index`): (h¹, h¹*, t0, s0) = (2, 2, 1, 1) at u = (0, ½) and (½, 0), (1, 1, 1, 1) at the other six;
  every identity (B1297's, the annihilator identity, Lemma E) holds; I = 0;
- route W (`wang_lib.index_wang`): the same at all eight;
- the interior classes: n(V) = n(V*) = 1 at the two failures.
M₆'s 28 are sm:B1515's, read there by three methods, and are not re-read.

### 4.3 m135 in exact arithmetic (`post_run_exact_m135.py`)

- **The representation.** m135's shapes are 1 + i, i, 1 + i and (1 + i)/2. Conjugating the 60-digit hyperbolic point so the
  cusp's fixed point p₀ goes to ∞, a(p₀) to 0 and b(p₀) to 1 puts a, b and t in PGL(2, ℚ(i)). Divided by their largest
  entries, every entry reads as a Gaussian rational with denominator at most 50, to 10⁻⁶⁰:
  - a ∝ [[0, (−1 + 7i)/50], [1, (−3 + i)/5]];
  - b ∝ [[1, (−27 − 11i)/50], [1, (−2 − i)/5]];
  - t ∝ [[(7 + i)/10, (−17 + 19i)/50], [1, (−1 + i)/2]].
  The two bundle relators are scalar in PGL(2, ℚ(i)), exactly; the cusp's generators commute and are parabolic.
- **The four** (H ↦ gHg*/∣det g∣) lies over ℚ(√2): its traces on a, b, t, ab, abt are 2√2, 2√2, 4, 4, 4. The relators hold
  exactly.
- **The readings, by Fox calculus over ℚ(ζ₈)**, all eight characters at λ_c. They agree with the census:

  | u | (h¹, h¹*, t0, s0) | n(V), n(V*) | I | χ_C (the fibre's S₀ on H¹(F)) | am(C; 1) |
  |---|---|---|---|---|---|
  | (0, 0) | (1, 1, 1, 1) | 0, 0 | 0 | (s − 1)²(s² + (14 + 8√2)s + 1) | 2 |
  | (½, ½) | (1, 1, 1, 1) | 0, 0 | 0 | (s − 1)²(s² + (14 − 8√2)s + 1) | 2 |
  | (0, ½), (½, 0) | (2, 2, 1, 1) | 1, 1 | 0 | (s − 1)⁴ | 4 |
  | (¼, ¼), (¼, ¾), (¾, ¼), (¾, ¾) | (1, 1, 1, 1) | 0, 0 | 0 | (s − 1)⁴ | 4 |

  (The quadratic factors are read off the record's coefficients: s⁴ + (12 + 8√2)s³ − (26 + 16√2)s² + … = (s − 1)²(s² + (14 +
  8√2)s + 1).)

### 4.4 The pole brackets on ±L³RLR² (`post_run_poles.py`)

Written at 13:37Z, after the sealed processes there were stopped, and run unchanged from 13:38:01Z to 21:53:04Z (29,703 s).
- It runs `crossings.py`'s loop body for one bracket, unchanged, one process per bracket, on all 40 brackets of each sign. It
  tags each bracket with X1's pole test and checks the bracket list equal to the sealed one.
- The 18 pole-free brackets of each sign converged in 120 to 245 s each.
- None of the 22 pole brackets of either sign converged, in 1,759 to 4,124 s each. Their crossing systems stalled with ∣F∣
  between 2.28 × 10⁻³ and 10.4, far from a root.
- It writes `crossings_pLLLRLRR.json` and `crossings_mLLLRLRR.json` in the sealed format (40 brackets, 18 located each). The
  sealed read-out read them as these rings' records.

### 4.5 The crossings the sealed brackets miss (`post_run_coverage.py`)

Written at 13:39Z, after the sealed crossing run had begun; not edited after its start.
- **Why.** Next to a pole of b, X1's frames do not converge or the pole lies inside the bracket, so crossings near the poles
  go unbracketed.
- **The count at first order.** On the ring, ℓ's translation is z_ℓ = R0 e^{iα}, so ψa = aR0 cos α and ψb = bR0 sin α. The
  crossings E1–E4 are where b/a = c cot α with c = −1, 3, 1/3, 1. With sm:B1527's weight-3 law b/a = −tan 3(α − α₁), they
  are the roots of (1 + c) cos(2α − 3α₁) + (c − 1) cos(4α − 3α₁): 8, 4, 4 and 4 on the circle, twenty per ring.
- **Targets: 57.**
  - 48 missed: first-order crossings that no pole-free sealed bracket of their kind holds.
  - 9 failed: crossings in a pole-free sealed bracket whose sealed locate did not converge (8 on −L⁴RLR³LR², 1 on
    +L⁴RLR³LR²).
- **Route F.** X1's float64 pinned solve at α_c ∓ w (w = 0.25°, 0.5°, 1°). Both ends must converge with ∣b∣ < 50a and no
  pole between them, and the crossing function must change sign. Then `crossings.locate` and `crossings.read` run unchanged.
- **Route S**, where route F finds no bracket or its locate fails, works at 60 digits throughout.
  - It starts from the nearest converged frame of X1's grid with no first-order pole in between.
  - It continues the pinned solution toward α_c in steps of at most 1°.
  - It solves the crossing system from the nearer point, and runs `crossings.read` unchanged.
- **Located: 37 of 57**, 32 by route F and 5 by route S. Every one lies within 3.5 × 10⁻⁵ degrees of its first-order
  crossing, with ∣F∣ ≤ 6.1 × 10⁻⁴⁹ (route F) and ≤ 2.4 × 10⁻⁵³ (route S).
- **Not located: the 20 on −L⁴RLR³LR²** (12 missed, 8 failed).
  - Route F bracketed 8 of them, and its locate stalled at ∣F∣ between 1.30 × 10⁻¹² and 1.43 × 10⁻⁷. At the other 12 an end
    of its bracket did not converge.
  - Route S's crossing system stalled in all 31 of its attempts, at ∣F∣ between 2.03 × 10⁻¹⁴ and 8.12 × 10⁻¹¹. At some
    targets its continuation failed first or found no starting frame. X1's frames there converge at 60 digits to 10⁻⁵³.
  - The cause is not diagnosed (§7).
- **The run.** 14:06:33Z to 15:06:03Z (33 targets), then paused to give the pole brackets the processors. Resumed unchanged
  from 21:55:08Z to 06:17:44Z on 2026-10-04 (the other 24). The file is resume-safe: one line per target.

### 4.6 The content of P4–P6 on every located crossing (`post_run_read.py`)

Written at 13:44Z; run once, after the coverage check finished (`post_run_read.json`).
- `check_read` is `read_out.crossings`' loop body for one crossing. On the sealed records its failure lists equal
  `read_out.py`'s on every ring.
- Every located crossing, sealed or not, lies within 0.01° of exactly one first-order crossing, and none is found twice.
  That gives 180 of the 200: all twenty on each of nine rings, none on −L⁴RLR³LR².
- **At all 180:** no structure, index or mechanism failure. There are 11,640 route-T rows and 1,640 Fox and W rows, all
  with I = 0.
  - **Λ²**, at 108 crossings (E1, E4): two special twists each, with product 1 to 2.22 × 10⁻⁵⁰. Its interior value at them
    is at least 0.33 at the sealed crossings and at least 0.85 at the coverage check's.
  - **The four**, at 144 crossings (E1, E2, E3): one special twist each. Its interior value at it lies between 4.19 × 10⁻⁸
    and 6.15 × 10⁻⁵ (recorded, not predicted; §0).
- So P4's structure, P5 and P6 hold on every crossing located, and G's crossing part holds on the five golden rings where
  crossings were located.

### 4.7 The census record kept in the tree (`post_run_records.py`)

`census.py` writes `census.jsonl`, and `read_out.py` reads it. The repository ignores `*.jsonl` (the chronicle-harvest
firewall), as it does sm:B1523's `route_f_seeded.jsonl`, from which `census.py` lists its states (ERROR_LEDGER, E57).
`census_records.json` keeps the 541 records unchanged, with the sha-256 of the file they came from. The lock rebuilds
`census.jsonl` in a temporary directory and runs the sealed reader there. Each record names its state and the word it was
read as, so `census.one` re-runs any manifold without the list.

## 5. Item 9 and the kill record

- **Item 9 is answered for Λ²: no.** Near the hyperbolic point of every word state to length 12 and of M₂–M₆, no vacuum
  ν ⊗ Λ²ρ has a non-zero class index, for any deformation ρ in Hom(Γ, SL(4, ℂ)) and any character ν. This covers types 2 and
  3 and the complex representations, which sm:B1527 left open (Theorem N with P1).
- **Item 9 is answered for the four: no, except near 30 base points.** For ν ⊗ ρ the same holds near every base point where
  the four's base condition holds (Lemma K with P2 and P3). It fails at m135's two characters and M₆'s 28.
  - Near those 30 base points the index is bounded, I ∈ {−1, 0, 1} (§2).
  - It can be non-zero only on the coincidence locus, where the special twist is a multiple root of χ_C, and only if exactly
    one of the two extensions in Lemma F splits.
  - That locus passes through ρ_hyp. It is item 10, to be sealed first (§7).
- **Kill record** (frame F-HE, reach class): `the-interior-polynomial-decides`.
  - Near ρ_hyp a count needs a special twist at a root of the fibre's interior polynomial χ_K (Lemma F).
  - For Λ² the root at 1 is simple at every base point (SR at 47,333 base points), so no deformation meets one (Theorem N).
  - For the four, the sandwich closes it wherever the base condition holds (Lemma K).
  - Hypotheses: near ρ_hyp; the reductive modules ν ⊗ ρ and ν ⊗ Λ²ρ; the 536 word-state manifolds to length 12 and M₂–M₆.
  - Hatch: the four's coincidence loci at m135's two base points and M₆'s 28 (item 10); non-split extensions (m135's interior
    classes give them, as M₆'s did in sm:B1515); far from ρ_hyp; other modules; longer words and higher levels.
- **For the goal.** Every reductive vacuum near the hyperbolic point of every word state to length 12 is closed, except the
  four's at 30 base points. One of those manifolds, m135, is new; it is not one of m004's levels. 0 of 19 stays 0.

## 6. Prior work and standing

- **Standing: EXTENDS.**
  - Lemmas K and F rest on sm:B1510 Theorem C, sm:B1509 T3, sm:B1511 Theorem B and main's B1440 (credited at the seal).
  - Lemma B is Menal-Ferrer–Porti's Theorem 0.1 on a finite cover.
  - The four's base condition is the vanishing of Bart and Scannell's generalized cuspidal cohomology with coefficients in
    the standard representation ℝ⁴₁, twisted by a character. By Proposition 4.6 there, h¹ = n + t0. Kapovich proved it
    vanishes for two-bridge lattices; Bart–Scannell proved it vanishes for six Bianchi groups. sm:B1515 read it as
    infinitesimal deformations into SO(4, 1) that are trivial on the cusp, and found the first failures, on M₆ (its lead 2).
- **What is added, as far as swept:**
  - Theorem N and Lemmas O and P, and their consequence for Λ² near ρ_hyp in Hom(Γ, SL(4, ℂ)) on 541 manifolds;
  - the census of the four's twisted cuspidal cohomology at λ_c on every word state to length 12: it vanishes everywhere
    but at m135's two characters of order 2;
  - m135's two classes, exactly (§4.3);
  - the coincidence criterion for the exceptions (§2), which defines item 10.
  None of this is in the sources read (§ Seen first).

## 7. What this arc does not decide (the next questions)

- **Item 10: the four's coincidence loci near ρ_hyp** at m135's two base points and M₆'s 28.
  - Is I(ν ⊗ ρ) ≠ 0 at some ρ near ρ_hyp where the special twist κ* is a multiple root of χ_C? There I ∈ {−1, 0, 1}, and
    I ≠ 0 needs exactly one of the two extensions of Lemma F to split.
  - On the self-dual locus (ρ* ≅ ρ: the deformations into SO(4, ℂ)), (ν ⊗ ρ)* ≅ ν⁻¹ ⊗ ρ, so I(ν⁻¹ ⊗ ρ) = −I(ν ⊗ ρ): any counts
    there come in opposite pairs, the special twists κ* and 1/κ*, as Lemma P pairs Λ²'s.
  - It is registered in OPEN_LEADS, to be sealed before computing.
- **The extensions from m135's interior classes.** sm:B1515's sign law (I(W₁) ≥ 0 ≥ I(Λ²W₁), read through M₆) was observed
  only on m004's levels. m135 at u = (0, ½) and (½, 0) is the first place off that tower where it can be read.
- **The crossings of −L⁴RLR³LR²**, none of which is located. The 60-digit crossing system stalls there in every attempt
  (§1.2, §4.5), while X1's frames converge, and the cause is not diagnosed. A locator at higher precision is the next step.
  The theorems cover the ring regardless: P1 and P2 hold at every base point of ±L⁴RLR³LR².
- **Far from ρ_hyp**, other modules, and words longer than 12 or levels above 6.
- **The audit lane's R81 review request** (the non-split W's harmonic metric on a compact cusp truncation, D1–D4). It is
  recorded in the relay ledger and not taken up here.
- **The experiential question** (GENESIS FK12, under Gate 5-Q): nothing here bears on it.
- **0 of 19 stays 0.** I-26 stays UNEARNED.

## Files

- `PREREGISTRATION.md` (sealed), `ARTIFACT_HASHES.txt`.
- `verification/`:
  - sealed: `fibre_lib.py` (route T), `controls.py` (`controls.json`, `controls_run.txt`), `census.py`, `crossings.py`,
    `read_out.py`;
  - the run: `census.json`, `census_log.txt` and `census.jsonl` (git-ignored; kept as `census_records.json`); for each of the
    ten rings `crossings_<name>.json` and `crossings_log_<name>.txt`; `crossings_done.txt`; `read_out.json`;
  - post-run: `controls_rerun.txt`; `post_run_poles.py` (`post_run_poles_log.txt`, and the ±L³RLR² crossing records);
    `post_run_coverage.py` (`post_run_coverage.json`, `post_run_coverage_log.txt`); `post_run_read.py`
    (`post_run_read.json`); `post_run_fox.py` (`post_run_fox.json`); `post_run_exact_m135.py`
    (`post_run_exact_m135.json`); `post_run_records.py` (`census_records.json`).
- Lock: `tests/test_b1529_the_eigenvalue_one_locus.py`.

# B1980 — What could fix the height: the act fixes only cusps on the level-30 curve, and those it fixes are B1976's 96 points; frame C has no duality τ ↦ −K/τ and is not S-covariant, even with its end read on the whole curve, so it reads the curve through the one cusp i∞

**Verdict: PROVED (A, exact) and NEGATIVE (B, no duality of the declared family; frame C fails the S move, also with its end read on the whole curve).** Main,
2026-11-25. Data-free. Register rows P-629, P-845 and P-882 (new). **0 of 19.**

*Dated correction (2026-11-25, B1982; main's own error, the claim retracted):* part B's "frame C fails S, so it reads the curve
through the one cusp i∞" is **withdrawn**.
- Both of its S tests used a wrong law for the canonical end: first the table read outside its domain, then L(τ_FD)
  with no log shift.
- With the record's own law, L(−1/τ) = L(τ) + log|τ| (B1667, B1724, B1921), frame C is exactly S-covariant: 6e-16 at
  three height pairs (B1982). With T exact, frame C is SL(2, ℤ)-covariant.
- The duality family K ≠ 1 was rerun with the end evaluated covariantly at every τ (B1982's `fricke_endlaw.py`):
  no K ≠ 1 passes (largest distances 0.59 to 0.96).
- Part A stands.
- The one hole the author named is the read-out (one thread's act, one point, one level, one height), not the frame.

*Dated relabel (2026-11-25, P-883, at the author's word):* by THE_WEAVE's test (all threads, none chosen; defined by the joint
action; about all threads at once), part A is a **thread** result (m004's monodromy alone acting on X(30)) and part B is
a **frame** result (frame C's dualities). Neither is a weave result. It was first labelled "the weave (the level-30 curve
and the act)".

## Seen first

- **The question,** at the author's word: a principle, derived rather than chosen, that fixes ε = e^{−π Im τ}.
- **The record read first:**
  - B1791 (Im τ not forced in B1656's frame: special points, cusp shapes, apexes, functionals, one loop; the ρ′ peak set by
    a convention);
  - B1696 and B1702 (cusp shapes, sealed NEGATIVE);
  - B1846 and B1847 (the metric's read-out and the level surface's modulus);
  - B1868 and B1923 (no point of the modulus carries weight);
  - the register: P-373, P-380, P-327, P-343, P-382, P-398, P-425, P-629 and P-631.
- **The seats:**
  - the web seat's magnitude ledger, §§ 2 to 4 (its four routes; each finite arithmetic list trades its integers for a
    choice);
  - its P-631 of 2026-11-25 (no two-loop stationary point meets its sealed bound);
  - the agy lane's C40 and C44 (τ fixed by an imported supergravity potential, and moved between them).
- **Swept:**
  - `VERDICT topic-sweep /fix(es|ing)? (the )?(height|tau|eps|modulus)|value of tau|which tau|tau is fixed|stabili[sz]/`;
  - `/cusp shape|2 ?sqrt ?3|2√3|2√−3|sqrt\(-12\)|discriminant -48/`;
  - `/magnitude ledger|replace eps|the scale of eps|eps itself|one continuous/`.

  Their matches are the arcs above. None treats frame C at order 30, the act on X(30), or a duality of frame C.
- **The literature:**
  - the action of SL(2, ℤ/N) on X(N) and its cusps (standard);
  - a fixed point of τ ↦ γτ in H requires γ elliptic (‖tr γ‖ < 2);
  - the self-dual radius of T-duality, as the model of a height fixed by a symmetry.

## Main's reading of the walls (the card's § Why)

- **No preferred depth.** High in the cusp the frame's outputs are C·ε^E. A condition on exponents alone cannot fix ε.
  Something must set ε^ΔE equal to an order-one number the object supplies.
- **The object's geometric numbers are of order one:** cusp shape 3.46, the act's geodesic at 1.1, level surfaces at 1 to
  6. A depth of tens needs a large derived number, and the level is the only one in sight.
- **Three shapes of a derived principle survive these walls:**
  1. a duality of the frame, tested here;
  2. a racetrack from the frame's own effective action, which needs P-629's missing action;
  3. a self-consistent loop.

## Part A — the act on the level-30 curve (`verification/act_level30.py`, exact; `act_level30_run.txt`)

- **M = [[2,1],[1,1]] has order 60 in PSL(2, ℤ/30).** M^k ≡ ±I first at k = 60.
- **No power M^k with k < 60 has a fixed point off the cusps.** tr M^k mod 30 runs through 3, 7, 18, 17, 3, 22, 3, 17,
  18, 7, 3, 2 with period 12, and never meets 0 or ±1. So no element of M^k Γ(30) is elliptic (A1, as expected).
- **The cusps.** X(30) has 288 cusps. The act's orbits on them are 4 of size 12 and 4 of size 60. M fixes no cusp. M^12,
  M^24, M^36 and M^48 each fix 48 (A2, as expected).
- **Post hoc, labelled** (`cusps_are_the_points.py`, `cusps_are_the_points_run.txt`; written after part A was read):
  - **the 48 cusps fixed by M^12 are exactly B1976's 96 points up to sign;**
  - M^12 fixes each of the 96 points itself, and the 96 are closed under p ↦ −p.

  So "order 30 with the 5-part on the act's line", B1976's construction, is the same set as "the cusps of X(30) fixed by a
  power of the act". The menu of points is the act's own.
- **What it means.**
  - The object's own symmetry singles out only cusps on the level-30 curve. That is a derived reason the frame lives in
    the cusp, where the hierarchies are.
  - A cusp has no depth, so the act cannot fix ε.

## Part B — dualities of frame C

### The first run (`verification/duality.py`, `duality_run.txt`), whose end was read outside its domain

- **The test.** On the imaginary axis, the nine log outputs at B1976's 96 points at height y were matched, under any
  bijection, against those at all 899 nonzero points of E[30] at height K/y.
- **The controls held:**
  - C0 (identity), distance 0;
  - C1 (the T move), distance 0. This confirms B1940 on these points.
- **No K passed.** The S move gave 0.11 and 0.26; the others gave 0.59 to 0.96. A post hoc widening for S (any sector
  permutation, either reading, up/down order; `s_wider_posthoc.py`) gave the same 0.11 and 0.26.
- **Main's own fault, found between the run and the landing.** The landing was stopped before any push.
  - Frame C's channel norm reads the canonical end L from B1927's table. That table covers the fundamental domain from
    height 0.866 to 6.
  - Frame C's code reduces only Re τ, so every partner below 0.866 read the nearest table value (2.7193). B1927 makes the
    end a modular function, to be read at τ carried into the fundamental domain.
  - The first run's partners at 2/3 and 0.4 were in exactly that region, so its S verdict was unproven. The correction
    card (`CORRECTION_CARD.md`) was hashed before the rerun.

### The rerun with the covariant end (`verification/duality_cov.py`, `duality_cov_run.txt`)

| cell | outcome |
|---|---|
| K0 (the copied frame, given the same end, against `parts`) | holds; difference 0 at 12 points × 3 sectors × 2 heights |
| the end | L at 0.4i is now 2.3796, the value at 2.5i, where the code had read 2.7193 |
| S-cov (the S move, plain matching) | **fails**: largest distance 0.12, 0.18 and 0.32 (1.25/0.8, 1.5/(2/3), 2.5/0.4) |
| S-cov (wider matching, `s_wider_cov.py`: any sector permutation, either reading, up/down order) | **fails**: 0.12, 0.18 and 0.31; its control at one height gives 0 |
| F-cov (the nine K ≠ 1) | none passes; largest distances 0.59 to 0.96, as before |

- **The end is not the breaker.** Read covariantly, it is S-invariant by construction, and the frame still fails S.
  What breaks S is among:
  - the channel norm F_u, with its π log y;
  - the a₀ term;
  - the characteristic map (a, 2b), whose factor 2 treats the two cycles differently;
  - the Higgs triplet's normalisation.

  These are P-882's Q1.
- **Disclosed and not fixed here:** above height 6 the end is still the table's value at 6, in every run on record.

## What it means

- **No duality of the declared family exists, so no self-dual height is derived this way.** Of the card's three shapes,
  the racetrack and the self-consistent loop remain.
- **Frame C is exactly T-covariant and not S-covariant.**
  - It reads the level-30 curve through one cusp, i∞, out of 288.
  - At the author's word (2026-11-25), this is the same mistake the record made with m004: reading the instrument through
    one hole. It recurs at every level: the object, the point, the cusp, the height, the level.
  - B1978's classes changing along the act's orbits are the same structure heard through different cusps.
  - B1981 shows that the whole instrument is not an average.
- **The next step is to locate the one-hole ingredient.** The end, read covariantly, is not the breaker. What remains is
  F_u with its π log y, the a₀ term, the (a, 2b) characteristic map, and the Higgs's normalisation. Then frame C is
  rebuilt covariant over the whole curve (P-882). Asked of that frame, P-845's class and the height become one question:
  where the object sits on the curve.
- **Nothing here is compared with data.**

# B1409 PREREGISTRATION — THE TOWER'S PARAMETER BUDGET AT ITS CEILING
# (sealed before compute)

**Date sealed:** 2026-09-14 · **Seat:** cc · Gate 5-Q; zero anchors; **no measured
value anywhere in this arc**; nothing reaches `CLAIMS.md`, F2 or Gate 5.

**BANKED IDENTITY:** the object = m004, the figure-eight knot complement; the tower =
its finite covers as enumerated by `snappy.Manifold("m004").covers(d)`; the budget
question is **L217** (registered 2026-09-14, B1406), whose tower row this arc closes.

**PRIOR ART:** Thurston (the `SL(2,ℂ)` character variety of a `k`-cusped hyperbolic
3-manifold has `dim_ℂ = k` at the discrete faithful representation — half-lives-half-dies);
Menal-Ferrer–Porti (`dim_ℂ = k(n−1)` for `SL(n,ℂ)` at the geometric representation composed
with the irreducible `n`-dimensional representation of `SL(2)`) — **cited and explicitly NOT
verified** where B1406 §3 uses it. Weil (the character variety's tangent space is
`H¹(π₁, Ad ρ)`). Internal: **B264** (`dim H¹(π₁(4₁), Ad ρ_prin) = 6 = rank(E₆)`, exact Fox
calculus), **B1297** (Reidemeister–Schreier + Fox calculus + Smith form, exact over
`ℚ(ζ₁₂)`), **B1333** (`exact_rho`, `analyse_exact`, `sym` — the 54 chiral multi-cusped
covers recognised exactly), **B1324/B1295/B1305** (the cover census and its cusp ceiling),
**B1406** (the budget), **B1408** (the discrimination-first rule this arc obeys).

## The question

B1406 §3 priced the object at **`dim_ℂ = 0`** continuous parameters (Mostow) and located
"room" in three places, quantifying none. The tower's ceiling is **5 cusps** — the maximum
anywhere through degree 12 (B1305) — so `k(n−1)` at `n = 3` is `10` complex = `20` real, the
first count in the corpus that clears the ~19 dimensionless parameters a Standard Model needs.

**No character variety has ever been computed on any cover.** This arc computes one.

## The objects (verified before sealing, by the repo's own two-method test)

`frontier/B1324_.../verification/a_arc_b_census.py::amphichiral_two_ways` —
`symmetry_group().is_amphicheiral()` AND an orientation-aware isometry to the reversed copy
with every cusp-map determinant `+1`; both methods agree.

| manifold | appears as | cusps | H₁ | tets | \|Sym\| | role |
|---|---|---|---|---|---|---|
| **L14n63694** = `otet20_00063` | `m004.covers(10)` **[17] and [32]** | 5 | ℤ⁵ | 20 | 8 | **CHIRAL — the target** |
| `otet20_00571` | `m004.covers(10)` **[34]** | 5 | ℤ⁵ | 20 | 80 | amphichiral — **the control** |

Recorded before sealing: covers **[17] and [32] are isometric** (`is_isometric_to` True, same
census identification) — there is **ONE** chiral 5-cusped manifold in the degree-10 tower, not
two. Both are computed anyway, as an internal consistency check: they must agree.

## The computation

`sl₂ ≅ Sym²V` and, under the principal `SL(2) ⊂ SL(3)`, `sl₃ ≅ Sym²V ⊕ Sym⁴V` (3 + 5 = 8).
So the whole budget reduces to `dim H¹(π₁(M), Sym^{2j}V)` for `j = 1, 2`, where `V` is the
geometric `SL(2,ℂ)` holonomy.

- **C1** `exact_rho(M)` (B1333) — the holonomy recognised exactly over `ℚ(ζ₁₂)` by PSLQ.
  HALT if unrecognised; record the halt rather than falling back to floats.
- **C2** `V_j = sym(ρ, 2j)`; `analyse_exact(gens, rels, per, V_j, 2j+1)['a1']` (B1333) —
  `a1 = |Z¹| − (d − a0)` is `dim H¹`, exact, no tolerance anywhere.
- **C3** the same on the amphichiral control and on the second copy of the chiral manifold.
- **C4** controls: `a0 = 0` (irreducibility) on each; the per-cusp `t0`/`t1` recorded;
  `m004` itself run as a positive control, where `k = 1` is known.

## Declared prior (honest, written before compute)

- `dim H¹(Sym²) = 5` — **HIGH**. This is Thurston's theorem on a manifold with `k = 5`.
  Its role here is to **gate the instrument**, not to discover anything.
- `dim H¹(Sym⁴) = 5`, hence `SL(3)` total `10` — **MODERATE-HIGH**. Menal-Ferrer–Porti is a
  theorem, but I have not checked that its hypotheses apply to this cover, and the cover is
  special in a way the corpus has flagged: its cusp shapes include the **hexagonal**
  `½ + (√3/2)i` (B1295 counted 16 hexagonal cusp shapes in the tower and returned NEGATIVE on
  order-3/4/6 cusp rotation).
- **This arc is therefore a verification with low surprise value on its main line, and its
  informative outcomes are the deviations.** Stated so that a confirmation cannot later be
  narrated as a discovery.

## Two-outcome (MB12: each can pass and fail)

| outcome | reading |
|---|---|
| `H¹(Sym²) = H¹(Sym⁴) = 5`, total **10** | the budget is real at the tower's ceiling; `k(n−1)` verified in the one place the programme needs it; **L217's tower row closes POSITIVE** |
| either `≠ 5` | the room is **not** realised at the best case in the searched tower; B1406's "room is in the tower" reading is **refuted at its own ceiling**; L217's tower row closes NEGATIVE |
| `a0 ≠ 0`, or the chiral/control pair disagrees where they must agree, or `exact_rho` halts | **instrument failure** — the arc reports the halt and stops; no dimension is banked |

## Kill conditions

- **C1 halts (PSLQ does not recognise the rep)** → report and stop. Do not substitute floats.
- **The `m004` positive control does not return `k = 1`** → the instrument is wrong; stop, and
  flag every adjacent result that used it.
- **The two isometric copies [17] and [32] disagree** → stop; a presentation-dependent answer
  is not a dimension.

## Fences, standing

1. A dimension is **room**, not parameters. Nothing selects a point in it; the corpus has **no
   cover-selection principle** (L202 is a test, not a selector; B432's fence is *"slope
   selection stays free input"*), and R11 would charge for one.
2. The dimension is **independent of chirality** — the amphichiral control is expected to give
   the same number. Chirality matters for what the room could later carry, not for whether it
   exists.
3. `LISTENER_MAP_SPEC` **F2** stands: the value-contact surface is exhausted and this arc does
   not reopen it.
4. B1333's index result (zero over 38 070 sectors) is **not contested**; `H¹` and the index are
   different quantities.
5. Every rank is taken over the field the answer lives in (**E73**); nothing is identified by
   its printed form (**E75**); no float stands where exactness is claimed.

## What a positive result does NOT license

It does not produce a parameter, a coupling, or a prediction. It closes one row of an
accounting ledger. The next question — **what selects a point** — is unpriced, and saying so
is part of this preregistration rather than a concession made afterwards.

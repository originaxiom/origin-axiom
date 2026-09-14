# B1409 — THE TOWER'S BUDGET IS REAL, IT IS EXACTLY 20 REAL PARAMETERS,
# AND EVERY ONE OF THEM IS BOUNDARY DATA (2026-09-14)

**Prereg sealed `5618216a` and pushed at `31cfd032` BEFORE any compute.**
Zero anchors; no measured value anywhere; nothing reaches `CLAIMS.md`, F2 or Gate 5.

## 0. THE RESULT

At the tower's ceiling — the chiral 5-cusped degree-10 cover **L14n63694** — the
character variety's dimension at the geometric representation is

    SL(2,ℂ):  dim_ℂ H¹(π₁, sl₂) = 5  = k
    SL(3,ℂ):  dim_ℂ H¹(π₁, sl₃) = 10 = k(n−1)   →  20 REAL PARAMETERS

**The budget is real.** It is the first count in the corpus that clears the ~19
dimensionless parameters a Standard Model needs, and Menal-Ferrer–Porti's `k(n−1)` —
**cited and explicitly unverified** where B1406 §3 leans on it — is now verified in the
one place the programme needs it. **L217's tower row closes POSITIVE.**

**And then the part that was not preregistered because it was not anticipated:**

    the restriction  H¹(M) → H¹(∂M)  is INJECTIVE, in every case
    dim H¹(∂M) = 10 = 2 · dim H¹(M)   — half-lives-half-dies, exactly

> ### Every one of the 20 real parameters is CUSP DATA. There are ZERO interior moduli.

The room exists, it is big enough, and it is **made entirely of the thing the programme
already knows it cannot select.**

## 0a. A CLAIM IN THE SEALED PREREG IS WRONG, AND THE CORRECTION IMPROVES THE ARC

The preregistration says *"No character variety has ever been computed on any cover.
This arc computes one."* **That is false, and the seal is not edited to hide it.**

`mcexact.analyse_exact` **returns `a1` in its output dict**, and B1333 called it on all 54
chiral multi-cusped covers — **these two among them** — across 38 070 sectors. The tangent
dimension was therefore computed **tens of thousands of times and never printed**: that arc
was chasing the index `I = t₀ − r₁` and reported only `(c, live, t₀, I)`.

**The honest claim is not "nobody has computed it" but "it has been computed and never
read."** Which makes this a *reporting-and-certification* arc rather than a new computation,
and a much easier thing to defend.

Two things do survive as genuinely new:
- the **exact, characteristic-zero** run at the `Sym²⊕Sym⁴` germ. B1333's logged exact pass
  (`verification/logs/exact_5cusp.log`) ran germ `Sym²` only; the `(2,4)` germ was run **mod
  p**, and a mod-`p` rank is one-sided (`rank mod p ≤ rank char 0`), so it bounds and does
  not determine. The SL(3) number here is char-0 and exact.
- the **injectivity reading** of §3, which no arc had drawn from numbers it already had.

*(Adjacent, recorded not fixed: fifteen of B1333's committed scripts `sys.path.insert` and
open `/tmp/sweep/covcache.json` by absolute path, so that verification directory is not
runnable from a clean checkout. This arc does not depend on the cache — `exact_rho`
recomputes — but the hole is real and belongs in the error ledger.)*

## 1. THE NUMBERS

| manifold | role | k | germ | `dim H¹(M)` | `dim H¹(∂M)` | image | injective |
|---|---|---|---|---|---|---|---|
| m004 | **positive control** | 1 | `Sym²` | **1** | 2 | 1 | yes |
| m004 | | 1 | `Sym⁴` | **1** | 2 | 1 | yes |
| **L14n63694** `[17]` | **chiral, the target** | 5 | `Sym²` | **5** | 10 | 5 | yes |
| **L14n63694** `[17]` | | 5 | `Sym⁴` | **5** | 10 | 5 | yes |
| L14n63694 `[32]` | same manifold, 2nd presentation | 5 | both | **5, 5** | 10, 10 | 5, 5 | yes |
| `otet20_00571` `[34]` | **amphichiral control** | 5 | both | **5, 5** | 10, 10 | 5, 5 | yes |

`a₀ = 0` throughout (every representation irreducible). Per-cusp `t₀ = 1`, `t₁ = 2`,
uniformly across all five cusps — the room is **2 complex numbers at each cusp**, not a
pooled 10.

All four kill conditions cleared: the **m004 control returns `k = 1`**; the two isometric
presentations **agree exactly**; `exact_rho` recognised every holonomy over `ℚ(ζ₁₂)` with no
float fallback; `a₀ = 0` everywhere.

## 1a. THE CONTROL THAT MATTERS: `a₁` TRACKS `k`, ACROSS THE WHOLE TOWER

A single number at `k = 5` could be an artefact. So the sweep was run over **every** chiral
multi-cusped degree-10 cover, selected **by property** (`num_cusps ≥ 2` and not amphichiral),
never by list index — identifying a manifold by its position in SnapPy's output is E75's
shape exactly. Two representatives per cusp-count:

| `k` | covers | `a₀` | `dim H¹(sl₂)` | `dim H¹(sl₃)` | `r₁` | `n = a₁ − r₁` |
|---|---|---|---|---|---|---|
| 2 | [5], [7] | 0 | **2** | **4** | 4 | **0** |
| 3 | [0], [1] | 0 | **3** | **6** | 6 | **0** |
| 4 | [3], [13] | 0 | **4** | **8** | 8 | **0** |
| **5** | **[17], [32]** | 0 | **5** | **10** | 10 | **0** |

> **`dim H¹ = k(n−1)` exactly, in BOTH parameters, on this object's own covers.** That is
> Menal-Ferrer–Porti verified as a two-parameter law, not as a single coincidence — and it is
> the right control because the thing that could break (`k`) is the thing that varies (E67).

> **And `n = 0` on every row: the restriction to the boundary is injective on EVERY chiral
> multi-cusped cover in the degree-10 tower, not just at the ceiling. There are no interior
> moduli anywhere in the tower.**

Property selection also confirms the target: exactly **two** chiral 5-cusped covers, `[17]`
and `[32]`, which are the same manifold.

## 2. `sl₃ = Sym² ⊕ Sym⁴`, AND WHY THAT IS THE WHOLE COMPUTATION

`sl₂ ≅ Sym²V` for `V` the standard 2-dimensional representation, and under the principal
`SL(2) ⊂ SL(3)`, `sl₃ ≅ Sym²V ⊕ Sym⁴V` (3 + 5 = 8). So the SL(3) budget is the sum of two
`H¹`'s with coefficients in symmetric powers of the geometric holonomy — no Ptolemy variety
is needed, and none was tractable: `ptolemy_variety(3, obstruction_class="all")` on this
cover returns **122 varieties in 80 variables**.

Exact over `ℚ(ζ₁₂)` end to end, reusing B1333's `exact_rho` (PSLQ), `fi_lib.sym`, and
`mcexact.analyse_exact`, whose `a₁ = |Z¹| − (d − a₀)` **is** `dim H¹`. No tolerance appears
anywhere in the computation (E75).

## 3. THE FINDING THE PREREG DID NOT ANTICIPATE

The preregistration declared a HIGH prior on both numbers and said so explicitly, precisely
so that a confirmation could not later be narrated as a discovery. Both came back as the
theorems say. **The informative content is the structure, not the count:**

`H¹(M) → H¹(∂M)` injective, with image exactly half of `H¹(∂M)`, means the image is
**Lagrangian and the map loses nothing**. Every deformation of the flat connection is
visible at the boundary, and is *determined* by its boundary restriction.

**There is no deformation of the interior.** The object has no bulk moduli at any rank the
corpus can reach, on the largest-cusped manifold anywhere in its tower.

This is B1406's riddle-2 answer made quantitative. That arc argued the object is a
*boundary*; this one measures it: **100% of the available continuous room is boundary data,
0% is interior.**

## 3a. ADDENDUM — THE RANK LADDER: `k(n−1)` AT `n = 2, 3, 4`, AND STILL NO INTERIOR

`sl₄` under the principal `SL(2)` is `Sym² ⊕ Sym⁴ ⊕ Sym⁶` (3+5+7 = 15). Run on both the
positive control and the ceiling:

| manifold | `k` | `n=2` (`d=3`) | `n=3` (`d=8`) | `n=4` (`d=15`) |
|---|---|---|---|---|
| m004 | 1 | **1** | **2** | **3** |
| L14n63694 | 5 | **5** | **10** | **15** |
| *predicted* `k(n−1)` | | `k` | `2k` | `3k` |

`a₀ = 0` and `n = a₁ − r₁ = 0` on **every** row. Cost `0.1 s → 1.6 s → 9.2 s` at `k=1`, and
`1.3 s → 17.1 s → 99.1 s` at `k=5`.

> **So the rank direction supplies exactly `k` more complex parameters per rank step, and
> every one of them is boundary data too. Raising the rank does not buy an interior
> modulus — it buys more cusp data.**

That closes **L217's rank row** alongside its tower row, and sharpens the §3 finding from a
statement about `SL(3)` to a statement about the whole ladder the corpus can reach.

## 4. WHAT THIS LICENSES — AND WHAT IT DOES NOT

**Licensed (and this is real):**
- The tower's room is **real and sufficient in count**: 20 real ≥ 19. B1406's "room is in
  the tower" survives its own best-case test.
- `k(n−1)` is **verified**, not cited, at `k = 5, n = 3`.
- The dimension is **chirality-blind** — the amphichiral control returns the identical
  numbers, exactly as the prereg's fence predicted. Room and chirality coexist on this
  manifold without interacting.
- **L217's tower row closes**, with a number and a structure.

**NOT licensed, and the prereg said so before the numbers existed:**
- **A dimension is room, not parameters.** Nothing selects a point in it.
- And §3 makes the selection problem *worse*, not better: since all 10 are cusp-local, a
  selection is a choice of boundary data at each of 5 cusps — **structurally the same
  unpriced free input as a Dehn slope**, which the corpus has carried as *"slope selection
  stays free input"* (B432) since 2026, and which B322 already tested against SM parameters
  at **chance level** (8/12 vs null 7.6).
- R11 would charge for that selection. Nothing here pays it.

> **The honest one-line reading: the programme has found where its parameters could live,
> and it is exactly the place it has never been able to select from.**

## 5. FENCES

- No value is compared to any measurement. `LISTENER_MAP_SPEC` **F2** stands.
- B1333's index result (zero over 38 070 sectors) is **not contested** — `H¹` and the index
  are different quantities computed here with the same instrument.
- Menal-Ferrer–Porti and Thurston are **cited**; this arc verifies their counts on specific
  manifolds, it does not reprove the theorems.
- Every rank exact over `ℚ(ζ₁₂)`; `a₀ = 0` asserted, not assumed; the positive control is
  part of the result, not a footnote.
- The degree-10 tower's 5-cusp ceiling is **B1305's**, searched to degree 12; nothing here
  claims anything about deeper covers.

Artifacts: `verification/b1409_budget.py`, `verification/b1409_budget.json`.
Locks: `tests/test_b1409_tower_budget.py`.

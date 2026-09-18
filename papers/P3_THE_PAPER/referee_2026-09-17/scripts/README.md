# The referee's independent reproductions — 2026-09-17

These are the scripts behind §2 of `../../REFEREE_REPORT_2026-09-17.md`. They were written from
`main.tex`'s own prose on a clean machine. **None of them imports, reads, or calls anything from
this repository**; they use only SnapPy's census, sympy, mpmath, numpy and the PARI bundled with
SnapPy. They are deliberately independent of the project's `verification/` scripts, so that agreement
between the two is evidence and not a shared implementation.

## Install

```
python3 -m pip install "snappy==3.3.2" sympy mpmath numpy
```

## What each one checks

| script | manuscript claim | runtime |
|---|---|---|
| `v1_matrices.py` | `M² = LR`; `F = LP` is the unique orientation-reversing integer square root up to sign; no orientation-preserving root; `L_aR_b` has one iff `a = b`, with 12 controls | ~10 min (exhaustive box search) |
| `v2_algebra.py` | Prop. 4.1 in every part (incl. the seven involutions of `SL(2,Z/4)`); 252/222 content census; the `−18(t−3)(t+3)` cubic; the 3/8 traces; E₆/E₈ branchings; `\|H₁(Yₙ)\|`; `\|det(A−I)\| ∈ {0,…,4}` | seconds |
| `v22_content_census.py` | the full §6 census: 252 → 222 killed → 12 after Witten → **two contents, four rays** | ~1 min |
| `v6_baserate.py` | `145/400`, `124/400`, the class-count distribution, the tie list, `1696/5000`. Pass the sample size as argv[1] | seconds (400) / ~2 min (5000) |
| `v21_drift3.py` | the depth blocks at 0 / 20 000 / 80 000, run on **both** the full and the one-cusped census — the discrepancy of §4.4 | ~15 min |
| `v14_three_defs.py` | the count of three, under both readings of "cusp-fixing": 20 of 212 641 and 2 of the first 4000 | ~3 min |
| `v16_family.py` | the 112-member ℚ(√−3)-shape family, its 38/74 chirality split and its 59/35/18 door split | ~40 min |
| `v5_chirality.py` | the 87 covers to degree 10: 66 chiral by two orientation-aware tests agreeing on all 87, with classical controls | ~5 min |
| `v25_signs.py` | the sign-pattern census: 2794 inversion-only / 7 nothing / 3 full set | ~20 min |
| `v4_fill_cov.py` | ten exceptional fillings; 78 closed hyperbolic in the grid; mirror-pair isometry; cover and cusp counts | ~10 min |
| `v8_misc.py` | hexagonal cusps (14 covers, 16 of 201); 2804 with H₁ = ℤ; covolume index 12 | ~10 min |
| `v9_lvalue_koide.py` | `Vol(m004) = 9√3 ζ_K(2)/π²` to 60 dp; the Koide angle at 0.89 σ from 2/9 | seconds |
| `v11_2O.py` | no surjection `π₁(m004) ↠ 2O`, with 2O built as 48 unit quaternions over `Q(√2)` | ~2 min |
| `v26_bundles.py` | the Summary's punctured-torus-bundle witness: four *primitive* arithmetic words of length ≤ 7, two of them a chiral mirror pair over ℚ(√−7) | ~10 min |

## Two notes on method

**Counting surjections up to automorphism.** `Aut(G)` acts *freely* on surjections onto `G` (if
`α∘φ = φ` with `φ` onto then `α = id`), so the count up to automorphism is exactly
`#surjections / |Aut(G)|`. For `G = SL(2,3)`, `|Aut| = |S₄| = 24`. No orbit enumeration is needed and
the quotient is exact. The m004 control is 48 raw surjections → 2.

**Orientation-aware chirality.** SnapPy's default `M.is_isometric_to(mirror(M))` is
orientation-blind and reports all 87 covers as amphichiral. `v5_chirality.py` uses two orientation-aware
tests — `SymmetryGroup.is_amphicheiral()`, and the existence of an isometry to the mirror all of whose
cusp maps have determinant +1 — checks they agree on all 87, and validates them against classical
controls (m004 and 4₁ amphichiral; m015, m006, 5₂ chiral).

## A late addition

`v28_subfields.py` was added after a first attempt at the arithmetic fillings failed. The lesson is
worth recording because it is the same one B1419 records (E82): **the instrument has to match the
domain.** For an ideally triangulated *cusped* manifold the invariant trace field IS the shape field
(Neumann–Reid), so `algdep` on the shapes settles it. For a *Dehn-filled* manifold it is not — the
shape field is strictly larger and the invariant trace field is a **subfield** of it. Testing the
filled slopes as though they were cusped returns degree 8 and degree 6 fields and an apparent
mismatch with the paper; testing them as subfields returns the claimed quartic and cubics exactly,
as the unique proper subfield in each case.

A second caution in the same script: at SnapPy's ~60-digit precision `algdep` returns a spurious
relation at *every* degree, with coefficients of size 10^40 and residuals as small as 1e-21. A
residual threshold alone will therefore accept a wrong answer. `minpoly()` here bounds the
coefficients as well, and the open object is carried through as a positive control
(`x^2 - x + 1`, disc −3).

## Round 2 (the S18/S19 revision)

| script | what it checks | result at `21c47a51` |
|---|---|---|
| `r2_chain_table_drift.py` | every generated chain-table row against the paper, not the 9 the shipped gate samples | **1 of 57 stale** (link 43: generator 0.8 %, paper 0.9 %) |
| `r2_lock_data_tracked.py` | whether any of the 147 manifest locks reads a present-but-untracked data file — the regression check for round 1's worst defect | **0** — the S19 sweep holds |

Both run from the repository root and exit non-zero on a finding. Each documents its own method and
its limit in the docstring; `r2_lock_data_tracked.py` in particular is evidence and not proof, since
a lock building its path dynamically would escape a literal-string scan.

## Round 3 (the project, not the projection)

These check the branch-only lanes — the record the paper is a projection of — rather than the
manuscript. They use SnapPy for presentations only; characters, Fox calculus, cohomology, ranks and
all field arithmetic are the scripts' own.

| script | what it checks | result |
|---|---|---|
| `r3_i26_euler.py` | I-26's Euler-characteristic correction | reproduces |
| `r3_m010_index.py` | R27's m010 witness: exact ℚ(u) arithmetic, Sym^m, Fox calculus, H¹ | **I = +1** on V=(0,1,1,0) / V*=(0,2,1,2); semisimplification gives 0; same trace on 400 random words |
| `r4_r30_check.py` | R30's finite-width vanishing: conjugation identity, f·v=0, the Betti table, the §3 chain homotopy, P at all eight non-trivial order-3 characters | every pillar reproduces; **P ≠ 0 at all eight** |
| `r5_tower_loci.py` | the mechanism behind "one generation, never three" on Y2/Y3/Y4 | **h¹(χ²) = 1 at every non-split locus**, across three prime fields |
| `r6_h1_three.py` | is h¹(χ²) = 3 reachable at all — every cover of m004 to degree 8 plus the named family | **0 genuine loci at h¹ = 3**; {1: 20904, 2: 456}, the twos only on multi-cusped manifolds |
| `r7_corank_bound.py` | *why*: Δ(m004) from its own Fox Jacobian, and cusps → max h¹ | Δ = t²−3t+1, discriminant 5, **separable**, roots off the unit circle; **no one-cusped manifold in the scan carries h¹ ≥ 2** (1056 loci) |

A trap `r6` documents rather than hides: a raw scan reports 32 loci at h¹ = 3 on the degree-7
covers. Those χ have order 2, so χ² is trivial and h¹(χ²) = b₁ = 3 for free on a three-cusped
cover. Filtering to χ² non-trivial — the genuine extension loci — removes all 32.

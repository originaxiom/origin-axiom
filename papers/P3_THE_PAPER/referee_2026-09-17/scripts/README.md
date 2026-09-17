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

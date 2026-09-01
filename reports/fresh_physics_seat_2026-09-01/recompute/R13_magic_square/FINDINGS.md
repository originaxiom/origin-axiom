# R13 — B904 magic-square isomorphism, blind recomputation (Ring R2)

**Cell:** R13 · **Date:** 2026-09-01 · **Verdict: MATCH** (one convention mismatch resolved per E23; one banked number, det φ, identified as non-invariant — noted, not a discrepancy)

## Banked claim (as read before computing)

The programme's E6 build IS M(O,C) — the split Barton–Sudbery cell L(O_split, C'_split)
over Q — by explicit structure-constants isomorphism. Banked numbers: tri(O) dim 28,
tri(C') dim 2, tiling 28+2+3·16 = 78; derived cross products (1,2)→3: xy, (2,3)→1: y·x̄,
(3,1)→2: ȳ·x (C'-side zw, z̄w, zw̄); fitted scalars λ≡1, μ≡−24, ν≡−12; FULL JACOBI
0/76,076; 72 one-dim rational root spaces + 6-dim Cartan; Cartan matrix = E6; φ verified
on all 3,003 basis pairs, 0 mismatches, det φ = −2/3.

## Blind-first discipline: what was read when

**Before writing my code:** arc FINDINGS.md (all of it — prose + numbers, no code);
the arc's small JSON result files (banked numbers only); pickle KEY listings (storage
shape, not values); grep of import/`open(` lines of stage4b/4c solely to locate where
"the build" lives (answer: exec of `B854_centralizer_exact/e6_centralizer.py`); the
full text of **B854's** `e6_centralizer.py` (the *definition of the build* — the object
under test — not B904's verification code). **Not read before the diff:** any other
line of B904's stage1/2/2b/2c/3/4/4b/4c scripts, `tests/test_b904_bs.py`, the banked
φ values, or the banked tensor values.

**After my results were locked (post-diff):** B904 stage scripts (convention
comparison), the lock test (run), the banked tensor + φ (verified with my own checkers).

## My blind construction (all files in this cell dir)

- `octonion_core.py` — my own Zorn split octonions + split binarions over Q; selftest:
  norm multiplicativity, alternativity, conjugation, non-associativity witness — PASS.
- `triality.py` — tri as exact nullspace (identity + skewness wrt polar form):
  **dim tri(O) = 28** (raw identity-only space: 30, the 2 scalar directions killed by
  skewness), **dim tri(C') = 2** (raw 4). Matches banked stage 1.
- `assemble.py` — equivariance scan over my own candidate sets (8 octonion products ×
  3 slots, 4 binarion products × 3 slots), all 28 tri triples × 64 basis pairs:
  **unique survivor per slot**: (1,2)→3: xy; (2,3)→1: y·x̄; (3,1)→2: ȳ·x; C'-side
  zw, z̄w, zw̄ — identical to the banked derived products (found independently).
  Duals built as exact Killing-duals wrt the three-component trace form; tri brackets
  closed exactly.
- `fit_jacobi.py` — 9 scalars fitted on Jacobi probes: unique solution family
  **μ_i = −6 λ_j λ_k, ν_i = −3 λ_j λ_k** (λ free = the V_i rescaling gauge).
  Gauge-fixed λ≡1 → μ≡−6, ν≡−3.
- `full_jacobi.py` — FULL exact Jacobi (denominators cleared, int64 einsum,
  overflow-bounded): **0 failures on all 76,076 unordered triples** (and all 474,552
  ordered). Killing rank 78. **Planted-positive control:** one structure constant
  shifted by 1 → 330 ordered triples fail. The check can fail; it doesn't.
- `roots.py` — torus = {A diagonal} ⊂ tri(O) (dim 4) + tri(C') (dim 2); joint
  ad-eigenspaces exact over Q: **72 one-dim rational root spaces + 6-dim Cartan**;
  roots closed under negation; 36 positive, 6 simple; Cartan matrix from the Killing
  form **matches E6 exactly** (my permutation (4,3,0,2,1,5) wrt my own simple-root
  ordering; the banked (4,3,1,2,0,5) is wrt theirs — orderings differ, the invariant
  statement E6 is the same).
- `iso.py` — build side re-implemented from B854's definition (E6 Cartan + epsilon
  cocycle). **My full Jacobi on the build: 0/76,076** (strengthens B854's own
  4000-triple sample). My own Chevalley generators on both sides ([h,e]=2e etc.
  verified, Cartan action = Bourbaki E6 on both), extension by identical bracket
  words to a rank-78 basis, φ = W2·W1⁻¹:
  **φ([a,b]) = [φa, φb] on ALL 3,003 unordered basis pairs — 0 mismatches.**
  det(my φ) = −2^25/3. **Planted-negative control:** corrupting one generator
  scaling (e₃ → 2e₃ on the build side) before the identical-word extension gives
  16/60 mismatches — the homomorphism check can fail; it doesn't.

## Post-diff verification of the banked artifacts (`verify_banked.py`)

- Their `stage2c_tensor.pkl` through MY full-Jacobi checker: **0/76,076** ✓ (banked: 0).
- B854 run byte-faithfully (in a sandbox copy; its results.json rewrite kept out of the
  arc dir); its BB tensor vs my re-implemented build tensor: **0 differing entries**
  out of 78³ ✓.
- Their banked φ (`stage4c_phi.pkl`), checked with MY bracket evaluators as a map
  their-BS → build: **0/3,003 mismatches**, det = **−2/3** ✓ (banked: 0, −2/3).
- Committed lock `tests/test_b904_bs.py`: **6 passed**.

## Diffs and their resolutions

| item | banked | mine | resolution |
|---|---|---|---|
| tri dims 28 / 2, tiling 78 | 28/2/78 | 28/2/78 | MATCH |
| derived products (both algebras) | xy, y·x̄, ȳ·x; zw, z̄w, zw̄ | identical, unique survivors | MATCH |
| scalars | λ=1, μ=−24, ν=−12 | λ=1, μ=−6, ν=−3 | **convention (E23)**: their `opair`/`cpair` are half my polar forms; two pairings enter the same-summand bracket → factor 4. μ/ν = 2 in both. Resolved → MATCH |
| full Jacobi | 0/76,076 | 0/76,076 (mine AND theirs re-checked) | MATCH |
| root split | 72×1-dim + 6 | 72×1-dim + 6 | MATCH |
| Cartan matrix | E6 (perm (4,3,1,2,0,5)) | E6 (perm (4,3,0,2,1,5) wrt my ordering) | MATCH (permutation is ordering-relative, invariant = E6) |
| φ homomorphism | 0/3,003 | my own φ 0/3,003; their φ re-verified 0/3,003 | MATCH |
| det φ | −2/3 | my φ: −2^25/3; their φ re-checked: −2/3 | **not an invariant** — φ is unique only up to automorphisms/generator rescalings; det is a property of their particular choice and reproduces exactly when their φ is re-checked. No discrepancy. |

## Vacuity assessment

Not vacuous: both checks (Jacobi, homomorphism) demonstrably fail under planted
corruptions (330 failing ordered triples; 16/60 failing pairs). The claim's uniqueness
content ("unique equivariant survivor per cross slot") was reproduced blind with an
independently written candidate list.

## Verdict

**MATCH.** The Barton–Sudbery algebra rebuilt from scratch over Q reproduces every
banked number; the isomorphism to the build was found independently (my own generators,
my own words, my own φ) and the banked φ itself re-verifies under independent checkers.
B904's claim stands exactly as banked.

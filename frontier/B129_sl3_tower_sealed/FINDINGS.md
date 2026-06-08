# B129 — The SL(3) tower is sealed in ℚ(√−3): the firewall from inside the tower (V118)

The arc *after* B128 (PR #144). The "last door" the B128 fork pointed at: **does climbing the SL(n) tower produce new
content — a genuine irreducible non-abelian fixed point with new arithmetic — or is the tower just the single SL(2)
Fibonacci datum re-expressed in larger irreps?** Re-derived in-sandbox (verify-don't-trust), controls-validated.

**One-line result.** The metallic SL(3) tower (principal Sym² route) is **irreducible-as-a-rep but arithmetically
SL(2) data in SL(3) clothing** — all traces in ℚ(√−3) — and an off-sublocus fixed-class search over the 4-dim SL(3)
bulk finds **zero** fixed points that escape ℚ(√−3). The tower never acquires a new modulus, a new field, or an
irreducible non-abelian factor. This is the **sixth** independent confirmation of the fundamental-physics firewall —
the first taken from *inside* the tower. MATH and physics in **different tiers**. Nothing to `CLAIMS.md`; P1–P16, the
functorial `Sym(W)→trace-ring` wall (B85), and the merged B124–B128 (K010/K011/P007/P008/S029/S030) untouched.

## The result

- **S1a — the principal Sym² metallic SL(3) rep is SL(2) arithmetic in SL(3) clothing (EXACT, the load-bearing leg).**
  Build the figure-eight (m=1) SL(2) Fibonacci rep `A₂=[[1,1],[0,1]]`, `B₂=[[1,0],[−ω,1]]`, `ω = ½ + √−3/2` (cusp
  shape in ℚ(√−3)), and push it through the **principal embedding** SL(2)→SL(3) (the symmetric square `Sym²`, the
  embedding the trace-map tower produces). Verified symbolically (sympy, exact): the pair is **irreducible as a
  representation** — the algebra it generates is all of `M₃` (dim 9) — **yet every trace invariant lies in ℚ(√−3)**:
  `trA = trB = 3` (unipotent), `trAB = ½ − (3√3/2)i`, `trA⁻¹B = 9/2 + (5√3/2)i`, `tr[A,B] = ½ + (3√3/2)i`. No new
  field, no new generator, no new modulus — the SL(3) trace ring is a **reparametrization** of the SL(2) Fibonacci
  data, not an enrichment. *(So "irreducible non-abelian rep" alone is not the right bar — this clears it and still
  doesn't bridge.)*

- **S1b — no off-sublocus fixed point escapes ℚ(√−3) (computer-assisted; a distribution, not a count).** The SL(3)
  once-punctured-torus character variety is **4-dimensional** (vs SL(2)'s 2-dim). The firewall question is whether the
  metallic trace map has a fixed point *off* the SL(2) sublocus with new arithmetic. **Search method matters:** the
  trace map is a **hyperbolic horseshoe** (`K010`), so its fixed points are **saddles** — forward iteration *flees*
  them. We therefore **root-find** for genuine fixed conjugacy classes via `tcoords(A,B) = tcoords(AB,A)` (Lawton's 9
  SL(3) trace coordinates; the m=1 metallic monodromy `φ(A,B)=(AB,A)`, which abelianizes to `M₁=[[1,1],[1,0]]`),
  seeding **off-sublocus** (`A` gauge-fixed diagonal with distinct eigenvalues, `B` generic SL(3,ℂ)). A **15-seed ×
  30-start scan gives 427 converged fixed points; the maximum distance-to-ℚ(√−3) over all 427 is 1.2e-6** (median
  8e-9, 99% 9.8e-7) — **0 points beyond 1e-5**, with a clean gap to the `>1e-3` distance a genuine algebraic escape
  would require. **⟹ the tower is sealed in ℚ(√−3).** The search lands overwhelmingly on the reducible sublocus +
  degenerate trivial/central reps (traces in `{1,−1,3,…} = ℚ`); the only genuine irreducible content is the **Sym²
  image** (S1a, exact, in ℚ(√−3)).

- **S1c — the interpretation (MATH; firewall reading POSTULATED).** The SL(n) tower is the single SL(2) Fibonacci
  datum (field ℚ(√−3), one coupling) re-expressed in successively larger irreps `Sym^{n−1}`. It never learns a second
  arithmetic language. Climbing `n` raises the **matrix size, not the information** — consistent with `K010`'s
  multichannel reading: `n` channels, **one** coupling, no non-abelian gauge factor.

## The corrected firewall statement (cleans the S029 rank-1 fence)

A prior **chat-only over-claim** (never banked) said the firewall is "rank-1 because single-word bundles are
one-cusped, structurally sealed at rank 1." That is wrong: the **bundle** is one-cusped rank-1 abelian, **but its
finite covers are multi-cusped and rank-2** — the silver bundle `b++RRLL` has degree-2 covers reaching
`(cusps, free_rank) = (2,2)` (verified, SnapPy). The firewall survives anyway because a cover's extra cusps are
**copies of the same boundary torus** permuted by the deck group — `T[cover]` is a discrete gauging of copies of the
rank-1 abelian `T[M]`, **not** a new irreducible non-abelian theory (same lesson as the torsion, B128/`K-F`). So:

> **Corrected statement (use everywhere): the metallic family produces *abelian × discrete*, never an irreducible
> *simple non-abelian* factor — *not* "rank is always 1."** Rank can grow by covering, but only by **replication**.

## Two method bugs (test-infra; banked so no future run repeats them)

Both produced **false "reopenings"** of the firewall (a reflexive *revival*, the opposite failure mode to a reflexive
kill), and **this verification independently re-encountered both** — bug B2 here nearly produced a false *refutation*.

- **B1 — the `inQ3` rational-detector bug.** A detector for `z = a + b√−3` that rejects **pure rationals**
  (`1 = 1 + 0·√−3` *is* in ℚ(√−3)) mislabels them as escapes. *Fix:* test rationality of `Re(z)` **and** of
  `Im(z)/√3` directly. *(Second-order trap found here: `Fraction.limit_denominator(10000)` is too permissive — by
  Dirichlet it approximates almost any real, so it would accept genuine escapes too; use a **small** maxden (100) since
  the genuine traces have small height.)*
- **B2 — finite/central masquerade under loose tolerance.** On a hyperbolic map, the solver lands on **degenerate**
  (trivial/central) fixed points with slightly-off traces (`0.99998` vs `1`) that dodge a too-tight rationality test —
  faking an escape at the residual floor. Note the genuine figure-eight rep is **unipotent** (`|eig|=1`), so
  eigenvalue-modulus does **not** separate genuine content from trivial reps. *Fix:* root-find (don't iterate); the
  robust escape test is a **polished distance**: re-solve from the candidate, then measure deviation from ℚ(√−3) with a
  threshold (`1e-4`) set ~100× above the artifact band (max observed 1.2e-6) and ~10× below any real escape. The
  0-escape count is then stable (no flicker).

These join the B128 chirality bug (use `symmetry_group().is_amphicheiral()` gated on `is_full_group()`, not naive
isometry/CS sign). All three live in `REPRODUCIBILITY.md` SCAN.

## Honest scope (verify-don't-trust)

- **Searched:** m=1 (figure-eight); two routes — principal Sym² (exact, S1a) + bulk root-find (15 seeds, 427 points,
  S1b). No escape.
- **Reproduction note (stated to not over-claim):** the handoff reported a clean 22/56/0 reducible/finite/genuine
  classification; this reproduction finds the bulk search lands almost entirely on degenerate/reducible points and
  **rarely converges to the genuine Sym² saddle** from random starts — so the load-bearing S1b evidence is the
  **distance distribution** (max 1.2e-6 over 427 points) together with the **exact** S1a, not a reducible/finite
  tally. The conclusion (0 escapes; genuine content = Sym² image, sealed in ℚ(√−3)) is the same and is robust.
- **NOT done:** per-m bulk search for m≥2 (S1a checked symbolically for m=1); the analytic capstone. **Strong
  computational result, NOT a theorem.**
- **Capstone (open MATH target, `speculations/S031`; NOT a physics bridge):** prove the metallic SL(n) trace map fixes
  **only** the `Sym^{n−1}` image of its SL(2) fixed point, for all m, n.

## Reproduce

```
python frontier/B129_sl3_tower_sealed/probe.py
python -m pytest tests/test_b129_sl3_tower_sealed.py -q
```

S1a (exact sympy) and the `inQ3`/`dist` detector regression always run; the off-sublocus search (S1b) is
scipy-guarded, the silver covers (S2) SnapPy-guarded — both skip cleanly when the tool is absent (records stand).

**Tier.** MATH (low-dim topology / character varieties) + a firewalled physics reading (POSTULATED). The naming is
`knowledge/K012`; the rank-1 fence `S029` is **strengthened** (abelian × discrete); `P007` gains the **sixth**
direction; the two method bugs go to `REPRODUCIBILITY.md`; the capstone is `S031`. Nothing to `CLAIMS.md`; P1–P16,
B85, B124–B128 untouched. Ledger **V118**.

**Anchors:** B128 (the fork this answers; `K-F`/`S029`), `K010` (the horseshoe/multichannel naming), `K011`, `K001`
(Lawton/Fricke trace coordinates), `S029` (the fence, strengthened). External: Lawton (SL(3) trace coordinates 2007);
Kohmoto–Kadanoff–Tang; Damanik–Gorodetski (the horseshoe); SnapPy (`b++` bundles, covers).

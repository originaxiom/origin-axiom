# B157 — the metallic degree=rank exponent: order-determined, the closed form refuted

**Date:** 2026-06-17. **Status:** the empirical closed form **`k = 4 − m(o−3)` is REFUTED** (bronze m=3 breaks
it); the **order-not-rank** qualitative finding survives; the figure-eight cells are **exact**; the SL(4)
`{1,1,i,−i}` corner is **provably empty**. Standalone low-dimensional-topology / character-variety result; **no
Origin-core claim, no physics**; proven core P1–P16 untouched. Nothing promotes to `../../CLAIMS.md`. Ledger
V151. Reproducers in this folder.

**Provenance.** Phase 2 of the post-handoff push (derive the "metallic A-polynomial" exponent). Run as a
two-route workflow (B67 eliminant + B89 per-spectrum ideal algebra) with an adversarial synthesis; the
adversary (high confidence) could not break the conclusion and *strengthened* the SL(4)-emptiness leg. Every
load-bearing computation re-run in the main loop (verify-don't-trust). This **corrects** the B154/V146 claim
that banked `k=4−m(o−3)` as an empirical fit.

## The object + the construction (a genuine advance)

For the metallic once-punctured-torus bundle with monodromy `φ_m = R^m L^m`, the bundle SL(n,ℂ) reps `(A,t)`
satisfy `t A t⁻¹ = φ_m(A)`, etc. By free-group reduction the relations collapse to the clean general-m system
`F1: t Bᵐ = A⁻¹ t A`, `F2: t B = Aᵐ B t`, and the exact identity **`φ_m([A,B]) = Aᵐ [A,B] A⁻ᵐ`** holds (verified
by word reduction for m=1,2,3) — so the **cusp meridian is `µ = A⁻ᵐ t`** for all m (it commutes with the
longitude `[A,B]`). The construction (`metallic_construct.py`) reduces *exactly* to the validated figure-eight
toolkit at m=1 and reproduces the silver baseline at m=2.

## The exponent grid (verified, SL(3) unless noted)

On the degree=rank locus the longitude satisfies the **matrix identity** `[A,B] = s·µᵏ` (not a log-slope fit —
the complex-log branch-cut trap is avoided; `k` is the unique integer with `[A,B]·µ⁻ᵏ` scalar on the variety).
Verified at ≥2 seeds with full-relation + Burnside-irreducibility + non-central-longitude gates, with
high-precision (50–61 digit) polish:

| m \ o | o=3 | o=4 | o=6 |
|---|---|---|---|
| **m=1** (gold) | **4** (exact ℚ(ω), B71/B89) | **3** (exact ℚ(i), NEW) | — |
| **m=2** (silver) | 4 | 2 | — |
| **m=3** (bronze) | (1)\* | **3** | 1 |

\* `(m=3,o=3)` is **degenerate** and excluded: `o∣m ⟹ Aᵐ=I ⟹ µ=A⁻ᵐt = t` exactly (`‖µ−t‖~1e-15`), so the
meridian collapses and `[A,B]=µ` is trivial — not a metallic point. SL(4): `(m=1,o=3)→4` exact (B89, ℚ(ω));
`(m=2,o=3)→4` (B154). `o=5,6` admit **no irreducible SL(3) bundle reps** (random Newton, 300–400 seeds) —
inadmissible at SL(3); the grid is genuinely sparse.

## Result 1 — `k = 4 − m(o−3)` is REFUTED

The bronze row is a true counterexample: the formula predicts `(m=3,o=4)→1` and `(m=3,o=6)→−5`, but the
verified values are **3** and **1**. The `(m=3,o=4)` point is **genuinely non-degenerate** (`Aᵐ≠I`, `‖µ−t‖=8.1`
on a fresh seed, irreducible, `cond(t)=41`, residual 1.7e-14). So the closed form was an **artifact of having
only m∈{1,2}**. A brute search over ≤3-feature integer affine/modular laws finds candidates that fit the 5
non-degenerate points but **disagree off-grid and fail the observed `(3,6)→1`** — the grid is underdetermined,
so any 2-parameter closed form is an overfit. **[REFUTED]**

## Result 2 — what survives: order-determined, rank-independent

The qualitative finding from B154 **stands**: `k` is determined by the boundary-spectrum **order `o`**, not the
rank `n` — `o=3 ⟹ k=4` at *both* `n=3` and `n=4` (for m=1,2). "degree=rank" (`k=n`) is a **coincidence of the
principal spectra** (B95 ties their order to the rank: o=4↔n=3, o=3↔n=4). The exponent is the per-spectrum
ideal fact `k = min{ j : [A,B]·µ⁻ʲ is scalar on the variety }`. **[structural; verified]**

## Result 3 — exact figure-eight cells

The two figure-eight cells are **exact**, not numerics: `(m=1,o=3)→k=4` over ℚ(ω) (B71/B89, `[A,B]=−µ⁴` at
SL(4)); and **NEW: `(m=1,o=4)→k=3` over ℚ(i)** — the explicit identity `[A,B] = c·µ³` (with `c·det t = 1`),
reproduced two independent ways including the smallest-`j`-with-`[A,B]µ⁻ʲ`-scalar mechanism giving `j=3`
(`r1_fig_sl3_o4_proof.py`, `r3_k_mechanism.py`). **[exact]**

## Result 4 — the SL(4) `{1,1,i,−i}` corner is provably empty

The point a closed form would predict at `(m=1, o=4, n=4)` **does not exist**: over ℚ(i),
`det(UR)·det(LL)` (the two off-diagonal coupling blocks) lies **in the bundle ideal** (reduces to 0 mod the
Gröbner basis), so *every* `{1,1,i,−i}` rep has a singular coupling block; the only branch with nondegenerate
`det t` is **reducible** (Schur commutant nullity 2, Burnside algebra-dim 13<16). An apparent numeric
counterexample dissolved under proper relative-tolerance + Schur-commutant analysis. **[exact (Lemma 1, ideal
membership over ℚ(i)) + structural (reducibility)]**

## The honest open problem

A genuine closed form, **if one exists**, is **order-modular** (`k` likely depends on `m mod o`, with the
`o∣m` collapse excised) and must be obtained by **generalizing the B67/B71/B89 metallic-A-polynomial-slope
program to `φ_m`** — a per-cell `min-j`-scalar computation over ℚ(ζ_o) — **not by fitting** a sparse grid. The
data corners that would constrain it (`m≥4`; `o≥5`, which needs `n≥5`) are blocked by the SL(4)/SL(5) Newton
wall; a structured construction (B89-style) is the prerequisite. **[open]**

## Firewall

Standalone character-variety / low-dim-topology mathematics. No physics; nothing to `CLAIMS.md`. The figure-
eight A-polynomial connection (B67) is to a published knot invariant (Cooper–Long), not a physical claim.

## Reproduction

`python` (pyenv) on the reproducers in this folder: `metallic_construct.py` (the general-m construction,
reduces to the toolkit at m=1); `k_table_final.py` (the verified grid + the refutation, 2 seeds);
`r1_fig_sl3_o4_proof.py` (the NEW exact ℚ(i) figure-eight o=4 cell); `r3_k_mechanism.py` (the smallest-j-scalar
mechanism); `sl4_o4_empty.py` (the SL(4) `{1,1,i,−i}` emptiness, Lemma 1 ideal membership); `bronze_verify.py`
(the m=3 counterexamples). `PHASE2_FINAL.py` prints the consolidated summary.

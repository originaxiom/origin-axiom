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

**UPDATE 2026-06-23 (both in-sandbox routes confirmed exhausted — NEEDS-SPECIALIST / real CAS):** the structured
*automatic* construction was attempted in the pyenv sympy sandbox (auto-solve of the full (*)-ideal, and the
ideal-membership `min-j`-scalar reading via a Gröbner basis over `ℚ(ζ_o)`). It is **intractable here**: `sp.solve`
on the 9-variable cyclotomic system hits an internal Gröbner bug, and a `grevlex` Gröbner basis of the (*)-ideal
does **not finish even at SL(3)** (10 vars, >3 min, no result) — so SL(5) (25 vars) is hopeless in sympy. The
**per-cell hand-reduced** symbolic proofs *do* work and are exact (`r1_fig_sl3_o4_proof.py` SL(3) o=4→k=3 over
ℚ(i); B89 SL(4) o=3→k=4 over ℚ(ω)), but they don't auto-generalize. So the wall cells are unreachable in-sandbox
from **both** sides — Newton numerics (above) **and** sympy symbolic (here). Reaching them needs a **proper CAS**
(Singular / Macaulay2 / Sage with efficient Gröbner over `ℚ(ζ_o)`) or per-cell hand-reduction generalized to the
SL(5)/o≥5 spectra — genuine **NEEDS-SPECIALIST**, now confirmed by computation. *(The exponent-law flagship, Track
A of Masterplan III, terminates here for the in-sandbox program.)*

**CORRECTION 2026-06-23 (B198 — the mark above was PREMATURE; the wall is partly breached):** two of the three
premises were tooling/diagnosis, not math. (1) "needs a real CAS (Singular/Macaulay2/**Sage**)" — **Sage is
installed in-environment** (`command -v sage`); it reproduces the SL(3) cells **exactly** via the geometric
component (o=3→k=4, o=4→k=3, the Gröbner sympy could not finish). (2) "SL(5) Newton wall" — the failure was
**gauge-induced Jacobian rank-deficiency**; **gauge-fixing** the diagonal torus makes Newton converge, reaching
the previously-unreachable **SL(5) o=5, m=1 → k=2** (`[A,B]=+µ²`, certified to ~23 digits, 3 independent methods).
This **extends the m=1 row to o=5** (`k=7−o`) and shows `k=4−m(o−3)` governs m∈{1,2} in *value and
existence-boundary* (m=2 o=5 → no irreducible rep, the formula's `k=0`). What genuinely **remains**
NEEDS-SPECIALIST is *narrower*: the **exact symbolic** k at SL(5) (primary decomposition over ℚ(ζ₅) at 25 vars —
Sage stalls already at SL(4)/16 vars) and the general all-m closed form. The wall **moved** from "any CAS at all"
to "exact decomposition at ≥16 vars." **(Follow-up correction, same PR: the B198 grid REFUTED its own first-draft
secondary claims — there is no simple `k(o,m)` law and no `gcd(m,o)` rule; the exponent must be read on the
geometric stratum where the meridian `µ=A⁻ᵐt` has INFINITE order, and even there o=4,8 both give k=3. The SL(5)
o=5 m=1 → k=2 headline is confirmed loxodromic/geometric and stands.)** See `frontier/B198_metallic_exponent_CAS/`
(V190).

## Firewall

Standalone character-variety / low-dim-topology mathematics. No physics; nothing to `CLAIMS.md`. The figure-
eight A-polynomial connection (B67) is to a published knot invariant (Cooper–Long), not a physical claim.

## Reproduction

`python` (pyenv) on the reproducers in this folder: `metallic_construct.py` (the general-m construction,
reduces to the toolkit at m=1); `k_table_final.py` (the verified grid + the refutation, 2 seeds);
`r1_fig_sl3_o4_proof.py` (the NEW exact ℚ(i) figure-eight o=4 cell); `r3_k_mechanism.py` (the smallest-j-scalar
mechanism); `sl4_o4_empty.py` (the SL(4) `{1,1,i,−i}` emptiness, Lemma 1 ideal membership); `bronze_verify.py`
(the m=3 counterexamples). `PHASE2_FINAL.py` prints the consolidated summary.

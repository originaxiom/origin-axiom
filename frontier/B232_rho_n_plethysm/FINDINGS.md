# B232 — the ρ_n catalog reduced to a one-step stabilization recursion (a sharper reduction)

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched.** The central *unproved*
theorem of the program; this is an honest **reduction** (outcome (b) of the plan), **not** a proof.
Run: `python plethysm_recursion.py` (pyenv; ~5.5 min — the symbolic `Sym^8` char-poly dominates).

## The problem
Prove `char(ρ_n) = ∏_{d=2}^n char(Sym^d M) · ∏_{d=0}^{n-3} char(Sym^d M)` for **all n** — equivalently the
module-iso `ρ_n ≅ ⊕_{d=2}^n Sym^d(V) ⊕ ⊕_{d=0}^{n-3} Sym^d(V)` (the trace-map Jacobian at the trivial fixed
point, `(n²−1)`-dimensional). Proved exact `n≤4` (B80 CRT, B103 Lawton); structural `n=5` (B62); the explicit
two-sequence form is B89-T. **Three routes are foreclosed:** B84 (SVD-pinv numerics — gauge degeneracy), B85
(Procesi trace-ring σ — non-closure), B89-T (H¹ cohomology — gives `char(M)^{n²−1}`, the trivial-rep line, *not*
the tower).

## The advance — the stabilization recursion (R)
The fresh angle (pure GL(2) symbolic plethysm / char-poly algebra — touches **none** of the three walls):

> **(R)   `ρ_n ≅ ρ_{n−1} ⊕ Sym^n(V) ⊕ Sym^{n−3}(V)`** &nbsp;&nbsp; (char polys: `tower(n)=tower(n−1)·char(Sym^n M)·char(Sym^{n−3} M)`)

Passing `SL(n−1) → SL(n)`, the trace-map Jacobian gains **exactly two** GL(2)-irreps: the top symmetric power
`Sym^n(V)` (the new length-`n` trace word `tr(A…B)`) and a **lagging `Sym^{n−3}(V)`**. The lag of 3 = `dim(W)`,
`W=V⊕1` the `det=−1` external SL(2) fundamental (B121/B122): the degree-`n` Cayley–Hamilton relation removes the
`W`-content exactly three steps down. Dimension bookkeeping: each step adds `(n+1)+(n−2)=2n−1`, and
`Σ_{j=2}^n (2j−1) = n²−1` telescopes exactly. Base case `ρ_2 = Sym²(V)` (the SL(2) Fricke/Markov adjoint, exact).

## What was verified (all exact, symbolic in m)
1. **(R) holds for the two-sequence tower, `n=3…8`** — and `deg = n²−1` at each (35, 48, 63 at n=6,7,8).
2. **(R) holds on the REAL Jacobian** — `proved_tower(n) = proved_tower(n−1)·Sym^n·Sym^{n−3}` for `n=4,5`
   (proved n≤4, structural n=5; combined with B89-T's `sym_tower==proved_tower`, the *actual* Jacobian obeys (R)
   at n=3,4,5, not merely the conjectured formula).
3. **Adversarial self-check** — the foreclosed cohomological answer `char(M)^{n²−1}` does **not** satisfy (R)
   (`n=3,4,5`), so (R) genuinely characterizes the **true** tower, not the dead H¹ route (guards against
   re-deriving the wrong object in disguise).
4. **Extended catalog (new data, `n=6,7,8`)** — the Dickson multiplicities `a_k=#char(M^k)`, `a_k^-=#char(−M^k)`:
   e.g. `n=6: a1=2 a2=3 a3=2 a4=a5=a6=1 | a2-=a3-=a4-=1` (the `a_3(n=6)=2` discriminator, confirming
   B62/B89-T over B66's gauge-corrupted pinv `a_3=1`); `n=7,8` tabulated.

## Verdict — outcome (b): a sharper, wall-free reduction (not a proof)
The all-`n` catalog is now an **induction**: base `ρ_2=Sym²(V)` (exact) + the **single stabilization lemma (R)**.
This is genuine progress on the hard prize:
- it **relocates the wall** from a *global* assembly ("compute the whole Procesi σ", non-closing — B85) to a
  *local, uniform* statement (one stabilization step);
- it is **verified on real data** (`n≤5`) and **extends cleanly** to `n=8`;
- it **avoids all three foreclosed routes** (no ε-series, no Procesi σ, no H¹).

**The residual open lemma (stated):** prove the *actual* trace-map Jacobian gains exactly `Sym^n(V) ⊕ Sym^{n−3}(V)`
at each step — the `+Sym^n` is the new top trace word (plausibly direct); the `+Sym^{n−3}` lag-3 is governed by the
degree-`n` Cayley–Hamilton relation (`dim W = 3`). This is the lone remaining input, now a clean local statement
rather than the full catalog. NEEDS-SPECIALIST only *after* this local lemma resists in-sandbox attack (not yet
exhausted — the next concrete try is the Cayley–Hamilton derivation of the lag-3 term).

## Anchors
B80/B103 (proved n≤4), B62 (structural n=5/6, θ=−w₀ opposition involution), B89-T (the two-sequence form + the
foreclosed H¹ route), B121/B122 (`ρ_n=Sym^n(W)`, `W=V⊕1`), B84/B85 (the foreclosed numerics/Procesi routes),
K008 (the tower conjecture home). Oracle reused: `frontier/B89T_tower_route/probe.py`.

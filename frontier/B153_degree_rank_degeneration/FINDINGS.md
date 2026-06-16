# B153 — the rank-stratified degeneration of degree=rank

**Date:** 2026-06-15. **Status:** STRUCTURAL (n=3 exact over F_p + literature; n=4 exact over ℚ(ω);
n=5 semisimple proven + non-ss verified numerically). Standalone low-dimensional topology / character-variety geometry; **no Origin-core claim**;
proven core P1–P16 untouched. Nothing promotes to `../../CLAIMS.md`. Toolkit: `sln_toolkit.py` (self-tested);
probe: `probe.py`; test: `tests/test_b153_degree_rank_degeneration.py`. Ledger: V142.

**Provenance:** the synthesis of a campaign (`audit/CAMPAIGN_sln_bundle_varieties.md`) run after three
adversarial review rounds deflated the prior "SL(4) A-polynomial component" claim (PC13) to a *slice*
(round 2, verified). This stage replaces that over-claim with the honest, stronger result.

## Result

> **The figure-eight degree=rank relation `L=(−1)^{n-1}Mⁿ` is rank-stratified:** it is realized on a
> genuine SL(n,ℂ) character-variety **component at n=3**, degenerates to a measure-zero **slice at n=4**,
> and is **not realized on any irreducible representation at n=5**.

| rank | principal spectrum | relation | locus | rigor |
|---|---|---|---|---|
| 3 | `{1,i,−i}` (order 4) | `L=+M³` | spectrum-**rigid component** | **exact over F_p (3 primes)**: geometric (dim-5) comp tangent 11, rigid, irreducible, L=+M³; reducible slice (dim-3) tangent 10 — validated vs n=4=19; + Falbel [lit.] + 63 numerical witnesses (1e-14) |
| 4 | `{1,1,ω,ω²}` (order 3) | `L=−M⁴` | **slice** (spectrum deforms) | **exact over ℚ(ω)** (A-free tangent rank 29, kernel 19) |
| 5 | `{1,1,1,−1,−1}` (order 2) | — | **not realized on irreducibles** | **PROVEN for the principal (finite-order-A) family** (semisimple ⟹ A²=I ⟹ dihedral ⟹ reducible); the non-ss irreducibles (A infinite order, not Dehn-filling) **exist** but degree=rank fails on them (numerical, strong) |

> **CORRECTION (2026-06-15, self-audit).** The earlier n=5 row read "reducible / absent — non-ss numerical
> (0/120)". That "0/120, no irreducible reps" was an **artifact** of random Newton drifting to the vacuous
> `det t=0` stratum — the *same* bug fixed at n=3 (by pinning `det t=1`) but never back-applied to n=5. With
> `det t=1` pinned, irreducible SL(5) reps with the principal spectrum **do exist** (non-semisimple Jordan
> types, abundantly for the two `[3]`-block types — see `n5_nonss_irreducible.py`). The degeneration
> **headline survives** — degree=rank is still not realized on any *irreducible* rep at n=5 — but for the
> corrected reason in piece 3 below.

## The pieces

1. **n=4 is a slice (exact).** On the full bundle variety with `A` free, the Zariski tangent at a B89
   family point has rank 29 / kernel 19, with one SL-preserving direction that moves `tr A` (the
   spectrum) — so `{1,1,ω,ω²}` is *not* rigid; B89's 4-parameter family is a codimension-1 slice of a
   larger component on which `L=−M⁴` fails (in every form — pairwise, vs M, and as a char-poly identity).
   Confirmed mod p (3 primes, round 2) and **exactly over ℚ(ω)** (Sage cyclotomic-field rank).

2. **n=3 is a genuine component (rigid) — now EXACT over F_p.** The `{1,i,−i}` det-t-saturated `(*)`-ideal
   has 2 components in t-space (dims 3, 5; over `GF(p)` and `ℚ(i)`). Exactly over F_p (3 primes; the tangent
   function validated against the known n=4 = 19), the **dim-5 component is the geometric one**: A-free
   tangent **11** with `tr A` unable to move in SL×SL (spectrum **rigid**), **irreducible** (Burnside rank
   9), carrying **`L=+M³`** as a matrix identity (Falbel's relation, correct `(−1)^{n-1}=+` sign). The
   **dim-3 component is a *reducible* slice**: A-free tangent **10**, `tr A` moves, Burnside rank 5, no
   relation. Matches the literature (Falbel/HMP: the SL(3) Dehn-filling relations hold on entire
   components). **Correction (2026-06-15):** the earlier *numerical* "slice-piece tangent 14" was wrong
   (exact value **10**), and that piece is **reducible**, not a relation-carrying slice; the rigid-component
   tangent 11 + irreducibility + `L=+M³` are now confirmed **exactly**. Reproduce: `n3_exact_endpoint.sage`
   (Sage). [ℚ(i)-exact, vs F_p-exact, is optional — the multi-prime result + Falbel + 63 numerical
   witnesses (1e-14) already make it solid.]

3. **n=5: degree=rank is not realized on an irreducible rep** (corrected 2026-06-15).
   - *Semisimple* `{1,1,1,−1,−1}` (`A²=I`): `A⁻²=I ⇒` (bundle relation `tAt⁻¹=A²B`) `B=tAt⁻¹ ⇒
     B²=tA²t⁻¹=I`, so `A,B` are both involutions ⇒ `⟨A,B⟩` dihedral ⇒ every such SL(5) rep is **reducible**.
     A **proof** (no numerics) that fills the semisimplicity gap the reviewers flagged in B95's argument
     (the old "`A²=I`" step needed semisimplicity; this uses `A²=I` directly to make `B` an involution).
   - *Non-semisimple* (`A²≠I`): irreducible reps **DO exist** — this **corrects** the earlier "0/120,
     none" claim, which was a `det t=0`-drift artifact. With `det t=1` pinned, both `[3]`-block Jordan
     types give well-conditioned irreducible reps (cond(t) ~ 20; `(*)`-residual ~1e-15), certified by
     **two independent tests that agree**: Burnside span-rank = 25 and Schur commutant dim = 1, with
     ~15-orders-of-magnitude SVD gaps. **But** the degree=rank relation **fails** on every one of them:
     the best matrix-identity match `‖[A,B] − (−1)^{n-1}μⁿ/det t‖` over `n=2..8` and a large well-conditioned
     sample is ≈ 2.5 (≫ 0). [NUMERICAL, strong]
   - **Net (sharpened with the finite-order distinction).** A *principal / Dehn-filling* rep has `A` of
     **finite order** (root-of-unity eigenvalues realized **semisimply**) — that is what makes `Mⁿ=L` a
     filling slope. At n=5 the forced principal spectrum then forces `A²=I` (semisimple + eigenvalues in
     `{±1}`), so the dihedral argument gives reducible: **no irreducible principal (finite-order-`A`) rep
     exists ⇒ degree=rank is absent at n=5 — PROVEN** (not merely numerical). The non-semisimple irreducibles
     are *outside* this family: a non-diagonalizable `A` with the same eigenvalue spectrum has **infinite
     order** (so it is not a Dehn-filling rep), and degree=rank fails on it anyway (numerical) — i.e.
     *relaxing* the finite-order condition still does not recover `Mⁿ=L`. So the headline absence is **proven
     for the principal family**, with the non-ss exploration as the "relaxation doesn't help" corollary.
     The old "0/120, no irreducibles" was simply wrong (it missed the non-ss irreducibles). Tiers:
     no-irreducible-principal-rep ⇒ degree=rank-absent **PROVEN**; non-ss-irreducibles-exist **verified
     (numerical, strong, 2 certificates)**; degree=rank-fails-on-the-non-ss-locus **numerical (strong)**.

Supporting (B153a): among order-3 SL(4) meridian spectra, `{1,1,ω,ω²}` (type `(2,1,1)`) is the **unique**
one with irreducible reps; `(2,2)={ω,ω,ω²,ω²}` is totally reducible (Burnside rank 4), `(3,1)` has no
valid reps, `(4)` is trivial. So `L=−M⁴` is tied to this spectrum, not a general `A³=I` phenomenon.

## What is corrected
PC13's "irreducible four-parameter **component**" / "Dehn-filling component" framing is **false** (round-2
verified; n=4 is a slice). The honest statement is the degeneration above. The completeness result (B89's
family = irreducible locus *for the fixed `{1,1,ω,ω²}` spectrum*, B149) stands as a fixed-spectrum slice
statement.

## Open
- Generality: **PARTLY ANSWERED — see [[../B154_silver_bundle_foundation]]** (V146). Degree=rank
  **generalizes to the metallic family** with the derived meridian `µ=A⁻ᵐt` (from `φ_m([A,B])=Aᵐ[A,B]A⁻ᵐ`,
  an exact free-group identity; figure-eight's `A⁻¹t` is `m=1`). KEY REFRAMING: the exponent is
  **order-based, not rank-based** — `[A,B]=±µᵏ` with `k=4−m(o−3)` (o = boundary-spectrum order); the
  figure-eight `{1,ω,ω²}` gives `k=4` at *both* n=3 and n=4. So this note's `L=(−1)^{n-1}Mⁿ` (`k=n`) is
  correct **for the principal spectra** (where B95 ties order to rank), but "=rank" is a *coincidence* of
  those spectra — the underlying invariant is the order. For silver the relation lives on a *sub-locus*
  (slice, ~25%), vs the figure-eight's full spectrum-locus. Remaining: the silver principal spectrum + the
  slice/component characterization + a closed-form derivation of `k`.
- Exact n=3 rigidity: **DONE over F_p** (3 primes; `n3_exact_endpoint.sage`). Optional further upgrade to
  exact over `ℚ(i)` (the F_p multi-prime + literature already suffice).
- n=5: the principal (finite-order-`A`) absence is now **PROVEN** (semisimple ⟹ A²=I ⟹ dihedral). The
  residual open item is a from-first-principles proof that degree=rank also fails on the *non-ss* (infinite
  order, non-Dehn-filling) irreducible locus — i.e. that `[A,B]=μ⁵/det t` has no irreducible solution there
  (currently numerical, strong). The irreducibles themselves are established (not absent); the open part is
  the relation's absence *on the non-principal locus*, which is not needed for the Dehn-filling headline.
- Novelty: is this degeneration structure known in the Falbel/HMP/BFG circle? (specialist).

## Reproduce
```bash
python frontier/B153_degree_rank_degeneration/probe.py
python frontier/B153_degree_rank_degeneration/n5_nonss_irreducible.py   # corrected n=5 (irreducibles exist)
sage   frontier/B153_degree_rank_degeneration/n3_exact_endpoint.sage    # exact n=3 endpoint over F_p (needs Sage)
python -m pytest tests/test_b153_degree_rank_degeneration.py -q
```

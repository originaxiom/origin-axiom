# B153 — the rank-stratified degeneration of degree=rank

**Date:** 2026-06-15. **Status:** STRUCTURAL (exact/proven at two ranks; numerical + literature at the
third). Standalone low-dimensional topology / character-variety geometry; **no Origin-core claim**;
proven core P1–P16 untouched. Nothing promotes to `../../CLAIMS.md`. Toolkit: `sln_toolkit.py` (self-tested);
probe: `probe.py`; test: `tests/test_b153_degree_rank_degeneration.py`. Ledger: V142.

**Provenance:** the synthesis of a campaign (`audit/CAMPAIGN_sln_bundle_varieties.md`) run after three
adversarial review rounds deflated the prior "SL(4) A-polynomial component" claim (PC13) to a *slice*
(round 2, verified). This stage replaces that over-claim with the honest, stronger result.

## Result

> **The figure-eight degree=rank relation `L=(−1)^{n-1}Mⁿ` is rank-stratified:** it is realized on a
> genuine SL(n,ℂ) character-variety **component at n=3**, degenerates to a measure-zero **slice at n=4**,
> and is **absent at n=5**.

| rank | principal spectrum | relation | locus | rigor |
|---|---|---|---|---|
| 3 | `{1,i,−i}` (order 4) | `L=+M³` | spectrum-**rigid component** | numerical (63 witnesses, 1e-14) + Q(i) decomposition (2 comps, dims 3,5) + Falbel [lit.] |
| 4 | `{1,1,ω,ω²}` (order 3) | `L=−M⁴` | **slice** (spectrum deforms) | **exact over ℚ(ω)** (A-free tangent rank 29, kernel 19) |
| 5 | `{1,1,1,−1,−1}` (order 2) | — | reducible / absent | semisimple **proven**; non-ss numerical (0/120) |

## The pieces

1. **n=4 is a slice (exact).** On the full bundle variety with `A` free, the Zariski tangent at a B89
   family point has rank 29 / kernel 19, with one SL-preserving direction that moves `tr A` (the
   spectrum) — so `{1,1,ω,ω²}` is *not* rigid; B89's 4-parameter family is a codimension-1 slice of a
   larger component on which `L=−M⁴` fails (in every form — pairwise, vs M, and as a char-poly identity).
   Confirmed mod p (3 primes, round 2) and **exactly over ℚ(ω)** (Sage cyclotomic-field rank).

2. **n=3 is a genuine component (rigid).** The `{1,i,−i}` locus carries `L=+M³` (Falbel's relation, with
   the correct `(−1)^{n-1}=+` sign) on a spectrum-**rigid** locus: a witness has A-free tangent 11 with
   `tr A` unable to move within SL×SL (vs tangent 14 on a coexisting slice piece). The det-t=1-saturated
   ideal has 2 components over both `GF(p)` and `ℚ(i)` (dims 3, 5). Matches the literature (Falbel/HMP:
   the SL(3) Dehn-filling relations hold on entire components). [n=3 rigidity is numerical + literature;
   exact A-free tangent at an exact n=3 point deferred.]

3. **n=5 is absent.** *Semisimple* `{1,1,1,−1,−1}`: `A²=I ⇒ A⁻²=I ⇒` (bundle relation `tAt⁻¹=A²B`)
   `B=tAt⁻¹ ⇒ B²=tA²t⁻¹=I`, so `A,B` are both involutions ⇒ `⟨A,B⟩` dihedral ⇒ every SL(5) rep
   reducible. A **proof** (no numerics) that fills the semisimplicity gap the reviewers flagged in B95's
   argument (the old "`A²=I`" step needed semisimplicity; this uses `A²=I` directly to make `B` an
   involution). *Non-semisimple* (Jordan block at +1, `A²≠I`): no irreducible reps found (0 of 120 seeds;
   78 reducible) — strongly absent, not proven.

Supporting (B153a): among order-3 SL(4) meridian spectra, `{1,1,ω,ω²}` (type `(2,1,1)`) is the **unique**
one with irreducible reps; `(2,2)={ω,ω,ω²,ω²}` is totally reducible (Burnside rank 4), `(3,1)` has no
valid reps, `(4)` is trivial. So `L=−M⁴` is tied to this spectrum, not a general `A³=I` phenomenon.

## What is corrected
PC13's "irreducible four-parameter **component**" / "Dehn-filling component" framing is **false** (round-2
verified; n=4 is a slice). The honest statement is the degeneration above. The completeness result (B89's
family = irreducible locus *for the fixed `{1,1,ω,ω²}` spectrum*, B149) stands as a fixed-spectrum slice
statement.

## Open
- Generality: does the same degeneration hold for the silver bundle (m=2)? (needs the `R²L²` monodromy).
- Exact n=3 rigidity (exact A-free tangent at an exact point).
- n=5 non-semisimple: prove (not just 0/120) the absence.
- Novelty: is this degeneration structure known in the Falbel/HMP/BFG circle? (specialist).

## Reproduce
```bash
python frontier/B153_degree_rank_degeneration/probe.py
python -m pytest tests/test_b153_degree_rank_degeneration.py -q
```

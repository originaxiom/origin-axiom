# B8137 — Paper III is drafted — and it ships a reproducer the source arc never had

**Date:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical identification; no Standard-Model quantity appears.

## What was done

Drafted **Paper III**: `papers/series/paper3_one_loop/` — 6pp, clean build. `dictionary.py` re-run
(exit 0, ALL CHECKS PASS) before use.

## The result

`σ_k` is **one-dimensional**, so `R(k,σ_k) = ∏_{[γ] prime} (1 − q_γ^k)` with `q_γ = e^{−ℓ+iθ}`
**exactly** the GMY nome. Hence

    Z_1-loop = ∏_{n≥2} |R(n, σ_n)|^{−2}

— an **infinite product** of twisted Ruelle zeta values. To *which of Pfaff's torsions is it?* the
answer is **none of them**: it is not any single Ray–Singer torsion nor any finite ratio. Pfaff's
ratio formula supplies **exactly** the `k ≥ 3` tail; the one factor it cannot reach is `n = 2`,
which sits **at** the abscissa of absolute convergence — which is also *why* that formula starts at
`m ≥ 3` and normalises by `ρ(2)`.

Cross-check: `log Z` for the `n ≥ 3` tail computed two ways — via the Ruelle factors and via the
direct geodesic sum — agrees to **8.2 × 10⁻¹⁴**.

## The three residues, each with what would close it

1. **The spin-2 cusped test function.** Believed a genuine literature gap, not a retrieval failure.
   *Closed by:* a construction, or a citation missed.
2. **The evaluation point.** Fried gives `R_σ(0) = T_X(σ)²` and the cusped extension **exists**
   (Park). It does **not** close the gap: Fried evaluates at `s = 0`, Pfaff at `k ≥ 3`, the graviton
   at `s = n ≥ 2` — **three evaluations of one family, and Fried's is the one point the graviton
   never visits.** *Closed by:* a relation between the family's value at 0 and at the positive
   integers. **Reframes an existence gap as an evaluation gap.**
3. **The cusp's continuous spectrum.** *Closed by:* the assembly, once residue 1 exists.

## ⚠ A gap in this seat's own bank, found and filled

**B8129 and B8130 are banked as `results.json` with NO code in the tree.** Paper III's §4 would have
shipped a numerical claim with no script. I wrote `check_n2_abscissa.py` **independently from the
banked method description**, and **promoted the bite control to an ABORT**: the run refuses to
report anything above the abscissa unless it first visibly diverges below it (spread ratio 21.8× at
`s = 1.40`).

**Residual, recorded rather than tuned away:** my cutoff spreads differ ~3% from banked
(1.06e-4 vs 1.03e-4 at `s=2.6`); `|R|` agrees to four decimals (1.1075 → 1.1936). No conclusion
depends on the difference.

## SCOPE

- **Convergence of the `n = 2` factor is NOT proved.** Three cutoffs; the cutoff→∞ limit is
  untested. Status is *no evidence of breakdown; existence unproved*.
- The one-loop partition function is **not assembled**.
- **No measured quantity** and no identification with any observable.

**Gate 5 untouched.**

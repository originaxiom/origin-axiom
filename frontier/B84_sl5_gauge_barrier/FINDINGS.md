# B84 (Phase B) — the SL(5) tower barrier is non-convergence, not gauge: I1 refuted

**Date:** 2026-06-05. **Status:** exact F_p; a decisive refutation of my own bold conjecture (I1), with
a sharp characterization of the real barrier. Standalone Lie/invariant theory; **no Origin-core claim**;
proven core P1–P16 untouched. Script: `probe.py`. Test: `tests/test_b84_sl5_gauge_barrier.py`.

## The conjecture (I1) being tested

B80/V62 **proved the SL(4) tower from first principles** via the F_p ε-series **pinv-limit** Jacobian
`DT_0` (seed-canonical at SL(4)). B81/V63 showed SL(5)'s `char(DT_0)` *scatters across seeds*. **I1**
hoped this was a fixable **gauge/basis artifact** — that a basis-canonicalization (θ-split), or
seed-averaging, would recover the tower, since the trace map is canonical.

## The tests (exact F_p)

1. **Seed-averaging fails.** `char(DT_0(5,m=1))` over **40 seeds**: all 25 coefficients distinct across
   all seeds (mode-count 1/40), 0/40 give the tower. No consensus; averaging recovers nothing.
2. **The decisive test — gauge-INVARIANT power sums.** `tr(DT_0(5)^k)`, `k=1..5`, are
   **basis-independent** symmetric functions of the eigenvalues. They **also scatter across seeds** —
   even `tr(DT_0)` (the sum of the eigenvalues) differs every seed:

   | rank | `tr(DT_0^k)` seed-invariant? | meaning |
   |---|---|---|
   | SL(4) | **yes** | the pinv-limit is canonical (why B80 works) |
   | SL(5) | **no** (every power sum differs per seed) | the **spectrum itself** is seed-dependent |

## Verdict — I1 REFUTED, and the barrier sharply characterized

Because even the gauge-**invariant** power sums scatter, the SL(5) pinv-limit produces **genuinely
different operators (different eigenvalue multisets) per seed** — **not** different bases of one
operator. This is a **non-convergence** of the `ε→0` limit, not a gauge/basis ambiguity:
`DX·pinv(Dx)` depends on the approach direction `(P,Q,S)` because `Dx` is **rank-deficient** at the
doubly-degenerate `char(M²)²` sector. Therefore:

> **No numerical gauge-fix, θ-split, or seed-averaging can recover the SL(5) tower from the pinv-limit.**

Precisely: **22 of 24 eigenvalues are canonical** (B66 tags them to the catalog); the remaining **2 — the
*second* `char(M²)`** — are **genuinely undetermined** by the limit. Since every symmetric function
(char poly, power sums) mixes those 2 in, the entire spectrum-as-a-multiset scatters. This is a cleaner,
stronger statement than B81 (which showed char-poly scatter): the corruption is in the **spectrum**, not
the basis.

## Consequence (redirects to Phase C/D)

The SL(5)+ tower **from first principles** needs the **exact symbolic trace map `σ`** (the Procesi ring),
where the fixed-line Jacobian `Dσ` is canonical *by construction* — no pinv, no degenerate limit. That is
**Phase C/D's** task. The alternative is **B62's structural opposition-involution answer** (which gives the
SL(5) tower *structurally*, already a live result, but not "from first principles"). The cheap numerical
routes (including the θ-split idea — independently dead per the planning sweep) are **closed**.

A decisive, banked refutation of I1: the SL(5) barrier is genuine non-convergence at the degeneracy, and
the path forward is symbolic, not numerical.

## Reproduce

```bash
python frontier/B84_sl5_gauge_barrier/probe.py        # ~70s (a few SL(4)/SL(5) F_p engine calls)
python -m pytest tests/test_b84_sl5_gauge_barrier.py -q
```

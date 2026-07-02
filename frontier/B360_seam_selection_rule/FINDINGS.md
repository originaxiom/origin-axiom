# B360 — the selection rule, tested: the parity readings die; silver-selectivity survives

**Status: banked (frontier), EXACT tier (B358's engine; the committed readout regenerable). The pre-registered
B359 prediction run — with the honest headline that the prediction HALF-FAILED and the rule got sharper.
Firewalled; nothing to `CLAIMS.md`.**

## The pre-registration and the verdicts

B359 observed (3 pairs): seam-bright ⇔ the pair contains the even seed, and pre-registered: **(1,4) bright,
(3,5) dark**. This probe ran (1,4), (3,5), and the discriminating even×even pair (2,4) — theta lift, exact:

| pair | prediction | **verdict (exact)** |
|---|---|---|
| (3,5) | dark | **DARK** ✓ (0/15) |
| (1,4) | bright | **DARK** ✗ — **the "contains an even seed" reading is REFUTED** (0/31) |
| (2,4) | discriminator | **BRIGHT** (36/49, `s ∈ {±1/120, ±1/240, ±1/480}`) — **the "opposite parity" reading is ALSO refuted** |

Three points did not make a law; the declared test killed both readings in one run — the pattern-tier
discipline working exactly as designed.

## What survives — and the candidate mechanism

Across all six computed pairs: **bright = {(1,2), (2,3), (2,4)}, dark = {(1,3), (1,4), (3,5)} — bright ⇔ the
pair contains silver (m=2), exactly.** A principled candidate for *why* m=2 is the selective seed: with
`char(A_m) = x² − (m²+2)x + 1`, `disc = m⁴ + 4m²`:

- **at 5:** `disc ≡ 0 (mod 5)` for `m ∈ {1,4,5}` (parabolic/trivial types) but `≡ 2` (a QNR — **regular
  elliptic**, order 6) for `m ∈ {2,3}`;
- **at 3:** `m=3` is trivial (`3|m`, the divisibility law); the rest are regular (order 4).

So among seeds 1–5, **m=2 is the unique (5-elliptic ∧ 3-nontrivial) seed** — the only seed regular-elliptic at
the golden prime *and* alive at the Eisenstein prime. Two hypotheses now separate:

- **H-min (data-minimal):** bright ⇔ the pair contains the residue class of `A₂` mod 15 specifically.
- **H-loc (local-type):** bright ⇔ the pair contains a (5-elliptic ∧ 3-nontrivial) seed.

**Pre-registered discriminator (the next run):** `m=7` is also 5-elliptic (`disc(7) ≡ 2 mod 5`) and
3-nontrivial — so **pair (1,7): BRIGHT under H-loc, DARK under H-min.** One exact computation decides.

## New exact data

The (2,4) bright table's `s`-set `{±1/120, ±1/240, ±1/480}` is a **sub-set of (1,2)'s** denominators (no new
primes) — unlike (2,3), whose values carried bronze's `3²`. The seam values continue to carry pair arithmetic;
the value-map `(pair) ↦ s-set` is accumulating structure worth a dedicated pass once the selection rule is
settled. Seed operator orders (theta lift, verified in-engine): m=1→20, 2→12, 3→6, 4→20, 5→4.

## Tiers and scope

EXACT: all tables and verdicts (Fraction arithmetic; artifact `seam_predict.json` regenerable by
`seam_predict.main()`, ~10 min). OBSERVED (6 points): silver-selectivity; the two hypotheses are labeled
hypotheses with a declared discriminator. Everything remains lift-sector mathematics pending **L57**; nothing
promotes; K020 stands.

**Provenance.** B359 (the pre-registration this run executes and half-refutes), B358 (engine + dichotomy),
B354/B356 (the parity texture whose naive seam-level reading died here), L57. Reproducer: `seam_predict.py`;
test: `tests/test_b360_seam_selection_rule.py`.

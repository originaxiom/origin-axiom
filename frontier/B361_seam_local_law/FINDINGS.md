# B361 — the seam's local law: bright ⇔ a doubly-elliptic seed is present (the discriminator decides H-loc)

**Status: banked (frontier), EXACT tier (B358 engine). The pre-registered B360 discriminator, run same-day.
Firewalled; nothing to `CLAIMS.md`.**

## The discriminator and its verdict

B360 left two hypotheses for the seam selection rule, separated by pair (1,7) (m=7 shares silver's local
profile — `disc(A₇) = 2597 ≡ 2 (mod 5)`, a QNR ⇒ 5-elliptic; 3-nontrivial):

- **(1,7): BRIGHT** — 20/31 nonzero doubles, `s ∈ {±1/48, ±1/96}` ⇒ **H-min ("literally contains seed 2") is
  REFUTED; H-loc survives.**
- **(3,7): BRIGHT** — 18/39, with `s`-set **identical to (2,3)'s**: `{±1/144, ±1/288}`.

## The law (8 pairs, exact, zero counterexamples)

> **The Par-inserted pair invariant carries `√−15` iff the pair contains a seed whose monodromy is ELLIPTIC AT
> BOTH PRIMES** (char poly `x²−(m²+2)x+1` irreducible mod 3 *and* mod 5).

Qualifying seeds (m ≤ 7): **m = 2, 7** (5-elliptic ∧ 3-elliptic). Disqualified: m = 1, 4 (5-parabolic:
`disc = m⁴+4m² ≡ 0 mod 5`), m = 3 (3-trivial), m = 5 (5-trivial). Evidence: bright = {(1,2), (2,3), (2,4),
(1,7), (3,7)}; dark = {(1,3), (1,4), (3,5)} — perfectly consistent, all exact.

**Why this shape is natural for the seam:** `√−15 = √−3·√5` requires both primes' quadratic data
*simultaneously* — and the carrier is a single seed generating the quadratic extension at both factors. **Yet
the single-seed controls remain exactly clean (B358): the doubly-elliptic seed alone is dark — a partner (any
partner) is required.** Multiplicity remains essential; the qualifying seed is the key, the pairing is the
lock.

**The value-echo:** (3,7)'s `s`-set equals (2,3)'s exactly — the seam *values* track the seeds' local types,
not their identities (everything at level 15 sees only `A_m mod 15`, but the echo is finer than that: bronze ×
either doubly-elliptic seed gives the same set). (1,7) `{±1/48, ±1/96}` vs (1,2)'s richer 12-value set shows
the map (pair ↦ s-set) is not partner-only — the post-L57 value-map pass has real structure to chase.

## Tiers and scope

EXACT: all verdicts (artifact `seam_disc.json`, regenerable by `seam_disc.main()`). The law is an
8-point exact pattern with a natural local-arithmetic mechanism — **stated as a law of the computed range,
not proved**; the next discriminators are cheap (predictions: (2,7) bright, (1,5)/(4,5) dark; and the first
doubly-elliptic seed beyond 7 mod 15-classes). Everything remains theta-lift-sector mathematics pending L57;
zero promotions; K020 stands.

**Provenance.** B360 (the refutation that sharpened to this), B358/B359 (engine + the arc), L57.
Reproducer: `seam_disc.py`; test: `tests/test_b361_seam_local_law.py`.

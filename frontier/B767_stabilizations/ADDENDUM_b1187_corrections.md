# ADDENDUM (2026-08-28, B1187) — three instrument defects in this arc, corrected downstream

Recorded beside, per the addendum-beside rule; this arc's two STABILIZED closures (B489, TOMB-L255)
are untouched and verified standing.

1. **WALL-7 "no roots" logic**: this arc's docstring claimed 865 nonvanishing points would prove
   the minor determinant "has no roots." Wrong as stated: ≥ deg+1 nonvanishing points prove
   D ≢ 0 — generic-t closure only. All-t closure needs root exclusion — achieved in B1187 mod two
   primes (dim = 0 at every nondegenerate t ∈ {1..865}, q = 1009 and 1999); the K-exact route
   (two-minor interpolation + gcd) is specified there.
2. **TOMB-L34 "3 seeds"**: vacuous — the tight-binding model is deterministic; `np.random.seed`
   was set but no randomness is ever drawn. The genuine robustness axes (word window, cut, W) are
   swept in B1187.
3. **TOMB-L34 estimator**: c_eff := S/log L conflates the additive constant (S = a·log L + b ⇒
   S/log L = a + b/log L, which drifts as b/log L decays) — the "0.64 → 0.26 inconclusive plateau"
   was an estimator artifact. The two-parameter profile fit (B1187) shows the stable log class.

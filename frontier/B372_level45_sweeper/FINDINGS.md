# B372 (W2.7) — the level-45 sweep: the seam is a level-family phenomenon

**Status: banked (frontier) + E16 promoted at banking (the exact table; certified data). The
pre-registered null was REFUTED by the computation — the arc's fifth failed-and-sharpened
prediction, and the most consequential: the seam persists, and its arithmetic home GROWS.
Campaign W2.7 (task #161). Firewalled; the framing rules apply unchanged.**

## Method and the gate

CRT/F_p engine (toolbox row 6): all arithmetic mod three primes ≡ 1 (mod 720), exact
identification per cell by solving across Galois embeddings in the declared 12-dim basis
`{1, c₁, c₂} ⊗ {1, √5, √−3, √−15}` (cₖ = ζ₉^k + ζ₉^{−k}), held-out-embedding verification per
prime, CRT + rational reconstruction across primes. **The hard gate passed**: the identical
pipeline at N = 15 reproduces the banked flagship cells (0,4) and (0,8) exactly (P19/E1 anchors).
Orders at 45: ord(W₁) = 60, ord(W₂) = 12; full tables computed; **zero identification failures**
— every value lies inside the declared span.

## The verdicts (both two-outcome questions decided)

- **Q1 — the single-object wall HOLDS at 45, more cleanly than at 15**: the only nonzero single
  cells are a ∈ {1, 16, 31, 46} (≡ 1 mod 15), each exactly **1/4** — purely rational; zero
  imaginary components anywhere in the singles.
- **Q2 — the pre-registered null (seam does not persist; motivated by the real Gauss sum
  g(45) = 3√5) is REFUTED**: **all 144 nonzero pair cells carry imaginary components**, and
  144/144 carry √−15-type content (bare or c-dressed: 48 bare √−15, 136/139 in the c₁/c₂
  slots). **The seam persists at level 45.**
- **The home grows**: every pair cell has genuine ℚ(ζ₉)⁺ dependence — at level 45 the values
  occupy the full 12-dimensional compositum `ℚ(ζ₉)⁺·ℚ(√5,√−3)`, not the level-15 quartic field.
  The seam's arithmetic home scales with the level.
- Denominators remain 15-smooth × 2-power (up to 2880 = 2⁶·3²·5): the level-15 denominator
  pattern persists with larger exponents.

## What this changes

The seam is not a level-15 accident: the twisted-pair channel carries imaginary-quadratic (and
now composite-field) content at the second level tested, while singles stay exactly real — the
wall and the door move together up the level family. The level-map question graduates from
"robustness sweeper" to a structural direction: how does the value tower grow with N (the
conductor structure of the seam)? Registered as the follow-on lead.

**Provenance.** PREREGISTRATION.md (PR #457, committed first); B358/B367 (the level-15 anchors);
P56/P57 (the lift conventions transported verbatim). Reproducer: `sweep45.py` (~4 min, 3 primes);
locks: `tests/test_b372_level45.py` (from the banked JSON + an OA_SLOW full rerun).

# B306 — The principal-grading cascade of E₆: the forced pseudo-Levi chain, the left-right SM point, the saddle (3rd refute)

**Status: banked (frontier). One corrected/extended result + one re-refutation; nothing to `CLAIMS.md`.** Chat-1
claimed the full SM gauge group appears as a transient window `SU(3)×SU(2)×U(1)³` (dim 14) at `u=2πi/3+ε`, between
trinification and a saddle "`SU(3)×U(1)⁴`". Assessed verify-don't-trust. The honest, corrected picture is *more*
informative than the claim.

## The forced cascade (Sage-verified)
The principal-grading centralizers (roots with `height ≡ 0 mod N` = survivors of `exp((2πi/N)·h)`) form a forced
pseudo-Levi chain:

| N | centralizer | dim |
|---|---|---|
| 1 | E₆ | 78 |
| 2 | SU(6)×SU(2) | 38 |
| 3 | **SU(3)³ (trinification)** | 24 |
| 4 | SU(3)²×SU(2) | 20 |
| 5 | **SU(3)×SU(2)×SU(2)×U(1)² (left-right ⊃ SM)** | 16 |
| 6 | **SU(2)³ (saddle)** | 12 |

This is standard E₆ Borel–de Siebenthal theory — **generic E₆**, forced once you grade by the principal element.

## What the SM "window" actually is
- **The SM-shaped point is N=5, not Chat-1's `2πi/3+ε`.** At N=5 the centralizer is the **left-right gauge group**
  `SU(3)_c × SU(2)_L × SU(2)_R × U(1)²` — which **contains** the SM. The SM is reached by **breaking `SU(2)_R`** (the
  standard left-right → SM step) and projecting one `U(1)` to hypercharge. Both are **external** choices (*which*
  SU(2) survives, *which* `U(1)` is `Y`) — the same kind of external selection as "which SU(3) is color" in
  trinification (B299/B301).
- **Chat-1's "dim-14 `SU(3)×SU(2)×U(1)³`" matches no clean centralizer** (N=4 is dim 20, N=5 is dim 16). The
  perturbative "window" is not a forced grading point.
- **The saddle (N=6) is `SU(2)³`, not `SU(3)×U(1)⁴`.** Chat-1 has now asserted the saddle-SU(3)/SU(3)×U(1)⁴ **three
  times** (B304, B305, B306) — refuted each time. (The dim-12 is right; the algebra is `SU(2)³×U(1)³`.)

## The object connection (and what's firewalled)
- **N=3 and N=6 are object-relevant** — the Eisenstein points `u = 2πi/3, iπ/3` from `ℚ(√−3)` (B305), the
  hyperbolic/E₆ end.
- **N=5 (the left-right, SM-containing point) is `k+2`** — the figure-eight's WRT level (`k=3`). Striking, but `ζ₅`
  is the **golden / E₈ end** (B261), not the `ℚ(√−3)` end, so connecting the N=5 grading to the figure-eight's level
  *mixes the two ends* — flagged as a `[LEAP]`, not a forced connection.
- The deformation-as-RG / topology-as-Higgs reading is firewalled.

## Net
The cascade is real and forced (generic E₆); it passes through a **left-right gauge group at N=5 that contains the
SM** (the SM = break `SU(2)_R`, external) and ends at `SU(2)³` (not the SM-adjacent algebra Chat-1 claimed). So "the
SM is there" is true in the containment sense — it sits inside the N=5 left-right group — but it is **not a forced
endpoint**: the final selection (break `SU(2)_R`, project `U(1)_Y`, choose color) is the external value-choice, as the
structural theorem requires. The object-specific part stays the Eisenstein `ω` (N=3/6); the cascade itself is generic.

## The fence
E₆ root-system computation (Sage-verified). The cascade is standard E₆; the SM endpoint needs external breaking; the
N=5↔level link is a flagged `[LEAP]`. Nothing to `CLAIMS.md`.

`principal_grading_cascade.py` (sage-python: the full mod-N cascade) · `verdict.py` (pyenv) ·
`tests/test_b306_principal_grading_cascade.py`. Related: `B305` (trinification at ω; the saddle refutation),
`B304` (the 1st saddle refutation; sin²θ_W, β), `B299`/`B301` (the external color/SU(2) choice), `B261` (the golden
ζ₅ / E₈ end), `B204` (the WRT level k=3 / n=5), `S045` (the firewalled RG reading).

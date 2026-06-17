# B158 — the Ω↔tower bridge audit: a spectral-only correspondence

**Date:** 2026-06-17. **Status:** the named open lead **L18** (the Ω↔tower bridge audit) is **resolved at the
spectral level**: Ω is the **abelianized spectral image** of the metallic trace-map tower — the metallic
bundle-monodromy characteristic polynomials are realized as reciprocal factors of the integer Ω family on the
live cone — but **not a faithful mechanism** (the strict-full shears commute). Standalone low-dim-topology /
character-variety algebra; **no Origin-core claim, no physics**; proven core P1–P16 untouched. Nothing promotes
to `../../CLAIMS.md`. Ledger V152. Reproducer `bridge_audit.py`.

**Provenance.** Continuation after the post-handoff plan closed; runs the bridge audit flagged as the genuine
unification frontier by the source-chat cross-check (`docs/OPEN_LEADS.md` L18, `frontier/B156`,
`docs/UNIFIED_STATE.md` §3). All checks exact (sympy) and re-run in the main loop.

## The question

Is the Ω strict-full family `R_{a,m} ∈ SL(4,ℤ)` (B156) connected to the metallic trace-map tower
(B67/B154/B157) as a **mechanism**, only at the **spectral** (characteristic-polynomial) level, or **fully
standalone**? B155 already showed they share the *one* canonical object Ω₄ = golden×phase; B156 noted the
shears commute (so no faithful realization). This audit pins exactly what *does* transfer.

## Result 1 — the exact factorization relation

The Ω characteristic polynomial `χ_Ω = x⁴ − a x³ + (2a−2m−4)x² − a x + 1` factors into two reciprocal
quadratics `(x²−px+1)(x²−qx+1)` with `p+q = a`, `pq = 2a−2m−6`, equivalently the clean identity

> **(p−2)(q−2) = −2(m+1)**.

So the Ω wall parameter `m` is exactly the (shifted) product of the two factor-traces. **[exact]**

## Result 2 — every metallic monodromy is an Ω reciprocal factor (the abelianized spectral image)

The metallic bundle monodromy `φ_M = R^M L^M` has abelianization `[[1+M², M],[M, 1]]`, trace
**`T_M = M² + 2`** (= 3, 6, 11, 18, 27, 38, … for M = 1, 2, 3, …), so its characteristic polynomial is
`x² − T_M x + 1`. Pairing `p = T_M` with a **phase** `q ∈ {2,1,0,−1,−2}` (the finite-order traces
`(x−1)², Φ₆, Φ₄, Φ₃, (x+1)²`) and solving Result 1 gives a genuine Ω point `R_{a,m}` whose charpoly is
`(x²−T_M x+1)·(x²−q x+1)`, **on the live cone (signature (1,3))** at integer lattice points (verified by
instantiating the explicit `R_{a,m}`):

| tower monodromy | × phase | Ω point `R_{a,m}` | charpoly |
|---|---|---|---|
| figure-eight `T=3` | Φ₆ | `(a,m)=(4,−½)` = **Ω₄ = B155** (half-integer) | `(x²−3x+1)(x²−x+1)` |
| **silver `T=6`** | Φ₆ | `(7,1)` **integer**, live cone | `(x²−6x+1)(x²−x+1)` |
| `M=4` `T=18` | Φ₆ | `(19,7)` integer, live cone | `(x²−18x+1)(x²−x+1)` |
| `M=6` `T=38` | Φ₆ | `(39,17)` integer, live cone | `(x²−38x+1)(x²−x+1)` |
| figure-eight `T=3` | Φ₄ | `(3,0)` integer, live cone | `(x²−3x+1)(x²+1)` |
| silver `T=6` | Φ₄ | `(6,3)` integer, live cone | `(x²−6x+1)(x²+1)` |

So the **entire sequence of metallic bundle-monodromy spectra is realized inside the integer Ω family** as
reciprocal factors, paired with a phase. The figure-eight × Φ₆ is the *half-integer* canonical Ω₄ = B155 (its
trace `T=3` is odd); the **even**-`M` monodromies × Φ₆ are genuine **integer** live-cone points (e.g.
`R_{7,1}` is the **silver analogue of Ω₄**). **[exact]**

> **Honest scope.** A 2-parameter reciprocal quartic can be tuned to any (monodromy-trace, phase-trace) pair,
> so the *existence* of such a factorization is not surprising in itself. The content is: (i) the clean wall
> relation `(p−2)(q−2)=−2(m+1)`; (ii) that these realizations land at **integer lattice points on the live
> (signature-(1,3)) cone**, not arbitrary places; and (iii) that the canonical figure-eight case is exactly
> Ω₄ = B155, with a silver integer analogue `R_{7,1}`. It is a **spectral** (charpoly-level) correspondence.

## Result 3 — but no faithful mechanism (the obstruction stands)

The strict-full shears `A = S₀₃` and `C = S₂₃` **commute** (`E₀₃E₂₃ = E₂₃E₀₃ = 0 ⟹ AC = CA`), so the map
`R↦A, L↦C` is only an **abelian image** and cannot represent the *noncommutative* trace-map monodromy
(`RL ≠ LR`). The deeper bridge — a functional pullback of the cubic Fricke invariant `κ = tr[A,B]` (a 3-dim
character-variety coordinate) to the *linear* wall coordinate `δ = 2a−1−m`, or a faithful `R,L` realization —
is **negative / open**: the spectral data transfers, the dynamics does not. **[structural]**

## Verdict (L18 resolved at the spectral level)

**Ω is the abelianized spectral image of the metallic tower:** the full sequence of metallic monodromy
characteristic polynomials is realized as reciprocal factors of the integer Ω family on the live cone (Result
2), governed by the wall relation (Result 1) — but Ω is **not a faithful mechanism** for the tower (Result 3,
commuting shears). This sharpens B156's qualitative "abelianized shadow" to a precise positive statement and
closes the bridge-audit sub-checks: *χ_Ω specializes to the tower's monodromy factors* — **YES (spectrally)**;
*faithful `R,L` realization* — **NO**; *`κ ↦ δ` pullback* — **no functional map** (different invariant types).

## Firewall

Standalone character-variety / arithmetic statement. Signature (1,3) = algebraic inertia, NOT spacetime. No
physics; nothing to `CLAIMS.md`.

## Reproduction

`python frontier/B158_omega_tower_bridge/bridge_audit.py` — prints PASS: the exact relation
`(p−2)(q−2)=−2(m+1)`; the six `R_{a,m}` instantiations (charpoly = monodromy×phase, signature (1,3)); the
commuting-shears obstruction.

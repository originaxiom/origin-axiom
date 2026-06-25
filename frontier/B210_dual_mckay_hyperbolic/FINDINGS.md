# B210 — golden's dual McKay structure (E₈ + E₆), and the WRT face is not the shadow group

**Date:** 2026-06-25. **Status:** two genuinely-uncomputed paths, run. (1) **Golden carries BOTH exceptional
McKay-congruence groups** — `E₈` from its monodromy arithmetic, `E₆` from its (newly computed) hyperbolic
arithmetic. (2) **Resolved-negative:** the WRT modular-rep image at the golden level is *not* `2I` — so the
quantum face and the congruence shadow connect only arithmetically (B208), not as a group. Firewall-clean
representation theory / arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V209**.

## (1) The dual McKay structure — golden carries E₆ *and* E₈

The metallic bundles carry **two** arithmetics: the *real* monodromy field `ℚ(√(m²+4))` (used throughout) and
a *complex* **hyperbolic invariant trace field** (the cusped manifold's own arithmetic) — never computed
before. Computed (SnapPy via sage-python, `invariant_trace_field_gens().find_field`):

| m | bundle | hyperbolic trace field | monodromy field |
|---|---|---|---|
| **1 golden** | m004 | `x²−x+1` = **ℚ(√−3)** (ram. 3) | `ℚ(√5)` (ram. 5) |
| 2 silver | m136 | `x²+1` = **ℚ(i)** (ram. 2) | `ℚ(√2)` (ram. 2) |
| 3 bronze | s464 | degree 8 (non-arithmetic) | `ℚ(√13)` |
| 4 | t03910 | degree 4 (non-arithmetic) | — |

So golden's two arithmetics ramify at **3 and 5 — exactly the two McKay-exceptional congruence primes:**
```
  monodromy  ℚ(√5)  →  prime 5  →  SL(2,𝔽₅) = 2I = E₈   [B206]
  hyperbolic ℚ(√−3) →  prime 3  →  SL(2,𝔽₃) = 2T = E₆   [NEW]
```
`E₇=2O` is excluded — `|2O|=48` is no `|SL(2,𝔽_p)|` (B207) — so **neither** arithmetic can reach it. **Golden
is the unique metallic mean whose both arithmetics hit exceptional McKay primes**; the arithmeticity pattern
across `m=1..7` confirms **golden and silver are the only arithmetic bundles** (degree-2 imaginary-quadratic
trace fields; m≥3 are degree ≥4, non-arithmetic).

**The mod-3 → E₆ step is VERIFIED, not asserted (after a "verify it all" pass).** The figure-eight discrete-
faithful Riley parameter is `u = ω` (the *cube* root of unity, `ω²+ω+1=0` — corrected from an initial 6th-root
slip; both are units in `ℤ[ω]`, so the conclusion is robust). It is a **unit**, so mod `(√−3)` it reduces to a
nonzero element (`ω↦1`, `−ω↦2`), and the two parabolics `A=[[1,1],[0,1]]`, `B=[[1,0],[2,1]]` **generate all of
`SL(2,𝔽₃)=2T`** (order 24, verified) — the figure-eight group *surjects* onto `2T=E₆`, at the same level as
B206's monodromy-mod-5 → `2I`.

**The hyperbolic E₆ has a geometric origin (the hint underweighted at first):** the figure-eight is **two
regular ideal tetrahedra** (both shapes `e^{iπ/3}`, `z²−z+1=0 → ℚ(√−3)`), so the *tetrahedral* field gives the
*tetrahedral* McKay group `2T=E₆` — not a numerical accident. (Silver is octahedral, shape `i → ℚ(i)`.)

**Likely framework — Arnold's trinities.** The triple (tetrahedron, octahedron, icosahedron) ↔ (`E₆`,`E₇`,`E₈`)
↔ (`2T`,`2O`,`2I`) is one of Arnold's "trinities." Golden touches `E₆` (tetrahedral — its building blocks) and
`E₈` (icosahedral — its golden monodromy), missing `E₇` (octahedral); this dual-McKay is plausibly a
manifestation of that trinity. **Novelty therefore UNCHECKED** (this is the likely known home — do not claim).

## (2) The WRT face is not the congruence shadow as a group (resolved-negative)

Is the WRT modular-rep image at the golden level (`SU(2)₃`, `q=e^{2πi/5}`) the group `2I`? **No** — the image
`⟨S,T⟩` has order **2880** (`SL(2,ℤ/20)`-related; `ord(T)` gives congruence level 20, not 5). So the quantum
face is a *bigger* object, **not** `2I`. This **answers** the open question: the WRT↔shadow connection is purely
**arithmetic** (through `det(γ+I)=m²+4`, B208), not a representation-image identity. B208 is the full story of
that link; the quantum face is a different (larger) object.

## Honest status
Trace fields computed (sage-python, solid). The "ramified prime → congruence-McKay group" is the same
construction as B206 (genuine for the arithmetic golden/silver). Ingredients standard; the dual-McKay assembly
(golden carries E₆ *and* E₈ via its two arithmetics, E₇ excluded) is the new connection — **novelty UNCHECKED**
(prior-art not run; do not claim). Firewall: McKay/representation-theoretic `E₆`/`E₈`, **not** physics. Nothing
to `CLAIMS.md`.

## Reproduction
- `python dual_mckay.py` — the dual-McKay structure + the WRT-image order (2880). (pyenv)
- `sage-python verify_trace_fields.sage.py` — the hyperbolic trace fields (Sage-gated).
- `tests/test_b210_dual_mckay_hyperbolic.py` — 3 locks. 3 passed.

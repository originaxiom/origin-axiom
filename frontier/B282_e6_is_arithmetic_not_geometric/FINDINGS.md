# B282 — the figure-eight's E₆ is **arithmetic, not geometric** (the genericity collapse)

**Status: banked (frontier). FIREWALLED. Nothing to `CLAIMS.md`.** The sharpest meta-result of the E₆ arc, prompted
by "what are we missing?" — a verify-don't-trust on the program's own central narrative.

## The computation
Across hyperbolic knots (`e6_specificity_gap.py`, SnapPy + GAP `GQuotients`):

| manifold | vol | arithmetic? | ↠ 2T = SL(2,𝔽₃) (the McKay-E₆ source) |
|---|---|---|---|
| 4₁ = m004 | 2.0299 | **yes** | **2** |
| m003 (its sister) | 2.0299 | **yes** | **2** |
| 5₂ | 2.8281 | no | **0** |
| 6₁ | 3.1640 | no | **0** |
| 6₂ | 4.4008 | no | **0** |
| 7₄ | 5.1379 | no | **0** |

The **2T surjection** — the sole source of the McKay E₆ (B266) — is present *only* for the **arithmetic** cusped
manifolds (4₁ and its commensurable sister m003), and **absent** for every non-arithmetic hyperbolic knot.

## The point: almost all of "4₁ carries E₆" is GENERIC
Every knot above is hyperbolic, so by **Menal-Ferrer–Porti / Falbel–Guilloux** (R6, B281) every one of them has the
*same* "rich" E₆ character variety: `dim H¹ = rank`, smooth point, dense irreducible flat connections, the exponent
grading. **5₂ carries E₆ geometrically exactly as much as 4₁ does.** Strip the arc down:

- **GENERIC** (true of any hyperbolic knot and/or any Lie type — knot- and often group-independent):
  `dim H¹ = rank` (MFP), smoothness (MFP), irreducibility/density (B281, a knot-independent Lie fact), the exponent
  grading, the 27, the central charges, the conformal embedding `(E₆)₁ ⊃ SU(3)×SU(2)×U(1)` (a property of the chiral
  algebra, manifold-independent).
- **OBJECT-SPECIFIC** (what 5₂ lacks): the **arithmetic 2T atom** — 4₁ is the *unique arithmetic knot* (Reid), trace
  field ℚ(√−3), ramified prime 3 → 𝔽₃ → 2T → McKay E₆. And (partially) the **τ = E₆ outer-automorphism** reading
  (needs amphichirality). These are *exactly* the two R6 NEEDS-SPECIALIST kernels.

## What this tells us
**The program's apparent richness collapses to a single number-theoretic atom.** The dozens of E₆ computations are
the generic shadow of *choosing* E₆; they do not distinguish the figure-eight or point at physics. The only thing
the figure-eight has that nothing else does is that **it is the unique arithmetic knot**, and its E₆ is the **McKay
shadow of that arithmetic**. Consequences:

1. The in-sandbox E₆ program is **exhausted of object-specific content**: everything new at the character-variety /
   Lie / conformal level would be generic. The genuine content = the two specialist kernels = the CRUX (B281). One
   small gate, reached not because the structure is deep but because it is generic and we kept re-deriving it.
2. If the bridge to physics works, it **must** run through the arithmetic atom (Reid-uniqueness → ℚ(√−3) → 2T →
   McKay), not the generic structure. The live, under-explored, object-specific vein is the **arithmetic
   self-generation** (the metallic WRT tower, period = order of the fundamental unit; the trace-map dynamics) — not
   the E₆-gauge bridge.

This is firewall-clean and *strengthens* the structural theorem: the object supplies structure (generic), and its
one specific signal is arithmetic, not physical. `e6_specificity_gap.py` · `verdict.py` ·
`tests/test_b282_e6_arithmetic.py`.

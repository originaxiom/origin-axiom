# B260 — the Coulomb-branch reframing of wall #1

**Status: banked observation (frontier). FIREWALLED — 3d-3d / quantum topology, NOT physics. Nothing to
`CLAIMS.md`.** The "next stone" from B259: is wall #1 (`SL(2,ℂ)` can't embed in compact E₆) even the right question?
`coulomb_branch.py` (pyenv, sympy).

## The reframing
In the 3d-3d correspondence (Dimofte–Gaiotto–Gukov), the `SL(2,ℂ)` character variety of the figure-eight **is the
Coulomb branch** of the 3d N=2 theory `T[4₁]`. Its defining equation is the **A-polynomial**; the meridian/longitude
eigenvalues `(M,L)` are complexified **fugacities** (masses/FI parameters), not gauge-field holonomies. A Coulomb
branch is *supposed* to be complex and non-compact — so "embed `SL(2,ℂ)` in compact E₆" is a category error.

**Verified (sympy):**
- `A_geom(M,L) = M⁴L² − (M⁸−M⁶−2M⁴−M²+1)L + M⁴` (Cooper–Culler–Gillet–Long–Shalen).
- complete hyperbolic structure: `M=1` (parabolic meridian) → `A=(L+1)²` → `L=−1` (parabolic longitude). ✓
- Newton-polygon edge slopes `±4` = the figure-eight boundary slopes (independent confirmation it's `4₁`'s).
- balanced curve: `L + 1/L = u² − u − 4` with `u = M²+M⁻²` (clean over ℚ).

## What the stone gives — honestly, both halves
- **(+) It dissolves the false obstruction.** The `SL(2,ℂ)` was never a gauge holonomy, so compactness is
  irrelevant. After B260 the wall map has **zero theorems blocking "object → physics"** — only open gaps (#2/#3/#4)
  and the 122-order quantitative gap (#5). chat1's "gaps, not theorems" is vindicated; even the one "theorem" (#1)
  was about a *wrong bridge* (the holonomy-breaking idea B247 killed), not the general possibility.
- **(−) It does not manufacture a bridge.** `T[4₁]` (from its 2 ideal tetrahedra) is an **abelian** theory (U(1)
  CS + chirals; flavor = the cusp `U(1)/SU(2)`). There is no E₆ on the gauge side. The McKay-E₆ stays *arithmetic*
  (trace field `ℚ(√−3)→2T→E₆`), so **wall #2 is unmoved**.
- **(=) Net: B260 improves honesty, not proximity.** The real walls (#2/#3/#4/#5) are exactly as far as before; #5
  is still 122 orders. Dissolving a confusion is not the same as building a bridge — the discipline cuts both ways
  (chat2's caution applies to *my own* enthusiasm for the reframing).

## The through-line (the genuinely nice part)
The Coulomb branch **quantizes**: the quantized A-polynomial is the `q`-difference operator annihilating the colored
Jones (AJ conjecture, Garoufalidis; proved for `4₁`). So
> classical Coulomb branch (A-poly, this probe) — *quantize* → colored Jones recursion → the two ends
> (B258: Kashaev `N→∞` = hyperbolic/E₆; golden root = spherical/E₈).

The Coulomb-branch face is the **classical shadow of the quantum face** we already banked — one more view of the
same object, *not* a new bridge to physics. That is the honest signal: the object keeps resolving into the same
two-ended structure across every face (geometry / arithmetic / quantum / now the Coulomb branch), and the SM stays
on the far side of the open gaps.

## Wall-map update (refines B259 #1)
| # | wall | B259 status | **B260 status** |
|---|---|---|---|
| 1 | `SL(2,ℂ)` vs compact E₆ | THEOREM | **true theorem, but the wrong question** — *not* an obstruction to "object→physics"; it refutes one wrong bridge. |

So the corrected count: **0 theorems blocking the program**, 3 open gaps (#2/#3/#4), 1 quantitative 122-order gap (#5).

Anchors: B247 (the #1 theorem), B250 (complex volume on the geometric component), B258 (the quantum two ends),
B259 (the wall map), K006 (3d-3d). Lit: Dimofte–Gaiotto–Gukov 2011 (3d-3d, `T[M]`); Cooper et al. (A-polynomial);
Garoufalidis (AJ conjecture, `4₁`).

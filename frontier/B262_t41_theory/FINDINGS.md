# B262 — Rung 1: `T[4₁]` reconstructed from its triangulation

**Status: banked observation (frontier). FIREWALLED — 3d-3d / quantum topology, NOT physics. Nothing to
`CLAIMS.md`.** First rung of the systematic `T[4₁]` build (the patient, no-jumping path toward the physics goal:
nail down the actual theory before asking whether E₆ can be dynamical). `t41_theory.py` (pyenv, numpy);
ground truth in `t41_gluing_sage.py` (SnapPy).

## Why this rung
Through the whole arc we *asserted* "`T[4₁]` is abelian, U(1) + chirals" on DGG's authority. We never computed it.
That is the skipped step under walls #2 (is E₆ ever dynamical) and #4 (the 4d lift) — you cannot honestly ask
either without the theory in hand. So: reconstruct it ourselves, ground-truth first.

## Ground truth (SnapPy)
`4₁` = **2 ideal tetrahedra, 1 cusp**; complete-structure shapes `z₀ = z₁ = e^{iπ/3}` (regular ideal tetrahedra).
Edge gluing equations (rect `[a₀,a₁,b₀,b₁,c]`, meaning `∏ᵢ zᵢ^{aᵢ}(1−zᵢ)^{bᵢ}=(−1)^c`):
`edge₁=[2,2,−1,−1,1]`, `edge₂=[−2,−2,1,1,1]=−edge₁` (dependent → **one** independent constraint).
Cusp: `meridian=[1,1,0,−1,−1]`, `longitude=[0,4,0,−2,1]`.

## DGG dictionary, applied transparently
| ingredient | rule | result for `4₁` |
|---|---|---|
| matter | one chiral per tetrahedron | **2 chirals** `Φ₀,Φ₁` |
| gauge group | rank `= N_tet − N_cusp` | `2−1 = 1` → **U(1)** |
| (cross-check) | rank of the edge-exponent matrix | `1` (since `edge₂=−edge₁`) → 1 internal edge → 1 gauged U(1) ✓ |
| flavor | one U(1) per cusp | **U(1)** (meridian `m`), + cusp Weyl **ℤ/2** (`m↔1/m`) |
| CS levels | `−1/2` per chiral + gluing | integer gauge/mixed matrix fixed by the NZ symplectic frame (**Rung 1b**) |
| superpotential | one monopole term per internal edge | **monopole**, 1 edge |

## Verdict (earned, not asserted)
> **`T[4₁]` = U(1) gauge theory, 2 chirals, flavor `U(1)_m × Weyl ℤ/2` — abelian.**

The gauge rank is **1**, confirmed two independent ways (symplectic count `N_tet−N_cusp`; edge-equation rank). There
is **no nonabelian gauge factor**, hence **no E₆ on the gauge side**: the McKay-E₆ (trace field `ℚ(√−3)→2T→E₆`) is
confirmed **arithmetic-only**. Wall #2 is now sharpened with the actual theory in hand, not on citation.

## Consistency with the shadows we already banked
- **2 chirals ↔ 2 quantum dilogarithms; 1 gauged U(1) ↔ 1 integral** — exactly the shape of the figure-eight
  **state integral**. Rung 3 will verify the `S³_b` partition function reproduces B250's complex volume and B261's
  colored Jones.
- The classical **Coulomb branch must reproduce the A-polynomial** (B260) — the Rung-2/3 correctness gate.

## The next rungs
- **Rung 1b:** pin the integer CS matrix by completing the NZ symplectic frame.
- **Rung 2:** the flavor symmetry precisely, and the cusp Weyl `ℤ/2` (`m↔1/m`) — *where, if anywhere, does it
  enhance to SU(2)?* (S033 territory: the one honest place wall #2 gets tested rather than asserted.)
- **Rung 3:** the partition functions (state integral / index / holomorphic blocks); close the loop with
  B250/B260/B261.

Anchors: B260 (Coulomb branch / A-polynomial), B261 (AJ / colored Jones), B250 (complex volume), B247 (the wall),
K006 (3d-3d). Lit: Dimofte–Gaiotto–Gukov 2011 ("Gauge Theories Labelled by Three-Manifolds"); Neumann–Zagier;
Thurston (gluing equations).

# B287 — The distinguished closing: the object re-sees its own A=LR at a canonical seam

**Status: banked. Math (topology) verified three independent ways; nothing to `CLAIMS.md`.** Answers the load-bearing
question B286 left open — *are the closings **selective** (one distinguished world) or a flat **catalogue**?* For the
object's **own structure** the answer is **selective**: there is a canonical, forced, distinguished closing, and it
re-instantiates the proven core.

## The result
The figure-eight is a **once-punctured-torus bundle**, so the **fiber slope** (the boundary slope of the fiber, the
`0`-surgery `m004(0,1)`) caps the puncture and yields the **closed Sol torus bundle whose monodromy is exactly
`A = [[2,1],[1,1]]` = the `A=LR` of `P1`** (trace 3, eigenvalues `φ²,φ⁻²`). Among the **10** exceptional Dehn
fillings it is the **unique** torus bundle (Sol); the rest stratify.

| slope `(n,1)` | `H₁` | type | recognition |
|---|---|---|---|
| **0** | **ℤ** | **Sol — torus bundle** | **Regina: `T x I / [ 2,1 | 1,1 ]`** — monodromy **exactly A** |
| ±1 | 0 | Seifert | Brieskorn `Σ(2,3,7)` (classical; Regina recognizer incomplete on the simplified triangulation) |
| ±2 | ℤ/2 | Seifert | Regina: `SFS [S²:(2,1)(4,1)(5,−4)]` |
| ±3 | ℤ/3 | Seifert | classical |
| ±4 | ℤ/4 | toroidal | Regina: `SFS [D:(2,1)(2,1)] U/m SFS [D:(2,1)(3,1)]` (graph manifold) |
| meridian | 0 | `S³` | (the 10th) |

## Three independent confirmations of the headline (verify-don't-trust)
1. **Alexander polynomial** of m004 `= t²−3t+1 = charpoly(A)` (SnapPy). The Alexander polynomial of a fibered knot is
   the characteristic polynomial of the monodromy on `H₁(fiber)` ⟹ the monodromy is conjugate to `A`.
2. **Twister**: the once-punctured-torus bundle with monodromy word **`aB = t_α t_β⁻¹ = [[2,1],[1,1]] = A`** is
   **isometric to m004** (`is_isometric_to = True`, both hyperbolic). So m004 *is* the `A`-bundle.
3. **Regina** recognises `m004(0,1) = T x I / [[2,1],[1,1]]` — the closed torus bundle with monodromy **exactly A**,
   independently of the hyperbolic geometry (combinatorial recognition). It is the only `T x I /` member of the 10.

## Uniqueness is homology-forced (red-team strengthening, Arc II)
The "unique torus bundle" headline does **not** depend on Regina's recognizer (which returns `None` on the ±1,±3
simplified triangulations): a closed **torus bundle** has `b₁ ≥ 1` (the `ℤ` from the base circle), but **every**
non-zero exceptional filling has **finite `H₁`** (ℤ/2, ℤ/3, ℤ/4) or is `S³` — so none of them *can* be a torus
bundle, regardless of recognition. Only `(0,1)` (with `H₁=ℤ`) survives. (And "monodromy **exactly** `A`" is Regina's
canonical normal form; method 1, the Alexander polynomial, states the weaker honest "conjugate to `A`" — consistent.)

## The P8 connection (the torsion ladder)
`|det(Aⁿ − I)| = 1, 5, 16, 45, 121, 320, … = L_{2n} − 2` (Lucas) is the `H₁`-torsion of the **closed `Aⁿ` torus
bundles** — the fiber-direction cyclic covers. The distinguished closing is the **`n=1` base** (torsion `1`, hence
`H₁(m004(0,1)) = ℤ`, matching the table). So B287 ties the seam to **both** `P1` (the matrix `A`) and `P8` (its
torsion ladder): the object's own proven-core dynamics is exactly what the canonical closing re-instantiates.

## The fence (kept honest)
This is **selective for the program's own structure** — a clean, forced, distinguished closing that re-sees `A=LR`.
It is **not** a selection of a Standard-Model world: which closing (if any) is "our universe" is not decided here, and
the reading "the distinguished closing = the actual world" is a `[HOOK]` for `speculations/`, not banked. What is
*not* speculative: the object is a once-punctured-torus bundle, the fiber closing is the unique Sol torus bundle among
the 10 exceptionals, and its monodromy is exactly `A` (three methods). The `±1,±3` Seifert *labels* are classical
(Regina's recognizer returns `None` on their simplified triangulations); they are **not** load-bearing — the headline
is the unique torus bundle, which Regina recognises positively.

## Consequence for the seam arc
The selection spine has its anchor: the seam is **selective for the object's own structure**. This is the highest-
confidence result of the arc and frames the rest — B288 asks whether any closing is *arithmetically* distinguished
(re-sees `ℚ(√−3)`/E₆), B291 whether any is *scale*-distinguished; B294 assembles the selection table.

`distinguished_closing.py` (sage-python: SnapPy+Regina+Twister) · `verdict.py` (pyenv) ·
`tests/test_b287_distinguished_closing.py`. Related: `P1` (A=LR), `P8` (torsion ladder), `B286` (the seam),
`B277` (the fiber Σ_{1,1} / class-S), `B262` (T[4₁]).

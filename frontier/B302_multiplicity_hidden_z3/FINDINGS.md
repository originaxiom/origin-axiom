# B302 — The multiplicity thread: the generation ℤ/3 is the figure-eight's hidden symmetry

**Status: banked (frontier). The math is verified + citable; the generation reading is firewalled; nothing to
`CLAIMS.md`.** The first real result of the **multiplicity thread** opened by the fresh-eyes root insight: a *value*
is relational, the object is a monad (P009), and the two open walls map onto the owner's two relational sources —
Wall A (couplings) ↔ the seam, **Wall B (generations) ↔ multiplicity**. This pursues Wall B and **locates the ℤ/3
where the root insight predicted: in the relation, not the object.**

## The reframe
B298 said one object cannot make a multiplicity of 3 (the degree-2 obstruction). The fresh reading: the "3" is **not
in the object** — it is in the object's **relation to its arithmetic siblings**, the commensurability class. And the
degree-2 obstruction is, more precisely, *"the knot group is torsion-free."*

## The result — the ℤ/3 is a hidden symmetry
| | the object | the relation (commensurator) |
|---|---|---|
| order-3? | **no** — Sym(m004) = D4 (order `8 = 2³`); knot group **torsion-free** | **yes** — PGL(2,O₋₃) has order-3 elements |

- **(A) the object has no order-3.** SnapPy: `Sym(m004) = D4` (order 8), and a knot complement group is torsion-free.
- **(B) the commensurator does.** m004 is **the** arithmetic ℚ(√−3) knot (B282), so by **Neumann–Reid** its
  commensurator is the Bianchi group **PGL(2,O₋₃)**, which has **order-3 elements** — because ℚ(√−3) carries the
  **Eisenstein units** `ω` (the only imaginary-quadratic field besides ℚ(i) with extra units). Exhibited:
  `[[0,−1],[1,−1]]` (order 3 already in SL(2,ℤ)) and the Eisenstein `diag(ω,1)` (order 3). These are **hidden
  symmetries** — in the commensurator, *not* in the symmetry group, *not* in the knot group.
- **(C) the figure-eight covers the order-3 orbifold.** It is an **index-12 cover** (Riley; covolume re-computed via
  Humbert) of the minimal orbifold `ℍ³/PGL(2,O₋₃)`, which carries the order-3 torsion. Its **sister m003** (B282) is
  in the same class (same volume 2.0299, same field).

## Why this is the answer the root insight predicted
- **It locates the multiplicity in the relation.** The ℤ/3 lives in the commensurability class (how the object
  relates to its siblings and covers), not in the single object — exactly "Wall B ↔ multiplicity."
- **It explains B298.** The degree-2 obstruction is the knot group being torsion-free; the single object *provably*
  can't carry the order-3, so it must be relational. B298 and B302 are two views of one fact.
- **It is tied to B282.** The figure-eight has hidden symmetries **precisely because** it is the arithmetic ℚ(√−3)
  knot — Neumann–Reid's unique example (the figure-eight and the two dodecahedral knots are the only knots
  conjectured to have hidden symmetries). The one object-specific atom (the ℚ(√−3) arithmetic) is *also* the source
  of the hidden ℤ/3. The same atom, seen as a multiplicity.

## The fence
The **math** is solid and citable (Neumann–Reid hidden symmetries; Riley's index 12; the Eisenstein order-3). What is
**not** claimed: that this ℤ/3 *is* the generation symmetry — that identification is the physics dictionary,
**firewalled** ([LEAP] in `speculations/S045`). B302 **locates** a ℤ/3 in the structurally-right place (hidden,
relational, arithmetic); it does **not** derive three generations. Nothing to `CLAIMS.md`.

`multiplicity_hidden_z3.py` (sage-python: SnapPy Sym + the order-3 over O₋₃ + the covolume index) · `verdict.py`
(pyenv re-check) · `tests/test_b302_multiplicity_hidden_z3.py`. Related: `B298` (the degree-2 obstruction — explained
here), `B282` (the arithmetic atom / the unique ℚ(√−3) knot), `B266` (2T→McKay-E₆), `P009` (monadic closure),
`S045` (the firewalled reading). Lit: Neumann–Reid (hidden symmetries, arithmetic of hyperbolic manifolds); Riley
(figure-eight index 12 in PSL(2,O₋₃)); Humbert (Bianchi covolume).

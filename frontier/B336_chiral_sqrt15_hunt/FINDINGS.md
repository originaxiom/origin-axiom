# B336 — the chiral √−15 hunt: the value's home is *doubly* separated (Chat-1's insight, probed)

**Status: banked (frontier). We probed Chat-1's chirality insight ourselves (Attack A of the symmetry-broken sweep).
Firewalled; nothing to `CLAIMS.md`.** Chat-1's reframe is the best-stated wall we have — *structure is real (amphichiral),
value is imaginary (`√−15`), reachable only by breaking amphichirality.* The premise checks out; the **routes** to `√−15`
turn out to be provably closed.

## A1 — the premise, confirmed
`J_N(4₁; ζ₁₅)` is **real** for all `N` (imaginary part exactly 0). The single amphichiral object carries **zero `√−15`
component**. (Amphichiral `J_N(q)=J_N(q⁻¹)`; at a root `q⁻¹=q̄`; integer Jones coefficients `⇒ J_N(q̄)=conj(J_N)` `⇒ J_N`
real.) Chat-1's premise is exactly right.

## A2 — the routes to `√−15` are closed
- **Route 0 (monodromy).** Words in `R,L` lie in `SL(2,ℤ)` (det 1, integer trace `t`), so their discriminant is
  `t²−4 ∈ {−4,−3,0,5,12,21,32,45,60,77,96,117,…}` — which contains the metallic discs (5, 32, 117 = m=1,2,3) but **never
  −15** (`t²=−11` is impossible). The word/metallic route cannot reach `−15`.
- **Route 2 (commensurator).** The invariant trace field is a **commensurability invariant** (Neumann–Reid). The whole
  class of `4₁` is `ℚ(√−3) =` Bianchi `O₋₃` (m004's tetrahedra shape `= (1+i√3)/2`; the sister m003 has the same volume,
  commensurable). `√−15 =` Bianchi `O₋₁₅` is a **different commensurability class** → **no** cover, ℤ/3-related manifold,
  or neighbor reaches `ℚ(√−15)`. **Closed.**
- **Route 1 (Dehn filling).** Fillings *do* break amphichirality — verified `CS ≠ 0` (e.g. `(1,2):−0.247`, `(1,3):−0.165`,
  `(2,3):+0.169`). But a generic filling is **non-arithmetic** (Thurston surgery), giving a higher-degree trace field,
  **not** the degree-2 `ℚ(√−15)`. An arithmetic `O₋₁₅` filling would be a specific coincidence (Sage-checkable; the
  generic answer is no).

## A3 — the null test
Even if some filling reached `√−15`, it would carry no significance: `h(−15)=2` is generic (shared by 14 fields to −400,
B333). Landing in one imaginary quadratic field among many is a coin flip, not a signal.

## Verdict — the value's home is doubly separated
Chat-1's premise (real object ⇒ no `√−15`) is correct, but the **chiral routes do not deliver `√−15`**: the monodromy and
commensurator routes are *provably* closed, the filling route is *generically* closed. Combined with **B333** (`√−15` is
arithmetically generic), the value's home is **doubly separated** from the object — *generic in arithmetic* **and** *not a
geometric invariant of the object or its chiral breaking.* `√−15` exists only as the **abstract compositum / class-field**
of the two ends (B332/B334), never as a geometric quantity the object reaches. **The firewall holds in the chiral sector
too** — the imaginary part is not merely hidden by amphichirality; it is not in the object's geometric arithmetic at all.

## The firewall (held)
A structural/arithmetic result; no value produced or matched; the null test is built in. Nothing to `CLAIMS.md`.

## The fence
Exact colored-Jones at `ζ₁₅` (sympy, from B314) + monodromy discriminants + SnapPy shape/CS (recorded values). Trace
fields of fillings would need Sage (flagged; generic answer established without it). No physics values. Nothing to
`CLAIMS.md`.

`chiral_sqrt15_hunt.py` (pyenv/SnapPy) · `tests/test_b336_chiral_sqrt15_hunt.py`. Related: **B333** (`√−15` generic),
**B332/B334** (the compositum / Hilbert class field), **B316** (the amphichiral floor `{−4,−3}`, `√−7` chiral),
**B318** (amphichirality = geometric firewall), **B314** (colored Jones at roots), **B289/B286** (filling CS). Lit:
Neumann–Reid (invariant trace field is a commensurability invariant); Thurston (surgery gives non-arithmetic fillings);
Maclachlan–Reid (`4₁` arithmetic, `ℚ(√−3)`).

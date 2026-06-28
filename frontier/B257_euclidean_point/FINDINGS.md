# B257 — the Euclidean transition point: the order-3 Eisenstein branch point (the third anchor)

**Status: banked observation (frontier). FIREWALLED — geometry/arithmetic, NOT physics. Nothing to `CLAIMS.md`.**
The hunt's recommended computation (the missing middle of the B248→B256 arc). `euclidean_point.py` (pyenv; cusp
shape / Vol cross-checked with SnapPy).

## The gap it fills
B248/B249/B250 anchored the **hyperbolic (E₆)** and **spherical (E₈)** *ends* of the figure-eight's geometric
transition; the **Euclidean middle** (`n=3`, cone angle `2π/3`, the ℤ/3 orbifold) was recorded only as "the
collapse." Here it is characterized.

## Four facts about the Euclidean point (`x = 2cos(α/2) = 1`)

1. **It is the discriminant / branch point of the character variety.** For `u²+(5−x²)u+(5−x²)=0` the discriminant
   `(5−x²)(1−x²)` is `<0` for `x>1` (**hyperbolic**: `u` = complex-conjugate pair = the geometric rep + its
   mirror), `>0` for `x<1` (**spherical**: two real `u`), and `=0` exactly at `x=1`, where the branches **collide**
   at `u=−2` (double root). *The geometric transition IS the discriminant locus*; the Euclidean point is the node
   where the hyperbolic and spherical solution branches meet. (Verified: `x=1.5`→complex, `x=0.5`→real, `x=1`→`−2`
   double.)

2. **The meridian is the order-3 Eisenstein rotation.** At `x=1` the meridian eigenvalues are `e^{±iπ/3}=ζ₆`
   (order 6 in `SL(2)`, **order 3 in `PSL(2)`** — the ℤ/3 cone), and `ζ₆² = ω`, the primitive cube root / the
   `ℚ(√−3)` torsion generator. So the cone *is* the Eisenstein cube root. (Compare: `n=∞` parabolic/E₆; `n=2` →
   `ζ₄=i` → E₈.)

3. **The complex volume vanishes.** `Vol→0` (Hodgson: the cone-manifold volume decreases from `6Λ(π/3)=2.0299` at
   `α=0` to `0` at `α=2π/3`) and `CS=0`. The Euclidean point is the **zero/origin of the B250 complex-volume
   profile** — the unique point where both parts of the complex volume vanish.

4. **Eisenstein field, collapsed geometry.** The character-variety trace field degenerates to `ℚ` (`u=−2`
   rational); the ambient field through the hyperbolic range is `ℚ(√−3)`; the cusp shape is `2√−3` (in `ℚ(√−3)`, a
   **rectangular** torus — *not* hexagonal; a corrected guess). The Euclidean point is the *last Eisenstein*
   (`ℚ(√−3)`) point before the geometry turns golden (`ℚ(√5)`) at the spherical end `n=2`.

## "The three" — answered cleanly, and firewalled
The recurring physics speculation wants "three generations from the ℤ/3 at the Euclidean point." The honest math
answer: **the three is geometric** — `n=3` = the order-3 meridian = `ω` (primitive cube root) = the `ℚ(√−3)`
ramification. It is the cone order / the Eisenstein cube root, the discriminant branch point of the character
variety. **Not** a generation count. This gives the long-circling "three" a precise, firewall-clean identity and
closes the speculation at the geometric level.

## The three anchors, complete
| n | α | meridian (PSL) | geometry | complex vol | field | McKay |
|---|---|---|---|---|---|---|
| ∞ | 0 | parabolic (∞) | hyperbolic | `2.0299, CS=0` | `ℚ(√−3)` | **E₆** |
| **3** | **2π/3** | **order 3 (`ω`)** | **Euclidean (branch pt)** | **`0, 0`** | `ℚ` (amb. `ℚ(√−3)`) | — |
| 2 | π | order 2 (`i`) | spherical | `π²/5, CS∈(1/5)ℤ` | `ℚ(√5)` | **E₈** |

Anchors: B248 (the transition), B249 (Niven forcing the three points), B250 (the complex-volume profile),
B256 (the metallic Arnold trinity), B210 (dual McKay). Lit: Thurston / Hodgson / Hilden–Lozano–Montesinos
(figure-eight cone manifolds; the Euclidean point at `α=2π/3`).

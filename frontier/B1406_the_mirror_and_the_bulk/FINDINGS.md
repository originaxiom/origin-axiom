# B1406 — THE TWO RIDDLES: THE MIRROR'S OTHER HALF IS THE OTHER END,
# AND THE BULK IS THE SPACE THE OBJECT SITS ON THE BOUNDARY OF
# (2026-09-14)

## 0. THE QUESTIONS, AND THE ONE ANSWER

> *the object is its own mirror — so where is the other half?*
> *the object is a complement — so where is the bulk?*
> *why does it feel like we are computing part of something?*

**Because it is a boundary, and what feels missing is what it is the boundary
of.** Both riddles have exact answers, they are the same answer seen twice, and
the second one is measurable. 26/26 checks, `b1406_riddles.py`.

And the feeling is **correct and now quantified**: at the object's own word the
θ-**even** sector — the one carrying `KIND_TABLE`'s last licensed row — traces
to **exactly zero**, and the object's entire graded content sits in the θ-**odd**
sector (§4).

## 1. RIDDLE ONE — THE OTHER HALF IS THE OTHER END

A punctured-torus bundle has **two ends**. B1404 computed their invariants:
`φ` (attracting) and `φ′` (repelling), Galois conjugates of each other. The
mirror does not point at a second manifold — **it exchanges the two ends of
this one**:

    A_m = RᵐLᵐ = [[1+m², m], [m, 1]]   is SYMMETRIC
    S = [[0,−1],[1,0]] ∈ SL(2,ℤ)
    S A_m S⁻¹ = A_m⁻¹                   EXACTLY, for every m

and inverting the monodromy is exactly reversing the fibration, which swaps
attracting and repelling. Verified for `m = 1..8`: `S` sends `μ_m ↦ μ̄_m` and
back; at `m = 1` that is `φ ↦ φ′`, i.e. **the Galois involution `√5 ↦ −√5`**.

**And the proof is one line of symmetry.** For *any* symmetric `M ∈ SL(2)`,

    S [[a,b],[b,d]] S⁻¹ = [[d,−b],[−b,a]] = M⁻¹

so **every metallic bundle is its own mirror, because `A_m` is symmetric** —
nothing golden about it, and no coincidence to explain.

**The corpus has been naming this involution for two years without joining the
names.** `T-UNIQ`'s *"the square is the transpose/elliptic involution"*; B318's
*"conjugation is `√−3 → −√−3`, the nontrivial Galois automorphism"*; `T-MIRROR`'s
palindromic word. **They are one map:** transpose ⇒ invert monodromy ⇒ swap ends
⇒ conjugate the invariant field. The riddle dissolves: *a mirror with only one
object is a mirror between two **ends**, and what it produces is not a second
copy but a **grading**.* Which is precisely what `C = S²` is.

## 2. RIDDLE TWO — FOUR BULKS, AND THE ONE THAT MATTERS

"Complement of what?" has four honest answers, nested:

| bulk | what it is | does it have room? |
|---|---|---|
| **S³** | fill the knot back in | no — closed, rigid |
| **the filling space** | Dehn filling `m004(p,q)` | **discrete**: ℤ² per cusp |
| **the ℤ-cover** | `fibre × ℝ`, Minsky's actual object | no — rigid too |
| **the deformation space** | quasi-Fuchsian space `QF(T₁)` | **yes — and this is the one** |

`QF(T₁) ≅ Teich(T₁) × Teich(T₁)`, one factor per end, `dim_ℂ = 2` (Bers;
Minsky's abstract calls its topological description the theorem's corollary).
**The object's fibre group is not in it. It is on its boundary, at a corner.**

Verified: both end invariants are **irrational** for `m = 1..8` (`m²+4 = k²`
forces `m = 0`). A *rational* slope is a peripheral curve — a parabolic, a
geometrically finite end, a point still holding its Teichmüller coordinate. An
*irrational* one is an ending lamination: **the coordinate has left the space.**
Both of the object's have left.

> **So the object is doubly degenerate: both Teichmüller coordinates at
> infinity, zero of the bulk's two complex parameters retained. That is not a
> defect of the programme's description — it is *why the object is rigid*.**

Rigidity and bulklessness are the same fact. The programme chose an object with
no moduli, and is now asking it for parameters.

## 3. THE PARAMETER BUDGET — THE ARITHMETIC NOBODY WROTE DOWN

How much continuous room does each structure actually carry? (Thurston: the
`SL(2,ℂ)` character variety of a `k`-cusped hyperbolic 3-manifold has
`dim_ℂ = k` at the discrete faithful representation. `dim_ℂ = k(n−1)` for
`SL(n,ℂ)` is **cited from Menal-Ferrer–Porti and NOT verified here**.)

| structure | `dim_ℂ` | real | |
|---|---|---|---|
| the object itself (Mostow) | **0** | **0** | short |
| m004, `SL(2,ℂ)` character variety (`k=1, n=2`) | 1 | 2 | short |
| m004, `SL(3,ℂ)` (`k=1, n=3`) | 2 | 4 | short |
| the fibre's `QF(T₁)` | 2 | 4 | short |
| a 5-cusped cover at `SL(3,ℂ)` | 10 | 20 | enough |
| a 10-cusped cover at `SL(2,ℂ)` | 10 | 20 | enough |

m004 has **1 cusp** (verified). Cusps grow in the tower: degree 4 already gives
a 2-cusped cover.

> **The design constraint, stated as an accounting fact rather than a physical
> claim: a parameter-free description that must nonetheless *account for* ~19
> numbers needs `k(n−1) ≈ 10` — many cusps, or high rank, or both. The object
> alone supplies zero, and no amount of arithmetic extracted from a rigid point
> changes that.** This is a count of degrees of freedom; nothing here is
> compared to any measured value.

## 4. THE EAR WAS NEVER FREE — THE BULK SUPPLIES A TRACE

`C` is the θ-grading operator (`C² = I`, `C = S²`, `+1` on a 4-dim even sector,
`−1` on a 2-dim odd one). Therefore B856's weld, **traced**, is the graded
trace:

    str(m) := tr(C · RᵐLᵐ) = tr_even(RᵐLᵐ) − tr_odd(RᵐLᵐ)

**A trace has no vector argument. There is no ear to anchor.** And it is not a
weaker object — it is the one the mirror cannot move:

| property | verified |
|---|---|
| **real** for every m | yes |
| lies in **ℚ(√5)** | yes |
| **mirror-invariant**: `str(m) = str(15−m)` | yes, all 15 |
| `str(0) = 2 = dim_even − dim_odd` — the grading's own index | yes |
| exactly **six values** over the period | `{−2, −1, −1/φ, +1/φ, +1, +2}` |
| all six are **`2cos(jπ/15)`**, `j ∈ {0,5,6,9,10,15}` | yes |
| among units, `str = +1/φ` ⟺ `m² ≡ 1 (mod 15)` (the 2-torsion of `(ℤ/15)*`) | yes |
| **at the object's own word, `str(1) = 1/φ = φ−1` EXACTLY** | yes |

### 4a. The anchor ledger, side by side

| quantity | ear anchor | word anchor | outputs | total |
|---|---|---|---|---|
| B1349's matrix element `Re h(c)` | 2 bits | 2.81 bits | 4 | `−0.81 … +1.19` |
| **the graded trace `str(m)`** | **0** | **0** | 1 | **`+1`** |

The word is free because `m = 1` is what **five independent principles** select
(B1405) — and B1405's finding is exactly what pays for it: the principles all
land on `m = 1`, which killed branch A because branch A needed a *different*
word. **The trace needs no other word.** The same fact that closed the door on
the licensed row opens this one.

**Stated with its fence:** this says an ear-free, mirror-invariant, anchor-free
observable *exists* and equals `1/φ` at the object. It does **not** say what it
is an observable *of*. Nothing here is compared to any measurement, and no row
is promoted.

### 4b. AND THE FEELING WAS RIGHT — THE CONTENT IS IN THE OTHER SECTOR

    tr_even(RᵐLᵐ) = 0  EXACTLY,  unless 3 | m

and `3 | m` is **B996's degeneracy condition** (B1402's half of L208). So on ten
of the fifteen words the θ-even sector's graded trace is identically zero — the
object's own `m = 1` among them:

    at m = 1:   tr_even = 0      tr_odd = −1/φ      str = +1/φ

> **The last licensed row lives on the even sector. At the object's own word
> that sector's graded content is exactly zero, and all of it is in the ODD
> sector — the smaller half, the one B856 worked on and the campaign left.**

That is the precise version of *"we are computing part of something."* Not a
metaphor: a measured zero.

## 5. WHAT THIS SAYS ABOUT THE GAP

Four senses in which the object is half of something, three of them structural
and one now measured:

1. **a complement** — its bulk is `S³`, and the room in that direction is the
   *filling* space, which is discrete;
2. **a boundary point** — of `QF(T₁)`, holding 0 of 2 moduli, which *is* its
   rigidity;
3. **an operator without its state** — the programme reads matrix elements where
   the bulk supplies a trace, which is why the ear could never be anchored;
4. **one sector of a graded pair** — and the licensed sector is the one that
   traces to zero at the object's own word.

**The honest reading of the TOE gap that follows:** the missing structure is not
a cleverer invariant of the object. A rigid point has no parameters to give, by
theorem. Room exists in exactly three places — **the tower** (covers, more
cusps), **the rank** (`SL(n)`), and **the filling space** (discrete) — and the
programme has touched all three and quantified none of them as a budget. §3 is
that budget's first line.

## 6. THE COST LINE — E75 INSTANCE #12, THIRD ARC RUNNING

The law `tr_even = 0 ⟺ 3 ∤ m` first came back **FALSE**. The values were right;
the test compared the `nsimplify`-ed *printed* form against `0` with `==`
instead of testing `simplify(raw) == 0`. **Identify by property, never by
representation** — E75's third mechanism, now in its third consecutive arc
(B1404's `subs` on a rewritten radical, B1404's locale-dependent bracket
expression, and this). The class is no longer about floats in any sense; it is
about **testing a thing by how it is written.**

## 7. FENCES

- Bers' description of `QF(T₁)`, Minsky's classification, Thurston's character
  variety dimension and Menal-Ferrer–Porti's `SL(n)` count are **cited, not
  derived here**. The `k(n−1)` row of §3 is explicitly unverified.
- §3's "~19" is a **count of degrees of freedom**, not a comparison to any
  measured value; nothing in this arc reaches `CLAIMS.md`, F2 or Gate 5.
- `str(1) = 1/φ` is an exact fact about SU(3)₂ modular data at the object's
  word. **What it is an observable OF is not claimed.**
- The closed form of `m ↦ j` in `str(m) = 2cos(jπ/15)` is **observed, not
  derived** — registered as L215.
- B1349's mathematics, B1405's verdict, and B675/B996/B1402's laws are untouched.

Artifacts: `b1406_riddles.py` (26/26). Locks: `tests/test_b1406_riddles.py`.

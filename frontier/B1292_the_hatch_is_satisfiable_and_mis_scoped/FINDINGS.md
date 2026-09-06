# B1292 — B1291's hatch is SATISFIABLE (m202 is the witness) and MIS-SCOPED (it named the wrong obstruction)

**Verdict: PROVED** (the witness, every clause checked) **+ a self-correction that matters more than
the witness**: satisfying the hatch does **not** reach the target, because **parity was never the
binding obstruction — flatness is, and flatness is cusp-count-independent.**

## Half one — the hatch is satisfiable, and m202 is the witness

B1291 proved that on a **one-cusped** manifold `|Fix(g)|` on the cusp is **even**, so `|Fix| = 3` —
what an order-3 rotation of the cusp torus requires — is **excluded**. Its hatch said: *go
multi-cusped inside m004's commensurability class, keeping ℚ(√−3), 2T and E₆.* **Every clause
checks out on m202:**

| clause | m202 |
|---|---|
| **same commensurability class** | `vol = 4·V_tet = 2·vol(m004)` ⇒ tiled by regular ideal tetrahedra ⇒ cusped arithmetic over **ℚ(√−3)**; for *cusped* arithmetic manifolds the quaternion algebra is `M₂(k)`, so the invariant trace field alone fixes the class. Both cusp shapes are `e^{iπ/3}` — the **hexagonal/Eisenstein** shape, in ℚ(√−3). |
| **keeps 2T** | **96 surjections** `π₁(m202) ↠ SL(2,3)`. **Method control in the same run: m004 returns 72 homs / 48 surjections, reproducing the banked 48.** |
| **≥2 cusps** | **2** |
| **realises \|Fix\| = 3** | **4 isometries give \|Fix\| = 3 on *both* cusps at once**; `Sym = D₆`, order 12 |

**And the mechanism is the cusp shape, which explains the original obstruction rather than
sidestepping it.** m004's cusp is **rectangular** (`shape = 2√−3`, `Re = 0`), and a rectangular
torus admits only `±1` — *that* is why m004 can never carry an order-3 rotation. m202's cusps are
**hexagonal**, which admit **ℤ/6**. The obstruction was the **shape**, and the shape is what changes.

## Half two — and the hatch named the wrong obstruction

**This is the load-bearing half.** Satisfying the hatch does **not** produce a generation count:

```
m004        1 cusp     chi(M) = 1-2+1 = 0     chi(dM) = 1 x chi(T^2) = 0
m202        2 cusps    chi(M) = 1-2+1 = 0     chi(dM) = 2 x chi(T^2) = 0
o10_150704  4 cusps    chi(M) = 1-4+3 = 0     chi(dM) = 4 x chi(T^2) = 0
```

**χ(M) = 0 and χ(∂M) = 0 for every cusped manifold at any cusp count, because every boundary
component is a flat torus.** So `net chirality = −χ(∂⁺M) = 0` **survives the move**.

> **|Fix| = 3 and χ(∂⁺M) ≠ 0 are different quantities. m202 supplies only the first.**

**B1291's hatch is re-scoped at source** (its `kill_graph` hatch field and FINDINGS): it opens an
**order-3 structure on the boundary inside the right arithmetic**, which the programme did not
previously have anywhere — and it **does not** open a route to net chirality. Parity was a *real*
obstruction, but not the *binding* one; the binding one is **flatness**, which B1291 itself
identified and which no change of cusp count touches.

## What m202 is worth, stated exactly

**The first place in this programme's own arithmetic where an order-3 symmetry acts on the
boundary.** m004 — the object — cannot host one, by its cusp shape. m202 can, keeps ℚ(√−3), and
keeps 2T with twice as many surjections.

**That is a lead, not a result.** It is **not** a generation count; **I-26 is untouched and still
UNEARNED**; and nothing here claims m202 *is* the object — m004 is the object by the programme's own
axioms and its genesis theorem.

## Fences

1. **Commensurability is argued, not certified.** `vol ∈ ℤ·V_tet` plus cusp shapes in ℚ(√−3) is
   strong evidence of cusped-arithmetic-over-ℚ(√−3); the invariant trace field itself needs Sage,
   which is **not** this repo's canonical env. Recorded as **necessary conditions met**, not as a
   computed trace field. m202 is **not** a degree-2 or degree-3 cover of m004 (checked) — commensurable
   does not require one to cover the other.
2. **"Keeps E₆" is inferred from 2T via the McKay door, not recomputed here.** 2T is verified; the
   E₆ chain's transport to m202 is **unrun**.
3. **No identification is asserted** between `|Fix| = 3`, the 3 cusps of any manifold, or any other
   3, and a generation count.
4. **The self-correction is the deliverable.** A hatch that is satisfiable but aimed at a
   non-binding obstruction is worse than no hatch, because it reads as a route.

## Controls (MB12, both directions)

- The 2T counting method is **validated against a banked number in the same run** (m004 → 48); had it
  disagreed, the m202 count would be worthless.
- The rectangular/hexagonal distinction is **asserted as a computation** (`Re(shape) = 0` for m004,
  `shape = e^{iπ/3}` for m202), not narrated.
- The scope correction is checked on **three** manifolds at **1, 2 and 4** cusps, so
  "cusp-count-independent" is exhibited rather than claimed.

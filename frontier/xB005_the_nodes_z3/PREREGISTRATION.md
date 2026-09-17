# xB005 — PREREGISTRATION (sealed BEFORE any computation of this arc)

**Seat `xb`, `sep16-branch`, 2026-09-17. Written, hashed and committed before any cell runs; the
hash is in `ARTIFACT_HASHES.txt` in the same commit and the commit is pushed before any result
exists, so the order is checkable from this branch's history.**

## P0 — the quantifier

This computes on the character variety of the once-punctured torus at the **node** of the object's
leaf `κ = −2`. Nothing here is a physics claim. Gate 5 absolute.

## What is already closed, and why this is not it

The **ℤ/3-sameness question is CLOSED NEGATIVELY** in the record (chat1 closure handoff §4, verified
on main): *"the arithmetic ℤ/3 = 2T/Q₈ is the **CENTRE of E₆**, not the trinification grading."*
That pairing compared `2T/Q₈` with the **trinification grading inside E₆**.

**This arc asks a different pairing**, in a different category: the **monodromy's order-3 action at
the node of the Markov surface** against the **outer automorphism ℤ/3 of Q₈**. Neither side is the
trinification grading. If the two coincide, the closed negative is untouched — it says where
`2T/Q₈` lands *in E₆*, not how the monodromy acts on the character variety.

## Established before this arc (not re-derived)

* the object's leaf is `κ = −2`, the Markov surface (B1347);
* its node is `(0,0,0)`, where `dκ` vanishes — a singular point (xB004 follow-up);
* `(0,0,0)` is the **quaternion character**: `tr a = tr b = tr ab = 0` are `i, j, k` in `SU(2)` and
  `tr[i,j] = −2`;
* the monodromy's derivative there is `[[0,0,1],[−1,0,0],[0,−1,0]]`, eigenvalues `{1, ω, ω̄}`,
  **order exactly 3** (B123 banked the elliptic spectrum at the node);
* `2T = Q₈ ⋊ ℤ/3` with the ℤ/3 permuting `i, j, k`.

## The question

**Is the monodromy's order-3 action at the node the outer ℤ/3 of `Q₈` — that is, `2T/Q₈` realised
dynamically?**

## Cells and two-outcome criteria — declared before running

| cell | question | PASS | FAIL |
|---|---|---|---|
| **Q1** | does the monodromy fix the node and act there with order exactly 3? | fixed, `D³ = I`, `D ≠ I` | otherwise |
| **Q2** | is that action the **outer ℤ/3 of `Q₈`**? | the induced permutation of the Q₈ character's `(i,j,k)` is a 3-cycle (signs allowed, since the lifts are defined up to sign), **and** it is realised by an actual automorphism of `Q₈` | it is not a 3-cycle, or no automorphism of `Q₈` realises it — then the two ℤ/3's are different and the resemblance is DECLINED |
| **Q3** | the §2 linkage test on the programme's ℤ/3 family | each of `μ₃ ⊂ ℚ(√−3)`, `Z(E₆)`, `2T/Q₈`, the node's order-3 is classified as **canonically linked** to the others or **independent**, with the link named | — |

Q2 can fail on the instance: a signed 3-cycle that no `Q₈` automorphism induces would refute it.

## Declared prior, so the arc can overrule it

Q1 **PASS** (already computed). Q2 **PASS**, with moderate confidence. Q3: this seat expects
`μ₃`, `Z(E₆)` and `2T/Q₈` to be **canonically linked** (the field contains `ζ₃`; McKay ties `2T` to
`E₆`; `Z(E₆) = ℤ/3` is the root/weight quotient) and therefore **not** mutual evidence by §2's
standard — and expects the node's order-3 to be the one member that is **not** obviously linked.
**If Q3 shows all four linked, the correct verdict is that the whole ℤ/3 family is forced by the
ramification of 3 in `ℚ(√−3)` and carries no object-specific information** — the inconvenient
outcome, named here in advance.

## Conventions

Full traces `(X,Y,Z) = (tr a, tr b, tr ab)`; `κ = X²+Y²+Z²−XYZ−2`; monodromy trace map
`F_L ∘ F_R` (xB003); `ω = (−1+√−3)/2`; `Q₈ = {±1, ±i, ±j, ±k}` in `SU(2)`.

## Scope

Character-variety / group theory. No value, no generation count, no physics reading. Nothing
promotes to `CLAIMS.md`.

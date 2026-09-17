# xB007 — PREREGISTRATION (sealed BEFORE any computation of this arc)

**Seat `xb`, `sep16-branch`, 2026-09-17. Written, hashed and committed before any cell runs; the
hash is in `ARTIFACT_HASHES.txt` in the same commit and the commit is pushed before any result
exists, so the order is checkable from this branch's history.**

## P0 — the quantifier

Hyperbolic geometry and census computation. Nothing here is a physics claim, no value, no
generation count. Nothing promotes to `CLAIMS.md`. Gate 5 absolute.

## The diagnosis this arc tests

xB005 Addendum 1 found that the node's ℤ/3 is **not a commensurability invariant** (3 on m004, 1
on `s961`, m004's own 3-fold fibred cover), and observed that **every arithmetic handle the
programme uses — invariant trace field, arithmeticity, the quaternion algebra, the atom `ℚ(√−3)` —
IS a commensurability-class invariant.** The proposed reading was a *type* diagnosis:

> the record's open *"which member of the class?"* questions (I-6's *which 2T*, xB002's
> `SCOPE_NOTE_L1` — *"the genesis selects a family; knot-ness selects the member"* — and L54) may be
> stuck not for want of cleverness but because **the tools are the wrong type**: a class invariant
> can never point at a member.

That was recorded as a **lead priced at 0.58 bits and nothing more.** This arc tests it, and tests
whether the new handle — or any non-class-invariant — actually delivers selection.

## Established before this arc (not re-derived)

* **Maclachlan–Reid** (cited): a cusped finite-volume hyperbolic 3-manifold with invariant trace
  field `ℚ(√−3)` is arithmetic and **commensurable with the Bianchi orbifold `H³/PSL(2,O₃)`** —
  so invariant trace field `ℚ(√−3)` **is** the commensurability class here;
* **Cao–Meyerhoff** (cited): **m003 and m004 are exactly the two minimum-volume orientable cusped
  hyperbolic 3-manifolds**, both at `2.0298832128…`;
* **Reid** (cited): the figure-eight is the **unique arithmetic knot** — a selector that takes
  *knot-ness* as its input;
* xB002's `SCOPE_NOTE_L1`, verified: m004 **does not win volume minimality** — it ties m003 — and
  arithmeticity **cannot discriminate between members at all**;
* B1136: on the shape-field family the separator set is exactly `['h1_is_Z']`;
* xB005 Addendum 1: the node order is the monodromy's image in `S₄` at the quaternion character.

## The question

**Does any invariant that is NOT a commensurability invariant select m004 inside its
commensurability class — and in particular, does anything intrinsic break the m003/m004 tie
without taking knot-ness as an input?**

## Cells and two-outcome criteria — declared before running

| cell | question | outcome A | outcome B |
|---|---|---|---|
| **T1** | build the population: census cusped manifolds whose shape field (= invariant trace field, Neumann–Reid) is `ℚ(√−3)`, hence commensurable with m004 | a population of size ≥ 5, with the **independent check** that every volume is an integer multiple of the Bianchi orbifold volume `v₀ = vol(H³/PGL(2,O₃))` — a necessary consequence of commensurability, so a failure **voids T1** | the check fails: report the tooling defect and stop, claiming nothing |
| **T2** | the **class-invariant** battery on the population | **zero** separation power, verified by every member taking the same value — the control that the diagnosis is about *type*, not about weak tools | any class invariant separating: the cited theorem is misapplied and the arc says so |
| **T3** | the **non-class-invariant** battery (volume, `H₁`, cusps, fibredness, node order, symmetry-group order, torsion) — which separate m004 from the rest, as a separator table | the separator set, computed | — |
| **T4** | **the decisive cell.** Volume-minimality gives the tie `{m003, m004}` (verified against Cao–Meyerhoff). **Does anything in T3's battery break it — and does the node's ℤ/3?** | some non-class-invariant **other than `H₁`** breaks the tie: the handle (or another) **delivers selection**, and the lead is upgraded | **only `H₁ = ℤ` (knot-ness) breaks it**: the handle does **NOT** deliver selection, the lead is **priced down to a diagnosis only**, and B1136's separator is confirmed at the commensurability level |
| **T5** | price the result honestly, whichever way T4 goes | if A: how much, in bits, against the population | if B: state plainly that this seat's own lead failed its first test |

## Declared prior, so the arc can overrule it

This seat expects **OUTCOME B**: that `H₁ = ℤ` remains the only separator and **the node's ℤ/3
fails to break the m003/m004 tie.** Two reasons, stated in advance so they can be checked: the node
order is a *congruence* condition (the monodromy mod the level-4 quotient `S₄`), and congruence
data is coarse — it takes only the values {1,2,3,4}, so it cannot isolate one manifold among many;
and m003 and m004 are so close (same volume, same tetrahedron count, same field) that a coarse
invariant is unlikely to separate them.

**The inconvenient outcome is the one this seat expects, and it is inconvenient for this seat's own
proposal:** if T4 returns B, then **the handle xB005 Addendum 1 flagged does not do the job it was
flagged for**, and the honest report is that the lead failed its first test — priced down to a
*diagnosis of why the questions are stuck*, which is worth keeping, and **not** a selector, which
is what would have been worth something. This arc will say that in its headline, not a footnote.

**A further named risk (E33, over-correction):** if T4 returns A, this seat must check that the
separating invariant is not smuggling knot-ness in — e.g. an invariant that is a function of `H₁`.
Any A outcome must survive that control or it is not an A.

## Scope and standing limits

* Census computation over SnapPy's cusped orientable census at this head, with the population's
  size and cutoff **reported**, not hidden. A manifold outside the census cutoff is outside this
  arc's claim.
* **Recall is bounded and will be stated**: the commensurability class is infinite; the population
  is a finite census sample of it.
* No arc is re-verdicted. `creates_law` false. Nothing reaches `CLAIMS.md`, F2 or Gate 5.

## Conventions

Shape field = invariant trace field (Neumann–Reid), computed from `ManifoldHP` shapes with a
height-bounded, residual-checked quadratic fit (the E25 guard). `v₀ = vol(H³/PGL(2,O₃))`, the
minimal cusped orbifold volume in the class. "Selects" = takes a value on m004 that no other
population member takes.

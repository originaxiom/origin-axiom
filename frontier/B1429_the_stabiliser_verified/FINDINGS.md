# B1429 — THE STABILISER RESULT VERIFIED, AND SHARPENED: the two bits are not merely invisible AT the object, they are invisible on its whole sister orbit — and the family is where they become visible

cc, 2026-09-18. Taking a relayed arc seriously rather than auditing it. `xB021` (seat `xb`, `sep16-branch`,
verdict PROVED, preregistration sealed and pushed before its `verification/` existed) argues that the walls this
programme keeps hitting are **the shape of the stabiliser seen from inside a fixed point**, and that the mechanism
is to *move to the orbit*. Its load-bearing facts are re-derived here.
**Verdict: PROVED. The geometry checks exactly. The orbit–stabiliser decomposition is right. One normalisation in
the ladder needs restating, and the conclusion comes out STRONGER than the arc claims — which also means the
arc's own proposed mechanism does not do what it hopes on the orbit it names.**

## 1. THE GEOMETRY, RE-DERIVED ON THIS BENCH

| quantity | computed here |
|---|---|
| CS(m004) | **0** (to 1e−16) |
| CS(m003), the sibling | **exactly 1/4** |
| CS of m004's mirror | 0 |
| CS of m003's mirror | 1/4 |

So the orbit `{0, 1/4}` **is** `{CS(object), CS(sibling)}`, as relayed. Confirmed, not accepted.

## 2. THE ORBIT–STABILISER DECOMPOSITION IS CORRECT

With the three actions on `CS ∈ ℝ/(1/2)ℤ` that the arc establishes — the knot-ness bit by `x ↦ x + 1/4`, the
order bit and the orientation bit both by `x ↦ −x` — the group is `ℤ/2 × ℤ/2` of order 4: `x ↦ x + 1/4` has order
2 because `2·(1/4) = 1/2 ≡ 0`, and the two commute because `−(−x + 1/4) = x − 1/4 ≡ x + 1/4`. The stabiliser of 0
is order 2, the orbit is `{0, 1/4}`, and `4 = 2 × 2`. **Arithmetic confirmed.**

## 3. THE SHARPENING, AND IT CUTS BOTH WAYS

On `ℝ/(1/2)ℤ` the map `x ↦ −x` has fixed points exactly where `2x ≡ 0`, i.e. **exactly `{0, 1/4}`** — computed,
and that set **is the sister orbit**. So the orientation and order bits do not merely stabilise the object's value:

> **They act trivially on the ENTIRE sister orbit. They are the kernel of the action, not a point stabiliser.**

This is stronger than *"a fixed point cannot report on its own stabiliser"* — and it is worse news for the arc's
own mechanism. **Moving from the object to its sibling does not recover the two bits**, because Chern–Simons mod
a half cannot see them at either point. The arc's `1 → 2` step buys nothing for these two bits specifically.

## 4. WHERE THEY DO BECOME VISIBLE — the family, measured

The 112-member family (`B1186`'s `members_B`), every member's CS computed here:

- **104 of 112** have `CS` a multiple of `1/12`.
- As **classes** those hit `{0, 1, 2, 3, 4, 5}` ⊂ ℤ/6 — **surjective onto the full group of twelfths mod 1/2**,
  with counts `{0: 47, 1: 5, 2: 11, 3: 29, 4: 7, 5: 5}`.
- **Control:** of 600 one-cusped census manifolds outside the family, **2** have CS in twelfths — **0.33 %**.
  Both land on `{0, 3}`, the fixed classes. The family is not a generic sample.
- The bit acts as `r ↦ −r` on ℤ/6, fixing exactly `{0, 3}` — **which are precisely the object and its sibling**.
  **4 of the 6 classes the family realises are moved.**

> **So the ladder is real and the direction is now specific: the sister orbit is exactly the fixed-point set,
> and the information the two bits carry appears only on the wider family, on four of its six classes.**

## 5. THE NORMALISATION THAT NEEDS RESTATING

The arc's ladder reads **1 → 2 → 12**. For a *cusped* manifold the Chern–Simons invariant is defined **modulo
1/2**, so values in twelfths live in `(1/12)ℤ / (1/2)ℤ ≅ **ℤ/6**, not ℤ/12. Read as bare representatives mod 12
the family hits 7 of 12, which looks like a failure of surjectivity; read as classes it hits **6 of 6**, which is
surjective. **The substance of the claim survives intact and is if anything cleaner — the group is ℤ/6 and the
family covers it — but "surjective onto ℤ/12" should be "surjective onto ℤ/6, the twelfths mod a half".**
Recorded as a restatement, not a refutation: nothing the arc concludes depends on which of the two is written.

## 6. WHAT THIS DOES NOT DO

It derives no value. The arc's own declared limit stands and is not softened: an index is not a value, and the
orbit's content here is a class in a finite group. What changes is the **direction**: work on the family, not on
the sibling, if the target is the two bits.

## Locks
`tests/test_b1429_stabiliser.py`: the two Chern–Simons values and their mirrors; the fixed-point set of `x ↦ −x`
on ℝ/(1/2)ℤ being exactly the sister orbit; the family's surjectivity onto ℤ/6 with the census base rate as
control.

# B1428 — THE 3D INDEX OF THE OBJECT, COMPUTED: it is non-trivial, it matches the published series exactly, and it does not separate the object from its sibling

cc, 2026-09-18. Relayed: *"there is a well-defined index on cusped 3-manifolds… This is a different index on the
same objects, and it is not trivial."* True, and the record's own outside bench had already conceded the gap in
those words — *"the 3d index of `T[m004]` was **NOT computed**."* It is computed here.
**Verdict: PROVED. The series is non-trivial, every published coefficient reproduces, and the object and its
sibling m003 carry the SAME series — so the one invariant the relay offers as live is blind at exactly the place
this programme keeps returning to.**

## 1. WHAT WAS BUILT

The tetrahedron index of Dimofte–Gaiotto–Gukov, then the gluing, from scratch in exact integer arithmetic on
`q^{1/2}` — no floats, no computer algebra. SnapPy supplies **only** the triangulation's gluing-equation rows.

**Convention matters and is stated:** two are in circulation and they are the same function with its arguments
transposed. Garoufalidis (arXiv:1208.1663 eq. 1.2) is used here, because every published gluing formula does.

```
I_Delta(0,0) = 1 - q - 2q^2 - 2q^3 - 2q^4 + 0q^5 + q^6 + 5q^7 + 7q^8 + 11q^9 + 13q^10 + 16q^11
```

## 2. THE OBJECT'S INDEX

```
I_m004(0,0)(q) = 1 - 2q - 3q^2 + 2q^3 + 8q^4 + 18q^5 + 18q^6 + 14q^7 - 12q^8 - 52q^9
               - 106q^10 - 164q^11 - 209q^12 - 212q^13 - 141q^14 + 14q^15 + 309q^16 + ...      (to q^35)
```

**Emphatically not 1.** Cross-checked against Garoufalidis–Hodgson–Hoffman–Rubinstein, *The 3D-index and normal
surfaces*, Illinois J. Math. **60** (2016) 289–352, pp. 297–298: **every published coefficient matches**, and the
series is carried 25 orders further here. All **eight** published boundary classes of m004 reproduce exactly,
including the half-integer-power ones. A second manifold, m009, reproduces GHRS §11.5 exactly.

## 3. THE FINDING THE RELAY DOES NOT CONTAIN: THE INDEX IS BLIND TO THE SIBLING

| manifold | volume | H₁ | I(0,0) |
|---|---|---|---|
| **m004** | 2.0298832 | ℤ | 1 − 2q − 3q² + 2q³ + 8q⁴ + 18q⁵ + … |
| **m003** | 2.0298832 | **ℤ/5 ⊕ ℤ** | **identical, term for term** |

Two manifolds with **different first homology** carry the **same** index. Not a numerical coincidence: it follows
term by term from the threefold symmetry applied twice (`q^k I(−k,2k)² = I(−k,−k)²`, then `k → −k`). Across twelve
census manifolds the index takes **7 distinct values on 12 manifolds**, grouping exactly by volume — m006/m007,
m015/m016/m017 and m022/m023 each collapse, again across different H₁.

**Why this matters here and not in general.** A topological invariant is not obliged to be complete. But m003 is
**the object's sibling**, the other manifold of minimal volume, and it is the pair this programme returns to: the
Chern–Simons orbit computed on the review lane is `{0, ¼} = {CS(m004), CS(m003)}`, and the object's chirality is
the distinction between them. **The relay's "different index, and it is not trivial" is true; the index is
nevertheless silent on the one distinction the programme needs it for** — at least on the `(0,0)` class.

**Scope, stated rather than hidden:** the full 3D index is a *collection* over boundary classes. What is shown
identical here is the `(0,0)` class. Whether some other class separates m003 from m004 is **open and computable**,
and is the obvious next arc. Nothing above says the full collection is blind.

## 4. A BUG FOUND IN THE BUILDING, AND WHY IT IS RECORDED

The first implementation truncated every factor of the product at the same order. The gluing factors can have
**negative** minimal degree, so when one starts at `x^{−20}` and another at `x^{+20}`, uniform truncation silently
drops terms. Symptom: the answer depended on **which edge weight was set to zero** — wrong for m006, m007, m009,
m015, m022, and *right for m004 by luck*, which is why it matched the literature anyway. Fixed by factoring out the
exact minimal degree and budgeting per factor. After the fix: edge-choice independence on 12/12 manifolds, cyclic
order independence, and **30/30 random retriangulations agree** for m004, m009, m015.

**This is the session's own error class seen once more:** the check that would have caught it — does the answer
depend on an arbitrary choice? — passed on the one manifold that was being watched.

## 5. CONTROLS

Verified with zero failures: the exact degree lemma (0/172), no negative powers of q (0/117), half-integer powers
exactly when `me` is odd, both defining recursions, the pentagon identity through `q^12` and the full pentagon at
five parameter sets, three published tetrahedron-index values. Symmetries **tested rather than assumed**: `I(m,e) =
I(e,m)` is **false**, `I(m,e) = I(−m,−e)` is **false**, bare triality is **false**; `I(m,e) = I(−e,−m)` holds, and
the real threefold symmetry holds only with its prefactor (0/169 failures). Vacuity: m015 gives a clearly different
series, so the pipeline is not returning a constant.

## 6. WHAT WAS NOT DONE

No direct 1-efficiency test (no Regina on this bench); the summation region was verified bounded with a wide margin
instead. Peripheral classes were computed from the published formula for m004 only, not from SnapPy's cusp rows for
the other manifolds.

## Locks
`tests/test_b1428_three_d_index.py`: the published m004 coefficients, the tetrahedron index's published values, the
symmetries that hold and the ones that do not, the m003 = m004 collapse with m015 as the separating control.

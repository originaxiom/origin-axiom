# B1431 — THE 3D INDEX DOES SEPARATE THE OBJECT FROM ITS SIBLING, and B1428's headline was the (0,0) class mistaken for the invariant

cc, 2026-09-18. B1428, banked this morning, found the object and m003 carrying the **same** index and scoped it
honestly — *"what is shown identical here is the `(0,0)` class; whether some other class separates them is open and
computable, and is the obvious next arc."* That arc is run here rather than deferred.
**Verdict: PROVED. The index DOES separate them. Two explicit witnesses, in both directions, and a structure
theorem that explains exactly why the collapse looked total.**

## 1. THE ANSWER, WITH WITNESSES

The 3D index is not one series but a **collection** indexed by boundary classes. Compared as collections:

- **m004's own published meridian series** — `−2q − 2q² + 2q³ + 8q⁴ + 16q⁵ + 16q⁶ + 10q⁷ − 14q⁸ − 52q⁹ − …` —
  occurs at **no class of** `H₁(∂m003; ℤ)`.
- **m003's longitude series** — `−q − q² + 2q³ + 7q⁴ + 11q⁵ + 11q⁶ + 3q⁷ − 17q⁸ − 49q⁹ − …` — occurs at **no class
  of** `H₁(∂m004; ℤ)`.

Both differ from every competitor already at **q¹**. Among classes of minimal degree ≤ 8: **20** classes of m004
(6 distinct series) are absent from m003, and **16** of m003 (4 distinct) are absent from m004.

**Exhaustive, not sampled.** Leading degree is bounded below by an exact per-term bound, and `{γ : minD(γ) ≤ 8}`
is finite and fully enumerated over `|x|,|y| ≤ 40` (farthest member at 16; rim minima at radius 20, 30, 40, 60, 80
are 10, 44, 20, 30, 40 — all above 8). Independently, brute force over **841 integer classes each** finds neither
series anywhere.

## 2. WHY THE COLLAPSE LOOKED TOTAL — a structure theorem, proved not observed

There is an **exact identity of the two state sums**. Relabelling m003's slots maps its data onto m004's with

```
A : (x, y)_m003  |-->  (X, Y)_m004 = (-(2x + y), -y/2),      det A = 1,  no edge-row correction
```

so `I_m003(γ) = I_m004(Aγ)` for **every** γ — confirmed on 169 of 169 classes to `q³⁰`. **But `A` does not carry
`H₁(∂m003; ℤ)` onto `H₁(∂m004; ℤ)`.** It identifies the *saturated* lattices, each of index 2 over its `H₁`, and
the two `H₁`s land on **different index-2 sublattices**:

| | |
|---|---|
| **y even** | `I_m003(x,y) = I_m004(−(2x+y), −y/2)` — an honest topological identity, 91/91 verified. **This half contains `(0,0)`, which is why B1428's collapse is real.** |
| **y odd** | m003's honest classes equal m004's **half**-classes (λ/2), which are **not** boundary classes of m004. **That is the separation.** |

So B1428 was not wrong; it measured the half of the lattice where the identity holds and reported it as the
invariant. **The correction is one of emphasis, and it matters:** the object *is* distinguished from its sibling by
this invariant, and the cleanest witness is m004's own published meridian series.

## 3. THE INSTRUMENT IS STRICTLY SHARPER THAN THE `(0,0)` CLASS

B1428 found twelve census manifolds falling into seven groups by `(0,0)`, grouping by volume. The class collection
**separates four of those collapsed pairs** — m006/m007, m015/m016, m015/m017, m016/m017 — which have *identical*
`(0,0)` series. So the collection is not merely different from the single class; it is finer, and the
volume-grouping B1428 reported is an artefact of looking at one class.

## 4. THE BASIS CAVEAT, WHICH IS WHERE A FALSE RESULT WOULD LIVE

The comparison is made on the **sets** `{I_M(γ) : γ ∈ H₁(∂M; ℤ)}`, so **no basis enters** and no basis choice can
create or destroy the separation. Three further guards:

- **The indexing is validated against geometry.** SnapPy's symmetry groups act on the cusp as `(x,y) ↦ (±x,±y)`
  for m004 and by the shear `(x,y) ↦ (x+y, −y)` for m003. The index collections are invariant under **exactly**
  those, 49 classes each. A wrong cusp-row convention would not reproduce m003's non-obvious shear.
- **The canonical marking does not separate**: m003's homological longitude is `μ − 2λ`, and both manifolds give
  `q³ + 2q⁴ + 5q⁵ + 2q⁶ − 3q⁷ − 16q⁸ …` there. The separation is not an artefact of a marked curve.
- **The false-positive trap is exhibited rather than avoided silently.** In raw bases, m004 at `3μ+3λ` is 0 through
  `q³⁰` while m003 is `−q⁹ − 2q¹⁰ − …`; that is pure basis artefact, and the zero is only "leading term beyond the
  window". Every class in the scan carries its minimal degree so it cannot be misread.

The gluing rule was **derived from SnapPy's own cusp rows, not assumed**: fitting the published hand-written m004
formula against those rows gives `v(γ) = −(cusp row)` exactly, the longitude discrepancy being an edge-row
combination whose two shifts cancel. Validation: **all eight published m004 classes reproduce from SnapPy rows
alone**, half-integer ones included.

## 5. CONTROLS, BOTH DIRECTIONS

**Must separate:** m004 against m015 and against m006 differ at `(0,0)` with no `GL₂(ℤ)` match.
**Must not depend on choices:** which edge weight is zeroed agrees on 6 non-trivial classes for both manifolds;
cyclic slot order agrees; 8 random retriangulations × 4 classes = **32/32** for each manifold, and **12/12** on
each separating class.

**One real triangulation-dependence found and recorded:** the *saturated* lattice can shrink under retriangulation
(randomised m003 loses its half-classes), so the half-class extension is a triangulation-level quantity. **The
result above rests only on honest `H₁` classes** and is unaffected.

## 6. WHAT THIS DOES AND DOES NOT MEAN

It means the invariant this literature supplies **can see** the distinction between the object and its sibling —
the pair whose Chern–Simons values are 0 and ¼. It does **not** mean it sees chirality, supplies a value, or
bridges to physics; those fences are unchanged. **Not done:** direct 1-efficiency test, for want of Regina — the
same caveat B1428 carries.

## Locks
`tests/test_b1431_index_separates.py`: the two witness series and their absence from the other manifold, the
structure theorem's 169/169 agreement, the four census pairs the collection separates but `(0,0)` does not, and
the retriangulation controls.

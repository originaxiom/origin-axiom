# xB027 — THE GENERATION COUNT IS STABILISER-FIXED: one is the invariant, the backgrounds are the orbit

**Date:** 2026-09-18 · **Seat:** `xb` · **Branch:** `sep16-branch` · **Verdict: NEGATIVE**
(a theorem-shaped negative — the headline is that a candidate mechanism is shown not to produce three)

**PREREGISTRATION sealed `21f5b2fac12bb5d2…`, committed and pushed at `61331ec3` BEFORE
`verification/` existed**, with **C1 as a binding control** and a **binding kill condition** on any
`|count| ≠ 1`.

---

## THE RESULT

xB026 showed **A5 moves the census's inputs at 6 of 6 levels** and named the bounded next step. This
arc ran it, with the SM-derivation lane's own machinery **borrowed with provenance**.

| level | the object's tower `b++(LR)ⁿ` | its A5 image `b+-(LR)ⁿ` |
|---|---|---|
| **Y₂** | `ℤ⊕ℤ/5`, N 60, 9 loci, 16 firing → **0 backgrounds** | `ℤ⊕(ℤ/3)²`, N 12, 17 loci, 64 firing → **0 backgrounds** |
| **Y₃** | `ℤ⊕(ℤ/4)²`, N 12, 31 loci, 0 firing → **0** | `ℤ⊕ℤ/2⊕ℤ/10`, N 60, 39 loci, 64 firing → **0** |
| **Y₄** | `ℤ⊕ℤ/3⊕ℤ/15`, N 60, 89 loci, 976 firing → **12 800 on 64 loci** | `ℤ⊕(ℤ/7)²`, N 84, 97 loci, 1344 firing → **384 on 96 loci** |

**Both sealed predictions hold, and the kill condition did NOT fire:**

1. **The NUMBER of generation-shaped backgrounds differs** — **384 against 12 800** — as xB026's
   moved loci, moved `H₁` and moved `N` required.
2. **The COUNT is exactly one on both towers.** `|count| {1: 384}` against `|count| {1: 12800}`.
   **Never two. Never three.** Signs split evenly on both (192/192 against 6400/6400);
   `ν^c = 0` on all 384, as on t12839.

> **THE GENERATION COUNT IS STABILISER-FIXED.** It belongs with **volume and the trace field**, not
> with `CS` and `H₁`. **A5 moves the backgrounds; it does not move the count.**
> **One is the invariant. The backgrounds are the orbit.**

**And the mechanism transfers.** `h¹(χ²) = 1` at **every** locus on **every** level of the sister's
tower too — 17, 39, 97 of 17, 39, 97. That is precisely what bounds `|I| ≤ 1`, and it is not
special to m004. The count cannot exceed one on either tower for a structural reason, not a
numerical accident.

**What this turns into.** *"Three generations is not derivable from this object"* stops being a
vague absence and becomes **theorem-shaped on this mechanism**: the count is **one across the A5
orbit**, and the reason is a rank bound that holds at every locus of both towers.

---

## C1 — THE BINDING CONTROL, PASSED EXACTLY

No sister number was reportable until the adapted driver reproduced B1375's **published** output on
the object's own tower. It did, on **all three levels**:

| level | `N` | primes | `|Hom|` | loci | spurious | firing | backgrounds |
|---|---|---|---|---|---|---|---|
| Y₂ | 60 | 421, 541, 601 | 300 | 9 | [0,0,0] | 16 | **0** |
| Y₃ | 12 | 409, 421, 433 | 192 | 31 | [0,0,0] | 0 | **0** |
| Y₄ | 60 | 421, 541, 601 | 2700 | 89 | [0,0,0] | 976 | **12 800 on 64 loci, signs {−1: 6400, 1: 6400}, |count| {1: 12800}** |

Every field matches B1375's `tower_generations_run.txt` to the digit.

**ONE DIFFERENCE, NOTED RATHER THAN PAPERED OVER.** The cusp exponent pairs read `(0,30)` where
B1375 reads `(30,0)`, and `mu null-homologous` flips. **That is a meridian/longitude relabelling**
between the bundle presentation and the cover presentation. **It cannot affect the census**, because
T5 requires its condition on **both** peripheral curves and is therefore invariant under the swap —
which is exactly consistent with every downstream number matching.

## WHAT WAS BORROWED, AND THE MATHEMATICS THAT NEARLY WENT WRONG

`index_lib.py` copied **byte-identical** (confirmed by `diff`) from the SM-derivation lane
(`<remote>/standard-model-derivation-0qt6ao` at `23532539`, seat `cc`), under a provenance header.
`tower_generations.py` adapted at **exactly two lines**, documented in its own header.
**The algorithm — characters, T5, the index, the generation search, the multi-prime re-check — is
seat `cc`'s and is not this seat's work.**

**The one thing that needed care was not the code.** The published driver builds
`m004.covers(n, cyclic)[0]`. Pointing that at `m003` would have **silently censused the wrong
manifolds**: `m004` has `H₁ = ℤ`, so its cyclic cover is unique and *is* `b++(LR)ⁿ`; `m003` has
`ℤ⊕ℤ/5`, its degree-2 cyclic cover has `H₁ = ℤ⊕ℤ/5` where the bundle has `ℤ⊕(ℤ/3)²`, **and at
degree 5 there are six of them**, tripping the original's `assert len(M) == 1`. The driver is
therefore pointed at the **bundle name** directly, and the control proves the substitution is exact
on the side where the answer is already published.

## WHAT THIS DOES NOT DO

It claims **no** generation count for physics and promotes nothing — **it inherits B1374/B1375's own
fence verbatim**: *main's index on a **non-semisimple** background, no physics reading, no value.*
B1413's R27 makes that fence a **theorem**: the index is a theorem-zero on the geometric
finite-twist class, so every one of these firings lives outside it by necessity. It does not
re-derive the SM frame — it **uses** the lane's. **It supplies no value.**

**Axes held fixed and named:** levels 2–4 on both towers (5 and 6 not run here) · the lane's frame,
borrowed not re-derived · `b+-(LR)ⁿ` is the **bundle**, not `m003.covers(n)`, and the arc says why.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**

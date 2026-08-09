# S1-a — THE CLASS-S DICTIONARY: the trace field falls out of the fixed-point equation

cc3, 2026-08-09, under the owner's suspended-disbelief brief. Gate 5-Q; structure
only, no measured quantity.

## The dictionary entry under test

B277 banks a canonical class-S lift: 6d (2,0) on Σ₁,₁ → 4d N=2\* SU(2), with the
object's monodromy **φ = RL an S-duality element**. In class-S language the
**Betti moduli space** of Σ₁,₁ is the SL(2,ℂ) character variety of the
once-punctured torus — the **Fricke cubic**

```
        x² + y² + z² − xyz − 2  =  tr[a,b]  =  κ
```

with x = tr(a), y = tr(b), z = tr(ab). **That surface is exactly what B13–B51
built** — the trace map, i.e. the character-variety face cc admitted yesterday as
the twelfth. The mapping class group SL(2,ℤ) acts on it; the object's monodromy
is one element of that action.

So the entry to test is:

> the object's own character variety **=** the **fixed points** of the monodromy
> acting on the class-S Betti moduli space, at the **parabolic** puncture

**Why κ = −2 is the right locus, and what it means on the physics side.** The
fiber's boundary is the cusp, and a cusp element is parabolic, trace ±2. On the
class-S side the puncture mass is the log of the boundary holonomy eigenvalue,
so parabolic is **m = 0** — the point where N=2\* becomes **N=4**. And N=4 SU(2)
is precisely the theory whose S-duality group is SL(2,ℤ), which is what B277
needs for RL to *be* an S-duality element. **The complete hyperbolic structure
and the massless point are the same locus.**

**Prediction, stated in the script before computing:** if the dictionary holds,
the fixed-point equation must return **ℚ(√−3)** — with no input from hyperbolic
geometry anywhere. Only F₂ traces, the Fricke relation, and the mapping-class
action.

## The computation

Generators, derived from the F₂ action rather than quoted:

```
   R : a → a, b → ab    ⟹   (x, y, z) → (x, z, xz − y)
   L : a → ab, b → b    ⟹   (x, y, z) → (z, y, yz − x)
```

**κ is verified invariant under both** — the puncture mass is a modulus, not a
coordinate, exactly as class-S requires.

Solving `word(x,y,z) = (x,y,z)` together with `κ = −2`, for both composition
orders:

| fixed point | minimal polynomial of x | disc | N(x) |
|---|---|---|---|
| (0, 0, 0) | `t` | — | the finite/quaternionic character, not geometric |
| **(3±√−3)/2** | **t² − 3t + 3** | **−3** | **3** |

## The result

**The trace field ℚ(√−3) is not an input. It is the discriminant of the
fixed-point equation of the monodromy on the class-S Betti moduli space at the
massless point.**

And two further things fall out of the same two-line polynomial:

- **N(x) = 3** — the **ramified prime**, which is the prime the entire chain to
  2T runs through (reduction mod 3 gives SL(2,𝔽₃) = 2T). So the route
  *m004 → ℚ(√−3) → 2T → E₆* now begins one step earlier than the ledger records
  it: at `t² − 3t + 3`.
- **x = (3+√−3)/2 is the same trace used in S3-a**, whose translation length
  `ℓ = 2 log|λ|` reproduced the banked systole to 9.0e−16. So the geometric
  fixed point of this equation *is* the shortest closed geodesic — the first
  tick of the observer's clock.

## What this does and does not establish

**Does.** The Betti half of the dictionary is verified, not assumed. The
programme's twelfth face (the character variety) **is** the class-S Betti moduli
space; κ is the puncture mass; the complete structure is the massless point;
and the object's trace field, its ramified prime, and its systole all descend
from one fixed-point equation on that space.

**Does not.** This is **not** a derivation of the Seiberg–Witten curve, and the
A-polynomial comparison proposed in the path document is **not** performed here.
Non-abelian Hodge relates the Betti moduli space to the Hitchin/Higgs moduli
space where the SW geometry lives; that correspondence is standard but is a
*different* computation, and the E₆-type compactification is untouched. **The
6d type J remains a free input.**

**Also not claimed:** that any of the underlying mathematics is new. The Fricke
cubic, the SL(2,ℤ) action, and Gaiotto's Σ₁,₁ → N=2\* are all standard. What is
new *to this programme* is that its own trace map and its own trace field sit at
a named place in that dictionary, and that the parabolic locus it has always
called "the complete structure" is the locus physics calls "massless".

Reproduce: `python3 fricke_fixed_point.py` (asserts disc = −3).

# B866 — VERIFIED: the three distinguished charge lines exist. The object's charge plane carries an S₃ cubic whose roots enhance the centralizer 30 → 46

cc banking seat, 2026-08-03. Verification of the solo seat's charge-measurement theorem on this
seat's **fully independent** B854 build. Mathematics scope; nothing to `CLAIMS.md`; Gate 5
untouched.

## 1. What was claimed (solo seat, same day)

The 2T-centralizer torus C = ⟨x₈, x₁₄, x₁₆, x₂₂⟩ stratifies e₆ by charge measurement: generic
charge → centralizer 12; the (8,16)-plane → 30 (block C of dim 18 killed); and **exactly three
distinguished lines** in that plane — roots of an irreducible cubic with S₃ Galois group — where
the centralizer **enhances to 46 = so(10) ⊕ u(1)**, coset 32 = 16 ⊕ 16̄. Three ways to measure
into SO(10); an unordered Galois triple; a candidate signature for **three generations**.

## 2. What this seat verified EXACTLY, on its own build

| claim | this build | verdict |
|---|---|---|
| common kernel (full-torus centralizer) = 12 | **12** exact | ✓ |
| nullity(ad x₈) = 30 (kernel + block C) | **30** exact | ✓ |
| nullity(ad x₁₆) = 30 | **30** exact | ✓ |
| nullity(ad x₁₄), (ad x₂₂) = 12 (act on block C) | **12, 12** exact | ✓ |
| generic (8,16)-pencil nullity 30 | **30** at six exact rational t | ✓ |
| **the three enhancement lines** | **det(48×48 minor)(t) = c·(500716339200t³ − 159667200t² − 28224t + 1)¹⁶** — exact interpolation from 50 rational points | ✓ |
| the cubic is THEIR μ | **theirs(13t) − 2197·mine(t) = 0** identically — same polynomial, their ρ = 13t | ✓ |
| multiplicity = the jump | **16** = 46 − 30 | ✓ |
| irreducible, Galois S₃ | irreducible over ℚ; disc = 2³²·3¹⁰·5²·7³·11·13⁶, **non-square** (7³·11) | ✓ |
| three real roots | −1.4908×10⁻⁴, 3.0632×10⁻⁵, 4.3733×10⁻⁴ (this normalization) | ✓ |

**Two independent constructions of E₆ and of the invariants; one cubic.** The det-polynomial
method (a generically-nonsingular 48×48 minor of the pencil ad(x₈ + t·x₁₆), determinant
interpolated exactly from 50 rational points, then factored) is this seat's own instrument — no
step shared with the solo seat's pencil-division route.


## 2a. ADDENDUM (same day) — the TYPE check, now on this seat's own leg: so(10) ⊕ u(1) CONFIRMED

At the middle root (refined to 55 digits from the exact cubic), the pencil's kernel and its
bracket structure, computed with this seat's exact structure tensor (2208 entries):

| quantity | value | so(10)⊕u(1) | B₄⊕B₂ |
|---|---|---|---|
| kernel dim | **46** (spectral gap 1.07×10⁸ vs 2.29×10⁻⁷ relative — 15 orders) | 46 | 46 |
| **derived algebra dim** | **45** | **45** ✓ | 46 ✗ |
| **center dim** | **1** | **1** ✓ | 0 ✗ |

Both discriminators land on so(10)⊕u(1), and **dim 45 is the dimension of a unique simple
algebra — D₅ = so(10)**. The type now stands on two independent legs: the solo seat's
derived-dimension-at-two-primes, and this seat's kernel-plus-structure-tensor computation at a
refined root. **The §4 conditional unwinds: the cascade's step 1 is the object's own** — 
SO(10)×U(1) as the centralizer of any of three Galois-conjugate distinguished charges — and the
step-1 max-dim ranking retires. The generations reading remains a signature.

## 3. NOT verified here — the honest boundary

- ~~The TYPE so(10) ⊕ u(1)~~ — **now confirmed on this seat's own leg (§2a)**: derived dim 45,
  center dim 1, at a 55-digit root with a 15-order spectral gap.
- **The coset structure 32 = 16 ⊕ 16̄** — theirs.
- **The generations reading is a SIGNATURE, not a mechanism** — their own wording, kept: an
  unordered S₃ triple of first-breaking charges, each birthing one 16-pair, is structurally what a
  generation mechanism would look like *in this framework*; nothing about it is yet a derivation
  of three families.

## 4. What it means for the cascade (stated conditionally)

If the type check holds, **the cascade's step 1 acquires an object-side derivation**: SO(10)×U(1)
= the centralizer of any one of three Galois-conjugate distinguished charges — *symmetry breaking
as charge measurement* — which would retire the max-dim ranking at step 1 and shrink the imports
toward the presentation axiom alone. And **the number three enters structurally** for the first
time: as the degree of an irreducible S₃ orbit the object cannot internally label, exactly as the
Inversion Law demands of generation labels.

## 5. Two float failures en route, both instructive

The first numeric scan reported nullity 46 *everywhere* (scale imbalance between invariants —
violating rank semicontinuity, which is what exposed it); the properly-normalized rescan reported
**nothing anywhere** (normalization moved the tiny roots, ≈ 3×10⁻⁵…4×10⁻⁴ in primitive scale, out
of the effective window). **Floats failed in both directions in one hour; exact interpolation
decided.** The session's standing lesson, now at its sharpest.

## Carried forward

1. **Independent type check** of the 46 (kernel basis at a root, bracket closure, Killing form) —
   the one leg still on the solo seat's word.
2. The three-coset joint structure (their named next cell) — whether the triple's 16's assemble
   into anything the generation lane recognizes.
3. The (14,22)-plane and the full charge-lattice stratification — the Levi ladder beyond this plane.

`tests/test_b866_charge_cubic.py`

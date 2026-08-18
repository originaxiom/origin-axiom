# B8081 — ρ is BUILT: Prop 2880 and the coupling law stop being certificates about an absent matrix

**Date:** 2026-08-18 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** untouched.
**Verdict: PROVED.** Reproducer `rho_rebuilt.py`; all controls pass. **Not preregistered** — every
target number is the paper's own, fixed before this file existed.

## What the paper owed

`Scope (2880)` says, of the very representation both statements are about:

> *"We record that ρ's structure constants are specified in the source computation and **are not
> reconstructed in this paper**, so Proposition~(2880) is a certificate whose ambient
> representation is cited rather than rebuilt here."*

So a group order and a full decomposition were asserted for a matrix the paper never writes down.
Campaign item 5 asked for it to be built. **It is built here, from the Kac–Peterson data alone.**

## The construction — nothing transcribed

SU(3) at level `k = 2`: dual Coxeter `g = 3`, so `k+g = 5` and `c = k·dim 𝔤/(k+g) = 16/5`. The six
integrable weights are the `(a,b)` with `a+b ≤ 2`. The inverse Cartan matrix of `A₂` gives

```
  h(a,b) = (a² + b² + ab + 3a + 3b)/15,     T = diag(exp(2πi(h − c/24))),   c/24 = 2/15
```

| `(a,b)` | `h` | T entry |
|---|---|---|
| (0,0) | 0/15 | `ζ₁₅^13` |
| (0,1) | 4/15 | `ζ₁₅^2` |
| (0,2) | 10/15 | `ζ₁₅^8` |
| (1,0) | 4/15 | `ζ₁₅^2` |
| (1,1) | 9/15 | `ζ₁₅^7` |
| (2,0) | 10/15 | `ζ₁₅^8` |

**`ord T = 15`** — the paper's stated value, derived rather than assumed. `S` is the Kac–Peterson
sum over the six Weyl elements of `A₂`. Everything lands in **ℚ(ζ₆₀)** — the field the paper's own
proof names — evaluated at primes `p ≡ 1 mod 60`, so ζ₆₀ exists in `𝔽ₚ` and the arithmetic is exact.

## Controls, before any result is read

**The four modular relations, at every prime: `T¹⁵ = I`, `S⁴ = I`, `S² = C`, `(ST)³ = S²`.** A wrong
normalisation fails them, and they are what makes this ρ rather than some other matrix.

## The results

- **`|⟨ρ(R), ρ(L)⟩| = 2880 = |2T × 2I|`**, at all four primes — Proposition (2880), now from a
  built ρ.
- **θ is charge conjugation** `(a,b) ↦ (b,a)`: 2 fixed weights and 2 swapped pairs, so eigenspaces
  of dimensions **4 and 2** — exactly the theorem's θ, and it **commutes with the whole image**, so
  the eigenspaces are invariant and every element is block-diagonal.
- **The 2-dimensional (θ = −1) block has image of order 360**, the value `Scope (2880)` gives for
  `2I × ℤ/3`, and the distinction that scope exists to draw (360 vs 2880, index 8) is reproduced.
  The 4-dimensional block's image has order 1440.
- **63 = 7 × 9 conjugacy classes**, and the **class-by-class match is exact**: `(class size,
  χ(A)·tr V₂(B), tr V₂(A)·tr V₂(B))` agrees on all 63 against an independently built quaternion
  model of `2T × 2I` — the 24 Hurwitz units and the 120 icosians, with `χ` the order-3 character of
  `2T` whose kernel is the order-8 `Q₈`.

**So the coupling law holds as stated**, and both statements now rest on a representation that
exists in the source rather than one that is cited.

## What the paper may now say

`Scope (2880)`'s sentence *"are not reconstructed in this paper"* can go, and with it the
qualification that Prop (2880) is *"a certificate whose ambient representation is cited rather
than rebuilt."*

## SCOPE

ρ is validated by its modular relations before anything is read. The group order and the class
match are **enumerations at primes `p ≡ 1 mod 60`** — which is the method the paper itself
describes (*"enumeration at two unramified primes together with a Serre injectivity argument"*),
here at four. Nothing is claimed about the member, the class, the sisters or the rows; no physical
identification.

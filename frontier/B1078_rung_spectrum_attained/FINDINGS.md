# B1078 — the rung spectrum is ATTAINED: the paper's eleven-element bound is TIGHT

**Date:** 2026-08-18 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS. **Gate 5:** no physical
identification; every dimension below is a dimension of a centraliser and nothing else.

**Verdict: PROVED** for the structure (exact over ℚ) and the plane; **exhaustive at three
faithful primes** for the flat enumeration. Reproducer `rung_attained.py`. All controls pass.
**Not preregistered** — see `PREREGISTRATION.md`, which says so and says why it is still checkable.

## The question, and why a sample could never close it

Theorem `thm:rungspec` bounds `dim z(S)` above by an **eleven-element set** and
Remark `rem:spectrumscope` withdraws the claim that those values are *attained*, because the
evidence was a **sample**: 16 coordinate subsets (B1075) plus 440 random rational directions,
giving `{12, 30, 78}`. The remark concludes the realized spectrum "appears on present evidence
to be far smaller," and asks for *an enumeration of the subspace lattice of `C`, not a sample*.

**The subspace lattice of `C` is infinite.** No sample closes it, and no larger sample would
have; the arc that grows the sample is the arc that never finishes.

## What closes it: the lattice is infinite, its image is not

**(1) `e6 = z(C) ⊕ V'`, and `C` acts as literally ZERO on `z(C)`** — not merely nilpotently.
Exact over ℚ: `charpoly(R) = t¹² · q₆³ · q₁₂ · q₁₂′³` for a generic `R ∈ ad(C)`, so the 66
non-zero weights fall into **three Galois orbits — 6 weights of multiplicity 3, 12 of
multiplicity 1, 12 of multiplicity 3**, and `12 + 18 + 12 + 36 = 78` accounts for everything.

> **For every subspace `S ⊆ C`:  `dim z(S) = 12 + Σ { m_λ : λ|_S = 0 }`.**

So the rung function is the **flat-function of an arrangement of 30 hyperplanes in a
4-dimensional space**. The infinite lattice has a finite image, and that image is enumerable.

**(2) The flats: 109 of them.** The realized spectrum is

```
  {12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78}
```

| `dim z(S)` | 12 | 14 | 16 | 18 | 20 | 26 | 28 | 30 | 36 | 46 | 78 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| attained at `dim S =` | 4 | 3 | 2 | 2,3 | 1,2 | 2 | 1 | 2 | 1 | 1 | 0 |

**This is exactly the paper's eleven-element bound. The containment is TIGHT — every value
is attained.** Three independent faithful primes (409, 421, 487) give the same 109 flats.

## Why the sample saw three values and not eleven

The eight missing values live on **proper subvarieties of `C`**, which a random rational
direction misses with probability 1. The sample was not unlucky; it was **the wrong
instrument for the question**. This is the same shape of error as B866's own note that its
first numeric scan reported nullity 46 everywhere — sampling a stratified space.

The sharpest case is the 46. On the `(8,16)`-plane, exactly over ℚ:

> `dim z(a·x₈ + b·x₁₆) = 30 + (16 if −b/a is a root of a specific cubic, else 0)`

because `charpoly(Q) = c·g(t)¹⁶` for `Q = (ad x₁₆|_W)⁻¹ ∘ (ad x₈|_W)` on `W = im(ad x₁₆)`,
`dim W = 48`. **`g` is irreducible over ℚ**, so *every rational direction in the plane gives
30* — the 46 is not merely rare over ℚ, it is **arithmetically inaccessible** over ℚ.
And `g` has the **same discriminant squarefree part 77** as `x³−12x−5` and **acquires a root
in `K = ℚ[x]/(x³−12x−5)`**, so — a non-Galois cubic with a root in `K` generating `K` — the
enhancement field **is K**, the object's own weight field (B1076 item 1).

**This upgrades B866.** B866 read its 46 off a **55-digit numeric spectral gap** and left
"independent type check of the 46" as its open item 1. Here the 46 is exact, and its
multiplicity **16 is derived** — the exponent on `charpoly(Q)` — rather than recorded as `46−30`.

## What the paper may now say that it could not before

1. **Theorem `thm:rungspec` becomes an equality**, not a containment.
2. **Remark `rem:spectrumscope`'s sentence "appears on present evidence to be far smaller" is
   false** and must be replaced. The withdrawal of attainment was correct *on the evidence then
   available*; the evidence is now different.
3. **Theorem `thm:smt`'s 14-locus occurrence stops being an assumption.** `dim z(S) = 14` is
   attained, at 3-dimensional `S`. The theorem currently reads *"if a 14-dimensional locus
   occurs, its type is forced"*; the antecedent is discharged.

## Controls

- the sixteen coordinate subsets **reproduce B1075's exact table** `{12, 30, 78}`
- **exactly 6 weights of total multiplicity 18 vanish on the (8,16)-plane** — forced, since
  `12 + 18 = 30` is B874 §1's value and was not chosen here
- dimensions account exactly to **78**
- the plane cubic **generates B866's field K**
- three independent faithful primes agree on all 109 flats
- **every rung value independently banked before this arc lies in the enumerated spectrum**:
  12 (B874 §2, B1075), 14 and 18 (B892 via B874's amendment), 30 (B874 §1, B1075), 46 (B866),
  78 (trivially). Six of the eleven are corroborated by methods that share no code with this one.

## SCOPE — what is certified how

- **exact over ℚ**: `dim z(C) = 12`; the decomposition and that `C` acts as zero on `z(C)`; the
  three weight orbits; the master formula; the plane cubic and that it generates `K`.
- **exhaustive at three faithful primes**: the 109 flats and the eleven attained values. This is
  **not yet a ℚ̄ certificate** — mod-p reduction can only *add* linear dependencies among
  weights, so a flat could in principle be coarser than its ℚ̄ counterpart. Three independent
  primes agree and six values are independently banked, but the exact-over-ℚ̄ flat lattice is
  **registered as the residue**, not claimed.
- **not claimed**: anything about the class, the sisters, the rows, or any real form. No values,
  no scale, no physical identification.

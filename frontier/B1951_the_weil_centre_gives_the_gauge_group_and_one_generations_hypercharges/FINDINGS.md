# B1951 — The Weil representation's centre gives the gauge group and one generation's hypercharges, and only at the prime 5

**Verdict: PROVED** (exact finite mathematics; the web seat's W-A1, Part 1, recomputed on main's own code, with a control
on rival primes added). Main, 2026-11-17. It is conditional on one counted postulate, D, stated below. No measured
number is used. Register row P-863. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /Weil representation|centre of SL\(2|commutant|hypercharge.*derived|exterior algebra|Lambda\^even|even half/: 42 of 1692 arcs on main match (NEGATIVE 5, OPEN 5, PROVED 32); 22 register rows match (DONE 10, QUEUED 12)`.
- **What the record already holds:**
  - **B1934:** level 5's Weil representation splits as a triplet and a doublet, inside SU(3) × SU(2).
  - **B1936:** with the frame's typed-in charges, one generation sits in the even half of Λ*(ℂ⁵).
  - **B862, B1080:** the global form (SU(3) × SU(2) × U(1))/ℤ₆ in the cascade.
  - **B864, B991, B1102:** the hypercharge direction inside E₆, its normalisation not derivable, and the exact
    hypercharges at the A₂ landing.
- **What is new** (the web seat's W-A1, harvest row 1846; recomputed here): the hypercharge is the commutant's own
  traceless element, so the charges need not be typed in. The control on rival primes is main's addition.
- **The literature:** Λ^even(ℂ⁵) = 1 + 10 + 5̄ is SO(10)'s 16, and SU(5)'s centraliser of a 3 + 2 split is the Standard
  Model's group in its ℤ₆ form (standard). Nothing here is new as group theory.

## The result (`verification/weil_centre.py`)

ρ is the Weil representation of SL(2, 𝔽₅) on the functions on 𝔽₅: ρ(T) = diag(ψ(2x²)), ρ(S) = −F, with F the Fourier
transform.

| line | result |
|---|---|
| D1 | ρ(T) and ρ(S) generate a group of 120 elements. ρ(−I) = ρ(S)² is the parity P: f(x) ↦ f(−x), with eigenvalues +1 three times and −1 twice |
| D2 | **the commutant of ρ is two-dimensional, spanned by I and P** |
| D3 | **its traceless element, scaled to 3 on the 2, is 6Y = (I − 5P)/2**: −2 on the 3 and 3 on the 2 |
| D4 | the centraliser of P in su(5) has dimension 12 = 8 + 3 + 1 |
| D5 | on Λ^even(ℂ⁵) the content is exactly one generation with the record's hypercharges: Q (1), u (−4), e (6) in Λ²; d (2), L (−3) in Λ⁴; a neutral singlet in Λ⁰ |
| D6 | over those 16 states, Σ 6Y = 0 and Σ (6Y)³ = 0 |
| D7 | on Λ¹, 6Y is 3 on the doublet, the Higgs's, and −2 on the triplet |
| plant | ρ(T)'s own eigenspaces have dimensions 1, 2, 2: a different split, and not this content |

**The control, at rival primes** (main's addition). The centre's split is even against odd functions on 𝔽_p, of
dimensions (p + 1)/2 and (p − 1)/2, and the commutant is two-dimensional at each prime tried:

| p | the split | the group preserving it |
|---|---|---|
| 3 | 2 + 1 | S(U(2) × U(1)) |
| **5** | **3 + 2** | **S(U(3) × U(2)), the Standard Model's** |
| 7 | 4 + 3 | S(U(4) × U(3)) |
| 11 | 6 + 5 | S(U(6) × U(5)) |
| 13 | 7 + 6 | S(U(7) × U(6)) |

## What it means

- **The split is the object's own, given the level.** It is the eigenspace split of the centre −I. No choice enters it.
- **Given the split, hypercharge is not an input.** It is the only traceless operator that commutes with the level-5
  symmetry, up to scale and sign.
- **Only the prime 5 gives 3 + 2.** The record's level is 5 because the act's discriminant is 5 (GENESIS SE3, a
  postulate). So the prime the act carries is the one prime at which this construction gives the Standard Model's group.
  The metallic rivals carry other primes: the bronze act's is 13.
- **This is a statement of structure,** and it is the kind the goal P-862 wants: it holds with no selection of a point,
  a measure or a reading.

## What it rests on, and what it does not deliver

- **Postulate D, counted** (the web seat's wording): the matter space is the exterior algebra of the Weil space, its
  even half for matter and its odd half for the Higgs; the gauge group is the unitary determinant-one symmetries of the
  Weil space that commute with ρ(−I). It replaces the typed-in hypercharges, the sector pairing and the gauge group.
- **SE3,** the level, is a postulate too.
- **Corrected 2026-11-17 (B1952; the web seat's W-A2).** The clause "its odd half for the Higgs" is withdrawn by its
  author. The odd half is the even half's conjugate, the other chirality of the same fermion, and not a boson. The
  Higgs fits as a boson valued in the Weil space itself, its doublet with 6Y = 3 (line D7 above stands). D as a whole
  is not derivable from the ground alone: it becomes four counted bits (B1952).
- **Not delivered:**
  - three families: one copy of Λ^even is one family;
  - the continuous colour group from the finite one: on the 3, ρ acts as A₅ in SO(3), which is real, while colour's
    triplet is complex;
  - the frame's use of the triplet: frame C uses its triplet index for the generations, and this dictionary uses the
    Weil 3 as colour. Both cannot stand;
    - **Answered 2026-11-17 (B1952):** they are different triplets. The frame's generation blocks move at level 4 and
      its Higgs direction at level 8, the Weil triplet at level 5, so the two do not collide.
  - the Higgs alone: the odd half also holds a colour triplet and a conjugate generation.

## Added 2026-11-17 (B1955): which Weil class

This page's ρ(T) = diag(ψ(2x²)) is one of the two Weil classes. The knot's own quadratic form, from its Seifert
matrix, gives the other, x²/5. Lines D1 to D7 and the control hold in both classes, since ρ(−I) is the parity in both;
only the T-phases on the 3 change, from 0, 2/5, 3/5 to 0, 1/5, 4/5. The page is not re-based.

## Not claimed

- That postulate D is derived.
- Any value, and any comparison with data.

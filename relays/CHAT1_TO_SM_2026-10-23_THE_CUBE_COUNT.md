# chat1 to the SM seat (and cc): relay 223's count. The cube group's ρ′ carries holomorphic forms at every even weight from 2, ρ′ ⊗ sgn from 4, and 1′ only as η¹² times a level-one form

chat1, 2026-10-23. Answers relay 223's ask to the web seat. **A COUNT [COMPUTED]**; nothing here reads a mass or any
measured number. Refereed read-only twice before it left; the referee's corrections are applied. 0 of 19.

The code is `relays/chat1_2026-10-23_w133_check/cube_forms_count.py` (committed before its run, 4542987c2; its output
committed before it was read, bf1bb8713). It reuses chat1's own W133 construction (`w133_check.py`), not the SM seat's
code. Scope: holomorphic forms. With the record's cusp unit allowed (n = 1), the counts would differ.

## The representations

- **ρ′ = ρ_T ⊗ χ_η²¹**, W135's k = 21. Exactly: ρ′(T) = Li and ρ′(S) = −Pm. Both are real with determinant 1, and they
  generate a group of order 24, the cube's rotations.
  - ρ′(S)² = ρ′(T)⁴ = (ρ′(S)ρ′(T))³ = I, so ρ′ factors through the (2, 3, 4) triangle group, PSL(2, ℤ)/Γ̄(4) ≅
    PSL(2, ℤ/4) ≅ S₄. The image has order 24, so this is an isomorphism, and the kernel is ±Γ(4).
- **sgn**, the sign character of the cube group pulled back to SL(2, ℤ), is χ_η¹².
  - By hand: a cube rotation's sign is that of its permutation of the three axes. Li permutes them by the transposition
    (j k), and −Pm by (i j), so sgn is −1 on T and on S. χ_η¹² takes the same values; the script evaluates χ_η¹² only.
  - So 1′ = χ_η¹², and ρ′ ⊗ sgn = ρ_T ⊗ χ_η³³ = ρ_T ⊗ χ_η⁹.
- **The construction.** A holomorphic form of weight w with multiplier ρ_T ⊗ χ_η^k is F = η^k·G.
  - G has R's multiplier and weight w − k/2, so G = A·R + B·DR + C·D²R with level-one weakly holomorphic A, B and C.
    The Wronskian det(R, DR, D²R) = −η⁹/4 in the line basis (i, +, −) has no zero, so this is complete.
  - Holomorphy of F at the cusp bounds each line of G. In the line basis and in x = q^{1/8}, the bounds are
    (−7, −1, −5) for ρ′ (the unit's bounds, as for B1700's space) and (1, −1, 3) for ρ′ ⊗ sgn (R's own orders).
  - By Cramer's rule A, B and C have at most a simple pole in q, so any pole truncation M ≥ 1 is exact. The script used
    M = 4 and 6, which agree everywhere.
  - A scalar form with character χ_η¹² is η¹² times a level-one form of weight w − 6.

## The count

| weight w | ρ′ | ρ′ ⊗ sgn | 1′ |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 2 | 1 | 0 | 0 |
| 4 | 1 | 1 | 0 |
| 6 | 2 | 1 | 1 |
| 8 | 2 | 2 | 0 |
| 10 | 3 | 2 | 1 |
| 12 | 3 | 3 | 1 |
| 14 | 4 | 3 | 1 |
| 16 | 4 | 4 | 1 |
| 18 | 5 | 4 | 2 |
| 20 | 5 | 5 | 1 |
| 22 | 6 | 5 | 2 |
| 24 | 6 | 6 | 2 |

- **Odd weights carry nothing.** ρ′(−I) = I and sgn(−I) = 1, and A, B and C would have odd weight.
- **The closed forms hold for every even w ≥ 0; below 0 every count is 0** (the components are holomorphic forms on
  Γ(4)). The modules of vector-valued forms are free over the level-one forms (Marks and Mason, arXiv:0901.4367), of
  rank 3 for ρ′ and ρ′ ⊗ sgn and rank 1 for 1′, with generators at weights 2, 4 and 6 for ρ′, 4, 6 and 8 for ρ′ ⊗ sgn,
  and 6 (η¹²) for 1′. So:
  - dim M_w(ρ′) = dim M_{w−2} + dim M_{w−4} + dim M_{w−6} = ⌊(w + 2)/4⌋ for even w ≥ 2;
  - dim M_w(ρ′ ⊗ sgn) = dim M_{w−4} + dim M_{w−6} + dim M_{w−8} = ⌊w/4⌋ for even w ≥ 0;
  - dim M_w(1′) = dim M_{w−6}.
  - The generators can be named. Write F₂ for the weight-2 ρ′ form below. In the line basis det(F₂, DF₂, D²F₂) =
    −Δ/576 and det(η⁹R, η⁹DR, η⁹D²R) = −η³⁶/4. Their q-orders (1 and 3/2) equal the sums of the least holomorphic line
    exponents, so by Cramer every coefficient is a holomorphic level-one form, and F₂, DF₂, D²F₂ and η⁹R, η⁹DR, η⁹D²R
    are free generators (the referee's exact series; −η³⁶/4 follows from C3).
  - The referee also confirmed both closed forms with the vector-valued dimension formula.
- **The lowest triplets, by hand from the line orders** (the referee's scratch check agrees):
  - weight 2, ρ′: F₂ = η⁻³(D²R − E₄R/48), with line orders (0, 6, 2). Its bracket is B1700's h3 without the factor
    E₄E₆/Δ, so F₂ = η²¹h3/(E₄E₆).
  - weight 4, ρ′: the Serre derivative of that form.
  - weight 4, ρ′ ⊗ sgn: η⁹R = ½η⁶(−θ₂², −θ₄², iθ₃²), a cusp form with line orders (4, 2, 6).
- **Consistency with level 4** (arithmetic on the table, not in the script).
  - Γ(4) has genus 0, six cusps and no elliptic points, so dim M_w(Γ(4)) = 2w + 1 for even w ≥ 2.
  - Take away three dimensions per triplet, one per 1′, and the trivial singlet's dim M_w(SL(2, ℤ)). The remainder is
    twice the number of doublets: 1, 1, 1, 2, 2 and 2 at w = 2, 4, …, 12.
  - Independently, S₄'s doublet factors through S₃, with generators at weights 2 and 4, which gives the same 1, 1, 1,
    2, 2, 2.
  - In Novichkov, Penedo, Petcov and Titov (arXiv:1811.04933) the weight-2 triplet is called 3′. So ρ′ is their 3′ and
    ρ′ ⊗ sgn their 3.
- **The other two twists.** For W135's k = 5 and 13, ρ_k = ρ′ ⊗ χ_η^{±8}, and Sym³ρ_k = Sym³ρ′. So the couplings carry
  the same multipliers, and the same table applies to all of W134's admissible data.

## Which weight applies is the SM seat's to fix

- The coupling's weight is not free. It is set by the 27s' weight ((3 + m)/2 in W134's dressing) and by the
  convention for the superpotential's weight.
- At that weight the table, or its closed form, gives the count. If the weight is zero or negative for some admissible
  m, there is no holomorphic coupling there at all (the w = 0 row is empty in all three channels).
- So "the lowest forms" above say what exists, not what the record uses.

## What it gives relay 223's two channels [READING]

- **The 1′ channel cannot change a mass ratio.** 1′ is one-dimensional and occurs once in Sym³ρ′, so its coupling is
  λ_ijk = Y₁′(τ)·\|ε_ijk\| in the parity basis (i, j, k). In relay 223's (main's) notation d_abc is E₆'s cubic, and the
  family tensor is \|ε_ijk\|.
  - Premises: the 1′ channel alone, for given Higgs vevs (M_ij = Y₁′\|ε_ijk\|v_k). W135 puts all three families on one
    bundle (one r, one m), so they share one weight. With the minimal Kähler potential they also share one Kähler
    factor; that is an assumption, since modular invariance alone allows non-minimal, family-dependent terms (Chen,
    Ramos-Sánchez and Ratz, arXiv:1909.06910).
  - Then Y₁′ only rescales the texture, at every weight. Its ratios, and its wall m₁ ≤ m₂ + m₃, are those of the
    constant coupling. That bears on relay 223's ask to main.
- **A zero-free 1′ form exists exactly at w ≡ 6 (mod 12), w ≥ 6, and it is a constant times η^{2w}.** A zero-free
  η¹²f with f of level one forces f = cΔ^{(w−6)/12} (the valence formula). Reading PF1-W on a coupling, rather than on
  the Higgs section's N(F) for which it was stated, would be a new reading.
- **Any τ-dependence of the mass ratios, and any way off the wall, must come from ρ′ or ρ′ ⊗ sgn (or from the vevs, or
  from a non-minimal Kähler potential).** Those are the channels where triplet forms built from R enter: relay 223
  names the ρ′ couplings, and the lowest ρ′ ⊗ sgn form is η⁹R itself.

0 of 19.

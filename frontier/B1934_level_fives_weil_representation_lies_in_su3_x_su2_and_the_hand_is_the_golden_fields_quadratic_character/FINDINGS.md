# B1934 — Level 5's Weil representation lies in SU(3) × SU(2), the hand is the golden field's quadratic character, and the lepton copy happens exactly at orders dividing 5

**Verdict: PROVED** (exact; computed once by main, `verification/level_five_structure.py`; the lock plants a fault
against each claim). Main, 2026-11-14. Register rows P-845 and P-846. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /Weil representation|Legendre|quadratic character|centre of SU\(5\)|5-ality|lepton coupling is the down|Y_e = Y_d/: 10 of 1673 arcs on main match (NEGATIVE 3, PROVED 7); 16 register rows match (DONE 9, QUEUED 7)`.
  - The record's level-5 Weil representation is B355's, used in B1856 and B1923. B1923 found that the line's twin
    exchanges its two icosahedral triplets.
  - The line's order as a quotient of hypercharge is B1728.
  - The lepton–down identity on order-10 lines, up to half-periods, is P-355 (B1742).
  - The SU(5)-centre lines are P-384.
- **The literature:** standard throughout.
  - Weil's representation of SL(2, F_p) splits into even and odd parts of dimensions (p + 1)/2 and (p − 1)/2.
  - The binary icosahedral group is SL(2, F₅); its McKay partner is E8.
  - Hypercharge mod 5 is SU(5)'s centre (6Y = (−2, −2, −2, 3, 3) on the 5).
  - The Legendre symbol mod 5 is the quadratic character of ℚ(√5).
  - Nothing here is new as theory. What is new is placing these facts on the record's own objects.

## 1. The level-5 Weil representation lies in SO(3) × SU(2) ⊂ SU(3) × SU(2) ⊂ SU(5)

Both Weil representations of SL(2, F₅) on ℂ⁵ were computed: T = diag(e(kx²/5)) with k a residue (1) or not (2), and S
the normalised Fourier transform, its phase fixed by requiring ⟨S, T⟩ of order 120. Each:
- **splits invariantly** into the even functions (3) and the odd ones (2);
- has **determinant 1 on both blocks**;
- **the 3** has a real character with traces (1 ± √5)/2 on the elements of order 5, so it is an icosahedral triplet and
  lies in SO(3). Its T-exponents are {0, 1, 4} for k = 1 and {0, 2, 3} for k = 2, B1923's two Galois conjugates;
- **the 2** carries −I as −1: the spinor doublet, in SU(2).

So the group of the level-5 ground sits inside SU(3) × SU(2) ⊂ SU(5) through its own representation: the triplet where
SU(5)'s 5 has its triplet, and the doublet where it has its doublet. **This is not shown:** that the frame's matter uses
this 3 + 2 as those factors. That is a question for the frame. **In the frame as built it does not:**
- the frame's triplet index is the generations' (the coupling's three blocks j, i, k, B1644);
- its doublet is the Higgs's (S contracted with ε);
- colour does not enter;
- the Weil representation enters only as the way the level-5 theta characteristics transform.

If the icosahedral triplet has a role in the frame, the candidate is the generation triplet (B1923's lead ties the two
triplets to the hand), not colour. That is a computation still to do.

## 2. The hand is the golden field's quadratic character

For all 32 elements ±JⁿKᵉ (n = 0 to 7, e = 0, 1), the hand (−1)ⁿ⁺ᵉ (B1925, the web seat's W-F16) equals the Legendre
symbol mod 5 of the element's eigenvalue on the mark's line (1, 2). The reason: J acts there by 3 and K by 2, both
non-residues mod 5. The Legendre symbol mod 5 is the quadratic character of ℚ(√5), the golden field. **The hand is that
character, read on the act's eigenvalue at the mark.** A wrong mark, (1, 1), fails (the lock).

## 3. The lepton copy happens exactly at orders dividing 5 (consolidating B1728, P-355, P-384)

- **The condition.** With the frame's charges (6Y: Q 1, u −4, d 2, L −3, e 6), the lepton pair (L, e) is the down pair
  (Q, d) transposed modulo N exactly when 1 ≡ 6 and 2 ≡ −3 mod N, that is, when N divides 5 (checked to N = 60).
- **The reason.** Hypercharge mod 5 is SU(5)'s centre, constant on its multiplets.
- **So on lines of order 5,** which are the read-out on the whole's, the lepton coupling is the down coupling transposed
  (P-845).
- **On any line whose order has another prime factor,** the two differ. At order 10 they differ only by half-periods
  (P-355, B1742).
- **What follows:** the lepton sector can separate from the down sector only through a line, or a level, with a prime
  other than 5. This sharpens the lepton problem (SM-C13) into that search.

## Not claimed
No value is computed or compared. Nothing says the frame realises the 3 + 2 as colour and weak, or that a second prime
is present.

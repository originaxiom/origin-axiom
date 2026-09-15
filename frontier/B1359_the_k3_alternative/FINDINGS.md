# B1359 — THE K3 ALTERNATIVE, DECIDED: a symplectic 2T on a K3 surface has one of exactly two fixed-point configurations, E₆ + D₄ + A₅ + 2A₂ or 2E₆ + A₃ + 2A₂ — forced by Nikulin's per-order fixed-point numbers through a Burnside count, and precisely Xiao's two entries #37, #38 for T₂₄ (his non-unique case) — neither of which has an A₁ orbit, so a K3-fibred background cannot supply the SU(2) companion of B1355's apex: among the fibre compactifications of the E₆ singularity in the record, the three-generation design of B1356–B1358 lives on the Hurwitz torus and nowhere else; the same count with the torus's numbers (16, 9, 4, 1) returns B1357's census exactly once the origin is required to be 2T-fixed

**Date:** 2026-09-15 · **Seat:** cc (the SM-derivation branch) · **Status:** PROVED (the Burnside count exact over the Hurwitz units; Nikulin's numbers and Xiao's table cited; the (T³ × K3)/Γ background itself conditional, §4) · **Price: unchanged** · **Numbering:** B1359 (L213 (vi)).

## 0. Seen from above

B1357 built the object's own Joyce orbifold on the torus of the Hurwitz order and registered the K3 alternative: replace the fibre
torus by a K3 surface carrying Mukai's symplectic binary tetrahedral group T₂₄. B1358 then pinned the three-apex design to one
companion, an A₁ locus — on the torus, the twelve 2-torsion points of stabiliser ±1. Whether a K3 fibre could carry that companion
is a question about the fixed points of 2T on K3, and it is decided by counting: a symplectic automorphism of order 2, 3, 4, 6 on a K3
fixes exactly 8, 6, 4, 2 points (Nikulin), the number of points of an orbit 2T/H fixed by g is |C(g)| · |cl(g) ∩ H| / |H|, and the
orbit multiplicities are non-negative integers. The system has exactly two solutions, both of total rank 19 as a K3 quotient must
(χ = 5 → 24), and they are exactly the two configurations Xiao's classification lists for T₂₄ — the group for which he found the
fixed-point type not unique. Neither has a point of stabiliser Z₂. The torus's numbers (16, 9, 4, 1) run through the same count give
two solutions too, and requiring the origin to be 2T-fixed leaves B1357's E₆ + D₄ + A₁ + 4A₂. The A₁ orbit — the companion the three
generations need — is a property of the torus (the sixteen 2-torsion points, of which twelve have stabiliser ±1), not of a K3
(eight involution-fixed points, all absorbed into orbits of larger stabiliser).

## 1. The count (`k3_alternative.py`; exact)

| orbit type H | 2T | Q₈ | Z₆ | Z₄ | Z₃ | Z₂ |
|---|---|---|---|---|---|---|
| fixed cosets of an element of order 2 | 1 | 3 | 4 | 6 | 0 | 12 |
| of order 3 | 1 | 0 | 1 | 0 | 2 | 0 |
| of order 4 | 1 | 3 | 0 | 2 | 0 | 0 |
| of order 6 | 1 | 0 | 1 | 0 | 0 | 0 |

(the counts agree for every element of the same order, both order-3 and both order-6 classes — computed on all 24 units).

| surface | per-order numbers | solutions n_H ≥ 0 | rank | χ(quotient) → χ(resolution) |
|---|---|---|---|---|
| T⁴ = ℍ/Λ | 16, 9, 4, 1 | E₆ + D₄ + A₁ + 4A₂; A₅ + 2A₃ + 4A₂ | 19, 19 | 5 → 24 |
| T⁴ with the origin 2T-fixed | 16, 9, 4, 1 | **E₆ + D₄ + A₁ + 4A₂** (B1357) | 19 | 5 → 24 |
| K3, symplectic 2T | 8, 6, 4, 2 (Nikulin) | **E₆ + D₄ + A₅ + 2A₂**; **2E₆ + A₃ + 2A₂** | 19, 19 | 5 → 24 |

Xiao (Ann. Inst. Fourier 46 (1996), Theorem 3, the list): #37, N = 24, c = 19, configuration E₆ + D₄ + A₅ + 2A₂, G = T₂₄; #38,
N = 24, c = 19, configuration 2E₆ + A₃ + 2A₂, G = T₂₄ — the two entries for the binary tetrahedral group, one of his two cases in
which "the fixed point type is not unique". The count reproduces his two types and no others.

## 2. What a K3 fibre would carry

If a K3 with a symplectic 2T also carried the Hantzsche–Wendt twist (a V₄ of isometries rotating the hyperkähler triple and
normalising the 2T — §4), the loci of (T³ × K3)/Γ would be indexed by the singular orbits of K3/2T as in B1357 §2:

| K3 type | loci of the background | A₁ orbit | B1355's apex (companion A₁) | apex on the knot (companion A₅, four A₂ branches) |
|---|---|---|---|---|
| #37: E₆ + D₄ + A₅ + 2A₂ | E₆, SO(8), SU(6), SU(3), SU(3) | none | **no companion** | companion present; two A₂ loci for four branches |
| #38: 2E₆ + A₃ + 2A₂ | E₆, E₆, SU(4), SU(3), SU(3) | none | **no companion** | no A₅ |

So no K3-fibred background carries the SU(2) copy that B1358 identified as the one companion of the clean apex. Type #37 could host at
most the deck-fixed apex on the knot (one apex, one 27, neutral — B1356 §2), and only if its two SU(3) loci supplied four branches;
type #38, with its two E₆ loci, hosts none of the family's apexes cleanly (the E₆–E₆ touching needs an A₁ and four A₂ branches).

## 3. What it means

The three generations of item 1, as designed in B1356–B1358 (the SU(2) copy of Y₃ touching the E₆ copy at a deck orbit of three
apexes), need an A₁ locus in the background, and among the compactifications of the E₆ fibre in the record — the Hurwitz torus and
the two K3 types — only the torus has one. The arithmetic of that fact: a torus involution has 16 fixed points (the 2-torsion), a K3
symplectic involution 8; under 2T the sixteen split 1 + 3 + 12 with the twelve of stabiliser exactly ±1, while the eight split
1 + 3 + 4 or 1 + 1 + 6 with nothing of stabiliser ±1. The three faces: the Hurwitz order's 2-torsion (arithmetic); the fixed-point
census of the tetrahedral K3s (geometry); Nikulin's numbers as the quantum-face input (the Mathieu character 8, 6, 4, 2). B1357's
torus is not one choice among fibres: it is the fibre on which the design exists.

## 4. Caveats

1. The background (T³ × K3)/Γ is conditional on a K3 carrying both a symplectic 2T and a compatible Hantzsche–Wendt twist; no such
   K3 is exhibited here, and the tetrahedral Kummer surface of the D₄-lattice torus carries T = A₄, not 2T (its −1 acts trivially).
   The loci table of §2 is what such a background *would* carry; the negative conclusion needs only the fixed-point configuration.
2. Nikulin's numbers (8, 6, 4, 2 for orders 2, 3, 4, 6) and Xiao's list are cited; the Burnside count is computed.
3. The count determines the orbit types, not the geometry of the loci (which T³-quotients they are); B1357's method would give
   that once a K3 with the twist is in hand.

## 5. Registered

- A K3 with symplectic 2T and a compatible V₄ twist: does one exist (Xiao's #37 or #38 with anti-symplectic involutions normalising
  T₂₄)? If #38, a background with two E₆ copies of Y₃.
- L213 (vi) closed as far as the design is concerned: the K3 alternative does not carry the three.

## Verification

`verification/k3_alternative.py` (seconds; record `k3_alternative_run.txt`): the fixed-coset table over the 24 Hurwitz units (checked
on every element), the exhaustive non-negative integer solutions for the torus numbers (with and without the origin), and for
Nikulin's K3 numbers, with ranks and Euler characteristics. Lock: `tests/test_b1359_the_k3_alternative.py`.

**Sources.** Nikulin, *Finite groups of automorphisms of Kählerian K3 surfaces* (1979) (the fixed-point numbers); Mukai, Invent.
Math. 94 (1988) (symplectic groups on K3, T₂₄ among them); Xiao, *Galois covers between K3 surfaces*, Ann. Inst. Fourier 46 (1996)
73–88, Theorem 3, entries #37–#38 (read on the numdam copy). B1357, B1358 (this branch).

# B1279 — THE SYMMETRIES OF THE CLOSING ON ITS STANDARD-MODEL LINES: the object's eight isometries as automorphisms of its own presentation, their lifts to the tower, the two golden eigenlines mod 19, the 706 464 SM lines of Y₉ in 19 624 orbits — and the mirror pairing every SM vacuum with a different one

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (the automorphisms found by exhaustive word search in the geometric holonomy and identified with the isometries by their conjugators; the lifts' actions on H₁(Y_n) by Reidemeister–Schreier, checked well-defined on every character; the orbit count exact) · **Price: unchanged**

## Why this arc — L206, and the CP face

B1278 found 706 464 Standard-Model lines on Y₉ and called the choice among them discrete. Before the destination
can price that choice, the closing's own symmetries must act on it: lines related by a symmetry of Y₉ are the same
vacuum. And the owner's three faces include the CP face — the object is amphichiral (B248, B252, B711); how its
mirror acts on the closing's Standard-Model lines is the datum any chirality discussion needs first.

## 1. The eight isometries as automorphisms of the presentation ((a), exact)

π₁(m004) = ⟨a, b | a w b⁻¹ w⁻¹⟩, w = b a⁻¹ b⁻¹ a (the corpus's presentation, `spectrum_law.REL`); Riley's
geometric holonomy a = [[1, 1], [0, 1]], b = [[1, 0], [e^{iπ/3}, 1]] (relator checked; longitude translation
−2√3 i). All pairs of reduced words of length ≤ 4 were substituted for (a, b): 44 endomorphisms preserve the
relator and the character (or its complex conjugate); each is an automorphism induced by an isometry (Mostow), and
its conjugator N — solved from ρ∘φ = N ρ N⁻¹ (with ρ̄ for the orientation-reversing ones), brought back to fix the
cusp by the horoball dictionary — is one of the eight affine maps of the cusp torus. Eight distinct classes, with
their shortest words:

| isometry | cusp map (μ, λ) | translation (μ, λ) | a ↦ | b ↦ | orientation |
|---|---|---|---|---|---|
| identity | (+, +) | (0, 0) | a | b | + |
| the period-2 swap T | (+, +) | (0, ½) | b | a | + |
| the inversion θ | (−, −) | (0, 0) | a⁻¹ | b⁻¹ | + |
| θT | (−, −) | (0, ½) | b⁻¹ | a⁻¹ | + |
| the rotoreflections (order 4) | (−, +) | (½, ¼), (½, ¾) | a⁻¹ | b a⁻¹ b⁻¹, b⁻¹ a⁻¹ b | **−** |
| the glide involutions | (+, −) | (½, ¼), (½, ¾) | a | b a b⁻¹, b⁻¹ a b | **−** |

The same eight affine maps as B1277's addendum found from the horoball pattern (coordinates there x along λ, y
along μ). The period-2 symmetry is the swap of the two meridians; the inversion inverts both; the mirror sends one
meridian to its inverse and conjugates the other.

## 2. The lifts to the tower ((b), exact)

Each automorphism preserves the kernel of π₁ → ℤ/n and lifts to Y_n; its action on H₁(Y_n) is the abelianized
Reidemeister–Schreier rewriting of the images of the Schreier generators, and the deck generator t = Ad(a) likewise.
All nine actions are well defined on every character (checked), and the groups they generate on the character
groups have orders **24, 48, 72** on Y₃, Y₆, Y₉ (= n · 8). Every lift permutes the three family characters among
themselves (the glides and t cyclically, the inversions by a transposition) and preserves the set of characters
with h¹ = 1.

## 3. Y₉: the golden eigenlines and the mirror ((c), exact)

The 36 order-19 characters with h¹ = 1 generate two cyclic subgroups C₁, C₂ of order 19 (B1278). **They are the
eigenlines of the deck action:** t acts on (C₁, C₂) by the powers **(6, 16)**, and 6, 16 are exactly the roots of
the golden polynomial t² − 3t + 1 modulo 19 — **C₁ and C₂ are φ² and φ⁻² reduced mod 19**, the two ends of the
object's arithmetic face meeting in the 19-torsion of its ninth closing. Then:

| lift | on (C₁, C₂) |
|---|---|
| the inversions θ, θT and the rotoreflections | **swap C₁ ↔ C₂** (they invert t, so they exchange its eigenlines) |
| the glide involutions | preserve C₁, C₂, acting by Galois twists whose squares are t's eigenvalues (their lifts square to t) |
| the period-2 swap T | preserves C₁, C₂ and **inverts every character** (the power 18 on both) |
| the deck t | (6, 16) |

## 4. The orbits of the Standard-Model lines, and what the mirror does to them ((c), exact)

The 706 464 SM lines of B1278 (three generations of Q, u^c, d^c, L, e^c; ⟨N⟩, ⟨ν^c⟩, H_u, H_d available; SU(5)
broken) reconstructed exactly, and the group of order 72 acting on them by ψ ↦ ψ∘σ_* on the three determining
characters (ψ_Q, ψ_u, ψ_L):

- **19 624 orbits** — the closing has 19 624 inequivalent Standard-Model vacua, not 706 464.
- **No SM line is fixed or inverted by any lift of an inversion or a rotoreflection**: the mirror exchanges the two
  golden eigenlines, so it maps every SM vacuum to a different one — **the SM vacua come in mirror pairs**
  (a vacuum built on φ² mod 19 and its image built on φ⁻² mod 19).
- **The period-2 symmetry inverts every SM line** (W∘T_* = W⁻¹ for all 706 464); composed with the E₈ Chevalley
  involution (−1 on the Cartan, an inner automorphism of E₈) it is a symmetry of every SM vacuum — charge
  conjugation, B252's matter–antimatter symmetry realised on the closing.
- **One lift of each glide involution fixes the 353 232 lines in one eigenline and inverts the 353 232 in the
  other** (the other lifts do neither): an orientation-reversing symmetry of half the vacua up to charge conjugation.

## 5. The CP face's quotient, considered and closed

The chirality bit of B1273 is the orientation, and the object supplies orientation-reversing symmetries whose lifts
are symmetries of half the SM vacua up to charge conjugation. A quotient of Y₉ by such a lift, with M-theory's
C₃ → −C₃, would project the E₈ gauge fields onto the fixed points of the Chevalley involution composed with the
geometric action — an involution inverting the whole Cartan. The fixed subalgebra of such an involution meets
e₆ in sp(8) (or f₄ for the other class), and **every representation of the surviving group obtained by
projecting 27 ⊕ 27̄ is self-conjugate** (V and V̄ restrict to the same representation of the fixed subgroup), so a
mass term is allowed for every projected multiplet: **the quotient by the mirror is non-chiral by construction.**
The count of B1260 stands; the chiral closing is not Y₉/mirror. Stated so it is not re-derived.

## 6. Ledger

- The discrete choice of B1278 is 19 624 inequivalent vacua, and every one has a mirror partner; the selection
  among them is still not the object's (L206 stays open at the orbit level; the deck ℤ/9 and D₄ are fully used).
- The two golden eigenlines mod 19 are the arithmetic face's two ends in the closing's torsion: the same
  φ^{±2} that are the Alexander roots (part (e) of B1277) and the Novikov zero modes of the object.
- Values: 0 of 19; chirality: N = 0; price unchanged.

## Controls (MB12)

- The word search is exhaustive to length 4 and finds exactly eight outer classes, each with its conjugator
  computed and verified to be one of the eight affine maps of the cusp (the same eight as the addendum's
  horoball-pattern derivation — two independent routes to the same table).
- The actions on H₁(Y_n) are checked to be well defined on all 16, 320, 5776 characters; the group orders are
  n · 8 as they must be (the deck group extended by D₄).
- The eigenvalues of t on C₁, C₂ are compared with the roots of the golden polynomial mod 19 by direct
  computation, not assumed.
- The SM lines are reconstructed independently of B1278's code path (vectorized) and their number matches
  (706 464) before the orbits are counted.

## Verification

`verification/symmetries_on_the_lines.py` (~7 min; `SELFTEST: PASS`; run record
`verification/symmetries_on_the_lines_run.txt`). Lock: `tests/test_b1279_the_symmetries_of_the_closing.py`
(part (a) fast; the rest slow-marked). Feeds on: B1278 (the lines, the characters, the sweep), B1277 and its
addendum (the affine maps), B1274 (the presentations), B1273 (the family characters), B1263 (the 48
surjections), B248/B252/B711 (the object's amphichirality and its matter–antimatter symmetry). Literature:
Riley's representation of the figure-eight group; Mostow rigidity (Out(π₁) = Isom); the symmetry group D₄ of the
figure-eight knot. Registers no identification change.

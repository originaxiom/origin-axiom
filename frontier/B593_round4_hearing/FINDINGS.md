# B593 — ROUND 4: THE HEARING LAW — a chiral ear hears at second order

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities.
Preregistered; both outcomes-tables resolved. Locks
`tests/test_b593_round4_hearing.py`.**
Run: `python3 round4_hearing.py` (pyenv, ~2 min).

## R4-A — THE SECOND-ORDER HEARING LAW (holds exactly)

Deform the listener along the dial: ψ_ε = ψ + εu with u in the θ-odd plane.
The mirror flips the odd part, and exactly (verified to 1e-15 for every weld
g ∈ {I, RL, RRLL}, every direction u ∈ {u₃, u₆, mixed}, every ε tested):

> **A_ε(g) = A₀(g) − ε² · (u† W(g) u), with NO first-order term,** and
> **A^twisted_ε − A^untwisted_ε = −2ε² · (u† M_odd(g) u).**

The O(ε) term vanishes by parity conservation (theorem); the ε² coefficient
is the open matrix's θ-odd block — the object whose sign the twist flips
(B592-OPEN). **The first closed chiral amplitude from the geometry:**

> at the object's own monodromy weld (g = RL):
> u₃† M_odd u₃ = **1/(2φ) + i·sin(2π/5)/√5** = +0.309017 + 0.425325i,
> u₆† M_odd u₆ = its complex conjugate —

nonzero imaginary part, golden-pentagonal exact values, the two θ-odd
directions hearing conjugate phases. At the bare weld (g = I) the quadratic
form is −1 (the odd metric): the displaced listener pays a real norm cost and
hears nothing chiral until a monodromy plays.

**The arc closes coherently:** vacuum deaf (X3) → bare states deaf (third
unhearability) → closed contractions deaf, the sign unsummable (fourth,
B592) → **hearable at second order by a listener who is themselves chirally
displaced.** The quadrature theorem (X2R) was the shadow of this law: the
chirality enters amplitudes quadratically because the first-order channel is
parity-forbidden. It takes a chiral ear to hear a chiral voice, and the
hearing is quadratic in how chiral the ear is.

## R4-B — the third entity is NOT a non-invertible knot's fundamental state (null)

The pipeline (re-validated on 4₁) computed J₃ of 8₁₇ — the first
non-invertible knot; braid word gated by the determinant identity
|V(−1)| = 37.0000 through the N = 2 layer — against its reverse (the reversed
braid word) and the index-flipped word:
> J₃(8₁₇) = J₃(reverse) = J₃(flip) = +0.673762079 (equal to 1e-15).
Banked null, consistent with the folklore that RT invariants do not detect
inversion: the C-symmetry wall extends past invertibility at this color and
root. The third-entity route stays closed at the fundamental-color level;
R4-A's dial-displaced listener is the constructive route, and it needs no
third entity.

## Reading (firewalled)

The measurement chain is now complete grammar: the object's chirality exists
(B575/B576/B582), is carried as a sign on the open θ-odd block (B592-OPEN),
is invisible to every undisplaced listener (three-plus-one unhearability
theorems), and is heard — with exact golden-pentagonal complex amplitudes —
by a listener displaced along the object's own chiral moduli, at second
order in the displacement. Measurement of chirality is not passive: the
observer must lean into the chiral direction to hear it, and what they hear
grows as the square of the lean. (Cf. the observer-coupling thesis; no SM
statement is made or implied.)

## Anchors

B592/B592-OPEN (the sign and the blocks), B575 (the dial directions are
honest moduli), X2R (the quadratic shadow), B584 (the antiphase channel),
B581 (the sign law's operator shape), the R-matrix pipeline (B592-C4).

## Verification addendum (owner: "u sure? verify first" — the adversarial pass)

- **V1 (the headline, EXACT):** the closed chiral amplitude coefficient was
  re-derived in exact symbolic arithmetic over ℚ(ζ₂₀) (sympy: the Kac–Peterson
  S-matrix built independently in exact cyclotomics, unitarity trace = 6
  exact):
  > u₃†(Cρ(RL))u₃ − [1/(2φ) + i·sin(2π/5)/√5] = **0** (symbolic zero).
  Two independent S-constructions (b238's numeric, the exact sympy one) agree.
- **V2 (the 8₁₇ identity, strengthened):** the braid closure pinned by the
  FULL Jones polynomial of 8₁₇ at two generic q (previously only the
  determinant 37) — exact coefficient-level match.
- **V3 (semantic self-consistency):** 8₁₇ is negative-amphichiral (mirror =
  reverse); the pipeline gives J₃ REAL and J₃(mirror word) = J₃(forward) —
  the triangle (mirror = reverse = forward at the invariant level) closes,
  consistent with reverse-blindness.
- **Caveat made explicit:** "reverse = the reversed-word closure" is the
  standard braid anti-involution lemma (cited, not re-proven here); V3's
  triangle supports it circumstantially. The R4-B null's wording depends on
  this lemma.

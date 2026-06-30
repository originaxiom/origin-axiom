# B307 — The generation count, closed: no hyperbolic knot has a C₃ trace field (the totally-real obstruction)

**Status: banked (frontier). A theorem + a census confirmation; nothing to `CLAIMS.md`.** From a Chat-2 handoff that
sharpened the generation conjecture and asked for the one decisive census scan (it lacked Sage). Run here — and the
answer is a **theorem**, cleaner than the conjectured "C₃ is rare."

## The path to it (Chat-2's sharpening, verified)
- The naive conjecture "3 generations need a degree-3 trace field" is **refuted by 5₂**: its trace field `x³−x²+1`
  has disc `−23` (not a square) → Galois group **S₃** → signature `(1,1)` → splits **1+2**, *the same structure as
  the figure-eight*. So a generic cubic still has a distinguished embedding. "Degree 3" is not enough. (Verified.)
- Sharpened: three *symmetric* generations would need a **cyclic-cubic (C₃)** trace field (three interchangeable
  embeddings, disc a perfect square). The target fields exist as number fields — `ℚ(ζ₇)⁺` (disc 49), `ℚ(ζ₉)⁺` (disc
  81), the conductor-13 field (disc 169) — all C₃, **all totally real (signature (3,0))**.

## The theorem (the decisive result)
> **No hyperbolic knot can have a cyclic-cubic (C₃) trace field.**

Proof: a C₃ field is **Galois**, so it has no order-2 automorphism, so no complex embedding → **C₃ cubics are totally
real**. But a hyperbolic 3-manifold's invariant trace field **always has a complex place** (the geometric rep is not
conjugate into `PSL(2,ℝ)`) → **not totally real**. The two are disjoint. ∎

**Census-confirmed:** of 500 cusped census manifolds, **32 have degree-3 trace fields; all 32 have signature `(1,1)`
= S₃; zero are cyclic (C₃).** So Chat-2's "outcome B" is **forced by the theorem**, not "empirically rare."

## The consequence (unifies B298 + B302)
A single hyperbolic knot's trace field carries `C₂` (the complex-conjugate pair) → matter multiplicities **1 or 2**
(B298), and a symmetric `C₃` triple (three *equal* generations) is **arithmetically impossible** for *any* single
hyperbolic knot. So **the single-knot trace-field route to three generations is closed for all hyperbolic knots** —
and three generations, if arithmetic, come **only from multiplicity**: the commensurator's hidden ℤ/3 (B302), which
is the arithmetic of the whole **commensurability class**, not a single object's trace field. This unifies B298 (the
figure-eight specifically) and B302 (the multiplicity route) into one theorem, and confirms B302 *from the arithmetic
side*: the generation ℤ/3 *must* be the hidden symmetry, because the trace-field route is provably closed.

## The corrected structural insight (sharper than Chat-2's "C₂-cheap / C₃-rare")
- **`C₂` (the complex-conjugate pair) is generic** for a hyperbolic knot — every such trace field has a complex
  place, giving the 1-or-2 structure. The figure-eight has it.
- **`C₃` (a symmetric triple) is not "rare" — it is impossible** for a hyperbolic knot (the totally-real
  obstruction). The "value-3 everywhere, multiplicity-3 nowhere" puzzle is resolved decisively: the figure-eight's
  *value*-3 (ramified prime, E₆-center, level k=3, trace 3) lives in a `C₂` field; a *multiplicity*-3 needs a
  symmetric triple, which **no** hyperbolic knot's trace field can be — so multiplicity-3 is not a single-object fact
  at all. (This *strengthens* Chat-2's framing: not "C₃ is special/rare," but "C₃ is forbidden, so the 3 must be
  relational" — exactly B302.)

## The fence
Pure arithmetic (the totally-real obstruction theorem) + a census confirmation. The "generations = trace-field
structure" reading is the firewalled physics dictionary; the *theorem* (C₃ impossible for hyperbolic) stands on its
own. The literature context (the knots-as-particles prior art, the Shape-Dynamics validation of the scale reframe) is
recorded firewalled in `speculations/S045`. Nothing to `CLAIMS.md`.

`totally_real_obstruction.py` (sage-python: 5₂, the C₃ fields, the census scan) · `verdict.py` (pyenv re-check) ·
`tests/test_b307_totally_real_obstruction.py`. Related: `B298` (the degree-2 obstruction — generalized here),
`B302` (the multiplicity / hidden-ℤ/3 route — now forced), `B305`/`B306` (the Eisenstein ω / trinification),
`S045` (the firewalled literature notes). Lit: Maclachlan–Reid (invariant trace fields have a complex place);
the knots-as-particles prior art (arXiv:1910.09966); Shape Dynamics (Barbour–Bertotti).

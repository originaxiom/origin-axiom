# B617 — the sign-law family theorem: the bundle sign law is pure parity

**Status: banked (frontier). Promotion candidate (with B613) at the next
review. Lock `tests/test_b617_sign_law.py` (fast). Run:
`python3 sign_law_theorem.py`.**

## THE THEOREM (one line, symbolic)

For ANY hyperbolic A ∈ SL(2,ℤ) with eigenvalue λ (|λ| > 1) and any
m ≥ 1, pairing the reduced-determinant factors k ↔ 2m−k gives
(1−x)(1−1/x) = −(√x − 1/√x)² < 0 per pair, hence

> **sign det′(I − Sym^{2m}(A)) = (−1)^m** — the sign law holds for EVERY
> object — and the closed form
> **τ_m(A) = (−1)^m ∏_{j=1}^m (λ^j − λ^{−j})²
>          = (−1)^m (tr²−4)^m ∏_{j=1}^m U_{j−1}(tr/2)².**

Verified: the pairing identity symbolically; closed = direct at all six
E₆ exponents for the fig-8 (tr 3), m136 (tr 4), and a tr-5 control; the
banked B423 (fig-8) and B616 (m136) values reproduced exactly; the
Fibonacci face τ_m = (−1)^m·5^m·(∏F_{2j})² for the fig-8.

## What it reframes

The BUNDLE-level sign law carries NO object information — it is pure
parity, a theorem of the whole family. Two consequences:
1. **The sharpened question (registered, open):** B581's EXTERIOR sign
   law (the Fox/Wada adjoint torsions at the discrete rep, same (−1)^m
   pattern) is now the genuinely informative one — universal like the
   bundle law, or figure-eight-specific? Decidable only by the m136
   exterior port (the designated heavy held-out arc).
2. **The conductor-unification candidate (exploratory, exact on two
   objects):** the closed form's base (λ − λ⁻¹)² = tr² − 4 is 5 for the
   fig-8 and 12 for m136 — the SAME constants that gate the two objects'
   hearing trace laws ([5|κ] for the fig-8; the disc-12 levels for
   m136). The object's torsion base and its stage conductor appear to be
   one number. Registered for a prereg'd test on a third object
   (tr 5 ⇒ base 21: prediction — its hearing trace law lives on
   disc-21-related levels).

## Quadrature note

Theorem 6.3 of PC26 (quadrature via the sign law) now rests on a family
theorem rather than a computed table at the bundle level; its
exterior-torsion face keeps its computed status.

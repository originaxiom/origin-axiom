# B423 (GATE B, computed) — the E₆ torsion is a Fibonacci-square product: rich structure,
# figure-eight-specific, but Fibonacci arithmetic (not SM) — 3 of 4 bars cleared

> **LABEL CORRECTION (2026-07-04, see CORRECTION.md + [[B425]]):** this computes the **dynamical
> zeta** det(I−Sym^{2m}(A)) with A = the *homological monodromy* (golden cat map), NOT "the torsion
> at the holonomy" the prereg claimed. The geometric torsion at ρ_geo is Eisenstein (adjoint −3,
> B425/V30/V31). The numbers below are correct as the **dynamical zeta**; read "torsion" as
> "dynamical zeta" throughout. The two are the object's two cornerstone-side torsions.

**Status: banked — a genuinely new result + the honest verdict. The owner's compute-don't-
argue distinction VINDICATED. Firewalled.**

## The computation (blind, exact, closed form)

Gate B's leading (regularized adjoint torsion) term, run for the first time:

    τ(E₆) = ∏_{i∈{1,4,5,7,8,11}} τ_{m_i},   τ_m = (−5)^m · (∏_{j=1}^m F_{2j})²
          [from det(I − Sym^{2m}A) with the invariant direction removed; identity
           2 − L_{4j} = −5·F_{2j}² — the H¹=1-per-exponent regularization, B347]

**Prime content: {2, 3, 5, 7, 11, 13, 17, 19, 29, 41, 47, 89, 199}** = exactly the primes
dividing F₂·F₄·…·F₂₂ (the Fibonacci APPARITION primes up to F₂₂). Rich, forced, exact.

## What this settles (the owner was right)

Every SYMMETRY test read the object as "golden = flat = prime 5." The COMPUTATION produces
thirteen forced primes the symmetry analysis could not see. **The wall was never purely a
symmetry wall.** Bars cleared: (i) forced ✓, (ii) unsought (computed blind) ✓, (iv)
control-distinctive ✓ — the SILVER monodromy control gives the PELL primes
{…,23,59,…} ≠ the figure-eight's {…,47,89,199,…}, so the spectrum is figure-eight-specific.

## The fourth bar (iii): NOT an SM structure — Fibonacci arithmetic

The forced spectrum is the Fibonacci law-of-apparition prime set — a theorem of analytic
number theory (Fibonacci entry points), NOT an SM invariant (not a gauge-rank pattern, not
the generation count, not an anomaly lattice). Bar (iii) fails. **Honest verdict: the
object's COMPUTATION produces rich, figure-eight-specific, forced structure — the Fibonacci
prime spectrum — and it is deep MATHEMATICS, not the Standard Model.** The wall now holds
from the computation side too, but for a deeper reason than "flat": the object computes
number theory (Fibonacci arithmetic of its E₆ torsion), not physics.

## Consequence
This is a NEW theorem (the closed-form regularized E₆ adjoint torsion of the figure-eight =
a Fibonacci-square product with the apparition-prime spectrum) — a real strengthening for
the papers (Gate B's leading term, computed, not argued). The full oscillatory state
integral's Hessian remains the specialist residual, but its leading term is now KNOWN and
is Fibonacci-golden. The methodological lesson is banked: symmetry-arguments can hide
structure that computation reveals — but here the revealed structure is still mathematics.

**Provenance.** gateB.py → gateB.json; locks tests/test_b423_gateB.py.

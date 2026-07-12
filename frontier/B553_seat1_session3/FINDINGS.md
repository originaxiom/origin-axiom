# B553 — Seat-1 Session-3 harvest: verified items + the Markoff-unicity deflation

Processes Seat-1's session-3 summary verify-don't-trust. Most of it corroborates
already-banked work (relations negative = B539/B541; dictionary φ-ladder = B542;
−4/j=2 = B534; promotion refuted = B550; ℤ/11 charge = B552; Markov=Fibonacci
Hamiltonian is KNOWN — K007/K010 κ=2+λ², Kohmoto–Kadanoff–Tang). New/actionable:

## Verified exact
- **Metallic torsion:** |det(A_m − I)| = m² for all m (tr A_m = m²+2, det 1 ⟹
  det(A_m−I) = 1−(m²+2)+1 = −m²). So the natural Weil level of member m is m²
  — composite for m≥2; only m=1 (figure-eight) has level 1. (Seat-1's "prime
  natural level" phrasing is off: 1 is a unit, not a prime.)
- **Odd-Fibonacci cluster:** the mutation gives F(2n−1) = 1,2,5,13,34,89,233,
  610,1597,4181,10946 — the Fibonacci-indexed Markoff numbers. ✓
- **2-cycle holonomy = 1 mod 11:** forced — the ℤ/11 charge space (B552) is
  1-dimensional at every node, so any node-preserving holonomy acts as a unit
  scalar on it; the charge does NOT couple to the double clock. Charge–clock
  decoupling confirmed structurally.

## Correction to Seat-1's own self-correction
Seat-1's "what I got wrong #3" claims the SL(5) character variety "has
dimension n−1 = 4." That is the RANK of SL(5), not the dimension. For the
once-punctured-torus fiber (π₁ = F₂), dim X(F₂, SL(n)) = n²−1 — the program's
banked trace-coordinate count (B66: 24 at SL(5), 35 at SL(6)). The original
"25 = n²" was the matrix size; the correction "4 = n−1" is the rank; the
operative dimension is **n²−1 = 24**. One wrong number replaced by another.

## THE MARKOFF-UNICITY FEASIBILITY ASSESSMENT (CORRECTED 2026-07-12)

**Correction to an earlier over-deflation in this file (caught by owner
challenge).** An earlier draft called the P4/Markoff connection "a shared
Cayley cubic coincidence, not a method bridge." **That was WRONG.**

The connection is DEEP and REAL: P4's object — the metallic once-punctured
torus character variety with its trace map — IS the Markoff cubic. The Fricke
identity tr[a,b] = x²+y²+z²−xyz−2, evaluated at κ = tr[a,b] = −2, gives exactly
x²+y²+z²−xyz = 0 (the Markov/Cayley cubic; integer points = Markoff triples),
and the trace map IS the Markoff (Vieta) mutation (Goldman 2003, Bowditch 1998).
P4 lives ON the Markoff surface — not near a look-alike of it.

**The correct distinction (statements, not objects):**
- P4 proves a POINTWISE uniqueness — the (1,2)/metallic critical pair uniquely
  closes the cusp. One distinguished point of the surface.
- Markoff Unicity (Frobenius 1913) is GLOBAL TREE RIGIDITY — every Markoff
  number is the max of a UNIQUE integer triple; a statement about the whole
  mutation tree. (Proved for prime-power: Aigner/Button/Zhang; Fibonacci/Pell:
  Baragar 1996; open in general.)

**Corrected verdict: OPEN, worth a real bounded assessment — NOT dismissable
and NOT claimable.** Seat-1's conditional framing ("uniqueness for metallic
points; unicity asks for ALL points; IF P4's technique extends → a major open
problem") was the honest one; the earlier dismissal here was the error. The
genuine feasibility question — does P4's cusp-closing / trace-map-fixed-point
argument bear on the GLOBAL tree rigidity, or only ever on distinguished
points? — is a specific, bounded thing worth actually assessing before either
claiming or dismissing. What remains true: "P4 IS a special case of Markoff
Unicity" as a flat statement is still inaccurate (pointwise ≠ global), so no
unicity claim ships without the extension actually being demonstrated.

## Seat-1's three proposed paper targets — honest reads

## Seat-1's three proposed paper targets — honest reads
- **Markoff-P4 extension:** OPEN (corrected — see above). The connection is real
  (P4's object IS the Markoff surface); extension from pointwise to global tree
  rigidity is an open feasibility question, not dismissable. Do not CLAIM unicity
  until the extension is demonstrated, but it is a legitimate bounded assessment.
- **Spectral bridge (character variety = Fibonacci Hamiltonian surface):**
  KNOWN (KKT 1983, Casdagli 1986, Roberts 1992; and banked here as
  κ=2+λ², K007/K010). Seat-1 concedes this. Not a contribution; cite.
- **Charge-transport lemma (B552):** possibly real, but "general theorem for
  any substitution" needs a symbolic-dynamics / K-theory lit check (Smith
  normal form of I−M and its transport is elementary; likely known). Gate
  before any novelty claim.

## Convention-dependent items (moot, per B536)
Entropy S=1.0620 and the exact Schmidt σᵢ²: these live on the same
convention-dependent operator lift that B536 already flagged (period-6 did not
reproduce under the natural lift; the natural lift gives S=0.5623, rank 2).
Computing exact σᵢ² of a convention-dependent object is not worth the effort
until the operator convention is pinned. No action.

Locks: tests/test_b553.py.

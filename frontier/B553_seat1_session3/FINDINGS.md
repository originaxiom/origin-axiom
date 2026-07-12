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

## THE MARKOFF-UNICITY FEASIBILITY ASSESSMENT (the deflation)

Seat-1 proposes P4 (metallic Markov uniqueness) as "a special case of the
Markoff Unicity Conjecture" and a paper target ("Proceedings AMS or higher if
unicity extends"). **Honest verdict: LOW feasibility — the connection is a
shared-surface coincidence, not a method bridge.** Steelman then check:

- *Steelman:* both live on a Cayley/Markov cubic; P4 proves a uniqueness; the
  metallic points ARE the Fibonacci-indexed Markoff triples; maybe the
  cusp-closing argument extends to all integer points.
- *Check (why it fails):* the two "uniquenesses" are DIFFERENT PROBLEM TYPES.
  Markoff Unicity (Frobenius 1913) is a DIOPHANTINE statement — every Markoff
  number is the max of a unique INTEGER triple of x²+y²+z²=3xyz (open; proved
  for prime-power by Aigner/Button/Zhang, for Fibonacci/Pell by Baragar 1996,
  by NUMBER-THEORETIC descent). P4 proves a DYNAMICAL/geometric statement —
  which Dehn filling closes the cusp on the SL(2,ℂ) CHARACTER VARIETY (the
  Fricke surface x²+y²+z²−xyz−2=κ over ℂ), via trace-map dynamics. P4's method
  is representation-theoretic (complex reps, cusp geometry); it says nothing
  about integer-triple uniqueness. The Cayley cubic appearing in both is not a
  bridge — it is the same normal form hosting two unrelated questions.
- *Verdict:* claiming P4 → Markoff Unicity would be an overclaim of exactly the
  kind the firewall exists to catch. Cite the shared-surface connection as a
  known fact (Fricke; Goldman); do NOT frame P4 as a route to the open problem
  unless someone exhibits an integer-triple uniqueness OUTPUT from the
  cusp-closing argument — which it structurally does not produce. NOT a paper
  target as stated.

## Seat-1's three proposed paper targets — honest reads
- **Markoff-P4 extension:** LOW (above). Not viable as "unicity contribution."
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

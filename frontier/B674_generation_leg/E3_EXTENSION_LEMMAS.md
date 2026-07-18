# E3 EXTENSION LEMMAS (proven on the main seat 2026-07-18; HELD in
# scratch until the W3 gate comparison runs — banked with that PR so
# the exclusion is not widened mid-gate)

L-A (algebraic-integer eigenvalues suffice): the coefficients of
Π_j (1 − λ_j q^{g_j})^{−m_j} are complete homogeneous symmetric
functions of the (repeated) eigenvalues — integer polynomials in the
λ_j. If every λ_j is an algebraic integer (roots of unity NOT
required), every coefficient is an algebraic integer; growing v₅
denominators are impossible. Witness: the φ-type operator
(eigenvalues φ, −1/φ — units of ℤ[φ]): 12/12 coefficients verified
algebraic-integer (monic integer minimal polynomials).

L-B (bounded denominators suffice): if a construction's coefficients
satisfy v₅(c_n) ≥ −k for a fixed k (bounded 5-denominators, e.g. a
fixed 5-power from structure constants), the banked targets force a
mismatch at every scale: their v₅ = −1, −12, −49, −99, −146 at
n = 1, 10, 40, 80, 119 is unbounded below, so for ANY k there is an
explicit witness n with v₅(target_n) < −k. Verified per-k witness
table (k = 0, 5, 50, 145).

Consequence: E3 widens from "finite-order operator" to "any fixed
operator whose construction yields algebraic-integer (L-A) or
bounded-5-denominator (L-B) coefficients" — killing φ-type fixed
operators and fixed cubic-structure-constant composites by the same
mechanism, IF the gate's agreed class list contains them as
conditional kills.

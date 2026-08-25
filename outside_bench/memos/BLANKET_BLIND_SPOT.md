# THE BLANKET'S BLIND SPOT IS THE BEAT'S BIT — QP-1 closes: the cusp's self-report is identically blind to exactly one interior bit, and that bit is the beat's mirror
## (outside bench, 2026-08-25; thirty-seventh memo; campaign cell C5 = QP-1, the Markov-blanket quartet's last open item; the preregistered SECOND branch realized, with the mechanism exact)

### The cell
QP-1 asked: does boundary (cusp) data determine the interior character-variety point?
Preregistered two-outcome: generically injective (the self-report faithful, exceptional
locus exact) — or blind (a hidden interior bit invisible to the cusp, "a surprise
worth its own hunt"). The second branch fired, and the hunt took one afternoon: the
hidden bit has a name, and the record already owned it.

### THE THEOREM (`certificates/c5_qp1.py`, exact, sympy over ℚ(m,s))
On the eigenvalue-Riley family A = [[m,1],[0,1/m]], B = [[m,0],[s,1/m]]:
1. **The rep variety is found, not assumed:** the relator entry factors into two
   s-quadratic candidates; only ONE kills the FULL relator (all four matrix entries) —
   φ(m,s) = m⁴s − m⁴ + m²s² − 3m²s + 3m² + s − 1 — and it reduces at m = 1 to the
   Riley quadratic s² − s + 1 (the parabolic fiber {q, q̄}). The other factor is a
   false component (relator fails off the (1,0) entry); the s = 0 locus is reducible.
   For every m the interior fiber over the meridian eigenvalue has exactly 2 points.
2. **The blindness is an identity, not a genericity failure:** reducing
   tr λ (λ = the banked longitude word) modulo φ leaves α(m) + β(m)·s with
   **β ≡ 0 identically** — the boundary character (tr μ, tr λ) takes the SAME value
   on both interior points over EVERY meridian eigenvalue. The cusp's self-report is
   1-bit blind, everywhere, exactly.
3. **The hidden bit, identified:** on the two fiber points the oriented longitude
   eigenvalues (computed on the meridian's common eigenvector; λ commutes with μ,
   verified) satisfy **L₁·L₂ = 1 with L₁ ≠ L₂** — the fiber swaps L ↔ 1/L with the
   meridian fixed; and over real m the two points are complex conjugates
   (discriminant < 0 at the sample; the m = 1 fiber is {q, q̄}).
4. **And the record already owns that operation:** λ ↦ λ⁻¹ with μ fixed is EXACTLY
   the beat's action on the cusp lattice (memo 31: Ω_cusp = diag(1,−1)); and complex
   conjugation is the beat's antiholomorphic half (memo 16). The fiber swap the
   boundary cannot see is the beat's mirror.

> **QP-1 CLOSED, second branch: the Markov blanket's self-report hides exactly one
> bit of the interior, identically — and it is the beat's bit, the same ℤ/2 that
> selects the spin structure. Oriented boundary data (m, L) does separate the fiber;
> what the character forgets is precisely the orientation of the beat's reflection.
> The quartet completes: QP-2 FLAT · QP-3 INTEGRATED · QP-4 NO-HATCH · QP-1
> ONE-BIT-BLIND, the bit named.**

### Why this is the good outcome
A faithful self-report would have been tidy; a blind one with an anonymous bit would
have been a debt. What the computation delivered is the third thing: an exact
identity (β ≡ 0) whose hidden degree of freedom is the object's own deepest banked
symmetry. The observer reading only the cusp's characters cannot tell the object from
its mirror — and everything the programme has built (spin selection, cusp reflection,
matter reality) says that bit is the one the object resolves internally via the beat.
Fact 4's synthesis sentence is labeled a READING; facts 1–3 are exact.

### Fences
Exact throughout; the blindness is proven on the geometric component of the
eigenvalue-Riley slice (the component carrying the discrete rep, found by the
full-relator test — not assumed); character-variety subtleties off this slice
(reducible locus, the false factor) are excluded by construction and shown. One
error caught in-session before any claim: the first draft took the PRODUCT of the
two candidate factors as "the curve" (caught by the preregistered degree gate; the
full-relator test then rejected the false component — filed as lane error #2).
Gate 5 untouched.

### Certificates
`certificates/c5_qp1.py`; output `outputs/c5_qp1_out.txt`. Deps: sympy only.

### One sentence for the ledger
The one thing the boundary cannot say about the inside is which mirror-half it is —
tr λ collapses identically across the fiber while the oriented eigenvalue splits it
as L versus 1/L — and the operation that exchanges those halves is the very beat the
object uses to choose its spin, so the blanket's only blind spot is the bit the
object keeps for itself.

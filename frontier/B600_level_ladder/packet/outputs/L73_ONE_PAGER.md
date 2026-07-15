# L73 — ABELIAN INVISIBILITY: the one-page proof

**Claim (the vein's anchor, made a theorem).** Let φ = A₁ = [[2,1],[1,1]] ∈ SL(2,ℤ) (the
object's monodromy). For every finite abelian group A on which SL(2,ℤ) acts through
SL(2, ℤ/exp A) in the standard way, φ has exactly one fixed point (the origin). Consequently,
in every abelian anyon theater (A, q) — a finite abelian group with a nondegenerate quadratic
form, i.e. a pointed modular category — the (anomaly-normalized) torus-bundle invariant of the
mapping torus of φ equals **+1**: the abelian theater sees no object at all.

## The two-line core

det(φ − I) = det [[1,1],[1,0]] = −1.

Hence φ − I ∈ GL₂(ℤ/N) for **every** N ≥ 2 (its determinant is a unit in every ℤ/N), so
(φ − I)x = 0 has only x = 0 on (ℤ/N)²; by CRT the same holds on any finite abelian A² —
Fix(φ) = {0}. ∎ (lemma)

## From the lemma to Z = +1

For a pointed modular category C(A, q) the modular data is the finite Weil representation:
T_a = e^{2πi(q(a) − c/24)} with e^{2πic/8} = |A|^{−1/2} Σ_a e^{2πi q(a)} (Gauss–Milgram),
S_{ab} = |A|^{−1/2} e^{−2πi b(a,b)}, b the polarization of q. The torus-bundle invariant of
the mapping torus of φ is Tr ρ(φ) (word T²ST in the locked convention). Writing the trace as
a character sum over A × A and summing the free character directions, every term cancels
except those supported on solutions of (φ − I)x = 0 — a finite-Heisenberg stationary-phase
identity that is exact (Deloup's torus-bundle formula; the mechanism behind the banked AP2
Gauss–Milgram theorem, B570). By the lemma the solution set is {0}: the sum collapses to the
vacuum term, whose anomaly-normalized value is +1 — independent of A, q, and the level. ∎

**Scope note (honest boundary).** The lemma is unconditional. The collapse step is the
standard abelian stationary-phase identity; this packet **locks it computationally** on the
cyclic family (ℤ/N, q(j) = cj²/N or cj²/2N, all nondegenerate c), N ≤ 40 — every theater
passing the modular gates gives Tr ρ(A₁) = +1 to 1e−10 (`p_proof_lock.py`) — and defers the
literature-exact Deloup citation formatting to the banking seat (the banked AP2 already
covers the 243-theater ground exactly).

## Why this matters for the ladder

- It explains AP2's "Z = +1 for ALL 243 abelian theaters" as a **one-line determinant fact**
  about the object, not a coincidence of the sweep: the object's monodromy is a *unit
  translation away from the identity* on every torsion lattice.
- It predicted (before Q1 ran — the vein's own note) the abelian null of the chord program.
- **It does NOT extend to nonabelian theaters as "Z ≡ 1":** this campaign's level-4
  computation gives Z = 0 exactly at E₆ level 4 (integer-cyclotomic certificate). The correct
  statement after this campaign: Z_k = +1 for k ≤ 3 and **0** at k = 4 — the E₆ theater's
  Z-ladder is {+1, +1, +1, 0, ?}. H133's "Z ≡ 1 at every level" is dead at its own gate; what
  replaces it is the sharper question of **which levels the theater sees the object at all**
  (residual hint: the exact zero has both parity sectors vanishing — a selection-rule-shaped
  fact, cf. B599's parity theorem, which forces zeros of odd contractions but does not force
  this one).

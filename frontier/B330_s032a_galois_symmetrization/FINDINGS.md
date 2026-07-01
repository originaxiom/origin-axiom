# B330 / S032-A — the no-forced-choice capstone, attacked via one Galois-symmetrization mechanism (conditional)

**Status: banked (frontier) as a CONDITIONAL structural result. Attacks gate A in-sandbox (compute-before-deferring).
Firewalled; nothing to `CLAIMS.md`.** Gate A asks whether *any* invariant of the single seed is (1) trace-map-invariant,
(2) discretely multivalued, (3) **unsymmetrizable** — a genuine forced choice the object itself makes. This probe folds
the three previously-sealed cases into one mechanism and stresses it against two fresh invariant classes.

## The unified mechanism
> **Lemma (elementary).** If a discrete invariant's value-set is a finite orbit of the object's arithmetic Galois group
> `G`, then its elementary symmetric functions lie in the fixed field (`ℚ` or the base) — i.e. the invariant is
> **symmetrizable**, hence **not** a forced choice. *A finite Galois orbit is always symmetrizable.*

The content of gate A is therefore not the lemma (which is trivial) but the **claim that every trace-map-invariant
discrete invariant of this object is a Galois orbit.** That claim is what B130/B314/B318 established case-by-case, and
what this probe stresses against new classes.

## Verified (the mechanism, on the object's two arithmetic ends + the fresh classes)
- **Trace ring (B130).** `κ = tr[A,B]` is a **continuous** coordinate (non-zero gradient) → fails clause (2)
  (not discretely multivalued) → cannot be a forced choice.
- **Quantum / golden end (B314).** The two values under `√5 → −√5` have symmetric functions `sum = 1`, `prod = −1`
  (rational) → **symmetrizable** (the golden pair `φ, φ′` has canonical symmetric data).
- **Eisenstein / CP end (B318).** The CP-sign pair `e^{±iπ/6}` swapped by `√−3 → −√−3` has `sum = √3`, `prod = 1`
  (real/canonical) → **symmetrizable** (the object gives the symmetric pair `√3`, not a signed member).
- **Cover-torsion (B326, fresh stress).** The deck `ℤ/3` on `H₁(3-fold cover) = (ℤ/4)²` acts with `det(C−I) ≡ 3 (mod 4)`
  (a unit) → `(C−I)` invertible → the **only** fixed vector is `0`. So there is **no canonical distinguished
  sub-object** for the object to "force"; the only canonical object is the whole (symmetric) module → **not a forced
  choice.** (The irreducibility that could have looked like rigidity is exactly what makes it maximally symmetric.)
- **Cohomology `H¹` (fresh stress).** `dim H¹(π₁(4₁); Ad ρ)` is a single integer (functorial, canonical; Fox calculus,
  B264) — not multivalued → no forced choice.

## Conclusion — CONDITIONAL (worded per the C-guardrail)
For the invariant classes examined — **trace ring / quantum-WRT / Eisenstein-CP / cover-torsion / cohomology H¹** —
every trace-map-invariant discrete invariant is either continuous, a **symmetrizable Galois orbit**, or a **canonical
object**: **no genuine forced choice exists among them.** This is a real consolidation (the three sealed cases + two new
ones under one mechanism), but it is **not** a proof over *all* invariant classes. Per the C-guardrail, *"no forced
choice reachable by these classes"* is **`open`**, not a proof of universal impossibility.

**Untested classes (the residual, named).** Reidemeister/​Ptolemy torsion of the character-variety components;
Chern–Simons / `η`-invariants; torsion of higher (`n>3`) cyclic and irregular covers; the `SL(n≥3)`/Falbel
gluing-variety invariants; Bloch-group / scissors-congruence classes. The general S032-A theorem stays **open** pending
these; the mechanism gives the candidate proof strategy (show each such class is a `G`-orbit).

## The firewall (held)
A structural (no-value) statement about the object's invariants; it *supports* the firewall (the object hands you
symmetric orbits, never a member — the CP sign is exactly a Galois pair the object does not resolve). Nothing to
`CLAIMS.md`; the result stays `open`/conditional, not promoted.

## The fence
Elementary Galois symmetrization (sympy exact) + the B326 deck-action stress test (invertibility mod 4). No physics
values. Nothing to `CLAIMS.md`.

`s032a_galois.py` (pyenv) · `tests/test_b330_s032a_galois_symmetrization.py`. Related: **B130** (`κ` continuous),
**B314** (golden Galois orbit), **B318** (Eisenstein amphichiral), **B326** (the cover-torsion), **OPEN_PROBLEMS.md**
gate A, **K020** (the structural theorem as a Galois theorem). Lit: standard Galois theory (symmetric functions of an
orbit lie in the fixed field).

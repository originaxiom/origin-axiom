# B1003 — the axiom prices ARE paid: five ROBUST, two FRAGILE — and B998 is corrected

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** MATHEMATICS + governance. Gate 5 untouched.
**Campaign Phase 1, item 2.**

**P0 — the quantifier:** computes over **the axiom chain's forks** — sibling objects obtained by
varying one axiom. Not a manifold.

---

## The correction to B998, which is mine

B998 found `THEOREM_LEDGER` citing `test_b749_genesis_forks.py` as the lock for C1–C4 while the file
tests only F4–F7 — **no F2, no F8.** That much is right and stands.

**But B998 wrote that F2 and F8 are *"the two prices that are the programme's own computations"* in a
way that reads as though the computations were missing. They are not.**

**B749 computed all seven forks** — `compute.py`, `output.txt` and a verdict in `RESULTS.json` for
each. **What was absent was any TEST asserting those verdicts**, so a regression in `RESULTS.json`
would have been silent. **The gap was in the locks, not the work.** Corrected here.

## What the two prices actually say

**F2 — A2's price (inexhaustibility). ROBUST.** The sibling family — det = +1, |tr| ≤ 2 monodromies
of the once-punctured torus — was measured **whole and symbolically**: Cayley–Hamilton over every
det = 1 trace in {−2..2} gives orders 3/4/6, infinite order at non-central tr = ±2, and
**max|eigenvalue| = 1 exactly ⟹ pseudo-Anosov count 0 for the entire family.** With the lemma
tr² − k² = 4 ⟹ periodic/rational-slope words force |tr| ≤ 2. **Hyperbolicity ruled out by three
independent routes** (Thurston pA = 0; 0/8 live SnapPy twister builds geometric; both positive
controls geometric).

> **Allowing periodicity does not merely degenerate — it loses the hyperbolic carrier entirely.
> A2 selects the destination.**

**And it was falsifiable:** *"FRAGILE would have been triggered by any of the 8 sibling builds
returning 'all tetrahedra positively oriented'; the two positive controls prove the instrument
returns exactly that signal on hyperbolic input."* **MB12 satisfied inside the arc.**

**F8 — A5's price (the geometric carrier). GEOMETRY-NECESSARY.** Sibling = the Fibonacci
substitution hull + its AF C\*-algebra. **Four redundancy witnesses, pre-registered before computing,
all fail exactly:**

| | witness | result |
|---|---|---|
| **W1** | trace-pairing field contains ℚ(√−3) | **x² + 3 is IRREDUCIBLE over ℚ(√5)** — with an instrument control that *does* split over ℚ(√−3) |
| **W2** | a gap label generates a field with ℚ(√−3) inside | gap labels in **ℤ[φ]**, real; freqs (φ−1, 2−φ) exact |
| **W3** | an order-endomorphism X with X² = −3 | cone preservation forces **End = ℤ[M] ≅ ℤ[φ]** |
| **W4** | 3-torsion / ℤ[ζ₃]-structure in K₀, K₁ or hull cohomology | absent |

**And the vacuity check is textbook:** *"with the order forgotten, [[0,1],[−3,0]] in M₂(ℤ) squares to
−3I, so W3 can in principle hold."* **They proved the criterion could fire before running it.**

> ### **The combinatorial carrier sees ONLY ℚ(√5). It cannot reach √−3 by any of four routes. ℚ(√−3) is bought at geometrization and nowhere earlier.**
>
> **That is the being/hearing split, and it is FORCED by the step into geometry.**

## The chain's real price, now stated

| verdict | forks |
|---|---|
| **ROBUST / GEOMETRY-NECESSARY** | **F2** (A2) · **F3** (the slope) · **F4** (the shadow rule) · **F7** (control) · **F8** (the carrier) |
| **FRAGILE** | **F5 — A6, orientation** · **F6 — A5b, the puncture** |

> **Five cheap axioms, TWO load-bearing ones: orientation and the puncture.**

P019's own rule: *"A fork that comes back FRAGILE does not break the chain; it prices it."* **So the
chain's price is exactly two axioms, and they are named.** F5's record even carries the identity
behind it — **M² = RL**, the golden matrix squared (B14) — so *"orientation = choosing the child of
the parent"* is a matrix fact, and the discarded child is **Gieseking**.

## The locks, written

`tests/test_b1003_f2_f8_locks.py` — five locks asserting: all seven forks carry a verdict; F2's
pA-count-0 and its falsifiability note; F8's four failing witnesses, the x²+3 irreducibility, the
ℤ[φ] order, and its satisfiability proof; that the two FRAGILE forks are exactly orientation and the
puncture; and that F5 records M² = RL.

---

**Verdict: the axiom prices are PAID and now LOCKED.** Phase 1 item 2 complete. **The chain costs two
axioms — orientation and the puncture — and both alternatives are named objects.**

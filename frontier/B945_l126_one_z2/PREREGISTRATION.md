# B945 PREREGISTRATION — L126: ONE ℤ/2 OR TWO? (sealed before compute)

**Date sealed:** 2026-08-07 · **Seat:** cc (banking) · **Lane:** MATHEMATICS.
Gate 5 untouched. **Register:** L126, opened by B944's sweep.

## The question

B717's capstone lists **TIME** and **CHIRALITY** as two separate closings, from two
separate arcs. But B716's probe 1 says the Anosov suspension has **no arrow because of
amphichiral time-reversal** — the same amphichirality that blocks handedness (B713).
B944 found the identification stated nowhere, and proved the **matrix level cannot decide
it** (both involutions admit conjugators of both determinants).

This cell asks it at the level B944 named — the **mapping-class / word level**, where
GHH's criterion lives (B136):

> **amphichiral ⟺ reverse(W) = swap_{L↔R}(W), cyclically.**

Define two involutions on cyclic LR-words:

- **ρ (reverse)** — word reversal. Geometrically: reversing the base S¹ of the
  fibration, i.e. **TIME REVERSAL** of the suspension flow.
- **σ (swap)** — R ↔ L. Geometrically: an orientation-reversing map of the **FIBER**,
  i.e. the **CHIRALITY / mirror** involution.

They generate a Klein group V = {1, ρ, σ, ρσ}. GHH says amphichirality is the
statement that **ρσ** fixes W. The question is what the object's **stabilizer in V**
actually is.

## The cells

**Cell 1 — the object.** Compute Stab_V(W) for W = RL (m004), on cyclic words.

**Cell 2 — the metallic family.** Same for W = R^m L^m, m = 1..8 — is the object's
answer generic to the family or special to m = 1?

**Cell 3 — the census.** All cyclic LR-words up to length 10: the distribution of
stabilizers, restricted to the amphichiral ones (those fixed by ρσ). This decides
whether the object's stabilizer is typical among amphichiral bundles or exceptional.

**Cell 4 — the matrix cross-check, and the identity that explains it.** Rᵀ = L, so
ρ = σ ∘ transpose as operations on words. Verify on the object that reverse(W) =
swap(Wᵀ), and that amphichirality is therefore equivalent to **W conjugate to Wᵀ**.
Report whether that equivalence is vacuous (every integer matrix is conjugate to its
transpose over a field — so the content, if any, must be integral/conjugacy-class level,
and this cell must say which).

## The two outcomes (fixed now)

- **OUTCOME LOCKED** — Stab_V(object) = {1, ρσ}: neither ρ nor σ fixes the object
  alone, only their product. Then **time-reversal and chirality are two distinct ℤ/2's
  that the object locks together on the diagonal**, and any closing that breaks the
  amphichiral symmetry breaks **both at once** — one input, two gaps closed. L126
  resolves as *not the same ℤ/2, but inseparable*, which is stronger than the naive
  identification and is what the physics reading needs.
- **OUTCOME INDEPENDENT** — Stab_V(object) = V (both ρ and σ fix it separately). Then
  the two ℤ/2's are **independent symmetries**, the object is invariant under each on
  its own, a closing may break one without the other, and **L126's unification FAILS**:
  TIME and CHIRALITY stay two separate closings exactly as B717 has them, and B944's
  suggested collapse must be withdrawn.

Two further stabilizers are logically possible ({1,ρ} or {1,σ} alone, or trivial). Any
of those means **the object is not amphichiral by the GHH criterion**, contradicting
banked fact — so their appearance is an INSTRUMENT FAILURE, to be reported as such and
not interpreted.

## The disclosed prior

**Split, and honestly so — I do not know.** The naive reading of GHH ("amphichiral =
fixed by the composite") suggests LOCKED, and that is the outcome the physics reading
wants, which is itself a reason for suspicion. But a scoping observation made **before**
this seal cuts the other way: the object's word RL has only **two** cyclic rotations,
{RL, LR}, and *both* ρ and σ send RL ↦ LR — so on this shortest word each may fix it
cyclically **on its own**, which would give INDEPENDENT. If that is what happens, the
honest reading is that **m004 is degenerate for this test** (its word is too short to
separate the involutions) and the question must move to the family — which is exactly
what cells 2 and 3 are for, and they are pre-committed here rather than added after
seeing cell 1.

**Weight: INDEPENDENT-at-the-object slightly favoured; LOCKED-in-the-family unknown.**
The convenient answer is LOCKED; it is therefore the one that must clear the higher bar.

## Files (after sealing)

`b945_cells.py` → `results.json`; `FINDINGS.md` verbatim against these criteria; locks in
`tests/test_b945_l126.py` (seal-integrity first).

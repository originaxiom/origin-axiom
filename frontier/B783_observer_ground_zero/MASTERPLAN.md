# B783: THE OBSERVER GROUND-ZERO — cc3 campaign masterplan

cc3 audit seat, 2026-07-24. Gate 5-Q.

## The question (one sentence)

When σ acts on the word and 'a' becomes 'ab', the pointer must choose:
follow the parent (a) or the child (b). That choice is NOT determined
by σ. It is the observer's choice. It is binary. It might be θ.

## The thesis under test

θ is the reading act — specifically, the parent/child tracking choice
that the substitution forces but does not resolve. This would explain:
- θ is geometric, not Galois (tracking is spatial, not arithmetic)
- θ is vacant in the correspondence table (precondition, not content)
- θ is trivial at SL(2) but non-trivial at SL(3) (tracking becomes
  visible only at higher descriptive resolution)
- The listener's clock lands in θ-odd (the clock is about the POINTER,
  not the WORD)

## The 5-step computation

### Step 1: DEFINE THE POINTER

A position n in the Fibonacci word F_k (the word after k applications
of σ). The pointer has a state: (position, reading direction).

### Step 2: DEFINE THE POINTER'S EVOLUTION UNDER σ

When σ stretches the word from F_k to F_{k+1}: each letter maps to its
image. The pointer at position n in F_k maps to position π(n) in F_{k+1}.
There are TWO natural maps:
- π_P (parent-tracking): when a→ab, follow the 'a' (left of pair)
- π_C (child-tracking): when a→ab, follow the 'b' (right of pair)
- When b→a: only one option (no choice needed)

The choice between π_P and π_C is the θ-bit.

### Step 3: COMPUTE THE POINTER'S TRAJECTORY

For each tracking choice (parent or child): compute the sequence
n₀, n₁, n₂, ... as k → ∞. Check:
- Does the trajectory have a period? A monodromy? A limit?
- Does n_{k+1}/n_k → φ? Does the normalized position n_k/|F_k| converge?
- Does the trajectory define a CLOCK through successive σ-applications?

### Step 4: CHECK THE SYMMETRY-BREAKING

The F₂³ = ⟨c, θ, γ₅⟩ acts on the closing torsor. The pointer's
trajectory breaks some subset of this symmetry. Test:
- Does word reversal swap parent↔child tracking? (If yes: tracking = θ)
- Does reading direction correspond to golden conjugation? (If yes:
  direction = γ₅)
- Does the level distinction (letter vs rule) correspond to complex
  conjugation? (If yes: level = c)

### Step 5: CHECK AGAINST C22

Does the pointer's full state (position, direction, tracking-choice)
have a F₂³-fixed point? C22 says no equivariant section exists.
- If no fixed point: co-emergence satisfies C22.
- If fixed point: co-emergence doesn't suffice.

## Preregistered prediction (proposal #16)

See PREREGISTRATION.md. Summary:
1. Parent/child tracking = θ
2. Reading direction = γ₅
3. Case level = c
4. No F₂³ fixed point → C22 satisfied
5. Co-emergence closes 2/3 or 3/3 bits

Track record: proposals #1–#15 scored 0 for 15.

## Connection to listener's clock

CC Wave 5: θ-odd block factors through SL(2, Z/3κ), monodromy order as
f(stage, level). If tracking = θ: the tracking-dependent trajectories
live in θ-odd. The pointer's trajectory through successive σ defines a
clock. That clock IS the listener's clock. It lives in θ-odd because it
is about the POINTER (θ-odd), not the WORD (θ-even).

## Workflow design

### Phase 1: FOUNDATION (parallel)

**Agent A1 — Tracking computation:** Write and run Python. Generate
Fibonacci words F_0–F_18. Define position maps. Compute parent and
child trajectories from several starting positions. Test the reversal
swap. Compute scaling ratios. Analyze letter-visit densities.

**Agent A2 — Torsor construction:** Read B766, B780, B769, K021, B749
from the repo. Construct the F₂³ torsor explicitly. Define c, θ, γ₅
actions on traces. Record the rank-onset discriminator.

### Phase 2: SYMMETRY TESTS (parallel, after Phase 1)

**Agent B1 — θ-test:** Does word reversal swap parent↔child tracking?
Is the swap clean or approximate? Key test of P16.1.

**Agent B2 — γ₅-test:** Does reading direction correspond to golden
conjugation? Do trajectories' position ratios involve φ↔φ̄? Key test
of P16.2.

**Agent B3 — c-test:** Does the level distinction (letter vs rule)
correspond to complex conjugation? Is there a clean mathematical
definition of "reading at rule level"? Key test of P16.3.

### Phase 3: VERDICT (parallel, after Phase 2)

**Agent C1 — Synthesis:** Grade proposal #16. Two-outcome verdict.
C22 test. Monodromy check. Negatives first.

**Agent C2 — Adversarial:** Try to REFUTE proposal #16. Alternative
assignments, level mismatches, overcounting, underdetermination.

## Dependency graph

```
A1, A2 ──→ B1, B2, B3 ──→ C1, C2
```

## Campaign statistics

8 agents across 3 phases. Two-outcome decisive test.

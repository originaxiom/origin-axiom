# B783: THE OBSERVER GROUND-ZERO — FINDINGS

cc3 audit seat, 2026-07-24. Gate 5-Q. Negatives first.

## Campaign: 7 agents, 3 phases, ~850s runtime

Preregistered prediction (proposal #16) tested against computation.
Fibonacci word tracking maps computed through F_18 (length 6765).
Reversal test: zero mismatches across all levels k=3..8 and all
starting positions.

---

## NEGATIVES FIRST

### 1. Proposal #16 scores 1/5. Cumulative: 1 for 20.

| prediction | statement | result |
|---|---|---|
| P16.1 | tracking = θ | **PASS** |
| P16.2 | direction = γ₅ | FAIL |
| P16.3 | level = c | FAIL |
| P16.4 | no F₂³ fixed point | FAIL |
| P16.5 | 2/3 bits closed | FAIL |

### 2. γ₅ is NOT reading direction — it is complement (a↔b swap)

Four tests fail decisively:
- Reversal preserves letter frequencies; γ₅ swaps them (d(a)=1/φ ↔ 1/φ²)
- The cutting-sequence decomposition proves γ₅ = reversal + complement
- Both reading directions see growth rate φ (not φ vs φ̄)
- K-theory positive cone is identical for both directions

γ₅'s combinatorial avatar is the COMPLEMENT operation: swap a↔b in the
word. This correctly implements φ → φ̄ on frequencies. But complement
is not a pointer state — it acts on the word's CONTENT, not on the
pointer's PARSING.

### 3. c has NO word-level counterpart

Three candidate formalizations of "level distinction" all fail:
- Block tracking collapses to θ (parent and child land in the same block)
- σ² tracking is a subsequence, not a Z/2 involution
- Meta-reading has no second word to scan

B749 F8 independently forbids it: Q(√-3) is born at hyperbolization.
The substitution rule is purely combinatorial.

### 4. The trajectory-level degeneracy

The two proposed independent binary choices (direction and tracking)
are INDISTINGUISHABLE at the trajectory level:

    parent(σ) = child(σ_mirror)     [exact, zero mismatches]
    child(σ) = parent(σ_mirror)     [exact, zero mismatches]

Switching reading direction has EXACTLY the same effect as switching
tracking choice. γ₅·θ is in the kernel of the trajectory representation.
The pointer has 1 observable binary DOF, not 3.

### 5. C22 is NOT satisfied by the pointer alone

Fixed subgroup under the pointer: ⟨γ₅, c⟩ = V₄ (4 of 8 elements fix
the pointer state). The pointer is rank-1 in a rank-3 torsor.

---

## THE POSITIVE

### 6. Tracking = θ: CONFIRMED (first structural verification)

σ_mirror = R·σ·R (the reversal-conjugated substitution) exactly swaps
parent-tracking and child-tracking. The mechanism:

    σ(a) = ab     → parent = LEFT = 'a', child = RIGHT = 'b'
    σ_mirror(a) = ba → parent = RIGHT = 'a', child = LEFT = 'b'

Position labels (left/right) are θ-INVARIANT.
Content labels (parent/child) are θ-SWAPPED.

The tracking choice is the ALIGNMENT between the observer's tracking
direction and the substitution's intrinsic writing direction. θ reverses
the substitution's direction, flipping this alignment.

Evidence:
- Perfect position-by-position swap at all levels k=3..8 (up to 34
  a-positions per level): zero mismatches
- Perfect multi-step trajectory match (12 steps, all 5 starting
  positions): parent(σ) = child(σ_mirror) for every trajectory
- Independent verification reproduces all results exactly
- Consistent with the torsor flip-table (θ flips T6 alone)
- Consistent with S1 rank-onset (θ trivial at SL(2), non-trivial at SL(3))

### 7. Parent-tracking from position 1 gives exact Fibonacci numbers

    k:   3   4   5   6   7   8   9  10  11  12  13  14  15
    pos: 1   2   3   5   8  13  21  34  55  89 144 233 377

The pointer IS the Fibonacci recurrence made visible.

---

## THE ADVERSARIAL VERDICT

Strongest attack: OVERCOUNTING (the pointer has 1 observable DOF, not 3).
Status: KILLED, not merely wounded. 3 of 7 attack vectors independently
kill the proposal. 1 vector is ANSWERED (the θ attack — tracking = θ
survives).

The θ result survives as a standalone lemma about the Fibonacci
substitution. It does not carry the proposal's structural claims.

---

## THE REVISED PICTURE

What the computation actually established:

| operation | torsor generator | level |
|---|---|---|
| parent/child tracking | θ (word reversal) | combinatorial |
| complement (a↔b swap) | γ₅ (golden conjugation) | combinatorial |
| chirality (ρ_geo vs ρ̄_geo) | c (complex conjugation) | geometric |

The pointer closes θ (1 bit). Complement closes γ₅ (1 bit, IF
observer-side — but complement acts on the word, not the pointer).
c requires geometry.

C22 status under revised picture:
- If all 3 closable (θ + γ₅ as complement + c as chirality): C22 satisfied
- If γ₅ is object-side (not closable by observer): 2 bits, C22 fails
- Current (pointer alone): 1 bit, C22 fails

---

## OPEN QUESTIONS FOR THE OBSERVER PROGRAM

1. **γ₅ slot:** Is complement observer-side (the observer relabels
   letters) or object-side (the word has intrinsic letter identity)?
   If observer-side: expand the pointer to include a complement bit.
   If object-side: the pointer cannot close it.

2. **c slot:** The geometric observer's state lives in Q(√-3).
   Identify the geometric counterpart of the combinatorial pointer —
   likely the chirality choice ρ_geo vs ρ̄_geo on the character variety.

3. **Trajectory degeneracy:** Direction and tracking are
   indistinguishable at the position level. Separating them requires
   SL(3)/Sym² observables (where θ first becomes non-trivial). Need
   the trace-map intertwining theorem: does the word-level σ_mirror
   map through the KKT recursion to the character-variety θ?

4. **The trace-map bridge (missing theorem):** The adversarial agent
   identifies this as the key gap: "tracking = θ at the word level"
   and "θ acting on the character variety" share a name but lack a
   demonstrated mathematical connection. The intertwining is the
   theorem to prove.

---

## SEAL

Algorithm: SHA-256 of this file's content excluding the SEAL section.

# B1481 — PREREGISTRATION: THE HAND IS A PHASE

**Sealed before `hand_phase.py` runs on anything but the word LR with its two signs (m004 and m003).** cc (main),
2026-10-07. L246 Phase 2, first cell (the plan the owner approved on 2026-10-04); after B1479 (the bit is the sign of
the word state) and B1480 (the class index does not follow the sign at own level).

**Why this cell.** The record's class index I = n(V) − n(V*) contains no spinors: it is blind to the spin structure by
construction, so it could not follow a bit that lives there (B1480). The quantity that sees the bit must be a spinor
quantity. The record has one that is spin-dependent and odd under orientation: B1475's D_s(t) = Im R₁^{(s)}(t), the odd
twisted Alexander function of the lift itself. R₁^{(s)}(t) is defined up to a real unit ±t^k, so

  **θ_s(t) = arg R₁^{(s)}(t) ∈ ℝ/πℤ**

is an invariant of (M, s). A mirror f gives θ_{f·s} = −θ_s; a mirror-invariant s has θ_s ∈ {0, π/2}.

## 0. Seen first

- `VERDICT topic-sweep /phase of the torsion|arg R|torsion.*phase|spin.dependent|orientation-odd/: 18 of 1353 arcs on main match (NEGATIVE 2, OPEN 6, PROVED 10)` — read at the level of the verdict lines: B1475 (D_s, "a continuous orientation-odd invariant of (M, s), nonzero on
  all seven … in √3·ℚ at t = 2"), B1471, B1476, B1477 are the arcs that bear on it; none takes the phase modulo π as the
  invariant, evaluates it at t = 1, or reads it on the word states.
- **Seen in data before this seal, all of it:** the two controls on this instrument — **+LR = m004: θ = 0 on both spin
  structures at t = 1, 2, 3, 0.6; −LR = m003: θ = +π/3 and −π/3 at t = 1 (to six digits), 0.3010π, 0.2561π, 0.3156π and
  their negatives at t = 2, 3, 0.6.** B1475's table for the family's seven (the phase not read there). Nothing else: no
  other word state has been run.
- **Literature:** that the phase of a complex torsion is governed by an η-invariant is the Cheeger–Müller circle of
  results, cited from memory and unread on this bench; **no cell rests on it** — the phase is computed.

## 1. The cell

`hand_phase.py all`: the 34 amphichiral words to length 12 of B1479's table with both signs (68 states), every spin
structure, θ_s at t = 2, 3, 0.6 and at t = 1 where the function is defined. States whose H₁ has rank above one are
reported, not folded.

## 2. Predictions

| | prediction | prior |
|---|---|---|
| **P1** | on every − state, no spin structure has θ ∈ {0, π/2} at t = 2, 3 or 0.6 | 90% (it is B1479's P3 with Theorem A, read on the torsion) |
| **P2** | on every − state the spin structures pair off with opposite phases at each of those t, none self-paired | 90% |
| **P3** | on every + state at least two spin structures have θ ∈ {0, π/2} | 85% |
| **P4** | **the hand is quantised at t = 1:** on every − state where it is defined, θ_s(1) is a multiple of π/24 | 30% — it is π/3 on the control, whose trace field is ℚ(√−3); other words have other fields and nothing I know forces a root of unity there |

**Kills.** P1/P2: a − state with a real or imaginary odd torsion, or an unpaired phase — then Theorem A's conclusion and
the torsion disagree and one of the instruments is wrong. P3: a + state with fewer than two special phases. P4: one −
state with a phase off the lattice — then the quantisation is m003's (its field's), not the sign's, and the page says so.

**Reading, whatever P4 does.** P1 and P2 holding: on the − states of the generated state space every spin structure
carries a non-trivial phase and its mirror partner the opposite one — **a hand the mirror exchanges rather than
preserves; choosing a spin structure is choosing a hand.** Stated, and not banked as physics: no sign is selected, no
count is derived, and a phase is not yet a physical observable.

## 3. Disclosed

Instrument (sha256, first 16): `hand_phase.py` f15c2591495c6a02; it reuses B1471's Wada function and B1475's character list through
B1477's module, unchanged. Numerical (HP holonomy; phases to 1e−8). The function at t = 1 may be undefined on some
lifts (a vanishing normaliser) — reported. The owner's rule of 2026-10-06: nothing cited is load-bearing.

## 4. Scope

Frame F-CI. Object: the 68 amphichiral word states to length 12 (X_gen, named as that set). Reach class. No physical
quantity. 0 of 19 before and after.

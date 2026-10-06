# B1481 — THE HAND IS A PHASE: on every amphichiral − word state to length 12 each spin structure carries a non-trivial phase of its odd torsion and its mirror partner the opposite one; on every + state at least two spin structures carry none; the quantisation seen on m003 is that member's, not the sign's

**Verdict: PROVED** for P1, P2 and P3 on the sealed range, with **P4 FAILED and reported as failed**. Scope: frame F-CI;
the 68 amphichiral word states to length 12 (X_gen, named as that set), 304 spin structures; reach class. A census
statement about a phase; it selects no sign, derives no count, and a phase is not yet a physical observable. cc (main),
2026-10-07. Sealed `00f2306d4` (sha256 1c39c831). L246 Phase 2, first cell. **0 of 19.**

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /phase of the torsion|arg R|torsion.*phase|spin.dependent|orientation-odd/` (quoted in the
preregistration) — B1475, B1471, B1476, B1477 bear on it; none takes the phase modulo π as the invariant, evaluates it at
t = 1, or reads it on the word states. Seen before the seal: the two controls only. **Literature:** the relation of a
complex torsion's phase to an η-invariant is cited from memory and unread; no cell rests on it.

## 1. The invariant

R₁^{(s)}(t), the twisted Alexander function of the lift ρ_s at Sym¹, is defined up to a real unit ±t^k. So
**θ_s(t) = arg R₁^{(s)}(t) ∈ ℝ/πℤ** is an invariant of (M, s). A mirror f gives θ_{f·s} = −θ_s; a mirror-invariant s has
θ_s ∈ {0, π/2}. It is a spinor quantity — it depends on the lift — which the record's class index is not (B1480).

## 2. Results (`verification/hand_phase.py` → `hand_phase.json`; 68 states, no errors)

| | sealed prediction | prior | result |
|---|---|---|---|
| **P1** | on every − state no spin structure has θ ∈ {0, π/2} at t = 2, 3, 0.6 | 90% | **HOLDS: 0 of 152 spin structures on 34 of 34 states**, at each t (and at t = 1) |
| **P2** | on every − state the spin structures pair off with opposite phases, none self-paired | 90% | **HOLDS: 34 of 34**, at each t (and at t = 1) |
| **P3** | on every + state at least two spin structures have θ ∈ {0, π/2} | 85% | **HOLDS: 34 of 34** — two of two on 20 states, four of eight on 13, eight of eight on one; the others pair off with opposite phases on all 34 |
| **P4** | the hand is quantised at t = 1 on − states: θ_s(1) ∈ (π/24)ℤ | 30% | **FAILS: 2 of 152** — only m003's ±π/3. The phases at t = 1 take 70 distinct values; the quantisation is m003's, not the sign's |

The phase is a function of t on every − spin structure (it differs between t = 2 and t = 3 on 152 of 152). On five lifts
of two + states the function is undefined at t = 1; reported.

**So, on the amphichiral word states to length 12:** with the sign − every spin structure has a hand — a phase that is
never 0 or π/2 — and the mirror carries it to the spin structure with the opposite phase; with the sign + at least two
spin structures have none. This is B1479's bit read on a spinor quantity: three instruments now agree on all 34 words
(the cusp's lattice and Theorem A; the Chern–Simons class; the torsion's phase).

**Not predicted, recorded, not claimed.** On −LLRR (the silver word, H₁ = ℤ/2 ⊕ ℤ/4 ⊕ ℤ) the eight phases at t = 1 are
±0.05703π shifted by multiples of π/4; on −LR (m003) they are ±π/3. The phases appear to carry each member's own number
field (quarter-turns for ℚ(i), sixth-turns for ℚ(√−3)). Post-hoc; a sealed question for another arc.

## 3. What it means, and what it does not

- **Stated:** on the − states of the generated state space, choosing a spin structure is choosing a hand, and the mirror
  exchanges the two choices. Parity there is not a symmetry of one configuration but a map between two. That is the
  structural shape of a parity-violating theory; nothing more is claimed.
- **Not derived:** which hand; any count of fermions; any coupling. The phase is a number attached to (M, s); a physical
  reading needs the step from it to a spectral asymmetry (L246 Phase 2's remaining cell, B279's link).
- **For FK4 (GENESIS v1.13):** the stake is now concrete on 34 words — if the principle generates the sign, it generates
  states on which every fermionic configuration is handed.

## 4. Disclosed

P1–P3 were expected from B1479 with Theorem A and are a confirmation on a second instrument rather than a discovery;
P4 was the open one and it failed. Numerical (HP holonomy; phases to 1e−8). The observation of §2's last paragraph is
post-hoc. The reading of §3 is a reading.

# B536 — Seat-1 Phase 2-3 verification (measurement architecture, level 15)

Processes the seat-1 "Measure the Architecture" handoff (2026-07-09, Phases 1-3)
under verify-don't-trust. Phase 1 items 1.1/1.2/1.3/1.5 were ALREADY PROVED by
B534 (dark hyperbola, power-set, asymptotic darkness, tower law). This probe
verifies the six Phase 2-3 findings. Conventions: theta lift (B358): W1 =
diag(zeta^{n(n-1)/2}), W2 = F W1^-1 F^-1, Par = F^2; evolution U = rho(A1) =
W1·W2 (A1 = T·L, rho(T) = W1, rho(L) = F rho(T)^-1 F^-1).

| # | Finding (seat-1) | Verdict |
|---|---|---|
| F1 | {Par,W1,W2} irreducible, 224 observables | **CONFIRMED** — commutant {W1,W2} = 4 (the 2+3+4+6 Weil sectors), adding Par → 1. Mechanism: the banked B358 Heisenberg twist (Par does not normalize the sector split in the theta lift). |
| F2 | period 6 | **NOT REPRODUCED** — under the natural lift the post-measurement state has period 20 up to phase (= the order of A1 in SL(2,ℤ/15)); ⟨Par⟩ sequence differs. Seat-1's operator construction was unspecified; period 6 is convention-dependent. UNVERIFIED-AS-STATED. |
| F3 | entanglement exactly conserved; S = 1.0620 | Conservation **CONFIRMED but TRIVIAL** (Q1): U = U3 ⊗ U5 exactly (CRT-local unitary; tensor residual 6e-15). The specific value 1.0620 NOT reproduced (natural lift gives S = 0.5623, Schmidt rank 2, not 3) — convention-dependent. |
| F4 | measurement eliminates darkness | **CONFIRMED but GENERIC** (Q3): every state tested (including basis states and random states) has 0/225 dark points. Not a special property of the post-measurement state; the architecture/state distinction stands, the "Big Bang" framing does not. |
| F5 | [W1,W2] has eigenvalues ±iφ | **CONFIRMED at level 15** (exact to 1e-9), and refined: ABSENT at level 5, whose commutator magnitudes are {√φ, 1/φ} — the ±iφ is a composite-level phenomenon, not a mod-5 one. |
| F6 | Par splits 8/7 = (2+1)⊗(3+2) | **CONFIRMED** (exact; trivial). |

**Answers to the handoff's five questions:** Q1 trivial-yes (tensor factorization
proven). Q2: the natural-lift period is 20; "6" needs seat-1's construction to be
specified before it can be assessed. Q3: generic. Q4: level-15 exact yes; not
level-5; literature status unassessed (flagged). Q5: moot under the natural lift
(S = 0.5623 = the rank-2 value −(3/4)ln(3/4)−(1/4)ln(1/4)).

The interpretive frame ("the Big Bang as first measurement") remains firewalled
speculation-room material; nothing here banks as physics. Locks: tests/test_b536.py.

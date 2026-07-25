# B787 — THE INTERACTION PROGRAMME (solo campaign masterplan)

**From:** Chat-1's INTERACTION_PROGRAMME_HANDOFF (2026-07-25). **Run by:** cc, solo, as a
multiagent workflow with adversarial cross-verification at every step. **Gate 5 + Gate 5-Q
binding. Nothing to CLAIMS. JUNO=0.30902 the one pin (no post-hoc registration).**

## The thesis under test

Values are not in the object (12 walls) nor the observer (pointer = 1 bit). Are they in the
INTERACTION (pointer touches letter; S-matrix connects observer-state to object-invariant;
Born rule makes a number)? Chat-1's record: **1-for-21, 48 errors, all caught by discipline.**
So the campaign's FIRST LAW is base-rate honesty — a clean recorded NEGATIVE is the deliverable;
a forced hit is the failure mode (error 48 = J₁₅ V₄ "hits" that were base-rate).

## The governing discipline (every door obeys)

1. **Prereg-seal two outcomes BEFORE compute** — what is a HIT, what is the base-rate MISS.
2. **Base-rate control on every numeric door** — the look-elsewhere budget (Chat-1: 6 ratios ×
   10 candidates × 6% window ⇒ ~3.6 expected by chance). A "hit" must clear that budget.
3. **Gate 5** — no SM value to CLAIMS. JUNO=0.30902=1/(φ√5)... NO: JUNO=0.30902 is the pin;
   |S_ττ|²=1/(φ√5)=0.27639 is a THEOREM (Fibonacci MTC Born prob) but ≠ JUNO. Do NOT force it.
4. **Gate 5-Q** — no consciousness claims (P021 phenomenology stays firewalled, priced at C18).
5. **Adversarial verify every door before banking** — a skeptic prompted to REFUTE; a door
   only banks HIT if the skeptic fails to refute AND it clears base-rate.

## The work (completion criteria, handoff Part 9)

### Phase 1 — the ι-identification (HIGHEST PRIORITY; gates the relabeling)
Which (ℤ/2)³ element is ι (inversion, w→w⁻¹)? Evaluate c, ι, θ, γ₅ on the SL(3) geometric rep
(B71/B99/B101 data). Extends B786 (θ=reversal trace-trivial; ι=inversion trace-active at SL(3)).
Two outcomes: ι ∈ {c, θ, γ₅, cθ, cγ₅, θγ₅, cθγ₅} identified exactly / ι is a NEW independent
generator (rank-4). Verified against the B766 torsor.

### Phase 2 — the six doors (independent; each compute → adversarial-verify)
| # | door | computation | HIT criterion (pre-stated) |
|---|---|---|---|
| D1 | Fox calculus bridge | Fox matrices ∂w/∂{a,b} of σ vs σ_mirror at an SL(3) rep; θ-type relation? | a computed θ-intertwiner in the group ring that is NOT a trace artifact |
| D2 | R-matrix braiding | Fib R=diag(e^{−4πi/5},e^{3πi/5}) on τ×τ; Born probs at each V₄ orientation | a Born number = JUNO (0.30902) clearing base-rate, OR an exact new invariant |
| D3 | 15A8 newform @ Fib | a_n of the weight-2 level-15 newform at n=1,2,3,5,8,13,21,34,55,89 | a closed form / recursion / periodicity in a_{F_n} beyond generic |
| D4 | E₆(78) under V₄ | 78 = ⊕ V₄-eigenspaces; torsion spectrum {U_m(3/2), m∈exps} sorted c/θ-parity | a forced parity assignment of the cascade (not base-rate) |
| D5 | state integral Z(u) | fig-8 DGG 1-dim integral at u=φ−1, ω₃−1, ζ₅−1, ζ₁₅−1 | a transcendental the algebraic specialisation misses, with structure |
| D6 | Habiro c_n @ Fib | c_n (integers to 150, B776) at Fibonacci indices | a growth law / recursion / r-stream link in c_{F_n} |

### Phase 3 — the ι-relabeling propagation (conditional on Phase 1)
If ι≠θ changes labels: sweep B759 (coupling norm √3), B769 (T1 triadic), Wave-5 (listener's
clock) — relabel "θ-odd → ι-odd" where the computed object is inversion, not reversal. Each
relabel is a computed check, not a text edit.

### Phase 4 — synthesis + completion + honest verdict
Per-door HIT/MISS (expect mostly MISS); the completion-criteria checklist; the honest final
state in one paragraph. What (if anything) survives base-rate + adversarial verify goes to
HINT_LEDGER only (never CLAIMS) unless it is a proven theorem.

## Out of scope (specialists / owner-gated — recorded, not run)
GSWZ send (owner-gated); the discrete Maass spectrum (EXTERNAL numerics); PC26 submission;
JUNO timestamp (owner-gated). These are Part-5 items; the campaign records their state, does
not execute them.

## Deliverables
- `PREREGISTRATION.md` (sealed, hash in ARTIFACT_HASHES.txt) — the two-outcome criteria above.
- One results.json per door + the ι-id + the synthesis, each with an adversarial-verify verdict.
- `FINDINGS.md` — the honest per-door table + the completion checklist.
- `tests/test_b787_interaction.py` — locks on whatever proves out (theorems + the ι-id).
- Ledgers updated; HINT_LEDGER for any base-rate survivors; nothing to CLAIMS.

## The workflow shape (multiagent loop)
`workflow_b787.js`: Phase-1 ι-id + Phase-2 six doors run as parallel compute→adversarial-verify
chains (pipeline, no barrier); Phase-3 relabeling gated on the ι-id result; Phase-4 a synthesis
agent + a completeness critic ("what door was under-computed, what claim unverified?"). Every
compute agent is prereg-bound and base-rate-disciplined; every result is adversarially verified
before it counts.

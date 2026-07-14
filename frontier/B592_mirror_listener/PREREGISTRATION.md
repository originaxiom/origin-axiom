# B592 — R3-M: THE MIRROR LISTENER (the cut-open trace) — prereg

**Date: 2026-07-14. Registered BEFORE the computation. Firewall: nothing to
CLAIMS.md; no SM quantities (the B580 binding rule).**

**Provenance note (honest):** the original `R3M_PREREG_FOR_CC.md` was authored
on the chat-1 seat and did not reach this filesystem; this prereg is the
faithful reconstruction from the owner's relay (2026-07-14), registered before
any computation. Where the relay is silent, choices are stated here and
frozen. Deviations from the original document, if any surface later, are to be
reconciled against this file.

## The measurement (from the relay, verbatim in structure)

**The cut-open trace of the θ-odd-twisted mirror-double.** Cut the mirror-
double open along the gluing torus: copy b's state enters as a COVECTOR
against copy a's state:

> A(g) = ⟨ψ_b | C ρ(g) | ψ_a⟩,

where |ψ_a⟩ = Σ_λ c_λ e_λ is the object's boundary state (c_λ = the λ-colored
invariant of 4₁ at the stage root), ⟨ψ_b| is the MIRROR copy's state as a
covector (orientation reversal: components conj(c_λ) on the conjugated labels),
C is the mirror twist, and g sweeps gluing words (frozen sweep: I, the
object's own monodromy word RL, and RRLL, RRL — the θ-odd-twisted dial family
on the stage).

**Decompose by θ-parity, channel by channel.** The channel amplitudes
a_λ = conj(c)_λ̄ · [C ρ(g) ψ_a]_λ, grouped into: the singlet channels (λ = λ̄),
and for each conjugate pair {λ, λ̄} the pair-symmetric (θ-even) and
pair-antisymmetric (θ-odd) combinations. **Read which channels carry the
imaginary part.**

## The stage (frozen choice)

SU(3)₂ (the golden stage; κ = 5): every ingredient is banked (B238 modular
data; B584 C; B245's validated colored invariants of 4₁ — J₃ = H^sym_[1],
J₆ = H^sym_[2] at A = q³, q = e^{iπ/5}; J₃̄ = J₃ and J₆̄ = J₆ by invertibility,
proven). The 8-channel (λ = (1,1), self-conjugate) is PURE θ-even and cannot
affect the verdict, which reads the θ-odd (pair-antisymmetric) channels; its
absolute value is a known method gap (no banked adjoint-colored formula) and
is reported as such. E₆₂ is out of reach for state components (R3-C) — the
relay's channel language is implemented on the golden stage where the pairs
are (3, 3̄) and (6, 6̄).

## The four controls (from the relay)

- **C1 — untwisted double:** drop C: A₀(g) = ⟨ψ_a|ρ(g)|ψ_a⟩-type pairing must
  be REAL (reality gate).
- **C2 — swap-symmetric gluing:** the swap-symmetrized amplitude
  ½(A(g) + A(g⁻¹-conjugate)) must be REAL.
- **C3 — level-1 rank:** the same measurement at SU(3)₁ (three primaries,
  pairs (3, 3̄)): the θ-odd channel must be DEAF (the level-1 rank theorem —
  fillings/states span θ-even only; B580-Q1R).
- **C4 — the 5₂ knot:** the non-amphichiral control. Its fundamental-channel
  state component J₃(5₂) is computed IN-SANDBOX by an independent
  U_q(sl₃) R-matrix braid computation (validated against B245's J₃(4₁)
  first); 5₂'s state components are non-real at the root, and its channel
  table is read the same way (the contrast is the control).

## The outcomes table (from the relay; frozen)

- **HEARD:** Im(A) ≠ 0 and the imaginary part sits in the θ-odd
  (pair-antisymmetric) channels only, with all four controls behaving
  (C1/C2 real; C3 deaf; C4 contrast). → The first chiral amplitude from the
  geometry: the mirror hears the object's chirality, channel by channel.
- **DEAF:** Im(A) = 0 in every channel for every g in the sweep — the
  **Θ-reality kill condition**: some antiunitary symmetry forces the
  cut-open pairing real; the mirror-double is self-deaf at the state level,
  and the verdict is banked with the same care (the silence would itself be
  a theorem-shaped fact, to be proven structurally afterward).
- **MIXED (registered for honesty):** Im appears in θ-even channels or
  controls fail → machinery error until proven otherwise; stop and diagnose.

## MB13

B584/B585/B586 (the listener machinery + the closed-trace results — this
cell is the OPEN-trace complement), B245/B240 (colored inputs), B582 (the
twisted double), B279 (invertibility), B580-Q1R (the level-1 rank control).
The closed traces heard −1/φ (all-θ-odd); nothing banked computes the
CUT-OPEN pairing — this is the new measurement.

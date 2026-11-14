# E21 — Self-evidencing closure (instantiates E18)

> **Phase C frontier probe.** Logged observation, not a claim
> (`../../GOVERNANCE.md` §5). See `../README.md` for ground rules.

This path quarantines an ambitious interpretive framing so its **exact algebra**
is kept and its **over-reach** is named, rather than letting the framing leak
into the standalone trace-map mathematics (PC12). It is a concrete instantiation
of **E18** (bootstrap / self-consistency selection), not a new mechanism class.

## The mechanism (as proposed)

Among the couplings of the metallic-mean substitution trace map, the value
`λ = m` (equivalently `I = m²/4`) is singled out because the linearized
half-return reproduces the characteristic polynomial of the substitution's own
generator `M`. Read as selection-by-self-consistency, this is the E18 idea: the
"self-evidencing" coupling is the one whose coarse-grained dynamics is
consistent with its own algebraic identity. An interpretive layer then maps the
discrepancy `D(I) = (4I − m²)²` onto a variational *free energy* (Friston's Free
Energy Principle) and lists spontaneous symmetry breaking, einselection, and an
"origin principle" as parallel framings.

## What is exact (verified — `probe.py`)

On the `SL(2)` Fricke–Vogt surface `I = c² − 1`, the half-return (third iterate)
of the Fibonacci trace map `T(x,y,z) = (2xy − z, x, y)`, restricted to the
surface at `(0,0,c)`, has characteristic polynomial `t² − (4c² − 2)t + 1`. This
equals `char(M²) = t² − (m² + 2)t + 1` exactly when `4c² − 2 = m² + 2`, i.e.
`I = m²/4`, i.e. `λ = m`. Verified for symbolic `m`. (The `SL(3)` exchange
structure around this point is locked separately in
`../../frontier/B54_general_c_exchange_structure/` and
`../../tests/test_general_c_exchange_structure.py`.)

## What is interpretation, not result

- The condition is the **single linear identity** `4c² − 2 = m² + 2`. The
  "self-model discrepancy" `D(I) = (4I − m²)²` is the squared residual of that
  identity; its unique zero at `I = m²/4` is immediate. The "action matching"
  `log ρ(J²) = 2 log φ_m` and the Fisher-information statements are the **same
  identity re-expressed** via eigenvalues — not independent results.
- The Friston free-energy mapping is a **structural analogy**: `D(I)` is a
  polynomial-coefficient residual, not a Kullback–Leibler divergence between
  distributions. The originating write-up concedes this ("we do not claim that
  `D(I)` is a free energy in any established sense").
- **No observable is predicted.** This matches the originating exploration's own
  physics-path-exhaustion conclusion.

## What would distinguish E21 from a relabeling

A genuine self-consistency/bootstrap result (E18) would need (a) a stochastic or
quantum framework in which `D(I)` is a *bona fide* free energy / surprise,
derived rather than assigned; and (b) an observable that the `λ = m` coupling
controls and that a non-self-evidencing coupling does not. Neither exists.

## Further controls (2026-06-02)

- **Fisher information = Weil–Petersson coefficient (exact, elementary).**
  `F(m) = 16/(m²(m²+4)) = 16/disc(char(M²)) = 16·g_WP(m²+2) = (4/Δ_eig)²`, with
  `g_WP(α)=1/(α²−4)` the Goldman/Weil–Petersson coefficient. Exact (verified), but
  it is the chain rule on `arccosh(2I+1)` plus `disc(t²−αt+1)=α²−4=1/g_WP(α)`. The
  session itself flags the geometric reading as possibly "just calculus" — recorded,
  **not promoted**.
- **Aubry self-duality at `λ=m` is dead.** `λ=m` is the trivial fixed point of the
  duality map `λ→m²/λ`, so "self-dual at `λ=m`" is vacuous; the off-diagonal model
  has no genuine Aubry self-duality at `λ=m` for `m≥2` (session IPR test). No
  metal–insulator observable. See `../../docs/atlas/FAILURE_ATLAS.md`.

## Relation to other probes

- `../../frontier/B52_multichannel_fibonacci_bridge_control/` — the naive
  multichannel physics bridge fails (`6×6` symplectic, not `SL(3)`).
- First-order `SL(3)` bridge: tautological — see `../../docs/atlas/FAILURE_ATLAS.md`.
- `../../frontier/B56_figure_eight_invariant_surface/` — the figure-eight does
  **not** lie on the `I=1/4` surface this framing centres on (diagonal reps at
  `I ∈ {4, −17/2 ± 7√5/2}`, none `= 1/4`); the `c=1` Eisenstein resemblance is a
  cyclotomic coincidence. A direct negative control on the self-evidencing bridge.
- `../../frontier/B54_general_c_exchange_structure/`, `B55`, `B51`, PC12 — the
  underlying trace-map algebra, kept as standalone mathematics.

## Verdict

`STALLED` — structural analogy only; predicts no observable. See `FINDINGS.md`.
Not promoted; not part of PC12; no Origin-core claim changes.

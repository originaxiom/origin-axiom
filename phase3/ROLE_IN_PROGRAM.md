# Phase 3 (Mechanism) – Role in the Origin Axiom Program

## 1. Scope and purpose

Phase 3, in its **mechanism incarnation** under `phase3/`, has a narrow,
structural role in the Origin Axiom program:

- It defines a **toy vacuum ensemble** with a global, phase-dependent
  amplitude observable \(A_0(\theta)\).
- It implements a **non-cancellation floor** \(\varepsilon_{\mathrm{floor}} > 0\)
  and the corresponding floor-enforced amplitude
  \[
    A(\theta) = \max\bigl(A_0(\theta), \varepsilon_{\mathrm{floor}}\bigr),
  \]
  using a quantile-based choice of \(\varepsilon_{\mathrm{floor}}\).
- It demonstrates the existence of a **genuine binding regime**, in which
  the floor is active on a non-zero fraction of the \(\theta\)-grid while
  leaving regions where the unconstrained dynamics are still visible.
- It provides **binding-style diagnostics** (mean shift, \(L^2\) distance,
  binding fraction, quantiles) showing that the floor has a quantitative,
  non-trivial effect on the observable while remaining numerically stable.

In other words, Phase 3 (mechanism) is a **worked example** of the Origin
Axiom acting on a global vacuum-like amplitude, with clean separation
between:

- the unconstrained observable \(A_0(\theta)\),
- the floor-enforced observable \(A(\theta)\), and
- the diagnostics needed for a Phase 0–style binding certificate.

## 2. Relationship to other phases

- **Phase 0** defines the contracts, falsifiability conditions, and the
  notion of a binding certificate and \(\theta\)-filters at the corridor /
  ledger level.
- **Phase 1–2** explore toy phasor / lattice / FRW constructions and
  corridor ideas, but with more entangled roles for the phase parameter
  and the non-cancellation machinery.
- **Phase 3 (mechanism)** sits below those as a **clean mechanism module**:
  it focuses only on “what it means” for a global amplitude to be subject
  to a non-cancellation floor and how to quantify a binding regime, without
  making contact with external data or cosmological observables.

At this stage, Phase 3 mechanism does **not** attempt to reconcile or
unify the various \(\theta\) roles used in earlier phases. It provides a
controlled sandbox that later phases (and the global program) can use
when designing a unified \(\theta\) story and cross-phase corridor logic.

## 3. Deliberate non-claims and deferred work

Phase 3 mechanism **does not** claim:

- that the toy vacuum ensemble is the real quantum vacuum;
- that the chosen \(\varepsilon_{\mathrm{floor}}\) has any direct
  physical interpretation;
- that Phase 3, by itself, defines a physical \(\theta\)-corridor or a
  canonical \(\theta_\star\);
- that the toy amplitudes match any observed vacuum energy scale or
  cosmological observable.

The following items are **explicitly deferred** to later work:

- Construction of a **full Phase 0–style binding certificate**, in which
  downstream observables are compared with and without the floor enforced.
- Design of a **Phase 3 \(\theta\)-filter artifact** consumable by the
  Phase 0 corridor ledger. Any future filter derived from this mechanism
  must clearly distinguish between:
  - purely **mechanism-level** admissible regions, and
  - **physics-level** constraints informed by external data.

Until such work is done, **Phase 3 mechanism is to be treated as a
mechanism module**, not as a standalone physical constraint on \(\theta\).

## 4. Archived flavor-based experiment

The earlier **flavor-calibration experiment** (CKM/PMNS-based ansatz and
empty-corridor result) has been archived under:

- `experiments/phase3_flavor_v1/`

That experiment remains reproducible and historically important, but it
is **not part of the canonical Phase 3 mechanism** and is not wired into
the Phase 0 ledger. Any future flavor-based work is expected to:

- treat `experiments/phase3_flavor_v1/` as a **negative-result prototype**,
  and
- build new flavor or data-driven constraints on top of a clearer global
  mechanism and \(\theta\)-unification story.

At the current rung, **Phase 3 (mechanism) is considered frozen**: its
role is to provide a clean, reproducible mechanism-level building block
for the broader Origin Axiom program, without over-claiming physical
content or prematurely fixing a \(\theta\)-corridor.

---

Doc status: Phase 3 role-in-program note; explains how the Phase 3 mechanism module fits between Phase 2 and Phase 4/5; descriptive but canonical for program narrative; see also `phase3/PHASE3_ALIGNMENT_v1.md` and `docs/PHASES.md`.

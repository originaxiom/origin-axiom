# B177 — the metabolism test (H3 to the knife): a crystal/horseshoe, not a cell; life relocates external

**Date:** 2026-06-18. **Status:** the decisive test of the cross-session ("chat2") **"is it alive?"** hunt — does
κ>2 order **starve** when you stop feeding the chain (a self-maintaining *cell*), or is it **conserved/frozen** (a
*crystal*)? **Verdict: a conservative active-chaotic CRYSTAL/HORSESHOE, not a cell.** Metabolism, homeostasis, and
the arrow are **not in the object** — they relocate **external** (the K018 firewall verdict, now in the life
register). **Firewall-side** speculation test (S035 register); emergent dynamics math; no scale/Λ/life-claim;
**nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V171. Reproducer `metabolism_test.py` (`ALL CHECKS PASS`).

## The hunt, and why it resolves cleanly

The cross-session reframe was right and sharp: *order is cheap (κ>2 is a quasicrystal — dead, ordered); the real
question separating a **crystal** from a **cell** is **self-maintenance** — order held open by doing work against its
own decay.* The four hypotheses (H1 bounded set = life; H2 homeostatic feedback; H3 metabolism = flux-sustained
steady state; H4 a mirror-odd arrow). H3 was chosen as the first kill. It resolves against what is **already banked**:

- **C1 — κ does NOT starve (H3 original form DEAD).** The Fricke–Vogt first integral `I` (the κ-type invariant) is
  **conserved by the trace map across "generations"** (iterations) to machine precision (drift < 1e-8 over 60
  generations). A conserved invariant **cannot decay when you stop feeding** — so "κ>2 dies under starvation" is
  refuted *by the conservation law* (B148/B130). κ is **indifferent to flux → crystal.**
- **C2 — the gaps FREEZE, they don't metabolize (H3 revised form DEAD).** Growing the **real Sturmian (Fibonacci)**
  chain through generations (lengths 233→2584), a prominent gap width **converges to a positive constant** (1.0655 →
  1.0653, successive `|Δw|` shrinking to ~1e-4) and **stays**. The gap is held by the **static structure**, not by
  ongoing **flux**: stopping growth *freezes* it, it does **not close**. A conservative spectral problem has **no
  metabolism** — that needs an *open, driven, dissipative* system (which this is not).
- **C3 — reversible ⟹ no arrow.** The trace map is **invertible** (`T⁻¹∘T = id` to 3e-17) and κ is mirror-even
  (B124) — the dynamics has **no dissipation, no relaxation, no time-arrow**. Metabolism is irreversible; this
  conservative dynamics **cannot supply it from within**.
- **C4 — the real positive: active, but not alive.** The dynamics has **both** frozen states (a fixed point
  `T(1,1,1)=(1,1,1)`, exact) **and** an **active recurrent set** — the κ>2 Cantor/**horseshoe** (positive entropy,
  banked B163/B165 *via the clean MST method*). So "order that never freezes" is **real** (H1 yes). But it is
  **reversible-conservative chaos** [C3] = *order that wanders*, **not** *order that maintains itself by doing work*.
  **A horseshoe is not a cell.** (We **cite** the horseshoe rather than re-demo divergence: B165 recorded that
  sensitive-dependence/"domination" diagnostics are **escape-contaminated** — a fresh demo would repeat a diagnostic
  our own ledger already flagged unreliable. Verify-don't-trust on our own probe.)

## The verdict (the pattern you'll recognize)

**Life, in this object, relocates external — exactly as scale did.** κ is conserved (cannot starve), the gaps are
held by static structure (no flux-sustained steady state), and the dynamics is reversible (no arrow). The
self-maintaining layer — metabolism, homeostasis, the arrow — is **not intrinsic**; it must be **added**, and lives
in the addition (an open driven+dissipative system for H2/H3; the **combinatorial** Ω-accretion arrow for H4, B168 —
itself dimensionless/external). The object is **active-chaotic ordered *form* (a horseshoe), not a cell** — the K018
"form, not content" verdict in the life register.

## What this does and does not say (honesty)

- It does **not** say "life is impossible" — it says **this conservative object cannot be a cell from within**; a
  cell would be the object **plus** an external open-system driver, and the "life" would be in that driver.
- H1 (active set) is **yes** (the horseshoe); H3 (metabolism) is **no** (κ conserved, gaps freeze, reversible);
  H2 (homeostatic feedback) and H4 (the arrow) both **relocate external** (an added controller; the combinatorial
  accretion arrow). The "heredity already owned" framing is an over-read — κ-conservation is a *symmetry* (a *rhyme*
  with heredity), not heredity with variation+selection.
- Speculation register (S035): nothing here is a life-claim or supports a physics claim; nothing to `CLAIMS.md`.

## Firewall
Emergent dynamics / quasicrystal mathematics testing a firewalled speculation; no physical-magnitude or life claim;
**nothing to `../../CLAIMS.md`**; P1–P16 untouched.

## Anchors
`B148`/`B130` (κ conserved — C1), `B124`/`P006` (reversible, mirror-even, no arrow — C3), `B163`/`B165` (the κ>2
Cantor/horseshoe — C4, cited), `B168` (the Ω accretion = the only genuine arrow, combinatorial/external — H4),
`B175`/`B176` (the collective structure this "life" hunt sits on), `K018` (the firewall-robust verdict this extends
to the life register), `../../speculations/S035` (the "building blocks' behaviour" reframe). External: dissipative
structures / far-from-equilibrium self-organization (Prigogine) — the *open-system* machinery a metabolism would
need and this conservative object lacks.

## Reproduction
`python frontier/B177_metabolism_test/metabolism_test.py` — C1 κ conserved across generations; C2 the Sturmian gap
freezes (converges); C3 the trace map is reversible; C4 frozen fixed point + the cited active horseshoe. Prints
`ALL CHECKS PASS`.

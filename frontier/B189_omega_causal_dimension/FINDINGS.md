# B189 — the Ω accretion causal-set dimension: a d≈4 that is a graded-DAG artifact (firewall holds by computation)

**Date:** 2026-06-22. **Status:** Masterplan III, **Track E** — the L21 firewalled hook. **Computed** the
Myrheim–Meyer ordering-fraction dimension of the Ω strict-full class DAG (B156/B159), *and hunted the artifact*.
**Result: the estimator gives `d_MM ≈ 3.94` for the full poset — but it is a generic graded-DAG / truncation
artifact, not an emergent spacetime dimension.** The firewall holds **by computation** — the single most
over-readable number the program could produce (a "4") is shown vacuous as physics, with a null control.
**Firewall-side:** combinatorial-only (`K010` boundary / the standing physics firewall); no scale/Λ; **nothing to
`../../CLAIMS.md`**; P1–P16 frozen. Ledger V184. Reproducer `omega_causal_dimension.py` (`ALL CHECKS PASS`).

## Method (verify-don't-trust the formula)

Rather than trust a remembered Myrheim–Meyer formula, the ordering-fraction estimator is **calibrated on Minkowski
causal-diamond sprinklings** (d=2,3,4) and shown to match the Meyer closed form
`f(d)=Γ(d+1)Γ(d/2)/(4Γ(3d/2))` to a few percent (**C0**) — so on a genuine Lorentzian sprinkling it *does* measure a
dimension. The Ω class DAG (N=474, L4–L10) is then turned into a poset by transitive closure of the accretion
edges, and its ordering fraction → `d_MM`.

## The result and the artifact-hunt

- **C1 — the raw number.** The full Ω class poset has ordering fraction `r ≈ 0.053` → `d_MM ≈ 3.94` (suspiciously
  close to 4).
- **C2 — it DRIFTS (no convergence).** `d_MM` rises monotonically with truncation level: `L≤6 → 2.08`, `L≤7 → 2.70`,
  `L≤8 → 3.28`, `L≤9 → 3.63`, `L≤10 → 3.94`. It does **not** stabilize — the value tracks the *number of layers*
  included. A real spacetime dimension would converge; a graded poset's "dimension" grows with its depth.
- **C3 — NULL CONTROL: a generic graded-DAG artifact.** A **random** graded DAG with the *same level sizes* and the
  *same consecutive-level edge counts* gives `d_MM = 3.79 ± 0.01` — **indistinguishable** from Ω's 3.94. So the
  value is **not special to Ω**; it is what *any* layered DAG of this shape yields.
- **C4 — FIREWALL (decisive).** The Myrheim–Meyer estimator assumes a Lorentzian **sprinkling**; the Ω cone is a
  **graded 7-layer DAG**, which violates that assumption. The `d≈4` is truncation-dependent (C2) **and** reproduced
  by a null (C3) — a **combinatorial artifact**, not a spacetime dimension. The L21 hook is **computed and closed as
  firewalled**: a graded DAG is not a causal set without a justified Lorentzian poset; signature/dimension here is
  algebraic-combinatorial, exactly as the standing firewall states (signature (1,3) = algebraic inertia, *not*
  spacetime). One-way hook only.

## Why this matters

This is the program's most dangerous number — a "4" emerging from the fundamental object — and the discipline is to
**hunt the artifact before reading it**. Computation shows it is vacuous as physics (drifts with depth, matched by a
null). So the L21 causal-set door is answered honestly: **no emergent spacetime dimension** — the apparent 4 is a
generic property of a layered DAG with these layer sizes, preempting any "Ω predicts 4D" over-read.

## Scope / honesty
- The estimator is calibrated and *correct on sprinklings* (where it means a dimension); applying it to the graded Ω
  poset is precisely the boundary-probe, with the truncation-drift + null-control showing the result is artifactual.
- Uses the class DAG (474 nodes); a history-multiplicity-weighted poset is a variant not run here (the
  truncation-drift + null already settle the firewall verdict).
- Combinatorial mathematics only; no physical-magnitude claim; nothing to `../../CLAIMS.md`; P1–P16 untouched.
  (The accretion-rate retention trend — B168 G2, "decreasing but decelerating" — is a separate banked B168 result,
  not re-litigated here.)

## Anchors
`docs/OPEN_LEADS.md` L21 (the firewalled hook this closes), `B159_omega_class_dag` (the class DAG + CSVs),
`B156_omega_strict_full_cone` (the L4–L10 counts, independently verified), `B168_omega_accretion_generative` (the
combinatorial arrow / rates), the standing physics firewall (signature/dimension = algebraic, not spacetime).
External: Myrheim (1978) / Meyer (1988) causal-set dimension; Bombelli–Lee–Meyer–Sorkin (causal sets); the
ordering fraction / Alexandrov interval; sprinkling = a Poisson process in Lorentzian spacetime (the assumption a
graded DAG violates).

## Reproduction
`python frontier/B189_omega_causal_dimension/omega_causal_dimension.py` — C0 the sprinkling calibration; C1 the raw
`d_MM≈3.94`; C2 the truncation drift; C3 the random graded-DAG null control; C4 the firewall verdict. Prints
`ALL CHECKS PASS`. Fast locks in `tests/test_b189_omega_causal_dimension.py` (2 tests, ~0.5s).

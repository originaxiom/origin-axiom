# B166 — SL(n) higher-rank aperiodic operators: non-Hermitian, one scale, structure open (P2b)

**Date:** 2026-06-18. **Status:** P2b of Masterplan II (lead L20). Pushes the metallic trace-map tower past SL(2)
to higher rank. **Honest outcome (as calibrated): a characterization + NEEDS-SPECIALIST.** SL(n≥3) is
**intrinsically non-Hermitian** (the symplectic obstruction, exact) and carries **one golden tower scale**, but
its spectral structure does **not** trivially inherit SL(2)'s Cantor set — the rigorous non-Hermitian
higher-rank theory is genuinely open. Standalone dynamics/spectral math; emergent/condensed-matter at most (not
fundamental); P1–P16 frozen; nothing to `../../CLAIMS.md`. Ledger V163. Reproducer `sln_aperiodic.py`.

## Results

- **Q0 [exact] — the symplectic obstruction (V29, re-derived).** A nondegenerate antisymmetric form on ℝⁿ exists
  iff `n` is **even**; for odd `n` every antisymmetric matrix is degenerate (`det = 0`, verified n=3,5). A
  self-adjoint 1D operator's transfer matrices preserve the **Wronskian symplectic form**, so they live in `Sp`,
  which equals `SL` only at `n=2`. Therefore **SL(n≥3) is not the transfer group of any self-adjoint (Hermitian /
  quantum) operator** — the higher-rank metallic system is **intrinsically non-Hermitian / classical**. The
  SL(2)↔Fibonacci-Hamiltonian quantum spectrum is an `n=2` coincidence (`Sp(2)=SL(2)`), not a tower feature.
- **Q1 [num, RECORDED NEGATIVE] — Cantor structure does not trivially transfer.** A naive SL(3,ℝ) metallic
  transfer cocycle (companion matrices, Fibonacci-ordered potential) shows **no clean SL(2)-style Cantor
  thinning**: the Fibonacci ~zero-Lyapunov fraction (`0.048, 0.055, 0.055` across depths) does **not** fall below
  the periodic-control band (`0.040`). So SL(2)'s zero-measure Cantor spectrum does **not** obviously extend to
  higher rank in this construction — the higher-rank non-Hermitian spectral structure is genuinely unclear
  (artifact of the naive cocycle, or a real difference — undecided here). *This is the NEEDS-SPECIALIST gap,
  recorded honestly rather than overclaimed.*
- **Q2 [cited] — the tower is one golden scale.** The SL(n) trace-map tower eigenvalues at the fixed point are
  `±φᵏ` (B107/B60) — a single golden scale (the band-center linearization), **not** a mass spectrum (B107's
  headline negative). So the higher-rank object inherits the same one-scale structure.

## Verdict

SL(n≥3) is a genuine **non-Hermitian** higher-rank aperiodic object [Q0] on one golden scale [Q2], but its
spectral set does **not** trivially inherit SL(2)'s Cantor structure [Q1]. The rigorous theory (Hausdorff
dimension, a non-Hermitian horseshoe, the actual spectral-set topology) is **NEEDS-SPECIALIST** — there is no
ground truth for non-Hermitian higher-rank cocycles (unlike the SL(2) Sturmian case, Damanik–Killip–Lenz). This
is the honest endpoint the plan predicted: a clean structural fact (non-Hermitian), a recorded negative (no
trivial Cantor transfer), and a specialist hand-off.

## Firewall
Emergent/condensed-matter mathematics at most (the K010 boundary), **not** fundamental physics; no scale, no Λ;
nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
V29 / `physics_probes/sln_multichannel_probe.py` (the symplectic obstruction this re-derives), B58–B66 / B60 / B61
/ B153 (the SL(n) tower; `sln_toolkit.py`), B107 (one golden scale, the headline negative), K007/K010 (the SL(2)
Sturmian framing — the ground truth that does *not* exist at higher rank), `OPEN_LEADS` L20. Ledger V163.
External: Damanik–Killip–Lenz (SL(2) Sturmian, the missing higher-rank ground truth); non-Hermitian topological
spectral theory (the specialist domain).

## Reproduction
`python frontier/B166_sln_aperiodic/sln_aperiodic.py` — Q0 (symplectic obstruction, exact), Q1 (the recorded
negative: no clean Cantor transfer), Q2 (one golden scale). Prints `ALL CHECKS PASS`.

# B381 (D2) — THE SEAM IS A TWIST INVARIANT: the twist isolated, the mechanism a commutant fact

**Status: banked (frontier) + P62 promoted at banking (exact: exhaustive finite search + one-line
commutant halves + the banked B358/P57 pillars as independent support). Campaign D2 COMPLETE.
Firewalled.**

## Q1 — the two lifts are inequivalent (the twist is structure, not convention)

Exhaustive search over the natural intertwiner family `U = Xᵐ·diag(ζ₁₅^{q·j(j−1)/2 + r·j})·P_σc`
(all m, q, r mod 15; all Galois relabels c) against all canonical targets (T-powers up to phase;
S-words): **NONE intertwines the theta lift into the canonical lift.** Pre-registered outcome
(b): the half-characteristic twist cannot be gauged away within the natural family — the
seam-bearing and seam-null models are genuinely different decorated quantizations of the same
cat map.

## Q2 — the mechanism, exact

- **The commutant fact:** Par commutes (up to phase) with the ENTIRE canonical image, and does
  NOT commute with the theta image. Hence in the canonical model the Par-inserted pair
  observable lies in the commutant and detects nothing — the banked B358 seam-null is a
  one-line corollary. In the theta model the gap between Par and the true parity J is exactly
  the elementary Weyl step (P57: `Par = J⁻¹·ζ₆⁻¹·XZ`).
- **The twist cocycle, exhibited:** `D_θ(j)/T_can(j) = ζ₁₅^{−j(j+1)/2}` exactly — the
  half-characteristic translate. This is the entire difference on the diagonal side; the
  S-side difference is the g(15)-normalization forced with it.

## The theorem (D2's deliverable)

> **seam ≠ 0 ⟺ the quantization carries the half-characteristic twist.** The twist is the
> explicit diagonal cocycle ζ₁₅^{−j(j+1)/2}; the seam values are the matrix elements of the
> Weyl step (XZ) that the twist exposes between the eigenframes (P60's reduction gives the
> per-cell form). Untwisted ⇒ Par central ⇒ seam identically zero; twisted ⇒ Par−J gap = XZ
> ⇒ the seam is the twist's fingerprint.

Combined with C6 (within the geometric premise the twist is FORCED) the chain closes: the
premise forces the twist, the twist forces the seam's existence, the eigenframes force its
support (P60), the Galois group forces its symmetries (P61) — the remaining freedom in the
rigid sector is the single normalization 1/12 (the named D3(b) residue).

**Provenance.** PREREGISTRATION.md (PR #475, first); B358/P19 (the canonical null), P56/P57
(the parity/Weyl structure), C6 (the forcing). Reproducer: `twist_isolation.py` (seconds);
locks: `tests/test_b381_twist.py`.

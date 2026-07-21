# FINDINGS — B745: the B742 revivals (B58, B225) cross-verified — CONFIRMED ×2

cc banking seat, 2026-07-21. Prereg SEALED before computation (hash in ARTIFACT_HASHES.txt);
number reserved pre-use (R27-4; reassigned from the second seat on its closure). The audit
seat's two revivals from the negatives hunt (B742) required an independent cross-verify before
correction headers could land on the original arcs — by the audit seat's own design. Gate 5:
pure algebra; nothing to CLAIMS; base-rate discipline applied to revivals exactly as to kills.

## Verdict: CONFIRMED ×2

Both protocol layers passed for both revivals:

1. **Re-execution layer** — the audit seat's `recompute.py` re-executed in THIS seat:
   B58 check-lines IDENTICAL to the banked output; B225 verdict-lines IDENTICAL.
2. **Independent layer** — five checks of my own (`crossverify.py`, none present in the audit
   seat's artifacts), all PASS:
   - **C1 (B58)** charpoly of B65's banked exact J(1) (the 15×15 symbolic SL(4) Jacobian,
     loaded from `jacobian_m.json`) equals char(A⁻¹)char(A)char(A²)char(A³)char(A⁴)char(−A²)
     (t−1)²(t+1) with A=[[1,1],[1,0]] the Fibonacci matrix — sympy-exact. Negative control:
     the same identity with the cat map [[2,1],[1,1]] fails, as it must (det +1 vs −1; the
     spectrum's ±φᵏ pairs force the Fibonacci convention).
   - **C2 (B58)** the sign-sector closure lemma: no positive-family char(Aᵏ) root (|k|≤12)
     nor ±1 lies within 1 of −φ² (margin 1.618…; monotone beyond the window) — so the
     computed −φ² eigenvalue is genuinely the char(−A²) sector, not a mismatched match.
   - **C3 (B58)** my OWN 8×8 Jacobian of the m=1 trace map, built from B48's declared
     convention (x1..x8, CH recurrences), at the fixed-line point c=3: charpoly ==
     (t−1)(t+1)(t²−3t+1)(t²+t−1)(t²−4t−1) — the exact SL(3) anchor, independently rebuilt.
   - **C4 (B225)** vacuity, empirically: 30 seeded random monic-in-z polynomials over ℤ[x] —
     disc_z mod 2 is a square in 𝔽₂[x] every time. The kill's criterion can never fail.
   - **C5 (B225)** the 11a3 control re-derived from scratch: Weierstrass Δ=−11 (odd ⇒ good
     reduction at 2) yet the branch-locus extraction reports 2 (lc=4). Independent false
     positive at 2 on a 2-good curve.

## Consequences applied (this arc)

- **Correction headers** on the original arcs (the B731 pattern — header-only, substrate
  untouched): `frontier/B58_sl4_tower_test/FINDINGS.md` (the headline "cannot be tested
  numerically" NEGATED; the necessary component — identity-rep first-order degeneracy —
  stands) and `frontier/B225_conductor_decomposition_test/FINDINGS.md` (the "2 = parent
  REFUTED" half retracted as vacuous; reopens OPEN; the golden "5 = filling" half stands).
- **B742 pending status resolved** (its FINDINGS "await cross-verify" line now points here).
- **Shortlist re-rank**: B58 reopens the SL(5)+ numerical tower door — the ε-extrapolated
  pinv route computes the ambient fixed-line Jacobian, so the tower prediction IS numerically
  testable; B225's octahedral-parent question returns to OPEN pending genuine
  (Jacobian-conductor) 2-parts.
- Lock: `tests/test_b745_revivals.py` (C1, C3, C4, C5; C2 is a one-line numeric bound
  inside C1's sector logic and locked via the script's exit status).

## Scope honesty

A CONFIRMED revival is not a new positive claim (E20 untriggered — no new structure asserted):
B58's residue is "the symbolic SL(4) task is OPEN with a working numerical route"; B225's
residue is "the decomposition's 2-half is UNDECIDED". The kills' necessary components stand.
One instrument lesson recorded: the C1 matrix-convention trap (det −1 Fibonacci vs det +1
cat map) — an identity check that silently "fails" under the wrong banked convention is a
convention probe, not a refutation; resolve conventions from the computed spectrum first.

Artifacts: `crossverify.py` + `output.txt` (ALL 5 PASS), prereg + hash. Reruns of the audit
seat's scripts left in `frontier/B742_negatives_hunt_p1/recompute/` untouched (their seals).

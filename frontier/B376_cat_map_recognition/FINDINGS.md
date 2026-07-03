# B376 (R1) — RECOGNITION HIT: the level tower is the quantized golden cat map

**Status: banked (frontier) + promoted at banking (P59 — the exact order identity, five levels,
machine-checked). PRIOR-ART GOVERNS THE FRAME: quantized cat maps are classical mathematics
(Hannay–Berry lineage) and their Hecke theory is Kurlberg–Rudnick's — nothing of that is claimed;
what is banked is the exact identification of OUR tower with that object and the resulting
derive-target. Nothing about the seam is derived yet — that is Phase 2's job, not this probe's.**

## The identity (exact, five levels, including the sector-less one)

    ord(W₁ @ level N) = ord(A₁ mod N) = π(N)/2        (π = the Pisano period)

verified at N = 15, 45, 75, 135, 225 (orders 20, 60, 100, 180, 300 — the last being the level
where the minimal sector does not exist). The previously banked "ord = 4N/3" was a coincidental
formula on the tested family; the Pisano identity is the structural one.

**Registered predictions (before computation):** ord(W₁) = 500, 540, 900 at N = 375, 405, 675.

## What this reframes

- **The phase-map riddle** (a(N) = 6, 6, 25, 54) becomes a question about the eigenvalue of the
  quantized cat map on its distinguished doublet — Kurlberg–Rudnick Hecke territory, where
  eigenspaces are governed by characters of (ℤ[φ]/N)^*.
- **The prime-power existence law** (sectors at m = 1, 3, 5, 9; none at m = 15) has a candidate
  mechanism: the splitting arithmetic of ℤ[φ] at the level (5 RAMIFIES in ℚ(√5), 3 is INERT) —
  the R2 obstruction cocycle at 225 should be computable as a character-alignment failure.
- **Phase 2's derive-don't-fit target is fixed:** derive the doublet's existence law, the exact
  a(N) values, and (the hard part) the seam tables C-5 from cat-map Hecke theory. A derivation
  reproducing the Constraint Document banks as the campaign's breakthrough; a failure banks as
  the sharpest possible boundary between our object and the known theory.

**Provenance.** docs/RECOGNITION.md (the campaign + R1 prereg), B372–B374 (the measured orders),
Hannay–Berry / Kurlberg–Rudnick (the frame — cited, not claimed). Reproducer:
`pisano_identity.py` (seconds); lock: `tests/test_b376_pisano.py`.

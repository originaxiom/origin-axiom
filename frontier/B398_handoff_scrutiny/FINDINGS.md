# B398 — S1–S4 BANKED: the handoff's math layer, verified item-by-item

**Status: S1–S4 complete; S5 (the binding statistics gate) next; S6 + decision memo after.
Prereg committed first. Firewalled — no physics wording in this file.**

## S1 (A1, the spectral theorem): FULLY VERIFIED + the fork pinned
- Both sector blocks exactly [[a,−a],[−a,a]], a = 1/48 ⇒ the σ = 1/24 doublet ✓.
- F₄-restricted Gram exactly [[49/115200, −13/57600],[·,·]] ⇒ eigenvalues
  {1/1536 = 75/115200, 23/115200}, **ratio 23/75 exact** ✓; ×480² integers: 98, −52 ✓.
- **The fork pinned:** 23/75 is the K2 ∈ {1,5}-restricted 2×2 Gram ratio; the banked FULL
  spectrum's rational pair gives 23/25. Both exact; the headline's provenance is now
  unambiguous (s1_s2.json).

## S2 (A3, cross-pair): verified with two corrections
- (2,3): the exact ℤ/3 point VERIFIED (norms 1/6912, inners −1/13824, all equal) — but
  **"ratio 1/3 EXACTLY" is a MISLABEL**: the three columns sum to zero (Gram kernel), and
  the full Gram's nonzero spectrum is an exact DOUBLET {1/4608 ×2} — ratio 1, not 1/3. The
  "TBM limit" reading is construction-inconsistent with (1,2)'s 23/75 (different objects).
- (3,4): **7/5 VERIFIED** — the full Gram's nonzero eigenvalues are exactly {7, 5}/2304.
- (2,4) rank 1 ✓; s-matrix ranks (1,2)=4, (2,3)=2, (3,4)=2, darks 0 ✓ (s1_s2.json,
  s2_fullgram.json).

## S3 (A2, tensor structure): pattern verified; headline NOT supported
- CRT fiber ranks exactly as claimed: (0,0),(2,2) → 1; (1,1),(1,3),(3,1),(3,3) → 2 ✓.
- **"Tensor rank EXACTLY 4": unsupported** — the matricization rank is 3; the s-matrix
  rank is 4 (a different object); no tested reading yields "tensor rank 4".
- Rectangle count 296/464 not reproduced (canonical CRT-class count: 168/265); the
  qualitative claim (the naive 2-factor split fails badly) HOLDS (s3_tensor.json).

## S4 (provenance): two anchors, one failed identification
- The 7: banked-exact — the void Jacobian's hyperbolic trace φ⁴ + φ⁻⁴ = 7 (B109); the
  handoff's "Eisenstein fixed point" label is imprecise; 49 = 7² has exact provenance in
  banked dynamics, attribution needs their code.
- **A6's "Weil(15) = σ ⊗ Weil(5)": the σ-identification FAILS the character check** — the
  3-local generator has traces (1, −1, 1, 3) with non-central square; the 2T adjoint
  requires −1 at order 4 and a trivial center. The CRT factorization itself is banked
  (P66); the adjoint bridge is not established. McKay graph of 2T = affine E₆: textbook ✓.
- A5 (1/48 Haar): recorded as an unforced face; the derived split remains 1/16 + 1/48
  (P64).

**Net effect on the physics layer (pre-S5):** the 23/75 headline stands on exact banked
data; the TBM-limit narrative and the McKay bridge — two of the three coherence arguments —
are weakened or unsupported; 6/11 and 23/1050 remain pattern-matched per the handoff's own
caveats. S5's pre-registered gate now decides.

**Provenance.** s1_s2_spectral.py, s3_tensor.py, the S4 inline checks → four JSONs; locks
tests/test_b398_handoff_scrutiny.py.

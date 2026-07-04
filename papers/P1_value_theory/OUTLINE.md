# PAPER 1 — The quantized golden cat map with a half-characteristic twist:
# exact value theory and class-field structure at level 15

**Status: outline (flagship campaign). Every theorem is banked + lock-backed. Phrasing
governor binding: novelty claimed only for the overlays + first-computed instances;
frameworks cited (Gelca–Uribe, Weil, Kurlberg–Rudnick, Hannay–Berry).**

## Abstract (draft)

We study the level-N Weil (theta) representation of the metaplectic double cover attached to
the golden cat map A = [[2,1],[1,1]] (the figure-eight monodromy), with a half-characteristic
twist, and its parity-inserted pair invariants ("the seam"). We prove: (i) the tower's order
law is the Pisano period (the tower IS the quantized golden cat map); (ii) an exact shifted
trace formula that localizes the twist to a single half-characteristic term and yields the
closed form of the sector constant 1/12 = 1/16 + 1/48 by det-class; (iii) an existence law
for the value sector, predictive at nine levels; (iv) that "brightness" is a local (CRT-
tensor) property; (v) a root-of-unity law with genus-character-gated torsion; and (vi) that
the entire value theory is organized by the class field theory of ℚ(√−15) (the seam field is
its Hilbert class field). All results are exact and machine-checked.

## The theorem list (precise statements, lock-backed)

| Thm | statement | lock |
|---|---|---|
| T1 (P59) | ord(W₁@N) = π(N)/2 (Pisano) — the tower is the quantized golden cat map | test_b376 |
| T2 (P62) | the seam is a twist invariant; canonical lift seam-null; twist = ζ₁₅^{−j(j+1)/2} | test_b381 |
| T3 (P63) | the existence law (line⊗doublet by prime-power parity + QR class); predictive 9/9 | test_b377_* |
| T4 (P64) | the shifted trace formula; twist = −½ω(v,(1,1)); 1/12 = 1/16+1/48 by det-class; universal (661/661) | test_b382, test_b396 |
| T5 (P65) | row-16 reality: t(16,b) ∈ ℚ(√5) ∀b; the ζ₅-spectrum mechanism | test_b383 |
| T6 (P66) | the CRT-local closed form: C = C₃·C₅; the 1/12 as a two-branch product | test_b386 |
| T7 (P67) | brightness is local (tensor-convolution); predictive out-of-sample | test_b390 |
| T8 (P68) | the root-of-unity law; χ₋₃(det)-gated 3-torsion (Eisenstein gate, derived) | test_b404 |
| T9 (P60/P61) | the rigid-sector reduction + Galois covariance (σ₃₁, mirror = τ₃) | test_b379/80 |
| T10 (W-C) | the class group of ℚ(√−15) acts on the value constants; genus selection rules | test_b401 |

## Section structure
1. Introduction: the object, the frame (Kurlberg–Rudnick / Hannay–Berry — cited), the twist
   (our addition). 2. The theta model + the twist (T2). 3. The tower order law (T1).
4. The shifted trace formula + the 1/12 (T4, T6). 5. The existence law (T3). 6. Locality +
   the root-of-unity law (T7, T8). 7. The class-field organization (T10, T5, T9). 8. The
   boundary theorems (the walls — scale/content, as structural results). 9. Methods
   (exact ℚ(ζ₆₀) engine, fp/CRT identification) + the reproducibility ledger.

## Novelty (governor): the seam object, the existence law, locality, the class-group action,
the root-of-unity gate = APPEARS-NOVEL overlays (needs-specialist). Gelca–Uribe cited as the
closest prior (abelian CS = Weil reps; our pair+twist extends it). Frameworks cited.

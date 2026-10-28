# B1793 — THE CURVATURE ROUTE FOR THE LEPTON FACTOR (P-397; DATA-FREE): IN B1656'S FRAME A ZERO-NET HYPERCHARGE CURVATURE ONLY RE-WEIGHTS THE FOUR CHANNEL NORMS, IDENTICALLY FOR DOWN QUARKS AND LEPTONS; REALISABLE PROFILES KEEP R₂ WITHIN 2% OF 1, AND THE JOINT (3, 3) IS NEVER REACHED — THE CURVATURE CANNOT SUPPLY c = 3; ONE-LEG ROUTES REMAIN

**Verdict: NEGATIVE as scoped.** Data-free. cc (main), 2026-10-28, main's plan step 2's route left (P-397, after B1789).
Corrected before landing at its hostile referee (§ 4). **0 of 19.**

## 1. The argument

- **The weight.** A sector's channel kernels K_s = P_s/R_s are sections of the pair's bundle L_x ⊗ L_y. A periodic
  curvature (potential φ, zero net degree) leaves every holomorphic datum unchanged: the sections, the residues R_s and the
  zero-mode count. It enters only the hermitian norm, weighting the channel-norm integrand by exp(−Qφ), where Q = q_L + q_R
  is the pair's total charge. That is +3 for down (1, 2) and for leptons (−3, 6), and −3 for up. The Higgs's −Q keeps the
  coupling gauge-invariant.
- **Stricter than the draft said (the referee):** the kernels themselves are identical for down quarks and leptons, to
  5 × 10⁻¹⁴ on four lines at two heights.
  - The fibre coordinate enters only through 3w; the individual charges sit only in the constant residues.
  - So any metric on the pair kernel re-weights the four channels identically in both sectors.
  - The lepton/down difference can only come from the residues, which the curvature does not touch.

## 2. Computed (`verification/curvature.py`, `curvature_b.py`; the referee's `verification/referee/`)

- **The weighted routine** is B1656's cA with the weight, the cusp's log term carrying W(0) (the referee's correction), run
  through B1726's pipeline (readings S, the Higgs DR). At ε = 0 it equals the instrument exactly.
- **On (2/5, 1/5), where B1742's identity is exact:** R₂ = R₁ = 1 to 10⁻¹⁰ for every profile, the asymmetric one
  included.
- **On (2/5, 1/10) and (2/5, 23/30), at gentle amplitudes:** R₂ stays within 1.5% of 1. R₁ moves by a few per cent (for
  example 1.2148 at ε = 0.2 against 1.2093).
- **Over every weight a curvature can realise** (the frame's own channel norms with positive bumps; 40 000 draws per
  cell): R₂ stays in 0.98–1.002, and never reaches [2.5, 3.5] (`referee/r3_free_lambda_run.txt`).
- **Arbitrary channel weights,** not shown to be realisable by any curvature, can push R₂ alone to 3 on some cells (median
  per-cell maximum 7.1 over 600 slope-2/5 cells). R₂ and R₁ are never both ≥ 2.5: the best joint distance to (3, 3) is
  2.85, with one channel switched off (`referee/r4_band_joint_run.txt`).

## 3. What it means

**The curvature route cannot supply the lepton factor.**
- It sees only the pair's total charge, which down quarks and leptons share.
- Realisable profiles keep R₂ at 1.
- Georgi–Jarlskog's (3, 3) is not reached even by unconstrained weights.

**What remains (the referee's list; P-397):**
- a 24-type vev;
- a charged insertion on one leg;
- a separate metric per field;
- another U(1) (B − L sums to 0 on both pairs);
- a curvature that flips sign under the shift by τ (a double-cover picture, outside the frame; it would see q_L − q_R:
  −1 against −9).

Each fields' own fibre norm sees q_L and q_R separately. It cancels here only because B1653's generations are images of one
doublet value at the puncture.

**No input removed. 0 of 19.**

## 4. The referee (hostile, read-only; `audit/referee_s230_p397/`, kept in `verification/referee/`)

1. **BLOCKING, applied:** the draft's headline ("cannot give c", differences "from the kernels' different shapes") was
   false as worded. The kernels are identical; arbitrary weights can reach R₂ = 3 alone. The verdict is now scoped to
   realisable profiles and the joint (3, 3).
2. **CORRECTION, applied:** the cusp's log term must carry W(0). Without it the result changes under φ → φ + const, which
   is only a rescale. Both scripts were rerun.
3. **NOTE:** an independent reproduction with Duffy quadrature agrees to 10⁻¹⁰.
4. **NOTE:** the sign and 2π conventions only rescale ε. The double-cover curvature is outside the frame.
5. **CORRECTION, applied:** each field's own norm, and why it cancels (B1653).
6. **NOTE:** Im τ 6 lies outside B1667's L column; L is clamped there.
7. **NOT COVERED:** the one-leg routes listed in § 3.

## Seen first

`VERDICT topic-sweep /lepton factor|Georgi|Jarlskog|Clebsch|c = 3|factor 3|flux|hypercharge flux|P-294/ (full text): 82 of 1535 arcs on main match (NEGATIVE 24, PROVED 58); 29 register rows match (DONE 15, QUEUED 14)` (B1789's sweep; since then, B1789 and P-397).

**Literature:** arXiv:1211.6529 (the hypercharge flux's effect on wavefunctions, with a fitted flux ratio). Winkelmann,
Mém. SMF 72–73 (1998), Thm 8.13.1: on compact quotients of semisimple groups every holomorphic bundle has c₁ = 0 (P-401).

## Files

- `verification/curvature.py` → `curvature.json`, `curvature_run.txt`.
- `verification/curvature_b.py` → `curvature_b.json`, `curvature_b_run.txt`.
- `verification/referee/` (r0–r4 and ref_lib).

The lock: `tests/test_b1793_the_curvature_route_for_the_lepton_factor.py`.

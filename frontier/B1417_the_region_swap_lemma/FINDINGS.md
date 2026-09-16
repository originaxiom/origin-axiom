# B1417 — THE REGION-SWAP LEMMA (fc R71 §2) VERIFIED ON MAIN: for any θ-odd field on the cusp torus with a transverse zero set, χ(∂⁺M) = χ(∂⁻M) = 0 whichever Fourier mode leads; the SM seat's "±4" is a non-transverse zero set, where χ is undefined, not non-zero — the last claim-level gap of the fc census closed, the fc harvest complete

**Date:** 2026-09-16 · **Seat:** cc (main) · **Lane:** HARVEST (MASTERPLAN v3.1 §1a). **Source:** the physics seat (fc), `reports/fresh_physics_seat_2026-09-01/R71_THE_SEATS_ON_THE_CUSP.md` §2 at the frozen tip **659487bb** (worktree `<audit>/wt-fc`). **Verdict:** VERIFIED (a two-line theorem, checked by own code). Nothing promotes; Gate 5 untouched.

## 1. The lemma
Let σ be an involution of T² and g a σ-odd field (g∘σ = −g) whose zero set Z is a closed 1-manifold. Then σ maps {g > 0} onto {g < 0}, so χ({g > 0}) = χ({g < 0}); and by additivity of the compactly supported Euler characteristic over T² = {g > 0} ⊔ Z ⊔ {g < 0}, χ({g > 0}) + χ({g < 0}) = χ(T²) − χ(Z) = 0. **Hence χ(∂⁺M) = 0 for every θ-odd field with transverse zeros.** No statement about which mode leads enters. On m004 the involution is θ: z ↦ −z on the cusp torus (fc R62/R71's table of the eight isometries, reproduced in B1298's re-run), with four fixed points — the corners — on which every θ-odd field vanishes.

## 2. Verified here (`verification/region_swap.py`, own code)
- 60 random rotation-odd trigonometric fields (modes (k, l) ≤ (6, 3)) on a 480 × 480 grid, χ of the superlevel set by the cubical count V − E + F: **(χ(g > 0), χ(g < 0)) = (0, 0) every time.** The space sampled is larger than fc's "allowed" subspace (which also fixes parities under the other seven maps), so the check covers fc's case a fortiori.
- **The SM seat's caveat:** the exact product mode sin(4πx)·cos(2πy) has a zero set with eight crossings; the cubical count of the open rectangles gives +4 on each side (fc's grid, counting closures, gives −4) — with crossings ∂⁺M is not a surface and χ(∂⁺M) is not defined. Adding 0.05 of a generic odd mode (sin 2π(x + y), or sin 2π(2x + 3y)) resolves the crossings: **0 and 0.** The SM seat's leading mode sin(4πx) alone: 0 and 0 (two annuli each side).
- Contrast, recorded because it is the trap: for a *reflection* (x, y) ↦ (−x, y) — not the object's θ — odd fields vanish identically on the two fixed circles, the zero set generically has crossings there, the hypothesis fails and the cubical count wanders (2 … 6). The lemma needs transverse zeros; it does not need a fixed-point-free σ.
- fc's own grid test was re-run on main in B1298 (`fc_r71_seats_on_the_cusp_rerun.txt` §(d): six random allowed fields, 0/0; the product mode −4/−4; with subleading modes 0/0).

## 3. Where it lands
Addendum on B1291 (THE PARITY THEOREM), whose "net chirality = −χ(∂⁺M) = 0 survives the move" is exactly this lemma's consequence; B1290's "annular ⇒ zero" is the same theorem from the index side; B1296 already credits R71 §3. Harvest row 631. The fc census is now fully harvested (R01–R72 rowed, backlog 0, relays 0/4 unrowed): the retirement gate is met; archiving the branch awaits the owner's word (`docs/SEAT_REGISTER.md`).

## 4. What is NOT claimed
Nothing about the localised count on several cusps (B1321, B1333); nothing about the physics of the field g (a b₁-class dual to the meridian in fc's reading); no value.

## Reproduce
`verification/region_swap.py` (its `.out`) · lock `tests/test_b1417_region_swap.py`.

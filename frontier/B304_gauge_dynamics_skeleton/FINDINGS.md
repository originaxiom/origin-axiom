# B304 — The gauge-dynamics skeleton + the two peer handoffs assessed

**Status: banked (frontier). Verifications + one refutation + one firewalled consolidation; nothing to `CLAIMS.md`.**
Two web-Opus seats pushed fresh-eyes on the SM-from-axiom bottleneck. Assessed verify-don't-trust. The genuine
finding: our structural theorem (the object forces dimensionless structure) **reaches into gauge *dynamics*** — the
RG running and `sin²θ_W` are forced, not just the gauge group + reps.

## Verified, forced — but generic-GUT (the same tier as B299/B301)
1. **`sin²θ_W = Tr(T₃²)/Tr(Q²) = 2/(16/3) = 3/8`** at unification (Georgi–Glashow), over one SM generation.
   **Generation-independent** — so it **routes around the degree-2 generation wall** (B298). But it holds for *any*
   GUT with the SM in a complete multiplet (SU(5), SO(10), E₆), so it is **forced via E₆⊃SM, not object-specific.**
2. **One-loop β-signs from one 27**: SU(3), SU(2) **asymptotically free**, U(1) grows — the unification direction.
   The dynamical reason a GUT is *possible*, forced by the matter content (no generation count needed). Generic-GUT.

This is a real **extension of what we said was forced** — from kinematics (group, reps) into *dynamics* (the running).
Chat-2's "bypass" (ask for dimensionless ratios/flows, not dimensionful couplings) is our structural theorem applied
to gauge dynamics, and it works. The tier is generic-GUT; the object-specific atom is still the arithmetic.

## Verified, object-relevant (the gem)
3. The number of E₆ adjoint weights (principal `sl₂` grading, exponents `{1,4,5,7,8,11}`, B264) with **`j ≡ 0 mod 3`
   is exactly `24 = |2T|`** (binary tetrahedral group order). Per-exponent `{1:1, 4:3, 5:3, 7:5, 8:5, 11:7}`. This
   ties the E₆ **principal grading mod 3** to the **McKay group of E₆** (B266: `ℚ(√−3) → 3 → 2T → McKay-E₆`) — the
   `mod 3` is the Eisenstein-3 of the figure-eight's own field. A genuine object-relevant connection.

## Refuted (a clean verify-don't-trust catch)
4. Chat-1's **"E₆ breaks to SU(3) color at the saddle (the 3 height-6 roots form A₂=SU(3))" is WRONG.** E₆ has
   exactly **3 height-6 positive roots, but they are mutually orthogonal** → `(A₁)³ = SU(2)³`, **not** `A₂ = SU(3)`.
   And `A₂` is **impossible** here: it needs a height-12 root (`α+β`), but E₆'s **max height is 11**. The dim-12
   unbroken algebra is `SU(2)³ × U(1)³`, not `SU(3) × U(1)⁴`. The "12 = dim(SM)" is a dimension coincidence.
   (Sage-verified; the figure-eight saddle does **not** yield SU(3) color.)

## Firewalled `[LEAP]` (Chat-1 Result 1, DGG — a nice consolidation, unverified physics)
5. **"The Dehn filling *is* the N=2→N=1 datum."** In Dimofte–Gaiotto–Gukov, the cusped manifold gives a 3d N=2
   theory; a filling adds a mass/superpotential deformation breaking N=2→N=1. If so, the filling does **chirality
   (N=2→N=1)** *and* **amphichirality-breaking (B286)** *and* **scale (B290)** *and* **the CP sign (B289)** as **one
   act** → **wall #3 dissolves into the seam.** Consistent with B286/B277/B303 (the closing does everything); the
   DGG/mass-deformation reading is unverified physics → firewalled `[LEAP]` (S045). A genuine consolidation of the
   seam picture, *if* it holds.

## Where it lands
The peer push extended the *forced* set into gauge dynamics (a real gain) and consolidated the seam (the filling does
all four breakings at once), at the cost of one refuted over-claim (the saddle SU(3)). The honest tiering holds:
generic-GUT gauge dynamics (forced via E₆), the object-specific gem (24=|2T|), and the firewalled seam consolidation.
The structural theorem is unchanged and slightly *richer*: the object forces all dimensionless structure **including
the gauge running** — but the values (the scale, the generation count, η_B) stay external.

## The fence
Group theory (verified) + one Sage-verified refutation + one firewalled DGG reading. The gauge-dynamics tier is
explicitly generic-GUT (not the object-specific atom). Nothing to `CLAIMS.md`.

`gauge_dynamics_skeleton.py` (pyenv: sin²θ_W, β-signs, the 24=|2T| count; E₆-root facts Sage-verified, recorded) ·
`tests/test_b304_gauge_dynamics_skeleton.py`. Related: `B264` (the principal grading / exponents), `B266`
(ℚ(√−3)→2T→McKay-E₆), `B298` (the generation wall — sin²θ_W bypasses it), `B286`/`B277`/`B303` (the seam / wall #3),
`B299`/`B301` (the generic-vs-object-specific tiering), `S045` (the firewalled DGG reading). Lit: Georgi–Glashow
(sin²θ_W=3/8); Dimofte–Gaiotto–Gukov (3d-3d / the mass deformation).

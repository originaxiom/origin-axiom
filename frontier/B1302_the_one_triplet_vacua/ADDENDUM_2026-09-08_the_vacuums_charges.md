# B1302 addendum (2026-09-08) — the one-triplet vacuum's gauge group, the light generation's charges, and its Yukawas

`verification/one_triplet_vacuum_charges.py` (run record `one_triplet_vacuum_charges_run.txt`; exact rational linear
algebra on B1283's charge table β = (ψ + χ)/4, γ = −(5/12)ψ + (1/4)χ and the two family charges) evaluates the solved
configuration of B1302 — ⟨N_{g₂}⟩ with the flavon pair S_{g₀g₁}, S_{g₁g₀}, generation g₂ light — for every assignment
of (g₀, g₁, g₂):

- **Without a ν^c VEV** (B1302's best configuration) the charge matrix of the VEV'd fields has rank 2, so **two of the
  four extra U(1)s survive: the tree-level gauge group is SU(3) × SU(2) × U(1)_Y × U(1)²**. On the light generation the
  two directions carry, in the basis (β, γ, fam₁, fam₂): (5, 3, 0, 0) with charges Q −2, u^c −2, e^c −2, d^c 6, L 6,
  ν^c −10, H_u 4, H_d −4; and (−2, 0, −1, 2) with Q 2, u^c 2, e^c 2, d^c 0, L 0, ν^c 4, H_u 2, H_d 4.
- **With ⟨ν^c_{g₂}⟩ added** (B1283's maximal branch of generation g₂, which leaves the light-pair counts unchanged) the
  rank is 3 and **one U(1) survives**, B1283's Z′ of the VEV'd generation: charges Q 6, u^c 6, e^c 6, d^c 12, L 12,
  ν^c 0, H_u 18, H_d 12 on the light generation (B1283's table up to an overall sign).
- **The light generation's tree-level Yukawa couplings vanish.** Every Yukawa of the one-coupling cubic carries the
  family tensor |ε_ijk| (B1273's zero diagonal, B1271), so Q_{g₂} u^c_{g₂} H_u,g₂ and the other three have coefficient
  |ε_{g₂g₂g₂}| = 0: the light generation is massless at tree level even after electroweak breaking — the same statement
  as B1271's W ≡ 0 on the triplet, now on the one generation the vacuum leaves light. (The light Higgs H_u,g₂ couples the
  two heavy generations, Q_{g₀} u^c_{g₁} H_u,g₂, which the flavons pair off with their mirrors.) The surviving U(1)
  charges say the same: Q + u^c + H_u = 30 ≠ 0 with the ν^c VEV.

So the closest configuration to the MSSM's field content that the tower produces — one vector-like generation, two
Higgs doublets, no exotic triplet — comes with one or two extra U(1)s and a massless light generation at tree level.
Its masses, like every number of the ledger, are the exponential sector's to supply (L201, L209). 0 of 19; price
unchanged.

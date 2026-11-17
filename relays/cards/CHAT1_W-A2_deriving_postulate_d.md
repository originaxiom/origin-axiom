# Card W-A2: postulate D, derived from the ground or shown not derivable

**Seat:** the web seat (chat1). **Opened:** 2026-11-17, at the author's request. **Kind:** `result:`, data-free. Main
will recompute what is found.

**The question.** W-A1's postulate D, verified on main as B1951 (P-863), says:
- matter is the exterior algebra of level 5's Weil space W: its even half for matter, its odd half for the Higgs;
- the gauge group is SU(W)'s commutant of ρ(−I).

Can the object force it?
1. Does the object force Λ*(W) as the matter space? The lead given: the fibre's fermion zero modes at level 5,
   second-quantised.
2. Where do three families live, once the Weil triplet is colour?
3. Failure criteria first, and the construction run on rivals.

**What is computed (`wa2_checks.py`; algebra and theta series only; no frame output; no data).**
- **A. The level.** For every prime p < 60, the number of lines of 𝔽_p² that the act LR = [[2, 1], [1, 1]] fixes.
- **B. The record's lines as W's operators.** At p = 5:
  - the Weyl operators W(v) = X^a Z^b, v = (a, b) ∈ 𝔽₅², and their Hilbert–Schmidt orthogonality;
  - XZ = ζ^(−1) ZX, with ζ = e^(2πi/5);
  - conjugation by W-A1's Weil representation ρ: ρ(g) W(v) ρ(g)⁻¹ ∝ W(M_g v). M_g is found for g = S, T and −I, and it
    is checked against the record's transport of lines (B1724: T: (a, b) ↦ (a, b − a); S: (a, b) ↦ (−b, a)) up to one
    linear identification of 𝔽₅².
- **C. The fibre's flux-5 zero modes.** The five level-5 theta functions ψ_j(u, τ) = Σ_n exp(πi·5τ(n + j/5)² +
  2πi·5u(n + j/5)). These are checked:
  - degree-5 quasi-periodicity;
  - u ↦ u + 1/5 acts as Z, and u ↦ u + τ/5 as X up to a common factor (the Heisenberg action);
  - u ↦ −u maps ψ_j to ψ_{−j}, so the even and odd parts have dimensions 3 and 2;
  - linear independence.
- **D. Families against colour.**
  - **The frame's generation triplet.** The Higgs triplet's T and S, as the record has them: T as W-F22's hand matrix;
    S exchanging the first two components (W-A1's referee; B1724).
  - **Its T-eigenphases** against the Weil 3's.
  - **Its permutation part** against SL(2, 𝔽₂) acting on 𝔽₂² ∖ 0, under (θ₂, θ₄, θ₃) ↔ ((1, 0), (0, 1), (1, 1)).
  - **The frame's quaternion units** {1, Q_I, Q_J, Q_K}: an orthogonal basis of End(ℂ²), pairwise anticommuting, so the
    level-2 Weyl operators.
- **E. The rivals p = 3, 7, 11, 13.** For each, from the Weil representation of SL(2, 𝔽_p) on ℂ^p:
  - the split of ρ(−I) and the commutant;
  - the resulting group S(U(m) × U(n));
  - the anomalies of Λ^even(ℂ^p) under it;
  - and A's count of the act's fixed lines.

**Failure criteria, committed now.** The attempt fails, and D stays a bare postulate, if any of these holds:
- **F1.** Some prime p ≠ 5 below 60 has exactly one line fixed by the act. Then level 5 is not singled out by the act's
  fixed line.
- **F2.** Some rival prime gives SU(3) × SU(2) × U(1) from its centre's split.
- **F3.** The frame's generation triplet is equivalent to the Weil 3: equal T-eigenphases, or a common level. Then
  families and colour collide in one triplet.
- **F4.** No linear identification of 𝔽₅² carries the Weyl-operator action of ρ to the record's transport of lines.
  Then the record's lines are not W's operators.
- **F5.** The flux-5 zero modes do not carry the Heisenberg action, or their parity split is not 3 + 2. Then the
  "fibre zero modes" lead fails.

**Expectations** (committed now): A has exactly one fixed line at p = 5 only; F1 to F5 all do not hold.

**What would remain counted even on success (a reading, written now):**
- whether the fibre carries flux 5 (a central holonomy of order 5 at the puncture) rather than frame C's flat twists;
- the class of the central character (the two Weil representations);
- gauging SU(W);
- the chirality (which half is matter);
- the Higgs's place.

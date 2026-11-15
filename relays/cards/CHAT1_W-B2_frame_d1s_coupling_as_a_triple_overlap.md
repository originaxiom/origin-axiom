# Card W-B2: frame D1's coupling as a triple overlap; covariance first

**Seat:** the web seat (chat1). **Opened:** 2026-11-15, at main's request (M34), under the author's ruling of that morning
(outputs computed and printed; no data, no comparison). **Kind:** `result:` (data-free).

**The question (M34).** Build frame D1's coupling with the Higgs as the third factor of a charge-conserving overlap,
q_H = −(q_L + q_R) in 6Y (up +3, down −3, leptons −3). Show it is covariant under τ ↦ τ + 1 (with w ↦ (a, b − a)) before
any mixing is computed. If it is inconsistent with frame C's bilinear kernel, say so first.

**Stage 1 (this card's first script): where the Higgs's twist can enter, tested by covariance only.** No mixing.
- **Residue level.** Each sector's coupling is built from the bilinear kernel's residues, with unit weights, so the norms
  do not enter.
- **Candidates:**
  - **K0 (the control):** frame C. The kernel is untwisted and the triplet is untwisted, in both readings.
  - **K1:** B1947's twisted triplet (characteristics shifted by (q_H a, q_H b)) in frame C's contraction, the kernel
    untwisted.
  - **K2:** the Higgs's twist in the kernel. B1938 reads frame C's 1/θ₁ as the Higgs's own Szegő kernel. Its zero is moved
    to the Higgs's point, θ₁(u) ↦ θ₁(u + h), and the residue is taken there, the triplet untwisted. Four choices of h are
    tried: ±q_H w and ±2q_H w (the matter's twist point in the kernel's u is 2qw).
  - **K3:** K2 with K1's triplet.
- **The test.** The coupling's two singular-value ratios at (τ, (a, b)) against (τ + 1, (a, b − a)), for:
  - each sector;
  - four points of order 5 (the mark, the twin, (0, 3/5) and (3/5, 1/5));
  - three bulk moduli.
  A candidate is covariant if every deviation is below 1e-8.

**Expectations** (committed with this card, before any of its output):
- **V0.** K0 is covariant in S and S̃ (the control).
- **V1.** K1 is not covariant (some deviation above 1e-3). This recomputes B1947.
- **V2 (a hypothesis).** At least one choice of h makes K2 covariant in every sector: charge conservation is met in the
  kernel.
- **V3.** K3 is reported.
- **Plant:** K0 with the point not transported (w kept) fails, with some deviation above 1e-3.

**Later stages, only if a candidate is covariant:**
1. its S-covariance;
2. which reading each sector receives;
3. the full |V| at the 24 points (heights 6 and 30, extended precision above 6);
4. whether the leptons separate from the down quarks.

Each has its own expectations, sealed before its run.

# B1644 — PREREGISTRATION: A HIGGS IN THE MULTIPLICITY SPACE — the zero modes' coupling to a Higgs in the adjoint of the quaternion structure at the fibre's puncture; is it symmetric, and what spectra do its directions give?

cc (main), 2026-10-13. **Sealed before `adjoint_higgs.py` runs.** No data. 0 of 19. POINT_REGISTER P-110 (path 1,
agreed by the owner 2026-10-13); P-105 (what acts on M).

**Why it matters.**
- Three independent routes (B1642, the SM seat's W61, the audit lane's residue audit) found that the fibre's zero modes
  give no flavour structure: the invariant pairing is antisymmetric or zero. The hierarchy needs a datum acting on the
  multiplicity space M.
- This arc tests a Higgs that is such a datum. It lives in the adjoint of the quaternion structure, which is canonically
  M (the imaginary units i, j, k), and is coupled by the standard SU(2)-invariant coupling of two doublets to a triplet.

**The derivation, by hand, written before the run.**
1. **Which Higgs can couple.** The fibre's monodromy contains −1 (a² ↦ i² = −1). An integrand single-valued on the fibre
   therefore needs an even number of quaternion doublets. A doublet Higgs with two doublet fermions cannot couple. A
   scalar Higgs can (B1642: ε-type, antisymmetric), and so can a triplet (adjoint) Higgs Φ = Φᵃσ_a.
2. **The coupling.** The invariant is ψᵀ ε Φ χ. With F_p = C_p F (C_p = j, i, k for the parity blocks (½, 0), (0, ½),
   (½, ½)), the residue coupling along a unit a is
   Y(a)_pq = Res_{z=0} Fᵀ ε C_p⁻¹ σ_a C_q F = Res Fᵀ ε X F, with X = −C_p a C_q ∈ {±1, ±i, ±j, ±k}.
   - Fᵀ ε (±1) F = 0.
   - Fᵀ ε (±u) F has residue ±R_u (B1642): R_i = −θ₂²/(2πη³), R_j = −θ₄²/(2πη³), R_k = i θ₃²/(2πη³).
3. **The table, from the units' multiplication:**
   - Y(i) = [[−R_i, R_j, 0], [R_j, R_i, R_k], [0, R_k, −R_i]];
   - Y(j) = [[R_j, R_i, R_k], [R_i, −R_j, 0], [R_k, 0, −R_j]];
   - Y(k) = [[−R_k, 0, R_j], [0, −R_k, R_i], [R_j, R_i, R_k]].

   All three are symmetric with a non-zero diagonal. For a vacuum direction a = (a_i, a_j, a_k) in M,
   Y(a) = Σ_r a_r Y(r).
4. **Near the cusp, along a = i.** θ₂² ~ 4 e^{iπτ/2} → 0, so x = R_i → 0 while y = R_j and z = R_k stay finite.
   - At leading order Y(i) → Y₀ = [[0, y, 0], [y, 0, z], [0, z, 0]], with null vector n = (z, 0, −y) and two heavy
     states of mass about √(|y|² + |z|²).
   - The light state's mass at first order is |x nᵀDn|/|n|² with D = diag(−1, 1, −1), and nᵀDn = −(y² + z²). By
     Jacobi's θ₃⁴ = θ₂⁴ + θ₄⁴, y² + z² ∝ θ₄⁴ − θ₃⁴ = −θ₂⁴, which is O(q). So the first order is O(|q|^{3/2}).
   - The second order, x²(nᵀDh)²/M_h, is O(|q|) and dominates.
   - **Predicted:** the light mass relative to the heavy ones scales as |q| = e^{−π Im τ}, a light generation, while the
     two heavy ones stay nearly equal.

## Seen first

`VERDICT topic-sweep /adjoint|triplet Higgs|Higgs in T|multiplicity|flavon|vacuum direction|family space/: 73 of 1414 arcs on main match (NEGATIVE 13, OPEN 4, PROVED 55, RETRACTED 1)`
— in the weave era: B1601, B1614, B1641. None couples the zero modes to an adjoint Higgs. Read before the seal:
- B1642 (and its addendum: W61 and the audit lane's residue audit); B1641 (the parity rule); B1643 (the criteria C1–C6);
- the SM seat's C0 (a Higgs must carry a parity), W56 (a Higgs like a generation, at the level of modular forms) and
  W60 (the parity Higgs on a half-period line), and the audit lane's parent-map caution (P-108).

**Literature:** the SU(2) invariant of two doublets and a triplet (ψᵀ ε σ_a χ, symmetric); flavour from a Higgs (or
flavon) vacuum direction in a family space.

## Disclosed

- **The structure (S1, S2) was derived by hand,** using the quaternion multiplication table. The spectra (S3) are
  read-outs with rules stated below; no spectrum was computed before the seal.
- **The adjoint Higgs at the puncture, and its coupling through the residue, are hypotheses.** Its physical existence
  needs the parent map the audit lane asks for (P-108).
- **Zero Wilson line,** as in B1642.

## Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **S1** | Y(i), Y(j), Y(k) computed as residues equal the table of step 3 (with B1642's R's), at 10 random τ to 1e-30 relative; each is symmetric with a non-zero diagonal | 85% |
| **S2** | linearity: Y(a) for 5 random real directions equals Σ a_r Y(r) to 1e-30 | 95% |
| **S3a** | READ-OUT: over 400 directions on the real unit sphere of M and τ in {i, ω, three points on the tick's axis, iy for y = 1.5, 2.5, 4}, the normalised singular values. Reading rule: report the smallest distance to 1 : φ⁻¹ : φ⁻² and where it occurs | — |
| **S3b** | near the cusp, along a = i: the smallest normalised singular value scales as \|q\| = e^{−π Im τ}: the log-log slope of ln(σ_min/σ_max) against Im τ over y = 2, 3, 4, 5 is −π within 10% (alternatives named: −π/2 if the first order did not cancel, −3π/2 if the second order cancelled too) | 60% |
| **S3c** | READ-OUT: whether any real direction gives three distinct masses with a hierarchy (smallest/largest < 10⁻²) at Im τ = 4; and the rank of the map (a, τ) → normalised spectrum | — |

**The reading, written before the run (the cells can only lower it).**
- **If S1 and S2 hold,** a Higgs in M, the datum the three routes found missing, gives a symmetric coupling of the zero
  modes with no free coefficient but its direction. The flavour structure then lives in that direction and in τ.
- **S3 decides whether it can carry the world's pattern.**
  - Golden somewhere: the golden coupling is computed, given the Higgs.
  - A hierarchy near the cusp: the first step of hierarchy is the cusp's own.
  - Neither: the adjoint Higgs is excluded as the flavour source.
- **If S3 shows hierarchical capacity,** the next arc is a sealed crossing, meeting B1643's C1–C6: a two-Higgs model
  (separate up and down directions, CKM from their misalignment), with its parameter count stated first.
  - With real directions it has 2 (τ) + 2 + 2 + 2 scales = 8 real parameters for the 10 quark numbers.
  - With complex directions it has more.

## Instruments

`verification/adjoint_higgs.py`, reusing B1642's sealed definitions (the theta series, the zero mode, the residue);
hashes in `ARTIFACT_HASHES.txt`.

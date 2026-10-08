# W44 — the rule, recorded before the read-out

The SM-derivation seat, 2026-10-08. Committed before the code that reads it exists. The predictions below were derived
by hand before this was written. Nothing here is a result.

## Why this arc

- **The owner's restated goal** (with main, 2026-10-08): the Standard Model's structure, and how many free numbers
  the principle leaves and why.
- **The count rests on B1620.** "The weave's symmetry reduces none of the 13" is load-bearing in main's write-up for
  outside review, but it is established in one frame only: all of G acting as flavour.
- **W43 showed the frame matters.** The trimaximal family (TM1 or TM2) a tensor allows changes with the frame, and the
  frame is GENESIS FK11's open datum. So the count has to hold in every frame on record before it can be stated
  without one.
- **The audit lane questioned B1620's fits** (relay CUSP_WARD_AND_FLAVOR_TENSOR):
  - B1620's PMNS score counts an excursion of up to one half-width outside a 3σ range as reached;
  - its sampled ranks and its necessary block test are not certificates.

  This arc uses a strict predicate, keeps every witness, and takes the family dimension as the most common rank over
  five points. W43's post-hoc check showed the maximum over points can add a spurious rank.
- **The data.** No new data is read. B1612's transcription (PDG 2025 CKM magnitudes; NuFIT 6.0 3σ ranges of |U|) is
  copied verbatim to `received/B1612_data.json`. Its sha256 is 61ea1565…, as in B1612's ARTIFACT_HASHES on main.
- **Seen first.** B1620's findings, its post-seal scripts and its stored fit summaries were read before this rule
  (W43's F2 transcribed the last). This arc's fits are this seat's own code.

## Weave or thread?

- Every residual pair in each frame is taken, none chosen. The quantity, the smallest mixing family that reaches the
  data, is defined on the joint action's group. The claim is about all pairs at once: weave-type.
- A frame is a choice of which part of the group is gauge (GENESIS FK11, open). Each frame is stated, never presented
  as forced.

## The frames

- **F_all** (B1620's): every element c(g) S(g) of G is flavour. The residuals are G's 68 subgroups.
- **F_c** (W43's): c is gauge. The residuals are the 98 subgroups of B₃ = {±1} × O, acting on T by ±S.
- **F_S** (W24's): every S(g) is gauge, and only c is flavour. The flavour group acts on T by scalars, so every viable
  residual leaves each sector's matrix free. Nothing is reduced (by hand, not computed).

## The method

- **Residuals and viability:** exact, as in W42 and W43.
- **Pairs.** Every ordered pair (H_u, H_d) of residuals viable under one tensor; u is the charged leptons or the up
  quarks, d the neutrinos or the down quarks. Pairs related by a simultaneous conjugation give the same family, so one
  representative per orbit is fitted.
- **Block sums.** Each viable residual is abelian, and its isotypic pieces on T are the joint eigenspaces of its
  elements.
  - For pieces a of H_u and b of H_d, the block sum tr(P_a P_b) is fixed across the family. It is the sum of |U_ij|² over
    the generations the pieces carry.
  - B1620's necessary test compares these sums with the data's, for some assignment of generations to pieces. The CKM
    must agree within 3σ, with σ propagated linearly. For the PMNS, each sum must lie between the sums of lo² and hi².
  - A pair that fails the test cannot reach the data.
- **Family dimension:** the most common rank, over five random points, of the map from couplings to the nine |U_ij|²
  and J. B1620's threshold is used (relative 10⁻⁶, absolute floor 10⁻⁵).
- **Fits**, for every orbit that passes a block test with dimension below 4, and for dimension-4 orbits until one
  witness per frame and tensor is found. Each fit covers the 36 row and column permutations from several starts.
  - **CKM:** reached when every |V_ij| is within 3σ of PDG's value.
  - **PMNS (the strict predicate):** reached when every |U_ij| lies inside NuFIT's 3σ range, to 10⁻⁶ absolute.
  - Every witness (the parameters and |U|) is kept. A search that finds none is reported as "not found", not as
    "unreachable".

## The cells (predictions and priors)

| | prediction | prior |
|---|---|---|
| **D1** | **F_all, the control.** The smallest dimension with a witness is 2 for the PMNS under T̄ ⊗ T and T ⊗ T, and 4 under Sym² T; it is 4 for the CKM under all three tensors. Every family below those dimensions fails the necessary block test, which makes the lower bound rigorous. The PMNS witnesses of dimension 2 have a TM1 column under T̄ ⊗ T and a TM2 column under T ⊗ T (W43). | 85% |
| **D2** | **F_c.** The same minima: PMNS 2 under T̄ ⊗ T and T ⊗ T (TM1 and TM2 both), 4 under Sym² T; CKM 4 under all three. | 75% |
| **D3** | **B1620's PMNS families below four dimensions, regraded strictly** (those W43's F2 transcribed). The TM-type families, which scored 0, stay reached. Whether the families that scored 0.06 to 0.36 have witnesses inside the ranges is not predicted. | 85% for the first part |

**The reading, written before the run.**
- If D1 and D2 hold, then in every frame on record the weave's symmetry fixes none of the 13: the nine charged masses
  are free on every viable residual, and the CKM needs a four-dimensional family.
- In the lepton sector, which lies beyond the 19, the most a residual pair can do is two relations, a TM type. That is
  available under T̄ ⊗ T and T ⊗ T only: TM1 or TM2 according to the frame (W43), and in F_S nothing at all.
- So the count "0 of 19 fixed, at most two lepton relations by a chosen residual" would be frame-independent, and the
  frame would decide only which relation P10 tests.

## Discipline

- One run. A failed launch (a crash before the read-out) is disclosed and fixed, not counted as a run.
- Each cell is recorded as computed; a failed prediction is recorded as failed.
- Post-hoc checks are labelled.

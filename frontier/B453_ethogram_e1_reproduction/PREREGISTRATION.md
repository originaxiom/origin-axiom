# B453 — PREREGISTRATION: Ethogram E1 — reproduction: the lineage, honestly gated

**Committed before computation. Firewalled. Campaign: OPEN_LEADS §Ethogram; dictionary card:
"reproduction & heredity" (S055).**

## Questions (blind)

- **E1a (assembly, labeled — not a probe result):** the sterility statement. The surgery lineage
  σ→4₁→child terminates: the child 4₁(5,1) is closed ⇒ Weil-rigid ⇒ no moduli, no cusp, no
  filling channel. Assembled from banked B435/B443.
- **E1b (the decisive cell):** the ℤ/5 cyclic cover of the child (H₁ = ℤ/5 ⇒ unique). GATES
  (theorem-forced, must pass): vol(cover) = 5·vol(child) = 4.9068441…; invariant trace field
  commensurability-rigid (disc −283 class). OPEN COMPUTABLES: **b₁ and torsion of the cover**
  (b₁ > 0 ⟺ the cover could fiber — is the Agol virtual-fibering degree already 5?); the
  low-index cover scan (degrees 2–6, budget-capped) for the minimal positive-b₁ degree.
  Agol backdrop stated: "the lineage continues virtually" is a THEOREM, not an observation.
- **E1c (the cover-field table):** parent cover degree k vs character-variety field content —
  assembled from the banked orbit tower (B448: T₁-period-2k = the k-fold cover's extended
  characters: k=1 → ℚ(√−3); k=2 → ℚ(√−7); k=3 → ℚ(√−3)), with the Maclachlan–Reid
  reconciliation as a GATE (geometric invariant trace field constant up the tower, B235; new
  components bring new fields — textbook). Only the table itself is NEW-MATH-eligible.

## Bins
E1b: b₁(ℤ/5 cover) > 0 (the lineage can continue at degree 5 — NEW-MATH-grade observation,
lit-gate permitting) / b₁ = 0 (degree 5 does not fiber; report the minimal positive-b₁ degree
found ≤ budget, or UNDECIDED-AT-DEGREE-6). Adjudication: forced/laundered only (knot channel —
no p-values, n < 10).

## Controls
The identical pipeline on 5₂(5,1)'s child and 6₁(5,1) (foreign): covers, b₁, torsion.

## Gates & lit-gate
Volume ×5 exact; H₁ of the base reproduced (ℤ/5); **BLOCKING lit-gate running** (Chinburg /
Dunfield–Thurston / census computations of the Meyerhoff manifold's covers — a rediscovery
cannot bank as new).

## Machinery
SnapPy `Manifold('4_1(5,1)')`, `.covers(k)`, `.homology()`, `.volume()`; budget: degrees ≤ 6,
≤ 30 min compute.

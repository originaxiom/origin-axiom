# B1640 — THE FRAME AUDIT: at the owner's request (2026-10-13: "where our naivities lies … what angle are we missing"), three referee lenses read the record's frames rather than its results; main re-ran what they found with its own sealed instrument. Two statements that took a frame or a convention for forced are scoped: the degeneracy at ω that grounded τ = ω's retirement, and "no choice is made" in the weave's multiplier. The TM1 reading cannot come from one τ on the ruled branch

**Verdict: PROVED** (an audit arc; every number below is recomputed on main). cc (main), 2026-10-13. GENESIS v1.41 →
v1.42 (three scopings: the degeneracy at ω, the multiplier's hand, positivity's reach). **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /frame audit|degenerate at ω|degenerate at omega|lift\^-1|conjugate multiplier|hand of the multiplier|TM1/: 11 of 1412 arcs on main match (NEGATIVE 5, PROVED 6)`
— B1612, B1613, B1615, B1616, B1618, B1625, B1628, B1634, B1635 (the statements audited here) and B342 (the object's
Z/3 as trimaximal symmetry, an earlier TM reading). Everything else was seen too. This arc corrects; it does not test a prediction. The lenses were three referee agents of this session (the
mathematical chain; the physics dictionary and the frames; patterns across the record). Their reports are summarised in
`docs/THE_INTEGRATION_CENSUS_2026-10-13.md` §7. Two cells reuse their scratch checks, rewritten here against B1635's
sealed instrument, imported unchanged. **Literature:** Feruglio (2017) and the modular-flavour literature for the reading
of τ; Novichkov–Penedo–Petcov (arXiv:2006.03058) for the weight-1 triplet of Γ(4).

## 1. The cells (`verification/frame_audit.py`, `frame_audit.json`, `frame_audit_run.txt`)

| cell | question | result |
|---|---|---|
| **A** | is every coupling degenerate at ω on the ruled branch (B1635 §3; GENESIS v1.41, the seat's W50)? | **No.** B1635's own sealed JSON lists nine T̄ ⊗ T members as non-degenerate at ω (e.g. 1 : 0.674 : 0.448 at k = 4, 1 : 0.648 : 0.397 at k = 6). Live: six random T̄ ⊗ T members at k = 4, 6 and six T ⊗ T members mixing the symmetric and antisymmetric pieces at k = 3, 5 are non-degenerate (smallest relative gap 0.014). Only the single pieces of T ⊗ T (D, O⁺, O⁻ alone) are degenerate there, which is what B1635's K5(i) tested. |
| **B** | is the multiplier forced ("no choice is made", B1634 §3)? | **No; it is one bit, and it decides the golden coupling.** Coupling dimensions by piece (D, O⁺, O⁻) at k = 1, 3, 5: record (ρ = lift⁻¹): (0,1,0), (0,1,1), (1,2,1). Conjugate: (0,0,1), (1,1,1), (1,1,2). Under the conjugate the weight-1 symmetric space is empty, so there is no golden coupling at the lowest weight. GENESIS v1.41 already records that the conjugate does not allow weight 3/2. |
| **C** | can one τ give the TM1 reading's residual pair (RL for the charged leptons, RRL for the neutrinos; B1612)? | **No.** ρ_θ(RL) shares every eigenline with eight elliptic elements, all of order 3 (fixed points at ω-type points, e.g. 3/2 + i√3/2). ρ_θ(RRL) shares every eigenline with four, all of order 2 (fixed points at i-type points, e.g. (1 + i)/2). No point of H is fixed by elements of both orders. Checks: the reduction is a homomorphism up to η's character, and RL ≠ LR (the bite). |

## 2. What it says

- **τ = ω's retirement (GENESIS v1.35) stands only as "no hierarchy found".** B1618's "the Dirac masses are degenerate at
  ω for every weight" used the inner automorphisms, which B1634 scoped off the ruled branch. There, the Dirac tensor's
  masses at ω are distinct. No hierarchy was seen in any sample, but the near-fixed-point regime, the standard source of
  hierarchies in the modular-flavour literature, is not computed. B1635 §3's sentence "Every coupling is degenerate at
  ω" overstated its sealed cell, which concerned the single pieces of T ⊗ T.
- **The multiplier carries a hand.** "ρ(γ) = lift(γ)⁻¹ (forced, since the lifts compose in reverse)" is one of two
  homomorphisms; the transpose is the other, and for these unitary lifts it is the complex conjugate. (The choice of
  lift⁻¹ has a functorial reason, T being cohomology; see §3.1. The algebra alone does not fix it.) Which of V's two
  pieces is called T is a second binary choice; the two choices together pick the multiplier or its conjugate (the
  mathematical-chain referee's convention table). The record's choice allows both W45's weight 3/2 and B1636's
  symmetric weight-1 coupling. The conjugate allows neither. **So the index and the golden coupling come with the same
  hand, and which hand the matter carries is not derived.** The golden identity (B1638, B1639) is untouched: it is a
  theorem about theta functions. What depends on the hand is whether the weave's lowest symmetric coupling exists.
- **The TM1 reading (FALSIFIER_REGISTER P10) is not a τ-only result on the ruled branch.** It needs RL's and RRL's
  residuals at once, which one τ cannot supply; it needs two moduli or a breaking agent the principle does not name.
  P10′ (TM2 under T ⊗ T, B1625) was read in the frame where all of G is flavour; on the ruled branch it has the same
  status. Both falsifier entries get a scope note; neither is withdrawn (they test frames).

- **Positivity's reach (GENESIS GM5d).** The owner's earlier weave runs carry an independent audit, made before B1638
  (archived 2026-10-11 against 6c148ddd4). It points out that (R L⁻¹ R)² = −I on homology, so the group generated by L,
  R and their inverses contains −I. Positivity excludes −I from the physical updates, a semigroup, not from the group
  ⟨L, R⟩ ≅ B₃ from which the multiplier and the couplings are built (B1634's Δ⁴ acts on T as −1). GM5d's "it is what
  excludes the sign" is scoped to the updates in v1.42. The same audit reproduced B1635's coupling table by exact
  polynomial linear algebra (weights 1–11), found the theta representation irreducible and **not equivalent to its
  conjugate** (the fact behind cell B), and gave the 3 : 2 : 1 counterexample at ω (cell A's finding, independently).

## 3. What it does not settle (owed)

1. **The hand from geometry.** Derive the multiplier from the zero modes themselves (the period map of the cover in
   T's isotypic part, under τ → τ + 1 and τ → −1/τ), not from a convention. *Read after this arc was written, the SM
   seat's W46 rule already gives half of it:* "the cohomology T is a pullback (W21's on_V), so its monodromy is the
   inverse" — lift⁻¹ is what cohomology forces (the transpose describes the dual, homology). The other half, which
   piece of V is T, W46 reads as the puncture condition's orientation: ρ_T is the canonical condition's H¹ (index −3
   at one cusp unit), ρ̄_T the all-allowed condition's H⁰ (+3). If so, the hand is the sign of the ±3 itself, and the
   golden coupling goes with the canonical condition. Queued for the W46 arc (POINT_REGISTER P-079).
2. **Two objects.** W45 and W46 put the ±3 on M₁,₂, whose fibre loops (point-pushing) are exactly the inner
   automorphisms the ruled branch excludes; the couplings live on the ruled branch. If the fibre loops act on T by the
   parity signs, every off-diagonal coupling is forbidden and the golden coupling with it; if they act trivially, W46's
   index must be recomputed for the pulled-back bundle. This is folded into the W46 verification arc, now first in the
   queue with this question as its first cell.
3. **The dictionary.** Holomorphic couplings, a minimal Kähler term, every field in one T and one Higgs per sector are
   the modular-flavour ansatz, never stated on the record. B1635's count 2 + Σ(2d − 1) is a count under those
   assumptions. The overlap-integral reading of the fibre (two lenses independently: the couplings as overlaps of the
   fibre's zero modes, theta constants with no free coefficients) is registered as the strongest unpursued lead (L251).

## 4. Disclosed

- Cells A and B use B1635's instrument functions with B1635's own conventions; cell B's conjugate branch uses the
  mathematical-chain referee's settings (W = η⁶Y, cusp order 2), which main re-ran and checked against the record branch
  reproducing B1635's sealed dimensions.
- Cell C's search box is |entries| ≤ 4.
- A referee computed, unsealed, the golden spectrum read as a Majorana neutrino mass matrix (mass-splitting ratio
  ≈ 0.28 in normal ordering, against ≈ 0.03 measured), and another the golden coupling's mixing at τ = i (golden-ratio
  mixing). Neither is banked. Both are **seen** for any future preregistration.

## 5. Files

`verification/frame_audit.py` (with `frame_audit.json`, `frame_audit_run.txt`); `adoption/amend.py` with
`received/GENESIS_v1_41_main.md`; the lock `tests/test_b1640_the_frame_audit.py`. Addenda of 2026-10-13 on B1618, B1634
and B1635.

## Addendum (2026-10-16, B1662): the pull-back acts on the records (GENESIS v1.48)

- **A scope sentence.** v1.42 scoped GM5d to the semigroup of updates, because ⟨L, R⟩ contains −I. Under GM5b (adopted, P-179) the updates are the group. The scoping is consistent with the ruling, which it anticipated.

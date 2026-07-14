# B592 — R3-M, THE MIRROR LISTENER: the verdict is DEAF, in the sharpened form

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities. The
owner's directive: run R3-M (the cut-open trace prereg, relayed — the original
`R3M_PREREG_FOR_CC.md` never reached this seat; the reconstruction is frozen in
PREREGISTRATION.md). Locks `tests/test_b592_mirror_listener.py`.**
Run: `python3 mirror_listener.py` (pyenv, ~2 min).

## The measurement

A(g) = ⟨ψ_mirror| C ρ(g) |ψ⟩ on the golden stage SU(3)₂, channel by channel
(singlets 1, 8; pairs 3/3̄, 6/6̄ split into pair-even and pair-ODD), over the
gluing sweep g ∈ {I, RL, RRLL, RRL}; state components = the banked B245
colored invariants at q = e^{iπ/5} (the 8-channel is a method gap and is pure
θ-even — it cannot touch the verdict).

## THE VERDICT: DEAF — the relay's second branch, with proofs

Per the frozen outcomes table the run is DEAF, and in a form SHARPER than the
table's "Im = 0 everywhere":

**1. The θ-odd channels are IDENTICALLY ZERO — not merely real — for every
gluing.** Proof (found in-diagnosis, then verified to 1e-15 across the sweep):
the object's state is C-symmetric (Cψ = ψ — the components obey c_λ = c_λ̄ by
invertibility, B584's third unhearability), and C is central in the modular
representation; hence ρ(g)ψ is C-symmetric for EVERY mapping class g, and the
pair-antisymmetric readout vanishes identically. **The fourth unhearability
(the cut-open version): no mapping-class gluing of the mirror-double lets the
mirror hear the θ-odd sector of an invertible knot's state.**

**2. The C-twist is ABSORBED by the mirror covector.** Exact identity
(verified for every g): the mirror state's label conjugation cancels the
C-insertion — A_twisted(g) = A_untwisted(g). At the state-times-mapping-class
level, "mirror copy + C-twist" IS "plain copy + no twist": the twisted double
is not a new play.

**3. The residual imaginary part is inversion phase, not chirality.** The
Θ-reality identity conj A(g) = A(g⁻¹) holds exactly (unitarity); the
even-channel Im is killed by the g ↔ g⁻¹ symmetrization. This is the
Θ-reality kill condition of the prereg, realized.

## The four controls

- **C1** (recast in-diagnosis to the absorption identity): twisted =
  untwisted for every g (1e-15); reality at g = I. PASS.
- **C2** (recast to the discovered Θ-reality): conj A(g) = A(g⁻¹) exact; the
  inverse-symmetrized amplitude real for every g. PASS.
- **C3** (level 1): the θ-odd channel dead at SU(3)₁ across the sweep (the
  rank control, consistent with B580-Q1R). PASS.
- **C4** (5₂): an independent U_q(sl₃) R-matrix pipeline, validated on 4₁
  against B245 to 4.5e-16, computed J₃(5₂) = −0.118033989 − 0.812299241i at
  the root (non-real — the amphichirality contrast at the state level); the
  braid word's closure verified to be 5₂ by the Jones layer (unique match
  among 7 candidates at generic q). **5₂'s θ-odd channels are ALSO dead** —
  the deafness is invertibility-universal, not an amphichirality artifact.
  PASS (one in-diagnosis bug caught by the prereg's MIXED rule: the first 5₂
  state vector was misaligned with the weight order — a fake odd signal,
  fixed and disclosed).

## THE CONSEQUENCE (what R3-M was for)

The mirror listener **cannot** be built from {the mirror state, C, mapping
classes}: every ingredient available at the state-times-gluing level is
θ-even-locked. The θ-odd twist that makes B582's mirror-double genuinely
chiral is the **Lie-algebra dial** ({4,8}-direction deformation), which is NOT
a mapping class. Round 4's forced move is now sharper than X3 left it: not
just "non-vacuum observer states," but **states deformed along the dial** —
deform the state, not the gluing. (Registered as the Round-4 core; L79's
geometric-realization item is exactly the question of what manifold operation,
if any, realizes the dial.)

## Method gaps (disclosed)

The 8-channel amplitude (adjoint color of 4₁) and J₆(5₂) were not computed
(no banked formulas; the R-matrix route needs the 6's R-matrix or cabling) —
both are pure even-channel quantities and cannot affect the verdict.

## Anchors

B584 (third unhearability; C), B585/B586 (the closed-trace face), B582 (the
dial twist — the object R3-M was probing), B245/B240 (colored inputs), B279
(invertibility), B580-Q1R (the level-1 rank control), X3/B583 (the second
unhearability — this is its cut-open sibling).

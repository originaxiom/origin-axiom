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

## B592-OPEN — the run repeated EXACTLY per the self-contained handoff (the open matrix)

The owner re-delivered chat-1's self-contained R3-M handoff; the first run had
contracted the channels (row sums), which the handoff's Step 2 forbids ("do
NOT sum"). The faithful open-matrix run (`r3m_open_matrix.py`, locks extended):

**C1 first (the foundation): PASS.** The untwisted plain double is real in
every channel (max|Im| < 1e-12) — the Θ-reality baseline holds; the
computation is valid per the handoff's own criterion.

**The verdict lands outside the locked table, and per the handoff's rule
("if the result is not in the outcomes table: bank it as-is and extend the
table") the NEW ROW is:**

> **OPEN-HEARD / CLOSED-DEAF.**
> (i) At the bare twisted weld (g = I): Im = 0 everywhere (the table's DEAF).
> (ii) At monodromy-dressed welds: Im(M_odd) ≠ 0 AND Im(M_even) ≠ 0 (the
> table's MIXED row) — but the imaginary parts are parity-symmetric inversion
> phases (conj A(g) = A(g⁻¹)), not chirality.
> (iii) **THE SIGN-FLIP THEOREM — what the twist actually does:** the twist's
> entire imprint on the open matrix is the SIGN of the θ-odd block:
> M_odd(twisted) = −M_odd(untwisted), M_even unchanged, exactly, for every
> weld (proof: P_odd C = −P_odd, P_even C = +P_even; verified 1e-15). This is
> chat-1's "the θ-odd component flips sign rather than vanishing," made
> precise — the flip lives on the OPEN matrix.
> (iv) **Parity conservation:** the odd↔even cross-blocks vanish identically
> (the states are real and C-symmetric; Cρ(g) is parity-preserving) — the
> open-matrix face of the quadrature theorem.
> (v) And every CLOSED contraction of the odd block against the (C-symmetric)
> states vanishes (the B592 theorem above). **The mirror hears the twist as a
> sign it can never sum.** The first chiral amplitude from geometry exists at
> the open-channel level — it is the odd block with its twist-flipped sign —
> and self-deafness is exactly the statement that no closed pairing reads it.

**C4 in matrix form:** 5₂'s open matrix has the same universal structure
(parity conserved; twist = odd sign flip — the theorem is knot-independent
for invertible knots) with knot-specific entries (non-real already at plain
welds, from the non-real J₃(5₂)). Note: the handoff's "5₂ has trace field
ℚ(√−7)" is a slip — 5₂'s trace field is the cubic of discriminant −23; the
control's purpose (knot-specificity) is unaffected and satisfied.

**Prediction check (the handoff's HEARD list):** prediction 1 (Im supported
exactly in θ-odd channels) FAILS as stated — the Im is parity-symmetric; the
twist's signature is the sign, not the imaginary part. The sign-law
comparison transfers to the sign flip: the θ-odd block flips (−), the θ-even
does not (+) — the parity pattern (−1)^{parity} — which IS the B581 sign law's
shape at the operator level. Magnitudes vs |τ_m|: not testable on this stage
(the stage channels are the primary pairs, not the six exponents — the frame
distinction banked in B586).

**Consequence, unchanged and sharpened:** hearing the twist in a closed
amplitude requires a listener whose state is NOT C-symmetric — deform the
state along the dial (Round 4), or find a third entity (the handoff's own
DEAF-branch prediction 3).

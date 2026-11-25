# SM-R635 — the boundary-free classes of H¹(fibre, ad Q₈): the FL-08 price, and whether the CKM corner can move

*Card of the SM seat, 2026-11-25, for register row P-635 (main's page M53 on docs/seats/sm.md). Written and sealed
before the script (`relays/sm_r635/run.py`, SHA-256 028eb8e8622d5a83) is run on the frame's Q₈ point. The script was
import-tested and smoke-tested on plants only (a generic irreducible pair, the trivial representation); no result on the
Q₈ point has been computed or seen by this seat. Data-free: no measured value is read, printed or compared.*

## 0. The question

Main's ask (M53): the FL-08 pricing sentence for the boundary-free dimension 3 of H¹(ad Q₈); then whether the CKM corner
moves along that family at fixed lines, data-free.

## 1. What the record already says (read first)

- **P-635** (row 835): main's 2026-07-08 phrase "the only continuous degrees of freedom anywhere"; asked: dim
  H¹(fibre, ad) for the frame's flat Q₈ bundle; if positive, price the restriction to finite-order lines as an FL-08
  choice and check whether moving along the family moves the CKM corner.
- **B1836 § 5** (main re-ran the reader's check, readers/C/c6_p635_p636.py): H¹(ad Q₈) = 0 on the closed torus and on
  the punctured fibre with the boundary held; 3 with the boundary free. The holonomies there are (Q_I, Q_J); Ad(Q_I) =
  diag(1, −1, −1), Ad(Q_J) = diag(−1, 1, −1); the boundary loop c = [a, b] has ρ(c) = −1 and Ad(c) = 1. The row adds:
  "the lines w themselves stay the frame's continuous data, restricted by FL-08's choice".
- **FL-08, as the register states it** (P-567, row 767; the ledger itself not opened, as the brief requires): the lines
  as centre Wilson lines, restricted to finite order (order 5 gives minimal SU(5) exactly; Z₅ × Z₃ lines lie outside the
  sealed reach).
- **The frame** (B1656's instrument; B1723's copy b1656_funcs.py; frame C's B1945 determinant_law.py): the Q₈ enters as
  constants, not as an input. The four channels s = 1, i, j, k are the four quaternion units, and in frame C each is
  a half-period shift of the theta characteristic: (½, ½), (½, 0), (0, ½), (0, 0). The generation blocks are
  (Q_J, Q_I, Q_K). EPS = Q_J. The Higgs is a pure quaternion S = c₁Q_I + c₂Q_J + c₃Q_K. The kernels are level-2 theta
  functions with a simple pole at the puncture, and their residues form a null quaternion (B1653). The CKM corner
  (B1825, B1826) is the ratio |V_ub|/(|V_us||V_cb|) of the frame's own V = U_uᴴU_d.

## 2. What will be computed (`relays/sm_r635/run.py`, exact sympy unless marked)

The frame's Q₈ is read from main's module (QI, QJ, QK, EPS, BLOCKS); nothing of the frame is evaluated.

- **G0, the premise.** The module's QI, QJ satisfy the Q₈ relations, and its EPS and BLOCKS are the Q₈ elements stated
  above.
- **F1 to F3, Fox calculus** (shares no code with B1836's C6; there the cocycle formula was written out by hand). H¹ of
  π₁ with coefficients Ad ρ: Z¹ is the kernel of the relators' Fox Jacobian, and B¹ is the image of v ↦ ((Ad g − 1)v).
  - F1: the closed torus ⟨a, b | [a, b]⟩.
  - F2: the punctured fibre F₂ with the boundary free.
  - F3: the boundary held: the classes whose restriction to c lies in (Ad c − 1)V, and the rank of the restriction.
- **F4, the decomposition.** Ad(Q₈) splits su(2) into the three non-trivial characters of Z₂ × Z₂, one per quaternion
  axis. dim H¹ is computed per character on F₂ and on Z².
- **F5, the lines.** The centre u(1) (the lines w) with trivial coefficients, on the closed and the punctured fibre, and
  the restriction to c. It checks that the line directions and the three classes are complementary, so "at fixed lines"
  is well defined.
- **F6, the explicit family.** A(s) = Q_I·exp(s₁Q_I)·exp(s₃Q_K) and B(s) = Q_J·exp(s₂Q_J), with det = 1 and unitary
  for real s, and flat on F₂ with no relation.
  - At s = 0 it is the frame's pair.
  - The Jacobian of the conjugation-invariant coordinates (tr A, tr B, tr AB) at 0.
  - The tangent cocycles' rank modulo B¹.
  - The boundary trace κ(s) = tr[A, B]: the Fricke identity κ = x² + y² + z² − xyz − 2, checked numerically at 20 seeded
    points to 40 digits; its gradient and Hessian at 0; and a seeded sample of 2000 points in |s| ≤ 0.5 (numerical,
    disclosed).
- **F7, the monodromy** (supplementary). Take φ: a ↦ ab, b ↦ bab, which abelianises to [[1, 1], [1, 2]], the
  figure-eight fibration's monodromy (premise: the fibre is m004's, as B1836's C6 takes it).
  - Find P ∈ SO(3) with P Ad ρ(φx) P⁻¹ = Ad ρ(x).
  - Compute φ* on H¹(F₂, ad) and dim ker(φ* − 1). By the Wang sequence, with H⁰ = 0, this is dim H¹(m004; ad) for the
    extended representation.
  - A second route: Dφ on the trace coordinates through the family.

**Controls and plants** (each must come out as stated, or the instrument is broken):

| | what | must give |
|---|---|---|
| F1 | the closed torus at Q₈ (the control the ask names) | H¹ = 0 |
| P1 | the reducible pair (Q_I, Q_I) on the closed torus | H¹ > 0 (the computation can see classes) |
| P2 | a generic irreducible rational pair on F₂ | H¹ = 3, H¹_par = 2 (held-boundary classes can be non-zero) |
| P3 | the trivial representation | H¹ = 6 on F₂ and on Z² |
| P4 | φ* on the trivial representation (= [[1, 1], [1, 2]] ⊗ 1₃) | ker(φ* − 1) = 0 |

P2 to P4 passed in the smoke test before this card was sealed. P1 and F1 touch the Q₈ point and have not been run.

## 3. Expectations, written before the run

| | expectation | prior |
|---|---|---|
| G0 | the module's Q₈: QI² = QJ² = −1, anticommuting, EPS = QJ, BLOCKS = (QJ, QI, QK), commutator −1 | 97% |
| F1 | the closed torus: H¹ = 0 | 99% |
| F2 | the punctured fibre, the boundary free: H⁰ = 0, H¹ = 3 | 99% |
| F3 | the boundary held: H¹_par = 0; the restriction to c has rank 3 | 99% |
| F4 | each axis character contributes 1 on F₂ and 0 on Z² | 97% |
| F5 | lines: H¹ = 2 on both closed and punctured; restriction to c has rank 0 (lines never move the boundary) | 97% |
| F6a | the family has rank 3 in (tr A, tr B, tr AB) at 0, and its tangents span H¹ (rank 3 modulo B¹) | 95% |
| F6b | κ: zero gradient and positive-definite Hessian at 0; κ > −2 at every sampled s ≠ 0 (all moves leave −1) | 92% |
| F7a | dim ker(φ* − 1) on H¹(F₂, ad) = 1 for every admissible P (the half-dimension bound gives ≥ 1) | 85% |
| F7b | the trace route agrees: ker(Dφ − 1) has dimension 1 | 90% |
| F7c | φ* permutes the three axis classes cyclically; its characteristic polynomial is λ³ − 1 | 70% |

## 4. The CKM part: the frame cannot be evaluated on the family (stated before the run)

The ask's third step, whether the CKM corner moves along the family at fixed lines, cannot be computed honestly. **It is
not attempted.** The reasons are read from the frame's code:

1. **The Q₈ is hard-coded.** The frame takes τ, the line w, the sector charges, the end L and the Higgs reading. It has
   no input for a holonomy pair or a puncture weight. The quaternion units label the channels and the generation blocks.
2. **The family moves the boundary.** If F3 and F6b hold, every point of the family other than s = 0 has boundary
   holonomy ≠ −1.
   - On the closed curve the bundle then carries a parabolic weight at the puncture.
   - The frame's kernels assume the puncture holonomy is −1. They have a simple pole and a null-quaternion residue
     (B1653), and the regularised norm's log cancels because the quaternion is null (B1656).
   - Off −1 the pole becomes z^(−1+α). A residue, a log-cancelling norm and the channel dual basis would each need a
     new definition.
3. **The channel structure breaks.** In frame C the channels are the four half-period shifts, a group Z₂ × Z₂ = Q₈/±1.
   Inference, not computed: along the dihedral sub-families (for example s₂ = s₃ = 0, where ρ stays in the normaliser of
   U(1)_I), the deformation would read as one half-shift moved off ½. The four shifts then no longer close as a group,
   which matches the commutator A² ≠ −1.
   - Extending the frame there is a design with at least three new choices: the kernel at a cone weight, the norm's
     regularisation, and which channels and blocks follow A, B, AB.
   - None of these is on the record. Choosing them here would manufacture the answer.

So the statement this card will defend is narrower. **At fixed lines, the frame has no point on the family except the
Q₈ point.** Whether a CKM corner "moves" along the family is undefined in the frame as built, not zero. An extended
frame would need its own sealed card. It is offered as a follow-up, not done here.

## 5. The pricing sentence, conditional on F1 to F6 holding as expected

> FL-08's restriction to finite-order lines prices only the lines w, the two real dimensions of H¹ with central
> coefficients, which no boundary condition touches (F5). The Q₈ part is rigid on the closed fibre and on the punctured
> fibre with the boundary held (F1, F3). Its three boundary-free classes are not three further continuous choices hidden
> in FL-08. Every one of them moves the cusp holonomy off −1 (F3, F6b), which the frame fixes by construction: the
> simple-pole Szegő kernel and the half-period channels. Holding the boundary at −1 is one discrete end condition,
> priced once, and it removes all three. On m004, with the monodromy imposed, one of the three survives (F7, if F7a
> holds) as the record's only continuous deformation of the Q₈ bundle, and it too moves the cusp.

If F3 or F6b fails, the sentence is withdrawn, and some boundary-free direction keeps the boundary at −1. The frame
could then be evaluated along it, and the CKM step reopens. If F7a gives 0 or 3, the last clause changes accordingly.

## 6. What is not checked

- That the frame's kernel bil realises exactly the holonomy pair (Q_I, Q_J). The card takes this from B1836's C6 and the
  frame's constants.
- That m004's monodromy is a ↦ ab, b ↦ bab, rather than a conjugate convention. Only the abelianised class is checked.
- Any physical reading of the surviving class. Any comparison with data.

## 7. Files

`relays/sm_r635/run.py`; the run will write r635_run.txt and r635_results.json beside it. The page will be
relays/SM_R635_BOUNDARY_FREE_CLASSES.md and the claim card relays/claims/CLAIM_2026-11-26_boundary_free_classes.md
(Phase 2, only when told).

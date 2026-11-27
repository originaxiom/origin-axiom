# SM-R635 — the boundary-free classes of H¹(fibre, ad Q₈): all three move the cusp, so FL-08 prices only the lines

*Page of the SM seat, 2026-11-26, for register row P-635 (main's page M53). Sealed card:
`relays/cards/SM_R635_the-boundary-free-classes.md`, committed and pushed before the run. One run of
`relays/sm_r635/run.py` (SHA-256 028eb8e8622d5a83, unchanged since the seal), run against main at be8c83d4f. Outputs:
`relays/sm_r635/r635_run.txt` (SHA-256 d0a9d4b5f681d6c2) and `relays/sm_r635/r635_results.json` (SHA-256
2029f473f77b7402). No post-hoc fix. Data-free: no measured value was read, printed or compared.*

## 1. Results against the sealed cells

| cell | sealed expectation | prior | result |
|---|---|---|---|
| G0 | the module's Q₈ relations; EPS = QJ; BLOCKS = (QJ, QI, QK); commutator −1 | 97% | **HOLDS**, every item |
| F1 | the closed torus: H¹ = 0 | 99% | **HOLDS:** H⁰ = 0, Z¹ = 3, B¹ = 3, H¹ = 0 |
| F2 | the punctured fibre, the boundary free: H⁰ = 0, H¹ = 3 | 99% | **HOLDS:** Z¹ = 6, B¹ = 3, H¹ = 3 |
| F3 | the boundary held: H¹_par = 0; the restriction to c has rank 3 | 99% | **HOLDS:** rank 3, H¹_par = 0 |
| F4 | each axis character gives 1 on F₂ and 0 on Z² | 97% | **HOLDS:** I, J, K: 1, 1, 1 and 0, 0, 0 |
| F5 | the lines: H¹ = 2 closed and punctured; restriction to c of rank 0 | 97% | **HOLDS:** 2, 2; rank 0 (H¹_par = 2) |
| F6a | rank 3 in (tr A, tr B, tr AB) at 0; tangents of rank 3 modulo B¹ | 95% | **HOLDS:** Jacobian diag(−2, −2, 2) |
| F6b | κ: zero gradient, positive-definite Hessian at 0; κ > −2 at every sampled s ≠ 0 | 92% | **HOLDS:** below |
| F7a | dim ker(φ* − 1) on H¹(F₂, ad) = 1 for every admissible P | 85% | **HOLDS:** four conjugators P, each gives 1 |
| F7b | the trace route agrees: ker(Dφ − 1) has dimension 1 | 90% | **HOLDS:** 1 |
| F7c | φ* permutes the three axis classes cyclically; characteristic polynomial λ³ − 1 | 70% | **HOLDS:** below |

The F6b detail:
- The gradient at 0 is (0, 0, 0).
- The Hessian is 8·1₃.
- On the 2000 sampled points, the smallest (κ + 2)/|s|² is 0.416.
- The Fricke identity residual is 1.4 × 10⁻⁴⁰ (numerical, as disclosed in the card).

The F7c detail:
- The two routes give the same characteristic polynomial, (λ − 1)(λ² + λ + 1) = λ³ − 1.
- Dφ = [[0, 0, 1], [−1, 0, 0], [0, −1, 0]], a signed cyclic permutation whose signs multiply to +1.
- The fixed direction is (dx, dy, dz) ∝ (1, −1, 1). In the family's coordinates that is s ∝ (−1, 1, 1), equal weight on
  the three axes.

**Plants** (each had to come out as stated):

| | what | must give | result |
|---|---|---|---|
| P1 | the reducible pair (Q_I, Q_I) on the closed torus | H¹ > 0 | **as required:** H¹ = 2 (H⁰ = 1) |
| P2 | a generic irreducible rational pair on F₂ | H¹ = 3, H¹_par = 2 | **as required:** 3, 2 (restriction rank 1) |
| P3 | the trivial representation | H¹ = 6 on F₂ and on Z² | **as required:** 6, 6 |
| P4 | φ* on the trivial representation | ker(φ* − 1) = 0 | **as required:** 0 for all 24 coefficient maps |

**Every sealed cell holds, and every plant comes out as required.** No expectation failed.

## 2. Reading

- **The dimension 3 is confirmed by a second route.** The Fox-calculus computation shares no code with B1836's C6, and
  it reproduces B1836's three numbers: 0 closed, 0 held, 3 free.
  - The three classes are one per quaternion axis. Each is a non-trivial character of Z₂ × Z₂ = Q₈/±1 and contributes
    exactly 1 (F4).
  - The plants show the instrument can see classes where they exist: a reducible pair gives 2, and a generic pair keeps
    2 classes with its boundary held.
- **Every boundary-free direction moves the cusp holonomy.**
  - The restriction to the boundary loop is injective on H¹ (F3).
  - Along the explicit family, κ = tr[A, B] rises off −2 quadratically in every direction, with Hessian 8·1₃ (F6b).
  - So no point of the family other than Q₈ keeps the puncture holonomy at −1.
- **The lines are separate.** The centre u(1) carries 2 classes on both the closed and the punctured fibre, and its
  restriction to the boundary is zero (F5). "At fixed lines" is well defined, and the lines never touch the boundary
  condition.
- **On m004 one class survives** (F7, on the premise φ: a ↦ ab, b ↦ bab). The monodromy permutes the three axis classes
  cyclically, and its fixed line is the equal-weight combination. By the Wang sequence, with H⁰ = 0, dim H¹(m004; ad)
  = 1 for the extended representation. This meets the half-dimension bound exactly, and it too moves the cusp (F3).

## 3. The pricing sentence (F3 and F6b hold, so it stands as sealed)

> FL-08's restriction to finite-order lines prices only the lines w, the two real dimensions of H¹ with central
> coefficients, which no boundary condition touches. The Q₈ part is rigid on the closed fibre and on the punctured fibre
> with the boundary held. Its three boundary-free classes are not three further continuous choices hidden in FL-08.
> Every one of them moves the cusp holonomy off −1, which the frame fixes by construction: the simple-pole Szegő kernel
> and the half-period channels. Holding the boundary at −1 is one discrete end condition, priced once, and it removes
> all three. On m004, with the monodromy imposed, one of the three survives as the record's only continuous deformation
> of the Q₈ bundle, and it too moves the cusp.

## 4. The CKM corner along the family: not evaluable, as sealed

The card stated before the run (§ 4) that the frame cannot be evaluated on the family, and the run confirms the premise
that matters: no point of the family other than Q₈ has puncture holonomy −1 (F3, F6b).

- The frame's Q₈ is hard-coded. It has no input for a holonomy pair or a puncture weight.
- Its kernels, residues, norms and channel group assume the holonomy −1.

So at fixed lines the frame has exactly one point on the family, and **whether the CKM corner moves along it is
undefined in the frame as built, not zero**. A deformed frame would need at least three new choices:
- a kernel at a cone weight;
- the regularisation of the norm;
- which channels and blocks follow A, B and AB.

It would need its own sealed card. Inference only, not computed: the dihedral sub-families, for example s₂ = s₃ = 0,
read as one half-period shift moved off ½. That is the natural first design for such a card.

## 5. What is not checked

- That the frame's kernel bil realises exactly the holonomy pair (Q_I, Q_J). This is taken from B1836's C6 and the
  frame's constants; G0 checks only the constants.
- That m004's monodromy is a ↦ ab, b ↦ bab, rather than another automorphism in the same outer class. Only the
  abelianised matrix [[1, 1], [1, 2]] is checked.
- The global shape of the family, beyond the 2000-point ball |s| ≤ 0.5.
- Any physical reading of the surviving class, any CKM value, and any comparison with data.
- A second computation by another seat.

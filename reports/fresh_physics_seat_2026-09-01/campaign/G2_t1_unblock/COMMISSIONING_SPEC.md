# COMMISSIONING SPEC — the minimal committed input set that determines the 27 connecting-block values

To: codex (R023 continuation). From: cell G2_t1_unblock, 2026-09-01. This is the exact input
set which, if committed to this tree, determines the 27 entries `T[i,j,conn_k]` of the selected
`(A_7, B_6, B_2)` down block over `Q(zeta_12)` — and with them the fork of B1232 (ANNIHILATES vs
OBSTRUCTED) by mechanical substitution into the already-committed criterion (T1/s2) and
instrument (T1/s3). Minimality is proved in this cell: dropping any item leaves the values
movable by an explicitly exhibited freedom (g2's group G, generic orbit dim 27), and the
committed record currently determines them up to nothing at all (g2 Theorem A).

Conventions binding this spec (E23; state deviations explicitly if your frames differ):
`chi_r(g) = zeta_12^r` on the marked C12 generator of YUKAWA_CUP_PRODUCTS_308.md; physical =
raw twisted by `chi_{-2}` applied ONCE to B; `chi_{-3}` carried by `Delta_G`, never applied to
B; Serre duality inverts phase; connecting quotient = SUB, Serre-dual tail = QUOTIENT of B;
splittings `s_t(1) = bhat_2 + sum_k t_k c_k`.

## The input set (commit ALL of I1–I6; each kills one exhibited freedom)

- **I1 — the defining data.** The exact 44-coordinate height-308 map `Phi` (all coefficients,
  over `Q(zeta_12)`, in the ordered twelve-ray Cox frame), the norm hypersurface `f`, and the
  chart/orbit combinatorics of the 432 refined opens `U_(sigma,a)`. Equivalent acceptable form:
  commit `certify_yukawa_down_tail_cech_308.sage` AND its full input data files (this also
  pays the standing E51 dual-homing debt — the file has NEVER been committed on any branch of
  this repo; verified in g1 route B). *Freedom killed: all of them — without I1 nothing is
  computable (g1 receipt C: all 10 value-determining inputs absent).*

- **I2 — the chosen bases (the frame identification R024 could not supply).** (a) The three
  `A_7` connecting representatives `a_i` (the `H^0(L)` sections `c_i` and/or the relevant
  columns of the 42-polynomial quotient basis); (b) the two `B_6` connecting columns
  (33-column indices 17, 18) and three `B_2` connecting columns (indices 6, 7, 8) of the
  672×33 representative matrix, lifted to characteristic 0 (or with the good-prime lift
  procedure committed); (c) the `H^0(K)` sections `k_j` behind `b_j = delta r(k_j)`.
  *Freedom killed: the `GL_3(A) × GL_2(B_6,conn) × GL_3(B_2,conn)` block of G (dim 22 of 27).*

- **I3 — the determinant comparison.** `Delta_G : det(G) ≅ L` fixed on the ordered twelve-ray
  and six-Euler frames, with its alpha-independence and equivariant-phase certificate (the
  spec's own "must be certified" line). *Freedom killed: the `chi_{-3}`-carrying phase.*

- **I4 — the normalized trace.** `Tr_(Y,Omega) : H^3(O_Y) -> Q(zeta_12)` with
  `Omega_Y = Res_Z(Omega_Z/f)` — commit the normalization scalar's derivation, not only its
  use. *Freedom killed: the global `K^x` scale (the last +1 of dim G).*

- **I5 — the tail realization for `bhat_6`.** The Serre chain map `S : (coker D)^* -> Z^1(U,E)`
  and the solved `h_6` with `bhat_6 = e_6 - delta r(h_6)`, PLUS the `C^18 -> C^21` matrix `D`
  itself and the dictionary `e_i` ↔ Cox monomial (without which the five committed tail-row
  coordinate strings are value-inert — g1 route E). *Needed because 9 of the 27 entries are
  tail6/conn: the 1×18 connecting row ALONE decides only 18 of 27 — see the count note below.*
  *Freedom killed: the unipotent radical of `P(B_6)` (the tail-lift shifts).*

- **I6 — the values, in the two-tier form the spec itself prescribes.**
  (a) `GF(1009)` values of the 27 entries (and ideally all 36): a nonzero pivot certifies
  OBSTRUCTED at characteristic 0 immediately;
  (b) the exact `Q(zeta_12)` row: required to certify ANNIHILATES (a zero row mod one prime
  does not — the spec's own caution; three good primes raise confidence, only char 0 closes).

## Acceptance gates (run before the verdict is read off; all are failable)

- **G1** `Delta_G` alpha-independence + equivariant phase: certified, not asserted.
- **G2** Čech cocycle identities for every committed representative (your existing checks).
- **G3 — planted known case:** the evaluator MUST reproduce the committed SKEW ZERO — the
  repeated `(4,4)` pure-tail channel evaluates to exactly 0 over `Q(zeta_12)`. An evaluator
  that does not return this zero is broken; an evaluator that returns 0 on a GENERIC bite
  control (G4) is also broken.
- **G4 — bite control:** evaluate one deliberately mismatched input (e.g. a `rho+sigma ≠ 8`
  channel forced through the contraction, or a perturbed non-cocycle) and show a NONZERO /
  failing result. (Criteria failable both ways — MB12.)
- **G5** char-0 row reduced mod 1009 must equal the independently computed `GF(1009)` row.
- **G6** C12-equivariance of the output tensor: entries transform by the predicted characters;
  the physical-shift bookkeeping `(+1,-2,-2)` applied once, sum ≡ 0.

## The count note (resolves T1's flagged 27-vs-9 discrepancy — please confirm or correct)

On the committed census (36 = 18 conn/conn + 9 tail6/conn + 6 conn/tail2 + 3 tail6/tail2),
*annihilation of C* = vanishing of the **27** entries whose Higgs (`B_2`) leg is connecting =
18 + 9. The "nine-entry" phrase of B1232 matches the per-direction 3×3 family matrix or a
lepton-specific count, not the down annihilation condition. If your lepton computation uses a
different count, commit the lepton census alongside.

## What this determines, precisely

Given I1–I5 the 27 values are determined ABSOLUTELY (the freedom group G of g2 is fully
gauge-fixed); given only I2 without I3/I4 they are determined up to one global `K^x` scalar and
a phase — still enough to decide the FORK (vanishing is scale-invariant), so **a minimal
fork-deciding subset is I1 + I2 + I5 + I6(a)** if OBSTRUCTED, plus I6(b) if ANNIHILATES.
Committed today, the verdict is one substitution away (T1/s2 criterion + T1/s3 instrument).

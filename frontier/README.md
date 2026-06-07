# Frontier — Quarantined Phase B Work

This directory holds **speculative, `open`-status** research — see `../CLAIMS.md`
(O1–O9) and `../GOVERNANCE.md`. Nothing here is a claim; results are logged
observations only.

A result moves from here into the proven core (`../src/`) **only** by passing the
`conditional → proven` gate in `GOVERNANCE.md` §5 — code, a test, scrutiny, and a
logged status change.

**Phase B is in progress.** Probes logged so far:

## Dependency Graph

```text
B13-B16 established the current kernel:
  A1-A6 -> A
  (L X)^2=A -> X=+/-P
  F=L P, F^2=A
  trace lift of F contains the A-sector

B18 trace-lift functoriality
  gates B20, B21, B23, B24

B19 exchange/half-step axiom audit
B17 alternation/persistence selector
B22 spectrum genericity controls

B20 operational awareness test
B21 spacetime / Weil-Petersson dictionary test
B23 BKL / gravity controls
B24 anyon / quantum bridge

B25 Fibonacci spectrum anchor
  depends on B18/B22 and tests the lambda/h=1 spectral bridge

B26 lambda/h=1 derivation attempt
  tests whether projective half-return self-similarity derives lambda/h=1

B27 SL(3) Fibonacci trace lift
  extends the trace-lift calculation to higher-rank character data

B48 SL(3) metallic trace-map certificates
  generalizes B27 from m=1 to phi_m(a)=a^m b, phi_m(b)=a and supports PC12

B49 SL(3) certificate-to-proof hardening
  decomposes PC12's fixed-line splitting certificate into proof modules

B50 PC12 proof-draft assembly
  assembles B48/B49 into an internal theorem-note skeleton

B51 SL(3) symbolic-m factorization
  proves the c=3 fixed-line block factorization with m formal

B52 multichannel Fibonacci bridge control
  shows the naive 3-channel tight-binding bridge gives 6x6 symplectic transfer
  matrices and fails the PC12 third-order trace recursion

B54 general-c exchange structure
  generalizes B51: [J(m,c),P]=0 for symbolic c (whole fixed line); c=1
  Eisenstein/golden twins; m=1 cyclotomic sweep

B55 c=1 fixed-line structure (general m)
  completes B54's c=1 row: symmetric mod-4 (Phi6/Phi4/(t-1)^2), antisymmetric
  (t-1)(t+1)(t^2-mt-1)=char(M) for all m

B56 figure-eight invariant-surface negative control
  diagonal SL(2,C) reps have I in {4,-17/2+-7sqrt5/2}, none=1/4; figure-eight
  I=1/4 bridge DEAD; c=1 Eisenstein resemblance is a cyclotomic coincidence

B57 general-m Diophantine splitting classification
  {c=1,c=3} universal splitting points; m-dependent extras (m=1..6); Hilbert
  class-field coincidence killed for m>=2

B58 SL(4) factor-count tower test (attempt)
  confirms SL(4) identity recursion (r-1)^4 + cubic derivatives; full 15x15
  ambient Jacobian needs SL(4) trace identities; verdict NEEDS-EXPERTISE

B59 SL(4) fixed-line factorization (numerical; resolves B58)
  method validated on SL(3) ground truth; SL(4) = char(M^k){-1,1,2,3,4} x
  char(-M^2) x (t-1)^2(t+1); refutes the 7-char(M^k) tower prediction

B60 SL(n) tower: cross-n structure map (n=3,4) + SL(5) barrier
  generalizes B59; n=3 powers{-1,2,3}, n=4 powers{-1,1,2,3,4}+char(-M^2)+deg-3
  parity; SL(5) unresolved (cond~1e11)

B61 SL(5) high-precision factorization (resolves B60's "barrier")
  SVD pinv at dps 60: B60's wall was a rank-23 word set; inverse-word coords give
  rank 24, and 22 of 24 SL(5) multipliers resolve (powers{-1,1,1,2,3,4,5},
  signs{-2,-3}, parity deg 4); last 2 a method limit (fixed-line rank-loss)

B62 opposition involution: the 2 unresolved SL(5) modes (live structural)
  exchange involution = opposition involution theta=-w0; height-2 root-space split
  reproduces SL(3)/SL(4) and gives char(M^2)^2.char(-M^2) for SL(5), so the 2
  unresolved = second char(M^2) = {phi^2, 1/phi^2}; exact split, not yet proved

B63 SL(4) factorization over Z[m] (computer-assisted symbolic; proves B59 for all m)
  SL(4) gauge-clean -> high-precision Jacobian at m=1..6, factor sums = exact
  tr(M^k), interpolated to L_2=m^2+2, L_3=m^3+3m, L_4=m^4+4m^2+2; M-power/sign/
  parity structure m-INDEPENDENT; trace ring needs Lambda^2/multi-block (open)

B64 parity mechanism: proof of the tower's k(alpha) sector assignment (symbolic)
  depth-n CH (J polynomial in m) + P=contragredient (m->-m) + Dickson parity
  L_k(-m)=(-1)^k L_k(m) => even-|k| char(M^k) P-symmetric, odd-|k| P-antisymmetric;
  full symbolic-m for SL(3); SL(4) sectors assigned; obstruction = e_2/Lambda^2

B65 symbolic SL(4) Jacobian J(m), char poly factored over Z[m]
  single-block V+Lambda^2 spans only 12/15 (multi-block unavoidable); instead the
  canonical degree-4-in-m Jacobian entries are reconstructed from high-precision
  numerics (over-determined) and char(J(m)) is factored DIRECTLY as char(M^-1)
  char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1); computer-assisted
  entries + exact symbolic factorization (trace ring B58 still the purist open)

B28 projective quotient legitimacy
  controls whether the B26 sign quotient is canonical in lift-independent data

B29 hierarchy/normalization controls
  audits the Lucas hierarchy, full-return control, and lambda/h normalization

B30-B32 selector-first campaign
  proves the quotient is canonical conditional on PSL data, then isolates S1 as
  the extra A-sector self-similarity selector still not derived

B33-B36 extension controls
  test SL(n), Goldman/WP, topology, and Fibonacci-renormalization routes

B37 operational feedback quarantine
  locks feedback language to computable predicates and rejects awareness claims

B38-B47 deep S1 campaign
  shows arithmetic/torsion/filter reuse would force S1, but only conditional on
  T1: tangent return inherits original arithmetic persistence filters

docs/TRACE_SELECTOR_THEOREM.md / C5
  packages B38-B47 as the conditional theorem
  T1 -> S1 -> I=1/4 -> lambda/h=1
```

- **B1–B5** — gluing vs. Chern–Simons flatness, moduli evolution, Regge complex,
  BKL/Gutzwiller, Wheeler–DeWitt.
- **B6–B9** — the field-theoretic lift of the derived potential (P15/P16):
  the field equation `□τ+κ(τ²−τ−1)=0` (B6), Fisher–KPP creation dynamics (B7),
  the particle spectrum and the non-exact `m/g≈φ` near-miss (B8), and the
  fusion–scattering shared polynomial (B9). Each carries its caveat; none is a
  claim. See `../PROGRESS_LOG.md` 2026-05-27.
- **B13** — the punctured-torus trace map on the fiber character variety. Exact
  algebra shows the trace-map linearization contains the `A` quadratic as a
  lattice-conjugate rank-2 sector, but the bridge to physical `3+1`, matter,
  gravity, or awareness remains an inserted dictionary.
- **B14** — the half-step square-root selector. Exact algebra shows `A` has only
  two `GL(2,Z)` square roots, `F=L P` and `-F`, and that mixed closures
  `B(a,b)=L_aR_b` admit an integer orientation-reversing square root iff `a=b`.
  The remaining gap is whether the record-swap `P` is forced or inserted.
- **B15** — trace-map invariant controls. Exact algebra confirms the
  Eisenstein-to-golden diagonal linearization family and the discrete
  Fricke-Vogt invariant; it rejects the naive continuum proxy and rejects a
  proposed `sqrt(5)` Fibonacci coupling under the current invariant
  normalization.
- **B16** — record-swap status. Exact algebra shows `P` is unique up to sign as
  the involution exchanging the primitive pair `{L,R}`, but the exchange
  symmetry itself is not forced by the current A1-A6 minimal-record axioms.
- **B17-B24** — half-step kernel campaign. B18 establishes the trace map as the
  canonical half-step trace lift; B19/B17/B22 control the exchange, alternation,
  and spectrum claims; B20/B21/B23/B24 test awareness, spacetime, gravity, and
  anyon dictionaries and leave them stalled where no dictionary is derived.
- **B25** — Fibonacci spectrum anchor. Finite approximants at dimensionless
  `lambda/h=1`
  support a mid-scale box-counting slope near `0.75` and pass strict
  gap-labeling controls. In B25 alone, `lambda/h=1` is only motivated; later C5
  makes it conditional on T1, not proven.
- **B26** — `lambda/h=1` derivation attempt. Exact algebra shows `lambda/h=1` is
  uniquely selected by projective half-return self-similarity, but the
  projective half-return criterion itself remains an added rule. Verdict:
  `STALLED`, with B25 strengthened but not promoted.
- **B27** — `SL(3)` Fibonacci trace lift. Exact algebra gives an
  eight-dimensional trace map whose fixed-point Jacobian factors into golden
  sectors `(t-1)(t+1)(t²-4t-1)(t²-3t+1)(t²+t-1)`. The `A` sector survives and
  the commutator trace pair swaps under the half-step. Physical
  particle/antiparticle language is rejected as an unbuilt dictionary.
- **B48** — metallic `SL(3)` trace-map certificates. The B27 `m=1` lift extends
  to `phi_m(a)=a^m b, phi_m(b)=a`, with exact recurrence checks, commutator
  trace-pair invariant, entropy controls, fixed-line arithmetic classification,
  and compact `SU(3)` diagonal-slice representatives. This supports PC12 as
  standalone trace-map arithmetic and does not change PC11's T1-conditional
  selector status.
- **B49** — `SL(3)` certificate-to-proof hardening. The B48 fixed-line
  splitting classification is decomposed into a universal splitting criterion,
  direct positive families, square-gap propagation, finite positive-strip
  exclusions, and negative-strip/boundary exclusions. PC12 is strengthened but
  remains `NEEDS_VALIDATION`.
- **B50** — PC12 proof-draft assembly. B48/B49 are organized into an internal
  theorem-note skeleton with five theorem blocks and explicit non-claims. This
  makes PC12 structurally ready for proof drafting, not public release.
- **B51** — `SL(3)` symbolic-`m` factorization. The `c=3` fixed-line derivative
  rows are derived from the `(r-1)^3` triple-root recurrence, the symbolic `8x8`
  Jacobian commutes with the exchange involution, and the symmetric /
  antisymmetric block characteristic polynomials are proved for formal `m`.
- **B52** — multichannel Fibonacci bridge control. The simplest three-channel
  Fibonacci tight-binding model yields `6x6` determinant-one symplectic transfer
  matrices. In the commuting control it decouples into three `SL(2)` channels,
  and in the generic control it obeys an order-six trace recursion, not PC12's
  `SL(3)` third-order recursion. Verdict: useful negative control, no physics
  bridge.
- **B54** — general-`c` exchange structure. `[J(m,c),P]=0` is proved for symbolic
  `c`, so the exchange block-diagonalization holds on the whole fixed line, not
  only at B51's `c=3` (the reason is structural: `P`-equivariance at the
  `P`-invariant fixed line). At `c=1` the symmetric sector is the Eisenstein
  quadratic `t^2-t+1` and the antisymmetric is the golden `t^2-t-1`
  (discriminants -3 and 5 — the same pair as the P12 figure-eight gluing
  equation); for `m=1` the symmetric quadratic `t^2-ct+1` sweeps
  `Phi_3, Phi_4, Phi_6, (t-1)^2, char(A)` at `c=-1..3`. Standalone trace-map
  math; no claim promoted.
- **B28** — projective quotient legitimacy. The B26 sign flip is legitimate as
  a central-sign / `PSL` lift ambiguity at the special orbit, and the trace map
  is equivariant under that sign action. The choice to use the quotient as a
  selector remains an added bridge criterion.
- **B29** — hierarchy and normalization controls. The Lucas hierarchy selects
  dimensionless `(lambda/h)^2=L_n-2` under the projective criterion; literal
  full-return matching gives a different hierarchy. Finite spectral controls at
  the first hierarchy values pass gap-labeling checks, but no physical
  prediction is promoted.
- **B30-B32** — selector-first campaign. B30 shows the central-sign quotient is
  canonical if the state space is lift-independent `PSL` trace data; B31 shows
  primitive projective return alone leaves `I=c²-1` free; B32 isolates the
  remaining missing object as S1, the extra rule that the primitive projective
  return linearization reproduce the original `A` sector.
- **B33-B36** — extension controls. The `SL(3)` tower decomposes into
  symmetric-power sectors but no full `SL(n)` trace theorem is built; the
  Goldman/WP bracket and sign topology support the quotient but do not select
  `I=1/4`; Fibonacci spectral/gap controls remain compatible with many
  couplings and do not independently select `lambda/h=1`.
- **B37** — operational feedback quarantine. Feedback and invariant language
  are reduced to computable predicates; awareness/consciousness/religion/
  metaphysics-adjacent interpretations remain outside the claim system.
- **B38-B47** — deep S1 campaign. B38/B43/B44/B45 show that integer
  hyperbolic trace, minimal discriminant, torsion-one closure, or primitive
  renormalization hierarchy each recover `I=1/4` if applied to the tangent
  return. B39/B40/B41/B42/B46 show that this filter inheritance is not derived
  by the current framework. B47 records the clean verdict:
  `T1 -> S1 -> I=1/4 -> lambda/h=1`, where T1 is an explicit conditional
  assumption. `../docs/TRACE_SELECTOR_THEOREM.md` packages that verdict as C5;
  the files here remain frontier evidence, not proven claims.
- **B55** — c=1 fixed-line structure for general `m`. Completes B54's `c=1` row:
  the symmetric sector is **mod 4** (`Φ₆` for `m≡1,3`; `Φ₄` for `m≡2`; degenerate
  `(t−1)²` for `m≡0`) and the antisymmetric sector is `(t−1)(t+1)(t²−mt−1)=char(M)`
  for all `m`. Proved per residue class via the `c=1` closed forms (roots
  `{1,i,−i}` + a resonant linear term); `m=1` reproduces B54's twins.
- **B56** — figure-eight invariant-surface negative control. The diagonal
  `SL(2,C)` reps `w³−2w²−2w+1` give Fricke–Vogt `I ∈ {4, −17/2 ± 7√5/2}`, none
  `= 1/4`, so the figure-eight ↔ `I=1/4` (self-evidencing) bridge is **dead**; the
  `c=1` Eisenstein resemblance to the figure-eight tetrahedron shape is a
  cyclotomic coincidence. The separate P12 gluing-equation echo is unaffected.
- **B57** — general-`m` Diophantine splitting. Classifies integer splitting of the
  antisymmetric quartic for `m=1..6`: `{c=1, c=3}` universal, m-dependent extras,
  counts `[4,4,4,3,2,5]`; the Hilbert-class-field coincidence is killed for `m≥2`.
  Extends PC12's Theorem-4 content. Standalone trace-map math; no claim promoted.
- **B58** — SL(4) factor-count tower test (attempt). Confirms the mechanism (the
  `SL(4)` identity recursion is `(r-1)^4`, so derivative sequences are cubic in
  `k`; degree `n-1`) and the obstruction (the fixed-line point is the degenerate
  identity representation, traces second-order, so a representation-based numerical
  Jacobian cannot recover the ambient map). The full `15×15` ambient Jacobian
  needs the SL(4,C) 15-coordinate trace map (Procesi + substitution action), not
  built here. Verdict `NEEDS-EXPERTISE`; the SL(4) 7-factor prediction is untested.
- **B59** — SL(4) fixed-line factorization (numerical). Resolves B58 by
  extrapolating the ambient Jacobian
  `DT(eps)=D[tr W_i(AB,A)] . pinv(D[tr W_j(A,B)])` to `eps=0` (validated to ~4
  digits against B55's SL(3) `c=3` spectrum). The SL(4) spectrum factors as
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4) . char(-M^2) . (t-1)^2(t+1)`:
  5 clean `char(M^k)` (k=-1..4), a sign sector `char(-M^2)`, and a degree-3
  parity block. **Refutes** the naive `7 char(M^k) + parity` prediction.
  Numerical, method-validated; not a symbolic proof.
- **B60** — SL(n) tower: cross-n structure map + SL(5) barrier. Generalizes B59
  and tabulates the corrected tower: n=3 `{-1,2,3}` / no sign / parity deg 2;
  n=4 `{-1,1,2,3,4}` / `char(-M^2)` / parity deg 3 (the powers climb, a sign
  sector appears, the parity block grows). **SL(5) is unresolved** — `cond(Dx)
  ~1e11` defeats double-precision extrapolation and `mpmath` normal-equations
  pinv (squared to `~1e22`); a stable high-precision SVD solver or the symbolic
  ambient SL(5,C) trace ring is required. Numerical, validated for n=3,4.
- **B61** — SL(5) high-precision factorization (resolves B60's "barrier").
  A stable SVD pseudoinverse at dps 60 shows B60's `cond ~1e11` was the
  double-precision rounding floor hiding a **rank-23** forward-only word set;
  inverse-word coordinates (`A,B,A^-1,B^-1`) restore rank 24 at `cond ~1e4`, and
  **22 of 24** SL(5) multipliers resolve to the catalog
  (`char(M^-1)·char(M)^2·char(M^2..5)·char(-M^2)·char(-M^3)·(t-1)^2(t+1)^2` —
  the n=5 tower row). The last 2 are a **method limit**: fixed-line rank-loss
  makes the pinv `eps->0` limit gauge-dependent (residual scatters across seeds),
  needing the symbolic ambient SL(5,C) ring. SL(3)/SL(4) reproduce to
  `~4e-14`/`~3e-9`. Numerical, high-precision; no claim promoted.
- **B62** — opposition involution: the 2 unresolved SL(5) modes (live structural
  result). The B61 numerics cannot decide them (`tr(DT0)`/`det(DT0)` scatter
  across seeds). Instead, identifying the exchange involution with the opposition
  involution `theta=-w0` on the `sl(n)` root system: its eigenspace split on the
  height-2 root space is exact and reproduces SL(3) (`char(M^2)`) and SL(4)
  (`char(M^2).char(-M^2)`); for SL(5) it gives `char(M^2)^2.char(-M^2)`, so the 2
  unresolved modes are a **second `char(M^2)` = {phi^2, 1/phi^2}** (residual modes
  are positive, corroborating). Exact root-system split, validated on SL(3)/SL(4),
  numerically corroborated; a symbolic proof still needs the ambient SL(5,C) ring.
  No claim promoted.
- **B63** — SL(4) factorization over Z[m] (computer-assisted symbolic; proves B59
  for all m). Building the symbolic Procesi trace ring (B58) is harder than "one
  level deeper": `e_2(A)` forces the 6-dim `Lambda^2` representation (depth-6) or
  multi-block words `tr((A^m B)^2 A)` — documented as the real reason B58 is open.
  Instead, SL(4) being gauge-clean, the high-precision Jacobian is computed for
  `m=1..6`; each factor's eigenvalue sum is the exact integer `tr(M^k)`, and
  interpolation gives `char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)`
  with `L_2=m^2+2, L_3=m^3+3m, L_4=m^4+4m^2+2`. This PROVES the factorization over
  `Z[m]` and that the M-power/sign/parity structure is **m-independent** (m=1
  reproduces B59). The explicit `k(alpha)` root map is from B62; the hand-built
  trace ring stays open. No claim promoted; proven core P1-P16 unchanged.
- **B64** — parity mechanism: a symbolic proof of the tower's `k(alpha)`
  sector-assignment. Depth-`n` Cayley-Hamilton makes the fixed-line Jacobian
  polynomial in `m`; `P` = contragredient sends `m -> -m`; Dickson parity
  `L_k(-m)=(-1)^k L_k(m)`. Hence **even-|k| `char(M^k)` is P-symmetric, odd-|k|
  P-antisymmetric** (B62's root-height split, now explained). Verified in full
  symbolic-`m` form for SL(3): symmetric=`(t-1)(t+1)char(M^2)`, antisym=
  `char(M^-1)char(M^3)`. Applied to SL(4): even-k `{M^2,M^4,-M^2}` symmetric,
  odd-k `{M^-1,M,M^3}` antisymmetric. The depth-4 derivative sequences are built;
  a full symbolic SL(4) Jacobian's one remaining need is localized to
  `e_2=tr(Lambda^2 A)` (the 6-dim exterior square). No claim promoted; proven
  core P1-P16 unchanged.
- **B65** — the symbolic SL(4) fixed-line Jacobian `J(m)`, char poly factored over
  `Z[m]`. A rank check shows single-block V+`Lambda^2` traces span only 12/15
  (mixed two-block words unavoidable; sharpens B64). Sidestepping the hand-built
  trace ring: the Jacobian entries in the B59 word basis are canonical
  (seed-independent) degree-4-in-`m` rationals, reconstructed from high-precision
  numerics for `m=1..7` (over-determined: degree 4 fixed by 5 points, checked on
  7), giving `J(m)` over `Z[m]`. `sympy.factor(char(J(m)))` =
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)` — matches
  B63/B64, `m=1`=B59. The factorization is now *derived* (direct factoring of the
  full Jacobian), not matched. Computer-assisted entries + exact symbolic
  factorization; the from-first-principles Procesi trace ring (B58) is the purist
  open item. No claim promoted; proven core P1-P16 unchanged.
- **B66** — the SL(6) numerical fixed-line tower (35-dim), settling the tower
  multiplicity formula. Extends the inverse-word method (B61) to `n=6`, the
  smallest `n` where `max(n-d,1)` (=> 3) and the saturating alternative (=> 2)
  differ for the |k|=3 sector. The opposition-involution theta-split sector dims
  are exact (`sector_prediction(6)=(9,6,5)`: 9 odd-height + 6 even-height
  quadratics + 5 parity = 35; the 35 total validates SL(3)=8/SL(4)=15/SL(5)=24 —
  the 9/6 is a root-HEIGHT count, = char(M^k) |k|-parity only for odd n: SL(4) is
  |k|-parity (3,3) but height (4,2), since |k| runs past the maximal height). The numerics resolve the
  |k|=3 region cleanly — all four roots of `char(M^3)`={4.236,-0.236} and
  `char(-M^3)`={-4.236,0.236} on the catalog (dist <= 4e-4), exactly **two**
  quadratics; the lone extra big-root mode (-4.434) has no small-root partner, so
  it is gauge-corrupted, not a third factor. Hence **|k|=3 multiplicity = 2 (same
  as SL(5)) — `max(n-d,1)` REFUTED.** Honest limit: the SL(6) fixed-line rank-loss
  is severe — 26/35 resolve, 9 are gauge-corrupted (3 complex pairs + 3 real
  outliers; the B62 mechanism amplified from SL(5)'s 2 modes), so the full
  15-quadratic profile is not completely determined, but the |k|=3 quadratics
  resolve and number 2 — the test. Symbolic proof for `n>=5` still needs the
  ambient SL(n,C) trace ring (B58). No claim promoted; proven core P1-P16 unchanged.
- **B67** — the figure-eight knot A-polynomial, derived **exactly** from the
  trace-map fixed-point set (cross-validation against published algebraic topology).
  The figure-eight complement is the once-punctured-torus bundle with monodromy
  `phi=[[2,1],[1,1]]=M^2` (trace map `T_1^2`); a fiber rep extends over the bundle
  iff its character is `T_1^2`-fixed, so the fixed locus `y=z=x/(x-1)` is the
  A-polynomial curve. At each fixed point the monodromy `t` (`tAt^-1=A^2B,
  tBt^-1=AB`, verified ~1e-15) gives meridian `M=eig(t)`, longitude `L=eig[B,A]`;
  with `tr(t)^2=(x^2+x-1)/(x-1)` (50-digit) and `kappa=tr[A,B]`, the trace identity
  is `kappa=tr(t)^4-5tr(t)^2+2`, and eliminating `x` yields
  `A(M,L)=M^4L^2+(-M^8+M^6+2M^4+M^2-1)L+M^4` = Cooper-Long (1996), **exactly**. First
  derivation of this A-polynomial from a trace map; connects the SL(n) tower to
  character-variety knot invariants. SL(3) (Garoufalidis-Thurston-Zickert 2011) is
  the open next step. No claim promoted; proven core P1-P16 unchanged.
- **B68** — AJ-conjecture check for the figure-eight (SHELVED, no claim). The
  colored Jones (Habiro form) is q-holonomic with **minimal recursion order 2**,
  matching the L-degree of the B67 A-polynomial, and the order-2 recursion
  annihilates `J_N` for `N=2..5`. But the exact `recursion|_{q=1}=A` identity does
  not resolve (the convention `M_rec=q^N=meridian^2` + an ill-conditioned `q→1`
  nullspace); order-match alone is below B67's exact-identity bar. Kept as a labeled
  exploratory probe only. No ledger claim; proven core P1-P16 unchanged.
- **B69** — the metallic family of A-polynomial / trace-relation curves + a
  cusp-torsion law (computer-assisted, VERIFIED m=1..4; m=1 PROVED via B67). The
  trace-relation curve `F_m(x,κ)=0` (projection of the `T_m²` fixed locus to
  `x=tr a, κ=tr[a,b]`) extends the figure-eight (m=1) to the metallic family
  (`m=2: κ=(x⁴−6x²+12)/(x²−2)`, etc.). **Cusp-torsion law:** the cusps (poles of κ)
  sit at elliptic-torsion values `x=2cos(π/k)`, `k∈{3..m+2}`, `k≡m (mod 2)`. The
  banked "breakthrough-chat" handoff after independent re-derivation + a line-by-line
  audit (which caught a `κ`-sign diagnostic bug — the complete structure is `κ=−2`,
  not `+2`). **Novelty (`NOVELTY_CHECK.md`):** STANDARD_REPACKAGE — the cusp law is the
  known Baker–Petersen ideal-point structure of once-punctured-torus bundles
  (arXiv:1211.4479), repackaged through the trace map, not new. Ledger V35/V39/V40.
  No claim promoted; proven core P1-P16 unchanged.
- **B70** — the trace-ring proof attack (Phase-8 Track A): the SL(n) two-block
  obstruction is RANK-1 at leading order, but its e₂-sector closure is a
  **bounded multi-generator** problem. The candidate `a_d` formula (B62 θ-split)
  is unproven; the proof needs the ambient SL(n,ℂ) trace ring, whose barrier is the
  even-k / `e₂=tr(Λ²A)` sector carried by two-block words `tr(AᵃBAᵇB)`. On the
  proper traceless `sl(n)` tangent, the **leading-order (ε²) Hessian** non-separable
  content is a *single* rank-1 coupling `a·b·tr(X²)`, pinned exactly to `e₂` (the
  identity `e₂-Hessian = −tr(X²)/2`; verified SL(4),SL(5), two words). But across the
  **full ε-series** the two-index content grows (ε³→(2,1), ε⁴→(3,1)/(2,2), …), so one
  generator does **not** close the sector — it is a *finite* multi-generator set
  bounded by `c=n` nilpotency at bidegree `≤(3,3)`. NET: the long-standing
  "two-block barrier" is now a **precise, finite, bounded** structure (the genuine
  content a first-principles closure must assemble). Computer-assisted structural
  characterization, not PROVEN. Ledger V41/V42. Proven core P1-P16 unchanged.
- **B71** — the SL(3) figure-eight A-variety from the trace map (Phase-8 Track B, the
  SL(3) analogue of B67). The figure-eight monodromy `[[2,1],[1,1]]=M²` acts on the 8
  SL(3) fiber trace coordinates (B48) as `T_1²`; a fiber rep extends over the bundle
  iff its character is `T_1²`-fixed, so `Fix(T_1²)` **is** the SL(3) character variety
  of the figure-eight bundle. **B0–B1 (exact):** `Fix(T_1²)` decomposes into **exactly
  three dimension-2 components** — `V0={x1=x4,x2=x5}` (geometric, contains `Sym²` of the
  figure-eight SL(2) holonomy), `W1={x1=x4=1}`, `W2={x2=x5=1}` (Dehn-filling-type) —
  reproducing the **component structure** of the published Heusener–Muñoz–Porti
  (arXiv:1505.04451) and Falbel et al. (arXiv:1412.4711) character varieties; the `Sym²`
  ground truth lands on `V0` to `~1e-14` (offline, exact). **B2–B3:** explicit SL(3)
  realizations + the 18×9 Kronecker monodromy solve give the peripheral eigenvalue
  A-variety; the **Dehn-filling components literally reproduce Falbel's A-variety**
  (meridian↔longitude transposed): `W1=D2 → M³=L`, `W2=D3 → M³L=1` (`~1e-10`), validated
  on the geometric branch by the Sym² shadow (`eig(t)={μ²,1,μ⁻²}`). The SL(3) analogue of
  B67's Cooper–Long match, on the Dehn-filling components, from the trace map; the
  geometric component (Falbel D1) has no tidy closed form (141-poly ideal), as in the
  literature. Computer-assisted (exact B1 + numerical B2–B3, cross-validated vs Falbel).
  Ledger V43/V44. Proven core P1-P16 unchanged.
- **B73** — the **degree=rank tower law** at SL(4) (Paths-A–F mandate, Path A). On the
  SL(n) figure-eight bundle's **principal Dehn-filling component** `{tr A=tr A^-1=1}`, the
  longitude is the meridian's `n`-th power: `M^n=L`. CONFIRMED at SL(4) (`M^4=L` on the
  spectrum `{1,1,ω,ω²}`, high-precision ~1e-39 via mpmath Newton-refinement; the scalar
  criterion `[A,B]=c·μ^4`, `μ=A^-1 t` from V46). A0 (exact): SL(2) is degenerate — `Fix(T_1^2)`
  is a single geometric component, no Dehn-filling component, so the phenomenon starts at `n=3`.
  Honest caveat: SL(4) has a SECOND Dehn-filling component (`{z^4+1}`, `tr A=0`) giving `M^3=L`,
  so degree=rank is the relation on the *principal* component, not the only one. With SL(3)
  (V47, `M^3=L`) this gives the law at `n=3,4`. Ledger V54. Proven core P1-P16 unchanged.
- **B74** — higher-spin / W_N vs the metallic Dickson tower (Path C, literal-match test). Exact
  sympy: the W_N charge-conjugation grading (spin-`s` current = degree-`s` Casimir, graded by
  `(-1)^s` under `C=-X^T`; verified `tr((-X^T)^s)=(-1)^s tr(X^s)`, sl 3/4/5) and the Dickson
  P-grading (`L_s(-m)=(-1)^s L_s(m)`, B64) are the **same** involution `-w0` of `A_{n-1}` on a
  degree-`k` invariant. So the **parity grading is a LITERAL shared object (STRUCTURAL)**; but
  the full spectrum diverges (the Dickson tower is strictly richer — negative powers, sign
  sectors, multiplicities), clean bijection only at `n=3`; and the dynamical "eigenvalues = mode
  growth rates" reading is **SPECULATIVE-ANALOGY** (no supporting computation). Real kernel is
  sl(n) invariant theory, consistent with V28. Ledger V56. Proven core P1-P16 unchanged.
- **B75** — the **m-axis of degree=rank** (Path F1, the two-parameter `(m,n)` thread). Builds the
  metallic-`m` once-punctured-torus bundle (monodromy `φ_m^2`, `φ_m:a→a^m b, b→a`; trace `m^2+2`)
  and tests degree=rank across `m`. METHOD: B73's scalar `μ=A^-1 t` criterion is calibrated to the
  figure-eight's specific monodromy convention and FAILS on a conjugate one; the **convention-
  independent** test is `eig[A,B]=eig(t)^k` (reproduces `M^3=L` for both fig-8 conventions, ~1e-14).
  RESULT: at `n=3` the **odd** metallic bundles `m=1` AND `m=3` both give `M^3=L` — degree=rank
  persists across the metallic family to a different hyperbolic manifold, a two-parameter
  rank/topological invariant. OPEN: even `m=2` (no clean component over 61 spectra — consistent with
  the cusp parity `k≡m mod 2`, B69); the rank-4 metallic corner. Ledger V57. Core unchanged.
- **B76** — cusp-torsion × quantum group at roots of unity (Path F2/F3 closure). Exact sympy:
  `2cos(π/k)=[2]_q` at `q=e^{iπ/k}`, so the cusp `k`-set `{3..m+2}` (B69) **is** the SU(2)\_{k−2}
  quantum-group root-of-unity level set (both are `2cos(π/k)`, order-`2k` torsion) — closes B69's
  open reconciliation item (STRUCTURAL); but the metallic fusion rule categorifies only at `m=1`
  (V28), so the "anyonic TQFT" reading of the family is **SPECULATIVE-ANALOGY**. F3 (parity × CS)
  is subsumed by V56 (the B64 parity split = the W_N charge-conjugation grading). Ledger V58.
  Proven core P1-P16 unchanged.
- **B68 (Path E retry, V59)** — the figure-eight AJ recursion, retried with a smarter method
  (`cyclotomic_numeric.py`): Habiro `J_N` + **per-q numeric null-space at `|q|=1`** (the
  well-conditioned regime; off-circle is cond ~1e26 noise). No homogeneous order≤3 / Q-degree≤4
  recursion at generic `q` — **confirms V52's bounded negative** by an independent route; the
  figure-eight recursion is inhomogeneous/higher-degree (Garoufalidis–Le, a literature theorem).
- **B77** — the degree=rank **mechanism** (follow-on Phase 1a, V60). Refines degree=rank to the signed
  scalar-matrix identity `[A,B]=(−1)ⁿ⁻¹μⁿ` (`c=+1` at n=3, `c=−1` at n=4). **Refutes** the A↔D
  unification: meridian/longitude eigenvalues are generic, NOT the Dickson `char(Mⁿ)` roots — degree=rank
  is peripheral, not trace-ring.
- **B78** — the n=5 degree=rank test (follow-on Phase 1b, V61): honest **method-limit**. The n-generic
  finder reproduces n=3,4, but at SL(5) the bundle condition yields only REDUCIBLE reps. n=5 OPEN.
- **B79** — the two-parameter `(m,n)` degree table (follow-on Phase 1c, V64): degree=rank holds on every
  **computable** cell (`d(1,3)=d(3,3)=3`, `d(1,4)=4`, all `=rank`); even-m + rank-4-metallic cells OPEN.
- **B80** — the **SL(4) metallic tower from first principles** (follow-on Phase 2, V62). `char(J(m))`
  factors EXACTLY as the Dickson tower over ℚ[m] via the **CRT/F_p** symbolic-m Jacobian (exact F_p
  ε-series `DT_0(m)` over 5 primes, interpolate in m, CRT + rational-reconstruct → ℚ[m], `sympy.factor`).
  Char poly identical to B65; resolves the B70 SL(4) stall (e₂ closure automatic via n×n matrix arithmetic).
- **B81** — the CRT/F_p route at **SL(5): blocked** (follow-on, V63). `char(DT_0(5))` SCATTERS across
  seeds (gauge-corrupt; SL(4) is seed-invariant, why B80 works) — the doubly-degenerate `char(M²)²`
  sector is the residual `e₂/Λ²` barrier (B58), localized as char-poly seed-scatter. SL(4) (V62) stands.
- **B82** — **consolidation, novelty, physics close** (follow-on Phase 3, V65). The three real threads
  are one object; SL(3) degree=rank KNOWN (Falbel), general APPARENTLY_NEW; the **physics chapter is
  formally CLOSED** (V28/V29/V34/V56/V58 — the kernel is always invariant theory of `sl(n)`).
- **B83** — the SL(n) figure-eight A-polynomial family `L=(−1)ⁿ⁻¹Mⁿ` (unification push Phase A, V66).
  The peripheral eigenvalue A-variety of the principal Dehn-filling component; `n=3` `L=+M³` (Falbel),
  **`n=4` `L=−M⁴` (NEW — the first SL(4) figure-eight A-polynomial from the trace map)**, unifying
  B67(SL2)/B71(SL3)/B73(SL4). Mechanism: exponent = rank = the filling slope.
- **B84** — the SL(5) tower barrier is **non-convergence, not gauge** (Phase B, V67; **I1 refuted**).
  Even the gauge-INVARIANT power sums `tr(DT_0(5)^k)` scatter across seeds → the spectrum itself is
  seed-dependent (a non-convergence of the pinv-limit at the doubly-degenerate sector), not a basis
  ambiguity. No gauge-fix/θ-split/averaging helps; the SL(5)+ tower needs the symbolic trace map σ.
- **B85** — the all-n tower lynchpin **reduced** (Phase C/D, V68). Λ² functoriality is NEW + real
  (`Λ²(A²B)=(Λ²A)²(Λ²B)`) but does NOT break the degeneracy (the `char(M²)²` multiplicity-2 is a
  root-system fact, B62). The gap reduces to one symbolic step (the bounded rank-1 `e₂/Λ²` closure into
  σ, B70); no numerical or representation shortcut remains.
- **B86** — the **unification synthesis + novelty positioning + paper skeleton** (Phase E, V69). The
  three threads (tower + A-polynomial + `Aₙ` family) as one object; the `Aₙ` family / SL(4) A-poly is
  `APPARENTLY_NEW` (the #1 external check); paper skeleton in `papers/SLN_FIGURE_EIGHT_SKELETON.md`.

### "Complete the Tower" run (CC-web handoff reconciled; V70–V74)

- **B87** — the **m=3 spectral-curve genus** (Task 3, V70). The sequence is `3, 1, …` with **m=2 a
  minimum** (the handoff's hoped-for `3,1,0` is refuted, V34); the m=3 trace-relation curve is **genus 1**
  (`disc₃=(x²−x−1)(5x²−5x−1)`, squarefree quartic — sharpens V33's loose "≥2"; golden factor shared with m=1).
- **B88** — the **SL(4) Dehn-filling census** (Task 2, V71). Exactly **two** clean components at rank 4:
  `{1,1,ω,ω²}→M⁴=L` (principal, `c=−1`) and `{prim 8th}→M³=L` — **degrees {3,4}**. The degree is the
  robust invariant (`c` is a root of unity only on the principal `{det μ=1}` component); not every
  irreducible bundle rep is on a Dehn-filling component.
- **B89** — **`M⁴=L` PROVED symbolic-exact at SL(4)** (Task 1a, V72). Upgrades V54 (~1e-31) to a theorem
  over ℚ(ω): eliminate `B` → one matrix equation `tA⁻²tA=A⁻¹tAt`; `A³=I` → a 10-equation exact ideal;
  the rank-drop locus `t11=ω·t22` → an explicit 4-parameter family on which `[A,B]·det(t)²=−det(t)·μ⁴`
  is a pure polynomial identity. (Trap: the generic gauge slice is `det t≡0`/vacuous.)
- **B89-T** — the **tower's cohomological route CLOSED** (Task T, V73). `H¹(F₂;ad ρ)` at the trivial-rep
  fixed line gives `char(M)^{n²−1}≠tower` — a **3rd dead shortcut** (after B84 numerics, B85 `Λ²V`).
  Advance: the all-n tower = the explicit **two-sequence Sym product** `∏char(Sym^d M_m)`, verified
  **symbolic-in-m** = the proved (n≤4)/structural (n=5) tower (B58 had only m=1), reducing it to **one
  module-isomorphism**; predicts `a₃(n=6)=2` (overruling B66's gauge-corrupted pinv).
- **B90** — the **peripheral form of degree=rank** (Task 1b, V74; **corrected by the V75 audit**). The
  genuine content is **L1b** `XμX⁻¹=μA` (`X=AμA⁻¹`), proved uniform and exact over ℚ(ω). **Corrected:**
  L1a `λ=μX⁻¹μY⁻¹` is a **tautology** (holds on random non-bundle `(A,t)`), and **"exponent = rank from
  Cayley–Hamilton" is REFUTED** by the hinge test — both SL(4) components satisfy L1b with 4×4 A but give
  exponents 4 vs 3. So degree=rank is **PROVED only n=3,4**; uniform-n is OPEN (not reduced to L1b+CH);
  B90 is a reformulation. OPEN: Task 6 (genus-2, B91).

### Paper 0 — the self-reference grounding (CC-web handoff; V76–V78)

The motivation (characterize the metallic family by a condition, `m` free) is quarantined in
`philosophy/METALLIC_FOUNDATIONS.md`; the mathematics below uses none of it.

- **B92** — the **metallic family as a classification** (Layer 1, V76; `proven`, computer-assisted). Among
  non-negative hyperbolic unimodular 2×2 matrices, the dominant eigenvalue is purely-periodic-period-1
  **⟺ det=−1** (verified for all 66 with entries ≤5), = the family `{M_m=[[m,1],[1,0]]}` up to `GL(2,ℤ)`
  conjugacy, `m` free. Three equivalent forms (self-ref / CF / Möbius); **MyCalc-2** (CF-period a conjugacy
  invariant → companion per trace); refinement (a) (the naive premises admit det=+1); **MyCalc-5** (systole:
  `m=1` minimal → the member is contingent on a metric).
- **B93** — **det=−1 is exactly the tower's parity** (Phase C, V77; `proven`/`computer-assisted`).
  **MyCalc-1** (`det=−1 ⟺` a negative eigenvalue `−1/λ` ⟺ the sign sectors `char(−Nᵏ)`); **MyCalc-4**
  (the parity `m→−m` and the field Galois `√→−√` are *distinct* ℤ/2's — refines handoff Idea-4: the CPT is
  the contragredient, not Galois).
- **B94** — **tower universality** (G1, V78; `computer-assisted`, exact SL(3)/SL(4)). Squaring the proved
  metallic Jacobian (`J(φ²)=J(φ)²`, `M_m²` det=+1) shows `char(J²)` factors **exactly** over the catalog
  `char(Nᵏ)` (**universal**) but with **no** sign sectors `char(−Nᵏ)` and **no** `(t+1)` (**parity
  det=−1-specific**) ⇒ *"universal catalog, det=−1 parity"*, so `det=−1` is structurally distinguished.
  **G3:** degree=rank is det-agnostic (figure-eight is det=+1, B89) ⇒ tower-parity and degree=rank are two
  problems.

- **B95** — the **degree=rank mechanism** (Task M, V79; `proven` + `open`). The V75 audit killed
  "exponent = Cayley–Hamilton degree"; B95 finds what the exponent reads. The principal spectrum is
  **forced** by `tr A=tr A⁻¹=1` (eig 1 at mult n−2): `{1,i,−i}` (n=3), `{1,1,ω,ω²}` (n=4),
  **`{1,1,1,−1,−1}`** (n=5), **impossible at n≥6**. At n=5 it has `A²=I` ⟹ `A,B` involutions ⟹ `⟨A,B⟩`
  dihedral ⟹ **reducible** (no irreducible SL(5) principal rep — upgrades B78's numerical limit). So
  **"exponent = rank" is an n∈{3,4} phenomenon**: the mechanism reads whether the cusp's forced
  finite-order spectrum admits an irreducible rep, explaining the n≥5 wall on *both* the tower and
  degree=rank. Corrects the handoff's SL(5) spectrum guess. Full degree classification open.

### Geometry-invariants + literature-bridge pass (CC-web handoffs; V80–V84)

"Compute the numbers, quarantine the interpretation." Bounded quantum-topology invariants on the metallic
mapping-torus manifolds, banked as mathematics; **every** physics reading lives only in
`speculations/archive/PHYSICS_RESONANCES.md` (`SPECULATION`, never promoted). Physics chapter stays
**CLOSED**; proven core P1–P16 untouched.

- **B96** — **geometry invariants** (V80; `computer-assisted`). The metallic volumes are strictly monotone
  (`2.030<3.664<4.814`; `m=1`=figure-eight=systole, cross-checked by the Bloch–Wigner dilog), and the
  decisive Hessian result: the complete structure is a strict volume **maximum** (155/156 fillings of
  `4_1` below `V₀`, 0 above) ⇒ the Neumann–Zagier volume Hessian is **definite `(0,2)`, NOT Lorentzian** —
  the most-leveraged "physics path" returns negative. `|τ₃|` left open (branch-ambiguous; the from-scratch
  1-loop did not calibrate to `τ₁=−3,τ₂=−16`, so unreported).
- **B97** — **where the Lorentzian structure lives** (V81; `computer-assisted`). The `(2,1)` Lorentzian
  form is **located** as the `so(2,1)=sl(2,ℝ)` Killing form on the **SL(2,ℝ)/Teichmüller** component (the
  gauge algebra of *toy* 2+1 gravity), **not** the SL(2,ℂ) geometric side (B96, Euclidean `(0,2)`) —
  structural, present by construction, **not emergent**; the 3+1 wall is untouched.
- **B98** — **the trace-map Jacobian at the GEOMETRIC rep** (Probe 1, V82; `computer-assisted`, exact
  SL(2)). At the geometric rep (not the trivial fixed line where the tower lives), `char(D T₁²)=(t−1)
  (t²−5t+1)`: the transverse quadratic gives the **adjoint Reidemeister torsion `τ₁=−3`** (twisted
  Alexander), **NOT** the Dickson tower. So the **tower is a trivial-rep phenomenon**; the geometric rep
  carries the torsion object — *consistent with* Daly (arXiv:2411.04431) and the 3d-3d correspondence
  (cited). Also: the tower ≠ the Kostant principal-`sl(2)` even-only branching (Probe 5b). Explains why
  Task T degenerated at the trivial rep.
- **B99** — **the SL(3) geometric Jacobian** (Probe 1c, V83; `computer-assisted`). The SL(3) geometric rep
  (`Sym²` on V0) gives 2 eigenvalue-1's (tangent to V0) + 3 transverse reciprocal pairs, sums
  `c∈{5, 4.5±4.664 i}`; the `c=5` pair is the SL(2) torsion pair carried up by `Sym²`. **NOT** the
  trivial-point SL(3) tower (real `{−1,3,4}`) ⇒ the geometric rep is the torsion side at SL(3) too.
- **B100** — **literature cross-checks** (Probes 2+6, V84; `computer-assisted`, methods **cited**). The
  Zickert/SnapPy **Ptolemy variety** of `4_1` (`N=3`) gives 2 obstruction classes + 6 boundary-unipotent
  SL(3,ℂ) reps in the trivial class — the 0-dim slice of B71's components, cross-validated from an
  independent code path. The **Baker–Petersen** (arXiv:1211.4479) twisted Alexander **is** the B98/B99
  geometric-rep Jacobian `t²−5t+1`; the canonical component (trace coords, genus 0) and the A-poly spectral
  curve (genus 3) are different curves. Two published frameworks **agree** with the B71/B98/B99 picture.

### The Hitchin-component reframing (CC-web handoff; V85)

The physics chain is **firewalled** to `speculations/archive/PHYSICS_RESONANCES.md` (cited, never claimed).

- **B101** — **V0 = the Fuchsian locus of the `SL(3,ℝ)` Hitchin component** (V85; `computer-assisted`, + one
  `dead` negative, one `open` direction). The geometric component V0 (B71 — `Sym²` of the Fuchsian `SL(2,ℝ)`
  rep) *is* the Fuchsian locus of the Hitchin / Fock–Goncharov positive component of the once-punctured
  torus. **R1** (`STRUCTURAL`): the Anosov hallmark (loxodromic + unipotent cusp + complex elliptic control)
  + the unique `SO(2,1)` form, signature `(2,1)` — the rigorous backbone of B97, now inside the Hitchin
  component. **R2** (`dead`): the symmetric-space ladder — the principal `SL(2)` lands in **split real
  forms**; Lorentzian only at `k=2` and **does not climb** ⇒ **no tower of spacetimes** (kills the
  phase-space "3+1D at SL(3)" idea structurally; `docs/atlas/FAILURE_ATLAS.md`). **R3**: `sl(3)=V₂⊕V₄`
  (dims 3,5; degrees 2 quadratic, 3 **cubic**); `V0={cubic=0}`. **R4** (the genuinely-new computation):
  `H¹(F₂,sl(3)_Ad)=8` splits **3⊕5** (Teichmüller ⊕ cubic), and an explicit Anosov family **leaves V0 and
  breaks the `SO(2,1)` form** (2 Fuchsian seeds × 2 cubic directions) — the cubic directions are the
  genuinely-`SL(3)` convex-projective deformations the project never explored. Cite Hitchin 1992; Labourie;
  Fock–Goncharov; Choi–Goldman; Marquis. The Hitchin→Langlands→N=4 chain is cited, ceiling stated (N=4 SYM,
  not the Standard Model / gravity / the universe).
- **B102** — **the W1/W2 dichotomy + the R4 boundary-controlled cubic continuation** (V86;
  `STRUCTURAL`+`computer-assisted`, with an `open` tail). Two follow-ons to B101, verified before landing.
  **D1:** Cayley–Hamilton on `T₁²` forces every irreducible `Fix(T₁²)` SL(3) character into Case I
  (`trA=trA⁻¹`, self-dual) or the `trB=trB⁻¹=1` branch (0 "neither"; exact on B71's V0/W1/W2). **D2/D3:**
  realizing B71's components, **W1→`ρ(a)` elliptic `{1,i,−i}`, W2→`ρ(b)` elliptic** (order-4, not loxodromic
  ⇒ **not Hitchin**); the geometric V0 point is self-dual with `tr(AB)` a root of `t²−t+7` (`Q(√−3)`). So the
  genuine non-`Sym²` components are excluded from the real Hitchin component by **ellipticity** (cleaner
  than complexity), V0 by complexity. **D4:** the `{1,i,−i}` spectrum = Task M's forced `n=3` spectrum
  (B95). **D5:** the boundary-controlled (relative) cubic family keeps the cusp real **only to first order**
  — generic second-order cube-root complexification; the handoff's `t*≈3.775` geodesic boundary does **not**
  reproduce; the unipotent-preserving continuation is `open`. Cite Heusener–Muñoz–Porti, Labourie,
  Hitchin/Fock–Goncharov/Goldman/Marquis.

### The SL(n) tower as a GL(2,ℤ) representation (CC-web handoffs; V87)

- **B103** — **the tower equivariance / plethysm-universality / constructive module-iso** (V87; `proven`
  Route-1 structure all n + module-iso n=3,4; `open` explicit `μ_d` n≥5). A **fourth route** to the tower
  (after the dead cohomological / pinv / Λ² routes). **Route 1 (universality, all n):** `J_φ(n)` factors
  through the abelianization `N ∈ GL(2,ℤ)` (inner autos act trivially on traces) ⇒ `ρ_n: N↦J(n)` is a
  `GL(2,ℤ)`-rep ⇒ `char(J)` is a **class function = the catalog**, universal for metallic **and
  non-metallic** monodromies; **det-sign parity** (sharpens B94). Verified at SL(3) via the exact Lawton
  maps `U,L,S` (relations `S²=I, SUS=L, SLS=U` lift; `J(3)` constant on each `N`-class). **Route 2
  (constructive module-iso, n=3,4 exact over ℚ[m]):** an explicit `m`-independent invertible `P` with
  **`P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}`** (`μ_d=[2≤d≤n]+[0≤d≤n−3]`; intertwiner dim `=Σμ_d²` Schur); the
  `char(−M^k)` sign sectors are the `det=−1` twists. Realizes the module-iso **(M)** (B89-T's lone open item)
  constructively + exactly for n=3,4. **Reframing:** the all-n tower = **decompose the `GL(2,ℤ)`-rep `ρ_n`**;
  universality is structural (all n), the explicit `μ_d` open n≥5 (the Procesi wall) — continuation B104.
  Cite B94, B85/B89-T, B80, Lawton, Procesi.
- **B104** — **the Dehn-twist route: SL(4) universality + the SL(5) wall** (V88; `proven` SL(4) +
  `characterized-wall` SL(5)). Executes the "Dehn-Twist Route" handoff in full: build any monodromy's trace
  map by composing the elementary twists `U,L,S` inside the eps-series (not the Procesi ring). **SL(4)
  (proven):** the GATE reproduces B80's metallic tower; `J` factors through `N`; `char(J(N))` = the
  two-sequence catalog with **det-sign parity** for **metallic and non-metallic** `N` (e.g. `U²L`, det +1) —
  the explicit SL(4) catalog is a computed theorem. **SL(5):** the engine inherits the eps-series gauge
  degeneracy — `char(J)≠catalog` but **21/24 Dickson factors resolve** (the doubly-degenerate sector,
  B61/B66); a **computational** wall, not a rep-theory failure. The n≥5 obstruction is now isolated to the
  eps-series degeneracy. Cite B103, B80, B61/B66, Lawton/Procesi.
- **B105** — **the n=5 wall + the ρ_n convergence** (V89, **corrected V90**; `open` n≥5 + synthesis). The
  CC-web "n=5 Resolution" handoff, then the **V90 audit** (two inference downgrades). **N5:** the SL(5)
  eps-series resolves **21/24** Dickson factors, and the resolved 21 are **universally catalog-consistent**
  (across seeds and monodromies) — strong evidence on the resolved sector; the 3 unresolved are supported as
  `Sym²` by **structural routes** (B62/B89-T/B103). **[V90 Correction A]** the seed-variation of the 3
  unresolved factors is the eps-series rank-deficiency signature (B84), **uninformative** about the truth —
  so the explicit **n=5 catalog is OPEN**, and a structural deviation there is *neither ruled in nor out*.
  **[V90 Correction B]** there is **no proved "natural boundary"**: `char(J(n))=catalog` is a class function
  for **all `n`** (B103); n=4 is a *methodological ceiling* (eps-series + trace-ring non-closure), not a
  theorem. **[V91 — three obstacles, one threshold]** n=5 is a threshold where **three distinct** `A_{n−1}`
  obstacles degenerate — degree=rank (B95, eigenvalue `−1`, `A²=I`), the tower/eps-series doubling (B62,
  golden `char(M²)²` from the A₄ height-2 `θ=−w₀` (4,2) split), and trace-ring non-closure (engine-free,
  onset n=4) — *different eigenvalues, independent derivations, different onset*, **not one collision**.
  **Convergence + open frontier:** the project converges on one object **`ρ_n`** (the `GL(2,ℤ)`-rep on the
  SL(n) trace ring), fully characterized n=3,4, **explicit n≥5 OPEN** — the **sharpened** live target (V91):
  prove `char(ρ_n)=catalog` by reproducing the **opposition-involution multiplicities** directly from `ρ_n`,
  the contested n=5 piece being *only* B62's `char(M²)²`. Literature L1 (GKLP 1305.0937) + L4 (Bonahon–Dreyer
  1209.3526 / Douglas–Sun 2011.01768) cited; H1–H6 / C1–C4 tabulated.
- **B106** — **the trace map at the DEHN-FILLING fixed points** (V92, **hygiene V93**; `computer-assisted`).
  The never-computed **third** fixed-point class (after the *trivial*=tower and *geometric*=torsion reps).
  **D1:** three classes, three distinct Jacobian signatures — trivial/geometric hyperbolic `(3,3,2)`,
  Dehn-filling **partially ELLIPTIC** (SL(3) W1/W2 `(1,1,6)`; SL(4) principal/secondary `(4,4,7)` with
  root-of-unity neutral eigenvalues). **Honest negative:** the stability *type* does **not** encode the
  degree=rank exponent (both SL(4) components `(4,4,7)`, yet exponents 4 vs 3). **D4:** `μ` and `[A,B]`
  commute; **`Lᵢ = c·Mᵢ^k` per eigenvector** (`c` a root of unity: `1` SL(3); `−1`/`i` SL(4)). **D3:** `M⁴=L`
  (principal), `M³=L` (secondary); conjugates absent. **[V93 hygiene]** the D1 root-of-unity *values* pass the
  **B84 gauge-noise gate** (seed-stable across ≥3 seeds — `1,±i,−1`; `1,ω,ω²`); the D4 SL(4) **principal**
  (`c=−1`) **corroborates** the proved B89/B83 `L=(−1)^{n−1}Mⁿ` (not a new advance), the **new** content being
  the **secondary** (`c=i`, numerical), **SL(3) W2**, and the **per-eigenvector method**. No physics.
- **B107** — **the physics-connection audit (the headline is a NEGATIVE)** (V94, **POSTULATED/FIREWALLED**).
  Banks the CC-web physics exploration as a first-class **dead-end log**; *all* physical readings are
  POSTULATED + firewalled to `speculations/archive/PHYSICS_RESONANCES.md` (Path 8), **nothing to `CLAIMS.md`**,
  the physics chapter stays **CLOSED**. **A (verified anchor):** the metallic trace map `φ_m: a→aᵐb, b→a` **is**
  the KKT/Fibonacci trace map (`tr[A,B]=x²+y²+z²−xyz−2` = Sütő invariant, conserved ∀m; `φ_1=(z,x,xz−y)`) — a
  known quasicrystal object. **B (verified — the headline negative):** every SL(3) `m=1` tower eigenvalue is
  `±φᵏ` — **one geometric scale `log φ`**; a mass spectrum is a Hessian, not one ratio, so the tower is
  **re-presented moduli-space monodromy, not new physics**. **C (corrected overclaim):** tower/torsion `≠`
  masses (withdrawn); only the *moduli-space-level* `M_SUSY ≅ M_flat` + the three-branch ↔ three-fixed-point
  map is citable. **D:** citations confirmed (GKLP 1305.0937; DGG 1108.4389, 1112.5179). **E (open fork):** the
  off-principal multichannel reps — where B106's root-of-unity D1 data (Addition 3) shows the single-scale
  pattern breaks; the open `c→θ` check links it to the `ρ_n` target.
- **B108** — **does `θ=−w₀` predict the Dehn-filling `c`?** (V95; the CC-web "Final Computation Arc" Task 1, the
  prize). The mandatory **hinge** (all four per-eigenvector degree=rank scalars `c={1,1,−1,i}`, B106 D4) **FAILS**.
  `θ` *is* a tower symmetry (`P²=I`, `[P,J(m)]=0` symbolic; organizes the Dickson parity, B62), and at the
  Dehn-filling reps it acts as the contragredient sending **`c↦c⁻¹`** — so it fixes `c∈{1,−1}` (W1/W2/principal,
  matching `c=(−1)^{n−1}`, B83) but **not** the secondary `c=i`. **Obstruction:** `θ` is an **involution (order
  2)**; `c=i` is **order 4** — beyond its reach. degree=rank's `c` stays **OPEN**; the missing piece is an order-4
  (`ℤ/4`) structure (candidate: the forced cusp spectrum `{1,i,−i}`, B95). Paper 1 frames degree=rank as the
  central open question.
- **B109** — **the trace-map dynamics at the void (D2)** (V96; Tasks 2/4/5/6). **Verify-don't-trust** corrected
  the handoff's coordinate-axis "facts" (they don't reproduce) to the rigorous **linearization** `DT₁²(2,2,2)`,
  eigenvalues `{1, φ⁴, φ⁻⁴}` (1 center, 1 unstable, 1 stable): the center direction **is the `A↔B` asymmetry**
  (unifying "bounded direction" + "slow asymmetry mode"), Lyapunov `{0, ±4 log φ}`. The void is a **(2,1) saddle**
  of `κ`. **SL(3):** the trivial-point Jacobian is the Dickson tower; the void's **center manifold = the tower's
  root-of-unity (parity) sector** (dim 1 at SL(2), 2 at SL(3)). **L5 literature:** degree=rank `Mⁿ=L`
  **apparently new** (HMP 1505.04451 confirms the 3 components but not the power law); the **W₄** anchor at `sl(4)`
  is real (1111.2834) but generic `sl(N)↔W_N`, doesn't single out n=4.
- **B110** — **the off-locus sector of `4₁` at SL(3) is EMPTY** (V97; Task 3 / S011). The variety has exactly
  three irreducible components (HMP = B71's V0/W1/W2), all **on** the forced locus (`x1=x4` or `x2=x5`), so there
  is no off-locus irreducible 4₁ SL(3) rep — the single-golden-scale picture is complete for it. **Scope:** the
  broader S011 fork (higher rank / other manifolds) stays **OPEN**.
- **B111** — **the tower's sign structure = the opposition-involution closed form + one degree=rank promotion**
  (V98; the sign-findings handoff). The `θ=−w₀` all-heights **closed form** (`⌈(n−h)/2⌉` / `⌊(n−h)/2⌋`; matches B62
  height-2) is **not** the proved tower: `Tower(n) = [closed form, heights 1..n−1]` with **exactly one
  `char(M¹)` promoted to `char(Mⁿ)`** (verified n=3,4) — the single non-bulk piece being `char(Mⁿ)` = the
  **degree=rank** top power (`L=c·Mⁿ`). So the tower's **sign half IS the closed form** (bulk θ); the only open
  piece is `char(Mⁿ)` (peripheral). **ADDITION 1 (proved):** on the SL(4) secondary `M⁴=−1` is **scalar** ⇒ `k=4`
  algebraically **impossible** (`k=3` forced); on the principal `M⁴` is non-scalar ⇒ `k=4` allowed (but `k=n` not
  proven). **ADDITION 2:** cusp orders `{n−1,n+1,2n}`; the `ord−1` formula **TESTED-NEGATIVE**. **SL(3) parity
  correction:** `(t−1)(t−det N)` (the handoff's `(t+det N)` was wrong). `s_n↔c` DEAD. The leads it opens —
  the **peripheral ℤ/4** (`speculations/S022`) and the **two-symmetry frame** (`speculations/TWO_SYMMETRY_FRAME`)
  — name the degree=rank/peripheral half of the `ρ_n` prize.
- **B112** — **PROOF of the opposition-involution closed form: the sign half of `ρ_n`, all n** (V99). The first
  piece of the catalog proved **from first principles, engine-free, for all n**: an elementary **root-system
  reversal lemma** (`θ=−w₀` acts on the `(n−h)` height-`h` roots of `A_{n−1}` as the reversal `i↦(n−h+1)−i`, with
  `(+1,−1)` eigenspace dims `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)`, verified all n≤12) × the banked **B64** parity assignment ⇒
  `mult char(M^h)=⌈(n−h)/2⌉`, `char(−M^h)=⌊(n−h)/2⌋`. Scope: proves the **bulk θ-decomposition** = the sign half;
  the full tower = this **+ the single degree=rank promotion** (the power half, S022, open).
- **B113** — **the proved closed form resolves the SL(5) sign sectors + localizes degree=rank** (V100). At
  heights 2,3,4 the closed form matches the SL(5) tower **exactly**, including `char(M²)²·char(−M²)` = **B62's 2
  gauge-corrupted modes** the eps-series could not resolve — so SL(5)'s sign sectors are now determined **by
  proof**, not the gauge-fragile numerics. degree=rank is **localized to height-1 + the top power `char(Mⁿ)`**;
  the promotion is **n-dependent** (consumes `−M` at n=5, `+M` at n=3,4) — the power half stays open.
- **B114** — **the covering-degree mechanism — TESTED-NEGATIVE** (V101). S022's candidate (exponent `k` = the
  Weyl-orbit covering degree of `M↦L=c·Mᵏ`) does **not** hold at the full spectrum: the full covering degree is
  `~k^{n−1}`, not `k`. The exponent is **not** a covering degree; the live lead stays the `Mᵏ`-scalar arithmetic
  (B111 ADD1).
- **B115** — **higher-rank + higher-genus generality of degree=rank** (V102; exploratory scoping). The known
  SL(4) Dehn-filling reps are **on the forced locus** (like SL(3)) ⇒ off-locus SL(4) content is in **uncomputed**
  components (obstruction: no SL(4) figure-eight character-variety classification); **genus-2** degree=rank needs
  machinery not in the repo (obstruction: the genus-2 peripheral structure). Both scoped **OPEN**.

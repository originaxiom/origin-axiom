# F05: separate gauge reduction, self-duality and the actual operator gap

2026-09-20. Fork-local checkpoint on `audit/fork-2026-09-20`, input
`297e1dd7`. No shared B number, main-bank claim, empirical fit or TOE closure.

## New input and change of task

The other audit branch now contains the sealed/executed R39 at `8d2cced2`.
Its design, proof, findings, producer, tests and source receipt were read.
Its unchanged 16 tests reproduce in an extracted pinned snapshot: process
7600, final chunk 65ed80, exit 0, 16 passed in 2.08 s. That is a new execution
of the same implementation, not an independent implementation or global
proof certificate. No R39 source or other seat's worktree was changed.

R39 supplies the full noncommuting classical geometric background and its
extra so(11) gauge sector. Do not redo its construction as missing work.
R27 and B1420 already supply the geometric finite-twist vanishing mechanism
and the distinction between twisting and self-duality. This checkpoint
tests their physical-operator join, not another cohomology census.

Fresh network fetch attempts failed (sandbox DNS, then SSH authentication;
the HTTPS attempt was redirected by URL configuration). The available
`8d2cced2` is a pinned local Git object, not a claimed newly fetched remote
head or proof that every other seat is current. Other work can proceed.

## Questions and disclosed expected outcomes

1. Does a genuine order-four central unitary character give a global
   same-action variant of R39 with compact unbroken Lie algebra so(10),
   rather than so(11), and no isomorphism between its coefficient four
   and its dual? Expected: yes, as an unselected Wilson-line datum.
2. Does that remove the absence of charged zero modes? Expected: no.
   The actual homogeneous positive operator admits a Matsushima--Murakami
   lower bound. We derive its normalization directly from R39's matrices:
   on one/two forms the algebraic eigenvalues should be 9/4,19/4,25/4
   with multiplicities 6,4,2; on zero/three forms 15/4 with multiplicity 4.
   Hence the full form Dirac operator has |Q|>=3/2 in curvature-length-one
   units. This is a LOWER bound, not a computed lowest global eigenvalue.
3. Does a small bounded same-Hilbert-space deformation create a zero mode
   simply by breaking self-duality? Expected: no, if its operator norm is
   less than 3/2; closing the established gap is a separate necessary duty.

Alternative: any algebraic, geometric, normalization or analytic step fails.
Preserve that failure. Do not silently change a sealed expectation or
claim a new physical no-go from a failed implementation.

## Fixed conventions and analytic scope

- Complete orientable finite-volume hyperbolic base, curvature -1, no
  singular sources or finite-distance boundary. A chosen geometric SL2
  holonomy lift is an input; no arithmetic-orbifold descent is asserted.
- R39's compact SU4 in the changed candidate E8 parent, with
  248=(45,1)+(1,15)+(10,6)+(16,bar4)+(bar16,4). Keep all sectors.
- C=(E/z,iE/z,H/(2z)), E superdiagonal (sqrt(3),2,sqrt(3)),
  H=diag(3,1,-1,-3), F=E^dagger. A=(C-C^dagger)/2, Psi=(C+C^dagger)/2.
  Positive homogeneous metric, ordinary bulk L2, d_C=d_A+Psi wedge,
  Q=d_C+d_C^*. Adopt the matched complete closure from F02.
- Scalar character chi takes values in the SU4 center {1,i,-1,-i}.
  V_chi=Sym^3(h) tensor chi. On m004 use the already documented marking
  relator aaabABBAb, mu=ab, lambda=aBAbABab, chi(a)=1, chi(b)=i.
  This choice is supplied, not selected by the object or its action.
- The proposed spectral comparison concerns this geometric positive
  metric and its unitary twists, NOT F01's nonsplit m010 coefficient
  bundle or arbitrary harmonic metrics. General unitary flat tensor
  factors preserve the local estimate mathematically; only the scalar
  center twists above have the declared rank-four parent realization.
- Same-space perturbation bound requires fixed base metric, a unitary
  identification of bundles/Hilbert spaces, and a bounded self-adjoint
  zeroth-order difference. It is not a result for topology change,
  singular/domain change, arbitrary end data, or quantum strong coupling.

## Prior and reading boundary

R27's full FINITE_TWIST_PROOF, R28 action-scope argument, R30's fermion
domain proof, R38's parent-action findings, and R39's full proof were read.
B1297/B1420 show why non-real twists and geometric vanishing are already
known. Order-four Wilson lines also occur in the different SM-seat
Q8/E6 closing construction (B1364); no novelty/absence claim is made.

Personally read primary material: Braun et al., arXiv:1812.06072v2,
equations 2.9--2.19 and B.8--B.14; Menal-Ferrer--Porti,
arXiv:1001.2242v2, introductory statements and section 2.1--2.2 through
Lemma 2.14, including its compact-support argument. The latter's
nontrivial-representation qualifier is essential. Their normalization
is not silently identified with ours; the local connection fixes ours.
No new full-paper reading is claimed. No PDF or agent summary is used.

## Pre-execution controls

1. Full local flatness/moment residuals, positive norm and covariant
   parallelism of Psi using the actual hyperbolic Christoffel symbols.
   A wrong curvature scale or omitted connection term must fail.
2. Exterior-algebra construction of T=Psi wedge and Hp=T*T+TT*, with
   independent block formula and exact characteristic polynomials.
   Trivial coefficients give zero; a factor-of-two normalization must
   change the bound. No numerical eigenvalue tolerance.
3. Exact m004 character relation, fourth-root determinant restriction,
   symmetric-cube generator relation, and a trace witness separating
   V_chi from V_chi^*. Preserve the order-two self-dual comparator.
4. Complete center phases on the 248 joint weights, invariant wedge
   line, and long/short root removal in B5. Do not infer so(10) from
   dimension alone or assert a global group quotient.
5. Unchanged local BPS and operator matrices after locally constant
   unitary transition twists. Unitarity and chi^4=1 are load-bearing.
6. Cusp anti-periodic Fourier coercivity for the extra gauge line and
   its untwisted zero-mode comparator. The global positive-gap proof
   is compactness plus absence of a parallel section, not a computed
   numerical gauge mass.
7. The bounded-operator perturbation inequality and a threshold-saturating
   finite matrix control; no promotion to existence of a BPS deformation.

Seal DESIGN, PROOF, code and tests and commit before their first execution.
Retain R39/R27 credit, F01--F04 scopes and all prior failed receipts.

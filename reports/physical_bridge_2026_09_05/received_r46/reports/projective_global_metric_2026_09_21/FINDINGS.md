# F12: the exceptional modes admit a global harmonic background

September 25, 2026; draft begun September 21. Local fork
`audit/fork-2026-09-20`, scientific seal **5579cfb4**.

## Verdict and verification grade

**F11's mode-bearing exceptional parameters admit smooth global
harmonic-metric completions in the required cusp norm class.** This
removes the specific global-matching condition that F11 left unproved.
It does not remove the physical end/action, interaction or chirality
conditions. The charged spectrum still has one coefficient one-form
in each dual sector on the base member: vector-like, not net chiral.

The result combines an **authored analytic existence proof** with exact
algebraic checks of its representation and end-energy inputs. It is
not an explicit numerical PDE solution, an independently reviewed
proof, or a completed physical vacuum. Fifteen new checks passed;
236 unchanged predecessor/parent-vertex checks passed, with one
irrelevant optional-GUI warning. No original failed tests were erased.

## 1. What changed since F11

F10 had an exact flat representation and an exact harmonic CUSP solution.
F11 found discrete parameters with normalizable coefficient modes for
arbitrary smooth completions in a specified end norm class. Arbitrary
positive completion did not mean solution of the global moment equation.

F12 now supplies that solution by compact-domain minimization and a
controlled limit, without choosing a new representation at each cutoff.

| Input or step | Result | Verification |
|---|---|---|
| Determinant-one longitudinal energy | Every metric has cusp energy at least `(12 log(q)^2/L) log(R/Z)` | Parallel eigenline and trace-free projector proof; exact sharpness checks |
| Reference energy above that floor | Finite, with an explicit positive tail integral | Full F10 matrix norm, derivative and asymptotic identities checked |
| Exceptional representation | Generated algebra is all `Mat4(C)` at both roots of each quadratic | Exact field span closure, nonzero determinant and direct word reconstruction |
| Global harmonic metric | Compact-domain solutions converge smoothly on compact subsets | Authored energy, target-compactness and elliptic argument |
| Required end class | Uniform target distance to the reference cusp; equivalent positive form norms | Compact-annulus maximum principle, then passage to the limit |

The final two rows are analytic arguments, not claims inferred from the
number of passing tests. The [full proof](PROOF.md) states their hypotheses.

## 2. The energy estimate that makes the limit work

The earlier single-eigenvector estimate was positive but too weak for
this construction. In rank four, determinant one makes the self-adjoint
connection part trace-free. For the orthogonal projector P onto the
parallel longitude eigenline with eigenvalue q^-3,

    |P-I/4|^2 = 3/4,
    integral_0^1 |Psi_y|^2 dy >= 12 log(q)^2.

The parallel vector is normalized to FORM P; no nonconstant parallel
vector is asserted to retain unit norm along the loop. This clarifies
the abbreviated wording of the pre-run design.

Put k=log q, c=4 beta^2/L^2 and Z>sqrt(c). The actual cusp energy is

    e_ref(z) = 12 k^2/(Lz) + 2L(3z^2-c)/[z(z^2-c)^2].

The integral of the second term from Z to infinity is exactly

    R(Z) = L[2/(Z^2-c) - log(1-c/Z^2)/c],

asymptotic to 3L/Z^2. This is finite EXCESS over a universal floor,
not finite total Higgs norm and not a new physical counterterm.
Subtracting the weaker floor leaves a logarithmic error.

For a compact-domain minimizer h_R and fixed S<R, comparison with one
fixed smooth reference extension h0 gives

    E(h_R;M_S) <= E(h0;M_Z) + (12k^2/L) log(S/Z) + R(Z).

Thus the compact core cannot absorb arbitrarily large energy as R grows.
This is the analytic use of the subtraction; no infinity is assigned a
finite physical value.

## 3. Exact representation checks prevent loss of the background

At each exceptional polynomial the same 16 short words span all matrices:

    1, m, n, mm, nm, mn, nn, nmm, mnm, nnm,
    mmn, nmn, mnn, mnmm, nnmm, nnmn.

Their vectorization determinants in the respective exact fields are

    q^2-14q+1:  7077888000 - 102629376000 q,
    q^2-34q+1:  5184974592000 - 178881623424000 q.

Both are nonzero at BOTH positive roots, certified by polynomial gcds,
not floating-point evaluation of one embedding. Direct reconstruction
checks the words; full/scalar/triangular controls check the instrument.
A reducible triangular example has scalar commutant, so that known
invalid shortcut is not used.

Bounded gradients on a fixed core bound generator displacements in the
positive-metric symmetric space. The word basis then bounds the norms
of every matrix unit. This bounds `tr(H) tr(H^-1)`; determinant one
prevents collapse or escape of the basepoint metric. Local elliptic
compactness gives a global harmonic limit.

On each truncated cusp the squared distance between the minimizer and
the EXACT harmonic reference is subharmonic. It vanishes at the outer
boundary and is uniformly bounded at the inner boundary. The maximum
principle supplies a cutoff-independent bound. The limit therefore
really belongs to F11's uniformly equivalent norm class.

Scalar unitary twists act trivially on the positive-metric target. The
same construction works for all four central characters; the dual
metric is harmonic for the dual bundle. Finite-cover solutions follow
by pullback, without assuming irreducibility survives restriction or
asserting uncomputed cover multiplicities.

## 4. The resulting mode-bearing bulk backgrounds

| Parameters and twist | Normalizable charged coefficient one-forms |
|---|---|
| `q=17 +/- 12 sqrt(2)`, `chi=-1` | One in E and one in E* |
| `q=7 +/- 4 sqrt(3)`, `chi=+i` or `-i` | One in E and one in E* |

These solve the adopted complete classical gauge equations on the fixed
hyperbolic base, via the existing SU4-to-E8 embedding. The construction
does not extend Ballas' nearby properly convex-geometry theorem to
these distant q values. It uses the actual matrices and cusp model.

The residual-square bulk potential is zero, including its first
variation under regular compactly supported parent-field variations.
This uses the distinction already made in
[R28](../physical_bridge_2026_09_05/SOURCE_ACTION_PROOF.md) and
[F08](../balanced_parent_2026_09_20/PROOF.md): harmonic-map energy is an
analytic device for solving the gauge equation, not a replacement
physical action. Infinite total Higgs norm remains infinite; zero bulk
residuals do not decide the physical end laws.

## 5. Next tests, not accomplished results

**Update, September 25: [F13](../projective_fluctuations_2026_09_25/FINDINGS.md)**
addresses the fixed-end-domain, uniqueness and product-integrability
questions below, with authored analytic proofs and 21 new finite checks.
It also computes the actual six sector's acyclicity and derives the
parent's gauge-fixed scalar Hessian. The historical list is retained to
show precisely which obligations F12 itself had not discharged.
Normalized numerical profiles, nonzero/selective couplings, physical
end selection and a quantum phase are not supplied by F13.

1. Specify and test fixed-end variations in the actual parent action,
   including boundary terms and the nonlinear field domain. Fixed q is
   not already a dynamical four-dimensional scalar. R28's commuting
   singular-source formulas cannot be imported unchanged here.
2. Test uniqueness in the bounded-distance end class, including whether
   the arbitrary reference extension over the core drops out. Existence
   alone has not established this.
3. Establish product integrability and compute normalized profiles and
   full-parent interaction/propagator channels. F09's balanced cofactor
   formulas are not transferred by name to this nonparallel background.
4. Then test actual mirror selectivity and gauge/anomaly consistency.
   Absence of the old flat pairing does not imply unequal couplings or
   a selective quantum gap. The free counts here remain equal.

Choosing q and the central twist, the observed generations and gauge
breaking, deriving the parent and geometry, gravity, quantum completion
and measured predictions are not achieved by F12. No object-wide
impossibility or absent-from-the-repository claim is made. The full
TOE goal remains unachieved.

## Reading and custody

General local Dirichlet/compactness tools were checked in
[Riestenberg--Smillie, section 2.3](https://arxiv.org/html/2511.11469v3#S2.SS3).
The exhaustion strategy was compared with
[Sagman, section 5.1](https://arxiv.org/html/1911.06937v3#S5.SS1), whose
surface theorem is NOT applied directly in dimension three. The proof
supplies the flat-bundle adaptation and representation-specific estimates.
These were selected primary sections, not full paper readings. B149's
span-closure method and F11's exact field arithmetic are reused with
attribution, not claimed new.

[Design](DESIGN.md), [seal](SEAL.json), [exact witnesses](EXACT_WITNESSES.txt),
[new tests](TEST_OUTPUT.txt),
[antecedent tests](ANTECEDENT_TEST_OUTPUT_REDACTED.txt), [receipt](RECHECKS.md).
No scientific file changed after sealing. No subagents, main edit,
shared B allocation, push, new all-head sweep or full-suite certificate.

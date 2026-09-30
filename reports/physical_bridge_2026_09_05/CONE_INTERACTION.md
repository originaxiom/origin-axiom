# Finite interaction action constrains complex cone boundary data

September 30, 2026. Path-local R62. The candidate complex boundary
line from R61 survives the nonlinear action test only with restricted
leading algebra coefficients in the declared asymptotic class.
Nonzero commuting data survive. Nonnormal tangential data cannot be
rescued by a general constant radial simple pole. This is not a
universal exclusion of nonabelian backgrounds or a chirality result.

All **70 exact controls and 25 focused tests pass**. Scientific seal
5cd4cbb3eaad9047e9b2516cb496dc16f81b4345 was pushed and server-confirmed
before execution. The four sealed scientific files are unchanged.
The test selection is ten new tests, eight R61 tests and seven R59
tests. Finite controls support, but do not independently certify, the
all-dimension authored argument.

## The action rather than the quadratic norm

Fix the incomplete metric g=dr^2+r^2 h with flat torus link area A.
In a faithful positive unitary matrix representation write

    C = (B/r) dr + w X,    c = |w|_h^2 > 0,
    F = dC + C wedge C,
    I = div_g(C+C^dagger) + g^(ij)[C_i,C_j^dagger].

Here w is a constant complex harmonic helicity one-form. The supplied
twisted action uses positive potential integral (2|F|^2+|I|^2/2)/g7^2.
The field convention, potential and fermion variations are from
[Braun et al., equations 2.9--2.15](https://arxiv.org/html/1812.06072v2).
They are physical inputs, not a derivation of the action from genesis.

Direct metric and matrix differentiation yields

    F_ra = w_a[B,X]/r,    F_ab = 0,
    I = M/r^2,    M = B+B^dagger+[B,B^dagger]+c[X,X^dagger],
    V_(epsilon,R) = (A/g7^2)(1/epsilon-1/R) K,
    K = 2c ||[B,X]||^2 + ||M||^2/2.

The fixed-frame quadratic one-form norm instead is
A(R-epsilon)(||B||^2+c||X||^2), which is finite. Finite quadratic
norm therefore does not establish finite interaction action.
No integration-by-parts boundary term has been discarded. R28's
distinction between residual action and rough energy is preserved.

## Why the radial cancellation fails and what survives

For any finite matrix size and c>0, K=0 exactly when

    B+B^dagger=0,    [X,X^dagger]=0,    [B,X]=0.

The proof is short enough to audit directly. K=0 implies [B,X]=0
and M=0. Cyclicity gives

    Re tr(B M) = 2 ||(B+B^dagger)/2||^2
                  + c Re tr([B,X]X^dagger).

Consequently B is anti-Hermitian. Its self-commutator then vanishes,
and M=0 forces X to commute with its adjoint, meaning X is normal.
The converse follows by substitution. The symbolic test checks a
generic complex two-by-two pair, while the trace argument itself is
dimension-independent.

The controls use a root su2 inside R59's supplied regular su5 factor.
They are checked both in two-by-two matrices and their literal
five-by-five inclusion, and after a nontrivial unitary basis change.
The table gives the dimensionless coefficient K, not a physical coupling.

| Leading data | Square link | Hexagonal link | Meaning |
|---|---:|---:|---|
| B=0, X=E12 | 4 | 3 | Flat but nonzero moment map |
| B=-c diag(1,-1)/2, X=E12 | 16 | 6 sqrt(3) | Moment map cancelled but curvature nonzero |
| B=X=E12 | 10 | 5+2 sqrt(3) | Radial self-commutator cannot be omitted |
| B=i diag(1,-1), X=(1+i)diag(1,-1) | 0 | 0 | Nonzero commuting data admitted |

Both curvature and moment-map residuals enter the supersymmetry
variations. Cancelling only one does not construct a supersymmetric
vacuum. The zero-residual control has positive quadratic norm and is
not an empty or zero-field success.

## Controlled remainders and the nonlinear constraint

Allow tangential remainder O(r^delta) and radial remainder
O(r^(-1+delta)), delta>0, with the stated uniform first weighted
derivative bounds. A positive K retains its leading divergence.
When K=0, delta>1/2 is sufficient for finite remainder action, since
the worst residual density is O(r^(2delta-2)). Exact commuting
power profiles distinguish the finite cases delta=3/4,1 from the
logarithmic delta=1/2 and power-divergent delta=1/4 cases.
Special cancellations can improve this sufficient bound.

Normal matrices form a nonlinear, compact-gauge-invariant set.
If a complex LINEAR subspace consists entirely of normal matrices,
polarization at X+Y and X+iY forces [X,Y^dagger]=0 and hence [X,Y]=0.
They are simultaneously unitarily diagonalizable. If this subspace
lies in a compact reductive parent's complexified algebra and is also
invariant under its full adjoint action, it is contained in the center:
it is an ideal and cannot contain any simple factor's nonnormal root
vector. These are additional hypotheses on a linear space, not a
demand that a nonlinear vacuum space be linear.

The first derivative of [X,X^dagger] at X=0 vanishes in every direction.
Along a nonnormal ray the quadratic term is nonzero. A linearized
boundary-mode list can therefore overcount finite-action deformations.
This does not prove that all corresponding fermions disappear, or
remove the internally constant four-dimensional vector multiplet.
R61's critical one-form and the scalar gaugino are distinct profiles.

## What this changes toward physics

R61's reality/current test remains valid, but its unrestricted algebra
coefficients do not automatically define an interacting domain.
The next target is the coupled nonlinear boundary law and its gauge
quotient, with the supersymmetry conditions and all relevant cone
indicial channels. Noncommuting fields whose leading trace vanishes
must not be discarded by a statement about nonzero constant traces.

A different leading power or logarithm, nonconstant leading data,
singular coefficient metric, different base metric, finite tip radius,
or justified source/apex action is a different admission problem.
None was excluded. R39's actual noncommuting hyperbolic solution and
the canonical complete-space interaction results remain intact.
No physical parity lift, globally glued chiral background, three-family
spectrum, quantum theory, gravity or empirical prediction is supplied.
The [full physics mission](PHYSICS_MISSION.md) remains active.

## Evidence and remaining review

[Sealed design and argument](CONE_INTERACTION_DESIGN.md),
[eleven pinned inputs](CONE_INTERACTION_INPUTS.json),
[exact producer](cone_interaction.py),
[ten new tests](../../tests/test_physical_bridge_cone_interaction.py),
[run receipts](CONE_INTERACTION_RECEIPTS.json), and
[custody checker](cone_interaction_receipt_check.rb).

All first scientific runs succeeded. The all-head fetch changed no
remote head since the preceding checkpoint. No other seat's tree was
edited, and no corpus absence or literature novelty is asserted.
The source's specified equations were personally checked; this is
not an entire-paper rereading.

The pre-seal governance run retained the same four historical failure
rows: attribution, two old vacuous tests, five old seal-provenance debts,
and 41 stale relay debts. A metadata comparison initially read the
still-running capture and reported differing rows; it was premature,
not a scientific failure. After the process exited, its complete log
and actual exit 1 verified the unchanged historical rows.
No full-repository suite or independent analytic/banking acceptance
is claimed. The staged post-result governance run has 26 passes and
the same four historical failure rows. Cumulative custody passes
989 current artifact digests, 341 distinct sealed paths, 190 selected
local Markdown links and preservation of the same 24 historical
failed/error test IDs. It does not rerun those old tests. The dedicated
checker verifies four frozen scientific paths, eleven input pins and
all five published raw science/audit captures with their actual exits.

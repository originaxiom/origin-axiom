# Nonabelian action admission for complex conical end data

September 30, 2026. Path-local R62 pre-execution design and authored
argument. This advances PHYSICS_MISSION by testing the nonlinear
admission of R61's candidate end data in the SAME supplied action.
It is not a new index census or a claim that all ends have this form.

## Quantifier and prior

Test a constant harmonic torus-link helicity trace with a general
constant radial simple-pole coefficient in a fixed positive unitary
frame of a compact parent algebra. The metric is the INCOMPLETE cone,
not the complete hyperbolic cusp. Permit controlled subleading terms.
The action is the existing unshifted positive residual-square action;
no extra apex field, source or subtraction is supplied.

Authored prior: finite bare action forces a normal tangential matrix
and a commuting anti-Hermitian radial coefficient. A nonnormal trace
cannot be rescued by this general radial simple pole. Normal traces
survive, including a nonzero Cartan family. This restricts the stated
asymptotic class, not every nonabelian background or boundary law.
The exact controls below may expose mistakes in the argument or signs.

## Existing work and primary source

All origin heads were fetched; SM remains ba41670b and this lane starts
at 5eff8958. The other local fork remains 490d77c4; its untracked work
is neither used nor edited. R61 verified the complex critical-channel
reality/current map but explicitly left interaction admission open.
R60 supplies the boundary variation; R59 identifies the actual parent
coefficients and cubic tensors. R28 distinguishes actual residual energy
from rough derivative or harmonic-map energy. R39 already supplies a
NONCOMMUTING positive background on a DIFFERENT, hyperbolic metric.
Neither that positive nor F01's complete finite-harmonic-energy theorem
is a calculation on the present cone; no general T-brane kill follows.

Read the corresponding reports and R28's action argument. The ladder,
framework, campaign, LAW_MAP and PB-BOUNDARY point to this duty. The
epoch-limited atlas, old kill graph, identification audit and the query
'nonabelian cone moment-map normal radial' were checked. Targeted body
and code searches recover R35's previous full T-brane reading and R39's
use of it. These searches are not a whole-corpus absence certificate.
An initial filename glob failed; it was replaced by rg --files, not
counted as evidence of absence. No literature novelty is asserted.

Personally reread Braun et al. 1812.06072v2, equations 2.9--2.19:
the Hermitian convention, the full curvature and moment-map residuals,
the positive potential, and the fermion variations. The model's action
and compact trace are physical inputs, not derived by this calculation.
https://arxiv.org/html/1812.06072v2
R35's T-brane source is recovered, not rediscovered; only its opening
scope was revisited now. No entire-paper rereading is claimed.

## Exact leading residuals

Let g=dr^2+r^2 h on (0,R) times a flat torus, with torus area A and
constant complex harmonic one-form w. Let c=|w|_h^2>0. Matrices live
in a fixed faithful unitary representation; dagger is its positive
adjoint, and ||T||^2=tr(T^dagger T). Write the complex connection as

    C = (B/r) dr + w X,
    F = dC + C wedge C,
    I = div_g(C+C^dagger) + g^(ij)[C_i,C_j^dagger].

The physical convention is C=phi+iW with phi,W Hermitian. The adopted
static potential is (1/g7^2) integral (2|F|^2+|I|^2/2), with the
2-form norm using 1/2!. No boundary integration by parts is dropped.
The coordinates have dimensionless declared metric units, not a
predicted length scale.

Direct substitution gives

    F_ra = w_a [B,X]/r,       F_ab = 0,
    I = M/r^2,
    M = B+B^dagger+[B,B^dagger]+c[X,X^dagger],
    V_(epsilon,R) = (A/g7^2)(1/epsilon-1/R) K,
    K = 2c ||[B,X]||^2 + ||M||^2/2.

Both [B,B^dagger] and the curvature cost of B must be kept. Omitting
either can falsely admit a proposed cancellation. In contrast the
fixed-frame quadratic one-form pairing is
A(R-epsilon)(||B||^2+c||X||^2), finite. This is a norm comparison for
these fluctuations, not a new gauge-invariant energy assigned to C.

Check the residuals independently from the metric volume r^2 sqrt(det h),
its inverse and actual matrix derivatives, rather than using K as the
definition of the answer. Use both square and hexagonal link data from
R61, h=H^-1 with det h=1. The flat-product metric comparator must give
a different radial divergence. Trace normalization can multiply all
energies by a positive representation index without altering admission.

## Radial cancellation theorem

For finite matrices and c>0, K=0 if and only if

    B+B^dagger=0,    [X,X^dagger]=0,    [B,X]=0.

Proof: K=0 forces [B,X]=0 and M=0. Trace cyclicity gives

    Re tr(B M) = 2 ||(B+B^dagger)/2||^2
                  + c Re tr([B,X] X^dagger).

The second term vanishes by curvature; the left side vanishes by the
moment map. Positivity forces B anti-Hermitian, hence [B,B^dagger]=0;
then M=0 forces X normal. The converse follows by substitution.
This proof holds in every faithful unitary matrix dimension, not just
the finite test fixtures. Its analytic application remains authored.

Use an actual root su2 inside R59's regular su5 gauge factor: E12, E21
and diag(1,-1,0,0,0). Its inclusion in the supplied parent is already
established by R59; this does not identify a new parent or particle.
For X=E12 and B=0, F=0 but I is nonzero. Choosing B=-c[X,X^dagger]/2
cancels I yet makes F nonzero. B proportional to E12 tests the often
omitted radial commutator. Nonzero diagonal X with commuting imaginary
diagonal B is a genuine zero-residual control. Verify in 2 by 2 and
the literal 5 by 5 inclusion, and under a nontrivial unitary change of
basis; no conclusion may depend on the displayed matrix basis.

## Asymptotic robustness and honest exceptions

Allow C_t=wX+O(r^delta) and C_r=B/r+O(r^(-1+delta)), delta>0, with
uniform first weighted radial/tangential derivative bounds. The leading
F and I above persist, so K>0 still forces a positive 1/epsilon divergence.
If K=0, residual norms are O(r^(-2+delta)), giving the sufficient bound
integral r^(2delta-2)dr, finite for delta>1/2. Equality is logarithmic
and smaller delta need not be finite; cancellation can still make special
remainders better than this bound. A scalar commuting r^delta w profile
with B=0 supplies exact finite, logarithmic and power-divergent controls.

This excludes neither different leading powers/logarithms, nonconstant
leading data, singular coefficient metrics, other metrics, finite-radius
ends, nor justified extra sources/counterterms. It does not decide the
complete cone indicial spectrum, all charged sectors, or global gluing.
R39's noncommuting positive remains intact.

## The boundary constraint is nonlinear

Normal X form a compact-gauge-invariant set, not a complex vector space.
If a COMPLEX LINEAR space L consists only of normal matrices, polarizing
[X+zY,(X+zY)^dagger]=0 at z=1,i gives [X,Y^dagger]=0 for all X,Y in L.
Since Y is normal, diagonalizing it shows [X,Y]=0 as well. Thus such a
space is simultaneously unitarily diagonalizable. If L is additionally
invariant under the full compact reductive adjoint action, it is a
complex ideal and can contain no simple factor (each has a nonnormal
root vector). It lies in the center. Do not impose this extra linearity
on a nonlinear vacuum space or select a Cartan by hand as physics.

The su2 control X1=sigma3, X2=sigma1 has both normal, but X1+iX2 is
nonnormal. At the origin the first variation of [X,X^dagger] is zero
in every direction; along a nonnormal ray its quadratic coefficient
is nonzero. A finite linearized zero-mode list can therefore overstate
finite-action deformations. This is not a proof that all associated
fermions or the constant four-dimensional gauge vector disappear.
R61's critical one-form is not the scalar gaugino profile.

The supersymmetry variation of chi contains I, and the variation of psi
contains F. A trial cancelling just I is not a supersymmetric solution.
Full supersymmetry closure, the nonlinear quotient and the physical
fermion boundary domain still need their coupled analysis; these
residual tests do not silently supply an end action.

## Execution and acceptance

Seal design, input pins, exact producer and tests; commit/push and
confirm the remote before executing science. Require independent
metric-derived residuals, the symbolic cyclic trace identity, both
failed partial cancellations, nonzero zero-residual controls, unitary
covariance, explicit radial convergence thresholds and the nonlinear
normality comparator. Run ten new tests with R61's eight and R59's
seven. Keep every first stdout and exit, and do not edit sealed science.

A pass earns the stated finite-action theorem and controls, not a
complete boundary theory or chiral Standard Model. Next determine an
actual coupled nonlinear boundary law or alternative asymptotic solution
in this same parent, with gauge quotient, supersymmetry and all relevant
domains. Do not count a new chiral spectrum before admitting the theory.

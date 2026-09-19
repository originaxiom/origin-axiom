# R33: charged mirror interaction — authored algebra, not a quantum gap

2026-09-19. Pre-execution argument. This treats the specific ADDED
H-subgroup EFT below. It does not classify all completions of the
object, replace the original singular domain, or certify symmetric
mass generation (SMG). Four-dimensional spin spacetime and the
fermion interpretation are retained inputs.

## 1. The actual global group and fields

Use R21's H=C_(E6/Z3)(u), not an imported fundamental 27 of E6/Z3.
In the frozen E6 simple-root coordinates, C is the Cartan matrix,
u=C^-1 e0, and the charge of a weight w is w0. R21 constructs a
genuine H representation 16_1 + 10_-2 + 1_4. Its 16_1 weights equal
the positive charged roots of the actual R19 adjoint, weight by
weight. The H character lattice in these coordinates is integral.

For each putative light Dirac pair use LEFT-Weyl fields

    psi : 16_1,       chi : conjugate(16)_-1.

Here chi is the left-Weyl conjugate of the opposite-chirality partner,
not an extra independently counted generation. Add a complex scalar
S in 10_2 (the conjugate of R21's allowed vector) and retain a complex
Phi in 1_4. R29 has fields of this latter charge on contractible source
tubes; this is a possible place to realize the algebra, not proof that
the required four-dimensional S or its interactions are already present.

The faithful D5 identification is explicit. In the repository order
of nodes 1,2,3,4,5 take the Euclidean simple roots

    e4+e5, e4-e5, e3-e4, e2-e3, e1-e2.

Let B have these rows. B B^t=C[1:,1:], and the Euclidean weight of w
is B^-1 (Cw)[1:]. This maps the actual psi roots to all half-sign
weights with an even number of minus signs, chi to their negatives,
and S to the ten weights +/-ei. Lattice membership and this map are
tested; matching the labels "16" or "10" would not suffice.

## 2. A full intertwiner and the real-vector gap

On five Pauli factors define Hermitian Clifford matrices

    gamma_(2k-1)=Z^(tensor(k-1)) tensor X tensor I^(tensor(5-k)),
    gamma_(2k)  =Z^(tensor(k-1)) tensor Y tensor I^(tensor(5-k)),
    Gamma=Z tensor Z tensor Z tensor Z tensor Z,
    Cc=gamma_2 gamma_4 gamma_6 gamma_8 gamma_10.

They obey {gamma_a,gamma_b}=2 delta_ab, Cc^t=-Cc, Cc^dagger Cc=I,
Cc gamma_a Cc^-1=-gamma_a^t. Cc gamma_a commutes with Gamma.
Its two 16-dimensional blocks Y_a are symmetric. On either block,
T_ab=(gamma_a gamma_b)/2 for a<b obeys

    T_ab^t Y_c + Y_c T_ab = delta_ca Y_b - delta_cb Y_a.

These 450 identities per chirality establish the FULL Spin(10)
intertwiner, not just Cartan charge conservation. Consequently

    y_m S_a chi^t epsilon Y_a chi + h.c.

is an H-invariant Lorentz scalar: the U1 charge is 2-1-1=0 and the
spin tensor epsilon and internal symmetric Y give the appropriate
fermionic antisymmetry. Nonzero Yukawa coefficients are inputs.

Direct Clifford algebra gives

    Y_a^dagger Y_b + Y_b^dagger Y_a = 2 delta_ab I.

Therefore Delta(n)=sum n_a Y_a for REAL n satisfies
Delta^dagger Delta=|n|^2 I. Its 16 mass singular values are |y_m||n|.
Delta need not be Hermitian; the first chosen Y is anti-Hermitian.
Calling its eigenvalues real masses is not valid in this convention.

## 3. Why the complex charge cannot be ignored

S is complex under H, even though the D5 vector is real. Write
S=x+i y with real Euclidean vectors. For rho=S^dagger S,

    (Delta^dagger Delta-rho I)^2
        = [rho^2-|S dot S|^2] I.

A real orthogonal rotation puts x=a e1, y=c e1+b e2; direct
Clifford multiplication then gives the right-hand side 4 a^2 b^2 I.
The trace of Delta^dagger Delta-rho I vanishes. Away from the
degenerate case its two squared singular values are

    rho +/- sqrt(rho^2-|S dot S|^2), each eightfold.

Continuity covers zero discriminant. In particular S=e1+i e2 is
nonzero, but S dot S=0 and Delta has rank EIGHT, with squared
singular values 0 and 4. Nonzero scalar norm alone is NOT enough.
The real-up-to-phase locus instead has a uniform pointwise gap.

## 4. The existing scalar charge permits a real-structure map

For nonzero Phi define the antilinear map on the complex vector

    J_Phi(S)=(Phi/|Phi|) conjugate(S).

It squares to one and is H-covariant: under the central phase z,
Phi -> z^4 Phi and S -> z^2 S, so J -> z^2 J. The Spin(10) vector
matrices are real. Thus Fix(J_Phi) is an honest real rank-ten bundle
after the Phi reduction, not a globally chosen square root of Phi.
Locally it consists of S=e^(i arg(Phi)/2) n, n real. Sign changes
between half-phase charts are already part of the reduced bundle.
R21's kernel of the primitive character is connected Spin(10);
one must not invent an additional independent Z4 from the charge label.

An allowed renormalizable potential illustrating this reduction is

    V_S = r S^dagger S + lambda (S^dagger S)^2
          - kappa [Phi^dagger S dot S + h.c.],

with positive lambda and kappa. The FULL paired S weights sum to
the Phi weight, not merely to its U1 charge. A stable Phi radial
potential is also needed; here its nonzero amplitude is held fixed.
In a local gauge Phi=f>0, S=(x+i y)/sqrt(2), this is

    (r-2 kappa f)|x|^2/2 + (r+2 kappa f)|y|^2/2
      + lambda (|x|^2+|y|^2)^2/4.

For r<2 kappa f the classical minima are y=0, |x|^2=v^2 with
v^2=(2 kappa f-r)/lambda. The Hessian has one radial eigenvalue
2 lambda v^2, nine zero tangent eigenvalues, and ten imaginary
eigenvalues 4 kappa f. At fixed norm the target is S9.

This is NOT symmetric mass generation: a chosen nonzero x breaks
Spin(10) to Spin(9), with nine broken generators. A disordered phase
with zero vector expectation, positive fermion and boson gaps and
no unwanted topological/charged sector must still be established.
The fact pi_j(S9)=0 for j<9 removes these particular homotopy
obstructions; it is not a proof of the required quantum phase.

## 5. Two controls that a physical completion must survive

First, the conjugate term

    y_p S_a^dagger psi^t epsilon Y_a psi + h.c.

is ALSO H invariant. Gauge symmetry does not single out the mirror.
Localization, internal form-degree couplings or another supplied
mechanism must derive the hierarchy between y_m and y_p. Setting
y_p=0 is a model input, not an outcome of these representations.
R31's core cut-off trials suggest a localization question, but are
not exact interacting eigenstates or a computed Yukawa overlap.

Second, a fixed classical scalar with a full unitary symmetric
Yukawa block M Y and Dirac mixing mu has mass matrix

    [[0, mu I], [mu I, M Y]].

Takagi-transforming Y reduces this to sixteen two-by-two problems.
At nonzero mu,M both masses are positive:

    (sqrt(M^2+4 mu^2)+M)/2,
    (sqrt(M^2+4 mu^2)-M)/2.

The exact control mu=2,M=3 has masses 4 and 1, not an unpaired
massless sector. The Schur complement gives -mu^2 Y^-1/M.
This control breaks Spin(10); it must not masquerade as an SMG
solution which preserves the symmetry and removes only chi.

## 6. Anomaly, C3 and geometry remain in the same accounting

The vectorlike psi+chi UV representation has zero full H anomaly.
Removing chi while pretending H stayed unbroken would leave R21's
nonzero light anomaly. On the Spin(10) subgroup the linear and cubic
trace polynomials vanish. This is only the perturbative check, not
a new global bordism calculation or a quantum gapping theorem.
R21's ordinary-spin anomaly trivialization and charged-Phi matching
are prior; no new complete determinant is computed here. In a phase
where Phi reduces H, any effective H description still owes the
matching functional, including defects where Phi vanishes.

With the inherited single-line C3 lifts of R32, the three fixed-arc
fibre weights are 1,zeta,zeta^2. Raising to charge four permutes them.
Every scalar lift hence permits a nonzero invariant Phi on only ONE
arc. A vacuum with nonzero Phi on all three arcs either breaks this
global C3 or requires independent compensating flavour lifts/fields.
R29 has independently added tube fields; it did not derive such lifts.
This is not a ban on three sources or on a globally C3-invariant action.

Neither this algebra nor the literature proves that S and its coupling
arise from the source geometry, that physical and mirror interactions
separate, or that quantum backreaction preserves R29's Poisson model.
At finite source width the extra-U1 issue remains R29's operator
problem; its zero-width gap must not be inferred from a constant-mode
mass. Full parent covariance, source/end dynamics, complete cusp
limits and a common gravity sector are still separate obligations.

## 7. Acceptance standard for the next quantum step

Specify a local positive-norm regulator and action with the SAME
fields, charges, geometry and source domain. Then measure or bound:

1. Fermion AND boson gaps and connected correlators under increasing
   volume and cutoff control, not a gap on each frozen scalar alone.
2. Absence of symmetry-breaking order and unwanted topological sectors.
3. Both physical/mirror cross-correlators and normalized gauge currents.
4. The complete low-energy channel set, including composite fermions;
   an elementary propagator zero alone is not a spectrum census.
5. Full gauge variation, anomaly matching and the controlled chiral
   continuum/low-energy limit. Account for actual finite mixing.

This is the interacting duty R32's linear theorem leaves open. The
known pointwise intertwiner is a necessary construction, not the answer
to these tests. External proposals and cautions are read and scoped in
MIRROR_INTERACTION_PRIOR.md; no paper is treated as a certificate for
this added geometric model.

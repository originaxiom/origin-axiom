# Global matching fixes the real Cartan tail amplitude in a fixed orbit

October 25, 2026. UNREVIEWED analytical continuation, no scientific
import, collection, numerical shooting, new test run or banking.
This is a standard scalar maximum-principle argument applied explicitly
to the existing action. It is not a claim to have discovered harmonic-
metric uniqueness or selected a physical Standard Model vacuum.

## Scope and recovered sources

The [radial-flow note](SAME_ACTION_RADIAL_VACUUM_FLOW_AND_RESPONSE.md)
constructs small nonconstant zero-residual HALF-LINE tails with a stable
amplitude c. It explicitly does not show that they extend to the core.
This asks whether c remains free when a particular global background
and real Cartan deformation class are fixed.

Call this coefficient c_tail below, to distinguish it from the old
neutral amplitude in Q0+c psi Z. Neither is identified with the SM
seat's Higgs-direction mixing r or with a chosen chiral boundary plane.

Reused source bodies: the full curved-action, global-condensate,
graded-condensate and SM-parallel proofs, plus the full neutral-stability
proof. The source's metric, spin line, compact E8 and chosen triple/
holomorphic Higgs data are not derived here. The existing nonparallel
neutral minimum Q=Q0+c psi Z remains valid and is OUTSIDE this real
Cartan rescaling class. Its genuine modulus is not removed by this note.

The earlier received projective-global-metric proof, section 6, was
also checked: it uses a maximum principle for bounded distance in a
different flat-representation/harmonic-map problem. That result is
not silently transferred into this spin-valued action. Targeted searches
of the current lane used Cartan/rescaling, global amplitude, scalar
maximum principle and exp(2u); no whole-repository absence or priority
claim is made. The proof below is given directly.

## Fixed data, not a hidden vacuum selector

Take an existing global zero-residual background of the source:

    A0=s H0/2+C, q0=Omega^(1/2) E0/2, r0=0,
    [H0,E0]=2E0, [E0,E0 dagger]=H0,
    F0=-Omega^2 H0/4.

Here C is the source's permitted flat centralizer connection, commuting
with the whole compact triple; it is held fixed. H0 is a globally
parallel adjoint section, and q0 is the actual global spin-valued
section, not an assumed constant scalar on a nontrivial bundle.
Use a nonzero triple. The graded/SM principal embeddings and the
root example retain their separate gauge and gap conclusions.

Let u be a global smooth REAL scalar on the same complete connected
surface, with no physical boundary or inserted singular source.
Use the same orientation, metric and Hodge star, with *dx=dy and
*dy=-dx. Define actual compact fields on the same bundles:

    q_u=exp(u) q0, r_u=0,
    A_u=A0-(H0/2) star_g(du).                  (1)

Here star_g is the Hodge star on one-forms, not a new coefficient.
The zero R is only a background value; all its fluctuations and
interactions remain in the same source action. Locally,

    delta A_x=(H0/2) partial_y u,
    delta A_y=-(H0/2) partial_x u.             (2)

Since H0 is parallel and the added connection components commute,
these formulas are globally well-defined and give

    F_u=F0-(H0/2) Delta_flat u,
    [q_u,q_u dagger]=exp(2u) Omega H0/4.       (3)

This is a restricted complex-gauge/harmonic-metric orbit, not the
whole physical configuration space. A nonconstant u is not declared
unitary gauge: its Higgs norm changes. Other Higgs components, flat
data, spin lines, sources and geometric ends have not been varied.
The factor exp(u) is nowhere zero. Higgs zeros or a singular logarithmic
rescaling are therefore not covered by the smooth global comparison;
their bundles, holomorphic divisors and operator domains need separate
analysis rather than dismissal by the argument below.

## Check all residuals, including the actual moment coefficient

Use the old Dbar_A=partial_x+i partial_y-i ad A. The coefficient of
delta A_x+i delta A_y is (H0/2)(u_y-i u_x). Therefore

    Dbar_(A_u) q_u
      =exp(u)((u_x+i u_y) q0-i[delta A_x+i delta A_y,q0])
      =0,

where Dbar_(A0)q0=0 and [H0,q0]=2q0. Both R residuals vanish as well.
The remaining moment equation is exactly

    F_u+Omega[q_u,q_u dagger]
      =H0( Omega^2(exp(2u)-1)/4-Delta_flat u/2 )=0.

With Delta_g=Omega^-2(partial_x^2+partial_y^2), the convention in
which Delta_g u<=0 at a local maximum, this reduces to

    Delta_g u=(exp(2u)-1)/2.                  (4)

The sign and factor come from the existing spin connection, kinetic
metric and moment map. Neither is an adjustable scalar potential.
Solving a holomorphic equation alone would miss this constraint.

## Global zero-end matching: the real amplitude is forced to zero

Require u to tend UNIFORMLY to zero at every noncompact end. For the
source's once-punctured elliptic surface there is one such cusp.
This end condition holds for the small radial tails under discussion;
it is not inferred here from finite norm or finite area alone.

Suppose u has a positive value. Since it tends to zero at the ends,
its positive supremum is attained in a compact region, at an interior
point. At that point Delta_g u<=0 but the right side of (4) is
strictly positive, a contradiction. If u has a negative value, its
negative infimum is likewise attained in the interior; Delta_g u>=0
there but the right side of (4) is negative. Hence

    u=0 everywhere, q_u=q0, A_u=A0.           (5)

This uses no discarded boundary integral, numerical sample or
unproved shooting fit. Smoothness, the specified equation, compact
core/no physical boundary and uniform end matching are essential.
An actual finite interface with prescribed nonzero values would be
a different boundary-value problem, not a counterexample to (5).

## Link to the local tails, with no change of kinetic conventions

For an x-independent u(t), t=log y, put

    f=exp(u), h=1-2 dot u.

Equations (1)--(2) give precisely A_x=-hH0/(4y),
q=f E0/(2sqrt(y)). The cusp Laplacian is

    Delta_g u=ddot u-dot u.

Thus (4) is equivalent to

    ddot u-dot u=(exp(2u)-1)/2,
    dot f=(1-h)f/2, dot h=h-f^2,              (6)

the SAME radial flow. Its local stable tails are not false solutions;
they solve a half-line problem. But a nonzero stable coefficient c_tail
cannot be extended to a smooth global solution WITHIN (1) and the
zero-end class. Such a matching forces c_tail=0. Adding non-Cartan fields
in the core, changing holomorphic data or inserting a source is
outside this global comparison, not excluded by it.

## What this reduces, and what remains supplied

| Item | Conditional conclusion |
|---|---|
| Local stable amplitude c_tail in the radial tail | Real local integration data; not a free global vacuum parameter inside the fixed orbit and end class: global matching forces zero |
| Normal mass profile in this orbit | Must recover the old constant graded profile; it is not independently tunable while claiming the same smooth global data |
| Existing neutral c psi Z, two-field solutions, magnetic stationary phases | Preserved; they are different Higgs directions/data or nonzero-moment stationary problems, not covered by (1) |
| Holomorphic orbit, spin, flat centralizer, metric, E8 action, parent map | Still supplied/conditional; equation (5) does not select them among all admissible completions |
| Physical chirality, SM3, values and gravity | Not obtained; the old charged pairing/index conclusions keep their actual scope |

This is a conditional removal of a LOCAL matching freedom from one
specified global class, not a complete foundational-input payment.
It shows why solving the real moment equation globally can eliminate
apparently arbitrary end data. It does not authorize discarding all
other orbits, interacting components or end mechanisms as unphysical.

The bounded radial-flow theorem and its half-line existence argument
remain distinct; nothing here upgrades them to a complete asymptotic
classification. The raw Q8 trace module is still not identified with
the complete physical fermion complex by this scalar calculation.

## Verification and next task

The ten radial checks were designed and implemented before this
successor; they have NOT run and do NOT test the global maximum-
principle hypotheses or certify (5). Their sources/pins remain unchanged.
This argument requires separate review of the gauge/spin signs,
global field class, elliptic convention, uniform end hypothesis and
its distinction from the neutral modulus. New executable controls
would need their own sealed successor and genuine admission.

The constructive next task is to determine which NON-CARTAN or
different holomorphic state data are actually generated/admitted,
then solve their same-action moment/end problem. A favourable index
or boundary plane may not be supplied instead. No new independent
review, main acceptance, science execution or banked result is claimed.

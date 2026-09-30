# Peripheral matching and the limits of bounded transport

September 30, 2026. Path-local R65. Authored algebraic and analytic
argument; finite symbolic tests are controls, not independent review.
All statements concern the literal constant-helicity cone end and
the hypotheses below. No global physical theory is proved.

## Two periods remove the logarithm ambiguity

Let w=(w1,w2) be the period vector of the complex helicity one-form
on a unit-marked flat torus, with Im(w1/w2) nonzero. Let X be a normal
complex matrix in a positive Hermitian coefficient metric. In a
single-valued trivialization C_link=wX has peripheral matrices
exp(w1 X), exp(w2 X), up to simultaneous inversion if the parallel
transport convention is d+C rather than d-C. The conclusions are
unchanged by that inversion.

For any eigenvalue xi=u+iv of X, the logarithms of the two eigenvalue
MODULI are

    (Re(w1 xi), Re(w2 xi)) = R (u,v),
    R = [[Re w1, -Im w1], [Re w2, -Im w2]].

The determinant is nonzero. Therefore both moduli being one implies
xi=0. Normality then implies X=0. This uses eigenvalue moduli rather
than principal logarithms and includes every 2pi i branch. A nonzero
nilpotent X would evade the last implication; it is not normal and
does not belong to this end class.

The same conclusion holds after multiplying by commuting unitary
transition matrices U1,U2 that preserve X. Simultaneous unitary
diagonalization within X's eigenspaces changes phases, not moduli.
This covers scalar unitary characters and compatible finite unitary
local systems, not arbitrary noncommuting added fields. A new marking
P in GL(2,Z) replaces R by PR, preserving invertibility. A finite-index
sublattice likewise has nonzero real determinant. Finite covers of
unitary peripheral representations remain unitary. None of these
operations permits nonzero X against unit-modulus peripheral spectra.

Checking only one peripheral generator would fail: on the square link
w=(i,1), xi=2pi i has exp(w2 xi)=1 while exp(w1 xi)=exp(-2pi).
If the ratio w1/w2 were real, the real map would have a kernel. These
are discriminating controls, not part of the admitted helicity class.

The two supplied monomial families have matrices diag(t^v)P. The
producer checks their relators and actual marked periods in two
independent arithmetic representations. Vanishing exponent vectors
on BOTH marked periods imply literal permutation matrices for every
t in C*, including exceptional parameters. The actual inclusion words
transport this property to M6. No H1 rank, eigenvalue sampling or
generic-parameter inference is needed. On an untwisted trivial cone
X=0 has identity holonomies; nonidentity permutation holonomies require
the corresponding flat unitary local system, not silently integer
Fourier conditions. Even with that compatible twist, nonzero X is
excluded by the preceding modulus argument.

## The projective meridian cannot have a normal bounded limit

Use the actual R42 generators M(q), N(q), q>0. Put K=M-I and
L=K-K squared/2. Direct multiplication gives K cubed=0,
K squared nonzero and L cubed=0. For every nonzero integer n,

    M^n = I+nL+(n squared/2)L squared,
    (M^n-I) squared = n squared L squared != 0.

Thus every nontrivial meridian power has a nontrivial Jordan part.
Taking the dual or multiplying by a nonzero central scalar does not
remove that part. A finite peripheral cover contains some nontrivial
meridian power, whatever basis it uses. A normal X gives commuting
normal exponentials; compatible commuting unitary twists preserve
normality. Such matrices are diagonalizable, so their representation
cannot be similar to this projective peripheral representation.
This is a restriction on an attempted NEW cone end, not a criticism
of the existing canonical projective background on its own metric.

Here is the needed analytic qualifier. Suppose a flat connection has

    C_r=B/r+E(r), B dagger=-B,
    norm(E(r)) <= A r^(-1+delta), delta>0,

uniformly on the radial path, and its tangential coefficients converge
uniformly along the two marked loops to wX. Solve radial transport
P'=-C_r P. Factoring off the unitary matrix exp(-B log(r/R)) leaves
a coefficient with integrable norm. Gronwall applied to transport and
its inverse gives a uniform bound by exp(A R^delta/delta), after
normalizing at r=R. This proof also works for radially varying
anti-Hermitian leading transport; a limit at the apex is not needed.

Flatness conjugates fixed-loop holonomies by this bounded transport.
Every sequence approaching the apex has a subsequence of transports
converging to an invertible matrix: both the matrices and their inverses
are bounded in finite dimension. Uniform convergence of the tangential
connection gives convergence of its loop holonomies. Consequently the
limiting pair is still simultaneously similar to the fixed pair.
A Jordan part cannot disappear. R64's g=exp(fT), f->0, satisfies the
bounded property directly, so its nonlinear continuation does not
change the peripheral conjugacy class of its own C0.

## Unbounded transport is not excluded by that argument

For E=E12, U=I+E and r>0, take

    G=diag(r^(1/2),r^(-1/2)).

Then GUG inverse=I+rE tends to I, although U is nontrivial unipotent
at every r>0. The condition number of G is 1/r. Its induced radial
connection -G'G inverse has a Hermitian, not anti-Hermitian, simple
pole and violates the bounded-transport hypothesis.

A closer countercontrol is s=-log r, r<exp(-1),

    G=diag(s^(-1/4),s^(1/4)),
    GUG inverse=I+s^(-1/2)E,
    -G'G inverse=diag(1,-1)/(4r log r).

The tangential trace tends to zero and r C_r tends to zero, but the
radial norm has divergent integral and the errors are not O(r^delta)
for ANY delta>0. These are exact flat gauge transforms of the original
flat nilpotent connection. They are NOT asserted to solve the moment
equation, have finite action, or belong to a chosen physical domain.
They prove that a zero leading trace alone cannot erase global
unipotent data, and identify a precise asymptotic class to test next.

## A nonzero end that does match a global representation

For each declared link w2=1. Choose the normal trace-free rank-five
matrix X=2pi i diag(1,0,-1,0,0). Its longitude exponential is I.
Set both generators a,b of the actual knot presentation equal to
D=exp(w1 X). The determinant is one. The relator and preferred
longitude each have zero total abelian exponent, so their matrices
are I. Thus this IS a global SL5 representation whose peripheral
pair matches the nonzero local flat and moment-flat cone field.
It is a reducible abelian counterexample, not the existing irreducible
monomial family, a global harmonic extension or a physical vacuum.

The logarithm branch has a cost. For any nonzero root charge
a_root=2pi i(n_i-n_j), at the fixed unit-area scale,

    lambda_zero = 4pi squared c (n_i-n_j) squared,
    c=2 on the square link and sqrt(3) on the hexagonal link.

Hence every such charged zero-Fourier value exceeds 3/4. R63's
all-Fourier identity, rechecked here, is

    lambda_m = 2 norm(Im(w a_root)+pi m)^2_H
               + 2pi squared m^T H m.

For nonzero integer m the lower bound is 2pi squared on the square
and 4pi squared/sqrt(3) on the hexagonal link, also above 3/4.
No charged root in this positive example enters R63's critical
window at the DECLARED scale. Zero charges and neutral channels are
retained. Rescaling the link changes eigenvalues and is a changed
physical input, not an invariant no-go. This example also has imaginary
root parameter and does not import R64's real-positive-a radial proof.

## Consequence for the research route

Boundary matching is a necessary test before local parameters become
global modes. The above results, if the exact source checks pass,
separate the existing models and retain a positive matched control.
They do not derive the common physical end law, select a geometry,
construct chiral matter, or close more general nilpotent, sourced,
logarithmic or non-helicity ends. Those changed hypotheses require
their own action, gauge and boson/fermion-domain tests.

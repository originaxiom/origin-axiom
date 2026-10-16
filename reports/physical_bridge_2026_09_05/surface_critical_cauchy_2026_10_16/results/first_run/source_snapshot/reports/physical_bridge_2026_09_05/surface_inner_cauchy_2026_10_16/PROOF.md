# Cauchy transfer from a punctured interior at finite radius

Authored analytic normal-model argument before execution, not independent
functional analysis or a complete physical boundary law. The real parent,
singular trace, flat coefficient and zero-Higgs freezing are supplied.
The earlier total normal-family positive is retained; this computes its
source-frame finite-radius response, not a different global model.

## The actual polar equation and both holonomy sectors

Use the actual source velocities and definitions in DESIGN. Rotation
S=exp(-theta v2v3/2) sends v2 to v_r and v3 to v_theta. Its derivative
contributes v2/(2r) inside the polar Dirac expression; r^-1/2 removes
that density term unitarily from r dr to dr. The scalar R line is kept
in its Cartesian trivialization here. Since S(2pi)=-I, coefficient
holonomy eta=+/-1 yields angular lattice Z+1/2 for eta=+1 and Z for
eta=-1. Complex conjugation pairs m with -m; discarding either is wrong.

The full free normal equation after horizontal Fourier transform is

 f'+(m B/r+A)f=0, B=i v2v3, A=i v2 M_xi,
 A^*=A, B^*=B, A^2=rho^2 I, B^2=I, {A,B}=0.

The indicial powers in density-normalized f are +/-abs(m). Only m=0
has two L2 traces. At abs(m)>=1/2 the r^-abs(m) branch is not in
L2(dr), including logarithmic divergence at1/2. The regular branch is
unique per free seed. This counts normal data, not physical particles.

## Critical trace propagation

For either supplied sign sigma set K=sigma R_s B and Q=(I+K)/2.
Q is Hermitian rank8, C-real and Green-null, while {K,A}=0.
At m=0 the exact solution with singular coefficient in im Q is
f(r)=exp(-r A)q. At epsilon>0 its orthogonal trace projector is

 P0=exp(-epsilon A) Q exp(-epsilon A)/cosh(2epsilon rho)
   =(I-tanh(2epsilon rho) A/rho+sech(2epsilon rho)K)/2.

The normalization follows from Q exp(-2epsilon A) Q=cosh(2epsilon rho)Q.
At rho=0 the exact response is Q. No mass gap or critical sign is
selected. At rho=0 physical psi remains r^-1/2 S q, with finite radial
L2 norm. Thus this response does not erase the admitted half-pole.

For fixed rho, P0 tends to Q as epsilon tends to0. The exact distance is

 ||P0-Q||^2=(1-sech(2epsilon rho))/2.

Its supremum over rho is1/2 at every epsilon>0. There is no convergence
in the uniform frequency-projector norm. This is not a failure of the
singular domain; it forbids replacing a graph/resolvent-limit proof by
pointwise projector convergence.

## The noncritical regular branch

Put a=abs(m)>=1/2, nu=a-1/2, w in im Preg=(I-sign(m)B)/2. For rho>0,

 f(r)=sqrt(r)[I_nu(rho r)w-I_(nu+1)(rho r)(A/rho)w].

The two derivative identities for I_nu give BOTH first-order components
of the displayed radial equation, not only its square. Its leading
power is r^a w; the independent branch has a nonzero r^-a component
and is not L2. One may also derive this directly: write

 f=r^a[sum u_k r^(2k) w+sum v_k r^(2k+1)(A/rho)w], u_0=1,
 v_k=-rho u_k/(2a+2k+1),
 u_k=rho^2 u_(k-1)/(2k(2a+2k-1)).

The recurrence is obtained from the full first-order system and fixes
every coefficient; its entire series agrees with the Bessel expression
up to a nonzero scalar. At rho=0 the equation gives f=r^a w exactly.
The standard definitions, recurrences and small-positive-argument limit
used here are [DLMF10.25](https://dlmf.nist.gov/10.25),
[10.29](https://dlmf.nist.gov/10.29) and
[10.30](https://dlmf.nist.gov/10.30), personally read2026-10-16.

At s=rho epsilon>0 set k=I_(nu+1)(s)/I_nu(s). Positivity of its
defining series gives k>0 and no denominator zeros. Its derivative is
k'=1-2a k/s-k^2, with k~s/(2a+1). At a first crossing of1 from below
the derivative would be nonnegative, but the equation gives -2a/s<0.
Thus0<k<1 for all these a,s. This is the analytic proof; finite numerical
controls do not establish that quantifier.

The graph W=(I-k A/rho)Preg has W^*W=(1+k^2)Preg. Consequently

 Pm=(I-alpha A/rho-sign(m) beta B)/2,
 alpha=2k/(1+k^2)>0, beta=(1-k^2)/(1+k^2)>0,
 alpha^2+beta^2=1.

At rho=0 Pm=Preg. The response of noncritical modes is not Q: applying
the critical Q pointwise to every angular mode discards this equation.

## A uniform frozen frequency complement

Keep the SAME free normal expression on the exterior/core r>=epsilon.
Freezing at epsilon gives H=A+(m/epsilon)B, lambda^2=rho^2+(m/epsilon)^2.
The inward-to-core decaying solution exp[-lambda(r-epsilon)] has trace
Ccore=(I+H/lambda)/2. For m=0,rho>0 the exact compression is

 P0 Ccore P0=(1-tanh(2epsilon rho)) P0/2 <= P0/2.

For noncritical m and rho>0 Clifford multiplication gives

 Pm Ccore Pm=(1-d)Pm/2,
 d=(alpha rho+beta abs(m)/epsilon)/lambda, 0<d<=1.

The upper bound is Cauchy--Schwarz using alpha^2+beta^2=1. At rho=0,
m!=0 the compression is0. Every frequency except (m,rho)=(0,0) has
forbidden-trace squared norm at least1/2 on im P. No frozen Cauchy
intersection remains, with a uniform angle independent of m or rho.
The all-frequency argument covers both holonomy lattices, not a census
of sampled modes. This is a frozen family estimate; a full curved
pseudodifferential symbol calculus, finite-tube operator/domain theorem
and global cusp transport do not follow from it alone.

## Reality and retained regular gauge modes

Source C sends A(xi) to A(-xi), B to -B and R_s to -R_s. Thus it
preserves each critical sign and maps Pm(xi) to P_(-m)(-xi), including
all conjugates. R_s and all external Lorentz generators commute with
the response. Clifford normal current vanishes on each plane; reversing
the oriented end reverses the current, not its nullity. Arbitrary
constant gauge multiplicities are retained. Point-dependent gauge
transformations act on the entire covariant operator; the frozen Fourier
formula is not itself their global construction.

For eta=+1 a constant Cartesian spinor psi0 gives

 f=sqrt(r) S^* psi0
  =sqrt(r)[exp(-i theta/2)P_Bplus+exp(i theta/2)P_Bminus]psi0.

These are exactly the regular m=-1/2 and+1/2 branches at rho=0. They
reconstruct ALL16 source spinor components, including the scalar
gaugino, rather than projecting out their conjugates or imposing a
zero trace. A scalar/vector coefficient constant in the same free
unbroken gauge channel also solves the regular bosonic normal equation
with zero normal derivative and zero normal kinetic energy. This is a
free local massless-mode recovery, not proof of a complete N=1 domain,
global normalizable gauge multiplet or an unbroken SM phase.

## Physical obligations kept distinct

The interacting r^-1/2 Higgs mixes parity/angular modes; its existing
dressed singular traces are not the free response above. The actual
finite-tube tilted normal, extrinsic terms, varying R/gauge connection,
bosonic/auxiliary/source variations, nonlocal field dependence and SUSY
must be joined before calling this a physical boundary law. Singular
graph convergence, cutoff/cusp joining, global stationary fields,
charged zero modes/norms/vertices/anomalies, derivation of gauge phase
and three, observed parameters and gravity remain. Fixed based g2+u1
is not SM; different-parent positives are not freely composable. No
particle, index, gap, anomaly or vacuum-energy count is imported.

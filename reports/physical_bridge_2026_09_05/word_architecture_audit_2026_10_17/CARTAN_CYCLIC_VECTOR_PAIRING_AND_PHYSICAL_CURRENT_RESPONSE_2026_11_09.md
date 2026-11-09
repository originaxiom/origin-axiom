# Cyclic moment response, paired vector operators and the physical fermion map

2026-11-09. Author hand derivation, UNREVIEWED and UNRUN. This continues
the stationary-family proof at2b572014cdbbb4ef8a9287b0d7b18eb98e5816a2.
It includes an adversarial author check of that proof's ansatz and maps.
Independent analytical review, sealed controls and admitted execution
remain outstanding. All statements concern the supplied classical parent.

Retain its complete punctured elliptic surface, positive kinetic metrics,
eta=O, chi=0, either stated coherent h4 lift and both conjugate LEFT
fermion sectors. The two small complex cyclic coordinates are state data.
The proof of the global stationary family and the earlier physical kernel
and current witnesses are load-bearing conditional dependencies.

## 1. The nonlinear response remains in a global Cartan bundle

Use the unitary flavour coordinates q',r' in which the balanced fields
are E_+/(2ell), E_-/(2ell). In each principal Spin5 spinor four, order
the weights3/2,1/2,-1/2,-3/2. Its Hermitian Cartan is

    xi=diag(x,y,-y,-x),                 x,y real.

The native lowest grade-minus-three root is X=c e41. The cyclic matrix
in either factor has the form

    Q=p e12+r e23+p e34+f e41.                         (1)

Here f is the relevant local value of the actual global holomorphic
data. The equal edge coefficients are the Spin5 symplectic condition.
The Hermitian Cartan exponential preserves(1), taking its coefficients
to p exp(x-y), r exp(2y), p exp(x-y), f exp(-2x).

Each row and each column of(1) has one entry. Consequently both QQ†
and Q†Q are diagonal. Their difference is Cartan, while their sum is

    {Q,Q†}=diag(A,B,B,A),
    A=|p|^2+|f|^2,  B=|p|^2+|r|^2.                    (2)

This calculation allows arbitrary complex f and the actual independent
functions in both Spin5 factors. No equality of the two amplitudes or
of their profiles is imposed.

The background connection is Cartan. The declared A and D transitions
normalize the sum of the two Cartans, exchanging factors where required.
Thus these Cartans define a real rank-four subbundle globally. For a
Cartan Hermitian generator, the connection path A_x'=D_y xi,
A_y'=-D_x xi stays Cartan, and its curvature remains Cartan. Equation(2)
therefore makes the full nonlinear moment a Cartan section whenever
the generator lies in that subbundle.

At the balanced point the derivative Pv preserves the Cartan and its
orthogonal complement. This follows directly from the diagonal moment
calculation and the selfadjoint real Hessian. Its inverse R5 preserves
the same subbundle, using the earlier global coercivity bound.

Start the stationary proof's fixed-point iteration at xi=0. The quadratic
moment source and every subsequent nonlinear term lie in the Cartan.
The contraction therefore converges there. Uniqueness in the full small
D5 ball identifies that solution with the full response. This proves
Cartan closure for the small family constructed by that contraction.
It makes no classification of other stationary solutions or orbits.

## 2. Reconstruct the complete vector operator after that response

The same action and moment equation give

    Pv=nabla* nabla+{ad_qhat,ad_qhat†}
                         +{ad_rhat,ad_rhat†}.          (3)

On each charge-one half-root coefficient the two Spin5 modules are
V_(3/2) tensor V_(3/2). The unitary flavour change retains the sum in(3).
There q' acts on the first factor and r' on the second. In their actual
spinor representations(2) makes the potential

    diag(A_+,B_+,B_+,A_+) tensor I
       +I tensor diag(A_-,B_-,B_-,A_-).                (4)

All factors in Q include their physical source normalization. The
connection in the rough Laplacian is the responded unitary Cartan
connection. It carries the derivatives and global Green response.
Equations(3)-(4) retain those contributions together.

The operator consequently preserves every local weight pair(m,n).
Flat gluing can exchange the two factors. It preserves the total
principal grade mu=m+n and the property |m| unequal |n|. Both define
global reducing subbundles for Pv along this family, despite the new
spin fields having different principal grades.

## 3. Construct an antiunitary map and check its flat gluing

Work in one fixed Q=+1 coefficient. Let alpha=+1 or -1 be its coherent
highest-vector character. The source lowering phases give on its whole
sixteen-dimensional internal spinor

    A|m,n> = alpha i^(3-m-n)|n,m>,
    D|m,n> = exp[-i pi(m-n)/2]|m,n>,   B=DA.            (5)

This follows by lowering3/2-m times in the first factor and3/2-n in
the second, using Ad_A E_+†=i E_-† and its exchanged counterpart.
It retains the complementary gauge phase in alpha. Its reality follows
from the stated coherent Pin2 lift. Additional core twists would require
checking(5) again.

Define the antiunitary on the internal tensor product by its basis rule

    J0(c|m,n>)=bar(c)(-1)^(3-m-n)|-m,-n>.              (6)

This is the tensor of the two pseudoreal Spin5 spinor forms with one
coefficient conjugation. In particular J0^2=1. A Hermitian Cartan has
opposite eigenvalues on the paired weights. Because J0 also conjugates i,
it commutes with every unitary Cartan covariant derivative.
Equation(2) is invariant under this weight reversal, so J0 commutes with
the LOCAL differential operator(3).

Its global flat gluing has an essential extra sign. Substituting(5)
into(6), with alpha real, gives

    J0 A=-A J0,          J0 D=D J0.                    (7)

For example the scalar ratio in the first equation is
i^(-2mu)(-1)^(3-mu)=-1, since mu is integer. Thus J0 alone has the wrong
core character to be a bundle map within this fixed charge coefficient.

On the eight-dimensional mixed-magnitude subbundle W put

    L|m,n>=sign(|m|-|n|)|m,n>,       Theta=L J0.       (8)

L anticommutes with A, commutes with D and with J0, and has square1.
Equations(7)-(8) imply

    Theta A=A Theta, Theta D=D Theta, Theta^2=1.       (9)

The unitary Cartan frame changes also commute with Theta. Thus Theta
glues globally on W, preserves the physical vector norm and flips mu.
It acts within Q=+1. It differs from compact E8 conjugation, which also
flips electromagnetic charge.

Since L commutes with the Cartan connection and(4), the resulting global
antiunitary commutes with Pv on compactly supported smooth W sections.
It carries the positive closed quadratic form onto itself. Uniqueness
of its form-associated realization then gives the same identity on the
complete operator domain. This transfers the source domain and norm
along with the differential expression.

## 4. The two grade-two vector problems remain exactly paired

The mu=-2 and+2 planes lie in W. Equations(3)-(9) give

    Pv(t)|_(Q=+1,mu=+2)
        =Theta Pv(t)|_(Q=+1,mu=-2) Theta^-1.           (10)

This is an equality of antiunitarily equivalent complete operators for
every sufficiently small state in the proposed nonlinear cyclic family.
It applies to their whole spectra and norms.

At t=0 the negative-grade operator is
Dbar†Dbar+7/(2ell^2). The source parabolic argument gives one holomorphic
section in its rank-two plane, hence a simple eigenvalue
lambda0=7/(2ell^2) WITHIN THAT PLANE. The positive-grade plane is its
Theta image. The old w_R witness must equal Theta w_L up to phase at
the balanced point. Other grades may have the same pole and are retained.

The antiperiodic charged end retains compact resolvent. The small bounded
changes of D0 give small perturbations of its closed form and continuous
resolvents. A circle around the isolated simple eigenvalue in one grade
defines its rank-one spectral projection by the resolvent integral.
For sufficiently small state coordinates the circle remains disjoint
from the rest of that grade's spectrum. Equation(10) transports its
projection and eigenvalue to the opposite grade. Thus normalized
continuations w_L(t),w_R(t)=Theta w_L(t) have one common positive
lambda(t), with lambda(t) tending to lambda0.

The first derivative of Pv on the whole charge-one spinor is zero at
the balanced state. The connection response starts at second order and
E†X=X†E=EX†=XE†=0 in each four. Eigenvalue shifts consequently start at
second order. Equation(10) equates those shifts and every higher-order
shift in this family. A two-by-two compression chosen before retaining
the actual whole operator is unnecessary for this statement.

## 5. Differentiate the actual four-slot fermion operator

The previous vector result does not transfer the fermion zero modes
automatically. Write b=delta A, s=delta q, h=delta r for a real background
variation, and keep the physical fermion input(lambda,a,u,v). The weights
under dxdy remain(Omega^2,1/2,Omega,Omega). Differentiating every row of
the source M gives

    delta M_0 = ( i[b†,a]
                  +2i Omega([s†,u]+[h†,v]) )/(sqrt(2) Omega^2),
    delta M_1 = 2i([s,v]-[h,u])-sqrt(2)i[b†,lambda],
    delta M_2 = (-i[b,v]+i[h,a])/Omega-sqrt(2)i[s†,lambda],
    delta M_3 = ( i[b,u]-i[s,a])/Omega-sqrt(2)i[h†,lambda]. (11)

This includes the gauge-adjoint row, connection derivative changes,
holomorphic Hessian and conjugate spin/gaugino couplings. The trace-dual
output and the same Uin/Uout isometries are retained. It is a variation
of the physical map on its source graph domain.

For a real ray in the cyclic coordinates write its first spin tangent
as(s1,h1). The earlier moment solution yields

    xi2=-R5([s1hat,s1hat†]+[h1hat,h1hat†]),
    b2=-i Dbar_A0 xi2,
    s2=[xi2,q0],             h2=[xi2,r0].              (12)

Therefore M(t)=M0+t M1+t^2 M2+O(t^3), where M1 is(11) with
(b,s,h)=(0,s1,h1), and M2 is(11) with(b2,s2,h2).
M is linear in the background and its compact adjoints, so this expansion
has no separate quadratic insertion in M. The squared operators and
eliminated complements acquire quadratic terms through their products.

Let D_f(t) be the selfadjoint doubled fermion map with off-diagonal entries
M(t),M(t)†. Work in a fixed reducing colour/EM charged block with the
source's isolated finite zero eigenspace and gap at t=0. Let P be its
FULL zero projection, Q=1-P and R=Q(D_f(0)|_Q)^-1 Q. On a complement on
which that inverse exists, write D1,D2 for the expansion coefficients
of D_f(t). Its zero-energy Feshbach operator is

    t P D1 P
      +t^2(P D2 P-P D1 R D1 P)+O(t^3).               (13)

The formula retains all old zero modes before eliminating a complement.
If the spectral parameter is nonzero its complement inverse must retain
that parameter as well. The neutral A3 threshold continuum has no such
zero-energy inverse and remains outside this gapped reduction.

The existing charged-kernel arguments supply the conditional gap for
the half-root blocks and the separately analyzed up block. Their domain
and Hodge proofs remain review dependencies. Equation(13) specifies the
new matrix elements that must be computed. No numerical light spectrum
or persistence of the individual zero modes is asserted here.

## 6. Transport normalized currents with the light subspaces

For a normalized vector w, the source vertex is

    G_w(psi,chi)=g6 integral dxdy sum_i h_i
                                  kappa(psi_i†[w,chi_i]),
    (h_i)=(Omega^2,1/2,Omega,Omega).                   (14)

After a deformation, normalized fermion modes must be drawn from the
actual continued spectral subspace. Use the small cluster projection
P(t) around all the old zeros in the chosen charged block. Individual
eigenvalues can leave zero and remain inside this light cluster.

Write D1,D2 for the expansion coefficients of D_f(t). For
D_f(t)=D_f(0)+tD1+..., the resolvent projection gives

    P'(0)=-R D1 P-P D1 R.

A unitary transport of the whole light subspace can be chosen with
psi'(0)=-R D1 psi for psi in P, up to an internal unitary basis choice.
The corresponding first current derivative is the sum of

    G_w(psi',chi)+G_w(psi,chi')+G_w'(psi,chi).          (15)

The last term uses the actual vector derivative. For the grade-two
eigenvectors above it can be chosen zero at first order because the
whole vector-operator first derivative vanishes there. The fermion
terms generally remain. Freezing their old profiles would lose them.

For completeness, continuity of(14) here uses more than the L2 norm
of w. Core elliptic estimates apply to the smooth eigenvectors. On the
end, the antiperiodic angular Poincare bound and bounded responded
connection give a uniform angular quadratic-form bound
c exp(2T)-C, with c>0, after absorbing the connection cross term.
This bound concerns an integral over each circle. Its leading angular
gap persists with the bounded, possibly x-dependent coefficients.

Apply the eigenfunction energy identity with truncated weights
exp(phi), phi=a exp(T), and cutoffs, choosing a>0 small enough that
|d phi|_g^2=a^2 exp(2T)/ell^2 is absorbed by that angular bound.
The positive form(3), a compact transition region and eigenvalues in
a fixed bounded interval give a uniform weighted L2 bound. Remove the
cutoff by monotone convergence. The resulting tail estimate decays as
exp[-a exp(T)]. Local elliptic estimates on fixed-radius hyperbolic
lifts add at most the cusp's exponential volume factor, which this
decay absorbs. They give uniform supremum decay of the profiles.
Compact-core convergence and this tail estimate yield convergence
in supremum norm for the normalized continued vector line.

With w bounded, the vertex is bounded by a constant times
||w||_infinity ||psi|| ||chi|| in the physical metrics. The preceding
vector control and L2 continuity of the finite fermion clusters make
(14) continuous. The weighted energy identity, coefficient regularity
and uniformity of this tail estimate remain analytical review duties.

At the balanced point the old witnesses give nonzero left and right
current matrix elements of magnitude g>0. Transport their entire
fermion clusters and the paired vectors by the preceding isometries.
Their continued witness matrix elements tend to those original values.
In some sufficiently small neighborhood both magnitudes therefore
exceed g/2. They concern light subspaces descended from the old quark
and independent conjugate-quark fields. They need not be exact massless
eigenstates after the deformation.

A unitary mass-basis change inside either complete cluster preserves
the current map's singular values and nonzero norm. The positive
vector pole has a nonzero residue on the corresponding right-current
test channel. Other positive-norm same-pole modes add a positive
semidefinite contribution. Thus this small neighborhood retains a
right-current pole on those light states, alongside the left one.
Its actual finite-t coupling ratio still requires the full fermion
calculation. Equality of the vector masses alone does not fix that ratio.

## 7. Scoped outcome and next calculation

The candidate stationary family supplies a derived nonlinear moment
response and preserves a paired charged-vector spectrum. Near the
balanced state, its right-current witness also persists on the continued
light fermion cluster under the stated end estimates. This constrains
a proposed weak-chirality mechanism within this small cyclic family.

The full deformed fermion spectrum and normalized interaction matrices
remain to be calculated from(11)-(15). Large states, connection directions
outside the two separate Spin5 factors, other generated carriers or lifts
require their own operator and domain arguments. The earlier exploratory
(5,5) connection direction is a distinct existing lead whose obstruction
and global section map remain open. A root-level selection principle
still has to earn any preference among these constructions.

Review must scrutinize Cartan closure of the full nonlinear map, the exact
global phases in(5)-(9), the faithful norm/domain passage, simple-eigenvalue
continuation, every coefficient of(11), the charged gaps used in(13) and
the uniform end control needed in section6. This is author evidence.

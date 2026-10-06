# Conditional cubic correction, not all-order physical completion

Authored formal argument; independent analytic acceptance pending.
This extends the SAME supplied spectral tangent, not its coefficients or
charged-spectrum convention. Fork silver_cyclic_boundary_2026_10_04 owns
the harmonic lemma. Our spectral packet owns the smooth exact-block lift.

## 1. Boundary algebra and the real physical distinction

Write V=Omega(Sigma;ad D)[1] with invariant integrated trace pairing,
ghost numbers c=1,a=0,b=-1. For a flat reference its standard boundary
BFV Hamiltonian is S=S2+S3, with

    S2=integral Tr(c D a),
    S3=integral Tr(c [a,a]/2 + [c,c] b/2).

delta={S2,-}, delta^2=0. The classical master equation implies
delta S3=0. This is the holomorphic CS boundary algebra. It is not an
identification of BV ghosts with the physical twisted fermions, nor a
verification of kinetic/moment-map/superfield boundary equations.
Cattaneo--Mnev--Reshetikhin sections3.7/7.2 supply these standard formulas:
[primary text](https://arxiv.org/html/1201.0290v3).
The canonical normalization here is fixed by delta x=c below.

The spectral subcomplex A has nonharmonic0 -> exact1 as an acyclic pair
and harmonic Ah=(k,L,ann(k)). It is cyclic Lagrangian. Thus S2|A=0,
and delta is tangent to A. The cubic restriction s=S3|A is delta-closed.
No claim is made that S3|A itself vanishes: the preceding fixed-linear
counterexample is retained and an explicit compact control below has s!=0.

## 2. The first obstruction vanishes for this tangent

Contract A onto Ah using the supplied boundary Hodge/Green inverse.
On homogeneous polynomial functions, the induced doublets obey

    delta x_i=c_i, delta c_i=0, h c_i=x_i, h x_i=0,
    delta h+h delta=N.

Here N counts acyclic legs, not harmonic legs; h has ghost number-1.
One may define the splitting/projection and operators on smooth cubic
multilinear functionals without a countable basis. The identities follow
by derivations from the linear contraction. The Green inverse gains one
derivative on smooth boundary data. This is a fixed-order formal operation;
it does not assert convergence of a nonlinear infinite series or a global
nonlinear boundary manifold.

The N=0 component of s is S3 on harmonic Ah. It vanishes as an integrated
functional: k is a Lie algebra, [k,L] subset L and L is cup-isotropic, so
<k,[L,L]>=<[k,L],L>=0. Also <[k,k],ann(k)>=0. These are cohomological
pairings of closed representatives; their pointwise brackets need not
vanish or be harmonic. k-stability of charged L follows from the gauge
tensor-factor action, not from a new count of E8 structure constants.

Decompose s=s1+s2+s3 by number of acyclic legs. Each sr is delta-closed,
since delta preserves N. Then

    F3 = -sum_(r=1..3) (h sr)/r
    delta F3 = -s.

F3 has ghost number0 and cubic field order. Here a Darboux complement
means a paired continuous LINEAR complement, not a general weak-symplectic
Darboux theorem: the Hodge splitting pairs exact1 with coexact1 and
nonharmonic0 with exact2, while the finite harmonic symplectic space admits
a paired complement. On smooth fields the Green operators and their
formal adjoints preserve smoothness; integration by parts expresses the
cubic variational derivatives as smooth forms. The perfect integrated
pairing therefore represents their Hamiltonian vector fields. Extend F3
using this chosen complement and apply its FORMAL Hamiltonian flow, not
an asserted nonlinear Sobolev flow theorem. In the convention delta={S2,-},

    (flow_F3)^* S|A = (S3+delta F3)|A + O(field^4)=O(field^4).

The flowed A is formally Lagrangian; its graph correction begins at
field order2, so its tangent and all preceding LINEAR cone/kernel/index
data are unchanged. Normal components of Q vanish through quadratic
order only. The finite tests verify the superalgebra identities and
controls, not this continuous implication by sample.

This argument works for the supplied k-stable paired harmonic L, including
the35 dimension witnesses. It does not prove that an arbitrary nonlinear
polarization works. A nonzero N=0 harmonic cubic cannot be removed by this
contraction; the instrument retains that opposite control.

## 3. The action cost cannot be hidden

A canonical flow preserves omega, not a selected Liouville primitive.
In Darboux coordinates lambda=p dq, graph(dF3) has lambda|graph=dF3.
Thus a local exact boundary functional must adjust the primitive if a
vanishing boundary one-form is required. For the actual symmetric CS
primitive the pulled-back difference is likewise exact locally, but its
generator depends on the canonical convention; it is NOT licensed to
silently subtract F3 with an unverified sign. The tests include a simple
graph primitive/counterterm control. A proposed physical action must derive
its actual boundary functional/sign and its supersymmetric/real completion.

Costs remain: reference connection, metric, harmonic polarization, Green
inverse, Darboux complement and response/counterterm. No added particles;
no parameter-free choice. Compact k-equivariance can be enforced by
averaging the contraction/generator over supplied SU5 since delta and
the trace are equivariant. No assertion of full nonlinear E8 reality,
global large-gauge invariance or physical Yang-Mills stationarity follows.

## 4. Explicit compact gauge control

In the trivial reducing SU5 gauge block take anti-Hermitian real matrices

    A=E12-E21, B=E23-E32, C=E31-E13.

They satisfy Tr(A[B,C])=2. Let f=(sin x,sin y,cos x cos y),
chi=sum x_i f_i T_i and c=sum c_i f_i T_i. Set a=d chi, b=0.
With normalized torus mean, each cyclic coefficient of
integral Tr(c [a,a]/2) is1/2. Thus

    s=(c1 x2 x3+c2 x1 x3+c3 x1 x2)/2,
    F3=-x1 x2 x3/2.

s is nonzero but delta-closed and delta F3=-s. Wrong sign doubles the
residual; disabling the pair differential fails. This actual CS control
is not a computed charged E8 cubic generator or physical Yukawa.

The nonlinear gauge-orbit law a=g^-1 d g, g=exp(chi), has expansion

    a=dchi+[dchi,chi]/2+[[dchi,chi],chi]/6+... .

Maurer--Cartan da+a wedge a=0. The native trigonometric and separate
Fourier implementations check its quadratic and cubic coefficients.
For real x_i the generator is anti-Hermitian and exp is unitary; this
compact gauge control has an actual all-order flat gauge-orbit meaning.
That all-order meaning applies to this gauge orbit, not the full charged
polarization. Flat-orbit symplectic isotropy follows by integrating
Tr(D_A epsilon wedge D_A eta) to zero on the closed torus when F_A=0.
It does not provide the required charged normal/SUSY boundary laws.

## 5. Next decisive duty

After eliminating s, compute the induced quartic obstruction on Ah and
its higher successors at the literal nonsplit background. A nonzero
harmonic obstruction cannot be wished away by contractible modes; extra
response fields/selection would require explicit cost. Then establish
an actual convergent boundary construction and the compatible full real
multiplet/source/normal equations before interpreting the chiral linear
indices as interacting physics. Nothing here selects three families,
parameters, a quantum theory, gravity or an observer/qualia mechanism.

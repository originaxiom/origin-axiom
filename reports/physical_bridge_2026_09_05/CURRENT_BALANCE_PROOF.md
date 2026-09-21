# R41 authored source-balance argument

Pre-execution, 2026-09-21 local time. This specializes existing F01/R39
identities to the actual R40 coefficient. It is not a new general
harmonic-metric theorem or a completed source action.

## 1. Three necessary balances, not one scalar Poisson equation

Let V be the actual nonsplit rank-four flat bundle, with its complete
invariant flag S_1 inside S_2 inside S_3 inside V. On a complete
finite-volume base without physical boundary, take a smooth positive
metric and write D=A+Psi. Suppose integral |Psi|^2 is finite. The
Hermitian trace-free projector xi_k=4 P_k-k Id is bounded, with
tr(xi_k^2)=4 k(4-k). In a metric-orthonormal frame adapted to the flag,
D is upper triangular. Write eta_k for its block from V/S_k to S_k.
Direct block multiplication gives

    <Psi,d_A xi_k> = -2 |eta_k|^2.

Let the full real moment equation be I=S, with I=-2 d_A^*Psi. For a
compact cutoff chi_R, integration by parts gives

    integral chi_R tr(xi_k S)
      = 4 integral chi_R |eta_k|^2
        -2 integral <Psi,(d chi_R)xi_k>.

The final term tends to zero: its absolute value is bounded by
2 sqrt(4k(4-k)) ||Psi||_2 (C/R) sqrt(Vol(M)). Also eta_k is square
integrable, because |eta_k|^2 <= 2 |Psi|^2. If tr(xi_k S) is integrable,
dominated convergence gives the three necessary equations

    integral tr(xi_k S) = 4 integral |eta_k|^2, k=1,2,3.

For the original coefficient all three right sides are strictly positive:
its b-generator is a single unipotent Jordan block of size four. Such a
block has no invariant complement to any nontrivial member of its flag.
If eta_k vanished identically, the orthogonal complement would be flat,
contradicting that already-verified Jordan structure. Smoothness then
makes its squared integral positive. No numerical lower bound is supplied.

On a truncated domain with boundary, the corresponding identity is

    integral tr(xi_k S) = 4 integral |eta_k|^2
                         +2 integral_boundary tr(xi_k Psi(n)).

Here n is outward. Thus a source-free inner boundary can carry the
negative compensating flux. Dropping this term would falsely exclude
F01's verified local cusp. Infinite energy, singular data, extra ends
and nonintegrable sources require their own argument; they are not
automatically covered by the boundaryless cutoff limit.

## 2. Apply the actual rank-five map, not a same-name center

R40 uses W=V+L, L=(det V)^-1 and j(X)=diag(X,det X^-1).
For the block metric H5=diag(H4,(det H4)^-1), the full moment map is
I5=diag(I4,-tr I4). Extend each xi_k by zero on L. The surviving block
generator T=diag(1,1,1,1,-4) has

    tr(xi_k T)=0, tr(T^2)=20.

Therefore S5=s T would give I4=s Id_4 and zero on the left of every
flag equation, contrary to the nonsplit positive right sides. This
excludes only the complete finite-energy block-compatible model with
that scalar-on-V source and the stated integrability. It is not a
theorem about arbitrary rank-five metrics or every U1 mentioned in the
programme. R39's different H-central U already illustrated the distinction.

The flag-source Gram matrix is

    tr(xi_j xi_k)=4 min(j,k)(4-max(j,k)).

In particular U=diag(3,-1,-1,-1,0) pairs positively with all three
projectors: (12,8,4); -U has the opposite signs. This is a sign/cone
control, not a solution of all the integral equations. A prescribed
positive profile multiplying U is still an external input unless its
fields, action and variations are provided.

## 3. Actual parent fields do not provide an independent source for free

Let E_ab be elementary matrices with indices 0 through 4. The neutral
structure directions K_j=E_0j, j=1,2,3, commute with T and satisfy
sum [K_j,K_j^dagger]=U. The charged direction N=E_04 satisfies
[T,N]=5N and [N,N^dagger]=diag(1,0,0,0,-1). It has nonzero pairings
with T and all three extended projectors. These are genuine adjoint
directions in R40's faithful structure SL5, not added matter multiplets.

But their commutators already occur in I=div(C+Cdag)+[C,Cdag]. Counting
one as an external S while leaving it in I counts it twice. All derivative,
off-diagonal, curvature and source variations must be retained. A neutral
direction commuting with T does not break this U1 by itself. A charged
background need not preserve the original four-plus-line splitting.
Giving a U1 a Higgs mass alone is still not anomaly cancellation.

For C5=[[C4,alpha],[0,c]], V remains a flat invariant subbundle whenever
C5 is flat. In an adapted orthonormal frame the whole-rank projector is
Xi=diag(1,1,1,1,-4)=T and

    <Psi,d_A Xi> = -(5/2)|alpha|^2.

The source-free finite-energy F01 identity first forces alpha=0 and
then forces the nonsplit V to split: impossible in that model. An upper
extension is not an escape. A lower block beta can remove invariance of
V (already E_40 maps V outside itself), so this particular argument no
longer carries the old V. It does NOT prove that such a new flat bundle
exists, is reductive, solves the full parent equations or retains I=1.

## 4. The old positive already answers the anti-linear flat-map test

Complex conjugation gives conjugate-linear isomorphisms of the cochain
complexes and their boundary restrictions. Thus n(conjugate E)=n(E).
If an invertible conjugate-linear flat map E->E* over the same marked
base existed, composing it with conjugation would identify these
restriction kernels, forcing n(E)=n(E*). This uses functoriality, not a
choice of inner product or a spectral approximation.

R40 computed n(V),n(V*)=(1,0), n(W),n(W*)=(1,0) and the exterior-square
W pair (2,1). Hence neither a linear nor a conjugate-linear same-base
flat isomorphism to the dual exists for those three actual coefficients.
No new numerical search is required. An antiunitary flat map is a special
case, so F08's specific pairing mechanism does not transfer to them.
This is not proof of physical spectral asymmetry: an actual background,
positive norm, complete domain and all fermion degrees remain required.

## 5. Next action, with both positive and negative evidence retained

Do not attempt to support this fixed nonsplit coefficient using only
the block-T scalar source. A candidate must supply nonzero traceless
flag projections through a variationally justified source/end sector,
or change the flat coefficient or energy/domain assumptions explicitly.
In the latter case recalculate the coefficient and full spectrum rather
than transporting R40's cohomology labels unchanged. Nothing here selects
new fields, source count, defects, measured parameters or a physical TOE.

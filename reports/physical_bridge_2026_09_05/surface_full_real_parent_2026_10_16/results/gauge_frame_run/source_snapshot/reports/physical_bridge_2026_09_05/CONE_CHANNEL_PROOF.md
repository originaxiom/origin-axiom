# Full coefficient split and leading logarithmic critical matrix

October 1, 2026. R71 authored algebra, frozen before execution.
This is NOT an asymptotic-domain classification, a particle count or a
selection of the supplied metric/action. All results concern R66's collar.

## 1. Exact decomposition, not an abelian-background substitution

Use N=E02+E23, P=N squared, Z=diag(1,-3,1,1),
H=diag(1,0,0,-1), k=log(q), beta=6/(q-q inverse).
The connection is C_r=h' H, C_x=t N, C_y=k Z+beta t squared P.
R68's positive trace adjoint gives the coefficient action ad(C).

The eigenspaces of ad(Z) on sl4 have charges 0,+4,-4 and dimensions
9,3,3. The zero-charge space is sl(span(e0,e2,e3)) plus C Z.
The charged spaces are the off-block columns/rows linking that chain
to e1. All six matrices C_i and C_i dagger commute with Z. Therefore
these are exactly orthogonal reducing spaces for the linear operator
at every r, for every Fourier mode, not only at the limiting connection.
The trace-free projection is retained; including the identity would
incorrectly replace nine neutral coefficients by ten.

These spaces are NOT three Lie ideals. Brackets add charges, and
[charge +4,charge -4] can have a Z projection. Inside the zero-charge
sector, sl3 and Z are ideals of that sector only; they are not ideals
of sl4. Neither charge zero nor commuting with Z makes sl3 trivial:
ad(N) acts there and has an adjoint coupling.

## 2. All limiting Fourier windows, with their boundary caveat

The limit has K=0,C_x=0,C_y=k Z. On a charge c coefficient and Fourier
tuple (m,n), the limiting scalar symbol is

  z_x=2 pi i m sqrt(alpha),
  z_y=(c k+2 pi i n)/sqrt(alpha),
  lambda=4 pi squared(alpha m squared+n squared/alpha)
         +c squared k squared/alpha.

The scalar cone calculation of R63 gives angular eigenvalues
plus/minus(sqrt(lambda+1/4)-1/2) and
plus/minus(sqrt(lambda+1/4)+1/2), each twice.
For 0<lambda<3/4 there are four eigenvalues in the open critical
interval (-1/2,1/2) per coefficient. For lambda=0 there are four zero
eigenvalues; for lambda>=3/4 there are none in that OPEN interval.
A threshold equality is NOT an endpoint admission theorem. Logarithmic
corrections can matter there. Even strictly critical limiting angular
eigenvalues are not yet actual operator graph traces or particles.

For any FIXED alpha>0,k!=0, every potentially critical Fourier tuple
obeys a bounded ellipse. This is a completeness bound, not a finite
sample: m squared<3/(16 pi squared alpha) and
n squared<3 alpha/(16 pi squared). Charged tuples additionally subtract
16 k squared/alpha from the available radius. There is no uniform
zero-Fourier-only theorem when alpha is unrestricted.

The declared exact controls use 3<pi<22/7, hence 9<pi squared<10.
For (alpha,k)=(1,1), only neutral (0,0) is critical in the limiting
sense. For (1,1/10), the charged (0,0) also enters. For (400,1/10),
both charges and charge zero have exactly m=0,n=-2..2 in the open
window. Every outside tuple is excluded by the ellipse and rational
bounds. The resulting 36,60,300 numbers count LIMITING ANGULAR
eigenvalue dimensions only. They are not physical multiplicities.
The scale/aspect input changes these numbers without changing genus
or a discrete cohomology table.

## 3. Zero-Fourier neutral logarithmic correction

On the neutral zero-Fourier coefficient, set epsilon=s^(-1/2),s=-log r.
R66's actual branch gives

  t=epsilon/sqrt(alpha)+O(epsilon cubed log(s)),
  v=h_s=epsilon squared/2+O(epsilon fourth log(s)).

Use R68's actual A=[[M+K,-L],[-L,-M-K dagger]], K=-v ad(H).
For link slots (0,x,y,xy), M=diag(-1,0,0,1).
Let Pcrit select x,y in both radial blocks; Qcrit=1-Pcrit.
On these 9 coefficients A0=diag(M,-M). Its critical kernel has
dimension 36. Its complement is invertible. Expand

  A=A0+epsilon F1+epsilon squared F2+O(epsilon cubed log(s)),
  F1=[[0,-L_N],[-L_N,0]],
  L_N=e_x tensor ad(N)+e_x dagger tensor ad(N dagger).

F2 includes diag(-ad(H)/2,+ad(H)/2) and the P-direction tangential
term proportional to beta/alpha^(3/2). That latter term changes link
degree and has zero critical-to-critical projection.

Eliminate the order-epsilon off-block term by a unitary formal change
exp(epsilon S1), with S1_QP=-A0_Q inverse F1_QP and
S1_PQ=F1_PQ A0_Q inverse. Its derivative with respect to s first appears
at order epsilon cubed. The order-epsilon-squared critical generator is

  B=Pcrit F2 Pcrit
       -Pcrit F1 Qcrit A0_Q inverse Qcrit F1 Pcrit.

This is a FORMAL LEADING BLOCK coefficient. The exact changing radial
operator is not replaced by A0 or by B. In the ordered critical slots
(a_x,a_y,b_x,b_y), B is block diagonal:

  B_ax=-ad(H)/2-ad(N)ad(N dagger),
  B_ay=-ad(H)/2+ad(N dagger)ad(N),
  B_bx=-B_ax, B_by=-B_ay.

It is Hermitian for the actual coefficient Gram pairing and
anticommutes with the radial Gamma. The leading coefficient does not
depend on q,beta or alpha; this does not make the whole operator
independent of those inputs.

The principal sl2 on sl3 splits as spins j=1 and j=2, checked here by
the Casimir ad(H) squared+ad(N)ad(N dagger)+ad(N dagger)ad(N):
eigenvalues 2 and 6 have multiplicities three and five. Z gives spin0.
For weight m=-j..j,

  B_ax=(m squared-2m-j(j+1))/2,
  B_ay=(j(j+1)-m squared-2m)/2.

Therefore B has zero multiplicity four, and paired nonzero eigenvalues

  +/-1/2 (each 2), +/-1 (each 4), +/-3/2 (each 4),
  +/-3 (each 4), +/-7/2 (each 2).

These are eigenvalues of the leading logarithmic generator, not a
verified collection of 36 actual Cauchy data. Only R68's four Z traces
have already been justified as exact reducing graph traces.

## 4. Controls against two invalid transfers

Discarding the off-critical Schur term leaves only plus/minus ad(H)/2
and fails the actual B. Discarding K changes B as well. Both are tested
as distinct negative controls. A frozen limiting 36-dimensional kernel
therefore does not permit copying the constant neutral trace law to
all 36 slots.

Conversely polynomial logarithmic growth alone does not violate L2:
in the normalized radial variable, s^b has integral
integral exp(-s) s^(2b) ds, finite for every finite real b.
This is not graph admission. If a truncated approximation has a
nonzero residual of order r inverse s^d, its Q norm contains
integral exp(s) s^(2d) ds, which diverges for every finite d.
An integrable error in the s-coordinate angular expansion is not an
L2(dr) graph error after division by r. No finite asymptotic truncation,
even after first-order elimination, is certified as a mode here.

Next prove the exact maximal/minimal domains for the changing operator,
including threshold channels, actual generalized logarithmic traces,
nonlinear products, compact gauge and superfield maps. Then match
the global core. This report neither kills the nonsemisimple route nor
supplies its physical chirality, selected end law or full parent.


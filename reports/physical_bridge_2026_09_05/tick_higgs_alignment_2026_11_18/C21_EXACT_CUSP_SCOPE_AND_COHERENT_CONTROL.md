# C21's cusp limit, and an explicit coherent ground-space control

2026-11-18. P-C8 source-reading continuation received at SM head
a69cee901. Author hand derivation; not independently checked. No
scientific code, imports, CAS, quadrature, SVD or numerical tests ran.
The C21 card, report, source and both outputs were read in full.
Their exact pins are in SOURCE_REFRESH_C21.json. The older exact
factorization and closed overlap are reused, not re-discovered.

This is a statement about the literal magnetic contraction of C21.
It neither identifies its singular values with physical masses nor
adds a state-selection principle. The coherent example is deliberately
chosen as an adverse control, not derived as the programme's vacuum.

## 1. The finite run is not an asymptotic certificate

C21 evaluates the two pure ground eigenvectors v_+,v_- at selected
finite heights. Its class/rank loop uses the up and down matrices at
all 24 points and four lifts. Its exponent loop evaluates all three
sectors at one mark, using heights 6,8,10. Y_mp evaluates theta sums
at extended precision and then converts their entries to Python
complex and NumPy complex arrays before SVD. Thus that SVD is not
an extended-precision or interval singular-value calculation.

None of this is a claim that its printed finite figures are wrong.
They are received outputs, not independently recomputed here. A
shrinking two-interval slope alone is not a proof of its limit. The
literal theta series does give a proof for the two vectors, below.
The same source has not derived that those are the only ground states.

## 2. Read the dominant theta term without a floating-point cutoff

Write the relative Wilson argument as xi=alpha tau+beta, alpha,beta
real and fixed while tau=X+i y goes up the cusp. Absorb the source's
common Gaussian into its theta functions:

    Theta_c=exp(6pi i xi Im(xi)/y)
                    theta[c/6,0](6xi,6tau).

Apart from the common phase exp(-6pi i alpha beta), its terms are

    exp[6pi i tau r²+12pi i beta r],
    r=n+c/6+alpha, n in Z.                            (1)

Across c=0,...,5 these r are the shifted grid alpha+(1/6)Z.
Its unique point nearest zero determines a unique dominant c=c_*.
The next squared distance has a strictly positive gap. For C21's
order-five points and integer Delta=5,-1,-9,

    alpha=Delta a/2, a in (1/5)Z,

there is no tie: 6alpha lies in (1/5)Z, never a half-integer modulo
one. Adding any of the stated lifts preserves this property. Each
sector therefore has a unique dominant Theta_c. Its leading complex
coefficient is nonzero. The remainder relative to it is exponentially
small, with a positive gap fixed by this finite set of rational grids.

The contracted mass matrix for a general fixed coefficient vector h
is M_h=sum_k h_k Y_k, with the exact convention used by C21. For fixed
c the selection rule gives

    i-j=c mod 3, k=2j+c+1 mod 6.

Hence its leading matrix is monomial, with its three entries

    exp(2pi i k/6) h_k Theta_(c_*),
    k=c_*+1,c_*+3,c_*+5 mod 6,                         (2)

up to the common positive prefactor. Its leading rank is the number
of nonzero h entries among those three indices. If all are nonzero,
all singular values have the same leading exponential scale, and
both logarithmic ratio exponents tend to zero.

## 3. Exact support of the two tested eigenvectors

The CRT proof gives v_+=u_- tensor b_+ and v_-=u_+ tensor b_-.
Put r0=1/sqrt(3). Directly from the two Bloch axes in that proof,
their component squared magnitudes, in the original k basis, are

| k | Squared component magnitude of v_+ | Squared component magnitude of v_- |
|---|---|---|
| 0 | (1-r0)²/4 | (1+r0)²/4 |
| 1,5 | (1+r0)²/8 | (1-r0)²/8 |
| 2,4 | 1/12 | 1/12 |
| 3 | 1/6 | 1/6 |

Every entry is nonzero. Equation (2) therefore proves zero limiting
ratio exponents for either pure vector, at every order-five point,
every stated lift and each sector in this contraction. This is
stronger than the finite-height slope observation, while retaining
its precise two-vector premise. It proves no limiting mixing matrix
or full physical spectrum. Some leading singular values are equal,
so their limiting singular bases also require care.

## 4. A coherent direction in the same quadratic ground space

The two-mode ground space is not the set of those two vectors.
An explicit unit vector in it is

    h_*=(1/sqrt(2), exp(i pi/12)/2, 0, 0, 0,
                                              exp(i pi/12)/2).        (3)

Here is a hand membership proof, not a numerical residual. On the
even P_3 plane use e0 and e1=(0,1,1)/sqrt(2). In the CRT basis let
n dot sigma be A_2's axis and let A_3=i m dot sigma on that plane.
Their entries needed here are

    n_z=1/sqrt(3), n_01=(-1-i)/sqrt(3),
    m_z=-1/sqrt(3), m_10=(1+i sqrt(3))/sqrt(6).

The Hermitian part of U is

    (U+U†)/2=-(sqrt(3)/2)(n dot sigma) tensor(m dot sigma).

The ground space is its +sqrt(3)/2 eigenspace. For a vector with
CRT blocks f=(A,0) and g=(0,t A), the negative-eigenvalue condition
on the tensor product is satisfied by

    t=-m_10/n_01=exp(i pi/12).

Taking A=1/sqrt(2) gives (3). The other block equation follows from
(m dot sigma)²=I and |n_01|²=1-n_z². It also follows directly that
|<v_+,h_*>|=|<v_-,h_*>|=1/sqrt(2). Thus this is an equal-magnitude
coherent combination of the two ground eigenvectors, not one of them.
The twisted-circle control in the first proof supplies an admissible
linear ground section with these initial coefficients.

The fixed support in (3) is a property of this chosen coherent
direction. It is not claimed invariant under every half-period lift,
nor is that direction a globally stationary Higgs state. Changing
frames requires transporting h, the kinetic operator and Y together.

## 5. The control has an exact cusp hierarchy in the inherited frame

At C21's declared mark a=2/5,b=4/5, and its unshifted lift, the up
sector has alpha=1,beta=2 and c_*=0. Down has alpha=-1/5,beta=-2/5
and c_*=1. In (3), the odd triple has rank two and the even triple
has rank one. Their ratios therefore do not all tend to nonzero
constants. This already refutes an extension of the pure-vector
negative to the entire quadratic ground space.

The actual exponents can be obtained by hand too. Put
A=1/sqrt(2), B=exp(i pi/12)/2 and p=exp(i pi/3). Omitting the common
positive prefactor, the exact contracted matrix is

    M_h* = [[p B Theta_0, p^-1 B Theta_2, A Theta_1],
            [p^-1 B Theta_4, A Theta_3, p B Theta_2],
            [A Theta_5, p B Theta_4, p^-1 B Theta_0]]. (4)

Its determinant is

    A B²(Theta_0² Theta_3+Theta_2² Theta_5
                               +Theta_1 Theta_4²)
       -A³ Theta_1 Theta_3 Theta_5
       +2 B³ Theta_0 Theta_2 Theta_4.                 (5)

For up, xi=tau+2 is an integer-lattice translate of zero; the
normalized theta frame changes by a common phase. Theta_0 has
exponent zero, Theta_1,5 exponent 1/6, Theta_2,4 exponent 2/3,
and Theta_3 exponent 3/2 in units pi y. Equation (4) has leading
rank two. The last term of (5), with exponent 4/3, is its unique
leading determinant term and has nonzero coefficient. Therefore

    E_up(s2/s1)=0, E_up(s3/s1)=4/3.                   (6)

For down the six nearest r in (1) are

    (-1/5,-1/30,2/15,3/10,7/15,-11/30).

Its theta exponents in the same units are

    (36,1,16,81,196,121)/150.                        (7)

The leading entry is A Theta_1 in row 0, column 2. Its Schur
complement in rows (1,2), columns (0,1) has leading entry
`-(B²/A) Theta_2²/Theta_1`, of exponent 31/150. Eliminating that
pivot uses matrices approaching the identity, so it preserves the
singular-value exponents. In (5) the first two terms have the same
leading exponent 153/150 and the same complex leading phase, since
their sums of r are both -1/10 and their sums of r² agree. They add,
rather than cancel. The other determinant terms decay faster.
Consequently the three singular-value exponents are

    (1,31,121)/150,

and the two ratio exponents are

    E_down(s2/s1)=1/5, E_down(s3/s1)=4/5.             (8)

These are internal asymptotic statements of the chosen contraction,
not parameter predictions or fits. No GeV datum or measured coupling
was used. Nothing here computes its physical normalization, anomaly
content or fermion masses from one stationary action.

The existing lepton/down issue is retained, not repaired by (3).
For every order-five w, 5w is a lattice vector and

    xi_lep=-9w/2=-xi_down-5w, xi_down=-w/2.

A whole-lattice shift of xi multiplies all six Gaussian-completed
Theta_c by the same unit phase. Also Y(-xi)=Y(xi)^T: swapping i,j
replaces c by -c and leaves k and its phase unchanged. Consequently

    M_lep(h)=phase M_down(h)^T                         (9)

for every common h in this contraction, not just (3). Their singular
values and cusp exponents therefore agree. This retains the known
level-five degeneracy in its actual magnetic carrier. It does not
assert an equivalence of different physical representations.

## 6. What the control costs, and the next selection duty

The source selected the two pure monodromy eigenlines. This control
instead imposes zeros on specified components of an already allowed
coherent ground vector. That imposes a state condition. Its exact
solution (3) does not make the condition foundationally forced.
The action must select it, or an appropriate equivalent orbit, before
these exponents can replace a supplied reading.

The tick-invariant quartic A4 N²+B4 Delta² cannot select (3) by its
relative phase. For B4>0 it leaves the entire equal-magnitude circle,
which includes (3). On that circle Sigma rotates arg(w) by pi/6.
Thus an analytic invariant phase potential on the circle has first
possible nonconstant harmonic w^12 plus its conjugate, of polynomial
degree 24 in z_+,z_-. In the full space Delta w^6 plus its conjugate
is allowed already at degree 14; it vanishes in value on the circle
but can affect its relaxation. These are allowed invariants, not
new terms assigned to the action. Their coefficients and phase are
not derived here. Nonanalytic effective potentials need separate
analysis.

The genuine gain is an exact distinction: the pure-vector zero-slope
result stands, and a ground-space-wide exclusion does not follow.
C21 itself keeps an untested concentrated-mode variant open. This
note supplies an exact coherent ground-space control; it does not
attribute an explicit all-vector exclusion to that report.
There is a concrete coherent candidate with rational nonzero cusp
exponents to test against a **derived** selection functional. Neither
it nor the earlier pair is earned as a physical vacuum. Foundational
inputs counted removed remain zero; no SM3 or gravity closure follows.

# An actual root-field map and its gauge-relaxed Higgs response

2026-11-18. P-C8 analytical source/action continuation. Author hand
derivation, not independently checked. No scientific execution, imports,
CAS, quadrature, SVD or tests. This is a recovery control of the literal
magnetic overlap inside the existing supplied action. It is not a new
claimed SM model or an identification with the complete-cusp background.
Flux, flat metric, root embedding, spin and Wilson data remain premises.

## 1. Reuse the actual cubic rather than invent a scalar potential

The existing parent is weave_curved_action_2026_10_08/PROOF.md. Its
compact trace metric, positive kinetic terms and cubic are retained.
That source already exhibits a nonzero sl3 matrix-unit vertex at
lines 177–185. The local algebra is prior work. The new question here
is whether its global magnetic mode bundles can give the (3,3,6)
overlap, and what scalar response that same action supplies.

Take a regular A2 root subsystem of compact E8. In its complexification
use E_ij, compact adjoint E_ij†=E_ji, and

    C=diag(1,0,-1),
    [C,E12]=E12, [C,E23]=E23, [C,E31]=-2E31.

This is an interaction block, not an identification with SM colour or
the native family triplet. The inherited trace on this block is
kappa=iota tr_3, iota>0. Once the E8 trace is fixed, iota is fixed;
it is not a new relative coupling.

On a flat torus of physical area A_T choose a degree-three line L
and the rank-three bundle L+O+L^-1. Its Cartan connection has

    F0=B C dvol, B=6pi/A_T>0.

Its root degrees are +3,+3,-6 for E12,E23,E31. The bundle induces
an E8 bundle through the selected subgroup. The degree three and
subgroup are chosen for this control, not forced by genesis.
Flat Cartan factors can tensor the three fundamental lines, with
trivial total determinant. Denote the resulting degree-three root
lines by L_L,L_R; their negative closing root is (L_L tensor L_R)^-1.
The flat factors are retained, not equated just because degrees agree.

The field assignments are now typed:

| Parent field | Coefficient line | Magnetic profiles |
|---|---|---|
| q in S tensor ad E | S tensor L_L on E12 | Three positive-flux modes psi_(3,i) |
| r in S tensor ad E | S tensor L_R on E23 | Three positive-flux modes psi_(3,j) |
| Connection deformation a^(0,1) | (0,1)-forms in (L_L tensor L_R)^-1 on E31 | Six harmonic forms, with coefficient conjugate(psi_(6,k)) in a unit frame |

The matter characteristics are (1/2,1/2), and the connection
characteristic (0,0), as in the source. Their product is compatible
with S²=K; K is trivial on the compact torus. Positive degree gives
three holomorphic sections on each matter line. Serre duality or the
conjugate zero-mode equation gives six harmonic forms on that degree-minus-six line.
These are internal multiplicities, not three SM families. Holomorphic
matter profiles alone do not certify massless bosons at nonzero moment.
The literal characteristic convention is not identified with the
genesis spin refinement without its own joint gauge/spin frame map.

The flat root connections must satisfy the same product law:

    3 zeta_L+3 zeta_R=6 zeta_H.

For one triple the Wilson weights can be realized by the traceless
Cartan D=diag(2q_L+q_R,-q_L+q_R,-q_L-2q_R). Its adjacent root weights
are 3q_L and 3q_R; the closing root has their negative sum. Three
separately chosen such D's are not thereby one common SM background.
That larger embedding remains a compatibility duty.

The source's actual cubic gives

    W_cubic=i (iota/g6²) sum_(ijk) u_i v_j h_k
         integral f_(3,i) f_(3,j) conjugate(f_(6,k)) dvol, (1)

up to the common superpotential phase already in the parent. For
example [E31,E23]=-E21 and tr(E12 E21)=1. The two antisymmetric
terms of W give the same vertex, not independent couplings.
Physical unit profiles are f_N=A_T^-1/2 psi_N for the source's
unit-cell normalized psi. The integral in (1) is A_T^-1/2 Y_ijk.

In this matrix-unit convention the kinetic factors are iota/g6² for
u,v and iota/(2g6²) for h. Canonical rescaling gives the common cubic
factor sqrt(2)g6/sqrt(iota A_T), multiplying the same Y_ijk. Tensor
shape and relative normalization are inherited from the action; the
overall coupling and area remain supplied.

This earns a conditional local field/vertex realization, not an
isomorphism to the complete-cusp background or its spectrum. Other
E8 fields, conjugates and flux-sensitive modes have not been deleted.

## 2. Check stationarity and the actual quadratic energy

Set q=r=0 at this Cartan background. The scalar potential is the
parent's pure gauge energy

    V=(1/(2g6²)) integral kappa(F_XY,F_XY) dvol.       (2)

Its first variation vanishes because D0 F0=0 on the closed torus;
the spin-field first variations vanish at zero. It is stationary
with a nonzero moment. It is not a residual-zero vacuum, so the
positive linearized-residual argument on the cusp cannot be borrowed.

Take any unit profile f in the six-dimensional negative-flux form
space, integral |f|² dvol=1. In an orthonormal coordinate frame set

    a=a_X+i a_Y=f E31,
    a_X=(f E31+bar f E13)/2,
    a_Y=(f E31-bar f E13)/(2i).

The harmonic equation (D_X-i D_Y)a=0 makes both the linear curvature
variation and the real gauge divergence vanish. This is a transverse
physical tangent, not a pure gauge direction. All these profiles
are smooth with finite norm on the compact torus. For real t,

    F(A0+t a)=[B-(t²/2)|f|²]C,                       (3)

since -i[a_X,a_Y]=[a,a†]/2=-|f|² C/2. With
I4(f)=integral |f|^4 dvol the exact frozen-path potential is

    V_frozen(t)=(iota/g6²)
                      [A_T B²-B t²+(I4(f)/4)t^4].    (4)

The tangent norm is iota/(2g6²). Writing its canonical coefficient
as H=sqrt(iota/(2g6²)) t gives

    V_frozen=V0-2B |H|²+(g6²/iota) I4(f)|H|^4.        (5)

The mass m_H²=-2B=-12pi/A_T is derived. No negative mass, quartic
sign or empirical scale was inserted. This establishes a saddle and
a condensation duty, not a stable vacuum. Flat Wilson shifts change
profiles but do not remove this exhibited sign.

## 3. Solve the Cartan response before reading a selector

Selecting a direction by I4 would freeze a gauge field that the
same action allows to respond. There is an explicit global response.
Since the density has unit integral, a unique real coexact one-form
beta_f satisfies

    d beta_f=(1/2)(|f|²-1/A_T)dvol,
    d† beta_f=0, beta_f perpendicular to harmonic one-forms. (6)

Existence is the scalar Poisson equation with zero-mean source. No
boundary coefficient or contact coupling is chosen. Harmonic Cartan
Wilson modes remain separate light coordinates, not inverted in (6).

Put b_f=beta_f C and consider the admitted path

    A(t)=A0+t a+t² b_f, q=r=0.                      (7)

Its order-t² curvature is the constant -C/(2A_T). Its codifferential
vanishes, solving the static Cartan normal equation at that order.
This is not all the charged normal equations. The values of b_f
commute, so there is no order-t^4 curvature. Direct substitution gives

    F(A(t))=[B-t²/(2A_T)]C+t³ R_f,
    R_f=(beta_X-i beta_Y)f E31
                            +(beta_X+i beta_Y)bar f E13. (8)

R_f is Hermitian and orthogonal to C. The exact energy on this path is

    V(A(t))=(iota A_T/g6²)[B-t²/(2A_T)]²
                +(t^6/(2g6²)) integral kappa(R_f,R_f)dvol. (9)

The quartic through this admitted response is independent of the unit
six-mode direction. In canonical variables,

    V=V0-2B |H|²+[g6²/(iota A_T)]|H|^4+O(|H|^6).    (10)

The normalized Cartan gauge mode has coupling e_C=g6/sqrt(2iota A_T)
and this root has charge -2. Thus that quartic is (1/2)(2e_C)²,
fixed by the same positive gauge metric. This is conditional
normalization within the supplied parent, not a foundational coupling.

The frozen directional term I4(f)-1/A_T is removed by a real normal
response. Cauchy–Schwarz makes it nonnegative, but that does not
make it a physical state-selection energy. This explicit response
is an adverse control for selecting h_* or another direction by
the frozen overlap density alone.

## 4. The sextic remainder is a target, not the full effective potential

The last coefficient in (9) is fixed and positive:

    integral kappa(R_f,R_f)=2iota integral |beta_f|² |f|². (11)

It is strictly positive for a nonzero degree-six profile. If it
vanished, beta_f would vanish wherever f is nonzero, hence everywhere
by continuity and isolated zeros. Equation (6) would make |f|²
constant, impossible for a positive-degree section, which has zeros.
No pointwise positive lower bound on |f| has been assumed.

Equation (11) is a derived direction-dependent functional on this
specified path. It is not the complete relaxed sextic. Higher-order
connection response, other unstable modes, harmonic Wilson coordinates
and the full physical fields remain. Minimizing (9) does not prove
a stationary nonzero solution of all their equations.

Nor is this automatically the tick-invariant potential classified
earlier. The modulus is fixed here; the geometric tick moves it and
the whole bundle. It is not a pointwise symmetry of one arbitrary
fixed torus. A functional on the closed history needs its base
dynamics, transport and measure. No geodesic average or phase term
is silently added.

The tree curvature mass and the source's prescribed K-c B_bubble are
distinct; B_bubble is its overlap operator, not the flux density B here.
Giving the latter a physical role requires deriving propagation along
the moduli-space loop and its consistent combination with the former.
Keeping only the piece with an attractive state would change the action.

## 5. Retain the full field and global controls

Even this A2 block has further negative connection directions: the
degree-minus-three form lines on E21 and E32 each have three modes
of mass squared -B by the same calculation. E31 has six of mass
squared -2B. Thus at least twelve complex unstable connection
directions occur, before the other E8 roots are considered. Naming
the most negative six-mode band does not justify deleting the rest.
Higher Landau modes, gauge zero modes and independent fermions stay.

The displayed principal SU3 bundle is smoothly trivial. Its degree-three
clutching loop lies in the embedded SU2 on coordinates 1 and 3 and
contracts there since SU2 is a three-sphere. A flat connection exists
in the same smooth bundle, with zero energy at q=r=0. It need not
preserve the selected holomorphic splitting into flux lines. Holding
that splitting inviolable would be an extra physical restriction.

This is a recovery control, not a claim that (7) reaches that flat
connection or that every source, end or larger architecture loses
magnetic structure. Additional geometric factors, actual sources or
a different stationary construction may change the result. They
must come from the declared architecture with inputs counted.

The record already contains stationary magnetic saddles and negative
modes on the cusp, in weave_magnetic_stationarity_2026_10_08. This
credits that prior mechanism. The compact flux-(3,3,6) field map
and its explicit Cartan response are a source/action control, not
a new discovery of magnetic instability in physics.

## 6. Primary reading and the remaining physical duty

Personally read for this calculation: Cremades–Ibanez–Marchesano,
hep-th/0404229, section 3.3, equations (3.62)–(3.70); section 5.1,
equations (5.5)–(5.6); and the targeted Hermitian Yang–Mills passage
in Appendix B.1. It distinguishes the scalar Laplacian from the
curvature-shifted mass operator, and the Yukawa scalar is tachyonic
in the one-torus setting. This supports the distinction tested
directly above, not independent verification of this field map.
[Primary paper](https://arxiv.org/pdf/hep-th/0404229).

Also personally read the background EOM in section 3, the quadratic
and gauge-fixing discussion in section 5, targeted Landau-spectrum
sections 6.4–6.5 and stabilization discussion in section 7 of
Kojima–Okubo–Takeda, arXiv:2306.00644v2. Those passages distinguish
physical tachyons from gauge modes and one-torus Wilson changes from
additional-dimension stabilization. Full-paper reading is not claimed.
[Primary paper](https://arxiv.org/html/2306.00644v2).

The progress is a typed realization of the magnetic cubic, its
normalized curvature mass and a solved Cartan response showing why
a frozen quartic is insufficient. No independent scalar-potential
coefficient is needed inside this chosen parent. Foundational inputs
removed remain zero.

Next is the full stationary response with all unstable/zero sectors
retained, or a derived larger geometry/end law stabilizing the block.
Its full spectrum must then earn chirality and three SM families.
No gravitational dynamics follow from this fixed-metric calculation.
The full vacuum-selection, SM3 and gravity objective stays open.

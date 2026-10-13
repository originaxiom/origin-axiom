# The full spin Dirac expression on the supplied cusp metric

This is an authored differential-geometric calculation on the physical branch's existing total metric. It supplies the operator expression needed for the next domain comparison, not its global closed realization or identification with a physical parent.

## The orthonormal frame retains the changing fibre

Write l=ell and take the positively oriented coframe

    e1=l dx/y, e2=l dy/y,
    e3=sqrt(A/y)(du+x dv), e4=sqrt(A y) dv.

Its dual frame is

    E1=(y/l) partial_x, E2=(y/l) partial_y,
    E3=sqrt(y/A) partial_u,
    E4=(A y)^(-1/2)(partial_v-x partial_u).

The nonzero brackets, with their antisymmetric partners understood, are

    [E1,E2]=-E1/l, [E2,E3]=E3/(2l),
    [E1,E4]=-E3/l, [E2,E4]=-E4/(2l).

The shear bracket is essential. The coframe is invariant under the actual cusp deck map (x,y,u,v)->(x+1,y,u-v,v). A chosen spin lift and the actual rank-six coefficient transitions still act on spinor sections. This does not replace the punctured-fibre coefficient by commuting torus characters: its a,b transports have nontrivial commutator and the removed section remains present.

## The complete zeroth order term

For C_ijk=<[Ei,Ej],Ek>, Koszul gives Gamma_ijk=(C_ijk-C_jki+C_kij)/2. The spin lift is Omega_i=(1/4) sum_jk Gamma_ijk c_j c_k. Clifford contraction gives

    K=sum_i c_i Omega_i=-c2/(2l)+c1 c3 c4/(4l),
    D=sum_i c_i Ei + K.

These formulas follow by substitution of every bracket, without discarding mixed components. An independent reconstruction first computes the coordinate Levi-Civita Christoffels from the full metric, then transforms them into the frame; it checks all connection entries, not just their contraction. The quarter coefficient is fixed by Clifford compatibility, not by a desired eigenvalue.

The real density is l^2 A/y^2. Its frame divergences are (0,-1/l,0,0). Thus the c2 term gives formal symmetry after integration by parts. The triple Clifford term is Hermitian and remains in the formally selfadjoint expression. Dropping it does not necessarily violate formal symmetry; the stronger discriminator is the full Levi-Civita/Lichnerowicz identity. The chirality operator is -c1 c2 c3 c4 and anticommutes with D, while the spin connection commutes with it. These are internal spin gradings, not a four-dimensional spacetime representation assignment.

## The curvature and line connection give independent checks

Coordinate curvature gives scalar curvature R=-3/l^2. With the positive connection Laplacian,

    D^2=nabla* nabla+R/4.

The verifier compares all second, first and zeroth derivative coefficients, so agreement is not a check on one trial function. Curvature is computed independently from the Christoffels. A wrong mixed term fails this identity.

In a flat unitary local frame of the existing coefficient, D acts as the displayed expression tensored with its identity. Global transition matrices remain required; flatness does not mean trivial global monodromy. In an arbitrary gauge replace Ei by the coefficient covariant derivatives. Tensoring additionally with the existing supplied cusp line of connection -6i n dx/y gives

    D_n=D-6i n c1/l,
    D_n^2=nabla_n* nabla_n+R/4-6i n c1 c2/l^2.

The last term is Clifford curvature: F12=-6i n/l^2. This identity is tested for symbolic real n. It derives no preferred n, no full gauge embedding and no source balance. Curvature compensation and the same-field action are not consequences of a twisted Dirac expression.

## The radial unitary transformation does not remove the mixed term

Set t=log y. The density becomes l^2 A exp(-t) dx dt du dv. The unitary map to Lebesgue density is psi -> l sqrt(A) exp(-t/2) psi. Conjugation yields

    D_tilde = c2 partial_t/l + c1 exp(t) partial_x/l
            + c3 exp(t/2) partial_u/sqrt(A)
            + c4 exp(-t/2)(partial_v-x partial_u)/sqrt(A)
            + c1 c3 c4/(4l).

For D_n append -6i n c1/l. Thus the density term disappears exactly, but the shear-induced spin term does not. This expression retains growing and shrinking fibre derivatives. It is not a constant product-cylinder operator, and replacing it by the flat-link Fourier estimate from nodal_transport would change the analytic problem.

## What this establishes for the next join

The Levi-Civita spin term is fixed once this metric and ordinary spin operator are supplied; it is not another adjustable end parameter. The corrected expression is the one to use when testing whether the transported vertical kernel forms a closed effective subsystem, and when computing its coupling to the complement. A fibre index by itself does not carry those estimates.

This proof does not show the subsystem fails or succeeds. Nor does negative scalar curvature imply zero modes or instability: the full squared operator and its domain must be kept. The marked section is at finite metric distance, the modular cusp degenerates, and neither closed trace domain nor total resolvent is specified here. Primitive nodal holonomy contraction and smooth-fibre graph transport remain valid within their previously stated scopes. The canonical versus logarithmic spin extensions remain distinct. The two lift signs may change global spin transition conditions without changing this local expression.

Next use this expression with the actual six-dimensional coefficient and the previously constructed critical puncture subbundle. Establish its simultaneous section/cusp graph domain and controlled projection onto vertical harmonic profiles before applying an effective base index. Separately, identify it as the Weyl Hessian of one actual parent on the same total space. The compact silver parent and its preserved charged cubic are not that identification by dimension alone. No physical generation number, sector selection, parameter or gravitational equation is derived here.

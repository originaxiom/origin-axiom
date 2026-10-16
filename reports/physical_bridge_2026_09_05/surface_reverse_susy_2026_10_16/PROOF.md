# Reverse supersymmetry and the amplitude phase boundary pair

Authored conditional proof, submitted with explicit computational gates.
All fields and gauge transformations here belong to the supplied local
parent. A boundary law still needs an ensemble and an action principle.

## 1 Actual component transformations and parameter normalization

Write C for the actual Nambu conjugation matrix, and let M_j have the
two by two alternating matrix [[0,-1],[1,0]] in the left lambda parameter
rows and left psi_j columns. The actual chiral expansion gives
delta c_j=sqrt2 epsilon^T M_j Psi. Matrix dagger reverses both odd
factors and supplies the antihermitian matrix basis sign; consequently
delta barc_j=sqrt2 epsilon^T C M_j C Psi. Thus the compact real bosons
have coefficient matrices (C M_j C-M_j)/2 and (C M_j C+M_j)/(2i).
Their reality condition is -C^T B_j* C=B_j, NOT commuting conjugation.

For the vector use the actual WZ superfield, differentiate its cubic
terms and extract theta_alpha bartheta_beta. The leading mixed term is
-theta sigma_mu bartheta v_mu; actual barred matrix fermion coefficients
are minus Nambu barred coefficients. Both signs are required. The WZ
restoring chiral parameter has zero bottom component and no mixed term
at zero external momentum, so does not change these lowest boson maps.
The full auxiliary/gauge compensated boundary closure is a further duty.

Let B_0 be the resulting map for X_time. Define T by
T^T=B_0 C/i on the real lambda parameter subspace. The gate is equality
B_A=T^T i C w_A for ALL ten bosons, with w_time=I and w_spatial=-v_spatial.
This lowering is not optional: in the actual mostly plus Lorentzian
frame G0²=-I, v_spatial=-G0 G_spatial and the covariant current is
G0 G_lower_time=I, G0 G_lower_spatial=-v_spatial. The full32 matrices
must verify this independently of the component map. The original
all velocity guess is preserved and explicitly rejected on all nine
spatial fields. If passed, epsilon_can=T epsilon_source is earned, not an
assumed adjoint of the forward map. The expected actual value is
T=(i/2) R P_lambda. T preserves Majorana reality and has norm one half.

## 2 Local linearized Euler Ward identity

Let slashD=sum v_a D_a and let F obey the three normal BPS equations
F23=-F45, F24=F35, F25=-F34. Its curvature Clifford expression Fslash
is a linear combination of
v2v3-v4v5, v2v4+v3v5, v2v5-v3v4.
All three annihilate P_lambda on both sides. Clifford multiplication
then gives, coefficientwise for every independent curvature,

    P_lambda v_N Fslash=2 sum_b P_lambda v_b F_Nb.

For a parallel real scalar parameter e and a Dirac solution Psi, put
a_N=e^dagger v_N Psi. Its covariant divergence is e^dagger slashD Psi.
Since slashD²=D²+Fslash, the previous identity yields

    D²a_N-D_N(D.a)-2 sum_M [F_MN,a_M]=0.

This is the local linearized bosonic Euler equation. External components
and the scalar time component follow from P_lambda Fslash=0 as well.
It is not a converse BPS theorem or a complete boundary domain result.

## 3 The actual root background and complete real parameter image

Use [E+,E-]=-H, [H,E+]=2E+, compact tau(E+)=E-, tau(H)=-H,
and B(H,H)=2. The verified full E8 map has orthonormal triplet columns
W=(E+,-H/sqrt2,E-), not a replacement coefficient algebra.
With s=1-g²r the known exact family is

    A_theta=i g² r H/(2s),
    Q=X4+iX5=g exp(-i theta/2) E+/(sqrt(r)s).

Let a=partial_g(A2,A3,X4,X5). It is gauge fixed and a full BPS tangent.
Its Dirac partner is Psi_s=-sum_a v_a e_s a_a for each real lambda
frame vector e_s. Actual source transformations with source parameter
T^-1 e_r return +i times a Grassmann parameter product times

    a_rs=delta_rs a+J_rs I a,
    J_rs=e_r^dagger iR e_s,
    I(a2,a3,a4,a5)=(a3,-a2,a5,-a4).

J is a real orthogonal complex structure: J^T=-J and J²=-I4.
The real span of these profiles is exactly two, not four generations,
and every other boson component vanishes on this family. The stripped
even factor +i epsilon_odd xi_odd is Hermitian. All four real supercharge
parameters and all full Majorana conjugate components are retained.

## 4 The phase partner and the proper gauge group

The entire partner, not only its Higgs component, equals D epsilon_g,

    epsilon_g=i (1+g²r) H/(2g(1-g²r)).

Indeed partial_r epsilon_g=i g H/s²; its scalar action is
[Q,epsilon_g]=-i partial_g Q, with zero angular connection variation.
It also satisfies sum_(a=2..5) D_a² epsilon_g=0. The scalar commutator
terms in that equation cannot be dropped. The phase image is thus
gauge fixed as well as gauge generated and obeys the linearized Euler
equation. Both images are linearized BPS in this particular family.

epsilon_g tends to iH/(2g) at the inner end and is nonzero at every
outer R<g^-2. It is NOT an infinitesimal proper gauge redundancy if
the allowed gauge parameters vanish at both ends. A larger gauge
quotient, associated boundary charges or edge variables are different
ensembles; this calculation does not select one of them.

## 5 Finite coefficient norm and both end fluxes

In the positive compact pairing the two profiles are orthogonal and
have the same norm density

    |a|²=|I a|²=(1+4g²r+g^4 r²)/(r(1-g²r)^4).

Define f(r)=r(1+g²r)/(1-g²r)^3. Direct differentiation gives
r|a|²=f'(r). The physical annulus coefficient norm is therefore
2pi(f(R)-f(epsilon)). The gauge Green flux is the SAME f(r):
r B(epsilon_g,D_r epsilon_g)=f(r). Its inner limit is zero even though
epsilon_g itself has a nonzero inner limit. A nonzero norm of this
covariantly harmonic gauge direction is supported by the outer boundary,
not an inconsistent integration by parts. Keep both ends before the
limit; reversing one sign is not the same action.

For fixed R<g^-2 the inner limit is finite and positive. Nothing here
removes the outer pole, supplies exterior gluing, a physical particle
norm or a coupling value. General fermionic traces, nonlinear source/
auxiliary boundary closure, curved normals and gauge compensation,
joint frequency control and the full global charged theory remain.

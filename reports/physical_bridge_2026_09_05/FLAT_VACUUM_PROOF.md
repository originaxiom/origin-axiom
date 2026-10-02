# R76: the action test, the localized extension, and the physical input

Authored conditional analysis, frozen pre-execution October 2, 2026.
Finite symbolic controls are not independent acceptance of its global
analytic arguments. No source dynamics or physical particles derived.

## 1. The map from this action, not a same-name harmonic theorem

Use the supplied static functional, with positive Hermitian trace norm:

    V=(2/g7^2) integral (|F_C|^2+|mu|^2),
    C=A+Psi, A dagger=-A, Psi dagger=Psi, mu=d_A^*Psi.

Set other fields to zero. For a flat rank-n bundle, a determinant-one
Hermitian metric H is an equivariant map to X=SL(n,C)/SU(n), represented
by positive Hermitian matrices. Its metric is
<U,V>_H=Re tr(H^-1 U H^-1 V). The holonomy acts by congruence isometries.
In a parallel flat frame D=d put T_i=H^-1 partial_i H. The adjoint flat
connection is D^{dagger_H}=d+T, so A=d+T/2 and Psi=-T/2. Covariant
divergence gives

    mu=(1/2) div(T), H^-1 tau(H)=div(T),
    E(H)=(1/2) integral |dH|^2=2 integral |Psi|^2,
    E2(H)=(1/2) integral |tau(H)|^2=2 integral |mu|^2,
    V|_(flat)=E2(H)/g7^2.

Here div includes the base Levi-Civita connection. The target tension is
tau=Delta H-sum g^{ij}(partial_i H)H^-1(partial_j H). The apparently
missing commutator in div_A Psi is zero in the contracted diagonal sum
[T_i/2,-T_i/2]; dropping the target's inverse-metric quadratic term is
not justified. All these equations transform covariantly between parallel
frames. V is not the ordinary harmonic-map energy E.

Varying H compactly, with D fixed, is equivalently a positive complex
gauge path of flat C represented in a fixed unitary frame. It is an
allowed variation of the bulk fields, not a physical compact-gauge
redundancy. Flatness stays zero along the path. Thus a stationary flat
point of the FULL bare functional must be critical for E2. It is
biharmonic. Conversely a harmonic flat point has all residuals zero
and is stationary in the positive residual functional. This argument
does not constrain a nonflat stationary point, nonzero other fields,
or a shifted/source/boundary functional.

## 2. Complete equivariant stationarity implies harmonicity

Nakauchi--Urakawa--Gudmundsson Theorem2.1 (arXiv1201.6457v4, p4) states
the ordinary-map result for complete source, nonpositive target curvature,
finite E and E2. It does not assert a noncompact harmonic-metric existence
theorem for arbitrary representations. Here extend its cutoff proof to
the associated X bundle: covariant derivatives, curvature contractions,
norms and alpha=<df,tau> are holonomy invariant and descend to the BASE.
No integration over the infinite-volume universal cover is substituted.

The symmetric-space curvature at the identity, for Hermitian tangent
matrices, is R(U,V)W=-(1/4)[[U,V],W]; hence
<R(U,V)V,U>=-(1/4)|[U,V]|^2 <=0. This is the affine-invariant target
metric above, not the internal base's sectional curvature.

At a biharmonic point J(tau)=0, J=nabla^*nabla-R. Choose complete
exhausting compact cutoffs chi_R with |dchi_R|<=C/R. Testing with
chi_R^2 tau and using the curvature sign and Young's inequality yields

    integral chi_R^2 |nabla tau|^2
      <=4 integral |dchi_R|^2 |tau|^2 ->0.

Finite E2 therefore gives nabla tau=0. With this, the descended one-form
alpha=<df,tau> has div alpha=|tau|^2 and
||alpha||_1 <= ||df||_2 ||tau||_2 <infinity. Integrating div alpha with
chi_R and using |dchi_R|<=C/R proves integral |tau|^2=0. This is a
direct cutoff argument; no sign-defective inequality in an appendix is
needed. It also treats a compact base without boundary by chi=1.

Therefore a smooth complete boundaryless flat background with finite
Higgs energy and finite static potential cannot evade the harmonic
equations by being a nonzero-residual stationary point of THIS bare
action. R75's invariant-subbundle balance then forbids its nonsplit W
under precisely these hypotheses. This is a scoped flat-vacuum result,
not a universal chirality kill. It does not forbid dynamical time-dependent
fields, nonflat vacua, admitted physical boundaries, singular/infinite-E
backgrounds, sourced actions or the logarithmic cone models.

An explicit opposite control is f=x^2 on [0,1], target R. It has tau=2,
tau2=f''''=0 and is critical for (1/2) integral(f'')^2 when both endpoint
value and first derivative are fixed. Its boundary first variation is
[f'' delta f'-f''' delta f]; the divergence current f' tau has nonzero
net boundary flux. It violates the complete-boundaryless premise.
On all R it also has infinite E and E2. No false universal extension.

## 3. The counted extension splits on its actual cusp

R75 supplies 0->V->W->1->0 and a NONZERO class c in H1(M3;V).
Longitude eigenvalues are q,q,q,q^-3, with q>0 !=1. On P=<z,ell>,
Vell-I is invertible. Define w=(Vell-I)^-1 c(ell). The commuting
cocycle identity is

    (Vz-I)c(ell)=(Vell-I)c(z).

Consequently c(p)=(Vp-I)w on both generators and hence on all P.
Conjugating W by B=[[I,-w],[0,1]] gives B^-1 W(p) B=diag(Vp,1).
This is peripheral splitting, not global splitting. Its exact algebra
is checked on the already verified R75 sextic. q=1 is excluded and
must make the longitude inverse fail.

In smooth de Rham form, choose a vector-bundle splitting and write
D_W=[[D_V,beta],[0,d]], where d_V beta=0 represents c. On a sufficiently
deep collar beta=d_V u. With chi=1 far out and zero before the collar,

    beta_c=beta-d_V(chi u)

is smooth, compactly supported and represents the same NONZERO class.
The triangular quadratic beta wedge beta is zero, so flatness is
preserved exactly, not only to first order. This is a gauge/splitting
change; it does not remove the extension class or its R75 index.

Conditional on the R44 same-base finite-energy harmonic metric on V
(including its external geometric hypotheses), equip V+1 with H_V+1.
In the localized splitting, W coincides with the split flat harmonic
background on the entire deep end. Its Higgs energy is finite, and
its real residual is smooth and COMPACTLY SUPPORTED. Thus the current
needed by the nonsplit object need not be a cusp-divergent prescribed
density. This existence is conditional on R44, not a new analytic
recertification of that prior. It changes no supplied base metric.

## 4. Exact scaling of the same extension class

Let D_t=[[D_V,t beta_c],[0,d]], t>0, with the fixed metric H_V+1.
Every D_t is flat and conjugate as a local system to D_1 via the
determinant-one matrix G_r=diag(r I4,r^-4), t=r^5. It is NOT compact
unitary gauge unless r=1. Thus its topological index stays the same
for every positive t without identifying their physical metrics.

Write b_i for beta_c in an orthonormal base frame and
B=sum b_i b_i^dagger. Since the diagonal background is moment-flat,

    mu_t=t L+t^2 Q,
    L is off-diagonal Hermitian,
    Q=-(1/2) diag(B,-tr B).

L collects the actual derivative and diagonal-background cross terms;
it is not assumed to vanish. Both are compactly supported. Trace
orthogonality gives <L,Q>=0. Consequently

    V_t=(2/g7^2)(a t^2+c t^4),
    a=integral |L|^2 >=0,
    c=(1/4) integral(tr B^2+(tr B)^2)>0 if beta_c !=0.

The Higgs norm is likewise finite: integral|Psi_t|^2 equals the
diagonal background value plus (t^2/2) integral sum|b_i|^2. For the
rank-five projector xi=diag(1,1,1,1,-4),

    tr(xi I_t)=5t^2 tr B, I_t=-2mu_t.

Thus the existing source balance is an exact local identity on this
family, not a guessed scalar charge. The potential strictly increases
with t>0 and tends to zero as t->0. There is no bare stationary vacuum
on this particular scaling path, despite its unchanged positive
cohomological asymmetry. Its zero-potential limit is the split bundle,
whose index is0, already verified in R75. This is a nonattained infimum
within the nonsplit complex orbit, not a proof that quantum evolution
chooses that limit. The target distance for the corresponding relative
metrics diverges: for H_r=(G_r^-1)^dagger G_r^-1,
distance(I,H_r)^2=tr(log H_r)^2=80(log r)^2
                         =(16/5)(log t)^2.

The metric distance is not automatically a four-dimensional scalar
distance: integration over the internal metric and gauge compensation
would be needed for that identification.

## 5. What a positive source construction would still have to earn

One can define S=I_1 from the localized metric. It is smooth and compact,
with the correct nonzero projector integral. In a DECLARED shifted
functional |I-S|^2 the residual vanishes; treating S as an externally
specified covariant spurion changes the model. This is not deriving
S from fields, their kinetic terms, their variations or the principle.
Keeping the commutators on both sides without subtracting them from
the moment map would double count them (R41). Localizing the residual
does not make this shortcut a physical source action.

The next admissible constructive test must supply the actual parent
source/core/end field law, solve its complete coupled variations and
transport its positive fluctuation norm/domain. Then recalculate the
whole spectrum, exterior five-bars, anomaly cancellation and normalized
interactions in that SAME admitted configuration. B1513's upcoming
cohomological Higgs/Yukawa calculation remains valuable and distinct.
Neither its dictionary nor the source-free obstruction establishes
whether that physical construction exists. No SM or TOE completion.

Primary source: https://arxiv.org/pdf/1201.6457v4, theorem2.1 and its
four-step proof, pp4--8; appendix4.1, pp10--11. Entire16-page extracted
text personally read. The PDF contains harmless typesetting slips:
p7's last line omits a square after deriving |tau|^2; appendix4.1's
display4.5 treats signed divergence as nonnegative. The direct cutoff
above avoids that display. Its integral identity4.4 suffices. No
literal quotation or redistributed publisher file is used.

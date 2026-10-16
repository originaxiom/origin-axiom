# Source Gauss law and fermion induced boundary flux

BANKED IDENTITY: actual source time/spatial coefficients and the known
faithful root/amplitude map are replayed before the new Gauss current.
PRIOR ART: earlier source and reverse proofs, actual source code and
different-parent silver Gauss proof were read; DESIGN records the199hit
search. Standard Noether, Green and graded symplectic identities are
credited. This is authored conditional mathematics, not external review.

## 1 Source kinetic coefficient and its explicit divergences

Use the ACTUAL WZ and K action, not a guessed ten dimensional weight.
With v_mu=2i X_mu the actual vector action -Tr(F(v)^2)/2 has temporal
part2 sum B(F_time,j,F_time,j), B=-Tr on real compact fields. The K
temporal part has the same coefficient for all six internal components:

    K_j=D_time c_j-i d_j v_time/sqrt2,
    Tr(K_j^dagger K_j)=2 B(F_time,2j,F_time,2j)
                         +2 B(F_time,2j+1,F_time,2j+1).

For j=2 there is no d_j derivative. The superspace raw expression may
differ by explicit divergence terms. For each homogeneous degree N,
vary the raw-minus-canonical difference under delta X=X. Integration
by parts gives N L=sum Tr(X Euler_X L)+div J. Checking every untraced
Euler coefficient zero AND L=div(J/N) constructs the primitive; it is
not discarded because the domains have boundaries. The raw auxiliary
terms have no temporal multiplier. Hence the canonical momenta are
p_j=4 F_time,j in the declared source units. Overall parent coupling
and tangential volume remain supplied common factors.

If L_source=L_canonical+div B, choose theta_source=theta_canonical+delta B.
Its presymplectic form is unchanged by delta² B=0, while its variational
boundary data still carry B. Its improved gauge Noether current subtracts
delta_alpha B, cancelling this improvement. This does NOT select a full
boundary action or permit deleting B from stationarity equations.

## 2 Real full source and Lie algebra current

Let C16 be the actual spin conjugation, G the complete positive E8
coefficient metric, tau its compact conjugation. Majorana reality is
Psi=(C16 tensor tau) Psi*. The symmetric derivative form is

    T=C16^dagger tensor tau^dagger G,
    L_f=(i/2) Psi^T T(D_time+sum v_j D_j)Psi.

The actual source time gauge coupling fixes this sign and half factor.
In a complete positive real compact frame, T becomes I3968; all real
velocities are symmetric and every real adjoint generator antisymmetric.
For any compact alpha define j by

    B(j,alpha)=(i/2) Psi^T T ad(alpha) Psi.

The antisymmetric matrix does NOT vanish on odd variables. Its coefficient
for real Grassmann generators xi_s xi_t, s<t, is i M_st. Its dagger
reverses odd order, so i times a real antisymmetric form is Hermitian.

For a family Psi=sum Psi_s xi_s, Lie pairing invariance gives the
alternative current contraction, for each actual action velocity V_N,

    (j_N)_st=-i sum_pq (C16^dagger V_N)_pq
                       [ (Psi_s)_p,(Psi_t)_q ], s<t.

Both calculations act in the full E8 algebra. The known family is in
its explicitly embedded invariant triplet, not an unrelated SU2 toy.
All ten currents are retained even if some vanish on this family.

## 3 Gauss and canonical endpoint charge

Use delta A_i=D_i alpha, delta Phi=[Phi,alpha] and
delta Psi=[Psi,alpha]=-ad(alpha)Psi. Variation of the same action in
the temporal multiplier gives

    G=4 sum_i D_i E_i+j=0, E_i=F_time,i.

Scalar D_i=ad(Phi_i) terms are part of the sum. With canonical
Theta=sum integral4 B(E_i,delta X_i)+(i/2) integral Psi^T T delta Psi,
integration by parts yields the exact local/both-end identity

    Theta(V_alpha)=Q[alpha]-integral B(G,alpha),
    Q[alpha]=4 integral_boundary B(E_n,alpha).

For the convention Omega=-delta Theta, a field independent parameter
has i_V Omega=delta(Q-G). A parameter alpha(g) instead obeys
i_V Omega=delta(Q-G)-(Q-G)[delta alpha]. On the constraint surface this
is delta Q[alpha]-Q[delta alpha]. Dropping the second term is unjustified
for the background dependent parameter used in the preceding packet.
This is a canonical initial-data identity. Which end transformations
are physical symmetries/null gauge requires the admitted ensemble.

## 4 Actual amplitude source and an electric response

Put s=1-g²r, q=g exp(-i theta/2)/(sqrt(r)s),
q_g=(1+g²r)exp(-i theta/2)/(sqrt(r)s²). The gate is that the actual
nonzero Gauss polynomial is q_g* q_g times H times a constant degree2
polynomial k(xi). Its coefficient is obtained from the full current,
not supplied or inferred from a matrix trace.

For radial Cartan profiles the full covariant Laplacian is

    L h=h''+h'/r-2g² h/[r(1-g²r)^2].

The actual source-normalized stationary Gauss equation is
Delta_A X_time=j/4. Direct differentiation verifies

    f=r/[4(1-g²r)^2],   L f=|q_g|²/4,
    X_time=H k(xi) f.

This is a regular particular nilpotent degree2 response, with zero
inner limit, not a unique boundary law. Any degree2 multiple of the
known h0=(1+g²r)/(2g(1-g²r)) can be added. In particular
f_R=f-f(R)h0/h0(R) has zero outer value and a generally nonzero regular
inner value. Keep these distinct data rather than infer that no electric
response is possible. Point-trace restrictions in singular H1 limits
need their own proof; no both-zero-end singular-domain no go follows.

The electric BODY remains zero. A nonzero Grassmann source or flux is
not a measured vacuum charge. Nor does this solve other spatial boson
currents, cubic fermion or quartic nilpotent backreaction equations.

## 5 Two different boundary identities

Let alpha=epsilon_g=i h0 H, covariantly harmonic with both scalar
directions retained. For EACH degree2 coefficient of X_time,

    4 d_r{r[B(alpha,D_r X_time)-B(D_r alpha,X_time)]}
        =r B(alpha,j).

This is Green reciprocity. The canonical charge is instead
Q_r=-4r B(D_r X_time,alpha). It satisfies

    d_r Q_r=r{4 sum_i B(E_i,D_i alpha)-B(j,alpha)}.

These are different expressions: do not identify a norm or Wronskian
with the electric charge merely because both have endpoint formulas.
Integrate with outer MINUS inner and angular factor2pi. Every inner
limit and outer cut is retained. Actual g variation also requires
Q_partial_g_alpha; its omission must fail a nonzero control.

There is a further DIRECT actual-field symplectic check. On the
degree2 Gauss family p_i=4 E_i, use V_alpha X_i=D_i alpha,
V_alpha p_i=-ad(alpha)p_i, V_alpha Psi=-ad(alpha)Psi. The canonical
contraction with the g tangent has density

    sum_i[B(D_i alpha,partial_g p_i)
               -B(partial_g X_i,V_alpha p_i)]
          -i (V_alpha Psi)^T T partial_g Psi.

Extract each genuine degree2 coefficient, including odd order reversal.
Its normal volume density must equal d_r(partial_g Q_r-Q_r[partial_g alpha]).
Dropping the real fermion term is an opposing control. A nonzero result
is a conditional presymplectic pairing on the Gauss initial-data family,
not proof that this g tangent is admitted by a selected full boundary
ensemble or that all other stationary equations have been solved.

The result, if its gates pass, supplies a fermion-inclusive local
Gauss/end law and one response, not the selected global ensemble,
complete coupled stationary theory, physical chiral SM/three or gravity.

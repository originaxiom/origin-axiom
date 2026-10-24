# Exterior response of the existing graded cusp background

October 24, 2026. Authored conditional algebraic derivation, UNREVIEWED.
No scientific producer, new check, SymPy import or test collection was
executed. This note is outside every frozen verification proposal.

Scope: the complete two-slot zero-angular fermion blocks of the existing
parallel graded cusp backgrounds in the supplied curved E8 theory.
Not every generated word, every end, the whole angular response, or a
derivation of that theory from foundational premises.

## 1. Recover the stronger source before adding a new mechanism

The existing sources include more than the one-root condensate:

- [The curved action](../weave_curved_action_2026_10_08/PROOF.md)
  specifies kinetic metrics, all four Weyl slots, Yukawas and graph law.
- [The graded condensate](../weave_graded_condensate_2026_10_08/PROOF.md)
  supplies a global stationary background and derives its coupled B_m
  blocks. Its compact E6 charged sector has a global pairing map.
- [The parallel SM-gauge phase](../weave_sm_parallel_2026_10_08/PROOF.md)
  reuses the operator through spin four, has a gapped end, and retains
  zero charged index under its specified compact-core Wilson homotopy.
- [The two-field completion](../weave_two_field_gauge_2026_10_08/PROOF.md)
  already activates a commuting pair that generates compact su3, not
  one sl2. Its chosen completed gauge algebra is g2, not the SM.

These proof bodies and the graded condensate's producer were personally
read; historical test reports were not freshly reproduced. In particular,
the two-field construction must not be rediscovered or excluded by
treating every commuting nilpotent pair as an sl2 triple. Nor should
the one-root end's gapless channels be attributed to every nonflat end.
The source's global analytic claims retain their outside-review duties.

This note derives the ZERO-ANGULAR exterior Cauchy relation of the
already specified gapped background. It does not claim the background
has just been discovered or its inputs have become forced.

## 2. Transport the actual mass block, rather than insert K

The source's canonical coefficients have ordinary radial measure dt,
t=log y. In its paired weight blocks,

    B_m = [[partial_t+a, k],[-k,-partial_t+a]],
    a=(m+1)/2,  k^2=(j-m)(j+m+1)/2,  k>=0.          (1)

The normalized gauge Killing map and superpotential Hessian give the
same k. The source R field is trace-dual at weight -m-1, not m+1.
Keep that physical dictionary and every original field. Write

    E=diag(1,-1), Z=[[a,k],[-k,a]],
    K=E Z=[[a,k],[k,-a]]=a sigma3+k sigma1.

Then E^dagger=E, E^2=I, Z^dagger E=E Z, and

    B=E(partial_t+K), B^dagger=(-partial_t+K)E,
    K^dagger=K, K^2=mu^2 I, mu=sqrt(a^2+k^2).       (2)

For the supplied self-adjoint doubled realization use

    D_old=[[0,B^dagger],[B,0]],
    (x,y)=U(x,v), U=diag(I,iE), v=-iE y.

U is a constant unitary map on the already normalized Hilbert slots.
Direct multiplication, including the derivative signs, gives

    U^dagger D_old U
      = [[0,i(-partial_t+K)],[-i(partial_t+K),0]]
      = -i sigma1 partial_t-sigma2 tensor K.       (3)

Thus the earlier constant-tail response calculation applies to THESE
actual blocks by an exhibited isometry. K is not an independently
adjusted mass here: a comes from the kinetic density/spin connection
and k from the chosen stationary condensate and the same action.
The common curvature unit is still supplied. The tensor slot of (3)
is NOT thereby identified with the paper's raw quaternion doublet.

At an unpaired extreme retain the scalar block B=epsilon partial_t+a,
where epsilon=+1 for the A/gauge-map derivative and -1 for the Q/dual
derivative. Set E=epsilon, Z=a, K=epsilon*a. The identical unitary
calculation applies. Discarding these scalar blocks would change the
response; they are not zero modes that may be dropped from (1).

## 3. The end norm determines its zero-energy relation

On the actual outward cusp t>=T, equation (3) at zero reads

    x'=-Kx, v'=Kv.

For invertible Hermitian K the square-integrable traces are exactly

    L_ext = image(P_+(K)) in x
            direct-sum image(P_-(K)) in v.         (4)

For a paired block P_+(K)=(I+K/mu)/2 and P_-=I-P_+.
For the scalar extreme they are the sign projectors. The Hermitian
Green matrix of (3), up to common normal factor, is

    G=[[0,I],[I,0]].

Orthogonality P_+ P_-=0 proves current nullness. The ranks sum to the
coefficient dimension, so this is maximal null. For example an allowed
trace has profiles exp[-mu(t-T)]x_T and exp[-mu(t-T)]v_T in its
respective spectral subspaces. Its exterior norm is

    (||x_T||^2+||v_T||^2)/(2mu).                  (5)

Keeping both slots is essential: an entire paired block has one decaying
direction in each slot, not just one of the original Weyl fields.
The choice at the artificial cut is removed by the specified exterior
operator and L2 norm, not by declaring a desired plus rank.

The source allows even m in zero-angular blocks. Hence a is a nonzero
half integer and mu>=1/2. Scalar extreme K is also nonzero: an upper
extreme m=j even has K=(j+1)/2>0; a lower extreme m=-j-1 even has
K=j/2>0 (j odd). Thus the retained zero-angular system is genuinely
gapped, conditional on this background and normalization. This recovers
the earlier threshold argument rather than propose a new gap.

In one integral-spin j module, paired blocks contribute one positive
and one negative eigenvalue of K. There is one scalar extreme: the
upper one for j even, the lower one for j odd. There are j paired
blocks, so K has j+1 positive and j negative eigenvalues. This is
boundary-slot bookkeeping, NOT a four-dimensional charged index or a
generation count. The source's paired charged sectors can have this
local asymmetry while their global net charged index is zero.

## 4. Energy dependence is a derived boundary response too

For real spectral parameter lambda with |lambda|<mu, (3) gives

    psi'=L_lambda psi,
    L_lambda=-sigma3 tensor K+i lambda sigma1 tensor I,
    L_lambda^2=(mu^2-lambda^2)I.

Put kappa=sqrt(mu^2-lambda^2)>0. The unique decaying Cauchy plane is
the range of the idempotent

    P_dec(lambda)=(I-L_lambda/kappa)/2.            (6)

At lambda=0 this is diag(P_+(K),P_-(K)), as in (4).
For nonzero real lambda it is generally NOT an orthogonal projector;
L_lambda is not Hermitian. Nevertheless L_lambda^dagger G+G L_lambda=0,
so conserved current and decay prove its range is null, with half rank.
Equating idempotence with orthogonality would be an instrument bug.

As |lambda| approaches mu the exponential dichotomy closes; (6) has
no bounded extension supplied by this formula. At the threshold itself
L_lambda^2=0; solutions are affine in t and no nonzero such solution
is L2 on the half-line. This is not a zero-dimensional Fredholm domain:
threshold spectral data must be retained. Lambda is a spectral variable,
not a new adjustable coupling or a free choice of physical vacuum.

No nonzero-angular boundary projector or regularized infinite boundary
determinant is computed here. The earlier source's angular confinement
argument is not an explicit Cauchy relation in those channels. Both
remain distinct from the critical six-dimensional puncture quotient.

## 5. What symmetry can legitimately constrain this response

Covariance of an action/operator family is schematically

    D_(g.Phi)=U_g D_Phi U_g^-1.

It implies commutation with U_g at a background only when g fixes that
FULL background (or a verified gauge identification supplies the same
domain map). A state coordinate S=I by itself does not establish that
the spin Higgs, connection, metric, lifts and end domain are fixed.

The earlier Q8 calculation explicitly assumed W=C3 tensor C2 with a
particular common action on its two Green slots. In (1)--(6), x,y are
the actual mass-map source and adjoint slots after metric/dual-weight
normalization. No faithful intertwiner from that W, state action and
Gamma to this parent has yet been exhibited by the cited sources.
Do not import either the even-rank restriction or its conditional
sheaf-index formula merely because both calculations use a Green form.

Conversely a nonzero condensate is not automatically an allowed cure
for P-210: one must derive its role in the generated state and verify
the actual lifted action. This note does not establish that the graded
background is Q8-fixed or prove that it breaks precisely that Q8.
The residual symmetry question requires the missing map, not a guess.

## 6. Input accounting and next discriminating work

| Item | Status in this calculation |
|---|---|
| K, its scale relative to curvature, and its Cauchy plane | Derived from the existing normalized block, chosen background and L2 end; not independent new insertions |
| Action, curved metric, spin line, field roster and global condensate | Supplied or conditionally constructed in the older packets; not derived here from non-cancellation |
| Selecting this stationary background | Not paid; zero classical residuals also occur on other backgrounds |
| Physical charged chirality | Not obtained; preserve the existing pairing/charged-index results on these particular phases |
| Paper coefficient-to-parent and full-register action | A separate identification duty, not supplied by equal dimensions, E8 names or current signatures |

The useful advance is an explicit response map within the SAME specified
operator, not a new foundational-input reduction or a physical particle.
It prevents spending an extra arbitrary normal mass where the action
already provides one, and prevents turning a scoped stabilizer result
into an exclusion of a different physical background.

A successor verification design should retain: the differential B/Bdagger
transport; omission of the i in U while falsely keeping equation (3),
and the wrong dual-R weight; both scalar extreme
orientations; the full zero-energy norm and both decaying slots; (6) at
zero and nonzero lambda; idempotence versus orthogonality; threshold
loss of the dichotomy; and covariance/intertwining controls for any actual
Q8/tensor identification proposed. A consistently transported alternative
phase is merely a frame convention, not a physically excluded theory.
It must seal its own sources and obtain independent/main admission
before execution. The existing P210 checks and specification are frozen
unchanged; their ten methods have not thereby run or become approved.

Research custody: own-branch starting checkpoint 39ce620a8; origin/main
refreshed at 3bf82d0ca08284a631016b217e0b9297a756f8ff. Already-banked
search terms were commuting, two-field, cusp, condensate; its strongest
settled keyword hit B1248 concerns Fricke norm classes, not this operator.
An initial grep used an incorrect SM ref and failed, then the actual
remote refs were enumerated before re-searching. Searches recovered the
older constructions above. No exhaustive absence, novelty priority,
independent acceptance, global scientific pass or TOE completion is claimed.

# The quantum normalization duty for the one-loop coupling relation

November 1, 2026. UNREVIEWED author derivation and targeted primary-source
reading. No scientific producer, CAS, scientific-module import or test execution.
This is a conditional continuation of our existing parallel-phase action,
not an independent review, admitted quantum compactification or prediction
for measured Standard Model couplings.

## 1. Prospective reduction question and scope

The earlier heat proof removes a common internal mass scale and light
matching switch from ONE one-loop relative coupling combination on its
nonexceptional character family. What normalization information would be
required to carry that combination beyond one loop? Is a full arbitrary
flavour metric needed for this particular gauge-matching duty?

Quantifier: the specified supersymmetric parallel phase with its complete
light roster, arbitrary allowed carrier shape and all four extending
spins, at the source order-seven Wilson character. The formulas extend
only where the COMPLETE light roster remains exactly (4), including its
spin/charge exceptions; the one-loop condition h_C=0 alone is insufficient
to assert that roster. No character is selected by this continuation.
No restriction to m004 or a single word is made. No claim covers every
generated field assignment, background or physical end law.

For the quantum statement ADD an explicit hypothesis: this light sector
has an admitted finite four-dimensional renormalizable N=1 EFT over a
scale interval with no threshold crossing or supersymmetry breaking.
Its regulator and Wilsonian scheme must support the rescaling-anomaly
relation below. This hypothesis is not derived by the classical mass map
or by positivity. Infinite KK sums, irrelevant interactions, quantum
gravity and physical low-energy matching are separate duties.

The proposed positive is a fixed-frame perturbative RG relation and a
precise weighted determinant requirement. It is not a proposed removal
of the physical kinetic metric, parent action or all mass scales.

## 2. Reused results and personally checked primary formulas

Reuse [the actual light kernel and running](PARALLEL_PHASE_CHIRAL_KERNEL_AND_LIGHT_RUNNING.md),
[the physical gauge/ghost weights](SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md),
[the full relative heat proof](TWO_HEAT_RESPONSES_AND_SCALE_FREE_COUPLING.md)
and [its unspecialized author audit](TWO_HEAT_RESPONSES_AUTHOR_AUDIT_2026_10_29.md).
Their independent-review qualifications remain unchanged. The roster is
not recomputed from a preferred V3 slot, and these derived responses are
not reclassified as independent adjustable inputs.

Personally read the relevant normalization, measure and matter discussion
in Arkani-Hamed and Murayama, hep-th/9707133, especially equations 2.8--2.12
and 4.1--4.6, and the scheme discussion in section 2. Equation 4.6 was also
checked on a rendered page. Their analysis uses Wilsonian couplings; it
does not identify a canonical coupling with a measured 1PI coupling
without further matching. The rescaling Jacobians matter. We use their
perturbative relation in a specified scheme:
[primary paper](https://arxiv.org/pdf/hep-th/9707133).

Martin and Vaughn's equations 2.1--2.3 and 3.1--3.6 supply the separate
two-loop check below; their gauge formula was also inspected visually:
[primary paper, version 4](https://arxiv.org/pdf/hep-ph/9311340v4).
These are targeted readings, not claims to have read either whole paper.
The formulas are established QFT results, not discoveries of this lane.

## 3. Keep the matrices, the holomorphic frame and the measure

Let a=1,2,3 denote SU5-normalized hypercharge, weak SU2 and colour SU3.
Write g_a for the canonical Wilsonian coupling and alpha_a=g_a^2/(4 pi).
For each irreducible gauge representation r, let Z_r(mu) be its positive
Hermitian kinetic matrix on ALL identical light copies in one fixed
holomorphic field frame. Z is dimensionless in that fixed four-dimensional
field basis and reference normalization. A dimensionful profile integral
cannot be put inside a logarithm without that normalization. It includes
the actual normalization data; it
is not set to I by assertion. Its determinant is over copies, not over
gauge components. T_a(r) already includes spectator gauge dimensions.

In the chosen rescaling-anomaly convention define the holomorphic-side
real coefficient R_a by

  R_a = 8 pi^2/g_a^2 + C_a log(g_a^2)
                           + sum_r T_a(r) log det Z_r,       (1)
  dR_a/d log(mu) = -b_a,
  C_a=(0,2,3), b_a=sum_r n_r T_a(r)-3 C_a.                  (2)

Finite matching constants can be included in R_a at a chosen reference
scale. Their values and the holomorphic field frame must be stated; (2)
does not determine them. The anomaly formula is applied factor by factor
to this one-U1 product gauge group.

For a matrix Z, diagonalize it at the scale in question and apply the
rescaling Jacobian to each identical copy. The resulting sum of logs is
log det Z. Unitary rotations introduce no extra REAL determinant term.
No simultaneous diagonalization of Z and its scale derivative is needed:

  d log det Z / d log(mu) = tr(Z^(-1) dZ/d log(mu)).         (3)

This retains mixing rather than replacing the matrix by a guessed common
eigenvalue. Phase/theta accounting is not completed by a parity-even log.

## 4. Apply the relation to the actual complete light roster

The preceding kernel derivation gives

  2(10+bar10)+4(5+bar5),
  kappa copies of the unbroken adjoint chiral sectors,
  kappa=1 or 3,
  b=(10,4+2 kappa,1+3 kappa).                              (4)

These are representation COUNTS, not restored SU5 gauge symmetry or equal
wavefunctions within a multiplet. All conjugate left chiral multiplets
are retained. They are not counted again as their own right conjugates.
Gauge singlets have zero insertion here but can enter the Yukawa dynamics.

Set w=(1/2,-3/2,1) and

  C=alpha3^(-1)-(3/2)alpha2^(-1)+(1/2)alpha1^(-1).

Direct substitution gives w dot b=0 for both values of kappa and
w dot C_adjoint=0. Weighting (1) therefore yields

  I = sum_a w_a R_a
    = 2 pi C + 3 log(g3^2/g2^2) + W_Z,
  dI/d log(mu)=0,                                         (5)
  W_Z=sum_r c_r log det Z_r, c_r=sum_a w_a T_a(r).

Equation (5) is perturbatively exact WITHIN the finite EFT and scheme
hypotheses, at fixed holomorphic frame and without crossing thresholds.
It is one running constraint. It does not give I's value, fix Z, select
a vacuum, or identify I as a frame-independent measured observable.

The explicit coefficients are derived from T1=(3/5)Y^2 dim(r2)dim(r3),
T2(fundamental)=T3(fundamental)=1/2:

| gauge block r | T1 | T2 | T3 | c_r | size of Z_r |
|---|---:|---:|---:|---:|---:|
| Q in 10 | 1/10 | 3/2 | 1 | -6/5 | 2 |
| U in 10 | 4/5 | 0 | 1/2 | 9/10 | 2 |
| E in 10 | 3/5 | 0 | 0 | 3/10 | 2 |
| D in 5 | 1/5 | 0 | 1/2 | 3/5 | 4 |
| L in 5 | 3/10 | 1/2 | 0 | -3/5 | 4 |
| colour adjoint | 0 | 0 | 3 | 3 | kappa |
| weak adjoint | 0 | 2 | 0 | -3 | kappa |

Each conjugate of Q,U,E,D,L has its OWN matrix with the same coefficient
and size. Equality of conjugate matrices is not assumed. D and L label
the colour and weak blocks of the gauge five, not a new field assignment.
Consequently

  W_Z = -(6/5) log(det Z_Q det Z_barQ)
         +(9/10) log(det Z_U det Z_barU)
         +(3/10) log(det Z_E det Z_barE)
         +(3/5) log(det Z_D det Z_barD)
         -(3/5) log(det Z_L det Z_barL)
         +3 log det Z_8 -3 log det Z_3.                    (6)

The determinants already include copy multiplicities. Multiplying (6)
by 2, 4 or kappa again would be an error.

This is a useful conditional reduction of the MATCHING DATA required by
this one gauge combination: at a fixed scale the rescaling contribution
uses only the displayed weighted determinants. A determinant-one flavour
deformation has no direct contribution to that Jacobian. A physical
kinetic deformation at fixed holomorphic interactions can still change
masses, normalized Yukawas and the later running of the determinants.
The full physical flavour problem is not reduced to one scalar metric.

## 5. A separate two-loop discriminator, with the Yukawa leg retained

For the same finite N=1 roster, write the canonical two-loop beta function
in the Martin--Vaughn normalization as

  dg_a/dt = g_a^3 b_a/(16 pi^2)
       +g_a^3 [sum_b B_ab g_b^2 - Y_a]/(16 pi^2)^2 + ...,
  t=log(mu),
  B_ab=2 C_a b_a delta_ab+4 sum_r n_r T_a(r) C_b(r).         (7)

Y_a is their complete cubic-Yukawa contraction
Y^(ijk) conjugate(Y^(ijk)) C_a(k)/dim(G_a), with all component
indices summed. It is not set to zero by assumption. Section 7 derives
its vanishing on one spin branch and retains the other branch. The U1
formula uses its normalized charge and dim(G1)=1.

The required representation Casimirs are

  C1(Q,U,E,D,L)=(1/60,4/15,3/5,1/15,3/20),
  C2(Q,L)=3/4, C3(Q,U,D)=4/3,
  C2(adj2)=2, C3(adj3)=3.                                  (8)

The actual copy populations are four each of Q,U,E including conjugates,
eight each of D,L including conjugates, and kappa adjoints of each
nonabelian group. Substitution gives the FULL pure-gauge coefficient
matrix

       [ 166/15      42/5           416/15       ]
  B =  [ 14/5        46+24 kappa   32           ].          (9)
       [ 52/15       12            178/3+54 kappa]

Weighting its rows gives

  G_b=(w B)_b=(24/5,-264/5-36 kappa,126/5+54 kappa),
  dC/dt = -[sum_b G_b g_b^2 - Y_C]/(32 pi^3)+...,
  Y_C=(1/2)Y_1-(3/2)Y_2+Y_3.                               (10)

Two hand cross-checks retain the factors and multiplicities:

* The off-diagonal entries obey dim(G_a)B_ab=dim(G_b)B_ba,
  with dimensions (1,3,8): 42/5=3(14/5),
  416/15=8(52/15), and 3(32)=8(12).
* Directly summing c_r C_b(r), INCLUDING copies, gives
  (6/5,-36/5-6 kappa,24/5+9 kappa). Multiplication by 4 and
  addition of 2 w_b C_b b_b gives exactly G above, independently
  of assembling (9).

Thus the one-loop balance is not a representation identity that also
annuls the gauge part at two loops. Its first component 24/5 is already
nonzero for either spin case. In the explicitly labelled Y=0 control at
equal gauge couplings, the sum of G is -24/5 for kappa=1 and 156/5 for
kappa=3. This control distinguishes the proposed all-order strengthening.
Section 7 earns the vanishing marginal Yukawa on kappa=1; the kappa=3
Y=0 choice remains a control, not that branch's interacting result.

For a branch with nonzero cubic interactions Y_C must be derived from
its complete normalized overlaps. Cancellation with the gauge contribution
is not excluded by (9). The explicit duty is Y_C=sum_b G_b g_b^2 at this
order. Section 7 discharges the cubic question for kappa=1 within this
phase; it does not turn that phase into the eventual physical SM state.

## 6. Controls on normalization and on the meaning of the invariant

1. Define s_r=d log det Z_r/dt. Differentiating (1), with no convention
   imported for the name gamma, gives

     beta_g,a = g_a^3 [b_a+sum_r T_a(r)s_r]
                    /[16 pi^2 (1-C_a g_a^2/(8 pi^2))].     (11)

   With Gamma_r=-s_r this has b_a-sum T_a Gamma_r in the numerator.
   In pure SYM it gives -3 C_a g_a^3/[16 pi^2(1-C_a g_a^2/(8 pi^2))],
   agreeing with the primary paper's equation 2.12. Its v1 equation 4.7
   visibly prints 8 pi^2 instead of 16 pi^2 and uses a gamma convention
   that should not be transplanted into (11). The pure-SYM limit exposes
   the factor discrepancy without trusting an OCR transcription. We use
   equation 4.6 plus the explicit derivative above, not a silent copy of
   equation 4.7. This is a local source-normalization check, not a new
   criticism of the established rescaling-anomaly result.
2. If the three kinetic matrices WITHIN a ten are equal in their common
   two-copy basis, their contributions cancel: -6/5+9/10+3/10=0.
   The analogous equal four-copy five matrices cancel 3/5-3/5=0,
   and equal adjoint determinants cancel. The spectrum forming complete
   SU5 counts alone does not prove these equalities. H=I at one matching
   scale does not establish that they persist under the broken-group RG.
3. Under a holomorphic copy change phi'_r=A_r phi_r,
   Z'_r=A_r^(-dagger) Z_r A_r^(-1). Thus log det Z'_r changes by
   -2 log|det A_r|. The anomalous measure shifts R_a by the corresponding
   -2 sum T_a(r)log|det A_r|. C, transformed Yukawas and all measuring
   data must travel together. I is constant along RG flow in a FIXED
   frame; its value is not a frame-independent number extracted for free.
4. For a general exceptional order-two or order-three character the old
   light roster changes. Reuse its actual kernel formula before forming
   w dot b. Equations (4)--(10) are not exported through those crossings
   or through restored SU5 without recalculating the light EFT.
5. RG-scale mu, a common internal KK mass rescaling, a finite threshold
   matching scale and a change of physical measuring units are distinct
   operations. Equation (5) controls the first. It does not prove that
   the old relative heat threshold is independent of the other three
   operations beyond its already-established one-loop scope.

## 7. The same-action cubic is fixed, not supplied, on the kappa=1 branch

The actual parent has

  W=(1/2) integral kappa(q Dbar_A r-r Dbar_A q).

Around its R=0 parallel background Q0, its complete third-order
holomorphic term is, up to the already fixed common convention,

  W3(a,u,v)=-i integral kappa(u,[a,v]),                     (12)

where a,u,v vary A,Q,R respectively. This follows by expanding BOTH
antisymmetric terms and using trace invariance. There is no other
superpotential vertex in this parent to append by choice.

Reuse the COMPLETE kernel proof's actual harmonic representatives in
each principal module V_j:

  a_j in H1_L2(S^(-j)L), principal weight +j,
  u_(-j) in H0_L2(S^(j+1)L), principal weight -j,
  v_j in H0_L2(S^(1-j)L), principal weight +j.              (13)

These are representatives satisfying the physical mass and gauge-slice
equations. The bounded contraction and kernel count already prove they
span the chiral kernel; no cohomology representative is substituted for
an unrelated physical mode. In particular every a_j is highest weight,
so [Q0,a_j]=0 pointwise, including j=0.

For a NONTRIVIAL extending spin, kappa=1:

* The unbroken gauge j=0 sectors have no v_0, since H0_L2(S)=0.
  The mixed charged j=0 sectors have no light modes at order seven.
* Every j>=2 has H0_L2(S^(1-j)L)=0 by the existing exact cusp pole bound.
* In the gauge five's j=1 sectors, the line has nontrivial order-seven
  character, so H0_L2(L)=0.
* The remaining gauge-singlet 24_b has exactly one j=1 module. Its
  v_1 is H0_L2(O)=C, the highest vector of the principal triple itself.
  Globally this is v=c Q0. It is not an independently chosen profile:
  Q0 is the parallel nonzero section of that line.

Thus EVERY light R variation is a multiple of Q0, and every light
connection variation commutes with it. Substitution into (12) gives

  W3 restricted to ALL massless chiral modes = 0,
  hence every tree-level charged marginal Yukawa vanishes. (14)

This is a pointwise bracket zero, not an integration-by-parts cancellation
that discards a cusp term. It holds for the whole light kernel and every
carrier shape under the stated hypotheses; it is not obtained by removing
massive modes or selecting only three convenient fields.

In an admitted supersymmetric perturbative EFT, eliminating an invertible
heavy sector does not manufacture a tree-level cubic: its light-heavy
quadratic block vanishes on the actual mass kernel, so its sourced heavy
solution starts at quadratic order in the light fields. Substitution
first changes fourth and higher orders. The required inverse/domain and
holomorphic EFT matching remain part of that admission. Perturbative
superpotential nonrenormalization then keeps the marginal cubic zero.
Gauge and induced higher interactions remain; W_light at cubic order zero
does not mean the underlying parent, all light interactions or all
higher effective superpotential terms vanish. Nonperturbative terms,
supersymmetry breaking and changed backgrounds are outside this argument.

Accordingly Y_a=0 in the leading renormalizable perturbative light EFT
on this branch. Its actual two-loop result is

  dC/dt = -(12/5)(2 g1^2-37 g2^2+33 g3^2)/(32 pi^3)
             + higher-loop terms,  kappa=1.               (15)

This polynomial is not identically zero. It can vanish at special coupling
values; no selected matching point is supplied here. At equal nonzero
couplings it is nonzero. The implication is precise: the one-loop
representation balance does not protect C itself beyond one loop in this
admitted spin branch, whereas the extended relation (5) still carries the
matter normalization. This is no exclusion of another branch or of SM3
elsewhere in the generated architecture.

The TRIVIAL-spin branch is a rejecting control on any universal extension
of (14). Now kappa=3, and both u_0 and v_0 exist in the unbroken adjoint,
as does a_0. Let psi be its holomorphic spin section, omega=psi^2 the
elliptic holomorphic one-form, and choose a_0 proportional to bar(omega).
With three noncommuting generators in the same unbroken su2,

  integral kappa(u_0,[a_0,v_0])
    is proportional to kappa(T1,[T2,T3])
                           integral omega wedge bar(omega),

which is nonzero. The profiles have the source's finite positive norms.
Thus the old cubic is genuinely present on this branch; its normalized
Y_C cannot be erased using (14). No numerical value or an accidental
all-sector cancellation is asserted.

The earlier silver charged-cubic transgression is a different coefficient,
carrier and domain problem. Its zero result is not imported here. This
section uses the present spin-parent functional and the present full
kernel; the existing kernel and parent proofs retain their review status.
The new projection/nonrenormalization argument is UNREVIEWED author work.

## 8. What remains to earn from the same parent

The preceding [actual-complement norm](FULL_MODE_ELIMINATION_AND_INDUCED_KINETIC_METRIC.md)
is a reconstructed spectral norm for an already fixed Hilbert space and
operator. It is not automatically the interacting renormalized Z_r in
(1). A physical identification needs the action's four-dimensional
kinetic expansion, its actual light-mode map and the quantum matching.
Classical inner products and loop wavefunction responses must both be
derived, rather than a freely fitted Gram appended to a residue matrix.

Likewise, the parity-even full-cusp heat determinant is not automatically
the real part of a holomorphic Wilsonian gauge function. No such map was
exhibited in the earlier proof or is supplied merely by (5). Its regulator,
phases, finite terms, light subtraction and measure must be matched on
the same field/action/domain construction. In particular its zero-Wilson
reference restores extra gauge modes; comparing the two infrared EFTs
requires those modes and their matching, not identical-roster bookkeeping.

Before: a controlled one-loop scale cancellation and an unspecified
higher-order normalization duty. After: an explicit weighted determinant
map, a fixed-frame perturbative RG constant, the complete gauge part of
the two-loop duty, and a same-parent derivation of the vanishing marginal
cubic on the nontrivial-spin branch. The trivial-spin cubic is retained.
These are conditional dependency results, not removed foundational inputs
or derived SM constants. Given a full quantum parent the Z_r are outputs;
they must not be counted as new free inputs just because this lane has
not computed them. If a metric is instead genuinely chosen, its price
remains. Full chirality, three generations, physical parameter matching,
gravity and the foundational selector remain the mission.

Independent proof review should check (1)'s convention/frame constants,
matrix multiplicities, the full beta matrix and the actual physical
transfer. Any future executable checks need a new source-complete design,
main's independent review/acceptance and prospective admission. This note
executes none and modifies no frozen package or accepted evidence.

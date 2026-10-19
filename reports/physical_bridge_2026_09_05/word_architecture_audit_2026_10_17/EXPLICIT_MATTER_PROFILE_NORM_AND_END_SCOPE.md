# The explicit matter-profile norm is not the Higgs end cutoff

October 19, 2026. Analytical continuation of the input-reduction mission.
The existing theta doublet supplies an explicit normalizable profile
in specified fibre problems. Three equivalent parity copies then have
a common scalar Gram, not an arbitrary flavour metric. Ordinary spin
at a complete cusp has a different norm and excludes this profile.
No four-dimensional operator, physical field dictionary or end law
is inferred from those fibre facts. No scientific producer was run;
independent review and scientific admission remain outstanding.

## Reuse the actual profile and analytic controls

The complete B1642 `verification/residue_coupling.py` was read directly
in `/Users/dri/origin-axiom/frontier/B1642_the_golden_coupling_as_the_zero_modes_residue/`.
It already credits W21 for F=(f(z),f(z+tau)) dz with
f(z)=theta_3(z|2tau)/sqrt(theta_1(z|tau)), fixing the second
component's square-root branch explicitly. Its numeric outputs
were not rerun. This profile is not newly discovered here.

After the fixed unitary frame change used in
[the theta repair](THETA_SEQUENCE_REPAIR_AND_MONODROMY_DUTY.md), use

    F(z,tau)=(i theta_2(z|2tau),theta_3(z|2tau))^T
                                      /sqrt(theta_1(z|tau)),
    v(tau)=(i theta_2(0|2tau),theta_3(0|2tau))^T,
    d(tau)=partial_z theta_1(0|tau).

Arguments have periods 1,tau. The square root and period paths are
retained. The preceding proof gives period continuations by plus/minus
i and plus/minus j, with puncture commutator -I. Choices of the
central period signs give equivalent quaternion coefficients through
fixed unitary conjugations; the map to a source's precise marking
must accompany that conjugation. Pointwise ||F|| is single-valued.

The [form-parent proof](../weave_form_parent_2026_10_08/PROOF.md)
already derives one holomorphic form per rho_Q coefficient on the
quaternion cover, hence three for the stated rank-six coefficient.
The [retained finite-distance spin proof](../surface_odd_form_2026_10_14/upstream_puncture_fredholm_PROOF.md)
separately identifies the upper extreme-domain kernel with the
holomorphic extension and gives three positive kernels and no
cokernel there. Those authored analytic results retain their own
hypotheses and pending specialist acceptance. They are not new
execution receipts or an identified common physical parent.

## Local behavior and the two different norms

At the puncture,

    F(z,tau)=z^(-1/2) v(tau)/sqrt(d(tau))+O(z^(3/2)). (1)

The preceding theta product proof establishes v!=0 and d!=0
on the upper half-plane. Thus its leading coefficient is nonzero.
There are no other singularities on the punctured torus.

For a flat unitary coefficient, the squared norm of the one-form
F dz in two real dimensions is conformally invariant, up to one
fixed positive convention factor. Define that reference norm by

    N1(tau)=integral_(E_tau) ||F(z,tau)||^2 dx dy. (2)

The integrand is asymptotic to C/r near zero, C>0. With area
r dr dtheta, the local integral is proportional to integral dr,
finite. Positivity away from the puncture gives N1>0. On the
double cover z=w^2, F dz has regular leading term
2 v(tau) dw/sqrt(d(tau)), in agreement with the existing cover proof.

For the ordinary positive spinor F sqrt(dz), a conformal metric
ds^2=Omega(z)^2 |dz|^2 instead gives, in the holomorphic spin frame,

    Nspin(tau,Omega)=integral Omega(z) ||F||^2 dx dy. (3)

Indeed the spin frame contributes Omega^-1 to its squared norm
and the area contributes Omega^2. This agrees with the source's
Omega^-1/2 conformal transport of a Cartesian spinor.

If Omega is smooth positive across the deleted point, (3) is finite.
Then (1) belongs to the upper extreme critical trace, not the lower
or minimal trace. With the retained analytic theorem and the stated
extending odd spin structure, the three equivalent copies give the
known extreme kernel. The formula is not a proof that this domain
or metric is selected.

At the complete hyperbolic cusp Omega=1/(r |log r|), (3) instead
contains integral dr/(r |log r|) and diverges. The profile is not an
ordinary-spin L2 mode for that operator. The one-form norm (2)
remains finite. This preserves BOTH existing results; changing
spin versus form type or the metric changes the actual problem.

## The integrated three-copy Gram

In the common flat coefficient frame, the rank-six bundle is
C3 tensor rho_Q. For the specified identical extreme domains
or the complete-cusp holomorphic-form realization, its three
sections are e_p tensor F. In the original parity frame they
are supported in separate blocks with unitary factors Q_p F.

If the common coefficient norm is the scalar one from
[the flat-metric compatibility proof](COEFFICIENT_METRIC_CONSTRAINTS_AND_PHYSICAL_PRICES.md),
their actual integrated Gram in this frame is

    K_pq=h N1(tau) delta_pq                       (4)

for forms, or h Nspin delta_pq for the finite-distance spinors.
This follows from the direct-sum supports and Q_p^dagger Q_p=I,
not a numerical inference from three eigenvalues. The common
geometry and domains are indispensable hypotheses.

The scalar function is a specified profile integral, not three
independently fitted weights. The overall coefficient/action
normalization h and geometry are still inputs. Modulus-dependent
non-scalar coefficient metrics, different domains or backgrounds
breaking copy equivalence are outside (4) and require their own
profile calculation. In particular this does not replace the
compact silver cover's different rank-five harmonic Gram.

For interactions with two such triplet slots, canonical normalization
rescales the raw matrix by common slot factors. It preserves rank
and singular-value ratios; arbitrary flavour hierarchies cannot be
inserted through a free family metric within (4). No prediction
of physical Yukawas is made without the actual field assignments,
interaction and all other kinetic slots.

Multiplying F by a nonzero scalar basis function c(tau) changes
its Gram by |c|^2 and the corresponding bilinear raw matrix by c^2.
With consistent canonical normalization their singular-value ratios
do not change. Such a representative choice is not automatically
an additional physical parameter. Changing the parent action's
relative couplings is a different operation.

## Modular covariance of the reference form norm

The explicit theta laws also fix useful consistency controls for (2).
On the previously chosen lifted generators l and s, the numerator
has respectively factors mu(l)g_l and
sqrt(tau) mu(s)g_s exp(pi i z^2/(2tau)). The standard theta_1
inversion law has factor -i sqrt(-i tau) exp(pi i z^2/tau).
Taking the continuous root with phase exp(-3 pi i/8) gives

    F(z,tau+1)=exp(pi i/8) g_l F(z,tau),
    F(z/tau,-1/tau)=exp(-3 pi i/8) tau^(1/4) g_s F(z,tau). (5)

The Gaussian factors cancel in the second formula. The theta laws
were read directly in [DLMF 20.7.26--33](https://dlmf.nist.gov/20.7#viii);
the level-two numerator law follows by splitting the even/odd sums,
as in the preceding repair. Full branch-root cocycles must still
be retained; (5) is not a proof of descent of every field to E.

Norms are independent of the central root sign. The transformed
area contributes |tau|^-2, while the squared coefficient factor
contributes |tau|^(1/2). Thus

    N1(tau+1)=N1(tau),
    N1(-1/tau)=|tau|^(-3/2) N1(tau).             (6)

Equivalently (Im tau)^(-3/4) N1(tau) is modular invariant.
Covariance alone does NOT determine its value or make it constant.
No closed-form integral or numerical normalization is claimed here.

## Matter normalization does not pay for the Higgs end law

The existing Higgs-channel fields S_r behave as 1/z. Their
squared norm has integral dr/r, and the source's boundary-class
norm contains the common logarithm plus finite channel terms.
Those are the objects in
[the end-norm transport analysis](GEOMETRIC_END_NORM_TRANSPORT.md).

F behaves as z^-1/2 instead. Its finite form norm requires no
arbitrary puncture cutoff. It is therefore wrong to charge every
matter normalization with the Higgs's logarithmic end freedom,
or to claim that a finite matter norm determines the Higgs end
condition. Ordinary-spin nonnormalizability at the complete cusp
is a third, distinct result, not repaired by choosing a finite cutoff.

The next duty is the SAME physical parent's identification of
these profiles as forms/spinors, its full field roster, actual
connection/domain and Higgs/background response. Equations (2)-(6)
remove an arbitrary flavour-Gram ansatz in the specified fibre
control, not the supplied physical dictionary or the end law.
The full goal, independent review and prospective admission remain
open. Frozen v2/v3 are unchanged; no input row is marked fully paid.

## Literature identification retained for the next source pass

There is a concrete external name for the cover used by the source:
the quaternion origami, or Eierlegende Wollmilchsau. Flake and Thevis,
[Strata of p-origamis](https://doi.org/10.1002/mana.202100290), section
2.1, constructs precisely the normal cover (Q8,i,j), with right
generator gluing, eight tiles and four cone points of angle 4pi
(Example 2.3). This matches the source cover's literal construction,
not merely its genus. Their Lemma 2.4 and Example 2.5 distinguish
changes of generating pair from a genuinely different origami.

Reading coverage here is the introduction and section 2.1's
construction/examples; the complete paper was NOT read and none
of its later theorems enters (1)-(6). Its Example 5.11 is a lead
for an inverse family above the quaternion cover, not an already
verified enlargement of the programme. Further Hodge/Prym and
Kontsevich-Zorich results require direct primary-source reading
and an actual profile/period comparison before use. No closed
norm formula follows from identifying the cover's established name.
Nor is this permission to promote that one cover into the whole
generated architecture or to infer physical spacetime from it.

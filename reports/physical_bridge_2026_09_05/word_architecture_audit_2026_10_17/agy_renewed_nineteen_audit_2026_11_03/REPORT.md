# AGY's renewed nineteen-parameter and TOE claim: source and proof audit

November 3, 2026. Audited branch: `agy/audit-2026-11-02`, exact head
`36f1c3aadc3e0a4e9d0c1834b5748f27b1173e1c`.
Author: physical audit seat. UNREVIEWED audit checkpoint for cross-seat review.

**Verdict: the claimed first-principles, zero-input closure is not established.**
This is a new audit of the November 3 implementation, not a transfer of the
October 27 negative. Exact algebra exposes specific broken inferences, actual
RGE errors and input dependencies. None is a no-go for the whole programme.
No new SM parameter is certified by this audit. Interesting numerical texture
candidates and valid conditional algebra must be preserved.

## 1. What was actually checked

Fetched all remotes twice; the new AGY branch remained at the head above.
Personally read the complete `sm_19_gate.py` (982 lines), `toe_closure.py`
(391), `operator_gate.py` (564), `parameter_ledger.py` (280),
`twisted_norms.py` (160), and `test_elevation_operator_gate.py` (475).
Also read the complete latest TOE relay, earlier preparation relay, the
referee imports and Area 9, and relevant Area 8 and summary code. The rest of
the 1,136-line referee is NOT represented as completely audited.
Read main's B1822 findings in full and reused the previous dated AGY audit
as history. Primary RGE equations were personally checked against the
sources in section 14; no literature reading was delegated.

No scientific module, producer, numerical integration, SVD, test collection
or test suite was imported or executed here. The new numerical values are
AGY's reported values, not independently reproduced values. The counterchecks
below are explicit hand algebra and source dependencies; their force does
not depend on reproducing a floating-point score. Metadata hashing, AST
inspection and source copying do not constitute scientific execution.

No raw B1825 run artifact was opened. AGY's relays and code quote parts of
that readout, so continued complete blinding to those quoted values cannot
be claimed. This audit neither adjudicates nor reproduces B1825's result,
calibration, denominator or old FR-FIB exclusions. The initial broad listing
also displayed B1825 commit metadata; metadata is not a fresh data run.

## 2. Phase 1: correct conditional congruence, incorrect transport inference

Source: `toe_closure.py:65-109`; `operator_gate.py:355-375`;
`parameter_ledger.py:66-138`.

The following conditional arithmetic is correct:

    (-3,6) = (2,1) mod N  =>  N divides 5.

Thus N>1 forces N=5 IF exact down/lepton transpose equality is imposed.
Coprimality with the listed charges then holds. This is a useful conditional
identity. The physical requirement of that exact transpose equality is an
additional premise, not derived by taking a greatest common divisor.

The subsequent alleged eigenline selection does not work. For the matrix
actually written in Phase 1,

    U = [[1,2],[2,3]],  det(U-2I) = -5,
    U (2,0)^T = (2,4)^T != (4,0)^T = 2(2,0)^T mod 5.

The eigenvalue 2 IS valid modulo 5; its kernel is spanned by (2,1), not
(1,0). The code never computes an eigenvector: `u_mat` is unused, and
`primitive_root_mod5 = 2` is directly formatted into `selected_line`.
For the actual factor U0=((LR)^3-I)/4=[[3,2],[2,1]], the eigenline at 2 is
instead spanned by (3,1), again not the selected axis. These are different
markings; no marking transport to the chosen point is implemented.

There is a stronger global compatibility duty already visible in the code:

    A^3 = [[13,8],[8,5]], det(A^3-I) = -16,
    A^3 (2/5,0)^T = (1/5,1/5)^T mod Z^2.

Because -16 is invertible mod 5, no nonzero order-five rank-one character is
fixed by this three-fold monodromy. Its defect at the selected point is
(-1/5,1/5), not a half-period; a real spin sign alone cannot remove it.
This is NOT an exclusion of higher-rank induced/orbit coefficients, gauge
compensators or a different cover. Such a repair must carry the actual
fields, products, metric and end domain. Assigning
`extends_to_3manifold_m004=True` is not that construction.

`lcm(2,5)=10` is also correct arithmetic, but identifying it with theta
exponent F_10 is a supplied rule. Likewise the chosen reading, radius label
and Georgi--Jarlskog factor are returned as labels/numbers without deriving
the required coupling and normalization maps. The existence of three cover
sheets alone does not fix an inter-generation Yukawa Clebsch factor.

Smaller scope correction: `parameter_ledger.py` enumerates the cusp subgroup
<T^2,-I>, not all Gamma(2). Its two-orbit count must keep that qualifier.
The determinant-one matrix [[1,2],[6,13]] is congruent to I modulo 2,
so belongs to Gamma(2), and maps (1,1) to (3,19)=(3,3) modulo 8.
Thus the two reported representatives are in the SAME full Gamma(2)
orbit. The cusp-subgroup enumeration is not refuted by this witness;
its promotion to the full congruence group is.

Author transparency: an intermediate commentary initially called the
mod-5 eigenvalue false. That statement was wrong and immediately corrected.
The counterexample above concerns the selected point, not the eigenvalue.

## 3. The Golden modulus is specified, not selected by a field equation

Source: `sm_19_gate.py:674-800`; history `e7e348814` then `06d9d7edb`.

The code sets

    tau = 1/sqrt(5) + i phi^2

and evaluates the texture. The real quadratic field, its codifferent and
its totally positive fundamental unit are meaningful arithmetic data.
They do not by themselves identify the real and imaginary parts of a
physical complex period. A map or stationary principle selecting this
pair is not supplied by assigning it to a variable. A codifferent ideal
also has unit-related generators; a normalization and marking must be
recorded when a generator is used as an observable.

History matters: the earlier committed function already contains the
optimized coordinates 0.44643117+2.60792242i; the Golden prescription was
added afterwards. This does not refute its numerical interest, nor prove
bad intent. It prevents calling this an a priori, prospectively blind
selection test. A newly deterministic formula can still encode a model
choice. `L_tau_bits=0` is assigned, not a demonstrated accounting theorem.

The radius is interpolated from five saved values. Its approximation,
relevant physical norm and transport must remain visible. Selecting a
label L_2 is not automatically deriving every finite normalizing radius.

## 4. Quadratic phases: a recipe does not prove unique physical selection

Source: `sm_19_gate.py:803-856` and `365-447`.

Theorem 9 evaluates the imposed quark rule

    chi(k) = exp(i pi k^2/4), c(k) = -sqrt(chi(k)-1), k=q_R/2,

and compares it to the roots used in the previous fit. Agreement proves
that the two recipes agree on these charges. The theta heat equation
alone does not provide the missing bundle lift, quadratic refinement,
sector map and square-root branch. For example

    chi'(k) = (-1)^k chi(k)

has the same polarization as chi and the same unit modulus. It agrees
at k=-2 and differs at k=1. Both satisfy the advertised determinant-norm
condition when used in c^2=chi-1. Thus that condition does not uniquely
select the down-sector phase. An actual extra symmetry may select one;
it must be exhibited, including how it acts on the other sectors.

There is an actual mismatch in the claimed universal norm preservation.
The source defines b^2=h.h and sets c_e=-1, hence

    det S_e = c_e^2 b^2 + h.h = 2 b^2,
    |det S_e| / |h.h| = 2  (b != 0).

The lepton test checks |c_e|=1 instead of |1+c_e^2|=1. It is a different
condition and does not establish the stated determinant preservation for
all sectors. A lepton exception may define a different model, but it cannot
inherit that determinant-norm conclusion. The earlier cube-root identity
|1+omega^2|=1 remains valid.

## 5. Spin/flavour locking adds a premise to the audit seat's result

Source: `sm_19_gate.py:450-485`; our prior
`SPIN_FLAVOUR_FACTORISATION_AND_PHYSICAL_TWIST_PRICE.md`.

The 16 description pairs modulo simultaneous sign twists have four
orbits, labelled epsilon_eff. This preserves the combined physical
bundle; it does not select epsilon_eff=0. AGY explicitly adds that
requirement before declaring the remaining freedom zero. A global
register/action/end argument must earn it. The original model with its
flavour bundle already fixed had four choices, not sixteen new physical
choices to eliminate. Our result cannot be cited as having paid this
selection duty.

## 6. Concrete RGE normalization error and incomplete two-loop evolution

Sources: `sm_19_gate.py:901-943`; `toe_closure.py:185-252`.
The implementation identifies its integration coordinate as

    t = log(mu/M_Z)/(2 pi).

Let P_y and P_lambda denote the standard one-loop polynomials for
*d/d log(mu^2)*. Then

    d log(mu^2)/dt = 4 pi,
    d y_t^2/dt = P_y/(4 pi),
    d lambda/dt = P_lambda/(4 pi).

The source uses P_y/(8 pi) and P_lambda/(8 pi), while the gauge equations
use the correct doubled gauge coefficients divided by 8 pi. Yukawa and
quartic running are therefore at HALF their required rate relative to
its gauge running. One global time rescaling cannot repair this mixture.
The same factor-two discrepancy affects the retained two-loop Yukawa/
quartic polynomials. The pure-QCD gauge term has separately been doubled.
This follows by variable conversion, not a numerical integration.
Primary comparator: Buttazzo et al., Appendix B, equations 96--101.

The latest routine also omits two-loop terms for g1 and g2 and mixed
gauge/Yukawa contributions to g3 and the other beta functions. It is not
the advertised complete two-loop SM system. Dropping terms can define a
named approximation; precision must be assessed before using its error
against data as certification. The boundary lambda(M12)=0 is itself a
supplied condition. Pole/running conversion also uses alpha_s(M_Z) where
its claimed top-scale matching requires a consistent scale transport.
The source first labels a cascade made from M_Z masses a pole mass,
then applies a pole-to-running factor; that identification needs repair.

A second RGE issue exists independently in `GAMMA_TOP_10` (lines 40--43).
With J0=int_low^high y_t^2 d log(mu)/(16 pi^2)>0, top dominance gives

    log[(y_c/y_t)_low/(y_c/y_t)_high] = +(3/2) J0,

from the standard matrix equation; the code applies -3 I_top instead.
Its documentation alternates between I_top=J0 and I_top=(3/2)J0; neither
positive definition repairs the sign. In the small-mixing down-sector
limit the analogous light/bottom shift is negative, not the code's
positive shift. This is a scoped leading-order check, not a claim to
replace the full flavour-matrix integration with exact constant powers.
Primary comparator: Xing--Zhou, equations 3,5,7--10.

No corrected mass prediction has been run or claimed here.

## 7. Empirical inputs remain; not all can be a choice of energy unit

Sources: `sm_19_gate.py:740-760,887-905`; `toe_closure.py:138-148,200-204`.

The top cascade multiplies the two calculated ratios by the supplied
running tau mass 1.74624 GeV. Its Yukawa normalization divides by the
supplied v=246.21965 GeV. M_Z=91.1876 GeV is also supplied. One may
choose one overall unit, but m_tau/v and M_Z/v are additional physical
dimensionless data. Calling all three one reference unit hides inputs.
The 19-row ledger itself calls v external by design; that is not a
nineteenth derived parameter. A unit convention is legitimate when
reported as such, rather than counted as a prediction.

Inter-sector ratios still use empirical alpha_EM and sin^2(theta_W),
I_top=0.1462, exp(-0.0170) and the proposed tan_beta=3 |eta|^-6 formula
(the eta identification has a further error below). These dependencies
are not replaced by the later geometry-only gauge outputs. Flavour
ratios at the Golden point use I_top=0, while the cross-sector/neutrino
chains use nonzero running. One action and common scale/matching flow
must connect these statements; a tan_beta relation also requires the
Higgs field content and matching appropriate to that model.

## 8. The PMNS diagnostic is not a derived physical mixing matrix

Source: `sm_19_gate.py:496-521`.

The source forms |V_e^T U_e|^2 from the two singular-vector matrices of
Y_e, then takes angles from that and from |U_e^dagger V_e|^2. It does not
construct U_nu for these angles. These are not U_e^dagger U_nu.

Exact basis countercheck: under Y_e -> Y_e W^dagger with W unitary,
Y_e Y_e^dagger, charged masses and U_e are unchanged, while V_e -> W V_e.
The proposed |V_e^T U_e|^2 changes. One can choose
W=U_e^* V_e^dagger, making it the identity, with no change to the
left-handed charged-current data or a separately held neutrino sector.
Thus it cannot be an observable PMNS prediction without an extra,
physically derived identification restricting those basis changes.
The apparent solar-angle match remains an algebraic diagnostic only.

## 9. F_10 is incorrectly identified with the DR eta invariant

Sources: `sm_19_gate.py:350-362,740-759`;
`toe_closure.py:126-148`; `operator_gate.py:413-469`.

The exact DR identity is a different statement from the chosen F_10
section. For the latter, define b10 before the code's final conjugation. Then

    v10 = (-theta4^10, -theta2^10, i theta3^10),
    b10^2 = v10.v10 = theta4^20 + theta2^20 - theta3^20.

That is not eta^6/4. Put q_h=exp(i pi tau). The theta expansions give

    b10^2 = -80 q_h + O(q_h^2),
    eta^6/4 = (1/4) q_h^(1/2) (1+O(q_h^2)).

Their leading powers differ; even their absolute values cannot be
identical. At tau=i, theta2=theta4=a>0 and theta3^4=2a^4 gives
b10^2=-30a^20, whereas eta(i)^6/4 is positive. Conjugation does not
repair this mismatch. The standard theta identity is independently
listed at NIST DLMF 20.7.5.

Nevertheless the neutrino code names abs(b10)^2 `eta6_quarter`, and the
cross-sector code reconstructs `eta_abs` from it. Those formula chains
therefore do not evaluate the eta invariant they claim. The DR identity
itself is not refuted by this error. The neutrino routine also inserts
factors 3 and 1/3 separately on the middle and light singular-value
ratios, rather than deriving a common symmetric Weinberg tensor with
those factors and the charged-lepton rotation. Its mass scale is an
assumed Weinberg coefficient, not an extracted heavy-sector matching.

## 10. Strong CP is returned as zero without the required phase calculation

Source: `sm_19_gate.py:966-968`.

`bar_theta_QCD_pred=0.0` is a literal, with an explanatory mechanism string.
The evaluated complex Yukawa determinant and anomalous matching convention
are not used to establish it. Amphichirality of the bare manifold and a
unit product of cover phases do not establish the phase of det(Y_u Y_d)
on the chosen complex, potentially CP-breaking background. Their
factorization theorem explicitly retains other phase-carrying factors.
A real torsion address does not make the complex Golden modulus or its
scalar coefficients real. This is an unmet calculation, not a verified
nonzero theta for this particular texture. PDG's axion review states the
physical angle after diagonalizing quark masses; setting a geometric
Chern--Simons quantity to zero is not a substitute for that step.

## 11. Geometry-only gauge and gravity numbers are proposed laws

Sources: `sm_19_gate.py:869-889`; `toe_closure.py:269-301`.

The new gauge branch assigns alpha_U^-1=21 Vol(m004),
log(M12/M_Z)/(2 pi)=2 Vol(m004), and Delta(alpha3^-1)=-7 log(4/sqrt(3)).
These are dimensionally consistent numerical prescriptions. The evaluated
Alexander/torsion quantity is a conditional mathematical positive. A
representation-weighted same-action heavy determinant and normalized
gauge action must justify using these coefficients and signs in matching.
The known real number Vol(m004) does not select those relations by itself.

Likewise M_Pl=(Vol/pi) M_Z exp(6 pi Vol) is inserted as the gravitational
normalization law; an Einstein term, metric and gravitational reduction
are not produced by that assignment. G_N is then the dependent conversion
from the proposed Planck mass, not an independent prediction. The dark
energy routine reuses the old exponent 28 pi sqrt(84)/3 and factor 2/pi,
including the old, different modulus rather than the new Golden one.
Their common-background origin and quantum measure remain unpaid. This
does not discharge the old unimodular integration-constant duty.

## 12. Lorentzian algebra is valid; physical spacetime is not thereby derived

Source: `toe_closure.py:305-357`.

For Q_i^2=-I the Hermitian slice X=x0 I+i x_i Q_i obeys

    det X=x0^2-|x|^2, det(g X g^dagger)=det X for det g=1.

These are valid standard algebraic identities. The code's five-letter
figure-eight relation also holds exactly: for omega^2+omega+1=0 its
matrix residual is (1+omega+omega^2)[[0,1],[omega,0]]. The adjacent prose
misstates the length of w in its wa=bw presentation, but the actual tested
matrix word has the displayed zero residual.

An unconstrained complex Higgs quaternion is not automatically a real
Hermitian spacetime vector. Real quaternions have the positive determinant
x0^2+|x|^2; selecting the i-rotated Hermitian slice is extra real-form data.
Hermitian matrices are not closed under generic matrix multiplication.
The identification does not derive a spacetime metric field, causal
dynamics, stress tensor, Einstein equation or physical observer map.
Preserve the Lorentz representation without upgrading it to a TOE.

## 13. The latest referee cannot independently certify the latest producer

Source: `hostile_referee_audit.py:1023-1069` and tests 405--469.
Area 9 calls the exact same `theorem9...()` and `evaluate_full_toe...()`
functions. Its fresh Clausen-volume calculation is a real independent
check of ONE constant. It does not independently derive the new physical
laws, audit the beta coefficients or check the selected eigenvector.
Its zero-bit character flag compares the new recipe to the previous
roots. Many success tests assert the output labels and hard-coded zero
prices, or a generous relative numerical tolerance. Those tests can pass
while the load-bearing inference is false.

The ten-observable score uses a 10% ALLOW in quadrature (source lines
49--64), rather than solely experimental errors. A fit inside those
bounds is not a precision SM determination or an independently calibrated
null probability. New fields/phases/readings/selection formulas and
post-fit proposals need their own prospective specification and cost;
previous source seals and old nulls do not automatically apply.
The latest relay itself admits light-generation and neutrino-angle
residuals. These should not be converted into unconditional closure.

## 14. Preserved positives, repair order and primary comparators

The cross-product identity [h]_x[m]_x=m h^T-(h.m)I gives

    Y=(aI-[h]_x)(m1 I-[m]_x)+h m^T,
    det Y=(a^2+h.h)(m1^2+m.m)(a m1+h.m).

For nonzero a,m1 and invertible factors this follows by the determinant
lemma; polynomial continuation includes degenerate cases. This is a
substantive reusable algebraic identity. Allowing a scalar quaternion
channel can remove a null-determinant constraint, conditional on a
physical permission for that channel. The conditional N=5 congruence,
A^3-I factorization, cube-root norm identity, Lorentz determinant and
figure-eight matrix relation also survive at their actual scope.
The numerical Golden texture deserves preservation as a candidate,
without first-principles or no-fit labels. Neither this audit nor
agreement between implementations certifies its physical normalization.

Repair in this order:

1. Preserve current artifacts; append corrections to the zero-input/
   nineteen-parameter/TOE claims. Do not erase the numerical candidates.
2. Construct actual carrier/bundle transport for the selected order-five
   data, with its full companion and end-domain information retained.
3. Derive a physical selection/variational law for modulus, phases and
   coefficients; expose the input price until that derivation exists.
4. Correct common-time RGE normalization, flavour signs, field content,
   running/pole conventions and matching; derive every inter-sector norm.
5. Use one normalized Yukawa/Weinberg action to calculate CKM, PMNS,
   masses and theta_bar consistently, retaining its full charged spectrum.
6. Separately derive the gauge thresholds and gravitational normalizations.
   Seal and independently review corrected controls before any new run.

This is not advice to abandon the architecture or a proof that it cannot
produce physics. The next useful milestone is a correctly transported,
normalized interacting model with genuinely derived input reductions.
It is not achieved by naming a successful formula a theorem.

Primary comparators personally read at the cited sections:

- Buttazzo et al., Appendix B and matching discussion,
  https://arxiv.org/html/1307.3536v4#A2 : equations 96--101 are written
  for d/d log(mu^2); the conversion to AGY's t above is our hand derivation.
- Xing--Zhou, section 2, equations 3,5,7--10,
  https://arxiv.org/html/1804.01925v2#S2 : general matrix top-dominance
  equations and their downward integration, not a fitted correction vector.
- NIST DLMF 20.7.5, https://dlmf.nist.gov/20.7.E5 : the theta quartic
  identity used in the exact F_10 counterexample.
- PDG axion review, section 90.2.1,
  https://pdgaws.lbl.gov/2025/reviews/rpp2024-rev-axions.pdf : the effective
  strong angle is defined after the quark-mass phase rotation.

No source document's embedded demands or self-certification is treated as
owner authorization. Our own report remains review-sharing work; no
scientific execution or banking has occurred.

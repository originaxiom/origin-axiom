# R24 — the actual sourced field has nonzero total mass-eigenline flux

**The global boundary charge is computed, not inferred from three assumed
Morse points.** In R15's specified positive-source class, with every cusp
incident to a source, the actual field obeys

    integral_(whole rounded boundary C) K = sign(q) * k.

Here k counts the prescribed proper source arcs, C is the source-excised
compact core, and K is R23's positive-mass eigenline Chern form with
the actual spin connection. Thus the existing three-arc construction
has total flux +3 at positive charge. This is the same signed net
chirality as R18/R19's conditional relative spectrum. The source
selection, singular-domain law and quantum boundary completion are
NOT consequences of this integer.

Original seal d304e2b0; source-informed equality control 833b939b.
No B number. [Design](GLOBAL_MASS_FLUX_DESIGN.md),
[prior and receiving scope](GLOBAL_MASS_FLUX_PRIOR.md),
[producer](global_mass_flux.py), [connection control](global_mass_flux_control.py).
This is a mathematical theorem for a specified source/cut class with
finite computational controls, not an independently reviewed physical TOE.

## 1. The bundle is the one in the actual operator

R23 exhibits U on even forms, with the kinetic and mass Clifford
actions on two different Pauli factors. R24 additionally transports
the natural Levi-Civita connection on exterior forms. In column
conventions, nabla e_j=sum_i e_i A_ij, A v=a cross v. The calculation gives

    U^dagger nabla_even U =
        d + Gamma tensor 1 + 1 tensor Gamma,
    Gamma = -i a.sigma/2,
    U^dagger mass U = 1 tensor (m.sigma).

The independent control constructs the exterior representation by
replacing each coframe factor, without the original creation/annihilation
connection routine. All three generators and the arbitrary coefficient
residual agree. Missing the second spin factor, reversing the sign,
and exchanging two connection components each fail exactly.

An oriented three-manifold admits a spin structure. For any fixed
choice, the equivariant local map therefore glues; it does not impose
a globally flat auxiliary spin bundle. Changing that spin structure
tensors each spin factor by the same flat sign line. The even tensor
product is unchanged and the eigenline curvature has the same
surface integrals. This does not determine a torsion determinant
phase or select the spin structure physically.

**An original instrument failure is retained.** The first routine
compared an expanded matrix with an unexpanded one using structural
equality. It returned false even though every entry of their
difference is identically zero. The original source and failing test
remain unchanged. The separately sealed control proves the exact
polynomial equality and rejects three wrong maps; no sign, unitary
or mathematical target was fitted after the failure.

## 2. The eigenline is minus the normalized secondary Euler form

Set n=grad(qF)/|grad(qF)| where the gradient is nonzero and
P=(1+n.sigma)/2. With f=da+(a cross a)/2, the arbitrary-connection
Pauli computation gives

    K = i/(2 pi) Tr[P F_Gamma + P(DP)^2]
      = n.f/(4 pi) - n.(Dn cross Dn)/(8 pi)
      = -Phi.

Nie uses row connection omega=-A and curvature Omega=-F_A.
Substituting those conventions into his n=3 expression yields the
last equality, including both factors of two from exterior products.
The identity is verified with arbitrary connection/derivative jets
on a stereographic chart; smoothness extends it to the other chart.

The standard theorem used here is: on an oriented compact manifold
with smooth boundary and a vector field nonzero there,
Ind(V)+Ind(partial_- V)=chi(C). The normalized secondary Euler form
has boundary integral Ind(V) in dimension three, because its exterior
derivative is the negative Euler curvature form, which vanishes in
odd dimension. It does not require a product boundary metric.
[Nie, equations (1.4), (1.5), (2.2)--(2.12), Remark 1.12](https://arxiv.org/pdf/0909.4754).

Controls independently integrate K to -1 on the outward unit sphere
in spherical and stereographic coordinates; mass reversal gives +1.
For the actual hyperbolic orthonormal coframe dx/z, dy/z, dz/z,
a=(dy/z,-dx/z,0) passes the torsion-free equation. On a horosphere
with n vertical, the two terms are +1/(4*pi*z^2) and -1/(4*pi*z^2):
K=0. Dropping either term produces a false nonzero answer. The
curved-frame cancellation is not optional normalization.

## 3. Why the corners do not erase or double the charge

Write T for the k source-tube annuli and E for the punctured exterior
cusp tori. Their 2k circular seams are retained. At a finite cap
z=Z, use a tube of constant Euclidean radius rho=epsilon and local
normal coordinates u=rho-epsilon, v=Z-z. The metric is conformally
Euclidean. For q>0, V=grad(qF) has normal-plane components (a,-b),
with a,b strictly positive. Its component along the seam is unrestricted.

Round using (u,v)=delta*(1-cos t,1-sin t), 0<=t<=pi/2.
The outward normal and the tangent from T to E give

    V.normal  = -a cos(t) + b sin(t),
    V.tangent =  a sin(t) + b cos(t).

For a frozen field the normal pairing crosses zero once, from
negative to positive, while the tangent pairing is strictly positive.
At the crossing its value is sqrt(a^2+b^2). Thus the tangential
field exits the incoming tube region. Reversing V also exchanges
the incoming region with the E side, so its outward tangent pairing
is AGAIN positive, not negative.

For the variable actual field we do not assume a/b is monotone.
At each fixed finite regulator, choose a sufficiently small collar;
the strict two-face signs extend into a positive cone there.
A collar-supported homotopy freezes the transverse coefficients
while staying in that nonzero cone. It preserves the eigenline
Chern number. After this homotopy the incoming region is a collar
extension of T for q>0, or E for q<0; in both cases its tangential
field points outward along its boundary. The ordinary surface
index theorem consequently gives chi(T) or chi(E).

One may perturb the interior and the tangential field generically,
fixed near the boundary of the relevant region, to define total
indices if zeros are nonisolated. This is an index-definition device,
not a claimed harmonic deformation or a physical critical-point
census. The preceding theorem now applies:

    integral_boundary K = -Ind(V)
                        = chi(incoming) - chi(C).

There is no uncounted corner contribution.

## 4. Annuli stay annuli; the core changes

The original compact core Q has only torus boundaries, so chi(Q)=0.
A regular neighborhood N of k proper arcs is k balls, with
C intersection N=T a union of annuli. Euler additivity gives

    0 = chi(Q) = chi(C) + k - 0.

Thus chi(C)=-k, chi(T)=0 and chi(E)=-2k. For the specified signs,

| charge | incoming piece | vector-field index | total K flux |
|---|---|---:|---:|
| q>0 | T, Euler 0 | -k | +k |
| q<0 | E, Euler -2k | +k | -k |

This is exactly why the smooth annular zero-index argument does not
kill this sourced construction. We did NOT turn the annuli into
discs or assume corners are disc vertices. We changed the domain by
excising actual prescribed sources. In the positive-charge convention,

    integral_boundary K = -chi(C,T) = chi(C,E) = k.

The cell controls rebuild the complete relative complexes on
(T^2 minus k discs) times I for k=0,1,2,3, with a second resolution
and height at k=3. Both charge signs and all Betti ranks agree.
They are product-model controls, not an identification of the actual
hyperbolic manifold with a product. General Euler additivity, not
that finite sample, establishes the all-k statement. A constant
field on a ball has a disc incoming region and zero flux, while
outward/inward radial fields give -1/+1; these controls reject
dropping a genuine disc's Euler contribution.

**A useful corollary:** for k>0, the actual gradient must vanish
somewhere inside every admissible core. Otherwise n and the closed
form K would extend over that entire core, contradicting Stokes and
its nonzero boundary integral. If the actual field is Morse, the
signed sum forces at least k nondegenerate critical points. Neither
Morseness nor exactly k points is proved; no individual mode has
been assigned a critical-point location.

## 5. The total integer survives the complete exhaustion

This uses R15's actual asymptotic construction, not a chosen mass map.
On each high cusp,

    F = U(w) + exp(2s)*(b*s+c) + v,       b=pi*Q_cusp/A > 0,
    exp(-2s) partial_s F =
        2*b*s+b+2*c + exp(-2s) partial_s v.

U has no s dependence, including when w approaches a puncture.
The smooth L2 corrector is harmonic on the whole high torus; its
constant/decaying Fourier expansion gives a bounded partial_s v.
If |c|<=C and |partial_s v|<=D, take s>=0 and
s>=(2*C+D)/(2*b), also above the geometric/Fourier cutoff.
The scaled derivative is then at least b>0, uniformly in w.
Thus every sufficiently high cap has the required outward sign.

At any fixed finite cap height, subtracting beta*log(rho) at a
source leaves a smooth regular part. Bound its radial derivative
by B on the relevant compact collar. Choosing
rho<=beta/(B+1) gives partial_rho F>=1. Compact tube portions have
the corresponding logarithmic estimate; matching tube shapes can
be chosen sufficiently small. Finally choose the rounding collars.

The order matters: high caps first, then sufficiently small tubes,
then corners. A fixed radius need not dominate an error bound
growing with height. The producer retains that counter-control and
the failure of the cap-sign inference when b=0. A cusp without
a source endpoint is outside the stated positive-sign theorem.

Every such deep regulator has the SAME total integer. This proves
the total topological exhaustion value; it does not prove convergence
or independent quantization of every open face's integral. The
finite homogeneous through-flux coefficients change safe cutoff
heights, not this class. Arbitrary positive source strengths give
the same class, but its comparison with the complete Hilbert kernel
uses R18's additional strong-maximal-domain hypothesis |q beta_a|>=1.

## 6. The physical join, and what has not been supplied

For the R19 charged sector, the boundary coefficient is now
computed from the actual global field: k times the actual H-spinor
anomaly polynomial. At k=3, the root-derived linear and cubic U1
traces are both 48, not zero. This agrees with the net relative
index independently of the trivial/Alexander-exceptional vector-like
pair. It does not turn one charge sector and its conjugate into
two independent determinants.

R23's descent retains the outer term. With an internally constant
gauge parameter, outer coefficient k equals the total local
coefficient k, so the bulk variation is zero and the net anomaly
remains. This round computes the required total boundary response,
not a quantum sector carrying its opposite. For general external
families, R23's full degree-eight eigenbundle expression, including
higher K powers and the regulator term, remains necessary.

Closing sentence for this sub-duty:
"Within the specified positive-source class, the actual global
mass-eigenline boundary charge equals the signed relative index,
including all rounded seams and the complete topological exhaustion."

PB-BOUNDARY remains OPEN. The immediate next task is an actual
source/end action and domain supplying the compensating anomaly
response, or compatible massive-gauge-field dynamics, with its
effect on the charged spectrum checked. Separate cusp/tube phases,
a global eta/Pfaffian regulator, finite-action defect completion,
source/holonomy selection, Spin(10)-to-SM breaking, a controlled
neutral-sector 4D limit and gravity remain distinct duties.
The theorem works for k, not only three: it is NOT a three-family
selector. The claimed full TOE has not been achieved.

Fresh all-head intake also brought outside memo 192, which confirms
the earlier E7-to-E6 scope correction. Its rank-grading U1 observation
does not prove that every completion must retain a massless U1;
R21's conditional Higgsed EFT and R22's same-source qualification
are both preserved. Other fresh numerical claims are not recertified
by this round. See the prior receipt for exact scope.

## 7. Verification and custody

Both native producers completed with their full JSON preserved:
the original in 9.388 s, the exact connection control in 0.254 s.
The original JSON's false comparison is NOT relabeled as a pass.

| completed run | passed | failed | errors |
|---|---:|---:|---:|
| first R18--R24 selection, including original R20 locks | 110 | 7 | 0 |
| R23/R24 with the separately sealed connection controls | 41 | 1 | 0 |
| 45-file expanded regression | 326 | 14 | 8 |

The first selection includes six old R20 transfer failures plus
R24's raw matrix-comparison failure. The second retains only that
raw comparison as a failure. All four new exact control tests pass.
The expanded run's 22 failed/error IDs equal R23's prior 21 plus
that one identified original comparison; none disappeared. Runtime:
266.80 s. The tree remained read-only throughout each certifying run.

Receipts: [first focused run](GLOBAL_MASS_FLUX_CHECKS.txt),
[separate-control checks](GLOBAL_MASS_FLUX_CONTROL_CHECKS.txt),
[complete expanded regression](GLOBAL_MASS_FLUX_REGRESSION.txt).
Public pytest captures redact environment prefixes; full original
stdout is also retained locally outside the worktree. Scientific
JSON is preserved without substitution. No original source, test,
tolerance or first failure was rewritten.

This is not full-repository green or independent proof acceptance.
The metadata prechecks confirm both new designs have the literal
provenance markers and all 57 registered design digests match.
Reporting governance and final custody are recorded separately in
GLOBAL_MASS_FLUX_GATES.txt and BANKING_RECEIPT.md; old failures are
not waived. Current reader surfaces, the scoped law index and the
open completion duty are updated. No main merge or external relay.

Reporting governance completes with 27 PASS / 3 FAIL, the same
attribution, old delegation-lock and old provenance-marker findings
as R23. The new path/reference/law and design-digest checks pass.
No governance baseline was changed to obtain this result.

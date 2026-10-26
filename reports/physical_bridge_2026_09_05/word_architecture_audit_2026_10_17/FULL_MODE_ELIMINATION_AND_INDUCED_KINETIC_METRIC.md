# Eliminating the actual complement also determines the retained mode norm

October 26, 2026. Authored conditional analytical continuation,
UNREVIEWED. No scientific import, symbolic evaluation, test collection
or numerical producer run. This is not an admitted effective theory,
new family count or derivation of a physical parent from genesis.

## Named reduction duty and existing work

After a full operator, its actual mode projection and domain are fixed,
is a separate freely adjustable retained kinetic Gram still required?
The target is the norm of reconstructed states, not an arbitrary
positive metric chosen for a desired hierarchy.

Reuse [the previous joining analysis](EXTERIOR_RESPONSE_AND_JOINING.md):
it already derives the static Schur complement and explains why a
singular complement needs retained kernel variables. Reuse the
[constant-tail response/norm](ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md):
its energy derivative already retains exterior normalization. These
are not new discoveries of this note. The extension here is the actual
surface-mode decomposition, its induced norm and the grading constraints.
No claim of general Schur/Feshbach novelty or repository absence is made.

Personally read the full surface_mode_transport, surface_odd_form,
surface_weak_completions and surface_even_channels source proofs, the
FULL_EVEN_PROOF, and the byte-preserved upstream_horizontal_projection
proof under surface_odd_form_2026_10_14. The last explicitly derives
bounded [D,P], domain preservation and bounded off-diagonal B, while
warning that B need not map into Dom(D_V). Their analytic/global
admission qualifications are retained. No old producer was rerun.

## Actual operator hypotheses, not a vertical inverse substitution

Suppose the specified parent has its OWN admitted selfadjoint operator
D on a Hilbert bundle, with physical positive norm and fixed domain.
Let P be its actual orthogonal vertical-kernel projection, Q=I-P.
Assume P preserves Dom(D) and [D,P] is bounded, as in the source's
conditional construction. Write

    D=[[A,B dagger],[B,C]],
    A=PDP, C=QDQ, B=QDP.                                  (1)

Subtracting the bounded selfadjoint off-diagonal part gives legitimate
selfadjoint diagonal blocks on P Dom(D) and Q Dom(D). B is bounded
between the two Hilbert spaces. C is the TOTAL complementary operator,
including horizontal derivatives, mixed connection and the actual
critical-domain law. It is not D_V restricted to its complement.

Fix a real interval I in the RESOLVENT set of this C and put
R(lambda)=(C-lambda)^-1 for lambda in I. This spectral admission is
an essential hypothesis. The source's growing tail estimate or a
vertical spectral gap alone is not a proof of this global inverse.

## Reconstruct the eliminated fields and retain both energy and norm

The complementary equation of (D-lambda)(x,y)=0 is

    y=-R(lambda) Bx.

Define the full reconstruction and reduced spectral pencil

    J(lambda)x=(x,-R(lambda)Bx),
    F(lambda)=A-lambda-B dagger R(lambda) B.               (2)

For x in Dom(A), J(lambda)x is in Dom(D), since R maps into Dom(C).
Direct substitution gives

    (D-lambda)J(lambda)x=(F(lambda)x,0).                   (3)

Thus ker F(lambda) and ker(D-lambda) are in bijection by J(lambda).
Neither a complement field nor a conjugate mode is thrown away.
The exact retained norm is

    ||J(lambda)x||^2=<x,N(lambda)x>,
    N(lambda)=I+B dagger R(lambda)^2 B >= I.              (4)

The resolvent inverse identity yields R'=R^2, hence

    -F'(lambda)=N(lambda).                               (5)

The unbounded A has a common domain and cancels from differences;
all derivatives in (5) are bounded there and extend boundedly to PH.
For two real parameters the exact form is

    F(lambda)-F(mu)
      =-(lambda-mu) J(mu) dagger J(lambda).                (6)

Equation (4), direct reconstruction, independently checks the sign.
The minus in (5) is not a negative physical norm: F uses D-lambda.
The inverse-propagator convention lambda-D has the opposite sign.
This also differs in convention from the previous boundary Weyl M,
whose derivative is positive. One must not combine their signs by name.

If the actual distance from lambda to sigma(C) is at least delta>0,

    0 <= N-I <= ||B||^2/delta^2 I,
    ||B dagger R B|| <= ||B||^2/delta.                    (7)

These bounds require the ACTUAL inverse with its domain and remote
conditions. Substituting the growing vertical gap for delta would
repeat the source's already identified error. In particular, the
fact that Bx is not in Dom(D_V) does not invalidate (2)--(4): the
bounded B first gives an L2 source and the actual R maps it into
Dom(C). No divergent vertical derivative of Bx was taken.

## Zero modes, continua and the verified end qualifications

A compact-resolvent C can have bound-state zero modes even when its
end is confining. At an isolated complementary eigenvalue lambda0,
enlarge the retained space by its finite eigenspace before using (2).
The other complement then has an inverse in a sufficiently small
spectral interval. Do not replace R by a pseudoinverse and delete the
kernel: the old joining note's compatibility equations still apply.

If zero belongs to complementary essential spectrum, retaining only
the kernel does not repair the inverse. The rechecked ordinary n=0
even Weyl sequence is precisely such a warning when that sector is
put into C. Its nonzero fixed-frequency thresholds cannot substitute
for an inverse uniform over the Fourier population.

The canonical parent's old positive even-end bound removes that
particular obstruction; the odd total-complement estimate and actual
mode transport have their own conditions. None proves absence of
all core eigenvalues or supplies the global pointed domain. The
conditional Fredholm result must not be reported as automatic
invertibility. If an admissible low-energy complement is obtained,
(2)--(7) apply to it, with all newly retained modes included.

## A sharper odd-sector consequence: its induced correction dies at the end

The source's admitted ODD total C has compact resolvent under its
growing-tail and local-domain hypotheses. At a real lambda in its
resolvent set, R is therefore compact. Since B is bounded,

    B dagger R B is compact,
    N-I=(R B) dagger (R B) is compact and nonnegative.     (7a)

Let chi_T be a bounded scalar cutoff on the retained base bundle,
supported farther and farther into the cusp. It commutes with the
fibrewise P and tends strongly to zero on PH. Then

    ||R B chi_T|| -> 0,
    ||chi_T (N-I) chi_T|| -> 0.                           (7b)

For completeness, approximate the compact K=RB in operator norm by
a finite-rank sum of maps |u_j><v_j|. Each right product with chi_T
has norm bounded by ||u_j|| ||chi_T v_j||, tending to zero. The
uniform cutoff bound controls the approximation error. The second
claim follows by squaring the first. It is not obtained by replacing
the total resolvent with a vertical inverse or imposing an arbitrary
condition at a finite-height cut.

Thus in this admitted odd block an arbitrary new asymptotic kinetic
weight cannot be inserted while claiming the same reconstructed
operator. Its exact finite-core correction can remain nonzero and
depends on the actual resolvent. There is no rate in (7b), no
pointwise local matrix formula and no derived physical hierarchy.

This compactness conclusion is NOT transferred to every E8 direction.
The regular even source proves a positive essential end gap for the
canonical parent, not compact resolvent of its entire complement.
There (4)--(7) still require their own admitted inverse, and a finite
bound does not prove (7a)--(7b). The full nonlinear E8 interactions
also couple the parity sectors; the free-background block split is
not a new truncation of that theory.

## A static trace does not retain the induced metric

As an elementary instrument control, take the two-dimensional
selfadjoint matrix

    D_c=[[1,sqrt(c)],[sqrt(c),c]], c>0,

with the first component retained in its fixed measuring coordinate.
At lambda=0 every c has F(0)=0, but

    J(0)=(1,-1/sqrt(c)), N(0)=1+1/c.

For c=1 and c=4 the norms are 2 and 5/4 despite the same static
reduced equation. Their other eigenvalues are 2 and 5. These are
direct two-by-two identities, not executed controls or OA vacua.
As c tends to zero, the normalized zero mode's retained amplitude
tends to zero while its full state survives in the complement.
The divergent norm signals a failing elimination chart, not a ghost
or a theorem that a physical particle disappeared. At c=0 the
complementary kernel must be kept.

## Original grading and registered covariance survive legitimate elimination

If D anticommutes with its original chirality Gamma, P commutes with
Gamma and the domains respect it, let Gamma_P and Gamma_Q be the
restrictions. At zero, assuming C invertible,

    {A,Gamma_P}=0, {C,Gamma_Q}=0,
    Gamma_Q B=-B Gamma_P.

It follows directly that

    {F(0),Gamma_P}=0, [N(0),Gamma_P]=0,
    Gamma J(0)=J(0) Gamma_P.                              (8)

Thus reconstruction and the positive N(0)^(-1/2) normalization
preserve the inherited grading. Where the required chiral Fredholm
realizations exist, the graded zero-mode difference is unchanged by
eliminating this invertible complement. No new chiral sector is
created by naming a projected slot plus or by changing its norm.
This statement does not select a physical boundary domain or equate
chirality with an unrelated cohomology degree.

N^(-1/2) is a bounded invertible Hilbert-space change, but it has not
been shown to preserve Dom(A). A normalized effective operator must
carry its TRANSPORTED domain and all action/trace pairings. Neither
positivity nor compactness in (7a) licenses leaving an unbounded
operator's domain fixed by assumption. The grading assertion uses
that transported domain and the actual reconstruction, not an
unproved commutator estimate for A and N.

Likewise, a full unitary registered transport which intertwines D,
its domain and P transports A,B,C,R,F and N together. A change of
frame cannot leave a separately fitted N behind. The source earns
this statement for its actual cusp transition; it does not establish
every global based move. An arbitrary coefficient intertwiner alone
is insufficient for this operator/domain covariance.

## Before/after input account and physical limits

Given the full parent/operator/domain, actual projection and an
admitted complement inverse, the retained kinetic NORM in (4) is a
derived dependence, not another independent matrix. In a physical
mode expansion of that same parent it must contribute to canonical
normalization. Interpreting lambda as a four-dimensional mass/energy
still requires the parent's actual separation and kinetic map.

The data supplying D, P, its global spectrum and inverse are not
derived here, nor is the common action coefficient of card 01 fixed.
The result is classical/quadratic. Full effective vertices require
solving the nonlinear complementary equations with their product
integrability and domain conditions. A projected cubic alone cannot
replace that task; no loop corrections or anomalies are computed.

Finally F(lambda) is an energy-dependent spectral pencil and can be
nonlocal on the base. The common-Clifford argument applies to the
FULL parent principal symbol. It must not be imposed afresh on F
while discarding its response and induced norm, which would change
the reduced theory and potentially hide the eliminated information.

The next concrete reduction duty is to derive/admit the actual
mode-bundle map and inverse on one retained physical construction,
then reuse (4) rather than supply a flavour Gram. Independent proof
review and any separately sealed executable controls remain owed.
No frozen verification source, review, admission or input ledger changed.

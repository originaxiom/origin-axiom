# What kinetic normalization can change in the weight three coupling

October 18, 2026. Analytical intake of the owner's parameter-audit
report and a derivation of its normalization duty. Positive invertible
kinetic normalization preserves rank and the determinant phase in the
stated transpose-bilinear convention. It can substantially change
nonzero singular-value ratios. Consequently a derived profile metric
could change the earlier numerical flavour test, but a freely chosen
metric would add enough freedom to erase its predictive content.

## Evidence and the actual scope of the report

The owner supplied the complete text at
`/Users/dri/.codex/attachments/8b13209e-ffa1-4122-9e65-3f4444e3522f/Pasted text.txt`.
Its old source pins are main `6c148ddd4` and SM `6877cc87d`.
Current inspected pins are main
`2e5716bd9bea013d69f3cd733f083b61a6f59dbd` and SM
`11ec0144ef25e8848968b909735c205809567fdf`.

The current SM `W53_RULE.md` was read completely, together with the
form normalization/objective definitions in its producer and the
relevant stored control and post-hoc records. They confirm the stored
quark-only objectives 41.358238929833945 and 1873.0131908551518,
the failed M0(e) aggregate, and the omitted (3,3,5)/(3,3,7) assignments.
These are source/output checks, not new optimization runs.

The report's independent scripts, refined fit outputs and comparison
runner were not supplied with its text and were not located in the
current workspace search. Their quoted refined values and numerical
error bounds remain received claims. The report itself discloses an
uncommitted exploratory design rather than a banked experiment.
The exact polynomial argument below is independent of those runs.

The current B1635 findings and the paper's modular-section source
preserve the dependence on weight, hand and ansatz. In particular the
weight-one golden spectrum at i is not a weight-three full-rank result.
Neither a failed optimizer search nor a failed aggregate classification
is promoted to exclusion of the whole generated architecture.

## The determinant identity does not need a theta reduction

Use exactly the report's raw forms, with symmetric upper entries

    a=-w(u^2+v^2), b=v(u^2-w^2), c=u(v^2+w^2),

and antisymmetric upper entries d=w^3,e=v^3,f=u^3. The diagonal is
zero. Direct expansion for arbitrary a,b,c,d,e,f gives

    det(S+rA)=2abc+2r^2(-aef+bdf-cde).             (1)

Odd powers cancel between the two nonzero determinant permutations.
Put x=u^2,y=v^2,z=w^2. The coefficient identity needed here is

    (x+y)xy+(x-z)xz-(y+z)yz
       =(x+y)(x-z)(y+z).

Expanding the right side gives
x^2 y+x y^2+x^2 z-x z^2-y^2 z-y z^2, exactly the left side.
Thus -aef+bdf-cde=-abc, and

    det(S+rA)=det S (1-r^2),
    det S=-2uvw(u^2+v^2)(u^2-w^2)(v^2+w^2).       (2)

This is an identity for arbitrary complex u,v,w, stronger in algebraic
scope than requiring v^2=u^2+w^2. Its interpretation as weight-three
couplings still requires the report's theta and representation inputs.
The equality theta_2(i)=theta_4(i) then makes every raw matrix singular
at tau=i. For generic tau, r=+1 or -1 also gives singular matrices.

W53 instead normalizes its two forms separately. If

    Y=e^c(S/||S||+rho A/||A||)=alpha(S+r A),

then alpha=e^c/||S|| and r=rho ||S||/||A||. The raw cancellation
values r=+/-1 correspond to rho=+/-||A||/||S||, not automatically
rho=+/-1. This conversion needs the same relative basis normalization
and sign as the actual branch forms. Equality of singular spectra alone
would not establish the left mixing convention.

## Derive the normalization from a fixed kinetic form

For two columns of independent left-handed fields take kinetic matrices
K_L,K_R positive Hermitian, and transpose bilinear psi_L^T Y psi_R.
Put psi_L=L psi_L,c, psi_R=R psi_R,c with the positive roots

    L=K_L^-1/2, R=K_R^-1/2,
    Y_c=L^T Y R.                                  (3)

Then L^dagger K_L L=R^dagger K_R R=I. The transpose in (3) belongs
to this declared bilinear; a barred-left convention has its corresponding
different written formula. Physical comparisons must keep one convention.

Both matrices are invertible, so rank(Y_c)=rank(Y), exactly. Furthermore

    det Y_c=det Y / sqrt(det K_L det K_R).          (4)

The denominator is real and positive. Thus positive canonical
normalization alone leaves arg det Y unchanged wherever it is defined.
Subsequent anomalous rephasings must be tracked together with the
topological angle; they are not a mechanism supplied by (3).
The report's plus-sign strong-angle convention and the paper's minus-
sign convention must be reconciled with the field/action definitions
before comparing their written formulas. No strong-CP conclusion is
inferred just from matching the word determinant.

Equations (2)--(4) show that a nonsingular kinetic metric cannot lift
the exact zero at i or r=+/-1. A singular or divergent metric is outside
the hypothesis and needs an actual Hilbert-space/domain analysis; it
cannot be used as an ordinary normalization at that point.

## Quantifying the possible change in a hierarchy

Let s_j be singular values in decreasing order and kappa the spectral
condition number. Invertibility and the singular-value min-max bounds
give for P Y Q

    s_min(P)s_min(Q)s_j(Y) <= s_j(PYQ)
                              <= s_max(P)s_max(Q)s_j(Y).

For (3), the factor kappa(P)kappa(Q) is

    C=sqrt(kappa(K_L) kappa(K_R)).

Therefore every nonzero ratio obeys

    (s_j/s_1)/C <= s_j(Y_c)/s_1(Y_c) <= C(s_j/s_1). (5)

For example the weight-one floor s_2/s_1>=1/2 becomes the conditional
bound s_2(Y_c)/s_1(Y_c)>=1/(2C). A result obtained with minimal kinetic
terms does not extend to all positive metrics without controlling C.
Conversely a smooth bounded metric with bounded inverse preserves the
order of a simple singular-value zero near r=+/-1, since (5) bounds it
above and below by fixed multiples of the original value.

A free metric can remove the mass prediction entirely in an isolated
invertible sector. For any positive diagonal target D, choose

    K_R=I, K_L^T=Y D^-2 Y^dagger.

This K_L is positive Hermitian. Equation (3) gives
Y_c^dagger Y_c=D^2 by direct inversion, hence exactly the desired
singular values. This construction is a diagnostic of supplied freedom,
not a legitimate prediction or a derived metric. In a full model the
same quark-doublet metric appears in both up and down sectors, so this
isolated-sector observation cannot be counted as an independent metric
fit for each sector or as proof every CKM matrix is achievable.

## The metric and coupling must come from the same modes

For actual modes s_a on an admitted domain the kinetic matrix is the
profile Gram

    K_ab=integral_X <s_a,s_b>_kinetic dvol
                         + any derived boundary kinetic contribution.

Its measure, bundle metric and boundary terms are those of the same
action. The physical cubic is that action's trilinear evaluated on
those same modes. Their simultaneous basis changes transform both
K and the tensor; they do not generate new physical hierarchies.

The existing [connected-cover cubic](../silver_cover_cubic_2026_10_12/PROOF.md)
already reduces a class of overlaps to a boundary Stokes expression
with both sheets and their relative factors retained. Its full proof
was read directly. It explicitly leaves profile Grams and normalized
strengths uncomputed. An invertible Gram preserves whether the complete
trilinear tensor is zero. It can change entries and their magnitudes;
the different rank-five cover tensor must not be substituted for the
weight-three modular ansatz without an actual field map.

The new [theta/end transport](GEOMETRIC_END_NORM_TRANSPORT.md) gives
another part of this duty: norms require transport of the cut and
remain sensitive to physical end prescriptions. The
[exterior response](EXTERIOR_RESPONSE_AND_JOINING.md) specifies how
eliminating an admitted exterior feeds back through the same action,
with its kernel constraints retained. Neither construction yet provides
the complete physical profile Gram for W53's matter fields.

The concrete next calculation is thus one admitted global field/domain
construction's Gram and full overlap tensor, followed by (3) and a
properly scoped comparison. Its mode/bundle/action map to the modular
forms, if claimed, must precede using those forms as physical Yukawas.
Adding a freely fitted metric or higher-weight coefficients would
supply further input rather than discharge this duty.

This note is an analytical checkpoint pending separate review. No
optimizer, symbolic algebra producer or experimental control has run.
The frozen v2/v3 packages remain unchanged. A sealed successor needs
raw/normalized coefficient conversion, rank and phase controls,
metric condition bounds and shared-left-metric countercontrols.

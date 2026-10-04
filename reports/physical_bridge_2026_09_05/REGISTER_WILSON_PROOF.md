# From a formal register to Wilson characters

Authored pre-execution argument, October 4, 2026. These are standard
compact-group facts and exact representation identities applied to the
existing supplied model. Finite controls do not prove physical admission,
derive a quantum measure, or replace independent review.

## The operational connection

For a compact group K and connection A, holonomy on a closed based loop
transforms by conjugation under a gauge transformation. Consequently
W_R(gamma,A)=chi_R(Hol_gamma A) is gauge invariant. Its definition is
separate from any expectation value or coupling to a measuring apparatus.
This is the standard Wilson construction described by John Baez,
[Week15, May23 1993](https://math.ucr.edu/home/baez/twf_html/week15.html),
personally read in full. Only that elementary definition is imported;
none of the article's quantum-gravity proposals is adopted.

For unitary irreducible representations, character orthogonality gives

    integral_K chi_R(g) conjugate(chi_rho(g)-chi_rho*(g)) dg
       = mult_rho(R)-mult_rho*(R),

with normalized Haar measure. One proof averages a rank-one operator
between representations over K; the resulting intertwiner is zero for
inequivalent irreducibles and scalar for an equal irreducible, with the
trace fixing its normalization. Extending by direct-sum additivity gives
the equation. This realizes B871's Kronecker contraction at the compact
group-character layer. The integration ranges over the whole group,
not over a predicted distribution of physical loop holonomies. A single
Wilson value is NOT the integer register and can vanish in a chiral R.
The group Haar projector is NOT the Born rule or a functional-integral
measure. Stage-internal SU3 level-two realization remains distinct.

In this existing model K=SU5 is the retained gauge factor of the actual
E8 roster. Its individual subgroup injection follows from the root
center kernel (z,z^-2): fixing either factor to1 forces z=1. The quotient
does not grant (10,1) as a representation of the whole product. Gauge
SU5 characters are used only after the supplied residual-gauge framework
has been declared. No full-E8 gauge-invariant chirality operator or
genesis-derived gauge choice follows automatically.

## Exact integration on the torus

Write z1...z5=1. The Weyl integration formula for a class function F is

    integral_SU5 F = (1/120) CT_T [F(z) Delta(z) Delta(z^-1)],
    Delta(z)=det(z_i^(j-1))_(i,j=1..5).

CT_T keeps exponent tuples that are equal in all five coordinates, or,
equivalently, exponent zero in four determinant-one torus coordinates.
The native producer builds the determinant from120 signed permutations,
forms its integer Laurent density and evaluates all character Gram
entries. This checks the normalization rather than inserting a Kronecker
answer. Representation weights come from the pinned R87 pure helpers;
the complete roster is first compared with the actual240 roots and
eight zero Cartan weights.

The separate finite-field evaluation computes Delta(z)Delta(z^-1) as
the product over pairs (zi-zj)(zi^-1-zj^-1). Its characters use
chi10=((sum zi)^2-sum zi^2)/2 and chi24=chi5 chibar5-1, independently
of the native weight enumeration. Grid averaging projects to the
constant term modulo53. For these Gram entries each original z exponent
has magnitude at most6 (density4 plus two character factors at most2
in total); subtracting the fifth coordinate bounds each determinant-one
exponent by12. Order13 therefore has no nonzero multiple13 alias. The
normalization120 is invertible in F53. This confirms modular outputs;
the integer native calculation and analytic argument are still needed.

The R=10+bar5 registers are +1 at10 and -1 at5, reversed for R*.
For two copies each of10,bar10,5,bar5, every odd register is zero.
The latter matches R85's supplied paired dictionary, without claiming
its cohomology or physical fermion interpretation has been rerun here.
The R40 signed algebraic index and opposite sign convention cannot be
promoted to physical handedness by this character calculation.

## Anomaly cancellation does not erase a chiral character

Let h=diag(h1,...,h5) be traceless and p_j=sum h_i^j. The ten weights
are hi+hj for i<j; bar5 weights are -hi. Therefore

    tr_10 h^n = 1/2 [sum_(k=0)^n binom(n,k) p_k p_(n-k) - 2^n p_n].

Here p0=5 and p1=0. It follows that

    tr_(10+bar5) h = 0,
    tr_(10+bar5) h^3 = 0,
    tr_(10+bar5) h^5 = 10 p2 p3 - 12 p5.

The cubic identity is the familiar SU5 anomaly cancellation already
checked in R40. It is not a proof that the representation is self-dual.
The quintic identity is nonzero: at (1,1,1,1,-4), p2=20, p3=-60,
p5=-1020, so the fifth moment is240. For g=exp(i epsilon h),

    chi_R(g)-chi_R*(g) = 2i sum_(n odd) (-1)^((n-1)/2)
                                      epsilon^n tr_R(h^n)/n!.

The fifth term is the first possible nonzero odd term in this example;
its coefficient on the stated direction is4i. This is a character's
holonomy Taylor series, NOT a fifth spacetime-derivative physical
operator. Along special h even the fifth moment can vanish. In the
balanced representation every odd coefficient vanishes. In 10+5 the
cubic moment is2 p3, providing the opposite anomaly control.

At the unitary holonomy diag(z,z,z,z,z^-4), z a primitive seventh root,
the character is6z^2+4z^-3+4z^-1+z^4. Subtract its inverse-holonomy
character and reduce modulo Phi7=1+z+...+z^6. The result is

    -4 - 8z + 2z^2 - 9z^3 + z^4 - 10z^5,

nonzero since Phi7 is the minimal polynomial of z over Q. The holonomy
is unitary with determinant1; this is exact, not an unverified numerical
CS witness. Reversal negates the value. It is a test fixture, not a
selected universe holonomy or a parameter prediction.

## Detecting and sourcing remain different operations

B599 counts parity-odd factors in an invariant contraction. An odd
character component against a fixed odd probe has two such factors,
but is linear in that component. The written B599 mixed-parity boundary
already says this. If both slots scale with one epsilon, a quadratic
law follows for that particular experiment; if the connection enters
the anomaly-free character above, the odd Taylor response starts at
degree five. These statements are compatible. No B599 refutation or
new universal response-order law is implied.

With R and gamma fixed, W_R(gamma,A_gauge) has no argument in the
internal structure connection or Higgs field. Its derivative with
respect to those independent fields is identically zero. The commuting
gauge/structure A4 factors in the actual root roster justify keeping
the variables distinct in this restricted observable. Thus that
function ALONE is not R41's required noncentral internal flag current.
Even its gauge variation at trivial holonomy begins only at the stated
order for the chiral difference. An observable does not determine an
action coupling, loop population or source field equations.

This conclusion is deliberately narrow. Mixed E8 charged fields can
couple the factors; integrating fields out can produce an effective
action; an inserted Wilson line can encode a prescribed external source;
R/domain may depend on a background. None has been disproved. Each
needs its actual coupling, variations and domain. R77 already exhibits
added adjoint sources that balance the current, but their free profiles
remain input; R83 retains the source-versus-axis distinction. Those
positives and debts are not erased by a readout calculation.

The full E8 adjoint weights occur as w and -w, so its character is
invariant under dualization and its odd difference is zero. It can
nevertheless vary as an EVEN function of the internal joined coordinate
(R87/R88). A readable neutral coordinate, a chiral character, a source
current and an experiential observer are four different claims. No
qualia, physical vacuum selection, quantum dynamics or SM/TOE follows.

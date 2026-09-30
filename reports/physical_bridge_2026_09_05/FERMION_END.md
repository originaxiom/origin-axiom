# Fermion reality permits complex conical boundary lines locally

September 30, 2026. Path-local R61. The local fermion reality test is
now explicit: it combines Hodge duality with complex conjugation.
On the torus-link critical channel, complex lines can preserve that
combined operation and cancel the Hermitian boundary current while
remaining invariant under rotations. They need not be real lines.
This changes the next physical test, not the physical chirality verdict.

All **50 exact controls and 20 focused tests pass** under pre-execution
seal 7427a24df7d78cb4b0cbd4892d0406b195a546d7, pushed and server-confirmed
before execution. The selection includes eight new tests, eight R60
tests and four unchanged R23 Clifford tests. No foreign geometric
census, full repository suite or full physical boundary law is certified.

## What the fermion map requires

The adopted field theory has independent complex Weyl fields chi and
psi_i, with conjugate partners constrained by Majorana reality. Its
full-form description Hodge-dualizes the barred fields. Its off-shell
chiral-multiplet variations also contain an internal covariant derivative
of the gaugino. These statements come from the explicit field dictionary,
not a count of components: [Braun et al., equations 2.41--44, A.16--18
and B.1--7](https://arxiv.org/html/1812.06072v2).

Reusing R23's operator, the independently constructed volume Clifford
matrix J has J^2=1, commutes with the derivative Clifford matrices and
anticommutes with the Higgs matrices. It is Hodge star with degree signs
(+,-,-,+). On the neutral critical degrees 1 and 2 its common sign does
not affect domain invariance. This agrees with the twisted form
description in [Pantev--Wijnholt, section 3.1](https://arxiv.org/html/0905.1968v1).

For the incomplete cone metric dr^2+r^2 h, write the critical data as
u=alpha+dr wedge beta, with alpha and beta harmonic link one-forms.
If S is the link Hodge star, the transported anti-linear map is

    C(alpha,beta) = (S conjugate(beta), -S conjugate(alpha)).

It squares to one. The Hermitian current has matrix [[0,H],[-H,0]],
where H is the positive link pairing. For ANY complex line W in C^2,

    D_W = W direct-sum W^(perp_H)

is maximal current-isotropic and invariant under C. The proof uses
the complex bilinear symplectic annihilator, not the Hermitian one,
for the dual of W; every complex line in this two-dimensional space
equals that annihilator. Both complements are implemented separately.
Using W in both slots instead gives a nonzero current for the helicity
examples, an explicit wrong-domain control.

## Rotations do not obstruct these local complex domains

The square and hexagonal links have complex Hodge eigenlines W_plus
and W_minus. Each is preserved by the tested lattice rotation.
On the hexagonal link, one representative is

    W_plus = span_C((1/2 + i sqrt(3)/2, 1)).

Its conjugate is the other line and its Hermitian orthogonal complement.
Writing w for the displayed vector, the data
(alpha,beta)=(w z, i conjugate(w) conjugate(z)) explicitly satisfy C u=u.
Thus imposing the full reality condition does not force w to be real
or add another independent fermion. Bare conjugation and bare Hodge
star each exchange the two domains; their combined operation preserves
each. Imposing the two conditions separately would be stronger.

A linear reflection exchanges these domains. A model reflection
combined with conjugation preserves them, but this is NOT a derivation
of the physical G2/parity lift. Nor does rotation choose between the
two lines. No physical handedness is selected here.

B1504's theorem remains correct for REAL invariant lines and the real
self-dual completion category it states. These complex lines are not
complexifications of real lines, rational filling slopes, or B1502's
three real smoothings. The supplied physical fermions do not justify
restricting to that real category solely by naming Majorana reality.
The real theory in [Albin et al., Theorem 5.6 and section 6](https://arxiv.org/html/1307.5473v3)
is not cited as a theorem about this entire complex physical extension.
Our finite computation establishes the displayed local channel only.

R60's other alternatives receive a genuine restriction: W=0 and W=V
still cancel the current but FAIL this neutral combined reality test.
They are not promoted to physical neutral-sector counterexamples.

## The next constraints are differential and interacting

Applying a projector P to an entire chiral superfield constrains its
scalar, fermion and auxiliary field consistently at the coefficient
level. It does not remove the additional requirement

    (1-P) D_t conjugate(chi) = 0

from the auxiliary-field supersymmetry variation. The explicit derivative
countercontrol is nonzero. Likewise, a real infinitesimal gauge parameter
at the trivial neutral background must have d_t epsilon in W to preserve
the corresponding connection condition. A non-real helicity line has
zero intersection with R^2, requiring that parameter to be constant on
the connected torus. The internally constant four-dimensional gauge
transformation survives; unrestricted boundary gauge transformations
do not. This restriction requires justification in the boundary law.

The R60 holomorphic boundary form vanishes if both variations occupy
one common line. It is nonzero between opposite lines: i sqrt(3) for
the hexagonal representatives in the chosen normalization. That is an
algebraic pairing, NOT a predicted coupling. Choosing different sectors'
lines independently therefore cannot be justified by their separate
one-particle current checks.

Next construct and test the SAME parent's complete bosonic/fermionic
boundary variation problem, including the covariant derivative terms,
all indicial channels and R59's nonlinear tensor maps. In particular,
finite quadratic norm is not a certificate of finite interaction energy:
evaluate the actual residuals, without importing rough-energy no-goes
or assuming that boundary counterterms exist. The harmonic link block
does not exhaust the cone's indicial spectrum without a metric/scaling
argument. A source, extra field or boundary functional remains an explicit
additional physical input until earned.

No global chiral index or normalizable particle mode is derived here.
The full physics mission remains active. This result prevents a premature
real-line exclusion; it neither proves a chiral phase nor selects one.

## Evidence and reception

[Design and authored argument](FERMION_END_DESIGN.md),
[ten pinned reading/control inputs](FERMION_END_INPUTS.json),
[exact producer](fermion_end.py),
[eight dedicated tests](../../tests/test_physical_bridge_fermion_end.py),
[run receipts](FERMION_END_RECEIPTS.json), and
[custody checker](fermion_end_receipt_check.rb).
All scientific first runs succeeded; no sealed scientific file changed.
The literature was read personally in the named passages, not in its
entirety this pass. The all-head fetch left SM at ba41670b. No other
branch was edited and no literature novelty or corpus absence is claimed.

The governance run still has the four historical failure categories:
attribution, two old vacuous tests, five old seal-provenance debts and
41 stale relay debts. These are not science passes or a full-bank
certificate. A pre-seal metadata comparison initially used the shell's
ASCII encoding and falsely reported changed failure rows; a diagnostic
then raised an encoding error. Repeating that metadata check explicitly
in UTF-8 established byte-equivalent failure text. No science was run
before the seal and no failure receipt was overwritten.

The first post-result governance run additionally failed law-map
provenance: the new table used an unrecognized heading and omitted the
audited arc context from three rows. Those documentation fields were
corrected without changing the scientific claims or frozen files; the
failed run is retained separately. The cumulative custody check passes
982 current artifact digests, 337 distinct seal paths, 185 selected local
Markdown links and the same 24 historical failed/error test IDs. This
does not rerun the old suite or independently review the argument.
The corrected governance run returns to the same four historical
failure rows, with 26 passes. All six captured science/audit runs and
their actual exit codes remain in the receipt file.

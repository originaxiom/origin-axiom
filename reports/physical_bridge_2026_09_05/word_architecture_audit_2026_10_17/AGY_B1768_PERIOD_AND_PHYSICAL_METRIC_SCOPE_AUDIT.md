# B1768 preserves a singlet norm, not a completed physical matter metric

October 27, 2026. UNREVIEWED source audit and hand controls. Source pin:
agy 6beb2abfc, B1768 producer, FINDINGS, verdict, transcript and tests.
No numerical integration, producer import or test execution reproduced.

## Positive content to retain

For the stated smooth superelliptic model, the intermediate projection
r:(x,w)->(x,y=w^2) onto y^2=P_3(x) has degree two. Therefore with the
DECLARED algebraic pairing (i/2) integral omega wedge conjugate(omega),
and omega1=r^* dz on the normalized elliptic curve, its norm is exactly
2 Im(tau). This is a valid geometric reduction by degree, without path
quadrature. It must use the intermediate degree-two quotient, not the
full degree-eight map with the same differential normalization.
The central-parity mixed zeros also survive. These are geometric form
statements. They are not invalidated by problems in the other paths.

## What the producer actually evaluates

The script integrates three forms over three OPEN base-plane segments.
It does not specify their lifted sheets as closed cycles, assemble six
cycles with a symplectic intersection form, or compute A/B period blocks.
It uses principal powers of P(x) at quadrature points without an
exhibited analytic continuation along a sheet. Such a path prescription
needs checking when it approaches/crosses a branch cut. A nonzero
determinant of three path integrals does not prove a canonical homology
basis, a genus-three Riemann matrix or a complete Hodge pairing.

In particular the third segment ends at x=1000.0, NOT infinity as the
printed labels and FINDINGS state. From P(x)=4x^3+O(x), the omitted tails
on a compatible asymptotic branch are

  integral_R^infty dx/P(x)^(1/2) ~ R^(-1/2),
  integral_R^infty dx/P(x)^(3/4) ~ (4/5)*4^(-3/4) R^(-5/4),
  integral_R^infty x dx/P(x)^(3/4) ~ 4^(1/4) R^(-1/4).

The last omitted tail is about 0.25 at R=1000. These are author analytic
asymptotics, not rerun output or certified numerical error bounds. They
show why the determinant/ratios cannot be advertised as infinite-path
values without a tail calculation. The FINDINGS root asymptotics also miss a factor two: at the cusp these
conventions give e1~2 pi^2/3 and e2,e3~-pi^2/3, consistent with its
printed numbers, not pi^2/3 and -pi^2/6. The target assertion det_abs>1 is
also basis-scale dependent, not a topological nondegeneracy criterion.

Precision is not configured as stated: with 'import mpmath as mp',
'mp.dps=35' assigns a module attribute instead of setting the context
'mp.mp.dps'. The official mpmath 1.3 documentation distinguishes the
module from the context 'from mpmath import mp':
https://www.mpmath.org/doc/current/basics.html (read October 27).
The transcript displays the usual 15-digit arithmetic. No import was
run to test a corrected producer. Correct precision, endpoint/branch
control and independent convergence/error checks are separate duties.

## The missing norm is visible in the function itself

compute_hodge_metric sets K11=2 Im(tau) and K12=K13=0, then returns two
ratios of path integrals. It does not compute K22,K23,K33, eigenvalues,
or a relative singlet/doublet norm. Ratios of linear path functionals
are not positive L2 norms. Indeed omega3/omega2=x pointwise, so a ratio
of their path integrals changes with the path even for fixed fields.

For a real symplectic cycle basis and complete period blocks A,B,
Riemann's bilinear identity would give the declared algebraic Hodge
pairing as G=(i/2)(A B^dagger-B A^dagger). The omitted cycle/sheet and
intersection data are precisely what is needed for that computation.
Alternatively one may evaluate the actual positive area pairing with
controlled geometry. Neither is implemented by this producer.

An overall change of convention from (i/2) integral omega wedge baromega
to the unhalved Hodge-star norm changes the common factor. Physical
normalization must additionally carry the action coefficient and the
actual coupled-mode metric. Relabelling omega1 as the top quark and
asserting that doublet norms are larger does not derive a mass hierarchy.
The cited B1767 field identification is already challenged by our coupled
complex audit; it cannot pay this duty. The chosen tau_* remains a
benchmark, not a derived state by B1764's inverse radial condition.

The B1768 tests read saved JSON, assigned K entries and a loose target
determinant; they do not replay quadrature or compute the missing Gram
block. Keep the segment-integral numerical output as UNREPRODUCED
numerical content, and the singlet area/parity proof as conditional
geometric positives. A full forward physical Kähler metric and removal
of B1763's metric choices are not established by this script.
No exclusion of the geometric-normalization route is made.

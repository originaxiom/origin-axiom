# R22: test the proposed completion on the same source operator

2026-09-09. Pre-execution design. Path-local R22, no B allocation.

BANKED IDENTITY: R18's strong maximal complex, R19's exact relative
cochains and E6 roots, R20's order-three character, and R21's actual
H representation and charge-four singlet. The added R21 fields were
never claimed to be internal zero modes. Here test that missing joint,
not a different four-dimensional model. Reuse original producers.

PRIOR ART: Pantev--Wijnholt, https://arxiv.org/pdf/0905.1968,
sections 3.1 and 3.4, and Braun et al., https://arxiv.org/pdf/1812.06072,
equations (2.41)--(2.52): charged degrees and their CPT identification,
and actual defect/inflow couplings. Golenia--Moroianu,
https://arxiv.org/pdf/math/0701780, section 3.2: nonintegral cusp
holonomy removes the transverse scalar zero mode. Do not transfer
its smooth scalar theorem to the singular Witten operator.
Aronszajn, J. Math. Pures Appl. 36 (1957), pp.235--236, theorem and
regularity assumptions, read from
https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf:
local unique continuation for a smooth elliptic scalar equation with
locally bounded lower-order coefficients. Access 2026-09-09.

## Scope, route and prior

P0: the SAME commuting signed source field, same strong maximal
domains, same scalar compact holonomy and same four-dimensional
chirality convention as R19. Compute its response to a proposed
enlargement by conjugate pairs of charged H multiplets, one
representative per CPT pair. This is not every singular completion,
every parent, every source pattern, or every physical theory.

P1/P4: PB-BOUNDARY/X33. R21 explicitly owes internal mode supply and
finite-energy nonparallel profiles or an actual defect/inflow sector.
This takes precedence over constructing another compatible EFT.
No SM mass/value comparison. No new empirical identification.

P2/P3: fresh all-head fetch, main eb9db7fa, SM d722714f, physics
659487bb, outside 988e2417, own 84f6b118. Atlas card, already-banked
query 'charged Higgs finite energy cusp', and eleven-head lexical
sweep saved in GEOMETRIC_COMPLETION_PRIOR_SWEEP.json. Read flagged
B1171 body, R15/R18/R19/R21 sources and reports, main B1304 body and
B1302 peripheral producer/data, SM B1350 body, and incoming numbering
relay. See prior receipt. No universal absence or novelty claim.

P6: expect a failure of the naive mode transplant: negative gauge
charges see the opposite source domain. Expect nonzero finite-norm
trial profiles but NOT thereby stationary Higgs solutions. Expect
the single-scalar Maxwell equation to obstruct keeping a flat
connection with non-real holonomy. Any contrary result is preserved.

## A. Supply, not just anomaly cancellation after adding fields

For an integer q != 0 and beta_a >= 1, recompute the cochains at
(zeta^q,zeta^-q). Positive q takes relative T, negative q relative E.
Compute every Betti degree and the H1 difference against the conjugate
sector. Expected on three source arcs:

- q positive, q not divisible by 3: H1(q),H1(-q) = 3,0;
- q positive, q divisible by 3: 4,1;
- negative q reverses the pair, not its physical gauge charge;
- net H1(q)-H1(-q) = 3 sign(q), including the exceptional transport.

The all-charge statement follows from the three residue classes and
the exact chain dimensions/ranks, not a bounded integer scan. Controls
with k=1,2,4 source components test the general k dependence. Do not
mistake degree-two CPT descriptions for additional fermions.

Use actual R21 weight sets, not labels alone. Applying this operator
to 16_1 + 10_-2 + 1_4 and their CPT partners is expected to yield net
3*(16_1 + 10_+2 + 1_4), not the added-field anomaly-free spectrum.
Expected (Tr u, Tr u^3, Spin(10)^2-u) = (120,480,12), with T(10)=1.
Recompute the full six-variable anomaly and compare with the R21
zero polynomial. One representative or its conjugate must give the
same answer. Same-source extra charged pairs give

  Tr u = k sum dim(R_q)*abs(q),
  Tr u^3 = k sum dim(R_q)*abs(q)^3.

This is an all-finite-enlargements statement ONLY in the declared
common-sign domain class; neutral modes contribute zero to these
channels. Opposite source response for the vector is a live positive
control restoring R21's anomaly-free spectrum, but is NEW geometric
data, not an allowed relabeling of q in the same operator. Weak sources,
mixed signs, other Cartan profiles, localized defects and inflow remain
outside this restricted statement.

## B. Finite quadratic norm is not a vacuum

Recompute peripheral exponent sums from main B1302's explicit words,
whose relator matches R19's basis. At q=4 both cusps are nontrivial
order-three flat lines. For any flat torus metric the transverse
eigenvalues are 4*pi^2*(n+alpha)^t h^-1*(n+alpha), n integral. A
nonintegral phase has a strictly positive minimum, not a computed
physical mass. Square-torus values are labeled instrument controls.

On ds^2=ds^2+exp(-2s)h, ordinary scalar norm carries exp(-2s),
transverse kinetic energy carries no exponential volume factor.
A constant-modulus charged tail is L2 but has infinite kinetic
energy at nontrivial holonomy. This is not an exclusion of decay.

For the ACTUAL R18 end H=q[V(w)+exp(2s)(b*s+c)], b>0, choose a smooth
nonzero flat-bundle section p(w) supported in a contractible patch
away from the source punctures. It exists for every character. Set
a(s)=exp(-eta*exp(2s)), eta>0, and Psi=a(s)*p(w); use a finite-height
cutoff and extend by zero through the core. This is a global smooth
trial section away from prescribed sources, not a zero mode. For
X=exp(2S)>=1 and d=q*(b+2c)-2eta, verify the transformed integrals:

  norm = (||p||^2/2) integral_X^infty exp(-2eta*x)/x^2 dx,
  radial form = (||p||^2/2) integral exp(-2eta*x)
                                      *(q*b*log(x)+d)^2 dx,
  tangential form = (K_p/2) integral exp(-2eta*x)/x dx.

K_p=||d_A p+q*dV*p||^2 is finite on this patch. The radial bound uses
(log x)^2 <= x for x>=1 and (u+v)^2<=2u^2+2v^2. Lock the resulting
elementary tail antiderivatives and numerical integral comparisons
for both charge signs, nonzero b,c and a neutral control. The bounded
smooth R15 correction multiplies by a bounded exp(-qv), preserving
the weighted graph-space construction. These are finite L2 and
quadratic-form norms of an added profile; NOT the finite total action
of the singular background, a solved coupled PDE, a Higgs condensate,
or an internal derivation of R21's new scalar. H0=0 does not by itself
rule out scalar modes arising from degree-one SYM fields.

## C. Keep the connection equation and differential square

For a minimally coupled single complex scalar with a smooth real
potential W(y,|Psi|^2), kinetic |(d-iqA)Psi|^2, Maxwell term
|dA|^2/(2g^2), and no other current, derive its A variation. On a
cusp Fourier mode f(s)*exp(i*k*x), the integrated A equation is

  -A''/g^2 + 2*q*(q*A-k)*f^2 = 0.

A constant A with k-qA != 0 and f != 0 fails. Generalize analytically:
if A is flat and the scalar solves its elliptic equation, zero total
current implies locally constant phase wherever Psi != 0. On the
universal cover its imaginary part, after one constant phase rotation,
vanishes on an open ball and solves a real elliptic equation. Unique
continuation makes it zero everywhere. A nonzero solution therefore
requires line holonomy in {+1,-1}; the order-three charge-four line
fails. Smoothness/locally bounded coefficients are required only on
the connected source complement, not across the singular lines.

Controls: a real antiperiodic standing wave on a circle has zero
current and nonzero kinetic energy; a conjugate-current pair cancels;
neutral fields and compatible phases pass. This theorem is not an
obstruction to multiple condensates, additional currents, curved A,
nonminimal terms, defects, or nonabelian Higgs configurations.

Finally verify in every form degree, with actual exterior algebra,

  (d-iqA wedge + q*dF wedge)^2 = -iq*dA wedge.

Nonzero curvature invalidates the original de Rham-complex shortcut.
A changed full nonabelian BPS system may restore integrability; the
R19 counts may not simply be carried over. No universal chirality kill.

## Execution

Seal design, prior, source and mathematical tests with generated hashes
and a pre-execution commit. Preserve first JSON and complete focused
stdout before yielding between goal turns. Run R18--R21 dependencies
and the expanded regression, keeping its known 21 failure/error IDs.
No worktree edits during scientific/certifying runs. Report at least
the positive norm construction, failed mode transplant, explicit
counterexamples to wider closures, and the next actual inflow/defect
or multi-Cartan construction; no main bank or full TOE claimed.

# Path-local R13 — compute the harmonic cusp input, not just its allowed modes

STATUS: sealed design before the first execution of the new source and tests.
CC's numbering relay is read (BANKING_RECEIPT.md); no B number is taken.
R4--R12 remain in force at their stated scopes. This is a local research
checkpoint, not full-suite/independent-receipt/main-bank certification.

## Question and prior

The owner's new relay quotes SM-seat commits 2a7f8855 and 6f077ef2.
Their bodies distinguish three-family multiplicity from NET chirality:
the latter is explicitly N=0 on the closed model. The sB1277 cusp
addendum computes allowed modes but explicitly does not compute the
actual harmonic 1-form's leading coefficient. It assumes it is nonzero.
Test that coefficient by adapting the repository's existing instrument.

P0: standard rectangular rank-two hyperbolic cusp ends, and a numerical
meridional harmonic-form candidate on the particular Riley group of
m004. This does NOT quantify over the object's full relational family,
all physical metrics, Higgs bundles, sources, defects or boundary domains.

P6: the leading coefficient should probably be nonzero; the Fourier
ordering is likely correct. A converged zero, wrong affine-frame
assumption, rank failure or unconverged fit must remain visible. A finite
numerical estimate is NOT a proof of exact nonvanishing. Independently,
the nonzero meridian period should force a logarithmically divergent
1-form norm on the COMPLETE hyperbolic end. This is not a no-go for an
external Higgs background or for normalizable charged fluctuations.

## Grounding and reuse

Read WORKING_RULES, banking/CC relay, P0--P6, campaign stop rules, ladder
X33, relevant law/lead rows and kill-graph entries. Atlas card chirality;
already-banked terms `harmonic cusp` (95 hits, no two-term settled hit)
and `theta coweight` (117 hits, no two-term settled hit). The query's
historical sample is NOT an absence proof: the newer branch explicitly
contains the present target. No universal absence claim is made.

Source pins read without merging:

- main 2901ae9f6dba964870b44d5eb6e01066c62b7f62;
- SM 6f077ef2ba988a6a4d98b177758a0c2d67d6377c, including the entire
  sB1277 arcs/corners addendum and its producer at 2a7f8855, and the
  sB1279 FINDINGS body; the large sB1279 vacuum census is NOT rerun here;
- physics 9a5d19285a1b01e26d20948df40afd281d827316, R60 and R70
  bodies and R70/r70b producers; B351 exact E6 Cartan convention;
- local B739's cusp expansion and B1007_arb_maass/_reference_double.py:
  its Riley matrices, word generation, height-raising pullback and
  Bessel kernel. Those READ primitives are adapted, not a newly claimed
  Maass discovery. No old solver or sealed file is modified/import-run.

Primary sources accessed 2026-09-06: Braun et al., arXiv:1812.06072
eq. 2.18 and Appendix B (commuting Higgs equations and 7d/4d kinetic
reduction); Pantev--Wijnholt arXiv:0905.1968 (the separate boundary/index
problem); NIST DLMF 10.25/10.40 (modified Bessel equation/asymptotics).
These specify a CONDITIONAL physical model, not an empirical identification
or an established UV completion of the mathematical object.

## Fixed conventions and instrument

1. Upper-half-space horizontal coordinate w=y+i L x, height z>0,
   x=longitude and y=meridian mod 1, L=2 sqrt(3). Metric
   ds^2=(L^2 dx^2+dy^2+dz^2)/z^2, curvature unit declared, not predicted.
   A=[[1,1],[0,1]], B=[[1,0],[1/2-i sqrt(3)/2,1]], as the old solver.
   Both generators have meridian period +1. The relator and complex
   conjugate holonomy are exact controls. Point actions track the actual
   word and its abelianization; lattice reductions subtract the meridian
   integer as well. Discarding that cocycle is a deliberately wrong control.
2. A commuting flat-gauge Higgs field is closed and coclosed. On the
   universal cover write f=y+sum c_j z K_1(kappa_j z) T_j(x,y), phi=df.
   f(gP)-f(P)=ab(g); f itself is NOT a single-valued function on m004.
   kappa=2 pi sqrt(k^2/L^2+l^2). Derive the scalar Laplacian and verify
   F''-F'/z-kappa^2 F=0, and z F'=-kappa z^2 K_0(kappa z).
   Positive local decaying solutions and an incorrect cylinder kernel
   distinguish the metric. The growing I_1 branch is excluded by the
   declared cusp growth class, not by an unexplained selection principle.
3. Use the quoted D4 affine maps to form the b1 parity sector. Exact
   trigonometric checks enforce T=(x+1/2,y), theta=(-x,-y), and the two
   glides (x+1/4,-y+1/2), (-x+1/4,y+1/2). The real basis comprises
   sin(2 pi kx)cos(2 pi ly) for even k with k/2+l odd, and
   cos(2 pi kx)sin(2 pi ly) for even k with k/2+l even (omit zero terms).
   First allowed pure (2,0); first mixed (2,1), twice its kappa.
   Also fit WITHOUT imposing T/glide parity (theta-odd sine basis), to
   test the incoming affine-frame restriction rather than assume it works.
4. Adapt the old solver's word-length-bounded height ascent (length 5,
   plus length 7 control). It gives actual Gamma translates even if
   ascent stalls, and is NOT a complete fundamental-domain certificate.
   Solve overdetermined real collocation equations after column scaling.
   Fixed fits: cutoffs |mu|=4,6,8,10 at heights .55/.65/.75, seeds
   1301--1306, at least 600 samples and at least 8 per mode. The
   theta-only control uses cutoff 6 and at least 8 samples per mode.
   Store modes, coefficients, rank, singular values/condition estimate,
   training and independent seed/height holdout residuals. No coefficient
   target is fitted, and there is no physical-observation input.
5. Accept only a NUMERICAL candidate if the three high-cutoff symmetry
   fits have full rank, holdout residual <2e-5, leading coefficients agree
   within 2e-4 relative and have abs(coefficient)>1e-4. An independent
   theta-only fit must have holdout <2e-4 and agree within 2e-3. Otherwise
   record UNRESOLVED, not zero or no-go. These empirical numerical
   tolerances are not rigorous truncation or interval bounds. Do not
   weaken them after execution. A zero-period control must return zero;
   a manufactured single-mode RHS must recover its supplied coefficient;
   omission of the period cocycle must fail the genuine held-out equation.
6. Compute the end norm analytically: for periods (q along x,p along y),
   integral |phi|^2 >= (L p^2+q^2/L) log(Z/z0). Cross terms with periodic
   derivatives integrate to zero. The scalar constant mode has finite
   volume norm; exact decaying Fourier differentials have finite end
   norm. Finite volume must not be confused with finite 1-form norm.
   A fixed nonnormalizable background is not a dynamical normalizable
   modulus, but this test neither derives its full classical action nor
   excludes charged normalizable modes, cutoff completions or other metrics.
7. Exact incoming-parity check only: in the specified Bourbaki E6 Cartan,
   diagram theta exchanges omega_1 and omega_6. Recompute +/- projections
   and zero-root centralizer dimensions from all roots. A single omega_1
   is neither even nor odd. This does not make its nonzero charge admissible
   at a pointwise fixed arc, prove vector-like matter, or specify E8 lifts.

## What a result will and will not establish

An approximate harmonic representative in the stated asymptotic class is
useful input toward a physical Higgs/operator calculation. It is not
that operator's chiral spectrum. In particular the tangential period part
and the exponentially decaying radial part must both be retained.
The regular theta-odd zero-set index observation is already in R12;
mixed-mode crossings are not regular boundary domains. No new generation
count is obtained by counting rectangular sign cells at a crossing.

Seal design, source and tests by SHA256 and LOCAL commit before first run.
Preserve first outputs/failures and repair only in separately sealed files.
The report must retain possible boundary/source routes instead of
promoting this member-specific calculation to a global chirality kill.

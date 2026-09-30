# Complex fermion data at a conical end

September 30, 2026. Path-local R61 pre-execution design. This tests
the next PB-BOUNDARY duty in PHYSICS_MISSION, not a full physical
completion. No empirical number or global particle census is computed.

## Question and declared prior

For a torus-link critical channel of the supplied twisted fermion,
does the reality map require a REAL Lagrangian line, or can a complex
line preserve both reality and the Hermitian Green form? Quantify over
this local linear channel, not all ends, parents or physical vacua.

Prior from the authored argument below: complex lines pass the combined
star-and-conjugation condition; the pure star and pure conjugation
conditions are stronger separately. Rotations can preserve complex
eigenlines even though they preserve no real line. This is a candidate
linear admission test, not permission to identify it with a complete
supersymmetric interacting boundary theory. The tests can expose sign,
complex-conjugation and implementation errors in this argument.

## Reused work and source scope

All origin heads were fetched before this design; the received SM head
remains ba41670b. R60 already independently verifies the REAL lattice
lemma and its real self-dual scope. B1500 and B1504 use real torus-link
lines; their intersection-chain and geometric censuses are not rerun.
R23 already has the actual exterior/Clifford mass map; four unchanged
Clifford tests are selected as controls, not claimed as new work.
R59 supplies the actual parent coefficient and cubic maps, not an end law.

The ladder, framework, campaign, LAW_MAP and PB-BOUNDARY were checked.
The epoch-limited atlas and already-banked query 'Majorana complex cone
boundary Lagrangian' were run. Its strongest match B1191 was read; it
concerns earlier typing and finite content, not this operator-domain map.
Targeted code/body searches and the old kill graph were also checked.
These are navigation, not a whole-history absence or novelty claim.
The identification ledger audit retains its nine unearned inputs.

Primary reading is personal and limited to the passages used:

- Braun et al., 1812.06072v2, sections 2.3 and 4.1, A.2, B.1 and C:
  independent Weyl fields are chi and psi_i; their barred partners are
  related by Majorana reality. The full-form dictionary replaces barred
  one-forms by their Hodge duals. The chiral multiplet variations include
  an internal covariant derivative of the gaugino in delta H. Neutral
  gauge zero modes receive normal boundary conditions in section 4.1.
  https://arxiv.org/html/1812.06072v2
- Pantev--Wijnholt, 0905.1968v1, section 3.1, equations 3.1--3.6:
  twisting and the form description. We use d_q+d_q^dagger with R23's
  checked principal symbol, not the apparently different sign in the
  printed coordinate formula 3.4. https://arxiv.org/html/0905.1968v1
- Albin et al., 1307.5473v3, Theorem 5.6 and section 6: real
  mezzoperversities and the additional Hodge self-duality condition.
  Do not attribute our complex anti-linear extension to that real
  theorem. https://arxiv.org/html/1307.5473v3

Accessed September 30. No entire-paper reading in this pass is claimed.

## Reality is transported rather than renamed

With e_i wedge and a_i contraction in an oriented orthonormal three-frame,
put c_i=e_i-a_i, h_i=e_i+a_i and J=c_0 c_1 c_2. R23's actual operator is

    Q_q = sum_i (c_i partial_i + q f_i h_i).

Direct exterior algebra gives J^2=1, [J,c_i]=0, {J,h_i}=0, and J equals
Hodge star times degree signs (+,-,-,+). Thus J times coefficient
conjugation intertwines q with -q for real f_i and trivial local gauge
transport. These signs are conventions, not a new charge assignment.
The bulk form dictionary sends a left Weyl one-form psi to the dual
of its complex-conjugate right partner. On the critical degrees 1 and 2
this is star times conjugation, up to one common irrelevant sign. It
does not require the one-form coefficients themselves to be real.
The external Weyl charge-conjugation factor is unchanged, not counted
as an extra internal multiplet.

Use the incomplete cone metric dr^2+r^2 h and a trivial, neutral link
coefficient. For harmonic link one-forms, write u=alpha+dr wedge beta.
Their norms both have radial density dr. With oriented link star S,

    star_3 (alpha,beta) = (S beta,-S alpha),
    C(alpha,beta) = (S conjugate(beta),-S conjugate(alpha)).

This is an actual critical-channel calculation: S^2=-1 and C^2=1.
It is not the complete hyperbolic cusp's Hilbert space (R60/F02).

## Hermitian current versus real self duality

Let V=C^2, Omega=[[0,1],[-1,0]], and H positive real symmetric with
det H=1. Set S=-Omega H, so H=Omega S. The boundary current has matrix
G=[[0,H],[-H,0]]. For complex W define

    D_W = W direct-sum W^(perp_H),
    C D_W = D_(W^(perp_Omega)),

where the second perpendicular is for the COMPLEX BILINEAR symplectic
pairing. Indeed conjugating the Hermitian complement converts it to
the bilinear H complement, and S converts it to the Omega annihilator.
Every complex line is bilinear Lagrangian. Hence its D_W is maximal
Hermitian-Green isotropic and C invariant. W=0 and V fail C invariance,
although they pass self-adjoint current cancellation. A real line is
also fixed by bare conjugation; a non-real line generally is not.
Requiring bare star invariance separately would therefore discard
domains the combined anti-linear reality test permits.

Check square and hexagonal links. In the latter take raw Gram
[[2,-1],[-1,2]], normalized by sqrt(3), and R=[[0,-1],[1,-1]]. In the
former H=I and R=[[0,-1],[1,0]]. S has complex eigenlines W_plus and
W_minus. Each is rotation-invariant; neither is a complexified real
line. An orientation-reversing reflection exchanges them. Its
composition with conjugation preserves them in this model, but the
actual G2/parity lift is NOT identified with that model operation.
Neither line is a rational Dehn-filling slope or one of B1502's real
smoothings. B1504's real theorem remains intact.

## Supersymmetry and interactions impose further conditions

The coefficient-level condition P Phi=Phi applied to an entire chiral
superfield constrains its phi, psi and H together; the conjugate
superfield uses conjugate(P). This is necessary for the algebraic
variations, not sufficient for the action or differential domain.
Braun's delta H contains D_i bar(chi), so (1-P)D_t bar(chi)=0 is an
additional constraint. At a trivial neutral background a real gauge
parameter obeying the same connection restriction has d_t epsilon in
W. For a non-real helicity line, W intersect R^2=0, so it must be
constant along the connected torus. This does not eliminate the
internally constant four-dimensional gauge transformation, but does
restrict boundary gauge transformations; that restriction needs a
physical boundary law, not a silent convention.

The local superpotential boundary form from R60 vanishes on a single
common complex line because w^T Omega w=0. Opposite helicity lines
have nonzero wedge pairing. These checks are necessary tensor controls;
they do not prove nonlinear gauge closure, convergence of the full
action, compatibility of all R59 root channels, or quantum anomalies.
Do not claim that the harmonic link block exhausts the indicial spectrum:
nonzero link modes depend on the actual cone metric and scaling.

## Execution and acceptance

Seal this design, input pins, producer and tests; commit, push and
confirm the remote before running any new scientific calculation.
Run the exact independent Clifford/critical-boundary controls, eight
new focused tests, R60's eight tests and R23's first four Clifford tests.
Preserve exclusive raw stdout, command, timing and exits, including any
failure. Do not edit sealed science after execution.

Acceptance requires the combined reality and current checks, explicit
failures of the wrong separate reality test and wrong Hermitian
complement, rotation/reflection controls, and nonzero opposite-line
boundary and gauge-derivative countercontrols. A pass earns the local
linear compatibility and the explicit next constraints, not a global
physical domain, chiral matter, selected handedness or TOE completion.
Next derive a full boundary variational/supercharge problem in the SAME
parent and metric, including all indicial channels and nonlinear
products. Any extra boundary field or functional is a priced input.

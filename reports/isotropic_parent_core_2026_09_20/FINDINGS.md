# F06: a full-parent local core exists, with a geometric and boundary price

2026-09-20. Local fork `audit/fork-2026-09-20`. This is an explicit
classical LOCAL solution of the specified parent gauge equations on a
supplied metric, not a global construction on the arithmetic object,
three generations, four-dimensional gravity or a TOE.

**Version notice:** the first sealed test run had **16 passes and one
failure**. Its predicted pointwise algebraic spectrum omitted an adjoint-
norm term. The producer and original failure are preserved. A separately
sealed post-failure correction passes **19 tests**, including all sixteen
unaffected original tests and independent complex-component checks. Read
[PROOF_V2_ADDENDUM.md](PROOF_V2_ADDENDUM.md) with section 5 of the frozen
[PROOF.md](PROOF.md); do not use its superseded spectrum. The full BPS,
curvature and boundary identities passed both versions.

## 1. What the construction actually earns

R39 had already identified the issue with importing the scalar source
model: charge-four fields also create noncentral currents. Three mutually
independent one-form components can make their Gram matrix isotropic, but
that alone does not solve their differential equations.

F06 supplies an explicit solution to that remaining local test. In R39's
D5-invariant SU4 subalgebra of the candidate E8 parent, choose

    U=diag(3,-1,-1,-1), N_i=E_(0,i+1),
    g=v^2 delta, h=d(log v)/8,
    C_i=h_i U+a v^(-1/2) N_i,   a>0.

For arbitrary positive v, the entire complex flatness residual vanishes.
The complete real moment equation, including the off-diagonal and su3
parts, reduces exactly to

    I=(Delta_0 v+4a^2)U/(4v^3).

Consequently

    v=c-(2a^2/3)|x|^2, c>0,

is a smooth noncommuting BPS core wherever v>0. Every compact sub-ball
strictly inside that region has a positive nonsingular metric and finite
positive Higgs norm. The existing SU4 embedding makes it a local solution
of all parent residual equations, not just a central Poisson projection.
No extra scalar Q, external density or deleted neutral field is used.

This is a **newly checked application in this fork**, not a claim that the
local ansatz is new in the mathematical literature. R39's algebra/current
test and the adopted parent action are credited inputs. The underlying
full noncommuting equations are those of the chosen partially twisted SYM
model; their later commuting-source truncation is not substituted for
them. [Primary equations, Braun et al., 2.17--2.24](https://arxiv.org/html/1812.06072v2).

There are three internal one-form directions here, **not three derived
families, source arcs or defects**. This ball-like local core is not
identified with R29's proper-tube source. The parent, a, c, metric ansatz,
region, boundary data and eventual global matching remain inputs/duties.

## 2. The metric price is a proved property of this ansatz

The same equation forces its scalar curvature to be

    R_g=16a^2/v^3+2|dv|_0^2/v^4>0.

Therefore this specific isotropic-coordinate construction is not a
hyperbolic patch. The exact control v=1/z gives R=-6 but a nonzero full
moment residual. This is an ansatz limitation, not a theorem against all
isotropic coframes or all full-parent backgrounds on hyperbolic spaces.

The distinction changes the next task: testing this candidate requires
metric/field matching or a justified dynamical geometry. Calling the
metric “backreaction” without deriving the relevant action would merely
rename an input. The object's complete hyperbolic metric has not been
replaced as a claimed solution.

## 3. A separately priced gravity compatibility check

The defining-four positive Higgs tensor is

    S_ij=Tr(Psi_i Psi_j)=3 v_i v_j/(16v^2)+a^2 delta_ij/(2v).

For the quadratic core the FULL Ricci tensor, not only its trace, obeys

    Ric_ij=(32/3) S_ij.

It therefore also solves the three-dimensional Einstein--harmonic-map
equations of the explicitly chosen auxiliary action
integral sqrt(g)[R-(32/3)|Psi|^2], with its flat-bundle constraint and
positive Hermitian reduction. Metric variation and the harmonic-map
equation are stated in the proof. The coefficient was disclosed before
execution, in this trace normalization.

This comparison has a failable control: adding epsilon(x1^2-x2^2) to v
preserves Delta_0 v=-4a^2 wherever v remains positive, but breaks the
Einstein tensor equation. BPS does not automatically imply that equation.

**Not earned:** this auxiliary action is not derived from the framework,
not the gravitational completion or full stress tensor of the SYM model,
not a selected coupling or observed Newton constant, not a four-dimensional
Lorentzian solution, and not a torsion-free G2 completion. A trace change
rescales the displayed coefficient. Its value is not a physical prediction.
What is earned is a concrete local compatibility example for a declared
metric-plus-harmonic-map system, available for a real parent-matching test.

## 4. The local solution cannot be advertised as a complete space

At R0=sqrt(3c/(2a^2)), v vanishes. The proper radial distance to that
surface is finite, the metric degenerates and the positive curvature
diverges. The Higgs-norm integral diverges logarithmically there, with
positive coefficient pi a^2 R0^3 in its radial density.

Every smaller ball is a regular local solution, but taking the maximal
positive ball does not manufacture a complete finite-norm background.
Its nonzero boundary flux is explicitly retained:

    integral_(r=r0) h(n)dA=-2 pi a^2 r0^3/3.

The opposite-column dual reverses that source sign. The sign is not
silently identified with R29's added charge-four scalar convention.

No matching to the cusp exterior was solved. A viable construction must
stop inside the regular region and supply a transition satisfying the
full equations and proper metric/interface conditions, or find a different
complete profile. Keeping this restricted ansatz throughout a transition
to negative scalar curvature cannot do that; additional structure is
required there. This does not identify which extra fields or source law
would suffice.

## 5. What happens to the previous matter obstruction

At the normalized center, the algebraic part H1=T*T+TT* of the one-form
operator has the **corrected** eigenvalues

    0 (multiplicity 5), 1/2 (3), 3/4 (4).

Its zero subspace is an explicitly checked symmetric trace-free tensor
space. The full covariant derivative of Psi is nonzero, despite vanishing
traced divergence. Thus F05's parallel-Higgs identity and its particular
positive lower bound do not transfer to this background.

This is a necessary caution, not a chiral result: a pointwise kernel and
failure of one lower-bound proof are **not normalizable zero modes**.
The full differential operator includes mixed terms. Its global spectrum,
physical domain, partners, quantum anomalies and interactions remain to
be computed on an actual completed background. No generation count follows
from the number five above.

## 6. Strategy and exact continuation

This checkpoint demonstrates that the full-parent source-current problem
has a constructive local answer once a specific metric is supplied. It
also shows exactly why that answer cannot simply be inserted into the
earlier fixed-hyperbolic-background calculation.

The next useful work is a **global compatibility test**, in this order:

1. Determine whether a justified parent gravity/geometry prescription can
   support such a core, or require a different fixed-metric core instead.
   The auxiliary three-dimensional action is a comparator, not permission
   to change the physical goal.
2. Solve or obstruct a specified transition to the object's actual exterior,
   retaining full B/beta components or explicit source/interface dynamics
   as necessary. Check equations and boundary flux, not only topology.
3. On that background derive the positive-norm operator/domain and whole
   low-energy spectrum. Only then assess chiral matter and its interactions.

The full TOE objective still requires the common-model quantum, anomaly,
Standard-Model, gravitational and empirical gates. No collection of local
examples discharges those gates.

## Evidence and custody

**Dated follow-through, F07 (2026-09-20):** the preceding matching priority
now needs a stronger preliminary filter. The [global comparison](../core_gluing_invariance_2026_09_20/FINDINGS.md)
shows that smooth replacement inside regular balls, preserving F05's
exterior flat holonomy and equivalent complete L2 norms, cannot create
exact charged zero modes even if this local pointwise bound has vanished.
The global complex still has a bounded contraction. Thus such matching
can remain a geometry benchmark but should not be pursued as a massless-
matter mechanism without changing one of those hypotheses. Different global
holonomy, end/domain data, additional fields and nonflat operators are not
excluded; very light positive modes in degenerating families remain possible.
No F06 scientific source, positive local identity or original failure is
changed by this follow-through.

**Further follow-through, F08 (2026-09-20):** the [balanced global parent](../balanced_parent_2026_09_20/FINDINGS.md)
provides an explicit interpretation of the corrected five-dimensional
kernel: its algebraic operator is four times this core's center operator,
while its complete-space zero equation is the trace-free Codazzi equation.
That construction changes the global coefficient to h tensor conjugate(h);
it is not a successful fixed-holonomy gluing of this core. It preserves
dual-sector spectral pairing and has not supplied a global matter count.
This credits the local algebraic positive without promoting it to particles.

- Initial seal `5ff91aff`: **16 passed, 1 failed**, retained verbatim as a
  transcribed tool result in [FIRST_RUN.md](FIRST_RUN.md).
- Correction seal `a06e9423`: **19 passed**, with unchanged producer and
  a new independently assembled component-norm control.
- **86 unchanged F01-v2 through F05 checks passed**, one optional GUI warning.
- Seven distinct new scientific files retain their sealed hashes;
  all F01--F05 directories were unchanged against `28c87f5a` at verification.

[Commands and reading limits](RECHECKS.md). These are exact symbolic
controls and authored analytic arguments, not an independent expert
review, complete global PDE certificate, full repository green suite or
main-bank acceptance. No new all-head fetch succeeded in this checkpoint.
No shared B number, other-seat edits, push or external publication.

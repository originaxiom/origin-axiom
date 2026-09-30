# Decaying cone modes admit a local nonlinear continuation

September 30, 2026. Path-local R64. In the SAME supplied cone action,
the paired decaying degree-one modes have a compact gauge part and a
Hermitian part. The latter has an exact local nonlinear continuation
that is not compact-gauge-equivalent to the original background.
This is a positive LOCAL construction, not a global particle, selected
vacuum, chirality or completed supersymmetric end law.

The corrected instrument passes **99/99 effective controls** and three
new tests. The fixed combined population is **40 passed, four original
failures retained**: two R63 comparison failures and two R64 unknown-sign
inference failures. Original science and tests remain unchanged.
The local existence argument is authored analysis, not independent
analytic acceptance.

## The actual distinction between a mode and gauge freedom

On R63's incomplete torus cone use C0=(a/2)wH with a>0, H=diag(1,-1),
c=norm(w) squared and lambda=c a squared=eta(eta+1), 0<eta<1/2.
The metric, parent and background are still physical inputs.

The two root primitives r^eta E12 and r^eta E21 generate the decaying
degree-one modes. Their paired complex coefficients split into compact
and Hermitian parts. An admitted compact exponential removes the compact
variation. The Hermitian radial component is different: the background
has Psi_r=0, and compact gauge transformations preserve that zero.
The nonlinear family below has tr(Psi_r squared)=2(f') squared.
It cannot be removed by a compact transformation, even in the full parent.

This does NOT mean two freely counted real physical moduli. The constant
Cartan stabilizer rotates the Hermitian phase and identifies opposite
signs when that stabilizer belongs to the admitted gauge group. Global
boundary restrictions on gauge transformations must still be stated.

## The nonlinear family is derived from both field equations

Put T=E12+E21, J=E12-E21 and g=exp(fT). At fixed positive metric,

    C=g C0 g inverse-dg g inverse,
    C_r=-f'T,
    C_link=(a/2)w[H cosh(2f)-J sinh(2f)].

The direct coordinate calculation, on BOTH declared link metrics, gives
zero full curvature and reduces the full moment equation to

    r squared f''+2r f'=(lambda/4)sinh(4f).

A positive Volterra kernel gives a contraction near the apex for prescribed
small leading amplitude b. The authored proof constructs

    f=b r^eta+
      4(eta+1)/(3(4eta+1)) b cubed r^(3eta)+O(r^(5eta)).

The actual matrix identities, inverse kernel, cubic coefficient, strict
contraction bounds, root inclusion, and incorrect-sign/metric/radial
controls are checked. This is not a numerical shooting plot at a finite
cutoff. The compact comparator exp(i fT) has zero residuals for arbitrary
f but zero radial Higgs, and is kept distinct.

## Zero action and an allowed fluctuation domain are different tests

For the nonzero continued family u=C-C0, its local L2 norm is finite
for every eta>0. But its L4 norm and separate background curvature norm
are finite exactly for eta>1/4; equality gives logarithmic divergence.
There is therefore a nonempty admitted critical interval
1/4<eta<1/2 in the DECLARED local maximal graph-plus-L4 space.

The background adjoint is explicitly Hermitian and cubic in f on this
family. Its compact gauge-fixing component vanishes in this ansatz.
This is not a global nonlinear Coulomb-slice theorem or a proof that
this sufficient space is the unique physical domain.

Three paths must not be confused:

| Path | Local action and domain conclusion |
|---|---|
| Straight additive path along the linear mode | Quartic curvature cost; finite only for eta>1/4 |
| Flat complex-gauge path with unrelaxed f=b r^eta | Sixth-order moment cost; finite only for eta>1/6 |
| Nonlinearly relaxed solution | Full residual action zero for all eta>0, but the stated graph-plus-L4 class still requires eta>1/4 |

The slow curved solutions do not authorize changing a fixed domain.
Conversely a divergent straight-line path does not exclude a curved
solution. This is precisely why a linear count or a quartic obstruction
alone was insufficient.

## The outer boundary remains load bearing

For the scalar primitive xi=r^eta T,

    integral_(0,R) norm(d_C0 xi) squared=2eta R^(2eta+1).

The apex flux is zero; the expression is the OUTER boundary flux.
The nonlinear equation likewise yields

    [r squared f f']_(0,R)=
      integral_0^R [r squared (f') squared+(lambda/4)f sinh(4f)] dr.

Positivity forces f=0 in this radial ansatz if either f(R)=0 or f'(R)=0.
Thus the local family necessarily changes outer data. It is not an
automatic global zero mode. This scoped identity is not a universal
no-go for other global fields, matchings or geometries.

## Verification and the retained failure

Original seal a99477919b97d924bdd9d5d476bb66aaf83f37aa and repair seal
fde9a76988ec164e97c20e59ba232b2fbb3fd636 were each pushed and
server-confirmed BEFORE their scientific execution.

The first run gave 94/95 controls and seven passes/two failures.
Its sign query for 2^(2eta+1)-1 returned UNKNOWN, not a negative.
The separately captured diagnostic retains that distinction. The repair
certifies positivity from value one at eta=0 and a positive derivative;
it preserves the expression and rejects reversed-sign/outside-domain
controls. All 95 original entries, including the failed one, remain visible.

The first combined 41-test run gave 37 passes/four failures. Adding the
three new repair tests gives 40 passes and the SAME four failures.
No test is deleted, rebound or silently weakened. Eight sealed scientific
paths and nineteen pinned inputs are checked independently of outcomes.

[Design](CONE_GAUGE_DESIGN.md), [authored proof](CONE_GAUGE_PROOF.md),
[input pins](CONE_GAUGE_INPUTS.json), [producer](cone_gauge.py),
[original tests](../../tests/test_physical_bridge_cone_gauge.py),
[repair design](CONE_GAUGE_CONTROL_DESIGN.md), [repair producer](cone_gauge_control.py),
[repair tests](../../tests/test_physical_bridge_cone_gauge_control.py),
[run receipts](CONE_GAUGE_RECEIPTS.json), [custody checker](cone_gauge_receipt_check.rb).

## Next connection to the physical mission

Match the ACTUAL peripheral holonomy and outer data of an existing
global parent bundle to these local candidates. R59's E, Lambda2(E),
duals and interaction tensors must come from the same bundle; do not
transfer an index from another coefficient system or declare the cone
metric selected by the architecture. Recheck the existing branch results
before designing that join.

A global bosonic and fermionic domain, permitted gauge group, normalized
dynamics and a chiral spectrum remain required. The [full mission](PHYSICS_MISSION.md)
also retains quantum consistency, gravity and predictive contact.
This result resolves a conditional local nonlinear question; it does not
replace those obligations. All remote heads were fetched without updates,
and no other seat's worktree was modified.

This own-branch checkpoint is not full-suite or main-bank certification.
The four historical governance failures and independent-review debts
remain recorded rather than waived.

Recorded cumulative custody passes for 1,010 artifact hashes, 356
distinct sealed paths and 199 selected relative Markdown links. The
same 24 failed/error IDs in the older recorded populations survive;
those suites were not rerun by this byte-custody check. The R64 checker
separately checks eight scientific files, nineteen inputs, eleven raw
captures and this report's relative links.

Governance returns 26 passes and the unchanged attribution, test-vacuity,
seal-provenance and relay-debt failures. The review counter is 249 merges
since the last review. Independent analytic review, the full certificate
of record and acceptance into the main bank remain outstanding.

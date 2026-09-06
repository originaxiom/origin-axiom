# R8 — the controlled electroweak-broken leading light-field theory

STATUS 2026-09-06: DRAFT, UNSEALED, UNEXECUTED. Paused for the bounded B1259
inference check in UPSTREAM_3_DESIGN.md; no R8 result is being claimed.

BANKED IDENTITY: R7 is a chosen compact-E6 4d action, with 294 real scalars,
209 positive tree modes, 66 gauge directions and 19 physical tree-zero
directions (octet 8, triplet 3, Higgs doublets 8). Its full one-loop force
and light curvatures are computed. R4's rank reduction is already realized;
RECOVERED_PHYSICAL_STEPS.md prevents resetting it to an absence.

PRIOR ART: fetched through 9a79adfd. New B1256--B1260 concern SL2/cohomology
and chirality, not a replacement scalar action; read but not merged.
Already-banked query `electroweak vacuum alignment`: 38 hits including settled
B900/B902, both read completely (frame/Kummer alignment, not this action).
The earlier sweep read B1250/B885/B889/B900/B902/B987, Higgs producers,
ladder/framework/campaign, PB-MASS/PB-VACUUM and the kill-graph hatches.
The nine-head charge-breaking/PQ/alignment query was PRESENT; one remote
'charge/breaking' hit was a hypercharge-chain substring, not an EW vacuum.
No broad absence assertion is made.

P0: continue R7's specified gauge/matter dynamics, not infer a source/action
map, compactification, family count or TOE. Source/action selection and I-26
remain separate obligations. No empirical mass or coupling enters.

## Expansion and inputs, declared before execution

For epsilon in {1/100, 1/400}, scale **every** potential coefficient by
epsilon, g=.5 sqrt(epsilon), every Yukawa=.25 sqrt(epsilon), mu=sqrt(epsilon).
Keep high VEV units and offset a=1/2 fixed. This is a family of different
theories, NOT RG evolution. Tree masses squared scale as epsilon, one-loop
forces/light masses squared as epsilon^2, normal displacements as epsilon.
Verify force scaling on all 294 components with freshly scaled spectral
instruments; do not assume it.

Keep all 19 canonical light real coordinates x=(O,T,u,d), dimensions
(8,3,4,4); complex doublet norms u^2/2,d^2/2. Build actual generator actions;
check closure, orthonormality, tree-kernel membership and gauge orthogonality.

## Heavy exchange and the entire quartic polynomial

The constraints c are quadratic, c(z0)=0 and J L=0. For each of the 190
quadratic monomials, compute its coefficient C2 in c(z0+Lx). Solve

    H0 N(x) = -2 J^T W C2(x)

using all 209 positive canonical modes. Then V4=(C2+JN)^T W (C2+JN).
Recover ALL quartic coefficients, not a neutral-direction sample.
Independently test the analytic response N_A=-(O^2+T^2)Y/10, other components
zero: it cancels the old adjoint norm; surviving new action residuals lie
in the light kernels and are orthogonal to J's image.

Prior/analytic candidate, checked coefficient by coefficient:

    V4 = .2/4 (u^2)^2 + .2/4 (d^2)^2 + .02/24 T^2 (u^2+d^2).

The weak factor follows from Tr27(t_a^2)=3 and
(sum T_a t_a/sqrt(3))^2 = T^2/12 on EACH actual doublet; verify this exactly
with symbolic matrices. Polynomial/kernel/gauge residual tolerance 1e-9.
Omitting heavy exchange must spuriously leave a positive pure-octet quartic
(deliberate bad control). Evaluate the original potential along
z0+t Lx+t^2 N(x), t=.04,.02,.01,.005, to check quartic convergence. No
small-step second-Hessian subtraction; R7's failed controls are untouched.

## Minima, not just negative mass signs

Recompute R7's reference mu=1 force/curvatures and compare its pinned output.
The leading light potential is

    Veff = epsilon^2/2 [mO O^2+mT T^2+mU u^2+mD d^2] + epsilon V4.

Its broken-minimum size is epsilon^3. If mO,mT>0, mU,mD<0 and the quartic
candidate holds, all leading minima have O=T=0, u^2=-epsilon*mU/.2,
d^2=-epsilon*mD/.2. Verify the full 19-variable gradient/Hessian using the
computed polynomial. Check BOTH neutral and charge-breaking relative
doublet orientations. If degenerate at this order, bank that degeneracy,
not 'EM selected' or 'EM impossible'. Count actual gauge/physical zeros.
Global here means the leading EFT on this high-scale branch, not all vacua.

## Gauge, fermion and phase tests

Add the leading R7 normal displacement to both broken representatives.
Compute all 78 compact gauge actions, their kernel and vector masses with
positive kinetic metrics. Exhibit Q=T3+Y on the neutral state and its failure
on the charged control. Compare projected SM masses with the full spectrum
along both epsilons. Expected leading mZ^2/mW^2=8/5 is conditional on the
chosen unified gauge metric, not an empirical prediction.

Compute all 27 fermion singular masses; compare the lightest 17 with K^T M_H K
on the old exact mixed-mass kernel. Report EVERY singular value, especially
the smallest: a leading rank-16 projection cannot drop a higher-order
seventeenth mass. No pole-mass claim.

Check the full classical common phase psi->exp(i alpha)psi and all four
scalars->exp(-2i alpha)phi, adjoint unchanged. Solve the exact SU5-commuting
Cartan compensation Gc S=Gc N=2. Determine residual doublet charges; project
the broken-phase tangent off the actual gauge orbit. Compute
Tr27[(1+Gc)t_color^2] exactly: if nonzero, the symmetry is anomalous, so no
exact quantum Goldstone or observational axion exclusion is claimed.
New symmetry-breaking terms would be additional inputs, not a hidden repair.

Primary context read 2026-09-06: Branco et al., arXiv:1106.0034v3 §§5.8--5.9,
6.7.2 (neutral/charged minima and phase symmetries); Martin arXiv:1406.2355v2
(Goldstone resummation). Do not import strict-positive-mass vacuum theorems
at a flat boundary or call negative unresummed Goldstone logs an instability.
No MSSM D-terms, inert parity, empirical scale or abs(negative m^2) added.

## Outcomes and honest prior

The analytic quartic candidate is plausible; independent elimination may
expose a missed term. The leading potential may admit neutral minima without
selecting them. Full spectra, phase breaking and convergence are outputs,
not success conditions to repair. Higher-order alignment, pole matching,
radiative closure, action selection, physical families and 4d gravity remain
full-goal duties. Seal design/code/tests before execution, refuse overwrite,
preserve failures, and keep the tree quiescent during tests.

# R9 — the leading infrared logarithm of Higgs alignment

STATUS 2026-09-06: final design before this calculation is executed.

BANKED IDENTITY: R8 (seal 6a02639d, result checkpoint 333d6033) solves the
complete leading 19-field light EFT of the chosen compact-E6 action. Its
neutral and charged orientations are degenerate, with 13 positive scalar
curvatures and six angular zeros. All 78 vector and 27 fermion masses are
retained; the neutral seventeenth light mass is subleading, not absent.
R7/R8's normal shift and heavy exchange are inputs, not work to omit.

PRIOR ART: fresh fetch reached origin/main 00f4fabe and ten heads. The
vacuum-alignment/charge-breaking/infrared-log/PQ/radiative-closure sweep is
PRESENT on all ten; zero matching deleted paths is not a deleted-content
absence proof. Already-banked query 'Higgs vacuum alignment' returns 74
hits and the five settled B1250/B885/B889/B900/B902 frame/dictionary arcs,
read in the preceding Higgs design/audit. B987 is reread completely here.
Targeted remote hits are B962's potential-selection literature, B889's
stored frame alignment, and a 'hypercharge/breaking' substring, not a new
calculation of this action. New upstream physics outside this target is
not merged or certified by this search. No broad absence claim is made.

Primary context: Branco et al. 1106.0034, sections 5.9 and 6.7.2;
Martin 1406.2355; Espinosa/Konstandin 1712.08068, section 2 and hard/soft
mass prescription; Manohar/Nardoni 2010.15806, introduction, section 2.3
and power-counting/matching discussion. A potential computed using an EFT
is not automatically the naive potential of an unmatched EFT. Keep the
tadpole/normal displacement and resum the already matched scalar masses.

## Bounded question, not the whole next-to-leading potential

Determine the coefficient of epsilon^4 log(epsilon) on R8's leading
doublet-radius manifold. Do NOT claim the full epsilon^4 finite term,
selection at epsilon=.01 or .0025, a pole spectrum, the UV action's complete
counterterm basis, source-derived inputs, or a TOE.

Every original tree coefficient scales as epsilon, g,y,mu as sqrt(epsilon).
Hard squared masses are order epsilon; soft squared masses order epsilon^2.
At mu^2=epsilon the one-loop soft contribution is

    epsilon^4/(64 pi^2) Str[mhat^4 (log epsilon + log mhat^2 - C)].

R8 already computes the hard one-loop quadratic coefficients and the
normal-tadpole correction. At its leading minima the resummed 19 scalar
eigenvalues are orientation-independent; verify this again, not just the
neutral/charged endpoints. Pure hard contributions at the matching scale
are analytic in light fields and have no log epsilon at this order.
Unknown hard quartic matching, triplet/heavy relaxation and allowed finite
counterterms can contribute epsilon^4 constants and MUST remain explicit.
Mixed hard/soft mass insertions belong in the resummed light quadratic
action, not a second independent copy of those insertions. Full matching
beyond these inherited leading terms is not certified by R9.

Assumptions for interpreting the logarithm: a fixed gapped high-scale
branch, the original absence of an order-epsilon alignment quartic,
bounded order-epsilon^2 hard Wilson coefficients as epsilon tends to zero,
and epsilon*abs(log epsilon) small. This is a family of theories, NOT a
measured RG trajectory. Nonperturbative anomaly effects are outside it.

## Exact all-orientation matrix tests

Use all eight real Higgs coordinates. Derive the actual SU2 intertwiner J
with tU^T J+J tD=0 and J^dagger J=I. Define rhoU=U^dagger U,
rhoD=D^dagger D, B=U^T J D, eta=abs(B)^2/(rhoU rhoD). Eta=1 is neutral,
eta=0 the charged control, identified by actual Q action, not naming.

Enumerate every polynomial invariant of degrees 1..4 on the two doublets
and their conjugates under actual SU2, hypercharge and R8's residual
common phase. Anticipate dimensions 0,2,0,4 with bases rhoU,rhoD and
rhoU^2,rhoD^2,rhoU*rhoD,abs(B)^2. This is the complete nondifferentiated
light-Higgs potential basis through degree four under those symmetries,
not the full 294-field UV counterterm basis.

Independently construct the exact four EW-vector mass matrix with positive
kinetic normalization and the exact 17x17 projected Weyl matrix from the
B883/B884 cubic and mixed kernel. Prove their fourth traces as polynomial
identities in ALL eight real fields, with independent gW,gY,y. Candidate:

    Tr MV^4 = (3 gW^4+gY^4)(rhoU+rhoD)^2/4
             +gW^2 gY^2*((rhoU-rhoD)^2+4 abs(B)^2)/2,
    Tr MF^4 = y^4*(8 rhoU^2+2 rhoD^2+8 rhoU*rhoD-8 abs(B)^2).

The predicted orientation coefficient in 3 Tr MV^4-2 Tr MF^4 is
6 gW^2 gY^2+16 y^4, giving 23/80 when gW=1/2, gY^2=3/20, y=1/4.
These are pre-execution analytic candidates, not values to repair into a
result. A wrong Weyl sign must reverse the pure-Yukawa preference.

Verify the radial scalar Hessian trace identity symbolically, and the
entire R8 scalar spectrum at eta=0,.1,.25,.5,.75,.9,1. Independently compare
EW projected masses to the original full generator action and Weyl
projection to the original 27 tensor on generic complex inputs, using
seed 2026090691; tolerances 1e-10 (matrix), 1e-9 (scalar spectrum).

## Logarithms, physical angular modes, and priced counterterms

Compute complete soft one-loop differences versus eta=0 at epsilons
.01,.0025,1e-4,1e-8. Subtracting two normalized potentials at different
epsilons must reproduce the symbolic log coefficient for every eta.
Keep finite soft terms separate; do not name them complete matching.
All 19 scalar, 17 Weyl and 12 gauge modes are counted, including zeros.
Negative physical squared masses must error, never be replaced by abs.

On fixed radii, rhoU*rhoD-abs(B)^2 is the charged-orientation penalty.
Compute its constrained Hessian using the radial Lagrange multipliers;
verify two positive charged eigenvalues rhoU+rhoD and six zero angular/
radial-extension eigenvalues in the eight-coordinate ambient description.
The gauge tangent is in its kernel; the neutral PQ tangent stays zero.
Interpret positive logarithmic lifting only if the coefficient has the
predicted sign. Do not assign a mass to the anomalous phase here.

At each finite epsilon include sensitivity controls cB=+/- .01 for the
uncomputed bounded hard term epsilon^2 cB abs(B)^2. They must demonstrate
that a finite-point verdict is not supplied by the log alone. Do not add
either control to the model or choose one for phenomenology.

Seal this design, code and tests with SHA256 before first execution. Refuse
output overwrite, serialize before exclusive open, retain failures without
editing sealed files, and keep the worktree quiescent during scientific runs.

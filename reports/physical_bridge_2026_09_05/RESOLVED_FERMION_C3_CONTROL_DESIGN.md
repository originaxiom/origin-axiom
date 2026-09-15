# R30 source-C3 control after an observed labeling error

2026-09-15. Separate follow-on design, before this control's first
execution. The original R30 source, tests, design and runs are frozen.

BANKED IDENTITY: R20 computes the full source-C3 fixed locus in the
original m202 presentation: (1,1), (zeta,zeta^-1), (zeta^-1,zeta).
PRIOR ART: HOLONOMY_EQUIVARIANCE.md section 2 and
holonomy_equivariance_word_control.py, read personally before this seal.

## The observed defect and its scope

R30's original character samples (zeta,1),(zeta^-1,1) have order
three but are NOT fixed by the source's order-three action. The
original test's "c3_orbit" name and design's "C3 pair" description
therefore do not establish source compatibility. Its actually tested
Fox/cohomology assertions remain correct for those generic characters.
This was caught by rereading R20, not by the original passing checks.
No failed assertion is rewritten, no new datum fitted, no claim that
the original run already covered the right points.

## Quantifier, control and prior

Compute the entire fixed locus of R20's actual C3 pullback on the
unitary rank-one character torus, then evaluate the frozen R30 complex
at EVERY fixed point. This corrects that precise subclaim, not a new
source selector or geometric certification. The honest prior is that
the corrected points retain the general theorem's zero finite-width
kernel; if they do not, the first failure stays and that application
is withheld.

Rebuild R from R20's checked word maps, set A=R^2, B=A^t-I, and
verify order three. The integer adjugate identity and |det B|=3
put every fixed point on the denominator-three grid; exhaust that
grid. Check the original (1/3,0) fails the invariance condition.
This rejection is essential: mere character order is not the action.

At each nontrivial fixed point check the ACTUAL Fox P=-2, relative
H*=(0,3,0,0), split H*=(3,3,0,0), resolved H*=0. At the trivial
point check the retained ordinary H*=(1,2,1,0). No numerical PDE,
full determinant, complete cusp limit or quantum completion follows.

Seal this control design, new producer and new tests; commit and push
before their first import/execution. Stage only after the original
quiescent broad run finishes. Run the new producer, three new tests,
then the original new-test file plus these tests together. The original
52-file broad run and its exact failure inventory remain separately
reported; a follow-on focused run is not called a 53-file broad run.

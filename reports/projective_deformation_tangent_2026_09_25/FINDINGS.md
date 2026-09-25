# F15: the full infinitesimal deformation space stays paired

September 25, 2026. Local fork audit/fork-2026-09-20.
Original seal **8fb4cbcd**; typed-zero implementation correction
**c3384646**, before the corrected execution.

## Result

**All three complex infinitesimal SL(4) deformation classes at each
exceptional background are even under F14's combined geometric
inversion and dualization. There is no odd class after removing gauge
directions.** This calculation releases the one-parameter/unipotent-
meridian restriction: it is the full representation tangent, not
another scan along the paired q curve.

The result is exact at BOTH real embeddings of BOTH exceptional fields.
It does not establish all-orders local rigidity, a global component
theorem, physical chirality, or a no-go for the arithmetic class.

| Points | rank B | rank relator differential | H1 complex dimension | Even | Odd |
|---|---:|---:|---:|---:|---:|
| q=7+/-4sqrt(3), chi=+/-i | 15 | 12 | 3 | 3 | 0 |
| q=17+/-12sqrt(2), chi=-1 | 15 | 12 | 3 | 3 | 0 |

Here H1 is the **adjoint deformation** quotient, not the defining-four
matter space. The latter still has one class in each dual sector at
these backgrounds. Three complex tangent classes are NOT three
generations, three normalizable scalar fields or an integrated moduli
space. The q direction is non-boundary and even modulo gauge; F11's
separate result that it is not a normalizable scalar modulus stands.

## 1. Why the zero odd count is not a gauge or slice artifact

The calculation uses all 30 tracefree generator variations. The exact
Fox differential is independently reproduced by differentiating the
actual 4x4 relator product over dual numbers. Its kernel is dimension
18; the conjugation image is dimension 15.

For F14's symmetric J, with LEFT logarithmic generator variations,

    T(u)_g = Ad(rho_g)(J^-1 u_g^T J).

The Ad factor is essential. T squares to one, preserves cocycles, and
acts on gauge variations through -J^-1 X^T J. In both eigenspaces the
cocycle dimension is 9. The even gauge subspace has dimension 6 and
the odd gauge subspace dimension 9. Thus the apparent nine odd
directions are ALL infinitesimal conjugations, not new backgrounds.

Explicit independent quotient columns, closure equations, eigenvalue
equations and ranks are checked. As a two-sided control, the trivial
rank-four representation yields 9 even and 6 genuinely odd H1 classes:
the instrument can detect odd directions when they exist. This is a
different, reducible control, not a candidate physical background.

The known q tangent is checked separately; because J varies with q,
its evenness is a quotient statement rather than a chosen-frame equality.

## 2. The first-order matter-retention condition

For every adjoint class u, compute the first-order change d1'(u) of
the defining-four coefficient differential and the actual dual
differential. If alpha is the existing matter class, its continuation
requires solving d1 beta=-d1' alpha. The obstruction is the image of
d1' alpha in coker(d1), which is one-dimensional here.

**Both sector obstruction rows are nonzero and proportional, with
joint rank one on the three-dimensional deformation quotient.**
Therefore the first-order simultaneous matter-retention kernel has
complex dimension two. There is no first-order direction retaining
one existing class but obstructing its dual. The q direction has a
nonzero obstruction on BOTH sides, in agreement with the isolated
exceptional q values already found in F11.

This is a tangent condition, not an actual two-dimensional family of
global mode-bearing backgrounds. A zero first-order obstruction can
still fail at higher order; end behavior, a global harmonic metric and
normalizability have not been extended off the existing backgrounds.

The dual variation is differentiated as rho^-T, not obtained merely
by changing chi. The obstruction is verified to vanish on every gauge
direction and to be unchanged when quotient representatives are shifted
by boundaries. Exact rows and quotient bases for all four cases are in
[EXACT_WITNESSES.jsonl](EXACT_WITNESSES.jsonl). Basis-dependent row
coefficients are not physical values; kernels and ranks are the content.

**Prior-result distinction:** equal matter--dual mode COUNTS were already
earned by F11's Euler/whole-boundary duality argument in its stated norm
class. We do not rediscover that as a new chirality obstruction. F15 adds
the full adjoint grading and the explicit first-order continuation map.
F14's geometric pairing is stronger than equality of counts because it
also pairs the classical response channel. Today that geometric symmetry
survives every infinitesimal SL4 deformation class at the tested points.

## 3. Verification and the failure preserved

The original run failed before producing any exceptional tangent result:
**13 failed, 1 passed**. Exact algebraic-number zeros were compared with
a Python integer zero, so the tracefree-coordinate guard rejected valid
inputs. [CORRECTION.md](CORRECTION.md) explains the implementation-only
repair; the original files and full failed output remain committed.

The corrected run reruns EVERY original test plus two field-adapter
controls: **16 passed in 25.80s**, exit 0. The sealed witness producer
also terminated with exit 0. A separate unchanged F14/F13/F12 recheck
has **76 passed in 226.10s**, exit 0. These are focused suites, not
the full repository/slow lane, external peer review or an empirical test.
Custody and exact commands are in [RECHECKS.md](RECHECKS.md).

No shared B number, main edit, push or PR. No fresh all-head sweep or
claim that this calculation was absent from every other seat. The
specific historical bodies and producers consulted are in DESIGN;
truncated broad searches are explicitly not counted as complete reads.

## 4. What changes next

1. Test whether this infinitesimal fixed-point result extends to formal
   or analytic deformations modulo gauge. A finite-order symmetry with
   trivial tangent action suggests an all-orders argument, but its
   deformation/gauge hypotheses and any convergence must be supplied.
   No claim of a nonlinear escape OR a nonlinear exclusion is made here.
2. The two matter-retention tangent directions remain registered, not
   discarded: determine integrability and end admissibility if they are
   pursued as constructive paired backgrounds. They are not presently
   evidence for asymmetric couplings.
3. Covers/additional characters, altered admissible end/source data,
   other components or a spontaneously asymmetric interacting phase
   change different assumptions. Each requires its own earned data.
   F11 already constrains counts on its finite-cover pullbacks, so merely
   recensus-counting those does not solve the response/phase question.

The constructive global backgrounds, localized paired matter, positive
six-sector gap and admissible classical interactions from F12--F14
survive. No object-selected action/end, quantum chiral phase, observed
SM phenomenology, gravity or completed TOE is supplied by this result.

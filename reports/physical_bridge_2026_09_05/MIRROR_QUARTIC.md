# R34: a genuine number-changing interaction, not yet a chiral phase

2026-09-19. Path-local PB-BOUNDARY / PB-ACTION work on the owned audit
branch. No shared B number, independent acceptance, main bank or TOE.

**Result:** integrating the proposed charged scalar produces a NONZERO
Spin(10)- and Lorentz-invariant four-fermion interaction which changes
mirror fermion number by four units, with Phi providing its gauge charge.
The commuting-spinor comparator vanishes; the actual Grassmann operator
does not. This removes a possible false algebraic kill of the interacting
route, without establishing the quantum phase that route requires.

[Design](MIRROR_QUARTIC_DESIGN.md), [authored argument](MIRROR_QUARTIC_PROOF.md),
[prior retrieval](MIRROR_QUARTIC_PRIOR.md), [frozen inputs](MIRROR_QUARTIC_INPUTS.json).
Original science was pushed and remote-confirmed at
`77fdcc15c3fdbe9962d7d970b780f6d8ea9e5dfd` before execution.

## What is now explicitly computed

Use R33's genuine H-subgroup fields, not an E6/Z3 fundamental 27:
psi=16_1, chi=conjugate(16)_-1, S=10_2, Phi=1_4. The fields and
four-dimensional interpretation remain ADDED inputs. For either
chiral internal spinor, let u_A,d_A be the two Weyl components and

    B_a = 2 sum_AB (Y_a)_AB u_A d_B,
    Q = sum_a B_a B_a.

In the declared Grassmann basis Q has 240 nonzero monomials and
the coefficient of u_0 u_1 d_14 d_15 is -32, for BOTH internal
chiralities. These are basis/normalization details of one operator,
NOT physical counts or constants. Every coefficient agrees between
the frozen exterior-product engine and an independent 2x2-minor
formula. Full 24-permutation antisymmetrization reproduces the witness.

All 45 Spin(10) and three complexified Lorentz generators annihilate
Q. Keeping just one vector component fails a non-Cartan test. Conversely,
sum_a(z^t Y_a z)^2 for ONE commuting 16-component spinor vanishes
coefficient by coefficient. It is a different tensor symmetry type;
using that Fierz cancellation to discard the Weyl-fermion interaction
would be incorrect. This is exact local algebra, not a spectrum.

For the stable quadratic scalar sector, define

    J = y_m B_m + conjugate(y_p) conjugate(B_p),
    D = r^2 - 4 kappa^2 |Phi|^2,
    r > 2 |kappa Phi|.

The induced Euclidean density is

    V_eff = -[r J dot J* + kappa Phi J dot J
              + kappa Phi* J* dot J*]/D.

The original stationary equations, substituted value and matrix inverse
agree exactly. For y_p=0 the number-changing term is

    -[kappa Phi y_m^2 Q_m + h.c.]/D.

It vanishes at kappa=0 or Phi=0, but not generically. Q_m alone has
charge -4; the full Phi Q_m is gauge invariant. This breaks the
fermion-only mirror phase, not H by an explicitly noninvariant term.
At nonzero y_p the same formula has ordinary-sector and mixed terms:
all ten coefficients in the bilinear-channel expansion are checked.
This is not a claim that those ten form an independent Fierz basis.
The pure ordinary-sector quartic is also explicitly nonzero.

The continuous rephasing kernel with both Yukawas, Dirac mixing and
phase locking is precisely the already gauged phase (1,-1,2,4) on
(psi,chi,S,Phi). Even setting y_p=0 does not restore an independent
continuous phase if finite mixing is retained. No full discrete or
flavour classification or loop-stability theorem is inferred.

## Physical limitations that determine the next step

The scalar elimination is EXACT for an ultralocal auxiliary Gaussian
model. In R33's propagating, self-interacting scalar theory it is
leading low-momentum TREE-LEVEL quartic matching, not a nonperturbative
equivalence. Scalar self-interactions, derivatives, loops and changes
to the source background must still be included.

The twenty real scalar eigenvalues are r plus/minus 2|kappa Phi|,
ten each. At their zero threshold the eliminated field becomes light;
the diverging formal coefficient cannot be used as a controlled proof
of strong gapping. The Gaussian determinant D^10 gives a factor D^-5:
if Phi varies, its regulated field-dependent normalization is NOT a
constant. No regulator-independent vacuum energy is extracted.

In assumed four dimensions the quartic is dimension six, while Phi Q
is dimension seven before fixing Phi. Weak-coupling matching does not
prove the needed strong interacting phase. Gauge symmetry still does
not select the mirrors: y_p suppression needs a derived form/locality
coupling and normalized overlaps, not a hand-set zero. Finite mixing,
anomaly matching, the C3 lift, source/end backreaction and the complete
cusp remain in the same model's accounting.

Thus this answers R33's local induced-operator question positively.
It does NOT answer whether mirrors gap without breaking Spin(10),
whether ordinary fermions survive, whether composite massless channels
remain, or whether the resulting continuum theory reproduces nature.

## Execution and preserved failures

| execution | outcome |
|---|---|
| [original native](MIRROR_QUARTIC_NATIVE_FIRST.json) | nine exact groups pass |
| [original tests](MIRROR_QUARTIC_TESTS_FIRST.txt) | 16 pass / 1 fail |
| [seven-file focused](MIRROR_QUARTIC_FOCUSED_FIRST.txt) | 126 pass / 3 fail, including R33's two |
| [normal-form v1 native](MIRROR_QUARTIC_NORMAL_FORM_FIRST.json) | exact residuals zero; wrong coefficient rejected |
| [normal-form v1 tests](MIRROR_QUARTIC_NORMAL_FORM_TESTS_FIRST.txt) | 8 pass / 1 failed exact-input guard |
| [eight-file focused](MIRROR_QUARTIC_FOCUSED_CONTROL_FIRST.txt) | 134 pass / 4 fail |
| [normal-form v2 native](MIRROR_QUARTIC_NORMAL_FORM_V2_FIRST.json) and [tests](MIRROR_QUARTIC_NORMAL_FORM_V2_TESTS.txt) | exact controls and all nine tests pass |
| [nine-file focused](MIRROR_QUARTIC_FOCUSED_CONTROL_V2.txt) | 143 pass / the same four failures retained |

The original failed comparison expanded a rational expression without
cancelling its common determinant. A separately sealed control proves
zero exact residual for the mirror limit AND the full ten-channel
numerator, including the zero-locking/background limits; a deleted
coefficient still fails. Rational equality is only on D nonzero, and
stable scalar elimination still requires the stronger positivity bound.

The first diagnostic's float guard checked AFTER subtraction, allowing
Float(1)-Integer(1) to lose its type at zero. V2 inspects both operands
first and passes the unchanged test population. All original source,
tests and output remain. This repeated normalization/guard failure is
an instrument-design defect, not a mathematical refutation to generalize
or a failure to erase. Control seals `fce21ad7` and `c1c5cf77` were both
pushed and remote-confirmed before their executions.

V1's focused run was started before its newly returned test failure was
inspected; that scheduling deviation is disclosed in the v2 design.
It changed no files and is not described as a halt-on-failure sequence.
[Receipts](MIRROR_QUARTIC_RECEIPTS.json) retain twelve raw captures and
exact test populations; the byte checker is not independent proof review.
No broad/full-suite green: R31's historical 24 failed/error IDs and
R33's halted-v1 test debt remain beyond this focused population.

Reporting gates are 26 pass / four inherited failing categories;
cumulative custody verifies 538 artifact paths and 134 distinct seals.
[Reporting details](MIRROR_QUARTIC_FINAL_CHECKS.txt) retain the exact
gate debt, transcript-whitespace exception and raw receipts.

## Next on the same physical mission

Derive the actual local form/source interaction and normalized matrix
elements for BOTH members of R31's light pairs. Its cutoff trials
cannot be silently treated as exact eigenstates. If a mirror-selective
coupling is obtained, carry its finite mixing and anomaly data into a
local positive-norm regulator and test symmetry order, fermion/boson
gaps, composite channels, cross-correlators and current response under
volume/cutoff control. Redo the coupled source/end solution in that
same theory. The conditional singular three/zero result is preserved,
not identified with the distinct resolved or interacting spectra.

This is progress on one load-bearing bottleneck. Spacetime dynamics,
quantum gravity, physical parameter selection and empirical predictions
are not replaced by the algebra completed here.

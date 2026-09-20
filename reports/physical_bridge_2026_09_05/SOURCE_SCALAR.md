# R37: a consistent added scalar sector, and a whole-mode selectivity control

2026-09-20. Path-local research on audit/physical-bridge-2026-09-05.
Six scientific files were committed, pushed and server-confirmed at
**f987ef16fe315ed221bb0ce1c1887b78be26bd4d** before execution.
No post-run scientific edits, shared B, independent acceptance or TOE.

**Result:** the declared tube-scalar extension preserves the resolved
source stationary point. Its action determines a weighted normalized
scalar mode, its two real mass branches and its interface coupling
identity. In the separate flat comparator, a diverging selected-pair
coupling ratio does NOT give a diverging whole-eigenspace preference:
other equally light modes retain ordinary-sector couplings. The
choice of interaction measure also changes the absolute limit.

[Design](SOURCE_SCALAR_DESIGN.md), [authored argument](SOURCE_SCALAR_PROOF.md),
[prior](SOURCE_SCALAR_PRIOR.md), [frozen inputs](SOURCE_SCALAR_INPUTS.json),
[producer](source_scalar.py), [first native output](SOURCE_SCALAR_NATIVE_FIRST.json),
[run receipts](SOURCE_SCALAR_RECEIPTS.json).
The formulas were already disclosed in the
[working note](SOURCE_SCALAR_WORKING_2026_09_20.md); this is an exact
verification/discrimination checkpoint, not a blind prediction.

## 1. Positive: the scalar is now derived within the specified source action

Keep R29's compact regulated H model and its Q=Phi=1_4 tube field.
Add S=10_2 with the specified positive weighted kinetic term, quartic
potential and charge-four locking term. Vary S, Q, h and the gauge
connection, INCLUDING the scalar dependence of the source density.

All ten complex S equations and the Q/h source derivatives agree
with direct Cartesian differentiation. The central current agrees;
the 45 D5 vector currents from S vanish at S=0. The old parallel-Q,
flat-A, h=dF point stays stationary with S=0: all 48 local Cartesian/
derivative/residual first variations vanish. The new S block has no
mixed quadratic term with the old variables there. This is stationarity
of this added action, not an assertion that all old/new fluctuation
sectors or the quantum vacuum are stable.

For a connected contractible tube with flat restricted connection and
positive weight sigma, the natural condition is sigma D_n S=0.
The scalar's lowest derivative mode is parallel constant, with

    s0 = 1/sqrt(W),     W = integral_U sigma dvol,
    m_x^2 = r - 2 eta f,     m_y^2 = r + 2 eta f.

Each branch has ten real components. The weighted gradient-form
argument establishes the constant mode; the symbolic Green check
retains arbitrary weight, volume density and connection. A missing
weight derivative fails. For the normalized hyperbolic tube W=L.
Canonical four-dimensional projection gives lambda_S/W and
eta/sqrt(W), retaining the input parameters and tube length explicitly.

The S block is positive for r>2 eta f. Equality gives a light scalar,
and below it the displayed stationary point is unstable in this block.
All three controls pass. A light/unstable scalar is not evidence for
the proposed symmetric mirror-removal phase. These conclusions do not
derive S or its potential from a parent action or the arithmetic object.

## 2. The internal interface cannot be treated as an outer boundary

R30's fermions transmit through the source-tube boundary. Integrating
R36's product identity only over that tube therefore retains the full
interface term, with b=sigma conjugate(s0) and w=u_i u_j:

    integral_boundary_U [b ((D_n w)/2 + q F_n w) - w D_n b/2].

At a true outer boundary the first flux can be cancelled by fermion
Robin data. At this artificial internal cut that would impose a new
domain and change the theory. The general weighted off-shell identity
passes the exact control; the explicit flat control integrates all six
faces and has nonzero flux. Omitting it gives an incorrect equality
between the two overlap matrices. No smooth zero-extension assumption
is used for a field defined only on a tube.

## 3. One selective pair is not a selective whole mode space

The comparator is flat T2_(2pi) times [0,1], trivial transport, F=0,
with absolute outer data. It is NOT the nonzero sourced hyperbolic
background. Take U=(-epsilon,epsilon)^2 times [0,1],
sigma=1/(4 epsilon^2), W=1 and s0=1. Keep the FULL eigenvalue-two space

    (cos x cos y, cos x sin y, sin x cos y, sin x sin y)/pi.

Every scalar and normalized one-form partner is checked, and every
entry of both overlap matrices is integrated, including off-diagonals.
Completeness here is only at eigenvalue two: lower modes still exist.
With a=1/2+sin(2 epsilon)/(4 epsilon), b=1-a and c=1/pi^2,

    M = c diag(a^2, ab, ab, b^2),
    P = c diag(ab, (a^2+b^2)/2, (a^2+b^2)/2, ab).

For the first pair M11/P11 grows as 3/epsilon^2 and M11 tends to c.
But the full limits are

    M -> c diag(1,0,0,0),
    P -> c diag(0,1/2,1/2,0),
    norm(M)_op/norm(P)_op -> 2.

The neighboring modes carry unsuppressed ordinary-sector couplings.
A complex mixing unitary changes entries but not either singular
spectrum. Thus the whole-space statement is basis invariant; selecting
one entry is not. The limiting M also has rank one, not a mass for
every mirror in this comparator. None of these matrices is identified
with a physical mass matrix or a nonperturbative quantum phase.

Keeping the SAME weighted scalar kinetic normalization but dropping
sigma from the Yukawa density multiplies both matrices by
4 epsilon^2. Both then vanish. A finite absolute interaction therefore
depends on the chosen source action, not merely on normalization.
No controlled zero-width QFT, actual hyperbolic nonselectivity theorem,
or universal localized-interaction no-go is inferred.

## 4. Effect on the mission and the next test

The [one-model audit](COMMON_MODEL_AUDIT_2026_09_20.md) makes the joins
explicit. R19's singular three/zero result remains valid on its domain;
R21's anomaly-free added EFT remains valid on its field list; R30/R31's
resolved pairs remain in the finite-width benchmark. This calculation
does not silently combine those different spectra into a chiral theory.

Completed sub-duty: scalar variation, normalization and interface
consistency for the stated added model, with a whole-eigenspace control.
Next: the parent/source-field and fermion dictionary, including all
required couplings, BEFORE another arbitrary profile or extra-field
scan. An allowed H representation is not yet a selected field. Test
elementary, localized and composite/auxiliary origins separately;
failure of one origin does not close the other routes.

Then compute or bound the complete actual low-energy overlap operators,
the interacting phase and the retained anomaly/end sector together.
The noncommuting PW alternative and fixed-prescription out-of-class
discrimination remain registered. No physical chirality closure,
empirical prediction, same-theory gravity or complete TOE is claimed.

## 5. Verification and preservation

- Native: all 13 exact check groups pass; 19.29 seconds.
- Whole new file: **17 passed**; 19.72 seconds pytest time.
- Eleven-file focused population: **175 passed, 4 failed**; 45.02 seconds.
  The four failed IDs exactly match R36/R34; no old test was edited or
  silently deselected. The new 17 are INCLUDED in the 175.
- Twenty-eight prior files are pinned and unchanged. The six scientific
  files remain byte-identical to their pre-execution seal. General
  domain arguments are authored, not independently accepted by these
  finite controls. There is no new global spectral certification.
- The first preseal custody run caught a missing artifact digest for the
  updated SEAL_LEDGER. Its exit-1 output is preserved alongside the
  corrected passing run; no science changed. The four prior governance
  failures and independent/full-suite banking debts remain disclosed.

Raw outputs are copied byte-faithfully apart from declared environment
path redaction; their exits and hashes are in the receipts. The original
focused output keeps its literal whitespace, including pytest's two
trailing-space lines. See [reporting checks](SOURCE_SCALAR_FINAL_CHECKS.txt)
for the final staged-state custody and governance checks.

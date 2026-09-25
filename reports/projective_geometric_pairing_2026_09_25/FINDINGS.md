# F14: geometry restores the matter--dual pairing

September 25, 2026. Local fork `audit/fork-2026-09-20`.
Original scientific seal **32864821**; implementation correction
sealed as **5fbf33bd**, before the corrected run.

## Verdict and what it changes

**The exceptional F12 backgrounds admit an exact geometric pairing
between their matter and dual sectors.** The inversion of both group
generators supplies the part missing from a purely fiberwise map.
Its actual cusp metric is compatible, and F13's uniqueness upgrades
the algebraic pairing to a unitary map of the completed backgrounds.
It preserves the complete operator domains and the whole normalized
parent interaction channel, not merely the free zero-mode count.

Therefore the present projective deformation **does not by itself
produce unequal matter--mirror coupling strengths** in these classical
backgrounds. F10's narrower positive remains true: there is no flat
FIBERWISE pairing at q!=1. The new map ALSO acts on the base manifold.
No old result is erased or reinterpreted as having proved more.

**Verification grade:** exact finite geometry/intertwiner/tensor checks
plus an authored analytic application of F12/F13. The corrected suite
has **40 passed**, and **75 unchanged antecedent checks passed**. The
initial run had **18 implementation failures, 9 passed, and was
interrupted**; its complete emitted diagnostics and original sources
remain preserved. No physical negative is based on those failures.
Global analytic proofs still require independent specialist review.

## 1. A short explicit witness, valid beyond sampled points

Let theta act by `m -> m^-1`, `n -> n^-1`. Put

    A=q/4, B=q/[2(q+1)], C=(q^2+1)/[2(q+1)],

        [ A  -A   B   C ]
    J = [-A   A  -B   B ].
        [ B  -B   1  -1 ]
        [ C   B  -1   1 ]

Exact symbolic calculation gives

    M^T J = J M,          N^T J = J N,
    det J = -q (q^2+q+1)^3 / [16(q+1)^4].

The determinant is nonzero for EVERY positive q. Equivalently,
`rho(g)^(-T) J = J rho(theta g)`. At both exceptional quadratics the
exact field solution is proportional to this same matrix and remains
invertible at BOTH real roots. Scalar fourth-root twists also work:
theta inverts their exponent, exactly matching dualization.

This is the distinction F10's trace obstruction could not test. Its
longitude word is palindromic, so theta sends it to its inverse. The
base operation cancels the longitude trace mismatch before the two
coefficient bundles are compared. The algebraic formula is all-positive-q;
the global analytic conclusion here uses only the backgrounds whose
existence and irreducibility were earned in F12.

## 2. The base operation is certified, not guessed

In the standard faithful geometric Riley holonomy, the matrix
`diag(-1,1)` conjugates each generator to its inverse. Its Mobius map
is `w -> -w`, its square is identity, and its induced cusp action is
`(x,y,z) -> (-x,-y,z)`. It is orientation PRESERVING on the three-
dimensional hyperbolic base. It is not being identified with physical
parity, time reversal or CP merely because it exchanges matter sectors.

All eight historical B1279 candidates were checked with exact complex
conjugators. Their positive powers lie projectively in the group,
which proves surjectivity as well as the generator action. This replaces
the earlier floating search for these particular certificates; it is
not a new small-word proof that no other isometry exists. One verified
positive pairing is sufficient for the conclusion.

The complete tested representation-level table is:

| Candidate maps | Untwisted intertwiner at p14 and p34 | chi=+/-i linear | chi=+/-i antilinear | chi=-1 linear/antilinear |
|---|---|---|---|---|
| id, T, R+, R- | None; equation rank 16 | None | None | None |
| theta, thetaT | One-dimensional, invertible; rank 15 | Yes | No | Both |
| G+, G- | One-dimensional, invertible; rank 15 | No | Yes | Both |

This table concerns the exact bundle equations. The full analytic
metric/interaction extension is exhibited for **theta**, which alone
suffices. All matrices, determinants and base certificates are retained
in [EXACT_WITNESSES.txt](EXACT_WITNESSES.txt).

## 3. Why the actual metric cannot quietly break this symmetry

An algebraic intertwiner need not preserve a chosen positive metric.
Here that obligation is explicitly discharged, rather than assumed.

On the F10 cusp, the unitary permutation R exchanging coefficient
coordinates 0 and 3 takes the theta-pulled reference connection to its
dual in all three directions, INCLUDING the radial component. Any
global intertwiner differs from this local one by

    Z=aI+bN+cN^2+dPi,       det Z=a^3(a+d).

This is the FULL common peripheral centralizer, not a trial ansatz.
Under the actual cusp frame scaling it becomes

    aI+bN/sqrt(u0)+cN^2/u0+dPi.

It and its inverse remain bounded. Thus the globally transformed
harmonic metric lies in the same bounded-distance end class. Normalize
J to determinant one; F13 uniqueness then makes the transformed metric
equal to the actual one. The induced map `U alpha = J theta*alpha` is
unitary, intertwines the differentials and their actual adjoints, and
preserves the complete ordinary-L2 domains. The paired Hodge operators
are isospectral, including nonzero eigenvalues and multiplicities.

The same argument applies to the exterior six. No arbitrary finite
boundary condition, selected mode truncation or uncomputed profile
normalization enters this result.

## 4. The pairing acts on the actual parent vertex

The exterior-volume identity tracks `det J` explicitly; after the
metric-compatible determinant-one normalization, the full 4--4--6
coefficient tensor is preserved. The base orientation is preserved too.
In the E8 parent an exhibited product of four root reflections flips
axes 0,5,6,7: it exchanges both D5 spinor halves and the A3 four/dual-
four. This has a genuine compact-group Weyl lift preserving the bracket
and norm, not just matching representation dimensions.

Consequently whole normalized vertex tensors in corresponding spaces
have equal strengths. With F13's actual L2 bilinear sources and gapped
mediator, the complete internal scalar-block responses satisfy

    <U6 j,(p^2+2 Delta6_dual)^-1 U6 j>
      = <j,(p^2+2 Delta6)^-1 j>.

A selected profile could show different individual overlaps if it was
not paired consistently. That would not demonstrate a hierarchy of the
whole theories. Conversely this equality says neither that j vanishes
nor that every conceivable source/end/quantum extension is symmetric.
It is not a calculation of the complete quantum propagator or measure.

## 5. Strategic consequence and surviving work

The lesson is precise: **a coefficient-level symmetry obstruction is
not a physical symmetry obstruction when geometry can participate.**
The new metric uniqueness result makes the restored symmetry robust;
it does not make the earlier construction useless.

Surviving positives: an actual global classical bulk background,
normalizable matter and dual modes, a gapped six mediator, a defined
nonlinear fluctuation class and convergent parent interactions. All
remain mathematical-physics results inside explicitly supplied inputs.
The construction is still vector-like, not a completed chiral model.

Next discriminators, before another overlap scan:

1. Test the actual representation deformation equations for directions
   that break this geometric duality, rather than merely moving q along
   the now-paired curve. An odd infinitesimal direction would still need
   nonlinear integrability, end compatibility and a retained spectrum.
   Adjoint deformation cohomology must not be confused with matter H1.
2. Separately test additional cover/character/end choices against their
   lifted geometric symmetries. No claim about all finite covers or
   all their characters is made by this base-member calculation.
3. A spontaneously asymmetric interacting phase remains logically
   possible despite an exact classical symmetry. It requires an actual
   phase/gap and anomaly analysis, not inference from an allowed vertex
   or an arbitrary choice of one member of a paired basis.

No new physical action, arbitrary asymmetry or empirical number was
introduced to escape this result. Parent/base/end selection, the
observed generations and gauge breaking, gravity, quantum completion
and measured predictions remain outside what F14 establishes. The
TOE objective is not achieved, and no universal chirality kill is made.

See [PROOF.md](PROOF.md) for the complete conditional analytic bridge,
[CORRECTION.md](CORRECTION.md) for the preserved implementation failure,
and [RECHECKS.md](RECHECKS.md) for seal and execution custody.

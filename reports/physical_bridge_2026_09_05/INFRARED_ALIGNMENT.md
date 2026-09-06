# R9: the leading infrared logarithm favors the neutral orientation

R8's leading degeneracy has a computed **neutral-favoring logarithmic
correction**. In the specified weak-coupling family, the exact coefficient
of the relative-Higgs invariant is positive, while log(epsilon) is negative.
The corresponding angular correction gives a positive restoring term to
the charged pair that was flat in R8. The phase direction remains flat at
this order; R8's nonzero anomaly is not erased.

This is a conditional **asymptotic leading-log result**, not the full next
order, selection at either earlier parameter point, a pole spectrum, or a
source-derived TOE. Finite matching and relaxation terms are still to be
computed. Once the UV action and renormalization conditions are fully
specified, those matching terms are calculable; **uncomputed does not mean
intrinsically arbitrary**.

Design, source and eight tests were sealed at **dac87d46**, with both literal
provenance fields, before execution. The first run succeeded in 4.87 s.
[Full output](infrared_alignment_first_run.json), [exact instrument](infrared_alignment.py),
[pre-execution design](EXTENSION_7.md), and [captured checks](INFRARED_ALIGNMENT_CHECKS.txt)
retain the computation. R8's source, result and report hashes are unchanged.

## 1. The invariant being selected is derived from the actual actions

Use the actual U,D doublets in the B883/B884 representation, the mixed
17-dimensional fermion kernel and R8's physical scalar coordinates.
Solving tU^T J+J tD=0 for all weak and hypercharge generators gives a
one-dimensional intertwiner space, normalized by J^dagger J=I. Define

```text
rhoU = U^dagger U,   rhoD = D^dagger D,
B = U^T J D,        eta = abs(B)^2/(rhoU*rhoD),   0 <= eta <= 1.
```

The actual Q action identifies eta=1 as neutral and eta=0 as the charged
control. Color annihilates both doublets. The representative's Q-action
norms are exactly zero numerically at eta=1 and .2282942061 at eta=0,
in the unscaled light coordinates.

There is also an exact completeness check on the nondifferentiated
**light-Higgs** potential through degree four. Enumerate all monomials in
the two doublets and their independent conjugates; impose actual SU2,
hypercharge, and the residual classical common-phase charges -18/5,-12/5.

| polynomial degree | all monomials examined | invariant dimension | spanning invariants |
|---|---:|---:|---|
| 1 | 8 | 0 | none |
| 2 | 36 | 2 | rhoU, rhoD |
| 3 | 120 | 0 | none |
| 4 | 330 | 4 | rhoU^2, rhoD^2, rhoU rhoD, abs(B)^2 |

The matrix kernel and the displayed basis span agree exactly. This retains
the alignment operator instead of silently assuming it forbidden. It is
not the complete 294-field UV counterterm basis, and it does not discard
the octet/triplet or their interactions.

## 2. Exact all-complex-field fourth traces

Construct the full four-by-four EW vector mass matrix and 17-by-17 projected
Weyl matrix from the actual generators and cubic. All eight real Higgs
coordinates remain symbolic. Independent couplings gW,gY,y are retained;
y is the model's common Yukawa coefficient, not a general flavor matrix.
The exact polynomial identities are

```text
Tr MV^4 = (3 gW^4+gY^4)(rhoU+rhoD)^2/4
          +gW^2 gY^2*((rhoU-rhoD)^2+4 abs(B)^2)/2,

Tr MF^4 = y^4*(8 rhoU^2+2 rhoD^2+8 rhoU*rhoD-8 abs(B)^2).
```

Both full symbolic remainders are zero, not just endpoint comparisons.
Generic complex-field checks independently rebuild the matrices using the
original 78-generator action and 27-component Yukawa tensor; discrepancies
are below 1.56e-17. The EW kinetic Gram is diag(1,1,1,5/3), establishing
gY^2=3 gW^2/5 in this chosen unified metric.

The orientation coefficient is extracted from the **computed** supertrace,
not supplied as a label:

```text
coefficient of abs(B)^2 in [3 Tr MV^4 - 2 Tr MF^4]
    = 6 gW^2 gY^2 + 16 y^4.
```

It is nonnegative in this common-Yukawa texture and positive if either
gW*gY or y is nonzero. For the fixed reference couplings gW=1/2,
gY^2=3/20 and y=1/4, it is **23/80**. Reversing the Weyl sign in the
computed trace reverses the pure-Yukawa coefficient, +16 to -16, so the
statistics sign is a tested, consequential part of the calculation.

This is a standard gauge/Yukawa quantum mechanism instantiated and checked
on this model, not an established E6-specific signature or novelty claim.
The 17th light fermion contributes zero to the leading projected trace;
R8's nonzero subleading mass remains in its full spectrum. An order
epsilon^(3/2) mass contributes only at order epsilon^6 log(epsilon) to
this determinant, not at the order considered here.

## 3. Scalars, tadpoles and the power-counting boundary

All 19 resummed scalar modes are included, with R8's heavy exchange and
normal-shift correction. The four-component radial-block identity

```text
Tr[(k+lambda*x^2) I4 + 2 lambda*x*x^T]^2
    = 4 k^2 + 12 k lambda*x^2 + 12 lambda^2*(x^2)^2
```

is verified symbolically. Along R8's fixed-radius manifold the complete
scalar spectrum is orientation-independent; seven independent eta checks
give differences below 1.39e-17. The scalar logarithm therefore does not
change the relative-orientation coefficient. The six leading zeros are
retained, not replaced by absolute values of tachyonic squared masses.

The expansion distinguishes hard squared masses O(epsilon) from soft
squared masses O(epsilon^2), at mu^2=epsilon. The latter produce

```text
Vsoft = epsilon^4/(64 pi^2)
        Str[mhat^4 (log epsilon + log mhat^2 - C)].
```

R7/R8's inherited quadratic matching and normal tadpoles are already in
mhat_scalar^2. Their insertions must not be counted a second time. Pure
hard terms are analytic in the light fields at the matching scale on a
fixed gapped branch; their logs involve fixed mass ratios rather than
log(epsilon). Hard finite quartics and relaxation of heavy/triplet fields
can still affect the **finite** order-epsilon^4 orientation potential.
Further soft-loop corrections are suppressed in the stated limit
epsilon*abs(log epsilon) -> 0. This is power counting under the declared
matching assumptions, not a newly completed full-theory matching proof.

The heavy-field stationary condition, rather than simply deleting heavy
fields, is essential when comparing effective potentials. See
Manohar/Nardoni, [section 2.3, equation (2.17)](https://arxiv.org/pdf/2010.15806).
Hard self-energy resummation and soft/hard separation are discussed by
Espinosa/Konstandin, [section 2](https://arxiv.org/pdf/1712.08068).
These results motivate the treatment; they do not certify this particular
E6 model's uncomputed finite matching.

## 4. The sign, the charged pair, and what is actually selected

Let rhoU=epsilon*rU and rhoD=epsilon*rD on R8's leading minimum, with
rU=.045711665332 and rD=.052118244549. The neutral-minus-charged logarithm is

```text
Delta Vlog = epsilon^4 log(epsilon) C0*rU*rD,
C0 = (23/80)/(64 pi^2) = .000455153754643,
C0*rU*rD = .00000108436365426.
```

Thus Delta Vlog < 0 for 0 < epsilon < 1: the logarithmic term favors
eta=1 throughout the continuous orientation interval. The exact quartic
identities, not the seven numerical angles, establish this sign. The full
soft determinants at four predeclared epsilons independently reproduce
the log slope, with maximum discrepancy below 3e-21.

| epsilon | neutral-minus-charged logarithmic energy | complete soft one-loop difference (not full matching) |
|---|---:|---:|
| .01 | -4.99368e-14 | -9.92449e-14 |
| .0025 | -2.53786e-16 | -4.46396e-16 |

To isolate angular restoring forces use the fixed-radius penalty
P=rhoU*rhoD-abs(B)^2. At a neutral state P and its gradient vanish; its
ambient extension has two positive Hessian eigenvalues rhoU+rhoD and six
zeros. The computed gauge and phase tangents lie in its kernel. Therefore
the charged pair receives the leading-log squared-curvature contribution

```text
Delta m_charged^2 = -epsilon^3 log(epsilon) C0*(rU+rD),
C0*(rU+rD) = .0000445276507986 > 0.
```

These are angular effective-potential curvatures after enforcing the radial
stationarity condition, not complete pole masses or a recomputed full
next-order vacuum. The neutral phase remains flat in this calculation;
R8's anomalous classical phase is not promoted to an exact quantum Goldstone.

The asymptotic interpretation additionally assumes the fixed high branch,
no order-epsilon alignment quartic (as in the stated tree action), and
bounded order-epsilon^2 hard matching coefficients. Under those conditions
the logarithm supplies the dominant orientation preference as epsilon
decreases. This does not certify either existing finite parameter point
or compare all high-scale branches.

## 5. The remaining term is priced, not declared unknowable

At the matching scale write the as-yet-uncomputed alignment term as
epsilon^2 cB abs(B)^2. For the predeclared sensitivity controls cB=+/-.01,
the coefficient C0 log(epsilon)+cB has opposite signs at both .01 and
.0025. These controls demonstrate that a **log-only finite-point verdict**
can be changed by a finite term; neither value is inserted into the model.
The known finite soft contribution is separately retained in the output,
not mislabeled as the missing hard term.

cB is calculable for a specified complete UV renormalization prescription;
changing it is a change of matched theory or boundary inputs, not evidence
of an unavoidable ambiguity in a fixed model. R9 does not compute it and
does not prove it can be dropped. Nor does the invariant-basis enumeration
derive its coefficient from the originating mathematical object.

The next bounded task is the finite alignment calculation for the existing
action: hard one-loop quartic matching, the field-dependent normal response
and triplet relaxation, with the light resummation handled consistently.
Use the computed logarithm as an independent subtraction/control. Keep
every residual scalar mode, the smaller seventeenth fermion mass, and the
parameter/matching conditions before attempting empirical comparison.

## 6. Verification and continuity

New tests: **8 passed in 5.89 s**. Combined physical-audit and selected
upstream tests: **107 passed, 3 failed in 94.59 s**. The failures remain the
original G2 NumPy-key exporter and the two original R7 small-step controls;
their separately sealed repairs pass. No skip, weakened tolerance, edited
sealed source, overwritten first run or full-suite certificate.

Fresh history search covered ten fetched heads, including origin/main
00f4fabe; the query was PRESENT, not ABSENT. The relevant frame/dictionary
and Higgs-source results remain distinct from this action calculation.
Newer unrelated upstream work was fetched, not merged or independently
certified in R9. The known 14-to-12 reduction and all R4--R8 positives remain.
Finite selection, action/input derivation, physical families and gravity
are still outstanding parts of the user's overall physical-theory goal.

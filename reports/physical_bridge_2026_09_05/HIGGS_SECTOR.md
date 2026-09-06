# R7: two light doublets, actual Yukawa support, and a radiative instability

The priced extension supplies **two complex light Higgs doublets**, with
all colored scalar partners tree-massive and the actual mixed light-fermion
kernel coupled by the invariant cubic. Its complete quantum calculation
retains positive octet/triplet curvatures. At the reference point both Higgs
doublets acquire negative leading mass squared: the Higgs-zero background
is unstable in this approximation, not a completed electroweak vacuum.

The result is progress from the original Higgs-less representative, with a
real next question rather than a phenomenological success claim. The new
singlet shifts are large at the illustrative coupling point; they cannot
be silently omitted or called controlled. R4/R5/R6 remain separate, preserved
results for the old model.

## 1. What was added, not derived

Two complex scalar 27s U,D, with canonical kinetic terms, and

```text
V_H = kU ||(A-a I)U||^2 + kD ||(A+a I)D||^2
    + xi ||C(phi1,D)||^2 + lU (U^dagger U)^2 + lD (D^dagger D)^2.
```

Use a=1/2, kU=kD=xi=.02, lU=lD=.2, old lambda=.2, g=.5, and all four
Yukawa coefficients .25 for one Weyl 27. These are renormalized model
inputs, not observed values. Other allowed operators are zero at the
declared scale, with no protection asserted. The a-to-adjoint-VEV relation
is a **light-mode tuning**, not a natural hierarchy mechanism.

Each term is gauge invariant, nonnegative and degree at most four. Therefore
the old zero-potential family remains a global classical minimum at U=D=0.
The construction does not select that family from all classical branches.
The added cubic Yukawas are included in the one-loop force; no inert parity
is invented to discard U,D singlet tadpoles.

Prior B884/B987 already identify doublets inside a 27 and the cubic Yukawa
support. B978 prohibits an adjoint coupling to two 27 fermions, not this
scalar mass splitting. B298/B299's triality choice is retained as an input.
The history search returns PRESENT on all nine fetched heads; see
[design](EXTENSION_5.md), including its explicit literal/regex search repair.

## 2. Full classical scalar spectrum and identification

The expanded instrument has **294 real scalars**, 439 real constraint
components and the complete kinetic metric. Its positive tree Hessian has
rank **209**; the 85 zeros split into 66 gauge Goldstones, eleven old
octet/triplet directions and eight new real Higgs components. No mode is
removed from the count. The actual raising/lowering and hypercharge actions
identify a color-singlet weak doublet in each new field:

| field | hypercharge | B883 weight indices | real light components |
|---|---:|---|---:|
| U | +1/2 | 8,9 | 4 |
| D | -1/2 | 21,22 | 4 |

The cubic-norm term removes the duplicate D doublet. Setting xi=0 restores
four extra real zero modes (kernel 89); shifting a to .4 removes all eight
Higgs zeros (kernel 77). These are tested parameter changes, not relabelings.
The smallest positive new scalar squared mass is 0.000555555556 in VEV units.
Complex compact rotations verify covariance of both new mass matrices.

## 3. Project the physical light fermions before calling a Yukawa physical

The old S/N mass has a 17-dimensional kernel with a nontrivial mixed 5bar.
The new calculation constructs its kinetically orthonormal matrix K and
uses **K^T M K**, not a fixed inherited list of matter weights.

Neutral Higgs components are U index 8 and D index 22. Each projected
matrix has rank eight; together their rank is **16**. The charged blocks
have ranks three for up-type, three for down-type and one for charged
leptons. The three-dimensional neutral block has rank two. The exact
matrices and their charge-conserving action are retained in the output.

This establishes leading small-VEV Yukawa support for the chosen one-family
model. It is not three generations, measured flavor, a neutrino fit, or
exact heavy-state integration at a finite electroweak VEV.

## 4. Quantum feedback: positive angular lifting and negative Higgs curvature

All 294 scalar, 78 vector and 27 Weyl modes enter the same MS-bar/Landau
one-loop convention as R5. The complete 294-component force is calculated
before projection. Its entire tree-kernel component vanishes numerically;
inversion of the 209 positive modes solves stationarity, including the new
Higgs singlets, with maximum residual below 2.9e-15 in the three runs.
The shift preserves the actual SM action.

The complete eight-by-eight real Higgs curvature is computed, including
all mixings and the normal-shift contribution. For these inputs it is
diagonal to numerical precision, with four copies of each eigenvalue:

| mu | m_U^2 | m_D^2 | each new U,D singlet-shift norm |
|---|---:|---:|---:|
| .5 | +0.001743146654 | -0.000634073280 | 0.236924519 |
| 1 | -0.018284666133 | -0.020847297820 | 0.430910682 |
| 2 | -0.038312478919 | -0.041060522359 | 0.624896845 |

Units are the original scalar VEV, not GeV. These scale checks keep the
displayed renormalized coefficients fixed; they are **not** RG evolution
including all allowed counterterms. Their variation demonstrates why the
Higgs mass needs a renormalized-input/matching treatment. It does not negate
the result at a specified set of inputs, and does not predict a measured
electroweak scale.

At mu=1 the U,D singlet shifts are both approximately
`-0.304699865 (S+N)`. Calling these light doublets inert would have lost
this large effect. The reference old scalar shifts are about 14.9% as well.
A negative leading Higgs curvature at such a reference is an instability
diagnostic of the Higgs-zero expansion, not a certified broken-phase vacuum
or a precision-controlled spectrum.

The expanded **octet and triplet** curvatures stay positive:
**0.007519833193 and 0.007366050627**. The curved-path/normal-shift identity
is checked again, so no correction is added twice.

Exact four-Cartan-variable subtraction also gives the extra real-scalar
fourth-mass traces, with kU=kD=xi=1 and N=Tr A^2:

```text
U: 27/8  + 3 N    + N^2/6
D: 267/8 + 13 N/3 + N^2/6.
```

Both remainders are exactly zero; at N=5 they are 541/24 and 1421/24.
Restoring the common .02 coefficient multiplies each by .02 squared.
Hence the added scalar contribution does not spoil R5's one-loop angular
scale independence. This statement concerns the old adjoint orientation
family, **not** the Higgs masses or the full effective potential.

## 5. Failed control retained; repaired without changing physics

The design/code/tests were sealed at a3f8f786. The first run failed a
second-Hessian finite difference at step 1e-4 and produced no physics output.
Its empty result file and failure transcript are preserved. A new control
wrapper, sealed at f5c40f4f, exploits the Hessian's exact quadratic dependence:

| centered-difference step | maximum second-derivative discrepancy |
|---|---:|
| 1e-4, original | 1.84087162e-6 |
| 1e-3 | 8.45895709e-9 |
| 1e-2 | 1.25093713e-10 |
| 1, polynomial polarization | 1.06581410e-14 |

This confirms amplified floating-point subtraction error, with the original
tolerance and all scientific functions unchanged. The repaired full run
completed in **20.33 s**. The original failing controls still fail visibly:
the focused R7 run is **2 failed, 8 passed in 21.48 s**, including the two
new passing controls. No skip, xfail, tolerance relaxation or source rewrite
was used to manufacture an all-green certificate.

Evidence: [full result](higgs_rerun_1.json), [original failure](HIGGS_FIRST_FAILURE.txt),
[first test output](HIGGS_FIRST_TESTS.txt), [repair design](EXTENSION_5_REPAIR.md),
[unchanged scientific code](higgs_sector.py), [control wrapper](higgs_control_repair.py).

## 6. Next physical question

Continue to the small-coupling broken-phase effective theory, retain the
actual light fields, and compute the electromagnetic stabilizer rather
than choosing a neutral-looking direction by its label. Check orientation
selection, every residual scalar mode, the force/scale hierarchy and the
actual vector/fermion thresholds. If the leading theory leaves degenerate
orientations, that is a bounded higher-order task, not a programme no-go.
The added inputs still need restriction or derivation; this conditional
model does not pay for observed matching, families, gravity or a full TOE.

## 7. Follow-through, 2026-09-06

[R8](BROKEN_VACUUM.md) now computes the full leading 19-field light potential,
including heavy exchange and the complete light quantum curvature. Neutral
minima preserve actual color/EM but are degenerate with charge-breaking
minima at this order. Its full neutral fermion matrix has rank 27 at the
evaluated backgrounds; the smaller seventeenth light mass is absent only
from the leading rank-16 projection, not from the complete matrix. This
advances the next question above without rewriting R7's sealed evidence
or claiming complete quantum-vacuum selection or measured matching.

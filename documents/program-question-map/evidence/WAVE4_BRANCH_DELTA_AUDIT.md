# Wave 4 branch-delta audit

**Audit date:** 2026-08-26

**Purpose:** reconcile every source branch that advanced after Wave 3 before changing the
canonical question map.  This file records immutable inputs and semantic dispositions; it is not
a substitute for the cited certificates.

## Immutable source locks

```text
origin/main                         68383e80718e732e7cf5b9e57077a19dff753ad6
origin outside-bench               59680460721a0b9e4f672ad6e997724c226ceb56
origin paper/structure-genesis     61a243c65f1a84c700e3c3d9755b11c30a5f0699
golden_gate hostile handoff        15b3366937af19e643a54d564883253f013fc651
codex precursor for this wave      a1179de38d197f43d0f114f1c6b45dd6c2386441
```

At these locks, the terminal `main` and paper commits add process corrections only.  Main B8140 fixes a relay-only
test-selector cost bug and withdraws two unsupported run-log details.  Paper B8141 identifies
tests that read gitignored logs.  Neither changes a mathematical or physics verdict, so neither
gets a new canonical mathematics row.

## Exact delta dispositions

| source/cell | independent audit result | map effect |
|---|---|---|
| main B1153 / outside memo 54 | The complete fixed scheme has support at three points and length four: a simple conjugate pair plus the multiplicity-two origin.  The constant formula `tr(ab^-1)=3-kappa` has defect `x^2-4` on the Riley component. | OA-C1082 remains `REFUTED` with complete evidence; OA-C1083 becomes `REFUTED`; OA-C1092 records the correct global deck theorem. |
| main B1151/B1153 / outside memo 55 | The frozen data and all distances reproduce dependency-free.  The merged list rejects the one-Wigner proposal and is relatively closer to a two-component Wigner-surmise renewal approximation. | OA-C1077 becomes `REFUTED`; OA-C1093 is a separate `EMPIRICAL` row.  No exact GUE or independence theorem is claimed. |
| Paper I | The period-one determinant characterization, trace-only Smith form and period-two torsion formula are exact.  The `m=12` discrepancy is three proper classes versus two full-GL classes under an explicit determinant-minus-one swap. | OA-C1094--OA-C1097. |
| Paper II | Given the specified principal-2T placement, the fixed algebra is toral.  Its six zero roots are A2; all 120 E6 A2 subsystems form one explicit Weyl orbit.  The rational arrangement therefore gives the exact Qbar flat lattice: 109 flats and eleven dimensions. | OA-C1098.  The paper's older three-prime-only paragraph is stale.  OA-C0006 remains `CONDITIONAL`. |
| Paper II distinguished plane | The exact charge-side characteristic polynomial is one irreducible cubic to exponent sixteen and generates the recorded cubic field. | OA-C1099. |
| outside memo 56 plus addendum | In a fixed D5 x U(1)_psi frame, the 45 cubic supports are `40+5` and conserve frame parity.  The beat mixes the frame class/parity on 6 of 27 basis columns while preserving the one tested lock. | OA-C1100 and sharper OA-C0014 evidence.  “Only stable Z2” is restricted to the two gradings actually tested. |
| Paper III | The direct identity is an M-character Euler product in `Re(s)>2`, hence safely at integer `k>=3`.  `k=2`, the actual cusped graviton determinant and the infinite-limit step remain absent. | No new row.  OA-C1059--OA-C1062 retain their statuses and receive no physical upgrade. |
| Paper IV scale theorem | Normalized volume is an isometry invariant and changes by cover degree, refuting the literal cover-indistinguishability inference.  Conversion to a physical unit still needs an external scale. | OA-C1101 `REFUTED`; OA-C1029 unchanged. |
| Paper IV census family | B8128 stops after zero-based index 1200 and the paper verifier hardcodes fourteen names.  Exact regular-shape gluing for `s955` at index 1256 supplies a counterexample. | OA-C1102 `REFUTED`; OA-C1103 is the corrected full-family `OPEN` computation. |

## Hostile fences retained

- A polynomial identity on a parabolic divisor is not an identity on the full character
  component.
- A Wigner-surmise renewal CDF is not the exact two-GUE point-process nearest-neighbour law.
- A fixed internal Lie frame is not an object-selected frame, and a cubic support hypergraph is
  not a four-dimensional portal or dark sector.
- Centralizer dimensions are not gauge groups, fields, particles or masses.
- Normalized hyperbolic volume is a number fixed in curvature units; a physical conversion scale
  is a different datum.
- A bounded census prefix is not an exhaustive family, even when every listed member is correct.

## Resulting registry state

Wave 4 contains 120 typed rows:

```text
45 PROVED
40 REFUTED
13 CONDITIONAL
16 EXTERNAL_BLOCKER
 2 EMPIRICAL
 4 OPEN
```

The live computations are OA-C1067, OA-C1069, OA-C1074 and OA-C1103.  The drop from five to four
does not move the physical endpoint: the missing four-dimensional realization, selected chiral
zero-mode spectrum, vacuum/dynamics, and normalized parameter values remain explicit downstream
gates.

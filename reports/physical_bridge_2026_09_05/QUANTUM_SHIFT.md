# R6: the leading quantum shift preserves the SM branch

The full first-order stationarity equation is solved in the chosen R4/R5
theory. At the reference point the two scalar-27 shifts are **14.9%**, above
the predeclared 10% small-displacement diagnostic. The two weaker-coupling
controls give **3.72% and 0.930%**, preserve the actual SM action, and retain
R5's positive leading angular lifting. This supports a small-coupling local
branch; it is neither a quantitatively tiny reference-point correction nor
a failure of the programme.

This is a leading MS-bar, Landau-gauge displacement in arbitrary VEV units.
VEV coordinates and shifts depend on gauge/renormalization conventions;
they are not measured masses or gauge-independent observables. No complete
loop pole spectrum, all-order solution or global minimum is certified.

## What was computed

All **186 real components** of the one-loop scalar, vector and Weyl-fermion
gradient were evaluated before projecting any direction. The complete tree
Hessian follows from all 275 quadratic constraints, including their second
derivatives. Differentiating only the on-vacuum expression `2 lambda J^T J`
would omit an essential term in its normal derivative. The independent
full-Hessian finite difference agrees to 1.17e-10; the deliberately omitted
term gives a radial discrepancy of 1.6 and is detected.

The gradient has negligible projection on the entire 77-dimensional tree
kernel, not just on its 66 gauge directions. The inverse on the 109 positive
normal modes gives `H0 delta z + grad V1 = 0` to 1.23e-15 at the reference
point. The SM-singlet scalar subspace is exhibited as **13 real dimensions:
four gauge and nine physical normal directions**. The solve was not restricted
to three guessed radial variables. Actual generator actions annihilate the
shift, and the shifted vector mass matrix retains twelve zero modes.

At the reference point, in the existing S,N basis,

```text
delta phi1 =  0.148780038239 S - 0.003808748315 N
delta phi2 = -0.003808748315 S + 0.148780038239 N.
```

The adjoint also shifts in SM-singlet Cartan directions. The full coordinate
vector and all three 186-component gradient contributions are in the first
result, not reduced to these summary numbers.

## Predeclared weak-coupling controls

The reference inputs are lambda=.2, g=.5, y1=y2=.25, mu=1. For epsilon=1/4
and 1/16, scale lambda by epsilon and g,y,mu by sqrt(epsilon), keeping the
classical VEVs fixed. This changes the input theory; it is **not** RG evolution
of one theory and is not a fit to measured couplings.

| epsilon | relative shift of each scalar 27 | relative adjoint shift | positive tree mass-squared gap | each-field 10% diagnostic |
|---|---:|---:|---:|---|
| 1 | 0.148828782 | 0.017835166 | 0.038888889 | fails |
| 1/4 | 0.037207195 | 0.004458791 | 0.009722222 | passes |
| 1/16 | 0.009301799 | 0.001114698 | 0.002430556 | passes |

The reference full canonical displacement norm is 0.300317317, or
0.100105772 relative to the original canonical VEV norm. All three points
preserve the SM algebra. Their stationarity residuals are below 1.23e-15.

Under this scaling the tree squared masses scale as epsilon, their logarithms
stay fixed, and V1 and its gradient scale as epsilon squared. Consequently
the leading displacement scales as epsilon, while R5's positive angular
curvatures scale as epsilon squared. The displacement scaling is verified
directly. The 10% criterion is a diagnostic, not a universal perturbativity
theorem or a bound on every higher-order correction.

## Why the normal shift does not overturn R5

Let X be a canonically normalized octet/triplet tangent to the classical
vacuum family, and k the second derivative of its norm-preserving path.
Differentiating tree stationarity along that family gives

```text
H0 k + V0'''[X,X] = 0,
H0 delta z = -grad V1,
X^T dH0[delta z] X = grad V1 . k.
```

Here k=-Y/5 in the adjoint coordinates. The last equality is checked with
independently constructed full tree-Hessian derivatives for both multiplets.
At the reference point, its two sides are -0.05848472012804148 and
-0.05848472012804130. This is a **contribution**, not the net angular mass.
R5's constrained second derivative already includes it through the path's
curvature. Subtracting it again would double-count the shift and manufacture
a false negative. The net leading octet/triplet values remain R5's
0.00751974898044 and 0.00736557837470.

Conversely, a tree Hessian evaluated at a quantum-shifted, non-tree-stationary
point is not the quantum mass spectrum. Off-shell Goldstone logarithms need
care at higher orders; the general warning is established in
[Martin, arXiv:1406.2355](https://arxiv.org/abs/1406.2355). This calculation
uses derivatives at the nonnegative tree spectrum, not absolute values of
off-shell negative masses, and does not claim to implement that paper's
resummation in this E6 theory. R5's one-loop conventions remain those of
[Martin, hep-ph/0111209, equations 1.1 and 3.2–3.5](https://arxiv.org/pdf/hep-ph/0111209).

## Custody, tests and next obligations

Design, code and five tests were sealed at **44a52ec4**, before first execution.
The scientific run succeeded in 6.16 s; the five focused tests passed in
7.39 s. No failed R6 scientific output was discarded. The earlier R4/R5
producers and outputs remain unchanged.

- [Design](EXTENSION_4.md), [producer](quantum_shift.py),
  [complete first output](quantum_shift_first_run.json).
- `tests/test_physical_bridge_quantum_shift.py` tests quadratic reconstruction,
  normal-derivative controls, scalar/vector/Weyl derivatives, kernel force,
  SM action, scaling and the angular-shift identity.
- The combined audit regression and governance results are recorded separately
  after banking; focused success is not a full-repository green certificate.

Reproduce to a **new** output path (exclusive creation prevents overwrite):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.quantum_shift --output /tmp/oa-normal-shift-new-run.json
```

PB-VACUUM advances from an uncomputed normal displacement to a verified
leading shift with small-coupling controls. It stays open for the complete
higher-order stationary solution, global comparison and other allowed
couplings/branches. PB-MASS still needs a light electroweak sector and
matching of the spectrum actually constructed. Added fields or interactions
must be priced and their effect on this quantum vacuum recomputed. Action
selection, physical parameters and four-dimensional gravity are not derived
by this result.

Final combined regression at 2215d67b: **59 passed in 35.56 s**, including
four post-result controls. Direct all-component scalar-Hessian contractions
and a reduced nine-mode singlet solve agree. Two deliberate defects each
make the original vector/Weyl derivative test fail, confirming its bite.
Governance is **27 passed, 3 failed**: the two preserved earlier defects and
a static NO-ASSERT false positive on that unchanged numerical-assertion test.
The checker is not weakened or exempted. All 48 then-listed hashes match.
Raw output: [QUANTUM_SHIFT_CHECKS.txt](QUANTUM_SHIFT_CHECKS.txt).

**Next model, R7:** [HIGGS_SECTOR.md](HIGGS_SECTOR.md) now computes a priced
two-scalar-27 extension. It retains the positive angular result, adds two
light doublets and actual light-kernel Yukawa support, but has a radiative
Higgs instability and large new singlet shifts at its reference point.
Those are results for the expanded model, not a retraction of R6 above.

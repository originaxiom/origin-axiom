# codex -> cc: R028 exact toric chart and line-bundle frames

## Claim for independent verification

R028 pins the convention layer required between R026's determinant cochain
and R027's marked top trace. It reconstructs the exact ray/monomial actions,
all 36 ordered ray matrices and their dual coordinates, and proves

```text
chart action: (i,j)->(j+1 mod 6,i),
orbit representatives: (0,1,2),
orientation census: 18 positive, 18 negative.
```

For every anticanonical and `H-D_c` lattice monomial on every chart it proves

```text
raw chart monomial = q_(D,sigma) * t^u,
ell_(D,sigma)=q_(D,sigma)^(-1).
```

Thus raw chart coefficients must be divided by `q_D` before they are compared
in common Laurent coordinates. It also records that the prior set-chosen orbit
representatives are nondeterministic and the displayed `Phi_a Phi_b` check is
only commutativity, not gluing.

This is a convention/frame result only. No characteristic-zero `Phi_308`
payload, Bezout multiplier, hypersurface class or Yukawa entry is claimed.

## Artifacts

- memo: `memos/YUKAWA_TORIC_CHART_FRAMES_308.md`
- certificate: `certificates/r028_toric_chart_frames/toric_chart_frames.py`
- output: `outputs/r028_toric_chart_frames.txt`

## Requested disposition

Please independently reconstruct at least one positive- and one
negative-orientation chart, the induced chart action, and the `q_D` identity.
If they reproduce, bank this as the chart/frame prerequisite for the remaining
OA-C1148 refinement and residue calculation.

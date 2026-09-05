# R7: a priced Higgs extension, including its full quantum feedback

BANKED IDENTITY: B883/B884 supply the 27 matrices and invariant cubic, not
their physical magnitudes. B987 already places Higgs doublets in the 27;
B978's adjoint-fermion prohibition does not prohibit cubic Yukawas. R4/R5/R6
give a chosen compact-E6 action, an SM vacuum family, positive leading
octet/triplet lifting and a verified leading normal shift. Those original
producers and results remain unchanged if this new model fails.

PRIOR ART: fetch still gives a8fd2460, included locally. The already-banked
check on Higgs/doublet/triplet/adjoint/potential gives 77 hits and four settled
arcs matching at least three terms. B987, B884, B978, B298/B299 and B1206
were read to their ends; the relevant original producers were inspected.
The ladder X8/X10 and PB-MASS/PB-VACUUM, framework, campaign, law/lead rows,
atlas and B299's kill-graph hatch were checked. B1206's projective-line count
does not select mass parameters in this action. B299's triality argument
is not a no-go for a chosen symmetry-breaking scalar potential.

Search repair retained: the first history command supplied an alternation
pattern without `--regex`, and therefore searched a literal string. Its
ABSENT line is not evidence about Higgs physics. Repeating
`absence_sweep.py 'doublet.triplet|light.Higgs|sliding.singlet|missing.partner'
--regex` returns PRESENT on all nine enumerated heads, with 32 working-tree
hits. Deleted *paths* matching are zero; deleted contents are not exhausted
by that statistic. No repository-wide absence claim is made.

P0: test one explicitly added, renormalizable 4d compact-E6 Higgs sector on
R4's chosen branch, not a forced extension of the relational object. The
owner's physical-completion directive motivates this PB-MASS continuation;
it does not close an old bounded rung or derive a source-to-action map.

## New inputs, all priced

Add two independent complex scalar 27 fields U,D with canonical kinetic
terms, no additional fermion families. To the R4 potential add

```text
V_H = kU ||(A-a I) U||^2 + kD ||(A+a I) D||^2
    + xi ||C(phi1,D)||^2 + lU (U^dagger U)^2 + lD (D^dagger D)^2.
```

All coefficients are positive. Each term is E6 invariant and has dimension
at most four; a is a dimension-one input, not a hypercharge derivation.
Preselect a=1/2 in R4's VEV units, kU=kD=xi=.02, lU=lD=.2. The old common
quartic is .2, g=.5 and y_phi1=y_phi2=y_U=y_D=.25 for one Weyl 27.
All other symmetry-allowed renormalized operators are zero at the declared
scale, not protected. In particular the Yukawas do not preserve an inert
Higgs parity; singlet Higgs tadpoles must be included, not forbidden by name.

This is two added scalar multiplets and freely specified couplings/scales.
The relation a=1/2 to the chosen adjoint VEV is a priced light-mode tuning.
No claim of natural hierarchy, observed masses or three families follows.

## Complete classical instrument

Real coordinates: the original 186, then Re/Im U (54), Re/Im D (54).
There are 294 real scalars and 439 real constraints: the original 275,
54 U-action constraints, one U-norm constraint, 54 D-action constraints,
54 cubic C(phi1,D) constraints and one D-norm constraint. The norm constraints
have target zero. The kinetic metric extends the original by 2 I108.

At U=D=0 the original zero-potential tree family survives, by positivity
of every new term. Build the full constraint Jacobian and Hessian, including
the constraint-Hessian term off the vacuum. Enumerate all eigenvalues and
the actual gauge orbit; isolate new kernels using generator actions, not
dimension labels. Expected algebraic candidate: one (1,2,+1/2) in U and
one (1,2,-1/2) in D, with colored partners massive. C(S,D) is intended to
lift the otherwise duplicate negative-hypercharge doublet. This intention
must be checked and may fail.

Project the new cubic Yukawa matrices onto the actual 17-dimensional
kernel of the old mixed S/N fermion mass. Use K^T M K, with K kinetically
orthonormal. Check actual color/weak/charge actions, charged mass-block ranks,
and the full projected rank with both neutral doublet components turned on.
This computes leading low-energy support, not a fitted mass spectrum or a
finite-VEV integration of heavy states.

## Quantum instrument and outcomes

Include every 294 real scalar, 78 vector and 27 Weyl mode, with R5's
MS-bar/Landau conventions. Extend the spectral Hessian to complex Hermitian
matrices, using absolute squares of off-diagonal derivative elements, and
test it on a complex rotating-matrix control. A nonzero linear perturbation
inside a zero-mass block is a failure/IR diagnostic, not permission to set
its logarithm to zero or take an absolute value.

Compute all 294 one-loop force components, check the entire tree-kernel
projection, solve the positive normal equation, and verify SM preservation.
Keep the Higgs singlet forces and shifts from the newly allowed Yukawas.
Compute the complete eight-real-dimensional light-Higgs curvature matrix,
including its normal-shift correction, plus octet/triplet curvatures along
the old tree family. Check the curved-path/normal-shift identity again in
the expanded model. Do not add a normal correction twice.

Report eigenvalues with their sign: positive supports local stability;
negative locates an instability of this high-scale Higgs-zero background;
zero leaves a higher-order question. None is a TOE verdict. A negative Higgs
mass could motivate a separately computed electroweak-broken branch, but is
not by itself evidence for the observed scale or an electromagnetic vacuum.

Predeclare mu=1/2,1,2, keeping displayed renormalized inputs fixed. These are
scheme/scale diagnostics, not full RG evolution with all counterterms. Check
the additional fourth-mass traces as exact four-Cartan-variable polynomials;
claim angular scale independence only if their remainders vanish. No global
quantum vacuum claim follows from a local Hessian.

Controls: finite differences of the full constraints/J/Hessian (including
complex fields and normal directions); a quadratic scalar with no desired
sign; a complex rotating-matrix spectral control; an emerging kernel with
nonzero linear mass that must be rejected; actual compact gauge covariance
of the new mass matrices; shifting a away from 1/2 removes the candidate
light doublets; omitting xi restores the extra D doublet. Report all first
results and any failures. Seal design, code and tests before execution.

Prior: the positive-square classical candidate is plausible and its weak
new couplings may preserve the old angular result. The complete light-Higgs
loop masses, mixings and tadpoles are not known in advance. Higher-order
stability, an electroweak vacuum, observed matching, input selection and
four-dimensional gravity remain separate obligations.

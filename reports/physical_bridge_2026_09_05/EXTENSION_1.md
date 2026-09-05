# Extension 1 — declared after R1/R2, before executing this extension

2026-09-05. The original design and first result remain unchanged. This is a
post-R1/R2 development, not part of the original preregistration and not an
independent empirical test. The comparison numbers remain B915's archived
fixture; no new observations enter.

## A reproducibility failure, not a negative mathematical result

Explicitly enabling B1098's live certificate test with the now-vendored
`B1148_carrier_harvest/verification/certificates/twisted_double.py` failed
before any triple was tested. Original test SHA-256:
`94ce763ed6b481f86a44388bf0ab18aeb21b1157c1b35ef5b1dc32b81f862416`.
Relevant failure output, preserved verbatim:

```text
>       exec(src[:src.find(chr(112) + 'rint(" IDENTITY double')], G)

tests/test_b1098_nonabelian_hatch.py:30:
E   NameError: name '__file__' is not defined

1 failed, 1 passed in 1.46s
```

Repair only the loader: provide the real source filename, fail explicitly if
the prefix marker disappears, and use the committed certificate by default.
Keep every triple identity and the dimension-16 centralizer assertion unchanged.
The original default suite in the baseline worktree remains untouched.

## R3 — can a common ultraviolet mass supply the fitted splitting?

Prior work: B884's cubic includes `1·10·10`; B970's original scout and WORK
already identify the singlet VEV as the exotic mass source. Neither masses
nor a VEV are derived by this audit. B970 also records other scalar/symmetry
choices and proton-decay issues: these are not to be forgotten.

The equal-PHYSICAL-threshold control in R2 does not rule out a common UV mass:
gauge running itself splits triplets and doublets. Test that distinction.

Quantifier: precisely R2's one-loop SM-plus-vectorlike-fermion effective
theories, one to three copies, with canonical kinetic terms, a common
SU(5)-equivariant triplet/doublet mass matrix at the meeting scale, and only
gauge contributions to exotic mass running below that scale. No exotic
Yukawa interactions, additional scalar thresholds, intermediate groups,
finite threshold matching, or nonperturbative effects are included.

1. Compute the commutant of the fundamental SU(5) generators on the 5, and
   separately of its SM subalgebra. Expect dimensions 1 and 2, respectively:
   a singlet mass and an independently split block mass. Verify the bases
   against every generator, including a split negative control for SU(5).
2. Use the gauge part of the one-loop mass beta function
   `d log m/dt = -6 sum_i C_i alpha_i/(4*pi)`. This is an explicit standard-QFT
   import, not supplied by the finite representation. Primary source:
   [Luo, Wang and Xiao, Eq. (62)](https://arxiv.org/pdf/hep-ph/0211440),
   accessed 2026-09-05. The anticommutator becomes twice the Casimir for a
   vectorlike Dirac pair; the loop factor is given by Eq. (13).
3. Integrate the mass running along explicit piecewise gauge trajectories.
   Compare analytic integrals with independent numerical quadrature and a
   constant-beta/constant-coupling control. Do not identify a running mass
   at an arbitrary scale with its decoupling threshold: use `M=m(M)` within
   this leading-log approximation.
4. Bound the entire allowed threshold range, not a sample of common masses.
   For n <= 3, `b3 <= -5`, hence `alpha3 <= alpha3(MZ)`; and
   `alpha1 <= 1/[x1(MZ)-(41/10+2*n/3)*tU/(2*pi)]` if the denominator is positive.
   Positivity of doublet mass enhancement then gives, per UV-degenerate pair,
   `log(MD/ML) <= tU*((2/5)*alpha1_max+8*alpha3(MZ))/(4*pi)`.
   Compare n times this upper bound with R2's required sum. A nonpositive
   denominator makes this bound inconclusive, not a failure of a theory.
5. Report the UV mass ratio still required by R2's illustrative split models.
   A split UV boundary is an additional input, not a recovered prediction.

Prior: gauge running is insufficient for the very large R2 split in this
restricted model. Passing or failing this bound will not adjudicate a model
with additional interactions. No global no-go, discovery claim, or promotion
of the fitted threshold to a physical prediction is authorized by this cell.

Additional regression checks will recompute R1's original boundary defect and
the corrected endpoint, rather than merely assert strings in the first-run JSON.

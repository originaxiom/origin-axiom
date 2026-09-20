# F02: a smooth complete cusp does not supply a free fermion-domain choice

2026-09-20. **The complete-space domain question has a scoped answer:** for
the adopted ordinary-L2 form-valued fermion operator, smooth unitary connection
and smooth Hermitian Higgs potential on a complete boundaryless base give a
unique self-adjoint closure. The Higgs background need not itself have finite
L2 norm. This is an application of standard mathematics, not a new theorem
of nature or a proof that the program has physical chiral matter.

[Design](DESIGN.md), [full proof and counterexamples](PROOF.md),
[exact controls](test_verify.py). Design, proof and controls were committed
at `09f41662` before first execution. All four sealed digests still match.

## What this settles and what it does not

| Question | Scoped answer |
|---|---|
| Must a zero-potential bulk background have finite integral norm(phi)^2? | No implication of that kind follows from the adopted residual-square functional; R15/R28 already provide the required distinction. |
| Can an unbounded smooth Higgs potential define a self-adjoint complete-space fermion operator? | Yes. The cutoff commutator depends only on the Dirac symbol, not on the size of the zeroth-order potential. |
| Can we choose an extra cusp extension just to obtain chirality? | Not for this fixed complete smooth operator and L2 norm: its closure is unique. |
| Does uniqueness force zero net chirality? | No. The complete-line oscillator countercontrol has an unpaired graded zero mode. It is not a BPS or physical-generation example. |
| Does uniqueness supply a discrete usable low-energy spectrum? | No. The free complete-line control is not Fredholm. |
| Does the result apply unchanged after deleting a singular source locus? | No. Completeness/smoothness can fail; explicit half-line deficiency vectors and the old R16 Green-form control detect the difference. |

The mathematical domain is {u in L2 : Qu in L2 distributionally}. It is not
asserted to be global H1 with an unbounded potential. No boundary limit was
silently exchanged with a finite regulator. No independent essential-self-
adjointness statement for Q-squared on its minimal domain was claimed.

## Positive background control, with its identity retained

R15's homogeneous through-flux construction already supplies the following
source-free specialization. On a connected finite-volume hyperbolic base
with at least two cusps choose nonzero c_i satisfying sum A_i c_i=0.
A compactly supported mean-zero Laplacian error is removed by the reduced
scalar resolvent. The resulting smooth global harmonic F has c_i exp(2r)
asymptotics; phi=u dF has zero commuting bulk potential. Its background norm
and nonzero c_i variations diverge. The complete-space fermion closure still
exists uniquely.

This is not a new global construction beyond R15, not a unique selected
vacuum, and not evidence for the nonsplit m010 representation: its exact
flat connection is complex-gauge trivial. The exact gauge multiplier is
unbounded, so it also cannot be used as an ordinary unitary L2 equivalence
to erase the spectral problem. The global scalar gap is a standard input,
not a newly computed charged spectral gap.

## Impact on the physical strategy

F01 remains a finite-harmonic-energy obstruction. F02 prevents two unjustified
extensions of it: equating that energy with the action's static potential,
and assuming an infinite background norm necessarily makes the fermion
operator ill-defined. Neither observation establishes that the nonsplit
candidate has an admissible global background.

The next actual discriminator is therefore **existence and asymptotics of
that background in one declared physical parent**, followed by its L2
zero-mode/essential-spectrum calculation. Smooth complete and singular
source-completed routes must remain separately labeled. The latter must
derive its source/domain from its action, not borrow a desired relative
index while discarding the resolved-core partners.

No global nonsplit PDE solution, Fredholm theorem for the program's charged
operator, generation count, anomaly cancellation, interaction spectrum or
gravitational completion was produced. The full physical goal is not achieved.

## Verification grade

First execution: **16 passed in 1.86 s**, exit 0. The exact controls cover
Clifford algebra, the potential-independent commutator, a nonsymmetric
mutant, cusp norm/flux formulas, the chiral oscillator, a non-Fredholm
complete operator and an incomplete operator with deficiency vectors.

The universal conclusion rests on the written cutoff/elliptic-regularity
argument, not the number of tests. This is a local research checkpoint,
not an independent expert review, full-suite run or complete banking pass.
Additional unchanged antecedent rechecks are recorded separately in
[RECHECKS.md](RECHECKS.md).

Those rechecks returned **23 passed and 1 failed**: R16's definite-integral
evaluation remained unevaluated in SymPy 1.14. An independently differentiated
primitive verifies the capacity identity, including a deliberately wrong
primitive control. The original failure is preserved and is not counted
as a passing old test. No R16 scientific source or assertion was changed.

## Subsequent background test

[F03](../nonsplit_cusp_growth_2026_09_20/FINDINGS.md) now sharpens the rank-two
background question without changing this domain theorem. Positive global
flux cannot be carried by a radially controlled harmonic cusp: it forces
finite-distance blow-up unless the angular Busemann oscillation becomes
large. Nineteen exact controls pass, including a smooth counterexample to
an invalid averaging shortcut. The general angle-dependent and independent
rank-four problems remain unresolved, as does their physical interpretation.

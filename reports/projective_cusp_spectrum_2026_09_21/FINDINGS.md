# F11: normalizable modes survive at exceptional twisted projective parameters

September 21, 2026. Local fork `audit/fork-2026-09-20`.

**September 25 follow-through:** [F12](../projective_global_metric_2026_09_21/FINDINGS.md)
supplies an authored global harmonic-metric existence proof at the
exceptional parameters, controlling the actual end norm class. Fifteen
new checks and 236 unchanged antecedents pass. The global-existence
duty named below is addressed in this model; physical end/action,
interaction and chirality duties remain. Original F11 science and its
failed expectation are unchanged. The body below records F11's own
September 21 checkpoint.

## Verdict: the initial vanishing expectation was wrong

F10 supplied an exact holonomy curve breaking the previous invertible
flat dual-bundle pairings and an exact solution of the local cusp gauge
equations. It did not decide the normalizable spectrum. This checkpoint
now identifies that spectrum's zero-mode cohomology in a specified
complete-space metric class, and computes the member's multiplicities.

**There are discrete nongeometric parameter values where a central twist
produces one normalizable coefficient one-form in each dual sector.**
Generic positive parameters have none on the base member. The initial
expectation that the geometric point was the only positive exception
failed for all three nontrivial twists. Those failures, the original
producer and the original assertions are retained, not rewritten green.

This is a concrete mode-bearing target for further physics work, not
net chirality. It is also NOT yet a global vacuum: the mode statement
holds for smooth metric completions with the declared cusp asymptotics,
but a global solution of the parent moment equation in that class has
not been constructed here.

## 1. The cusp-to-spectrum connection is now an actual map

Use F10's full rank-four connection, its positive kinetic norm and fixed
hyperbolic base. Write k=log q!=0, u=z^2/4-beta^2/L^2>0. The covariant
longitudinal derivative and an explicit inverse are

    T = partial_y-k D-beta P/u,
    T^-1 = S^-1+(beta/u)S^-1 P S^-1,
    S = i omega I-k D

on each Fourier mode, with D=diag(1,-3,1,1), P=E03. The inverse is
uniformly bounded over ALL frequencies because the real parts of S's
eigenvalues stay away from zero. It is not a truncated mode calculation.

The full flat differential, including the radial direction, obeys

    K=iota_(partial_y) T^-1,
    d_C K+K d_C=I,
    ||K||_(z>=Z) <= (L/Z)[1/|k|+|beta|/(u(Z)|k|^2)] -> 0.

The actual hyperbolic form norm, not a coordinate norm, supplies L/Z.
A nonflat comparator with invertible torus operators fails the full
identity, confirming why the radial equation cannot be omitted.

This gives a growing lower bound for the charged Hodge quadratic form
high in the cusp. Combined with the complete-space domain, compact-core
elliptic estimates and Rellich compactness, it proves compact resolvent
and closed differential ranges. Cutoff homotopies then explicitly give

    H^p_(2)(M;E) = H_c^p(M;E)
                 = H^p(core,whole boundary;E)
                 = H^p(core;E).

The last equality uses the already-verified peripheral acyclicity.
The usual closed-range Hilbert-complex identification with harmonic
forms is used only AFTER its hypotheses are established.
[Arnold--Falk--Winther, section 3.1.3](https://arxiv.org/html/0906.4325v3#S3.SS1.SSS3).
The new cusp maps and estimates are an authored application, not a
cited theorem with unstated end hypotheses or external peer review.

The proof applies to both dual coefficients, finite-cover pullbacks
and unitary scalar characters. It allows arbitrary smooth compact-core
changes and uniformly equivalent smooth positive norms in every degree.
It does not cover unbounded metric changes, sources, drilled boundaries,
nonflat operators or all representations of the arithmetic class.
It is a result for the charged defining four and its dual, not compact
resolvent for every neutral or other sector of the full E8 parent.

## 2. Exact surviving loci, including the failed expectation

For the two-generator relation of F10, let J be the evaluated Fox row
and B the coboundary matrix. The ordinary degree-one dimension is

    dim H1 = 8-rank J-rank B.

We compute all 70 maximal minors of EACH matrix, split exact real and
imaginary numerators, and determine their polynomial gcds. All
denominators are nonzero constants times powers of q, and an exact
Sturm count determines the entire positive-q root population. This
does not extrapolate from sampled ranks or numeric tolerances.

| Scalar character chi | Complete positive rank-drop locus | H1 at each listed point |
|---|---|---|
| 1 | q=1, from (q-1)^2 | 1 in ordinary cohomology; the F11 L2 theorem excludes this endpoint. |
| -1 | q=17 +/- 12 sqrt(2), from q^2-34q+1 | 1 in each dual sector, also ordinary-L2 in the stated class. |
| i or -i | q=7 +/- 4 sqrt(3), from q^2-14q+1 | 1 in each dual sector, also ordinary-L2 in the stated class. |

At all other positive q, for the character in that row, the base-member
H1 is zero. Rank B is four throughout. Away from the listed loci,
rank J is four; at them it is three. A double factor in the untwisted
minor gcd does NOT mean two H1 classes: the direct rank there is three.

The nongeometric counts have additional exact checks. Arithmetic over
Q(i)[q]/p verifies both real roots of each irreducible quadratic. For
each character and its dual we exhibit a closed generator cocycle v
with rank(B|v)=5, so it is NOT a coboundary, plus a 3-by-3 minor which
cannot vanish on that quadratic locus. Fox rows also agree with a
separately formulated affine-block cocycle calculation. Both algorithms
reuse R27's known approach, adapted to exact rational functions; this is
not independent human review or a newly invented cohomology instrument.

[Plot of the exact loci](EXCEPTIONAL_LOCI.png) (reporting only; the
horizontal coordinate is log q, not a measured mass or coupling).

For example at chi=-1 and q^2-34q+1=0, a representative has

    v(m)=((5q-1)/48, (3q-15)/16, (q+11)/8, 1),
    v(n)=(0,0,0,0).

All six coefficient/dual witnesses and rank-three minors are retained in
[the exact output](EXCEPTION_WITNESSES.txt). These are group cocycles,
not computed spatial harmonic wavefunctions or normalized Yukawa profiles.
Existence of their normalizable harmonic representatives follows from
the analytic comparison above.

## 3. What was gained toward physics, and what was not

The useful combination is specific: the central twist alone on F08
retained an antiunitary pairing; the untwisted nongeometric deformation
on this member is acyclic; the twist AND an exceptional deformation
give nonempty normalizable sectors without the old invertible flat
pairing. This is a more concrete target than generic parameter hunting.

Equal multiplicities nevertheless remain. For every finite-cover
pullback in the same end class, Euler characteristic and whole-boundary
duality imply equal charged degree-one counts. We have not computed
individual counts on those covers. On the base at an exceptional point
the count is explicitly one on each side. This is not three generations,
a chiral SM vacuum, or an assertion that all positive spectra or all
interactions are paired.

The q parameter is also not a normalizable scalar modulus of this
fixed-base family. Its variation has an unavoidable D-projection,
tr(D delta Psi_y)=-12 delta(log q), and hence a logarithmically infinite
kinetic norm. A smooth unitary gauge variation cannot remove that
projection. A fixed-q end background remains a different admissibility
question: this does not equate divergent modulus norm with divergent
residual potential or reject every fixed asymptotic sector.

The four positive nongeometric q values, with their character labels,
are mathematical rank loci, not measured constants or dynamically
selected physical parameters. No physical vacuum-count quotient is
claimed. In particular Ballas' nearby projective-geometry theorem is
NOT an existence theorem at these distant values. The actual matrices
and local gauge solution remain valid there independently of that
geometric interpretation. No new representation family or literature
novelty is claimed.

## 4. The next experiment is now better targeted

1. Test global harmonic-metric existence at these exceptional representations
   with F10's cusp asymptotics. An arbitrary smooth positive extension
   defines the proved spectral problem, but is not automatically a
   stationary parent vacuum. A possible route is an exhaustion argument
   comparing the reference cusp energy with the lower bound dictated by
   the FULL longitudinal spectrum. It needs a verified sharp bound,
   finite excess energy, irreducibility/coercivity and convergence in
   the required norm class; that existence argument is NOT completed here.
2. Derive the allowed fixed-end variation law and boundary terms of the
   actual action. Infinite background or modulus norm is not itself the
   answer; zero bulk residuals alone are not the answer either.
3. For an admitted global background, compute normalized profiles and the
   full relevant parent interaction channels. F09's balanced Codazzi
   cofactor and propagator formulas cannot simply be substituted into
   this different nonparallel background. Convergence of their products,
   genuine mirror-selective dynamics and anomalies need their own checks.

The immediate advance is a mathematically identified, mode-bearing target
and a testable global-existence route. Gravity, quantum completion,
vacuum selection, the observed matter spectrum and measured predictions
are not supplied by this checkpoint. The full TOE goal is unachieved.

## Verification and custody

Original seal **85454725** preceded execution: **27 passed / 3 failed**.
The failures were the incorrect global vanishing expectation at the
nontrivial twists. Correction seal **15c32b3c** then preceded a follow-up
that retained all unaffected checks and added exact exceptional classes:
**40 passed**. **196 unchanged antecedent/parent-vertex checks passed**
with one optional-GUI warning. No original science or old failed version
was altered. This is not a fully green repository or governance suite.

[Design](DESIGN.md), [analytic proof](PROOF.md),
[post-failure addendum](EXCEPTION_ADDENDUM.md),
[first-run transcript](FIRST_RUN_TRANSCRIPT.txt), [receipt](RECHECKS.md).
No new subagents, new all-head fetch, shared B number, main edit, push,
external publication or independent banking certificate is included.

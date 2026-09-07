# R18: the complete four/one kernel in a declared strong-source complex

2026-09-07. Pre-execution seal ad3857a7. Path-local research, no B ID.

## Result and the physical boundary of the result

The normalizable charged cohomology can now be compared with the full
regulated pair, not only its Euler characteristic. In the maximal
deformed de Rham complex specified below, with every effective source
strength abs(q)*beta_a >= 1, bounded end homotopies give

| charge | finite pair | complete cohomology in degrees 0,1,2,3 |
|---|---|---|
| q>0 | (C,T), relative source annuli | (0,4,1,0) |
| q<0 | (C,E), relative exterior cusp surfaces | (0,1,4,0) |

The displayed numbers require R15's two-cusp, three-proper-arc
homological hypotheses; the comparison theorem itself applies to the
stated wider source class. The differentials have closed range and
finite cohomology. Therefore the associated Hodge operator has these
finite-dimensional normalizable harmonic spaces. Its degree-one counts
are FOUR AND ONE, net three, not a pure three-mode spectrum.
The degree-two dual spaces are an alternative description of the
opposite-charge degree-one sector, not additional families to count twice.

This is an analytic conditional result with explicit algebraic/numerical
controls, not an interval PDE eigensolver or an independently reviewed
theorem. The maximal-complex realization, positive source densities,
strong amplitudes, W=0, parent and selected source locus are still
declared modeling data. They have not become consequences of the object.
A physical Lorentz/gauge assignment and a consistent defect completion
are not supplied by this comparison. A complete TOE is not established.

## 1. Precise Hilbert complex; the exponential changes spaces

Use R15's complete finite-volume orientable hyperbolic 3-manifold M
with finitely many disjoint properly embedded geodesic source lines
Delta. Each has constant beta_a>0. Every cusp has positive total
endpoint density Q_i. F is R15's global real commuting potential and
H=qF, q real and nonzero. There are no angular flat-bundle twists.

Let d_H=d+dH wedge have its MAXIMAL DISTRIBUTIONAL domain on M\Delta:
alpha and d_H alpha must both be in the canonical metric L2 spaces.
Its Hodge realization is D=d_H,max+(d_H,max)*. The star here denotes
the Hilbert adjoint. This is a specified closed Hilbert complex, not
an unspecified self-adjoint extension of the differential expression D.
Nilpotency follows distributionally from the global real potential.

Set u=exp(H) alpha. Direct calculation, in every degree, gives

```text
norm(alpha)^2 = integral exp(-2H) |u|_g^2 dvol_g,
d u = exp(H) d_H alpha.
```

Thus this map is unitary BETWEEN DIFFERENT Hilbert spaces and maps
their maximal graph domains exactly. It is not a bounded similarity
inside unweighted L2. R15's smooth corrector v is globally bounded:
it is smooth on the compact part, with constant and decaying full-torus
Fourier modes on the cusps. Removing qv multiplies the weighted norms
by globally bounded positive factors. Ordinary d stays the same; its
maximal domains, cohomology and closed-range property are unchanged.

## 2. Finite-height source collars: a boundary condition from the weight

Put a=q beta_a. At finite height the exact cylindrical metric is
uniformly comparable to dr^2+r^2 dtheta^2+dt^2. The radial density of
a coordinate component with epsilon_theta copies of dtheta is r^p,
where p=1-2a-2epsilon_theta. Adding dr changes neither that density
nor the tangential base degree. The exact/model ratio is

```text
(tanh r/r)^(-2a) (sinh r/r)^(1-2 epsilon_theta)
                 (cosh r)^(1-2 epsilon_t),
```

which tends to one and is bounded above and below on a finite collar.
Bounded regular parts of F do not change these equivalences.

For K0 f(r)=integral_0^r f(t)dt, the conjugated integral kernel has
squared Hilbert--Schmidt norm

```text
integral_0^R r^p integral_0^r t^(-p) dt dr
    = R^2/[2(1-p)]  (p<1).
```

For KR f(r)=-integral_r^R f(t)dt, exchange the integrals to obtain
R^2/[2(p+1)] for p>-1. Both are squared operator-norm upper bounds.
This includes p=1 in the second formula; a logarithm in an intermediate
primitive is not a divergent operator bound.

For a>=1, every tangential p<=-1. Constant endpoint traces are not
integrable, while K0 is bounded. The collar is acyclic with its zero
endpoint trace: a RELATIVE source boundary. For a<=-1, every p>=1;
all tangential constants are integrable, and KR retracts to the full
annular side: an ABSOLUTE source boundary. It does not fill the disk.

The weak a=1/2 scalar has p=0: its constant is L2 and its trace
projection is nonzero. K0 is still bounded, which shows why bounded
integration alone does not justify an amplitude-independent acyclicity
claim. Weak, mixed-sign, neutral and zero-endpoint-total cases are not
classified by this theorem.

These are radial weighted homotopies of the standard kind discussed
by [Bullock, sections 4 and 6](https://nyjm.albany.edu/j/2001/7-2.pdf).
The powers, endpoints and punctured-cusp application above are specified
here; that paper's whole theorem is not transferred without hypotheses.

## 3. Complete cusps, including simultaneous approach to a source

On each high cusp write s=log z and H=V(w)+h(s), with
h=q exp(2s)(bs+c), b=pi Q/A>0. For tangential degree j=0,1,2,
the radial weight, whether or not ds is present, is

```text
w_j(s)=exp((2j-2)s-2h(s)).
```

The base norm uses exp(-2V) on the entire punctured torus. Let
phi_j=(j-1)s-h(s). At R17's explicit sufficient S0, abs(h')>=8
and increases thereafter. With alpha0=abs(h'(S0))-1>=7,

```text
q>0: phi_j' <= -alpha0,  K_S f(s)=integral_S^s f(t)dt;
q<0: phi_j' >=  alpha0,  K_infinity f(s)=-integral_s^infinity f(t)dt.
```

Conjugation by sqrt(w_j) bounds the respective kernels by
exp(-alpha0*abs(s-t)) on their one-sided supports. Schur's test gives
norm(K)<=1/alpha0, for every tangential component. Constants are L2
on the positive-charge cusp (absolute face), not on the negative-charge
cusp (relative face).

No localization on the punctured torus was used. In particular no
uncontrolled exp(s)*dchi(w) term is introduced by angular partitions.
This handles the joint end before finite-height line collars are removed.
Near a joint corner use rho=abs(w-p) in the cusp coordinates; physical
normal distance is approximately exp(-s)*rho. Uniform disjoint tubes
of fixed PHYSICAL radius at arbitrarily large s are not assumed.

## 4. Maximal domains, bounded projections and global gluing

For u=alpha(r)+dr wedge beta(r),
du=d_B alpha+dr wedge (partial_r alpha-d_B beta). At a relative
end, reciprocal-weight integrability makes beta and the radial part
of du integrable against every compact smooth base test form. The
equation consequently defines a weak endpoint trace of alpha. A
nonzero trace would contradict its L2 norm, since the tangential
constant weight is nonintegrable. Hence this trace is zero.

Distributional integration now gives dK+Kd=I. This also proves that
K maps the maximal graph domain into itself: dKu=u-Kdu belongs to
L2. Separate control of partial_r alpha or d_B beta was not assumed.
The argument at infinity is identical with the reversed integral.

At absolute ends dK+Kd=I-P. Point evaluation at a regular slice is
not bounded on L2. Average BOTH the radial integral and the tangential
trace over a fixed regular slab with the same normalized density eta
in every degree. The averaged P is bounded by Cauchy--Schwarz and the
integrable constant tail; the averaged K is bounded by the above end
estimate plus a finite-slab correction. The identity is preserved.
Weak integration justifies it on the full maximal domain, not merely
compactly supported smooth forms that might impose an extra boundary law.

Choose a smooth chi equal to one near the end and zero before a finite
transition. With P=0 at relative ends and the averaged P otherwise,

```text
A=I-d(chi K)-chi Kd=(1-chi)I+chi P-dchi wedge K.
```

All terms are L2-bounded and A commutes with d. At a relative end A
vanishes on a terminal collar. Restrict A to a core cut there; the
inverse cochain map is zero extension of the relative core complex.
Zero extension has no distributional surface term precisely because
the tangential relative trace vanishes.

At an absolute end A depends only on input in the finite core: in the
tail it equals the averaged constant extension P. Restriction is one
cochain map; A's finite-data formula, followed by that constant tail,
is the other. Their compositions are homotopic to the identity by
chi K, on both the core and complete complexes. No point trace is
used as an L2-bounded restriction operator.

Perform these operations on whole cusps first. The remaining line
segments have finite length and uniformly comparable collar metrics.
Their transverse maps keep the longitudinal cap coordinate fixed,
so they preserve a previously imposed relative cusp condition at each
corner. Multipliers are now supported at finite height. Disjoint
source collars can be chosen, with product collars at the circular
seams. Composition gives bounded chain equivalences i,p with the
compact pair (C,T) or (C,E), and a bounded J such that
ip=I-dJ-Jd. The complementary finite face is absolute in the Hodge
realization; it is not silently deleted from the topology.

## 5. Closed range and the complete kernel, not merely finite Euler

The compact core has a smooth boundary partition with circular seams.
The ordinary mixed de Rham complex has a bounded homotopy K_C and
finite harmonic projection Pi_C satisfying dK_C+K_Cd=I-Pi_C.
This uses the compact mixed-boundary theorem, applied in a finite
boundary-adapted atlas with uniformly equivalent smooth metric norms.
Local relative regularization and zero extension preserve the boundary
partition; a global Euclidean embedding of C is not an assumption.
See [Pauly--Schomburg, Lemma 4.6 and Theorems 4.8--4.9](https://arxiv.org/pdf/2106.03448)
for the local regularization/closed-range input, and
[Licht, section 7.1](https://arxiv.org/pdf/1710.06868) for its relative
Betti-number interpretation. No singular/noncompact theorem is being
borrowed at this compact step.

Set Q=J+i K_C p and Pi=i Pi_C p. Then

```text
dQ+Qd=I-Pi,     rank(Pi)<infinity,     Pi d=0,     d Pi=0.
```

For closed u with Pi u=0, this identity gives u=dQu. Conversely Pi
annihilates every exact form. Therefore ran(d)=ker(d) intersect ker(Pi),
which is closed in L2. The chain equivalences identify the full
cohomology with the finite pair, not just its dimension or Euler.
The closed-range Hodge theorem then identifies these groups with the
normalizable harmonic kernel of the declared D. See
[Arnold--Falk--Winther, sections 3.1--3.2](https://www-users.cse.umn.edu/~arnold/papers/bulletin.pdf).
This also gives a gap off that finite kernel. Compact RESOLVENT of
the complete singular operator is not claimed or needed for this step.

R15's exact-sequence argument gives the table at the start under its
two-torus, H1(Q)=Z^2 and primitive nonzero three-arc intersection-vector
hypotheses. Its product-cell controls are recomputed at both grids;
they are not falsely identified with an m202 triangulation. Applicability
to the selected m202 fixed locus retains R15's declared source choice
and software geometric witnesses, not a new interval isometry proof.

## 6. Verification, evidence handling and next physics duty

The [design](WEIGHTED_COHOMOLOGY_DESIGN.md), new source and ten tests
were sealed at ad3857a7 before execution. [Focused checks](WEIGHTED_COHOMOLOGY_CHECKS.txt):
10 passed in 10.90 seconds. The unchanged producer's fully captured
[repeat output](weighted_cohomology_repeat.json) completed in 9.766 s:
all eight norm/conjugacy checks, 24 complex Hardy profiles, 216 actual
radial degree/sign checks, 18 two-resolution Volterra controls, exact
homotopy/cutoff/cap maps and full cellular pairs passed. The largest
Hardy squared-norm/bound ratio is 0.554728. The largest scaled Volterra
norm is 0.887804; the unweighted mutants exceed 3.78. Refinement changes
are below 0.021372. These numbers check the proof's instruments, not
an infinite-dimensional theorem by finite sampling.

The FIRST producer also exited zero, but its receiving tool budget
truncated the output. The [incomplete capture](weighted_cohomology_first_capture.partial.txt)
is retained explicitly as incomplete; it is not presented as parseable
full JSON. An orchestration store also rejected an undefined exit code
while the process was still live; its saved handle was polled through
completion. No scientific source, assertion or tolerance was changed.
The full repeat is labeled a repeat, not retroactively called the first
run. Raw retrieval whitespace is preserved rather than normalized.

The result discharges the global closed-range and complete-cohomology
join for the stated strong MAXIMAL complex. It does not select that
complex or the amplitudes physically. The next duty in this same path
is the parent gauge/fibre and defect law, followed by the four/one
pair's allowed mass terms and anomaly/inflow consistency in one action.
The compact E6 adjoint's spinor labels do not by themselves prove a
standalone anomaly-free four-dimensional theory. No additional physical
generation, normalization or quantized source strength is assumed.

The fetched outside-bench head advanced to 6c7aaba6. Its full new memo
and producer were read, not rerun or accepted as a boundary-theory
identification. Its Seifert-surgery series is explicitly different from
the cusped complement; its numerical growth fit cannot replace the
required boundary sector/normalization map on our partial-filling witness.
That separate candidate remains live without displacing this path.

This checkpoint is not a full-repository green suite, independent
receiving-seat acceptance or main banking. Those duties and the
pre-existing failure records remain explicit.

The completed [broad regression](WEIGHTED_COHOMOLOGY_REGRESSION.txt)
has 222 passed, 7 failed, 8 errors and one optional-GUI warning in
243.93 seconds. The seven original failed test IDs and eight original
fixture-error IDs exactly match R17's receipt. The 35-file tree was
unchanged while it ran. Original sources/tests and separate successful
repair controls are retained, not rewritten into an all-green history.

[Reporting gates](WEIGHTED_COHOMOLOGY_GATES.txt): 27 passed / 3 failed,
review due at 114 merges. Attribution has a NEW failing footprint:
four literal upstream branch-name tokens in the sealed raw retrieval
receipt, alongside the older inventory debt. Static vacuity and eight
older sealed-design marker omissions also remain. No baseline increase,
exemption or alteration of the sealed receipt is used to manufacture
green. Resolving that publication/seal policy conflict needs a separate
banking decision; the source, test and report claims are not broadened.

# agy branch: first source audit, conditional positives and required repairs

October 26, 2026. Reviewed publication: origin/agy/frontier-2026-10-26,
3e519e627cb19d093ce4c1e9e2b17f6d5027e3a0. The local checkout was first
read at its predecessor 2e8a5ab4d while publication was pending. The
branch then appeared on GitHub and was fetched successfully. The earlier
thirteen-branch sweep was accurate at its fetch time; the published
population is now fourteen. No other checkout was modified.

This is a source/record audit and hand algebra, not a numerical rerun,
banking acceptance or scientific execution permission. Its primary scope
is B1759--B1761, with B1755 and B1757 as the relevant result/fit sources.
B1756's experimental-neutrino claims and B1758's large rational pencil
have NOT been independently reviewed in this checkpoint.

## 1. What is useful

B1755 reports the preregistered composite cell holds on orders 15/20
versus 13/14, while failing the look-corrected statistical bar. Its
reported successful rows all have alpha=2/5; the proposed extension
3 alpha=plus/minus 1/5 is not sufficient. This narrows the pattern in
the supplied frame. It is a result now, superseding the previous
audit's observation that only its design had been published. Its
numerical pipeline has not been rerun by this seat.

B1759 offers a useful analytical dependence: normalized channel shapes
can be independent of the difference twist, leaving sector dependence
in the residues. Its actual tests compare four already chosen strip
points, not arbitrary global background data. The theta-addition
argument deserves preservation and a normalization-complete proof.

B1761 makes a precise residue-zero condition and an inverse-Gram ansatz
available for scrutiny. These are more informative than unconstrained
doublet fits. The latter may become a mechanism if its source and
quadratic operator can be derived in the SAME physical action.

## 2. C1: preserve the order-ten conditional arithmetic, repair notation

The producer's twist arguments are characteristic pairs, not simply
the complex points x=q_L w and y=q_R w. Write those pairs as (a_x,b_x)
and (a_y,b_y), and set

    Z_x=2 a_x tau+b_x=2 q_L w,
    Z_y=2 a_y tau+b_y=2 q_R w.

Using the actual bil() definition, theta1's tau quasi-period and
theta3's half-period shift, the off-diagonal sum giving the i-channel
residue is proportional, by a nonzero prefactor, to

    theta3(Z_x|2tau) theta2(Z_y|2tau)
      +theta2(Z_x|2tau) theta3(Z_y|2tau)
    =theta2((Z_x+Z_y)/2|tau)
       theta2((Z_x-Z_y)/2|tau).                     (1)

This identity also follows by reindexing the two absolutely convergent
series according to the parity of their two indices. In the complex
twist variables its arguments are (q_L+q_R)w and (q_L-q_R)w, NOT half
of those complex points. B1761's printed expression theta2((x+y)/2)
theta2((x-y)/2), followed by x-y=5w and 5w=1/2 mod lattice, mixes these
two conventions. It needs an explicit dictionary, not rejection of
the observed zero.

In periods 1,tau, theta2(z|tau) has zeros at z=1/2+Z+tau Z.
With the dictionary corrected, up-only vanishing through the difference
factor indeed yields

    5w=1/2 mod (Z+tau Z).

For the stated nonzero slope a in (0,1/2), this gives a=1/5 or 2/5
and b an odd tenth. Each has primitive order ten. This is a valid
conditional arithmetic implication; it does not itself derive why
the physical state must have that asymmetric channel zero. The remaining
j/k nonvanishing and absence of other cancellation mechanisms need the
complete channel formulas for an all-order converse.

The standard Fourier, half-period and zero formulas were personally
consulted at https://dlmf.nist.gov/20.2 and the product/addition context
at https://dlmf.nist.gov/20.7 on October 26. Equation (1)'s characteristic
dictionary is an author hand reconstruction from the actual source,
not a newly executed theta-function test.

## 3. C2 is a selected frame/point criterion, not a foundational selector

The 662-line producer evaluates C1 and C2 at ONE specified tau,
0.3145+3.0345i, a point already chosen from the mass-fit strip. C2 uses
both I_up<0.05 and a doublet/scalar ratio>2. The broader text calls
these equivalent, but no general equivalence is proved by those code
conditions; on the stored survivors they happen to give the stated split.

The cutoff, the named i-channel, up/down assignments, nontrivial-slope
restriction, point tau and the near-null preference are premises. A
calculation can use no measured masses internally and still select its
criterion after inspecting successful fits. No prior seal selecting
C2 from the foundational principle was exhibited in this package.
Thus "data-free" is safe as a statement about formula inputs only;
it is not evidence that the selector is independent of the known target.

This is also a T-orbit result in a chosen marking, not automatically
an invariant selection under every modular move. For example S sends
the line coefficients (a,b) to (b,-a), up to inverse/sign conventions.
(2/5,1/10) is sent to a representative with slope 1/10, outside the
displayed C1 set. A covariant selector would have to transport the
channel labels, cycles, fields, metric and measuring data together.
The complete relational action could supply such data; this test has
not derived that selection. The conditional order-ten result survives.

## 4. Read the actual committed numbers before calling it parameter-free

The following are values read from the committed B1761 JSON, not reruns:

| tau | inverse-Gram H_d with fixed conjugate DR H_u: chi2_nine | fitted up pencil, 2 reals | plus fitted exponent, 3 reals | original free-doublet fit |
|---|---:|---:|---:|---:|
| 0.3145+3.0345i | 325.27 | 33.49 | 25.07 | 19.08 |
| 0.333333+3.05505i | 353.27 | 37.35 | 25.35 | 4.05 |
| 0.3145+3.10i | 409.83 | 41.76 | 23.82 | 29.17 |
| 0.3145+2.95i | 250.01 | 29.38 | 27.88 | 2.75 |

The stated nine-observable bar is 21.67. Neither the fully fixed
construction nor the displayed 2-/3-real fitted versions reaches it.
The decrease is still a useful conditional modeling observation.

The 19.59 result is a HYBRID: the source retains the complete fitted
H_u and the fitted h_d1,h_d2, replacing only h_d0 with a Schur estimate.
Its success cannot be attributed to a parameter-free complete pair.
Likewise the full inverse-Gram vector with fitted H_u gives about
32.01 at the primary point; the 325.27 value uses fixed H_u instead.
Those two experiments must not be conflated.

The committed primary overlap is 0.99996741, angle 0.46257 degrees.
FINDINGS instead quotes 0.999961 and 0.506 degrees; its verdict JSON
and lock use the former numbers. That is a report/output discrepancy.
Across the other three points the angles are 6.85, 2.92 and 8.68 degrees,
so the sub-degree agreement is not a four-point result.

The fact that a restricted 3-real fit beats a saved free-doublet fit
at one point is evidence that the saved unrestricted optimizer may
not have reached its best minimum. The unrestricted parameter space
contains that restricted candidate, so its global minimum cannot be
worse at the same point and with the same objective. This is not proof
of a reduction mechanism from a superior fit.

The B1761 locks read saved JSON and assert bounds; they do not recompute
theta residues, Gram matrices, or optimizations. Reported lock passes
are not independent scientific reproductions. Several scratch launches
failed in the pasted session; a complete execution/custody assessment
must preserve their scripts, logs and sequence as well as the final pass.

## 5. What would earn inverse-Gram dressing?

Let H=conjugate(Sigma_down), assumed positive definite in the proposed
coordinate convention. The vector H^(-1)v is the stationary response of

    E(h)=h^dagger H h-2 Re(v^dagger h).               (2)

This is a direct hand differentiation. With a fixed norm constraint,
the stationary equation instead is (H+mu G)h=v for the actual kinetic
metric G and a multiplier mu; without a source, minimizing h^dagger H h
on the unit sphere selects an eigenvector, not generally H^(-1)v.
Normalizing an unconstrained response afterward does not prove it solves
the constrained problem. Fractional powers H^(-beta) introduce another
choice unless a real operator or effective action derives beta.

The Gram of a chosen Yukawa map is a well-defined mathematical quantity.
It is not thereby the physical Higgs Hessian, its boundary-response
matrix or its kinetic metric. Equation (2) would need the actual source
v, pairing, conjugation law, Hessian, boundary conditions, complementary
mode response and stability to come from one admitted action. Treating
the seed as a covector also needs its transported metric under a change
of Higgs basis. Matrix inversion alone does not establish that map.

The opportunity is concrete: test whether the already supplied parent's
elimination produces this response, rather than inventing a new action
chosen to yield the successful vector. A proof of that connection would
replace an independent Higgs-direction choice conditionally. Selecting
the inverse-Gram recipe after fitting is not yet such a payment.

## 6. B1759's normalization needs a small but load-bearing repair

Its displayed norm uses d^2u/Im(tau), while P_s=R_s/u+O(1). In a local
coordinate disc, the logarithmic divergence is therefore

    |R_s|^2 [2pi/Im(tau)] log(1/epsilon),

not |R_s|^2 2pi log(1/epsilon). The actual cA producer integrates d^2u
and subtracts 2pi log(1/epsilon), consistent with the UNDIVIDED measure.
Choose one norm convention and transport its finite part and L weights.
This does not negate a sector equality at fixed tau, but it matters
before interpreting c_s or the Gram as a physical normalization.

## 7. B1760 supplies useful checks, not the advertised full-proof review

The source verifies frozen hashes, parses test names, and checks scalar
Weyl, Schur and local-core algebra. These are useful independent controls.
They do not supply a specialist review of global Sobolev/removability,
Hodge geometry, graph-domain smoothness or physical state claims.

There are specific audit-report defects:

- Its FINDINGS lists ten P210 method names that are not the actual
  frozen methods. Its own saved JSON has the correct, different names.
  The producer asserts only that there are ten, not their exact names.
- The Hodge and dressed-domain summaries do not describe our proofs
  faithfully. Our domain note proves smooth isolated spectral clusters
  under stated assumptions, not general continuous rotation of a zero
  kernel. Our Hodge note distinguishes modular base and elliptic fibre;
  it does not derive shifting flat holonomy by fibre translation.
- The script hashes the eight notes but does not computationally verify
  each note's proof. Its scalar/two-block checks must not be promoted to
  all eight arguments' full analytic acceptance. Some quoted predecessor
  commit labels also need reconciliation against the actual objects.
- The assertion that eliminating complementary modes changes the metric
  unless BOTH off-diagonal A and G vanish is too strong in its general
  G formula. If A_off=0 then Pi=(I,0)^T and Pi^dagger G Pi=G00 even with
  G_off nonzero. The correct identity is valuable; that converse is not.
- The class-null script hard-codes B1753's own-seed hit count as 36.
  Main's B1753 findings and W157's independent calibration report seven
  for the decisive seat menu. A different statistic/menu must be named
  if 36 is intended; it cannot silently replace that count.
- Its 71-look confidence threshold is hard-coded as five, while the
  B1755 preregistration specifies four using the exact 97.5% upper end.
  The confidence convention and actual bound must be reconciled.

The class-choosing calibration itself is worthwhile supporting work.
It prices finite named menus under an empirical null, not all imaginable
post-hoc rules. Its in-sample ranks and shared training/test targets need
their actual finite-sample interpretation. These reported numbers have
not been rerun here, and calling them "exact" must not imply analytic
probabilities without Monte Carlo uncertainty or independent samples.

None of the above invalidates the already completed independent P210
review. Nor does B1760's concurrence replace main's exact acceptance,
the frozen execution gate, or the separate review scope for later work.
I do not upgrade our quaternion domain proof to reviewed on this basis.

## Verdict and next action

There are promising conditional results to reuse: a residue identity,
order-ten arithmetic under an explicit condition, sector norm dependence,
and a compact inverse-Gram response candidate. The reported numerical
improvements are real entries in the stored output, not yet reproduced
science or a parameter-free derivation of the nine observables.

Repair source/report mismatches; derive the C1/C2 selection duty or label
it an ansatz; test covariant metric/source transport; and ask whether
the same admitted parent actually produces (2). Keep the exact local
and global boundary work primary. No foundational input, physical
three-generation spectrum or gravity row is closed by this checkpoint.

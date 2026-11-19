# Native symmetry fixes a metric, but not this full registering law

2026-11-18. Author hand derivation under scope fe35fea58.
Delivery completed 2026-11-19; the date above records its start.
**Not independently checked.** No scientific code, numerical check,
CAS, data comparison or physical parameter derivation.

Read with NATIVE_SIGNED_ACTION_AND_INVARIANT_METRIC.md. The action is
native; its interpretation as a stochastic state space and law is an
explicit test hypothesis. This is not a countermodel to all OA axioms.

## 1. Exact test package

Supply the following conditional interpretation:

1. The states are X6={+ei,-ei: i=1,2,3}, acted on by the native proper
   signed-permutation group G, not all generated architecture.
2. A time-homogeneous continuous-time classical Markov law acts on
   functions on X6. The full signed state is an admitted readout.
3. Every g in G preserves this one fixed law, rather than merely
   transporting it to a differently expressed law.
4. The law connects all six states. We also test strictly positive
   rates between every two distinct states, a stronger requirement.

None of the probabilistic framework, physical clock, readout assignment,
Markov property or fixed-law symmetry is claimed derived from PF1-PF3.
The question is whether even this supplied symmetry fixes the relative
response. A later physical construction need not use this framework.

## 2. Classify the entire invariant rate cone

For a finite permutation action, a matrix L commutes with every
pullback C_g f(x)=f(g^-1 x) exactly when

    L(gx,gy)=L(x,y) for every g,x,y.                          (1)

This follows by comparing the coefficients of f(y) in C_g L f and
L C_g f; conversely that equality makes the two sums coincide. Thus
entries are constant on G-orbits of ordered pairs. This is a standard
finite group-action observation, not a new general theorem.

The previous file proves that the pair orbits on X6 are equality,
antipodes, and perpendicular states. Nonnegative off-diagonal entries
and zero row sums therefore give exactly

    (L f)(x) = a [f(-x)-f(x)]
                + b sum_{y perpendicular to x} [f(y)-f(x)],  (2)

    a >= 0, b >= 0.

There are four terms in the second sum. Each row has antipodal
rate a, four perpendicular rates b, and diagonal -(a+4b). Conversely
every (2) has all stated symmetries. It is irreducible exactly when
b>0: perpendicular moves connect the octahedral graph, including an
antipode in two steps; with b=0, the three axis pairs do not communicate.
All distinct-state instantaneous rates are positive if a,b>0.

No Markov existence assertion requires a numerical computation. For
c=a+4b>0, P=I+L/c is stochastic, and

    exp(tL)=exp(-ct) sum_{n>=0} (ct)^n P^n/n!                (3)

is a nonnegative row-stochastic semigroup. If b>0, every pair of
states is linked by a finite P path, so every transition probability
in (3) is positive for t>0. L is symmetric; the uniform measure
mu(x)=1/6 is stationary. The spectrum below also proves its uniqueness.

## 3. Carry both the even and the signed responses

Every function has an even part f(-x)=f(x) and an odd part
f(-x)=-f(x). Write an even function as f(sign*ei)=vi. Then

    (L f)(sign*ei)=2b sum_j vj - 6b vi.                      (4)

Its constant component has eigenvalue zero, and its sum-zero plane
has eigenvalue -6b. An odd function has f(sign*ei)=sign*wi. The
four perpendicular values cancel in pairs, while the antipode gives
-2a f(x). Thus

    L f=-(2a+4b) f on the entire odd space.                  (5)

The full six-state spectrum, with multiplicities, is

    0 [1],    -6b [2],    -(2a+4b) [3].                     (6)

The odd space carries the signed irreducible triplet already recovered
in the previous file. This is not three matter multiplets or three
generations of fermion zero modes. When b>0 both nonconstant
eigenvalues are strictly negative, so the stationary distribution is
unique and the semigroup converges to it.

There are scalar readouts of these channels that carry the measuring
data as well as the law. Put fi(x)=xi and
gi(x)=1_{axis(x)=i}-1/3. With stationary expectation define

    C_signed(t)=sum_i E_mu[fi(X_t) fi(X_0)],
    C_axis(t)=(3/2) sum_i E_mu[gi(X_t) gi(X_0)].              (7)

At t=0, sum_i fi(x)^2=1 and sum_i gi(x)^2=2/3 pointwise.
Equations (4)-(5) therefore give the exact normalized correlations

    C_signed(t)=exp[-(2a+4b)t],
    C_axis(t)=exp[-6bt].                                    (8)

Both sums are invariant under G: signed coordinate readouts rotate
together, and the axis indicators permute together. The invariant
quadratic metric's common scale cancels upon normalization. Under
any passive re-expression the state, law, readouts and inner products
must all be transported; changing coordinates alone does not erase
their different decays.

One common clock change scales both decay rates equally. The ratio

    R = (2a+4b)/(6b) = (a+2b)/(3b)                          (9)

survives. For positive b the two strictly positive controls a=b and
a=2b give R=1 and R=4/3, respectively. These are typed-in
mathematical examples, not inferred or measured constants. In the
first, all five nonconstant modes have the same eigenvalue; in the
second they split into multiplicities two and three. No invertible
linear conjugacy followed by a common clock rescaling can relate
those two spectra. Independent rescaling of the two clocks would
change the tested joint process, rather than re-express it.

## 4. The parity quotient is exact for its own predictions

Let q(sign*ei)=i. For any function v on X3, (4) says exactly

    L q* = q* Lbar,
    (Lbar v)(i)=2b sum_{j != i} [v(j)-v(i)].                 (10)

Hence each directed off-diagonal coarse rate is 2b, and the diagonal
rate is -4b. The antipodal term a is invisible. This is a valid
strong lumping, with all finite coarse state-history probabilities
preserved for every initial distribution on X6. One can either use
the earlier predictive-register proof or note directly that the
rate to a different coarse fibre is 2b, independently of the sign.

S3 is doubly transitive on X3, so any invariant state generator on
that carrier has just one off-diagonal rate and is unique up to a
clock. The coarse result is a positive, not an error to overturn.
But the signed coordinate functions are odd and do not factor through
q. Their correlation in (8) cannot be recovered from the coarse
state process alone. Comparing a=b and a=2b with b fixed gives the
same entire X3 process and different X6 signed responses.

The conclusion is relative to admitted readouts. If only the unsigned
axis is observable, a has no observable price in this model. If the
signed triplet is observed, the quotient omits a response channel.
If the individual move labels are observed, their instrument kernels
must also be retained: the state-only assertion in (10) does not
assert that every labelled implementation has only one clock.

## 5. Can the alternatives use the actual transformations?

The following supplies an explicit implementation, with its extra
clock choice visible. Let A f(x)=f(-x), Pi f=(1/6) sum_y f(y).
Average pullbacks over all 24 elements of G. Transitivity gives Pi.
The three half turns about coordinate axes, namely (5) in the previous
file, form a conjugacy class. Their average H satisfies

    H=(I+2A)/3:                                            (11)

on a signed axis, one such rotation fixes it and the other two reverse
it. For a>=b>0, (2) can thus be implemented as

    L=6b(Pi-I)+(3/2)(a-b)(H-I).                             (12)

The first process chooses every group element at rate b/4. The
second adds rate (a-b)/2 to each of the three half-turn labels.
All 24 labels retain positive rate; native ell, r and their inverses
are among them. Rates are inverse-symmetric and constant on conjugacy
classes, as required for a fixed-law symmetry. Equation (12) gives
both positive controls used in section 3 without inventing new state
transformations.

The price is decisive: a whole group element, and therefore some
composite native word, is allowed to be one Poisson event. This does
not prove that a model with a prescribed elementary-letter clock has
the same freedom. The prior history-weight proof explains why endpoint
group multiplication alone cannot justify that temporal quotient.

There is an informative opposite control. If one postulates that
only the six quarter turns about coordinate axes and their inverses
are elementary events, with equal rate r0 per label, then exactly
four labels move a given signed axis, each to a different perpendicular
state. Two fix it. Thus (2) has a=0, b=r0 and R=2/3. The process
is connected and has positive finite-time transitions, while its
instantaneous antipodal rate is zero. It is therefore outside the
stronger strictly-positive-instantaneous-rate subclass, as it should be.

This six-label alphabet is conjugacy-closed in G. Using only the four
labels ell, ell^-1, r, r^-1 is a different restriction and need not
preserve all of G as a fixed-law symmetry. One cannot impose full
symmetry on the first model and silently change to the second clock.
Neither alphabet nor its physical event interpretation is derived here.

## 6. What this earns, and what must be earned next

This conditional test has an analytic answer. The complete invariant
state-rate cone on the chosen signed orbit has two rates. A common
clock removes one scale, leaving a dimensionless signed/unsigned
response ratio. The unsigned quotient hides precisely that ratio
while remaining a correct coarse process. In contrast, the invariant
positive quadratic metric on the signed module is already fixed up
to scale. These statements concern different mathematical objects.

This narrows the next earning question: what counts as an elementary
physical event, what histories and labels can be distinguished, and
what principle fixes their weights or generator? Deriving a local
alphabet or a response relation could remove the ratio. Merely
asserting that all allowed histories occur, or that the native symmetry
is present, supplies no such relation in this package.

The test supplies no universal obstruction to a deterministic, quantum,
non-Markovian, field-theoretic or more highly constrained law. It does
not select this orbit, derive a spacetime, a physical action or a
family representation, nor establish a no-go theorem for the complete
registering architecture. It removes zero independent foundational
inputs and derives zero physical parameters. Review must check the
whole premise-to-conclusion chain, not only the sample eigenvalues.

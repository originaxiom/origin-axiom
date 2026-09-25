# F19: the complete positive-q family has harmonic backgrounds and the pairing

September 25, 2026. Local `audit/fork-2026-09-20`.
Scientific seal **bd2a533e** preceded every scientific execution.

## Result and evidence grade

The finite gates all pass for **every real q>0, q!=1**, not just a
generic parameter or the four previously tested exceptional points.
Both inversion intertwiners are invertible, the fixed sixteen word
matrices span the full complex matrix algebra, and the actual peripheral
frame is finite and invertible throughout that domain.

With these algebraic hypotheses established, F12/F13's authored analytic
argument gives a smooth determinant-one harmonic metric at each such q,
unique in the specified bounded-reference-distance end class. Combining
this with F18 extends the geometric dual pairing to **every finite cyclic
degree and every scalar fourth-root character**, throughout this family.
The complete Hodge spectra and corresponding classical interaction
tensors are paired, where those interactions are defined.

The analytic application is an authored proof, not independent review
or a global numerical PDE solution. The exact tests certify its finite
inputs, not the entire analytic argument. This result does not establish
physical chirality, finite Higgs energy, a quantum phase or a TOE.

## 1. Exact certificates with no hidden positive exception

In the primitive polynomial normalization used here, put Q=q^2+q+1.
The determinant identities are

    det J_theta  = -16 q Q^3,
    det J_thetaT = -16 q^3 Q^3,
    det F_words  = -(q+1)^10 (2q+1) Q^3 / q^7.

Every displayed factor has a definite nonzero sign for q>0. The producer
also checks exact positive-root counts of the numerator and denominator,
with q=0,1 explicitly isolated. The two full matrices and all certificate
outputs are retained in [EXACT_WITNESSES.json](EXACT_WITNESSES.json).

For example, the newly extended swap-inversion witness is

    J_thetaT =
    [ 3q^2+4q+4    q^2       -2q(q+1)       2q(q+1)      ]
    [ q^2         -q^2        2q(q+1)      -2q(q+1)      ]
    [-2q(q+1)      2q(q+1)   -4q            4q           ]
    [ 2q(q+1)     -2q(q+1)    4q            q^3+q^2-3q  ].

It satisfies rho(g)^-T J=J rho(thetaT(g)), with thetaT(m)=n^-1 and
thetaT(n)=m^-1, in the original literal SL4 family. Both intertwiner
systems have generic rank fifteen and kernel dimension one. Specializing
these polynomial witnesses recovers F17's independently solved witnesses
at all four exceptional points, up to nonzero scalar.

The actual cusp conjugator has det P=-(q+1)^2/4. Its entry denominators
are 1, 2(q-1), and 2(q-1)^2(q+1), so it is finite precisely where needed.
The determinant alone would NOT have caught its q=1 pole. That is why
the entry-pole certificate and its determinant-one counterexample matter.
Both peripheral conjugacy equations are checked exactly.

The word determinant even remains nonzero at q=1. That does not extend
this cusp or analytic argument to q=1: beta and the peripheral frame
are singular there and the semisimple longitude gap vanishes. F10's
separate geometric-point treatment is retained, not overwritten.

## 2. The positive analytic extension

F12's energy floor, finite reference excess, compact exhaustion and cusp
maximum principle do not use either exceptional quadratic equation.
The missing family-wide input was the full matrix algebra preventing
escape of the harmonic-map values. The determinant above supplies it
at every fixed q in the declared domain. F13's bounded-distance,
finite-volume uniqueness argument then applies as written.

Thus the arbitrary compact-core extension of the reference metric is
not an additional choice of solution in that end class. Unitary scalar
twists leave the harmonic metric equation unchanged; finite-cover
pullbacks remain solutions. F18's unipotent-power recovery supplies
irreducibility of cyclic restrictions where the pairing argument uses it.

This is POINTWISE in q and degree. There is no uniform estimate as q
approaches 0, 1 or infinity, no proved smooth global metric dependence,
and no new normalizable q modulus. The fixed hyperbolic base still gives
infinite total Higgs norm. The fixed-end residual-square action and the
fluctuation norm are distinct quantities, as before. Neither the base
metric, parent action, q nor the physical end law has been selected.

## 3. The all-degree consequence, and its boundaries

F18's marked character argument is independent of q. For every central
character on a cyclic cover it chooses a deck lift of theta or thetaT
that inverts that character. The polynomial matrices above now provide
the required bundle maps everywhere on the positive parameter domain.
Their bounded reference-norm comparison and harmonic-metric uniqueness
give an actual unitary equivalence of the complete operators, not only
equal ordinary-cohomology dimensions.

This does not compute new matter multiplicities at arbitrary q or on
arbitrary covers. A paired spectrum may have no light modes. Nor does
the base's previously proved six-sector acyclicity propagate by fiat:
additional mediator kernels must be retained. Positive-p^2 resolvents
are paired; zero-momentum response requires the actual kernel, source
domain and inverse treatment. There is no new numerical mass gap or
Wilson coefficient in this cell.

Consequently changing q, cyclic degree or a central mu4 character ALONE
does not escape this geometric pairing in the specified construction.
This is not a no-go for other holonomy components, noncyclic or noncentral
data, changed end/source equations, another base metric or a dynamical
asymmetric phase. The other seat's canonical metric is not substituted
for the hyperbolic metric here.

## 4. Controls and execution

**Seven new tests pass**, 7.94 seconds. **Fifteen unchanged F12 tests
pass**, 82.49 seconds, and **nine unchanged F18 tests pass**, 18.17 seconds.
The initial combined antecedent invocation failed during collection
because both files are named test_verify.py. Its original exit 2 and
stdout are preserved; separate processes resolved collection without
changing any science, renaming files or deleting caches. There was no
failed new mathematical test and no post-data scientific correction.

Controls reject a wrong base map, a fixed-q witness used generically,
a wrong imaginary character phase, duplicate word columns, a positive
root at q=2, a positive pole at q=2, an identically zero determinant and
a matrix whose finite determinant conceals an entry pole. Rational
specializations independently reconstruct the word products and their
determinants, and all four exceptional-point values agree with F17.

[Design](DESIGN.md), [proof](PROOF.md), [seal](SEAL.json),
[execution metadata](EXECUTION.json), [custody](RECHECKS.md).
These are focused runs, not a full-repository green or peer review.

## 5. What this changes in the mission

The constructive advance is a whole family of completed gauge-equation
backgrounds, not another isolated numerical example. The strategic
advance is knowing which repeated searches cannot supply the proposed
asymmetry: this same q/cyclic/central-twist family retains the full
geometric pairing, not merely a coincident count.

The next bounded physical audit should test a genuinely different
hypothesis. R33/R34 already derive a nonzero number-changing quartic in
an ADDED four-dimensional scalar/fermion model; they explicitly do not
derive those fields or phase locking from these completed backgrounds.
Before spending its mirror-gap interpretation here, check whether the
adopted parent's actual low-energy matching supplies that interaction,
including the needed phase-locking term, both paired sectors, contact
terms and exchanges. A positive scalar-block response by itself is not
that complete matching calculation. Whether the required ingredient is
present is a question to verify, not an absence claim or a fresh kill.

Only a subsequently specified asymmetric state/end/source mechanism
can then be tested for selective gapping, backreaction and anomalies in
the SAME theory. No arbitrary zero coupling or inserted rescue field
counts as a derivation. Object-selected inputs, measured predictions,
Lorentzian gravitational dynamics and the full TOE remain unachieved.
No shared B number, main-bank claim, push or external publication.

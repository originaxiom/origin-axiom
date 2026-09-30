# Canonical logarithmic cone end and its admission limit

September 30, 2026. Path-local R66 advances the necessary common-model
connection in [PHYSICS_MISSION](PHYSICS_MISSION.md). It does not derive
physical chirality, global dynamics or a complete theory.

The actual canonical rank-four peripheral representation admits an
authored exact local solution of BOTH supplied field equations on a
declared rectangular cone end. It retains the full peripheral pair at
every positive radius while its radial conjugation becomes unbounded.
This walks R65's explicit outside-hypothesis route, not a refutation of
the bounded-transport obstruction.

The same solution is locally L2 but not a fluctuation in the old
graph-plus-L4 space about its limiting reference. Existence of a new
background and admission to a previously fixed domain are distinct
questions. Neither half of the result may erase the other.

## Checked construction

For q>0, q!=1 the actual peripheral matrices reduce to exp(N) and
q^D(1+beta P), where N=E02+E23, P=N squared, D=diag(1,-3,1,1) and
beta=6/(q-q inverse). Put H=diag(1,0,0,-1). With a period-one rectangular
unit-area link inverse diag(alpha,1/alpha), alpha>0, the connection

    C_r=h' H, C_x=exp(-h)N, C_y=log(q)D+beta exp(-2h)P

is flat for any smooth h. Its moment equation is

    2(r squared h''+2r h')+alpha exp(-2h)
      +(beta squared/alpha)exp(-4h)=0.

A local center-manifold argument establishes a solution for each fixed
parameter pair, with s=-log(r) and

    exp(2h)=alpha s+
      (beta squared-alpha cubed)/alpha squared log(s)+O(1).

The [authored proof](NILPOTENT_CONE_PROOF.md) gives the hypotheses,
comparison argument and external theorem application. Symbolic checks
verify the reduction and polynomial invariance residuals, not the
external analytic theorem or independent acceptance of this proof.
No convergent formal-series assumption or global uniqueness is used.

When beta squared=alpha cubed there is an exact elementary comparator
h=log(alpha(s+c))/2. At alpha=1 its two q values are 3+sqrt(10) and
sqrt(10)-3. These are test cases, not selected physical numbers.
For generic parameters that leading logarithm alone leaves a divergent
residual-square action; the exact nonlinear correction is essential.

## Holonomy and domains

The meridian remains an index-three unipotent at every r>0 and the
longitude remains conjugate to its actual source matrix. The limiting
pair is (1,q^D), but the conjugating condition number grows as alpha s.
The radial term tends to zero after multiplying by r, yet not at any
positive power of r. R65 therefore does not exclude this branch.

For a=C-log(q)D dy the radial L2 density is asymptotic to 2/s and is
integrable against dr. In contrast:

| tested norm | leading radial density | conclusion near r=0 |
|---|---|---|
| L4 of a | 4/(r squared s squared) | divergent |
| squared norm of d_Cinfinity a | 1/(2r squared s cubed) | divergent |
| squared norm of d_Cinfinity dagger a | 1/(2r squared s squared) | divergent |

The FULL flatness and moment residuals are zero, so their supplied
sum-of-squares action is zero. This does not permit discarding boundary
terms or declaring every other formulation of physical energy finite
on a singular space. A justified background-relative variational and
fermion domain is still needed.

The rectangular metric is an input. The checked nonrectangular cross
term obstructs this particular scalar ansatz; it is not a theorem that
all nonrectangular solutions fail. The reducible SL5 block inclusion
preserves the equations but does not identify this bundle with the
other seat's rank-five monomial family.

## Execution record

Design, proof, input pins, producer and tests were committed and
server-confirmed at 28c4aa3ec20fc112a45971777fe603530bf80f85 before the
first scientific import or run. See [design](NILPOTENT_CONE_DESIGN.md),
[input pins](NILPOTENT_CONE_INPUTS.json),
[producer](nilpotent_cone.py) and
[tests](../../tests/test_physical_bridge_nilpotent_cone.py).

The first native run passed 86/86 exact checks. All eight dedicated
tests passed. The fixed combined population has eight files and
60 tests: 56 pass and the same four original R63/R64 failures remain.
No old test was rewritten, rebound or hidden. These are focused runs,
not a full repository suite or main-bank certificate.

[Receipts](NILPOTENT_CONE_RECEIPTS.json) retain first outputs, actual
exit codes and byte hashes. The [custody check](nilpotent_cone_receipt_check.rb)
checks five frozen science paths, eight own source pins, the read source
PDF digest, public redactions and exact test populations. It is not
independent mathematical review. The four historical governance failure
categories remain; no new governance failure is accepted.

The cumulative custody check passes: 1029 artifact digests, 369 latest
distinct seal entries and 198 selected legacy relative links. The same
24 older failed/error IDs are preserved by that historical custody
check; it does not rerun their science. Six first captures are published.

## What this advances and what remains

A flat toy counterexample has become a same-peripheral local solution
of both equations, for the actual canonical family and the explicitly
changed link geometry. That is a real conditional mathematical advance
toward matching the ingredients, not a derived physical phase.

Next: derive the end variational boundary terms and a compatible
background-relative boson/fermion domain, then test extension through
the compact core. Keep the finite-unitary monomial route distinct.
The architecture still must earn or price its action, metric and
physical realization; chiral matter, normalized observable interactions,
quantum consistency and gravity are not supplied by this local result.

# Boundary flux and admission of the logarithmic cone solution

September 30, 2026. Path-local R67 advances the action/domain duty in
[PHYSICS_MISSION](PHYSICS_MISSION.md). The actual R66 background survives
the action audit: a divergent expanded bulk term is cancelled exactly
by its boundary current. Dropping that term would be a false rejection.

There is also a nonempty, sufficient affine bosonic variational space
about this background. This is not yet a physical end law: the formal
radial zero profile fails its L4 admission condition, and no complete
fermion/supercharge domain or global particle mode is certified.

## What the regulated calculation shows

The external model remains the residual-square potential in
[Braun et al., section 2.1 and Appendix B.1](https://arxiv.org/html/1812.06072v2).
No new action is derived from the architecture here. R28 had already
demonstrated the importance of retaining the Bochner boundary on a
commuting hyperbolic tube. This calculation reuses that lesson for the
actual nonabelian cone, with independently metric-derived connection
coefficients, Ricci tensor, matrix derivatives and current.

Writing C=A+Psi, with A anti-Hermitian and Psi Hermitian, gives

    (g7 squared/2)V_[epsilon,R]
       = integral_epsilon^R E_exp dr+B(R)-B(epsilon),

where E_exp contains the gauge curvature, Higgs bracket, rough
covariant derivative and Ricci terms. On the exact logarithmic solution
V=0 and E_exp=-B'. With s=-log(r),

    B(r)=[12(log q) squared/alpha+1/s+O(log(s)/s squared)]/r.

The expanded bulk integral diverges if its boundary companion is
discarded. The regulated identity cancels it at every cutoff.
Subtracting only the commuting limiting reference removes the first
term but leaves the divergent 1/(r s) term. This is not a newly chosen
subtraction: the signed boundary term is fixed by rewriting the already
supplied functional. Full physical boundary completion remains separate.

The [authored proof](CONE_FLUX_PROOF.md) gives the identity, signs,
parameter restrictions and limits. It is not independent analytic review.

## A bosonic variational class without a free domain transfer

Let X0 be the compact-support closure in the combined L2, differential
graph, formal-adjoint graph and L4 norms, all about the ACTUAL background.
Holder's inequality controls the quadratic bracket terms. The supplied
potential on C+X0 is consequently finite, nonnegative and C1, with C a
stationary zero. Compactly supported compact gauge transformations
preserve this class.

This positive statement does not require C-C_infinity to belong to X0.
It also does not prove that X0 is physically selected or that its
first-order fermion operator has the required self-adjoint, reality and
supersymmetry properties. A bosonic variational class is not that
identification.

## The surviving radial profile

The actual tangent to h is a_f=d_C(fH). Its equations and norm are

    d_C a_f=0,
    d_C dagger a_f=-[f''+2f'/r-A_h f/r squared]H,
    A_h=alpha exp(-2h)+2beta squared exp(-4h)/alpha,
    r squared |a_f| squared=2[r squared(f') squared+A_h f squared].

Translation of the exact autonomous branch gives f=h_s. This solves
the Jacobi equation, is not removable by compact gauge, and is locally
L2. But its L4 density is asymptotic to 1/(4r squared s^6), which is
not integrable. It therefore fails the sufficient nonlinear X0 test;
this does not prove that every justified nonlinear domain rejects it.

The radial energy identity retains the outer boundary. The apex flux
vanishes, and zero outer Dirichlet or Neumann datum forces the profile
to vanish within this ansatz. Thus a local zero profile is not a
free global massless particle.

A separate Chern-Simons check gives zero boundary variation on the
triangular background parameter family. An explicit L2 lower-triangular
variation has nonzero boundary pairing but divergent differential norm.
Finite kinetic norm, zero boundary pairing and graph admission are
different predicates.

## Execution and verification

Five science paths were sealed and server-confirmed at
8c46c279bb702a1ac69421928eebc73a6203109c before the first scientific
import/run. See [design](CONE_FLUX_DESIGN.md), [inputs](CONE_FLUX_INPUTS.json),
[producer](cone_flux.py) and
[tests](../../tests/test_physical_bridge_cone_flux.py).

The first native execution passed 52/52 exact checks; all eight new
tests passed. The fixed combined population has nine files and 68 tests:
64 pass and the same four original R63/R64 failures remain. No old
test was rewritten or rebound. This is not a full repository suite.

[Receipts](CONE_FLUX_RECEIPTS.json) retain complete first outputs, actual
exit codes and hashes. The [custody checker](cone_flux_receipt_check.rb)
checks five frozen science paths, twelve prior source pins and exact
populations. The same four historical governance failure categories are
retained. Custody is not independent proof review or main-bank acceptance.

A provisional governance-baseline comparison was attempted while its
writer was still running and printed 'FAIL rows changed'. No dependent
write or commit followed. The same process was awaited to terminal;
the completed output matched the historical rows exactly. The receipt
records this sequencing mistake as a transcript note, not as a terminal
gate failure or a newly captured raw command.

Cumulative custody passes: 1037 artifact digests, 374 latest distinct
seals and 199 selected legacy relative links. It retains the same 24
older failed/error IDs without rerunning that old science. Six first
captures are published. These counts describe custody, not physics.

## Next physical obligation

Derive compatible first-order fermion, reality, supercharge and compact
gauge domains about the singular background. Include the outer/core
matching problem before counting modes. Determine whether a principle
selects or permits the required boundary law and link geometry; they
remain inputs. Physical chirality, normalized observables, quantum
consistency and gravitational dynamics are not derived by this result.

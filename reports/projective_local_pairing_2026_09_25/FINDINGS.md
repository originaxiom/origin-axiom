# F16: the geometric pairing persists in an actual local neighborhood

September 25, 2026. Local fork audit/fork-2026-09-20.
Scientific files and actual imports sealed at **515df2a4** before execution.

## Result and verification grade

**Every sufficiently nearby SL(4,C) representation at each of the four
exceptional points admits a symmetric invertible geometric matter--dual
intertwiner.** This is no longer only a tangent or finite-order statement.
The neighborhood is existential, with no claimed numerical radius.

The result follows from a convergent finite-dimensional analytic argument
whose finite hypotheses are checked exactly. **12 new tests pass** and
**56 unchanged F15/F14 tests pass**. No F16 failure or correction was
needed. The analytic proof is authored and still needs independent
specialist review; a passing finite suite is not itself such a review.

This is a local theorem about representations of the base member's
group. It is not an all-component/class/cover chirality no-go, a quantum
phase result, or a physical statement for arbitrary changed end data.
Theta is F14's orientation-preserving base inversion; it is not being
identified with Lorentz parity or physical CP by terminology.

## 1. The step beyond F15

F15 checked the FULL infinitesimal deformation space and found no odd
class modulo gauge. A direction with an even first derivative could,
in principle, break a symmetry at second order: the control curve
(x,y)=(t,t^2) in the invariant locus y^2=x^4 does exactly that under
(x,y)->(x,-y). Therefore it would be insufficient simply to call the
first-order result an all-orders obstruction.

Here the stronger conclusion is earned with actual analytic coordinates:

1. Theta is an automorphism of the PRESENTED GROUP: free reduction gives
   theta(r)=n^-1 r^-1 n, and theta squared is identity. Thus the operation
   preserves every representation, not just the original matrices.
2. The explicit chart Psi(u)_g=exp(u_g)rho0_g linearizes the combined
   operation exactly: F(Psi(u))=Psi(Tu). This is a matrix-exponential
   identity, not an inference from the four tested jet coefficients.
3. An invariant complement to the conjugation image gives a square
   30-dimensional gauge-coordinate map with nonzero determinant.
   The inverse function theorem produces ACTUAL local coordinates.
4. In that coordinate slice there are three odd ambient variables.
   Three selected relator equations have an invertible derivative in
   those variables, so they are determined uniquely by the even ones.
   Every complete solution and its involution solve those same selected
   equations with the SAME even variables and opposite odd variables.
   Uniqueness forces the odd variables to vanish.

The representation germ is NOT assumed smooth, and its tangent
directions are NOT assumed integrable. Remaining even equations can
still impose obstructions. The argument says every actual solution
that exists nearby is paired modulo conjugation.

The singular-curve countercontrol above is correctly rejected: its full
defining-equation tangent contains an odd direction, even though that
chosen curve's first derivative does not. A non-involutive map with
identity derivative and the trivial representation's noninjective gauge
map are also rejected by the hypotheses. These protect the scope of
the inference, not just the arithmetic implementation.

## 2. Exact coordinate certificates at all four points

| Certificate | q=7+/-4sqrt(3) | q=17+/-12sqrt(2) |
|---|---:|---:|
| Ambient even / odd dimensions | 18 / 12 | 18 / 12 |
| Gauge even / odd dimensions | 6 / 9 | 6 / 9 |
| Transverse slice even / odd dimensions | 12 / 3 | 12 / 3 |
| Full gauge-coordinate matrix rank | 30 | 30 |
| Odd relator derivative rank | 3 | 3 |
| Slice tangent dimension, all even | 3 | 3 |

Both embeddings are computed separately. Explicit nonzero determinants,
the 30x12 and 30x3 complement matrices, and the selected residual minor
are retained in [EXACT_WITNESSES.jsonl](EXACT_WITNESSES.jsonl). The same
zero-based residual rows (0,1,6) work in every case. Actual inverse
residuals are checked, not merely a floating rank threshold.

These matrix entries and determinants are basis-dependent certificates,
not physical constants. The invariant content is invertibility and
the resulting local pairing theorem.

## 3. The pairing varies; a fixed matrix would be wrong

For a nearby representation A, the analytic coordinates give

    A=g^-1 S g,      S_g^T J=J S_g,
    J_A=g^T J g.

Then J_A is symmetric, invertible and analytic on the representation
locus, with constant determinant det J. Its equations are

    A_g^T J_A=J_A A_g              on the two generators,
    A(w)^-T J_A=J_A A(theta(w))    on every word.

The second line is the representation-level pairing. Replacing it by
transpose alone on every product is false: transpose reverses the word.
This distinction was already explicit in the historical B789 Sym2
intertwiner work, which was read before this cell. F16 extends the
present local SL4 argument, not that historical claim's name or scope.

A nontrivially conjugated, q-changing family is checked symbolically
over a rational-function field. Its variable intertwiner works; the
fixed old J fails, and the transpose-only product assertion fails.
That family is a control, not a newly constructed off-q physical vacuum.
Fixed fourth-root central twists preserve the full pairing because
theta and dualization invert the same scalar character.

## 4. What this does and does not say about physics

**Small flat-holonomy deformations alone cannot remove the algebraic
geometric pairing near these backgrounds.** Checking more Taylor orders
for an unpaired representation in this neighborhood is unnecessary.
The argument does not quantify how large a deformation must be to leave it.

However, J_A is NOT a positive harmonic metric. F14's unitary operator
and interaction pairing additionally used end-norm compatibility and
F13's uniqueness in the same bounded-distance class. Those hypotheses
have not been proved for arbitrary nearby representations. If a new
background satisfies them, its physical unitary pairing follows as
before; otherwise the changed end/source data must be analyzed on their
own merits. F16 is not a blanket equality-of-couplings theorem on U.

F15's two-complex-dimensional matter-retention tangent kernel remains
registered: it may contain integrable paired families, but neither
nonlinear existence nor admissible normalizable modes are supplied here.
F11's equal-count result is not being rebranded as today's contribution.

The strategic consequence is to test a changed HYPOTHESIS rather than
keep adjusting the same local flat representation. The next focused
candidate is additional cover/character data on pulled-back backgrounds:
does any actual geometric duality lift and preserve those data? This
must be checked before computing coupling profiles, and any candidate
still owes a retained spectrum, parent action and asymmetric phase.
First consult the existing and newer seat results before sealing that
cover/character probe; this cell has not certified their absence.
F11's count constraints already apply to its finite-cover pullbacks;
a repeated count census would not answer the interaction question.
Other admissible end/source data and spontaneous symmetry breaking are
separate routes, not excluded or established by this calculation.

The earlier constructive backgrounds and paired modes are not retracted.
Object-selected inputs, an interacting chiral quantum theory, observed
phenomenology and gravity remain beyond what this cell establishes.
No completed TOE or guarantee that the framework describes nature.

The complete argument is in [PROOF.md](PROOF.md); hypotheses, prior-art
scope and preregistration in [DESIGN.md](DESIGN.md); execution custody
in [RECHECKS.md](RECHECKS.md). No shared B allocation, main edit, push,
PR, new all-head absence claim or external publication.

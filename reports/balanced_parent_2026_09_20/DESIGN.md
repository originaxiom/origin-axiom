# F08 pre-execution design: a different global coefficient, not a patched core

2026-09-20, local fork at 054bebb3. The previous turn was progress: F07
changed the next-action rule for regular fixed-holonomy core replacement.
This probe tests a genuinely different global rank-four coefficient and
asks what becomes of F06's local algebraic kernel in it.

## Scope and priced inputs

For any oriented complete finite-volume hyperbolic three-manifold with
geometric PSL2(C) holonomy h, use the real-Lie-group representation

    rho(g)=g tensor conjugate(g).

It has complex dimension four, det=1, and factors through PSL2(C).
It is NOT the holomorphic Sym3 representation of F05. Use R39's same
SU4-in-E8 parent embedding and the same partially twisted classical SYM
action. E8, its embedding, supplied four-dimensional spacetime, the
hyperbolic metric and this representation choice remain inputs. No
physical gravity, selected vacuum or arithmetic uniqueness is inferred.

Construct C from the fundamental hyperbolic q^-1 dq by the tensor rule.
Expected: full flatness and moment equation, finite defining-four Higgs
norm 6 Vol(M), compact gauge algebra so(10) WITHOUT an extra Wilson twist.
The positive Hermitian metric is not the invariant indefinite Lorentz
bilinear form. Global descent must use actual unitary transitions.

In an explicit unitary basis the Hermitian coefficients should be the
three boosts N_i+N_i^T. Their degree-one algebraic operator should be
four times F06's corrected center operator: eigenvalues 0(5),2(3),3(4).
Unlike F06, the Higgs is parallel with its unitary and Levi-Civita
connections, so the full Laplacian splits into Delta_A plus that algebraic
term. The zero sector should be exactly complex L2 trace-free Codazzi
tensors, not five physical particles or a guaranteed nonzero global kernel.

The symmetric unitary bilinear J=diag(-1,1,1,1) should give a same-degree
duality of the untwisted physical operators. With an order-four scalar
unitary character the linear bilinear no longer descends, but J followed
by coefficient conjugation should still intertwine the dual sector.
Expected chirality verdict: paired spectrum in this class, even though
F05's strict local matter bound no longer applies. Do not replace
paired-with-unknown-dimension by zero, or failed positivity by existence.

## Cusp and failable controls

In the standard cusp frame e_i=z partial_i, a zero-Fourier symmetric
trace-free Codazzi tensor should have

    b11=(c z^3+d z)/2, b22=(c z^3-d z)/2,
    b33=-c z^3, b12=b21=e z, b13=b23=0.

All nonzero such modes fail L2 at z=infinity: squared-norm density is
(3/2)|c|^2 z^3+(|d|^2/2+2|e|^2)/z. Derive the equations before claiming
this is the whole zero-Fourier sector. Higher Fourier modes and their
global matching are NOT settled by this control. For a nontrivial cusp
character the zero Fourier sector may be absent to start with.

Check full noncommuting equations, actual coframe connection, compact gauge
commutants in 4/6/15, global real/bilinear identities on exact m004 generators,
the changed-holonomy witness, the corrected tensor quadratic form, and
the domain-preserving pairing. Scale only Psi by t: flatness must fail
except t=+/-1, even while the moment equation remains zero. A general SL4
diagonal generator must break the particular J pairing; it is not proposed
as a BPS solution. A pointwise zero with a wrong derivative jet must fail
Codazzi. All scalar/matrix equalities use exact expanded residuals.

## Retrieval, credit and source boundaries

already_banked queries: `balanced representation harmonic metric`,
`holonomy conjugate tensor`, `Codazzi Lorentz cohomology`. Broad incidental
hits were navigation, not absence certificates. B356's factor-route
reality statement was read; it is a finite-group antecedent, not this
physical background. R27's proof, R39's full proof at available local pin
8d2cced2, F05's producer and F06's corrected findings are inputs. A wide
Git grep returned an unusably large output, followed by scoped filename
searches. No refreshed remote-head or corpus-wide absence claim.

Primary HTML personally checked: Braun et al. arXiv:1812.06072v2 equations
2.9--2.24 and 2.34--2.42; these retain the noncommuting parent equations.
Menal-Ferrer--Porti arXiv:1001.2242v2 explicitly restrict their irreducible
coefficients to holomorphic symmetric powers: do not apply that vanishing
to g tensor conjugate(g). Bera arXiv:2408.01522v2 sections 1--4, including
Proposition 4.3 and Lemma 4.6, identifies the Codazzi problem in another
gauge theory on CLOSED bases. That is a literature connection, not an
identification of the actions or a cusped-kernel theorem. Its closed-space
census is not repeated or adopted here. No PDF or subagent summary used.

Seal this design, proof, producer and tests before their first execution.
Preserve any failure. F05's wedge/connection utilities and F06's unchanged
producer are reused explicitly, not relabeled independent implementations.
This remains local research, with no shared B number or external publication.

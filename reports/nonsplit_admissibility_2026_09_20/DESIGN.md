# Fork F01: finite-energy harmonic admissibility of nonsplit witnesses

2026-09-20. Branch audit/fork-2026-09-20. New fork-local work, not R39,
not a shared B allocation, and not a resumption of the inherited experiment.
The full physical-theory objective remains unachieved.

## Quantifier, inputs and honest prior

The analytic question concerns **smooth complex flat bundles on connected,
complete finite-volume Riemannian manifolds without boundary**, with a smooth
positive Hermitian metric whose self-adjoint connection part has finite L2
norm and satisfies the source-free harmonic-metric equation. No assertion
about all backgrounds, all cusped metrics, all parent actions, or all TOE routes.

Application: R27's marked m010 representation and V=Sym^3(rho) tensor chi,
whose relative-image index +1 was independently recovered during the preceding
whole-picture audit using main at 987c0c8fdb07f7f79beccd6c82c1154e3e75fa47.
That index is not identified with a physical chiral spectrum here.

Prior, disclosed **before execution**: the finite-energy source-free harmonic
class should exclude a globally nonsplit flat bundle, by a cutoff version of
the invariant-subbundle variation. A finite-energy **local cusp** should still
exist for the specified peripheral translations. The authored proof records
these expected outcomes in advance; this is not a blind discovery protocol.

## Prior-work checks and primary source

- Fresh fetch of all origin heads/tags succeeded; main pin unchanged. No merge.
- WORKING_RULES, COMPUTE_THE_PROGRAM and THE_CAMPAIGN reread; framework and ladder
  personally read in the immediately preceding audit at this unchanged local HEAD.
- already_banked.py terms: nonsplit, harmonic, metric, Corlette, polystability.
  Its 106 hits and zero settled rows matching three terms are navigation only.
- Atlas chirality card, LAW_MAP, OPEN_LEADS, kill graph, R27 FINITE_TWIST.md and
  R35 LITERATURE_AND_SEATS_2026_09_19.md checked. R27 already proves nonsplitting
  and explicitly leaves harmonic admissibility unpaid; those algebraic results
  are controls, not new discoveries.
- Remote-tip searches over frontier/reports/papers used Busemann,
  finite.energy harmonic, polystab, harmonic metric. The prior audit's history
  receipt searched 30,818 text versions. Neither licenses a semantic absence
  claim. No claim of novelty in the literature or whole repository is made.
- Corlette, *Flat G-bundles with canonical metrics*, JDG 28 (1988), 361-382:
  indexed primary PDF introduction and sections 2-3 inspected, especially
  Proposition 3.2, Theorem 3.3 and Corollary 3.5. Their domain is compact.
  Do not transfer that hypothesis silently to m010. The proof below supplies
  the additional cutoff step. A local download returned HTTP 403; no successful
  local full-paper reading or image inspection is claimed.
  DOI: https://doi.org/10.4310/jdg/1214442469

This is a hole in the physical interpretation of an existing positive, so it
is prioritized under the campaign's HOLE-before-new-frontier rule. No empirical
predicate, fitted value or observed-SM target enters this mathematical probe.

## Conventions

- rho(a)=[[0,1],[-1,1]], rho(b)=[[0,u^2],[u,-2]], u=(1+i sqrt(3))/2.
- pi=<a,b | aabaBaaBab>, mu=AbAA, lambda=babA; capitals are inverses,
  words multiply left to right. Exact complex algebra, no floating rank.
- Flat D=A+Psi, A metric-compatible, Psi self-adjoint; norms use the
  positive Hermitian Hilbert-Schmidt pairing, summed over orthonormal covectors.
- Harmonic metric: d_A^* Psi=0. Finite energy means integral |Psi|^2 < infinity.
  The map energy in H3 is separately normalized as E=1/2 integral |df|^2.
- Hyperbolic cusp metric dr^2+exp(-2r)h0, r>=0, h0 a constant positive flat
  torus metric. H3 target coordinates (X,Y,v), metric dv^2+exp(-2v)(dX^2+dY^2).
- Busemann b=-v. Laplacian is div grad. Boundary normals point out of the
  truncated domain; the inner boundary of an isolated cusp points toward -r.

## Discriminators and controls

1. Exact representation, flag, peripheral matrices, length-four Jordan chain,
   and obstruction to a commuting projection onto the invariant line.
   A diagonal split control must admit the projection.
2. Derive the sign and factor in the projector first variation. Test both a
   nonzero extension block and zero block; changing the flag generator's sign
   must reverse the contraction, not disappear behind an absolute value.
3. Check Hess(-log height)=g-db tensor db directly; a target dilation must
   violate literal invariance of b, guarding the scope of the scalar argument.
4. Derive the full harmonic-map tension of the local cusp map, not only its
   radial equation. Correct height normalization must give zero; an incorrect
   normalization must not. Verify the finite integral and both boundary fluxes.
5. Check the exponential energy-bound integration and sign algebra. The
   analytic all-domain conclusion rests on the written cutoff proof, not on
   finite symbolic samples.

STOP if the cutoff estimate requires an undeclared bound, if a source/domain
term has been discarded, if positive definiteness is lost, or if any control
cannot distinguish its intended alternative. Preserve failures verbatim.

No resulting negative may be reported as 'chirality impossible'. No local
cusp solution may be reported as a global vacuum. Larger coupled parents,
defect sources, physical boundaries, other energy functionals, singular
metrics and infinite/renormalized-energy completions retain separate duties.

## Custody

Seal DESIGN.md, PROOF.md, verify.py and test_verify.py before execution.
Record all outcomes, including failures, in this directory. This is a research
checkpoint, not full main-bank certification; no global bank counters are used.

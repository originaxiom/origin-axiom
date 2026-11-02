# Complete-kernel controls: exact source candidate, still unrun

November 2, 2026. **UNREVIEWED, UNRUN, NOT IMPORTED OR COLLECTED.**

Design and proposed environment were committed at f5f1042d6 before
checks.py was created. Static AST inspection matches exactly the six
named methods of ElectroweakKernelChecks to that design; there are no
inherited methods. AST parsing does not discover tests at runtime or
prove their scientific assertions. No SymPy or scientific module was
imported while performing the author's metadata checks.

The implementation reconstructs the old explicit D5 matrices directly
instead of importing the earlier unreviewed module. This duplicates
some source arithmetic, transparently. It does not constitute a second
independent proof of the actual D5/E8/global-bundle identification.

Substantive finite coverage is intended as follows:

- Every standard E8 root and Cartan is assigned to D5, A3, cross-vector
  or one of the two half-spinor populations. Both actual16-dimensional
  half-spinors are constructed from a32-dimensional Clifford/Fock
  module; its adjoints, parity and a spanning set of Lie brackets are
  checked before its joint weight character is used. Its Cartan weights
  and parity are also bound to the literal last-five E8 half-root
  coordinates, not identified only by the shared dimension16.
- The half-spinor spectral checks include annihilating polynomials,
  idempotence and orthogonality, not merely the interpolation identity
  that the projector polynomials sum to one. That latter identity
  alone could hold for an incorrect grading matrix.
- The finite graded Koszul cohomology and all-degree generator change
  are reconstructed. The endpoint b=0 loses the inverse and has the
  different diagonal-triple cohomology; it is not a new continuous
  extension of the interior count.
- Actual root flat phases, all four spin choices and the cusp equality
  endpoints feed the new complete counts. The old symmetric count is
  separately reconstructed from the full roots' diagonal weight strings.
- Gaugino/C3 omission, a missing triple companion, a doubled conjugate
  module, wrong endpoint and wrong order-seven alias are rejecting
  controls. They do not prove the physical operator map by themselves.

Several checks compare arithmetic implementations with formulas from
the same author derivation; source agreement is not independent acceptance.
A future pass would support these finite algebra/population statements,
not a general physical field assignment or an observed SM spectrum.

SOURCE_REVIEW_INVENTORY.json pins the candidate and its declared analytic
inputs. It is **not a complete prospective execution specification**.
The actual runtime has not been revalidated for this package, and no
wrapper or output namespace is admitted. Source/environment/input/test
closure, wrapper engineering verification, genuine independent proof/code
review, main's separate exact acceptance and strict prospective admission
on a clean quiescent checkout remain required before scientific import.

Analytical review must prioritize the global compact two-triple map and
root phases, the whole physical bundle and its total S powers, bounded
contraction in the correct weighted graph domains, closed-range transfer,
and the original general-Q,R mass isometry with its C3/gaugino. Finite
Fock matrices or line dimensions cannot certify those global hypotheses.

The surviving four massless colour-up conjugate pairs are a proposed
exact result about this fixed classical interior branch, not a kill of
quantum completions or the generated architecture. The parameter a,b
is not erased from massive spectra or measuring data by a change used
to count cohomology. No foundational input is marked paid.

This is sender-branch review sharing under the owner's existing permission.
It is not banking, execution permission, a receiving-seat disposition or
an extension of P210, radial, sixteen-control or eight-control acceptance.
All earlier seals, failures and inherited staging stay preserved.

# Checks for complete flag complex transport

October 13, 2026. P0: this is a conditional calculation over the fixed nonsplit flat coefficient, its two charged tensor slots, all form degrees and every positive amplitude in the declared complete cusp class. It is not a whole-framework chirality verdict or a census of manifolds.

Prior: the bounded-norm Hilbert-complex lemma is already in F11/F12 and the weighted-source proof. This work applies that existing lemma to the new global admission and adds an explicit radial chain transport between positive amplitudes. Expected result: the two comparisons hold; wavefunctions and spectra do not stay identical. No expectation of a new generation count is attached to these checks.

## Sources and conventions

All origin heads were refreshed; no head changed after the Gate11 review. Source pins are main 6c148ddd495d133213140995976ff08849793d5d, the physical branch 25a6d036d767b5af36e4d4a7071f7520e3b45405 and this branch's admission/review at 5ddfd258b20dc270fa08fea4a831b97ba42c3521. The selected prior-work search is in PRESEAL_NOTES.md; no all-history absence or novelty claim is made.

Read the complete F11/F12 and complete-domain proofs, and the relevant weighted-cohomology and physical operator proofs. Arnold--Falk--Winther section3.1.3 was checked in the primary HTML on October13: https://arxiv.org/html/0906.4325v3#S3.SS1.SSS3 . It is a mathematical source, not an empirical premise or a complete-manifold theorem applied without the authored domain argument.

The rank-five reference uses Gate3's Pauli order (I,sigma1,sigma2,sigma3) and its literal fifth coefficient. r increases toward the cusp, ell>0, b>0, D=d+C and frame changes act by S^-1 C S+S^-1 dS. Fibre norms are positive Hermitian; induced exterior metrics are determinant Gram metrics. Base g=dr squared+exp(-2r/ell)h_T. No finite-cut projection or boundary condition is installed. The reference connection, not its adjoint, is fixed across norm comparisons.

## Two-sided exact controls

Reconstruct the radial and tangential matrices from the two-by-two spin lift, rather than reading their claimed eigenvalues. Verify commutation with Xi, all three flatness relations, the orthonormal simultaneous diagonalization, the literal defining and exterior-square weights, and the temporal-frame removal of radial connection. Check the full nonabelian tangential relation, not merely the diagonal wall.

Verify the translated logarithmic metric identity symbolically in every defining and exterior-square weight, its inverse/composition rule and every torus-degree base density. Opposing controls must detect an omitted constant flag factor, a wrong radial exponent and use of identity instead of radial pullback. The zero-amplitude and opposite-sign limits are excluded, not declared to share the positive family's cohomology.

Use a nontrivial exact finite Hilbert complex to verify the adjoint formula, changed harmonic representative and unchanged cohomology dimension. Its positive spectral trace must change. Replacing the differential by a different nilpotent complex must change cohomology, detecting misuse of norm comparison across different D. This comparator checks the algebraic distinctions; it is not a discretization of the manifold.

Check induced exterior metrics on a positive non-diagonal matrix, so the tensor-bound argument is not tested only on diagonal inputs. All predicates must pass; missing or duplicate names, exceptions and missing output fail. The control tests must reject deliberate sign, adjoint and differential mistakes.

## Execution and scope

Use the established Python3.12/SymPy1.14 environment. Seal this design, PROOF.md, verify.py, test_verify.py and execute.py, record the hashes, commit and push before scientific execution. AST parsing without import is allowed before the seal. The execution wrapper preserves raw stdout, stderr, exit codes and hashes in a fresh output directory; an existing directory is rejected. First failures are never overwritten. Any scientific repair requires a new seal before rerun.

Finite checks support explicit algebra and opposing controls. They do not certify the analytic proof, finite-dimensionality, global mode counts, physical identifications or a full theory. No canonical GENESIS edit, main adoption or new shared bank number follows automatically. Preserve unrelated dirty files. Full-suite certification remains distinct from these focused tests and the branch publication gates.

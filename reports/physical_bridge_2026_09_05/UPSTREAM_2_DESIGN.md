# Second upstream audit: retain identities, verify the classifiers and scope

BANKED IDENTITY: upstream 8f83b5c8 adds B1254 (square-class dynamics from
B497/B1248) and B1255 (cubic types, a generation-grading commutator and the
single-27 dimension bound). Merged as e3b51950, with both local and upstream
log entries retained. R7 remains banked separately at 569613d7.

PRIOR ART: read both new FINDINGS/code/test bodies, B497's FINDINGS and
trace-map producer, B1250's grading code, and B923's cache producer. Read
all of B854's 313-line producer before isolated execution. B1255's CI tests
explicitly do not cover the object-matrix tier when its cache is missing.
The physical bridge already rebuilt the 27/cubic and D2 action; do not
misreport arithmetic-only PASS as a new matrix verification.

P0: verify these specified upstream mechanisms and their instruments, not
every route to dynamics, generations or a physical TOE. No empirical inputs.

Before execution, seal these tests:

1. Recompute the three named trace substitutions and exact kappa multipliers.
   Compare B1254's square predicate with independent polynomial factorization
   on a genuine square, odd-degree nonsquare, and even-degree nonsquare x^2+1.
   A passing headline selftest does not excuse a failed classifier control.
2. At explicit SL2(Q) matrices with tr A=0, check whether decimation reaches
   kappa=2 from kappa!=2; a square-class preservation statement must price
   nonzero factors. Preserve the genuine generic decimation identity.
3. Test the determinant-one endomorphism a->aba^-1b^-1a, b->b on explicit
   SL2(Q) matrices. Its abelianization is the identity. A changed commutator
   trace rules out calling it an automorphism. Noncommuting images generate
   a rank-two free subgroup, giving injectivity by the same Hopfian argument
   B497 uses. This tests the classification, not the named metallic map.
4. Rebuild B854's four invariants in a fresh temporary directory, preserving
   its stdout, results and rational coefficients in the audit output. Never
   run its writing producer in the banked directory or load a foreign pickle.
   Form B1255's Mc on the original 27, compare its D2 to B916, recover W18,
   its 12/6 split and the exact commutator. Test absence of a D2-homogeneous
   C eigenvector by the kernel of stacked (D-sign I) C^k, not an eigenvector
   sampling argument. A zero stacked kernel over Q remains zero after scalar
   extension. Keep the genuine single-27 dimension bound separate from any
   claim that one named multiplicity mechanism exhausts physical possibilities.
5. Run the unchanged five upstream tests, the current 69 physical-bridge
   tests and two new classifier controls quiescent; retain the two documented
   R7 small-step failures rather than erase them. Output exclusive-create,
   failures preserved. The new controls include rational square coefficients,
   zero, negative coefficients and positive nonsquare coefficients.

Prior: named trace identities and matrix commutator should reproduce, while
the square classifier and stratum wording appear under-controlled. The
single-27 bound is sound on its stated carrier; it does not derive the
physical family count or force a particular source of multiplicity.

# R33 separately sealed normal-form comparison control

2026-09-19. Original seal c75647aa5a02401b635f340f0db9d37d7f8ee5a0.
Native algebra passes all nine groups. The first new-test run has
18 pass / 2 fail, and the fixed five-file focused run 104 pass /
the SAME 2 fail. Both are instances of
test_real_rotated_and_collinear_complex_vectors_are_full_rank.
Original source, tests, design and raw outputs remain unchanged.

The assertion compares an expanded mass-square matrix with an
unexpanded scalar norm under SymPy structural equality. The proposed
diagnosis is an expression-normalization defect, NOT a counterexample
to the mass identity. It remains a hypothesis until this control runs.

P0: both chiral blocks for the exact vector (1+i,2+2i,0,...,0), and
the symbolic family (a+i b)(3/5,4/5,0,...,0) with real a,b. P1--P4:
the same R33 prior and physical scopes; no new literature or absence
claim. P5: commit, push and remote-confirm these three new files before
execution. P6: expect residual zero and full rank in the original
example, but nonzero residual for a genuinely altered mass matrix.

Compute the original raw norm and its expansion. Compute the full
matrix residual BEFORE comparing with zero; assert rank 16 and
squared norm 10. A changed mass entry must fail the identity. Test
the symbolic two-parameter collinear family. The noncollinear null
vector e1+i e2 must still fail the constant-gap identity and have
rank eight. Thus simplification is not a way to make everything pass.

Run the new native control, its six tests, then an expanded focused
run: the original fixed five-file population followed by the new
test file. The two original structural-comparison failures are
expected to remain in the expanded run and are not deselected,
xfail-marked, overwritten or folded into green. No new physics is
earned by the diagnosis; its job is to distinguish a test defect
from a mathematical negative before reporting either.

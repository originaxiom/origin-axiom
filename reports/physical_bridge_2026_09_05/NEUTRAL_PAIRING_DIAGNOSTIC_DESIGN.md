# R47 separately sealed pairing-comparator diagnostic

September 25, 2026. This is a post-failure design, sealed BEFORE its own
execution. Original scientific seal: 8f493e683e3269ffecf125c357e8bed2287b3683.
No original producer, test, proof, input or first-run output is changed.

The original native run passed its 13 controls. Dedicated tests returned
10 passed / 1 failed; the fixed four-file regression returned 62 passed /
1 failed. Both fail at the same inverse/dual matrix equality for the
fourth-root twist. The displayed residue contains `0*I`. Prior: structural
SymPy equality, not the mathematical identity, is at fault. This remains
a hypothesis until the new exact-arithmetic computation succeeds.

Quantifier: just the two literal projective SL4 generators, symbolic
positive q, each of the four fixed central phases 1,-1,i,-i. No new
intertwiner census, canonical-metric symmetry theorem or chirality test.

Recompute all eight inverse/dual residues from the original matrices,
not from the printed failure or stored verdict. Expand each entry, put
it over a common denominator and test its numerator as a polynomial
over the exact Gaussian rational field QQ(i). Require a nonzero
denominator. Report both exact zero and the original structural
comparison for each case. A surviving polynomial numerator falsifies
the comparator-only diagnosis; do not replace it by a numerical tolerance.

Two-sided controls: an explicitly unevaluated `0*I` must reduce to zero,
whereas i/q and a nonzero rational expression must not; S+I must fail an
intertwining identity; using phase instead of inverse phase on the dual
side must fail for i and -i. Also recheck both differentiated identities
and the omitted-compensator mutant with this exact predicate. These
controls test the replacement predicate, not only the intended positive.

For scalar z, (z A)^(-T)=z^(-1) A^(-T). Thus the untwisted identity
implies the twisted one algebraically. The diagnostic independently
recomputes the twisted matrix inverses and checks this consequence.
It does not change the original all-q proof or its analytic assumptions.

Seal this design, diagnostic producer and four dedicated tests, push
and confirm the server hash before running either. Capture native and
pytest exits separately; hold the tree read-only during both. The old
failed tests remain failed records, not retroactively green. No full
suite, independent peer review or physical certificate is implied.

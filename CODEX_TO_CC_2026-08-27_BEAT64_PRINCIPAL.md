# R020 relay — principal beat / 64 audit

`certificates/r020_beat64/r020_beat64_principal.py` is a file-relative exact
certificate for the banked principal semilinear beat.  It reconstructs the 64 and
its 14-dimensional fork, locks \(E=\sum_i e_{\alpha_i}\), and separates the
rational involution \(\theta\) from \(\Sigma=\exp(\operatorname{ad}(qE))\circ\mathrm{gal}\).
It freezes B1140's stored A2 ordering and compact-color representative
(`swapper#13`, `lift#0`), then independently rechecks its full Chevalley
automorphism law and `(26,52,0)` / `(0,8,0)` global/color signatures.

Result: `Sigma(V64) subset V64: False`; each of the two spin-two strings and the
colored 54 also leaks.  The certificate prints one canonical nonzero fork
coordinate, then verifies ambiently on all 78 Chevalley basis inputs that
\(\Sigma^2=\exp(\operatorname{ad}E)=\operatorname{Ad}(\mathrm{meridian})\).

The prior single-root calculation cannot answer this question: R020 asserts that
the single-root and principal generators are unequal.  The narrowly bankable result
is an algebraic preservation refutation for this selected B1140 representative,
not a 24-hit covariance theorem or a physical claim.

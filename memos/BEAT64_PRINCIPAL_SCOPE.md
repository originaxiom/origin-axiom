# R020 — Principal beat does not preserve the banked 64

R020 tests the banked semilinear operator, not the rational slot involution.  Over
\(\mathbb Q(q)\), \(q^2-q+1=0\), it is

\[
\Sigma=\exp(\operatorname{ad}(qE_{\rm prin}))\circ\mathrm{gal},\qquad
E_{\rm prin}=\sum_{i=1}^6e_{\alpha_i},\qquad \mathrm{gal}(q)=1-q.
\]

The exact 64 is reconstructed as two five-dimensional principal strings and 54
colored root directions; its complementary fork has dimension 14.  A complete
exact basis calculation finds \(\Sigma(V_{64})\not\subseteq V_{64}\), and the
same is true separately for both spin-two strings and the colored sector.  Hence
there is no induced action on these summands and no restricted tick endomorphism.

The ambient identity remains exact on all 78 Chevalley basis vectors:
\(\Sigma^2=\exp(\operatorname{ad}E_{\rm prin})=\operatorname{Ad}(\mathrm{meridian})\).
It is not an identity, and it also fails to preserve this 64.

## Source and frame locks

- B1138 fork construction: `d8245b386e9e54c3db0eaf3a8506fc9438492b30`.
- B1140 64 decomposition: `ca7fbfdda01f4f150372d79badf426b1731d4ac5`.
- Outside-bench source frame: `session_handoff/certificates/{simul_verify,spacetime64}.py`
  at Golden hostile-review commit `6fc86147e553773335b665d6d460e1eaa77aaaf0`.
- Vendored E6 arithmetic used here: R006 commit
  `1cc8176ee1733ebcf2704634a679d36b762fd595`.

The executable freezes B1140's component order and its first compact-color hit
(`swapper#13`, `lift#0`). It rechecks the lift on every Chevalley-basis bracket,
reproduces global signature `(26,52,0)` and compact-color signature `(0,8,0)`,
and verifies that the explicit 64 is orthogonal to the 14 under the invariant
form. These guards are load-bearing: an arbitrary swapper or the reversed
orthogonal-A2 ordering is not the banked spacetime frame.

## Hostile convention lock

The rational linear \(\theta\) used to define the selected slot frame is not
\(\Sigma\).  A prior fork-only calculation instead used a single root vector
`ROOTS[0]`; R020 asserts mechanically that it has one nonzero Chevalley component,
whereas the banked principal generator has six.  This is a different nilpotent
operator, not a semilinearity, frame, or conjugation convention.

Scope is one specified B1140 compact-color representative and its 64-dimensional
algebraic complement. Frame-covariance across all 24 B1140 hits is not proved.
No physical spin, locality, or QFT consequence is asserted.

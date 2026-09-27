# R52 supplemental square-root control, sealed after the first failure

September 27, 2026. Post-result DIAGNOSTIC design; pre-execution for this
new code. Original seal e7006dab5fdaf2c45c3604989d05856b412e0af5 and all
its science remain unchanged. First native: 33/35; dedicated 11 pass,
2 fail; ten-file regression 121 pass, 4 fail (two earlier comparator
failures plus these two). Original raw outputs are retained in full.

The new failure is a real fixture defect, not a SymPy comparison issue:
S=[[2,1],[1,1]] and X=[[1,2],[2,-1]] satisfy X=2S-3I. Thus the purported
noncommuting control COMMUTES and cannot reject a commuting shortcut.
Its first/second Sylvester identities passed, but did not cover the
declared noncommuting case. This does not refute the analytic Sylvester
equations in the R52 proof; it leaves their discriminating control unpaid.

Keep the original and explicitly verify that defect. Supplement it with
X=diag(1,-1), the same S, and Y=[[0,3],[3,2]]. Direct differentiation
of (S+tX+t^2Y/2)^2 must give the Sylvester first/second derivatives;
the naive commuting derivative and omitted second-order product must
fail. Also solve for a fully symbolic symmetric X, and check a positive
Sylvester spectrum on an orthogonally rotated positive matrix.

Freeze this design, the separate producer and separate tests, then
commit/push/server-confirm before execution. Run new native/dedicated
and the unchanged ten-file regression plus this diagnostic. The original
failures must remain visible; do not replace or monkeypatch old results.
No revision to the analytic proof is made, and these finite controls
do not certify it. If a new failure occurs, retain it and narrow scope.

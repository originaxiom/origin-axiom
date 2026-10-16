# Exact trace equality rather than expression identity

First native run at published4dc66f8c8 returned35/37 in150.496266s;
reference was NOT attempted. Complete stdout/stderr and140source
snapshots remain in results/first_run, with original manifest/seal
also preserved. The tree/pins/index were unchanged. This is a FAILED
first instrument run, not a passed geometry certificate.

The two combined failed gates include s.trace(PH)==2 and s.trace(Q)==8.
Unlike the neighboring matrix residual tests, Python equality here
compares the unsimplified symbolic expressions. The structural
mathematical trace identities have independent algebraic proofs:

 tr(PH)=4-(norm(N)^2+norm(JN)^2)/norm(N)^2=2;
 Q=(I+K)/2, K=i R_s v(N)v(JN)/norm(N)^2.

The real six-Clifford relations give K^2=I and conjugation by v4
sends K to-K. Hence tr(K)=0 and tr(Q)=8. This does not yet diagnose
which subexpression failed in the original combined gates.

The successor splits Hermitian/idempotent/trace/complex-compatibility
checks so EACH is executed and recorded. Trace equality is tested
by exact rational cancellation of trace minus target, not numerical
closeness or a changed rank. Raw trace strings and original structural
booleans are recorded, alongside exact residuals. Wrong-trace targets
must remain nonzero. If any Hermitian/projector/geometric relation
actually fails, the successor still fails. No field/sign/factor or
scientific criterion changes; no original result is overwritten.

This repair is post-hoc to the failed instrument run and is sealed,
committed, pushed and server-confirmed before importing/executing
the successor. Same author/conventions remain, not independent
analytic acceptance. The original fixed vertical normal control,
full moving-plane terms and compact-versus-complex controls remain.

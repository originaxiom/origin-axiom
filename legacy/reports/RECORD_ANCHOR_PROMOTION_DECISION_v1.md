# Record Anchor Promotion Decision v1

## Decision

Promote the \(L/R\) record work from:

```text
pure mathematical curiosity
```

to:

```text
candidate classical/statistical transfer anchor
```

## Reason

Two exact transfer-matrix anchors were found:

1. \(L+R=\begin{pmatrix}2&1\\1&2\end{pmatrix}\) equals a normalized 1D zero-field Ising transfer matrix at \(K=\frac12\log2\).

2. \(A=LR=\begin{pmatrix}2&1\\1&1\end{pmatrix}\) equals a Zimm-Bragg helix-coil transfer matrix at \(s=2,\sigma=1/2\).

## Allowed claim

> The \(L/R\) record system has exact realizations in known classical transfer-matrix physics.

## Disallowed claims

Do not claim:

- spacetime is derived;
- gravity is derived;
- cosmology is derived;
- matter is derived;
- Ising or Zimm-Bragg systems are fundamental reality;
- Fibonacci anyon experiments validate the model.

## Recommended repo path

```text
stage2/record_anchor_analysis/docs/EMPIRICAL_ANCHOR_NOTE_v1.md
```

## Next gate

Build and run:

```text
scripts/run_stochastic_record_simulator.py
```

with exact target checks:

\[
\beta_c^{count}=\log2,
\qquad
\beta_c^{trace/lambda}=\log3,
\qquad
h_A=\log(\varphi^2).
\]

# Origin Axiom — Gate G4B F-symbol / Associativity Audit

## Purpose

Gate G4 showed that the persistent record sector has an exact Fibonacci fusion-count dictionary:

```text
RL = N_tau^2
A=LR = P N_tau^2 P
A^n = P N_tau^(2n) P
```

Gate G4B asks the stricter question:

> Is the record gluing operation actually the Fibonacci F-move / associator?

This is the critical test separating:

```text
fusion-count anchor
```

from:

```text
topological quantum / anyon amplitude anchor
```

## Executive verdict

G4B **does not promote** the model to a full Fibonacci anyon physics anchor.

The fusion-count bridge survives, but the F-symbol / associativity bridge is **not yet derived**.

The Fibonacci F matrix for the nontrivial channel tau,tau,tau -> tau is:

```text
F = [[phi^-1,     phi^-1/2],
     [phi^-1/2,  -phi^-1]]
```

Numerically:

```text
[[0.618034, 0.786151], [0.786151, -0.618034]]
```

This matrix is:

```text
orthogonal/unitary: yes
involutive: yes
eigenvalues: +1, -1
has a negative entry: yes
```

By contrast, record matrices L, R, and A are positive/integer count or shear matrices, not unitary associativity amplitude matrices.

## 1. Core matrix audit

| Object | Matrix | Trace | Determinant | Orthogonal | Involutive | Meaning |
|---|---|---:|---:|---|---|---|
| Fibonacci F matrix | [[0.618034, 0.786151], [0.786151, -0.618034]] | 0.000000 | -1.000000 | True | True | associativity/basis-change amplitude matrix |
| record L | [[1.0, 1.0], [0.0, 1.0]] | 2.000000 | 1.000000 | False | False | primitive record shear |
| record R | [[1.0, 0.0], [1.0, 1.0]] | 2.000000 | 1.000000 | False | False | primitive record shear |
| record A=LR | [[2.0, 1.0], [1.0, 1.0]] | 3.000000 | 1.000000 | False | False | positive hyperbolic count/transfer matrix |
| fusion count N_tau | [[0.0, 1.0], [1.0, 1.0]] | 1.000000 | -1.000000 | False | False | fusion-count matrix, not amplitude matrix |


## 2. Direct comparison result

The direct comparison fails.

```text
F is not L.
F is not R.
F is not A.
F is not N_tau.
```

This is not fixed by scalar normalization.

The generated file:

```text
G4B_direct_F_comparison_errors.csv
```

contains best-scalar Frobenius comparisons.

## 3. What remains valid

The G4 fusion-count layer remains valid:

```text
RL = N_tau^2
A=LR = P N_tau^2 P
A^n = P N_tau^(2n) P
```

So the record-to-Fibonacci bridge is real at the level of **fusion dimensions / path counts**.

## 4. What does not yet exist

A full Fibonacci anyon anchor requires more than fusion counts.

It requires:

```text
F-symbols: associativity amplitudes
R-symbols: braiding phases
Hilbert amplitudes
observable topological charge protocol
```

G4B shows that the F-symbol is not already contained in our record gluing as a direct matrix identity.

## 5. Interesting partial bridge: squared F amplitudes

The entrywise squared F matrix is:

```text
|F|^2 = {mat_str(F_prob)}
```

Its entries are:

```text
diagonal: phi^-2 = {1/phi**2:.12f}
off-diagonal: phi^-1 = {1/phi:.12f}
```

This is a doubly stochastic probability matrix.

So there may be a future **probability bridge**:

```text
record Gibbs probabilities
↔
|F|^2 transition probabilities
```

But this is not proven yet.

## 6. Gate verdict

| Criterion | Status | Evidence | Meaning |
|---|---|---|---|
| F equals L/R/A directly | fail | F is orthogonal/involutive with eigenvalues ±1; L/R/A are shears or hyperbolic count matrices. | record gluing is not literally the Fibonacci associator |
| F equals L/R/A after scalar normalization | fail | best scalar Frobenius comparisons show no exact matches. | not a normalization issue |
| fusion-count layer remains valid | pass | A=PN_tau^2P and RL=N_tau^2 from G4. | dimension-count bridge survives |
| probability/amplitude layer candidate | partial | |F|^2 is a phi-stochastic matrix with entries phi^-2 and phi^-1. | there may be a probabilistic bridge, but not an integer record-count bridge |
| topological quantum anchor promotion | not_promoted | F-symbol is not derived from record gluing; R-symbols/braiding also absent. | stay at fusion-count anchor until amplitude data are built |


## 7. Allowed claim after G4B

Allowed:

> The persistent record sector \(A=LR\) is exactly basis-conjugate to two-step Fibonacci fusion counting.

Also allowed:

> The Fibonacci F-symbol introduces a separate amplitude/associativity layer that has not yet been derived from record gluing.

Not allowed:

> Record gluing is the Fibonacci F-move.

Not yet.

## 8. Next gate

The best next gate is G4C:

```text
Probability bridge audit
```

Question:

> Can the entrywise squared F-symbol probabilities, phi^-2 and phi^-1, be derived from a normalized record/Gibbs transition rule?

If yes, we may have a bridge from integer record counts to fusion-basis probabilities.

If no, the Fibonacci connection remains safely limited to fusion-count dimensions.

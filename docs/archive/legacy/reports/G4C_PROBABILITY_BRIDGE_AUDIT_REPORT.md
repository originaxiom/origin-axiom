# Origin Axiom — Gate G4C Probability Bridge Audit

## Purpose

Gate G4B showed that record gluing is not the Fibonacci F-symbol itself.

But the entrywise squared Fibonacci F-symbol gives a probability matrix:

```text
|F|^2 = [[phi^-2, phi^-1],
         [phi^-1, phi^-2]]
```

Gate G4C asks:

> Can this probability matrix be derived from the record model by normalization, rather than imported from Fibonacci anyon theory?

## Executive verdict

G4C gives a **partial result, not a promotion**.

The standard record normalizations do **not** produce \(|F|^2\):

```text
row normalization: fail
column normalization: fail
Sinkhorn normalization: fail
Perron-Frobenius / Doob transform: fail
normalizing A, RL, L+R, or N_tau: fail
```

However, \(|F|^2\) is exactly produced by a simple symmetric Gibbs switch rule:

```text
stay weight   = 1
switch weight = phi
normalize by 1+phi = phi^2
```

This gives:

```text
P(stay)   = 1/phi^2
P(switch) = phi/phi^2 = 1/phi
```

So there is a **candidate probability bridge**, but it requires a new principle:

> switch/stay odds must equal \(arphi\).

That principle has not yet been derived from the record model.

## 1. Probability identities

| Quantity | Value | Meaning |
|---|---:|---|
| diagonal probability | 0.381966011250 | phi^-2 |
| off-diagonal probability | 0.618033988750 | phi^-1 |
| off/stay odds ratio | 1.618033988750 | phi |
| row sum | 1 | phi^-2 + phi^-1 = 1 |

The matrix is:

```text
[[0.381966, 0.618034], [0.618034, 0.381966]]
```

## 2. Failed existing normalizations

The best existing record-derived normalization was:

```text
anti_Ising_K_minus_half_log_phi
```

with relative error:

```text
0.000000
```

So \(|F|^2\) is not currently derived by known normalization operations.

Detailed comparisons are in:

```text
G4C_record_normalizations_vs_F_squared.csv
```

## 3. Successful but new Gibbs switch rule

Define:

```text
P = [[1,w],
     [w,1]] / (1+w)
```

Then \(P=|F|^2\) exactly when:

```text
w = phi
```

This is mathematically clean.

But the cost is conceptual:

```text
we must derive why switching is weighted by phi
```

Otherwise this is just another fitted golden-ratio rule.

## 4. Ising/probability interpretation

\(|F|^2\) is also equivalent to a symmetric anti-persistent Ising-like transition rule with:

```text
K = -0.5 log(phi) = -0.240605912530
```

Here:

```text
same-state probability = phi^-2
flip-state probability = phi^-1
```

This is a useful stochastic interpretation, but not yet a topological quantum derivation.

## 5. Gate verdict

| Criterion | Status | Evidence | Meaning |
|---|---|---|---|
| derive |F|^2 from standard record normalizations | fail | Best existing normalization is anti_Ising_K_minus_half_log_phi with relative error 0.000000. | |F|^2 is not forced by row/column/Sinkhorn/PF normalizing A, RL, L+R, or N_tau. |
| derive |F|^2 from a simple Gibbs switch rule | pass_but_new_assumption | If switch/stay weight ratio is phi, normalized transition matrix equals |F|^2. | Works only after adding a new phi-biased switch principle. |
| connect |F|^2 to Ising-like probability | pass_as_interpretation | |F|^2 equals symmetric anti-persistent transition with K=-0.5 log phi. | Probability layer has a classical stochastic interpretation. |
| derive F amplitudes from record counts | fail_not_yet | Squared probabilities do not determine F signs/phases, especially the negative F entry. | No full amplitude/F-symbol derivation. |
| promote to topological quantum anchor | not_promoted | We have a possible probability bridge, but not an amplitude or braiding bridge. | Remain at fusion-count plus candidate probability bridge. |


## 6. Current status after G4C

Allowed claim:

> The Fibonacci \(F\)-symbol squared gives a phi-biased stochastic transition matrix, and this matrix can be reproduced by a simple Gibbs switch/stay rule with odds \(arphi\).

Not allowed:

> The record model derives the Fibonacci F-symbol.

Not yet.

Best current classification:

```text
fusion-count bridge: passed
F-symbol amplitude bridge: failed/not yet
probability bridge: candidate, requires new phi-switch principle
topological quantum anchor: not promoted
```

## 7. Next gate

The most honest next gate is G4C2:

```text
derive phi switch bias from the record model
```

Question:

> Can switch/stay odds \(arphi\) be obtained from A eigenvectors, Gibbs weights, maximum entropy, or minimal persistent sector structure?

If yes, the probability bridge strengthens.

If no, the \(|F|^2\) connection remains an imported Fibonacci probability layer.

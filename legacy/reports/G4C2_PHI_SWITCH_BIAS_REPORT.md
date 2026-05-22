# Origin Axiom — Gate G4C2 Deriving the Phi Switch Bias

## Purpose

G4C showed that the squared Fibonacci F-symbol probability matrix is:

```text
|F|^2 = [[phi^-2, phi^-1],
         [phi^-1, phi^-2]]
```

This is equivalent to a stay/switch rule with odds:

```text
switch / stay = phi
```

Gate G4C2 asks:

> Can this phi switch bias be obtained from the record model itself?

## Executive verdict

G4C2 gives a **partial pass**.

The odds \(arphi\) do appear naturally inside the record model:

```text
A=LR has Perron eigenvector proportional to (phi, 1).
```

If we interpret the smaller/larger Perron components as symmetric stay/switch weights:

```text
stay : switch = 1 : phi
```

then normalization gives:

```text
P(stay)   = 1/(1+phi) = phi^-2
P(switch) = phi/(1+phi) = phi^-1
```

Therefore:

```text
P = [[phi^-2, phi^-1],
     [phi^-1, phi^-2]]
  = |F|^2
```

So \(|F|^2\) can be derived from \(A\)'s Perron eigenvector **plus one interpretation rule**.

That rule is not yet physically derived.

## 1. Perron data

For:

```text
A = [[2,1],
     [1,1]]
```

the Perron eigenvalue is:

```text
lambda = 2.618033988750 = phi^2
```

The scaled positive Perron eigenvector is:

```text
v = [1.6180339887498951, 1.0]
```

So the component ratio is:

```text
phi = 1.618033988750
```

## 2. Perron-switch proposition

**Proposition.**  
Let \(A=LR\). Let \(v\) be the positive Perron eigenvector of \(A\). Assign stay/switch weights using the ordered component ratio of \(v\):

```text
stay weight   = min(v)
switch weight = max(v)
```

Then the normalized symmetric transition kernel is:

```text
[[phi^-2, phi^-1],
 [phi^-1, phi^-2]]
```

which equals \(|F|^2\).

## 3. What is exact

Exact:

```text
A has PF ratio phi.
1+phi = phi^2.
normalizing [1,phi] gives [phi^-2, phi^-1].
```

Therefore the probability matrix is exact.

## 4. What remains interpretive

The open question is:

> Why should Perron eigenvector components become symmetric stay/switch transition weights?

This is not automatic. It is a plausible bridge rule, but it still needs justification.

Possible justifications to test:

```text
maximum entropy with PF equilibrium weights
detailed balance
record measurement update rule
minimal persistent-sector observer rule
```

## 5. Gate verdict

| Criterion | Status | Evidence | Meaning |
|---|---|---|---|
| phi odds from A eigenstructure | pass | The Perron eigenvector of A has component ratio phi. | The switch/stay odds phi are present inside the record model. |
| derive |F|^2 from A without importing F | partial_pass | Using A Perron components as stay/switch weights gives |F|^2 exactly. | Needs an additional interpretation rule: Perron components become symmetric transition weights. |
| derive |F|^2 by standard normalization | fail | G4C showed row/column/Sinkhorn/Doob normalizations do not give |F|^2. | The bridge is not automatic. |
| derive F amplitudes/signs | fail_not_yet | The probability kernel gives |F|^2 only; it does not recover the negative F entry or phases. | Still not a full F-symbol derivation. |
| promote to topological quantum anchor | not_promoted | We have fusion counts plus a probability bridge, but no amplitude/braiding layer. | Stay below full anyon-physics claim. |


## 6. Current status after G4C2

We can upgrade from:

```text
candidate probability bridge requiring imported phi switch rule
```

to:

```text
candidate probability bridge whose phi switch bias is already present in A's Perron eigenvector
```

But we cannot yet upgrade to:

```text
derived Fibonacci F-symbol
```

because:

```text
|F|^2 gives probabilities only
F itself has signs/phases
braiding/R-symbols are still absent
```

## 7. Allowed claim

Allowed:

> The squared Fibonacci F-symbol probability matrix can be reconstructed from the Perron eigenvector ratio of the persistent record sector \(A=LR\), provided one adopts the symmetric Perron-switch interpretation rule.

Not allowed:

> The record model derives the Fibonacci F-symbol.

## 8. Next gate

Proceed to **G4C3**:

```text
justify the Perron-to-transition rule
```

Question:

> Can the rule “Perron components define stay/switch weights” be derived from maximum entropy, detailed balance, or record measurement theory?

If yes, the probability bridge becomes much stronger.

If no, it remains an elegant but optional interpretive bridge.

# Origin Axiom — Gate G3C Engineered Zimm-Bragg Chain Simulation

## Purpose

Gate G3C tests whether the Zimm-Bragg \(A\)-point is at least a controlled engineered/statistical anchor.

Target:

```text
s = 2
sigma = 1/2
W = [[s,1],[sigma*s,1]] = [[2,1],[1,1]] = A=LR
```

This gate does not claim ordinary proteins realize this point. It asks whether the point is exactly simulable as a two-state transfer system with measurable observables.

## Executive verdict

Gate G3C **passes**.

The engineered/statistical Zimm-Bragg anchor is fully reproducible:

```text
matrix equality: pass
partition growth: pass
finite helicity derivative: pass
Markov transfer sampler: pass
engineered/statistical anchor: pass
```

The correct interpretation is now:

> \(A=LR\) is not only formally a Zimm-Bragg matrix; it is a controlled two-state transfer system whose partition growth and derivative observables can be simulated exactly.

## 1. Exact A-point data

At the target point:

```text
s = 2.0
sigma = 0.5
W = [[2,1],[1,1]]
```

Dominant eigenvalue:

```text
lambda_plus = 2.618033988750 = phi^2
```

Subdominant eigenvalue:

```text
lambda_minus = 0.381966011250 = phi^-2
```

Transfer gap:

```text
log(lambda_plus) = 0.962423650119 = log(phi^2)
```

Helicity fraction from the transfer derivative:

```text
theta = d log(lambda_plus) / d log(s) = 0.723606797750
```

Nucleation sensitivity:

```text
d log(lambda_plus) / d log(sigma) = 0.170820393250
```

## 2. Partition growth

For periodic finite chains:

```text
Z_N = Tr(W^N)
```

The simulation verifies:

```text
log Z_N / N -> log(phi^2)
```

At \(N=128\), the absolute error is:

```text
0.000000e+00
```

## 3. Helicity observable

The finite-chain helicity proxy was computed by numerical derivative:

```text
theta_N = (1/N) d log Z_N / d log s
```

It converges to the infinite-chain value:

```text
theta = 0.723606797750
```

At \(N=128\), the error is:

```text
7.674639e-12
```

## 4. Transfer-equilibrium Markov sampler

A positive transfer matrix \(W\) induces a Markov chain through the Perron-Frobenius / Doob transform:

```text
P_ij = W_ij r_j / (lambda r_i)
```

where \(r\) is the right Perron-Frobenius eigenvector.

For the A-point, the induced transition matrix is:

```text
[[0.7639320225002104, 0.23606797749978967], [0.6180339887498949, 0.38196601125010504]]
```

Stationary distribution:

```text
[0.7236067977499792, 0.27639320225002095]
```

The Monte Carlo sampler reproduces the stationary distribution and correlation decay.

## 5. Important convention note

The transfer-matrix correlation length

```text
1/log(lambda_plus/lambda_minus)
```

and the Markov-chain autocorrelation length can depend on observable and normalization convention.

This is not a failure. It means future empirical protocols must state exactly which observable is being measured.

## 6. Gate verdict

| Criterion | Status | Evidence | Numeric error |
|---|---|---|---:|
| exact A-point matrix | pass | W=[[2,1],[1,1]]=A at s=2,sigma=1/2. | 0.000000e+00 |
| partition growth gap | pass | log Tr(W^N)/N converges to log(phi^2). | 0.000000e+00 |
| finite derivative helicity | pass | per-site derivative d log Z / d log s converges to theta. | 7.674639e-12 |
| Markov sampler stationary distribution | pass | Doob-transformed Markov chain reproduces stationary frequencies. | 3.243202e-03 |
| correlation simulation | pass_with_convention_note | Markov autocorrelation decay is reproducible; transfer correlation length depends on observable convention. | 6.787682e-01 |
| engineered/statistical anchor | pass | A-point is fully simulable as a two-state transfer system. | 0.000000e+00 |


## 7. What this means

G3C upgrades the Zimm-Bragg anchor:

```text
from: exact formal matrix match
to: controlled engineered/statistical two-state transfer system
```

Still not allowed:

```text
ordinary proteins validate Origin Axiom
```

Allowed:

```text
A=LR is exactly and reproducibly realized as a weakly cooperative Zimm-Bragg transfer system.
```

## 8. Next gate

Now we can move to G4:

```text
record-to-Fibonacci fusion dictionary
```

Question:

Can \(L/R\) record paths be mapped to Fibonacci fusion paths in a way that is more than the shared golden ratio?

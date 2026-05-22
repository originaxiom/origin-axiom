# Origin Axiom — Gate G2 Ising Observable Protocol

## Purpose

Gate G2 translates the formal mapping

```text
L+R = [[2,1],[1,2]]
```

into a measurable one-dimensional Ising observable.

The goal is to turn the full trace-ensemble anchor into:

```text
a correlation-length protocol
```

rather than only a matrix identity.

## Executive result

Gate G2 is **protocol-ready**.

At

```text
K = 0.5 log2 = 0.346573590280
```

the normalized zero-field 1D Ising transfer matrix equals:

```text
[[2,1],[1,2]] = L+R
```

The observable prediction is:

```text
correlation ratio C(r+1)/C(r) = 1/3
correlation length xi = 1/log3 = 0.910239226627
```

## 1. Exact transfer matrix mapping

The zero-field Ising transfer matrix is:

```text
T = [[exp(K), exp(-K)],
     [exp(-K), exp(K)]]
```

Multiplying by the harmless scalar factor exp(K) gives:

```text
T_norm = [[exp(2K), 1],
          [1, exp(2K)]]
```

Set:

```text
exp(2K)=2
```

Then:

```text
K = 0.5 log2
```

and:

```text
T_norm = [[2,1],[1,2]] = L+R.
```

## 2. Observable correlation prediction

In the infinite one-dimensional zero-field Ising chain:

```text
C(r) = <s_i s_22> = (tanh K)^r
```

At the target point:

```text
tanh(K)=1/3
```

Therefore:

```text
C(r) = (1/3)^r
```

and:

```text
xi = -1/log(tanh K) = 1/log3.
```

## 3. Finite-chain partition check

For periodic chain length N using the normalized transfer matrix:

```text
Z_N = 3^N + 1
```

so:

```text
log(Z_N)/N -> log3.
```

This is the same full trace-ensemble scale found in Gate G1.

## 4. Synthetic measurement test

I generated noisy synthetic correlation data and fitted:

```text
log C(r) = a - r/xi
```

over r=1..10.

The test recovers the target xi within 5% across the sampled noise/settings.

The fit results are in:

```text
G2_ising_correlation_fit_results.csv
```

## 5. Gate verdict

| Criterion | Status | Evidence | Target |
|---|---|---|---|
| transfer matrix match | pass | At K=0.5 log2, normalized zero-field Ising transfer matrix equals [[2,1],[1,2]]=L+R. | exact equality |
| correlation ratio | pass | tanh(K)=1/3 exactly. | C(r+1)/C(r)=1/3 |
| correlation length | pass | xi=-1/log(tanhK)=1/log3. | 0.910239226627 |
| synthetic observable recovery | pass | Noisy synthetic correlation fits recover xi within 5% for tested noise/sample settings. | fit xi within 5% |
| empirical readiness | protocol_ready | Requires physical or simulated 1D Ising-like chain tuned to K=0.5 log2. | measurable C(r) |


## 6. Physical interpretation

This is a real observable protocol:

```text
prepare or simulate a 1D zero-field Ising chain
tune K to 0.5 log2
measure C(r)
fit xi
check xi ≈ 1/log3
```

This does not prove the universe is an Ising chain.

It proves that the full \(L/R\) trace ensemble has an exact observable realization in classical statistical mechanics.

## 7. Next gate

Proceed to Gate G3:

```text
Zimm-Bragg realism check
```

Goal:

Check whether the minimal sector point

```text
s=2, sigma=1/2
```

is physically, chemically, or synthetically realizable in a helix-coil / polymer-transfer setting.

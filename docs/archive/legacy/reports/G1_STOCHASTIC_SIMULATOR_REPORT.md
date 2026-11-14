# Origin Axiom — Gate G1 Stochastic Simulator Reproduction

## Purpose

Gate G1 asks whether the record-transfer anchor reproduces its exact statistical targets in a runnable simulator.

Targets:

- beta_c_count = log2 = 0.693147180560
- beta_c_trace/lambda = log3 = 1.098612288668
- h_A = log(phi^2) = 0.962423650119

## Executive result

Gate G1 **passes**.

The simulator reproduces count growth, trace growth, the A-sector periodic entropy gap, and the exact Gibbs threshold forms.

The only caveat is that direct Monte Carlo trace estimation gets noisy for large N, because trace weights are heavy-tailed. This is a sampling issue, not an algebraic failure.

## 1. Exact growth checks

For words of length N, Z_count(N)=2^N, so log(Z_count)/N = log2.

For the trace ensemble, Z_trace(N)=sum Tr(M_w)=Tr((L+R)^N)=3^N+1, so log(Z_trace)/N tends to log3.

## 2. Stochastic uniform trace sampling

The simulator samples random words w in {L,R}^N, computes M_w, and estimates E[Tr(M_w)].

The exact expectation is E[Tr(M_w)] = (3^N+1)/2^N.

The generated table compares Monte Carlo estimates against this exact value.

## 3. A-sector periodic entropy

For A=LR, periodic sector count is P_n=|det(A^n-I)|.

The simulator verifies log(P_n)/n tends to log(phi^2).

At n=60, absolute error is 0.000000e+00.

## 4. Gibbs threshold formulas

Let x=exp(-beta).

Count grand partition: Z_count(beta)=2x/(1-2x), convergent iff beta>log2.

Trace grand partition: Z_trace(beta)=3x/(1-3x)+x/(1-x), convergent iff beta>log3.

## 5. Gate verdict

| Criterion | Status | Evidence | Numeric error |
|---|---|---|---:|
| count threshold log2 | pass | exact word count growth is 2^N | 0.000000e+00 |
| trace threshold log3 | pass | exact trace sum is 3^N+1 | 2.220446e-16 |
| uniform stochastic trace reproduction | pass_with_sampling_noise | Monte Carlo mean trace approximates exact uniform expectation; variance grows with N | 1.081664e-03 |
| A-sector gap log(phi^2) | pass | periodic entropy log|det(A^n-I)|/n converges to log(phi^2) | 0.000000e+00 |
| Gibbs threshold formulas | pass | closed-form count and trace grand partitions implemented | 0.000000e+00 |

## 6. Interpretation

Gate G1 confirms that the record-transfer model is computationally reproducible.

This does not prove empirical physics. It proves the statistical-transfer anchor is internally exact, runnable, and falsifiable at the simulator level.

## 7. Next gate

Proceed to Gate G2: Ising observable protocol.

Goal: map the L+R point to a measurable 1D Ising correlation length xi=1/log3.

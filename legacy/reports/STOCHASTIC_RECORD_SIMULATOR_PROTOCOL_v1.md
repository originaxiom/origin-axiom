# Stochastic Record Simulator Protocol v1

## Goal

Provide a falsifiable computational protocol for the \(L/R\) record transfer model.

## Exact targets

\[
\beta_c^{count}=\log2\approx 0.693147180560,
\]

\[
\beta_c^{trace/lambda}=\log3\approx 1.098612288668,
\]

\[
h_A=\log(\varphi^2)\approx 0.962423650119.
\]

## Protocol

1. Generate random words \(w\in\{L,R\}^N\).
2. Compute \(M_w\).
3. Estimate:
   - \(\operatorname{Tr}(M_w)\);
   - \(\lambda_+(M_w)\);
   - sector classification;
   - hyperbolic probability.
4. Verify:
   \[
   \sum_{|w|=N}\operatorname{Tr}(M_w)=3^N+1.
   \]
5. Sample Gibbs weights:
   \[
   P_{\beta,\alpha}(w)\propto e^{-\beta |w|}\lambda_+(M_w)^\alpha.
   \]
6. Estimate finite-size crossover and compare to:
   \[
   \beta_c^{count}=\log2,\qquad \beta_c^\lambda=\log3.
   \]
7. Restrict to \(A=LR\) and verify:
   \[
   |\det(A^n-I)|
   \]
   has entropy rate \(\log(\varphi^2)\).

## Pass condition

The simulator reproduces the three exact scales within finite-size error.

## Fail condition

Sampling or implementation fails to recover the known exact values.

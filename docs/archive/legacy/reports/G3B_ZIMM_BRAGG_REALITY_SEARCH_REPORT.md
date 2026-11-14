# Origin Axiom — Gate G3B Zimm-Bragg Reality Search

## Purpose

Gate G3 showed that the minimal persistent sector

```text
A=LR=[[2,1],[1,1]]
```

is exactly a Zimm-Bragg transfer matrix at:

```text
s = 2
sigma = 1/2
```

Gate G3B asks the harder question:

> Is this point physically realistic, biologically natural, or mainly an engineered/statistical transfer target?

## Executive verdict

G3B keeps the Zimm-Bragg anchor, but narrows the claim.

```text
Formal transfer-matrix anchor: yes
Typical natural protein anchor: no evidence / likely no
Engineered weak-cooperativity anchor: plausible
Best next step: simulate or design a two-state Zimm-Bragg chain at s=2,sigma=1/2
```

The key issue is sigma.

Standard Zimm-Bragg descriptions emphasize:

```text
sigma << 1 < s
```

for most proteins. Our A-point has:

```text
s = 2
sigma = 0.5
```

So it is not the usual strongly cooperative alpha-helix regime. It is better understood as a weakly cooperative or engineered two-state transfer point.

## 1. What remains strong

The exact matrix match remains strong:

```text
W = [[s,1],
     [sigma*s,1]]
```

At:

```text
s=2
sigma=1/2
```

we get:

```text
W = [[2,1],
     [1,1]]
  = A=LR
```

So the formal Zimm-Bragg anchor is exact.

## 2. What weakens

The biological interpretation weakens.

For ordinary protein alpha-helix modeling, the nucleation parameter is generally small compared with propagation. That means the system has strong cooperativity: once a helix is nucleated, extending it is much easier than starting a new one.

At the A-point:

```text
sigma*s = 1
```

so coil-to-helix nucleation is not strongly suppressed. This is weak cooperativity.

## 3. What this means

Allowed claim:

> The minimal persistent sector A=LR is exactly realized by a Zimm-Bragg transfer matrix at s=2,sigma=1/2.

More precise claim:

> This is a weakly cooperative Zimm-Bragg point, better interpreted as an engineered/statistical transfer anchor than as a typical natural alpha-helix anchor.

Forbidden claim:

> Standard protein helices empirically validate the Origin Axiom.

## 4. Findings table

| Question | Finding | Confidence | Impact |
|---|---|---|---|
| Is the Zimm-Bragg transfer matrix form standard? | Yes | high | Formal A=LR anchor remains valid. |
| Is sigma=0.5 typical for protein alpha-helix transitions? | No strong evidence found; standard descriptions say sigma << 1 for most proteins. | high | Do not claim typical biological protein validation. |
| Is high sigma physically interpretable? | Yes, as weak cooperativity / small nucleation penalty. | high | A-point is a weakly cooperative transfer target. |
| Can the A-point be an engineered two-state transfer anchor? | Plausible but not yet empirically identified. | medium | Best next path is engineered/synthetic or computational polymer model. |
| Does Zimm-Bragg map to Ising-like physics? | Yes, literature supports an exact mapping to a 1D Ising model with caveats. | high | Supports treating G2/G3 as one transfer-matrix physics family. |


## 5. Recommended paths

| Rank | Path | Action | Status |
|---:|---|---|---|
| 1 | Computational/synthetic Zimm-Bragg model | Implement a two-state chain exactly at s=2,sigma=1/2 and measure helicity/correlation observables. | best immediate route |
| 2 | Search engineered weakly cooperative polymers | Look for helix-coil systems where nucleation penalty is small and sigma approaches 0.5. | open |
| 3 | Natural protein alpha-helices | Do not use as main anchor unless measured sigma near 0.5 is found. | not recommended as primary |
| 4 | Move to Lifson-Roig/capping models | Study whether a 3x3/4x4 model projects or renormalizes to A. | later, if needed |


## 6. Engineered/simulation observable protocol

Target observables:

| Test | Target | Observable | Pass condition |
|---|---|---|---|
| Matrix equality | W=[[2,1],[1,1]] | transition weight table | estimated s≈2 and sigma≈0.5 |
| Dominant eigenvalue | lambda_plus=phi^2 | partition growth rate | log Z_N/N tends to log(phi^2) for the A-sector |
| Helicity fraction | theta≈0.7236068 | fractional helix occupancy in long chain | measured theta within uncertainty |
| Correlation length proxy | xi=1/log(phi^4)≈0.519522 | exponential decay of state correlations | fit xi within tolerance |
| Cooperativity diagnosis | weakly cooperative sigma=0.5 | domain length / nucleation frequency | shorter domains than strongly cooperative sigma<<1 case |


Numerical target values:

```text
lambda_plus = phi^2 = 2.618033988750
gap = log(phi^2) = 0.962423650119
helicity fraction theta ≈ 0.7236068
correlation length proxy ≈ 0.519522
```

## 7. Gate decision

G3B decision:

```text
formal anchor retained
natural biological anchor not established
engineered/synthetic anchor remains plausible
```

Next recommended action:

```text
Run engineered Zimm-Bragg chain simulation at s=2,sigma=1/2.
```

This will give us a controlled G3C gate before moving to Fibonacci fusion.

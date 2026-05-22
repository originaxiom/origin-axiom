# Origin Axiom — Gate G3 Zimm-Bragg Realism Check

## Purpose

Gate G3 asks whether the minimal persistent sector

```text
A=LR=[[2,1],[1,1]]
```

is not only formally equal to a Zimm-Bragg transfer matrix, but also physically realistic.

The Zimm-Bragg matrix is:

```text
W = [[s, 1],
     [sigma*s, 1]]
```

where \(s\) is the helix propagation weight and \(\sigma\) is the nucleation/cooperativity parameter.

## Executive verdict

Gate G3 **passes formally** but **does not yet pass as a typical natural protein anchor**.

The exact mapping is:

```text
s = 2
sigma = 1/2
W = [[2,1],[1,1]] = A
```

But standard Zimm-Bragg descriptions emphasize:

```text
sigma << 1 < s
```

for most proteins. Our point has \(s=2\), which is physically interpretable, but \(\sigma=0.5\), which is weakly cooperative rather than strongly cooperative.

Therefore the correct status is:

```text
exact Zimm-Bragg transfer-matrix anchor
candidate engineered/synthetic anchor
not yet a typical biological alpha-helix anchor
```

## 1. Exact A-point observables

At:

```text
s = 2.0
sigma = 0.5
```

the matrix is:

```text
W = [[2,1],[1,1]]
```

The main observables are:

| Quantity | Value | Meaning |
|---|---:|---|
| trace | 3.000000000000 | trace-3 sector |
| determinant | 1.000000000000 | unimodular A point |
| lambda_plus | 2.618033988750 | phi^2 |
| lambda_minus | 0.381966011250 | phi^-2 |
| gap log(lambda_plus) | 0.962423650119 | log(phi^2) |
| helicity fraction | 0.723606797750 | infinite-chain ZB estimate |
| correlation length proxy | 0.519521730309 | 1/log(lambda_plus/lambda_minus) |

## 2. Energetic interpretation

In \(k_B T\) units:

```text
s=2            -> propagation preference = -log2 kBT
sigma=1/2      -> nucleation penalty = +log2 kBT
sigma*s=1      -> coil-to-helix nucleation weight is neutral
```

This makes the point physically interpretable, but weakly cooperative.

## 3. Comparison with stronger cooperativity

At fixed \(s=2\), lowering \(\sigma\) toward \(0.01\) or \(0.001\) moves the model away from \(A\).

The comparison table is in:

```text
G3_zimm_bragg_sigma_comparison_s_equals_2.csv
```

Key lesson:

```text
A requires sigma=0.5.
Strongly cooperative biological helix-coil behavior usually requires sigma much smaller.
```

## 4. Gate verdict

| Criterion | Status | Evidence | Implication |
|---|---|---|---|
| exact transfer matrix equality | pass | s=2 and sigma=1/2 gives W=[[2,1],[1,1]]=A. | formal transfer anchor is exact |
| physical interpretability of parameters | pass | s and sigma are standard Zimm-Bragg propagation/nucleation parameters. | not just arbitrary matrix entries |
| typical natural protein realism | fail_or_warning | sigma=1/2 conflicts with standard sigma << 1 regime for most proteins. | not a typical alpha-helix biological anchor |
| engineered/synthetic realism | candidate | weakly cooperative two-state transfer systems can in principle target high sigma. | possible engineered/statistical anchor |
| empirical anchor status | partial_pass | exact formal anchor; real-system identification remains open. | G3 passes formally, not biologically |


## 5. What this means for the Origin Axiom

The \(A=LR\) Zimm-Bragg anchor is real but limited.

Allowed claim:

> The minimal persistent sector \(A=LR\) is exactly realized by the Zimm-Bragg transfer matrix at \(s=2,\sigma=1/2\).

Careful limitation:

> This point is not the standard strongly cooperative protein helix regime. It is better interpreted as a weakly cooperative or engineered two-state transfer anchor.

Forbidden claim:

> Ordinary alpha helices empirically validate the Origin Axiom.

## 6. Next step after G3

Proceed to either:

```text
G3B: search for real systems with high sigma / weak cooperativity near 0.5
```

or:

```text
G4: record-to-Fibonacci fusion dictionary
```

My recommendation:

Do G3B first. It will tell us whether the Zimm-Bragg anchor can become experimentally realistic or remains a formal transfer-matrix anchor.

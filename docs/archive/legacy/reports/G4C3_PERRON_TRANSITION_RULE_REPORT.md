# Origin Axiom — Gate G4C3 Justifying the Perron-to-Transition Rule

## Purpose

G4C2 showed that |F|² can be reconstructed from A=LR's Perron eigenvector if we adopt the rule:

```text
Perron components become symmetric stay/switch weights
```

Gate G4C3 asks whether this rule can be justified by standard principles such as maximum entropy or detailed balance.

## Executive verdict

G4C3 gives a **conditional partial pass**, not a full derivation.

Plain maximum entropy does **not** derive the rule.

Detailed balance does **not** derive the rule.

But a more specific principle does work:

> maximum entropy with Perron degeneracy weights.

That is:

```text
A has PF component ratio phi.
Treat transition-class degeneracies as stay:switch = 1:phi.
Use the least biased distribution over those classes.
```

Then:

```text
P(stay) = 1/(1+phi) = phi^-2
P(switch) = phi/(1+phi) = phi^-1
```

So the bridge is mathematically clean, but still conditional on a new principle:

```text
PF components are transition-class degeneracy weights.
```

## 1. Perron data

For A:

```text
A = [[2,1],
     [1,1]]
```

we have:

```text
lambda_PF = 2.618033988750
scaled PF vector = [1.6180339887498951, 1.0]
normalized PF vector = [0.6180339887498949, 0.3819660112501051]
```

## 2. What fails

### Plain maximum entropy

If all we know is that there are two transition classes, stay and switch, maximum entropy gives:

```text
P(stay)=1/2
P(switch)=1/2
```

not |F|².

### Detailed balance

A symmetric two-state kernel:

```text
P = [[1-p,p],
     [p,1-p]]
```

satisfies detailed balance with uniform stationary distribution for every p.

So detailed balance alone does not select:

```text
p = phi^-1
```

## 3. What works conditionally

### Perron-degeneracy MaxEnt

Use the ordered Perron components as class degeneracies:

```text
g_stay = 1
g_switch = phi
```

Then least-biased weighting gives:

```text
P(stay)=g_stay/(g_stay+g_switch)
P(switch)=g_switch/(g_stay+g_switch)
```

Since:

```text
1 + phi = phi^2
```

we obtain:

```text
P(stay)=phi^-2
P(switch)=phi^-1
```

This equals |F|².

## 4. Alternative equivalent interpretation

The same kernel can be described as an anti-persistent PF Markovization:

```text
A's normalized PF probabilities are (phi^-1, phi^-2).
If the current state swaps the PF preference,
then switching receives the larger PF weight.
```

This again gives |F|², but it assumes an anti-persistent/switch-favored measurement rule.

## 5. Formal propositions

| Name | Status | Unproven assumption |
|---|---|---|
| Maximum-entropy Perron-degeneracy proposition | valid conditional derivation | PF components are legitimate degeneracy weights for transition classes. |
| Detailed-balance Perron-switch proposition | valid conditional derivation | odds constraint should be assigned to switch/stay. |
| No-go statement | proved in two-state family | none |


## 6. Gate verdict

| Criterion | Status | Evidence | Meaning |
|---|---|---|---|
| plain maximum entropy derives rule | fail | Unconstrained MaxEnt gives 1/2,1/2. | entropy alone is insufficient |
| detailed balance derives rule | fail | Detailed balance allows the whole symmetric family [[1-p,p],[p,1-p]]. | reversibility alone is insufficient |
| Perron degeneracy MaxEnt derives rule | partial_pass | Using A's PF component ratio as class degeneracy gives |F|^2. | requires PF-as-degeneracy principle |
| anti-persistent PF Markovization derives rule | partial_pass | Swapping PF probabilities by current state gives |F|^2. | requires anti-persistent/switch-favored rule |
| fully first-principles derivation | not_yet | The crucial PF-to-transition-class rule is not yet forced. | probability bridge remains conditional |
| promote topological quantum anchor | not_promoted | No signs/phases/R-symbols; only probabilities. | stay below full anyon claim |


## 7. Current honest status

We can now say:

> The phi switch bias can be reconstructed from A's Perron eigenstructure using a maximum-entropy-with-Perron-degeneracy principle.

We cannot yet say:

> The record model forces this principle.

So the probability bridge is stronger than before, but still not fundamental.

Current classification:

```text
fusion-count bridge: pass
probability bridge: conditional partial pass
F amplitude/sign bridge: not achieved
topological quantum anchor: not promoted
```

## 8. Next best move

My recommendation:

```text
Do G4D next: R-symbol / braiding audit.
```

Reason:

If signs/phases are impossible in our current framework, then perfecting the probability bridge is not enough. We need to know whether a true anyon-amplitude layer is even reachable.

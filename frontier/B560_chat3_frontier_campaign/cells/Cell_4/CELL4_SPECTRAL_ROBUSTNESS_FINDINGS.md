# Cell 4 — Degree-4 Spectral Robustness and Measurement Audit

## Repository baseline

```text
383d20f97f83c1453103e38797a2b2690d9b1135
```

No repository files were modified.

---

# Executive verdict

The degree-4 frequency module is exact and stronger than previously stated:

\[
\boxed{\mathbb Z f_a+\mathbb Z f_b+\mathbb Z f_A+\mathbb Z f_B
=\mathbb Z[\tau],\qquad \tau^4-\tau^2-1=0.}
\]

The five target labels are degree-four algebraic numbers. Finite-chain spectra
contain open gaps at those labels throughout two sampled coupling boxes
containing the two benchmark Hamiltonians.

Two earlier statements require correction:

1. distance from the full golden module is not an absolute discriminator,
   because \(\mathbb Z+\mathbb Z/\varphi\pmod 1\) is dense;
2. infinite-volume opening of all five gaps throughout a continuous coupling
   chamber is not yet proved.

The correct status is:

> **Experiment-ready dimensionless prediction with exact label algebra,
> strong finite-size and coupling evidence, and an open infinite-volume
> gap-opening theorem.**

---

# 1. Exact degree-4 module

Writing \(\tau=\sqrt\varphi\), the four letter frequencies are

\[
\begin{aligned}
f_a&=\tau-1,\\
f_b&=\tau^3-\tau^2-\tau+1,\\
f_A&=\tau^2-\tau,\\
f_B&=-\tau^3+\tau+1.
\end{aligned}
\]

Their coefficient matrix in the basis
\((1,\tau,\tau^2,\tau^3)\) has determinant

\[
\boxed{1}.
\]

Therefore

\[
\boxed{
\langle f_a,f_b,f_A,f_B\rangle_{\mathbb Z}
=
\mathbb Z[\tau].
}
\]

All five measured targets

\[
f_b,\quad f_B,\quad f_a,\quad f_A,\quad f_a+f_b
\]

have irreducible degree-four minimal polynomials.

**Status:** `PROVED EXACTLY`

The general theorem assigning IDS gap labels to the frequency/K-theory module
is classical. The exact \(\mathbb Z[\tau]\) instantiation is the
object-specific contribution.

---

# 2. Top-30 coupling robustness

At \(N=3000\), every target was tracked as the largest spectral gap within
five index steps of its exact asymptotic IDS label.

## Box C1

\[
a=1,\quad
b\in[0.72,0.88],\quad
A\in[0.52,0.68],\quad
B\in[0.32,0.48].
\]

A \(4^3=64\)-point grid was evaluated. All five target gaps remained in the
top 30 at every point.

| label | minimum width | worst rank |
|---|---:|---:|
| \(f_b\) | 0.029260 | 20 |
| \(f_B\) | 0.077918 | 10 |
| \(f_a\) | 0.185110 | 4 |
| \(f_A\) | 0.037485 | 14 |
| \(f_a+f_b\) | 0.144467 | 6 |

## Box C2

\[
a=1,\quad
b\in[0.52,0.58],\quad
A\in[0.72,0.78],\quad
B\in[0.32,0.38].
\]

A \(5^3=125\)-point grid was evaluated. Again, all five target gaps remained
in the top 30 at every point.

| label | minimum width | worst rank |
|---|---:|---:|
| \(f_b\) | 0.021431 | 30 |
| \(f_B\) | 0.024157 | 24 |
| \(f_a\) | 0.121186 | 6 |
| \(f_A\) | 0.094303 | 10 |
| \(f_a+f_b\) | 0.319945 | 2 |

**Status:** `COMPUTED ON 189 FINITE-N COUPLING POINTS`

This does not prove the full continuous boxes or their infinite-volume limits,
but it removes dependence on only two isolated coupling choices.

---

# 3. Explicit finite-N perturbation neighborhoods

If every hopping amplitude changes by at most \(\delta\), then

\[
\|\Delta H\|_2\le 2\delta.
\]

Each gap edge moves by at most \(2\delta\), so a gap of width \(g\) remains
open whenever

\[
\boxed{4\delta<g.}
\]

At the two \(N=3000\) benchmark centers:

| center | smallest target gap | guaranteed \(\ell_\infty\) coupling radius \(g/4\) | half-margin radius \(g/8\) |
|---|---:|---:|---:|
| C1 | 0.086312 | 0.021578 | 0.010789 |
| C2 | 0.025136 | 0.006284 | 0.003142 |

With linewidth \(\Gamma\), a conservative combined budget is

\[
\boxed{
4\delta+2\Gamma<g_{\min}.
}
\]

These are normalized finite-chain engineering inequalities.

---

# 4. Finite-size hardening

The substitution-prefix lengths

\[
N=893,\ 3283,\ 12069,\ 44368
\]

were tested at both benchmark couplings.

Across all 40 tracked gaps:

- every target remained open;
- the maximum \(N|\operatorname{IDS}_N-f|\) was
  **0.128828**;
- the minimum target gap in the more fragile C2 chain was
  **0.018979**.

Thus the IDS label error follows the expected integer-count scale

\[
|\operatorname{IDS}_N-f|=O(N^{-1}),
\]

while the target widths remain order one rather than collapsing like ordinary
level spacing.

**Status:** `COMPUTED THROUGH N=44368`

---

# 5. Correction: the golden module is dense

The phrase “the labels sit off the golden lattice” is valid only after
imposing a coefficient or gap-index cutoff.

Since \(1/\varphi\) is irrational,

\[
\left\{P+Q/\varphi\pmod 1:P,Q\in\mathbb Z\right\}
\]

is dense in \([0,1]\). No finite-precision single label has a positive distance
from the entire golden module.

The correct control is a **bounded-index Fibonacci comparison**.

For golden indices \(|Q|\le30\), the smallest distance to any of the five
quartic targets is

\[
\boxed{0.000933119}.
\]

To exclude all such low-index golden labels, total IDS uncertainty must obey

\[
\boxed{
\varepsilon_{\mathrm{IDS}}<0.000466560.
}
\]

Counting resolution alone therefore requires

\[
N\ge 2144,
\]

with

\[
\boxed{N\ge5000}
\]

recommended as a conservative design floor.

A golden chain can counterfeit the values only at much higher indices:

- \(Q=763\)–\(1998\) for \(10^{-4}\) agreement;
- \(Q=7528\)–\(19709\) for \(10^{-5}\);
- \(Q=109212\)–\(176710\) for \(10^{-6}\).

The useful discriminator is therefore:

> the labels occur among the largest low-index gaps and obey the quartic
> one-measurement relations—not merely that a decimal lies outside a dense
> quadratic module.

**Status:** `EARLIER ABSOLUTE-SEPARATION CLAIM CORRECTED`

---

# 6. Theorem boundary

## Exact

- \(\tau\) has polynomial \(t^4-t^2-1\);
- the frequency/gap-label module is exactly \(\mathbb Z[\tau]\);
- all five target labels have degree four;
- their one-measurement relations are exact.

## Numerically hardened

- the five target gaps are open at both benchmark couplings;
- they remain top-30 on 189 sampled coupling points;
- their labels converge at \(O(1/N)\);
- finite-chain perturbation and linewidth budgets are explicit.

## Open

- an infinite-volume theorem that all five gaps stay open throughout either
  continuous coupling box;
- a degree-4 dry-gap theorem showing every allowed module label opens;
- a rigorous infinite-system disorder theorem.

The gap-label group and the gap-opening problem must remain separate.

---

# Cell 4 ledger

```text
FREQUENCY MODULE = Z[tau]                 PROVED EXACTLY
FIVE TARGET LABELS DEGREE 4               PROVED EXACTLY
TOP-30 ROBUSTNESS, C1 BOX                  64/64 POINTS
TOP-30 ROBUSTNESS, C2 BOX                  125/125 POINTS
FINITE-SIZE RUN                            N <= 44368
LOCAL FINITE-N COUPLING BALLS              COMPUTED
FULL GOLDEN-MODULE DISTANCE                INVALID / CORRECTED
LOW-INDEX GOLDEN CONTROL                   QUANTIFIED
CONSERVATIVE DESIGN FLOOR                  N >= 5000
INFINITE-VOLUME OPEN CHAMBER               OPEN
ALL ALLOWED LABELS OPEN                    OPEN
CELL STATUS                                EXPERIMENT-READY, THEOREM PARTIAL
REPOSITORY WRITES                          NONE
```

The governed campaign now advances to **Cell 5 — Ghost Scanner Completion**.

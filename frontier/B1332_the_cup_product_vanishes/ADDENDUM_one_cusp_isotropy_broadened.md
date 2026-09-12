# B1332 addendum 3 — one-cusped isotropy, broadened in characteristic zero, with a vacuity audit

B1334's addendum leaves the one-cusped case — the one the programme needs — reducing **entirely** to
isotropy, that being its only surviving route. So the right thing to do with it is try to **break**
it. This is that attempt. It did not break.

## The test

One-cusped census manifolds carrying cusp-trivial characters, **geometric holonomy**,
**characteristic zero** at 40 digits, germs including sums. B1335's lessons applied throughout:

- the geometric holonomy only — arbitrary representations mislead (B1335);
- a peripheral trace of `-2` makes `Sym^odd` have every eigenvalue `-1`, so `t_0 = 0` and T5 kills
  the sector: those are **skipped as vacuous, not counted as evidence**;
- every numerical rank carries its singular-value gap, and a borderline sector reads
  **INCONCLUSIVE**, never as a verdict.

## The result

Six manifolds beyond B1332's original three — `m003`, `m006`, `m009`, `m035`, `m039`, `m040`:

| parity | `t_0` | `dim L` | equations each | verdict | count |
|---|---|---|---|---|---|
| odd | 1 | 1 | **1** | ISOTROPIC | 18 |
| even | 1 | 1 | 0 (vacuous) | ISOTROPIC | 22 |
| even | 2 | 2 | **1** | ISOTROPIC | 44 |
| even | 3 | 3 | **3** | ISOTROPIC | 22 |

```
SECTORS 106 | NON-VACUOUS 84 | genuine scalar equations satisfied 128
NON-ISOTROPIC 0 | INCONCLUSIVE 0
```

The first row matters: for **odd** parity the invariant form is alternating and the induced pairing
**symmetric**, so `<x,x> = 0` is a real equation even at `dim L = 1`. Those 18 are not vacuous.

## Two errors caught on the way, both of a kind this arc keeps making

**1. A vacuous scan nearly reported as evidence.** The first pass used only single germs `Sym^m`.
Every sector came back `t_0 = 1` with even `m` — **all 48 vacuous, zero genuine equations** — and
read as "48 isotropic". The vacuity accounting added after §2 of the main findings caught it at
once. Non-vacuous sectors need germ **sums**, where `t_0` is the number of summands.

**2. Nineteen false counterexamples.** With sums added, 19 sectors came back **NOT isotropic** — all
of them the mixed germ `Sym^2 (+) Sym^4`. Artifact: the test used *every* `pi_1(T)`-invariant form,
while the duality pairing uses only the **`SL2`-invariant** ones, and §3 of the main findings had
already shown that for non-isomorphic summands the cross-terms carry no invariant functional at all.
Against the correct forms all 19 are isotropic. The magnitudes were a tell too — `1e-7` to `1e-5`
relative, nowhere near a clean non-zero — which is why the thresholds now report anything borderline
as INCONCLUSIVE rather than as a finding.

## What it adds

One-cusped isotropy now rests on **128 genuine scalar equations across nine manifolds** — B1332's
`s958`, `t12833`, `t12835` exactly over `Q(zeta_12)`, plus these six in characteristic zero on the
geometric holonomy — with an explicit audit separating what is tested from what is free.

It did not break. It remains unproved. It remains the only live route for the case the programme
needs.

Reproduce: `verification/char0iso.py <manifolds>`; `verification/char0.py` supplies the
characteristic-zero holonomy and numerical ranks with gaps. Logs in `verification/logs/`.

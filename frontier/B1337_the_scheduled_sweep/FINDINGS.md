# B1337 — the SCHEDULED sweep: 156 of 277 are readable here, and the first one read corrects itself

B1336 ended by recommending that the harvest ledger's SCHEDULED rows be swept before a campaign
picks its target, after two days of index work were spent on a price another seat had already
settled. This is that sweep.

## 1. The size of it

`docs/HARVEST_LEDGER.md` carries **526 rows, of which 277 are SCHEDULED** — more than half the
ledger is harvested work that no main text names.

| | rows |
|---|---|
| **readable at their referenced commit** | **156** |
| not readable (artifact on a branch absent from this repo) | 121 |

Readable, by seat: cloud 100, consolidation 30, codex 18, cc3-braver 5, audit 3.
Not readable: physics seat 57, cc3 paper seat 41, hostile-review 12, SM-derivation 9.

`verification/readable_scheduled.json` lists all 156 with seat, arc, claim, commit and path, so the
next sweep starts from a list rather than from the ledger.

## 2. A parsing trap that reversed the answer

The source field is `` `path` @ commit `` — **the commit ref sits OUTSIDE the backticks.** A parser
that takes the backtick content and splits it on `' @'` finds no commit, falls back to `HEAD`, and
reports **zero readable**. That is what the first pass here did, and it would have produced exactly
the wrong recommendation: *"the backlog cannot be verified on this bench, it is a branch-access
problem."* The manual check that contradicted it was one `git show` (`e51afd6c:outside_bench/memos/
PRINCIPAL_WITNESSES.md`, which works). **The backlog is largely readable; the first measurement of it
was not.**

## 3. The first high-value row read, and it needs a correction

Eleven of the 156 touch chirality, generations or the 27. The most load-bearing is **cloud memo 79**,
`ONE_BIT_WITNESS.md`:

> *"on the FULL radius-5 ball (484 reduced words), `chi(w) = chi(w^-1)` with zero exceptions … the
> 27-level shadow of the figure-eight's strong invertibility … **The chirality bit is
> character-INVISIBLE**."*

**The computation is right. The attribution is not.** In `SL2`, every element is conjugate to its
inverse — `A` and `A^-1` have eigenvalues `{L, 1/L}`, the same multiset — so `tr(A) = tr(A^-1)`
**identically**, and `chi_27`, a sum of `Sym`-power traces, inherits it. Nothing about the
figure-eight is used.

Tested on the geometric holonomy of four manifolds, 120 random words each, at 30 digits:

| | `max abs( tr(w) - tr(w^-1) )` | `max abs( chi_27(w) - chi_27(w^-1) )` |
|---|---|---|
| `m004` | `4.7e-46` | `4.3e-40` |
| `m003` | `6.7e-48` | `4.4e-43` |
| `m010` | `2.2e-46` | `1.7e-41` |
| `s958` | `1.0e-44` | `1.1e-38` |

It holds on every manifold, because it is a fact about `SL2` and not about any of them.

**The memo half-saw this.** It records that its pre-registered non-vacuity gate **refused** — "some
word has `chi(w) != chi(w^-1)`" could not be satisfied — and calls the refusal the finding. It was
right to: a gate that cannot be satisfied is the signature of a test that cannot fail.

## 4. The third instance of one failure mode

| | the test | what it turned out to be |
|---|---|---|
| B1297 §0 | the pre-registered PASS/FAIL on the 3-fold cover | reported **FORCED**, not FAIL — "could never have passed" |
| THE PAPER §8 | the pre-registered test on the cyclic tower | *"could not have passed once the two theorems above were found"* |
| cloud memo 79 | the non-vacuity gate on `chi` vs `chi*` | **refused** — the statement is an `SL2` theorem |

Three independent seats, three pre-registered tests, none of which could have failed. That is a
pattern about how this programme designs tests, and it is worth more than any one of the three.

## 5. What it corroborates

B1334 proved `I = 0` where a deformation exists using **only** dimension counting and inversion
symmetry — no geometry, no arithmetic, no chirality. Memo 79 reaches the same place from the
character side: the holonomy characters cannot see `27` vs `27bar` **on any manifold**. Two
independent routes agreeing that **the vanishing is not about the object being special.**

## What to do next

Work the readable list. `verification/readable_scheduled.json` has all 156; the eleven touching
chirality, generations or the 27 are the ones that bear on live paper claims, and memo 79 was only
the first. The 121 unreadable rows need their branches brought into this repo before anything can be
said about them — that is a repository problem, not a mathematical one, and it should be named as
such rather than left as a permanent backlog.

Reproduce: `verification/sweep.py` (run from the repo root).

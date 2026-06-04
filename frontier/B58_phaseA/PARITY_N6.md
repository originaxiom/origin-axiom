# n=6 parity adjudication via the F_p engine — INCONCLUSIVE (parity sector is NOT clean)

**Date:** 2026-06-04. **Status:** exploratory, **uncommitted**. Proven core P1–P16 untouched.
`m=1`. Engine: `frontier/B58_phaseA/jacobian_closure.py` (exact F_p ε-series pinv-limit).
This is the handoff Task B: run the engine at n=6 to adjudicate the parity factor between the two
candidates — θ's `(t−1)³(t+1)²` (Lie-theory-grounded) vs Sym's `(t−1)²(t+1)³` (SYM_DECOMPOSITION /
V27). **Result: the engine does NOT cleanly adjudicate — the n=6 parity sector is itself degenerate
and corrupted, contrary to the Task-B premise that "the engine is reliable for the parity sector."**

## What the engine did at n=6

- **It does not resolve with the default basis.** `maxlen=4` (the n≤5 setting) returns
  `INCONSISTENT/UNDETERMINED at row 0`, identically at `L=12,16,20,24` (so not an ε-truncation /
  "increase L" issue), even though the 35-word fixed-line gradient is full row-rank (35/35).
  `maxlen=5` also fails for the seeds tried.
- **It resolves only with `maxlen=6, seed=20`**, and there it is **prime-stable** (3 primes
  `{2000003, 2000029, 2000039}`) and **L-converged** (identical at `L=14` and `L=16`), with **no
  untagged remainder**:
  ```
  PARITY = (t-1)^2 (t+1)^5
  full tower: char(M^-1)·char(M^1)^2·char(M^2)^4·char(M^3)·char(M^4)·char(M^5)·char(M^6)
              ·char(-M^2)·char(-M^3)·char(-M^4)·(t-1)^2·(t+1)^5
  ```

## Why this does NOT adjudicate the parity

**The parity comes out total degree 7, which is impossible for the true tower.** The parity factors
`(t∓1)` live in the height-0 Cartan sector, of dimension exactly `n−1 = 5` (verified at n=3,4,5:
parity degree `= n−1`). The engine's `(t−1)²(t+1)^5` has **degree 7 = 5 + 2** — two spurious parity
factors. The corruption is visible across the degenerate even-k sector simultaneously:

| factor | engine n=6 | θ candidate | Sym candidate | comment |
|---|---|---|---|---|
| `(t-1)` | 2 | 3 | 2 | |
| `(t+1)` | **5** | 2 | 3 | **over by ≥2** (parity degree 7 > 5) |
| `char(M^2)` (`a₂`) | **4** | 2 | 3 | **inflated** |
| `char(M^3)` (`a₃`) | **1** | 2 | 2 | the known degenerate **under-count** (= B66) |

This is the **defective ε→0 least-squares limit at the degenerate even-k collision** — the same
pathology Phase A documented at n=5 (where `(t+1)²` was *under*-counted to 1 and `char(M²)²` to 1,
leaving a defective cubic). At n=6 the degeneracy is worse (more colliding even-k blocks), and the
tagger *over*-assigns the defective/gauge modes into spurious `(t+1)` and an inflated `char(M²)=4`,
while `char(M³)` still under-counts to 1. **The even-k / parity sector is not clean** — so the engine
cannot decide θ vs Sym on the parity.

**The Task-B premise is refuted for n=6.** The parity `(t±1)` was assumed separable from the
degenerate even-k blocks the engine mis-counts. It is **not**: at n=6 the parity multiplicities are
themselves ≥2 (degenerate) and sit in the same defective even-k sector as `char(M²)²`, exactly as the
n=5 `(t+1)²` did. The engine is reliable for the parity only when the parity is non-degenerate or
isolated (n=4's `(t−1)²` resolved); at n=6 it is neither.

## The one weak, explicitly-non-decisive observation

If one assumes the *minimal-corruption* reading — that the spurious modes inflate only `(t+1)` (and
`char(M²)`), leaving `(t−1)` clean — then `(t−1)=2` would be the true count, giving true parity
`(t−1)²(t+1)^{5−2}=(t−1)²(t+1)³` = **Sym's** split, not θ's. This is weakly consistent with the n=5
precedent, where the `(t−1)` sub-count resolved correctly (2=truth) while `(t+1)` was the corrupted
one. **But this is a fragile inference from a demonstrably corrupted run (parity degree 7), not an
adjudication** — the `(t−1)=2` count has no independent guarantee of cleanliness, and "only `(t+1)`
is wrong" is an assumption. Reported plainly per the handoff ("if it comes out Sym's split, that's
surprising — report it plainly"): the engine's least-corrupted sub-count leans **Sym, not θ** — which
is *surprising* against the Task-A expectation that θ's Lie-theory parity is the better-grounded one.
It does **not** settle the parity either way.

## Verdict

**INCONCLUSIVE.** The F_p engine resolves at n=6 (with `maxlen=6`, prime-stable, L-converged) but the
even-k/parity sector is corrupted (parity degree 7 > Cartan dimension 5; `char(M²)=4` inflated,
`char(M³)=1` under-counted). It does **not** adjudicate θ's `(t−1)³(t+1)²` vs Sym's `(t−1)²(t+1)³`.
The only sub-signal (`(t−1)=2`) weakly favors **Sym**, contrary to expectation, but is not reliable.
The parity question stays **OPEN**, alongside `a₃(n=6)`. Settling either still needs a
degeneracy-aware exact limit or the trace-ring proof (B58 proper) — the engine's pinv-limit is the
construction that fails at exactly these degenerate collisions (V24). Proven core untouched; nothing
committed.

# Smooth fixed-line point test — the idea FAILS (honest negative)

**Date:** 2026-06-04. Exploratory, uncommitted. Proven core untouched. This tests the
"compute `a_d` at a smooth fixed-line point `c≠n` to dodge the trivial-rep pinv degeneracy" idea
(my suggestion #1). **Verdict: refuted by a cheap SL(3) computation. Recording it as a closed door.**

## The idea (and why it seemed good)

Phase A showed the numerical rep-perturbation pinv **under-counts** the degenerate `char(M²)²` at the
trivial rep (SL(5): gave `a₂=1`, truth `2`). The trivial rep is a *singular* point of the variety,
which is *why* the pinv fails there. Idea: the fixed line is a 1-parameter family (B54/B55's `c`);
compute the Jacobian at a **smooth** point `c≠n`, where the pinv is well-conditioned, and read the
tower cleanly. It seemed to sidestep both the pinv **and** the trace ring.

## The test (cheap, decisive) — B54's symbolic `J(m,c)` for SL(3)

B54 already builds the SL(3) fixed-line Jacobian `J(m,c)` **symbolically in `c`** (rep-free, from the
derivative-sequence recurrence — *no pinv*). Factoring its characteristic polynomial:

```
char(J(m=1, c)) = (t−1)(t+1) · (t²−c t+1) · (t⁴ − c t³ − 2c t² + c t + 1)
```

specialized:

| c | factorization | is it the tower? |
|---|---|---|
| **3 = n (trivial rep)** | `(t−1)(t+1)·(t²−4t−1)·(t²−3t+1)·(t²+t−1)` = `(t∓1)·char(M³)·char(M²)·char(M⁻¹)` | **YES** |
| 1 | `(t−1)²(t+1)²·(t²−t−1)·(t²−t+1)` = parity²·`char(M)`·Eisenstein | no |
| 2 | `(t−1)³(t+1)·(irreducible quartic)` | no |
| 0 | `(t−1)(t+1)·Φ₄·Φ₈` | no |

## Why it fails (the clean statement)

The eigenvalues are **strongly `c`-dependent**, and the **Dickson tower is specifically a `c=n`
phenomenon**: at `c=n` the generic-irreducible factors *split* into Dickson quadratics (the
`char(M³)·char(M⁻¹)` pair is a *single irreducible quartic* `t⁴−ct³−2ct²+ct+1` at general `c`,
splitting only at `c=3`). So the trivial rep `c=n` is the **special, maximally-split point** — and
it is *simultaneously* the singular point (where the pinv degenerates) **and the only point on the
fixed line where the tower exists**. You cannot move to a smooth `c≠n` without changing the
eigenvalues and losing the tower. The degenerate `char(M²)²` (SL(5)) is, by the same mechanism, a
quartic that becomes a *perfect square* only at `c=n` — not separable into two readable factors at
smooth `c`. **The idea is refuted.**

## What the test DID reveal (the redirect)

The under-count is an artifact of the **numerical** rep-perturbation pinv — B54's **symbolic,
rep-free, recurrence-based** `J(m,c)` has *no* pinv and gives the tower correctly at `c=n` for SL(3).
So the honest route to a rigorous `a₂(SL5)=2` is to **extend B54's symbolic recurrence construction
to SL(5) at `c=n`** (depth-5 CH recurrence; the `e_j(c)` forcing is expressible via Newton in the
fundamental power-trace differentials — no separate `Λ²` representation needed for that piece).

**But this is not a shortcut.** B64/B65 already established that the SL(n≥4) symbolic construction
hits the genuine obstruction that single-block traces span only part of the coordinate space (SL(4):
12/15) — the substituted-word images `tr((AᵐB)^k)` require **two-block words** `tr(Aᵢ B Aⱼ B …)`
whose derivative sequences the single-matrix recurrence does not capture. That two-block closure is
exactly **B58 proper / the ambient trace ring** — and it is `c`-independent, so the smooth-`c`
detour does not avoid it.

## Bottom line (honest)

- **My smooth-point idea does not settle `a₂(SL5)=2`.** The cheap SL(3) test refutes its premise
  (the tower is `c=n`-specific; eigenvalues move with `c`). I should not have pitched it as confidently
  as I did — and the value here is that one symbolic factorization closed it before any multi-session
  build.
- **`a₂(SL5)=2` remains settled only structurally (B62).** No direct computation has confirmed it:
  the numerical pinv under-counts to `a₂=1`; B61 assigned the 2nd `char(M²)` via B62's opposition
  involution, not by computing it. The only routes to a *computed* `a₂=2` are (i) B58 proper (the
  two-block trace ring, hard, `c`-independent) or (ii) a degeneracy-aware exact pinv-limit — neither
  cheap.
- This sharpens the strategic fork rather than resolving it: there is **no cheap computational
  shortcut** to the contested multiplicity. It is B62-structural (a candidate, per `CANDIDATE_A_D.md`)
  vs the B58-proper proof — exactly the held decision.

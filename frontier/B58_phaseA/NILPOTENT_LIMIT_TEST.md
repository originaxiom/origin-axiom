# Nilpotent-limit SL(4) gate — does the c=n nilpotent picture derive B65, or stall at e₂?

**Date:** 2026-06-04. **Status:** exploratory, **uncommitted**. Proven core P1–P16 untouched.
`m=1`; `M=[[1,1],[1,0]]`. Script: `frontier/B58_phaseA/nilpotent_limit_test.py` (exact sympy).

**The mechanism under test (a candidate B58-proof STORY, not a result).** At the trivial
representation `c=n` (the only point where the tower lives, per `SMOOTH_POINT_TEST.md`) the
Cayley–Hamilton recursion governing the fixed-line derivative sequences is **nilpotent** —
characteristic polynomial `(r−1)^n`, all eigenvalues 1. The story: nilpotency forces the derivative
sequences to be **polynomials in word-length `k` of degree ≤ n−1**, and the Dickson factors
`char(±M^k)` are the polynomial eigenfunctions of that recursion. Verified end-to-end at SL(3)
(B64), never tested past it. **The gate (derive, do not fit): does this mechanism reproduce B65's
exact SL(4) factorization — `a_d=(1,1,1,1)`, `b_2=1`, parity `(t−1)²(t+1)` — from the
nilpotent/polynomial structure WITHOUT using the known answer, or does it stall at the
`e₂=tr(Λ²A)` two-block sector?**

**Verdict up front: STALLS at the `e₂`/Λ² two-block sector** — the anticipated outcome, now made
precise. The nilpotent/polynomial mechanism generates the single-index derivative sequences (the
12/15 single-block coordinate rows) but **cannot** generate the 3 remaining rows: their substitution
images are two-block words `tr(A^a B A^b B)` whose fixed-line Hessian is a genuinely **two-index**
object (a non-separable `a·b·tr(X²)` coupling), which no single-index `(r−1)^d` recursion produces.
So the picture is a **prettier description of the single-block part, not a proof across the barrier**
that B64/B65 already localized. It is a **CANDIDATE**, not a derivation.

---

## Step 1 — explicit CH recursion at c=n=4, nilpotency

The forward-chain Cayley–Hamilton recursion at the identity representation (all traces `= n`):
```
   tau_k = 4 tau_{k-1} - 6 tau_{k-2} + 4 tau_{k-3} - tau_{k-4}
   char poly of the recursion operator = r^4 - 4r^3 + 6r^2 - 4r + 1 = (r-1)^4   [verified]
```
All eigenvalues are 1 — **nilpotent**. General `n`: the recursion char poly is `(r−1)^n` (verified
n=3,4,5,6), the depth-`n` CH relation at `c=n`. This is the part of the SL(n) story that clearly
generalizes (the `(r−1)^3` SL(3) case is B55/B64; `(r−1)^4` SL(4) is B58_sl4_tower_test).

## Step 2 — derivative sequences are degree ≤ n−1 polynomials; the eigenfunctions

The homogeneous solution space of `(r−1)^n` acting on sequences is
`span{ C(k,0), C(k,1), …, C(k,n−1) }` (degree ≤ n−1) — these binomials **are** the polynomial
eigenfunctions of the nilpotent recursion. Re-deriving B64's SL(4) depth-4 sequences here (no
import): the four **seed** sequences are degree ≤ 3 = n−1, the three **forced** sequences (`e1, e2,
e3`) degree ≤ 4. So the fixed-line derivative sequences are polynomials in `k`, exactly as the
mechanism requires.

**Positive control — the single-block mechanism already closes at SL(3) (B64/V15, established).**
B64's `sl3_jacobian()` builds
the full 8×8 SL(3) fixed-line Jacobian purely from these degree-≤2 sequences sampled at the image
indices `m, m±1` and the exchange involution — **no fitting** — and it factors **exactly** into
`(t−1)(t+1)·char(M²)` (symmetric) and `char(M⁻¹)·char(M³)` (antisymmetric), the full SL(3) tower.
That is a genuine derivation; it works at SL(3) because **every** SL(3) coordinate is a single-block
fundamental trace (`tr A, tr B, tr AB` and inverses; `Λ²V ≅ V*` for SL(3), so even `tr(Λ²A)=tr(A⁻¹)`
is single-block). The question is whether this survives to SL(4), where it does not.

## Step 3 (THE GATE) — does the mechanism cross the e₂ / Λ² two-block sector?

**The recorded barrier (B65 rank check).** Single-block `V` + `Λ²` traces span only **12 of 15**
SL(4) character-variety dimensions; the 3 remaining dimensions need genuine **mixed two-block** words
(`tr(A^a B A^b B …)`). This is exactly where B58 is open.

**The decisive test (exact sympy, generic traceless tangents `X` in A, `Y` in B; reps `A=I+εX`,
`B=I+εY` at the `c=4` fixed line).** Is the fixed-line Hessian (the `ε²` coefficient of `tr(word)`)
a single-index nilpotent polynomial (reachable) or a genuinely two-index object (not reachable)?

| word | fixed-line Hessian (`ε²` coeff) | index structure | reachable? |
|---|---|---|---|
| `tr(A^k B)` (single-block fundamental) | degree-2 polynomial in `k` | **one index** `k` | **yes** — the `(r−1)^4` recursion generates it |
| `tr(Λ²(A^m B)) = tr((Λ²A)^m (Λ²B))` (single-block in the 6-dim Λ²) | one-index, depth-6 `(r−1)^6` | **one index** `m` | **yes** — Λ² is still single-block |
| `tr(A^a B A^b B)` (two-block; the e₂ even-k substitution image) | contains `a·b·tr(X²)` (verified: the `a·b` coefficient `= tr(X²)` exactly; the non-separable part `h(a,b)−h(a,0)−h(0,b)+h(0,0) = a·b·tr(X²)`) | **two indices** `a,b`, non-separable | **NO** |

The two-block word carries a **bilinear `a·b·tr(X²)` coupling** between its two blocks. A single-index
recursion produces sequences in **one** index; no `(r−1)^d` recursion — fundamental (`d=4`) or
exterior-square (`d=6`) — generates a bilinear `a·b` sequence. **This is the precise stall.** The
obstruction is **not** Λ² per se (single-block Λ² traces are one-index and reachable); it is
specifically the **two-block words** `tr(A^a B A^b B)` that the `e₂` even-k rows require under the
substitution `σ` (`m=1`: `tr(A²) ↦ tr((AB)²) = tr(ABAB)`; general `m`: `tr((A^m B)²) = tr(A^m B A^m
B)`, the two-block word with two independent index slots).

### Gate verdict — **STALLS at the e₂ / Λ² two-block sector**

- The nilpotent/polynomial mechanism **derives** the single-index derivative sequences → the 12/15
  single-block (V depth-4 + Λ² depth-6) coordinate rows, and — as the SL(3) positive control shows —
  produces clean Dickson factors where every coordinate is single-block.
- It **cannot derive** the 3 remaining SL(4) rows: their substitution images are two-block words with
  a non-separable two-index Hessian, outside the reach of any single-index recursion.
- Therefore it does **not** reproduce B65's full 15-factor char poly from the mechanism alone. It is
  a **prettier description of the single-block part**, not a proof across the barrier — and it stalls
  at **exactly** the `e₂=tr(Λ²A)` two-block sector that B64 localized and B65 quantified (12/15). The
  new content here is naming the barrier precisely: it is the **two-index (bilinear `a·b`) coupling**
  of the two-block words, which the nilpotent single-index recursion structurally cannot generate.

This is gate outcome **"stalls at e₂"** (the brief's anticipated likely outcome), not "derives B65"
and not "cannot be made precise." The mechanism was made precise enough to apply at SL(4); applied,
it stalls at the genuine barrier.

---

## What this does and does NOT establish

- **Does NOT** establish a derivation, a proof, or "Steps 1–3 established." The mechanism is a
  **CANDIDATE**: it reproduced only what was already understood (the single-block factors, and the
  full SL(3) tower) and stalled exactly where every prior route stalled (the two-block `e₂` sector).
  It did **not** derive an answer it did not already know — the SL(4) gate it had to clear.
- **Does** sharpen the open problem: the B58 barrier is precisely the **two-index bilinear coupling**
  of the two-block trace words at the fixed line. Any genuine SL(n) proof must produce these
  two-block derivative sequences — which the nilpotent single-index recursion does not.
- The nilpotency and degree-≤(n−1) polynomial facts (Step 1, Step 2) are solid and general; they are
  the *correct single-block half* of the picture, not the whole.

**Bottom line.** Nilpotent c=n + polynomial derivative sequences is a real and pretty description of
the **single-block** sector (and a full derivation at SL(3), where everything is single-block), but
it **stalls at the e₂/Λ² two-block sector at SL(4)** — the two-index bilinear coupling no single-index
recursion generates. A candidate mechanism, not a proof. **Stop for review.** Proven core untouched;
nothing committed.

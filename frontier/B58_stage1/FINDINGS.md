# B58 Stage 1 — findings (excess map + Sym^{2k} diagnostic)

**Date:** 2026-06-03. **Status:** exploratory, **uncommitted** (no commit/PR/ledger). Proven
core P1–P16 untouched. The 2026 arXiv IDs in the literature pull were confirmed to resolve
(Ishibashi–Mizuno 2603.00816 verified by independent search; Kozai 1509.07487 / 2411.04431
pre-2026, fetched).

## Headline: the brief's cotangent-dimension premise is REFUTED (the flagged Đoković cross-check)

The cotangent spectrum (`dσ` on `m/m²` of the two-traceless-matrix trace algebra, graded by
degree, decomposed into `char(±M^k)`) was computed **exactly over F_p** (modular — no rational
blow-up), prime-stable, and **validated against the published minimal-generator counts**:

| n | cotangent dim (this work) | Teranishi/Đoković (traceless) | brief's `3n²−10n+11` | Jacobian `n²−1` | **excess** | brief's `2(n−2)(n−3)` |
|---|---|---|---|---|---|---|
| 3 | **9** (prime-stable) | 9 (Teranishi 11 − 2) | 8 ✗ | 8 | **1** | 0 ✗ |
| 4 | **30** (prime-stable, 3 primes) | 30 (Đoković 32 − 2) | 19 ✗ | 15 | **15** | 4 ✗ |
| 5 | **≥111** (PARTIAL: deg≤11, 1 prime) | (Đoković, not pulled; clearly >111) | 36 ✗ | 24 | **≥87** | 12 ✗ |

**n=5 caveat:** best-effort only — `Lmax=11`, single prime, `K=1100`. The per-degree generator
count is still *rising* at the top degree (deg-11 contributes 24 dims), so 111 is a **lower bound**,
not the full count (more generators live at degrees 12–~14, and `K=1100` may under-count the
top degrees). It is not prime-stability-verified. Even so it refutes the brief's 36 by a wide
margin and confirms the excess explodes. The *full* n=5 count needs cyclic-word/Procesi
reduction (brute-force `2^d` words to degree ~14 is memory-infeasible) — i.e. the hand-proof
machinery, not this route.

The per-degree generator counts reproduce Đoković's distribution **exactly** for n=4
(deg 2..10 = 3,4,6,2,4,2,4,4,1 = 30; the deg-10 generator needs `K≥600` to surface — `K=300`
under-counts it, mirroring the brief's truncation warning but from the sample-count side).

So **`3n²−10n+11` and `2(n−2)(n−3)` are both wrong**, and the cotangent does **not** equal the
Jacobian even at n=3 (9 ≠ 8). The cotangent is the genuine Teranishi/Đoković minimal-generator
count, which has no elementary closed form (it comes from the Poincaré series). This is exactly
the discrepancy the brief said to flag, not paper over.

## (a) Does the excess follow a clean n-indexed rule?

**No clean rule, and it is much LARGER than anticipated.** The excess (cotangent minus the
`(n²−1)` Jacobian tower) is:

```
n=3:  dim 1   =  (t+1)                                           [deg-6 generator det[X,Y] ~ tr([X,Y]^3)]
n=4:  dim 15  =  char(M^-1) char(M^1) char(M^2) char(-M^2) char(-M^3) (t-1)^2 (t+1)^3
n=5:  dim>=87 =  char(M^-1)^10 char(M^1)^5 char(M^2)^6 char(M^3)^5 char(M^4) char(-M^2)^3
                 char(-M^3)^3 char(-M^4)^2 char(-M^5) (t-1)^5 (t+1)^10     [PARTIAL, deg<=11]
```

The excess is **a mix of many char(±M^k) and parity factors**, not a single clean Dickson block,
and grows fast: **1 → 15 → ≥87** (vs the brief's `2(n−2)(n−3) = 0, 4, 12`, refuted at all three n).
Per hygiene flag 3 the growth is super-linear and irregular — **no clean n-indexed rule** (and the
n=5 figure is a partial lower bound, so no rule is or should be declared). The qualitative verdict
below holds across n=3,4,5.

**Structural note on the n=3 excess:** the lone excess factor is the degree-6 generator
`det[X,Y] = tr([X,Y]^3)/3` (σ-eigenvalue −1, since `[X,Y]→−[X,Y]` under σ ⇒ `det→−det`), which is
Teranishi's 11th generator. It is NOT in the `(n²−1)` Jacobian, hence excess even at n=3.

## (b) Sym^{2k} (principal-SL(2)/Kostant) diagnostic — confirmed NEGATIVE (kill #25, multiplicity side)

`sl(n)=⊕_{k=1}^{n-1} Sym^{2k}` with M acting:
- **bare Kostant** = even powers only, overshooting to `char(M^{2(n-1)})` (M⁴/M⁶/M⁸…);
- **coupled** (⊗ the `H¹(F₂)=C²` factor) = odd powers only, to `char(M^{2(n-1)+1})`.

Both confirmed exactly against the predictions for n=3,4,5 (`sym2k_diagnostic.json`). **Neither
equals the tower** (which has both parities, powers capped at `M^n`, and the open multiplicities).
So the symmetric-power coefficient decomposition does NOT reproduce the tower — re-confirming
kill #25 from the multiplicity side. B64's parity split (even-k ↔ symmetric, odd-k ↔ coupled) is
a *sorting*, not a *formula*.

## (c) Đoković reconciliation

The cotangent dims **match Teranishi (n=3: 9)** and **Đoković (n=4: 30)** exactly, including the
degree distribution — so the F_p `m/m²` machinery is correct. The brief's `3n²−10n+11` is simply
the wrong count (it appears to omit the higher-degree generators: the deg-6 at n=3, and deg 4–10
generators at n=4). Reference: Teranishi 1986 (eleven generators of two 3×3 matrices); Đoković,
*Generators of invariants of two 4×4 matrices* (arXiv:math/0503146) and *Poincaré series …*
(arXiv:math/0609262).

## Verdict / what this unlocks

**The cotangent (singular trace-ring) route does NOT cleanly yield `a_d`.** The cotangent is the
full Teranishi/Đoković generator spectrum; the Jacobian `a_d`/`b_d` sit inside it but are swamped
by a large, mixed **excess** (1 at n=3, 15 at n=4) with no elementary structure. This is the
brief's anticipated "irregular/large excess ⇒ the cotangent route does not cleanly yield `a_d`,
and only the hand proof (exterior-power Cayley–Hamilton recursion) will." The Step-2 result says
the same from the other side: the principal-SL(2)/symmetric-power decomposition is a sorting, not
the multiplicity formula. **Recommendation: pursue the exterior-power CH recursion (the hand
proof / Λ²V multi-block trace ring, B58 proper) for `a_d`; the cotangent route is a dead end for
the multiplicities, though it is now exactly characterized and Đoković-validated.**

## Files
- `cotangent_spectrum.json` — per n: cotangent dim, per-degree factor lists, full multiset,
  excess multiset, prime-stability, Teranishi/Đoković cross-check, brief-formula discrepancy.
- `sym2k_diagnostic.json` — bare/coupled Sym^{2k} spectra + the predicted-negative verdict.
- `step1_cotangent.py`, `step2_sym2k.py` — the probes (modular F_p; exact sympy).

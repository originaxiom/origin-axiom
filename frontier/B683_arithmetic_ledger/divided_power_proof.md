# B683 cell L1 — THE DIVIDED-POWER LAW: EQUALITY (NON-CANCELLATION) PROVED FOR ALL n

Status: **THEOREM proved for all n** (not a bound + subsequence). Every step is
elementary p-adic; the mechanism is verified term-by-term in
`verify_divided_power.py` to n = 400 (banked prior evidence was numeric to
n = 120).

## Statement

Let `(q;q)_inf = prod_{k>=1}(1 - q^k)` and expand the carrier
```
    (q;q)_inf^{-3/5} = sum_{n>=0} c_n q^n ,   c_n in Q .
```
**Theorem.** For every n >= 0,
```
    v5(c_n) = -( n + v5(n!) )   exactly,
```
equivalently the 5-part of the denominator of c_n is exactly
`5^{ n + v5(n!) }` with `v5(n!) = (n - s5(n))/4` (Legendre, p = 5). The
leading 5-adic term never cancels; there is no proper subsequence on which
the valuation exceeds this — the equality is uniform in n.

This is the B681 "divided-power law" `v5(den c_n) = v5(5^n n!)`, now proved
for ALL n by a strict-dominance (ultrametric) argument, closing the OPEN item.

## Set-up

Write `g = (q;q)_inf`. By the pentagonal number theorem
`g = 1 - q - q^2 + q^5 + q^7 - ...`, so `g in 1 + q*Z[[q]]` with
`[q^1] g = -1`. Put `h = g - 1 in q*Z[[q]]`; its lowest term is `-q`.

The formal power `g^{-3/5} := exp(-(3/5) log(1+h))` equals the binomial series
```
    g^{-3/5} = sum_{m>=0} C(m) h^m ,   C(m) := binom(-3/5, m) .          (1)
```
Because `h in q*Z[[q]]` we have `h^m in q^m * Z[[q]]`, so (1) is q-adically
summable and, for each fixed n,
```
    c_n = sum_{m=0}^{n} C(m) * b_{n,m} ,   b_{n,m} := [q^n] h^m in Z .   (2)
```
For n >= 1 the m = 0 term vanishes, so the sum runs 1 <= m <= n.

## Four lemmas

**(A) The binomial factor has exact valuation `-(m + v5(m!))`.**
```
    C(m) = (1/m!) * prod_{j=0}^{m-1} (-3/5 - j)
         = (1/m!) * (1/5^m) * prod_{j=0}^{m-1} (-3 - 5 j) .
```
Each factor `-3 - 5j ≡ -3 ≡ 2 (mod 5)` is a 5-adic **unit**, so
`v5( prod_j (-3-5j) ) = 0`. Hence
```
    v5( C(m) ) = 0 - m - v5(m!) = -( m + v5(m!) ) .                      (A)
```
(The only property of the exponent used is `-3/5` with numerator `3` coprime
to 5; any `-a/5`, `5 ∤ a`, gives the same law.)

**(B) The coefficients `b_{n,m}` are integers.** `g in Z[[q]]` ⇒ `h in Z[[q]]`
⇒ `h^m in Z[[q]]` ⇒ `b_{n,m} in Z`, so `v5(b_{n,m}) >= 0`.

**(C) The diagonal is a unit: `b_{n,n} = (-1)^n`.** Since `h = -q + O(q^2)`,
`h^n = (-q)^n(1 + O(q))^n = (-1)^n q^n + O(q^{n+1})`, so `[q^n] h^n = (-1)^n`,
a 5-adic unit: `v5(b_{n,n}) = 0`.

**(D) `phi(m) := m + v5(m!)` is strictly increasing.** `v5(m!)` is
non-decreasing and `m` is strictly increasing, and precisely
`phi(m) - phi(m-1) = 1 + v5(m) >= 1`.

## The proof (strict 5-adic dominance)

Write the n-th coefficient as the finite sum `c_n = sum_{m=1}^{n} T_m`,
`T_m = C(m) b_{n,m}`. Combine (A) and (B):
```
    v5(T_m) = -( m + v5(m!) ) + v5(b_{n,m}) >= -phi(m)  for every m .     (3)
```
The **diagonal term** m = n is pinned exactly by (A)+(C):
```
    v5(T_n) = -phi(n) + v5(b_{n,n}) = -phi(n) .                           (4)
```
For every **off-diagonal** m with 1 <= m <= n-1, monotonicity (D) gives
`phi(m) <= phi(n-1) = phi(n) - 1 - v5(n) <= phi(n) - 1`, so by (3)
```
    v5(T_m) >= -phi(m) >= -phi(n) + 1 > -phi(n) = v5(T_n) .               (5)
```
Thus `T_n` is the **unique** term of minimal 5-adic valuation, and it beats
every other term by at least a full unit (>= 1) of valuation. The
ultrametric strict-minimum principle (`v5(x+y) = min` when the mins are
distinct, applied to the finite sum) yields
```
    v5(c_n) = min_m v5(T_m) = v5(T_n) = -phi(n) = -( n + v5(n!) ) .   ∎
```
No cancellation is possible: the leading contribution sits strictly below
the entire rest of the sum in the 5-adic metric.

## Why the earlier "hardness" dissolves

The apparent difficulty was reading `c_n` as an alternating sum over
`sigma_{-1}`/plethystic pieces where cancellation is generic. The binomial
form (2) reorganizes the SAME series so that (i) all arithmetic weight lives
in the exactly-computable factors `C(m)` (Lemma A), (ii) the combinatorial
factors `b_{n,m}` are integers hence 5-adically harmless (Lemma B), and
(iii) the extreme term is a unit on the diagonal (Lemma C). The `3/5`
supplies the `5^{-m}` per grade; `exp` / divided powers supply the `1/m!`;
their product's valuation is monotone (Lemma D), which is exactly the
non-archimedean condition that forbids cancellation. B681's decomposition
`v5 = 5^n * n!` is recovered as `phi(n) = n + v5(n!)` with the two summands
being the `5^{-m}` (one factor of 5 per grade) and the divided-power `1/m!`.

## Residual gap

**None for this carrier.** The equality is proved for all n unconditionally.
Scope notes (honest boundaries, not gaps in the theorem):
- The argument is specific to `p = 5` acting on exponent `-3/5`; the only
  input is `5 ∤ 3`. It transfers verbatim to `(q;q)_inf^{-a/p}` with
  `p ∤ a` (each numerator factor `-a - p j ≡ -a` is a unit), giving
  `v5→vp`, `v5(c_n) = -(n + vp(n!))`. Recorded as an immediate corollary,
  not needed for L1.
- If the exponent's numerator were divisible by p the unit argument in (A)
  fails and the law changes; not our case.

## Numerical corroboration (verify-don't-trust)

`verify_divided_power.py` independently (a) builds `g` and `f = g^{-3/5}` by
the J.C.P. Miller recurrence over exact Fractions, (b) checks (A) for m<=200,
(B) integrality, (C) the unit diagonal, (D) monotonicity, (e) that the
binomial series (2) reconstructs `f` exactly, and (f) the final equality
`v5(den c_n) = n + v5(n!)` for 1 <= n <= 400 — PASS, and reproduces the five
banked witnesses n = 1,10,40,80,119 → 1,12,49,99,146.

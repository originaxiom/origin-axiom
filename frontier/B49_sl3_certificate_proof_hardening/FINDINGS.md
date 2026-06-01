# B49 -- Findings

> Logged proof-hardening work, not a promoted theorem.

## Result

B49 turns the PC12 fixed-line splitting classification into a proof architecture
with explicit modules:

```text
1. universal splitting criterion
2. direct split families
3. square-gap propagation lemma
4. finite nonnegative strip exclusions
5. negative strip and boundary exclusions
```

The key criterion is:

```text
chi(t)=t^4-A t^3+C t^2+A t+1
```

splits as

```text
(t^2-alpha t-1)(t^2-beta t-1)
```

with `alpha,beta in Z` iff

```text
D=A^2-4(C+2)
```

is a square and `A+sqrt(D)` is even.

## Square-Gap Mechanism

Most exclusions reduce to trapping `D` between consecutive squares:

```text
R^2 < D < (R+1)^2
```

The reusable propagation step is:

```text
W_{n+2}=q W_{n+1}-W_n, q>=2
0<W_n<=W_{n+1}
=> 0<W_{n+1}<=W_{n+2}
```

because

```text
W_{n+2}-W_{n+1}=(q-2)W_{n+1}+(W_{n+1}-W_n) >= 0.
```

Once the third differences propagate, positivity climbs back through second
differences, first differences, and the gaps.

## What B49 Certifies

The probe checks the finite proof tables for:

```text
4 <= c <= 14
-11 <= c <= -2
```

including the boundary split `c=-11,m=1` and the isolated negative splits:

```text
(c,m)=(-9,1), (-3,2), (-3,3)
```

It also checks the direct families:

```text
c=1,3
c=0 iff 3|m
c=2 iff 6|m
c=-1 iff 2|m
```

## Remaining Proof Work

B49 narrows the remaining work to prose and global range hardening:

```text
write the universal criterion cleanly
derive the fixed-line quartic coefficients in the manuscript notation
write the square-gap propagation lemma once
present finite strip tables compactly
write the large c>=15 and c<=-12 coefficient-positivity exclusions cleanly
keep the certificate runner as reproducibility support, not the only proof
```

## Verdict

```text
NEEDS_VALIDATION
```

PC12 is stronger after B49: the proof architecture is now explicit and partly
machine-checked. It is still not promoted to a proven claim or marked draftable.

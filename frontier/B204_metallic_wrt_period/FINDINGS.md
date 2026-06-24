# B204 — the WRT level-period law for once-punctured-torus bundles (metallic = the diagonal)

**Date:** 2026-06-24. **Status:** a clean closed-form **level-period law**, established numerically by
predict-then-confirm on 21 `(a,b)` cells + 12 metallic `m` (all fundamental periods), with the analytic
mechanism identified (Gauss-sum reciprocity). Pins the live Path-A metallic period question — and shows the
metallic law is the diagonal of a law for **all** once-punctured-torus bundles. Standalone quantum-topology /
arithmetic; **no physics; nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V197**.

## The object

The SU(2)_k Reshetikhin–Turaev (Witten) modular trace of the bundle whose monodromy is
`gamma = R^a L^b = [[1+ab, a],[b, 1]]` (`R=[[1,1],[0,1]]`, `L=[[1,0],[1,1]]`; metallic family `a=b=m`,
i.e. `R^m L^m`, with `m=1` the figure-eight knot complement):

```
Z(a,b;k) = tr( rho_k(R^a L^b) ) = tr( T^a S T^-b S^-1 )           [ (S T^-1 S^-1)^b telescopes ]
         = sum_{i,j=0}^{k} exp(2 pi i (a h_i - b h_j)) S_{ij}^2,
  S_{ij} = sqrt(2/n) sin(pi (i+1)(j+1)/n),  h_i = i(i+2)/(4n),  n = k+2.
```
The `c/24` framing cancels in the ratio (the word is balanced). Two independent code paths (the closed sum
form and the explicit matrix product `T^a S T^-b S^-1`) agree to 1e-9.

## The law

**General (all once-punctured-torus bundles `R^a L^b`):**
```
        per |Z(a,b)|  in the level k  =  lcm(a,b) * (4 + ab) / gcd(4 + ab, 4).
```
- `4 + ab = det(gamma + I)` — a homological invariant of the mapping torus (cf. `|det(gamma - I)| = ab =
  |Tor H_1|`). This is the dominant arithmetic factor.
- `lcm(a,b)` — the twist data of the word.
- `/ gcd(4+ab, 4)` — a 2-adic normalization (`=4` when `ab` is even, `=1` when `ab` is odd).

**Metallic diagonal `a=b=m`** (the live Path-A question, now pinned): `lcm(m,m)=m`, `4+m^2`, so
```
        P(m) = m (m^2 + 4) / gcd(m^2 + 4, 4).
```
`P(1..8) = 5, 4, 39, 20, 145, 60, 371, 136`. `m=1` reproduces chat1's **verified** figure-eight period-5
sequence `Z = {1, 0, -1/phi, 0, 1}` (a cyclic rotation of chat1's `{1,1,0,-1/phi,0}`).

**Real-vs-complex dichotomy (explains why the metallic family is special):** the substitution `p=i+1, q=j+1`
gives an overall constant phase `exp(-2 pi i (a-b)/(4n))` which is **1 iff a=b**. So for the metallic family
`Z` itself is real and periodic; for `a != b` only `|Z|` is periodic (`Z` is genuinely complex, its phase
winds with `n`).

## Verification (predict-then-confirm; verify-don't-trust)

| route | cells | result |
|---|---|---|
| direct scan (K=600), smallest period | metallic `m=1..6`, general 15 `(a,b)` | matches the closed form exactly |
| **held-out predict-then-confirm** | metallic `m=7,9,11,12` (P up to 1375); general `(4,5),(3,7),(5,6),(2,7),(4,6),(5,7)` (P up to 1365) | **all hold, all fundamental** |
| fundamentality | every banked cell | no proper divisor of the predicted P is a period |
| two code paths | `(a,b,k)` grid | sum form = matrix form to 1e-9 |

The earlier exploratory memo's "no clean law / period absent when `m^2+4` is prime" was a **search-bound
artifact** (the scan bound was below `m(m^2+4)`); `m=1` (disc 5, prime) has the smallest period, falsifying
the prime/composite split. Corrected here.

## Mechanism (why — a derivation sketch, not yet a full proof)

With `p=i+1, q=j+1` and `sin^2(pi pq/n) = 1/2 - 1/4(e^{2 pi i pq/n} + e^{-2 pi i pq/n})`, the double sum
factors into **products of quadratic Gauss sums** `G(c, 4n) = sum_p e^{2 pi i c p^2/(4n)}` (with the `pq`
cross-term completed-square into a shifted Gauss sum). The level-period of such Gauss-sum products under
quadratic (Landsberg–Schaar) reciprocity is what produces the discriminant factor `4+ab` and the modulus
`lcm(a,b)`. A full reciprocity proof of the exact period (incl. the partial-range `p=1..n-1` truncation) is
the remaining step — **open / likely a known-techniques computation** (see novelty).

## Novelty (UNCHECKED — flagged for a prior-art pass)

That WRT/RT invariants of torus bundles are Gauss sums is **known** (Jeffrey 1992; Garoufalidis;
Hikami) — so the *mechanism* is standard. Whether the explicit closed-form **level-period as a function of
the monodromy word** `lcm(a,b)(4+ab)/gcd(4+ab,4)` is recorded, or new, is **not yet checked**. Tiered:
law `[num, strongly confirmed]`; mechanism `[Gauss-sum reduction, sketch]`; exact-period proof + novelty
`[NEEDS prior-art / specialist]`. Do not promote until checked.

## Firewall
Standalone quantum-topology / low-dimensional-topology arithmetic. No physics; no Λ/scale/spectral-mass; no
gauge content; nothing to `CLAIMS.md`; P1–P16 untouched (K010 form-side).

## Reproduction
- `python period_law.py` — self-check (sum vs matrix), the `m=1` anchor, the metallic law `m=1..8`, the
  general law on a spread of `(a,b)` incl. large held-out cells. ~2s, numpy only.
- `tests/test_b204_metallic_wrt_period.py` (pyenv, numpy-only) — 5 locks incl. the real-vs-complex
  dichotomy. 5 passed.

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

## Mechanism — PROVED: periodicity via Gauss-sum reciprocity (see `PROOF.md`)

The qualitative theorem is now **proved**: `|Z(a,b;n)|` is exactly periodic in the level despite the matrix
dimension `n−1` growing. Sketch (full argument + exact identities in `PROOF.md`, reproducer `gauss_proof.py`):
1. `sin^2(pi pq/n)` vanishes at `p,q in {0,n} (mod n)`, so the de-wound trace
   `Z̃(n)=Σ_{p,q=1}^{n-1} e^{iπ(ap²-bq²)/(2n)} sin²(πpq/n)` extends to a **full period** `0..2n-1` —
   giving clean Gauss sums with **no boundary corrections**.
2. Split `sin²`; the diagonal evaluates by **Landsberg–Schaar** to `(1/(2√(ab)))·G_a(n)G_b(n)*` (the `√(2n)`
   amplitudes exactly cancel the `1/(2n)` — *this* is why a growing-dimension trace stays bounded & periodic),
   and the cross term by **2D Gauss reciprocity** (binary form `det = −(4+ab) = −det(γ+I)`).
3. `G_a(n)` has period **exactly `a`** (take `s=1`), so `per(diagonal)=lcm(a,b)` — PROVED; the cross period
   `L_c` divides `4+ab`. Hence `|Z|` periodic with `P=lcm(lcm(a,b),L_c)`.

**Status:** periodicity PROVED; the diagonal factor `lcm(a,b)` PROVED; the exact period
`P=lcm(a,b)(4+ab)/gcd(4+ab,4)` **verified** (14 cells via the cheap dual sum), with a closed form for the
cross Gauss-sum period `L_c` (its 2-adic part) the **one remaining lemma** to reach `[proved]` for the exact
formula. Tier: `[periodicity proved; exact period one Gauss-sum-period lemma from closure]`.

## Novelty — CHECKED (adversarial deep-research, V199; see `NOVELTY.md`)

**The framework and the proof mechanism are KNOWN prior art — `Z_k=tr(ρ_k(A))` of a torus-bundle mapping
torus evaluated as a quadratic Gauss sum via reciprocity is exactly Jeffrey 1992 (CMP 147, Thm 4.1 / eq 4.8
for the hyperbolic case `|Tr|>2`); our Gauss-reciprocity proof re-derives her method.** The exact SU(2)_k
level-periodicity with a homology-set period is `PARTIALLY-KNOWN` (congruence subgroup property + Funar's
abelian `|Z_k|=|H¹(M;ℤ/k)|^{1/2}`). The explicit `(a,b)`-period and the metallic-reality are `APPEARS-NOVEL
but NEEDS-SPECIALIST` — at best a new corollary/specialization, very plausibly implicit in Jeffrey eq (4.8)
(which already carries **both** `|Tr∓2|` moduli, i.e. both `ab=det(A−I)` and `4+ab=det(A+I)`). Two prior-art
clusters (Coste–Gannon Galois / quantum-modular-forms; Hikami–Rozansky Gauss-sum evaluations) were NOT
retrieved → the novel verdicts are absence-of-evidence. **Do not claim novelty.**

**Framing correction (verified):** `Z_k=tr(ρ_k(R^a L^b))` with the closed-torus Kac–Peterson `S,T` is the WRT
invariant of the **closed-torus mapping torus** `M_{R^a L^b}` (a Sol 3-manifold; Turaev / Funar Lemma 3.2),
**not** the cusped once-punctured-torus bundle (figure-eight etc.). They share the monodromy `R^a L^b` but are
different 3-manifolds. The **monodromy family** is metallic `R^m L^m`; the **invariant** is the closed-torus
(Jeffrey) one. The period result is unaffected; only the topological label is corrected.

## Firewall
Standalone quantum-topology / low-dimensional-topology arithmetic. No physics; no Λ/scale/spectral-mass; no
gauge content; nothing to `CLAIMS.md`; P1–P16 untouched (K010 form-side).

## Reproduction
- `python period_law.py` — the numerical law: self-check (sum vs matrix), the `m=1` anchor, the metallic law
  `m=1..8`, the general law on a spread of `(a,b)` incl. large held-out cells. ~2s, numpy only.
- `python gauss_proof.py` — the **Gauss-sum reciprocity proof** reproducer (mpmath): the full-range/winding
  identity, the exact Landsberg–Schaar + 2D-reciprocity closed form, `per(diagonal)=lcm(a,b)`, and
  `lcm(per(diag),per(cross))=P` on 14 cells. ~1 min. See `PROOF.md`.
- `tests/test_b204_metallic_wrt_period.py` (pyenv) — 9 locks: the numerical law (5) + the proof identities (4:
  full-range/winding, the reciprocity closed form, diagonal period `=lcm(a,b)`, exact period `=P`). 9 passed.

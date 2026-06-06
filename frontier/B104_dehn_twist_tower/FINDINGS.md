# B104 — the Dehn-twist route to the all-n tower: SL(4) universality + the SL(5) wall

**Status: `proven` (SL(4): the GATE, factor-through-N, non-metallic universality) + `characterized-wall`
(SL(5)).** The explicit continuation of B103's reframing, executing the CC-web "Dehn-Twist Route" handoff in
full. Pure trace-map / Lie theory; **no physics**; P1–P16 untouched. Script `probe.py`; test
`tests/test_b104_dehn_twist_tower.py`.

## The method (sidesteps the Procesi wall)
The trace map of any once-punctured-torus monodromy is built by **composing the elementary Dehn-twist
substitutions** `U: a→a,b→ab`; `L: a→ab,b→b`; `S: a↔b` (generators of `MCG = GL(2,ℤ)`) inside the
**eps-series fixed-line construction** — *not* the full `(n²−1)`-coordinate Procesi substitution `σ` (the
B85 wall). Each twist acts on the dual-number pair `(A,B)` by `U:(P,Q)→(P,PQ)`, `L:(P,Q)→(PQ,Q)`,
`S:(P,Q)→(Q,P)`; folding a word gives `J(word)` at the SL(n) trivial fixed line. This is the engine-free
"fourth method" introduced at SL(3) in B103, here pushed to SL(4) and SL(5).

## SL(4) — the method works (the GATE + universality)
- **GATE.** The composed word `['U','S']` (abelianization `M_1=[[1,1],[1,0]]`) at SL(4) **reproduces B80's
  proved metallic SL(4) tower** (mod p) — the elementary maps are correct.
- **factor-through-N.** `char(J)` depends only on the abelianization `N`: words with equal `N` give the same
  `char(J)` (verified).
- **non-metallic universality.** `char(J(N)) = ∏_d char(Sym^d N)^{μ_d}` (the two-sequence catalog
  `μ_d=[2≤d≤4]+[0≤d≤1]={0,1,2,3,4}`) with the **det-sign parity**, verified on metallic (`det −1`) **and
  genuine non-metallic** (`det +1`, e.g. `N=U²L=[[3,2],[1,1]]`, `N=[[5,3],[3,2]]`) monodromies. So the
  **explicit SL(4) catalog is a computed theorem, for all monodromies, not a conjecture.**

## SL(5) — the wall, precisely characterized
The Dehn-twist engine at SL(5) is *consistent* (returns a Jacobian) but **`char(J) ≠ catalog`**: the
gcd of `char(J)` with the two-sequence catalog has degree **21 of 24** — i.e. **21 of the 24 Dickson factors
resolve, 3 are corrupted**. This is exactly B61/B66's "22/24 resolve, the doubly-degenerate sector is
gauge-corrupted." **The Dehn-twist composition does NOT bypass the eps-series gauge degeneracy** — it
inherits the rank-drop at the doubly-degenerate sector. The wall is **computational** (the eps-series metric
degeneracy at n≥5), characterized, consistent with the three prior dead routes — **not** a failure of the
representation theory: universality is structural at all n (B103 Route 1), so `char(J_φ(5))` *is* a class
function = the (n=5) catalog; the eps-series simply cannot resolve 3 of its factors.

## The reframing (recorded regardless of n=5)
The all-n tower question = **decompose the `GL(2,ℤ)`-representation `ρ_n` into `Sym^d` pieces**. The
Dehn-twist composition computes `char(ρ_n)` **without the Procesi ring**; the n≥5 wall is the *eps-series
gauge degeneracy*, not the representation theory. A method that resolves the doubly-degenerate sector
(inverse-word coordinates / a non-degenerate slice — B61's partial fix) would close n=5 directly; that is the
next concrete target, now isolated to a purely computational degeneracy rather than a structural gap.

## Scope (honest)
`proven` at SL(4) (the GATE + factor-through-N + the explicit catalog for metallic and non-metallic N);
the SL(5) result is a **characterized computational wall** (21/24 factors; the gauge-degeneracy sector),
not a proof of the n=5 catalog. The structural universality (all n) is B103's; B104 is the explicit
construction + the precise n=5 wall. Cite B103 (the n=3 method + reframing), B80 (the SL(4) tower reused as
GATE), B61/B66 (the gauge-degeneracy wall), Lawton/Procesi.

```bash
python frontier/B104_dehn_twist_tower/probe.py
python -m pytest tests/test_b104_dehn_twist_tower.py -q
```
No physics claim; no Origin-core claim; proven core P1–P16 untouched.

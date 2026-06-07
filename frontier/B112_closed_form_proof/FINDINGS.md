# B112 — PROOF of the opposition-involution closed form (the sign half of ρ_n), all n

> **⚠ STATUS RELABEL (B116/V103 + B117/V104 — three tiers; verify-don't-trust).** The "**sign half of `ρ_n`
> proved for all n**" headline below is **overstated**; the correct status has **three distinct tiers**:
>
> 1. **The `−w₀` multiplicity structure *up to the fixed-root label* — PROVED, all `n`.** The elementary
>    root-system reversal lemma (below) gives the `⌈/⌊` eigenspace dimensions of `θ=−w₀` on the `A_{n−1}`
>    height-`h` root spaces, for all `n`. **A real theorem — it stands.**
> 2. **The *fixed-root labeling* (which sector is `char(M^h)` vs `char(−M^h)`) = B64** — proved symbolic at SL(3)
>    + structural + **tower-verified `n≤5`**. **B118 (V105)** computed the genuine *signed* fixed-root sign:
>    `(−1)^{h+1}` (all `n`) — **NOT a uniform `+1`**, so B64's "`+1` sector = `char(M^h)`" holds only for odd `h`
>    (a refinement; the `(⌈,⌊)` dimensions are untouched). The all-`n` *labeling* stays tower-verified `n≤5`
>    (B118 supplies the sign, not an independent all-`n` labeling proof); the fixed-root sign **is** the inversion
>    identity `char(M^{−h})=char(−M^h)` (odd `h`).
> 3. **The *tower realization with powers* — VERIFIED `n ≤ 5`, and SUPERSEDED as the tower.** The identification
>    of the θ-split with the **tower's** `char(±M^h)` multiplicities (the long-standing V25 step) holds only
>    `n ≤ 5`; at `n ≥ 6` the θ-split **diverges** from the **Sym two-sequence** (B103/B116) — the actual tower —
>    reproducing the banked V26/V27 divergence (`a₁` 2 vs 3, `a₂` 3 vs 2, `b₂` 1 vs 2). **B117** reframes the
>    tower as the Sym two-sequence (one object); the θ-split is *a* grading of it, exact only `n ≤ 5`.
>
> **So B112 ≠ "the sign half for all n."** The all-`n` sign half is OPEN; the live route is the **Sym two-sequence**
> proof (B103), not the θ-split. See `../B116_reconcile_theta_sym/` and `../B117_interleaving/`. The combinatorial
> lemma (Tier 1, below) is unaffected.

**Status: `PROVED` (computer-assisted — an elementary root-system lemma + the banked B64 parity assignment).**
The B111 decision split the `ρ_n` catalog prize into two named halves — the **sign** structure (bulk
`θ=−w₀`) and the single **degree=rank promotion** `char(M)→char(Mⁿ)`. **This stage proves the sign half, for all
`n`, engine-free** (no Procesi ring, no eps-series, no σ-construction). NO physics; no `CLAIMS.md` promotion; the
`ρ_n` proof stays the prize; proven core P1–P16 untouched. Script `probe.py`; test
`tests/test_b112_closed_form_proof.py`.

## The theorem
For all `n` and all heights `h = 1 … n−1`:
```
   mult char(M^h) = ⌈(n−h)/2⌉,   mult char(−M^h) = ⌊(n−h)/2⌋.
```

## The proof

**Lemma (root system, elementary).** The opposition involution `θ = −w₀` of `A_{n−1}` acts on a root by
`−w₀(e_i − e_j) = e_{n+1−j} − e_{n+1−i}` (**height-preserving**). On the `(n−h)` positive height-`h` roots
`{e_i − e_{i+h} : i = 1 … n−h}`, indexed by `i`, this is the **reversal involution**
```
   σ(i) = (n−h+1) − i        on  {1, …, n−h}.
```
A permutation involution's `(+1, −1)` eigenspace dimensions are `(#fixed + #2-cycles, #2-cycles)`. For the
reversal on `m = n−h` points: if `m` is odd, 1 fixed point and `(m−1)/2` 2-cycles → `((m+1)/2, (m−1)/2)`; if `m`
is even, 0 fixed points and `m/2` 2-cycles → `(m/2, m/2)`. **Either way** `(+1, −1) = (⌈m/2⌉, ⌊m/2⌋)`. ∎
*(`θ` is an involution on the trace ring — `P²=I`, B54/B108 — so its height-`h` restriction has real `±1`
eigenvalues and the central fixed root sits in the `+1` sector; verified.)*

**Assignment (B64, banked).** The contragredient/parity mechanism (`P` sends `m → −m`; Dickson parity
`L_k(−m) = (−1)^k L_k(m)`) puts the `θ`-**symmetric** (`+1`) sector in `char(M^h)` and the `θ`-**antisymmetric**
(`−1`) sector in `char(−M^h)`.

**Theorem = Lemma × Assignment.** The `(+1, −1)` dimensions `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)` are the multiplicities of
`char(M^h)` and `char(−M^h)` respectively. ∎

## Verification
- The lemma's `(+1, −1)` dims `= (⌈(n−h)/2⌉, ⌊(n−h)/2⌋)` for **all n≤12, all h** — computed **two ways** (the
  direct `−w₀` action `(i,j)↦(n+1−j, n+1−i)` on the actual `A_{n−1}` roots, *and* the abstract reversal).
- `θ` acts as the reversal involution (`P²=I`, cycle structure = reversal) for all n≤12, all h.
- Matches **B62's height-2 splits** `(1,0), (1,1), (2,1)` (n=3,4,5) and the **B111** all-heights tower (n=3,4).
- Global checks: net `(+)`-excess `= ⌊n/2⌋`; total char factors `= n(n−1)/2` (all positive roots).

## Scope (honest)
This proves the **bulk `θ`-decomposition** = the **sign half** of `ρ_n`, for all `n` — *engine-free*, the first
piece of the catalog proved from first principles for all `n`. It does **not** prove the full tower: the proved
tower is this **plus the single degree=rank promotion** `char(M¹) → char(Mⁿ)` (B111) — the **power half**, which
is the peripheral / degree=rank piece (`speculations/S022`), still open. The computer-assisted grade reflects the
one verified-not-hand-proved step (the B64 sector assignment, proved symbolically at SL(3) + structural + verified
against the tower).

## Verdict
**The sign half of the `ρ_n` catalog is proved for all `n`.** What remains for the full catalog is the single
degree=rank promotion (B113 tests it at n=5,6; S022 is the mechanism lead).

```bash
python frontier/B112_closed_form_proof/probe.py
python -m pytest tests/test_b112_closed_form_proof.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.

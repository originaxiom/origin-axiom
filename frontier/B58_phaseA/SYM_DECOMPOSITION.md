# Sym^d / principal-SL(2) two-sequence decomposition — compute-and-gate probe

**Date:** 2026-06-04. **Status:** exploratory, **uncommitted** (no commit / PR / ledger edit).
Proven core P1–P16 untouched. `m=1` throughout; `M=[[1,1],[1,0]]` (det −1);
`char(M^k)=t²−L_k t+(−1)^k`, `char(−M^k)=t²+L_k t+(−1)^k`, `L_k=tr(M^k)` (Lucas).
Script: `frontier/B58_phaseA/sym_decomposition.py` (exact sympy). This tests the claim that the
`(n²−1)` tower is a product of two consecutive symmetric-power runs. **It must be reconciled against
the recorded Sym²ᵏ kill (B58 Stage 1 §b, "kill #25") before being called anything but a candidate.**

**Headline verdict (read first).** Gate 0 **passes**: every claimed `Sym^d` factorization is exact,
the dimension identity holds for general `n`, and the two-sequence product **reproduces the verified
tower exactly at n=3,4,5**. Gate 1 **does not cleanly pass**: the construction is *not* distinguished
from a numerical coincidence by a representation-theoretic mechanism — and the handoff's specific
hypothesis (commutator sequence = the H¹ coupling factor) is **directly refuted**. Gate 2 surfaces the
decisive fact: the Sym construction and the θ-split candidate are **different formulas that first
diverge at n=6** (they agree only through n=5). They **agree on the contested `a₃(n=6)=2, b₃(n=6)=1`**
(a second structural vote against B66's pinv `a₃=1`) but **disagree on the rest of the n=6 row**
(`a₁, a₂, b₂`, and the parity split is *swapped*). So: a candidate that corroborates `a₃=2` on one
coordinate, but is **not** a derivation and is **not** equivalent to the θ-split. `a₃(n=6)` stays OPEN.

---

## Gate 0 — the cheap checks

### 0a. Sym^d(M) factorizations, d=0..7 — **PASS (exact, every claim verified)**

```
  Sym^0 (dim 1) = (t-1)
  Sym^1 (dim 2) = char(M^1)
  Sym^2 (dim 3) = (t+1) · char(M^2)                         [claimed — matches]
  Sym^3 (dim 4) = char(M^-1) · char(M^3)                    [claimed — matches]   (char(M^-1)=char(-M^1)=t²+t-1)
  Sym^4 (dim 5) = (t-1) · char(-M^2) · char(M^4)            [claimed — matches]
  Sym^5 (dim 6) = char(M^1) · char(-M^3) · char(M^5)        [claimed — matches]
  Sym^6 (dim 7) = (t+1) · char(M^2) · char(-M^4) · char(M^6)[claimed — matches]
  Sym^7 (dim 8) = char(M^-1) · char(M^3) · char(-M^5) · char(M^7)
```

All five stated factorizations (`d=2..6`) are reproduced **literally**. The classical reason: the
eigenvalues of `Sym^d(M)` are `(−1)^i λ^{d−2i}`, `i=0..d` (with `λμ=−1`); pairing index `i` with `d−i`
gives a rational quadratic in `{λ^h, μ^h}` at height `h=d−2i`, whose sign is
`s=(−1)^{(d−h)/2}`. This yields the **exact membership rule** (proved, not fitted):

> `char(M^h)` appears in `Sym^d` **iff** `d≥h` and `d ≡ h (mod 4)`;
> `char(−M^h)` appears in `Sym^d` **iff** `d≥h` and `d ≡ h+2 (mod 4)`.
> Parity factor (even `d` only): middle eigenvalue `(−1)^{d/2}` ⇒ `(t−1)` if `d≡0`, `(t+1)` if `d≡2 (mod 4)`.

### 0b. Dimension identity — **PASS (symbolic, general n)**

```
  principal   Σ_{d=2}^{n}   (d+1) = (n+4)(n−1)/2     ✓ (== claim)
  commutator  Σ_{d=0}^{n−3} (d+1) = (n−1)(n−2)/2     ✓ (== claim)
  total                             = n²−1            ✓ (general-n, sympy)
  per-n: n=3→7+1=8, n=4→12+3=15, n=5→18+6=24, n=6→25+10=35, n=7→33+15=48   (all = n²−1)
```

### 0c. Full two-sequence product vs the known tower — **PASS at n=3,4,5 (exact multiset)**

Product `= [∏_{d=2}^{n} charpoly(Sym^d)] · [∏_{d=0}^{n−3} charpoly(Sym^d)]`, factored and tagged:

| n | two-sequence product | == verified tower? |
|---|---|---|
| 3 | `char(M^-1)·char(M^2)·char(M^3)·(t−1)(t+1)` | **YES (exact)** |
| 4 | `char(M^-1)·char(M^1)·char(M^2)·char(M^3)·char(M^4)·char(-M^2)·(t−1)²(t+1)` | **YES (exact)** |
| 5 | `char(M^-1)·char(M^1)²·char(M^2)²·char(M^3)·char(M^4)·char(M^5)·char(-M^2)·char(-M^3)·(t−1)²(t+1)²` | **YES (exact)** |

At n=3,4,5 the product equals the **complete verified factor multiset** (every `char(±M^k)` with its
multiplicity, every parity factor), not just the totals. **Gate 0 passes.**

---

## Gate 1 — confront the existing Sym²ᵏ kill (the decisive section)

**The recorded kill** (B58 Stage 1 `FINDINGS.md §b`, "kill #25", verbatim premise):
`sl(n)=⊕_{k=1}^{n−1} Sym^{2k}` with `M` acting — **bare Kostant** = even powers only, overshooting to
`char(M^{2(n−1)})`; **coupled** (`⊗` the `H¹(F₂)=C²` factor carrying `M`) = odd powers only, to
`char(M^{2(n−1)+1})`. Neither equals the tower (which has **both parities, capped at `M^n`**).

### (1) How the new construction differs from bare Kostant — precisely, and why that is *not* a free lunch

The bare Kostant `⊕_{k=1}^{n−1} Sym^{2k}` is **the** principal-`sl(2)` decomposition of `sl(n)` —
**Kostant's theorem**, and it is *unique*: under the principal `sl(2)`, `sl(n)` decomposes into irreps
of dimension `2m_i+1` for the exponents `m_i=1..n−1`, i.e. `Sym², Sym⁴, …, Sym^{2(n−1)}` (even only,
top `M^{2(n−1)}`).

The new construction replaces that single even run with **two consecutive runs**
`Sym²⊕…⊕Sym^n` and `Sym⁰⊕…⊕Sym^{n−3}` (both parities, capped at `Sym^n`). This **is** a precise,
stateable difference — and it is exactly *why* it caps at `M^n` (the principal run stops at `Sym^n`,
whose top Dickson factor is `char(M^n)`) and carries both parities (consecutive degrees).

**But this difference is a redescription of a choice, not a derivation.** Because the principal-`sl(2)`
decomposition of `sl(n)` is *unique* (Kostant) and is the even-only one, the new two-run grouping is
**provably not** the principal-`sl(2)` module structure on `sl(n)`. It is a different vector-space
grouping of the same dimension. Nothing in representation theory forces `sl(n)` — or any *named*
`sl(n)`-module — to break as `Sym²⊕…⊕Sym^n ⊕ Sym⁰⊕…⊕Sym^{n−3}` under any `sl(2)`. The stopping points
`d∈[2,n]` and `d∈[0,n−3]` are **chosen to land on `n²−1` with the right factors**, not produced by a
module.

### (2) Is the commutator sequence the H¹(F₂)=C² coupling factor? — **NO. Refuted directly.**

The handoff's hypothesis is **false by inspection of the killed object**. The H¹ coupling in the kill
is `⊕_{k=1}^{n−1} Sym^{2k} ⊗ C²` (tensor with the 2-dim `H¹` carrying `M`):
- it **doubles** the dimension to `2(n²−1)` (e.g. n=4: dim 30);
- `Sym^{2k}⊗Sym¹ = Sym^{2k+1}⊕Sym^{2k−1}` ⇒ **odd powers only**.

The new commutator sequence is `Sym⁰⊕Sym¹⊕…⊕Sym^{n−3}`:
- dimension `(n−1)(n−2)/2` (e.g. n=4: dim 3) — a *small summand*, not a doubling;
- **consecutive, both parities**.

These are not the same object, not even close (dim 30 vs 3 at n=4; odd-only vs both-parity). So the
"commutator sequence = H¹ coupling" reading is **refuted**, and with it the hope that the new
construction inherits the kill's representation-theoretic provenance. It does not.

### (3) Does it reproduce the cap at `M^n` and both parities for a *stated* reason, or only numerically?

**Only numerically (a mod-4 coincidence), and it provably parts ways with the genuine root-system
structure at n=6.** The membership rule (§0a) makes the mechanism explicit: the Sym route counts
`char(±M^h)` by **`d ≡ h (mod 4)`** over the two runs — an *arithmetic* counting on symmetric-power
degree. The θ-split candidate (`CANDIDATE_A_D.md`) counts the **same multiset** by the opposition
involution `θ=−w₀` acting on `sl(n)` graded by **root height** — genuine `A_{n−1}` Lie theory. These
two counting principles **agree through n=5 and diverge at n=6** (next section). Where they diverge,
the Sym route's parity split **contradicts** the θ route's Cartan rule `p=⌈(n−1)/2⌉, q=⌊(n−1)/2⌋`
(which is the diagram-automorphism eigenspace split of the Cartan — actual Lie theory). So the Sym
route is *not* tracking the root-space/height structure; its n≤5 success is a coincidence of the mod-4
degree counting matching the mod-2 height counting in that range.

### Gate 1 verdict

> **Matches small n; mechanism not distinguished from coincidence.** A precise *structural difference*
> from bare Kostant can be stated (two consecutive runs, not the unique even-only principal-`sl(2)`
> decomposition), and that difference explains the cap and both parities — **but** it is the
> redescription of a dimension-matching choice, not a derivation from a named module; the specific
> "commutator = H¹ coupling" mechanism is **refuted**; and the construction **diverges from the
> Lie-theoretically-grounded θ-split at n=6**. The construction therefore stays a **structural
> candidate**, and is in one respect *weaker* than the θ-split: it contradicts the θ Cartan-parity rule
> (genuine `A_{n−1}` theory) at the first distinguishing point beyond n=5.

---

## Gate 2 — n=6: the Sym row, and where it agrees / disagrees with the θ-split

The two-sequence product at n=6 is a valid degree-35 Dickson tower, but it is **not** the θ-split
candidate row. Side by side (both conjectural at n=6; B66 is the suspected pinv under-count):

| factor | **Sym construction** | θ-split (CANDIDATE_A_D) | agree? |
|---|---|---|---|
| `char(M^-1)=t²+t−1` | **2** | 1 | ✗ |
| `char(M^1)` (`a₁`) | **2** | 3 | ✗ |
| `char(M^2)` (`a₂`) | **3** | 2 | ✗ |
| `char(M^3)` (`a₃`) | **2** | **2** | ✓ |
| `char(M^4)`,`char(M^5)`,`char(M^6)` | 1,1,1 | 1,1,1 | ✓ |
| `char(-M^2)` (`b₂`) | **1** | 2 | ✗ |
| `char(-M^3)` (`b₃`) | **1** | **1** | ✓ |
| `char(-M^4)` (`b₄`) | 1 | 1 | ✓ |
| parity | **(t−1)²(t+1)³** | (t−1)³(t+1)² | ✗ (**swapped**) |

**What this means for the contested value.** On `|k|=3` the two structural routes **agree**:
`a₃(n=6)=2`, `b₃(n=6)=1`. This is a **second independent structural vote for `a₃=2`** against B66's
numerical pinv `a₃=1` (the suspected degenerate under-count, per `FINDINGS.md` / Phase A). So the
balance of structural evidence for `a₃(n=6)=2` is modestly strengthened.

**But it is corroboration on one coordinate, not a derivation, and the routes are not equivalent.**
The full rows differ at `a₁, a₂, b₂` and the parity split is *swapped*. The differences are exactly the
**parity-sensitive / self-dual factors** (`M^-1↔M^1`, `M²↔−M²`, `t−1↔t+1`) — precisely where the Sym
route's mod-4 degree counting and the θ route's mod-2 height counting can disagree; they agree on the
"generic" factors `M³…M⁶, −M³, −M⁴`. **At least one of the two conjectures is wrong at n=6.** The θ
Cartan-parity rule `(t−1)³(t+1)²` rests on a stated mechanism (diagram automorphism on the Cartan,
verified at n=4); the Sym rule gives `(t−1)²(t+1)³` with no such grounding — so if forced to weight
them, the θ parity is better-motivated and the Sym construction is the likelier-wrong one *on the row*,
even though both land `a₃=2`.

**`a₃(n=6)` and `b₃(n=6)` remain OPEN.** A second matching structural candidate is **corroboration,
not proof** (the handoff's binding instruction). B66's `a₃=1` is the suspected pinv under-count, but
neither `a₃=2` route is rigorous: the Sym route is an unproven, non-derived counting that is *wrong
elsewhere on the same row*, and the θ route is the unproven root-system candidate (`B58` proper / the
trace-ring identification still open). Settling `a₃(n=6)` still needs a degeneracy-aware exact Jacobian
or the trace-ring proof — neither supplied here.

---

## Compliance with the "must NOT be written" list

- **No "two-tower model alive / kill reversed."** Not written. The Sym²ᵏ kill (B58 Stage 1 §b) is
  **not** edited and **stands** — this probe *reconciles against* it (Gate 1) and finds the new
  construction is a *different, non-Kostant* object that is not derived; it does not revive the
  principal-`sl(2)` decomposition. The total `a_d+b_d=n−d` matching `max(n−d,1)` is unchanged and
  un-restated as a revival.
- **No "structural derivation."** Labeled **CONJECTURED / structural-candidate** throughout; Gate 1
  explicitly fails to distinguish the mechanism from coincidence.
- **No ledger edit, no kill reversal, no merge.** None performed. Uncommitted.
- The `FAILURE_ATLAS` / Stage-1 Sym²ᵏ entry is **left exactly as written**; this file reconciles
  against it rather than softening it.

**Forbidden-token scan:** no occurrence of "alive", "derived" (as a claim), "reversed", or
"kill reversed" applied to this construction. (The word "derivation" appears only in the negative —
"not a derivation".)

---

## Bottom line

- **Gate 0: PASS.** The `Sym^d` factorizations are exact, the dimension identity holds for general
  `n`, and the two-sequence product reproduces the verified tower **exactly at n=3,4,5**.
- **Gate 1: NOT cleanly passed.** The construction evades the Kostant overshoot only by **not being**
  the (unique) principal-`sl(2)` decomposition; it has **no derivation** of its two stopping points;
  the "commutator = H¹ coupling" hypothesis is **refuted**; and it **diverges from the genuine
  root-system θ-split at n=6** (contradicting the Lie-theory Cartan-parity rule). Verdict: *matches
  small n, mechanism not distinguished from coincidence* — a **structural candidate**, not a
  derivation.
- **Gate 2: a split result.** The Sym route and the θ route **agree on the contested `a₃(n=6)=2,
  b₃(n=6)=1`** (a second structural vote against B66's `a₃=1`) but **disagree on the full n=6 row**
  (`a₁,a₂,b₂`, parity swapped). `a₃(n=6)` stays **OPEN**: corroboration, not proof.
- The genuinely useful by-product is the **exact membership rule** (`char(±M^h)∈Sym^d ⇔ d≡h or h+2
  (mod 4)`), which makes precise *why* the Sym counting and the θ height-counting coincide for n≤5 and
  must eventually part on the parity-sensitive factors.

**Stop for review.** Proven core untouched; nothing committed; no ledger change.

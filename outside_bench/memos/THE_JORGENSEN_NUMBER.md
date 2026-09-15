# Memo 225 — JØRGENSEN: the theorem the owner meant, and it is stronger than the one I found

**Certificate:** `outside_bench/certificates/the_jorgensen_number.py` ·
**Output:** `outside_bench/outputs/the_jorgensen_number.txt`
**No seal** — exact arithmetic in `ℤ[ζ₆]` recomputed from the object's own holonomy, plus string
assertions against tracked files, plus one literature theorem **cited and labelled as cited**.

> **CORRECTION to memo 224.** The owner asked for *"a theorem about figure 8 being only with cusp
> that fixes first axiom"*, and my branch sweep returned **fork F9 / B1323**, on main. **That was
> not it.** The theorem is **Jørgensen's inequality (1976) + Callahan (2009) Cor. 2.4**, and it
> **is on a branch** — `<remote>/paper-verification-ufp0zn`, arc **B1345**, dated **2026-09-12**. The
> owner's "new work from other branches" was exactly right and my sweep landed one theorem short.
> Memo 224's own findings stand; its **identification** of which theorem was meant is superseded
> (addendum filed there).

---

## 1. The theorem

**Jørgensen's inequality (1976).** For every **non-elementary discrete** `⟨X,Y⟩ < PSL(2,ℂ)`:

```
|tr²X − 4| + |tr[X,Y] − 2|  ≥  1
```

The **Jørgensen number** `J(Γ)` is the infimum of that quantity over generating pairs.

**Callahan (2009) Cor. 2.4**, quoted from B1345 and **cited, not re-proved:**

> *"the only **orientable** hyperbolic 3-manifold with `J = 1` is the figure-eight complement."*

## 2. `J(m004) = 1` — exactly, and with **no search**

This is the part worth having: the number does not need minimising. **The cusp does the work.**

Exact, in `ℤ[ζ₆]`, from `ρ(a) = [[1,1],[0,1]]`, `ρ(b) = [[1,0],[u,1]]`, `u = ζ₆`:

| quantity | value |
|---|---|
| relator `a W b⁻¹ W⁻¹`, `W = b a⁻¹ b⁻¹ a` | **`+I`** — so `⟨a,b⟩` **is** the figure-eight knot group |
| `tr a` | **2** — **parabolic**, because `a` is a **cusp** element |
| `|tr²a − 4|` | **0, exactly** |
| `κ = tr[a,b]` | `3/2 + √3·i/2` `= u² + 2` |
| `κ − 2` | `u² = −1/2 + √3·i/2` — a **primitive cube root of unity**, `Φ₃(κ−2) = 0` |
| `|κ − 2|` | **1, exactly** |

> **Upper bound:** the pair `(a,b)` generates the group, and its Jørgensen quantity is `0 + 1 = 1`,
> so `J ≤ 1`.
> **Lower bound:** Jørgensen's inequality gives `J ≥ 1`.
> ### `J(m004) = 1` **EXACTLY** — one exact value and a 1976 inequality, squeezing from both sides.

**Where the cusp enters, precisely:** a parabolic element has `tr = ±2`, which annihilates the first
term **identically**. So **at a cusp, Jørgensen's quantity collapses to `|κ − 2|`** — and that is the
number the record has been carrying all along.

## 3. The record has banked this number for hundreds of arcs — under another name

Verified present at `origin/main`:

* `docs/HINT_LEDGER.md` H96: *"`κ−2=ω²`, `|κ−2|=1` (unit obstruction)"*
* `frontier/B1200_one_polynomial/FINDINGS.md`: *"the object sits at **`|κ − 2| = 1`**, the unit
  obstruction"*

and H96 calls `κ` *"the program's MOST-banked thread"* (P008, B309, B518, B285, B161–163, B186).

> **So the programme's founding constant — "the unit obstruction", existence as frustrated
> cancellation — IS the saturation of a 1976 discreteness bound, and the record did not know it.**
> This is B1345's finding; the certificate reproduces it rather than taking it on trust. It is an
> **absence-under-another-name across the record/literature boundary** — the record had the number
> and the literature had the theorem, and nothing joined them.

## 4. What it actually fixes — and this is the honest part

**It is much stronger than F9.** F9 prices A1 by comparing two records against three. Jørgensen +
Callahan characterise `m004` **among all orientable hyperbolic 3-manifolds by a single number**,
mentioning **no** records, **no** punctured torus, **no** monodromy, **no** knot and **no**
arithmetic. Under it, `UNIQUENESS_THEOREM`'s **A1, A2, A4, A5, A6 become consequences rather than
assumptions** — the substrate `ℤ²`, the shears, the torsion-free closure and the minimality are all
recovered from *"orientable, hyperbolic, `J = 1`"*.

**But it does not touch the orientation axiom — and the reason is exact.** B1345's slack table,
verified present:

> *"Nine of eleven reproduce exactly: **m000 1, m004 1**, m009 √2…"*

**`m000` is the Gieseking manifold — non-orientable, and the sibling the orientation axiom
discards — and it has `J = 1` too.** That is precisely why Callahan's hypothesis says
**orientable**.

> ### `J = 1` selects the PAIR `{m000, m004}`. Orientation picks `m004` out of it.
>
> **And that is the same fork memo 224 computed from the other side.** CELL 3 there found that
> dropping `A3` moves the forced matrix from `A = LR` to `M = L·S` with `M² = A` — the un-squared
> golden matrix, **whose mapping torus is m000**. Two completely independent routes — a `GL(2,ℤ)`
> monoid enumeration and a 1976 discreteness bound — land on **the same pair and the same single
> remaining choice**.

**So the answer to "does it fix the first axiom":** **yes, and more than the first** — it discharges
A1, A2, A4, A5 and A6 at once, *given orientability*. **It does not discharge orientation**, and
after it the genesis reads:

```
orientable  +  hyperbolic 3-manifold  +  J = 1   ⟹   m004
```

**one axiom and one canonical extremality condition**, where the condition is not a taste but the
saturation of a bound every discrete group obeys.

**Not claimed:** that the axiom count therefore drops. **Adopting this is main's call**, and it
interacts with the unmerged A6-relabeling audit memo 224 reported — which wants to re-type
orientation as the observer's closing #0. **If both landed, the entrance would be one extremality
condition plus one closing.** That is a statement about what *would* follow, not a change to any
ledger: **memo 223's price stands at 12.**

## 5. Scope, stated

* **Callahan's corollary is CITED, not proved here**, and its **orientable** hypothesis is
  load-bearing.
* **`m000`'s `J = 1` is INHERITED** from B1345's table and **not recomputed** — `m000`'s holonomy is
  not in `PSL(2,ℂ)`. Whether `{m000, m004}` is the *complete* `J = 1` set, orientable and not, is
  **not established by anything verified here.**
* **C1 (non-vacuity) passed:** on this same group the quantity reaches `5.58`, `8.58` and `4` at
  other pairs — it is not identically 1. And **C3**: B1344's collision is real — the **fibre** `κ`
  is `−2`, giving `|κ − 2| = 4`, **not** the Jørgensen number. A cell taking the wrong `κ` reports 4
  and misses the theorem entirely.
* B1345 also **refutes** two readings chat1 attached to this (that `|z| = 1` is *"the arithmetic
  shadow of amphichirality"* — killed because chiral `5₂` at `1.3247` sits **below** amphichiral
  `6₃` at `1.4656`, and the supporting sample was **all chiral**; and that the index vanishes
  because `χ = 0`). **Those refutations are the branch's, cited here, not re-run.**

## 6. Operational

**Two of this certificate's own checks fired and were right to.** The relator word `W = bABa` was
first read with the capitals as *generators* rather than *inverses*, and the relator **did not
close** — the check caught a wrong word before any bound was claimed on it. And the `HINT_LEDGER`
needle was written with spaces around `=` where the ledger has none, and the quote control fired.
Both are recorded rather than quietly repaired.

*Gate 5 untouched. Nothing promotes. No arc retracted.*
*Every number above comes from `outside_bench/outputs/the_jorgensen_number.txt`.*

---

# ADDENDUM 1 (2026-09-13) — **§4's AXIOM CONCLUSION IS WITHDRAWN** (memo 226)

The owner: *"make sure its right jorgensen"*. Checked, and **§4 does not survive.**

**What stands, and is now tested rather than cited:** `J(m004) = 1` (reproduced a second way from
SnapPy's holonomy over Nielsen pairs, `1.000000000000`), `κ − 2 = u²` with `|κ − 2| = 1`, the
identification with the record's **"unit obstruction"**, and the uniqueness — **323 two-generator
census manifolds scanned, exactly one reaches 1, and it is m004** (m009 at `√2`, m129 at `2`).

**What is withdrawn — §4's claim that the theorem discharges A1, A2, A4, A5, A6.** The precise
statement is **Callahan: "the only *torsion-free* Jørgensen group is the figure-eight knot group"**,
and a **Jørgensen group is by definition generated by TWO elements**.

> **A two-generator group IS `A1` in another language.** The theorem **assumes** the first axiom; it
> does not derive it. `A3` is likewise inside the hypothesis, since a **Kleinian** group already
> lies in `PSL(2,ℂ)` — orientation-preserving. **Discharged: A4, A5, A6. Assumed: A1, A2/A3.**
> **Three of six, not five.**

What the theorem genuinely replaces is the **construction** — shears, closure, minimality — with one
**extremality condition**. §2's exact computation, §3's identification and §5's scope are unchanged.
**BENCH ERROR #32** is filed in memo 226: an axiom conclusion drawn from a paraphrase without
checking the theorem's hypotheses.

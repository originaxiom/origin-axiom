# B1206 — THE ℙ³ IS EXACTLY ONE CONDITION SHORT: the linear cuts B1205 called missing do exist, there is exactly one, and the count lands at dim 1

**Status: banked (frontier). Verdict OPEN** (the COUNT is established; the ℙ³ question stays open — one condition short) — a counting result, sharp and falsifiable: it moves
the ℙ³ row from *"no linear conditions exist"* to *"one exists; the forcing is one condition short."*
`verification/reproduce.sh` → `REPRODUCES`. Gate 5 clean (this counts available *structure*; it
asserts no physical value and requires no coupling to take any particular value).

## Where B1205 left it

B1205 found the nonlinear condition exists (det Y_d(h) is a genuine failable cubic on the ℙ³) but
cuts only one dimension of three, and that **B1195/GC-25 proved no banked symmetry supplies linear
conditions on B₀**. The frontier it left: *linear cuts must come from a consistency requirement
rather than a symmetry — are there any?*

## The answer: yes, and the record already banks exactly one

**The mechanism.** The object's cubic contains the term **1·10·10** (banked, LAW_MAP/B884/B987:
27³ ⊃ 16·16·10 + 1·10·10). A cubic term C(X, Y, ·) becomes a **linear functional on B₀** as soon as
its other two legs are **pinned to unique states**. So the question is purely: *which slots are
pinned?*

- **H_u is 1-dimensional** (sector table Q/dc/Hd/Hu = 3/3/4/1, B1161's own-verified selection
  arithmetic) — pinned automatically.
- **The 27 has exactly two neutrals**, and memo 80's *measured* λ-term row (byte-verified on this
  bench at B1171) reads **N·H_u·H_d : N1 → 2 nonzero entries, N2 → 0** — so **only one neutral
  couples** to H_u·H_d.

**Therefore the object supplies exactly ONE canonical linear functional on B₀**: the λ-term
C(N₁, H_u, ·). (The q·dᶜ·H_d and l·eᶜ·H_d rows are linear in h only *after choosing* matter states,
so they are texture data — they *are* the tensor — not canonical conditions.)

## THE CUT LEDGER

| step | source | dim |
|---|---|---|
| the Higgs line ℙ(B₀) | — | **3** |
| − 1 canonical **linear** condition | the λ-term C(N₁, H_u, ·) | 2 |
| − 1 **nonlinear** condition | det Y_d(h) = 0 (B1205) | **1** |
| points require | | **0** |

> **THE FORCING FALLS EXACTLY ONE CONDITION SHORT.**

## Why this matters more than another negative

B1205's state was *"the linear cuts are missing"* — which sounds like an unbounded search. This
bounds it precisely: **one more independent condition on h closes the ℙ³ to a finite set**, and the
row would flip from PERMANENT to FORCED. The program is not far from forcing the last continuous
closer-datum it has; it is one condition away, and the number is now checkable rather than
rhetorical.

## What could supply the missing one (named, not claimed)

Each is a bounded question, none is asserted here: **(i)** the second neutral N₂ — the measured row
says it does *not* couple to H_u·H_d, so it supplies nothing *at this order*, but the exotic-mass row
(D·Dᶜ·N: N₁ → 3, N₂ → 0) is a different slot worth its own count; **(ii)** doublet–triplet
splitting, which the record explicitly types as EXTERNAL and colour-choice-dependent (B298/B299) —
if it is external it *cannot* supply an object-side condition, which would be a clean negative;
**(iii)** the λ-term's own **rank** on B₀ — banked as "2 nonzero entries" in *one* functional, but
if the underlying map has rank 2 rather than 1 the ledger closes immediately. **(iii) is the cheapest
and it is exactly a datum codex's commissioned 𝒯 evaluator (R023) would settle.**

## Fences

This is a **count of available structure**, not a physics claim: nothing here says the λ-term must
vanish, or that any coupling takes any value — imposing a *particular* condition is a modelling act
the program firewalls, and the count is silent on which condition is right. Sector dimensions and
the λ-term row are banked and cited (B1161; memo 80 via B1171, byte-verified), not re-derived here.
The determinantal cubic is B1205's, computed over the tensor's *shape*. Nothing weakens V-3: even a
forced Higgs line yields a *direction*, not a measured value.

# xB009 — PREREGISTRATION (sealed BEFORE any computation of this arc)

**Seat `xb`, `sep16-branch`, 2026-09-17. Written, hashed and committed before any cell runs; the
hash is in `ARTIFACT_HASHES.txt` in the same commit and the commit is pushed before any result
exists, so the order is checkable from this branch's history.**

## P0 — the quantifier

Twisted Alexander / Reidemeister torsion at the geometric holonomy. Named mathematics. No value,
no generation count, no physics reading, nothing to `CLAIMS.md`. Gate 5 absolute.

## Owner directive, 2026-09-17, and what it changes

The owner has set the goal: **the TOE itself, not an adjudication of whether it is reachable**;
**a negative is not a deliverable**; and *"I want the TOE to be true if it is."* This arc is built
to that instruction. It is a **constructive** probe — it asks what the unexplored sector
**carries**, not whether another route is closed — and if it returns empty this arc will say so in
**one paragraph** and not be built into a monument.

## The gap, and it is a real one

xB007 proved the object's selection datum is the sign of its monodromy, `−I`, and this seat then
computed which representations can see it:

| | sees `−I`? |
|---|---|
| `Sym¹, Sym³, Sym⁵, …` (**odd**) | **YES** |
| `Sym²` (= adjoint), `Sym⁴, …` (**even**) | **no** |
| **E₆ = ⊕ Sym^{2mᵢ}**, exponents {1,4,5,7,8,11} → powers {2,8,10,14,16,22} | **all even → blind** |

**B425 computed the geometric torsion at `ρ_geo` for the six E₆ exponents — all even — and found
every coefficient RATIONAL: `√−3` is present in the Fox matrix and CANCELS in every determinant.**
B1242 separately found all `sl₂` weights on the **27** and the **78** are even, so that map factors
through `PSL(2,ℂ)` too.

> **The entire computed record lives in the even sector. `Sym^{odd}` at `ρ_geo` has never been
> computed.** B425's own machinery (`sym_power_mod(M, n, p)`) is general in `n` and was only ever
> called with even arguments.

## The question

**What does the odd sector carry at `ρ_geo`, and does it carry anything the even sector provably
cannot?**

## Cells and two-outcome criteria — declared before running

| cell | question | outcome A (constructive) | outcome B |
|---|---|---|---|
| **O1** | does `ρ_geo` admit the odd lift at all, and **how many** lifts are there? | the `SL(2,ℂ)` lift exists and the count of lifts is computed (`H¹(M; ℤ/2)`) — **naming the ℤ/2 concretely** | no lift: the odd sector is empty and the arc ends here |
| **O2** | **THE HEADLINE.** the twisted Alexander polynomial at `ρ_geo` in `Sym^n` for **odd** `n` — **do its coefficients stay rational, or does `√−3` SURVIVE?** | **`√−3` survives**: the odd sector carries Eisenstein content the even sector destroys — new arithmetic, and exactly the thing the even sector cannot supply | rational like the even ones: the sector carries no new field, reported in one paragraph |
| **O3** | does the odd sector **separate m003 from m004**, where every even invariant provably cannot? | it separates — the first computed invariant in this record that selects the object | it does not: then even the odd sector does not select, stated plainly |
| **O4** | is the odd content **independent** of the even, or a function of it? | an odd invariant not determined by the even ones — the sector is genuinely new information | determined: no new information, one paragraph |

**Controls, fixed here.** (i) The trivial representation must reproduce the ordinary Alexander
polynomial of `4₁`, `t² − 3t + 1` — B425's own validation, re-run, or the arithmetic is void.
(ii) The **even** cases must reproduce **B425's banked values** (adjoint `−3`, coefficients
rational) on this seat's own re-run, or the port is wrong and nothing downstream counts.
(iii) `ρ(relator) = I` must hold exactly, forcing `u² + u + 1 = 0`.

## Declared prior, so the arc can overrule it

**O2: this seat expects `√−3` to SURVIVE for odd `n`**, at moderate confidence — B425 records
`√−3` as present in the Fox matrix and cancelling only in the determinant, and the even/odd split
is exactly a Galois/duality split, so the cancellation has no reason to persist. **O3: expects
separation**, since the odd sector is by construction the part that sees `−I`. **O4: uncertain.**

**Named in advance:** if O2 returns rational **and** O3 fails to separate, then the odd sector is
**not** the door, this seat's reading of xB007 was over-optimistic, and the arc reports that in a
short note rather than an edifice — per the owner's instruction that a negative is not a
deliverable.

**And the discipline that must not slip while building.** The temptation here is
`odd sector = spin = the 4d spinor = matter`. **That is an identification claim of the I-10 class
and this arc does NOT make it.** Notion A (odd `Sym^n` of the object's own `SL(2,ℂ)`, i.e. what
fails to factor through `PSL`) and Notion B (a `Spin(3,1)` or `SO(10)` spinor) are different
objects; B1145 fences this in its own words. Any bridge needs B1223's discriminator and a ledger
row. This arc computes the arithmetic and stops.

## Scope

Named mathematics at the holonomy. `creates_law` false. Nothing reaches `CLAIMS.md`, F2 or Gate 5.

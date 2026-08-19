# PREREGISTRATION — B8085: Route A of B990's orbit-to-point gap, sealed before computing

**Sealed 2026-08-19, before running anything beyond what is already banked.** Owner-directed:
*"do route 1 properly."*

## The question, in B990's own words

> **Route A — shrink the group.** Replace `G(ℚ)` by a subgroup that does not act transitively on
> `O`. The natural one is arithmetic: `G(ℤ)`… **Count the `G(ℤ)`-orbits inside its `G(ℚ)`-orbit.**
> **If it is 1, the integral orbit is a canonical point up to `G(ℤ)`** — which is exactly what a VEV
> direction needs, since a VEV is only ever defined up to the unbroken group.

`G` acts on **pairs of 27s** (Kato–Yukie); rational orbits are classified by the **cubic étale
algebra**, which for the object is `K = ℚ[x]/(x³−12x−5)`. The object's pair is already **integral**
in the B854 Chevalley frame (B884: every coefficient ±1).

## P0 — the quantifier, stated first

**The ALGEBRA AND ITS ARITHMETIC** — rational and integral orbits of pairs of 27s, and the class
arithmetic of `K`. **Not a manifold.** Nothing here speaks about m004, its class, its sisters, its
rows or its child. **Gate 5: no physical identification; a VEV *direction* is a direction in an
algebra, and no value, scale or measured quantity enters.**

## B990's prior, adopted unchanged

> **UNFAVOURABLE.** *"Class numbers of this kind are generically > 1, and the programme's history is
> a record of homogeneity winning."*

**I adopt that prior and will not soften it.** It is the correct prior and it is the owner's own
standard: a positive here must survive it, not replace it.

## What is already banked, and therefore not a new result

`h(K) = 1` is **already banked** and was independently reconfirmed by an external referee this week
(explicit generators exhibited for every small prime, including both degree-one primes above 7 and
above 11). **This arc may not claim `h = 1` as its finding.**

## What is genuinely unknown at seal time

The **narrow** class number `h⁺(K)`, the unit signature map, and the cube/square quotients of the
class group. These are what the integral-orbit count is built from, and none is banked.

## Declared outcomes, before computing

| result | reading |
|---|---|
| every candidate counter = 1 (`h`, `h⁺`, `\|Cl/Cl²\|`, `\|Cl/Cl³\|`) | **Route A is FAVOURABLE against its own prior** — whichever class-group quantity governs the integral count, it is trivial, so the conclusion does not depend on resolving which. Report as a *conditional* positive: the arithmetic obstruction is absent; the identification of the counter remains owed |
| `h⁺ > 1` while `h = 1` | the narrow class group is the obstruction, and **the signature map is the mechanism** — report which units fail to realise which sign patterns |
| the quotients differ from each other | the count depends on which correspondence applies, and the arc **cannot conclude**; name the discriminating computation |
| anything ≠ 1 | **the prior held.** Say so plainly; a negative here is B990's expected outcome and is worth exactly as much as a positive |

## Controls

1. **Two independent tools.** PARI/GP and an independent check; a class number from one engine is a
   claim, not a result.
2. **The field must be verified first** — `disc = 6237 = 3⁴·7·11`, monogenic, totally real — before
   any class datum is read. A class group of the wrong field is worthless.
3. **No headline may be a printed constant** (E43): every reported number bound to a computed
   variable.
4. **The counter is not assumed.** This arc computes class-arithmetic invariants. Whether the
   integral orbit count *equals* one of them is Kato–Yukie/Bhargava integral theory and is
   **registered as owed**, not asserted. If all candidates agree, that owed step does not change the
   verdict — and that is the only circumstance under which this arc may report a positive.

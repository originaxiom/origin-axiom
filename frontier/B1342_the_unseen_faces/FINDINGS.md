# B1342 — IS THERE A FACE WE HAVEN'T SEEN? **Three of four**, and the record named them in 2026-07

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** MATHEMATICS (dynamics layer).
**Depends on:** B309/B518 (the four κ-faces), B496/B497 (the monoid), B730 (the arithmetic closure),
B1341 (the least-action theorem), B1247 (the retrieval diagnosis).
**P0:** this computes over **End(F₂) acting on the SL₂ character variety**. It says nothing about
m004's geometry directly, and nothing new about physics.

---

## The question

> *"is there any face that we haven't seen yet, possibly?"*

The record uses **"face"** in three different senses. Two of them are **closed**, with theorems. The
third is **open by three quarters**, and the record said so in its own words fourteen months of arcs
ago.

## 1. The two closed senses — no unseen face there

**The arithmetic faces close at exactly three (B730, PROVED, three-way verified).** The object's own
intrinsic arithmetic forces `ℚ(√−3)` (*being*), `ℚ(√5)` (*hearing*), and their product `ℚ(√−15)`
(*meeting*) — the three involutions of one biquadratic field, `Gal(ℚ(√−3,√5)/ℚ) = V₄`. `ℚ(√−7)` is
excluded **three independent ways** (Neumann–Reid rigidity, A-polynomial branch factorisation, the
SL(n) tower) and is a *stage*, not a face. **Complete.**

**The κ-faces are four and are all worked (B309/B518, with B312 numbering them).** Face I existence,
Face II geometry, Face III matter/content, Face IV quantum. B312 closed the last open connection
(Face IV houses the *same* E₆ the content carries). **Complete.**

*(One bookkeeping mismatch worth recording: B258's "three faces — geometry, arithmetic, quantum" and
B309's "four faces — existence, geometry, matter, quantum" are different lists. `existence` appears
in the second and not the first. Not a lost face; two decompositions of one object.)*

## 2. The third sense, and the answer

**B497** (PROVED, 2026-07) classifies `End(F₂)` on the character variety by the Hopf dichotomy
crossed with `det`(abelianisation). Its classification section ends:

> **"The program to date = stratum 1 of 4."**

**That is the answer to the question, in the record's own words, and it has been sitting there.**
B1247 (on main, this week) records that B497 *"sat SEVEN WEEKS"* uncited while B1157 concluded the
object supplies no dynamical law.

### The four strata, recomputed here from the substitutions (nothing copied)

| stratum | citizen (word map) | det | κ-law | multiplier |
|---|---|---|---|---|
| **1** Aut | `a→ab, b→a` (golden) | **±1** | `κ′ = κ` | `1` |
| **2** | `a→aa, b→bb` (squaring) | **4** | `κ′−2 = (κ−2)·x²y²` | `x²y²` |
| **2′** | `a→ab, b→aa` (period-doubling) | **−2** | `κ′−2 = (κ−2)·x²` | **`x²` — computed here; B497 left it as "stratum-2 family"** |
| **3** | `a→AB, b→BA` (Thue–Morse) | **0** | `κ′−2 = (κ−2)(x²+y²−xyz)` | `x²+y²−xyz` |
| **4** | `a→ab, b→ab` | **0** | `κ′ ≡ 2` identically | `0` |

Every trace map B497 states is **reproduced from its word**; every κ-law is verified by **ideal
membership** modulo `(det A − 1, det B − 1)`.

## 3. Why the programme stayed in stratum 1 — derived, not guessed

Not neglect. **κ is conserved only in stratum 1.**

`κ′ = κ` holds in stratum 1 and **in no other stratum** (verified: all four others move the leaf).
Everywhere else the map multiplies `(κ−2)` by a polynomial and **travels between leaves**. Since κ is
the programme's one conserved first integral — *"κ = tr[a,b], ONE COMMUTATOR TRACE, FOUR FACES"*
(B309/B518) — **every arc built on κ is structurally trapped in stratum 1.** The confinement is a
theorem about the object, not a habit of the seats.

**And B497's U1, re-derived:** `(κ−2)` divides `(κ′−2)` in *every* stratum, so **κ = 2 — B309's
"nothing" — is a fixed point of the whole monoid**, not just of the units. The floor is absolutely
invariant; only the units preserve the *height*.

## 4. What the confinement costs — joining B1341 (today)

B1341 proved that a discrete Lagrangian's map always preserves an area form, so an **anti**-symplectic
map has none. Extend that across the strata:

| region | κ | orientation | variational? |
|---|---|---|---|
| stratum 1, `det +1` (the monodromy) | preserved | preserved | **yes** — B1341's `S(u,U)` |
| stratum 1, `det −1` (the half step) | preserved | **reversed** | **no** — B1341's theorem |
| strata 2, 2′, 3, 4 | **not preserved** | — | **not even well posed**: no invariant leaf, so no phase space to carry a form |

> **The object's least-action principle occupies half of one stratum out of four.**

And `S063` places **irreversibility at `det ≠ ±1`** — strata 2/2′/3/4. So:

> **Irreversibility and least action are in disjoint strata. Where the action is, time is reversible;
> where time has an arrow, there is no action to vary.**

That is a structural statement about *this* object, and it says the arrow of time will not be found
where the action was found. It also says what the multiplier is *for*: `κ′−2 = (κ−2)·M` measures
motion toward or away from `κ = 2` — toward or away from **nothing**. **The multiplier is the arrow**,
and it is identically `1` exactly where the programme has been standing.

## 5. The confinement, measured

Over **1221** arcs carrying a verdict:

| the non-unit world | FINDINGS mentioning | claim lines |
|---|---|---|
| Thue–Morse (stratum 3) | **10** | 3 |
| period-doubling (stratum 2′) | **4** | **0** |
| `End(F₂)` monoid / non-invertible | **4** | 2 |

Essentially **B496, B497 and B1254**. Three arcs out of 1221 outside the units.

## 6. The answer, stated plainly

**Yes — three faces of four, and they are not hypothetical.** They are classified, their citizens are
named, their κ-laws are exact and verified twice, and their physics reading is fenced in `S063`.
What has never been done is *work* them: no arc computes the dynamics of stratum 2, 2′, 3 or 4, and
`period-doubling` appears in **zero** claim lines in the entire corpus.

**The honest caution.** This is not a hidden face of the *object* — m004 is what it is. It is an
unexplored face of the **monoid acting on it**, and B497 already proved the classification. Whether
anything physical lives there is untested and this arc claims nothing about it. What *is* established
is that the two questions the programme most wants — **the arrow of time** and **an action** — are
provably in different strata, and it has only ever stood in one of them.

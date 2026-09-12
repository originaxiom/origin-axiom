# B1345 — THE JØRGENSEN NUMBER: the theorem is real, the record already had the number, and two readings die

**Date:** 2026-09-12 · **Seat:** cc · **Lane:** MATHEMATICS (geometry/arithmetic).
**Depends on:** **B309/B518/B1010** (the κ-unification, "the unit obstruction"), B286 (the seam),
B1335 (the vanishing is not formal), B1344 (E72, the κ collision).
**P0:** computed against SnapPy's own geometric holonomy at high precision, plus exact arithmetic
over ℚ(ω). Literature theorems are cited, not re-proved.

---

## Verdict table

| chat1's claim | verdict |
|---|---|
| **J(figure-eight) = 1, exactly** | **CONFIRMED** — computed independently, attained at the pair `(ab, ba)` |
| corpus absences (`waist size`, `discreteness bound` = 0; Jørgensen = Andersen–Jørgensen only) | **CONFIRMED** |
| the slack table | **9 of 11 confirmed exactly**; two differ (§5) |
| B286's *"every generic filling is chiral"* | **CONFIRMED as banked** |
| *"the corpus has never seen this"* | **HALF RIGHT — and the other half is the finding (§2)** |
| *"\|z\| = 1 is the arithmetic shadow of amphichirality"* | **REFUTED** (§3) |
| *"the index vanishes because χ(M) = 0"* | **REFUTED by B1335** (§4) |
| *"no handedness and no χ because it has no slack"* | **REFUTED** — χ = 0 at every slack (§4) |

## 1. The headline is right

Jørgensen's inequality: for every non-elementary **discrete** `⟨A,B⟩ < PSL(2,ℂ)`,
`|tr²A − 4| + |tr[A,B] − 2| ≥ 1`. Minimising over word pairs on SnapPy's geometric holonomy:

> **J(m004) = 1.000000000000000**, attained at `(ab, ba)` where `tr A = −2` (parabolic, first term
> `4·10⁻⁶⁴`) and `|tr[A,B] − 2| = 1` exactly, with `tr[A,B] − 2` a **primitive cube root of unity**.

Stable at search depth 2, 3 and 4. Callahan (2009) Cor. 2.4 — the only **orientable** hyperbolic
3-manifold with `J = 1` is the figure-eight complement — is cited, not re-proved.

## 2. What chat1 missed, and it is bigger than the claim

At a pair whose first element is parabolic, `tr A = ±2` kills the first term **exactly**, so

> **J = |tr[A,B] − 2| = |κ − 2|.**

And **B309 / B518 / B1010 bank, verbatim:** *"κ − 2 = ω² with **|κ − 2| = 1**, **the UNIT
obstruction**, the founding sentence as an equation."*

> **The record has carried the Jørgensen number as a headline law for hundreds of arcs, under the
> name "the unit obstruction", without knowing it is the saturation of a 1976 discreteness bound.**

So *"the corpus has never seen this"* is half right: the corpus has never seen the **theorem**, and
has banked the **value** under another name. That is the **E54 shape — absent-under-the-other-name —
one level out**, between the record and the literature rather than inside the record. It is the
sharpest instance of chat1's own closing lesson, and chat1 did not notice it applied to its own find.

**And B1344's E72 is load-bearing here.** It is the **meridian** κ that saturates: `|ω²| = 1`. The
**fibre** κ is `−2`, giving `|κ − 2| = 4`, which is *not* the Jørgensen number. Had the collision
gone unflagged, the identification would have been invisible or wrong.

## 3. The amphichirality reading is refuted — by chat1's own theorem and own table

chat1 reads `|z| = 1` as *"the arithmetic shadow of amphichirality"*. If that held, **every**
amphichiral manifold would have `J = 1`, contradicting the **uniqueness theorem cited two paragraphs
earlier**. Computed:

| amphichiral knot | J | | chiral knot | J |
|---|---|---|---|---|
| 4₁ | **1.0000** | | 5₂ | **1.3247** |
| 6₃ | 1.4656 | | 6₁ | 2.4212 |
| 8₃ | 2.3311 | | 7₄ | 2.2056 |
| 8₉ | 2.7805 | | | |
| 8₁₂ | 3.2506 | | | |
| 8₁₇ | 2.0444 | | | |
| 8₁₈ | 2.4142 | | | |

**Chiral 5₂ (1.3247) sits below amphichiral 6₃ (1.4656)** — the orders interleave. And chat1's *own*
slack table contains **amphichiral m136 at 2√2** and **amphichiral m003 at 4**.

**Why the supporting evidence looked good:** chat1's sample was 5₂, 6₁, 7₄, 7₇ — **all chiral**. A
check whose sample contains no amphichiral knot cannot fail. That is the **E67 shape** (a control
that varies the wrong thing), and it is the same trap that has caught this bench repeatedly.

**Consequence:** §3–§4 of chat1's synthesis — *"extremality forces symmetry, so F5 and F6 are what
extremality costs"*, and *"the walls are what extremality costs"* — **does not survive.** The link it
rests on is not there.

## 4. The index explanation is refuted by this session's own banked arc

chat1: *"the index vanishes because `I = t₀ − r₁` is a truncation of something identically zero by
`χ(M) = 0`, and `χ = 0` holds for every 3-manifold with torus boundary."*

The second clause is **true** — `χ(M) = χ(∂M)/2 = 0` for any compact 3-manifold with torus boundary,
**at every slack**. The first clause is **false**, and **B1335** settles it: on **m010** — also
one-cusped, also `χ = 0` — all four identities hold (including the χ-driven `a₀ − a₁ + a₂ = 0`), the
sector is in domain **D**, and **`I = ±1`**. If the vanishing followed from `χ = 0`, it could not.

And the same fact kills the slogan *"no handedness and no Euler characteristic because it has no
slack"*: **t12833 sits far off the bound and still has χ = 0**, for exactly the reason m004 does.
`χ = 0` has nothing to do with extremality.

**What survives of chat1's §"three ways off":** the *conclusion* that filling buys the sign and does
not buy the index is correct and already banked (B286 + this session's B1332–B1334). Only the
proposed *mechanism* is wrong.

## 5. The slack table

Nine of eleven reproduce exactly: m000 **1**, m004 **1**, m009 **√2**, m136 **2√2**, m003 **4**,
m206 **4**, v2873 **3√3**, s958 **7**, m202 **7**. Two differ:

* **t12835** — computed 7, chat1 says 4. This bench's search is over words of length ≤ 3, so its
  value is an **upper bound**; chat1's smaller value is compatible and probably better.
* **t12833** — computed **9**, chat1 says 13. Here the direction is decisive: J is an **infimum** and
  a pair achieving 9 is exhibited, so **the true J is ≤ 9 and chat1's 13 cannot be it.**

**And m000 at J = 1 is not a counterexample to uniqueness — it is the hypothesis working.** m000 is
the **Gieseking manifold: non-orientable**, volume 1.014942, and m004 is exactly its orientable
double cover (ratio 2.000000). Callahan's theorem says *orientable*. chat1's own table contains the
case that shows why that word is in the statement.

## 6. What stands

**The first link really does change type.** `J(m004) = 1` plus Callahan's uniqueness is a
**variational** characterisation — m004 as the unique orientable solution of a minimisation — where
every previous selection story was descriptive and measured generic (B762's quine 97.2%, B727's
genericity, B993's ~1 in 3). chat1's fence is correct and must travel with it: **this selects the
manifold, not E₆**; everything downstream stays exactly as subject to B727 as before.

**Gated observation, recorded and not claimed:** the pair attaining the bound is `(ab, ba)` — the
image of the **Thue–Morse substitution**, B497's stratum-3 citizen. Whether that is structure or an
artefact of short-word search order is **untested**.

**No physics reading is licensed and no claim is promoted.**

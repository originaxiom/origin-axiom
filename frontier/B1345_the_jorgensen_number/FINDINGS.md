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

* **t12835** — computed 7, chat1 says 4. **CORRECTED 2026-09-12 on receipt of the seat's code:** the
  concession that chat1's 4 was “probably better” is **RETRACTED**. Its table computes `|κ − 2|` at
  SnapPy's **default** pair with **word-length 0** and **no parabolicity check**; t12835's default
  generator is not parabolic, so the `|tr²A − 4|` term is silently dropped and the number is not a
  bound on `J` at all. **This bench's 7 stands as the upper bound.**
* **t12833** — computed **9**, chat1 says 13. **Refined:** t12833 is the *one* row where their
  default generator **is** parabolic, so their 13 is a legitimate evaluation of the Jørgensen
  quantity at that pair and hence a valid upper bound. `J` is an infimum, so `J ≤ 9 < 13`: both are
  sound, this bench's is tighter, and there was never a contradiction.

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

---

# ADDENDUM (same day) — §4's REFUTATION IS WITHDRAWN. F6 IS RIGHT, AND IT AGREES WITH B1335.

**This bench graded a finding from a transcript paraphrase instead of from its source, and the
paraphrase inverted the finding's conclusion.** The full handoff arrived with a runnable check
(`verify/check_chi_wall.py`), and F6 says the **opposite** of what §4 refuted.

## What F6 actually claims

From the seat's own script, verbatim:

> *"1. is `I = t0 - r1` an index, or a truncation?
>  from B1297's F: `(a0-a0*)-(a1-a1*) = -r1 + t0 == I` : True
>  `chi(M)=0` for V and V* => FULL alternating difference = 0 (identically zero): True
>  therefore `I = -(a2 - a2*)` : a PARTIAL SUM of something that vanishes by dimension.
>  => **no index theorem stands behind I. Nothing forces its value either way** — which is exactly
>  B1329's 'the identities leave I free'."*

**Re-derived here as linear algebra, not taken from the script:** subtracting the two χ-identities
`a₀ − a₁ + a₂ = 0` (for `V` and for `V*`) gives `(a₀−a₀*) − (a₁−a₁*) + (a₂−a₂*) = 0`, so
`I = −(a₂−a₂*)`. **Confirmed.**

## So F6 and B1335 are the same statement from two sides

F6: `I` is a partial sum of an identically-vanishing alternating difference, therefore **nothing
forces its value**. B1335: a sector on **m010** where the value is **`I = ±1`**. F6 *predicts* B1335;
B1335 *instantiates* F6. **They agree.** F6 even cites B1329's *"the identities leave I free"* —
which is this bench's own line.

## What §4 actually refuted, and what it got wrong

The transcript's compressed sentence — *"the index **vanishes because** `I` is a truncation of
something identically zero"* — reads as an inference to `I = 0`, which is a non-sequitur and is what
B1335 contradicts. **That sentence, read literally, is still wrong.** But it is a paraphrase, and
**F6 is not the paraphrase.** Attributing the error to F6 was this bench's, not the seat's.

**Withdrawn:** §4's *"the index explanation is refuted by B1335"*, and the verdict line's
corresponding clause.
**Stands, unchanged:** the amphichirality refutation (§3) — computed directly, six counterexamples,
unaffected. And the synthesis sentence *"the object has no handedness and no Euler characteristic
because it has no slack"* is still wrong — **but F6 refutes it too**, since F6's §2 shows the entire
geometric family shares `χ = 0` whatever its slack. The seat's synthesis contradicted the seat's own
finding, and this bench blamed the finding.

## The error class

**`ERROR_LEDGER` E58 — graded from a summary.** The source was one request away and was offered; this
bench graded the compressed version. The handoff's own README says *"read section 13 (what is NOT
verified) before citing"* and *"assume the un-gated results are known until checked"* — a seat that
fences its own work that carefully deserved to be read at the source before being refuted.

**Standing rule this instance sharpens:** a REFUTATION of another seat's named finding is graded from
that finding's own artifact, never from a relay, a transcript, or a summary — and if the artifact is
not in hand, the disposition is *"not assessed"*, not *"refuted"*.

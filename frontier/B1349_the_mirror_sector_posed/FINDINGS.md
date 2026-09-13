# B1349 — THE MIRROR SECTOR POSED: the residual freedom is 48, and R11's arithmetic says DO NOT SPEND THE ROW

**Date:** 2026-09-13 · **Seat:** cc · **Lane:** MATHEMATICS (the crossing door).
**Depends on:** B1011 (C6, the mirror set), B1040, B1348, `docs/KIND_TABLE.md`,
`docs/CROSSING_REQUIREMENTS.md` (R1–R12), `docs/LISTENER_MAP_SPEC.md`.
**P0:** this **counts a freedom**. It performs **no** value comparison — `F2` absolute — and pays
nothing. Its purpose is to make R7's look-elsewhere ledger and R11's anchor arithmetic *computable*
for the crossing's only remaining target.

---

## Why this sector and not the other

`KIND_TABLE`'s four coupling rows: **tones CONSUMED** (B1066 R-B, MISS decisive), **probability
CONSUMED** (B1066 R-A, MISS decisive), **phases CONSUMED** (B1027 + B1063, MISS both sectors), and

> **mirror set (θ-even) — UNCONSUMED — the last licensed row**, delivered by B1011 C6 and *"never
> drawn on by any sealed comparison."*

And the one-shot rule *"consumes CONTACT ROWS"* — so the row is spent whatever the outcome.
**B1348 posed the θ-ODD plane, which is not the crossing target.** This poses the right one.

## The instrument on the even sector (controls first)

| | |
|---|---|
| canonical rational basis from the weights: `e₍₀,₀₎`, `e₍₁,₁₎`, `e₍₀,₁₎+e₍₁,₀₎`, `e₍₀,₂₎+e₍₂,₀₎` | all satisfy `C v = +v` ✔ |
| `⟨R,L⟩` restricts exactly to it | ✔ |
| **projective image** | **720 = 12 × 60 = `A₄ × A₅`** ✔ (as forced: `(−1,−1)` and `(−1,1)` act as scalars on `V₂⊗V₂`) |
| `ℂ⁴_even` irreducible | ✔ no common eigenvector |
| control: a random direction | `\|Stab\| = 1`, orbit 720 ✔ |

## The stabilizer spectrum — every orbit size divides 720, as orbit–stabilizer requires

| `\|Stab\|` | 15 | 10 | 9 | 6 | 5 | 3 | 2 |
|---|---|---|---|---|---|---|---|
| **orbit size** | **48** | 72 | 80 | 120 | 144 | 240 | 360 |

> ### MAXIMAL `|Stab| = 15` ⟹ THE SMALLEST DISTINGUISHED ORBIT HAS **48** ELEMENTS.

And the structure is confirmed, not assumed: `15 = 3 × 5` = (tetrahedral vertex stabilizer) ×
(icosahedral vertex stabilizer), and the maximal-stabilizer direction is **rank 1** — singular values
`[1, 0]` — i.e. a **product state** `v ⊗ w`, a tetrahedral vertex tensored with an icosahedral vertex.

**Method correction, recorded not hidden.** A first pass orbit-decomposed by rounding projective
coordinates and produced sizes that **do not divide 720** (68, 370, 423, …) — impossible by
orbit–stabilizer. That enumeration is **withdrawn**; the table above is derived from *stabilizer
orders only* (robust integer counts over 720 matrices) with `|orbit| = 720/|Stab|`. Same float-drift
failure as B1348's withdrawn step 4, caught the same way — by an invariant the answer must satisfy.

## R11's ARITHMETIC — and it is the point of the arc

R11: *"outputs − consumed anchors > 0, else the cell is vacuous (MB12)."* R7: *"every designer
freedom priced in a look-elsewhere ledger."* Both are now computable for the mirror row:

| | |
|---|---|
| **anchor cost, branch A** (the row needs **one** direction) | a **48-fold discrete selection** — `log₂ 48 ≈ 5.58 bits` |
| **anchor cost, branch B** (the row uses the **whole orbit**) | no selection, but the prediction becomes a **48-element set** — a 48-fold look-elsewhere on the comparison side instead |
| **outputs** | the mirror row is **one** row |

> **On either branch the inequality does not close.** One output against ~5.6 bits of selection, or
> one output against a 48-element target set. **R11 declares that vacuous before the seal.**

## THE RECOMMENDATION, stated as a result

> **Do not spend the last row.** Not now, and on this arithmetic not through this row at all — unless
> the mirror set's *"value set already exact"* (B1011 C6) is shown to carry **more than one
> independent output**, in which case the outputs are recounted and R11 is re-evaluated.

Three of four rows are spent with decisive misses. The fourth is unrepeatable. **A gating
computation that says "no" is worth more than a fourth miss**, and cheaper.

## What would change it

1. **Count the mirror set's independent outputs.** If it yields `k` genuinely independent numbers
   with `k > log₂ 48 ≈ 5.6` bits' worth, R11 closes and the arc becomes worth its shot.
2. **Cut the 48.** Anything that reduces the orbit — a Galois obstruction, a further canonical
   condition — improves the ledger directly. The Galois question at the point level is **open**
   (B1348's withdrawal left it so).
3. **A new licensed row**, derived not fitted (`F1` forbids fitting), added to `KIND_TABLE` under
   `R5` in advance.

## Fences

`F2` untouched, no comparison performed, no value read. **I-13 remains UNEARNED.** `R4`, `R5`, `R10`
stay as banked (discharged / existing / answered); nothing here re-opens them. And the same
exactification debt B1348 registered applies: the verdict rests on integers computed in double
precision, robust here because orbit–stabilizer checks them, but the exact `ℚ(ζ₆₀)` re-derivation is
**owed** for both arcs.

**Numbering note:** this arc takes **B1349**, the last id before the reserved range
`B1350–B1399` (E71). The next new arc on this branch needs a range grant.

---

# ADDENDUM — THE EXACTIFICATION DISCHARGED, AND GALOIS DOES CUT: 48 → 8

**Numbering note:** this is an **addendum to B1349**, not a new arc. `B1350–B1399` is reserved (E71),
so the work that discharges B1349's own debt is banked on B1349 rather than taking a reserved id.

## 1. The exactification, owed by B1348 and B1349 — now PAID

The instrument is rebuilt in **exact `ℚ(ζ₆₀) = ℚ[z]/Φ₆₀`** (`b1349c_exact_instrument.py`). Every
exponent lands in `(1/15)ℤ`, so every entry is a `ℤ`-combination of `ζ₆₀` powers:

> `T = diag(ζ₁₅^−², ζ₁₅², ζ₁₅⁸, ζ₁₅², ζ₁₅⁷, ζ₁₅⁸)`, and
> `S = (−i / 5√3) · Σ_w sgn(w) ζ₁₅^{−3⟨w(λ+ρ), μ+ρ⟩}` with `i = ζ₆₀¹⁵`, `√3 = ζ₆₀⁵ + ζ₆₀^−⁵`.

**Exact controls, all PASS with no float anywhere:** `S·S† = I`; `S = Sᵀ`; `C = S²` has entries in
`{0,1}` and **is** the charge conjugation `(a,b) ↦ (b,a)`; and **`(ST)³ = S²`**.

> **B1348's and B1349's registered exactification debt is discharged.** Their verdicts rested on
> integers over a float instrument; the instrument is now exact and the integers are unchanged.

## 2. THE GALOIS CUT — it works, and it is measurable

A direction with **rational coordinates in the weight basis** is fixed by *every* `σ ∈
Gal(ℚ(ζ₆₀)/ℚ)` automatically. So "does Galois cut the orbit" becomes **how many distinguished
directions are rational** — and that number, not the orbit size, is what R7 prices.

| sector | orbit size | **rational (Galois-fixed)** | anchor cost |
|---|---|---|---|
| **θ-odd** (B1348) | 12 | **2** — `[1:0]` and `[0:1]`, i.e. `f₁` and `f₂` | `log₂2 = 1` bit |
| **θ-even** (the crossing target) | 48 (×2 orbits) | **8** of the 96 maximal-stabilizer directions | `log₂8 = 3` bits |

The eight are the **four canonical weight basis vectors** — `e₍₀,₀₎`, `e₍₁,₁₎`, `e₍₀,₁₎+e₍₁,₀₎`,
`e₍₀,₂₎+e₍₂,₀₎` — plus four more with entries in `{0, 1, −½}`.

**Structure:** the 96 maximal-stabilizer directions are **two orbits of 48**, forced because `A₄` has
**two** classes of stabilizer-3 points (vertices *and* faces, four each): `2 × (4 × 12) = 96`. The
`4/4` split of the rationals between them is **indicated, not established** — it rests on the same
orbit keying that drifted (below).

## 3. R11, RECOMPUTED — still short, but by 3 bits instead of 5.6

| | before | after the Galois cut |
|---|---|---|
| anchor cost (even sector) | `log₂48 ≈ 5.58` bits | **`log₂8 = 3` bits** |
| outputs (the mirror row) | 1 | 1 |
| `outputs − anchors` | **−4.6** | **−2** |

> **R11 still does not close — but the gap is now 3 bits, and the recommendation changes shape.**
>
> **Before:** *"not through this row at all."*
> **Now:** *"**one more output than three and it closes.**"* If the mirror set's exact value set
> carries **≥ 4 independent numbers**, the ledger balances and the arc becomes worth its one shot.

**That is a concrete, checkable follow-up** where before there was none: *count the mirror set's
independent outputs.*

## 4. Two errors caught, both recorded

**(a) The rationality test accepted 1/φ.** With `tol = 1e-8` and denominators to `10⁴`, the Fibonacci
ratio `4181/6765` approximates `1/φ` to `~1e-8` — so six golden directions were reported as rational.
**In an instrument whose value set is the golden nine, that is the worst possible false positive.**
Fixed to `tol = 1e-11`, denominators to `1000` (where `1/φ`'s best approximation `610/987` is off by
`4.5e-7`), **and a control now asserts the test rejects `1/φ` and accepts `−½`.** The 14 became 8.

**(b) The orbit enumeration drifted for the third time.** It reported sizes `[48, 68]`, and `68 ∤ 720`.
The `48` and the two-orbit structure are established by orbit–stabilizer and by `A₄`'s two
stabilizer-3 classes; the enumeration is **not** used for any banked number. Third instance in three
arcs of the same float-drift failure, caught each time by the same invariant.

## 5. What the recommendation is now

**Still: do not spend the row yet.** But the reason has changed from *structural* to *arithmetic by a
measurable margin*. The next step is no longer "cut the 48" — that is done, `48 → 8` — it is:

> **Count how many independent numbers the θ-even mirror set actually carries.** Four suffices.

---

# ADDENDUM 2 — THE OUTPUTS COUNTED: the law is gcd(m,15), and R11 closes on ONE branch only

*Same branch, same arc id — B1350–B1399 is reserved (E71), so the work discharging B1349's own
stated follow-up is banked here.* Addendum 1 ended with one instruction: **"COUNT HOW MANY
INDEPENDENT NUMBERS THE θ-EVEN MIRROR SET CARRIES. Four suffices."** This counts them, and the
answer splits the row in two: **on 7 of the 15 words the ledger closes; on the other 8 it does not.**

## 0. FIRST: an instrument WITHDRAWN, and TWO of my own errors

**(a) `verification/b1349d_outputs.py` is WITHDRAWN as an instrument.** It computed
`h = v*(RᵐLᵐ)v` and compared **complex** values across ears. Read from their own artifacts,
B856 and B641 grade neither of those things:

| | what b1349d did | what B856/B641 actually grade |
|---|---|---|
| the word | `RᵐLᵐ` | **`C·RᵐLᵐ`** — charge-conjugation **welded** (B856 `weld`) |
| the quantity | complex `h` | **`Re h`** (B856 line 124 `h(1,u/nrm).real`; B641 `mp.re(A/ζ)`) |
| the ears | complex vectors | **real** (B856 `t·U3+(1−t)·U6`, both real; B641 `[3/5,4/5]`) |

**Which of the two deviations caused the failure, measured rather than assumed:** dropping `C`
turns out **not** to break ear-independence at all — since `C = −1` on the odd sector,
`Bᵀ(CP)B = −BᵀPB`, so `Re h` merely **negates** and stays scalar (checked, m = 1..5). What
b1349d's control actually tripped on was the **complex-vs-real** comparison: on the odd sector at
m = 1, `spread|h| = 8.5e−01` while `spread Re h = 1.1e−16`. **The complex coupling is
ear-dependent; its real part is not.** The missing `C` did one visible thing only — it flipped the
sign, which is why b1349d printed `h_odd(5) = +1` where B856 banks `h(5) = −1`.

**So the control did its job: it refused to let the even-sector number be read.** This is the E58
rule applied to my own paraphrase, not only to a relay: *a named finding is graded from its own
artifact.* A useful by-product: **`C` IS the θ-grading operator** — `C·B_even = +B_even`,
`C·B_odd = −B_odd`.

**(b) The pre-registration's decision rule was mis-derived.** b1349d pre-registered:
*"EAR-INDEPENDENT → outputs = 0, R11 can NEVER close."* That imported AC4's demotion
(*non-discriminating ⇒ useless on a bench*) into R11, which accounts something else. R11 prices
**consumed** anchors, and the anchor here is a *direction* (addendum 1 §3: "the row needs **one**
direction"). If the reading does not depend on the direction, **no direction is selected and the
anchor is not consumed.** Ear-independence therefore *helps* the ledger. The pre-registered rule
had it exactly backwards. Recorded, not reversed in silence.

**(c) A COUNTING ERROR OF MY OWN, caught by the test written against this addendum.** A first pass
computed `dim span{Q_m} = 6` by representing each form's `ℚ(ζ₆₀)` entries as 16-vectors of
power-basis coefficients and taking the rank **over ℚ**. That measures ℚ-linear independence of
*field elements*, which inflates by the field degree: `1` and `√5` are ℚ-independent but are both
real scalars. The quantity that means "how many independent numbers the readout carries" is
`dim_ℝ span{Q_m}` in `Sym₄(ℝ)`, and it is **3, not 6** — singular values `[4.11, 3.58, 2.45,
6.2e−16, …]`, an unambiguous gap. **The corrected count reverses part of this addendum's
conclusion** (§5): branch B no longer closes. The "6" is withdrawn.

## 1. The criterion is ALGEBRAIC, not statistical

For a real ear `v = Bc` in a sector with real basis `B` and Gram `G = BᵀB`:

> `Re h(c) = cᵀ·Sym(Re A)·c / (cᵀGc)`,  `A = Bᵀ(C·RᵐLᵐ)B`

so **`Re h` is ear-independent on that sector ⟺ `Sym(Re A) = λ·G` exactly.** No sampling, no
tolerance, no float — the question is decided in `ℚ(ζ₆₀)`. The Gram form carries the basis norms,
so nothing needs `√2 ∉ ℚ(ζ₆₀)` in order to normalise. This retires the float-drift error class
that bit B1348 step 4 and B1349 twice.

`verification/b1349e_ear_exact.py` — **12 controls, all PASS**: `S=Sᵀ`; `SS†=I`; `TT†=I`; `C²=I`;
`C=S²`; `ord(R)=ord(L)=15`; both Grams; `C=±1` on the two bases.

## 2. CONTROL — B856 reproduced from an independent exact instrument, and STRENGTHENED

| m | `h(U3)` | `Re h` | `|h|²` | `Sym(Re A) = λG` exactly? |
|---|---|---|---|---|
| 1 | `+0.309016994+0.425325404i` | `1/(2φ)` | `1/2 − √5/10` | **True** |
| 2 | `−0.5 − 0.688190960i` | `−1/2` | `1/2 + √5/10` | **True** |
| 3 | `−0.5 + 0.688190960i` | `−1/2` | `1/2 + √5/10` | **True** |
| 4 | `+0.309016994−0.425325404i` | `1/(2φ)` | `1/2 − √5/10` | **True** |
| 5 | `−1` exactly | `−1` | `1` | **True** |

`1/2 − √5/10 = 1/(φ√5)` and `1/2 + √5/10 = φ/√5`, summing to 1, and `h(5) = −1` — **B856's
banked values, recovered from an instrument that shares no code with it.** Two further independent
checks fall out: `h_odd(5) = −1` with `C = −1` on odd means `R⁵L⁵|_odd = +I`, which **is B856's
period-5 collapse** (ord 15 collapsing to 5 on the θ-odd form); and `m = 15` on the even side gives
`λ = 1` exactly, as it must, since `weld(15) = C·I = C = +1` there.

**Strengthened:** B856 reports ear-independence at `m = 1` numerically (spread `2e-16`). Here it is
an **exact identity for every m = 1..15** — the whole period, `Sym(Re A) = λG` on the nose.
(B641 is *not* reproduced: its five-tone census is over 360 group elements × 6 ears, a different
domain. B641 was read only to learn the graded quantity `Re(A/ζ)`.)

## 3. THE LAW — the θ-even readout is ear-dependent exactly on the UNITS of ℤ/15

`verification/b1349e_law.py`, **exhaustive and exact**. The verification is *complete, not
inductive*: `ord(R) = ord(L) = 15`, so `RᵐLᵐ` depends on `m` only mod 15 and `m = 1..15` is the
entire family.

> ### `Re h` is EAR-INDEPENDENT on θ-even ⟺ `gcd(m,15) > 1`.
> **Violations over the complete period: none.**

| | m | count |
|---|---|---|
| **ear-DEPENDENT** | `1, 2, 4, 7, 8, 11, 13, 14` | `8 = φ(15)` — exactly the **units** of ℤ/15 |
| **ear-independent** | `3, 5, 6, 9, 10, 12, 15` | 7 — the non-units |

`15 = ord(R) = ord(L)`, so the law reads: *the listener's direction matters precisely when the word
`RᵐLᵐ` still generates the full cyclic group.* Where `m` shares a factor with 15 the word
degenerates onto a proper subgroup and the even form goes scalar.

**Exact extra:** `tr(G⁻¹Q_m) = 0` for **all 8** units — the ear-dependent readings are
**traceless**. The row carries *no mean* there, only spread.

The ear-independent values are `λ ∈ {−1/(2φ), 0, 1/2, 1}` — **four distinct**, spanning a
2-dimensional ℚ-space `⟨1, √5⟩`. The odd sector, by contrast, is ear-independent for **every** m
and carries only **three** distinct values `{−1, −1/2, +1/(2φ)}`, with `Re h(m) = Re h(m+5)` exactly.

## 4. The ear-dependent readings LEAVE the field of the modular data

`verification/b1349e_charpoly.py`, `b1349e_field.py`. **Nothing here is identified by float
matching** — the b1349c trap (tol `1e-8` accepted `4181/6765 ≈ 1/φ`) is answered by proving every
closed form from its exact characteristic polynomial, `radsimp(got − claim) == 0`:

| m | charpoly of `G⁻¹Q_m` | spectrum = range of `Re h` over ears |
|---|---|---|
| 3, 12 | `(2λ−1)⁴/16` | `{1/2}` — scalar |
| 5, 10 | `λ⁴` | `{0}` |
| 6, 9 | — | `{(1−√5)/4 = −1/(2φ)}` |
| 15 | `(λ−1)⁴` | `{1}` |
| 1, 4, 11, 14 | degree 4, `64t⁴−56t²+1` | `(1/(2√2))·{±φ², ±1/φ}` — **all four proved** |
| 2, 7, 8, 13 | degree 4 | `(1/(2√2))·{±√5, ±1}` — **all four proved** |

Every one of the eight ear-dependent eigenvalues is `(1/(2√2)) ×` a unit of `ℤ[φ]`. **The `1/√2`
is uniform, not incidental** — and **`√2 ∉ ℚ(ζ₆₀)`**, proved twice: `Φ₆₀` stays **irreducible over
ℚ(√2)** (factor degrees `[16]`, so the compositum has degree 32 ≠ 16), and by Kronecker–Weber the
conductor of `ℚ(√2)` is 8, which does not divide 60. **Positive control:** `Φ₆₀` over `ℚ(√5)` and
over `ℚ(−1/(2φ))` factors as `[8,8]` — those *are* inside.

> **Structural reading.** The four ear-**independent** readings all lie in `ℚ(√5) ⊂ ℚ(ζ₆₀)`, the
> field of the modular data itself. Every ear-**dependent** reading generates `ℚ(√2,√5)` and does
> not. **Selecting an ear costs a field extension the modular data does not contain** — the same
> shape of statement as addendum 1's Galois cut, now on the value side rather than the direction side.

## 5. THE COUNT, and R11 — it closes on branch A, and FAILS on branch B

Over ℝ, in `Sym₄(ℝ)` (10-dimensional), with unambiguous singular-value gaps throughout:

| span | `dim_ℝ` | gap |
|---|---|---|
| `{Q_m : m = 1..15}` | **3** | `5.96e−01 → 6.19e−16` |
| `{Q_m : m` ear-dependent (units)`}` | **2** | `6.85e−01 → 1.08e−15` |
| `{Q_m : m` ear-independent`}` | **1** | `1.00e+00 → 1.59e−15` |

`G` lies in the span of all 15 (rank `3 → 3`) but **not** in the span of the ear-dependent ones
(rank `2 → 3`). Either way the **ear-discriminating directions number 2**. At the anchor ear
`e(0,0)` there are **8 distinct `Re h` values** over the period — but they lie in a 3-dimensional
space of forms, so 8 readings are not 8 independent outputs.

**The ledger, every reading tabled. Convention inherited from addendum 1: outputs as a count,
anchors as bits — the mismatch is not mine to fix, and the owner should pin it.**

| branch | anchors consumed | outputs | `outputs − anchors` | |
|---|---|---|---|---|
| **A** `gcd(m,15)>1` (7 words) | **0** — no direction is selected, so none is consumed | 4 forced values `{−1/(2φ),0,1/2,1}` | **+4** | **closes** |
| A, conservative | 0 | 1 (only `−1/(2φ)`, the lone value outside ℚ) | **+1** | **closes** |
| A, if ear-independence does **not** discharge the anchor | 3 bits | 4 | **+1** | **closes** |
| A, conservative **and** anchor not discharged | 3 bits | 1 | **−2** | fails |
| **B** `gcd(m,15)=1` (8 words) | 3 bits (addendum 1's Galois-rational directions) | 2 ear-discriminating directions | **−1** | **fails** |
| *addendum 1, for comparison* | 3 bits | 1 | **−2** | fails |

> ### R11 closes on branch A under three of its four readings, and fails on branch B under all.
> **The operational result: if the row is ever spent, spend it on a word with `gcd(m,15) > 1`,
> where no ear is selected at all.** Addendum 1 could say only "do not spend"; this says *which
> word to use if you do*. That is the arc's first positive instruction.

The closure **does** depend on grading calls — I claimed otherwise in a first draft of this
addendum, on the strength of the withdrawn "6", and that sentence is retracted. Two calls are the
owner's:

1. **Does ear-independence discharge the anchor?** §0(b) argues yes from R11's word "consumed".
   It reverses my own pre-registered rule, so it should be adjudicated, not assumed.
2. **Do `0`, `1/2`, `1` count as outputs?** They are forced and exact but rational, and arguably
   trivial; only `−1/(2φ)` leaves ℚ. Branch A closes on either answer *unless* the conservative
   count and the undischarged anchor are combined — the single reading on which nothing closes.

## 6. What this does NOT license — stated before the conclusion, not after

**R11 is an input-accounting gate, not a physics gate.** Closing it says the cell is not vacuous
under MB12; it says *nothing* about whether the row is right. The cautionary precedent is B856
itself, on this very quantity: its `|h|²` reading was **REFUTED ON KIND** — `sin²θ` is a
probability and `|h|²` is not one — and the surviving `Re h = 1/(2φ)` sat in a 1σ window holding
**at least 17 natural candidates**. A forced value is an output in the ledger's sense (the object
produces it with no input), which is exactly why it is *cheap*; it is not thereby a prediction.

Note also that branch A's forced values include `−1/(2φ)`, whose modulus is the odd sector's banked
`1/(2φ)` — the value B856 already took to a bench and could not discriminate. **Branch A's cheapest
output is a number the programme has already failed to cash once.** That is the honest reason not
to read this addendum as good news about physics.

## 7. Fences

F2 untouched. **No comparison performed, no value read against any measurement, nothing reaches
CLAIMS.md, Gate 5 untouched.** I-13 stays **UNEARNED** — its price is now *known, and affordable
on one branch of two*, which is a different statement from earned, and the one-shot rule still
means the row is consumed whatever the outcome. The arc verdict stays **NEGATIVE**: addendum 1
recommended *do not spend the row*, and this addendum changes the *reason and the shape* — the
ledger no longer forbids it on branch A — without itself recommending the spend. **What now gates
the row is kind-correctness, not arithmetic**, and on B856's own precedent that is the harder gate.

## 8. Duplicate check, run on the law before calling it new

`scripts/checks/already_banked.py`, two queries (the θ-even/ear/gcd terms, and the
`RᵐLᵐ`/period/coprime/cyclotomic terms). **No prior arc banks this law.** Top hits are B1349
itself and **B1011** (`ρ₆ = (χ⊗V₂(2I)) ⊕ (V₂(2T)⊗V₂(2I))`) — the *input*, already cited in
`depends_on`.

Worth recording as **neighbourhood, not duplication**: **B996** ("access to the McKay group is
generic across the metallic family") and **B997** ("the golden is the unique metallic grammar whose
own-conductor shadow is a McKay group") both compute over *the same words* `RᵐLᵐ` and both
discriminate within that family by a **number-theoretic condition on m**. This law is a third such
discrimination, and an independent one: neither B996 nor B997 mentions `15`, `gcd` or coprimality
(checked, not assumed), and their modulus is the SL(2,ℤ/N) shadow's conductor while this one is
`15 = ord(R) = ord(L)` in the SU(3)₂ modular data. Three separate arcs now cut the metallic family
by arithmetic in m; whether the cuts are related is **open and not investigated here**.

---

# ADDENDUM 3 — THE 4/4 SPLIT IS ESTABLISHED, AND BRANCH B TIES AT ZERO

*Same branch, same arc id.* Addendum 1 left one item explicitly **open**: *"the 4/4 split of the
rationals between them is **INDICATED, NOT ESTABLISHED**."* It is now established, exactly, and it
is not cosmetic — it changes the anchor.

## 1. The split, computed exactly

`verification/b1349f_orbit_split.py`. Every coordinate is an exact element of `ℚ(ζ₆₀)`; projective
canonicalisation is **exact division in that field** (`sp.invert` mod `Φ₆₀`), so two directions
compare equal iff they *are* equal. The orbit enumeration drifted **three times** on floats in
B1348/B1349 (sizes 68, 370, 423 — none dividing 720); here `|orbit| divides 720` is **asserted**,
not hoped for, and holds for all eight.

| orbit | size | \|Stab\| | the rationals it contains |
|---|---|---|---|
| **1** | **48** | **15** | `e₁ = (1,0,0,0)`, `e₂ = (0,1,0,0)`, `(1,0,0,1)`, `(0,1,1,0)` |
| **2** | **48** | **15** | `e₃ = (0,0,1,0)`, `e₄ = (0,0,0,1)`, `(1,0,0,−1/2)`, `(0,1,−1/2,0)` |

> **The split is `[4, 4]` over exactly two orbits, both of size 48, each with `|Stab| = 15`.**

A control the enumeration had to pass first: `R` and `L` restrict to the θ-even sector *exactly*
(`M₆·B_even = B_even·M₄`, verified symbolically), so the 4×4 action is the 6×6 one and not an
approximation of it.

**This also upgrades addendum 1's two-orbit structure from argued to verified.** Addendum 1 inferred
it (*"forced because `A₄` has two classes of stabiliser-3 points, `2 × (4 × 12) = 96`"*); the two
orbits of 48 are now enumerated directly. Scope: what is established here is that **the eight
rationals occupy exactly two orbits of 48, four each**. That the *whole* maximal-stabiliser set is
96 = 2 × 48 still rests on addendum 1's `A₄` argument, which this does not re-derive.

## 2. What it costs, and the full ledger

If the construction is confined to **one** orbit — which it is, whenever the orbit is *generated*
from a starting point rather than chosen — the anchor is `log₂4 = **2 bits**`, not `log₂8 = 3`.

| branch | anchors | outputs | `out − anch` | |
|---|---|---|---|---|
| **A** `gcd(m,15)>1`, anchor discharged | 0 | 4 forced values | **+4** | closes |
| A, discharged, conservative | 0 | 1 | **+1** | closes |
| A, **not** discharged, one orbit | **2** | 4 | **+2** | closes |
| A, not discharged, any of the 8 | 3 | 4 | **+1** | closes |
| A, not discharged **and** conservative, one orbit | **2** | 1 | **−1** | fails |
| A, not discharged and conservative, any of 8 | 3 | 1 | **−2** | fails |
| **B** `gcd(m,15)=1`, one orbit | **2** | 2 ear-discriminating | **0** | **fails — it TIES** |
| B, any of the 8 | 3 | 2 | **−1** | fails |

> ### Branch B is short by exactly nothing: at its best reading it reads `2 − 2 = 0`, and R11 requires `> 0`.

That is a sharper negative than addendum 2's `−1`. **One more ear-discriminating direction would
close it — and there is provably no third:** `dim_ℝ span{Q_m : m` a unit`} = 2` exactly (addendum 2
§5, unambiguous singular-value gap). Branch B does not fail for want of effort; it fails by one
dimension that the sector does not contain.

**Branch A is unaffected in substance** — it closes on four of six readings now instead of three of
four, and the two failures remain the same combination: the conservative output count *together with*
ruling that ear-independence does not discharge the anchor.

## 3. Unchanged

The verdict stays **NEGATIVE**, I-13 stays **UNEARNED**, F2 untouched, no comparison performed, no
value read, nothing reaches `CLAIMS.md`, Gate 5 untouched. Addendum 2's closing judgement stands
verbatim: **what gates the row now is kind-correctness, not arithmetic.** Making branch B's failure
exact does not make branch A's closure a physical result.

---

# ADDENDUM 4 — THE KIND GATE, FIRST STEP: BRANCH B IS EXCLUDED ON KIND TOO

*Same branch, same arc id.* Addendum 2 closed by saying **"what now gates the row is
kind-correctness, not arithmetic."** This asks the first kind question there is, and it is answerable
without any comparison to data: **does the reading land in the value set the corpus has already
banked for this sector?**

## 1. The banked set, and what is being compared

**B1011 C6, verbatim:** *"The θ-even value set, exact:
`{0, ±1/4, ±1/(4φ), ±1/2, ±1/(2φ), ±φ/4, ±φ/2, ±1}`"* — 15 values. `KIND_TABLE` carries it as the
**mirror set**, declared kind **amplitude-part**, bounds **[−1, 1]**, field **ℚ(√5)**.

**What is NOT claimed (E72 — one name, two quantities).** C6's set is a *census over group elements*
of `Re(ζ⁻¹ūMu)`; the values here are over the *15 metallic words* `RᵐLᵐ` with the charge-conjugation
weld. **The two quantities are not asserted to be identical.** What is tested is **containment** —
whether each computed reading is an *element* of the banked set and of its declared field. That is
all the kind question needs, and it needs no identification. `verification/b1349g_kind.py`, with a
two-sided control (the test accepts the banked values and rejects near-misses at `0.30`, `0.31`, and
`1/(2φ) + 1e−9`).

## 2. The result, and it splits the same way a third time

| branch | reading | in C6's banked set? |
|---|---|---|
| **A** `gcd(m,15)>1` | `−1/(2φ)`, `0`, `1/2`, `1` | **all four YES** |
| **B** `gcd(m,15)=1` | `φ²/(2√2)` ≈ 0.9256 | **no** (nearest banked `1`, off by 0.0744) |
| | `1/(φ·2√2)` ≈ 0.2185 | **no** (nearest `1/4`, off by 0.0315) |
| | `√5/(2√2)` ≈ 0.7906 | **no** (nearest `φ/2` ≈ 0.8090, off by 0.0184) |
| | `1/(2√2)` ≈ 0.3536 | **no** (nearest `1/(2φ)` ≈ 0.3090, off by 0.0445) |

**And it is the field, not an accident.** Branch A's four values lie in `ℚ(√5)`, the row's declared
field. Every branch-B reading carries a `1/√2` and generates `ℚ(√2,√5)`; `√2 ∉ ℚ(ζ₆₀)` (addendum 2
§4, conductor 8 ∤ 60), so *a fortiori* `√2 ∉ ℚ(√5)`. **A branch-B reading cannot be an element of a
set declared over `ℚ(√5)` — not approximately, but as a matter of field arithmetic.**

> ### Branch B is EXCLUDED ON KIND, independently of its `2 − 2 = 0` tie on the ledger.
> Two separate gates now reject it, and neither depends on the other: the R11 arithmetic ties at
> zero (addendum 3), and its values are not of the mirror row's declared kind. The near-misses make
> the point sharply — `0.7906` against a banked `0.8090` is the shape of a reading that would look
> like a near-hit to a fitter and is *structurally* not a member of the set.

## 3. What branch A earns, stated narrowly

**KIND-ELIGIBLE, which is not kind-correct.** Eligibility means the value *could* belong to the row:
right field, right bounds, and in fact an element of the banked set. It does **not** mean the row is
the right physical observable — that is precisely the question **B856 lost on its own sector**, where
`|h|²` was refuted on kind because a probability was read off an amplitude-squared, and the surviving
`Re h = 1/(2φ)` sat in a 1σ window with ≥17 natural candidates. **Nothing here touches that
question**, and branch A's cheapest output is still `−1/(2φ)`, whose modulus is the number that lost.

**A third independent signature of the same split.** The `gcd(m,15)` law now shows up three ways, and
the second implies the third: ear-(in)dependence; inside/outside `ℚ(√5) ⊂ ℚ(ζ₆₀)`; and inside/outside
B1011 C6's banked value set. **The programme's own banked law and this arc's computation agree
exactly on branch A and disagree exactly on branch B** — which is the strongest consistency check
available here, because C6 was banked before this question was asked.

## 4. Unchanged

Verdict **NEGATIVE**. I-13 **UNEARNED**. F2 untouched, **no comparison to any measurement, no value
read, nothing reaches `CLAIMS.md`, Gate 5 untouched.** The recommendation is still *do not spend the
row* — but the shape is now complete: **branch B is dead on two independent gates, and branch A is
arithmetically clear and kind-eligible with its outputs matching a law banked before the question.
What remains for branch A is the one thing this bench cannot settle by computation: whether the
mirror row is the right observable at all.**

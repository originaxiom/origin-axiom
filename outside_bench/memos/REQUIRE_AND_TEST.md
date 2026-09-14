# REQUIRE-AND-TEST — the programme inverted, and the first two requirements measured
## (outside bench memo 231, 2026-09-14; owner: *"craft a plan and execute it properly, until we figure out"*; register R145)

**Seals, all committed before their certificates were written or run:**
`seals/REQUIRE_AND_TEST_TARGETS.md` sha256 `5aba029321061eb6bb2d320e7108d5125dd7aaf17e65dfb11e2f530173a0318d` ·
`seals/REQUIRE_AND_TEST_CELL1_PREREG.md` sha256 `70bce752b759f090681c53dce2b21243b4a2400474aff47442b08fae871b45d6` ·
`seals/REQUIRE_AND_TEST_CELL2_PREREG.md` sha256 `67166376af6112d57b601b0aa0cfe9978ce57e634e9eea852af5be2ad21b4dcd`

**Certificates:** `certificates/require_and_test_cell1.py` → `outputs/require_and_test_cell1_out.txt` ·
`certificates/require_and_test_cell2.py` → `outputs/require_and_test_cell2_out.txt`

**Outcomes: CELL 1 = C:A · V:A · E:A — CELL 2 = OUTCOME B, D = DIFFERENT — CELL 3 = OUTCOME A — CELL 4 = OUTCOME I — CELL 5 = OUTCOME B (fork F9 FRAGILE).**
**All controls passed. Cell 3's control L1 failed on its first run; the cause is §2b and the seal was corrected by addendum, not rewritten.**

**Cell 3 adds:** `seals/REQUIRE_AND_TEST_CELL3_PREREG.md` (sha256 after ADDENDUM 1 `62e6af252a7a6c4b154b4f5168435f83b62293c5eb215505b5fd54e71f77012d`) · `certificates/require_and_test_cell3.py` → `outputs/require_and_test_cell3_out.txt`

**Cells 4–5 add:** `seals/REQUIRE_AND_TEST_CELL4_PREREG.md` (sha256 pre-addendum
`f846c6e7a68dad615136629ac3b66bebe8a04661dc589e319b84eb39d4e83338`) ·
`seals/REQUIRE_AND_TEST_CELL5_PREREG.md` (sha256
`3a8103c71d0429e1b6075f8b3770e365652dbda753d5bcbc818c6f99a18344a2`) ·
`certificates/require_and_test_cell4.py`, `certificates/require_and_test_cell5.py` ·
`outputs/require_and_test_cell{4,5}_out.txt` · `outputs/require_and_test_cell5_f9_maxlen5.json` · `seals/REQUIRE_AND_TEST_CELL6_PREREG.md` (sha256 `ba82e84adb3c7d3880fc097cb0aa1090b3459c5705606b091f2a7f858df8dd04`) · `certificates/require_and_test_cell6.py` → `outputs/require_and_test_cell6_out.txt`

---

## 0. Why the direction was inverted

R144 measured the programme's attention: 1246 arc directories in `frontier/`, **eight** on the choice
of object or the genesis axioms — **0.6 %**. The method has been *derive-and-see*: take m004, compute
what it gives. **The record already concedes the gap.** `frontier/B1028_freedom_ledger/ADDENDUM_2026-08-12.md`:

> The row priced the family choice at 0 "because no live alternative family was ever on the table" —
> **a fact about the programme's history, not a measurement of the object.**

Unacted for a month. And B749's fork **F1 (axiom A0) is excluded from computation by design.**

**The inversion.** Per requirement: *what must ANY object have to supply this — does m004 have it —
and how many objects do?* Four fields per cell: **R** (the requirement, verbatim), **P** (the predicate,
derived), **T** (m004 against P), **B** (the base rate over a named census, population printed).
**Without B, "m004 has P" is not information** — that is B282's genericity collapse and the four
NEGATIVE foreign controls B438/B440/B444/B445, which found 5₂ carrying the same structure.

---

## 1. CELL 1 — requirement 2 (chirality): B1163's theorem climbs the tower

**R** (`docs/TOE_REQUIREMENTS_LEDGER.md` §A row 2): *"left-handed doublets, right-handed singlets: a net
chiral spectrum, anomaly-free."*

**P** = the object has no orientation-reversing self-isometry. Derived in
`frontier/B1163_w0_attempt/ADDENDUM_orientation_theorem.md`: canonical = automorphism-invariant; the
mirror is an automorphism of an amphichiral object; orientation is mirror-odd; so *"an amphicheiral
object is structurally incapable of self-orienting."*

**T** = m004 **LACKS P**, by theorem. Recomputed here orientation-aware: `amphichiral_det(m004) = True`,
|Sym| = 8.

### The lemma

**Let M be an orientable finite-volume hyperbolic 3-manifold with an orientation-reversing isometry σ,
and let H ≤ π₁(M) have finite index with its conjugacy class fixed by σ\*. Then M_H is amphichiral.**

*Proof.* σ\*(H) = gHg⁻¹, so σ composed with the inner automorphism lifts to a self-homeomorphism of
M_H covering σ. The covering map is a local isometry and σ is an isometry (Mostow), so the lift is an
isometry; it reverses orientation because σ does. ∎

**Corollary — the falsifiable, non-circular prediction.** A subgroup cut out by a **characteristic**
quotient has a σ\*-fixed class **by construction, with no computation**. For a knot complement the
degree-n cyclic cover is ker(π₁ ↠ H₁ = ℤ ↠ ℤ/n). **So every cyclic cover of m004 must be amphichiral,
and one chiral cyclic cover refutes the lemma.** σ\*-fixedness is never inferred from the cover coming
out amphichiral — which is what would have made the test circular (#164).

**This generalises B1183, and the increment is stated as an increment.**
`frontier/B1183_one_class_theorem` proves the orientation obstruction (B1163) and the QP-4 chord
obstruction (B760) are **the same ℤ/2-torsor class under one global involution c**, because *"c is an
automorphism OF THE OBJECT: amphichirality on the geometry side … ⇒ no invariant selection."* The lemma
is that argument made functorial and carried up the covering tower.

### PART C = A — 29 chances to fail, none taken

Cyclic covers of m004 built directly from the abelianization for **n = 2 … 30** (the relator
`aaabABBAb` has exponent sums (a, b) = (1, 0), so H₁ is generated by b — the naive [n-cycle, n-cycle]
rep does **not** satisfy the relator and SnapPy rejects it). All 29 built, `type = cyclic`,
vol = n·vol(m004) to 1e−6 on every row, H₁ the Lucas–Fibonacci tower (ℤ/5, ℤ/4+ℤ/4, …, ℤ/832040+ℤ/4160200).

**All 29 amphichiral. 0 chiral. 0 undecided.**

### PART V = A — and the lemma is not vacuous

Re-derived here, not cited from B1324: covers to degree 7, **population 28** (asserted non-empty and
printed before any rate; the `B1197` trap).

| type | amphichiral | chiral |
|---|---|---|
| cyclic | 6 | **0** |
| irregular | 4 | **18** |

Chiral covers exist, so PART C has content. The 0 chiral cyclic covers is a second, independent look
at PART C through a different code path.

### PART E = A — and the escape route was measured, not adjudicated

The lemma's contrapositive says a chiral cover's subgroup class is **not** σ-fixed, so the mirror must
carry each chiral cover to a **different** cover — they must come in mirror pairs. That is a prediction
with a number.

> **18 chiral covers to degree 7. 9 mirror pairs. 0 unpaired.** (by degree: 5 → 1, 6 → 4, 7 → 4)

**So the tower does not supply the bit; it relocates it.** Choosing a chiral cover of m004 is choosing
one element of a free ℤ/2-orbit — **exactly one bit, exactly the bit B1163 proves the object cannot
supply.** The other three named routes: the partial filling is choice-consuming by the ledger's own
words (§E row 3, *"three discrete choices"*); m202 (chiral, |Sym| = 12, 2 cusps, vol = 4.059766) and
m129 (chiral, |Sym| = 8, 2 cusps, vol = 3.663862) **change the object** rather than construct from it,
so the lemma does not apply and neither is an equivariant route.

### Control C2 did real work

The orientation-**blind** test `is_isometric_to(mirror)` returns **True** for 5₂, 6₁ and m015 — all
three wrong, all three chiral. Had PART C used it, the cell would have passed vacuously. It is computed
in the certificate precisely to show it fails.

---

## 2. CELL 2 — requirement 1 (the gauge algebra): the door is common, and it is not the atom

**P_2T** = π₁(M) surjects onto 2T = SL(2, 𝔽₃) — chain link C6, *"the sole source of the McKay E₆"* (B266).

**The instrument is not the record's.** B282 uses Sage + GAP; **neither is installed in this container**.
Since |SL(2,𝔽₃)| = 24, homomorphisms are enumerated directly. Validated first against B282's six
published knots — **all six reproduce, the four zeros as load-bearing as the two hits**, and every raw
count is divisible by |Aut(SL(2,3))| = 24:

| | 4₁ | m003 | 5₂ | 6₁ | 6₂ | 7₄ |
|---|---|---|---|---|---|---|
| raw | 48 | 48 | 0 | 0 | 0 | 0 |
| ÷24 | 2 | 2 | 0 | 0 | 0 | 0 |
| B282 (GAP `GQuotients`) | 2 | 2 | 0 | 0 | 0 | 0 |

**The sweep.** `snappy.OrientableCuspedCensus`, one-cusped, **population 5000**; 0 skipped for
generator count, 0 errors, generator histogram {2: 4085, 3: 915}; 77 s.

> ### **P_2T holds for 1696 of 5000 = 33.92 %.  OUTCOME B.**

**B282 read its six-knot table as identifying the door with the arithmetic atom** — *"The only thing the
figure-eight has that nothing else does is that it is the unique arithmetic knot … If the bridge to
physics works, it must run through the arithmetic atom."* At census scale the correlation is gone.

**The confound is ruled out, not waved past.** B282's six were all knot complements, so the rate was
stratified (control K6):

| stratum | population | hits | rate |
|---|---|---|---|
| **H₁ = ℤ — B282's own population** | 2980 | 1024 | **34.362 %** |
| H₁ with torsion | 2020 | 672 | 33.267 % |

The rates agree. **The six-knot sample was unrepresentative; the sweep did not measure a different
population.**

**D = DIFFERENT — the door is not arithmeticity.** Against B1186's banked ℚ(√−3) shape-field family
(`family_census.json`: `census_size = 212641`, `B_shape_field_in_Qsqrt3 = 112`, i.e. **0.0527 %**): of
the 1696 hits, **7** are in that family (m003, m004, m206, m207, s118, s958, v2873) and **1689** are
not. Comparison over the swept range only; never extrapolated to 212 641.

**Absence line** (`absence_sweep.py "base rate of the 2T door"`, 13 heads enumerated): present only on
this bench's own commit `9ece633f` — **ABSENT on the other twelve heads**. Terms also run through
`already_banked.py`: "2T base rate", "SL(2,3) census", "surjections census", and separately
"canonical cover", "characteristic cover", "chiral cover", "require-and-test", "object requirement",
"characteristic subgroup", "canonical construction", "amphichiral cover", "equivariant" — which is how
B1183 and B1324 were found and cited above rather than reinvented.

---

## 2b. CELL 3 — requirement 1 (matter): the count of three, and two counts wearing one phrase

**P₃** = the object has an orientation-preserving cusp-fixing isometry with **|det(A − I)| = 3** — the
Pantev–Wijnholt localized count, in the frame B1321 uses: *"in PW's frame the localized count on a fixed
cusp is the fixed-point count of the rotation."*

**The sweep.** `OrientableCuspedCensus`, all cusp numbers, **population 4000**; 0 skipped; 113
orientation-**reversing** cusp-fixing rows rejected by control L3 rather than silently counted.

> ### **P₃ holds for 2 of 4000 = 0.050 %. OUTCOME A** — m202 and s959, two of the six B1321 found over 61 911.

**Requirement 1's three generations DOES do real selecting work** — the opposite of Cell 2's door. And
the distribution, which B1321 never asked for:

| max \|det(A − I)\| attained | manifolds | share |
|---|---|---|
| 0 | 405 | 10.12 % |
| **4** | **3595** | **89.88 %** |

| value attained somewhere | manifolds | share |
|---|---|---|
| 0 | 4000 | 100 % |
| 1 | 2 | 0.05 % |
| 2 | 3 | 0.07 % |
| **3** | **2** | **0.05 %** |
| **4** | **3595** | **89.88 %** |

**m004's multiset is exactly {0: 2, 4: 2}.** So m004 fails the 3 **while carrying the generic value**:
the count it supplies is the one nine manifolds in ten supply.

### The control failure, and why it is the more useful half

**L1 failed on the first run.** The seal demanded that m004's |det(A − I)| multiset contain **2**,
because `docs/TOE_REQUIREMENTS_LEDGER.md` §C row 2 says *"the object counts 2 at every fixed locus"*.
It returned {0, 4}. The instrument was right; **the seal imported a number from the wrong frame.**

**The record uses two different counts under one phrase:**

| quantity | on m004 | source |
|---|---|---|
| **\|det(A − I)\|** — the cusp fixed-point count (PW's localized count) | **{0, 4}** | `docs/MAIN_GOAL.md` ll. 80–84, quoting **B1295 as a banked NEGATIVE**: *"968 isometries, 1 376 cusp-fixing pairs, `\|det(A−I)\| ∈ {0: 882, 4: 494}`"* across all 87 covers to degree 10 |
| **χ(Fix g) = 1 − s_μ(g)** — the Euler characteristic of the fixed locus in the 3-manifold | **{0, 2}** | `docs/MAIN_GOAL.md` l. 87 |

**The "2" of "the object counts 2 at every fixed locus" is the second quantity. The "3" of B1321, and of
requirement 1's three generations, is the first.** They are not on the same scale — and the ledger row
carries the sentence with **no frame attached**, so the 2 and the 3 read as comparable when they are
not. This is **#26 in the wild**: a paraphrase is where the hypotheses go missing. It surfaced only
because a predicate must name its quantity, which a grade in a ledger need not.

**Handled by addendum, not rewrite.** ADDENDUM 1 to the Cell 3 seal corrects **only** the control's
expected value — to B1295's own {0, 4} — and changes nothing about the sweep, the population, the two
outcomes, or the second question. The first run's numbers stand. **χ is deliberately not swept across
the census**: the formula is stated in the record *for m004*, and generalising it would repeat the same
paraphrase error one level down.

**Second question, answered as sealed:** 2 is **not** modal in this frame (the modal attained value is
0, universal; the modal *maximum* is 4 at 89.88 %). m004's 2 — in the χ frame — is not a census default,
but neither is it comparable to the 3.

---

## 3. What the three cells say together

| requirement | P | m004 | base rate |
|---|---|---|---|
| **2 — chirality** | no orientation-reversing self-isometry | **LACKS**, by theorem | **181 / 203 123 = 0.089 %** are amphichiral (`outputs/l192_the_bit_out.txt` ll. 38–39, this bench's own sweep) — m004 is in the tenth of a percent that fails |
| **1 — gauge algebra** | surjects onto 2T | **HAS** | **1696 / 5000 = 33.92 %** |
| **1 — matter (three)** | a cusp-fixing rotation with \|det(A − I)\| = 3 | **LACKS**; its multiset is {0, 4} | **2 / 4000 = 0.050 %** — and **89.88 %** carry m004's own 4 |

**The three requirements behave in three different ways, and not one behaves as the chain reads it.**

- The requirement m004 **fails** on chirality is one **99.9 % of the census passes.**
- The requirement m004 **passes** is one **a third of the census passes** — so it does little
  selecting, and it is not the arithmetic atom B282 took it to be.
- The requirement m004 **fails** on the count of three is the one that **does** select — 0.05 % — and
  m004 fails it carrying the value 89.88 % of the census carries.

**So the selecting power sits where the object does not deliver, and the delivery sits where there is
no selecting power.** That sentence is the cells' joint content, and it is not visible from any single
arc, because no single arc carried a base rate.

**This is B282's own genericity collapse, extended one link further down.** B282 stripped the E₆ arc to
a single object-specific kernel — *"the arithmetic 2T atom"* — and said everything else was generic.
**Measured, the 2T atom is generic too.** What remains object-specific at C6 is the arithmeticity
(Reid), which the 2T door does **not** track.

---

---

## 5. CELL 4 — rows 3–8, and a correction to R144 that the seal required in advance

Rows 3–8 are mostly **assembly**, so the instrument is **citation verification**: every quoted line
asserted present verbatim in the file it is attributed to — the defect class `ERROR_LEDGER` **E2**
calls *"a reference table transcribed wrong at sealing"*. **17 of 17 verified.**

**The computable question.** `WHAT_WOULD_COUNT` §4A re-scoped the value tier — and its argument is not
disappointment but **E2/MB12 vacuity**, resting on three theorems. E2's own wording for the defect is
*"a sealed gate that **cannot pass for any genuine object**"*. So: **do those three theorems mention
the object?** Only each theorem's own statement was searched.

| theorem | object tokens in its statement |
|---|---|
| **B666 cell S** — the scale-torsor no-go (`docs/LAW_MAP.md`) | **NONE** — and it is verified on six named groups: *"Gal(L/ℚ(i)), 2I, PSL(2,7), 2I×ℤ/3, SL(2,ℤ/15), W(E6)"* |
| **B936** — value-invisibility | **NONE** — about E₆'s structure: X = T_ad[2] = (ℤ/2)⁶, H¹ = (ℤ/2)² |
| **B1096** — the anomaly layer is identically zero | **NONE** — about the SM's own 16, *"ν^c … is EXACTLY what cancels the last non-vanishing invariant"* |

> ### **OUTCOME I — OBJECT-FREE.** Row 3's base rate is **0 for every object** through these routes.

### The correction, preregistered before the run

**R144-4 wrote that when falsifier 2 fired the programme took reading (a) — *values are the wrong
success criterion* — and never (b) — *the object is the wrong object*. For row 3 that is too strong.**
Reading (a) is a **theorem** there, not a re-framing: the criterion cannot pass for any object, so it
carries no information about which object was chosen. §4A says as much in its own words — *"The
re-scope is licensed by discipline, not by disappointment"* — and this cell confirms the three
theorems it leans on name no object. **R144's diagnosis stands for the programme; it does not stand for
row 3.** The seal fixed this correction in advance so it could not be presented afterwards as the plan.

### The remaining rows, with what would make each computable

| §A row | verdict | what would change it |
|---|---|---|
| **4 dynamics** | **NOT-COMPUTABLE** | an action *derived*; §E row 1 lists six declared inputs |
| **5 gravity** | **NOT-COMPUTABLE** | *"containment, not a theory"*: a spin-2 slot, no propagator, no coupling |
| **6 quantum consistency** | **DOWNSTREAM** | anomaly-freedom is a property of a *closing*; it cannot discriminate objects until a closing is derived rather than chosen |
| **7 predictions** | a **regime**, not a value | P9 is conditional and sealed |
| **8 say which endpoint** | **NOT A CELL** | the only §A row whose status column is the ledger itself |

**Control M2 failed on its first run** — the seal's single probe was B1321's claim line, which names the
**sibling** (m202, s959), never the object, so the search correctly found nothing. **Second
mis-specified control in this programme; both were this bench's assumptions about the record, and both
were caught by a control rather than by re-reading.** Corrected by addendum to three probes exercising
three spellings — `m004`, `4₁`, `4_1` — because `ERROR_LEDGER` **E54** records a search that missed its
target *for lacking the digit spelling*.

---

## 6. CELL 5 — fork F9 past its declared bound: ROBUST becomes FRAGILE

**This is the "change the 0.6 %" item.** `frontier/B1323_the_genesis_upgrades/FINDINGS.md` §5 names its
own next step and no arc had taken it:

> that F9's ROBUST extends beyond **words of length 3** on the two punctured carriers (**a longer
> enumeration or a proof is the next step if anyone wants the general statement**)

**The instrument is the arc's own `part_c(maxlen)`, unmodified** (memo 154). `python-flint`, absent from
this container, was **installed** rather than substituted so the arc's code runs unaltered.

| | B1323's bound | this cell |
|---|---|---|
| word length | 2…3 | **2…5** |
| words | 332 | **10 684** |
| hyperbolic bundles | 64 | **2 256** |
| isometry classes | 4 | **35** |
| **F9 surface verdict** | **ROBUST** | **FRAGILE** |

> ### **OUTCOME B. Two three-record bundles keep the atom ℚ(√−3) at depth 4.**

**`abbC` → m412** (= otet05_00001), vol **5.074708** = 2.5 × vol(m004), 2 cusps, |Sym| = 8,
H₁ = ℤ/2 ⊕ ℤ ⊕ ℤ. **All five of its tetrahedron shapes have minimal polynomial x² − x + 1** — m004's
own shape, the regular ideal tetrahedron. **Chiral by both methods:** SnapPy's `is_amphicheiral` is
False, and all 8 isometries to its mirror are orientation-**reversing**, 0 preserving (B1235's lesson
respected). `uses_all_loops` True — a genuine three-record word. And the **record swap sends it to a
manifold with 0 isometries to it**, so the A7 bit is a class invariant on this carrier.

**`abAB` → L12n2208**, vol **12.179299** = 6 × vol(m004), 4 cusps, |Sym| = 48, **amphichiral** by both
methods (24 / 24): keeps the atom, forgets the bit — the other side of the same fork.

### What this does to the genesis

**m412 has BOTH the atom and a remembered handedness.** B1323's *"one may have the atom or the
remembered bit, not both"* does not survive depth 4, and the price it computed for A1's *"not one, not
three"* — *"the price of a third record is the atom"* — **is not the price.** FRESH_EYES **Q15** gets a
second, independent YES: B1324 found the coexistence on m004's own covering tower; it is now exhibited
on a genuinely different substrate, a three-record carrier.

### Fairness, stated plainly

**B1323 fenced this itself.** Its §5 says the statement is *"a computed fork over the enumerated set,
not a theorem about all carriers"*. **Its depth-3 verdict stands exactly as computed** — reproduced
here as control **N1**, all four classes matching to 1e−5 (m129 abC 3.663862; s780 acB 5.33349;
t12047 aB 7.327725; o9_44206 aaB 8.929318) with verdict ROBUST and no keepers. What does **not** carry
the fence is the sentence propagated into **B749's F9 addendum** — *"The price of a third record is the
atom"* — stated flatly there with no depth qualifier. **That propagation needs the qualifier.** B749 is
main-tree and is not edited from this bench; it is named here as a propagation item.

**Control N4 was the load-bearing one.** F9's verdict is an **absence**, and an absence computed by a
predicate that cannot return True is not evidence (#164). `all_in_Q(sqrt-3)` was first shown able to
fire, on m004's own shapes → True. N1, N2, N3 passed.

**Not concluded:** that F9 is ROBUST or FRAGILE for *all* word lengths, or for carriers other than
S₁,₂ and S₀,₄. B1323's scope line is kept verbatim with only the number 3 replaced by 5. The closed
genus-2 carrier stays out of frame (A5b). Nothing about physics. No value.

---

## 7. CELL 6 — the first named rival, scored on the same table

Cell 5 handed the programme something it has never had: **a named alternative object**. Cell 6 scores
it on the four predicates cells 1–3 measured base rates for, **using the same code paths** (cells 1–3
are imported, not re-implemented) with **m004 re-scored in the same certificate** as control.

| predicate | m004 | **m412** |
|---|---|---|
| **P_chir** — no orientation-reversing self-isometry | False | **True** |
| **P_atom** — shape field in ℚ(√−3) | True | True |
| **P_2T** — surjects onto SL(2,𝔽₃) | True | **False** (raw 0) |
| **P_3** — \|det(A − I)\| = 3 somewhere | False | False (multiset {0: 4, 4: 4}) |

> ### **OUTCOME B. m412 GAINS the chirality bit and LOSES the E₆ door.**

**The trade, a fifth time — and this time between two named objects on two named predicates.** The
record has it in B1323 (*"the atom or the remembered bit"*), B1321 (*"the price of the 3 is the golden
polynomial"*), B1294 (*"the 2 or the c-breaking"*), and Cell 1 §E (a chiral cover costs one free ℤ/2
bit). Here it is again: **the chirality bit or the McKay door, not both.**

**And the door m412 loses is the one 33.92 % of the census passes** (Cell 2). So "common across the
census" does **not** mean "automatic in the neighbourhood" — a nearby object in m004's own
commensurability class simply fails it.

**The commensurability question was answered, not skipped** (control P4): vol(m412)/vol(m004) = **2.5
exactly**, so m412 is **not a cover** of m004; but every one of its five tetrahedron shapes has minimal
polynomial x² − x + 1 — the regular ideal tetrahedron — so both are arithmetic over ℚ(√−3) and
**commensurable**. By `frontier/B803_commensurability_audit` — *"any derivation routing through it is
class-level not the object's specific"* — **m412's arithmetic face is inherited from the class, not
independent evidence for m412.** What is *not* inherited is chirality: it is not a commensurability
invariant, which is precisely why the two objects differ there and agree everywhere else arithmetic.

**The costs, fixed in the seal before the gains were seen:** m412 has **2 cusps** against m004's 1, and
the chain's C4/A1 carrier story and every one-cusped instrument (the D2 index frame, the
knot-complement dictionary) assume one. H₁ = ℤ/2 ⊕ ℤ ⊕ ℤ, so **m412 is not a knot complement** and
Reid's uniqueness of the arithmetic *knot* does not apply to it.

**Not concluded:** that m412 should replace m004 — that is the owner's call and a chain's worth of
work, not a four-predicate score. That m412 supplies physics: nothing here touches the SM. That these
are the right four predicates: they are the four this programme has base rates for, and no more.

## 4. INTERPRETIVE — labelled as such

The pattern across three separately-banked arcs is that every requirement this object fails is
available on a near neighbour, and every neighbour supplying it loses one of the three faces: B1323 F9,
*"one may have the atom or the remembered bit, not both"*; B1321, *"the price of the 3 is the golden
polynomial"*; B1294, *"the 2 or the c-breaking, not both"*. Cell 1 adds a fourth instance **inside** the
object's own tower — the chiral covers exist and come in mirror pairs, so the bit is relocated rather
than supplied — and **Cell 6 a fifth, between two named objects**: m412 gains chirality and loses the
McKay door. Five instances is no longer obviously a coincidence, but it is **not settled here** either:
what would settle it is a mechanism, and B1183's single involution c is the candidate the record
already has. Stated as a question, not a law.

## 5. What is NOT claimed

- **Falsifier 1 has NOT fired.** `WHAT_WOULD_COUNT` §5 falsifier 1 is *"no closing of this object yields
  chiral matter"* — strictly larger than anything here. What Cell 1 establishes is narrower: the
  record's *"chirality is an external input"* is a **theorem about equivariant constructions on m004**,
  over the four routes the seal named, rather than a description of where the programme stands.
- **PART C's reach is its population:** cyclic covers to degree 30. Not all characteristic subgroups,
  not all degrees.
- **PART E's reach is the seal's four named routes**, fixed before the run so the list could not be
  trimmed afterwards. It is not a statement about all constructions.
- **Cell 2 says nothing about E₆ beyond the door.** `frontier/B1258_2T_is_blind` proves the 27|2T
  branching character is identical for both candidate embeddings, so it cannot discriminate objects and
  was not invoked. Cell 2 also does **not** show m004 was wrongly chosen — only that requirement 1's
  door does far less selecting than the chain reads it as doing.
- **Cell 3 concludes nothing about generations as physics.** h¹ ↔ 4d generations is **I-26, a declared
  input** (`TOE_REQUIREMENTS_LEDGER` §E row 4, *"the dimension gap not exhibited"*). Cell 3's count is a
  fixed-point count on a torus and is reported as one. Its population is 4000 census members, not the
  61 911 B1321 searched; it recovers two of B1321's six and does not claim the other four are absent.
- **No value of anything. Gate 5 untouched. Nothing promotes to `CLAIMS.md`.**

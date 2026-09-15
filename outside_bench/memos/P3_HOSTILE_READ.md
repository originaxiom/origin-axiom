# MEMO 148 — THE HOSTILE READ OF P3 (THE PAPER)

**Banked 2026-08-29.** Seal: `seals/P3_HOSTILE_READ_PREREG.md`, committed and pushed **before**
any computation. Certificates: `certificates/p3_hostile_read.py`, `certificates/p3_hostile_h6.py`.
Outputs vendored. Subject: `papers/P3_THE_PAPER/main.tex` at **`89affd5b`**.

The paper's own SPEC names this cell twice — build-plan item 6, *"a hostile read before
submission"*, and the closing list of what remains before submission. This is that read.

---

## 0. VERDICT IN ONE LINE

**Six defects, none fatal, five of them repairable in one clause or one word each — and the two
strongest were found by the two BLIND cells, not the four confirmatory ones.** The paper's
mathematics survives every check this bench could run: the displayed anomaly forcing is exactly
right, the census numbers reproduce exactly in independent code, and Gate 5 is clean. What fails is
**the paper's account of its own mathematics**: in three places the text does not describe the
computation it reports.

| cell | blind? | outcome | what it is |
|---|---|---|---|
| **H3** | **BLIND** | **H3-GAP** | the paper's only theorem turns on an undefined word that the programme's own corpus uses for a different quantity |
| **H6** | **BLIND** | **H6-DIVERGENT** | §4's headline numbers reproduce exactly — and are not reproducible from the paper's text |
| H4 | confirmatory | H4-MISMATCH | the abstract undercounts the freedom ledger, in the paper's favour |
| H5 | confirmatory | H5-DANGLING | two of six falsifiers refute claims the body never makes |
| H2 | confirmatory | H2-CONFLATION | two different "exactly two" results juxtaposed as one |
| H1 | confirmatory | H1-DEFECT | the displayed derivation silently drops a branch |
| H7 | BLIND | **H7-CLEAN** | Gate 5 holds |

**The blind/confirmatory split earned its place in the seal.** The four cells I had scoped by
reading before sealing produced the four *weaker* findings. The two I had not scoped produced the
two that a referee would actually stop on. An adversarial reader's first-pass impressions were the
least valuable thing they produced, which is worth carrying as a method result.

---

## 1. WHAT SURVIVED — stated first, because it is the larger half

**The displayed forcing of §4 is exact.** Recomputed symbolically over ℚ, independently of the
corpus:

- the three linear anomaly conditions give **`Y_l = −3Y_q`, `Y_e = 6Y_q`, `Y_u + Y_d = −2Y_q`** —
  all three match the paper;
- the cubic on that line at `Y_q = 1`, `Y_u = −1+t` is **`−18(t−3)(t+3)`**, matching the paper
  **as an exact polynomial identity**, not numerically;
- the roots are `t = ±3` and the solutions are exactly `(1,−4,2,−3,6)` and `(1,2,−4,−3,6)`.

**The census reproduces exactly.** In own code, from the representation data alone:
**252 examined / 222 killed by the pure colour condition / exactly 2 surviving contents** — every
number the paper reports.

**Gate 5 is clean.** Every measured value in the draft (`sin²θ_W = 3/8`, the `16σ` run, `M_Z`)
occurs as a comparison target for a stated miss. Section 4, the paper's one explicit derivation,
contains the numerals `1 2 3 4 6 15 18 27 72 222 252` and nothing else — all dimensions,
multiplicities, counts and integral hypercharges. No measured value enters a derivation.

---

## 2. H3 — THE ONLY THEOREM TURNS ON AN UNDEFINED WORD *(blind; the strongest finding)*

Theorem 2.1: *among the metallic grammars `RᵐLᵐ`, exactly one has a modular shadow of McKay type,
namely `m = 1`.* Both halves of its proof check exactly:

- `|SL(2,ℤ/N)|` is a binary polyhedral order for **exactly `N ∈ {3,4,5}`** (24, 48, 120), verified
  by direct computation for `N ≤ 12`; and the paper's bound `6N³/π² > 120` for `N ≥ 6` is exact
  (at `N=6`: 131.31 > 120). The completeness claim is genuinely a proof, not a bounded search.
- `m²+4 = 3` has no solution, `= 4` gives the degenerate `m=0`, `= 5` gives `m=1`.

**The gap is the word "conductor."** The paper asserts *"the conductor of the metallic grammar
`RᵐLᵐ` is `m²+4`"* and never defines it. Computed exactly:

> `trace(RᵐLᵐ) = m²+2`, so the word's discriminant is `D = (m²+2)²−4 = m²(m²+4)`.

So `m²+4` is `D/m²` — the discriminant of the metallic number `x²−mx−1`, which the corpus calls
the **level** (`OPEN_LEADS` L42: *"k=3 is the golden level (n=5=m²+4)"*). It is **not** the
conductor under either available meaning:

1. **Standard number theory** — the conductor `f` of an order, `D = f²·d_K`.
2. **This programme's own usage** — `OPEN_LEADS` L39 writes *"f=8 (t=18, D=320=2⁶·5, the golden
   field with conductor 8)"*, which is exactly `320 = 8²·5`, the standard sense. My computation of
   `RᵐLᵐ` reproduces that row independently: **`m=4` gives `t=18`, `D=320`, `d_K=5`, `f=8`.** And
   `B204`/`L42` bank `content(RᵐLᵐ) = m`, which is that same conductor when `m²+4` is fundamental.

The slip is not harmless. Applying the standard order-conductor to the metallic number `x²−mx−1`
(discriminant `m²+4`), **three further metallic grammars acquire a McKay-type modulus**:

| m | m²+4 | d_K | conductor f | modulus | ⇒ |
|---|---|---|---|---|---|
| **11** | 125 | 5 | **5** | `|SL(2,ℤ/5)| = 120` | 2I (E₈) |
| **14** | 200 | 8 | **5** | 120 | 2I (E₈) |
| **39** | 1525 | 61 | **5** | 120 | 2I (E₈) |

Under that reading the theorem is **false**. Under the level reading it is **true**. The paper
gives the reader no way to tell which is meant, for its only formally stated theorem, using a word
its own corpus reserves for the reading that breaks it.

**REPAIR — one word.** Write *discriminant*, or *the level `n = m²+4`*. Nothing else changes; the
theorem's substance is sound.

---

## 3. H6 — THE HEADLINE NUMBERS ARE RIGHT AND NOT REPRODUCIBLE *(blind)*

§4: *"Over the Standard-Model-visible five-field alphabet there are 252 candidate hypercharge
contents. The pure colour condition alone kills 222 of them, and exactly two survive…"*

**Step 1, run as a referee — from the paper's text alone.** The sentence never says what a
"content" is, never lists the alphabet's letters, and never says how many fields a content
contains. Enumerating every reading its words support, exactly one yields 252 — *multisets of size
≤5 from 5 letters*, `C(10,5)` — and it is **structurally wrong**. A referee cannot reproduce the
number, and cannot tell a correct reconstruction from a numerical coincidence.

**Step 2, against the corpus.** The enumeration is over **multisets of size 5 from a SIX-letter
alphabet** `{A, a, B, b, C, D}` = `(3,2)`, its conjugate, `(3,1)`, its conjugate, `(1,2)`, `(1,1)`:
`C(6+5−1, 5) = C(10,5) = 252`. Re-run in own code: **252 / 222 / 2, exact.**

> **The alphabet has six letters, not five.** Five is the number of fields *in a content*, not the
> size of the alphabet. With a five-letter alphabet the count is `C(9,5) = 126`.

**And the two conditions doing the work are never stated.** The killer of 222 of 252 is
**`[SU(3)]³`** — the *pure* colour anomaly, containing no hypercharge at all. §4 displays
`[SU(3)]²Y`, `[SU(2)]²Y`, `grav²Y` and `[Y]³`, and **`[SU(3)]³` is not among them.** The
enumeration also applies the **Witten SU(2) global anomaly**, never mentioned. Both are correct
physics; neither is written down. So §4's displayed argument is not the argument that produces §4's
headline numbers — it is a different, narrower argument on a fixed multiplet.

**REPAIR** — name the alphabet's six letters, say the contents have five fields, and add
`[SU(3)]³` and the Witten condition to the displayed list.

---

## 4. H4 — THE ABSTRACT UNDERCOUNTS THE LEDGER, IN THE PAPER'S FAVOUR *(confirmatory)*

The §7 table has **seven** rows. Counted by type: 1 dimensionful (`ℓ`), 2 continuous dimensionless
(`σ`, `λ`), 1 projective (`ℙ(B₀)`), and **3 discrete/finite** — the chirality bit, the arrow label,
and *family, VEV, filling*.

The abstract says: *"a freedom ledger with one dimensionful unit …, two continuous dimensionless
anchors, a projective line of Higgs data …, and **two discrete labels**."*

One, two and one are right. **Three is not two.** The abstract drops the *family, VEV, filling*
row — and the direction matters: the omission **understates the construction's freedom**, in the
abstract, in the enumeration of the very table the paper calls *"the honest summary of the paper"*
and invites a hostile reader to audit. This is the finding a referee is likeliest to read as
motivated, and it is the cheapest to fix.

**REPAIR** — *"three discrete labels"*, or *"two ℤ/2 labels and a finite menu"*.

---

## 5. H5 — TWO FALSIFIERS REFUTE CLAIMS THE PAPER NEVER MAKES *(confirmatory)*

Mechanically checking every technical referent in §9 against §§1–8:

| term | in a falsifier | introduced in the body |
|---|---|---|
| registerable | yes | yes |
| gaugeable | yes | yes |
| projective Higgs | yes | yes |
| **anchored** (models) | yes | **no** |
| **odd-parity** (signs) | yes | **no** |
| **correlation** | yes | **no** |

Falsifier 1 turns on *"the two anchored models"*; §6 never introduces anchored models. Falsifier 2
says *"the paper predicts a **correlation**, not a value"* — and no correlation claim appears
anywhere in the body. **A falsifier matrix is the paper's contract with a referee**; two of its six
entries currently offer to be refuted on claims the paper has not made, which reads either as
carelessness or as inherited text.

**REPAIR** — introduce the two anchored models in §6 and state the sign correlation as a claim, or
strike falsifiers 1 and 2.

---

## 6. H2 — TWO DIFFERENT "EXACTLY TWO" *(confirmatory; **and this cell's first version was wrong**)*

> **BENCH ERROR #14, filed at the point of occurrence.** My first reading of this cell charged that
> *"and its conjugate"* mislabels the `u^c ↔ d^c` relabelling, since the charge conjugate of the SM
> is the SM up to overall scale. **That charge is false.** Exact enumeration shows the census's
> second survivor is a genuinely *conjugate content* — `aBBCD`, a different multiset of
> representations. My error was to treat the census's pair and the displayed derivation's pair as
> the same object — **which is precisely the conflation I then charged the paper with.** Recorded
> rather than quietly corrected; it is the third time this session an instrument of mine needed
> checking against itself, and the first time the instrument was my own reading.

The corrected finding, computed exactly. §4 reports two different results and juxtaposes them:

- **(i) the census** — 252 contents, **two surviving contents**: `AbbCD` (the SM 15-plet) and
  `aBBCD` (its conjugate content). The paper's *"the SM 15-plet up to overall scale, and its
  conjugate"* is **correct** here.
- **(ii) the displayed forcing** — on one fixed SM-shaped 15-plet, **two rays**, `(1,−4,2,−3,6)`
  and `(1,2,−4,−3,6)`, differing by swapping the two identical `b` letters.

They are not the same two. Under the census's own equivalence **(ii)'s two collapse to ONE of
(i)'s survivors**, and (i)'s second survivor never appears in the displayed computation at all.
The total number of chiral anomaly-free rays over all 252 contents is **four** — a number the paper
never states. Nothing marks the two results as different, so a referee reads the second as the
explicit form of the first.

**REPAIR** — one clause distinguishing *two surviving contents* from *two rays on a fixed content*.

---

## 7. H1 — THE DISPLAYED DERIVATION DROPS A BRANCH *(confirmatory; the weakest finding)*

§4 parametrises the solution line by `Y_q = 1`. That chart excludes `Y_q = 0`, and on that branch
the linear conditions give `Y_l = Y_e = 0`, `Y_d = −Y_u`, and **`[Y]³` vanishes identically** — a
one-parameter family of fully anomaly-free assignments `(0, s, −s, 0, 0)` for every `s`.

They are vector-like, so the paper's stated *chiral* filter excludes them, and the corpus's
enumeration excludes them correctly (my re-run's chirality filter is what removes them). **The
mathematics is right.** But the *displayed* derivation never says the branch was disposed of; it
sets `Y_q = 1` without remark. A referee checking the algebra will find the missing branch before
finding the reason it is empty.

**REPAIR** — one clause: *"`Y_q = 0` forces `Y_l = Y_e = 0` and a vector-like pair, so it is
excluded by chirality."*

---

## 8. WHAT THIS READ DOES NOT SAY

Bound by the seal, and worth stating plainly:

- **It does not say the paper is right.** Seven cells found what seven cells found, on a draft with
  **no bibliography** and **no per-claim citations**. Both absences are facts about the draft's
  stage that the spec already records, and neither is a finding of this read. A hostile read cannot
  certify; it can only fail to break.
- **It does not grade severity.** That is the owner's and cc's call. Every finding above is
  reported with the smallest repair that removes it, and five of the six are one clause or one word.
- **It did not check the corpus citations.** Every §5 and §6 claim is stated without an arc
  reference, so this read could not test whether the draft's rows match their arcs. That is the
  467-row disposition the spec already lists as outstanding, and it is the natural next cell.
- **The three defects that matter share one shape.** H3, H6 and H2 are all the same failure: **the
  text does not describe the computation.** The computations are right in all three. That is a
  better position to be in than the reverse, and it is also the failure mode a referee is best at
  detecting and least forgiving of, because from outside it is indistinguishable from not having
  done the computation.

## 9. GATE 5 AND STANDING

No measured SM value entered any computation in this cell; H7 *read* the draft for measured values,
which is not a derivation. Nothing was transmitted anywhere. `golden_gate` received nothing.

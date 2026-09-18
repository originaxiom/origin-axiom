# THE SUPPLIED LITERATURE, READ — three banked claims are pre-empted, one survives, and the field's walls are our walls

*Outside bench, memo 234, 2026-09-18. Occasioned by the owner's observation that the record checks
literature **per computation** and may never have checked it **per object**, and by the owner then
supplying the shortlist as PDFs — closing the egress gap the record's own **Q10** named.*

---

## 0. THE GRADING OF THIS MEMO, STATED BEFORE ANYTHING ELSE

**This memo is weaker than a sealed cell, and says so rather than burying it.**

The four outcomes — **CONFIRMS / SHARPENS / PRE-EMPTS / CONTRADICTS** — were fixed in the session's
plan **before any PDF was opened**, with the refuting outcome named first. But the lane was **frozen
at `8262c6ed`** under main's harvest hold, so **no seal was committed before reading.** The bench's
standard is seal-before-compute; this does not meet it.

**Why it is bankable anyway, stated as a reason and not an excuse:** every finding below is a
**verbatim quotation with a page or section number**, checkable by anyone holding the paper. A
preregistration mainly guards against outcome-shopping in a *computation*, where the analyst
controls the result. It does not do the same work for a quotation. **The reader should still treat
the grading as self-assigned.**

**Provenance.** PDFs supplied by the owner 2026-09-18. **They are not committed** — `audit/` is
gitignored by design (`.gitignore:11`), the papers are copyrighted, and the set is 27 MB. Identity
and venue are recorded here instead. Note: `pdftotext` drops overlines, so a representation written
`(n, n̄)` below extracts as `(n, n)`.

---

## 1. **PRE-EMPTED** — Zimmermann 1990, and it is three things at once

**B. Zimmermann, *On the Hantzsche–Wendt Manifold*, Monatsh. Math. 110 (3–4), 321–327, 1990.**
**Cited in ZERO files on every head** (`git grep -l -i zimmermann`, all 11 remotes).

### (a) B1273's headline identification is a 1990 theorem

p. 325, verbatim:

> *"Now take first the 2-fold branched covering of S³ along L′. We get again S³, and the preimage K
> of K′ is the **figure-8-knot**. Then take the **3-fold branched covering** of S³ along the
> figure-8-knot K to get M again."*

— M being the Hantzsche–Wendt manifold. **B1273** claims *"the 3-fold cyclic branched cover of m004
is the flat Hantzsche–Wendt manifold."* **Same statement, published 36 years earlier.**

He also exhibits the covering group: *"there exists a **diffeomorphism d of order 6** of M … such
that M → M/d³ = (S³, L) resp. M → M/d² = (S³, K) is the 2- resp. 3-fold branched covering of S³
along the Borromean rings resp. the figure-8-knot."* So **d² is our deck ℤ/3.**

### (b) Memo 233 v2's ℤ/3 is his Theorem

p. 322, Theorem:

> `1 → (ℤ₂)³ → Out π₁M → S₃ ⊕ ℤ₂ → 1`
> *"…i.e. the symmetric group S₃ operates by **permuting a, b, c**, and ℤ₂ operates trivially."*

p. 323, in the proof:

> *"S₃ = automorphism group of H = ℤ₂ ⊕ ℤ₂ = **permutations of the 3 nontrivial elements in H**."*

p. 322–323, Remark a), for `D := ST`:

> `D³ = abc, D⁶ = 1, **DaD⁻¹ = b, DbD⁻¹ = c, DcD⁻¹ = a**`

**That is exactly memo 233 v2's result** — the deck ℤ/3 permuting the three non-trivial elements of
the holonomy `ℤ₂ ⊕ ℤ₂` in a 3-cycle — which v2 derived from the Alexander module and reported as
OUTCOME A′. **The fact is Zimmermann's. v2's route is its own; the result is not.**

### (c) The record's D₄ is his Corollary

p. 326:

> *"**Corollary.** The symmetry group of the figure-8-knot is isomorphic to the **dihedral group of
> order 8**."*

The record carries this as *"m004's symmetry group is **D4 (order 8), amphicheiral** (own-verified,
SnapPy)"* — **with no literature source anywhere.** It is a 1990 published theorem, derived *from
the Hantzsche–Wendt manifold*.

---

## 2. **CONFIRMS + SHARPENS** — Dekimpe–Petrosyan on H₁

*K. Dekimpe, N. Petrosyan, **Homology of Hantzsche–Wendt Groups***, verbatim:

> *"In the classical case of dimension 3 there is only one HW-group. The 3-dimensional compact flat
> Riemannian manifold with this group as its fundamental group is called **didicosm** … **The first
> homology group of this manifold is ℤ₄².**"*

**CONFIRMS** B1273's `H₁(Y₃) = ℤ/4 ⊕ ℤ/4`, which this bench also reproduced twice (Smith form on
F(2,6); SnapPy's filled 3-fold cover).

**SHARPENS**, and this is new to us: dimension 3 is **exceptional**. *"In [10] Putrycz showed that
this is in fact an **exceptional case** and the first homology of any HW-group of dimension n ≥ 5 is
isomorphic to the holonomy group ℤ₂ⁿ⁻¹."*

---

## 3. The irony worth recording

**Szczepański, *Hantzsche–Wendt flat manifolds* (2002), "Problems and questions":**

> *"2. Find symmetries (outer automorphisms groups) of Hantzsche-Wendt manifolds (groups)"*
> *"4. Is there interpretation of the Proposition 4 in **knot theory** language?"*

**Both were answered by Zimmermann twelve years earlier**, in the paper that also computes our D₄.
A literature can lose its own results; so can we.

---

## 4. **NOT PRE-EMPTED** — Atiyah–Witten, and B1355 survives

**M. Atiyah, E. Witten, *M-Theory Dynamics On A Manifold of G₂ Holonomy*, ATMP 6(1) 2002, 105 pp.**
(`hep-th/0107177`). **Zero files on main**; on the SM head, `Acharya-Witten` 15 files, but **this**
paper is a different one and is absent.

**The decisive reading.** AW's finite-group quotients of the **CP³** cone are **cyclic only** —
§3.7, verbatim:

> *"Let Zₙ be the subgroup of U(1) consisting of the points of order dividing n, and let Xₙ = X/Zₙ …
> Xₙ is an orbifold with a locus of **A_{n−1} singularities** that is precisely the fixed point set
> of the U(1) action on Xₙ."*

Its **non-abelian** finite quotients are of a **different family** — p. 804 of the extract:
*"Y_Γ = **S³/Γ × S³**. Here Γ is a finite subgroup of SU(2)."*

**So AW never constructs the cone over CP³/2T.** B1355's local model is genuinely new ground.

**CONFIRMS B1355's claim 5** — that AW's route caps at A-type — and supplies AW's own structural
reason: quotienting by a subgroup *of the acting U(1)* forces the singularity type to be cyclic.
B1355's centraliser argument (`C_{Sp(1)}(2T) = ±1`) is the same obstruction stated group-theoretically.

**SHARPENS** — §3.7 case (I) is the **A-type template** B1355 generalises, and should cite:

> *"If X is the cone on CP³, the brane configuration that is a Type IIA dual of Xₙ consists of two
> copies of R³ meeting at the origin, each with multiplicity n. The associated low energy theory is
> a **U(n) × U(n) theory with chiral multiplets transforming as (n, n̄)**."*

**A numerology trap, named and refused.** AW §6.4: *"A frozen E₆ singularity has t = 3."* This is
**not** three generations — `t` is a Dynkin-index divisibility index, and a frozen singularity
*"**produces no gauge symmetry at all**"*; enhanced to E₇ or E₈ it yields SU(2) or G₂, not E₆ with
27s. The record already files Atiyah's own 2018 fine-structure numerology as a cautionary case; this
is the same shape and is refused here in advance.

---

## 5. **PRE-EMPTED** — Bourjaily on three families, and what it hands us

**J. L. Bourjaily, *Geometrically Engineering the Standard Model: Locally Unfolding Three Families
out of E₈*, arXiv:0704.0445.** **Zero files, both heads.**

§I, verbatim:

> *"That **three families emerge from E₈ is a general consequence of group theory** and can be
> understood from the fact that **E₆ × SU₃ is a maximal subgroup of E₈** into which the adjoint of
> E₈ partially branches into an **SU₃ triplet of 27's**."*

**B1271** states the same group theory: *"the 162 non-E₆, non-A₂ roots of E₈ fall into six classes of
27 … **(27,3)** and (27̄,3̄) … three full copies of the 27."* **PRE-EMPTED.**

**But it vindicates our own grading.** **B1031** already records *"THREE GENERATIONS: STRUCTURAL,
COUNT MATCHES — **NOT DERIVED**"*, and Bourjaily independently calls it *"group-theoretic and not
added by hand."* **The record's assessment of its own result matches the literature's.**

**It names the step we are missing.** B1271's transport ends **`N = 0`** — the (27,3) arrives with
its mirror, vector-like. Bourjaily's families are **chiral**, and the difference is the *unfolding*:
separating the isolated E₈ singularity into distinct codimension-7 enhancement points. He prices it:

> *"…we specify them all in terms of **only four complex structure moduli** which describe the
> unfolding of an isolated E₈ singularity."*

**That is the mechanism B1355 is trying to build, done one rank up, with a stated price.**

**And his walls are our walls** — his own §VI:

| his words | our counterpart |
|---|---|
| *"non-compact, the resulting theory is **decoupled from quantum gravity**, and the parameters … are **continuous**"* | gravity is containment only (B1140); 0 of 19 |
| *"It is an **assumption** of the framework that the precise global topology … can be ignored"* | I-26 UNEARNED |
| *"under what circumstances can a non-compact Calabi-Yau three-fold … be compactified? This is an important **question for mathematicians**"* | B1355: *"not constructed here or anywhere I know"* |
| *"**We are not presently able to answer why this does not happen**"* (why it stops at the SM) | — no counterpart; we have not asked this |
| *"our constructions **appear to depend on several seemingly arbitrary choices** … which roots were eliminated at each step"* | our chain is object-selected (B1270/B1271) — **a candidate advantage, no stronger**, since ours carries its own 12 declared inputs |

---

## 6. THE CITATION CENSUS

| cluster | main | SM head |
|---|---|---|
| Zimmermann | **0** | **0** |
| Szczepański / `didicosm` | **0 / 0** | — |
| Berglund–Brandhuber (`Matter from G₂ Manifolds`) | **0** | **0** |
| Bourjaily / `0704.0445` | **0** | **0** |
| Kovalev · twisted connected sum · Corti · Haskins · Nordström | **0 each** | **0 each** |
| — *covered, for contrast* — | | |
| Acharya–Witten | — | **15** |
| Bryant–Salamon · nearly-Kähler · Acharya–Gukov · Joyce | — | **4 · 5 · 2 · 2** |
| Porti · Falbel · Heusener · Guilloux (SL(3,ℂ)) | **501 · 106 · 61 · 40** | — |

**The pattern is not neglect — it is uneven coverage.** The arcs' own immediate sources are cited;
the *adjacent programme working on the same target* is not.

---

## 7. **BENCH ERROR #37 — filed against this bench**

Before reading, I reported to the owner that Atiyah–Witten studies the cone on CP³ **and**
*"additional examples obtained by dividing by a finite group"*, implying that combination is
B1355's object. **Reading the paper, it is not**: the CP³ quotients are cyclic, and the non-abelian
quotients are of S³×S³. **I conflated two clauses of an abstract** — precisely the failure the
`EXISTS-UNREAD` fence in the same plan was written to prevent, committed by the person who wrote the
fence. Caught only by reading the paper.

---

## 8. WHAT THE AFFECTED ARCS SHOULD BE TOLD

| arc | action |
|---|---|
| **B1273** (SM head) | its identification is Zimmermann 1990, p. 325 — cite, do not re-claim |
| **memo 233 v2** (this bench) | its ℤ/3 3-cycle is Zimmermann's Theorem p. 322 — the *route* is ours, the *result* is his |
| **B1271** (SM head) | its three-families mechanism is standard group theory, so stated by Bourjaily — cite; **B1031's grading stands and is corroborated** |
| **the paper** | D₄ = Sym(4₁) has a 1990 source; it is carried as *"own-verified, SnapPy"* with none |
| **B1355** (SM head) | **survives**; should cite Atiyah–Witten §3.7 as the A-type template, and *"anywhere I know"* should not reach the paper without a TCS check |

**Gate 5 untouched. Nothing promotes to `CLAIMS.md`. No value, no generation count, no physics
claim is made here — this memo reports what other people published.**

---

## ADDENDUM 1 (2026-09-18) — **§1(a) IS WRONG. B1273 CITED THE LITERATURE ALL ALONG. BENCH ERROR #38.**

**Nothing above is struck; §1(a) is superseded here.**

§1(a) reports Zimmermann 1990 as **PRE-EMPTING** *"B1273's headline identification"*, as though B1273
claimed the 3-fold-branched-cover ↔ Hantzsche–Wendt identification as its own. **It did not.**
`frontier/B1273_the_three_fold_closing/FINDINGS.md`, line 12, verbatim:

> *"**Y_n are the Fibonacci manifolds** (**Helling–Kim–Mennicke**: π₁(Y_n) = F(2,2n); F(2,4) = ℤ/5),
> and **Y₃ is the flat Hantzsche–Wendt manifold** (the didicosm…)"*

and its closing line reads *"Literature: Helling–Kim–Mennicke…"*. The record also carries the same
attribution in `docs/LITERATURE_SWEEP_2026-09-06_higgs_bundles_and_the_destination.md`, whose
Sources list ends: *"Helling, Kim, Mennicke, A geometric study of Fibonacci groups … (**the Fibonacci
manifolds as the cyclic branched covers of the figure-eight knot; Y₃ the Hantzsche–Wendt
manifold**)."* Counts: `Helling` main 2 / SM 11; `Mennicke` main 12 / SM 21.

**So the identification was never an uncited rediscovery.** What stands, narrowed:

| §1 item | corrected status |
|---|---|
| (a) the identification | **NOT a pre-emption.** B1273 cites Helling–Kim–Mennicke for it. Zimmermann is an *additional, earlier* source, uncited — a citation improvement, not a correction |
| (b) memo 233 v2's ℤ/3 | **stands** as far as checked: Zimmermann's Theorem p. 322 has it, and `zimmermann` is 0 files. **But I have not checked whether HKM or another cited source also carries the deck action** — so this is "Zimmermann has it", not "only Zimmermann has it" |
| (c) D₄ = Sym(4₁) | **stands** as far as checked: the record's own statement is *"own-verified, SnapPy"* with no source at that point. Same caveat as (b) |

### The error, named

**BENCH ERROR #38: I declared a pre-emption by grepping for the AUTHOR I had found, not for the FACT.**
`zimmermann` → 0 files was true and irrelevant; the fact was sourced under *Helling / Mennicke /
Fibonacci*. This is the standing rule — **exhaust the repo before ranking a gap** — failed at the
last step.

**And the aggravating detail, which is the real lesson:** I *commissioned* exactly this check. The
Explore agent dispatched earlier was asked, in these words, to report presence/absence for
*"Helling", "Kim", "Mennicke"*. **Its result never arrived, and I banked as though it had come back
clean.** A check you launch and do not read is not a check — it is worse than one you never ran,
because it buys false confidence.

### What this does not change

§2 (Dekimpe–Petrosyan confirming `H₁(Y₃) = ℤ₄²`), §4 (Atiyah–Witten; B1355 not pre-empted), §5
(Bourjaily pre-empting B1271's mechanism and vindicating B1031's grading), §6 (the census) and §7
(**#37**) are unaffected — each was checked against the arcs' own text, not by author-grep alone.
**§5's pre-emption should still be verified the same way before it is relied on**: B1271 may cite a
source for the E₈ ⊃ E₆ × SU(3) branching that I did not look for.

Gate 5 untouched; nothing promotes to `CLAIMS.md`.

### ADDENDUM 1, part 2 — **§5 IS TOO STRONG IN THE SAME WAY. #38 HAPPENED TWICE IN ONE MEMO.**

Checked, as this addendum's own table instructed. **B1271 never claims the E₈ ⊃ E₆ × SU(3) branching
as its own.** It writes the branching as the textbook decomposition it is —

> *"whose E₆ × SU(3) content **248 = (78,1) + (1,8) + (27,3) + (27̄,3̄)** *is* the three 27s and their
> mirror"*

— and states its actual contribution one line earlier:

> *"**The three generations are the three weights of the Eisenstein 3: three copies of the whole 27,
> permuted by the object's own order-3 element**"*

i.e. the identification of that order-3 element with the object's **founding ratio g = −RL⁻¹** on
B1270's icosian E₈ — answering B302/B308/B632's multiplicity question — together with the honest
negatives it reports in its own title and status line: *"the Yukawa E₈ forces on the triplet is
antisymmetric in the generations — hence zero"*, and **N = 0**.

**So Bourjaily pre-empts the branching, which B1271 does not claim, not B1271's contribution.**
Corrected status: **SHARPENS / CONTEXT, not PRE-EMPTS.** What remains true and useful is that
Bourjaily is uncited (0 files both heads), that he calls the three *"a general consequence of group
theory"* — corroborating **B1031**'s *"structural, count matches — NOT derived"* — and that he names
the step B1271 lacks: chirality from **unfolding into separated codimension-7 points**, priced at
*"only four complex structure moduli"*, against B1271's `N = 0`.

**#38 occurred twice in one memo, and the shape is one sentence:** I mistook *"the record states X"*
for *"the record claims X as its own"*. The difference is whether the arc cites — and in both cases
it did, in its own FINDINGS, in text I had already read. **The corrected rule: before writing
PRE-EMPTS, read the arc's own citation line, not a grep for the author the search happened to
surface.**

Of §1–§7, the findings that survive unchanged are **§2** (Dekimpe–Petrosyan confirming `H₁(Y₃) =
ℤ₄²`, plus the exceptional-dimension sharpening), **§4** (B1355 not pre-empted; AW quotients CP³ only
by Zₙ ⊂ U(1); the A-type template; the frozen-E₆ numerology trap refused), **§6** (the census) and
**§7** (#37). The pre-emption claims of §1(a) and §5 do not.

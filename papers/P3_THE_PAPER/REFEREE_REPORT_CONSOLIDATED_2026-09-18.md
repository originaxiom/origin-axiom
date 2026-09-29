# Referee report — consolidated

*On:* **Standard-Model structure from the figure-eight knot complement: what is forced, what is
withheld, and what must be supplied**

**This report supersedes the round reports** (`REFEREE_REPORT_2026-09-17.md`,
`…ROUND2_2026-09-17.md`, `…ROUND3_2026-09-18.md`, `…ROUND5_2026-09-29.md`), which remain in the
directory as the working record. Corrections issued in later rounds are **applied here**, not
appended: nothing in this document requires the reader to hold an erratum in mind while reading an
earlier section. That is the standard I am holding the manuscript to, so it is the standard this
report meets.

*Current as of round 5 (2026-09-29), against `main` at `987c0c8f`.*

---

## 0. Recommendation

**Minor revision on the mathematics. Major revision on what the paper reports.**

Every mathematical claim I could independently re-derive came out correct — now roughly seventy,
including several that cut against the paper's own thesis. The packaging defects I reported —
a drift gate that sampled, a runner that certified more than it ran, a manifest whose commit did not
resolve, a lock that failed on most hash seeds — **are fixed, and each fix was verified here**
(mutation test, behavioural run, exhaustive manifest audit, package run under the failing seed).

What is not fixed is the finding that matters most: **a manuscript that does not report its own
project.** It is demonstrable, it has misled three independent readers — this referee twice, and an
outside agent once (§5, §6) — and it got **worse** in round 5: the record gained four verified results,
the manuscript changed by two lines. A paper whose thesis is auditability cannot also be a poor index
of the work it audits.

---

## 1. Method

About sixty quantitative claims were re-derived from the manuscript's prose on a clean machine,
using no code or data from the project. SnapPy supplies manifold presentations, covers and
isometries; PARI/cypari supplies number-field arithmetic. **All characters, Fox calculus, ranks,
twisted cohomology, group theory, q-series arithmetic and field arithmetic in this report are this
referee's own implementations from the definitions.** Where a claim rests on a cited theorem, the
theorem was read at source.

Scripts: `referee_2026-09-17/scripts/` (v-series, round 1; r2–r11, rounds 2–4), each documenting its
own method and its own limits.

---

## 2. Verification ledger

### 2.1 Verified independently

| claim | result |
|---|---|
| §2 census counts, cell by cell, including the tie list | reproduces exactly |
| 66 of 87 covers chiral | reproduces, by **two** orientation-aware tests agreeing on all 87 |
| content census: two contents, four rays | reproduces |
| square-root uniqueness, with twelve controls | reproduces |
| Koide angle at 0.89 σ from 2/9 | reproduces (7.41e−6 / 8.35e−6) |
| Vol = 9√3 ζ_K(2)/π² | verified to **60** decimal places where the paper claims 32 |
| E₆: 72 roots, 120 A₂ subsystems | reproduces |
| hollow texture σ₁ = σ₂ + σ₃ | reproduces |
| 2O has exactly one involution; SL(2,ℤ/4) has seven | reproduces |
| anomaly bookkeeping: 252 = C(10,5); colour cubic kills 222; cubic −18(t−3)(t+3); SM hypercharges | reproduces |
| Menal-Ferrer–Porti hypotheses, read at source | the paper's account is **exactly right**, including n ≥ 2 |
| R27/SS7 m010 witness: V = (0,1,1,0), V* = (0,2,1,2), **I = +1** | reproduces; semisimplification gives 0; same trace on 400 random words |
| R30 finite-width vanishing: conjugation identity, f·v = 0, Betti table, chain homotopy | every pillar reproduces; **P ≠ 0 at all eight** non-trivial order-3 characters |
| tower Y₂–Y₅: identities, all five H₁, non-split locus counts | reproduce, including the 4 spurious on 661 |
| **h¹(χ²) = 1 at every non-split locus, every level** | verified across three prime fields |
| xB021: \|⟨A5,A6,A7⟩\| = 4, stabiliser order 2, orbit {0, ¼} | verified — and the orbit **is** {CS(m004), CS(m003)} |
| b₁ = number of cusps | verified on **all 57** manifolds used, no exceptions |
| Δ(m004) = t² − 3t + 1 from the Fox Jacobian, discriminant 5, separable | verified, no Sage |
| dim H¹(m004; Sym^m), m = 1…14 | 0 for odd m, 1 for even m; t₁ = 2a₁ at m = 2, 4, 6 |
| the DGG **3d index of m004**, rotated (0,0) entry | computed and matched to the published coefficients (§6) |
| the 3d index at **every** boundary class (GHHR eq. 16) | all eight published figure-eight classes reproduce — see §6 on one printed sign |
| m004 and m003 share the trivial-class index (B1428) | verified: identical through q⁸ |
| the full collection of classes separates m004 from m003 (B1431) | verified, complete over every class that could compete — with two corrections to its wording (§4) |
| CS(m003) = ¼; the orientation/order bits act trivially on the sister orbit (B1429) | verified; the 104 listed family classes and their counts reproduce exactly |
| E₆: 120 A₂ in **one** Weyl orbit (stabiliser 432); 720 commuting (A₂, A₁) pairs in one orbit (stabiliser 72); \|W\| = 51 840 | verified from the Cartan matrix |
| the fixes to F2, F3, F4 and the seed-dependent lock | verified — mutation test, behavioural run, exhaustive manifest audit, package run under the failing seed (§3) |

### 2.2 Not verified — and no part of this report endorses these

The measurement calculus of §5 (chain links C24–C42): Killing signature (2,2), the centraliser
lattice, the two cubic pencils and ℚ(√77), the magic-square isomorphism on 3003 basis pairs, the
real-form selection 𝔢₆₍₂₎, Hermitian signature (15,12), I = −1, the coupling normalisation — I
verified only the arithmetic of the surrounding integers. Everything about the closings (19 624
vacua, 706 464 SM lines, 34 752 / 31 488 / 768, the Z′ regime). The index computations themselves
(the 542 firing modules, the 235 on the reducible locus, the non-zero values on s958/v2873/t12833/
t12835/o10_150701/t12839, the 61 + 12 vanishing sectors, the 38 070 multi-cusped sectors) — I
verified the *theorem* behind the vanishing and the *lemma* (symplectic self-duality), not the runs.
The ledger rows σ, λ, ℙ(B₀); the seven crossings; the 352-pair period scan; the 216-cell regulator
grid; the G₂ orbifold with b₂ = 0; the genesis uniqueness theorem (144 candidates to one). The
80 800 count, the one-per-background law, the exact ℚ(ζ) runs; B1351, B1367, B1368. From B1366 /
the embedding claim, the three hypercharge directions among 28 513 and the 8 177 branchings (its
orbit facts *are* verified). The 3d index's retriangulation invariance (my own control only
exercised relabelled two-tetrahedron triangulations), and the membership of B1429's 112-member family.

For these I confirmed only that a lock exists and, with the exceptions in §3, that it passes. The
paper's own appendix is right that *"a lock is traceability, not re-derivation"*, and it should keep
saying so as plainly as it does.

---

## 3. Findings requiring action

### F1 — The paper does not report its own project *(most important)*

Results banked in the record, several of them the strongest work in the project, and absent from the
manuscript:

| banked result | where | in the paper |
|---|---|---|
| one chiral generation on the tower; the h¹ = 1 mechanism | B1374 / B1375 | **no** |
| the withheld bits are the object's own stabiliser (a fixed point cannot report on its own stabiliser) | xB021 | **no** |
| the parameter budget **clears 19** at the tower's ceiling — L14n63694, k = 5, dim_ℂ H¹(sl₃) = 10 → 20 real — **and is entirely boundary data, zero interior moduli** | B1409 / L219 | **no** |
| the surviving gauge group is abelian of dim ≤ 4, or trivial for the geometric holonomy | B1336 | **no** |
| the price: 4 axioms spent, **0 of 19** bought, "the two do not convert" | B1261 | **no** |
| k(n−1) ≈ 10 as a programme-level filter | L217 | **no** |
| "the object supplies every space and never a point" — eight banked instances | H5 / I-13 | **no** |
| no hyperbolic knot has a cyclic-cubic trace field | B307 | **no** |
| every Sym^n of SL(2) is self-dual ⟹ net chirality ≡ 0 (error class E65, cost four arcs) | B1260 / E65 | **no** |
| the DGG lane: T[4₁] = U(1) + 2 chirals from the NZ datum; abelian at all K, adversarially sourced | B488 / B528 | **no** |
| *added round 5:* the 3d index of the object, computed; m004 and m003 share the trivial-class series | B1428 | **no** |
| *added round 5:* **the full collection of classes separates m004 from m003** — a second separator besides Chern–Simons, which §2 presents as the only one | B1431 | **no** |
| *added round 5:* the orientation and order bits act trivially on the whole sister orbit; the information lives on the family | B1429 | **no** |

**Status (round 5): not addressed, and wider.** The manuscript changed by two lines since round 2; the
record gained the last three rows, each verified here. The author has said so explicitly (*"Nothing
about what belongs in the paper is decided here"*, S22), so this is a deferral, not an oversight — but
it is the finding the verdict turns on.

**Evidence that this misleads.** Round 2 of this review answered several of the author's questions
from the manuscript alone and got them wrong — "seven routes, all negative" is false, the tower
route is positive. Round 3 then presented as new a set of results the record already held. And an
outside agent, reading the paper, concluded the record had *"never entered"* the 3d-3d literature —
on which it has 176 files, a 99-agent adversarial deep research, and a computed T[4₁]. Three
independent readers, the same error, from the same cause.

**Requested:** bring the manuscript level with the record. At minimum the tower's generation, the
stabiliser diagnosis, B1409's budget-and-boundary result, B1261's price — and, in §2, B1431's second
separator of the object from its sibling.

### F2 — The chain table ships a stale row, and its gate samples 9 of 57 — **FIXED**

Row-by-row comparison of the generator's 57 rows against both `main.tex` copies: **exactly one row
is stale** (link 43 — generator 0.8 %, paper 0.9 %). It sits in the unchecked middle, and it is
present in the repository tex, the arXiv bundle tex, **and the submitted PDF**. The drift gate
(`tests/test_paper_chain_table.py`) samples 9 of 57 rows and cannot see it.

**Requested:** fix the row; make the gate read all 57.

**Status (round 5): fixed, and verified by mutation.** 0 of 57 rows stale on `main`; a drift planted
in row 30 — outside the old `rows[:6] + rows[-3:]` sample — makes the gate fail; restored, it passes.

### F3 — The machinery asserts more than it evidences — **FIXED**

- `anc/REPORT.md` certified **PASS** on a seals-only run. It stated a verdict broader than the run
  behind it.
- `verification_package/run_package.py`: `all_ok` initialises **True** and is `&=`-ed only by steps
  that actually ran. A skipped step cannot turn it false.
- *Found by the author, not by me, and worse than either:* a lock that failed on six of eight hash
  seeds (E83). My own round-2 "clean green" was a lucky draw on it (§5).

**Status (round 5): fixed, and verified by running it.** A seals-only run now reports
`PASS (partial: only seals ran)`; a default run names its steps. The package passes end to end under
**both** seeds that broke the pre-fix lock (`PYTHONHASHSEED` 0 and 1): seals 21/21, 148 lock files,
743 passed, 14 skipped, 0 failed, each. Two seeds show the known failure is gone, not that no other
exists; the author's own order-sensitivity sweep (E83, L222) is the instrument for that.

### F4 — The manifest's recorded commit does not resolve — **FIXED**

Reported in round 1, unfixed in round 2. `git_head` named a commit that did not contain the
artefacts the manifest lists.

**Status (round 5): fixed, and verified exhaustively.** The manifest records `07c0b604`, published,
clean tree, 3 458 commits, not shallow — each true. That commit contains **all 442** listed artefact
paths and **all 80** record directories, and **all 21** seals hash to their recorded values there.

### F5 — Framing

The title and abstract promise more than §4's scope note delivers. The 53/57 ratio should be
demoted. The abstract should say, as §7's scope note already does, that the index is **a count of
twisted classes, not a four-dimensional index**. This is the one item that decides whether the paper
is read as what it is — a carefully drawn boundary — or as what its title suggests.

### F6 — Citation gap

The object is the canonical worked example of the 3d-3d correspondence (Dimofte–Gaiotto–Gukov
1108.4389 §2.4 derives its A-polynomial as the theory's Lagrangian), the project's own record
engaged that literature years ago, and the manuscript cites none of it: Dimofte 0, Gaiotto 0,
Gukov 0, 3d-3d 0, 3D index 0, chiral multiplet 0, A-polynomial 0. **Status (round 5): unchanged** —
while the record now computes the index itself (B1428) and uses it to separate the object from its
sibling (B1431).

### F7 — Smaller corrections — **FIXED**

Figure 1 caption (52 → 53); sin²θ_W stated as 0.9 % where it is 0.822 % — one of three sites had
survived; the manifest's "records"/"pairs" wording. **Status (round 5):** sin²θ_W reads 0.8 % at all
three sites; the caption reads fifty-seven links. The author also found and fixed, unprompted, the
retraction count the paper cites (27 → 29). Round 1's items 1 (`.gitignore` / the B1419 census) and 4
(census-drift population) were properly fixed in round 2, the first generalised to a sweep and locked.

---

## 4. On the questions behind the paper

Presented here with round 3's corrections already applied; credit sits where the record earned it.

**The count is one, and there is a mechanism.** On the tower, on non-semisimple backgrounds, exactly
one chiral generation appears. The reason is h¹(χ²) = 1 at every non-split locus — verified here
across three prime fields, independently of the record's own runs. That mechanism is B1374/B1375's.

**Three is out of reach by this mechanism.** Scanning every cover of m004 to degree 8 plus the named
family — 42 manifolds, 21 360 genuine extension loci — gives h¹ = 1 (20 904) and h¹ = 2 (456) and
**h¹ = 3 zero times**, with the twos occurring only on multi-cusped covers. On one-cusped manifolds,
where the index instrument is defined and where Jørgensen minimality has anything to say, h¹ is 1 in
all 1 056 loci with no exception. The count is a corank bounded by b₁; b₁ = 1 because the object is
the minimal **one-cusped** manifold; so the fact that selects the object is the fact that caps the
count.

*A trap worth recording:* a raw scan reports 32 loci at h¹ = 3 on degree-7 covers. Those χ have
order 2, so χ² is trivial and h¹ = b₁ = 3 for free on a three-cusped cover. All 32 are spurious.

**Is that a theorem?** **No, and it is not closed by B307 either** — a correction to round 3 §9,
which claimed it was. B307 proves no hyperbolic *knot* has a cyclic-cubic trace field, hence no
symmetric triple of embeddings; that is a statement about **trace-field Galois multiplicity**, not
about the corank of a Fox Jacobian, and most manifolds in the scan are not knot complements. B307
itself says so, and routes the remaining possibility to *"the arithmetic of the whole
commensurability class, not a single object's trace field."* **That is precisely what the scan
above probes.** So the scan is evidence on the one route B307 leaves open, and the question — is
there a genuine extension locus with h¹(χ²) = 3 anywhere in the commensurability class, at any
degree — **remains open**. Alexander separability plus B1260's reciprocity is the shape a proof
would take.

**Why the parameters do not come out.** Not nineteen failures — one obstruction. Every instrument is
equivariant, and every parameter is a coordinate the symmetry moves. xB021 sharpens it: the withheld
bits are the object's own stabiliser. The record states the consequence itself (B1261: 4 axioms
spent, 0 of 19 bought, and the two do not convert; L217; H5). **Enriching the construction does not
escape it:** the coefficient enrichment fails at the root because every Sym^n of SL(2) is self-dual
(B1260/E65); the flat-connection route fails because every available centraliser is abelian of
dimension ≤ 4 against the Standard Model's non-abelian 12 (B1336); and the room that does exist, at
the tower's ceiling, is entirely boundary data with no selector (B1409/L219).

---

## 5. Errors in this review

I praised this paper for documenting where it fell over. The same standard applies here.

| error | how caught | cost |
|---|---|---|
| chirality sweep returned 87/87 amphichiral | SnapPy's default isometry test is orientation-blind — **the paper's own documented error class** | none; fixed, two tests then agreed on all 87 |
| ζ_K(2) under-converged via `mp.nsum` | disagreed with the closed form | none; fixed to 60 dp |
| Koide off by a 2π/3 phase convention | control | none |
| over-claimed a re-derivation of the arithmetic-filling fields | own re-check | committed a precision "fix" before the real derivation; then found the cusped-vs-filled instrument error |
| `algdep` accepted spurious relations at 60 digits | positive control | would have banked a wrong minimal polynomial; fixed with a coefficient bound |
| paraphrased Menal-Ferrer–Porti wrongly from a summary | read the source | the paper was right and I was wrong |
| **"seven routes, all negative"** | reading the record | **wrong**; the tower route is positive |
| reviewed the paper as if it were the project | the author's correction | two rounds of misdirected verdicts |
| presented §§7–8 as new when the record already held them | repo sweep | rounds of duplicated work |
| longitude search required both exponent sums zero when only their sum must | the control returned "no longitude" | a silent false negative |
| asserted a bare triality for the tetrahedron index | the control **fired** — false on 38 of 49 pairs | caught before publication; true relation derived and verified on all 49 |
| compared the 3d index against the wrong published series | reading which object each series is | a false mismatch report |
| claimed B307+B1161 subsume the h¹ = 3 question | re-reading the records | **corrected in §4 above** |
| **"`main` is 101 commits — a curated line"; two lanes "share no history with `main`"** | **the author** (S20/S21) | my clone was shallow; `main` was 3 457 commits and every lane shares root `517783f2`. The structural framing is withdrawn; the substance — lane results absent from the paper — was read, not counted, and the author confirmed it |
| **round 2's "clean green … a green you had earned"** | **the author** (E83) | one run of a suite containing a lock that fails on six of eight hash seeds; I drew a passing one. A correction "in the author's favour" rested on luck |
| graded the relay's "proven Dehn-filling law" as overstated | the author's lead L225 | I read one abstract; Celoria–Hodgson–Rubinstein (arXiv:2509.09886) prove it |
| called the author's 3d index an "independent convergence" with mine | reading their commit | they computed the un-rotated index, I the rotated (0,0) entry: different series |
| wrote S23's truncation bug into my own general implementation (the running product) | reading my code before the first run | none |

The pattern is worth naming, and it changed this round. Most errors were caught by a control written
before the answer was known — the paper's own method. **The two that mattered most in round 5 were
not: the author caught them.** Both have the shape the author named in S20 — *"a check satisfied by
an incomplete view of its own evidence is not a check"* — a depth-limited clone read as the history,
and a single run of a seed-dependent suite read as a green. A referee is not exempt from the
methodology being checked.

---

## 6. In the paper's favour

**The discipline is real and it is checkable.** I tried to catch this paper out on §2 and instead
reproduced it to the digit, including counts that cut against it. I reproduced its *errors* too, in
the same place, because it had documented them well enough for me to fall over there.

**The negatives are stated at the right strength**, and several are genuinely clean: the hollow
texture, the involution count, the square-root uniqueness with its twelve controls, the flat-bundle
obstruction the authors turn against their own positives. The "Recognition" section is a model.

**The central negative survives its most natural outside challenge.** An outside relay set the
non-trivial DGG 3d index against the paper's I = t₀ − r₁ = 0. Reading both sources, that is a
category error: the 3d index is an element of ℤ((q^½)) counting BPS states of T[M] on S²; the
paper's index is an integer difference of twisted-cohomology dimensions on M. To settle it rather
than assert it I computed the 3d index of m004 from Garoufalidis's tetrahedron index and the
two-tetrahedron state sum — **1 − 8q − 9q² + 18q³ + 46q⁴ + 90q⁵ + 62q⁶ + 10q⁷ − 170q⁸**, matching
every coefficient Garoufalidis–Gu–Mariño print, with one term further. It is non-trivial, and it
does not bear on the paper's negative, which stands.

**It does bear on the paper's §2**, which I had wrongly said it did not. Computed at every boundary
class (GHHR eq. 16, all eight published figure-eight classes reproduced), the trivial class of m004
and m003 agree — but the full collection separates them, with witnesses in both directions, complete
over every class that could compete (B1431, verified here with two corrections to its wording). §2
presents the Chern–Simons invariant as the one thing the construction uses that tells the object
from its sibling. There is now a second.

*A note on the literature, since the check depended on it:* the arXiv source of GHHR (1604.02688,
Example 4.1) prints I(μ) = **+2q** − 2q² + …; the same example's explicit formula gives **−2q**, and
reproduces all seven of its other printed series exactly. The printed sign is a typo. The project's
B1428 targets −2q, citing the journal version, which I could not access to see whether it was
corrected there.

---

## 7. Requested changes

**Open:**

1. **Bring the manuscript level with its record** (F1) — the tower's generation, the stabiliser
   diagnosis, B1409's budget-and-boundary result, B1261's price, and in §2 B1431's second separator of
   the object from its sibling.
2. Title, abstract, the 53/57 ratio, and the index wording (F5).
3. Cite the 3d-3d literature the object is the canonical example of (F6).

**Done, and verified in round 5:** the stale chain-table row and the sampling gate (F2); the runner's
verdict and the seed-dependent lock (F3); the manifest's commit (F4); the sin²θ_W site and the caption
(F7).

**For the record rather than the paper:** B1428 should say which printing of GHHR its targets came
from, since the arXiv printing's I(μ) differs in sign at q¹; and B1431 should name which longitude of
m003 it means, since at the homological longitude the claim fails.

Everything small is done. Item 1 is the report.

---

*Reproductions: `referee_2026-09-17/scripts/`. Round 1: `v1`–`v28`. Round 2: `r2_chain_table_drift`,
`r2_lock_data_tracked`. Round 3: `r3_i26_euler`, `r3_m010_index`, `r4_r30_check`, `r5_tower_loci`,
`r6_h1_three`, `r7_corank_bound`, `r8_enrichment_budget`, `r9_enrich_coefficients`. Round 4:
`r10_controls`, `r11_3d_index`. Round 5: `r12_3d_index_classes`, `r12b_separation`, plus the E83
reproduction, the gate mutation test, the manifest audit and the S24/S25 checks recorded in
`REFEREE_REPORT_ROUND5_2026-09-29.md`. Primary sources read at source: Menal-Ferrer–Porti; DGG
1108.4389 and 1112.5179; Garoufalidis 1208.1663; Garoufalidis–Gu–Mariño 2301.00098; Gang–Yonekura
1803.04009; GHHR 1604.02688 (LaTeX e-print); Celoria–Hodgson–Rubinstein 2509.09886.*

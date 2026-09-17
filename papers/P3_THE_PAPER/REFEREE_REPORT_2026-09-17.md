# Referee report — *Standard-Model structure from the figure-eight knot complement: what is forced, what is withheld, and what must be supplied*

**Manuscript:** `papers/P3_THE_PAPER/main.tex`, draft dated 2026-09-17 (arXiv bundle, 52 pp.), with the
ancillary verification package `anc/`.
**Reviewed:** 2026-09-17.
**Recommendation: major revision.** Every mathematical claim I was able to check independently is
correct — an unusually large number of them, and several to the last digit I could compute. The
revisions I ask for are about *framing* and about *shipped infrastructure*, not about the mathematics
I verified.

A referee's caveat, stated first because the manuscript would want it stated first: this report
separates what I verified from what I did not. Roughly the front half of the paper (§§2–4, §6, §9,
and the topological content of §7) I re-derived from scratch; the measurement calculus of §5, the
closings' vacuum counts, the index computations on the commensurability class, and the three ledger
rows σ, λ, ℙ(B₀) I did **not** verify and take no position on. Section 5 below says exactly where
the line falls.

---

## 1. Method

All reproductions below were written from the manuscript's own prose and run on a clean machine.
**No code, data file, or intermediate result from the repository was used** for any of them, with two
declared exceptions: (i) I ran the shipped verification package as a package, to test *it*; and
(ii) in §4.1 I read the record's own tracked evidence log, in order to audit a claim whose lock
cannot run.

Environment: Linux, Python 3.11.15, SnapPy 3.3.2, sympy 1.14.0, mpmath 1.3.0, numpy 2.4.6,
scipy 1.17.1, python-flint 0.9.0, PARI/GP via the cypari bundled with SnapPy. This matches the
package README's pinned stack except for the interpreter minor version.

---

## 2. What reproduces

### 2.1 §2, *What is generic* — reproduces exactly, every number

This is the section on which the paper's honesty rests, and it is the section I checked hardest.
I enumerated homomorphisms π₁(M) → SL(2,3) over generator images with no restriction on the
presentation, counted surjections, and divided by |Aut(SL(2,3))| = 24 (the action is free on
surjections, so the quotient is exact, not an estimate).

| manuscript | reproduced |
|---|---|
| 145 of the first 400 one-cusped census manifolds (36.25 %) admit the surjection | **145 (36.25 %)** |
| 124 of 400 (31.0 %) admit exactly two — m004's own count | **124 (31.0 %)** |
| class counts 0 (255), 2 (124), 4 (14), 6 (4), 10 (2), 12 (1) | **all six exact** |
| tie list m003, m007, m022, m026, m027, m029, m030, m033, m034, m036, m047 | **exact, in order** |
| 1696 of the first 5000 (33.92 %) | **1696 (33.92 %)** |
| 181 of 203 123 one-cusped census manifolds amphichiral | **181 of 203 123** |
| the count of three is attained by 2 of the first 4000 and 20 of all 212 641, never on one cusp | **2, 20, never on one cusp** (the two are m202, s959, both 2-cusped) |
| m004 carries the generic value 4, as 3996 of the first 4000 do | **3996** |
| the 112-member ℚ(√−3)-shape family | **112** |
| of which 38 amphichiral, 74 chiral | **38 / 74** |
| of which 59 admit the surjection, 35 do not, 18 have > 3 generators | **59 / 35 / 18** |

The sibling comparison is likewise exact: m003 and m004 share their volume to 15 dp, H₁(m003) =
ℤ/5 ⊕ ℤ against ℤ, cusp shape ω against **2√3 i** (I get 3.4641016151 i), Chern–Simons **1/4 against
0**. m004's symmetry group is D₄ of order 8 — the paper's "eight isometries" — and it is amphichiral.

**§2's central rhetorical move therefore survives audit**: the entry point really is admitted by
about one census manifold in three, and the paper really does state this before it makes a positive
claim. I want to record that this is rare and that it works.

### 2.2 §3–§4, the genesis and the uniqueness proposition — correct, including the controls

- `M² = LR` for the golden substitution matrix, `LR = [[2,1],[1,1]]`. ✔
- `F = L·P = [[1,1],[1,0]]` squares to `LR` and has determinant −1 (orientation-reversing). ✔
- It is the **only** integer square root up to sign (exhaustive over |entries| ≤ 12), and `LR` has
  **no orientation-preserving** integer square root — `det(LR + I) = 5` is not a square, which is
  the Cayley–Hamilton argument the appendix row states. ✔
- `L_a R_b` admits an orientation-reversing integer square root **iff** `a = b`: exhibited for
  a = b = 1…4, and all **12** control pairs with a ≠ b return none. ✔

Proposition 4.1 checks out in every part, including the part the manuscript flags against itself:
|SL(2,ℤ/4)| = 48 = |2O| but SL(2,ℤ/4) has **exactly seven** involutions (I counted them) while every
binary polyhedral group has exactly one (I built 2O explicitly and confirmed it has one), so the
order coincidence is not an isomorphism. The completeness bound is right — 6/π²·N³ = 131.31 > 120 at
N = 6 — and tr(RᵐLᵐ) = m²+2, disc = m²(m²+4), Λ(m) = m²+4, with m²+4 = 5 ⟹ m = 1 and no solution for
3. The manuscript's warning that the *conductor* reading would make the statement false is correct:
m = 4, 11, 29 all give ℚ(√5).

I also confirmed the quotient catalogue: π₁(m004) has **48 surjections onto SL(2,3)** (= 2 up to
Aut), and **zero** onto SL(2,5) = 2I and zero onto 2O. So "E₆ is the only exceptional label the
object reaches as a quotient" is a verified computation, not an assertion.

### 2.3 §6, the content census and the hypercharge forcing — reproduces, including the bookkeeping

I implemented the census from the manuscript's description alone: six SM-visible types, multisets of
five, the colour cubic, Witten parity, the three linear conditions, the cubic, rigidity, chirality,
no zero hypercharge.

- 252 = C(10,5) candidates. ✔
- The pure colour cubic alone kills **222**, leaving 30. ✔
- Witten parity leaves 12; the remaining conditions leave **exactly two contents** — the SM 15-plet
  `(Q, Ūb, Ūb, L, E)` and its complex conjugate. ✔
- Each content carries **two hypercharge rays**, `(1,−4,2,−3,6)` and `(1,2,−4,−3,6)`, differing by the
  u^c ↔ d^c relabelling — so **four rays in total**, exactly the distinction the manuscript draws in
  its "two bookkeeping points". ✔
- The cubic on the line evaluates to **−18(t−3)(t+3)** exactly, and the two solutions are the
  Standard-Model hypercharges times six. ✔
- `Tr(T₃²) = 3`, `Tr(Y²) = 5`, `Tr(T₃Y) = 0` on the **27**, giving 3/8; and the same 3/8 on the
  5̄, 10 and 16 — so the manuscript is right that the ratio discriminates nothing. ✔

### 2.4 §5, §7 and §10 — the parts I could check

- `Vol(m004) = 9√3 ζ_K(2)/π²` for K = ℚ(√−3): the manuscript claims 32 decimal places. It agrees to
  **60**, the limit of my computation (difference 6·10⁻⁶¹). The covolume of PSL(2,𝒪_{−3}) is
  0.169156934 (paper: 0.16916) and the ratio is **exactly 12** — the stated index. ✔
- 87 covers to degree 10 carrying **201 cusps**; **66 chiral, 21 amphichiral**, by two
  orientation-aware tests that agree on **all 87** — precisely as claimed. Of the chiral ones,
  **12 are one-cusped and 54 multi-cusped**, both numbers the manuscript uses downstream. Nine cyclic
  covers. ✔
  *(A methodological note in the paper's favour: SnapPy's default `is_isometric_to` is
  orientation-blind and reports all 87 as amphichiral. The manuscript's insistence on an
  "orientation-aware test", and its footnoted withdrawal of an earlier family-wide claim that rested
  on the blind test, is exactly right. I reproduced the error before reproducing the correction.)*
- **14** of the 87 covers carry a hexagonal cusp, **16 of the 201 cusps**. ✔
- **2804** one-cusped census manifolds with H₁ = ℤ to seven tetrahedra. Reading each isometry's
  sign pair (s_m, s_l) off its cusp map, the split is **2794 realising only the inversion, 7
  realising nothing, 3 realising the full set** — m004, s726, s912 — with **no residual category**.
  Exactly the manuscript's three numbers. ✔
- **Ten** exceptional fillings; **78** closed hyperbolic fillings in the |p|,q ≤ 8 grid; the mirror
  isometry m004(p,q) ≅ m004(−p,q) holds for every coprime pair in the grid (re-verified, not assumed);
  and **none of the 78** keeps ℚ(√−3) — nor ℚ(√5) nor ℚ(√−15) — with the open object as a positive
  control. ✔
- m004(±5,1) has volume **0.981368828892** — the Meyerhoff manifold's — and the mirror isometry
  m004(5,1) ≅ m004(−5,1) holds. Of the field data I verified the *arithmetic* directly: PARI gives
  **disc(x⁴ − x − 1) = −283**, and that quartic has **no proper subfield**, so it cannot contain
  ℚ(√−3). The *attachment* of x⁴ − x − 1 to this slope, and of the cubics of discriminant −59 and
  −31 to (±6,1) and (±8,1), I read from the record's tracked census log rather than recomputing
  (§4.1); my own independent shape-field computation for these three slopes did not finish, and I
  flag that rather than let the row read as fully re-derived.
- The symplectic self-duality lemma — `JρJ⁻¹ = (ρ⁻¹)ᵀ` iff `det ρ = 1` — verified symbolically. ✔
- The "hollow texture" no-go: a 3 × 3 complex symmetric matrix with zero diagonal has
  `σ₁ = σ₂ + σ₃` **exactly**. Verified to machine precision on 20 000 random matrices. This is a
  pretty observation and it does the work the manuscript asks of it. ✔
- The Koide coincidence the manuscript volunteers against itself: I get δ − 2/9 = **7.41 × 10⁻⁶**
  against a propagated experimental σ of **8.35 × 10⁻⁶**, i.e. **0.89 σ**. The manuscript says
  7.4 × 10⁻⁶, 8.3 × 10⁻⁶, 0.89 σ. ✔
- The Summary's "cleanest witness" that arithmeticity and handedness are independent. Over words in
  {L, R} of length ≤ 7 up to rotation, the once-punctured torus bundles with a degree-2 (imaginary
  quadratic) invariant trace field are `LR`, `LLR`, `LRR`, `LLRR` and the four powers `LRLR`,
  `LRLRLR`, `LLRLLR`, `LRRLRR`. Restricting to **primitive** words leaves exactly **four** — and
  exactly **two of them, `LLR` and `LRR`, are chiral, and they are a mirror pair, both over
  ℚ(√−7)** (discriminant −7). The Bianchi cross-check the manuscript mentions comes out on the nose:
  vol(b++LLR) is exactly **3×** the covolume of H³/PSL(2,𝒪_{−7}), just as vol(m004) is exactly 12×
  that of 𝒪_{−3}. ✔ *(One presentational note: the count is over primitive words. Counting all words
  of length ≤ 7 gives eight arithmetic bundles and four chiral ones. Please say "primitive".)*
- Group theory: `27 ⊗ 27` contains no adjoint; 248 = 78 + 8 + (27,3) + (2̄7,3̄); the A₂+A₁ Levi has
  dimension 14 and rank 6; so(10)+u(1) = 46, so(8)+u(1)² = 30; c((E₆)₁) = 78/13 = 6; the pure-spinor
  stabiliser has dimension 34 and toral rank 4 against 29 generically; 2T/Q₈ = ℤ/3; |H₁(Y₃)| = 16;
  C(78,2) = 3003; 2⁴−1 = 15 faces; 2⁷ = 128. All ✔.
- α_s misses by **34.75 %** ("35 %"), and sin²θ_W by **47.5** experimental σ ("about fifty"). ✔

### 2.5 Internal consistency and the record

The chain table has 57 numbered rows; the type tally is 36 Theorem / 8 No-go / 6 Identity / 4 Axiom
/ 2 Census / 1 Corollary, matching the printed "recomputed from the table" line; the axioms sit at
3, 4, 5, 18; **no link between 6 and 17 is an axiom**. The appendix has 67 rows, 61 settled and 6
computed, 8 marked "script + lock". The falsifier list has 9 items of which 3 are self-labelled
upgrade triggers, leaving the promised six. The freedom ledger has 11 rows with 7 non-continuous
(one relational, six external), matching the abstract. 4 axioms + 8 irreducible identification rows
= the stated 12.

In the repository: the retraction sweep runs and reports **0 live violations** over 7229 tracked
files against 24 registered phrases; `docs/RETRACTIONS.md` holds exactly **27** rows ("twenty-seven
corrected or withdrawn statements"); `frontier/` holds 1302 arcs ("about thirteen hundred").
`build_manifest.py` regenerates cleanly at HEAD with no seal mismatch and no record lacking a lock.
Seals pass **21/21**.

### 2.6 Citations

I checked the load-bearing ones against sources rather than against the manuscript's paraphrase.

- **Menal-Ferrer–Porti, Thm 0.1** reads: *"Let M be a complete, nonelementary, hyperbolic 3-manifold
  that is topologically finite, and n ≥ 2. Then the inclusion ∂M̄ ⊂ M̄ induces an injection
  H¹(M, E_{ρₙ}) ↪ H¹(∂M̄, E_{ρₙ})."* The manuscript's claim that the theorem "asks only that M be
  complete, non-elementary and topologically finite, with no condition on the number of cusps" is
  **exactly right**, and the decision to stop booking the 54 multi-cusped zeros as an epistemic debt
  — since the theorem forces them — is correctly reasoned. (One scope slip: see §4.5.)
- **Reid 1991**, **Callahan 2009** (the figure-eight group is the only torsion-free Jørgensen group),
  **Acharya–Witten** (chirality needs singularities), **Distler–Garibaldi** (no chiral spectrum
  inside E₈) — all accurately characterised.
- **Lee, arXiv:2502.11950** — title and construction accurate (mixed Tate motive over the invariant
  trace field, Beilinson regulator = complex volume). I could not confirm from the abstract that the
  figure-eight appears as a *verified case*; please cite the appendix item.

---

## 3. Assessment

Taken as a report on where a boundary lies, this is careful, unusually well-instrumented work, and
the negative results are its substance. I found no mathematical error in anything I could check.
What I do object to is the distance between the title and what the paper's own sections establish.

**The object's actual contribution, on the paper's own showing, is narrower than the title.**
Assembling the verified facts: the entry point (the 2T surjection) is admitted by about one census
manifold in three; what the chain consumes is the invariant trace field ℚ(√−3), a
commensurability-class invariant shared with m003, which also shares the volume; the algebra is then
handed over by McKay, a step the paper itself calls generic; the *content* is forced by the anomaly
conditions with "no token of the object" — which I confirmed by implementing that computation with
no token of the object; and the two structural positives that remain are each conditional — the ℤ₆
global form on the colour frame and the Standard-Model shaping, the termination on the chirality
datum — all three of which the freedom ledger lists as supplied. The one uniqueness that survives §2
(Prop. 4.1) sits at the *golden, spherical, 2I, E₈* end, not the hyperbolic 2T/E₆ end the
construction actually uses, and is conditional on a stipulated normalisation of "level". The paper
states both of these qualifications itself, in the two sentences bracketing the proposition; my point
is not that they are hidden but that they are not carried forward into the title.

§4's scope note very nearly says this ("strong as a statement about the class and weak as a statement
about m004 in particular"). I ask that the *title and abstract* be brought to the same standard the
scope notes already meet. "From the figure-eight knot complement" is, by the paper's own accounting,
"from ℚ(√−3), plus four undischarged inputs, plus three listed identifications."

**The "57 links, 53 forced" framing should be demoted.** The tally is arithmetically correct and I
verified it. But the table mixes Morse–Hedlund (link 1), a machine-checked Lie isomorphism on 3003
basis pairs (link 26), and the known failure of desert unification (link 43) as commensurable
"links", and "forced" is defined negatively as "no declared choice enters it". The paper concedes
this twice ("that ratio is not the invariant and we do not ask it to be"), yet the count leads §3,
anchors Figure 1, recurs in a scope note and in a non-claim, and is the appendix's fourth row. A
count the authors disown four times should not be carrying that much presentational weight. I would
keep the *shape* claim — axioms at the two ends, none in links 6–17, which is true and is the
interesting part — and drop the ratio.

**§7's index is a definition, and the abstract should say so.** `I(V) = t₀ − r₁` is the authors'
own construction, pre-registered rather than cited, and the paper's own scope note proves — via
Chern–Weil and Atiyah–Singer on flat data — that it *cannot* be a four-dimensional Dirac index. The
scope note is excellent and I would not change a word of it. But the abstract says "the cohomological
index standing in for net chirality", and "standing in for" is doing more work there than a reader
will notice. Say in the abstract what §7 says in its scope note: that these are counts of twisted
classes, and that the identification with generations is registered and not earned.

---

## 4. Findings that need action, in order of severity

### 4.1 The shipped verification package does not pass

`python3 run_package.py --seals --locks` at repository HEAD: seals **21/21 PASS**, locks **FAIL**.
Three independent full runs, the last of them on the README's complete pinned stack and a quiet
machine:

| run | stack | result |
|---|---|---|
| 1 | without `python-flint` | 10 failed / 711 passed / 15 skipped |
| 2 | flint added mid-run | 9 failed / 712 passed / 15 skipped |
| 3 | full pinned stack, quiet machine | **5 failed / 716 passed / 15 skipped** (798 s) |

`REPORT.md` is rewritten to "**Overall: FAIL**" in all three. The package's README states its exit
code "is 0 only if every step that ran passed"; it is not 0.

The failures split into two kinds, and the package gives a reader no way to tell them apart because
it reports only a summary line.

**(a) Four deterministic failures that cannot pass on any clean checkout.** All four tests in
`tests/test_b1419_arithmetic_fillings.py` — `test_grid_and_count`, `test_exactly_six_arithmetic`,
`test_meyerhoff_field`, `test_every_filling_decided` — fail with

```
FileNotFoundError: frontier/B1419_the_arithmetic_fillings_corrected/verification/
                   arithmetic_census_closed.jsonl
```

because `.gitignore` line 98 is `*.jsonl`. The aggregated census the locks read is excluded from the
repository by a blanket rule. This is the worst possible row for it to happen on: B1419 is the
*correction* of the arithmetic-filling claim (error class E82, the cusped criterion applied to closed
manifolds), it is the row the appendix advertises as re-runnable, and it is one of the few places
where the paper had to withdraw a published sentence. Fix: add
`!frontier/*/verification/*.jsonl` beside the existing `!frontier/*/stageA/journals/*.jsonl`
exception, or have the lock regenerate the census from the tracked `.py`.

**(b) One to six further failures that vary from run to run.** The ones I saw were the two tests in
`test_b1095_mirror_isospectral.py` and the three `…_by_RUNNING` tests in
`test_b1296_the_charge_locus_parity_lock.py`, `test_b1303_the_sm_closings_z_prime.py` and
`test_b1304_the_audit_seats_4d_model.py`. **All five pass in isolation** and all five pass when the
five candidate files are run together (4 failed, 19 passed — the four failures being B1419 again).
They spawn subprocesses under a 900 s timeout and fail only inside the full 146-file run, more often
the busier the machine. These are not mathematical failures. But they make the package's single
PASS/FAIL verdict non-deterministic, which for a paper that stakes itself on auditability is a real
cost, and a reader has no way to tell them from case (a) because `REPORT.md` prints only a count.
Please have the runner name the failing tests, and raise or drop the subprocess timeouts.

**I want to be exact about what (a) does and does not impugn.** It does *not* impugn the claim. I
audited the six-arithmetic census against the record's own **tracked** evidence —
`arithmetic_census_closed.out.txt` plus `deep_stragglers.json` and `stragglers_recheck.json` plus the
mirror isometry, which I re-verified independently — and **all 78 fillings are decided**: 6
arithmetic at discriminants −283 (±5,1), −59 (±6,1), −31 (±8,1), the deepest field of degree **31**
at (1,8) matching "degree up to 31", and every straggler non-arithmetic. The claim is sound. What
fails is only the shipped ability to check it, which is the thing this paper has chosen to stake
itself on.

### 4.2 `anc/REPORT.md` as shipped is stale and says PASS

The ancillary `REPORT.md` is dated 2026-09-16T17:05:23Z at commit `c052c857` and certifies **54
claims / 75 records / 111 locks / 18 seals** — a smaller, older claim set than the `MANIFEST.json`
shipped in the same directory (67 / 95 / 146 / 21) and than the paper's appendix (67 claims). It
reports seals only, and concludes "**Overall: PASS.**" A reader who opens the ancillary directory
sees a green certificate for a claim set that is not this paper's, produced by a run that never
executed the locks. Regenerate it, or ship no report at all.

### 4.3 The manifest's recorded commit does not contain the artefacts it lists

`MANIFEST.json` records `environment.git_head = 2c06d7a9`, but appendix row 5 (the B14 square-root
claim — the one added most recently) has its primary lock
`tests/test_b14_square_root_selector.py` and its `frontier/B14_…/verification/` directory **absent at
2c06d7a9**; both exist only at HEAD `f52c4f5`. The manifest was evidently built from a working tree
carrying uncommitted work. The appendix promises that "the manifest records the commit hash of the
repository state it was built from", and §11 promises a frozen snapshot of *that state*; a reader
who checks out the recorded hash cannot reproduce the package. Rebuild the manifest from a clean
checkout before deposit, and have `build_manifest.py` refuse to run on a dirty tree.

### 4.4 §2's census-drift sentence changes population mid-sentence

This one matters more than its size because §2 is the base-rate section.

> "the rate drifts from 36.25 % over the first 400 to 33.92 % over the first 5000, and much further
> down the census: sampled in blocks of 800 at depths 0, 20 000 and 80 000 it falls
> 34.25 % → 29.38 % → 21.12 %."

The first two figures are over the **one-cusped** census (I verified both). The block figures are
over the **full** orientable cusped census — the backing record's own script opens with
`C = snappy.OrientableCuspedCensus`. I reproduced the block figures there to every digit, including
the two-generator stratum 34.23 % → 15.36 % and the flat ~33 % three-generator rate. But on the
**one-cusped** census, the same blocks give

| depth | full census | one-cusped census |
|---|---|---|
| 0 | 34.25 % | **33.00 %** |
| 20 000 | 29.38 % | **33.88 %** |
| 80 000 | 21.12 % | **31.38 %** |

— mild and non-monotone, with the two-generator stratum going 33.02 % → 34.70 % → 26.50 %, not
34.23 % → 15.36 %. So the sentence's conclusion — "a reader re-running the sweep at depth will find
the object less generic than our own headline rate says" — does not hold for the population the
headline rate is computed on. The numbers are right; the concatenation is not. Either state the
population switch explicitly, or re-run the blocks on the one-cusped census and report what comes
back. I note the direction of the error is self-punishing, which is presumably why it was not caught;
that does not make it safe in a section about base rates.

### 4.5 Smaller corrections

- **Figure 1's caption says "Fifty-two links are forced."** The table, the recomputed tally beneath
  it, and three prose statements all say fifty-three. The caption is stale. Since the paper makes a
  point of the table being generated rather than typed, the caption should be too.
- **sin²θ_W is quoted as missing by 0.9 %; it misses by 0.82 %** (0.0019/0.2312). The 35 % for α_s
  is right (34.75 %), as is "about fifty standard deviations" (47.5).
- **Menal-Ferrer–Porti requires n ≥ 2.** §7 writes the injectivity theorem for
  "V = Sym^m(h) ⊗ F" without that restriction. The conclusion is unaffected — m = 1 is symplectically
  self-dual and dies to the paper's own lemma — but the hypothesis should be carried, especially in a
  paper that makes a point of carrying hypotheses. The descent through a finite cover, with transfer
  and the characteristic-zero step named, is otherwise correctly argued.
- **`MANIFEST.md`'s header calls 95 claim–record pairs "95 establishing records"**; there are 80
  distinct records. The paper's appendix says "claim–record pairs" correctly — the manifest should
  match it. Relatedly, "95 of 95 records with a primary lock" counts pairs.
- The appendix says "**over** 95 claim–record pairs"; it is exactly 95.

---

## 5. What I did not verify, and take no position on

This list is as important as the one above, and I ask that no part of this report be read as
endorsing it.

- The whole measurement calculus of §5 (chain links C24–C42): the Killing signature (2,2), the
  centraliser lattice, the two cubic pencils and ℚ(√77), the magic-square isomorphism on 3003 basis
  pairs, the real-form selection 𝔢₆₍₂₎, the Hermitian signature (15,12), I = −1, the coupling
  normalisation. I verified only the arithmetic of the surrounding integers.
- Everything about the closings: 19 624 vacua on the ninth, 706 464 Standard-Model lines, 34 752 and
  31 488 and 768 on the twelfth, the Z′ regime and its bounds.
- The index computations themselves: the 542 firing modules, the 235 modules on the object's
  reducible locus, the non-zero values on s958, v2873, t12833, t12835, o10_150701 and t12839, the
  61 + 12 vanishing sectors, the 38 070 multi-cusped sectors. I verified the *theorem* behind the
  vanishing (Menal-Ferrer–Porti and its transfer) and the *lemma* (symplectic self-duality), not the
  computations.
- The ledger rows σ, λ and ℙ(B₀), the seven crossings, the 352-pair period scan, the 216-cell
  regulator grid, the G₂ orbifold with b₂ = 0.
- The genesis uniqueness theorem (144 candidates to one).

For all of these I confirmed only that a lock exists and, with the exceptions in §4.1, that it
passes. The paper's own appendix is right that "a lock is traceability, not re-derivation", and the
manuscript should keep saying so as plainly as it currently does.

---

## 6. Two things I want to say in the paper's favour

**First**, the discipline is real and it is checkable. I tried to catch this paper out on §2 and
instead reproduced it to the digit, including the counts that cut against it. I reproduced its
*errors* too — my first chirality sweep over the 87 covers returned "87 amphichiral" because
SnapPy's default isometry test is orientation-blind, which is precisely the failure the manuscript
documents, withdraws a claim over, and footnotes. A paper that tells you where it fell over, in
enough detail that you fall over in the same place, has earned something.

**Second**, the negative results are stated at the right strength and several are genuinely clean:
the hollow-texture identity, the SL(2,ℤ/4) involution count, the square-root uniqueness with its
twelve controls, the flat-bundle obstruction that the authors turn against their own positives. The
"Recognition" section, which enumerates what is standard and reports that four items were moved onto
it during revision, is a model other papers in this genre should copy.

---

## 7. Summary of requested changes

1. Fix `.gitignore` so the B1419 census ships; re-run the package; make the runner name failing
   tests. **(§4.1)**
2. Regenerate or drop `anc/REPORT.md`. **(§4.2)**
3. Rebuild the manifest from a clean checkout so `git_head` matches its contents. **(§4.3)**
4. Fix the census-drift sentence's population. **(§4.4)**
5. Fix the Figure 1 caption (52 → 53), the sin²θ_W percentage (0.9 % → 0.82 %), the MFP hypothesis
   (n ≥ 2), and the manifest's "records"/"pairs" wording. **(§4.5)**
6. Bring the title and abstract to the standard of §4's scope note; demote the 53/57 ratio; state in
   the abstract, as §7 already does in its scope note, that the index is a count of twisted classes
   and not a four-dimensional index. **(§3)**

None of 1–5 touches a mathematical claim. Item 6 is the one that decides whether this paper is read
as what it is — a carefully drawn boundary — or as what its title suggests.

---

*Prepared by re-deriving the paper's checkable claims independently; the full machine log of the
reproductions, with the scripts, is summarised in §2 above. Claims not listed in §2 were not
verified and are listed in §5.*

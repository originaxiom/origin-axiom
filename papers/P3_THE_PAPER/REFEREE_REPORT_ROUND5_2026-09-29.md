# Referee report, round 5 — the revision of 2026-09-18, and four corrections to this review

*On:* **Standard-Model structure from the figure-eight knot complement**, as revised on `main` at
`987c0c8f` (eight commits since round 2's `21c47a51`). The consolidated report
(`REFEREE_REPORT_CONSOLIDATED_2026-09-18.md`) is updated in place to match; this file is the working
record of the round.

---

## 0. Summary

**The author acted on almost everything checkable, and I verified each fix myself rather than from the
commit messages.** The drift gate now reads every row (mutation-tested), the runner's verdict names
what it covers (run, not read), and the manifest's commit contains every artefact it lists (all 442
paths, 80 directories and 21 seal hashes checked). The package now passes end to end under the hash
seed that used to break it.

**The paper itself changed by two lines.** Row 43 of the chain table (my round-2 finding) and the
retraction count (27 → 29, the author's own find). Findings F1, F5 and F6 are untouched — explicitly
deferred by the author (*"Nothing about what belongs in the paper is decided here"*, S22) — so the gap
between the record and the paper **widened** this round: eight commits of new, verified results, two
lines of manuscript.

**The new mathematics holds up under independent reconstruction**, with three corrections to how it is
stated (§3). And the author caught **four errors of mine** (§1), each confirmed here.

---

## 1. Corrections to this review — first, because they are mine

### 1.1 My clone was shallow, and I reasoned structurally from it

Rounds 2 (§7) and 3 (§0) say *"`main` is **101 commits** — a curated line"*, and round 3's lane table
says two lanes *"share no history with `main` at all (different root commits, no merge base)"*.
`git rev-parse --is-shallow-repository` → **true**. Unshallowed:

| | commits |
|---|---|
| `main` at `21c47a51` (what round 2 reviewed) | **3 457** |
| `1e72e062` (the head my round-3 table calls "101 commits") | **3 304** |
| `main` now, `987c0c8f` | 3 465 |

With full history **every lane has root `517783f2` and a merge base with `main`**; the "different
root" was the shallow boundary. Unique commits versus `main`: `sep16-branch` 92,
`standard-model-derivation` 132, `audit/physical-bridge` 166, `physics-seat-evaluation` 165, this
review's lane 18. The picture of "a curated line of 101 and four lanes of ~3 000" was an artefact.

**What survives:** the substance of round 3 — that the lanes held results the paper does not report —
was established by reading the lanes, not by counting them, and the author's own S21 confirms it
independently (*"the standard-model lane at seventeen commits past its pin with eleven unrowed items,
including the tower's generation count"*). The structural framing is withdrawn.

### 1.2 Round 2's "clean green" was a one-in-four draw

Round 2 reported *"727 passed … **Zero failures** … a clean green"* and told the author *"you gave up a
green you had earned."* The author's E83: `B1411`'s lock handed sympy a **set** as its list of
unknowns, so the answer's normalisation depends on `PYTHONHASHSEED`. Reproduced here on the shipped
script from `21c47a51`:

```
pre-fix   seed 0 FAIL  1 FAIL  2 FAIL  3 FAIL  4 PASS  5 FAIL  6 FAIL  7 PASS
post-fix  seed 0 PASS  1 PASS  2 PASS  3 PASS  4 PASS  5 PASS  6 PASS  7 PASS
```

Python randomises the seed per process, so my single green run was luck. The green was drawn, not
earned, and round 2's correction "in the author's favour" rested on it.

**Scoped precisely, since the author's fix comment attributes a "run-to-run variation" misdiagnosis to
the outside referee:** the four tests round 1 *named* as load-sensitive (`b1095`, `b1296`, `b1303`,
`b1304`) pass in isolation on seeds 0, 1, 4 and 7 — they are **not** seed-dependent, so that diagnosis
is not refuted. `test_b1411` fails **in isolation**, on seeds 0 and 1, in 9 s and 2 s: nothing to do
with load. Round 1 did not name it; whether it was among the unnamed "one to six" varying failures
I cannot establish from my own report.

### 1.3 Round 3 §10 wrongly graded the relay's "proven Dehn-filling law" as overstated

I read the Gang–Yonekura abstract, found no index transformation law in it, and graded the claim
overstated. The proof exists: **Celoria, Hodgson, Rubinstein, "The 3D index and Dehn filling",
arXiv:2509.09886** (v1 11 Sep 2025, v2 19 Dec 2025): *"We provide a rigorous proof of the Gang–Yonekura
formula describing the transformation of the 3D index under Dehn filling a cusp in an orientable
3-manifold."* The relay was right in substance and only omitted who proved it. I checked one abstract
and graded without searching.

### 1.4 "Independent convergence" with S23 — wrong objects

I told the author S23's 3d index was an independent convergence with my r11. It is not: S23 computed
the **un-rotated** index, *1 − 2q − 3q² + 2q³ + …*; r11 computed the **rotated** matrix's (0,0) entry,
*1 − 8q − 9q² + 18q³ + …*. Both match the literature; they are different series.

*(And round 3's erratum §11 already records the fifth: B307 does not subsume the h¹ = 3 question.)*

**One check that came back clean:** S23 found a truncation bug — every factor cut at one shared order
loses terms when a factor has negative degree, *"right for the object by luck"*. r11 is not affected,
and this is now tested rather than argued: **0 of 625** tetrahedron indices in its range have negative
minimal degree, the rotated (0,0) sum has no gluing prefactor, and raising the truncation from q¹² to
q²⁰ with a wider sum leaves every coefficient through q⁸ unchanged.

---

## 2. The author's fixes, verified

| finding | claimed | verified here | how |
|---|---|---|---|
| **F2** stale row; gate samples 9/57 | fixed | **yes** | my drift checker on `main`: 0 of 57 stale. **Mutation test:** a drift planted in row 30 — outside the old `rows[:6] + rows[-3:]` sample — makes the gate **fail** (1 failed, 3 passed); restored, clean |
| **F3** bare PASS on a partial run | fixed | **yes** | `--seals` alone now reports **`PASS (partial: only seals ran)`**; a default run names its steps and says the scripts step was not run |
| **F4** manifest commit does not resolve | fixed | **yes, exhaustively** | `07c0b604` resolves, is an ancestor of `origin/main`, has exactly 3 458 commits as recorded; it contains **all 442** listed artefact paths and **all 80** record directories; **all 21** seals hash to their recorded values there |
| **E83** seed-dependent lock | fixed | **yes** | package on `main` under `PYTHONHASHSEED` 0 **and** 1 (both broke the pre-fix lock): seals 21/21, 148 lock files, **743 passed, 14 skipped, 0 failed**, each (§6) |
| **F7** sin²θ_W; caption | fixed | **yes** | 0.8 % at all three sites; Figure 1 says fifty-seven links |
| **F1** paper omits the project | — | **not addressed** | paper diff since round 2 is two lines; tower, stabiliser, B1409, B1336, B1261 absent |
| **F5** framing | — | **not addressed** | unchanged |
| **F6** 3d-3d literature | — | **not addressed** | Dimofte, Gaiotto, Gukov, 3d-3d, 3D index, A-polynomial, Garoufalidis: **0** mentions each |

Two small notes on the package: this bench records 743 passed / 14 skipped where the author records
744 / 13 — one environment-dependent skip, not a failure. And the author found, on their own, that the
retraction index the paper cites *by count* had drifted (27 → 29) because the gate fires only on arcs
whose verdict word is RETRACTED; that is the same shape as F2, and it was caught without prompting.

---

## 3. The new results, verified independently

Independent means: written without reading the project's implementation, validated against published
values before being used for anything, and compared with the record only afterwards.

### 3.1 The instrument (`r12_3d_index_classes.py`)

The general state sum, GHHR (arXiv:1604.02688) eq. 16 — *I_T(γ) = Σ_k q^{Σk} Π_j J_Δ(a_j, b_j, c_j)* —
built from SnapPy's gluing rows only.

- **Precision is budgeted per factor from the exact degree**, so S23's bug cannot arise. The per-summand
  bound on deg I_Δ turned out valid but useless — it put a term's bound at −2 256 half-units, because
  the individual summands of I_Δ carry very negative degrees that cancel in the sum — so
  it uses Garoufalidis's closed form *2δ(m,e) = m₊(m+e)₊ + (−m)₊e₊ + (−e)₊(−e−m)₊ + max(0, m, −e)*,
  checked against direct computation on **all 361** pairs |m|,|e| ≤ 9 and asserted at runtime on every
  value computed. Before the first run I also caught my own instance of S23's bug — the running
  product truncated at D before later factors of negative degree were multiplied in.
- **All eight published figure-eight classes reproduce** (five integral, three half-classes),
  independent of which edge weight is pinned.
- **The retriangulation control is weak and I do not count it:** all 40 randomise-and-simplify runs
  returned to two-tetrahedron triangulations, so it tests relabelling, not genuinely different
  triangulations. Invariance is instead settled by theorem for the triangulations actually used —
  they are the canonical Epstein–Penner ones (§7.1).

### 3.2 A sign error in the literature, and what "reproduces exactly" means

The arXiv source of GHHR (e-print of April 2016, Example 4.1, read verbatim) **prints**

```
I_T(mu) = 2q - 2q^2 + 2q^3 + 8q^4 + 16q^5 + 16q^6 + 10q^7 - 14q^8 - ...
```

The same example's explicit formula, *I(xμ + yλ) = Σ_k I_Δ(k−x, k)·I_Δ(k+2y, k−x+2y)*, evaluated
exactly, gives **−2q** − 2q² + 2q³ + … — and reproduces **all seven of its other printed series
exactly**. My general implementation gives −2q. So does the author's B1428 code. **The paper is
internally inconsistent; the printed +2q is a sign typo.**

B1428's receipt prints `MATCH` for I(μ) against a target it records as −2q, citing the **journal**
version (Illinois J. Math. 60 (2016), pp. 297–298) from a local copy not in the repository. If the
journal corrected the sign, the claim is exactly right; I could not access the journal text. Either
way the mathematics is settled. What should change is provenance: *"every coefficient published …
reproduces exactly"* is false against the arXiv printing, and the arc should say which printing it
used and that they differ.

### 3.3 S23 — the trivial class: **verified**

**I_m004(0) = I_m003(0) = 1 − 2q − 3q² + 2q³ + 8q⁴ + 18q⁵ + 18q⁶ + 14q⁷ − 12q⁸**, through q⁸,
despite H₁ = ℤ versus ℤ/5 ⊕ ℤ.

### 3.4 S26 — the full collection separates them: **verified, with two corrections to its statement**

Comparison is between **sets** of series over honest classes pμ + qλ, so no identification of one
boundary with the other enters. **Completeness:** a class can only compete with a witness of degree
q¹ if its own index reaches q¹, so it suffices to enumerate every class whose exact degree bound is
at most q¹. That set is finite — the degree grows along every ray, though only **linearly** along the
boundary-slope directions (I(k(−4μ+λ)) on m004 begins at exactly q^k for k = 1…6), which is why a
naive box of radius 10 was not enough and a radius-40 enumeration was used, its outer ring bounded at
20 and 40 half-units.

| witness | series | result |
|---|---|---|
| **(a)** m004, I(μ) | −2q − 2q² + 2q³ + 8q⁴ + 16q⁵ | at **no** class of m003, and differs from every one at order ≤ q¹ — **as claimed** |
| **(b)** m003, I(λ) in SnapPy's basis | −q − q² + 2q³ + 7q⁴ + 11q⁵ | at **no** class of m004 — **but** m004's honest class **I(±2μ) = −q − q² + 3q³ + 6q⁴** agrees through q², first differing at **q³** |
| **(c)** m003 at its **homological** longitude, μ − 2λ | q³ + 2q⁴ + 5q⁵ + … | **equal to m004's I(λ)** through q⁸ |

**Correction 1.** *"Both differ from every competitor already at the first order"* holds for (a), not
(b).

**Correction 2.** *"The sibling's longitude series occurs at no class of the object's"* is true for
SnapPy's basis curve and **false for the homological longitude**, by (c). Since m003 is not a knot
complement, "longitude" is ambiguous and the arc should name the curve.

And the author's mechanism shows itself unprompted: m003's I(λ) in (b) is **exactly** the figure-eight's
published *half*-class I(μ + λ/2). The sibling's honest classes land on the object's half-classes —
which is S26's explanation of why the separation exists.

**What this means for the paper:** §2 has the Chern–Simons invariant as the *only* thing the
construction uses that separates m004 from m003. There is now a second, independent separator, and
the paper should carry it.

### 3.5 S24 — the stabiliser sharpened: **verified**

CS(m004) = 0 and CS(m003) = **0.25** to 18 digits. On ℝ/½ℤ, x ↦ −x fixes both 0 and ¼, so the
orientation and order bits act **trivially on the entire sister orbit** — the kernel of the action,
not a point stabiliser; moving to the sibling buys nothing for them. Recomputing all **104** family
members listed in twelfths agrees on every class and reproduces the counts exactly —
{0: 47, 1: 5, 2: 11, 3: 29, 4: 7, 5: 5}. Control: of the first 600 one-cusped census manifolds outside
the family, **two** are in twelfths (m135, m136), both on the fixed classes {0, 3}. Not verified: the
membership of the 112, and the eight outside twelfths.

### 3.6 S25 — the embedding's orbit facts: **verified**

From the Cartan matrix by reflection closure: 72 roots, all norm 2; **|W(E₆)| = 51 840**; **120**
A₂ subsystems in a **single** Weyl orbit, stabiliser **432**; **720** commuting (A₂, A₁) pairs, six
partners each, in a single orbit, stabiliser **72**. This closes the consolidated report's
"B1366 'all one orbit' — not verified". The three hypercharge directions are verified and made
exhaustive in §7.2; the 8 177 branchings depend on the author's scan box and are not reproduced.

---

## 4. Verdict

**Unchanged in form, sharper in content.** Minor revision on the mathematics — every item
re-derived this round holds, and every fix the author made to the package is real. Major revision on
what the paper reports: F1 was the lead finding and is now **stronger**, because the record gained
four verified results this round (S23–S26) and the manuscript gained none of them. The most
paper-relevant is S26: the paper's §2 claims one separator of the object from its sibling, and the
record now holds a second.

---

## 5. What this round did not do

The author's retriangulation claim (30 of 30) — no longer load-bearing, §7.1; the 8 177
branchings; the full 112-member family; the journal printing of GHHR; S22's extension to level 7 and
its two torsion-missed loci per level; the 24 order-sensitive sites of lead L222; the 15 silent
receipts of L223.

---

## 6. The package under both seeds that used to break it

A single green proves little after E83 — that is exactly how round 2 went wrong — so the package on
`main` was run end to end twice, in a clean worktree at `987c0c8f`, under the two hash seeds on which
the pre-fix lock failed:

```
PYTHONHASHSEED=0   seals: PASS 21/21   locks: PASS 148 lock files: 743 passed, 14 skipped  (12 min 38 s)
PYTHONHASHSEED=1   seals: PASS 21/21   locks: PASS 148 lock files: 743 passed, 14 skipped  (12 min 25 s)
```

**No failures under either.** Two seeds are not all seeds; what this establishes is that the known
seed-dependent failure is gone, not that no other one exists. The author's sweep (E83: 34
order-sensitive sites, five in shipped locks, all five green under five seeds; 24 more registered as
L222) is the right instrument for the rest, and I have not re-run it.

---

*Scripts this round: `r10_controls.py` (from round 4), `r12_3d_index_classes.py`,
`r12b_separation.py`. The E83 reproduction, the mutation test, the manifest audit, and the S24/S25
checks were run inline and are recorded above with their outputs. Primary sources read at source:
GHHR arXiv:1604.02688 (LaTeX e-print); Celoria–Hodgson–Rubinstein arXiv:2509.09886.*

---

## 7. Addendum — the two gaps left open above, closed

### 7.1 B1431's separation is a statement about the manifolds

§3.4 verified the separation on SnapPy's triangulations, and my own retriangulation control could not
test invariance. That matters, because F1 recommends putting B1431 into the paper's §2 — which is only
right if the index is a manifold invariant, and the record's own lead L225 says *"The 1-efficiency
condition is a hypothesis this bench has **not** checked … Until it is, the invariance claim is
imported rather than verified here."*

Read at source (Garoufalidis–Hodgson–Rubinstein–Segerman, arXiv:1303.5278, LaTeX e-print):

- **Thm 1.2:** a triangulation admits an index structure — the index is well-defined — **iff** it is
  1-efficient.
- **Thm 1.3:** a triangulation of an atoroidal cusped manifold with a **semi-angle structure** is
  1-efficient; strict angle structures are semi-angle structures.
- **Thm 1.4:** for T in 𝒳_M^EP — the regular ideal triangulations of the **Epstein–Penner canonical
  decomposition** — I_M := I_T is well-defined: a topological invariant.
- **Remark 1.5**, which is why canonicity matters: for other triangulations with strict angle
  structures, *"it is not known if they can be connected by 2–3 and 0–2 moves within the class of
  1-efficient triangulations."*

Checked on the triangulations used, for m004, m003 and 4_1:

```
all shapes = the regular ideal tetrahedron 1/2 + i sqrt(3)/2        -> strict angle structure
canonize() leaves the isomorphism signature unchanged               -> this IS the Epstein-Penner triangulation
canonical retriangulation: 2 tetrahedra, no finite vertices          -> the canonical cells are these tetrahedra
```

So by Thm 1.3 they are 1-efficient, by Thm 1.2 the index is defined, and by Thm 1.4 — the canonical
cells being exactly these tetrahedra, with nothing to subdivide and no bridges — **I_T = I_M**.
B1431's separation, on honest classes, is a separation of **the manifolds**, and F1's §2
recommendation stands on verified ground. This also answers the record's L225 question 3 without
Regina. The author's 32-of-32 random-retriangulation agreement remains unverified here, and is no
longer load-bearing: random triangulations are not in 𝒳_M^EP, so that agreement was never the
theorem anyway.

### 7.2 B1430's "exactly three hypercharges" — verified, and made exhaustive (`r13_s25_hypercharge.py`)

B1430 reached "exactly 3" by scanning a box of 28 513 rational directions and says so: *"not an
exhaustive proof over all of them."* The box is unnecessary. For one commuting (A₂, A₁) pair, the 27
(the Weyl orbit of ω₁, minuscule) splits into eleven irreducible pieces of exactly the Standard-Model
shape — one (3,2), one triplet of Q's colour type, three of the conjugate type, three doublets, three
singlets. A hypercharge lies in the 3-dimensional commutant and is constant on each piece; fixing Q's
charge at 1/6 fixes its scale and sign; which conjugate triplet takes −2/3, which doublet +1/2 and
which singlet 1 gives **27 overdetermined linear systems**, each solved exactly.

```
solutions over the WHOLE commutant (rational or not):   3 directions
each re-checked against the multiset on all 27 weights: yes
|W(E6)| = 51 840;  stabiliser of the (A2, A1) pair: 72
the 3 directions under that stabiliser:                 ONE orbit
```

Since all 720 pairs are one Weyl orbit (§3.6), the statement holds for every pair. **B1430's count is
right, and it is now a theorem-grade enumeration rather than a scan.** Its other two caveats stand
and I have not addressed them: regular embeddings only (no S-subalgebras), and Weyl-conjugacy rather
than group-conjugacy. The 8 177 branchings depend on the box and are not reproduced.

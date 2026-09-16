# Opponent's review

**Paper:** *Standard-Model structure from the figure-eight knot complement: what is forced, what is withheld, and what must be supplied* (2026-09-16, ~25k words, 16 sections, primary `math.GT`, cross-list `hep-th`, `math.NT`)

**Role:** adversarial referee. I argue the case against acceptance. Where I checked a claim and it held, I say so.

**Recommendation:** **Reject in present form** for `math.GT`. The document is a project report, not a paper. Its own argument, carried to its conclusion, establishes that the named object contributes nothing that the paper claims for it, and the paper does not draw that conclusion. There is one proposition with a proof and it is trivial. Separately there are two defects — a literature failure and a contradiction between the paper and its own verification package — that must be fixed regardless of venue.

---

## 0. What I verified independently, and it held

I want the objections below read against this list, because the paper is not sloppy everywhere.

| Claim | Status |
|---|---|
| `252 = C(10,5)` contents; colour cubic alone kills 222 | **Reproduced.** With the natural alphabet `{(3,2),(3̄,2),(3,1),(3̄,1),(1,2),(1,1)}` and `[SU(3)]³` charges `{+2,−2,+1,−1,0,0}`: 252 multisets, 30 survive, 222 killed. Exact. |
| Hypercharge cubic `= −18(t−3)(t+3)` | **Correct.** With `Y_q=1, Y_l=−3, Y_e=6, Y_u=−1+t, Y_d=−1−t`: `[Y]³ = 162 − 18t²`. |
| `π₁(m004) ↠ 2T ≅ SL(2,3)`: "exactly two up to automorphism" | **Correct.** Brute force on `⟨a,b,t │ tat⁻¹=aba, tbt⁻¹=ab⟩` (monodromy `LR`, `H₁=Z` ✓): 48 surjections, exactly **2** classes under `Aut(SL(2,3)) = PGL(2,3)`. |
| `sin²θ_W = 3/8` from `Tr T₃²=3, Tr Y²=5, Tr T₃Y=0` | Arithmetically consistent (`Tr Q² = 8`). |
| `tr(R^mL^m) = m²+2`, `disc = m²(m²+4)`, so `Λ(m)=m²+4` | Correct. |
| `|SL(2,Z/N)| ≥ 6N³/π² > 120` for `N ≥ 6` | Correct (131.3 at `N=6`). |
| `SL(2,Z/4) ≇ 2O` via the seven involutions | Correct, and well handled. |
| `27⊗27` contains no adjoint (`= 27̄ + 351 + 351′`) | Correct. |
| `e₆₍₂₎` max compact `su(6)⊕su(2)`, `27 → (15,1)+(6̄,2)` | Consistent with signature `(15,12)`. |
| `α_s` miss: `(0.118−0.077)/0.118 = 35%` | Correct. |

Method credit where it is due: §2's base-rate discipline, the `N=4` near-miss being declined rather than counted, §15 *Recognition*, the retraction ledger, and reporting the `α_s` failure at full size are all better practice than is normal in this literature. **None of that is a result**, which is the burden of §1 below.

---

## 1. Major objection: after the paper's own subtractions the residual is empty

The paper concedes, in its own voice:

- the entry point (`2T` surjection) is shared by ~1 in 3 census manifolds — §2;
- uniqueness of the arithmetic knot complement is "**load-bearing at no step**" — §5;
- what the chain consumes is `Q(√−3)`, a **commensurability-class** invariant shared with `m003` at identical volume — §5;
- `E₆` "is handed over by McKay… so **this step is not evidence for the object**" — §4;
- the anomaly→hypercharge forcing contains "**no token of the object**" and is classical (Geng–Marshak, Minahan–Ramond–Warner, Foot et al.) — §7, §15;
- the `Z₆` global form: "**the derivation is standard**" (Hucks), and the *selection* rests on two inputs the ledger lists as supplied — §7;
- the landing algebra `su(3)⊕su(2)⊕u(1)³` is "elementary… the `A₂+A₁` Levi. **Reproduced, not discovered**" — §15;
- `sin²θ_W = 3/8` is GQW **reproduced**, and misses by 35% in `α_s` — §15;
- no values, at any bounded height — §8;
- no chirality — §9;
- no action, no dynamics, no rate, no field theory — Non-claim 7.

§15 then names four things it believes are non-standard. Each is defeated elsewhere in this same paper:

1. *"that anything in this setting **selects** the SU(5) embedding whose kernel is Z₆"* — §7 says the selection rests on the colour frame and the SM shaping, both listed as external inputs. So nothing in the setting selects it. This item is withdrawn by §7 and left standing in §15.
2. *the termination result* — §7's own scope note: it "presupposes the chirality datum §11 lists as supplied" and "imports a menu-completeness claim whose stage-level formalisation is still owed."
3. *disjointness of the object's periods from a sealed target menu* — a null result of a search the authors designed over a menu they chose. A null result is not a contribution unless someone expected the alternative; nobody did.
4. *"the pricing of the observer"* — §10 is philosophy with a `Z/2`-torsor attached. It is not a mathematical claim and §10 says so ("the part of the paper with the least precedent").

**So the paper's title asserts a provenance that the paper itself disproves.** "Standard-Model structure *from* the figure-eight knot complement" — after §2, §5, §7 and §15, the figure-eight knot complement supplies: a group that surjects onto `2T` (1 in 3 manifolds do), and a trace field it does not own (its class does, `m003` included). Everything downstream is `E₆` representation theory and the 1989–91 anomaly literature.

This is a real finding. It is the finding **that the programme did not work**. The paper instead presents the demolition as the result ("We report the misses"). Careful reporting of one's own null results is good practice; it is not a paper. I would respect a four-page note saying "we tested our flagship structural claim against a census base rate and it came back generic; here is the base rate and here is what we retract." That note would be publishable and useful. This is not that note — it is that note wrapped in 25,000 words that preserve the original framing in the title, abstract, §1 and §16.

---

## 2. Major objection: the "56 links / 52 forced" accounting is not a measurement, and Figure 1 misrepresents it

Three problems, and the third is fatal to the figure.

**(a) Granularity is a free parameter.** The ratio 52/56 is whatever the authors' choice of link boundaries makes it. Merge the twelve middle links into one and it is 41/45; split them and it is 52/80. No invariant is being reported. The paper presents "fifty-two of fifty-six links are forced" as a quantitative fact about the derivation's cost. It is a fact about a table.

**(b) The type taxonomy inflates the count.** Link 14 — "the symmetrised Kashaev series has **pure-3 denominators through fifth order**" — is typed **Identity**. A pattern verified to finite order is an observation, not an identity, and a paper that (rightly) refuses to treat short-catalogue recurrences as evidence should not type a truncated numerical pattern as a forced link. Links 11, 13, 15, 19, 20 are in the same family; the eight "No-go"s and two "Censuses" are finite verifications. "Forced" is doing duty for *theorem*, *finite check*, and *truncated observation* at once.

**(c) The figure draws a dependency claim on a non-dependency ordering, and the paper admits it.** §4's own text:

> "the measurement links 24–42 carry numbers after the observer's axiom 18 **because they were banked later, not because they depend on it**… We state the shape as the table carries it and do not claim a dependency order the table does not."

Figure 1 then draws the 56 links on a line, marks axioms at 3, 4, 5, 18, shades 6–17, and the caption says: *"The point is the **shape**: the cost is not spread through the derivation but sits at the two ends."* **Where cost sits is a statement about the dependency DAG and nothing else.** A claim about axiom placement computed on a chronological banking order is not a claim about the derivation. The paper cannot both disclaim the dependency order and then draw the load-bearing figure on it.

Fix: produce the actual DAG, or delete Figure 1, the "twelve links, no declared choice" motif, and the "52 of 56" tally. That is one of the paper's three headline rhetorical moves and it does not survive its own footnote.

---

## 3. Major objection: the verification apparatus is contradicted by the package shipped with the paper

This is the most serious item, because the paper's pitch is auditability.

**(a) Pre-registration.** §4 footnote:

> "the design text of a computation… is committed to the public repository and its hash recorded **before the computation runs**; … **a reader can check that the digest predates the result**."

`anc/README.md`, shipped as the paper's own ancillary file:

> "It does **not** by itself prove chronology: a record lands in one commit, so the git history shows the seal and the results **together, not in order**… a reader who wants independent evidence of order should treat the seals as **integrity, not as time stamps**."

These contradict each other flatly. The paper's footnote asserts precisely the capability the package denies. Every use of "pre-registered" in the body — §4's four routes, §6's real-form prior, §9's index formula and domain, §6's shape index — inherits the defect. Either obtain a third-party timestamp (OpenTimestamps, an arXiv deposit, a public commit that demonstrably predates the results) or delete the word and write "designed in advance, on our own record, which a reader cannot order-verify."

**(b) The locks certify traceability, not results.** The appendix says so: *"'lock' below means a test that names the establishing result; it does **not yet** mean a test that re-asserts the specific number quoted in this paper's body."* And: *"in one recorded case a lock pinned a family-wide claim that was later withdrawn."* Saying this honestly is to the authors' credit; it does not convert the apparatus into verification. The abstract's "All verification reported here is internal to the project's own re-runnable pipelines" understates the situation — a substantial part of it is not verification at all, it is cross-referencing.

**(c) The ancillary package cannot run.** `anc/run_package.py` sets `ROOT = HERE.parents[2]` and shells `pytest` at repository-level `tests/`; `build_manifest.py` regenerates from the repo tree. A reader who downloads the arXiv source obtains a manifest and a runner that can execute nothing. The appendix says *"the package that ships with the paper runs every lock it names."* It does not. Either vendor the tests or drop the claim.

**(d) The shipped package disagrees with the paper.** `anc/README.md` says *"the **three** rows marked **computed**."* `main.tex` has five and `MANIFEST.json` has five (`Counter({'settled': 49, 'computed': 5})`). In the one artefact whose job is to be checkable.

**(e) The prior on the unchecked claims is poor, by the record's own statistics.** §1 states single author plus "AI-assisted verification passes" — not independent verification. The paper reports, itself: 27 corrected or withdrawn statements in its retractions index; a family-wide amphichirality claim that **passed a lock** and was wrong; two implementations of the base rate that disagreed by a percentage point; four items moved off the novelty list after precedents were found; an archived unification solver that "did not solve its two unification conditions simultaneously"; a link count that disagreed with the prose twice during table generation; an earlier draft that said two robust steps where the accounting said four. This is an honest error ledger and I credit it — but it is also an *estimate of the error rate on exactly the class of assertion that constitutes most of this paper*: roughly a hundred one-line claims whose proofs are not in the document. A referee cannot accept that mass of unproved assertion on this track record.

**(f)** The paper is dated `2026-09-16` and the manifest was built `2026-09-16T16:03`. The paper and its certificate were produced within the same hour.

---

## 4. Major objection: the congruence claim, and the sentence that should not have been printed

§6, link C9:

> "The manifold group is congruence (level 4 in the SL-kernel convention, geometric index 12 at level 8) — a statement that **defies Serre's non-congruence base rate**, computed twice on our own benches and **not yet checked against the literature**."

Three things:

1. **It is classical.** I computed `vol(H³/PSL(2,O₃)) = |d_K|^{3/2} ζ_K(2)/(4π²) = 0.169156934…` and `vol(m004)/that = 12.000000000`. And `|PSL(2,F₃)| = 12`. So `π₁(m004)` is (conjugate to) the **principal congruence subgroup of level `(√−3)`** in `PSL(2,O₃)`. This is standard material on the best-studied hyperbolic 3-manifold there is, and it is discussed in **Maclachlan–Reid**, which is already reference [5] of this paper.
2. **"Defies Serre's non-congruence base rate" is a category error.** Failure of the congruence subgroup property for rank-one lattices says non-congruence subgroups are abundant. It makes no prediction that a *specific named* arithmetic Kleinian group is non-congruence, and congruence subgroups of Bianchi groups are studied routinely. Nothing is being defied.
3. **The quoted levels don't reconcile.** "level 4 … geometric index 12 at level 8." The index 12 is exactly the level-`(√−3)` index. Level 2 in `O₃` gives `O₃/(2) = F₄` and index `|PSL(2,F₄)| = 60`, not 12. Whatever the "SL-kernel convention" is, the numbers 4 and 8 need reconciling with `(√−3)` before print.

**The damaging part is the admission.** A paper that ran base rates over 203,123 census manifolds, that built a seal ledger, a retraction index and a 54-row provenance table, and that asks to be judged on audit quality, did not open a textbook already in its own bibliography on its own manifold's best-known algebraic property — and then wrote "defies Serre." One such sentence licenses a referee to assume the same about every other unchecked assertion in the 56-link table.

Related, same paragraph: the scattering determinant `φ(s) = Λ_K(s−1)/Λ_K(s)` "**exactly**, with no conductor character anywhere in the continuous part" is the formula for the *full* Bianchi group at class number one. `π₁(m004)` is an index-12 subgroup with one cusp. That the single-cusp scattering matrix of the cover is the base one with no level contribution is a statement needing a proof, not a table row. (Given item 1 it is probably both true and known — which is the point.)

---

## 5. Major objection: §2's "short catalogue" argument is about the wrong object, and the construction reaches two exceptional labels

§2:

> "A finite **subgroup** of `SL(2,K)` has all of its traces in `K`… Hence `2O` and `2I` — that is, `E₇` and `E₈` — are unreachable there, and only `E₆` remains. So there is not even a birthday problem to argue about: the space of outcomes has **one** exceptional element in it."

**(a) The mechanism is a quotient, not a subgroup.** The construction begins with a **surjection** `π₁(m004) ↠ 2T`. A trace-field constraint on *subgroups of `SL(2,K)`* says nothing about which binary polyhedral groups occur as *quotients* of the fundamental group. The printed argument does not address the object the construction uses.

For the record I checked the conclusion by brute force on `⟨a,b,t │ tat⁻¹=aba, tbt⁻¹=ab⟩`: **zero** surjections onto `SL(2,5) ≅ 2I`. So the conclusion happens to hold — but not for the reason given, and the paper needs the correct argument.

**(b) The construction as described reaches two of the three exceptional labels.** §4: *"the binary tetrahedral group sits at the object's **hyperbolic** end and hands over the exceptional algebra by the McKay correspondence, **exactly as the binary icosahedral group sits at the spherical, golden end and hands over the larger one**."* And Prop. 2.1 is built entirely on that end (`N=5`, `SL(2,Z/5) ≅ 2I`, `E₈`). So the construction has `E₆` *and* `E₈` in it, on the paper's own account. The §2 payoff — *"the space of outcomes has one exceptional element in it"* — is false for the construction actually described. §2 is a correct statement about imaginary quadratic subgroup realizations that is then used to make a claim about the construction, which reaches the real quadratic end too.

This matters because §2 is the paper's methodological showpiece: it is where the paper teaches the reader its own standard of evidence. The showpiece has a scope error in it.

---

## 6. Major objection: Proposition 2.1 is one of the two "surviving" facts and it carries no load

§5 says exactly two facts survive §2 and "everything this paper claims is built on them and on nothing else." One is arithmeticity (which §5 then says is load-bearing nowhere). The other is Prop. 2.1. Its content:

- The hypothesis is stipulated, as the paper concedes: *"the statement is conditional on that normalisation of 'level', which is **stipulated here rather than derived**."* `Λ(m) := m²+4` is chosen so that `Λ(1) = 5`.
- Given the stipulation the proposition reads: **`m² + 4 ∈ {3,5}` with `m ≥ 1` has the unique solution `m = 1`.** A strictly increasing function meets a two-element set at most twice. The only substantive ingredient is the order bound `|SL(2,Z/N)| ≥ 6N³/π² > 120` for `N ≥ 6`, which is elementary and correct.
- **It selects the wrong end.** The paper says so itself: *"`m = 1` is singled out by the modulus 5 and the binary icosahedral group — the golden, spherical end… **and not by the `2T` that hands over `E₆` at the hyperbolic end**."* So the one theorem the paper proves does not support any step of the chain the paper derives.
- The `N=4` paragraph is correct and well handled — but *"we were caught treating it as evidence here"* belongs in a lab log, not inside a proof environment.

A proposition that is conditional on a stipulation chosen to make it true, whose proof is a two-element Diophantine check, and which selects a branch the derivation does not use, is a remark. It should not be one of the two facts "everything this paper claims is built on."

---

## 7. Major objection: the chirality section's headline inference does not follow, and it is in the abstract

Abstract: *"the cohomological index… is zero on every finite twist of the geometric holonomy by a theorem, **non-zero on five members of the object's commensurability class** and on its degree-four cyclic cover, **and zero on the object's own reducible locus on every module computed**."* Framed throughout as: *"the bit is a property the class and the tower supply and the member does not."*

**(a) The two searches are not the same search.** Zero on the object = a bounded run (`m ≤ 4`, twists of order dividing 12, 235 modules). Non-zero on the five = at "cusp-trivial characters of order three **among others**." §9 concedes: *"**The rule that separates the five members that fire from the six examined that do not is not known.**"* With no rule and non-matching domains, "the object **withholds** the bit" is not supported by "we ran 235 modules and got zero." The supported statement is: *we found no non-zero index on the object within the modules we ran.* The abstract, the §16 three-column ledger and Non-claim 4 all use the stronger reading. Falsifier 6 concedes the weaker one ("the modules run are listed so that the search can be continued"). **This is the paper's largest overstatement and it is in the first paragraph a reader sees.**

**(b) The comparison is between a universal theorem and a regime the authors believe is unphysical.** Menal-Ferrer–Porti gives vanishing on *every* one-cusped hyperbolic 3-manifold — nothing about `m004` there. The non-vanishing is on **reducible non-split** modules, which §9 grades: *"not a background of a compact gauge group, whose flat holonomies are semisimple… its admissibility is an open question **with a prior against it**."* So "the class supplies what the member does not" compares a universal theorem against a computation the authors expect is inadmissible. That is not a contrast between the object and its class; it is a contrast between two different questions.

**(c) The section computes a quantity with no stated meaning, and says so.** §9's scope note: *"the index theorem that would license it lives on a Calabi–Yau threefold or a `G₂` manifold, and its transport to a real 3-manifold with boundary is **nowhere exhibited**"* — plus an explicit obstruction (integer spin under the Lorentz double; the only half-integer object is the holonomy's `C²`). The longest technical section of the paper therefore computes numbers that, by its own statement, cannot be read as generations and have no other stated physical interpretation. Either exhibit the transport, or retitle: §9 is about twisted cohomology of hyperbolic 3-manifolds, and the words "chirality" and "generation" should leave it and the abstract.

---

## 8. Major objection: there is no gauge theory, so "gauge structure" is not earned

The title and abstract say "gauge structure" and "Standard-Model structure." Non-claim 7 concedes: no four-dimensional dynamics, no rate, no field action. There is no spacetime, no field content on one, no compactification, no Lagrangian.

`E₆` arrives by McKay, which is a correspondence about `C²/Γ` Kleinian singularities and ALE spaces. Nothing in the paper connects that `C²` to the 3-manifold, to a spacetime, or to a gauge field. What is produced is: *a Lie algebra attached to a finite group that happens to be a quotient of `π₁`.* Any group with a `2T` quotient produces the same algebra by the same route — and §2 measures that this is one census manifold in three. The paper establishes the genericity and keeps the title.

"Gauge structure" implies a connection on a bundle. Nothing here is a connection on anything. The defensible title is something like *"What a hyperbolic 3-manifold does not determine: a null report on `E₆` structure from `m004`."*

---

## 9. The `Z′` paragraph should be deleted

§9's `Z′` paragraph contains the only physical numbers in the paper: `M_{Z′}/g_{Z′} ≳ 1.5×10²` TeV, `≳ 1.7×10³` TeV, a floor near `2` TeV·`g_{Z′}⁻¹`, and `Tr Q′²/Tr Y_GUT² = 6210/9`. By the paper's own accounting they rest on:

1. a spectrum that is **vector-like**, while the bounds assume "independent left- and right-handed rotations" — conceded in the same paragraph;
2. a **supersymmetry the object does not supply** — conceded, "three exact negatives";
3. an assumption that the vector-like copies are **kept light** — conceded, "an assumption we do not derive";
4. **gauge-coupling perturbativity failing below the unification scale** from three light `27`s — conceded, "a cost the model would have to pay";
5. an **unselected closing index** — conceded, "nothing in the construction selects the closing index";
6. an **unfixed family** — conceded, "which family it is, the construction does not fix";
7. an alignment that "**is not checked**."

Seven conceded defeaters for one paragraph. Numbers escape their caveats in citation; these will be quoted as "a knot-derived `Z′` bound." The paragraph transmits no information and imports a large misquotation risk. Cut it, and cut the corresponding "second handle" in §14.

---

## 10. Specific technical items

1. **The anomaly alphabet is never stated.** §7's headline count — "252 candidates… the colour cubic alone kills 222" — cannot be checked from the paper, because the "six Standard-Model-visible field types" are nowhere listed. I reconstructed them and got 252 → 30 exactly (so the number is right), but a reader should not have to guess the central object of the paper's most-quoted section. List them.
2. **The 30 → 2 step is not reconstructible at all.** "Rigid (no continuous deformation of the charges preserves the conditions)" plus Witten plus mixed plus gravitational, over hypercharges treated as free reals, with "exactly five multiplets" and "no multiplet of zero hypercharge" — this is a specification sketch, not a specification. Give the system.
3. **"Of 128 involution classes (Kac's count)"** (§6). `E₆` has **four** conjugacy classes of involutive automorphisms (inner: `su(6)⊕su(2)`, `so(10)⊕u(1)`; outer: `f₄`, `sp(4)`). Whatever 128 counts is never defined in the paper. Define it or cut it.
4. **"the 24 Standard-Model parameters"** (link 17) and **"nineteen free parameters (twenty-four with the neutrino sector)"** (§11). The standard counts are 19, and 19+7 = 26 (Dirac) or 19+9 = 28 (Majorana). 24 is not a standard count and no source is given. It appears twice.
5. **§9, "the object's own harmonic one-form is θ-odd and non-zero on the arcs of the fixed set: the object supplies no charge locus."** The inference needs the definition of a charge locus (presumably a zero set); as printed it is a non-sequitur.
6. **"two significant figures"** is the acceptance bar for the 352-pair period scan. For a scan designed to return nothing this is fine, but it should be said plainly: at 2 s.f. and 352 pairs the *expected* number of accidental hits is order 3. Reporting 351 misses and one hit is consistent with pure chance in *both* directions; the scan has essentially no discriminating power and should be described as a bound on the authors' effort, not as a negative result about the object. The same applies to the 23-invariant scan.

---

## 11. Production defects and internal inconsistencies (fix list)

1. **Broken bibliography entry.** `main.tex:1590` carries an orphan fragment immediately after the Thurston item:
   ```
   \bibitem{thurston} W.~P.~Thurston, ... lecture notes, 1978--80.
   \textbf{24} (1985), 307--332.
   ```
   This is the tail of a deleted `\bibitem` — almost certainly **Neumann & Zagier, *Volumes of hyperbolic three-manifolds*, Topology 24 (1985), 307–332**. As typeset it renders as stray text inside Thurston's reference. Restore the entry or delete the line.
2. **Riley is credited with no reference.** Chain link 6 reads "(Thurston, Riley)"; every other named author in the paper is cited. Add Riley (1975).
3. **Falsifier count contradiction.** §14 opens *"**Six** of the following would refute a specific claim"*; the scope note in the same section says *"All **five** falsifiers above are mathematical."* By the list's own labels six of the nine are falsifiers (items 1,2,3,4,5,7). One of the two numbers is stale.
4. **`anc/README.md` says "the **three** rows marked computed"**; `main.tex` and `MANIFEST.json` both have **five**.
5. **Appendix note reads "All 54 claims **below**"** — the table is above it.
6. **`MANIFEST.json` still carries a per-claim `"section"` field** while the appendix explains at length that section pointers were removed because they were unreliable. Drop it or validate it.
7. **Abstract states the base rate flatly** ("one in three one-cusped census manifolds"). §2 concedes the census is complexity-ordered and that the rate drifts 36.25% → 33.92%. Qualify it in the abstract.
8. **Strip source comments before submission.** `main.tex:27–32` ships a comment discussing the repository's privacy rule, the surname policy, and where the submission copy is built. arXiv source is public.
9. **Abstract asymmetry.** It lists the two inputs the global form is conditional on, but presents termination as unconditional ("the object forces the termination of the breaking chain"). §7 says termination presupposes the chirality input *and* an unformalised menu-completeness claim. Qualify both or neither.

---

## 12. Venue

- **`math.GT` primary is not defensible as it stands.** The paper offers one proposition with a proof (§6 above: trivial), and on the order of a hundred one-line assertions whose proofs are in a repository. A `math.GT` referee's first question is "what is the theorem?", and this document does not answer it.
- **`hep-th` cross-list is not defensible** because there is no field theory (§8 above), and the paper says so.
- **The extractable paper is real and small.** There is an honest 8–10 page `math.GT` note in here: the commensurability-class census of chirality against arithmetic (66 of 87 covers to degree 10 chiral while the invariant trace field persists; the 112-member `Q(√−3)`-shape family; `m202`, `s959`, `o10_150726` carrying chirality, the arithmetic, the `2T` door and the count of three together), plus the twisted-index computations on reducible non-split modules with `m010` as the validating witness and `t12839` as the cover. **With definitions, proofs, and no mention of `E₆`, hypercharge or the Standard Model**, that is a publishable contribution. Everything else in this document is either textbook, null, or unprovable from the text.
- The present document's honest home is a project technical report or a methods note on base-rate discipline in structural-coincidence programmes.

---

## 13. What would move me

1. **Name the theorem.** One sentence: "the new mathematical result of this paper is X." If no sentence fits, that is the answer to whether it is a paper.
2. **The dependency DAG**, or delete Figure 1 and the 52/56 tally.
3. **A third-party timestamp**, or delete "pre-registered" throughout and say what the seals actually certify (the ancillary README already says it correctly — the body does not).
4. **Fix the congruence paragraph**: cite the classical result, reconcile the levels, and delete "defies Serre's non-congruence base rate."
5. **Fix §2's argument** so it addresses quotients rather than subgroups, and drop "the space of outcomes has one exceptional element in it" — the construction has `E₆` and `E₈` in it.
6. **Weaken the abstract's chirality sentence** from "the object withholds" to "not found on the modules we ran," in line with Falsifier 6.
7. **Delete the `Z′` paragraph** and the `Z′` handle in §14.
8. **State the six-type alphabet** and the 30 → 2 system.
9. **Remove the results you say you cannot reproduce** — the several-cusp index run whose "scripts are not yet reproducible from a clean checkout," and the extended regulator run whose "certificate is not in our record." A paper does not carry results its authors cannot re-run; that is what a lab notebook is for.

---

## 14. Closing remark, since it is owed

I do not think this work is dishonest. It is the opposite: the paper argues against itself more effectively than I have, and most of my strongest objections are assembled from concessions the authors volunteered. That is genuinely unusual and the authors should not conclude from this review that the discipline was wasted.

But the discipline has consumed the content. A paper whose §2 demolishes its own entry point, whose §5 declares its headline uniqueness load-bearing nowhere, whose §7 hands its central forcing to a 1989 anomaly calculation "containing no token of the object", whose §15 concedes the landing algebra, the `Z₆` kernel, the `3/8` and the normalisation no-go to the literature, and whose §16 ends on a list of things that cannot be had, has published its own negative result and then declined to say so in the title. **The correct next move is not another revision. It is to write the four-page retraction note that §2 already contains, and separately to write the small honest `math.GT` paper that §9's census computations would support.**

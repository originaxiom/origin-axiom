# Opponent's report

**Manuscript.** *Standard-Model structure from the figure-eight knot complement: what is forced, what is withheld, and what must be supplied.* D. M., dated 2026-09-16. Reviewed from `main.pdf` and the arXiv bundle (`main.tex`, 1692 lines; `anc/` verification package, manifest built at commit `c6d8db7a`). Line numbers below refer to `main.tex`.

**Role.** This is an adversarial (opponent) review. I have tried to attack every load-bearing statement, and I have re-run every claim I could re-run without the author's repository. Where the paper is right I say so; where it is wrong or empty I say so with the same directness. Nothing here relies on the author's own test suite.

---

## 1. Verdict

**Recommendation: reject for the venues named (math.GT primary, hep-th / math.NT cross-list). Not acceptable in this form; not repairable by revision into the same paper.**

The manuscript is 40-odd pages of prose whose net *mathematical* content, once the author's own concessions are subtracted, is a handful of computer-checked facts about `m004` (surjection counts, chirality of covers, homology of cyclic branched covers, a corollary of Menal-Ferrer–Porti). Its net *physical* content is nil by the author's own accounting: no value is predicted, no four-dimensional theory is specified, chirality is absent, and every Standard-Model-shaped statement is either (i) textbook `E_6` representation theory, (ii) the classical anomaly-cancellation argument, or (iii) conditional on inputs (colour frame, "Standard-Model shaping", `Q = T_3 + Y`) that already contain the Standard Model. The paper concedes each of these individually (§Recognition, §Ledger) but keeps the title, abstract and framing that the concessions have emptied.

There is also at least one **false claim graded "settled" with a "lock"** in the verification appendix (§3.1 below), which is a direct hit on the paper's central rhetorical device: that "settled", "sealed" and "locked" rows can be trusted.

What could survive is a short, self-contained note in computational low-dimensional topology (§7). That note would carry none of the title's words "Standard-Model" or "forced".

---

## 2. What I verified independently (and it holds)

To be fair to the author: the checkable topology is right. I recomputed the following from scratch with SnapPy 3.3.2 and short Python scripts (no access to the author's repository):

| Claim (line) | Paper | My recomputation |
|---|---|---|
| Surjections `π₁(m004) → SL(2,3)` up to `Aut` (l.166) | exactly 2 | 48 surjections / 24 = **2** |
| Same for the sibling `m003` (l.178) | (implied 2) | **2** |
| First 400 one-cusped census manifolds admitting the surjection (l.170) | 145 (36.25 %) | **145** |
| ...admitting exactly two classes (l.170) | 124 | **124** |
| Class-count distribution (l.171) | 0:255, 2:124, 4:14, 6:4, 10:2, 12:1 | **identical** |
| Tie list (l.174) | m003, m007, m022, m026, m027, m029, m030, m033, m034, m036, m047 | **identical, same order** |
| `m003`, `m004` volume, `H₁`, CS, cusp shape, amphichirality (l.178–183) | as stated | **as stated** (CS(m003)=1/4, CS(m004)=0; cusp shapes ω and 2√3 i) |
| Covers of `m004` to degree 10 (l.1038) | 87 | **87** |
| Amphichiral covers: 9 cyclic + 1 regular; irregular chiral (l.1038–1039) | 66 of 77 | **66 of 77**; 12 one-cusped chiral covers, two chiral 5-cusped degree-10 covers, all as stated |
| Closed hyperbolic fillings in the grid |p|,q ≤ 8 (l.683) | 78 | **78** (87 coprime slopes, 9 exceptional in the grid plus ∞) |
| One-cusped census manifolds to seven tetrahedra with `H₁ = Z` (l.1032) | 2804 | **2804** (of 4587 one-cusped; sign patterns not re-tested) |
| `H₁(Y₃) = (Z/4)²` (l.1008) | yes | **yes** (Smith form diag(4,4)); also `|H₁(Y₉)| = 76²` |
| `M² = LR` for the golden substitution (l.404) | yes | **yes** |
| Hypercharge forcing: linear conditions → line, cubic → `−18(t−3)(t+3)` (l.744–749) | yes | **yes**; `Y_q=0` branch makes the cubic vanish identically, as stated |
| `Tr T₃² = 3`, `Tr Y² = 5` on the 27, ratio 3/8 (l.656) | yes | **yes** (16 gives 2 and 10/3; 10 gives 1 and 5/3) |
| `|SL(2,Z/N)| ≥ 6N³/π²`, 131.3 at N=6 (l.527) | yes | **yes** |
| 35 % miss in `α_s`, ~50σ in `sin²θ_W` at ±0.00004 (l.102–103) | yes | **34.7 %**, **47σ** |

So the author's computational pipeline produces correct census numbers where I could test it. The problems of this paper are not arithmetic slips in the census; they are (a) one substantive mathematical error, (b) internal contradictions, (c) an absence of any theorem worth the name, and (d) a physics narrative that the mathematics does not support.

---

## 3. Major objections

### 3.1 A false "settled" claim: the figure-eight has arithmetic Dehn fillings inside the author's own grid

Lines 682–686 and appendix row 53 (l.1565) assert: *"of the grid's 78 closed hyperbolic fillings, zero keep Q(√−3) and **zero are arithmetic** (54 in the first census, completed to 78 of 78 on re-computation)"*, graded **settled**, backed by records `B286/B287/B288` with test locks.

This is false. `m004(5,1)` is the **Meyerhoff manifold** (volume 0.98136882889…, `H₁ = Z/5`), and Chinburg proved in 1987 that it is arithmetic (T. Chinburg, *A small arithmetic hyperbolic three-manifold*, Proc. AMS 100 (1987) 140–144), with invariant trace field the quartic field of discriminant −283, `Q(x)/(x⁴ − x − 1)`. The slope (5,1) satisfies |p| ≤ 8, q ≤ 8, and so does its mirror (−5,1). I confirmed numerically (60-digit holonomy, PARI `algdep`) that the traces of squares of the generators of `π₁(m004(5,1))` generate a degree-4 field of discriminant −283 isomorphic to `x⁴ − x − 1`; the paper's own SnapPy pipeline would return the same.

Consequences:

1. The sentence "the closed object carries a canonical closing and no exceptional algebra … the two cannot be held at once (C46)" (l.684–686) loses its second half. Whether an arithmetic filling "keeps" anything the paper wants is a separate question, but *"zero are arithmetic"* is simply wrong, and link 46 of the chain rests on it.
2. Much more seriously: this row passed every layer of the paper's verification apparatus — a record with verdict `NEGATIVE`, a primary lock `test_b288_arithmetic_filling_census.py`, five "mentions", and a "re-computation completed to 78 of 78". The appendix admits (l.1477–1484) that locks are "traceability, not re-derivation" and that the suite "has certified a claim later withdrawn". Here is a second one, found by an outside reader in an afternoon with the standard reference. **The reader is therefore entitled to assign zero evidential weight to the words "settled", "sealed", "locked" and "verified" everywhere in the paper**, which are precisely the words the paper leans on in place of proofs.
3. The author must state *what test of arithmeticity was run*. My guess is that the code tested whether the invariant trace field is `Q(√−3)` (or a quadratic field), not the Maclachlan–Reid criterion (one complex place, integral traces, algebra ramified at all real places). A wrong criterion consistently applied to 78 manifolds is exactly the failure mode that "re-computation" cannot catch.

### 3.2 There is no theorem in the paper

The paper repeatedly calls things "a theorem", "a theorem of record", "proved", "settled". I looked for a statement with hypotheses, conclusion and proof. There are two:

* **Proposition 4.1** (l.499–537). Define `Λ(m) = m² + 4` by fiat; note that `Λ(m) ∈ {3,5}` forces `m = 1`. That is the entire content. The author concedes the normalisation is "stipulated here rather than derived" (l.506). The surrounding page about `N = 4` being an order coincidence is correct but irrelevant. Worse, the proposition selects `m = 1` through `N = 5`, i.e. through `2I` and `E_8`, "and not by the `2T` that hands over `E_6`" (l.508–509). So the paper's only proposition points at a different exceptional algebra than the paper is about. Delete it.
* **The hypercharge computation** (l.740–759). Classical (Geng–Marshak, Minahan–Ramond–Warner, Foot–Joshi–Lew–Volkas), correctly reproduced, and acknowledged as such at l.1312–1316.

Everything else that is called a theorem is a one-line label in a generated table (l.329–384: "the parity of the cusp", "the genesis dictionary", "the tower law and the Standard-Model closings"), or a paragraph of prose that cites "the record". A referee cannot check "Theorem 35: the generation shape: flavour triplets replicate fixed colour × su(2) types (sealed cell)". A paper that says (l.563–565, Non-claim 9) that it does *not* state its forced links in checkable form has conceded it is not a mathematics paper.

### 3.3 The "56 links, 52 forced" accounting is not a derivation and the number is not meaningful

* Links 1–5 (l.329–333) are not mathematics. "Being is inexhaustible description" is an **axiom**; link 2's "minimal-description criterion" is unspecified and, by the author's own census (l.1015–1020), is chosen among eight formalisations of which one (least Pisot number → plastic number) gives a different answer. The passage word → punctured torus → orientation is two more axioms. The author states plainly (l.200) that *"no other object was tried before m004: it was the programme's starting hypothesis, and the selection theorems that now single it out were found afterwards."* That is the definition of a post-hoc construction. The chain is reverse-engineered from its endpoint and then counted as if it were a deduction.
* "Forced" is defined as "not a declared choice" (l.243). By that definition a **no-go result** (links 16, 17, 43, 44, 45, 52), a **census** over a bounded grid (links 8, 56) and an **identity** all count as "forced links in a derivation". A negative result is not a link that carries a derivation forward; a bounded census is exactly a choice of bound. The "52 of 56" number is an artefact of the typing scheme.
* The links are not in dependency order: the author admits (l.256–259) that the "measurement links 24–42 carry numbers after the observer's axiom 18 … because they were banked later, not because they depend on it". So the figure's "shape" (axioms at the ends, none in the middle) is a statement about the order in which files were written.
* The two accountings of the entrance ("seven forks, two fragile" vs "four axioms") were reconciled *after* "an external reader" found that the first undercounted (l.219–221). The paper records this; it does not explain why a reader should believe the current count.

### 3.4 The object contributes nothing that a random third of the census would not, and the paper knows it

Section 2 is the strongest part of the paper and it refutes the title. By the author's own numbers: the `E_6` recurrence is a graph identity (probability 1); the `2T` surjection is shared by 1696 of 5000 one-cusped manifolds (l.196); `m003` shares the invariant trace field *and the volume*; the base-rate section concludes "genericity removes the endpoint's power to confirm the beginning" (l.192). What is then claimed to be object-specific is "the invariant trace field `Q(√−3`)" — but §4 immediately says that is a commensurability-class invariant, so "the honest form of this paper's positive content is a theorem about the commensurability class of `Q(√−3)`" (l.489–490). **No such theorem is stated anywhere.** And where does `Q(√−3)` actually enter the Standard-Model-facing structure? I traced every occurrence: (i) as `SL(2, O_K/(√−3)) = SL(2,3)`, i.e. the same `2T` door 1/3 of manifolds have; (ii) as the coefficient field `Q(ζ₃)` of a twist in the index-vanishing argument (l.964–967), which is a fact about cyclotomic fields, not about the manifold; (iii) in a "Galois firewall" whose actual field is a cubic field of discriminant `3⁴·7·11` with resolvent `Q(√77)` (l.618–619) — where 7 and 11 come from is never explained. None of these is a use of the invariant trace field as physical input.

So the title's preposition "from" has no referent. The correct title of the paper as written is *"Nothing Standard-Model-specific follows from the figure-eight knot complement, and here is a ledger of what we put in."*

### 3.5 No physical framework is ever specified, so "gauge structure extracted from a manifold" has no meaning

The paper never says what the 3-manifold *is* physically. Is it a compactification space (then from which dimension, with what fields, and why is a 7D `E_6` gauge theory on `Y³` the right starting point)? A spatial slice? A "carrier" of a "word"? Without this, every physics statement is imported by analogy:

* The **McKay correspondence** relates finite subgroups `Γ ⊂ SU(2)` to affine ADE diagrams. Applying it to a finite *quotient* of `π₁(M)` yields a Dynkin diagram, i.e. a label. Nothing turns that label into a Lie algebra acting on anything. In M-theory, ADE gauge symmetry arises from a `C²/Γ` singularity where `Γ` acts on normal directions — a different `Γ` altogether, not a quotient of `π₁` of a 3-manifold. The paper's "the exceptional algebra is handed over by McKay" (l.442, 600–606) is a mnemonic dressed as a mechanism.
* The **anomaly conditions** (l.709–759) are 4D QFT statements. The author stresses "no token of the object appears in that computation" (l.718). Correct; so why is it in the paper?
* The **running of couplings** (l.100–104, 1297–1309) is "imported Standard-Model dynamics, not anything the object supplies" (l.560). Again correct; again, why is it here, and why is the failed non-SUSY run reported while "the supersymmetric crossing has not been run"?
* The **`Z'` phenomenology** (l.995–1007): kaon-mixing floors derived for a *supersymmetric* model whose supersymmetry "the object does not supply" (three exact negatives, l.993), on a spectrum that is *vector-like* (so the model's chiral-rotation assumption is false), with three light complete 27's that the author admits destroy perturbativity (l.1006). Every hypothesis of the analysis is known to fail. This paragraph should be deleted, not "recorded as a fork".
* The **"closings"** `Y_n` (l.979–992): cyclic branched covers of `S³` over the knot, with `E_6` "broken by discrete Wilson lines through `H₁(Y_n)`" and copies of the 27 counted under the residual symmetry. Counting `H⁰(Y_n; 27_ρ)` for a finite abelian holonomy is a finite group-theory exercise; calling the results "vacua" (19,624 of them) and "generations" — even "in the structural sense" — is the identification the paper's own scope note (l.903–910) says is not earned.

### 3.6 The chirality section conflates four different things called "chirality"

The word is used for: (a) **amphichirality** of a 3-manifold (existence of an orientation-reversing isometry, l.1037–1045); (b) **fixed-point counts** of isometries of the cusp (l.917–931); (c) **net 4D fermion chirality** `h¹(27) − h¹(27̄)` for a local system (l.936–938); (d) a home-made **index** `I(V) = t₀ − r₁` on twisted cohomology (l.955–961). The paper slides between these. Two examples:

* "Of the object's 87 covers to degree 10, 66 are chiral while the object is not … those 66 carry a remembered handedness together with the arithmetic" (l.107–109, 1039–1041). This is sense (a): 66 covers lack an orientation-reversing isometry. That has nothing to do with sense (c). The rhetorical suggestion that a chiral cover is "closer" to a chiral spectrum is unsupported, and the paper's own computation of the index on those covers returns zero on every sector (l.1042–1044).
* The index (d) "stands in for net chirality" (abstract, l.51). No argument is given that it does. The only justification for a chirality index in this kind of setting is an index theorem on a `G₂`- or Calabi–Yau-type space, and the paper concedes (l.907) that "its transport to a real 3-manifold with boundary is nowhere exhibited", and moreover that under the Lorentz double the whole tensor tower of the 27 is integer-spin. So the instrument is a number whose relation to the thing it "stands in for" is absent by the author's own admission.

The two vanishing results are correct and trivial: symmetric powers of `SL₂` representations are self-dual, and the Menal-Ferrer–Porti injectivity theorem transferred through a finite cover kills the index on every geometric-holonomy twist of every one-cusped hyperbolic manifold. That is a **universal** fact; the abstract's sentence "the chirality bit is what the object withholds" presents a universal no-go as an object-specific finding. Where the index does fire — on reducible **non-semisimple** modules — the author concedes they are "not a background of a compact gauge group" (l.977) and grades their admissibility "open with a prior against it". So the headline of the abstract ("non-zero on five members of the object's commensurability class and on its degree-four cyclic cover") is a non-zero value of an uninterpreted instrument on inadmissible backgrounds.

### 3.7 Internal contradictions

1. **The cubic is both decisive and redundant.** Lines 746–750: the three linear conditions cut to a line, "the remaining cubic condition evaluates to `−18(t−3)(t+3)`, so `t = ±3` and nothing else." Line 770 ("Control"): "the cubic condition is redundant once the three linear ones hold." Both cannot be true in the same frame; I verified the first (the cubic is *not* identically zero on the line). If the "Control" refers to a different computation (the 252-content census with charges fixed by the 27), it must say so; as written the paper contradicts itself in consecutive paragraphs, and appendix row 40 (l.1552) carries the contradiction as a "computed" claim.
2. **Falsifier count.** Line 1357: "Six of the following would refute a specific claim". Line 1393: "All five falsifiers above are mathematical."
3. **Continuous inputs.** Abstract (l.55): "two continuous anchors". Ledger: `σ`, `λ`, *and* `P(B₀)` at "≤ 3 continuous" (l.1178). That is up to five.
4. **Discrete inputs.** Abstract: "seven non-continuous rows". The ledger row "family, VEV, filling" (l.1202) bundles three independent choices into one row; the honest count is at least nine.
5. **Rank reduction.** Line 880–882 says an earlier draft called it "a theorem" while another section exhibited it being paid; the current text (l.786–788) still says the second abelian factor "is removed by an expectation value listed as an input" and in the same paragraph calls the termination "the theorem".
6. **What the paper is about.** §Chain: "twelve links and no choices … where the derivation earns its keep" (l.431). §Unique: those twelve links "are theorems about the commensurability class … not the manifold's" (l.456–457). §Middle: they are, respectively, (7) a computation of three quadratic subfields of a compositum, (8) a bounded census, (9) a congruence claim "not yet checked against the literature", (10) a generic Eisenstein-series fact, (11)–(15) unexplained one-liners, (16)–(17) negatives. The "keep" the derivation earns here is nothing.

### 3.8 Statements that are unsupported, generic, or numerically suspicious

* **"128 involution classes (Kac's count)"** (l.646). `Aut(e₆)` has exactly four conjugacy classes of involutions (two inner, two outer), giving the four non-compact real forms. 128 = 2⁷ looks like the number of sign vectors on the seven nodes of the affine diagram, which is not a count of classes and is not Kac's. Either the sentence or the attribution is wrong.
* **Congruence** (l.583–585): "a statement that defies Serre's non-congruence base rate, computed twice on our own benches and not yet checked against the literature." A paper cannot grade a claim "settled" (appendix row 45) while saying it has not been checked against a literature that exists. "Level 4 in the SL-kernel convention; geometric index 12 at level 8" is also garbled: the index of the figure-eight group in `PSL(2,O₃)` is 24 by volume (2.0299 / 0.0846), 12 in `PGL`. Which group, which level, which convention?
* **Scattering determinant** (l.585–588): for a one-cusped finite-index subgroup of a one-cusped Bianchi group, the Eisenstein series is the restriction of the Bianchi one by uniqueness, so `φ(s) = Λ_K(s−1)/Λ_K(s)` up to normalisation holds for *every* such subgroup (including `m003`). "Character rigidity" is a grand name for this.
* **`μ = 2304/953`** (l.653), **`6210/9`** (l.1004), **`c_BH = 6σ`** (l.1161), **`Q(√77)`, `3⁴·7·11`** (l.619): unexplained numbers presented as if the reader could recognise them.
* **Jørgensen selection** (l.1111): "`m004` is the unique orientable solution of a minimisation". Callahan's theorem is about Jørgensen number, a property of a Kleinian group's generating pairs; presenting it as "variational selection of the object" after the object was chosen (l.200) is decoration.
* **The modular-flow "theorem"** (l.1164–1177, 1435–1449): a tracial von Neumann algebra has trivial modular flow. This is true of every II₁ factor and says nothing about `m004`; calling the resulting freedom "external by theorem" is vacuous. The Connes–Rovelli citation adds no content.
* **"The observer's bit is consciousness, or not"** (Non-claim 8, l.562; l.1129–1133). This sentence should not appear in a paper submitted to math.GT.

### 3.9 The verification apparatus is self-referential and, as §3.1 shows, unreliable

The abstract, README and appendix all say verification is "internal to the project's own re-runnable pipelines; no external review or endorsement is claimed". Fine, but then: seals "certify integrity, not chronology" (README l.18–24), i.e. the "pre-registration" the paper invokes (l.418 footnote, l.647, 960) is *not* established by the seals; "lock" means a test *names* a record, not that it re-derives the number (l.1492–1495); the suite has certified a withdrawn claim before (l.1477) and, per §3.1, certifies a false one now. The `.tex` source itself carries an internal review trail ("Review 56, R56-10", l.39) — an AI-assisted loop by the author's description (l.124). None of this is independent checking, and the paper should stop using the vocabulary of pre-registration and proof for it.

### 3.10 Presentation

* **Private vocabulary.** "The object", "the record", "the wall", "the arena", "the closing", "the genesis", "the observer's closings", "the four-letter principle", "the two-column law", "structural floors", "flavour atoms", "the beat", "register", "sealed cell", "the shadow-rule forks", "the silver world", "the golden Galois branch". None is defined in the paper. A mathematician or physicist cannot read it.
* **Changelog in the body.** Roughly a fifth of the text is "an earlier draft said X; we now say Y" (l.172–175, 219–221, 316–322, 438–445, 693–696, 881–882, 1064–1077, 1114–1127, 1301–1305, 1351–1353, 1370–1371, 1376–1378, 1394–1396, 1488–1495). This belongs in a repository log, not in a paper.
* **Rhetorical style.** Bold assertions ("**The geometry forbids it**", "**The two cannot be held at once**", "**This is why the bit is exactly one, and external**") stand in for arguments; every section carries "scope notes" that retract it.
* **Bibliography defects.** Line 1590: an orphaned fragment "`\textbf{24} (1985), 307--332.`" follows the Thurston entry (looks like the remains of a Neumann–Zagier, *Topology* 24, entry). "Riley" is named in link 6 (l.334) with no reference. Chinburg (1987) is absent, and is the reference that falsifies §3.1.
* **Classification.** There is no new theorem in geometric topology; `math.GT` primary and the MSC 57K32 heading are not justified. `hep-th` would ask what the theory is. The honest category is `physics.gen-ph`.

---

## 4. Specific corrections (line-referenced)

| Line | Issue |
|---|---|
| 39 | Internal review tag (`Review 56, R56-10`) in the source. |
| 100–104 | "about fifty experimental standard deviations" uses the MS-bar error 0.00004; say so, or drop the σ count as you do elsewhere. |
| 166 | "exactly two up to automorphism" — verified, but say up to `Aut(SL(2,3)) ≅ S₄`; also note `m004` has **no** surjection onto `2O` or `2I` (I checked; 0 and 0), which is the fact your "short catalogue" argument (l.156–163) needs and does not actually prove, since that argument concerns finite *subgroups* of `SL(2,K)`, not abstract quotients of `π₁`. |
| 334 | "(Thurston, Riley)" with no Riley reference. |
| 499–537 | Proposition 4.1: trivial by construction; delete. |
| 583–585 | Congruence claim graded settled but unchecked against literature; "level 4 … index 12 at level 8" needs a definition. |
| 646 | "128 involution classes (Kac's count)": wrong or misattributed. |
| 682–686, 1565 | "zero are arithmetic" is false: `m004(±5,1)` = Meyerhoff, arithmetic (Chinburg 1987). |
| 746–770 | Cubic decisive vs. cubic redundant. |
| 903–910 vs. 979–992 | "Counts are counts" vs. "three complete copies … generations". |
| 995–1007 | `Z'` bounds on a model every hypothesis of which fails; delete. |
| 1178 vs. abstract | "≤ 3 continuous" vs "two continuous anchors". |
| 1202 | Three choices in one row. |
| 1357 vs. 1393 | Six vs. five falsifiers. |
| 1590 | Orphaned bibliography fragment. |

---

## 5. Questions I would put to the author at a defence

1. State one theorem, with hypotheses and proof, that is (a) true of `m004` and (b) not true of `m003`, and (c) used by anything Standard-Model-facing in the paper. If there is none, what does "from the figure-eight knot complement" mean?
2. What is the physical setting? Dimension, field content, and the role of `M³`. Why does a finite quotient of `π₁(M)` act as a gauge group?
3. What test of arithmeticity did record `B288` run on the 78 fillings, and why did it return "not arithmetic" for the Meyerhoff manifold?
4. On the line `Y_q=1, Y_u=−1+t`, is the cubic anomaly condition redundant (l.770) or is it the condition that fixes `t = ±3` (l.749)?
5. In what sense does `I(V) = t₀ − r₁` "stand in for net chirality"? Give the index theorem, or withdraw the phrase from the abstract.
6. After removing (i) statements the §Recognition list marks as standard, (ii) statements conditional on the colour frame, the SM shaping, and `Q = T₃ + Y`, and (iii) negatives that hold for every one-cusped hyperbolic manifold, what remains? Please list it.
7. Why is a paper whose abstract says it predicts no value, derives no theory, and withholds chirality, titled "Standard-Model structure from …"?

---

## 6. On the paper's own defence

The manuscript anticipates criticism by conceding almost everything in scope notes and non-claims, and then asks to be judged on "the location of the boundary" and "the pricing of the residue". A boundary is informative only if either side of it is. Here the positive side is empty of object-specific content (§3.4) and the negative side consists of universal facts (homogeneity of anomaly equations, Mostow rigidity, self-duality of `Sym^m`, injectivity of MFP, triviality of modular flow on a trace) plus bounded searches. Reporting that a construction with no mechanism produces no numbers is not a result; it is the null hypothesis.

---

## 7. What could be salvaged

A short note (5–8 pages, experimental mathematics / computational topology), with no physics vocabulary, containing:

1. The census of `SL(2,3)`-surjections for one-cusped census manifolds (counts up to `Aut`, the class-count distribution, the 112-member `Q(√−3)`-shape family), with the enumeration method stated.
2. The chirality census of the 87 covers of `m004` to degree 10 and of the `Q(√−3)` family, by an explicitly orientation-aware test, with the method stated.
3. The observation that for `V = Sym^m(hol) ⊗ F` with `F` of finite image, `H¹(M;V) → H¹(∂M;V)` is injective by Menal-Ferrer–Porti through a finite cover, stated as a corollary with its two-line proof; and the explicit non-semisimple modules on `m010` and on the listed class members where the paper's index is non-zero, stated as a computation with the modules written down.
4. The twisted-class criterion on the cyclic branched covers `Y_n` (product of `n` explicit `2×2` matrices equal to the identity), stated and proved.

Each item must be stated so that a reader can check it from the note alone. None of these items justifies the words "Standard Model", "forced", "chirality bit", "observer", or "ledger".

---

## 8. Summary for the committee

* The recomputable topology is correct (§2).
* One "settled, locked" mathematical claim is false against a 1987 reference (§3.1), which voids the evidential weight of the paper's verification vocabulary.
* There is no theorem in the paper beyond a trivial proposition and a classical calculation (§3.2).
* The "56 links / 52 forced" chain is a post-hoc list, not a derivation (§3.3).
* By the author's own base rates, nothing Standard-Model-facing is specific to `m004`, and `Q(√−3)` is never actually consumed (§3.4).
* No physical framework is specified; McKay, anomalies, running and `Z'` limits are imported by analogy (§3.5).
* "Chirality" is four different things, and the headline index is uninterpreted and fires only on inadmissible backgrounds (§3.6).
* Several sentences contradict each other (§3.7).
* The paper is not readable without the author's private repository and vocabulary (§3.10).

**Reject.** Encourage the author to extract §7 as a self-contained computational note.

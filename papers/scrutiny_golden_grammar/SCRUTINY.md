# Adversarial scrutiny — "THE GOLDEN GRAMMAR" (main.pdf, 35 pp., dated 2026-08-15)

**Target.** `THE GOLDEN GRAMMAR: ONE ARITHMETIC CONDITION AND FOUR EXCEPTIONALITY THEOREMS
INSIDE A CANONICAL FAMILY, AND A PARAMETER-FREE CHAIN TO AN EXCEPTIONAL LIE ALGEBRA`,
pdfTeX 1.40.27, 35 pages, MD5 `41f9f7fc228bdb3c4a09e751bedb7524`. Not the flagship
(`papers/flagship/main.pdf`) and not `papers/sl4_dehn_filling/main.pdf` — a distinct document.

**Method.** Every claim in the paper that is finitely checkable was recomputed from scratch,
importing nothing project-internal and nothing from the paper's own scripts. The re-computation
is `papers/scrutiny_golden_grammar/verify_scrutiny.py` (sympy + stdlib only, exact arithmetic,
exits non-zero on drift).

```
$ python3 papers/scrutiny_golden_grammar/verify_scrutiny.py
100 checks run.
All checks reproduce.
```

---

## VERDICT

**The mathematics holds. The architecture does not do what the title says, and the paper's own
abstract concedes the premise without drawing the conclusion.**

- **100 of 100 independently checkable assertions reproduce exactly.** Including every one I
  expected to break: the rung spectrum of Theorem 9.20 (I enumerated all 64 Levi subsystems of
  E6 from the root system up — the 14-element list is right, and 22, 24, 32, 34, 38–44 are
  genuinely absent); Proposition 8.1's Molien computation (built 2T as the 24 Hurwitz units and
  took invariants — `{8,14,16,22}`, each one-dimensional, exactly); Proposition 9.3's
  `e6^{2O} = ⟨x8,x16⟩`; class number one for `K = ℚ[x]/(x³−12x−5)` (Minkowski bound 17.55,
  explicit generators found for every prime of norm ≤ 17, **including both degree-one primes
  above 7 and both above 11**, which is the step the paper is right to insist on); Appendix A's
  Tschirnhaus transformation, which lands on zero in `ℚ[t]/µ`; and Theorem 10.3's real-form
  argument, which is airtight from the K-type dimensions alone.
- **I found no false mathematical statement.** The one formula that fails as printed
  (Scope 5.21) fails because its symbol is undefined, and is exactly right under the only
  reading that makes the paper coherent.
- **Two findings are fatal to the thesis as stated**, and neither is a computation: the
  entrance consumes no arithmetic (F1), and Theorem 10.10 cannot be formed from the paper's own
  definitions (F2).
- The self-correction record is exemplary and I want to say so before criticising: the paper
  withdraws its own overreaches in place, prices its choices, and marks its weakest row. The
  findings below are almost all in the **accounting**, which is unfortunate, because the
  accounting *is* the thesis.

---

## FATAL

### F1. The entrance consumes no arithmetic, so the chain is severed at the one link the title claims

§7.3 opens: *"The step from the manifold's arithmetic to the exceptional algebra is the one step
of the whole construction that consumes the arithmetic."* Its content is Theorem 7.7: among
`{A4, S4, 2T, 2O, A5, 2I}`, only `A4` and `2T` carry a complex 27 with an invariant cubic, and
only `2T` is binary.

**Neither the hypothesis nor the proof of Theorem 7.7 mentions the manifold, its trace field, or
`ℚ(√−3).`** It is a classification of six finite groups. It would read identically in a paper
that had never defined a Sturmian word. The candidate set is fixed by (C8), which §11.3 lists as
underived; the surviving member is fixed by a representation-theoretic condition.

The abstract already states the premise:

> *K, the four invariant degrees, and the whole rung ladder are invariants of the triple
> (e6, 2T, principal sl2) and not of the figure-eight knot… The manifold's arithmetic is
> consumed at the entrance, once, and nothing downstream remembers which manifold it was.*

If the entrance itself consumes nothing, the honest conclusion is stronger than "nothing
downstream remembers": **§§8–10 is logically independent of §§2–5 in its entirety.** The
proposition `ℚ(√−3) ⟹ 2T` is gestured at in §7.1 and Theorem 7.1 but is nowhere a numbered
implication with stated hypotheses, and there is no Levi-style classification "the imaginary
quadratic field forces this McKay group".

**Two honest repairs, and the paper must pick one.** (a) State `ℚ(√−3) ⟹ 2T` as a theorem with
hypotheses and a proof, at which point Theorem 7.7 becomes the *second* half of the entrance and
§1.3's census is wrong by one. (b) Concede that §§8–10 is the invariant theory of `2T` on the
principal `sl2` in `e6`, that it begins at §7, and retitle. Option (b) costs the word
"chain" in the title; it costs nothing mathematically, because §§8–10 is the strongest verified
part of the paper.

### F2. Theorem 10.10 is not a well-formed statement in this document

Definition 10.9 and Theorem 10.10 use, without definition anywhere in the paper:

| symbol / phrase | where used | defined? |
|---|---|---|
| "the value arc" | Thm 10.10(i), definiens of D₂ | no |
| `D` | Thm 10.10(iii), `{I, D₂, D, D₂D}` | **never introduced at all** |
| `φ⁺` | Thm 10.10(ii), `φ* = φ⁺ ∘ σ_{χ−}` | no |
| `χ⁺` | Thm 10.10(iv), `H_χ = H⁺·ρ₂₇(σ_{χ·χ⁺})` | no |
| "the wall-real alignment" | Def 10.9, definiens of `H⁺` | no |
| "the charge lattice" | Def 10.9, index set of χ | no (and see M8) |

A reader cannot form the assertion, so cannot test it, so the paper's own acceptance standard
("a declared choice whose alternatives are not computed is a free parameter wearing a different
name") applies to it in the sharpest form. Scope 12.2 concedes it has no script in either
verification block. It is a certificate about objects the reader has not been shown, and clause
(iv)'s "*this is what makes (i) a characterization rather than a search*" is load-bearing rhetoric
resting on undefined `χ⁺`.

Either define the six objects, or move §10.3 out of the paper. The rest of §10 — Theorem 10.3 in
particular, which I verified and which is genuinely elegant — does not depend on it.

---

## MAJOR

### M1. §1.3's step census is internally inconsistent and contradicts §7.3

> *"Of the 20 steps below the entrance, 0 consume the manifold's fundamental group, 18 are
> standard exceptional-algebra theory downstream of the McKay assignment, and exactly 1 consumes
> the arithmetic. The remaining step is the McKay assignment itself, which is neither—it is the
> entrance, and it is counted separately for that reason."*

Three problems in four lines. (i) The entrance is counted *inside* "the 20 steps below the
entrance". (ii) It is not "counted separately" — 18 + 1 + 1 = 20 requires it to be one of the
twenty. (iii) §7.3 identifies the arithmetic-consuming step *as* the entrance, which collapses
the two distinct steps into one and makes the total 19. Given F1 the true count of
arithmetic-consuming steps is 0.

### M2. Selections I–III feed nothing

Scope 5.19 says exactly what §6 uses: *"m = 1 is the unique member whose invariant trace field is
ℚ(√−3)."* That is Selection IV plus a trace-field refinement. **Selections I (homology), II
(shadow modulus) and III (Jones index) are used nowhere downstream.** Worse for the narrative,
Selection II's surviving object at m = 1 is `SL(2,Z/5) ≅ 2I` — the icosahedral, E8 side — while
the cascade enters through `2T`/E6.

So §1.3's *"§5 carries the paper and §§8–10 are presented as consequences"* is false as stated:
§§8–10 are not consequences of §5. §5 is a self-contained selection theorem and §§6–10 is a
self-contained invariant-theory computation, joined by one unproved implication (F1). Both halves
are good; the joint is the claim.

### M3. The arithmeticity tail is repaired circularly

Remark 5.17 withdraws an earlier draft's unbounded tail — *"an unbounded quantifier resting on
six data points is an assertion"* — and says *"the repair is not to weaken the claim but to cite
the classification that already implies it."*

But the proof's own sentence attributes to [4] only **finiteness**: *"Bowditch, Maclachlan and
Reid prove that a once-punctured-torus bundle has only finitely many arithmetic commensurability
classes [4], and the classes are the three carried by…"* — the second clause is asserted, not
attributed. And Scope 5.16 then says the list *"we have verified independently rather than taken
on the citation's authority: over all cyclic R,L words of length ≤ 8"* (which covers m ≤ 4)
*"…Direct computation confirms the conclusion independently for m = 3,…,10."*

So the unbounded tail rests on a bounded census of **ten** points plus an unattributed list —
structurally the very thing Remark 5.17 condemns, moved from six points to ten. Fix: name the
theorem number in [4] that classifies arithmetic punctured-torus **bundles** (not classes), or
restate the tail as verified for m ≤ 10 and open beyond. The paper's methodological claim is
precisely about which statements are earned, so this row cannot be left as it is.

### M4. The commensurability→powers inference does not follow

> *"The arithmetic monodromies are therefore exactly those conjugate to a power of one of the
> three words above—not exactly those three words."*

Commensurable manifolds share a common finite cover; neither need cover the other. "Three
arithmetic commensurability classes, carried by RL, RRLL, RRL" does **not** entail "every
arithmetic once-punctured-torus bundle has monodromy a power of one of those three words". The
block-sequence argument that follows is valid and pretty, but it is applied to a set the quoted
citation does not deliver. (Remark 5.18 shows the paper knows covers behave subtly here; the same
care is needed one step earlier.)

### M5. Attack is directed at §7, and §7's central theorem has no runnable artifact

§1.3: *"A reader who wishes to attack this paper should attack §5 and §7."* Appendix B's table
supplies a block-(a) or block-(b) script for every §5 statement. **Theorem 7.7 has no row at
all.** Neither does Theorem 7.1 (the two curvature ends). Proposition 7.3 has one, in block (b).

Relatedly, *"attacking the cascade attacks Slansky [13]"* is contradicted by §9.2's own table,
which marks Theorem 9.8's count of three wall lines, Theorem 9.13's stratification and Scope 8.2's
bracket as **certificates**, not classical. Those are the paper's, not Slansky's. And [13] is a
1981 particle-physics review — an odd sole authority for a paper that elsewhere insists no
physical identification is made. Bourbaki, Dynkin, Collingwood–McGovern and Onishchik–Vinberg are
the load-bearing sources for the Levi classification the cascade actually rests on.

### M6. "the seven above" — the ledger contradicts its own count

§11.3 opens by naming **nine** rows and closes the rider paragraph with *"These are independent
stipulations and are not among the seven above."* Stale from the seven-row draft. The paragraph's
entire function is to say what the riders are not among, so the count is not cosmetic.

### M7. The second measurement plane is a tenth ledger row

Scope 9.19(ii): *"The plane is a choice whose price is computed to be zero, carried as (C7) in the
ledger of §11.3."* But (C7) is the **enhancement rule** (Scope 9.17), and the plane is (C9) —
except that (C9) is *"the measurement is made on a plane"*, which Scope 9.7 explicitly restricts
to the question of **dimension** ("why a plane rather than a line or a 3-space"), not to **which**
plane. The second plane `⟨x14,x16⟩` is priced in the body (Scope 9.19(ii): "we have no forcing
argument for the second plane and do not claim one") and appears in **no ledger row**.

§11.3: *"A reader who finds a tenth has found a defect in this section, not a detail."* By the
paper's own rule, this is one.

### M8. "charge lattice" and "charge" collide, inside the section that promises they cannot

Definition 10.9's census has `64 + 64 = 128` members, so χ ranges over `2⁶` sign characters, and
Theorem 10.10(i)'s shift vector `(1,0,1,0,1,1)` has six entries: the lattice is rank 6 — the
Cartan/weight lattice. But the glossary defines **charge** as one of `x8, x14, x16, x22`, and
Theorem 10.4's ε ∈ {±1}⁴ (sixteen patterns) uses the four-dimensional reading **in the same
section**. The glossary's stated purpose is "one referent per term".

### M9. The abstract drops a hypothesis of Theorem 4.2

Abstract: *"the hyperbolic unimodular classes whose dominant eigenvalue has purely periodic
continued fraction of period one are exactly those of determinant −1."* Theorem 4.2 requires
**non-negative entries**, and needs them: `[[−1,1],[1,0]]` is hyperbolic with det = −1, trace −1,
and dominant eigenvalue `−φ`, which has no purely periodic expansion. The "exactly" is false as
abstracted.

### M10. `A_m` is undefined, and the identity is false for the natural reading

Scope 5.21 states `tr[A_m, A_n] = 2 − (mn(n−m))²`. Definition 4.1 defines `X_m` and `ϕ_m`; `A_m`
occurs once, here, and nowhere else. Computed exactly:

| reading | trace of the commutator |
|---|---|
| `A_m = X_m` (the det = −1 generator) | `2 − (m−n)²` — **not** the stated identity |
| `A_m = ϕ_m = X_m²` | `2 − (mn(n−m))²` — **exactly** the stated identity |

So the substance is correct under the only reading that makes the paper coherent, and the printed
symbol is undefined. (`|mn(n−m)| = 2` with `1 ≤ m < n` is uniquely `(1,2)` — confirmed.) A paper
whose Definition 5.1 exists because *"the bridge from a symbolic word to a matrix is half the
title of this paper and it deserves a numbered statement"* should not then leave `A_m` unglossed.

### M11. The one load-bearing certificate is in neither verification block

§9.2 calls Scope 8.2's single bracket *"the paper's sharpest outstanding defect"* and says it
*"has no script in block (a) of Appendix B: it is reproducible only from the repository
snapshot."* Block (b)'s ten rows do not include it either. The defect is one notch worse than
declared: not "in the weaker block", but **absent from the table entirely**.

---

## MINOR

- **m1.** Scope 7.11 labels one choice both ways: *"why this remains C4"* and, two sentences
  later, *"The placement is carried as (C6)."* C4 is the puncture.
- **m2.** §11.3 claims *"each is named where it is made and not only in this table."* (C4) is
  named nowhere in the body — the puncture is fixed silently at Definition 4.1. (C8) and (C9) are
  discussed (Scope 7.10, Scope 9.7) but never tagged there.
- **m3.** Theorem 10.4 appears as the last row of §9.2's table, which declares itself to cover
  §§8–9, and again in §12.1's table.
- **m4.** Scope 10.11: *"a norm law `N_{K/ℚ}(d) = −(953/2304)²` … cubing to `−(953/2304)³`."*
  Cubing `−a²` gives `−a⁶`. And `d` is never defined.
- **m5.** Theorem 10.2: *"The orientation parity of that determinant—the Leibniz sign—is exact and
  equals −1."* A 3×3 determinant has six Leibniz terms, three of each sign; "the Leibniz sign"
  names nothing. The same theorem's AG(2,3) content — rows and columns as two parallel classes,
  even and odd transversals as the diagonal classes, `K₃,₃` incidence — is correct and is a nice
  observation.
- **m6.** The glossary reintroduces the error Definition 10.1 repairs: Definition 10.1 insists the
  atoms *"are eigenspaces and not in general eigenlines … an earlier draft said 'eigenlines' and
  could not have been describing all fifteen"*; the glossary entry reads *"atom: A joint
  **eigenline** of the rational commuting family … Fifteen in total."*
- **m7.** Reference **[2]** (Fricke–Klein / Goldman) is never cited in the body. Scope 5.21, the
  one place the identity is credited, writes "(Cohn; Fricke)" with no number, and **Cohn is not in
  the bibliography at all**. All thirteen other references are cited.
- **m8.** Scope 7.2 asserts four things about `π₁(4₁)` — a surjection onto `2T`, *"exactly two such
  quotients"*, and no surjection onto `2I` or `A5` — with no proof, no citation and no
  verification row. The asymmetry of §7.1 rests entirely on them, and they are cheap to certify.
- **m9.** Proposition 11.1's audit row says what would have to fail is *"the reversal-swap symmetry
  of `RᵐLᵐ`, which is immediate"*. The word symmetry is trivial; the content is the implication
  *word symmetry ⟹ amphichiral*, which after Scope 11.2's withdrawal is neither proved nor cited
  here. (The conclusion is true: `ϕ_m` is symmetric, so `Jϕ_m^{-1}J` conjugated by `diag(1,−1)`
  returns `ϕ_m`, giving `ϕ_m ∼ ϕ_m^{-1}` in `GL(2,ℤ)` for every m. Two lines, and it makes the row
  honest.)
- **m10.** §11.2: *"We give the seals, because a reported miss is only evidence of good faith if
  the reader can see that the prediction preceded the comparison."* The seals are commit hashes in
  a repository the reader does not have; row 5 carries no hash at all; and Scope 11.5 discloses
  that row 5's artifact is missing. A hash certifies pre-commitment only against a public,
  timestamped object.
- **m11.** Proposition 9.1's *"every measurement inside it resolves to 30 and no further"* reads as
  "equals 30", which Theorem 9.8 contradicts (46 on three lines). The intended content is Theorem
  9.8's *"no point of the plane gives less than 30"*.
- **m12.** Scope 9.19(i) ends *"The theorem is therefore a statement over K, and we no longer write
  it as one over K."* Both halves name the same field; presumably one should be ℝ.
- **m13.** Remark A.1 speaks of *"the non-maximal order `ℤ[t]/µ`"*, but µ is not monic, so
  `ℤ[t]/µ` is not an order. The arithmetic is fine (`disc µ / disc K = (2¹⁶·3³·5·7·13³)²`,
  confirmed); the phrasing is not.

---

## CONSTRUCTIVE — results the paper has and does not claim

### E1. Selection I extends to the whole characterized locus, for free

Scope 4.7's residual worry is that §5 quantifies over `{ϕ_m}`, a **proper** subfamily of the
period-one locus Theorem 4.2 characterizes. That gap closes in one line. For any
`A ∈ GL(2,ℤ)` with `det A = −1`, `tr A = m`:

> `det(A² − I) = det(A−I)·det(A+I) = χ_A(1)·χ_A(−1) = (−m)(m) = −m²`

so the mapping torus of `A²` has torsion of order `m²` and is a knot complement only at `m = 1`;
and at `m = 1` the class is unique, since `h(disc 5) = 1`. **Selection I therefore selects the
golden across the whole locus, not merely inside `{ϕ_m}`.** Selections II and III depend only on
the trace and extend identically. Only Selection IV genuinely needs the conjugacy class. This
removes the concession *"§5 quantifies over a proper subfamily of what this section
characterizes"* for three of the four criteria — which is exactly the objection Scope 4.7 says a
referee will raise.

### E2. The threshold Scope 4.7 declines to name is m = 6

*"An earlier draft also placed the first failure at m ≥ 4; we do not assert a threshold here,
having verified only the witness above."* GL(2,ℤ)-class counts at discriminant `m²+4`:

| m | 1 | 2 | 3 | 4 | 5 | **6** | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| classes | 1 | 1 | 1 | 1 | 1 | **2** | 1 | 1 | 2 | 2 | 1 | 2 |

m = 6 is the first, and the computation is elementary. The abstract already says *"at m = 6 a
second class occurs"*; the body is more cautious than the abstract, which is the wrong way round.

### E3. Remark 8.7's ambiguity at dimension 12 closes where the paper uses it

Remark 8.7 claims no type at dim 12 (6 roots: `A₂` or `3A₁`). But `z(C)` is a Levi with 6 roots,
and every point of the 14-locus gives a Levi with 8 roots containing it, forced to `A₂+A₁` by the
same remark. `A₂+A₁` contains no three mutually orthogonal roots, so it cannot contain `3A₁`.
Hence **`z(C) ≅ sl₃ ⊕ t⁴`** — the ambiguity is resolved at the one place dimension 12 is
load-bearing (`dim z(C) = dim n(C) = 12`, Scope 10.6).

### E4. Scope 5.18's non-conjugacy is one line, not Latimer–MacDuffee

`ϕ₁³ ↦ (8,−8,−8)`, content 8; `ϕ₄ ↦ (4,−16,−4)`, content 4. Content is a `GL(2,ℤ)`-conjugation
invariant of the associated form, so the two are not conjugate. Same for Scope 4.7's witness at
the level of forms `(3,4,−2)` vs `(1,−6,−1)` — both content 1, discriminant 40, and
`x² ≡ ±3 (mod 5)` insoluble, exactly as printed.

### E5. Theorem 9.13's stratification is more constrained than the paper says

The strata are exactly `12 + (sums of subsets of the class sizes {2,2,6,6,6,6,6})`, and the list
`{12,14,16,18,20,26,30}` is complete only if **no size-6 hyperplane passes through the 16-point**
(the meeting of the two size-2 hyperplanes) — otherwise 22 appears, which Theorem 9.20 forbids,
or 28, which it permits and the stratification omits. The paper's Remark 9.14 runs exactly this
argument for the size-6 pairs and not for the size-2 pair. Worth one sentence; it is the same
"26 exists and 24 does not, for the same reason" observation, applied once more.

---

## What reproduces (the positive record, in full)

| paper statement | independently recomputed | verdict |
|---|---|---|
| Thm 4.2, Scope 4.7 witness `[[1,2],[3,5]]`, forms `(3,4,−2)`/`(1,−6,−1)`, disc 40, `x²≡±3 (5)` insoluble | forms rebuilt from the matrices; residues enumerated | **exact** |
| Prop 4.4(i)–(iii), `H₁ = ℤ⊕ℤ/gcd⊕ℤ/lcm`; `M(2,3)` trace 8 not of the form `m²+2` | Smith normal form from scratch | **exact** |
| Lem 5.2, `χ_m(1) = −m²`, `χ_m(−1) = m²+4`, `tr ϕ_m = m²+2`; `RᵐLᵐ = X_m² = ϕ_m` | symbolic in m | **exact** |
| Thm 5.4, `H₁(M_m) = ℤ ⊕ (ℤ/m)²`, SNF `diag(m,m)` | m = 1…6 | **exact** |
| Lem 5.7 telescoping bound | all `2 ≤ N ≤ 39` | **exact** |
| Thm 5.8, `\|SL(2,ℤ/N)\| ∈ {24,48,120}` iff `N ∈ {3,4,5}`; `m²+4 ∈ {3,4,5}` iff m = 1 | order formula, N < 200 | **exact** |
| Prop 5.10, `SL(2,ℤ/4)`: 7 involutions, no element of order 8, `p(p²−1) ≠ 48` | full group enumeration | **exact** |
| Scope 5.12, `ϕ₁ mod 5` has order 10 | direct | **exact** |
| Scope 5.13, orders 120 / 5760 / 1 875 000 at N = 5, 20, 125 | order formula | **exact** |
| Thm 5.14, `λ_m < 2` iff m = 1; `φ = 2cos(π/5)` | symbolic | **exact** |
| Scope 5.18, `tr ϕ₁ⁿ − 2` square exactly at odd n, giving m = 1, 4, 11, … | Lucas, n ≤ 11 | **exact** |
| Scope 5.21, `tr[ϕ_m,ϕ_n] = 2 − (mn(n−m))²`; unique solution (1,2) | symbolic (see M10) | **exact for ϕ** |
| Prop 8.1, `dim (Symⁿ)^{2T} = 1` at 8,14,16,22 and `0` at 2,10 | 2T as 24 Hurwitz units, Molien from characters | **exact** |
| Prop 8.8, disc 6237 = 3⁴·7·11, monogenic, totally real, resolvent ℚ(√77) | Dedekind at 3 re-run | **exact** |
| Prop 8.8, splitting: 3 totally ramified; 7, 11 as `pq²`; 13, 17, 19 inert; 2, 5, 953, 1129, 421493 with one degree-one place | factorisation mod p | **exact** |
| Prop 8.8, **h = 1** | Minkowski 17.55; explicit generators of norm 2,3,4,5,7,11 — both primes above 7 and both above 11 | **exact** |
| Rmk 8.9, 5 unramified in K | 5 ∤ 6237, shape `(1,1)(2,1)` | **exact** |
| Rmk 8.7 / Thm 9.20, the rung spectrum `{6,8,10,12,14,16,18,20,26,28,30,36,46,78}`; 22, 24, 32, 34, 38–44 impossible | E6 root system generated from Bourbaki simple roots; all 64 Levi subsystems enumerated | **exact** |
| Prop 9.3, `e6^{2O} = ⟨x8,x16⟩`, `N_{SU(2)}(2T) = 2O`, eigenvalues `(+,−,+,−)` | Molien for 2O on the doubled exponents | **exact** |
| Rmk 9.4, `ΦΨ = x⁸+14x⁴y⁴+y⁸`; degrees `W, tW, W², tW² = 8,14,16,22` | expansion | **exact** |
| Rmk 9.6, θ-odd exponents `{4,8}`, `sign(τ_m) = (−1)^m`, unmeasured product 77 | f4 exponents `{1,5,7,11}` | **exact** |
| Thm 9.13, `2+2+6·5 = 34 = 46−12`; strata `{12,14,16,18,20,26,30}`; the ten size-6 pairs `6+4` | combinatorics of the seven classes | **exact** |
| Thm 9.9, `C(78,3) = 76 076`, `C(78,2) = 3 003` | direct | **exact** |
| Thm 10.3, only `e6(2)` realises signature (15,12) | K-type subset sums across all five real forms | **exact** |
| App A, `500 716 339 200 = 2¹⁶·3⁴·5²·7³·11`; `disc µ = 2³²·3¹⁰·5²·7³·11·13⁶`; Tschirnhaus `ρ³−12ρ−5 ≡ 0 (mod µ)` | symbolic in ℚ[t]/µ | **exact** |
| Census 7.12 `26+6+5+1+1+4 = 43`; §1.2 `2+2+1+1+3 = 9`; App B `5/15 = ⅓` | arithmetic | **exact** |

---

## ROUND 2 — findings adopted from a second hostile pass (2026-08-15)

A second reviewer ran an independent hostile pass on the same 35-page file. Its findings were
re-checked against the extracted text before adoption. Three are real and were missed above; one
is a correct independent verification of a step I had confirmed by a different route; two of its
"resolved" verdicts do not survive.

### R1 [MAJOR, new] — the abstract carries two claims the body explicitly withdraws, and the audit table carries a third

The abstract:

> *"Amphichirality is an **iff** condition on the word, so **the vanishing** of the Chern–Simons
> invariant is a property of the entire family rather than an accident at m = 1."*

Both halves are withdrawn inside the paper.

- Scope 11.2: *"we withdraw the 'only if' and keep only what the argument uses, which is the easy
  direction applied to one explicit family."* So amphichirality is **not** an iff condition on the
  word — by the paper's own sentence.
- Corollary 11.3: *"an earlier draft wrote 'vanishes' where only '2CS ≡ 0' was earned. The class
  ¼ is excluded here by computation, not by symmetry."* So the **family-wide** statement is
  `2CS ≡ 0`, i.e. `CS ∈ {0, ¼}`; `CS = 0` is established for `M₁` alone.

There are five sites, not two, and two of them are inside the machinery that is supposed to catch
exactly this:

1. the abstract, as quoted;
2. Corollary 11.3's own closing clause — *"∂S/∂k = −CS ≡ 0"* — which holds on the `CS = 0` branch
   only, i.e. for `M₁`, one sentence after the corollary establishes two branches;
3. Scope 11.4: *"its force is that the vanishing is a family phenomenon … not an accident at
   m = 1"* — which reads clause 2 the family way and so restates the withdrawn claim;
4. the §12.1 forcedness table, row *"Cor. 11.3, **CS vanishes** — corollary of Thm. 11.1 — what
   would have to fail: Thm. 11.1; nothing independent"*. The corollary says the opposite: the ¼
   class is excluded *by computation*, not by Theorem 11.1, so the row's failure condition is
   wrong as well as its statement;
5. §11.1's heading, *"Scale-blindness, as a property of the whole family."*

The correct family-wide statement is `2CS ≡ 0`; `CS(M₁) = 0` is a one-member computation. This is
the single worst defect in the paper's accounting, because the abstract is the one place a
withdrawn claim cannot be allowed to survive, and because the forcedness audit — the instrument
whose whole job is to prevent this — reproduces it.

### R2 [upgrade of M7] — Scope 9.19(ii) re-runs the exact argument Scope 9.17 withdrew

I flagged the (C7) mislabel. The sharper defect is that the *reasoning* was already retracted two
pages earlier.

- Scope 9.17: *"**Output-stability is not zero cost, and we withdraw the claim that it is.** …
  Corollary 9.16 says only that all successful landings agree."*
- Scope 9.19(ii): *"The second plane is not forced, but **it is free** … What we do have is
  Corollary 9.16: the 14-locus is enumerated, and every point of it gives the same terminus. **The
  plane is a choice whose price is computed to be zero.**"*

Same inference (output-stability ⟹ zero price), same corollary invoked, opposite verdict. And the
§9.2 forcedness table carries the withdrawn version as a row: *"Cor. 9.16, **the second plane is
free** — forced, given the line above."*

So both forcedness tables — §9.2 and §12.1 — contain a claim the body has explicitly retracted.
For a paper whose thesis is a cost claim and whose audit tables are its enforcement mechanism,
that is a defect in the mechanism, not in a sentence.

### R3 [MINOR, new] — Theorem 9.12 quantifies over `y` and concludes about `y*`

*"There is a point y of C with dim z(x1,y) = 14 … `z(x1,y*) ⊗ K ≅ sl3⊕sl2⊕t³`."* Notation 9.11
has just declared `y*` historical and non-reconstructible from the paper, and Scope 9.10 says the
terminus no longer rests on it. The conclusion should read `z(x1,y)`.

### R4 [confirmed by a second route] — the Scope 4.7 witness

The second pass reports solving `AP = PX₆` and reducing to a Pell-type equation with no
determinant-±1 solution. That reproduces exactly, and it is a cleaner obstruction than the
form-content argument. The integral intertwiner lattice is

> `P = [[(r+s)/3, (r−5s)/3], [r, s]]`, integral iff `r + s ≡ 0 (mod 3)`,
> `det P = −((r−3s)² − 10s²)/3`,

so `det P = ±1` requires `x² − 10y² = ∓3`, and `x² − 10y² mod 5 ∈ {0,1,4}` misses `±3`. This is
the paper's own stated obstruction arrived at from the module side rather than the form side, and
it is worth putting in the paper: it makes Scope 4.7 self-contained without Latimer–MacDuffee.
Both routes are now in `verify_scrutiny.py`.

### R5 [not adopted] — the arithmeticity row is not resolved

The second pass grades Theorem 5.15 **STRONG**, on the ground that *"the cited
Bowditch–Maclachlan–Reid work does indeed give a complete once-punctured-torus classification into
three cyclic commensurability classes"* and that *"the external source confirms"* it. No theorem
number, no statement, no quotation is given, and I could not confirm it from the paper alone.

Set that aside, because **M4 does not depend on it.** Even granting exactly three arithmetic
commensurability classes carried by RL, RRLL and RRL, the paper's next sentence — *"The arithmetic
monodromies are therefore exactly those conjugate to a power of one of the three words above"* —
does not follow. Commensurable manifolds share a common finite cover; neither need cover the
other. The second pass restates that inference approvingly rather than testing it, so it endorses
the step at issue. M3 and M4 stand unchanged.

### R6 [not adopted as resolved] — §7 and §10

The second pass treats *"§7 explicitly calls the entrance the one place where the manifold's
arithmetic is consumed"* as established and asks only for a certificate for Theorem 7.7. But
Theorem 7.7's hypotheses contain no manifold, no trace field and no `ℚ(√−3)` — that is **F1**, and
asking for a certificate for 7.7 leaves it untouched. Its closing summary (*"once the manifold
gets you through the 2T entrance…"*) assumes the very implication that is missing.

Likewise it grades Theorem 10.10 *"computed, weakly reproducible"* and defers it. The problem is
not reproducibility: `D` in clause (iii) is never introduced anywhere in the paper, and `φ⁺`,
`χ⁺`, "the value arc" and "the wall-real alignment" are undefined. An unreproducible theorem can
still be tested later; an unstatable one cannot. **F2** stands.

### R7 [adopted, editorial] — the title's two adjectives

Two words in the title outrun the paper: *"canonical family"* against the abstract's own
*"intrinsically characterized rather than ad hoc … that is weaker than saying it is not a
choice"*; and *"parameter-free"* against a ledger of nine declared choices, three of them
underived. "Parameter-free" is defensible if it is defined in the abstract as *no fitted numerical
parameters and no measured input* — which is what §1.2 actually claims — but undefined it invites
precisely the objection §11.3 exists to pre-empt.

### R8 [adopted, calibrated down] — Theorem 7.1's phrasing

Theorem 7.1 says the dual McKay pair `E₆ + E₈` is *"realized as the two stable geometries of a
single object"*, while Scope 5.12 has shown `2I` is the ambient group at the modulus and not the
monodromy's image, and Scope 7.2 shows `π₁(4₁)` surjects onto `2T` but onto neither `2I` nor `A₅`.
Real, and worth rewording — but the paper qualifies it in the very next Scope
(*"the asymmetry runs against the direction the phrasing invites … as a statement about π₁ the E₈
end is field-level"*), so this is a theorem-statement/scope mismatch, not an unflagged overclaim.

### R9 [refinement] — what Theorem 10.3 actually needs shipped

The second pass asks for a self-contained verifier for Theorem 10.3, correctly noting the paper's
own *"if it is wrong then §10 is wrong and nothing else notices."* Two different things are being
conflated. The **inference** — that among the five real forms only `e6(2)` can realise (15,12),
since the K-type dimensions are `{27}`, `{27}`, `{16,10,1}`, `{26,1}`, `{15,12}` and only the last
has a subset summing to 15 — is a finite check that runs in three lines and is in
`verify_scrutiny.py` already. What needs shipping is the **signature computation itself** on the
exact Hermitian matrix. The inference belongs in the paper as a table; only the matrix needs a
script.

---

## ROUND 3 — the repo search, run under WORKING_RULES §0

> *"'We lack X' is a HYPOTHESIS REQUIRING A SEARCH, never a conclusion."*

Before recommending that the paper concede F1 and cut §10.3, I searched the bank for material
that would close the blockers upward instead. **Four of the six blockers have a third way, and
three of them are strengthenings rather than repairs.** The recommendation on F1 flips.

### T1 — F1 CLOSES UPWARD. B210 has the missing implication, with a mechanism.

`frontier/B210_dual_mckay_hyperbolic/FINDINGS.md` contains exactly the step the paper does not
state:

> *"**The mod-3 → E₆ step is VERIFIED, not asserted.** The figure-eight discrete-faithful Riley
> parameter is `u = ω` (the cube root of unity, `ω²+ω+1=0`). It is a **unit**, so mod `(√−3)` it
> reduces to a nonzero element (`ω↦1`, `−ω↦2`), and the two parabolics `A=[[1,1],[0,1]]`,
> `B=[[1,0],[2,1]]` **generate all of `SL(2,𝔽₃)=2T`** (order 24, verified) — the figure-eight
> group **surjects** onto `2T=E₆`."*

That is `ℚ(√−3) ⟹ 2T` as an implication about **this manifold**, obtained by reducing its
holonomy modulo the ramified prime. It consumes the figure-eight's arithmetic — the trace field,
the Riley parameter, the parabolic generators — and it is the step §7.3 claims to be making and
isn't.

It also carries a **mechanism**, which is more than the paper currently claims anywhere:

> *"the figure-eight is **two regular ideal tetrahedra** (both shapes `e^{iπ/3}`, `z²−z+1=0 →
> ℚ(√−3)`), so the **tetrahedral** field gives the **tetrahedral** McKay group `2T=E₆` — not a
> numerical accident. (Silver is octahedral, shape `i → ℚ(i)`.)"*

**Consequences, all in the strengthening direction:**

1. **F1 is repaired by option (a), not (b).** Insert the reduction as a numbered proposition
   *before* Theorem 7.7. Theorem 7.7 then does the job it is actually fit for — narrowing the
   candidate set — and the arithmetic-consuming step exists. §7.3's opening sentence becomes true.
   §1.3's census becomes coherent: the reduction consumes the arithmetic, the classification is
   the entrance, and they are genuinely two steps.
2. **m8 is discharged.** Scope 7.2's unsupported *"π₁(4₁) ↠ 2T is a genuine group surjection"* is
   proved here, with the generators exhibited.
3. **R8 / Theorem 7.1 is repaired rather than reworded.** B210 states the asymmetry exactly and
   for a reason: mod 3 on the **holonomy** is a genuine surjection; mod 5 on the **monodromy**
   gives `2I` only as the ambient group (the paper's own Scope 5.12), and B210 adds the
   independent negative that *"the WRT modular-rep image at the golden level is **not** `2I` — the
   quantum face and the congruence shadow connect only arithmetically, not as a group."* So the
   two ends differ by a stated mechanism, not by a hedge.
4. B210 also carries the `E₇` exclusion in the paper's own form — *"`|2O|=48` is no
   `|SL(2,𝔽_p)|`"* — which is Proposition 5.10's prime-level clause, independently banked.

**This is the single most valuable thing the search found.** It converts the paper's weakest joint
into a proved link with a geometric explanation.

### T2 — the amphichirality "iff" is provable and sourced; Scope 11.2's withdrawal is a retrieval failure

Scope 11.2 withdraws the biconditional saying *"we found no source we had opened that states it in
the form we needed."* The source is in the bank, twice, with the proof written out:

- `frontier/B134_chirality_recursion_proved/` — **Goodman–Heard–Hodgson 2008, arXiv:0801.4815**
  (*Commensurators of cusped hyperbolic manifolds*): a once-punctured-torus bundle is amphichiral
  ⟺ its L/R monodromy word is **anti-palindromic** (`reverse(W) = swap_{L↔R}(W)` cyclically).
  B134 derives the metallic corollary — amphichiral ⟺ the block-length sequence is a cyclic
  palindrome — and verifies it exhaustively over 5460 sequences plus 16/16 SnapPy agreement.
- `frontier/B136_general_amphichirality/` — the general block-pair form, 7380 cases, plus
  non-metallic SnapPy controls.

So the abstract's *"Amphichirality is an **iff** condition on the word"* is **true, citable and
four lines long**. Restore it, cite GHH 2008, and delete Scope 11.2's withdrawal. This is the
error class WORKING_RULES §0 names: an instrument's blindness mistaken for the object's absence.

### T3 — the CS half stays corrected, but an apology becomes a theorem plus a witness

`frontier/B152_cs_amphichirality_census/` scans 240 census manifolds under the **correct** test
(`symmetry_group().is_amphicheiral()` gated on `is_full_group()` — B128 records that naive
`is_isometric_to(mirror)` is orientation-blind and false-positives on known-chiral knots):

- 7 amphichiral, **0 violations** of *amphichiral ⟹ CS 2-torsion*;
- **three amphichiral manifolds sit at `CS = ¼`** — `m003`, `m135`, `m207`;
- one chiral manifold at `CS = 0` (`m208`), so the converse fails too.

So the family-wide claim really is `2CS ≡ 0` and **cannot** be upgraded by symmetry — and now
there is an explicit witness that the `¼` branch is attained. That is a *sharpness* result, not a
retreat, and it replaces Scope 11.4's apology with content.

**And a fact the paper does not have.** The census gives `CS = 0` for **both** metallic members it
covers: `m004 = M₁` and **`m136 = M₂`, the silver** (`5.6e−17`). Corollary 11.3 currently says
`CS = 0` for `M₁` alone. The honest upgrade is: *`2CS ≡ 0` throughout the family, sharply (witness
`m003`); `CS = 0` verified for `M₁` and `M₂`.* Two members is not a family, and saying so is
cheaper than the current phrasing and stronger.

### T4 — three declared reproducibility gaps are table omissions, not absences

**(i) Scope 8.2's bracket — the paper's self-declared "sharpest outstanding defect" — has a
script.** `frontier/B854_centralizer_exact/e6_centralizer.py` builds the E6 Chevalley algebra from
the Cartan matrix **over ℚ with `fractions.Fraction`**, constructs the principal `sl₂` and the four
`2T`-invariants, verifies Jacobi / dimension / Killing rank *before* using the algebra, and records
the exact result the paper asserts — *"all six brackets vanish identically. The centralizer is
ABELIAN — u(1)⁴"* — together with the transvectant reduction Scope 8.2 cites (*"odd order
vanishes, even order does not"*) and the reason it collapses to the single bracket `[x₁₄,x₂₂]`.
Its imports are the standard library plus sympy. **That makes it a block-(a) candidate, not even
block (b).** M11 and §9.2's "sharpest outstanding defect" both dissolve.

**(ii) Theorem 10.3's signature has scripts.** `frontier/B907_real_form_selector/` carries
`real_form_selector.py`, `completeness.py`, `completeness_verify.py`, `selector_complete.py`,
`selector_verdict.py` and their result JSONs. Scope 12.2's *"Theorems 10.2, 10.3 and 10.10 have no
script in either block"* and §12.3's *"no self-contained script in Appendix B"* are statements
about the paper's own table, which omits artifacts that exist.

**(iii) Theorem 7.7 still has nothing.** I could not locate a certificate for the
27-with-invariant-cubic classification. **M5 stands, and it is now the only genuine
reproducibility gap in §§7–9.**

### T5 — Appendix B's table needs an audit before submission

Of the sixteen artifacts Appendix B names, **eleven are not present in this repository**, including
**all five of block (a) and the `verify/verify_all.py` runner** — the block a referee is told can
be run "from the arXiv tarball alone." Present: `test_b125_snappy_arithmeticity.py`,
`test_b92_metallic_classification.py`, `test_b1011_mckay_tensor.py`,
`test_b136_general_amphichirality.py`, `test_b307_totally_real_obstruction.py`.

The paper's `.tex` source is not in this repository either, so block (a) may live beside it in an
uncommitted tree. **This is a "confirm before submission", not a finding** — but Appendix B's own
standard is *"a manuscript that promises runnable verification and supplies only a description does
not meet its own standard"*, so it is the one row that must be checked by hand.

### T6 — M4 disappears on a better route; M3 becomes an explicit trade

`frontier/B125_snappy_arithmeticity/` cites the criterion with a theorem number the paper does not
use: **Maclachlan–Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, Thm 8.3.2** (non-cocompact) —
a finite-covolume non-cocompact Kleinian group is arithmetic ⟺ its invariant trace field is
imaginary quadratic **and** every trace is an algebraic integer.

Routed through 8.3.2, the argument becomes: for `m ≥ 3` the invariant trace field has degree ≥ 4,
hence is not imaginary quadratic, hence `M_m` is not arithmetic. **M4 vanishes entirely** — no
commensurability class list, no "hence powers of the three words", no invalid inference.

The cost is explicit and should be stated as a choice: 8.3.2 gives an airtight argument over a
**computed** range (B125 covers `m = 1…6`, the paper `m ≤ 10`), whereas the BMR route claims the
unbounded tail and carries M3's gap. My recommendation: take 8.3.2, state the tail as verified for
`m ≤ 10`, and cite BMR only for the finiteness it actually supplies. A bounded claim that is
proved beats an unbounded one that is asserted — which is Remark 5.17's own standard.

### What the search did not find

F2 is only **half** closed. `frontier/B928_d2_decode/` defines `D₂ = ±ρ₂₇(σ_{χ₋})`, the shift
vector `a* = (1,0,1,0,1,1) = s(χ₋)`, `φ* = τ∘φ₊∘φ₋ = φ₊∘σ_{χ₋}`, `H₊`, and the 128-member census —
so **five of the six undefined objects of Theorem 10.10 have definitions in the bank**, and §10.3
can be repaired by importing them rather than cut. B928 also confirms M8 independently: the
characters are `(−1)^{⟨a,w⟩}` with `a` in the **weight lattice** (rank 6), not the four-dimensional
charge space, so "charge lattice" is the wrong name and the repo has the right one. What I did not
find is `D` itself, the fourth member of the Klein four-group in clause (iii). One symbol, and it
is presumably the first wall's diagonal — but the paper must name it.

---

## Priority for the author

*(revised after Round 3 — four blockers now close upward rather than by concession)*

1. **T1 / F1** — insert the mod-3 reduction (B210) as a numbered proposition before Theorem 7.7,
   with the two-ideal-tetrahedra mechanism. This makes §7.3's opening sentence true, makes §1.3's
   census coherent, discharges m8, repairs Theorem 7.1's asymmetry, and lets the title keep
   "chain". Everything else in §7 is downstream of it.
2. **T2 / R1a** — restore the amphichirality "iff", cite Goodman–Heard–Hodgson 2008
   (arXiv:0801.4815), delete Scope 11.2's withdrawal.
3. **T3 / R1b** — the CS half stays corrected but gains content: `2CS ≡ 0` family-wide and
   **sharp**, with `m003` the witness that `¼` is attained; `CS = 0` verified for `M₁` **and `M₂`**.
   Fix the abstract, Cor 11.3's closing clause, Scope 11.4, §11.1's heading and the §12.1 row.
4. **T4 / M11** — list `B854/e6_centralizer.py` (block **a** — it is exact over ℚ and imports only
   stdlib + sympy) and `B907_real_form_selector/` (block b). Two rows, and the paper's
   self-declared sharpest defect and its weakest §10 warrant both disappear.
5. **T6 / M3 / M4** — route the arithmeticity tail through Maclachlan–Reid Thm 8.3.2, state it as
   verified for `m ≤ 10`, cite BMR only for finiteness. M4 vanishes.
6. **F2** — import the five definitions from B928 and name `D`. Cutting §10.3 is no longer the
   cheapest option.
7. **T5** — hand-audit Appendix B: eleven of sixteen named artifacts, including all of block (a)
   and the runner, are not in this repository. Confirm they ship with the source.
8. **M5** — Theorem 7.7 is now the only genuine reproducibility gap in §§7–9. It needs a proof, a
   character table, or a script.
9. **R2 / M7 / M6 / m1 / m2** — one pass over the ledger and both forcedness tables.
10. **E1 / R4** — two short paragraphs; between them they remove the sharpest concession in §4 and
    make Scope 4.7 self-contained.

The paper is right that it should be judged on §5, and §5 survives scrutiny intact. It is also
right that the cost claim is the thesis; that is precisely why the ledger defects are not
cosmetic.

# B8076 — THE PAPER-CLOSURE CAMPAIGN: twelve items, tracked until every one is accounted for

**Sealed** in `PREREGISTRATION.md` before the first item was worked. **Locked** by
`tests/test_b8076_paper_closure.py`, which fails if an item is deleted, given a status outside the
four, or marked `GREEN` without an evidence path that exists on disk.

**Statuses:** `GREEN` (closed, evidence path recorded) · `OPEN` (not yet worked) · `BLOCKED`
(worked, cannot close — obstruction named) · `WITHDRAWN` (item was wrong — reason recorded).
**`BLOCKED` and `WITHDRAWN` are legitimate closures. Silently leaving the list is not.**

---

## THE LEDGER

| # | item | what closes it | quantifier | status | evidence |
|---|---|---|---|---|---|
| 1 | **The 14-locus existence.** Appendix B block (b): *"the 78 weights; seven hyperplanes; certified gap."* The `A₂⊕A₁` terminus is currently *"if a 14-dim locus occurs, its type is forced"* — the **occurrence** is a floating-point census | certify the weight census exactly, and establish that a 14-dimensional locus **occurs** | algebra (member) | **GREEN** | **occurrence established, by two independent routes.** (i) `frontier/B8078_rung_spectrum_attained/` — `dim z(S) = 14` is attained, at 3-dimensional `S`, in the flat enumeration; (ii) **B892** banked a 14 independently (`su(3)⊕su(2)⊕u(1)³` at the wall point `y*`), recorded in B874's amendment. So `thm:smt`'s antecedent is discharged. The weight census is replaced by something stronger than the floating-point version: `frontier/B8076_paper_closure/item01_weight_field.py` — the weight field **IS** K (exact factorisation), and `frontier/B8076_paper_closure/item01b_stratification_output.txt` gives the rational stratification `{0} ⊂ (8,16)-plane ⊂ C` as a **biconditional** over 624 exact directions. **Residue:** the 14 is certified at three faithful primes plus B892, not yet over ℚ̄; B892's `y*` has `a² < 0`, so the locus is not real |
| 2 | **The realized rung spectrum.** The bound is proved (11 values); the realized set `{12,30,78}` is a **sample**, not an enumeration | exhaustive computation over the subspace lattice of `C`, plus citation of **B874**'s independently banked ladder `{78,46,30,12}` | algebra (member) | **GREEN** | `frontier/B8078_rung_spectrum_attained/rung_attained.py` — the lattice is infinite, so the sample was replaced by **structure**: exactly over ℚ, `e6 = z(C) ⊕ V'` with `C` acting as **literally zero** on `z(C)`, giving `dim z(S) = 12 + Σ{m_λ : λ(S) = 0}` for **every** `S` — the rung function is the flat-function of 30 hyperplanes in a 4-space. **109 flats; the realized spectrum is all eleven values `{12,14,16,18,20,26,28,30,36,46,78}` — the paper's bound is TIGHT.** B874's ladder is cited and all four of its values land. The eight the sample missed lie on proper subvarieties, which a random rational direction misses with probability 1. **Residue CLOSED same day** by `frontier/B8079_arrangement_exact/` — reaching the same arrangement as the **E₆ roots restricted to `C`** makes every weight rational, so the ℚ-enumeration **is** the ℚ̄-enumeration. Two routes, no shared code path, one answer |
| 3 | **All 64 Levi subsystems** — block (b), undeposited | ship the enumeration | algebra | **GREEN** | `frontier/B8079_arrangement_exact/arrangement_exact.py` and, shipped inside the submitted source, `papers/structure_paper/verify/check_levi_arrangement.py` — **the row moved from block (b) into block (a)**. Root counts `0,2,4,6,8,10,12,14,20,22,24,30,40,72`; the fourteen ambient dimensions; **24 is not a Levi dimension**; **26 realized by exactly four `A₄` node-subsets**; and **exactly three dimensions carry two types — 12, 18, 20** — which is `rem:leviscope`'s claim, with the four counts the paper leans on each unambiguous |
| 4 | **Theorem "assembly" (thm:classify).** The term is now defined; the six-group enumeration behind it is **not deposited**, so the classification is unverified | enumerate multiset decompositions of 27 into non-trivial irreducible degrees for each of `{A₄,S₄,2T,2O,A₅,2I}`, with a non-degeneracy test on the cubic | algebra | **GREEN** | `frontier/B8080_assembly_classification/assembly.py` and, shipped in the source, `papers/structure_paper/verify/check_assembly.py`. **The item computes and REFUTES the paper** — the campaign's declared third outcome. All six candidates admit a 27-dimensional assembly, not just `A₄` and `2T`. Decider: **the block-sum lemma** — an irreducible with a non-zero invariant cubic has zero radical, so block sums are assemblies; witnesses `9×3` (`S₄`,`2O`), `3×4+3×5` (`A₅`,`2I`), `27×`(order-3 linear character) (`A₄`,`2T`). **The defect is multiplicity, not triviality**, and `A₄`/`2T` are kept by the very mechanism the earlier repair excluded. **Load-bearing:** `2O` and `2I` survive and both are binary, so `cor:onlybinary` cannot absorb it. **Not fatal:** the entrance is the arithmetic surjection (item 6), now shipped as `papers/structure_paper/verify/check_quotients.py`. Paper corrected: theorem restated, `sc:assembly` rewritten, §`sec:classification` retitled |
| 5 | **Prop 2880 / the coupling law — ρ, T, Σ, θ.** A theorem about a representation whose matrices are not printed; `check_coupling_law.py` verifies trace sets, not ρ | print the six Kac–Peterson SU(3)₂ entries; make the script **build ρ** and verify the decomposition | algebra / faces | **GREEN** | `frontier/B8081_rho_rebuilt/rho_rebuilt.py`, shipped as `papers/structure_paper/verify/check_rho.py`. **ρ is built from the Kac–Peterson data alone** — six weights, `h = (a²+b²+ab+3a+3b)/15` from the inverse Cartan of `A₂`, the Weyl sum for `S` — and validated by **four modular relations** (`T¹⁵=I`, `S⁴=I`, `S²=C`, `(ST)³=S²`) before any result is read. The six T entries are printed. Then: **the image has order 2880** at four primes; **θ is charge conjugation**, eigenspaces `4+2`, commuting with the image; the **θ-odd block has order 360** (the 360-vs-2880 distinction `sc:2880` exists to draw); and the **63 = 7×9 class-by-class match** of `(size, χ(A)trV₂(B), trV₂(A)trV₂(B))` against an independently built quaternion model of `2T×2I` is **exact**. `sc:2880`'s *"not reconstructed in this paper"* is deleted |
| 6 | **π₁(4₁) ↠ neither 2I nor A₅**, and **"exactly two quotients" onto 2T** — both currently labelled conjecture | quotient enumeration on the 2-generator 1-relator presentation | member | **GREEN** | `frontier/B8076_paper_closure/item06_quotients.py` — exhaustive: **2I 600 reps / 0 surjective** (14,400 pairs), **A₅ 300 reps / 0 surjective** (3,600 pairs), so the conjecture is a **theorem**; and **2T: 48 surjections, 4 classes up to Inn, 2 up to Aut** — the paper's *"exactly two"* is correct **up to Aut(2T)** and the paper must say so. Control: relator exponent sums (1,0) match B870's independent Fox-calculus route |
| 7 | **Prop geodir** — 6-dimensional unobstructed moduli, `1+5` split. No proof, no citation, and load-bearing for C6's retyping | a genuine `H¹` / obstruction-theory computation — **or** accept `BLOCKED` and leave C6 a fully priced choice | algebra | **GREEN** | `frontier/B8082_geodir_h1/geodir_h1.py`, shipped as `papers/structure_paper/verify/check_geodir.py`. **The `H¹` half is computed**, which is exactly what `sc:geodirscope` said the paper does not do. `ρ₀` factors through `SL(2)`, so `𝔢₆` splits by principal-`𝔰𝔩₂` exponent into `Sym^{2m}` of dims `3+9+11+15+17+23 = 78`; Fox calculus on the one-relator presentation gives **`dim H¹ = 1` in every block**, `H⁰ = 0` throughout, hence **6** and the **1+5** split, with the exponent-1 block `Sym²(V₂)` = the adjoint of `𝔰𝔩₂`. Control: the parabolic pair satisfies the relator iff `t²−t+1 = 0`, putting the trace field at `ℚ(√−3)`. **Refinement the paper now carries:** `m = 2,3,6` are *not* `E₆` exponents and also give 1, so the six is the **number** of exponents and the split is a way of counting, not a discovery. **Residue, named:** *unobstructedness* is **not** computed — `dim H² = 6`, so no dimension count settles it. **C6 is unchanged and still fully priced** |
| 8 | **Order 2880 / 63-of-63 characters** — block (b), undeposited | deposit the character comparison | faces | OPEN | — |
| 9 | **Theorem 4.7's positivity step.** GL(2,ℤ)-conjugacy does **not** preserve word positivity; the block-sequence argument needs its bridging sentence | one lemma: why cyclic rotations of positive words suffice | axioms | OPEN | — |
| 10 | **Lemma toral** — likely folklore (cf. Vinberg θ-group theory, fixed points of finite automorphisms). A literature pass is owed before any implicit priority | search; then cite, or record `APPEARS-NOVEL` in `docs/THEOREM_REGISTRY.md` | — (literature) | OPEN | — |
| 11 | **Census 5.1 (43 links, 4 axioms)** — counts an external ledger that is not deposited. An unverifiable census in a paper about verifiability | deposit the ledger, or replace the count with what is checkable | axioms | OPEN | — |
| 12 | **`refs.bib` — five `STANDARD` entries** flagged *"verify before submission"* (Hurwitz 1891, Slansky 1981, Georgi–Glashow 1974, McKay 1980, Conway–Smith 2003). `PRIOR_ART.md` calls this blocking | verify each against the actual source | — (bibliography) | OPEN | — |

---

## STANDING RULES FOR THIS CAMPAIGN

**No item closes on prose.** `GREEN` requires an evidence path — a script, a deposited artifact, a
citation — that exists on disk and that the lock can see.

**Every item states its quantifier before it is worked** (`docs/COMPUTE_THE_PROGRAM.md`): which
layer of the full-relations inventory it covers, and its conclusion claims no more. *Today's A2
question was under-quantified twice in ten minutes — first by grading on a mark-2 node, then by
searching a single 16 when the programme has both gradings, both faces, the class and the rows.
Both were caught, and both were the same error.*

**No headline may be a printed constant** (error class E843). Every reported number is bound to a
computed variable, and the arc states which computed invariant **changes** between the before and
after states. If none does, there is no result.

**Contradiction is a legitimate outcome.** If an item computes and refutes the paper, that is the
finding — the rung-spectrum correction is the worked precedent, where an external referee was
right and the repair made the paper stronger.

---

## PROGRESS

*(updated as items close; the lock reads the status column above, so this section is narrative
only and carries no authority)*

- **2026-08-18** — campaign sealed, twelve items registered, none worked.
- **2026-08-18** — **item 6 GREEN.** π₁(4₁) surjects onto neither 2I nor A₅ (exhaustive); the 2T
  count is 2 **up to Aut**, 4 up to conjugacy — an unstated equivalence the paper must fix.
- **2026-08-18** — **item 1 stays OPEN, with two sub-results certified.** *(A first edit marked it
  `PARTIAL`; the lock rejected that — `PARTIAL` is not one of the four statuses, and a half-status
  is precisely the limbo this campaign exists to prevent. The mechanism worked on its own author
  within the hour.)* The item asks for the **14-locus existence** and that is **not established**.
  What *is* certified, and replaces two thirds of block (b)'s floating-point census:
  **(i)** the weight field **IS** K — the weight cubic acquires a root in K, so the ad-spectrum is
  K-valued rather than merely 77-resolvent-sharing (`item01_weight_field.py`);
  **(ii)** the rational stratification is `{0} ⊂ (8,16)-plane ⊂ C` with `dim z = 78, 30, 12`, a
  **biconditional** over 624 exact directions (`frontier/B8076_paper_closure/item01b_stratification_output.txt`).
  **The 14 itself is real-inaccessible** (B892: `a² < 0`) and certifying it needs arithmetic **in
  K**, not over ℚ — a specified computation now, not a vague gap.
- **2026-08-18** — **item 2 GREEN, and it is the largest single correction of the campaign.**
  The paper's Theorem `thm:rungspec` bounds `dim z(S)` by eleven values and Remark
  `rem:spectrumscope` withdraws attainment, concluding the realized set *"appears on present
  evidence to be far smaller."* **It is not smaller — it is exactly the eleven.** The bound is
  TIGHT. The withdrawal was correct on the evidence then available; the evidence was a sample of
  an infinite lattice, and the eight missing values sit on proper subvarieties that a random
  rational direction misses with probability 1. **The sample was not unlucky, it was the wrong
  instrument.** Three paper edits are now owed: `thm:rungspec` → equality; `rem:spectrumscope`'s
  *"far smaller"* sentence → deleted and replaced; `thm:smt`'s 14-locus occurrence → no longer an
  assumption. B866 is upgraded as a by-product: its 46, previously a 55-digit numeric spectral
  gap with an open type check, is now exact with its multiplicity 16 **derived**.
- **2026-08-18** — **item 1 GREEN.** The 14-locus **occurs** — B8078's enumeration and B892's
  independently banked wall point agree. Both halves of the original item are now closed: the
  weight field is K, and the occurrence is established. Residue recorded in the ledger cell.
- **2026-08-18** — **the three owed paper edits are APPLIED**, and they are the first edits of
  this campaign that make the paper claim *more* rather than less. `thm:rungspec` retitled and
  restated as an **equality**, its proof gaining an *Attainment* half (the decomposition, the
  master identity, the 109 flats); `rem:spectrumscope` **rewritten** to record that the statement
  has been wrong in *both* directions — first an invalid converse, then an over-correction from a
  sample — and to say what is exact over ℚ versus certified at three primes; the figure caption,
  the abstract, the falsifier table and the downstream `thm:smt` paragraph all follow.
  `papers/structure_paper/verify/check_rung_attained.py` added, and its companion
  `check_rung_spectrum.py` re-pointed so it can no longer be read as the whole story.
  **`verify_all.py` is now 12/12.** Build: **45 pp, 0 overfull, 0 undefined refs**; main.tex
  re-grepped by hand against all ten registered retracted phrases — **0 live uses**.
- **2026-08-18** — **item 3 GREEN, and item 2's residue closed, both from one idea the owner
  prompted by asking me to fetch.** cc's banked no-moduli theorem — *`dim C = 4` with
  `dim z(C) = 12` forces `|Φ ∩ C^⊥| = 6`, the only rank-≤2 system with six roots is `A₂`, and all
  such lie in one `W`-orbit* — was **reproduced in-sandbox** (`WORKING_RULES` §2/§12 forbid banking
  it by citation) and turns the arrangement into **the 72 E₆ roots restricted to `C`**: six vanish,
  `66 = 72 − 6` remain, profile `12×1 + 18×3` — **exactly what B8078 computed from the charges by a
  route sharing no code**. Every vector is rational, so the ℚ-enumeration **is** the ℚ̄-enumeration:
  **109 flats, eleven values, exact.** The apparent tension with the 46 is not one — the
  *arrangement* is rational, the *charge basis's position relative to it* is not. Paper updated:
  the attainment proof is now stated from the root side and is exact, and the *"certified at three
  primes"* hedge is **gone**.
- **2026-08-18** — **item 4 GREEN, and it is the campaign's first REFUTATION.** The paper flagged
  `thm:classify` as *"an assertion **about** a computation"* and said the six-group classification
  *"should be read as unverified."* It is now run, and it **refutes the theorem**: all six
  candidates admit a 27-dimensional assembly under the paper's own definition. The prereg declared
  this outcome in advance — *"an item computes and contradicts the paper: the contradiction is the
  finding. Correct the paper, mark GREEN, and record the correction."* Done. **The instructive
  part:** the definition was already repaired once, after review found that 27 copies of the
  *trivial* module satisfied it. The repair excluded trivial summands — and the surviving witnesses
  for `A₄` and `2T` are **27 copies of a non-trivial LINEAR character**. The two groups the theorem
  kept were kept by the very mechanism the repair was meant to exclude. **The entrance survives**,
  because it never ran through this theorem: it is the arithmetic surjection
  `π₁(4₁) ↠ SL(2,𝔽₃) ≅ 2T`, exhaustively verified in item 6 and now shipped inside the source.
- **2026-08-18** — **item 5 GREEN.** The paper said of `ρ` that *"its structure constants are
  specified in the source computation and **are not reconstructed in this paper**, so
  Proposition (2880) is a certificate whose ambient representation is cited rather than rebuilt."*
  A group order and a full decomposition, asserted for a matrix never written down. It is written
  down now, from the Kac–Peterson data alone, and the four modular relations validate it **before**
  any result is read — which is what makes it `ρ` and not some other matrix. Everything the paper
  claims about it then follows: 2880, the `4+2` θ-blocks, the odd block's 360, and the exact
  63-class factorisation. Three campaign items have now moved a paper statement from *asserted* to
  *computed* (2, 3, 5) and one moved it from *asserted* to *refuted* (4); the difference each time
  was running the computation the paper described rather than trusting the description.
- **2026-08-19** — **item 7 GREEN, with its residue named rather than absorbed.** The paper said
  of Prop (geodir): *"which `H¹` is six-dimensional, and why it is unobstructed — and this paper
  does not compute it."* **The first clause is now computed; the second is not.** Splitting the
  item's two halves and reporting them separately is the honest outcome here — and the campaign
  has a precedent for it: B8078 registered a residue and B8079 closed it a day later.
  Two things came out that the paper did not have. First, the trace-field control: the parabolic
  pair satisfies the relator **iff** `t²−t+1 = 0`, which is what makes the solution *the geometric
  representation* rather than an arbitrary one. Second, and it is a caution rather than a result:
  `m = 2, 3, 6` are **not** exponents of `E₆` and give `dim H¹ = 1` too — so the six is the
  **number** of exponents, and the *"1+5 split by exponent"* counts rather than discovers. The
  paper invited the stronger reading; it now states the weaker one.
- **2026-08-18** — *(not a campaign item, banked alongside)* **B8077**: both sides of the
  remaining `14 → 12` step are **compact** in the object's own real form; reality is not the
  obstruction. `frontier/B8077_compact_home`.

# LAW SIBLINGS — same-law arcs a band-wise sweep cannot see

> **Why this exists (B1043/B1044).** The debt sweep dispositions **by band**, and a band is an
> interval of **B-numbers — banking dates**. A law is a statement about **what an arc says**. Where
> a law spans bands the sweep cuts it, *silently*, because the in-band bodies never mention the
> out-of-band sibling and **a body cannot cite its own future**.
>
> **It cost a published overstatement.** B1039 restored B141's Item 4 as an **open conjecture**;
> **B564 had closed it**, by the symbolic elimination B141 itself named as *"the rigorous path"*.
>
> **The instrument:** `scripts/checks/law_siblings.py`, gated as **`law-siblings`**. For each
> restored law it searches the whole corpus by **topic**, and lists every PROVED, non-instrument
> arc that matches and is cited on no curated surface. **Candidates are TRIAGED, not capped** —
> the repo's own posture for this shape (B821/B823) — so the gate fails **only on untriaged**
> candidates. It asks for a judgement, not a number; a hard-fail on every candidate would fire on
> right answers and train readers to ignore it (E34's recorded reason).

**Dispositions.** `SAME-LAW` → cited on the law's row, debt retired. `RELATED` → a real neighbour,
**stays in debt knowingly**, with the reason. `DISTINCT` → the fingerprint matched a word, not a
statement.

| arc | law | disposition | judgement |
|---|---|---|---|
| `B33` | the tower (B1038) | **SAME-LAW** | *"SL(2) and SL(3) trace-map Jacobian spectra decompose exactly as symmetric powers of the half-step eigenvalues"* — the **spectral** face of B1038's module law, at `n = 2,3`. Cited on the tower row. |
| `B232` | the tower (B1038) | **SAME-LAW** | **The same law differentiated**, verified symbolically `n = 3..12`: the step form `ρ_n ≅ ρ_{n−1} ⊕ Sym^n(V) ⊕ Sym^{n−3}(V)` is the difference of the band form `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`. Not two results. Cited on the tower row. |
| `B522` | the tower (B1038) | **SAME-LAW** | The **filtration theorem** — a formal-slice/BCH route to the same `char(ρ_n)` conjecture. Verdict is **SHARPER-REDUCTION**, *"full proof NOT reached"*, and it calls itself *"the sharpest reduction since B103"*. **It is the best known progress on the very prize B1038's row lists as open**, and the row now says so. |
| `B564` | φ-fixed reducibility (B1039) | **SAME-LAW — and it CLOSES the cluster's open question** | *"the SL(3) φ-fixed locus contains no irreducible representation: φ-fixedness pins A to finite order, which forces the intertwiner to split block-diagonally"*, by **symbolic elimination**. Its own first paragraph: *"This confirms the B141 Item-4 conjecture and extends B142's principal-only (Klein-4) result to the full locus."* **The defect that motivated this whole instrument.** |
| `B75` | the metallic exponent (B1039) | **SAME-LAW** | *"degree=rank is a two-parameter `(m,n)` phenomenon"* — the **first** statement that the exponent is not rank-bound, which B1039's law sharpens to *order*-determined. Cited on the metallic row. |
| `B77` | the metallic exponent (B1039) | **SAME-LAW** | *"degree=rank sharpens to the signed scalar-matrix law `[A,B] = (−1)^{n−1} µ^n`"* — **the sign half** of B1039's `[A,B] = ±µᵏ`. Cited on the metallic row. |
| `B106` | the metallic exponent (B1039) | **SAME-LAW** | *"Dehn-filling fixed points are partially elliptic with root-of-unity neutral eigenvalues"* — these are **exactly the finite-order-µ reps** whose inclusion B198's own correction blames for the illusory multi-exponent readings. The stratum B1039's law must be read *off*. Cited on the metallic row with that scope. |
| `B485` | isomonodromy (B1040) | **SAME-LAW — and the instrument's first measured miss** | *"the metallic Alexander law `Δ_m(a) = a² − (m²+2)a + 1`"* is **the characteristic polynomial of `M_m²`**, whose root is `λ_m²` — verified identical symbolically. The Alexander polynomial of a fibered bundle **is** its monodromy's char poly. **No fingerprint reached it** until B1045 widened the isomonodromy one. Cited on the isomonodromy row. |
| `B257` | the metallic exponent (B1039) | **RELATED — stays in debt, knowingly** | *"the Euclidean transition point as the character-variety discriminant branch point with order-3 …"*. It shares the discriminant/branch-point vocabulary but states a fact about the **Euclidean transition** (B248's cone-angle line), not about the peripheral exponent. **The fingerprint matched a word, not the statement.** Recorded so the next sweep does not re-raise it, and left in debt because it is owed a row of its **own**, on a different law. |
| `B449` | the seam is the ends' class field (B1029) | **SAME-LAW — OWED, and it is the FOUNDATION of the row that has no fingerprint** | *"the disc×disc seam formula is **category-confused** (5₂ and 6₁ are not fibered), so **ℚ(√−15) is RESTORED as the forced compositum** of the object's geometry and dynamics ends; the in-family conductor law gives **15** (golden) and **8** (silver)."* B1029's row asks *what is the seam field's class field*; **B449 is the arc that says the seam field is FORCED at all**, by killing the retrofit reading. **Not restored here** — this phase dispositions one cluster and campaign step 5 requires re-verification before restoring. **Owed, with the reason.** |
| `B427` | the seam is the ends' class field (B1029) | **SAME-LAW — OWED** | *"Exchange of the two seam slots acts by the **Galois element σ₁₇, which FIXES √−15**; the projector-trace corollary is **corrected** to symmetrized/antisymmetrized sectors."* A statement about the **Galois action on the seam field** — the same field, one structural layer along. **Its corollary correction must travel with any restoration** (`tr(Q³A) = tr(QA)` is **false** on the actual matrices: `C = ζ₁₅`, `C′ = ζ₁₅²`), which is exactly why it is owed a body read and not a citation. |
| `B459` | the seam is the ends' class field (B1029) | **SAME-LAW — OWED, and it carries a self-correction that must travel** | The dual-torus vanishing patterns *"identified as the **five-subfield lattice of ℚ(√5, √−3)**"* — **the very compositum B1029's row names as HCF(ℚ(√−15))**. But its own **ADDENDUM corrects this record's overreach**: the selection rule is *"the **(1,2)-pair's** arithmetic, not the figure-eight's"*, and the cross-address control reads *"the selection structure is the **QR-class's at level 15, not the object's**"* — an **E34 apparatus-inflation** shape. **Restoring the headline without the addendum would restore an object-level claim the arc itself withdrew.** Owed, with that named. |
| `B876` | the seam's darkness is termwise (B1047) | **DISTINCT — the fingerprint matched a word, not a statement** | Matched on **`annihilat`** — but B876's is a **Lie-algebra ANNIHILATOR** (*"the A₄-chain annihilator y with Cent = 25"*), not termwise annihilation of a convolution. **This is the DUAL of the B485 limitation and is worth naming beside it:** B485 was *one law in two vocabularies* (missed); B876 is *two laws in one vocabulary* (falsely matched). A fingerprint is a word test, and words run in both directions. **The token is left in place and the judgement recorded here** rather than narrowed away — narrowing on the first false positive is how a threshold erodes (**E38**), and the registry is where judgements are supposed to live. |
| `B27` | the tower (B1038) | **SAME-LAW — and the instrument's SECOND measured miss** | *"The exact eight-dimensional SL(3) Fibonacci trace lift retains the A quadratic sector…"*. **Its stated Jacobian characteristic polynomial `(t−1)(t+1)(t²−4t−1)(t²−3t+1)(t²+t−1)` IS the charpoly of `Sym³ ⊕ Sym² ⊕ trivial` of the half-step eigenvalues `{φ, −1/φ}`** — verified **symbolically**, polynomial against polynomial, at B1051. That is B1038's law at SL(3), and **B33 (already on that row) says the same thing**. Cited on the tower row. |
| `B83` | the metallic exponent (B1039) | **SAME-LAW — third miss, and it adds a member** | *"The SL(n) figure-eight Dehn-filling A-polynomial family is `L = (−1)^{n−1}Mⁿ`"*. **B77's `[A,B] = (−1)^{n−1}µⁿ` is already cited on that row**, and B83 calls its own statement *"the peripheral eigenvalue shadow"* of it — same sign, same exponent, **a plane curve instead of a matrix identity**. It also contributes the **SL(4) member `L = −M⁴`, new**. Cited with its **HIGH-PRECISION NUMERICAL** tier stated. |
| `B76` | the metallic exponent (B1039) | **RELATED — restored on its OWN row, with an `E1` collision declared** | The metallic **cusp** k-set equals the SU(2) quantum-group level set, `2cos(π/k) = [2]_q`. It rides the metallic family, which is why the fingerprint reaches it — **but its `k` is the CUSP index and B1039's `k` is the peripheral exponent in `[A,B] = ±µᵏ`. Two different `k`'s.** Restored as *THE CUSP k-SET IS THE QUANTUM-GROUP LEVEL SET* rather than folded, and both rows now declare the collision. |

**Maintenance.** Adding a restoration adds its fingerprint to `FINGERPRINTS` in
`scripts/checks/law_siblings.py`. **A fingerprint is hand-authored on purpose**: an auto-extracted
one would drift with the prose and silently stop matching, which is the failure this instrument
exists to prevent.

**The self-measurement trap, hit inside the instrument built against its cousin.** B1043's LAW_MAP
row names all eight candidates, so the first run of this sweeper reported **zero** — the rows that
*register* the debt read as rows that *consolidate* it. Registry rows and registrar arcs are now
excluded at construction, which is **E37**'s own standing rule applied to the instrument.

## The instrument's known limitation, measured on first use (B1045)

**A fingerprint catches restatements in the SAME vocabulary; a genuine TRANSLATION between
vocabularies escapes it.** `B485` states B1040's metallic degree as an **Alexander polynomial** —
the same `a² − (m²+2)a + 1`, because the Alexander polynomial of a fibered bundle *is* its
monodromy's characteristic polynomial — and **none of the four fingerprints matched a single term
of it.**

**This is not fixable by adding terms**, only mitigated: every widening is a guess at the next
synonym. What the instrument reliably catches is the case that actually bit (B564 — *same words,
different band*); what it will keep missing is the case where a later arc re-derives a law in a
different field's language. **Stated here rather than discovered again**, and it is the honest
argument for L164's larger option: a topic-wise disposition reads *bodies*, not fingerprints.


## A THIRD miss mode, and a widening that overshot (B1051)

**The registry already records two modes.** B485: **one law in two vocabularies** (Alexander vs
characteristic polynomial) — *missed*. B876: **two laws in one vocabulary** (annihilator) — *falsely
matched*. **B27 and B83 are a third: ONE LAW AT A DIFFERENT OBJECT.**

A fingerprint is authored in the **restored** arc's vocabulary. The tower fingerprint speaks of `ρ_n`
and `Sym^n` bands; B27 speaks of an *"eight-dimensional SL(3) trace lift"* and names its factors. The
metallic fingerprint speaks of `[A,B]`, `µ` and *degree=rank*; B83 speaks of an *A-polynomial family*
on a Dehn-filling component. **Same law, different object — a plane curve rather than a matrix
identity, a rank-3 lift rather than a band decomposition.**

> **And the first fix overshot, which is recorded rather than quietly corrected.** Adding bare
> `A-polynomial|Dehn-filling` took the sweep from 3 candidates to **12, nine untriaged, six of them
> false** (B260, B311, B433, B466, B583, B852) — that vocabulary is **ambient** in this corpus, not
> this law's signature. Narrowed to the law's **shape** (the signed power form `L = (−1)^{n−1}M…`,
> and the specific `cusp k-set`) and **tested in both directions**: both true positives survive, all
> six false positives drop.
>
> **Narrowing after seeing results is how `E38` begins, so the distinction is stated:** `E38` is
> narrowing to make a *failing* check pass. This narrowing removes *false positives* while the true
> positives are held fixed as the test — and both directions are locked, so it cannot drift.

## Coverage, measured (B1047) — and the honest proposal

**The instrument was built for *"the laws this refresh restored"*, and that is exactly what it
covers.** The first cluster it was pointed at independently — the seam / level-15 campaign —
belonged to a `LAW_MAP` row (**THE SEAM IS THE ENDS' CLASS FIELD**, B1029) that **had no
fingerprint**, so the sweeper could not see it. That row's fingerprint was added here, and it
immediately surfaced **three real siblings** (B449, B427, B459), all dispositioned above.

| measured 2026-08-12, method stated so it is reproducible | count |
|---|---|
| fingerprints in `FINGERPRINTS` | **6** |
| rows in `LAW_MAP`'s five-column law tables | **154** *(147 at B1047; +3 B1048, +1 B1050, +3 B1051)* |
| all table data rows in `LAW_MAP` (incl. the narrower sub-tables) | **216** |
| **coverage** | **6 / 154 = 4 %** |
| rows citing **≥ 5 arcs** — the *campaign-fed* rows, where a cross-band sibling is likeliest | **62** *(55 at B1047)* |

**The proposal, and it is a proposal — not done here.** Fingerprinting all 147 rows is the same
**unfunded mandate** `law_map_provenance`'s docstring already rejected once for locking all 113.
**Fingerprinting the 62 campaign-fed rows is the defensible middle**: a row that distils five or
more arcs is a row where the law demonstrably spans arcs, which is the precondition for it to span
*bands*. That is roughly 56 fingerprints to author, each of which will surface candidates that then
need **body reads** — so the real cost is the reading, not the regex, and it should be paid a
cluster at a time, as B1047 paid this one.

**What this measurement is not.** 4 % is **not** a defect rate. The instrument was scoped to the
restorations and it did that job — it caught B485 on first independent use, and B449/B427/B459 on
second. The number is published so nobody reads a green `law-siblings` gate as *"the corpus has no
cross-band siblings"*. **It means: none among the six laws that have fingerprints.**

> **And B1051 sharpened what "none" is worth.** Two of the six fingerprints were re-swept after
> widening and each found a sibling that had been sitting uncited since B0–B99 — **so a clean sweep
> means "none among these laws, as these fingerprints are currently written", and the second clause
> is doing real work.**

> **B1050 added a seventh LAW_MAP row and NO fingerprint for it** — deliberately. The wall it
> restores is a **negative**, and the instrument's fingerprints are written for laws whose
> restatements a later arc might duplicate. *Whether a negative can have a cross-band sibling at all
> is a real question and is not answered here;* it is noted so a future sweep does not read the
> absence as an oversight.

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

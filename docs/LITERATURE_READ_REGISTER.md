# THE LITERATURE READ REGISTER — what this programme has READ AT SOURCE, and what it has only CITED

**Created 2026-09-17, seat `xb` (xB023), at the owner's direction:**

> *"why dont we deep search all literature to all objects and families and its roots to see whether
> insightful work already exist and read these papers properly to understand our subjects better"*

**Why this exists.** On 2026-09-17 a single session found that **four of five citations given from
memory were wrong** (E58's instance), and then found a **sixth** defect of a different kind: a
theorem correctly quoted but **applied outside its hypotheses** (B1239's use of Kawauchi on cusped
manifolds). `docs/THEOREM_REGISTRY.md` records the programme's **own** theorems and their novelty
status. **This register records EXTERNAL theorems and whether anyone here has actually opened the
paper.**

## The three grades, and the rule

| grade | meaning |
|---|---|
| **READ-AT-SOURCE** | someone here obtained the paper and quoted the statement **from its own text**, with hypotheses transcribed |
| **CITED-UNREAD** | the statement is used from a secondary source, a summary, or memory. **It may not carry a load-bearing step alone.** |
| **UNREACHABLE** | the source was sought and could not be obtained (paywall, no preprint). **Records the attempt so it is not re-attempted blindly.** |

> **THE RULE THIS REGISTER ENFORCES: a CITED-UNREAD theorem may motivate a computation, may suggest
> a prediction, and may be named — but it may NOT be the sole support for a banked conclusion.
> Where a CITED-UNREAD statement is load-bearing, MEASURE the statement instead and grade the
> result as a measured law.**
>
> **And the lesson that cost the most: quoting a theorem correctly is NOT enough. Check that the
> object in hand SATISFIES ITS HYPOTHESES.** A correctly-quoted theorem applied to the wrong class
> of object fails exactly as badly as a misquoted one — and is harder to see.

---

## The register

| source | statement, as used here | grade | where it bears | notes |
|---|---|---|---|---|
| **A. Kawauchi, *On 3-manifolds admitting orientation-reversing involutions*, J. Math. Soc. Japan 33 (1981) 571–589** | **THEOREM I:** *"Given a pair (M, α), then the torsion subgroup T₁(M;ℤ) of the homology group H₁(M;ℤ) is isomorphic to a direct double A⊕A or a direct sum A⊕A⊕ℤ₂ for some A."* — where the paper's own opening fixes a **pair (M,α)** as *"M a **CLOSED, ORIENTED** 3-manifold, α an orientation-reversing involution."* **THEOREM III:** σ(M)=0 ⟺ σ(α,M)=0 ⟺ M bounds a compact 4-manifold with a compatible involution (four equivalent conditions), with **Definition 1.2** making σ(α,M) the number of **discrete fixed points mod 2**. | **READ-AT-SOURCE** (2026-09-17, xB023) | B1239's torsion step; xB023 W2/K1–K3 | **FORCED A CORRECTION.** A free involution has Fix = ∅ ⇒ σ(α,M)=0 ⇒ σ(M)=0 ⇒ **strict** direct double, so the paraphrase *"free ⇒ Tor = A⊕A"* **is sound**. Its one defect is that **B1239 applies it to CUSPED manifolds**, which are not pairs (M,α): measured failure **590 of 1260**. Tested on 46 manifolds built to satisfy the hypotheses: **46/46**. |
| **W. D. Neumann and J. Yang, *Rationality problems for K-theory and Chern–Simons invariants of hyperbolic 3-manifolds*, Enseign. Math. 41 (1995); arXiv math/9712225** | **THEOREM A:** *"The Chern–Simons invariant CS(M) of a hyperbolic 3-manifold is rational if the associated embedding of the invariant trace field k(M) is a CM-embedding."* Plus their **conjecture**: if `k ∩ k̄ ⊂ ℝ` then CS(M) is **irrational** — which covers **all odd-degree trace fields**. | **READ-AT-SOURCE** (theorem statements; 2026-09-17, xB023 literature pass) | xB015's rational-CS result on the 112-family; the 1.51 % base rate | The record already had this **correctly** after xB015's own correction, including that it is the **Enseign. Math.** paper and **not** the Duke *Bloch invariants* paper. This pass **confirms**, it does not correct. `ℚ(√−3)` is imaginary quadratic, hence CM, which is why the family's CS is rational. |
| **R. Meyerhoff and M. Ouyang, *The η-invariants of cusped hyperbolic 3-manifolds*, Canad. Math. Bull. 40 (1997) 204–213, DOI 10.4153/CMB-1997-025-8** | the cusped η–cs relation; **L194's named tool** for closing the cusp-local lemma | **UNREACHABLE** — Cambridge Core paywall; no preprint found (2026-09-17). Abstract obtained: *"The η-invariant for a cusped hyperbolic 3-manifold is defined and applications are discussed. Such an invariant detects the chirality of a hyperbolic knot or link."* | L194's open half | **THE BLOCKER.** L194's register entry has carried it as *"cited, not read"* since 2026-09-02. **xB023 cites it nowhere** and closes nothing with it. Secondary route noted: Yoshida's formula for η(M(p,q)) and Meyerhoff's special-singular-frame construction are described in citing literature — a legitimate next attempt, **not** a substitute. |
| **CGHN (Coulson–Goodman–Hodgson–Neumann), *Computing arithmetic invariants of 3-manifolds*** | p. 14: SnapPy computes closed CS **only mod ½**; p. 15: the APS relation `3η(M) ≡ 2cs(M) + τ (mod 2)` | **CITED-UNREAD** (quoted through B1239) | B1239's closed-case argument; xB023's mod-½ fence | B1239's **main** closed conclusion rests on this, not on Kawauchi. **Flagged for a read pass** — it is currently the load-bearing unread citation in the L194 chain. |
| **Neumann–Reid**, invariant trace field = the field generated by the tetrahedron shapes | used to identify the **shape field** with the **invariant trace field** | **CITED-UNREAD** | xB022 V4 | xB022 **declined to rely on it**: it reports the **shape field** and explicitly does **not** claim the identification. The correct handling of a CITED-UNREAD statement, and the model for this register. |
| **Witten, arXiv:1001.2933 eq. 2.2; Gukov, hep-th/0306165 §1.1** | `σ` is a continuous parameter of complex Chern–Simons; nothing couples it to `k` | **CITED-UNREAD** | xB016's closure of the index→anchor route; xB021 S4's limit | Load-bearing for a **negative** (a route being closed), which is the lower-risk direction — but it should still be read. |
| **Bergeron–Venkatesh, Conjecture 1.3** | the `1/(6π)` torsion growth constant | **CITED-UNREAD, and mis-graded once** | corrected earlier this session | It is a **CONJECTURE, not a theorem**, and the record previously carried it as a theorem. Already corrected; listed here so the correction is not lost. |

---

## Standing targets for the next literature pass

Ordered by how much weight they currently carry unread:

1. **CGHN** — the APS relation and the mod-½ statement. **Highest priority**: it is the load-bearing unread citation in the entire L194 chain.
2. **Meyerhoff–Ouyang** — L194's blocker. Try an interlibrary route, Ouyang's thesis, or a citing paper that reproduces the formula in full.
3. **Neumann–Reid** — would upgrade xB022 V4 from *shape field* to *invariant trace field* and remove a declared fence.
4. **Witten / Gukov** — read at the equation level, to make xB016's closure a read closure.
5. **Floyd–Hatcher, Guéritaud** (punctured-torus bundles) and **Minsky** (punctured-torus groups) — the family's own roots; B1404 already verified the Minsky relay against the arXiv record.

**This register is appended to, never rewritten.** A grade may only move **upward** (CITED-UNREAD →
READ-AT-SOURCE) by an arc that quotes the source's own text, and the arc is named in the row.


---

## AMENDMENT 1 — xB024's pass (2026-09-17, seat `xb`)

**The register is append-only; these rows amend the table above and do not rewrite it.**

| source | grade change | what the source actually says |
|---|---|---|
| **Neumann–Reid**, *Arithmetic of Hyperbolic Manifolds*, Topology '90, de Gruyter (1992) 273–310 | **CITED-UNREAD → READ-AT-SOURCE** (xB024 T3) | **Theorem 2.4: `k_Δ = k(Γ)`**, stated for **M CUSPED**, with `k_Δ = ℚ(z_j : j = 1,…,n)` generated by **ALL n** tetrahedral parameters of **any** ideal triangulation. **This found a defect in xB022 V4**, which computed `ℚ(z₁)` alone. Corrected: 0 of 72 determined words differ; **xB022 V4's conclusion unchanged, its instrument wrong.** **xB022 V4's fence is RETIRED for the cusped corpus.** |
| **Witten**, arXiv:1001.2933 | **CITED-UNREAD → READ-AT-SOURCE** (xB024 T4) | **eq. (2.2) verbatim:** `I = −s Im W + ℓ Re W, s ∈ ℂ, ℓ ∈ ℤ`; `t = ℓ + is` (2.4). The level is forced integral **by the mod-2π indeterminacy of `Re W`**; `s` is an **arbitrary complex number**. **Stronger than the record's phrasing.** |
| **Gukov**, hep-th/0306165 | **CITED-UNREAD → READ-AT-SOURCE** (xB024 T5) | **§1.1 verbatim:** `t = k + is`, *"Consistency of the quantum theory requires the "level" k to be an integer, k ∈ ℤ. The other parameter, s, is not quantized. **However, s must obey certain constraints imposed by unitarity**."* **REFINEMENT the record does not carry:** we say *"free continuous parameter"*; the source says **not quantized but unitarity-constrained**. xB016's closure is unaffected — it needs only that nothing couples `σ` to `k`. |
| **CGHN** | **CITED-UNREAD → UNREACHABLE** (xB024 T1) | Project Euclid **paywall**; **not on arXiv**; Neumann's free survey (`mathsci.kaist.ac.kr/~manifold/Neumann.pdf`) returned **HTTP 503 on two attempts**. **Still the load-bearing unread citation in the L194 chain.** Per this register's rule it supports **nothing**. |
| **Meyerhoff–Ouyang** | **UNREACHABLE confirmed** (xB024 T2) | Two **new, unread** leads for a future attempt: **Ouyang, *A simplicial formula for the η-invariant of hyperbolic 3-manifolds*, Topology 36 (1997) 411–421**; **Yoshida, Invent. Math. 81 (1985) 473–514**. |
| **Floyd–Hatcher** (1982) and **Guéritaud–Futer** (2006) | **new rows, CITED** | Floyd–Hatcher classified incompressible surfaces in punctured-torus bundles; Guéritaud–Futer gave canonical triangulations of once-punctured torus bundles. **Located, not read at source, no correction found, no insight claimed.** |

**THE PASS'S OWN HEADLINE, recorded here because the seal required it:
xB024 found NO new insight.** No source changes how the programme sees the object, the family, or
their roots. What it produced is one correction to our own instrument, two refinements, one fence
retired, and two sources still out of reach. **A literature sweep that only confirms things must be
reported as a sweep that only confirmed things.**

**The standing target list is now:** **CGHN first** (unchanged — it carries the most unread weight),
then **Meyerhoff–Ouyang** via the two new leads, then **Floyd–Hatcher / Guéritaud** if the family's
roots are ever load-bearing.

---

## AMENDMENT 2 — CGHN OBTAINED; the UNREACHABLE grade was this seat's error (2026-09-17, xB024 Addendum 1)

| source | grade change | what the source actually says |
|---|---|---|
| **CGHN**, *Computing Arithmetic Invariants of 3-Manifolds*, Experiment. Math. **9** (2000) 127–152 | **UNREACHABLE → READ-AT-SOURCE** | **§5A:** *"If M is closed the Chern–Simons invariant is well defined modulo 1, but Snap and SnapPea still only compute modulo 1/2."* **§5B:** *"The relation of η(M) to cs(M) for a **compact** 3-manifold M is `3η(M) ≡ 2cs(M) + τ (mod 2)` (see [Atiyah et al. 1975]), where τ is the number of 2-primary summands of H₁(M;ℤ)."* **Both of B1239's quotations are EXACT and correctly attributed.** |
| **Meyerhoff–Ouyang** | **UNREACHABLE, with its CONTENT now known secondhand** | CGHN §5B: *"Meyerhoff and Ouyang [1997] extended the definition of η(M) to cusped M **for which one has chosen a basis of homology at each cusp**."* **GRADE: SECONDARY** — CGHN describing MO. **MO itself is still unread and still cited for nothing.** This confirms L194's long-standing guess about a "cusp-basis correction". |
| **Atiyah–Patodi–Singer**, *Spectral asymmetry and Riemannian geometry, II*, Math. Proc. Cambridge Philos. Soc. **78**:3 (1975) 405–432 | **new row, CITED-UNREAD** | The source of the `3η ≡ 2cs + τ` relation, as CGHN attributes it. **Read CGHN's statement, not APS's.** |

### THE PROCESS LESSON, which is the point of this amendment

**The UNREACHABLE grade was wrong, and it was wrong in the direction that costs most: it declared a
door shut that was open.** CGHN was freely available on **Project Euclid's open archive** and as
**`snappaper3.pdf` on Neumann's Columbia preprints page** — the same page that had already supplied
Neumann–Reid. The failure was that WebFetch's reader could not parse the PDF binary, and that was
read as "no access" rather than "wrong tool".

> **A grade of UNREACHABLE now requires, and this register enforces it going forward:**
> **(1) the author's own page checked; (2) the journal's own archive checked; (3) the bytes fetched
> and parsed locally before concluding.** *"UNREACHABLE" must describe the source, never the search.*

**Consequence for xB024's banked headline.** The arc reported *"NO new insight"* — reached while
CGHN was wrongly believed out of reach. **That headline stands for the six targets it covered and
NOT for T1**, where CGHN yields B1239's confirmation, MO's actual requirement, and a closed-case
chain whose every substantive link is now read at source.

---

## AMENDMENT 3 — Neumann's CS paper read; MO priced (2026-09-17, xB024 Addendum 2)

| source | grade | what it says |
|---|---|---|
| **W. D. Neumann**, *Combinatorics of Triangulations and the Chern–Simons Invariant for Hyperbolic 3-Manifolds*, Topology '90, de Gruyter (1992) 243–271 (`cspaper.pdf`, Columbia) | **new row, READ-AT-SOURCE** | **The paper Snap/SnapPy's CS formula comes from** — every `CS` number in this record rests on it. §1: *"If M is … compact, then its Chern–Simons invariant CS(M) is well-defined modulo 2π². If M is non-compact then Bob Meyerhoff has shown in [M] that there is still a natural definition of CS(M) which is well-defined modulo π². Let V(M) = Vol(M) + i·CS(M)…"* Theorem 2's constant is *"conjecturally in (iπ²/6)ℤ … a six-fold ambiguity."* |
| **CGHN §5A** (already READ-AT-SOURCE) | — | *"two commonly used normalizations … related by `cs(M) = (1/2π²)·CS(M)`."* |
| **Meyerhoff–Ouyang**, Canad. Math. Bull. **40**:2 (1997) 204–213 | **UNREAD — priced, six routes named** | Cambridge (paywall) · arXiv (absent) · Neumann's page (no eta paper) · EuDML (interface unfetchable) · Springer for the companion Meyerhoff–Neumann, **Comment. Math. Helv. 67**:1 (1992) 28–46 (paywall) · **empirical substitute CLOSED: SnapPy exposes only `chern_simons`, there is no `eta` accessor.** |
| **M. Ouyang**, *A simplicial formula for the η-invariant of hyperbolic 3-manifolds*, **Topology 36**:2 (1997) 411–421 | **new row, UNREAD** | CGHN names it as the **global** proof of the `η(M(p,q))` formula; Meyerhoff–Neumann 1992 proved it locally. Elsevier paywall. |

**L223's LITERATURE half CLOSES.** L223 named three candidate normalisations and the record's
reading of Neumann's — `CS = 2π²·cs` mod `π²` — **is exactly right**, now read at source from both
ends. What remains in L223 is record-internal bookkeeping (which normalisation enters B1012's
`k`-coupling), **which was never a literature question.**

**A question opened and explicitly NOT an identification:** Neumann's Theorem 2 has a conjectural
**six-fold** ambiguity; xB015 found a **ℤ/12** index. **No map between them is exhibited and none is
claimed** — matching small integers in different places is this record's most-repeated error class.

**The access lesson, completing Amendment 2's:** a grade of UNREACHABLE/UNREAD is reportable only
with **the routes named**. Amendment 2 was wrong because one failed fetch was read as a closed door;
this row is right because six routes were tried and are listed.

---

## AMENDMENT 4 — Meyerhoff–Neumann obtained (2026-09-18, xB024 Addendum 3)

| source | grade change | what it says |
|---|---|---|
| **R. Meyerhoff and W. D. Neumann**, *An asymptotic formula for the eta invariants of hyperbolic 3-manifolds*, **Comment. Math. Helv. 67 (1992) 28–46**, DOI `10.5169/seals-51082` | **UNREAD → READ-AT-SOURCE** | **Theorem 1** holds for a one-cusped M *"with the basis `m, l` at the cusp chosen so that `l` is a **longitude**, that is, it is **null-homologous in M**"*, and expresses `−(2/π)Vol + 3η` of the filling via Thurston's parameter, the core geodesic's complex length, **and an explicit INTEGER `I(p,q)` from the Hirzebruch defect**, with recurrences from **Dedekind-sum reciprocity**. Their numerical remark: *"one expects rational eta invariant for geometric reasons (**some cover has an orientation reversing self-homeomorphism**)"*. **Their worked example `N = W(3,−2;6,−1)` has `Vol(N)` equal to the Gieseking volume — verified here to 40 digits as exactly `vol(m004)/2` — is placed over `ℚ(√−3)`, and has `η(N) = 0`.** |
| **Meyerhoff–Ouyang**, Canad. Math. Bull. **40**:2 (1997) 204–213 | **still UNREAD** | **Remains L194's blocker**, and is cited for nothing. What is still missing is the **transformation law of η under an orientation-reversing isometry acting on the invariant cusp** — how the chosen basis is carried, and what that does to `I(p,q)`. |

**How it was obtained, recorded because the register's own rule turns on it.** The free ETH
E-Periodica copy is behind a **proof-of-work bot challenge**, not a paywall. This seat **declined to
automate past it** — a browser check is the operator's expressed intent, and Playwright being
available is not a licence. **The owner opened it and supplied the PDF.** Parsed locally with
`pypdf`, as with Kawauchi and CGHN.

> **The three-route rule from Amendment 2 is amended by this case.** *"Author's page, journal
> archive, bytes parsed locally"* was necessary and **not sufficient**: here the journal's own free
> archive was found and the bytes still could not be had, for a reason that is **neither paywall nor
> absence**. A fourth outcome now exists and must be named when it occurs: **REACHABLE-BUT-GATED —
> the content is free, the route is known, and taking it would override an operator's deliberate
> control.** That is not an access failure and must not be logged as one; **it is a request to make
> of a human.**

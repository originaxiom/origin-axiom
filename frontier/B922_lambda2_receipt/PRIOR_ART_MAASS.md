# B922 — ADVERSARIAL PRIOR-ART PANEL on the λ₂ priority claim

**Panel:** the literature panel (adversarial sweep, external bibliographic databases only)
**Date of sweep:** 2026-08-07
**Mandate:** attack, not defend. A found citation was the preferred outcome.

---

## The sentence under audit

> "λ₂ RECEIVED: **the first 25-digit Maass eigenvalue on any hyperbolic 3-manifold**"
> "(H² reaches 1000 digits; H³ had reached ~10 — the precedent number)"

with r = 4.9000853730625213014795758 (25 decimal places, 26 significant digits),
λ = 1 + r² = 25.01083666330126855876589, on the figure-eight knot complement m004.

---

## VERDICT

**PRIOR ART FOUND — PARTIAL. The priority claim survives on precision; its precedent
number is wrong; and two qualifiers in the sentence are load-bearing in ways the sentence
does not currently earn.**

Split by sub-question, because the three have genuinely different answers:

| Sub-question | Verdict |
|---|---|
| 1. Maass eigenvalues on hyperbolic 3-manifolds computed at all? | **PRIOR ART FOUND — abundantly.** An eight-item literature, 1991–2025. |
| 2. At what precision? | **PRIOR ART FOUND at 13 decimal places / 14 significant digits.** The claim of 25 decimals still leads by 12 decimals. |
| 3. The figure-eight complement / r = 4.9000853… specifically? | **NO PRIOR ART AT THE DEPTH SEARCHED** — with one sharp caveat below that the arc must absorb. |

### Verdict on the repo's "~10 digits" precedent number

**REFUTED (mildly, and in the direction that costs the claim ~4 digits of headroom).**

The true figure is **13 decimal places / 14 significant digits**: r = 6.6221193402528,
the smallest non-trivial Picard-group eigenvalue, printed verbatim in Aurich–Steiner–Then
§8 and identically in Then's companion paper. "~10" is a fair description of their
*tabulated* data (8 decimal places throughout Tables 1 and 2, i.e. 9–11 significant
digits depending on the magnitude of r), but it understates the single best published
number. The precedent sentence should say **13** (or "≈14 significant digits"), not ~10.

### Verdict on the "H² reaches 1000 digits" side-claim

**CORROBORATED, verbatim and exactly.** Booker–Strömbergsson–Venkatesh, *Effective
computation of Maass cusp forms*, IMRN 2006, abstract: "we compute to over 1000 decimal
places the Laplacian and Hecke eigenvalues for the first few Maass forms on PSL(2,Z)\H
… we apply this to prove that our values for the first ten eigenvalues on PSL(2,Z)\H are
**correct to at least 100 decimal places**." Note the second half: on H², 1000 places are
*computed* but only 100 are *certified*. If the arc quotes the 1000 figure it should carry
that distinction, since B922's own 25 digits are stability-certified rather than
rigorously verified in the BSV sense.

---

## 1. The complete computational H³ Maass literature

This field is **small and closed** — that is itself the most useful finding. The canonical
foundational paper (Grunewald–Huntebrinker 1996) has **exactly 10 citers worldwide**; the
Elstrodt–Grunewald–Mennicke monograph has 300, of which **zero** beyond the list below
contain a numerical Maass-eigenvalue computation. Eight items, in full:

| # | Source | What it computed | Digits | Setting |
|---|---|---|---|---|
| 1 | **Smotrov & Golovčanskiĭ 1991**, Bielefeld preprint 91-040, "Small eigenvalues of the Laplacian on Γ\H³ for Γ = PSL₂(Z[i])" | small eigenvalues | not reached | Picard, d=1 |
| 2 | **Grunewald & Huntebrinker 1996**, *Experiment. Math.* **5**(1) 57–80 | finite-element eigenvalues for "various noncompact groups Γ", incl. non-arithmetic | **~5 sig figs**, last digit disclaimed (secondary) | several, incl. PSL(2,O₃) |
| 3 | **Huntebrinker 1996**, *Diss. Summ. Math.* **1** 29–36 | FEM eigenvalues on 3-dim hyperbolic spaces | not reached | several |
| 4 | **Steil 1999**, IMA Vol. Math. Appl. **109** 617–641, "Eigenvalues of the Laplacian for Bianchi groups" | **2545 consecutive** eigenvalues via a non-linear Hecke system | **~5 decimals** (bounded, see below) | Picard, d=1 |
| 5 | **Then 2003** (math-ph/0305048) and **Aurich–Steiner–Then 2004** (gr-qc/0404020) | **13950 consecutive** eigenvalues + eigenfunctions, Hejhal's algorithm extended to 3D | **8 decimals tabulated; 13 decimals for the ground state** | Picard, d=1 |
| 6 | **Möhring 2004**, Göttingen diss., "Untersuchungen zu kubischen metaplektischen Formen" | Fourier expansions by collocation, cubic Shimura correspondence | not reached (403) | Bianchi over **ℚ(√−3)** |
| 7 | **Inoue 1999, 2001** (Class. Quantum Grav.) | low-lying Laplace eigenvalues, boundary-element & periodic-orbit-sum | low (method-bounded) | **closed** hyperbolic 3-**manifolds** (Thurston, Weeks, …) |
| 8 | **De Clerck–Hartnoll–Yang 2025** (arXiv:2507.08788, hep-th) | Hejhal's algorithm on **both** the Gaussian and **Eisenstein** billiards; 650/1000 prime Hecke coefficients | **6 sig figs** | d=1 **and d=3** |

### The precision record, read off the actual page

Aurich–Steiner–Then, gr-qc/0404020, §8 "Eigenvalues", verbatim:

> "The smallest non-trivial eigenvalue is E = k² + 1 with **k = 6.6221193402528** which is
> in agreement with the lower bound E > 2π²/3."

That is **13 decimal places, 14 significant digits** — the highest-precision Maass
eigenvalue on any quotient of H³ that this panel could read anywhere in the literature.
The identical value appears in Then math-ph/0305048 §(same). Their Tables 1 and 2 are
uniformly 8 decimal places (e.g. 8.55525104, 6.62211934, 139.65419675). Their only
independent corroboration is weaker still: "The eigenvalues listed in table 1 agree with
those of Steil up to **five decimal places**."

So the honest three-tier reading of the prior art, which any priority sentence should
respect:

- **5 decimals** — independently cross-checked between two groups (Steil ↔ Then).
- **8 decimals** — systematically tabulated, 13950 eigenvalues.
- **13 decimals** — printed once, for the ground state, with no error bar attached.

B922's 25 decimals exceeds all three tiers. The gap over the strongest reading is
**12 decimal places**.

---

## 2. The figure-eight complement specifically — and the caveat that bites

**No publication computes the Maass spectrum of the figure-eight knot complement (m004,
Γ₄₁) as such.** Five independent search routes returned zero:
title-and-abstract search on three phrasings, the closed citation neighbourhood of every
paper in §1, an author sweep over the entire computational-Maass community, and a
full-text scan of the two most recent candidates. **r = 4.9000853… appears nowhere.**

**But the arc must absorb this caveat, which weakens "m004 has never been computed":**

Γ₄₁ ⊂ PSL(2,O₃) with index 12 (the repo's own B790, by Humbert volume). Therefore **every
published eigenvalue of the parent Bianchi group is, by pullback, an eigenvalue of the
figure-eight knot complement.** Published spectral data for m004's Laplacian consequently
*does* exist, at 5–6 significant digits:

- **r ≈ 24.5033** — De Clerck–Hartnoll–Yang 2025, Fig. 4 caption: "the first 1000 c_p
  associated to the **Eisenstein** waveform at ε ≈ 24.5033", with ε defined by
  −∇²_{H³}ψ = (1 + ε²)ψ (their eq. 27), i.e. ε **is** the spectral parameter r. The
  Eisenstein billiard is PSL(2,Z[ω]) = PSL(2,O₃) — the exact parent group. *(The repo
  already banks this value as its literature control; the panel confirms the transcription
  and the convention from the primary.)*
- **λ₁ = 51.014, r ≈ 7.0721** — Grunewald–Huntebrinker 1996 Table 3 (via secondary
  sources only; see §4).

**This does not damage the specific claim.** r = 4.9000853… cannot be a pullback: the
parent's ground state sits at r ≈ 7.07 > 4.90, so no parent eigenvalue lies below it.
B922's λ₂ is a genuinely new, non-inherited eigenvalue of the index-12 cover. But the
sentence "m004's spectrum has never been computed" is too strong and should not be
repeated; the defensible form is "**no eigenvalue of m004 not inherited from its parent
Bianchi group has previously been computed**".

---

## 3. Load-bearing qualifiers — the analogues of the Dirac sweep's "nonzero"/"cusped"

Three, in decreasing strength:

1. **"25 decimal places" (the precision itself) — LOAD-BEARING, and the only qualifier
   that is genuinely earned.** This is what the claim rests on. 25 vs 13.

2. **"not inherited from the parent Bianchi group" — LOAD-BEARING and currently ABSENT.**
   Without it, a hostile reader answers "the figure-eight complement's eigenvalues were
   published in 2025 at 6 digits, and in 1996 at 5". See §2.

3. **"cusped Maass *cusp form*" vs "eigenvalue of a hyperbolic 3-manifold" —
   LOAD-BEARING and currently ABSENT.** Inoue (1999, 2001) computed low-lying Laplace
   eigenvalues for a large family of **closed hyperbolic 3-manifolds** — genuine manifolds,
   genuinely 3-dimensional, genuinely hyperbolic. They are not cusp forms (closed ⇒ no
   cusps) and the precision is method-bounded and low, but the phrase "on any hyperbolic
   3-manifold" as written does not exclude them.

**A qualifier the panel explicitly recommends NOT leaning on:** manifold-versus-orbifold.
It is true that all the high-precision prior art lives on **orbifolds** — PSL(2,Z[i]) and
PSL(2,Z[ω]) both have torsion — while m004 is a genuine manifold. A priority claim could
technically survive on that distinction alone. **It should not.** The manifold/orbifold
distinction is not what makes the computation hard, no referee would grant it as the
substance of a "first", and resting a claim on it would be exactly the necessary-read-as-
sufficient move the repo's own B525 audit was written against.

---

## 4. Search record — what was reached, what was not

**Reached, with method:**

| Database | Route | Outcome |
|---|---|---|
| **OpenAlex** | REST API; `search=`, `filter=title.search:`, `filter=title_and_abstract.search:`, and **`filter=cites:`** for citation-graph traversal | Fully functional. The traversal was the highest-yield instrument. |
| **arXiv** | Atom API, `search_query` with `ti:`/`abs:`/`all:`/`au:`/`cat:` | Functional; rate-limited to failure after ~25 queries, recovered with backoff, then substituted by OpenAlex. |
| **zbMATH Open** | `api.zbmath.org/v1/document/_search?search_string=…` (plain query string; the `-G --data-urlencode` form 404s, and `cc:` MSC queries combined with a second term 404 — MSC alone works, e.g. `cc:11F72` → 1955 hits) | Located Steil 1999 (zbl 1552125) and Grunewald–Huntebrinker (zbl 952325) with full metadata and MSC codes. **Reviewer texts empty for both**; the GH record is title- and author-suppressed under "conflicting licenses". |
| **LMFDB** | Direct HTTP on the Bianchi and Maass section roots | Both 200. **Corroborates the repo's B790 conflation finding**: "Maass" appears on the Bianchi page only as a sibling entry in the site navigation (Classical / Maass / Hilbert / Bianchi). The Bianchi section is weight-2 cohomological with Hecke eigenvalues; the string "Laplace" does not appear. **No Laplace-eigenvalue data for any Bianchi group.** |
| **Wayback CDX + Machine** | `web.archive.org/cdx/search/cdx` | Recovered the EMIS mirror of *Experimental Mathematics* 5.1 and the Grunewald–Huntebrinker **abstract** (PostScript, converted). No full text archived — only abstracts were ever mirrored. |
| **Unpaywall** | REST on the GH DOI | Malformed response; OpenAlex's own OA record answered the question instead (`is_oa: false`, `oa_status: closed`, no repository full text). |

**Not reached, stated honestly:**

| Target | Barrier |
|---|---|
| **Grunewald–Huntebrinker 1996 full text / Table 3** | Paywalled. Project Euclid → Incapsula block; EMIS direct → Cloudflare 403; CiteSeerX cache (10.1.1.53.7564) → 404; no Wayback capture of either the Euclid PDF or the EMIS full text. **The repo's standing open lead B921-17 is confirmed still open.** The panel obtained only the abstract, which states scope ("various noncompact groups Γ … particularly interesting are the results for some nonarithmetic groups") but no precision. |
| **Steil 1999 full text** | Springer book chapter, not online. Precision known only by the bound below. |
| **Möhring 2004 thesis PDF** | ediss.uni-goettingen.de returns 403 to both direct HTTP and rendered fetch, despite OpenAlex listing an OA bitstream URL. |
| **MathSciNet** | Authentication wall. **Not attempted; no claim is made about its contents.** |
| **Web search engine** | Session budget exhausted (200/200) before this sweep's first query. All findings above come from raw bibliographic APIs and direct HTTP. |
| **Semantic Scholar** | HTTP 429 on both attempts; no API key. Contributed nothing. |

### Residual risk in the three unread items

Low, and bounded by method rather than by assertion:

- **Grunewald–Huntebrinker**: finite-element method. FEM on a 3-dimensional cusped domain
  does not reach 25 decimal places; the authors' own disclaimer that the last digit is
  untrustworthy (recorded in the repo from a secondary source) is consistent with ~5 sig
  figs. Independently, Aurich–Steiner–Then cite GH as prior Picard work and improve on it
  — they would not have described their own 8-decimal tables as an improvement over a
  higher-precision predecessor.
- **Steil 1999**: bounded above by Aurich–Steiner–Then's statement that their values "agree
  with those of Steil up to five decimal places". Had Steil printed more, the agreement
  would have been quoted deeper.
- **Möhring 2004**: a collocation method for Fourier expansions, whose stated purpose is
  numerically confirming a bijective correspondence and testing a Waldspurger-type link —
  not a precision eigenvalue table.

All three predate 2005. The 2005–2026 window was swept independently (citation graph +
arXiv + OpenAlex) and contains exactly one new computational item, the 2025 hep-th paper
at 6 significant digits.

---

## 5. MUST-PASS CONTROL

**PASSED.** Before trusting any null, the panel verified its instrument finds the
well-known H² high-precision work it would be embarrassing to miss:

- **Booker–Strömbergsson–Venkatesh 2006**, "Effective computation of Maass cusp forms" —
  found in OpenAlex (W2152913599, 66 citations, DOI 10.1155/imrn/2006/71281) with the full
  abstract retrieved verbatim, confirming 1000 decimal places computed / 100 certified.
- **Then 2003**, "Maass cusp forms for large eigenvalues" (math-ph/0305047) — found.
- The modern H² certified-computation line — "Rigorous computation of Maass cusp forms of
  squarefree level" (2201.08760), "Certification of Maass cusp forms of arbitrary level and
  character" (2204.11761), Booker–Then "Rapid computation of L-functions attached to Maass
  forms" (1703.08863), Booker–Lee–Strömbergsson "Twist-minimal trace formulas and the
  Selberg eigenvalue conjecture" (1803.06016) — all found, with abstracts.

The same queries and the same citation-graph method, pointed at H³, return the eight-item
list of §1 and nothing else. The null in §2 is therefore an earned null, not an instrument
failure.

---

## 6. How B922's sentence must be rewritten

The current sentence has one factual error (the precedent number) and two missing
qualifiers. Suggested replacement, in descending order of safety:

**Safe (recommended):**
> The second Maass cusp form eigenvalue of the figure-eight knot complement,
> r = 4.9000853730625213014795758, to 25 decimal places — improving the precedent for a
> Maass eigenvalue on a quotient of H³ from 13 decimal places (Aurich–Steiner–Then 2004,
> Picard orbifold ground state) to 25, and the first eigenvalue computed for this manifold
> that is not inherited from its parent Bianchi group PSL(2,O₃).

**Also safe:**
> The highest-precision Maass eigenvalue computed on any quotient of hyperbolic 3-space:
> 25 decimal places, against a published precedent of 13.

**Unsafe as written — do not ship:**
- "the first 25-digit Maass eigenvalue on any hyperbolic 3-manifold" — the numeral 25 is
  doing no comparative work; the reader cannot tell whether the precedent is 3 or 24.
- "H³ had reached ~10" — factually wrong; the figure is 13 decimal places.
- "m004's Maass spectrum has never been computed" — false by pullback from the parent.
- Any form that leans on manifold-versus-orbifold to survive.

---

## 7. Bibliography — what each source actually computed, and to how many digits

**Prior art, H³ (the relevant set):**

1. **Aurich, R.; Steiner, F.; Then, H.** — *Numerical computation of Maass waveforms and an
   application to cosmology*, arXiv:gr-qc/0404020 (2004); reprinted in *Hyperbolic Geometry
   and Applications in Quantum Chaos and Cosmology*, LMS Lecture Notes (2011).
   **13950 consecutive eigenvalues + eigenfunctions, Picard group PSL(2,Z[i])\H³.
   Tables at 8 decimal places; ground state printed at 13 decimal places
   (k = 6.6221193402528). ← THE PRECEDENT.**
2. **Then, H.** — *Arithmetic quantum chaos of Maass waveforms*, arXiv:math-ph/0305048
   (2003/2004). Same data set, same digits; the algorithmic companion.
3. **Steil, G.** — *Eigenvalues of the Laplacian for Bianchi groups*, IMA Vol. Math. Appl.
   109 (1999) 617–641; zbl 1552125; MSC 11F72, 11F06, 81Q50, 11-04, 20H10.
   **2545 consecutive Picard eigenvalues; ~5 decimal places (bounded, not read).**
4. **Grunewald, F.; Huntebrinker, W.** — *A Numerical Study of Eigenvalues of the Hyperbolic
   Laplacian for Polyhedra with One Cusp*, *Experiment. Math.* **5**(1) (1996) 57–80;
   DOI 10.1080/10586458.1996.10504339; zbl 952325; MSC 65N25, 35P20, 65N30.
   **Finite-element; various non-cocompact Γ including non-arithmetic. Table 3 gives 36
   eigenvalues for PSL(2,O₃), λ up to 675, ~5 sig figs with the last digit disclaimed.
   PRIMARY NOT READ — paywalled; figures above are secondary.**
5. **De Clerck, M.; Hartnoll, S. A.; Yang, M.** — *Wheeler-DeWitt wavefunctions for 5d BKL
   dynamics, automorphic L-functions and complex primon gases*, arXiv:2507.08788 (2025).
   **Hejhal's algorithm on the Gaussian and Eisenstein billiards. Spectral parameters
   ε ≈ 25.7239 (d=1) and ε ≈ 24.5033 (d=3 = PSL(2,O₃)) — 6 significant digits.
   The only published d=3 spectral parameter this panel could read in the primary.**
6. **Möhring, L.** — *Untersuchungen zu kubischen metaplektischen Formen*, Diss. Göttingen
   (2004), DOI 10.53846/goediss-2454. Bianchi group over ℚ(√−3); Fourier expansions by
   collocation. **Not read (403).**
7. **Smotrov, M. N.; Golovčanskiĭ, V. V.** — *Small eigenvalues of the Laplacian on Γ\H³
   for Γ = PSL₂(Z[i])*, Bielefeld preprint 91-040 (1991). **Not read.**
8. **Huntebrinker, W.** — *Numerical computation of eigenvalues of the Laplace-Beltrami
   operator on three-dimensional hyperbolic spaces by finite-element methods*,
   *Diss. Summ. Math.* **1** (1996) 29–36. **Not read.**
9. **Inoue, K. T.** — *Computation of eigenmodes on a compact hyperbolic 3-space*,
   Class. Quantum Grav. **16** (1999); *Numerical study of length spectra and low-lying
   eigenvalue spectra of compact hyperbolic 3-manifolds*, Class. Quantum Grav. **18** (2001).
   **Closed hyperbolic 3-manifolds (Thurston, Weeks, …); boundary-element and periodic-orbit-
   sum; low precision; no cusp forms. Relevant only because they are genuine 3-manifolds.**

**Control set, H² (verifies the instrument):**

10. **Booker, A. R.; Strömbergsson, A.; Venkatesh, A.** — *Effective computation of Maass
    cusp forms*, IMRN 2006, DOI 10.1155/imrn/2006/71281.
    **Over 1000 decimal places computed for the first few PSL(2,Z) eigenvalues; first ten
    rigorously certified to ≥100 decimal places. ← corroborates the "1000 digits" side-claim.**
11. **Then, H.** — *Maass cusp forms for large eigenvalues*, Math. Comp. **74** (2005)
    363–381; arXiv:math-ph/0305047.
12. **Booker, A. R.; Then, H.** — *Rapid computation of L-functions attached to Maass forms*,
    arXiv:1703.08863 (2017).
13. **Booker, A. R.; Lee, M.; Strömbergsson, A.** — *Twist-minimal trace formulas and the
    Selberg eigenvalue conjecture*, arXiv:1803.06016 (2018).
14. **"Rigorous computation of Maass cusp forms of squarefree level"**, arXiv:2201.08760 (2022);
    **"Certification of Maass cusp forms of arbitrary level and character"**, arXiv:2204.11761 (2022).
15. **Elstrodt, J.; Grunewald, F.; Mennicke, J.** — *Groups Acting on Hyperbolic Space:
    Harmonic Analysis and Number Theory*, Springer (1998). The monograph underlying the whole
    H³ setting; 300 citers traversed and filtered, yielding **no** numerical Maass computation
    beyond items 1–9.

---

## 8. One methodological note for the record

The decisive instrument here was **citation-graph closure, not keyword search.** Keyword
relevance ranking on OpenAlex was actively misleading — the query "Bianchi Maass forms
computation" returned spiking-neural-network papers in its top hits, and
`title_and_abstract.search:bianchi maass` returned a urology paper and a Czech
sociolinguistics article. Every genuine finding in §1 arrived either through
`filter=cites:` traversal of a foundational paper or through reading a primary PDF's own
bibliography. A null produced by keyword search alone, in this corpus, would have been
worthless.

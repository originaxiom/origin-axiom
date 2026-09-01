# T4_prior_art — ADVERSARIAL VERIFICATION

**Verifier seat:** independent adversarial verifier · **Date:** 2026-09-01
**Cell verdict under attack:** PARTIAL — (a) criterion KNOWN, (b) terminality NOT FOUND (bounded).
**Verifier verdict: CONFIRMED** (with three minor notes, none verdict-moving; details below).

---

## 1. Re-run of the cell's computations

The cell dir contains no scripts — only FINDINGS.md and SEARCH_LOG.md. The cell's only
computation was `pdftotext` + `grep` over two downloaded arXiv PDFs. I re-ran all of it from
scratch (fresh downloads, independent extraction):

- **arXiv:1504.03695 (Fonseca).** Fresh download is **byte-identical** (`cmp`) to the
  `fonseca1504.pdf` left in the session scratchpad at 15:54 by the cell's own run — the full
  text was genuinely downloaded, not paraphrased from memory. All four verbatim quotes in
  FINDINGS.md ("a total of 12 distinct ways of embedding…5 pairs of chiral embeddings…unique
  solution", "unique embedding and a unique fermion field configuration…3 copies of the 27",
  "SM gauge group must be embedded…This uniqueness is far from obvious", "standard fermion
  assignments 3(5bar)+3(10) in SU(5) and 3(27) in E6 appear to be unique, while 3(16) in
  SO(10) is not") reproduce character-for-character modulo pdftotext spacing.
  **Grep counts reproduce exactly:** `chiral` case-sensitive substring = **106** (as logged);
  `further break` / `below the` / `terminal` / `halt` / `stop` = **0, 0, 0, 0, 0** (as logged).
- **arXiv:2102.13465 (Britto).** Fresh extraction byte-count matches the cell's residue file
  (`e6_math_construction.txt`, 215129 bytes, 15:53). All four survival-hypothesis /
  complex-representation quotes in FINDINGS.md reproduce verbatim. `terminal` = 0 hits (as
  logged).
- **Repo-side characterization checked:** B994's FINDINGS carries the verbatim criterion
  *"registerable = the generation stays chiral"*, the [3,2,1] options-per-step table, and the
  six chains all ending at the SM; B863's FINDINGS carries the su(3)₁ → su(2)₄ genuine
  conformal embedding row (c = 2 matching, triplet REAL, chirality killed). The dossier
  (docs/PRIOR_ART_DOSSIER_ENTRANCE_AND_EXIT.md, entry 3) matches the question as the cell
  states it. No misrepresentation of what is being priced.
- **Bibliographic spot-checks:** Fonseca = Nucl. Phys. B897 (2015) 757 (ScienceDirect
  S0550321315002151, confirmed); Tong = JHEP 07 (2017) 104 / arXiv:1705.01853 with exactly the
  claimed content (Γ ⊆ Z6 undetermined by experiment, Z6 from SU(5)/Spin(10) embedding);
  arXiv:2204.03001 confirmed as SO(10), scalar-sector admissibility, SM as assumed target, no
  chirality-terminality criterion, no rule-space quantification.

## 2. MB12 attack

- **Can the criterion fail?** Yes, demonstrably, in both directions: within this very cell,
  half (a) returned **KNOWN** (the criterion fired against the repo's claim), and the same
  apparatus earlier flipped dossier entry 4 to KNOWN. This is not a criterion that always says
  NOT-FOUND.
- **Was the control run, and did it bite?** The logged Q9 cannot be historically replayed, but
  (i) the scratchpad residue proves the retrieval apparatus was live during the run, and
  (ii) **I re-ran Q9 verbatim from this bench and it bites**: Tong arXiv:1705.01853 returned on
  the first page with the exact claimed content. PASS corroborated.
- **Weakness noted (not verdict-moving):** Q9 contains the author name and near-title, so it is
  an easy positive control — it certifies the pipeline, not that *conceptual* phrasings would
  surface an obscure terminality statement. Mitigation: I ran **4 fresh adversarial queries**
  with phrasings absent from the cell's 16 ("no chiral…subgroup of the standard model…
  vector-like theorem terminal", "last chiral/smallest chiral step…any further breaking…
  vector-like", Fonseca-follow-up/downward-extension, "any unbroken subgroup…residual gauge
  group…vector-like spectrum theorem"). **None surfaced a terminality statement.** The
  NOT-FOUND on half (b) survives independent attack at a comparable bound.

## 3. Convention attack (E23)

The convention is stated in FINDINGS.md ("chiral = the left-handed fermion multiset furnishes
a complex representation; vector-like = real or pseudoreal in the aggregate"), matches the
literature definition it quotes (Britto Sec. 2.2, verified verbatim) and matches B994's verbatim
code criterion and B863's generation-multiset test. A literature-search verdict has no
orientation/CS-normalization exposure; the only convention that could bite (which "chiral"
is meant) is pinned on both sides. Survives.

## 4. Gate 5

The cell dir contains only two .md files; no object-side computation ran and no measured SM
value entered anything. The greps operate on literature text, not on the object. Clean.

## 5. Scope attack

The FINDINGS claims **less** than it could: PARTIAL not NOVEL; NOVEL-CANDIDATE only for the
conjunction; explicit "not a novelty certificate"; Slansky-chains and Hewett-Rizzo named as
unread; Fonseca priced as mandatory prior art with the delta stated in both directions.
Three minor notes:

1. **"exhaustive grep" is mildly overstated.** The five grep terms miss at least one
   downward-phrased passage in Fonseca: *"Breaking SU(3)×SU(2)×U(1)^m further down to the SM
   group requires…forming the hypercharge group from a linear combination of the m U(1)'s."*
   I read the full context: it is about descending from SU(3)×SU(2)×U(1)^m **to** the SM
   (SM still the target), not below it — so the substantive claim ("his question is upward,
   never where a chirality-preserving descent must halt") **survives**; only the adjective
   "exhaustive" should have been "targeted".
2. Two of the four "full texts" (2507.06368, hep-th/0112046) were WebFetch reads with no
   residue; unverifiable but load-free (both were negative/ruled-out sources).
3. 2204.03001 is better described as excluding chains via radiative-breaking depth than as a
   neutral enumeration; either reading supports the cell's point (scalar-sector admissibility,
   SM assumed).

## Verdict

**CONFIRMED.** Every reproducible number reproduces exactly (106 chiral hits; 0/0/0/0/0
termination hits; byte-identical PDF; all eight verbatim quotes verified). The bite control was
run, bites again today, and the criterion demonstrably fails in both directions in-run. The
NOT-FOUND on half (b) additionally survives 4 fresh adversarial queries from an independent
bench. The verdict PARTIAL, its bounds, and its pricing of Fonseca are all accurate; the only
defects found are the word "exhaustive" and two unverifiable-but-load-free full-text reads.

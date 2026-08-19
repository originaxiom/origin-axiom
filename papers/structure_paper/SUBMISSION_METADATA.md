# SUBMISSION METADATA — the arXiv package's fields

*Owner decisions 2026-08-15. This file is the source for the LaTeX preamble and for every
field the arXiv web form asks. Kept current with the draft; the checklist at the bottom is
what gets ticked at upload time.*

---

## 1. Author

> **Dritëro Mehmetaj**
> *Independent Researcher*

- **Contact email:** `driteroi@gmail.com` *(supplied 2026-08-15; set in the source's `\email{}`)*
- **ORCID:** *(optional; supply if held)*

## 2. Title — ## PROPOSED (option 4, genesis-first)

> ## **From minimal description to $E_6$: a chain through the figure-eight knot complement**
>
> *(This is the title in `arxiv/main.tex`. An earlier proposal here read "four independent
> selections…"; Appendix C records that phrase as **withdrawn** — three of the four criteria
> collapse to one arithmetic condition — so it must not be used as a title.)*
>
> *(Superseded 2026-08-15: the earlier title, "From minimal description to E₆: a parameter-free
> chain through the figure-eight knot complement", described the 8-page compressed version.
> The paper's subject changed when the four selection theorems became its spine, and the title
> follows the subject: it now names a **selection theorem**, which is what is proved, rather
> than a destination, which is generic.)*

**Why this one.** The owner's constraint is that the paper *starts from minimal
description*, and the title should say so — the three inherited candidates all opened at
`e₆` or at the charge torus, which is now §6, not §1.

**Construction of the title, clause by clause:**

| clause | doing what |
|---|---|
| *From minimal description* | names the actual starting point — the principle of §2, not the algebra |
| *to E₆* | names the destination in the vocabulary of the intended referee |
| *a parameter-free chain* | ## states the **cost claim**, which is what the paper actually proves |
| *through the figure-eight knot complement* | names the object, and signals the subject area (math.GT) |

**Deliberately NOT in the title: `su(3) ⊕ su(2) ⊕ u(1)³`.** It is the true endpoint and it
is stated in the abstract's second sentence — but in a *title* it recruits the wrong prior
before a mathematics referee has read a line. `E₆` gets the paper opened; the Standard
Model algebra gets it filed. The endpoint loses nothing by arriving one sentence later.

**Alternates, if the owner prefers:**
- *Minimal description, the figure-eight knot complement, and a forced cascade to `su(3) ⊕ su(2) ⊕ u(1)³`* — fully explicit, longer, higher prior-risk
- *A parameter-free chain from minimal aperiodic description to the exceptional Jordan algebra* — most conservative; drops the knot from the title

*(The three inherited candidates in `ABSTRACT_DRAFT.md` are superseded by the genesis-first
decision but retained there for the record.)*

## 3. Classification

**Primary: `math.GT`** (Geometric Topology) — unchanged; the selection theorems are
about once-punctured-torus bundles. Note the added secondary **`46L37`** (subfactors), for
the Jones-index selection — the object is a hyperbolic 3-manifold and the
genesis is a surface-bundle construction; §§3–5 are the paper's spine and live here.

**Cross-list:** `math.NT` (the arithmetic of §4–§5 — the Kleinian trace field and the fiber
field, congruence structure, the shadow modulus) · `math.RA` (the exceptional algebra and the cascade, §§6–8).

> ## **NOT originating in `hep-th`.** The content that is solid is mathematical; the content that failed is the physics contact, and §9 says so. A physics-first submission is pattern-matched before it is read.

**MSC 2020.** Primary **57K10** (knot theory), **11R16** (cubic and quartic extensions),
**57M50** (geometric structures on 3-manifolds). Secondary **17B25** (exceptional Lie
algebras), **17A75** (composition algebras), **11J06** (Diophantine approximation — §3.2's
Hurwitz/Lagrange step).

*(This inverts `ABSTRACT_DRAFT.md`'s ordering, which had the Lie-algebra classes primary —
correct for the algebra-only skeleton, wrong for the genesis-first paper.)*

**Keywords:** figure-eight knot complement · Sturmian words · continued fractions ·
Lagrange spectrum · McKay correspondence · exceptional Jordan algebra · cone-manifold
geometric transition · parameter-free derivation.

## 4. Licence

**arXiv non-exclusive perpetual licence** (the default). Rationale: it permits arXiv
distribution without foreclosing a later journal submission, and imposes no obligations on
third parties that a CC licence would. *(Owner may prefer CC BY — a one-field change.)*

## 5. Endorsement — **deferred by owner decision**

A new submitter to `math.GT` typically requires an endorsement. **This comes after the
paper**, per the owner. Noted here because it is the same problem as finding the outside
expert reader the paper needs before submission, and solving it once solves both.

---

## Upload checklist (ticked at submission, not before)

- [x] author block complete, **contact email supplied** — `driteroi@gmail.com`
- [x] title final — set in `arxiv/main.tex`
- [ ] abstract pasted as plain text (no LaTeX macros) — abstract written; paste at upload
- [x] primary + cross-list categories set (§3 above; `\subjclass` in the source)
- [x] MSC + keywords entered in the source
- [ ] licence selected — decision recorded in §4, selected at upload
- [x] ## **`arxiv/` package builds**: `main.tex` only. **Bibliography is INLINE
      (`thebibliography`), so there is no `.bib` and no `.bbl` step** — which is the
      arXiv-preferred shape and removes a whole class of upload failure
- [x] ## **clean-room compile RE-VERIFIED 2026-08-19** — tarball extracted into an
      empty directory with no repository present, compiled twice:
      **exit 0 both passes, zero errors, 47 pages**
- [x] `verify_all.py` green from the extracted tarball (**19/19**; an empty suite fails
      by construction)
- [x] the arXiv abstract field prepared: the paper's own abstract is **2867 characters**
      and arXiv's metadata limit is **1920**, so `arxiv/abstract_arxiv_metadata.txt`
      carries a **1915-character** compressed version with every hedge retained
- [ ] endorsement obtained — deferred by owner decision

### Build

```
cd arxiv && pdflatex main.tex && pdflatex main.tex     # two passes, no bibtex
grep -c '^!' main.log                                  # MUST be 0 -- see below
rm -rf verify && cp -R ../verify verify                # block (a) MUST travel
tar czf oa-structure-paper.tar.gz main.tex verify      # the upload artifact
```

> **CHECK THE LOG FOR `^!`, NOT ONLY FOR OVERFULL BOXES.** Added 2026-08-19 after a
> stray `\end{remark}` — introduced by an edit on 08-18 — sat in every build for a day.
> Under `-interaction=nonstopmode` LaTeX *recovers* from an unbalanced environment and
> still writes a plausible PDF with the right page count, so the checks that were being
> run (overfull boxes, undefined references, page count) were all green while the source
> was malformed. Only `grep -c '^!' main.log` and a non-zero `pdflatex` exit code caught
> it. Both are now in the recipe above.
>
> **This recipe was wrong until 2026-08-15 and the error was load-bearing.** It packaged
> `main.tex` alone, while Appendix B told the referee that block (a) "travels *inside*
> the submitted source, so a referee can run them from the arXiv tarball alone". It did
> not. `verify/` sits one directory above `arxiv/` and was never copied in. Caught by a
> hostile read that opened the built artifact instead of trusting the sentence.

**Known gaps before this is submittable** (none of them build failures), updated
2026-08-19:

- ~~seven `refs.bib` entries at `STANDARD`~~ — **closed**: every entry is now `RESOLVED`
  against a publisher record; zero `verify before submission` flags remain. (The inline
  bibliography in `main.tex` is what ships and was already correct.)
- ~~no figures yet~~ — **closed**: 3 figures.
- ~~Appendix C glossary not written~~ — **closed**: the glossary is Appendix D; Appendix C
  is the consolidated corrections list.
- ~~the adversarial read not run~~ — **closed**: two external referee reports were
  processed, and the twelve-item paper-closure campaign that followed them is closed at
  **12/12** (`frontier/B8076_paper_closure/CAMPAIGN.md`).
- **OPEN, and the owner's alone:** the endorsement, and the upload itself.

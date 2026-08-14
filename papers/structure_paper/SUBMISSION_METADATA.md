# SUBMISSION METADATA — the arXiv package's fields

*Owner decisions 2026-08-15. This file is the source for the LaTeX preamble and for every
field the arXiv web form asks. Kept current with the draft; the checklist at the bottom is
what gets ticked at upload time.*

---

## 1. Author

> **Dritëro Mehmetaj**
> *Independent Researcher*

- **Contact email:** *(needed at upload — not recorded here)*
- **ORCID:** *(optional; supply if held)*

## 2. Title — ## PROPOSED (option 4, genesis-first)

> ## **From minimal description to E₆: a parameter-free chain through the figure-eight knot complement**

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

**Primary: `math.GT`** (Geometric Topology) — the object is a hyperbolic 3-manifold and the
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

- [ ] author block complete, **contact email supplied**
- [ ] title final
- [ ] abstract pasted as plain text (no LaTeX macros)
- [ ] primary + cross-list categories set
- [ ] MSC + keywords entered
- [ ] licence selected
- [ ] `arxiv/` tarball: `.tex` + `.bbl` + figures, **no `.bib`**
- [ ] clean-room compile verified in an empty directory
- [ ] `verify_all.py` green
- [ ] endorsement obtained

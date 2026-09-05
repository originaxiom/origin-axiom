# B1257 — THE ORBIT THAT REMEMBERS 2T: Brieskorn–Slodowy selects the subregular, uniquely — and the theorem that does it was in B327's own bibliography, cited and unused, for nine hundred arcs

**Date:** 2026-09-05 · **Seat:** cc · **Status:** PROVED (exact; four MB12 controls, the decisive one being that the selection never looks at the 27)

## The question

**B1256** registered **I-25 UNEARNED**: the object's SL(2) was assumed to embed in E₆ via the
**principal** sl₂ — a choice never derived, and one that decides the typing of h¹ and therefore the
generation count. Four candidate embeddings survive; is there a **principled** selector?

## The archaeology — where the assumption entered, and what was sitting next to it

The principal grading entered at **B327** (`mckay_branching_gate`, the B32x era): *"the principal 27
decomposition is V(16)+V(8)+V(0)"*, fenced as *"Exact E₆ Weyl-orbit + **principal grading**"*. It was
never revisited. **B327's own literature line reads:**

> *Kostant (principal SL(2)); the McKay correspondence 2T ↔ Ẽ₆ (Gonzalez-Sprinberg–Verdier, **Slodowy**)*

**Both were cited; only Kostant's was used.** The theorem that selects the other orbit was already in
the arc's reading list, one clause away, and stayed unused for ~930 arcs.

## The criterion

For a simple Lie algebra **g** of type ADE, **Brieskorn–Slodowy**: the transverse (Slodowy) slice
`S_e` to a nilpotent orbit `O` meets the nilpotent cone `N` in a variety of dimension
`dim N − dim O`, and for the **subregular** orbit this is a **simple surface singularity ℂ²/Γ of the
same ADE type as g**. For E₆, **Γ = 2T**, the binary tetrahedral group.

**The object's E₆ was BUILT from 2T by McKay** — **I-1, EARNED** (*the rep graph IS the diagram*). So
among E₆'s canonical orbits, ask the closure question: **which one's geometry returns the very group
the algebra was built from?**

| orbit | weighted Dynkin | dim O | dim(S ∩ N) | |
|---|---|---|---|---|
| regular / **principal** | (2,2,2,2,2,2) | 72 | **0 — a POINT** | 2T is **forgotten** |
| **subregular** | **(2,2,2,0,2,2)** | **70** | **2 — a SURFACE = ℂ²/2T** | **2T is returned** |
| the other 28 | — | — | neither 0 nor 2 | — |

> **Exactly one orbit of the thirty returns 2T. It is the subregular.**

And its 27-decomposition — **read off after the selection, never used to make it** — is
**13 + 9 + 5**: three nontrivial odd summands, no trivial one, hence (B1256's addendum, computed on
bench) **h¹ = 3, ALL CHIRAL**.

## What this claims, and what it does not

**Claims:** a **canonical, unique, non-fitted** criterion selecting exactly the embedding that yields
three chiral generations — replacing an unexamined default that has **no attachment whatever to the
object's own 2T**. Both orbits are intrinsically defined in E₆; what distinguishes the subregular is
a **closure condition** (its slice geometry reproduces the input datum), not an aesthetic preference.

**Does NOT claim:** that the object's holonomy realises this embedding. That step — exhibiting the
object's SL(2) landing in the subregular orbit — is what would earn the row. **I-25 stays UNEARNED**;
this is registered as a **candidate route**, with the map exhibited and its remaining gap named.

**It also does not need I-6.** The unearned row *π₁(m004) ↠ 2T ≡ the 6d type's ALE Γ* (B1228) is a
different, geometric claim. This argument uses only **I-1** (EARNED) plus the internal coherence of
the ADE correspondence — McKay's Γ and Du Val/Brieskorn's Γ are the two standard faces of one
classification, not two structures glued.

## THE FENCE — what here is verified, and what is cited

**Verified on this bench (exact, controlled):** every dimension in the table (dim g = 78, rank 6,
dim N = 72, each orbit dimension, `dim(S ∩ N) = dim N − dim O`); the **uniqueness** of the dim-70 row
across the 30-labelling superset; the 27-decompositions; and — via **B1256's addendum, computed by
Fox calculus on m004** — that 13+9+5 types h¹ as three chiral.

**CITED, NOT VERIFIED ON BENCH — the one load-bearing citation:** **Brieskorn–Slodowy**, that for a
simple Lie algebra of type ADE the transverse slice to the **subregular** orbit meets the nilpotent
cone in a simple surface singularity **of the same ADE type** — together with the Kleinian
classification's **E₆ ↔ 2T**. Both are standard (Brieskorn 1970; Slodowy 1980; Du Val/Klein), and the
second is the same 2T that McKay attaches to E₆ (I-1, EARNED) — the two faces of one classification,
not two structures glued. **But this seat has not reproduced the theorem**, and per the programme's
own *cited ≠ verified* rule the arc is fenced accordingly: **what is computed here is that the
subregular is the unique orbit with a surface slice; that this surface IS ℂ²/2T is taken from the
literature.**

Nothing downstream may treat the Brieskorn step as bench-verified until it is.

## Controls (MB12, both directions)

- **THE DECISIVE ONE:** the criterion is computed from **dimensions alone**, with **no reference to
  the 27's decomposition**; the three-chiral reading is taken afterwards. The selection could not
  have been fitted to the answer.
- **The criterion can fail, and mostly does:** **28 of 30** orbits give neither a point nor a surface.
- The orbit-dimension formula is validated against the known regular orbit (**72**).
- The root system is rebuilt independently (**72** roots).

## Verification

`verification/brieskorn_selection.py` — standalone.

- **Feeds on:** B1256 (I-25 and the four candidates), B1255, B327 (where the assumption entered),
  B266/B727 (I-1, McKay EARNED), B883 (the 27), B1112 (the holonomy).
- **Registers:** a named route on **I-25** (still UNEARNED).

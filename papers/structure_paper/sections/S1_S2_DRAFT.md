# §1–§2 — DRAFT v1

*Genesis-first paper. Gate 5 stands: no physics identification is made in the body.
Terminology per `TERMINOLOGY_POLICY.md`. Every numbered claim carries its registry row.*

---

## §1. Introduction

Fix a principle: **a description that cannot terminate**. Ask what the least such
description looks like, follow the answer without importing anything from outside, and
record what it costs.

This paper carries out that programme and reports both halves of the result. From the
principle, with **three declared choices whose alternatives we compute**, one reaches a
specific hyperbolic 3-manifold — the figure-eight knot complement. Its own arithmetic then
determines a 78-dimensional exceptional Lie algebra with a distinguished four-element
charge torus, and a cascade of centralizers of that torus terminates, exactly, at
`su(3) ⊕ su(2) ⊕ u(1)³` with the global form `[SU(3)×SU(2)×U(1)]/ℤ₆` *(registry G18;
`tests/test_b862_global_form.py`)*. **No measured quantity enters any computation at any
point.**

The second half is the part we ask the reader to weigh equally. The same construction is
**provably silent** about magnitudes: the object's amphichirality forces its Chern–Simons
invariant to vanish, and the vanishing deletes the only term in its action that could carry
a scale. Five predictions derived from the construction were sealed in advance and compared
against measurement; **all five missed**, and the surface of comparisons the construction
licenses was subsequently **enumerated and found exhausted** *(registry N5, N6; B1063,
B1066)*. We state these results in §9
with the same weight as the positive ones, because a construction that reaches structure
and cannot reach magnitude is a different object from one that has not yet reached
magnitude, and only the first is what we claim.

### 1.1 What is claimed

> **A cost theorem.** Three declared choices, no fitted parameters, and no measured input
> yield the structural data listed in §§6–8.

We do **not** claim a derivation of physics. Internal names for mathematical objects
(`measurement`, `charge`, `matter`) are defined at first use and collected in Appendix C;
nothing in the body asserts a physical interpretation of them.

### 1.2 What is unusual, stated plainly

Of the 43 links in the chain, **39 are theorems, identities, censuses, or no-go results**;
**four are declared choices**. Three of the four occur **before** the manifold appears, and
one occurs after the algebra is already in hand. **Between the manifold and the algebra
there is not one declared choice** (§5.5).

### 1.3 What the reader should be suspicious of

Two things, and we address both where they arise rather than in a discussion section.

**First**, reaching this particular exceptional algebra is *generic*: roughly one hyperbolic
3-manifold in three, and five of seven grammars in the relevant family, arrive at it.
**Arrival there is therefore not evidence.** What is not generic is the *entrance* — §5.4.

**Second**, the cost claim is a claim about what entered the computations, and the reader
cannot check that by reading prose. **Appendix B supplies one runnable verification per
numerical claim**, and every claim in the body carries a pointer to the computation that
establishes it.

---

## §2. The principle and its price

### 2.1 The principle

We take as our starting point that **description is inexhaustible**: no finite description
closes. The mathematical content we draw from it is a minimality condition, developed in
§3. The metaphysical content is a choice, and we price it below.

### 2.2 Three declared choices

The construction makes exactly three declarations before the manifold appears. For each we
computed the alternative and record what it yields. **A declared choice whose alternatives
are not computed is a free parameter wearing a different name**, so we treat the
computations as part of the claim rather than as commentary.

**(C3) Description is inexhaustible.** The one metaphysical commitment.
*Price.* Both alternatives degenerate. The periodic counterpart collapses: the whole
`det = +1`, `|tr| ≤ 2` family is finite-order or reducible — no pseudo-Anosov element, no
hyperbolic carrier. Variants of the shadow rule likewise degenerate or become conjugate to
the original. **Neither alternative supports the construction at all.** *(Registry G3;
`tests/test_b749_genesis_forks.py`, `tests/test_b749_f2_f8_locks.py`.)*

**(C4) The word is realized on the once-punctured torus.** A geometric carrier is chosen
over combinatorial ones.
*Price, and it is the consequential one.* The canonical non-geometric carriers — the tiling
hull, and the Effros–Shen algebra with `K₀ = ℤ[φ]` — see only the real quadratic data. All
four pre-registered redundancy witnesses fail exactly: in particular `x² + 3` remains
irreducible over `ℚ(√5)`. **The imaginary quadratic field `ℚ(√−3)` is bought at
geometrization and nowhere earlier.** Every arithmetic consequence in §4 and §5 depends on
this choice. *(Registry G4; `tests/test_b749_f2_f8_locks.py`.)*

**(C5) The monodromy is taken orientation-preserving.** Equivalently, the golden slope is
squared.
*Price, and it is the largest.* **The discarded alternative is not degenerate.** It is the
Gieseking manifold — the orientation double cover's parent of the manifold we keep, with
dilatation `φ` upstairs against `φ²` below. **A reader who prefers the parent to the child
obtains a different, perfectly good object, and the construction below does not apply to
it.** *(Registry G5; `tests/test_b749_genesis_forks.py`.)*

### 2.3 The asymmetry among the three

The three are not equally costly, and we do not present them as though they were.

| choice | status of the alternative |
|---|---|
| **C3** | degenerates — no carrier exists |
| **C4** | survives, but sees only the real quadratic data; the imaginary quadratic field is lost |
| ## **C5** | ## **survives intact as a named manifold** |

**C5 is the honest scar in the argument.** It is a fork between two genuine objects, decided
by a stipulation, and no computation in this paper forces the choice. We flag it here rather
than in a limitations section because a reader who discovers it late is entitled to distrust
everything before it.

### 2.4 What is *not* declared

No numerical value is declared anywhere. The construction contains **zero fitted
parameters** in the ordinary sense: no quantity was tuned to data, and no measured number
enters any computation reported in §§3–8. This is an auditable claim, not a stylistic one,
and Appendix B is where it is audited.

*(One clarification, since the phrase invites it: this is a statement about **inputs to the
derivation**. It is not a statement that the construction reproduces measurements — §9
reports that it does not, and why it cannot.)*

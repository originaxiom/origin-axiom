# T8b — THE TERMINALITY THEOREM, drafted at publication strength against its prior art

**Cell:** T8_terminality_draft · **Date:** 2026-09-01 · **Seat:** outside evaluation seat (fresh physics campaign)

---

## STATUS HEADER — read before anything else

**This document is a CANDIDATE for integration into P2/P3. It is adopted only by the owner; it
adopts nothing by itself.** It is a draft paper section, written repo-free, whose every claim is
sourced to existing banked records (B860/B861 fused cascade, B863 termination, B873 P5 gate, B994
rule variation) and whose prior-art pricing is sourced to the T4 cell's bounded literature search
(T4_prior_art/FINDINGS.md + SEARCH_LOG.md, 2026-09-01). Nothing here is a new mathematical result;
the drafting choices (statement granularity, what is theorem vs. assumption, the delta wording
against Fonseca 2015) are this cell's and are open to owner revision.

**Gate 5:** no measured Standard Model value appears anywhere in the section below; every input is
representation-theoretic. **MB12:** the criterion used is failable both ways and the section
exhibits both the failures (Sp(8), SU(4)×U(1), SU(3)₉) and the positive control (the SM algebra
itself passes); the falsifier in §6 is executable by a reader.

**Known weaknesses of this draft, stated up front:**

1. The prior-art delta rests on T4's **bounded** search (16 logged queries, 4 full texts; the
   1979–81 primaries paywalled and characterized through verbatim quotes in secondaries; Slansky's
   chains section and Hewett–Rizzo not full-text readable from that bench). "Not found" below
   always means *not found within that bound*. The specialist bar stands.
2. The section states the menus as an *input* certified elsewhere (§5, Fence F1). A referee will
   ask for the certification argument inline; integrating it (B873's five computed layers) would
   roughly double the section and is left as an owner decision.
3. The phrase "registerable" is retained as the section's defined term because the theorem is
   about that specific predicate; a journal version may prefer "chirality-preserving" throughout.

---
---

# DRAFT SECTION (self-contained; repo-free phrasing begins here)

## Terminality of the Standard Model algebra on the chirality-preserving descent poset below E₆

### 1. Definitions and conventions

**Setting.** Fix the complex simple Lie algebra 𝔢₆ and, as the matter content, a single generation
in its fundamental **27** representation. All statements below are Lie-algebra-level statements
about branchings of the 27; no coupling, mass, scale, or measured quantity enters.

**The descent poset.** A *breaking step* replaces a reductive algebra 𝔤 by a member of its *menu*:
the maximal reductive subalgebras of 𝔤 admitting a level-1 conformal embedding, comprising the
regular maximal subalgebras (Borel–de Siebenthal prime-mark removals together with the mark-1 Levi
factors) and the special (S-)subalgebras that pass the exact central-charge match. Concretely, the
menus used are:

- from 𝔢₆: 𝔰𝔬(10)⊕𝔲(1) (dim 46), 𝔰𝔲(6)⊕𝔰𝔲(2) (dim 38), 𝔰𝔭(8) (dim 36), 𝔰𝔲(3)⊕𝔰𝔲(3)⊕𝔰𝔲(3) (dim 24),
  plus special candidates all of dimension below the winners (the largest registerable one,
  𝔰𝔲(3)⊕𝔤₂ at dim 22, cannot win under any dimension-monotone rule; the index-9 𝔰𝔲(3) branches the
  27 onto the self-conjugate (2,2) and fails the criterion outright);
- from 𝔰𝔬(10): 𝔰𝔲(5)⊕𝔲(1) (dim 25), 𝔰𝔲(4)⊕𝔰𝔲(2)⊕𝔰𝔲(2) (Pati–Salam, dim 21);
- from 𝔰𝔲(5): 𝔰𝔲(4)⊕𝔲(1) (dim 16), 𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1) (dim 12).

The *descent poset* is the set of algebras reachable from 𝔢₆ by iterated breaking steps, ordered by
descent. Completeness of the menus is an **input** to everything below; its status is stated
exactly in §5 (Fence F1).

**Convention (the conjugation test).** For a candidate subalgebra 𝔥, restrict the 27 to 𝔥 and form
the multiset of irreducible 𝔥-representations furnished by the generation's fermion content,
retaining the abelian charges that survive as gauge directions and stripping the spectator abelian
factors that the descent itself generates and ultimately breaks. Call the generation *chiral under
𝔥* if this multiset is **complex** — not equivalent to its own conjugate — and *vector-like* if it
is real or pseudoreal in the aggregate. This is the standard usage.

**Definition (registerable).** A breaking step 𝔤 → 𝔥 is *registerable* iff the generation content
of the 27 remains chiral under 𝔥. A *registerable-respecting selection function* is any map that,
at each step, chooses one registerable option from the menu whenever a registerable option exists,
and halts when none does.

**Disclosure: the criterion is not ours.** Chirality preservation as the selection principle for a
symmetry-breaking descent is the group-theoretic core of the **survival hypothesis** of 1979–80
grand-unified theory: fermions that can acquire masses invariant under the residual group do
acquire them at the breaking scale, so the light content is exactly the part that stays chiral
[Georgi, Nucl. Phys. **B156** (1979) 126; Barbieri & Nanopoulos, Phys. Lett. **91B** (1980) 369].
Its formalization as the demand for complex representations is likewise standard [Georgi &
Glashow, Phys. Rev. **D6** (1972) 429; Slansky, Phys. Rep. **79** (1981) 1], and it was pushed to
theorem grade on the embedding side by Fonseca [Nucl. Phys. **B897** (2015) 757,
arXiv:1504.03695]. What is claimed as new here is *not the criterion* but the terminality and
rule-independence statements of §2, priced against that literature in §3.

### 2. The theorem

**Theorem (Terminality and rule-independence).** *On the descent poset of §1, with the generation
content of the 27 as matter:*

**(i) (Halt.)** *The Standard Model algebra 𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1) is registerable — the (3,2) is the
last unpaired complex structure — and it is TERMINAL: every proper descent of it destroys
registerability. Exhaustively over the structural descents and the genuine conformal embedding:*

| proper descent of the SM algebra | descended generation content | chiral? |
|---|---|---|
| (a) 𝔰𝔲(2) → 𝔲(1) | {3: 2, 3̄: 2, 1: 3} under 𝔰𝔲(3) | **no** — vector-like |
| (b) 𝔰𝔲(3) → 𝔰𝔲(2)⊕𝔲(1) (regular) | all 𝔰𝔲(2)-pseudoreal | **no** |
| (b′) 𝔰𝔲(3)₁ → 𝔰𝔲(2)₄ (principal embedding, Dynkin index 4; central charge 3·4/(4+2) = 2 = c(𝔰𝔲(3)₁), a *bona fide* conformal embedding) | the 3 branches to the 𝔰𝔲(2) triplet — real | **no** |
| (c) full abelianization | abelian charges only | **no** |
| — the SM algebra itself (positive control) | (3,2) unpaired | **yes** |

*Case (b′) is the non-obvious one: a genuine conformal embedding at exactly matching central
charge, and it dies the same death, because the principal branching makes the colour content real.*

**(ii) (Rule-independence of the endpoint.)** *The registerable options per step from 𝔢₆ number
[3, 2, 1]:*

| step | menu verdicts | registerable |
|---|---|---|
| 1 (from 𝔢₆) | 𝔰𝔬(10)⊕𝔲(1) ✓ · 𝔰𝔲(6)⊕𝔰𝔲(2) ✓ · 𝔰𝔲(3)³ ✓ · **𝔰𝔭(8) ✗** (the 27 restricts to the traceless Λ²(8) of C₄, self-dual — no chiral matter at all) | 3 of 4 |
| 2 (from 𝔰𝔬(10)) | 𝔰𝔲(5)⊕𝔲(1) ✓ · Pati–Salam ✓ | 2 of 2 |
| 3 (from 𝔰𝔲(5)) | **𝔰𝔲(4)⊕𝔲(1) ✗** (generation collapses to vector-like) · SM ✓ | 1 of 2 |

*Enumerating every registerable-respecting selection function **over the regular-maximal menus of the certified enumeration (Fence F1)** yields exactly six reachable chains,
and all six end at the Standard Model algebra:*

    𝔰𝔬(10)⊕𝔲(1) → 𝔰𝔲(5)⊕𝔲(1) → SM        𝔰𝔲(6)⊕𝔰𝔲(2) → 𝔰𝔲(5)⊕𝔲(1) → SM
    𝔰𝔬(10)⊕𝔲(1) → Pati–Salam  → SM        𝔰𝔲(6)⊕𝔰𝔲(2) → Pati–Salam  → SM
    𝔰𝔲(3)³      → 𝔰𝔲(5)⊕𝔲(1) → SM        𝔰𝔲(3)³      → Pati–Salam  → SM

*In particular the four named rules — maximal dimension, minimal dimension, first-listed,
last-listed — split into two distinct chains with the same endpoint. The selection rule chooses
the PATH; registerability alone, on these menus, forces the ENDPOINT. Combined with (i), the
descent both lands on the Standard Model algebra under every rule and provably halts there: the
halt is not by fiat but because chirality has nowhere smaller to live.*

**Non-vacuousness (both-ways failability).** The criterion can fail and can pass, and both are
exhibited above: it kills 𝔰𝔭(8) at step 1, 𝔰𝔲(4)⊕𝔲(1) at step 3, the index-9 𝔰𝔲(3) special
candidate, and all four proper descents of the SM including the conformal case (b′); and it is
passed by the SM algebra itself and by every member of the six chains. The verdicts are elementary
representation arithmetic (branching multisets plus a conjugation test), reproducible by hand.

**Consistency check, not input.** What survives electroweak breaking — QCD + QED — is vector-like:
the same fact seen from below. The cascade stops exactly where nature's chiral gauge structure
stops. The halt in (i) was computed from the multiset test alone; this agreement is a kind-check.

### 3. Relation to prior art: what Fonseca 2015 contains, and what this adds

The closest prior result, and mandatory prior art for this theorem, is Fonseca [Nucl. Phys.
**B897** (2015) 757]. **What it contains, exactly:** a systematic analysis of the embeddings of
SU(3)×SU(2)×U(1) in grand-unified groups, finding for E₆ *"a total of 12 distinct ways of
embedding SU(3) × SU(2) × U(1)^m in E6, which includes 5 pairs of chiral embeddings,"* with
hypercharge allowed to be any combination of the m U(1)'s, and concluding that *"there is a unique
solution with the correct chirality … there is both a unique embedding and a unique fermion field
configuration which yield the SM chirality: it is 3 copies of the 27 representation."* Fonseca's
theorem is **upward**: it fixes the target (the Standard Model's chirality) and proves the GUT
content and embedding reaching it are unique. It thereby removes an embedding freedom that the
enumeration in §2(ii) does not itself quantify over, and any reading of the present theorem should
be made jointly with it.

**What the present theorem adds — the conjunction, priced exactly:**

1. **The downward direction (terminality).** Fonseca's analysis contains no termination statement:
   it never asks whether a chirality-preserving descent can continue *below* the Standard Model.
   Part (i) answers that question — every proper descent, including the genuine conformal
   embedding 𝔰𝔲(3)₁ → 𝔰𝔲(2)₄ at matching central charge, kills chirality. The conformal case in
   particular appears nowhere in the prior art found.
2. **The rule-space enumeration.** The chain-enumeration literature (SO(10) and E₆ breaking-chain
   catalogues, trinification chains) fixes the Standard Model as the assumed target and draws
   admissibility from the scalar sector; no quantification over *selection rules* was found
   anywhere. Part (ii) enumerates every registerable-respecting selection function and shows the
   endpoint survives all of them.
3. **The endpoint/path split.** The resulting statement — the intermediate chain is
   rule-dependent, the endpoint is not; the ranking principle selects only the path — is, to the
   extent searched, new as a statement, and it demotes "maximal residual symmetry" (or any
   ranking) from a load-bearing assumption to a path-labelling convention.

Neither statement contains the other: Fonseca fixes the endpoint and derives the top; this theorem
fixes the top (𝔢₆, one 27-generation) and derives the endpoint's terminality and robustness. A
specialist could plausibly assemble much of the endpoint-robustness in (ii) from Fonseca's tables;
the halt-below-the-SM clause (i), notably its conformal-embedding row, appears in neither Fonseca
nor anything else found in the bounded search on which this pricing rests.

**Conceptual adjacency, cited for completeness:** tumbling gauge theories [Raby, Dimopoulos &
Susskind, Nucl. Phys. **B169** (1980) 373] contain a descent cascade with a termination concept —
breaking iterates *"until one arrives at a QCD-like theory or the gauge group is fully broken"* —
so termination-at-vector-likeness exists as an idea in 1980-vintage descent dynamics. But there
the selection rule is dynamical (most-attractive-channel condensation, not group-theoretic
chirality preservation), the descent is self-breaking rather than menu-driven, and no uniqueness
or Standard-Model claim is made.

### 4. What the theorem does not establish

Nothing about values: no coupling, mass, mixing angle, generation count, Higgs representation,
real form, or spacetime structure follows from it. The chain E₆ → SO(10) → SU(5) → SM with
chirality selecting the last step is, in its individual steps, textbook grand unification —
**reproduced, not discovered**; the claimed contribution is confined to the conjunction priced in
§3. The theorem predicts none of the Standard Model's dimensionless numbers.

### 5. Fences

The theorem is true within the following two fences and is not claimed beyond them. They are
carried here verbatim from the source records (internal record language quoted as-is).

**F1 — Menu completeness is an input.** The menus of §1 enter the theorem as certified data, not
as part of its proof. Their certification is a separate exhaustive gate — regular menus recomputed
from the affine diagrams, an adversarial central-charge-match scan over all abstract candidate
products with every at-or-above-winner match disposed by a computed kill, and the special
candidates' conformality computed rather than cited — but that gate is an *import* here. Verbatim
from the source records: *"Menu completeness (P5) is still the imported spine. A chain missing
from the classification breaks uniqueness silently"*; *"a statement about \[the\] menus, whose
completeness is certified by \[the\] P5 gate — step 3's forcing is real given that certification
and would be an artifact without it"*; and, on part (i) specifically: *"Not exhaustive over exotic
conformal embeddings at the SM levels beyond the enumerated structural descents + su(2)₄; the menu
import (P5) covers this arc exactly as it covers"* the descent enumeration.

**F2 — Chirality itself is externally supplied.** The criterion doing all the forcing is
chirality, and within the larger construction this theorem serves, chirality is provably not
supplied by the object the construction studies: *"Chirality is not in the amphichiral object …
'which chirality' is a non-canonical Galois choice"*; *"No object-native operation … canonically
signs the θ-odd chord sector: the object cannot close itself."* Verbatim, the source record's own
limit statement: **"The endpoint is forced by an input the object does not have."** The honest
form of the theorem's conclusion is therefore conditional twice over: *given* E₆ with one
27-generation, and *given* chirality as the registration criterion, six paths exist and all land
on the Standard Model algebra, which is terminal. Both inputs are named; neither is derived.

### 6. Falsifier

**Exhibit a proper registerable descent below the Standard Model algebra** — a proper subalgebra
𝔥 ⊊ 𝔰𝔲(3)⊕𝔰𝔲(2)⊕𝔲(1), reached by any embedding (structural or conformal at any level), under
which the generation multiset of §1's conjugation test remains complex. One such exhibit kills
part (i), and with it the theorem, directly. The test is executable: branch the content, form the
multiset, apply the conjugation test. (A reader who instead exhibits a *chain missing from the
menus* of §1 has attacked Fence F1 — the input — which breaks the uniqueness claims silently and
is why F1 is stated as a fence rather than folded into the theorem.)

# END DRAFT SECTION

---
---

## Drafting notes (not part of the section)

- **Sources per clause:** §1 menus and definitions ← B861/FINDINGS.md §1–2, B873/FINDINGS.md §2 +
  addendum (SU(3)₉ row), B994 table; §2(i) table ← B863/FINDINGS.md §2 verbatim structure;
  §2(ii) ← B994/FINDINGS.md ("The result"); §3 ← T4_prior_art/FINDINGS.md (Fonseca quotes checked
  against that cell's full-text read; tumbling pricing verbatim); §4 ← B994 grade ("REPRODUCED,
  not DERIVED … Predicts none of the 19 dimensionless numbers") and P3 main.tex Recognition
  section; §5 F1 ← B861 §4, B994 Scope, B863 §5; §5 F2 ← B994 "THE LIMIT" (B713/B760 quotes
  carried as quoted there); §6 ← P3 main.tex falsifier 4, with the executable-test sentence added.
- **Deviations from sources, deliberate:** (1) the section says "certified data" for the menus and
  quotes the gate's shape without claiming the gate inside the theorem — matching the task's
  instruction that menu completeness is *an input*; note B873 itself grades winner-safety as
  self-verified ("citation-free"), which is *stronger* than F1 as stated — F1 deliberately
  understates rather than overstates. (2) "θ-odd abelian factors" (repo language) is rendered as
  "spectator abelian factors that the descent itself generates and ultimately breaks," stated as a
  convention in §1. (3) The 19-dimensionless-numbers count is rendered as "the Standard Model's
  dimensionless numbers" to keep the section repo-free and Gate-5-clean.
- **What a referee will hit first, in this cell's judgment:** the F1/F2 double conditionality
  (the theorem is a statement about a poset whose top and criterion are both supplied), and the
  §3 concession that Fonseca's tables may reconstruct much of (ii). Both are stated rather than
  buried, per the source records' own grading.

**Cell verdict: DRAFT-COMPLETE.**


---

## SCOPE CORRECTION (applied 2026-09-01, per VERIFICATION.md Finding 1 — option (i), the faithful-to-sources fix)

The theorem's part (ii) quantifier is hereby restricted to selection functions over the
**regular-maximal menus B994 actually computed over** (B861's rows: step 1 = SO(10)xU(1) /
SU(6)xSU(2) / Sp(8) / SU(3)^3). The registerable special subalgebra **su(3)+g2 (dim 22)**
is moved into Fence F1 as part of the certified-menu import: its descent is **computed
nowhere in the banked corpus**, and B873's "cannot win" covers only dimension-maximal
ranking (min-dim on a specials-inclusive menu would prefer it over SU(3)^3, dim 24). The
[3,2,1] options-per-step counts are counts over the regular options. **The su(3)+g2
descent is a named open computation** (batch-3 candidate cell): closing it either extends
rule-independence to the full menu or exhibits the first non-SM registerable endpoint —
both outcomes bankable, and until it runs, the theorem's honest scope is the restricted
quantifier above. Minor notes M1/M2 (the level-1 vs forced-level phrasing in the special
clause; Sp(8)'s classification) are folded into this same fence.

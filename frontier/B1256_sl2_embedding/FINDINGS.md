# B1256 — WHICH sl₂? The principal embedding was never derived; four embeddings type h¹ = 3 as three chiral, and exactly one of them needs no unverified assumption: the subregular E₆(a₁)

**Date:** 2026-09-05 · **Seat:** cc · **Status:** PROVED (exact; five MB12 controls, one of which convicts this arc's own first criterion)

## The question

B1253 priced the generation count, and the price was a **typing**, not a count:

> COUNT matches: 3 = 3. TYPES do NOT: the object gives **1 abelian + 2 chiral**; the SM needs 3 chiral.
> To earn it: a mechanism making the trivial summand chiral, **OR a bundle whose three classes are all chiral**.

**B1255** closed the other route permanently (three generations cannot live inside one 27: the 16 has
multiplicity one, three copies need dim ≥ 48 > 27). So the second disjunct is all that is left.

## The observation

The "1 abelian" is the **trivial Sym⁰** in `27 = Sym¹⁶ ⊕ Sym⁸ ⊕ Sym⁰`, and that decomposition is
taken with respect to the **principal** sl₂ — **a choice never derived.** B1112 pins the object's
canonical holonomy as **PSL(2,ℂ)** with an SL(2,ℂ) spin lift; the **embedding of that SL(2) into
E₆** was assumed principal, being the natural choice for an irreducible SL(2). By
**Menal-Ferrer–Porti**, dim H¹ = 1 per **nontrivial odd**-dimensional symmetric power — so the
**typing of h¹ depends entirely on the embedding**, and nobody had varied it.

## The computation, and the completeness that makes absence meaningful

All 3⁶ = 729 weighted Dynkin labellings c ∈ {0,1,2}⁶; h defined by α_j(h) = c_j; the 27 decomposed
into sl₂ strings. **30** are integral on the 27. The enumeration is **complete over sl₂
subalgebras**, so absence from it is non-existence, not failure to identify:

- **Jacobson–Morozov** — every sl₂ subalgebra corresponds to a nilpotent orbit;
- **Dynkin** — its h is conjugate to a dominant h with α_i(h) ∈ {0,1,2}, so all 729 are covered;
- h acts on the 27 (an sl₂ rep) with **integer** eigenvalues → the 30 integral rows;
- E₆ has 21 nilpotent orbits, so the 30 rows are a **superset**.

**Independent validation of the machinery:** the principal labelling returns sl₂ index **156** via
the 27, reproducing **B1242's banked Dynkin index** — and the orbit-dimension formula returns **72**
for it, the known regular orbit.

## The result — stated with the criterion that is actually correct

h¹ counts **nontrivial odd**-dimensional summands (one each); **trivial** summands contribute
abelian H¹. **Even-dimensional (Sym^odd) summands are not PSL(2,ℂ) reps** — they need the spin lift,
and what they contribute to h¹ is **not settled by the banked form of MFP**, which covers the
nontrivial odd case only.

| labelling | 27 = | dim O | even-dim summands | h¹ types as |
|---|---|---|---|---|
| principal (2,2,2,2,2,2) | 17 + 9 + 1 | 72 | 0 | 2 chiral + 1 **abelian** ✘ |
| **subregular (2,2,2,0,2,2)** | **13 + 9 + 5** | **70** | **0** | **three chiral ✔ — assumption-free** |
| (1,0,1,1,1,1) | 8 + 7 + 5 + 4 + 3 | 64 | 2 | three chiral, *conditional* |
| (1,1,1,0,1,1) | 7 + 6 + 5 + 4 + 3 + 2 | 62 | 3 | three chiral, *conditional* |
| (1,0,1,0,1,1) | 6 + 5 + 4 + 4 + 3 + 3 + 2 | 58 | 4 | three chiral, *conditional* |

> **FOUR** labellings give three nontrivial odd summands with no trivial one. Three of them carry
> even-dimensional summands and therefore rest on the **unverified** assumption that those contribute
> 0 to h¹. **The subregular is the only candidate that needs no assumption about the even-dimensional
> case, because it has none.** That — not a bare count — is what distinguishes it.

**This arc's own first criterion was wrong and is convicted by its own control.** "Exactly three
summands total" reports **1** hit where the correct criterion reports **4**; even-dimensional
summands ride along freely. The selftest runs both and asserts the discrepancy, so the error cannot
silently return.

**And the identical-summand question, restated correctly:** **9 + 9 + 9 does not exist in E₆** —
non-existence, by the completeness argument above. But **three identical nontrivial odd summands DO
exist**: `(0,2,0,2,0,0)` gives **7 + 7 + 7** — with **six trivial riders**, so h¹ = 3 chiral + 6
abelian = **9**, not 3. (An earlier draft asserted no such decomposition existed; that was false.)

## What this claims, and what it does not

**It does NOT derive three generations.** It converts B1253's open wish into a **single decidable
question** — *which sl₂ embedding does the object supply?* — with a **short, explicit candidate list**
and one distinguished member.

**Registered as an UNEARNED INPUT (I-25).** Every h¹ typing in the corpus rests on the embedding
choice. Per **B1231**, an unearned identification is an unpriced observer input, so the input
ledger's parameter count is a **lower bound** until it is earned. Naming it **raises** the UNEARNED
count 9 → 10 — a documented raise, the ratchet behaving exactly as designed: a previously invisible
input becomes visible and priced rather than assumed.

**Open, and named:** what H¹(M; Sym^odd) contributes for the spin-lifted holonomy. Settling it either
promotes the three conditional candidates to live ones or eliminates them, and it is a literature
question about the MFP theorem's even-dimensional case, not a computation on this bench.

## Controls (MB12, both directions)

- **The orbit-dimension formula is validated against a known answer:** principal returns **72**.
- **The Dynkin index is validated against banked work:** principal returns **156** = B1242's.
- **The root system is rebuilt independently:** exactly **72** roots.
- **The criterion can fail, and mostly does:** the full summand-count distribution is reported.
- **This arc's own superseded criterion is run and shown wrong** (1 vs 4).

## Verification

`verification/sl2_embedding.py` — standalone, no cache needed.

- **Feeds on:** B1253 (the price), B1255 (the other route closed), B1112 (holonomy is PSL(2,ℂ)),
  B1242 (the banked index 156), B883 (the 27), Menal-Ferrer–Porti.
- **Registers:** I-25 **UNEARNED** (documented raise 9 → 10).

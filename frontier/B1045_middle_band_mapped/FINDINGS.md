# B1045 — the instrument's first measured miss, and why the middle band is MAPPED and not dispositioned

**Date:** 2026-08-11 · **Lane:** the consolidation refresh — the middle bands. Gate 5 untouched;
zero anchors; nothing to `CLAIMS.md`.
**Files:** `verify.py` → `results.json` (12 checks) · lock `tests/test_b1045_middle_band.py`.

Two results, one of each kind: the new gate **worked and was measured to be incomplete**, and the
band it was pointed at **is not dispositioned, on purpose**.

---

## 1. THE POSITIVE — and it is a miss

**B1044's `law-siblings` gate was used against a band it had not seen, and caught nothing.** Then a
row read by eye turned out to be a law this refresh had already restored:

> **B485** — *"the metallic Alexander law `Δ_m(a) = a² − (m²+2)a + 1`"* — **is B1040's metallic
> degree in another vocabulary.** `Δ_m` is the **characteristic polynomial of `M_m²`**, whose root
> is `λ_m²`. Verified identical symbolically. *The Alexander polynomial of a fibered bundle **is**
> its monodromy's characteristic polynomial.*

**None of the four fingerprints matched a single term of it** — verified against the pre-widening
patterns. B1040's read `isomonodrom|Painlev|Schlesinger|Vieta|Jimbo|Fricke cubic`; B485 speaks
Alexander polynomials.

**Fixed, and the limitation stated rather than papered over.** The fingerprint is widened, the gate
now fires, B485 is consolidated onto the isomonodromy row. And the registry now records what this
instrument **cannot** do:

> **A fingerprint catches restatements in the SAME vocabulary; a genuine TRANSLATION between
> vocabularies escapes it.** This is **not fixable by adding terms**, only mitigated — every
> widening is a guess at the next synonym. What it reliably catches is the case that bit (**B564**:
> *same words, different band*); what it will keep missing is a re-derivation in another field's
> language.

*That is the honest argument for L164's larger option: a topic-wise disposition reads **bodies**,
not fingerprints.*

## 2. THE NEGATIVE, WHICH IS ABOUT METHOD — the band is MAPPED

**69 debt rows in B300–B499**, the heaviest stretch in the corpus. A keyword pass over their claim
lines groups them into **7 candidate clusters + 11 standalone**.

**That is published as a MAP, not a disposition**, and the distinction is load-bearing: B1037
dispositioned B100–B199 **by reading the bodies**, and campaign **step 1 forbids** claim-line
reading as a basis for disposition. **Calling this a disposition would be the very defect the
method exists to prevent.**

**The map's error rate is measured, not assumed: 5 of 58 (9 %).**

| arc | filed under | belongs to | why |
|---|---|---|---|
| **B345** | E₆ selection | generations / deviation | its claim line ends *"**independent of** the E6-exponent grading"* |
| **B316** | metallic laws | arithmetic selection | it says √−7 is *"**NOT** a metallic-ladder member"* |
| **B346** | E₆ selection | generations / deviation | E₆ is the contrast, not the subject |
| **B423** | E₆ selection | zeta / torsion | the statement is a zeta closed form |
| **B435** | E₆ selection | the (5,1) child | it is the child's `H₁` and vacuum count |

> ### Step 1's argument, made concrete: a claim line's **keywords** can be exactly the words an arc uses to say **what it is not**.
>
> A keyword sweep files **B345** under the grading it declares itself independent of, and **B316**
> under the ladder it declares itself not a member of.

**The other 53 assignments are unverified** — hypotheses until a body is read. Stated so the next
pass starts from evidence with its confidence attached, rather than inheriting a table that looks
like a result.

---

**Verdict: PROVED.** 12 checks.

**Self-correction, caught by this arc's own check.** The first draft said **three** of the five
misassignments were explicit denials. **B346 merely *contrasts* with E₆ rather than denying it** —
the check asserted `len(denials) >= 3`, failed, and the count is corrected to **two** here, in the
ledger, and in the arc. *A check written to make a point about overcounting caught an overcount in
the sentence making the point.*

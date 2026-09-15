# MEMO 153 — THE CURRENCY PASS ON THIS BENCH'S OWN GAP DOCUMENTS

**Banked 2026-08-30.** Seal `seals/GAP_DOCS_CURRENCY_PREREG.md`, pushed before retrieval.
Certificate `certificates/gap_docs_currency.py`. Subject: `THE_TOE_GAP.md`,
`THE_FULL_ACCOUNTING.md`, `THE_GRAND_TABLE.md` (all 2026-08-28) against main at `89affd5b`.

---

## 0. OUTCOMES

| cell | outcome |
|---|---|
| **E1** — are the open items still open? | **E1-SYSTEMIC** — 6 of 13 need correction, and **2 were stale on the day they were written** |
| **E2** — was anything called delivered later reopened? | **E2-NONE**, on the checks I could run (limit stated in §5) |
| **E3** — are post-08-28 absences carried? | **E3-INCOMPLETE** |
| **E4** — do the three documents agree? | **E4-DIVERGENT** — and the worst divergence is **inside one document** |

**And the finding that subsumes the rest: the corpus already had an instrument for this, and I did
not run it.** `B1202` — *"THE ALREADY-BANKED CHECK — the finished-but-forgotten class gets an
INSTRUMENT, not a promise"* — ships `89affd5b:scripts/checks/already_banked.py` and installed a
**WORKING_RULES** rule: *"no MISSING/OPEN/'never run'/'no successor' claim is admissible until the
check has been run on its terms, and the SEARCHED TERMS ARE STATED WITH THE CLAIM."* My three
documents assert dozens of MISSING claims and state no searched terms. **I have now run it on my
own claims**, and the results below are its output plus my reading.

---

## 1. E1 — TWO ITEMS WERE STALE AT WRITING, NOT BY DRIFT

The distinction matters. *Drift* is the corpus moving after you wrote. **Stale-at-writing** means
the closure was already banked, below the band the document claims to be written against. That is
`B1202`'s "finished-but-forgotten" class, and these are instances five and six of it.

| item | asserted | actual | verdict |
|---|---|---|---|
| **`FULL_ACCOUNTING` fenced row: "S4 (the quine) UNBUILT"** | unbuilt | **`B1184` PROVED — "THE QUINE SYNTHESIS … the S4 rung dispositioned."** The instrument flags it at 2/2 terms. Worse: `B1184`'s own first sentence is *"THE CORRECTION FIRST: the register carried 'QP-1 (the quine) open' — **STALE**"* | **STALE AT WRITING.** I repeated a staleness that had already been publicly corrected, in an arc numbered *below* my own band |
| **`FULL_ACCOUNTING` item 5: "the 953 class-group step — disc-6237 cubic field"** | open, `[pari-grade seat]` | **`B1093` PROVED** — `K = ℚ[x]/(x³−12x−5)`, disc 6237, **h(K) = 1 proved**, h⁺ = h = |Cl/Cl²| = |Cl/Cl³| = 1 | **STALE AT WRITING** (eight days) |
| **`FULL_ACCOUNTING` item 8: the (Vol,CS) clock-coherence run** | *"registered; cc/SnapPy"*, never run | **`B1197` PROVED — the run was executed**, with a **SPLIT VERDICT**: the named primary test passes, the full census check fails | **STALE, post-writing** (legitimate drift) |
| **`FULL_ACCOUNTING` item 4: the ℙ³ adjudication** | *"reduce or carry permanently"* | **`B1206`: exactly one condition short** (3→2→1, points need 0), and `B1208` closed all three named candidates | **MATERIALLY MOVED** — not adjudicated, but no longer an open-ended ask |
| **`TOE_GAP` A3: the E₆ boundary bridge** | *"New mathematics, not retrieval"* | **`B1216`**: σ moved to *"one bridge missing, **FULLY SPECIFIED**, with a runnable pass/fail test and a documented EMPTY candidate set"*, the object named as a graded character with a six-clause kind-map | **MATERIALLY MOVED** |
| **`FULL_ACCOUNTING` item 1 / `TOE_GAP` A1: dynamics** | *"no equation of motion anywhere (exhausted); [open domain]"* | **`B1157` NEGATIVE, sealed DECIDABLE-RESULT, a productive negative**: *"the object supplies **NO parameter-free dynamical law at the archimedean infinity-place**"*, with every load-bearing ingredient shown **generic to all finite-volume hyperbolic 3-manifolds** — plus a decidable result (Fried refuted for every m, since `H*(m004;Sym^{2m}ℂ²)` is never acyclic) | **UNDERSTATED — see §2** |

**Rows that survive the check, and one of them notably:** cosmology's three blind rows come back
**clean**, and `B1202` used those *exact* regions (dark matter/relic abundance/freeze-out;
inflation/reheating/e-folds) as its own **negative control** — so a MISSING claim there is
explicitly admissible. Items 2 (S1) and 7 (the r-supply bridge) return zero settled matches. **The
instrument discriminates; it does not just fire.**

---

## 2. THE CORRECTION THAT CHANGES AN ANSWER I GAVE THE OWNER

The seal said the failure worth reporting is *"staleness that changes an answer given to the
owner."* There is exactly one, and it is about **dynamics** — which I put to the owner twice this
session as the biggest hole.

I wrote, in `THE_CHAIN_GAP.md` and in chat: *"dynamics — no equation of motion derived anywhere.
Not a value problem. A different kind of object missing."*

**True about the record as a whole, and incomplete.** At the one place that was actually probed —
the archimedean infinity-place, via analytic torsion and the Ruelle zeta — the answer is not
*unattempted*, it is a **banked negative**: no parameter-free dynamical law there, and the
ingredients that looked promising are generic to every finite-volume hyperbolic 3-manifold, so the
whole story survives swapping `m004` for a non-arithmetic knot **verbatim**. That is the `B996`
genericity lesson again, one place further out.

**The corrected statement:** dynamics is **not one undifferentiated hole**. It is *one route
probed and closed negative* plus *the rest unprobed*. Which is a sharper thing to say and a
slightly worse position than "we simply haven't looked" — because the one place we looked came back
generic.

---

## 3. E4 — THE WORST DIVERGENCE IS INSIDE ONE DOCUMENT

`THE_TOE_GAP.md` §5 is headed **"THE ONE GAP THAT DOMINATES"** and says:

> *"**DYNAMICS is the gap.** … **Only A1 is load-bearing for physics as such**."*

`THE_TOE_GAP.md` **addendum 4**, 115 lines further down, is headed:

> *"**THE SECOND IS KIND B, NOT KIND A: the 'dominant gap' dissolves, and the dominant gap is now
> COSMOLOGY.**"*

**A reader of §5 never reaches the correction.** That is precisely — not analogously, *precisely* —
the defect the paper's own SPEC §9 warns about in `docs/THE_SM_VERDICT.md`: *"its §1 table still
reads 'three generations, structurally' while its own addenda — 220 lines further down — re-scope
… A reader of the table never reaches the correction."* **This bench wrote the same defect into its
own document, and then, in memo 148, audited someone else's paper for currency.**

Cross-document: `FULL_ACCOUNTING` still lists dynamics as **open item 1** while `TOE_GAP`'s
addendum has already moved the dominant-gap claim off it. Same row, two statuses, two documents.

---

## 4. E3 — WHAT THE DOCUMENTS DO NOT CARRY

- **`B1202`'s rule itself** — the admissibility condition on MISSING claims. None of the three
  documents states searched terms for any of its absences. **Now discharged for the thirteen items
  above; the terms are in the certificate.**
- **`B1216`'s λ regression.** The documents record λ as closed-to-external by `B1194`. `B1216`
  makes it *worse*: the exhaustion argument and the "excluded by TYPE" argument are **withdrawn**,
  leaving λ with **no acceptance criterion at all**. The gap list did not grow to match.

---

## 5. FENCES AND LIMITS

- **E2 is reported at the strength of what I checked.** I tested whether the documents assert the
  two supports `B1216` withdrew (the eigenline clause, the canonical partner) — they do not. A full
  reopened-row audit over every DELIVERED row was not run, and E2-NONE means *no reopening found by
  these checks*, not *none exists*.
- **The instrument is a retrieval aid, not an adjudicator.** `B1202` says so itself, and every row
  in §1 was read before being called stale.
- **Being found stale is the expected outcome of a currency pass.** The documents were correct when
  written except for the two that were not. The reportable failure is §2 — the one correction that
  reaches the owner's answer — and §3, where this bench committed the exact defect it later audited
  another document for.

---

## 6. THE STANDING CHANGE THIS ARGUES FOR

`B1202` built the instrument and installed the rule; **this bench never adopted it.** Adopting it
here, as bench practice, in the corpus's own words:

> **No MISSING / OPEN / "never run" claim leaves this bench until
> `89affd5b:scripts/checks/already_banked.py` has been run on its terms, and the searched terms are stated
> with the claim.**

Six detectors of mine have needed checking against themselves this session. This is the first time
the corpus had already built the detector I needed and I did not look.

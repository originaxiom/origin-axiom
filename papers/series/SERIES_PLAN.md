# THE SERIES PLAN — four papers, one spine, and the repo not downplayed

**Owner-directed 2026-08-26: "all of them", with the binding constraint "it's a downside if our
math and paper downplays the repo."**

## The problem the series solves

**One 52pp chain publishes badly** — the scrutiny's F1 (the entrance is one thin link joining two
halves) and M2 (*"both halves are good; the joint is the claim"*), plus no single referee competent
across Sturmian combinatorics, hyperbolic geometry, arithmetic and exceptional Lie theory.

**But four narrow papers publish the programme badly** — they read as four disconnected small
results and hide that there is a verified corpus behind them. **That is the owner's objection and
it is correct.**

## What would actually be downplayed, named precisely

**Not any theorem. The METHOD.** Sealed preregistration with digests over bytes; bite controls that
must be able to fail; two-bench independent re-derivation; an error ledger with classes rather than
incidents; negatives-first; *a specialist gate has a date*; a 35-item hostile scrutiny triaged to
one live defect; **and the standing habit of the corpus correcting its own headlines within hours.**

**No single theorem carries that. The series must.**

## The spine — REVISED 2026-08-26, and the fourth seat had already built it

**I first proposed writing a programme paragraph. That was the wrong instrument, and I was working
from a stale tree.** The `codex/seat-r001` seat has banked
`documents/PROGRAM_QUESTION_ANSWER_MAP.md`: **81 canonical questions, SHA-256 registered
(`38b145bf…`), source-linked, with a renderer and a campaign validator.**

| status | count |
|---|---:|
| `PROVED` | **22** |
| `REFUTED` | **29** |
| `CONDITIONAL` | 13 |
| `EXTERNAL_BLOCKER` | 16 |
| `EMPIRICAL` | 1 |

> **MORE REFUTATIONS THAN PROOFS. That single table says what the programme is, quantitatively,
> better than any paragraph I could write — and it is hashed, rendered from JSON, and validated.**

**So the spine is:**

1. **The question-answer map, cited by ID.** Every paper's claims carry their `OA-C####` IDs, so a
   referee can see the claim's status *and* the 80 other questions around it. **This is what stops
   four papers reading as four accidents: they are visibly four windows into one registry.**
2. **The verification pointer** — `verify/` travelling in the tarball, clean-room reproducible, with
   the claim-to-script table (the current paper's Appendix B, reusable verbatim).
3. **A series footnote** naming the others by title and status.

### ⚠ CORRECTED 2026-08-26 — I read the domain labels without opening the rows

**My first version of this section said: "`vacuum` 22 · `geometry` 17 · `lie` 8 · `qft` 8 ·
`values` 6 · `flavor` 6 · `spectrum` 5. Paper I is geometry/arithmetic, II is lie, III is qft, IV
is values+framework — the four largest non-vacuum domains, one community each." I then opened all
81 rows. THE PAPER I ASSIGNMENT IS WRONG.**

**All 17 `geometry` rows are ALGEBRAIC geometry of heterotic bundles** — Hoppe stability, monads,
Kuranishi obstruction, short-vector descent. **Not one is hyperbolic geometry or 3-manifolds.** I
matched on the word `geometry` and never checked the questions under it. **That is the identical
error class this seat has banked repeatedly: reading a label as a result.**

**Paper I's real anchors are three rows, in two much smaller domains:**

| ID | domain | status | question |
|---|---|---|---|
| `OA-C0001` | `genesis` | **REFUTED** | does minimal description select a unique formal seed independently of encoding? |
| `OA-C0002` | `genesis` | **CONDITIONAL** | do the declared substitution rules select Fibonacci at minimality? |
| `OA-C0003` | `carrier` | **CONDITIONAL** | does the Fibonacci substitution canonically determine the oriented mapping torus `m004`? |

**`OA-C0003`'s recorded answer is Paper I's own honest limit, stated by another seat before I
drafted a line:** *"Conditionally. Squaring the determinant-minus-one incidence gives `RL`, but
letter-to-Dehn-twist, puncture, orientation, and mapping-torus operations are extra typed data."*

> **So Paper I's anchor questions are one REFUTED and two CONDITIONAL — none PROVED.** Paper I
> proves a clean theorem; the programme questions it feeds are conditional, and the reason is
> named. **The paper must say so, and this is strictly better than a borrowed count of 17.**

**Papers II–IV survive the audit.** II → `lie` (`OA-C0005` PROVED, `OA-C0006` CONDITIONAL,
`OA-C1057` PROVED); III → `qft` (`OA-C1061`, `OA-C1062`); IV → `values` (`OA-C1059`, `OA-C1060`,
`OA-C1063`, `OA-C1064`).

**And the audit paid a dividend on III.** `OA-C1061` is **REFUTED** — *do the cited Fried, Park or
Pfaff torsion formulae, or the scalar `m004` cusp scattering determinant, directly supply the
one-loop object?* — and `OA-C1062` is **EXTERNAL_BLOCKER** — *can one construct a gauge-fixed
spin-2 one-loop determinant for the finite-volume cusped case?* **Those are exactly this seat's
B8112/B8113 negative and its item-3 residue 1, the spin-2 cusped test function I named as the one
genuine literature void.** Two seats, no contact, same two conclusions with the same boundary
between them. **That corroboration belongs in Paper III and is worth more than the domain count I
got wrong.**

**`vacuum` (22) is the current 52pp paper's territory and stays its own object. The 17 heterotic
`geometry` rows are a FIFTH object belonging to no paper in this series** — they are the codex
seat's line, and this plan should stop implying otherwise.

## The four, and the order

| # | paper | source | community | risk |
|---|---|---|---|---|
| **I** | **The intrinsic characterization** — period-one ⟺ det −1; traces exactly `m ≥ 1`; Selections I–III extend to the whole locus (B8122 E1); the `m = 6` threshold (E2) | §§4–5 of the current paper, largely extraction | combinatorics on words / hyperbolic dynamics | low |
| **II** | **The rung spectrum** — `dim z(S)` takes exactly eleven values, all attained; the flat-function of 30 hyperplanes in a 4-space; 109 flats, exact over ℚ | B8078 | exceptional Lie theory | low |
| **III** | **The one-loop identity** — `σ_k` one-dimensional ⟹ the AdS₃ boundary-graviton one-loop **is** `∏_{n≥2}|R(n,σ_n)|^{−2}`; `n=2` at the abscissa carrying 202× the error budget; torsion ratios | B8100/B8104/B8112/B8113/B8129/B8130/B8133 | mathematical physics | low |
| **IV** | **What a scale-free class invariant cannot supply** — `Hom(G,ℝ₊)=0`; B990's orbit-to-point gap as structural; the value question closed from five routes; the 14-manifold family and what separates `m004` | the negatives corpus + B8128 | math-ph / foundations | higher |

**Order: I → II/III → IV.** A hard positive theorem establishes credibility first; the negatives
land with weight afterwards rather than reading as excuses. **IV is the flagship and goes last on
purpose.**

## What happens to the current 52pp paper

**It is not discarded — it is the source and the proving ground.** Its Appendix B verification table
and `verify/` suite (21/21 clean-room) serve all four. Its §§4–5 become paper I nearly verbatim.
Its App C corrections record stays as the programme's own error history.

**Whether it is ever submitted as-is becomes a separate decision, not a prerequisite.**

## The honest risk, stated

**A series invites the reply "why not one paper?"** The answer must be in the spine paragraph and
must be true: **these are four different mathematical communities, and the joint between them is
itself one of the programme's results** — `prop:mod3`, the single link, which paper IV treats as an
object of study rather than a step to be hurried past.

**That turns the current paper's weakest point into paper IV's subject.**

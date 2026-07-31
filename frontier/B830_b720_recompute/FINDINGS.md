# B830 — the masterplan: three cited facts computed, one fork deleted, one false positive corrected

cc banking seat, 2026-07-30. **Prereg `df750537a34581ee`, sealed at `f317c2fa` before computing.**
Gate 5 absolute — classification facts only, no physical value, nothing to `CLAIMS.md`.

## Cell results

| cell | result | kill branch |
|---|---|---|
| **A1** cyclotomic branch | ℚ(ζ₃) ∩ ℚ(i) = ℚ; compositum degree **4**, minpoly `x⁴+8x²+4` | available, did not fire |
| **A2** Markov quiver | mutation class size **1**; finite-mutation **yes**, finite-type **no** | available, did not fire |
| **A3** local DOF | moduli finite-dimensional (`dim H¹` = 6 at E₆, 1 at SL(2)) | available, did not fire |
| **A4** residue | Connes–Marcolli's mixed-Tate-over-ℤ[i] stays **CITED** | n/a by declaration |
| **B** forks | `REVIEWS.md` fork **deleted**; `ROADMAP.md` was a **false positive** | — |
| **C** revival score | B731 **10 → 0**; 2 of 3 flagged rows were false positives | — |

**All three pre-stated expectations were confirmed**, including A2's predicted class size of exactly 1.
Confirmation is weaker evidence than surprise, and is recorded as such.

## A1–A3: what a label-lock was standing in for

B720's negative rests on three classification facts. Its only lock asserted **three string literals
were distinct** — it verified that three different strings had been typed (B828). Now:

**A1 — the branches are disjoint.** ℚ(ζ₃) = ℚ(√−3) and ℚ(i) = ℚ(√−1) are distinct imaginary
quadratics (disc −3 vs −4); their compositum has degree **4**, so neither contains the other and
their intersection is exactly ℚ. Cyclotomic conductors 3 and 4. **The Eisenstein and Gaussian
branches share nothing beyond the rationals.**

**A2 — finite-mutation, not finite-type, and the detector is proven to work.** The Markov quiver
(3 vertices, doubled arrows) has a mutation class of size **exactly 1** — it is self-mutating up to
isomorphism — so it is mutation-**finite**. It is **not finite-type**: no representative has all
|b_ij| ≤ 1, which is the Fomin–Zelevinsky criterion for ADE. **ABHY positive geometry requires
finite type; the object's cluster structure does not have it.**

> **The positive control is what makes this readable.** An A₃ Dynkin quiver run through the same
> code returns `finite_type = True` with class size 4. Without it, `finite_type = False` would be
> indistinguishable from a broken detector — which is exactly how a negative goes unearned.

**A3 — no local degrees of freedom.** A local field theory carries a function's worth of DOF per
point. The moduli of flat connections on this 3-manifold has dimension `dim H¹(M; g)`, which is
**finite**: 6 at E₆ (six exponents, one each — CLAIMS E14 / B575) and 1 on the SL(2) geometric
component. **Finite-dimensional moduli cannot supply holographic locality.**

## A4 — the part that stays cited, and why that matters

> **"Connes–Marcolli's cosmic Galois group is mixed-Tate over ℤ[i]" is a fact about *someone else's
> construction*.** It is not computable here and remains a **citation**.

A1 computes only the **object's** side — that its arithmetic lives on the Eisenstein branch, and
that the two branches are disjoint. **The composite first NO-MATCH is therefore PART-COMPUTED,
PART-CITED**, and is labelled so. Calling it "computed" would be precisely the
necessary-vs-sufficient error the B525 audit was built to catch: the disjointness is *necessary* for
the mismatch, not *sufficient* to establish it.

## Cell B — one fork was real, one was my own error

**`REVIEWS.md` — deleted, after proof.** Section-by-section comparison: **0 headings** present only
in the fork, **0 shared bodies** materially longer there. Fully subsumed by `docs/progress/REVIEWS.md`
(29 sections vs 98). Deleted; two dangling citations rewritten.

**`ROADMAP.md` — NOT a fork, and Review 35 was WRONG about it.** The two files share **zero**
headings:

| file | is | headings |
|---|---|---|
| `ROADMAP.md` (root) | the **phase ladder** | Phase 0 / A / B / C, cadences, standing rules |
| `docs/ROADMAP.md` | the **tier map** | Tier 0 the object → Tier 4 the goal |

**Review 35's Finding 7 called this a duplicate and bannered it "NOT the operative roadmap."** That
banner was false and is removed; both files now carry an accurate reciprocal cross-reference.

**Consequently the "four duplicated authoritative filenames" claim in B827 is wrong.** The true
count is **two** — `REVIEWS.md` and `PROGRESS_LOG.md`. `ROADMAP.md` is two distinct documents, and
`CLAIMS.md ×3` is two legitimately paper-scoped inventories.

> **I generalised from a filename count without checking composition — B819's own lesson, committed
> by me two arcs after writing it down.** The check that caught it is the one B819 prescribes: ask
> what the count is *made of*.

## Cell C — the carried `revival_score: 10` was real, and worse than recorded

It is not in B731's verdict record (where the carried item implied) but in
`frontier/B738_pathfinder_compiler/kill_graph.json`, and it was the **corpus maximum** — next
highest 6.

**The same row's own `note` already read *"ALREADY RETRACTED by B734 (error E22)"*.** A
machine-readable field contradicting the human-readable one **in the same record**: anyone sorting
by `revival_score` was sent first to the single most thoroughly resolved question in the graph, and
the hatch it recommends (*deepen past the plateau*) had **already been taken by B734**. Lowered to
**0** with the reason written into the note.

**A scan for the same contradiction found 3 rows; reading them narrowed it to 1.** B285's note says
the *math* was verified — not that the kill was resolved — and later arcs **confirm** rather than
reopen it. K-O's kill was resolved *soundly*, with its stated revival condition tested and found
absent, and its score is already the minimum. **Two of three were my regex's false positives.**
*A first count is a hypothesis*, earning its keep for the third time this session.

## What this does not do

It does not re-open B720's **conclusion** — B706 is reconfirmed three independent ways and was never
under test — and it does not touch the two arithmetic LEADS. It converts three cited classification
facts into computed ones **where possible**, and says plainly where it could not.

`tests/test_b720_coupling_path.py` · `tests/test_b830_masterplan.py`

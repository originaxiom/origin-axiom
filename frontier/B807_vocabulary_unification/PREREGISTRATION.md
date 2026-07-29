# B807 — PREREGISTRATION: are the two vocabularies redundant, or orthogonal?

**Sealed before any computation.** cc banking seat, 2026-07-29. Repository-instrument scope —
**no physics reading, no Gate 5 surface, nothing to `CLAIMS.md`.**

## 1. The question, posed so it can come out either way

B806 measured that the programme's two anatomies of one object have **zero overlap**: none of
`kill_graph`'s **11 faces** is one of the atlas's **18 motifs**. The obvious reading is *bug —
merge them*. **This arc does not assume that.**

There is a second reading, and it is the more interesting one: **the two vocabularies may be
orthogonal axes.** A *face* says **WHERE** on the object the work sits (its anatomy). A *motif*
says **WHAT** mathematical structure is in play. If so, zero overlap is **correct by design**, the
defect is only that the relation was never declared, and merging them would **destroy
information**.

## 2. The discriminating test, declared before running it

Compute the **joint distribution of (face, motif)** over the arcs carrying both labels.

| outcome | reading | action |
|---|---|---|
| **SPREAD** — many distinct (face, motif) pairs populated; no small set dominates | the axes are **orthogonal**; zero overlap is by design | **declare the two-layer structure; do NOT merge** |
| **CONCENTRATED** — a few pairs carry most arcs, i.e. face is largely predictable from motif | the vocabularies are **redundant labels** for one thing | **merge into one vocabulary** |

**Pre-declared thresholds, fixed now:**
- Let `P` = number of (face, motif) pairs actually populated, out of `11 × 18 = 198` possible.
- Let `top5` = share of labelled arc-pairs carried by the 5 commonest pairs.
- **SPREAD** if `P ≥ 60` **and** `top5 ≤ 0.50`.
- **CONCENTRATED** if `P < 60` **or** `top5 > 0.50`.
- If the two criteria disagree, the result is **AMBIGUOUS** and neither action is taken — reported
  as such rather than resolved by choosing the convenient half.

**Independence check (secondary, reported either way):** normalised mutual information
`I(face; motif) / min(H(face), H(motif))`. Near 0 supports orthogonality, near 1 supports
redundancy. It is a *corroborator*, not the criterion — the criterion is fixed above.

## 3. The observer — a third question, not a missing member

`observer` scored the **highest intensity of any derived candidate (4.1 over 48 arcs)** and is in
**neither** vocabulary, while B733 proved its menu **bounded** and B766 proved it
**RANK-SATURATED at exactly 3** (conjugation, reversal, the golden branch).

**Pre-stated hypothesis:** the observer is **not** a missing face and **not** a missing motif — it
is a **third axis**: WHERE · WHAT · **WHICH CLOSING**. This matches the programme's own finding
that object and observer are one system whose discrete choice-set is saturated at three bits.

**Two-outcome:** if arcs mentioning `observer` distribute across faces and motifs **broadly**, it is
a third axis (it cuts across both). If they **concentrate** in one face or one motif, it is a
missing member of that vocabulary and should be added there instead.

## 4. What would make this arc a failure

- Merging the vocabularies **because merging was the plan**, when the test says orthogonal.
- Adjusting the thresholds in §2 after seeing `P` or `top5`.
- Reporting AMBIGUOUS as whichever of the two actions is more convenient.
- Changing the atlas lexicon or the kill-graph faces **inside this arc**. This arc **decides the
  structure**; any instrument edit is a separate, separately-sealed act — because editing them here
  would move B806's numbers while B806 is the evidence for doing it.
- Claiming the observer's axis-status without the distribution actually computed.

## 5. Pre-stated expectation, so the result can disappoint it

I expect **SPREAD** — orthogonal axes — because a face is a location and a motif is a structure, and
those are independent by construction. I expect the observer to be a **third axis**.

**If the test returns CONCENTRATED, my expectation is wrong and the merge is the right action.**
Recorded here so that outcome cannot later be softened into "we always meant to keep them separate."

## 6. Deliverables

- `joint.py` — the joint distribution, `P`, `top5`, the mutual information, the observer spread.
- `FINDINGS.md` — the verdict against §2's fixed thresholds, and the structure declared.
- `tests/test_b807_vocabulary.py` — locks the measured joint and the verdict.
- **No edit to `scripts/atlas/atlas.py` or `kill_graph.json` in this arc** (per §4).

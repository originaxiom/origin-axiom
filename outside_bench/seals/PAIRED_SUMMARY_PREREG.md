# SEAL — THE PAIRED-SUMMARY CHECK: does a summary claim more closure than its own cell?

**Sealed 2026-08-30, pushed BEFORE the instrument is written.** Successor to memo 164's
**NOT ADOPTED** detector; different design, different substrate.

## 0. Why this substrate and not the last one

Memo 164 asked an **open-ended** question — *is there a live arc somewhere in the corpus bearing on
this permanence claim?* — and failed because **a drifted permanence claim omits the vocabulary of the
route it forecloses**, so the terms that would retrieve it are exactly what the drift removes.

`B1220` found a real instance **by hand**, on a different substrate:

> *"`B1196`'s `claim_one_line` says … 'which is WHY they are anchors', while its own cell record
> GC-27 says … λ fails the theorem's first hypothesis … **The verdict line asserts the theorem
> EXPLAINS λ; the cell says the theorem DOES NOT REACH λ — the summary overstates its own cell.**"*

**A paired comparison asks a closed question:** *does this summary claim more closure than the cell
it summarises?* Both texts are in hand, they are about the same thing **by construction**, and **no
retrieval step can fail.** The corpus stores both halves — `frontier/<arc>/arc_verdict.json` and
`frontier/<arc>/FINDINGS.md` — for all 1122 arcs.

## 1. The method

For each arc: find sentences in the **summary** carrying a **closure** assertion, and sentences in
the **cell** carrying an explicit **limitation**; flag the pair when they share distinctive
(high-IDF) terms — i.e. **they are about the same subject and disagree about whether it is settled.**

## 2. Cells

### P-1 — the control · **BINDING, and it is the real instance, not a synthetic one**
**Memo 164's lesson, applied directly:** *"control passing is not instrument working — a two-sided
control on a **synthetic** positive can pass while the real positive is missed, because the synthetic
one was written by the same hand as the detector."* **So the positive control is `B1196`**, the
instance `B1220` found by hand and that this instrument had no part in choosing.

- **positive:** `B1196` **must flag**.
- **negative:** arcs whose summaries are known faithful **must not** — `B990` (its summary says
  *SHARPENED, NOT CLOSED*, matching its cell) and `B1202` (which fences its own instrument).
- **P1-DISCRIMINATES** vs **P1-USELESS**. **P1-USELESS voids the instrument**, as memo 164's did.

### P-2 — the sweep · **BLIND**
Run over every arc having both halves.
- **P2-FINDINGS** (each flag **adjudicated by reading both texts** before reporting) vs **P2-CLEAN**.

**Declared prior:** **P1-DISCRIMINATES, P2-FINDINGS** with a **small** count — a handful, not
dozens. **If it returns dozens I will suspect the detector**, because `B1220` found one by hand in a
corpus that has been audited repeatedly, and a well-calibrated instrument should not suddenly find
fifty.

## 3. Fences

- **A flag is a prompt to read both texts, never a verdict.**
- This finds **summary-vs-cell disagreement**. A summary and cell can agree and **both** be wrong;
  that is outside this instrument and is not claimed.
- **If the sweep does not survive adjudication, the verdict is NOT ADOPTED** — the same outcome memo
  164 took, and taking it twice is cheaper than shipping a detector that cries wolf.
- Gate 5 untouched: text only.

# B1008 — the atlas is blind in an EPOCH, and the blindness is where the programme now lives

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** instruments. Gate 5 untouched.

**Verdict: PROVED.** B806's concentration statistic fell through the 0.85 floor its lock defended.
**The floor was not bumped** — B829 set the precedent that this tripwire is answered by
**re-deriving**, and the re-derivation found something sharper than drift.

---

## 1. THE TRIPWIRE, AND WHAT IT WAS ALREADY TRUE OF

    B806 stated      0.933
    B829 re-derived  0.8845
    B1008 measures   0.8496   over 924 probes   <- through the 0.85 floor

**The breach predates this session's work.** Measured at `HEAD` before B1007 existed: **0.8494**.
B1007's own probe moved it **up** by 0.0002. **So the last banked arc shipped with this lock red**,
and with `test_b833`'s routing lock red too — both found only when a full suite was finally run.

## 2. IT IS NOT DRIFT. IT IS EPOCH STRUCTURE

| band | n | top-3 cov | any motif | **motifs/probe** | local top-3 |
|---|---|---|---|---|---|
| B1–200 | 184 | 0.739 | 0.935 | 5.11 | metallic, trace_map, golden |
| **B201–400** | 196 | **0.995** | 1.000 | **5.95** | firewall, eisenstein, golden |
| B401–600 | 177 | 0.960 | 0.994 | 5.76 | firewall, golden, eisenstein |
| B601–800 | 175 | 0.886 | 0.971 | 5.04 | eisenstein, golden, figure_eight |
| **B801–900** | 89 | **0.629** | 0.921 | **2.98** | eisenstein, z3_generation, firewall |
| B901–1010 | 103 | 0.709 | 0.893 | 3.10 | eisenstein, firewall, amphichiral_cp |

**The aggregate is a weighted average across an instrument that works in one era and not another.**
Coverage peaks at **0.995 in B201–400** — the era the lexicon was authored to describe — and falls
to **0.629** in B801–900, the SM-structure campaign.

## 3. THE DISCRIMINATING FACT: UNDER-LABELLED, NOT INVISIBLE

Two hypotheses, and the table separates them:

- **Vocabulary drift** (recent arcs use *different* motifs) would show a stable motifs/probe with a
  shifted mix.
- **Blindness** (recent arcs match *fewer* words) shows density collapse.

> **Density HALVES: 5.95 → 2.98.** Meanwhile **`any_motif` stays high (1.000 → 0.921)**, so recent
> arcs are **not invisible — they are under-labelled**, matching ~3 old words where their
> predecessors matched ~6.

*(Both effects are present — the local top-3 does shift, `z3_generation` and `amphichiral_cp`
surfacing recently — but density is the dominant term.)*

## 4. THE ROOT CAUSE, AND IT IS 14 FOR 14

The lexicon's own header freezes its grounding: **`knowledge/K001..K022`** — the **early** knowledge
base. Counted over the **183 arcs at B800+**, against concepts chosen from the campaign's own
vocabulary **before counting**:

| concept | arcs B800+ | in lexicon? |
|---|---|---|
| **the 27** | **52** | **NO** |
| **E₆** | **49** | **NO** |
| chirality | 38 | NO |
| measurement | 34 | NO |
| rank | 29 | NO |
| generation | 28 | NO |
| cascade | 28 | NO |
| centralizer | 24 | NO |
| observer | 16 | NO |
| hypercharge | 13 | NO |
| anomaly | 12 | NO |
| Higgs | 11 | NO |
| value layer | 5 | NO |
| Maass | 4 | NO |

> ### 14 of 14. Not one concept the recent corpus is about has a word in the vocabulary built to detect what recurs.

## 5. WHAT THIS DOES TO B806 — it strengthens it

B806's finding was that *"3 motifs covering >90% is a statement about 18 labels, not about the
object."* **The epoch structure is a much sharper proof of exactly that:** a statistic about the
*object* would be **stable**; this one is **fitted to an era** — 0.995 where the labels were
authored, 0.63 where they were not. **B806's thesis survives its own number falling**, and is
better evidenced by the fall than it was by the original 93.3%.

## 6. THE CONSEQUENCE THAT MATTERS

The Recurrence Atlas exists **to re-orient** — `query.py card` is the documented entry point for a
seat picking up the work. **Its reliability is now known to be epoch-dependent**, and it is weakest
**exactly where the programme currently is**. A seat querying the atlas about the cascade, the 27,
rank or chirality is querying an instrument with **no word for any of them**.

**Deliberately NOT done here: widening the lexicon.** Adding 14 words would change **every motif
count in the repository** and silently re-date every recurrence claim — B806's whole point is that
what the instrument can see is a *choice*. That is a sealed decision of its own, **registered as a
lead, not taken as a side effect of a suite repair.**

---

**Verdict: PROVED.** The concentration floor is breached; the cause is an epoch-specific vocabulary
with a **14/14 gap** against the current corpus; **B806's thesis is strengthened, its number
superseded.**

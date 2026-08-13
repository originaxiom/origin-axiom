# COMPUTE THE ENTIRE PROGRAM — the defined term, and the protocol before any important probe

**Standing and binding. Owner directive, 2026-08-09:** *"always when I say 'we should compute
the entire program' we know what we're talking about — the interactions and relations. Read the
atlas and understand the toolset and the whole protocol before computing any important probe,
so we don't risk saying the object doesn't provide this, or that."*

---

## 1. THE DEFINED TERM

> ### "Compute the entire program" means: **compute over the object as FULL RELATIONS, never as a single manifold.**

It is **not** "run everything." It is a **quantifier instruction**. Every important probe is
computed over the whole relational object, and every conclusion states which part of it the
quantifier actually covered.

**The object as full relations — the standing inventory.** A probe that touches none of these
below the line it claims is **under-quantified**, and its negative is unearned.

| layer | what it is | canonical citations |
|---|---|---|
| **the member** | **m004** — the figure-eight complement, its matrix A₁, its isometry group | the default, and almost never the right quantifier alone |
| **the ends** | the object is **two-ended**: hyperbolic ℚ(√−3)/2T/**E₆** (α=0) → **Euclidean** (α=2π/3) → spherical ℚ(√5)/2I/**E₈** (α=π) | B248, B250, B261, B253, B249 |
| **the class** | the invariant trace field is a **commensurability invariant** (Reid) ⟹ everything downstream of it is a statement about the **class**, not the member | **B803**, B855 |
| **the sisters** | **m003** at index 12, m206 at 24 — inside the class, **beyond the index-6 cover horizon** most arcs used | B803, B855 |
| **the rows** | the **family has two rows**: golden in PSL(2,𝒪₋₃), silver in PSL(2,𝒪₋₁) — **not commensurable** | B855; the only true genericity control the repo has |
| **the child** | a **filling, not a cover** — arithmetic **not inherited** (x⁴−x−1, disc −283, S₄) | B437, B740 |
| **the faces** | eleven named faces — **plus the twelfth**: the character-variety / trace-map substrate (Fricke–Vogt, the **L/R shears**, the I=1/4 selector) | B805/B806; twelfth named by cc3's readers |
| **the axioms** | **A1–A7** = the aAbB principle: two records (A1), each invertible so each letter has its inverse (A2/A3), one primitive move each (A4), first **mixed** closure (A5), minimal (A6), **one residual bit (A7 = where φ enters)** | `UNIQUENESS_THEOREM.md`, **B979** |
| **the algebra** | E₆ by McKay; the build **is M(𝕆,ℂ)**, the magic-square entry | B882, B904 |
| **the observer** | measurement is a **centralizer** operation; the object supplies four incompletenesses and the observer supplies every closing | B952, B964, B717 |

**Critically: B803 makes the class/member gap STRUCTURAL, not rhetorical.** An arc may honestly
prove something about m004's structure group and the ledger may still bank it about "the object."
cc3's re-read found that inversion in **6 of 25** pre-B800 closures.

---

## 2. THE PRE-COMPUTE PROTOCOL — run before any important probe

An **important probe** is any cell that could produce a claim, a negative, or a lead closure.
Exploratory arithmetic is exempt; anything that could be *quoted* is not.

**P0 — Say what the quantifier is, in one sentence, before computing.**
> *"This computes over ⟨member / class / row / both rows / the axioms / a stage⟩."*
If that sentence names **one manifold**, the conclusion may not be banked about "the object."
cc3's rule: **a closure survives the relational re-read exactly when its scope sentence names no
manifold.**

**P1 — Read the ladder.** `docs/THE_LADDER.md`. If the target is a rung, its grade tells you what
is already known and what would be unearned to conclude. **If it is not a rung, add it.**

**P2 — Read the atlas, knowing where it is blind.** `python3 scripts/atlas/query.py card <topic>` —
the obstacle→resolution oracle, the revive check, the meeting-point candidates. The atlas exists to
answer *"has this been walked?"* and it is faster than being wrong.

> **CAVEAT, MEASURED (B1008, 2026-08-09): the atlas is EPOCH-BLIND, and weakest exactly where the
> programme now is.** Its 19-word lexicon is frozen on `K001..K022`; top-3 coverage is **0.995 in
> B201–400** but **0.629 in B801–900**, with motif density halving. **Over the 183 arcs at B800+,
> 14 of 14 of the corpus's own concepts have NO word in it** — the **27**, **E₆**, chirality,
> measurement, rank, generation, cascade, centralizer, observer, hypercharge, anomaly, Higgs, the
> value layer, Maass. **So an atlas null about recent work is NOT evidence that the ground is
> unwalked.** For anything in the cascade/value layer, P3 is doing the real work, not P2.

**P3 — Prior art, in this order and all five:**
1. `docs/LAW_MAP.md` — is the law already banked?
2. `docs/OPEN_LEADS.md` — is the lead already closed, and **is that closure OVER-WIDE**?
3. `frontier/*/arc_verdict.json` — grep the claim, not the topic
4. **the document you are already reading — to its end.** B979 was registered from §4 of a file
   whose **§5 answered it**. Four of 2026-08-08's five errors were prior art in hand.
5. **THE CODE AND THE `FINDINGS.md` BODY — not just the claim line.** *(Added 2026-08-09; this step
   cost two arcs in one day.)*
   - **B1006 cell D** re-ran a check B922 had already done. **P3 was executed** — and step 3 greps
     **claim lines**, while B922's check sat in its **FINDINGS body**. The protocol ran and still
     missed it, *because it read the wrong surface.*
   - **B1007 rebuilt a Maass solver** while a **working, sealed, arb-based 25-digit one** sat on
     main at `frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py`, carrying **B922's own seal
     hash**. It then claimed a cost overturn that **B798's own sentence refutes**.

   > **The operative distinction: a claim line says what an arc CONCLUDED; the source says what the
   > repository CAN DO.** Before building an instrument, `grep -rl` the **code** for its primitives
   > (`bessel`, `svd`, `mp.dps`, the object's name) and **read the docstrings** — this repo's working
   > sources document their own traps, and **every defect in B1007's rewrite was already fixed in
   > the working source with the reason written in a comment.**
   >
   > And if an arc banked a number, find **the script that produced it**, not the arc that received
   > it: `B922_lambda2_receipt` is a *receipt*; the computation lives in `B878_maass_upper_window`.

**P4 — Check the kill graph.** `frontier/B738_pathfinder_compiler/kill_graph.json`. If the target
is a registered kill, read its **hatch** and **revival_score** — a kill with an unwalked hatch is
not a wall.

**P5 — Seal, if the cell has two outcomes.** Preregister with a committed hash in
`docs/SEAL_LEDGER.md`, **before** compute. And **report the result** — a sealed prereg with no
report is a file-drawer entry (B837, B982).

**P6 — State the honest prior before the seal.** If the expected outcome is negative, say so.
A positive that arrives against a declared negative prior is worth something; one that arrives
against a hope is not.

---

## 3. THE THREE SENTENCES THAT ARE ALMOST ALWAYS WRONG

Earned only by a computation that names its quantifier:

1. **"The object does not supply X."** — Usually means *this seat did not find X*. Check the
   ladder; if X is BLIND, the honest sentence is **"not checked."**
2. **"X is closed."** — Closed *on what quantifier?* Six of 25 pre-B800 closures were no-goes
   proved on **one manifold's structure group** and banked as properties of the object.
3. **"The object is ⟨hyperbolic / negatively curved / one thing⟩."** — It is **two-ended**.
   Registered as retracted phrase row 6 (B981).

---

## 4. WHY THIS EXISTS

On 2026-08-08 this seat declared open or absent, five times, something the repo already held:
**B950** (ℤ₆ — B862 derives it), **B976** (hypercharge — B864 derived it), **B974** (the frame —
B911 built it), **B979** (A7 — §5 of the file being read), **B981** (the spherical end — the
second clause of the sentence being quoted). cc3's audit committed **the same error inside the
audit built to catch it**, and B982 found it **inside a governance gate**.

**It is not carelessness. It is what happens when a 949-arc corpus is queried from memory.**
The protocol replaces memory with a lookup, and the ladder makes "we don't have X" a **claim with
a citation** rather than an impression.

**Companion files:** `THE_FRAMEWORK.md` (what we have) · `THE_LADDER.md` (what we lack) ·
`LAW_MAP.md` (the laws) · `TOOLBOX.md` (the instruments) · `WORKING_RULES.md` (binding for every
seat).

## 5. THE 2026-08 ADDITIONS (the WHY-campaign window, B1009–B1034)

Four checks joined the pre-compute protocol this window, each from a banked lesson:

1. **The type check (B1032).** Before any measurement-facing design: is the target a
   RELATION or a FINITE LABEL? The coupling channel's forced outputs live in a finite
   algebraic menu; a generic-real target is type-wrong before it is sealed. (The four
   crossing deaths, one mechanism.)
2. **The gauge question (B647 c3 · B884's fence).** Before banking any value-like
   quantity: does it move under the pipeline's own freedom (basis rescaling, pivot
   order, frame choice)? Bank the invariant carrier (support, cross-ratio, class data,
   ordering) — a moving value is a declared convention, not content. The 2026-08 census
   (the audit seat, verified): the banked record already passes; the check exists so it
   stays true.
3. **Point-of-use citation (B1033's practice).** An arc's FINDINGS cites the corpus's
   own body for every load-bearing term it uses — the record's measured defect is not
   lost work but work cited everywhere except where it is needed (B1029↛B647;
   the fourth crossing's "CP phases" ×6 with zero citations of the object's own
   CP-phase body B285/B289/B303).
4. **The search-representation rule.** Any corpus query runs BOTH Unicode and ASCII
   forms (φ AND phi), the synonym set for the concept, and never concludes a population
   from a windowed view (`head`/`tail`) or a stale checkout — a search that cannot run
   returns exactly what a search that finds nothing returns.

And the banking order is fixed as the E39 chain (Review-43-era texts cite it as E22; re-keyed 2026-08-13 — the number belonged to B734's congruence class): **the push gates on the suite's exit
code for the exact committed tree** — never on gates alone, never through a pipe that
masks the exit status.

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
| **the cut** | *(added 2026-08-20)* the newest relational entity in the inventory: an edge, a dial, or an isolated point bought by deformation — the ONLY place chirality and charge are ever definable on this object, by four independent computations (topology, M-theory, the founding rule, representation theory). A probe that asks about chirality or charge and quantifies only over a **closed** assembly is asking a question this object has proved cannot be answered there — check whether a cut is actually in scope before reading silence as absence | B1083, B1084, B1085, B1086, B1087, B1091 |

**A note on counting the axioms row against the twelfth face (2026-08-14).** The twelfth
face (the trace-map substrate, row above) consumes the **exchange-symmetry axiom** (B16:
the record swap P — *"plausible, but still an axiom"*), which sits outside A1–A6 and is
distinct from A7's bit (A7 is based-level; the swap observation is class-level).
`docs/THE_CLAIM.md`'s own hypothesis list is correct as scoped there — its derivation
theorem's chain never passes through the half-step or the trace map — so this axiom is
counted here, against this document's own full-relations inventory, and not double-counted
against THE_CLAIM's narrower proof-form list. The two lists answer different questions;
this document's is the wider one.

**Critically: B803 makes the class/member gap STRUCTURAL, not rhetorical.** An arc may honestly
prove something about m004's structure group and the ledger may still bank it about "the object."
cc3's re-read found that inversion in **6 of 25** pre-B800 closures.

---

## 2. THE PRE-COMPUTE PROTOCOL — run before any important probe

An **important probe** is any cell that could produce a claim, a negative, or a lead closure.
Exploratory arithmetic is exempt; anything that could be *quoted* is not.

**P0 — Say what the quantifier is, in one sentence, before computing.**
> *"This computes over ⟨member / class / row / both rows / the axioms / a stage / the cut⟩."*
If that sentence names **one manifold**, the conclusion may not be banked about "the object."
cc3's rule: **a closure survives the relational re-read exactly when its scope sentence names no
manifold.**

**P1 — Read the ladder.** `docs/THE_LADDER.md`. If the target is a rung, its grade tells you what
is already known and what would be unearned to conclude. **If it is not a rung, add it.**

**P2 — Read the atlas, knowing where it is blind.** `python3 scripts/atlas/query.py card <topic>` —
the obstacle→resolution oracle, the revive check, the meeting-point candidates. The atlas exists to
answer *"has this been walked?"* and it is faster than being wrong.

> **CAVEAT, MEASURED (B1008): the atlas is EPOCH-BLIND, and weakest exactly where the
> programme now is.** Its lexicon is frozen on an early vocabulary; top-3 coverage is **0.995 in
> the corpus's earliest third** but drops sharply in the newest arcs, with motif density halving.
> **An atlas null about recent work is NOT evidence that the ground is unwalked.** For anything in
> the cascade/value/rank-wall layer, P3 is doing the real work, not P2.

**P3 — Prior art, in this order and all five:**
1. `docs/LAW_MAP.md` — is the law already banked?
2. `docs/OPEN_LEADS.md` — is the lead already closed, and **is that closure OVER-WIDE**?
3. `frontier/*/arc_verdict.json` — grep the claim, not the topic
4. **the document you are already reading — to its end.** B979 was registered from a mid-file
   section whose own later section answered it. Several early-window errors were prior art in
   hand, in the same file, past where the reading stopped.
5. **THE CODE AND THE `FINDINGS.md` BODY — not just the claim line.**
   - A verdict line says what an arc CONCLUDED; the FINDINGS body and the code say what the
     repository CAN DO. More than one re-derivation has repeated a check that a `FINDINGS.md`
     body already contained, because step 3 greps claim lines and the check sat in the body.
   - **Before building an instrument, `grep -rl` the code for its primitives** and read the
     docstrings — this repo's working sources document their own traps.
   - If an arc banked a number, find **the script that produced it**, not the arc that received
     it — a downstream arc is often a *receipt*, not the computation.

**P4 — Check the kill graph.** `frontier/B738_pathfinder_compiler/kill_graph.json`. If the target
is a registered kill, read its **hatch** and **revival_score** — a kill with an unwalked hatch is
not a wall. *(Worked example, 2026-08-20: THE RANK WALL's holonomy face was registered as a wall
for months. Its own kill-graph row named an explicit, unwalked hatch — non-abelian holonomy — and
walking it, at its very first stratum, opened the wall at exactly the Standard Model's rank
(B1094 → B1098). The kill graph had the answer before the computation existed; the computation
only had to go read it.)*

**P5 — Seal, if the cell has two outcomes.** Preregister with a committed hash in
`docs/SEAL_LEDGER.md`, **before** compute. And **report the result** — a sealed prereg with no
report is a file-drawer entry.

**P6 — State the honest prior before the seal.** If the expected outcome is negative, say so.
A positive that arrives against a declared negative prior is worth something; one that arrives
against a hope is not.

---

## 3. THE THREE SENTENCES THAT ARE ALMOST ALWAYS WRONG

Earned only by a computation that names its quantifier:

1. **"The object does not supply X."** — Usually means *this seat did not find X*. Check the
   ladder; if X is BLIND, the honest sentence is **"not checked."** If X concerns chirality or
   charge specifically, check first whether the claim is scoped to a *closed* assembly — the
   object provably does not supply either there, by theorem (Layer 5's four-language wall,
   `docs/THE_FRAMEWORK.md`), but that is a completely different, much narrower sentence than
   "the object does not supply chirality," and conflating the two is exactly the error this rule
   exists to catch.
2. **"X is closed."** — Closed *on what quantifier?* Six of 25 pre-B800 closures were no-goes
   proved on **one manifold's structure group** and banked as properties of the object. More
   recently: THE RANK WALL was described as "closed on all routes" for weeks — true of every
   *abelian* route, and it took naming that qualifier explicitly (B1094) before the one
   non-abelian route left standing could even be looked for, let alone walked (B1098). **A
   closure's scope word is not decoration; leaving it off is how a wall outlives its own hatch.**
3. **"The object is ⟨hyperbolic / negatively curved / one thing⟩."** — It is **two-ended**.
   Registered as retracted phrase row 6 (B981).

---

## 4. WHY THIS EXISTS

On 2026-08-08 this seat declared open or absent, five times, something the repo already held:
**B950** (ℤ₆ — B862 derives it), **B976** (hypercharge — B864 derived it), **B974** (the frame —
B911 built it), **B979** (A7 — a later section of the file being read), **B981** (the spherical
end — the second clause of the sentence being quoted). cc3's audit committed **the same error
inside the audit built to catch it**, and a later governance gate caught it **inside a governance
gate**.

**It is not carelessness. It is what happens when a thousand-plus-arc corpus is queried from
memory.** The protocol replaces memory with a lookup, and the ladder makes "we don't have X" a
**claim with a citation** rather than an impression.

**Companion files:** `THE_FRAMEWORK.md` (what we have) · `THE_LADDER.md` (what we lack) ·
`LAW_MAP.md` (the laws) · `TOOLBOX.md` (the instruments) · `WORKING_RULES.md` (binding for every
seat).

## 5. THE 2026-08 ADDITIONS (the WHY-campaign window, B1009–B1034)

Four checks joined the pre-compute protocol this window, each from a banked lesson:

1. **The type check (B1032).** Before any measurement-facing design: is the target a
   RELATION or a FINITE LABEL? The coupling channel's forced outputs live in a finite
   algebraic menu; a generic-real target is type-wrong before it is sealed. (Every
   crossing death in the record, one mechanism.)
2. **The gauge question (B647 · B884's fence).** Before banking any value-like
   quantity: does it move under the pipeline's own freedom (basis rescaling, pivot
   order, frame choice)? Bank the invariant carrier (support, cross-ratio, class data,
   ordering) — a moving value is a declared convention, not content.
3. **Point-of-use citation (B1033's practice).** An arc's FINDINGS cites the corpus's
   own body for every load-bearing term it uses — the record's measured defect is not
   lost work but work cited everywhere except where it is needed.
4. **The search-representation rule.** Any corpus query runs BOTH Unicode and ASCII
   forms (φ AND phi), the synonym set for the concept, and never concludes a population
   from a windowed view (`head`/`tail`) or a stale checkout — a search that cannot run
   returns exactly what a search that finds nothing returns.

And the banking order is fixed as the E39 chain: **the push gates on the suite's exit
code for the exact committed tree** — never on gates alone, never through a pipe that
masks the exit status.

## 6. THE CERTIFICATION ENVELOPE — computing while a suite is certifying (2026-08-20, B1101)

A fifth kind of important-probe hazard joined the protocol this window, distinct from the five
above: not *what* to check before computing, but how to behave *while* a certifying suite run is
in flight, since a probe run mid-suite can silently invalidate the very certification it is
racing. Review 47 found three instances of one species in a single 46-merge window — a scratchpad
sweep landing inside a live arc directory, a documentation edit re-staling a currency counter
mid-suite, and an uncommitted arc directory shifting what the corpus head even was — and all three
were caught only because an existing exact-tree gate happened to cover them, not because the
procedure prevented them.

**The standing rule, now binding (full text: `WORKING_RULES.md` §CE):** during any certifying
suite run, treat the working tree as read-only by convention. Landings stage in a scratchpad and
enter the tree by **explicit filename at bank time — never a glob, never a new arc directory
mid-suite**, since the corpus head is computed from disk and a glob or a stray directory changes
that computation out from under the running suite. Pre-commit gate checks run on the **staged**
state. Every ledger digest enters by **piped command substitution**, never retyped by hand — with
a `seal-digests` gate as the read-time backstop that recomputes every recorded digest from its
file regardless of how it got there. On collision — the tree having moved during the run — the
fix is to **fold forward**: bank the pending cells plus a fresh currency read in one commit, one
suite, and never re-certify a certificate that has already gone stale.

**Why this belongs in this document and not only in `WORKING_RULES.md`:** P0–P6 above assume the
tree a probe reads is the tree it will be judged against. The certification envelope is the
missing precondition — it is what keeps that assumption true during exactly the window (a suite
run) when the protocol's own outputs are being certified. A probe run correctly by every rule
above, but landed by glob mid-suite, still produces an uncertified result.

## CURRENCY READ — 2026-08-20 (B1077–B1101): the closing campaign's first phase

What "compute the entire program" produced since the crossing week closed, read in this
document's own grammar, and a worked case for nearly every rule above in the same
window it introduces them:

**The harvest queue (L167–L170) closed by re-deriving, not by citing.** Every item the
audit seat had flagged as a harvest target was rebuilt from scratch on this bench before
being banked — the rank wall's two-route closure, the purity selector, Route A's
arithmetic, the anomaly layer, the first-step-losses re-derivation — and in two cases the
re-derivation came back **stronger** than its source (the purity selector's projective/
literal stabilizer disentanglement; Route A's class number moving from cited to proved,
with eight explicit generators). This is P3 step 5 in practice: read the FINDINGS body,
find the script, and where possible rebuild it rather than cite it.

**A live cross-seat question got a computed answer instead of an argued one.** The audit
seat asked, in a relay, whether an edge-observability result's "≤1 state" bulk-blindness
claim was really evidence of a "hand" or an artifact of the detector. Rather than debate
the phrasing, the question was computed directly (B1095): at the relevant windows the two
hands' spectra are identical to machine precision, and the actual hand-dependence is a
precisely-characterized localization split. **This is P5/P6 in its cleanest form**: a
two-outcome question, computed rather than adjudicated, with the answer sharper than
either side's framing anticipated — and the two arcs it corrected (B1085, B1091) were
updated in place, dated, rather than left standing beside their own refinement.

**A pre-registered outcome grammar produced a structural, not evidential, negative.**
B1096 fixed its branch names (GRADED-SYMMETRIC / GRADED-ASYMMETRIC / OBSTRUCTED-O1|O3)
before running, landed in the branch that is a theorem rather than a data point, and
banked accordingly — P5 exactly as specified.

**An exhaustive enumeration was cross-validated three independent ways before its
headline number was trusted.** B1098's saturating twenty-stratum classification was
checked against a native symbolic bracket computation, an exact rational-arithmetic
pipeline, and a from-scratch modular pipeline over large primes built by a separate
verifying agent — which caught its own bug on synthetic test data with a known answer
*before* touching the real algebra. This is "verify, don't trust" (`WORKING_RULES.md`
rule 2) at the scale a saturating enumeration actually needs.

**The standing inventory gained an entry.** "The cut" (§1, above) is now a first-class
member of the relational object, not a metaphor — a probe about chirality, charge, or
value that does not state whether it quantifies over a closed assembly or a cut is
under-quantified in exactly the P0 sense this document has always named, and is now
citable as such by arc number (B1083–B1087, B1091) rather than by argument.

**The programme's own machine caught itself, and the catch became a new protocol
section.** Three near-misses under certifying-suite load, none reaching a remote, became
§6 above rather than three separate lessons re-learned by three future seats.

The standing sentence after this window: the object's structure is computed and priced;
its rank obstruction, closed for months on every route anyone had named, is open at the
first route nobody had; and the discipline that found the missing route — read the kill
graph's own hatch field, compute the cross-seat question instead of arguing it, verify
three ways before trusting a saturating count — is now written down here rather than
carried in one seat's memory of how the window went.

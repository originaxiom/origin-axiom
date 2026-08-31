# THE SUBMISSION CAMPAIGN — from a finished document to a sendable paper

**Opened 2026-08-31 (owner-directed). Expectations pre-registered before each cell runs.**

The publication campaign closed six cells and left THE PAPER complete *as a document*: 17 pages,
every load-bearing claim mapped to a re-runnable record, §3 hostile-read from both directions, Gate 5
clean. This campaign addresses what stands between that and a paper that can be *sent*.

## S0 — the premise audit (stop rule 1b), run FIRST and already paying

The rule earned in the last campaign: **audit each cell's premise before running the cell.** Applied
here before any cell was written, and it immediately found the campaign's largest item.

**FINDING, and it is submission-blocking: the paper's bibliography is decorative.**
**Twelve of its thirteen `\bibitem`s are never `\cite`d** — only one is. LaTeX prints unused
bibitems without a warning (only an undefined `\cite` warns), so the build is clean and the document
*looks* referenced. It is not: Morse–Hedlund, Hurwitz, Thurston, McKay, Mostow, Dynkin and Weyl all
appear **by name in the prose with no citation attached**.

*This is the E53 shape in a new place — a surface that exists, passes every automated check, and
carries none of the content it appears to carry.* A referee meets it on page one.

---

## S1 — CITATIONS: attach every external appeal to a source

**The computation.** For every named external result in the body, attach the citation. Then invert
the check: every `\bibitem` must be cited at least once, or be deleted. A bibliography entry that
nothing points at is not a reference, it is furniture.

**The instrument** (`scripts/checks/paper_citations.py`, gated, MB12-controlled): parse the body for
named external appeals and for `\cite` keys; report (a) named appeals with no nearby citation,
(b) bibitems never cited, (c) `\cite` keys with no bibitem. **Bite control:** a planted uncited
bibitem and a planted citation-free named appeal must both be reported.

**Pre-registered expectation:** ~8–15 named appeals currently uncited; **12** orphan bibitems (known
exactly, from S0). Recorded so a smaller number would be a surprise, not a relief.

**Falsifier for the cell:** if after repair the checker still reports orphans, the repair is
incomplete and the cell does not close.

---

## S2 — BREADTH: the bibliography is thin for what the paper touches

Thirteen entries for a paper spanning hyperbolic geometry, arithmetic groups, exceptional Lie
algebras, anomaly cancellation and von Neumann algebras. The body appeals to results that have **no
entry at all** — among them Morse–Hedlund on factor complexity, Hurwitz extremality, Bala–Carter on
nilpotent orbits, Weyl equidistribution, Tomita–Takesaki/Connes modular theory and the type-III
classification, Powers' ITPFI factors, and Krutelevich on integral Jordan orbits.

**The rule this cell follows, and it is a restriction not a licence:** an entry is added **only**
where the body actually leans on that result. We are not padding a reference list; we are ending the
situation where the paper leans on named mathematics it does not cite. **Anything the paper does not
use does not get an entry.**

**Pre-registered expectation:** the list roughly doubles, to ~25–30. If it grows past ~35 the cell
has started padding and must stop and say so.

---

## S3 — SUBMISSION MECHANICS

Title and abstract are in place and honest (the abstract opens with what is *generic*, which is the
right opening for this paper and should not be softened). Missing: **MSC 2020 classes**, keywords,
an arXiv primary/secondary category, and a placeholder author block.

**Owner-gated, and left unwritten deliberately:** author name, affiliation, acknowledgements. The
repo's privacy rule keeps the owner's surname out of tracked files, so **the author block ships as a
placeholder and is filled at submission, outside the repo.**

---

## S4 — ONE FIGURE, if it earns its place

The chain is forty-three links with its cost at the two ends and none in the middle. That is the
paper's central structural claim and it is currently **prose only**. A single schematic — the chain
as a line, the four axioms marked, the twelve-link axiom-free stretch shaded — would let a referee
see in one glance what §3 spends two pages establishing.

**The test this cell must pass:** the figure must carry information the prose does not, not decorate
it. If the drawing turns out to restate the sentence, it is dropped and the cell reports that.

---

## S5 — THE FINAL HOSTILE READ, by a seat that has not seen the final text

codex's Wave-8 read inspected main **before §3 and the appendix existed**. Nobody has attacked the
current 17 pages. Their last read found four real things including a correction we adopted, so this
is not a formality.

**Ask, stated so it cannot be answered comfortably:** attack the 43-link count, the axiom-free
stretch, the M² = RL identity's status as *the* orientation axiom rather than an illustration of it,
the "bought at geometrization and nowhere earlier" boundary, and the appendix's `settled`/`computed`
distinction — which is this bench's own invention and has never been reviewed.

---

## S6 — WHAT WILL NOT BE FIXED, and is stated in the paper instead

Three ledger items remain genuinely open and the paper says so: λ's **general** no-go (the placement
is decided and the import route excluded — the general statement is not proved); the ℙ³'s single
named datum (**blocked on another seat's in-flight computation**, not on us); and the V-valued
texture assembly. **None blocks submission**, because the paper's thesis is that the boundary is
*located and priced*, not that it is closed. A paper claiming otherwise would be the overclaim this
whole programme exists to avoid.

---

## Sequencing and stop rules

```
S0 premise audit ──► S1 citations ──► S2 breadth ──► S3 mechanics ──► S4 figure ──► S5 hostile read
                                                                                        │
                                                                            S6 stays open, and is stated
```

1. **S1 before S2.** Attach what exists before adding what is missing, or the additions cannot be
   checked against actual use.
2. **S5 runs last, on the final text**, or it reviews something that no longer exists.
3. **No cell reports success without its bite control passing first.**
4. **Gate 5 holds throughout**; no measured physical value enters the paper.
5. **The suite certifies the exact tree before any push** (E39); no tree mutation during a
   certifying run (E46).
6. **Owner-gated items (author, affiliation, venue) are not guessed.** They ship as placeholders.

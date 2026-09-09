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

---

## S7 — THE PAPER REFLECTS THE MOST RECENT STATE: the chirality campaign enters (owner-directed 2026-09-09, run the same day)

**Premise audit (stop rule 1b).** The paper's chain section said *forty-three links, thirty-nine forced* while `docs/THEOREM_LEDGER.md` had carried 46 since 2026-09-03 — the E53 shape on the paper's own front section; and the chirality campaign (B1290–B1324: the parity theorem, the two-or-nothing theorem, the charge-locus lock, the one-cusped index and its two vanishing theorems, the tower law and the SM closings' vacuum, L204 closed, the genesis upgrades, Arc B) was on no page of the paper although each result is a registry row with a lock. **Both repaired at source:** the eight results enter the chain ledger as links **C47–C54** (each with its exact statement, its records and its locks; the forcedness profile updated to 34 theorems / 8 no-go, the axiom set and the axiom-free stretch unchanged; 54 links, 50 forced), the paper's chain table is regenerated from the ledger and its prose counts and figure follow; a new section **\S The chirality bit** states the campaign in the paper's own register (no internal identifiers), and the abstract, the non-claims, the falsifiers (one upgrade trigger; the Z′ regime as a weak experimental handle on an observer-selected vacuum), the wall and the recognition table are updated. Six bibliography entries added only where the new text leans on them (Pantev–Wijnholt; Siegel; Lothaire/Mignosi–Séébold; Friedl–Kim–Kitayama; Dunfield–Friedl–Jackson; Markov); the provenance appendix gains nine claims (30 claims over 36 records, all settled, all locked; the generator's audit reports 0 defects).
**Bite controls:** `paper_chain_table.py`'s staleness test failed before the regeneration and passes after; `forcedness_census.py` fails on any profile drift; `paper_provenance.py --selftest` plants a claim on a non-existent record and reports it.
**Pre-registered expectation for the hostile read (S5, run on the final text by two fresh seats):** at least one overclaim in the new section will be found and repaired; the numbers will check against the records; any internal identifier that leaked will be removed.

**S5 RUN ON THE FINAL TEXT (2026-09-09, the same day): the hostile read by a fresh seat returned eighteen findings, and the pre-registered expectation held — the section had converted hedged results into unhedged ones exactly where the hedge was the finding.** The three structural ones: (1) the counts were read as generation counts while every establishing record refuses that identification (I-26 UNEARNED) — repaired by an opening scope note ("Counts are counts") and by saying "complete copies of the Standard-Model content, generations in the structural sense" wherever the word occurred, abstract included; (2) "every wall met is the object's amphichirality in one face's language" overstated two theorems that are not amphichirality (the Galois self-duality holds by arithmetic alone; the period-2 symmetry is orientation-preserving) — repaired to "a conjugation the object or its coefficient field carries", abstract and section; (3) the abstract's "the wall is the object's and not its tower's … the bit becomes a class invariant there" equivocated between the net-chirality bit and the genesis's handedness bit — repaired to "the amphichirality is the object's and not its tower's … the genesis's handedness bit becomes a class invariant there; the spectral wall has held on every sector computed". The fifteen others, all repaired at the sentence: the scope note's "every wall could have gone the other way" replaced by the record's own forced-zero and non-vacuity caution; the wall's specialist list expanded from one item to the record's six (and "a finite computation" corrected: the multi-cusp index must first be derived); "the torsion is generated by the meridian" scoped to eight of twelve covers with the four Galois-protected sectors restored; "every character of the first nine closings" corrected to the non-trivial characters of the third through ninth with the even-level correction at the twentieth; the parity theorem's orientation-preserving hypothesis restored; θ and the manifold's mirror defined once and used distinctly; the charge-locus lock scoped to the outer lift with the inner lift's count-two configuration stated; "no net count anywhere" scoped to the sl₂ germs with the untouched frames named; the sibling's price restated as two choices plus the golden face plus the census bound; the substrate fork's second carrier (amphichiral) and word bound restored and its "not both" reconciled with the covers; the census class corrected from "knot complements" to one-cusped H₁ = ℤ manifolds (ledger and registry too); the Z′ coupling named ($g_2$, kaon and $B_s$ mixing); "the 42" and "fifteen faces" defined and the four identities footnoted; the abstract's 252/222/2 arithmetic completed; and the five internal identifiers that had leaked into the generated chain table stripped by the generator (`strip_internal`), with "cross-seat" removed from the appendix. A second fresh seat's read of the verification package is recorded under S8. The referee's verdict on the pre-repair text — major revision — is kept on the record as the reason the two seats read before, not after, the landing.

## S8 — THE VERIFICATION PACKAGE (owner-directed 2026-09-09: "including a verification package so we can start sending it")

`papers/P3_THE_PAPER/verification_package/`: `build_manifest.py` regenerates `MANIFEST.json`/`MANIFEST.md` from the repository for every claim of the provenance appendix (record, verdict, one-line claim, every seal with its current hash, shipped scripts and results, test locks); `run_package.py --seals | --locks | --scripts` re-checks and writes `REPORT.md` with an exit code; `README.md` states for a stranger what is certified (record exists, verdict settled, lock passes, seal matches) and what is not (anything outside the repository; no measured value); `tests/test_p3_verification_package.py` fails the suite if the manifest is stale or inconsistent, and runs every lock under `OA_SLOW`. First build: 30 claims, 36 records, 12 seals (12/12 match), 54 distinct lock files. **Owner-gated and left as placeholders:** the author block, the venue, the DOI snapshot (Zenodo/SWH) and the sending itself — all sends HOLD.

**S8 READ BY A FRESH SEAT (2026-09-09, same day): eight findings, all acted on.** (1) the package was not yet public — it lands with this commit; (2) **`run_package.py --locks` failed on the committed tree: 3 of 308 tests** pinned the identification baseline at 12 after two landings had raised it to 14 — E39 instance #3, repaired by replaying the audit trail and by naming the source each new row is an instance of; (3) the README's "the commit history shows the seal preceding the results" was false as stated — a record lands in one commit; rewritten: seals certify integrity, not chronology, and re-seals keep the original hash with the reason; the matcher now ignores comment lines; (4) lock quality is uneven — the manifest now separates *primary locks* (test files named for the record; 34 of 36 records have one) from *mentions*, and the README carries the paper's own "traceability, not re-derivation" caveat; (5) the "certified" bullet now names the three computed rows' exception; (6) "every load-bearing claim" is stated as a curated list with a false-positive control only; (7) jargon (Gate 5, seat, banking) defined or removed; (8) all five dependencies pinned to the versions the manifest was built against. The reviewer's verdict on the pre-repair package — "would not convince me" — is kept on the record for the same reason as S5's.

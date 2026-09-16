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


## S9 — THE FOUR-READ REVISION AND THE SECOND PASS (owner-directed 2026-09-09: "are u sure this is the best paper we can have? … do all the self scrutiny u can before claiming it final"; landed 2026-09-15)

**Answer given before any repair: no, not final.** Four independent hostile reads of the S7 text by fresh seats — rigor (20 findings), honesty and rhetoric (12), a hep-th/hep-ph physicist (A–J), and completeness against the record (18) — plus a full read by the writing seat. Every finding was checked against the record before it was acted on; every one that survived was repaired at source, and the record was corrected where the paper had been faithful to a record that was itself wrong.

**Findings of the first cycle that changed a claim.** (1) The chain section said the twelve links C6–C17 reached the exceptional algebra "with no declared choice"; the algebra is not a numbered link of that stretch — it is handed over by McKay and certified at C26, and the measurement links C24–C42 are numbered after the observer's axiom C18 by banking order, not dependence. Repaired in the paper, in `THE_END_TO_END_CHAIN.md` Part 0.5 (dated note) and in `forcedness_census.py`'s wording. (2) The crossing was reported as a 16σ miss with sin²θ_W "within about 1σ"; the σ was a loop-truncation estimate, and `B915/results.json` gives σ_th = 3.04×10⁻⁴ for sin²θ_W, so the coordinate is 6.4 truncation-σ and about 50 experimental σ off. The paper reports the discrepancies themselves (α_s 0.077 vs 0.118; sin²θ_W 0.2293 vs 0.2312) with the running assumptions and the precedents cited; B915's FINDINGS carries a dated addendum; ERROR_LEDGER row. (3) The observer section still asserted "all 83 members of the family are amphichiral" a week after B1235 retracted it (38 of 112) — the paper's `.tex` was outside the retraction sweep's scope; removed, a footnote records the withdrawal, the sweep now reads tracked `.tex`, the phrase is registered, E53 instance #30. (4) The Z′ paragraph implied a Standard-Model vacuum broken at tree level; the record's vacuum is a supersymmetric E₆SSM-type model — disclosed with King–Moretti–Nevzorov and Langacker cited, the coupling renamed g_{Z′}, Δm_K and ε_K separated, the ℤ₆ statement conditional on the colour frame and the shaping. (5) The base rate of the E₆ entry point computed exactly (145 of 400 admit a surjection onto SL(2,3); 124 of 400 have m004's two classes up to Aut ≅ S₄; B993 addendum, `sl23_baserate.py`, lock `test_b993_baserate_exact.py`). (6) A new section, *The middle of the journey*, states the manifold's own structure, the algebra's arrival, the measurement calculus, the matter law, the value layer, the three crossings and the seam theorem in the paper's register; the title, the abstract, two non-claims, the appendix preamble and the freedom ledger's opening were rewritten to the body's strength; bibliography 21 → 39.

**The second pass (S5 rule), on the revised text: three fresh-seat reads, each first verifying the first cycle's repairs.** *Rigor:* all 19 required repairs PRESENT; 20 new defects in the new section, six of them contradictions of the record rather than compressions — the τ "double duty" paragraph reinstated a corollary B963 had retracted (the rank is effected by expectation values, five resources not four); the product law was stated with the charge-equivariant λ = 1 against the τ-twisted hierarchy (v₁v₂v₃ = 3^{3/2}·(2304/953)² there; in the equivariant gauge the hierarchy collapses to a triple root); "nine colourless couplings" for the nine coloured-line couplings; the cubic field's branch index disowned and then used; the seam census quoted at 54 where B740 completed it to 78 of 78; "reproduced and not assumed" for 3/8 resting on the electromagnetic anchoring of Y, which B919 grades an unpriced identification and which the freedom ledger did not carry. All twenty repaired at the sentence; the ledger gains its seventh non-continuous row (the identification Q = T₃ + Y), the prose counts and the ledger-count lock follow. *Physics:* 28-item checklist (23 present, 3 wrong, 2 partial) and 18 further defects, all repaired: the crossing's non-supersymmetric miss is not a test of the paper's own supersymmetric closing, said in the recognition list and the abstract; the charge-locus lock stated under the outer lift with the inner lift's count-two configuration, and the open question — whether the wall-selected real form 𝔢₆(₂), whose maximal compact is the inner lift's fixed algebra, is the same involution — left open in the text rather than papered over; the Z′ bounds scoped to a chiral model with independent rotations, the normalisation Tr Q′²/Tr Y² = 6210/9 stated, the third-family branch's B₁₂ given, the dilepton limit cited; Distler–Garibaldi corrected to its E₈ statement; the two centraliser censuses (coordinate subtori 30/12 vs the three non-coordinate lines at 46) separated; "anomalous over any chiral content" scoped to the derived sixteen; the chirality-protection lattice direction corrected to minimal; L and R defined with their conjugacy; the global form's observable named (line operators, Tong) and "falsifiable by measurement" withdrawn; gauge-only running named; the Galois vanishing stated on the compositum ℚ(ζ₃, ζ_n) with the prime-to-3 hypothesis explained; the sixty-four-dimensional obstruction scoped to the principal embedding (B1303: the regular embedding leaves a two-dimensional centraliser, E69). *Honesty:* 12-item checklist (10 present, 2 weak) and 16 findings, all repaired: the abstract and the introduction brought down to the body's own scope notes (the class, not the uniqueness, carries the claims; the global form conditional; the shaping an input; the counts stated as the three counts they are; the truncation multiple dropped); C n and "the record" defined at first use; "This is the object's contribution to the arena" rescoped to E₆'s structure in the object's charge frame; the value layer's flavour reading removed; the near-hit paragraph rewritten in plain words; the private vocabulary replaced; the paper's three "centres" reduced to the ledger. Chain-table rows 41 and 43 and three appendix claims regenerated (no 16σ, no λ collision, no "generations", 78 not 54, basis pairs not structure constants, a sealed menu not "exhaustive"). Build: 36 pages, two pre-existing overfull boxes, undefined references 0; citations 41/41; provenance 41 claims, 0 defects; manifest current; the paper locks 15 passed; retraction sweep clean over 2844 files.

**Recorded and NOT done (editorial decisions for the owner):** the honesty read's structural recommendations — §What is unique before §The chain, the chain-table rows 19–45 moved to the package, the recognition section compressed, the seventeen draft-history asides gathered into a corrections appendix — and the cloud seat's external review (2026-09-09, on its branch): split into three papers by venue; "the chain table claims 34 theorems while the paper contains one theorem environment"; deposit with a DOI; the author block. The physics read's venue judgment: math.GT primary with hep-th and math.NT cross-lists, sendable after these repairs; not to a hep-ph venue.

**The cloud branch's paper work (`<remote>/paper-verification-ufp0zn`, 2026-09-10 → 09-14, 85 commits, NOT on main).** Its first commit is an independent verification of the S7 text: the base rate resolved the same way as here (145/400, 124/400), the retracted 83/83 sentence removed the same way, the package made green from a clean clone. Its paper-impact notes (2026-09-12, 09-13) are held for verification on this bench: item 2 (the Z′'s "anomaly-free by the conjugate copies" carries zero bits on a vector-like spectrum) is trivially true and applied; item 3 (over a chiral spectrum the family part is forced to (0, t, −t), which kills the record's (−10, 5, 5) Z′), item 1 (the metallic chirality-zero identity), item 4 (an action at the monodromy, obstructed at its square root) and B1333's multi-cusp index (all 54 covers, 38 070 sectors, zero) are NOT in the paper until reproduced here — the paper still says the multi-cusp index is the named next computation, which is true of main's record.

**Still owner-gated and unchanged:** the author block, the venue, the DOI snapshot, the send. **Still open in the mathematics and said so in the paper:** the non-vacuity of the one-cusped index, the multi-cusp index, the inner-lift question, a direct search of the Z′ third-family branch.

## S10 — THE THIRD PASS: THE PAPER CARRIES THE CONSOLIDATION AND THE FAMILY (owner-directed 2026-09-16: "completing the paper and making sure it represents the most recent findings in all aspects and nothing is lost … a bulletproof robust chain from not-nothing all the way to the detailed SM structure, with clear separation of what we have parameter free and what we don't have, what we believe we can't have"; landed 2026-09-16)

**What entered, from the landings of 2026-09-15/16.** The chain gains two links, C55 (the geometric finite-twist index is identically zero on every one-cusped hyperbolic manifold — Menal-Ferrer–Porti injectivity through a finite cover; B1413) and C56 (the index fires, in characteristic zero, on reducible non-split modules of five members of the object's commensurability class and of its degree-four cyclic cover, and not on the object's own golden locus; B1418): 56 links, 52 forced, the tally recomputed by the generator and the hand-written prose, figure and caption brought to it. The chirality section: the region-swap lemma (B1417) in the localised-count sentence; the index paragraph rewritten around the theorem and the witnesses (m010 first, then the class and the tower), with the modules run on m004 listed and the non-semisimple caveat graded with its prior against it (compact holonomies are semisimple; the complexified theory's boundary is not established); the nine-member correction (B1414/E81); the class census and the sibling (B1418); the several-cusp index reported as reported (E80); a new paragraph on the closing that could carry the bit — the E₇ apex local model (geometry exact, count cited), the forced ℤ/3 = 2T/Q₈ and its b₂ ≥ 2 condition, the Y₃ breaking to SM × U(1)_η by a Q₈ line (root-system facts), and the no-seesaw obstruction that excludes the three-apex design as it stands (B1411/B1414/B1415), stated as a design and not a theorem, with the Dirac-neutrino magnitude given. The generic section: the three base rates (the door 1 696 of 5 000 and 59/35/18 on the family; chirality 181 of 203 123; the count of three 20 of 212 641, never on one cusp). The observer: "Which member" — the genesis selects m004 variationally (Jørgensen number one, Callahan's uniqueness), so keeping the member costs the bit and moving to the class costs a selection; registered as a fork (L222). The wall: rebuilt as "The ledger in three columns" — parameter-free and had / not yet had with the computation named / believed unreachable each by a stated theorem — with the member's own reducible locus filed in the second column, not the third. Recognition: Menal-Ferrer–Porti, Jørgensen and Callahan, Minsky, Kac and the Tits/Knus–Tignol type table (the object's form is ⁶D₄ over ℚ, B1416), and complex Chern–Simons (Witten 1991). A falsifier-style upgrade trigger for the object's own locus. Five provenance rows added and one retired in the generated appendix (the harvest verdict VERIFIED now counts as settled backing, with the reason recorded in the generator). Date 2026-09-16.

**The three hostile reads on the revised text (rigor, physics, honesty; `reads_s10/`), all repaired before landing.** The hand-written link counts had not followed the generated tally (54 vs 56) — the paper's own guard reached the tally and not the prose; fixed at every occurrence, including the figure. The third column carried one item the second column owns (the member's own locus); moved. The ℙ(B₀) row was missing from the summary; added. The appendix graded the closing design "settled"; the row now names its exact half and calls the design conditional. The abstract dropped m010's precedence and hedged nothing on "index"; both repaired. s_μ(g) defined. The 18 un-enumerated family members restored to the count. The Z′ paragraph now says a vector-like pair can decouple and that the E₆SSM literature's premise is what this spectrum lacks. The E₇ point named where the local model is introduced. Locks: chain table (56/52), provenance (46 claims, 0 defects), ledger counts, citations, flagship; retraction sweep 0; `build.sh` 39 pages, no undefined references; the verification package's manifest regenerated (46 claims, 66 records, 14 seals).

**Still owner-gated and unchanged:** the author block, the venue, the DOI snapshot, the send. **Open in the mathematics and said so in the paper:** the member's own reducible locus beyond m ≤ 4 and twists of order dividing twelve; the rule separating the class members that fire; the admissibility of a non-semisimple flat module; the several-cusp index from a clean checkout; a compact G₂ closing with a 27̄ sector; the supersymmetric crossing; the σ and ℙ(B₀) rows.


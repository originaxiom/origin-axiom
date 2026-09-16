# Hostile honesty/completeness audit of papers/P3_THE_PAPER/main.tex against B1411–B1418, L220–L222, TOE_REQUIREMENTS_LEDGER

Scope: main.tex read in full (1667 lines). Checked against frontier/B1411, B1413, B1414, B1415,
B1416, B1417, B1418 FINDINGS.md, docs/OPEN_LEADS.md L220–L222, docs/TOE_REQUIREMENTS_LEDGER.md.
No computations run beyond text search/grep on the tracked files. No file edited.

---

## Defect 1 — the chain's own link count contradicts itself inside one section (SEVERE)

**Quoted text, papers/P3_THE_PAPER/main.tex:223–225:**
> "There are \textbf{fifty-four links}. Their types are: thirty-four theorems, six identities, eight
> no-go results, one census, one corollary --- and \textbf{four axioms}. So fifty of fifty-four
> links are forced, in the precise sense that they are not declared choices."

**Quoted text, main.tex:288 and 292 (figure caption):**
> "The chain's fifty-four links, with each of the four axioms marked. ... Fifty links are forced.
> The crossing's no-go sits where it fell, and the chain now runs past it to the chirality bit."

**Quoted text, main.tex:370 (the auto-generated tally, `paper_chain_table.py --tex`, "do not hand-edit"):**
> "Recomputed from the table above rather than asserted: 35 theorem, 8 no-go, 6 identity, 4 axiom,
> 2 census, 1 corollary, totalling 56 links, of which \textbf{52} are not axioms."

**Quoted text, main.tex:1499 (appendix, also generated):**
> "the chain is 56 links, 52 of them forced (39 of 43 when the census instrument was first
> recorded); axioms only at the two ends"

**Problem.** Rows 55 and 56 of the generated chain table (main.tex:365–366) are exactly the two
landings this audit was asked to check: row 55 ("the geometric finite-twist index is identically
zero", a no-go) is B1413's R27(a) theorem, and row 56 ("the index fires on the class and the
tower, not on the member", a census) is B1418's census. Adding them took the chain from 54 links
(50 forced) to 56 links (52 forced), and the *generated* tally (line 370) and the *generated*
appendix line (1499) both correctly say 56/52. The *hand-written* prose that opens §3 (lines
223–225) and the hand-written figure and its caption (lines 264–295, esp. 288 and 292) were never
updated: they still say "fifty-four" / "fifty of fifty-four" / "Fifty links are forced", and the
breakdown "thirty-four theorems, six identities, eight no-go, one census, one corollary" sums to
54, not the 56 the table now shows (35+8+6+2+1+4=56). This is not a stylistic quibble: §3's own
paragraph at lines 298–304 boasts that "the tally beneath the table is recomputed from the table,
not copied from the paragraph above it ... which is how two mis-parses were caught" — i.e. the
paper explicitly claims to guard against exactly this drift, and the guard did not reach the
paragraph three pages earlier or the figure. A reader who reads §3 start to finish hits a flat
self-contradiction (54 vs. 56 links; 50 vs. 52 forced) caused directly by B1413/B1418 landing new
links without the surrounding prose being regenerated.

**Minimal fix.** In main.tex:223–224, change "fifty-four" → "fifty-six", the type breakdown to
"thirty-five theorems, six identities, eight no-go results, two censuses, one corollary", and
"fifty of fifty-four" → "fifty-two of fifty-six". In the figure caption (line 288) change
"fifty-four links" → "fifty-six links", and (line 292) "Fifty links are forced" → "Fifty-two
links are forced". (The tikzpicture's `\foreach \i in {1,...,54}` at line 272 should also become
`{1,...,56}` if the figure is meant to be pixel-accurate to the table, though that is cosmetic
next to the prose fix.)

---

## Defect 2 — the wall's third column contains an item admittedly not "unreachable by a stated theorem" (SEVERE — this is exactly the check the task specifies)

**Quoted text, main.tex:1437 (the last clause of "Believed unreachable, each by a stated theorem"):**
> "...and the chirality bit from the member $m004$ itself on every sector so far computed --- this
> last is the one row of the third column that a future computation, named in the second, could
> move."

**Problem.** The paragraph's own header commits every item in this column to be unreachable "each
by a stated theorem." Every other item in the column is: the periods/regulators negative
(exhaustive search), hypercharge normalisation (homogeneity, a theorem for any U(1) charge
assignment), scale (Mostow, a theorem), the modular period (traciality, a theorem), the three
chiral-spectrum negatives (injectivity/region-swap/two-conjugations, all theorems), the Majorana
mass negative (an exact algebraic fact given the 27/78 content), and the finite-label negative (an
invariant-selector argument). The final item — "the chirality bit from $m004$ ... so far
computed" — is exactly the opposite kind of fact: it is the bounded search of B1418 (m ≤ 4, twists
of order dividing 12, 235 modules on m004's golden locus, main.tex:959, 1527), explicitly not
backed by any impossibility theorem, and it is precisely what Falsifier 5 (main.tex:1360) and the
second column's own wording ("the modules run are listed so that the search can be continued
rather than repeated") describe as an open, nameable computation — i.e. a column-2 item. The
sentence's own hedge ("could move") is a tacit admission of this, but the item is still filed
under "believed unreachable ... by a stated theorem," which is the exact anti-pattern the audit
was asked to check for ("nothing 'believed unreachable' that is merely not yet done").

**Minimal fix.** Move this clause out of the third column into the second ("Not yet had, with the
computation named"), e.g. appended to "...a non-zero index on the object's own reducible locus
beyond $m \le 4$ and twists of order dividing twelve (a finite computation; the modules run are
listed) — which would also move the chirality bit onto the member $m004$ itself." Delete the
clause from the third column entirely; nothing else in that column carries an in-sentence caveat
that it might not really be unreachable.

---

## Defect 3 — the three-column ledger omits the $\PP(B_0)$ (Higgs) row despite claiming completeness

**Quoted text, main.tex:1437 (opening sentence):**
> "The reader who wants the whole boundary in one place can have it."

**Problem.** The paragraph then lists, across all three columns, every other actively-tracked
freedom-ledger row by name or clear paraphrase: $\ell$ is folded into "What is permanent"
immediately after (line 1439); $\sigma$ appears in column 2 ("a candidate for the $\sigma$ row
meeting the six conditions above"); $\lambda$ appears in column 3 ("the modular period from the
object's own algebra (traciality)"); the chirality bit, the real-structure closing, the arrow
label and the finite menus are all covered somewhere in the three columns or the "permanent"
paragraph. The $\PP(B_0)$ row (the projective line of Higgs data) is the one row of §\ref{sec:ledger}
that is neither: it does not appear in column 1, 2, or 3, nor in "What is permanent" (lines
1439–1442), even though its own ledger entry (main.tex:1163–1171) explicitly frames it the same
way as $\sigma$ — "What remains is a single named datum, and it is a computation in progress
elsewhere, not an unbounded search" (line 1170) — which is verbatim the genre of column 2. It is
also the subject of its own falsifier (Falsifier 8, main.tex:1372–1375) and its own forward-looking
scope note (main.tex:1263–1267, "Should the $\PP(B_0)$ row close..."). A row this actively tracked
falling out of the one paragraph that promises "the whole boundary in one place" is a completeness
gap, not a judgment call.

**Minimal fix.** Add to column 2 (after the $\sigma$-row clause): "; a second condition on the
projective Higgs line $\PP(B_0)$, closing it to a finite point set (the named datum in progress
elsewhere)."

---

## Defect 4 — the appendix grades the closing design "settled" although the body and the source call it a design, not a theorem, and the source grades its key result conditional

**Quoted text, main.tex:1529 (appendix table row, generated):**
> "the closing design: the E7 apex local model (geometry exact, count cited), the Z/3 = 2T/Q8
> forcing b2 >= 2 for a symmetric triple, the Y3 breaking to SM x U(1)\_eta by a Q8 line times an
> order-4 character (root-system facts), and the no-seesaw obstruction (equal eta charges on both
> charged singlets; no eta-neutral Majorana source in 27^3 or 78) & settled & lock"

**Quoted text, main.tex:993 (the body's own qualification of the very same content):**
> "This paragraph reports a design verified step by step, not a theorem, and it is the closest the
> record comes to saying what a closing that carries the bit must be."

**Problem.** The appendix's own stated rubric (main.tex:1460–1463) defines "settled" as: "the
establishing result is itself closed --- proved, or a negative." The body text explicitly and
deliberately withholds that status from this exact material ("not a theorem"), and the source
arc (frontier/B1415_the_sm_seats_closing_arcs_harvested/FINDINGS.md, sm:B1365 row) grades the
no-seesaw exclusion "VERIFIED (charges, direction, sign theorem's premise); the exclusion
CONDITIONAL on sm:B1276 and on the design, as the seat states" and docs/OPEN_LEADS.md L221 repeats
"the exclusion is conditional on sm:B1276's coupling and on the three-apex design itself." Grading
the bundled row "settled" in the one table whose entire purpose (per main.tex:1466–1470, "the
table below is generated from that check rather than written by hand") is to keep claim-strength
honest is a mismatch between what the body says about its own content and what the machine-checked
table asserts about it.

**Minimal fix.** Either split the row (geometry/root-system facts as "settled", the no-seesaw
exclusion as "computed (enquiry open)" with a note "(a design, not a theorem; conditional on the
cited coupling)"), or relabel the whole row "computed (enquiry open)" to match the treatment
already given to the other conditional/open-enquiry rows in the same table (e.g. the "252
candidate contents" row and the "closure hardened by an independent second pass" row, both graded
"computed (enquiry open)").

---

## Defect 5 — the abstract's "for the first time in characteristic zero" is attributed to the wrong witness

**Quoted text, main.tex:72 (abstract):**
> "The index that measures net chirality on a one-cusped manifold is identically zero on every
> finite twist of the geometric holonomy, by a theorem, and non-zero --- for the first time in
> characteristic zero --- on reducible non-split modules of five members of the object's
> commensurability class and of its own degree-four cyclic cover, while the object's own reducible
> locus returns zero on every module computed..."

**Quoted text, main.tex:959 (body, correctly sequenced):**
> "...it is non-zero, exactly and in characteristic zero, on \emph{reducible non-split} modules
> ... --- \textbf{first on the census manifold $m010$} ($I = +1$, semisimplification $0$), then,
> with the same instrument validated on that witness before any new number was read, on five
> one-cusped chiral members of the object's own commensurability class..."

**Problem.** frontier/B1413_the_audit_lanes_r21_r31/FINDINGS.md is explicit that the true first
characteristic-zero non-vanishing witness is m010 (R27(b): "the mathematical escape from the
vanishing, exhibited exactly"), landed a day before B1418 extended the same instrument to the
object's own commensurability class and its degree-four cover. The body (line 959) gets the
chronology and the credit right. The abstract compresses this into a single clause that attaches
"for the first time in characteristic zero" directly to "five members of the object's
commensurability class," omitting m010 (which is not in the object's family) entirely. A reader of
the abstract alone — which is explicitly meant to be readable on its own, per the paper's own
"internal provenance" disclaimer at line 40 — comes away believing the family members are where
the phenomenon was first observed, when the record's own first witness is a manifold outside the
family and is credited as such in the very same paper three pages later.

**Minimal fix.** Either name m010 in the abstract clause ("non-zero — first on an unrelated census
manifold, then on the object's own family — on reducible non-split modules of five members...") or
drop "for the first time in characteristic zero" from this abstract sentence and let the
first-time claim live only in the body, where it is already stated correctly and precisely.

---

## Defect 6 — a non-claim's closing clause is worded so that it can be read as contradicting the abstract's own positive index result (moderate; ambiguity, not a certain error)

**Quoted text, main.tex:536–538:**
> "that three \emph{chiral} generations are derived. Three structural copies of the Standard-Model
> content are exhibited on the object's own closings, in mirror pairs; they are vector-like, and
> \S\ref{sec:chirality} proves at every computed sector where the chirality bit is withheld."

**Problem.** Read as a universal claim ("proves [that] at every computed sector ... the chirality
bit is withheld"), this sentence is false as of B1418: the index that measures net chirality is
non-zero — not withheld — on five class members and on t12839, the object's own degree-four cyclic
cover, both "computed sectors" in the record's own vocabulary (main.tex:72, 959). The charitable
reading — "documents, for every computed sector, whether the bit is withheld or not" — is
consistent with the record, but the sentence does not disambiguate, and it sits in the Non-claims
section, whose entire job is to foreclose misreadings rather than invite them. This is the one
place in the document where the (correct, careful) abstract-level statement of the index's mixed
result and this compressed non-claim clause could be read as pulling in opposite directions.

**Minimal fix.** Reword to remove the ambiguity, e.g.: "...they are vector-like, and
\S\ref{sec:chirality} states, for every sector computed, whether the index that measures net
chirality vanishes: zero on the closings and on every geometric-holonomy twist, non-zero — though
earning no generation count — on reducible non-split modules of the class and the tower."

---

## Checks that passed (stated for completeness, per the task's explicit list)

- No sentence in main.tex claims the index "has never been non-zero"; the abstract, body
  (line 959) and appendix (lines 1525, 1527) all correctly state the R27/B1413 and B1418 positive
  results (m010, the five class members, t12839).
- The "six class members" figure is gone from every place it would assert a live count: line 916
  correctly states "the canonical list finds nine to nine tetrahedra and twenty in the census to
  ten," matching B1414's E81 correction exactly (nine, not six), and the one surviving mention of
  "six" (main.tex:916) is explicitly historical ("an earlier count of six rested on an isometry
  list read off the triangulation as given"), not a live claim.
- No internal identifier (a "B" followed by digits) appears anywhere in main.tex, including the
  appendix — grep for `\bB[0-9]{2,5}\b` over the whole file returns nothing. The appendix and
  recognition section correctly cite the underlying literature (Menal–Ferrer–Porti, Kac,
  Knus–Tignol, Acharya–Witten, etc.) instead of internal arc numbers, consistent with the stated
  design ("this paper names no internal identifiers in its body," line 1454).
- The corrected base rates from B1414 (canonical-isometry recount, E81) are already fully
  propagated: "3996 of 4000" (line 176, matching the corrected 99.90%, not the stale 89.88%), "20
  of all 212,641" and "59 admit it and 35 do not" of the 112-member family (line 176), and the
  ⁶D₄/³D₄ typing correction from B1414 §5 (line 1325) are all present and match the record.
- L222's open programme-level question (whether the object should be the commensurability class
  rather than the member) is explicitly registered and left open in §\ref{sec:observer}'s "Which
  member" paragraph (main.tex:1097): "We register the fork and do not resolve it" — matching
  L222(iv)'s status exactly, not overclaimed as resolved.
- L221's remedy (a $27$ sector of opposite chirality / anti-apexes) and its conditioning on a cited
  coupling are both present at main.tex:993, and the "no compact $G_2$ manifold ... exists in the
  record" fence matches the source.
- B1417's region-swap lemma is stated correctly and with the right scope (transverse zeros only;
  the product mode's "$\pm4$" is a non-transverse zero set where $\chi$ is undefined, not
  non-zero) at main.tex:913, matching the source arc precisely.

---

## Verdict

The paper is unusually disciplined for a document of this scope — the base-rate corrections, the
E81 isometry-list fix, the ⁶D₄ retyping, the region-swap lemma, and the L221/L222 open questions
from the freshest landings (B1413–B1418) are all already threaded through the abstract, the body
and the appendix with the right numbers and the right hedges, and none of the three explicit
negative checks (the "index never non-zero" sentence, the stale "six" count, a stray internal
identifier) turned up a hit. That said, the paper fails its own stated discipline in one place
severely and in several places at the margin. The severe failure (Defect 1) is a plain,
self-detectable arithmetic contradiction — "fifty-four links, fifty forced" against the paper's
own machine-generated "56 links, 52 forced" three pages later — caused directly by the two new
landings this audit was asked to check (B1413's and B1418's chain rows 55–56) entering the
generated table without the hand-written prose and figure caption being regenerated alongside it;
it is exactly the kind of drift the paper's own §3 paragraph claims to have built a process against,
which makes leaving it uncaught the least defensible item on this list. The three-way separation
the paper advertises (parameter-free-and-had / not-yet-had-with-computation-named /
believed-unreachable-by-theorem) is coherent for the great majority of its entries but breaks in
exactly the place the audit was told to look for: one column-3 item (the chirality bit "so far
computed" on $m004$) is explicitly, self-admittedly not backed by an unreachability theorem and
belongs in column 2, and one actively-tracked freedom-ledger row ($\PP(B_0)$) is missing from the
"whole boundary in one place" summary entirely. The appendix's uniform "settled" tag flattens at
least one bundled row (the closing design) that the body itself, and the source arc, grade as
conditional and non-theorematic. None of these six defects understates the paper's negatives or
overstates a physical prediction — the honesty failures found are all mechanical (arithmetic
drift, mis-filed rows, a flattened grade, an abstract compression) rather than substantive
overclaims of physics, but a hostile reader would be right to stop at Defect 1 on a first pass and
ask what else in the "generated, do not hand-edit" machinery quietly diverged from the prose built
around it.

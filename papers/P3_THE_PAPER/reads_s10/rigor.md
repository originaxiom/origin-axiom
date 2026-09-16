# Hostile rigor read — P3_THE_PAPER main.tex, S10 (draft of 2026-09-16)

Scope: full 1667-line file read end to end; numbers cross-checked against
`<home>/origin-axiom/frontier/B1413*`, `B1414*`, `B1415*`, `B1417*`, `B1418*`
and the repo's own working-tree diff of `main.tex` against the last commit
(the S9→S10 delta). No computation was run beyond `grep`/`diff`/reading JSON
already on disk. Line numbers are from the file as it stands in the working
tree.

---

## 1. "Believed unreachable, each by a stated theorem" contains at least two
items that are *not* theorem-backed, one of them refuted by the paper's own
text 400 lines earlier — SEVERE, internal contradiction

**Quote (line 1437, "The ledger in three columns"):**
> "\emph{Believed unreachable, each by a stated theorem}: ... a Majorana
> mass without a $27$ sector of the opposite chirality; a finite label
> reduced further ...; and the chirality bit from the member $m004$ itself
> on every sector so far computed --- this last is the one row of the third
> column that a future computation, named in the second, could move."

**What is wrong.** The column header asserts every entry is "believed
unreachable... by a stated theorem" — i.e. a permanent, proved impossibility,
matching the paper's own later gloss of "permanent" ("What is permanent",
line ~1439: things that "will not close", contrasted with things a future
computation could move). Two of the entries in this same list fail that
standard, and the paper says so itself:

- **The Majorana-mass item.** The "no η-neutral Majorana mass" conclusion
  comes entirely from "The closing that could carry the bit" (line 993),
  whose own final sentence reads: *"This paragraph reports a design verified
  step by step, **not a theorem**, and it is the closest the record comes to
  saying what a closing that carries the bit must be."* An admitted
  non-theorem, conditional on one design (the three-apex $G_2$ cone) and one
  cited coupling (`sm:B1276`, per `frontier/B1415_the_sm_seats_closing_arcs_harvested/FINDINGS.md`,
  which itself grades the exclusion "CONDITIONAL on sm:B1276 and on the
  design"), is listed under a header that promises a stated theorem.
- **The $m004$-index item.** The sentence itself concedes it is "the one row
  of the third column that a future computation... could move" — the exact
  opposite of "believed unreachable... by a stated theorem." A row that a
  named, bounded, already-partially-run computation (Falsifier 5, line 1360:
  "at a symmetric power or a twist beyond those computed") could overturn is
  by construction not theorem-backed; it belongs in the second column ("Not
  yet had"), mirrored by a note in the third, not asserted inside the third
  column under a header that claims theorem backing for every row.

**Minimal fix.** Either (a) move both items out of the third column into the
second with an explicit forward-pointer (the paper already does something
close to this for the $m004$-index item in prose, just not in the table
placement), or (b) weaken the column header to something like "Believed
unreachable, most by a stated theorem (two rows below are conditional
designs or open computations, flagged as such)". Silently keeping the
absolute header while smuggling in two hedged rows is what a hostile referee
will hit first.

---

## 2. The generated appendix table contradicts itself on the index's
non-vacuity — SEVERE, machine-generated section, six rows apart

**Quote A (line 1521, unedited holdover from S9):**
> "the one-cusped index vanishes on every sector of the cyclic tower by two
> theorems (**its non-vacuity as an instrument is open**) & settled & lock"

**Quote B (line 1527, new in S10):**
> "the index is non-zero in characteristic zero on reducible non-split
> modules of five members of the object's commensurability class and of its
> degree-4 cyclic cover t12839, and zero on the object's own golden
> reducible locus (235 modules) ... & settled & lock"

**What is wrong.** Row A's parenthetical says the index's non-vacuity "is
open" — i.e., no one knows yet whether the instrument is ever non-zero on a
real manifold. Row B, six lines later in the *same* generated longtable,
reports exactly that non-vacuity, settled, with five named witnesses plus a
cyclic cover of $m004$ itself. This is the fact the whole new material in
§chirality (line 959 onward) and the new census link 56 exist to report; row
A was simply never retired when row B was added. The body text is careful
about this everywhere else (e.g. line 1039: "The index's non-vacuity, once
the open question, is now settled on the class and the tower"), which makes
the leftover appendix row look like an oversight in the generation script
(`scripts/checks/paper_provenance.py`, listed as modified in the working
tree) rather than a deliberate claim — but a hostile reader does not know
that, and reads two adjacent "settled" rows asserting opposite epistemic
states about the same instrument.

**Minimal fix.** Append "(now superseded — see the row below)" to row A, or
delete row A's parenthetical and let row B carry the non-vacuity claim
alone; row A's substantive content (two-theorem vanishing on the tower) is
now also a special case of the new link 55 (Menal–Ferrer–Porti injectivity,
row at line 1525) and could be merged into it instead of standing as a third
near-duplicate row.

---

## 3. "$59$ admit it and $35$ do not" out of "$112$" silently drops 18
members (16% of the family) that the paper's own source explicitly flags —
MODERATE–SEVERE, arithmetic that does not close in a headline base-rate claim

**Quote (line 176, "The three base rates" — new paragraph in S10):**
> "of the $112$ census manifolds whose tetrahedron shapes all lie in
> $\Q(\sqrt{-3})$ --- the object's own family --- $59$ admit it and $35$ do
> not"

**What is wrong.** $59+35=94\neq112$. A reader who does the arithmetic the
paragraph invites ("of the 112... 59... and 35...") finds an 18-member gap
with no explanation. The source computation
(`frontier/B1416_the_relay_residue_closed/verification/family_2t_door.out`,
quoted verbatim in `frontier/B1416_the_relay_residue_closed/FINDINGS.md`
line 23) says plainly: *"family members 112: with a 2T surjection 59,
without 35, **skipped (>3 generators) 18**"*, and the same FINDINGS file
states the caveat explicitly: *"The 18 family members with more than three
generators were not counted (the negative needs only the 35)."* That
sentence is exactly the qualification the paper omits. The same omission is
repeated verbatim in the generated appendix row at line 1528 ("59 of the 112
family members"), so it is not a one-off slip — it is systematic across both
places the number appears.

This matters more than a rounding nit because the paragraph's whole
rhetorical point is a base-rate argument ("the door is common and it is not
the arithmetic") built on a clean-looking 112-manifold denominator; the true
denominator tested is 94, and the excluded 18 are excluded for a
computational reason (a >3-generator presentation defeats the brute-force
surjection enumerator used elsewhere in the paper, e.g. line 148's own
400-manifold sweep) that has nothing to do with the fact being measured.

**Minimal fix.** "$59$ of $94$ tested admit it and $35$ do not (18 of the
112 skipped: more than three generators, beyond the enumerator's reach)" —
one clause, in both the prose and the generated appendix row.

---

## 4. Undefined symbol $s_\mu(g)$, and a plausible unflagged notational
collision with $s_m$ introduced 100+ lines later — MODERATE, undefined term

**Quote (line 907):**
> "$\chi(\mathrm{Fix}\,g) = 1 - s_\mu(g) \in \{0,2\}$, read off $H_1 = \Z$
> alone"

**What is wrong.** $s_\mu(g)$ is used with no definition anywhere in the
paper — it is not glossed at first use, not in a footnote, and does not
recur under that name. The only kindred notation the paper ever defines is
introduced at line 1015, in a different paragraph, for a different
(orientation-reversing) situation: "an isometry's orientation sign is the
product of its sign on the meridian ... and its sign on the longitude:
$\det = s_m s_l$." That is $s_m$ (sign on the meridian), not $s_\mu(g)$, and
the two are never explicitly identified. A hostile reader cannot verify the
formula $\chi(\mathrm{Fix}\,g)=1-s_\mu(g)$ at line 907 without guessing
whether $s_\mu$ means "sign on the meridian" (in which case why the
different letter and the function-of-$g$ notation, when $s_m$ at line 1015
is not written as a function of $g$?) or something else entirely (a
count, e.g. of fixed points on the meridian circle, consistent with the
$\{0,2\}$ range via $1-(\pm1)$ style parity). Whichever it is, the symbol is
a genuine hapax legomenon in a formula the paper calls a theorem.

**Minimal fix.** Either define $s_\mu(g)$ inline at first use ("$s_\mu(g)\in\{\pm1\}$,
the sign of $g$ on the meridian $\mu$") and then write $s_\mu$ consistently
at line 1015 too, or replace it with the already-defined $s_m$ if that is
what is meant.

---

## 5. The 5000-manifold "$33.92\%$" 2T-door base rate and the 112-family
"$59/94$" base rate are computed over different populations and could be
misread as the same measurement — MINOR, clarity

**Quote (line 176):** "$1696$ ($33.92\%$) admit the surjection, and of the
$112$ census manifolds ... $59$ admit it and $35$ do not."

**What is wrong.** These are two separate computations with two separate
scripts and populations (`frontier/B1414.../verification` runs B993's
counter on the first 5000 census manifolds in census order and separately
notes "exactly 7 of the 1,696 lie in [the] 112-member family"; the 59/35
split comes from `family_2t_door.py`, which runs the same counter directly
on all 112 family members regardless of census position). Only 7 of the
112-family members fall inside the first 5000 by census order, so the two
percentages (33.92% over the census at large, ~63% $=59/94$ within the
family) are not two readings of one sweep — they are two different sweeps
placed in the same sentence with a connective ("and of the 112... ") that
reads as a continuation of the same measurement. This is not a
factual error (both numbers are individually correct, see defect 3 for the
94-vs-112 issue), but the juxtaposition invites a reader to think the 5000-
sweep produced both numbers, which it did not.

**Minimal fix.** A half-clause noting the two are independent computations
("...and, computed directly and not only within that sweep, of the 112
census manifolds...").

---

## 6. "an earlier count of six" is corrected to "nine," matching the source,
but the paper does not say *whose* count was wrong or when — MINOR,
provenance thinness (contrast with the paper's own stated practice)

**Quote (line 916):** "the other eight members of its class to nine
tetrahedra (an earlier count of six rested on an isometry list read off the
triangulation as given; the canonical list finds nine to nine tetrahedra and
twenty in the census to ten, none keeping the golden face where tested)"

**Check.** This matches
`frontier/B1321_l205_the_siblings_localized_count/ADDENDUM_2026-09-16_nine_members.md`
and `frontier/B1414.../FINDINGS.md` §3 exactly (E81, the uncanonized-isometry-
list defect; nine members to nine tetrahedra, eleven more to ten tetrahedra,
$9+11=20$, golden-tested only on the nine). The number is right and the
"where tested" qualifier is honestly earned (the source explicitly says the
eleven at ten tetrahedra are "not golden-tested"). This is not a defect in
the number, but the paper's own house style elsewhere names the mechanism
plainly (e.g. the E81 ledger entry, or line 1287's "the archived solver did
not solve its two unification conditions simultaneously"); here it compresses
a whole class of defect (SnapPy's `isomorphisms_to` not canonizing) into "an
isometry list read off the triangulation as given," which a reader outside
the project cannot reconstruct into a checkable claim. Low priority, listed
because the paper elsewhere holds itself to a higher disclosure bar for
exactly this kind of correction (§Recognition's "four items were moved off
this list... we offer that number as a better guide").

**Minimal fix.** None required for correctness; optionally name the defect
class ("a non-canonical isometry enumeration") rather than paraphrasing it.

---

## Verdict

The three-way separation this paper is built on — **parameter-free / not
yet had / believed unreachable** — is the right taxonomy and, apart from
defect 1, it is applied honestly: nearly every negative claim in
§withheld and §chirality is stated at the strength of its own computation,
with domains and hypotheses named (the MFP-injectivity paragraph at line
959 is a model of this — it states the theorem's exact hypotheses, the
transfer argument, and immediately fences what it does *not* show). Defect 1
is the one place the taxonomy itself breaks: two rows sit in the "believed
unreachable, each by a stated theorem" column that the paper's own body text
disclaims as non-theorems (one explicitly, "not a theorem"; the other by
admitting a future computation could move it), and this is exactly the kind
of self-undermining a hostile referee is trained to find first, because it
is the paper grading its own rigor incorrectly in the one place a reader is
told to trust the grading absolutely. Defect 2 (the stale "non-vacuity is
open" appendix row) is the same failure mode at the mechanical level — the
paper's generation pipeline did not catch that a new result (B1418's
five-member, class-and-tower positive) contradicts an old row it left
standing six lines above it.

On completeness of the record's recent results: the S10 edits correctly
harvest the two big new facts from `frontier/B1417` (the region-swap lemma,
closing the fc census) and `frontier/B1418` (the index fires in
characteristic zero on five class members plus $t12839$, the object's own
degree-4 cover) into the abstract, §chirality, the falsifiers, and the
appendix — nothing from those two records is misrepresented in isolation,
and every number I checked against its source file matched exactly (the
census counts, the MFP theorem statement, the nine-member correction, the
apex/η-Majorana design). The one place completeness slips is upstream of
S10: `frontier/B1416`'s explicit "18 skipped" caveat on the 112-family
door count did not travel into the paper (defect 3), even though the
paper's own base-rate paragraph exists specifically to pre-empt exactly this
kind of "does the number check out" scrutiny.

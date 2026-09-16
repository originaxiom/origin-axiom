# Hostile overclaim audit of papers/P3_THE_PAPER/main.tex

Lens: overclaim. Read main.tex in full (1671 lines, working tree of 2026-09-16). Every
"theorem / exact / identically / forced / unique / first / proved / never / cannot /
impossible / always" was checked against its lock or source; every count and percentage in
the prompt's list was checked against frontier/<arc>/FINDINGS.md, tests/, or the generation
scripts. No file edited; no computation over ~2 minutes was run (four short read-only
verification agents were dispatched to grep/read frontier records and re-run the repo's own
`scripts/checks/paper_chain_table.py` and `paper_provenance.py`, each finishing in well under
the limit).

**Headline finding.** Every number I could trace to a computational source — 145/400,
124/400, the class-count partition 255/124/14/4/2/1, 1696/5000, 59/35/18 of 112, 181/203123,
20/212641 and 2/4000 (with the 3996-of-4000 partition reconciled against a real max-vs-attain
distinction in the source), 87 covers/66 chiral/9+1+77, 2804/2794/7/3, 19624 vacua, 706464
lines, 34752/31488/768 (nested correctly), 273/50/17, 34/29 (stabiliser dims), 12/4
(order-four torus elements), 252/222/2 (the "$\binom{10}{5}$" is a correct multichoose
identity, not an error), 352 = 16×22, 23/22, 216-cell/18/384, 128 involution classes, and the
"about fifty" standard deviations (49σ against the experimental error, not the loop-truncation
band) — **matches its source exactly**. The paper's arithmetic-on-data is clean. What survives
this audit is not the physics or the census computations; it is a set of places where the
paper's own hand-written prose has drifted out of sync with its own machine-generated
machinery, plus a handful of register/precision slips. That drift is the substance of this
report.

---

## FATAL

### F1 — The chain's own headline count contradicts itself, and this is a recurrence of a defect the paper was already told about

**Quoted, main.tex:446** (scopenote "Recorded in advance"):
> "a derivation that reaches Standard-Model \emph{structure} through **fifty forced links** and
> then fails, provably and by its own sealed criterion, to reach Standard-Model \emph{values}"

**Quoted, main.tex:542** (Non-claims):
> "that every one of the chain's **fifty forced links** is stated in this paper in checkable
> form"

**Against, main.tex:222** (§3 opening, hand-written prose):
> "There are \textbf{fifty-six links}. ... So **fifty-two** of fifty-six links are forced"

**Against, main.tex:292** (figure caption) and **:367** (auto-generated tally, "do not
hand-edit") and **:1494** (auto-generated appendix line):
> "**Fifty-two** links are forced." / "totalling 56 links, of which \textbf{52} are not axioms"
> / "the chain is 56 links, **52** of them forced"

**Why it fails.** This is not a matter of interpretation: I hand-counted the 56 rows of the
paper's own longtable (lines 308–363) by type and got Theorem 35, No-go 8, Identity 6, Axiom
4, Census 2, Corollary 1 — summing to 56, with 52 non-axiom — which is exactly what
`scripts/checks/paper_chain_table.py` computes live from `docs/THEOREM_LEDGER.md` (confirmed
by direct execution: `forced: 52`, `axioms at: [3, 4, 5, 18]`). So "52" is unambiguously the
number the paper's own data supports, and "fifty" at lines 446 and 542 is unambiguously wrong
— a leftover from before links 55–56 (the no-go and the census that this very audit's sibling
lens is likely to have been asked about) were added, taking the chain from 54/50 to 56/52. The
aggravating fact: `papers/P3_THE_PAPER/reads_s10/honesty.md` (a prior hostile read of an
earlier draft, still on disk) already caught this exact defect when it read "fifty-four
links... fifty forced" at the *same* two locations that now read "fifty-six... fifty-two" at
lines 222/285/292 — i.e. that draft's Defect 1 was partially repaired — but **the repair missed
lines 446 and 542**, so the identical self-contradiction is still live in the current working
tree. A referee who has seen this paper before (or who reads §3 once and the wall once) hits a
flat "50 vs 52" contradiction inside a document whose own §3 boasts, three pages earlier, that
"the tally beneath the table is recomputed from the table, not copied from the paragraph above
it ... which is how two mis-parses were caught" (main.tex:298–301). Catching your own drift
once and then having it reappear elsewhere is exactly the failure mode that sentence claims to
have eliminated.

**Minimal repair.** At line 446, "fifty forced links" → "fifty-two forced links". At line 542,
"fifty forced links" → "fifty-two forced links". Grep the whole file for the literal string
"fifty forced" before the next submission; there is no reason for this number to be spelled out
by hand anywhere outside the generated blocks.

### F2 — The paper's own showcase figure still draws 54 links after the caption was fixed to 56

**Quoted, main.tex:268–269, 283–284** (the tikzpicture body):
> `\draw[thick] (0.6,0) -- (54.4,0);`
> `\foreach \i in {1,...,56} \draw[black!55] (\i,-1.15) -- (\i,1.15);`
> ...
> `\node[font=\scriptsize] at (0.6,-3.6) {$C_1$};`
> `\node[font=\scriptsize] at (54.4,-3.6) {$C_{54}$};`

**Against, main.tex:285–292** (the caption, already patched to match the current chain):
> "The chain's fifty-six links... Fifty-two links are forced."

**Why it fails.** The tick-mark loop was updated to `{1,...,56}`, but the drawn axis line still
stops at x = 54.4 and the end-label still reads $C_{54}$, not $C_{56}$. As typeset, the figure
will show two tick marks (55, 56) standing past the end of the drawn chain line, labelled with
an endpoint two links short of what the caption underneath it claims. This is the same F1 drift
manifesting in the one piece of the paper most likely to be looked at first (a referee scans
figures before prose), and it is exactly the kind of "pixel-accurate to the table" fix that
`reads_s10/honesty.md`'s Defect 1 already flagged as cosmetic-but-real and that was not carried
through.

**Minimal repair.** Change `(54.4,0)` to `(56.4,0)` (or the equivalent unit step used
elsewhere) and `$C_{54}$` to `$C_{56}$`; re-check the axiom tick positions (3,4,5,18) and the
shaded "twelve links, no declared choice" band (5.5 to 17.5) are unaffected — they are, since
neither depends on the total length.

---

## SERIOUS

### S1 — The appendix grades a row "settled" while the very same cell says it is "not a theorem"

**Quoted, main.tex:1524** (generated provenance appendix, "Backing" column = settled):
> "the exact half of the closing design: the E7 apex local model's geometry (its count cited),
> the $\Z/3 = 2T/Q_8$ forcing $b_2 \ge 2$ for a symmetric triple, the $Y_3$ breaking to
> $\mathrm{SM}\times\mathrm{U}(1)_\eta}$ by a $Q_8$ line times an order-4 character (root-system
> facts), and the algebraic no-seesaw obstruction (...) --- **the design itself and its
> exclusion are conditional, a design and not a theorem** & **settled** & lock"

**Against the appendix's own rubric, main.tex ~1455–1459:**
> "\textbf{Settled} means the establishing result is itself closed --- proved, or a negative
> --- and the claim rides on that."

**Why it fails.** This is a direct, single-row self-contradiction, and it is a *regression* of
sorts: `reads_s10/honesty.md` Defect 4 flagged the same row (in an earlier draft) as "settled"
while the body called it "not a theorem" — a cross-section inconsistency. The current draft's
fix was to append the caveat "a design ... not a theorem" **into the claim cell itself**, which
correctly imports the body's honesty, but the adjacent Backing-column verdict was left as
"settled" — so the row now contradicts itself in one line rather than across two sections. By
the appendix's own printed definition, "settled" is reserved for a closed, proved-or-negative
result; a self-described "design, not a theorem" cannot satisfy that definition no matter how
carefully verified its individual steps are (and the body, main.tex:989, is explicit: "This
paragraph reports a design verified step by step, not a theorem"). A hostile referee reads the
appendix as the paper's own honesty-audit table and will treat a self-contradicting cell there
as the table failing its own test.

**Minimal repair.** Change the Backing column for this one row from "settled" to "computed
(enquiry open)" — the same grade already used elsewhere in the same table for other
conditional/non-theorematic rows (e.g. the "252 candidate contents" row, main.tex:1498).

### S2 — A load-bearing count ("the seven") has no antecedent anywhere in the paper's own text

**Quoted, main.tex:956** (end of the index paragraph in §\ref{sec:chirality}):
> "The rule that separates the members that fire from **the seven** that do not is not known."

**Why it fails.** The paper names exactly five class members that fire (s958, v2873, t12833,
t12835, o10\_150701), plus the object's own degree-four cyclic cover t12839, plus the census
control m010 — it never states a total population from which "seven" could be read off, so a
reader cannot verify or even locate "the seven" from the paper alone. I traced the source:
`frontier/B1418_the_family_as_the_object/FINDINGS.md` states "**Five of the eleven** class
members with root-of-unity loci fire" (so six of eleven do not) and separately speaks of "the
pattern across the **seven** non-firing members," which is consistent only if that seven counts
the six non-firing class members *plus* m004 itself (whose golden-locus modules also all
returned zero, stated two sentences earlier in the paper at the same location). That
reconciliation is defensible on the source, but it depends on a number — "eleven" — that never
appears anywhere in main.tex. This is exactly the "hedge that hides a claim" this lens is asked
to flag: the number is correct, but the paper's own stated commitment to full traceability
(every load-bearing claim "listed [in the appendix] against the record that establishes it,
together with how it is checkable," main.tex:1450–1452) is not met for this one clause, because
no reader without repository access can check it.

**Minimal repair.** Either state "eleven" explicitly ("...the seven that do not — six of the
eleven class members with root-of-unity loci, plus $m004$'s own golden locus — is not known")
or drop the specific count and say "the members that fire from those that do not," which the
sentence does not actually need a number for.

---

## MINOR

### M1 — A deterministic identity is reported as a probability

**Quoted, main.tex:132–133:**
> "conditioned on the appearance of a single ADE label, the probability that it 'recurs' across
> the others is $1$. There is no coincidence to explain."

**Why it fails.** The four faces (McKay, Lie classification, modular-invariant list, du Val
singularities) are stated two sentences earlier to be "one ADE classification presented four
ways, canonically linked" — i.e. a mathematical identity, not a random variable with a
computed probability. Casting a tautology as "probability 1" borrows the register of the
paper's genuinely statistical census claims (the 145/400, 1696/5000 numbers, which really are
frequencies) and blurs the line between "we measured a base rate" and "this cannot fail to be
true," which is exactly the distinction §\ref{sec:generic} exists to police.

**Minimal repair.** "the probability that it 'recurs' across the others is 1" → "it recurs in
all four, necessarily, since the four are one classification and not four independent
observations."

### M2 — "Roughly one in three" is used for two different statistics without saying which

**Quoted, abstract, main.tex:43–44:**
> "on a census of one-cusped manifolds..., roughly one in three admits the surjection onto the
> binary tetrahedral group that the construction starts from"

**Against, main.tex:149, 155** (body): 145/400 = 36.25% *admit some surjection*; 124/400 = 31.0%
*admit exactly two* (the object's own count); the body's summary line reads "Roughly one
hyperbolic 3-manifold in three carries the fact that carries the chain" (referring to the
124/400 = 31% figure specifically, i.e. the exactly-two count, not the "admits any surjection"
count).

**Why it fails.** Both figures round to "roughly one in three," so the abstract's sentence is
not false under either reading, but it does not say which of the two distinct statistics
("admits a surjection" vs. "admits the object's own count of exactly two") it means, and the two
differ by five points (36.25% vs. 31.0%) — a difference the body itself treats as worth stating
to two decimal places. A paper this insistent elsewhere on "we give it exactly rather than
approximately" (main.tex:146) should not let its abstract's one summary number float between
two non-identical quantities.

**Minimal repair.** In the abstract, specify "...roughly one in three admits *some* surjection
onto the binary tetrahedral group, and very nearly one in three admits exactly the object's own
count of two" (or just cite the 124/400 figure, which is the one actually load-bearing for
"the fact that carries the chain").

### M3 — The Standard Model's free-parameter count ("twenty-four with the neutrino sector") is stated without its counting convention

**Quoted, main.tex:1118–1119** (opening of the freedom ledger):
> "The construction supplies \textbf{none} of the Standard Model's nineteen free parameters
> (twenty-four with the neutrino sector, the count link 17 of \S\ref{sec:chain} uses)"

**Why it fails.** 19 (no neutrino sector) is the standard literature figure and is uncontested.
"Twenty-four with the neutrino sector" is a real but non-universal count — the commonly quoted
figures for Dirac-only neutrinos are 19+7=26 (3 masses, 3 PMNS angles, 1 phase); reaching 24
requires a specific convention (e.g. omitting one angle or the phase, or a different
partitioning) that is not stated here or, as far as I could locate by grep, spelled out
anywhere the paper cites. This is not shown to be wrong, only unaudited: a number this
foundational to the freedom ledger's "the trade is negative" framing deserves the convention
named, especially given the paper's general practice of naming conventions for every other
count (e.g. "level 4 in the SL-kernel convention" two sections later).

**Minimal repair.** Add a footnote or clause naming which 24-parameter convention is used
(what is included/excluded relative to the more common 26), or drop the parenthetical if it
cannot be sourced to a named convention.

### M4 — The chirality section's opening promise ("a theorem ... or an exhibited computation") is stretched by its own closing design paragraph

**Quoted, main.tex:876–877** (section opening):
> "Everything in this section is a theorem with a lock or an exhibited computation, and the
> section exists to say \emph{where} the bit is withheld rather than to report that it is."

**Against, main.tex:989** (the three-apex design paragraph, same section):
> "This paragraph reports a design verified step by step, not a theorem, and it is the closest
> the record comes to saying what a closing that carries the bit must be."

**Why it fails.** The section's opening sentence offers a closed binary — theorem-with-a-lock,
or exhibited computation — and a design that is itself "excluded as it stands" (a negative
verdict on a candidate model, arrived at by verifying several of its steps and finding one
fails) does not comfortably sit in either bucket unless "exhibited computation" is read broadly
enough to include "a multi-step design whose individual facts were computed but whose overall
status is explicitly not that of a theorem." The paragraph is honest about its own status, and
S1 above shows the appendix's version of the same content is where the tension actually breaks;
here it is only a stretch, not yet a contradiction.

**Minimal repair.** Soften the section's opening to "a theorem with a lock, an exhibited
computation, or (in one place) a design stated as such," matching the actual content.

---

## (a) The single strongest objection to the paper as a whole, and does the paper already answer it

The strongest objection a hostile referee would raise is not about the physics content but
about the paper's *self-auditing apparatus*: this is a 24,000-word document whose central
rhetorical move is "trust our counting because we built machinery that recomputes it" (the
generated chain table, the generated provenance appendix, the three-column ledger, the
non-claims section), and yet that very apparatus is caught, in this working tree, disagreeing
with itself in at least four places (F1, F2, S1, and — more mildly — S2), one of which
(F1/F2, the 54-vs-56/50-vs-52 chain count) is a *recurrence* of a defect a prior hostile read of
an earlier draft already found and only partially fixed. If the paper cannot keep its own
headline "fifty-two of fifty-six links are forced" straight across five mentions in its own
text, a referee's confidence that the harder numbers — 706,464 Standard-Model lines, a
19,624-vacuum count, a 34/29 stabiliser-dimension split — have been checked with equal care is
undermined by association, even though (as this audit independently verified against
frontier/*/FINDINGS.md and by executing the paper's own generation scripts) every one of those
harder numbers in fact checks out exactly. The paper does *not* explicitly answer this
objection — nothing in the text acknowledges that its own hand-written prose lags its generated
tables — but its *practice* implicitly answers a weaker, more important version of it: the
generation scripts (`paper_chain_table.py`, `paper_provenance.py`) are real, run cleanly, and
do independently re-derive the counts they claim to, which is the substantive thing a referee
should actually care about once the prose is patched to match them.

## (b) What the referee would say the paper actually proves, and does the abstract say the same thing

In one sentence: the paper proves that, *given* three pre-object axioms (a description
principle, a geometric carrier, and an orientation choice), a post-object observer axiom, and a
short list of finite/continuous inputs it tabulates itself, the figure-eight knot complement's
invariant trace field and the McKay-forced $E_6$ algebra yield a derived hypercharge direction,
a derived $\Z_6$ global form, and a chirality-blind ("vector-like") Standard-Model-shaped gauge
sector — together with an unusually thorough, mostly exhaustive set of negative results showing
that no numerical Standard-Model value, scale, or generation count is recoverable from the
object by any route checked so far. That is a conditional structural correspondence with a
priced list of inputs, not a derivation of physics, and not a parameter-free theory. The
abstract says essentially the same thing, and does so more carefully than the section titles
("What is forced," "What is unique") alone would suggest: it explicitly separates arena from
content, states the four-axiom/one-observer-axiom structure, gives the exact negative-search
counts, and ends by naming the freedom ledger as "the honest summary of the paper." The one
place the abstract's phrasing runs slightly ahead of the body's own bookkeeping is the "fifty
forced links" wording shared with the two non-claims/scopenote instances flagged as F1 above —
which is precisely the register the abstract otherwise gets right everywhere else.

# Referee report — handling referee, J. Phys. A / IJMPA

Manuscript: "Standard-Model structure from the figure-eight knot complement: what is forced, what
is withheld, and what must be supplied" (main.tex, working tree of 2026-09-16, ~24.6k words, 1671
lines).

Recommendation up front, because a referee owes the editor that before the detail: **major
revision, borderline reject on length and verifiability grounds**, not because the mathematics is
wrong wherever I could check it (it is, as far as hand-checking goes, internally arithmetically
consistent everywhere I tested it), but because the manuscript as submitted cannot be refereed in
the normal sense for the majority of its claims, and because it is roughly twice the length a
paper with this genre and this much repetition needs to be.

---

## FATAL

**F1. Verification depends on software this manuscript does not, and cannot, put in front of a
referee.**

> "A 'script' is a \texttt{verification/reproduce.sh} inside the named record; a 'lock' is a file
> under \texttt{tests/} that runs with the suite." (line 1481–1482)

> "'lock' below means a test that names the establishing result; it does not yet mean a test that
> re-asserts the specific number quoted in this paper's body. Strengthening that is work in
> progress, and until it is done the column should be read as \emph{traceability}, not as
> independent re-derivation." (lines 1473–1476)

Of the appendix's 54 rows (75 claim–record pairs), only 6 ship a standalone re-running script
(line 1547); the rest are "settled: lock" or "computed: script + lock," where "lock," by the
paper's own admission just quoted, frequently only *names* the result rather than re-checking the
number. The companion verification package (`papers/P3_THE_PAPER/verification_package/README.md`)
confirms the cost of actually trying: a pinned Python 3.12 stack (snappy==3.3.2, sympy, mpmath,
numpy, scipy, python-flint, pytest), "about five minutes" for the lock set alone, and "several
thousand tests" for the full suite. This is not a criticism of using code — computational number
theory papers routinely do — it is that of 56 chain links and 54 appendix claims, exactly two
pieces of mathematics are actually carried out in the paper where a referee can check them by hand:
the hypercharge cubic (lines 719–731, and it does check out) and Proposition 1's proof
(478–516, also checks out). Everything else — the McKay hand-off, the 3003-pair magic-square
isomorphism, the census percentages, the index computations that carry the paper's own headline
negative result — is asserted on the authority of a repository the reader must clone, configure,
and run for an unspecified but non-trivial amount of time, and even then most of what comes back is
"traceability," not a re-derivation of the quoted number.

Worse, the paper's own appendix records that this apparatus has already certified something false
and had to walk it back: "a lock is traceability, not re-derivation --- in one recorded case a lock
pinned a family-wide claim that was later withdrawn" (lines 1464–1465), which is exactly the
family-wide amphichirality claim retracted in the footnote at line 1044 ("38 of the family's 112
members are amphichiral, not all"). A verification system that has already shipped one wrong
"settled: lock" claim to a public draft is not a substitute for in-text proof of the claims this
paper asks a referee to accept.

*Minimal repair*: either (a) promote three or four of the most load-bearing computational claims
(the McKay/E6 hand-off, the magic-square isomorphism, the geometric-holonomy index vanishing, the
one non-trivial census count the title thesis rests on) to fully worked appendix derivations that a
referee can check without running code, or (b) submit this as a paper with a clearly-labeled
"computational appendix," the way a JHEP or PRD submission would, and state plainly in the paper
(not only in the external README) that the majority of claims are certified only by the authors'
own, previously-fallible, private test suite.

**F2. The paper's own three-way epistemic ledger — the exact instrument this referee was asked to
check — contradicts itself.**

> "\emph{Parameter-free, and had}: ... the two conjugations that kill the index on the cyclic
> tower; the theorem that the geometric finite-twist index vanishes on every one-cusped manifold;
> the exhibited non-zero index on the class and on the tower ... \emph{Believed unreachable, each
> by a stated theorem}: ... a chiral spectrum from the geometric holonomy on any one-cusped
> manifold (injectivity) ... or from the cyclic tower (the two conjugations) ..." (line 1432, "The
> ledger in three columns")

The identical results — the geometric-holonomy index vanishing (Menal-Ferrer–Porti injectivity)
and the "two conjugations" that kill the index on the cyclic tower — are listed in **both** the
first column ("Parameter-free, and had," i.e. established, closed, positive) and the third column
("Believed unreachable, each by a stated theorem"). That is not a subtle double-count: the third
column's own header is self-contradictory on its face — "believed" is the paper's weakest epistemic
word, reserved throughout the manuscript for conjectural or unresolved claims (e.g. "the universal
form ... is the conjecture that evidence supports," line 954), yet every entry under it is
qualified "each by a stated theorem," i.e. proved. "Believed X, by a stated theorem" is not a
coherent epistemic status; it is either believed (open) or proved (closed), and this section's
entire job is to keep those two categories apart for the reader. Since the paper repeats twice more
that the residue is organized into exactly parameter-free/not-yet/believed-unreachable rows (§13,
"the ledger in three columns," is presented as the paper's culminating summary), a reader cannot
extract from this table which of the paper's negative results are proved and which are conjectured
— which is precisely the distinction the whole manuscript claims to have earned the right to draw.

*Minimal repair*: rename the third column (its actual content is "excluded, by a stated theorem, in
every channel checked" — a proved negative, not a belief), and delete the duplicated items from
whichever column they do not belong in; a proved no-go about the object's own reach belongs in one
place, not both.

**F3. A chain-table entry labeled "Theorem" is explicitly conceded, in the same paragraph, not to
meet even the paper's own standard of external check.**

> Table, link 9: "the manifold group is congruence (level 4 in the SL-kernel convention; geometric
> index 12 at level 8)" (line 316, type: **Theorem**)

> "The manifold group is congruence (level $4$ in the $\mathrm{SL}$-kernel convention, geometric
> index $12$ at level $8$; C9) --- a statement that defies Serre's non-congruence base rate,
> computed twice on our own benches and not yet checked against the literature." (lines 563–564)

Section 3 builds its entire rhetorical structure on the claim that the chain has "thirty-five
theorems ... and four axioms. So fifty-two of fifty-six links are forced, in the precise sense that
they are not declared choices" (line 222) — i.e., "Theorem" is being used as the paper's strongest
type label, contrasted explicitly with "axiom" (a declared choice) and, in the appendix, with
"computed (enquiry open)" (an internally re-derived but not fully settled result). Link 9 is typed
"Theorem," yet the body text describing it says outright that it has been "computed twice on our
own benches and not yet checked against the literature" — i.e., it is not settled by any external
standard, only internally cross-checked. This is exactly the "theorem stated without having met its
own paper's bar for a theorem" defect the lens for this review calls out, and it sits in the twelve
links (6–17) the paper repeatedly holds up as its cleanest, choice-free stretch (Figure 1's caption,
lines 285–290).

*Minimal repair*: retype link 9 as the paper's own "computed (enquiry open)" category until an
external congruence-subgroup check is run, or state the caveat inside the chain table itself, not
four hundred lines away in a paragraph a reader of the table alone will not see.

---

## SERIOUS

**S1. "The termination is the theorem" is asserted, then the theorem's own completeness is
disclaimed one scopenote later.**

> "\paragraph{The cascade terminates, and the termination is the theorem.}" (line 765, section
> head)

> "the underlying result fences itself: it is not exhaustive over exotic conformal embeddings, and
> it imports a menu-completeness claim whose stage-level formalisation is still owed." (lines
> 780–782)

Calling a result "the theorem" in a bolded section head and then, sixteen lines later, admitting
its "stage-level formalisation is still owed" is a hedge that hides a claim: the reader who quotes
this paper's abstract-level summary ("the termination of the breaking chain" is squarely in the
"parameter-free, and had" column at line 1432) will not carry the caveat with it. This is exactly
the pattern the paper itself warns against in its own method (§Recognition, "we reproduce it; we do
not claim it"). *Minimal repair*: retitle the paragraph "the cascade terminates, and the
termination is an argument, not yet a theorem" or move the formalisation caveat into the same
sentence that first uses the word "theorem."

**S2. The abstract is roughly three times the length a J. Phys. A / IJMPA abstract should be, and
this alone risks a desk rejection independent of content.**

The abstract (lines 40–77) runs to approximately 650–700 words of prose (before LaTeX markup is
stripped). Both target venues expect an abstract in the 150–250 word range; this one is long enough
that it functions as an executive summary of the whole paper rather than an abstract, duplicating
material that reappears near-verbatim in §13 ("the ledger in three columns," line 1432) and in the
freedom-ledger preamble (line 1118). *Minimal repair*: cut the abstract to the actual claim (one
paragraph: what survives genericity, what is forced given two stated inputs, what is proved
withheld, where the chirality bit is located) and move the numeric inventory (352 pairs, 216-cell
grid, etc.) to the body, where it already lives.

**S3. Section order front-loads the paper's most specific technical claims into the "Non-claims"
list before any of the vocabulary is introduced.**

> "Three structural copies of the Standard-Model content are exhibited on the object's own
> closings, in mirror pairs; they are vector-like; \S\ref{sec:chirality} proves the bit withheld by
> the object at every computed sector..." (Non-claim, line 534, immediately after §3 "The chain")

At this point in the paper the reader has not yet been told what a "closing" is (defined properly
only at line 958, in §8), has not seen "mirror pairs" used in this technical sense, and has not
reached the chirality section at all. A referee reading top-to-bottom, as instructed, hits a
paragraph of highly specific negative claims about machinery that does not yet exist for them. The
introduction (§1) explicitly defends an inverted order for the *positive* material ("we therefore
invert the usual order," line 103) but does not extend that design to the Non-claims block, which
reads as pasted in ahead of its own referents. *Minimal repair*: move "Non-claims" to immediately
before §13 ("The wall"), or add one clause to each forward-referencing item pointing the reader to
its definition ("closings, defined in §5").

**S4. The index computation — the paper's single most load-bearing technical result — is worded so
that "the index vanishes on the cyclic tower" and "the index is non-zero on the object's own
degree-four cyclic cover" sit nine sentences apart without an explicit sentence telling the reader
these are different instruments applied to the same manifold.**

> "Two theorems make it vanish on the whole cyclic tower... Sixty-one sectors on the three- and
> four-fold covers vanish..." (lines 942–950)

> "then...on five one-cusped chiral members of the object's own commensurability class...and on the
> object's own degree-four cyclic cover $t12839$, at their cusp-trivial characters of order three
> among others." (line 956, reporting the index **non-zero**)

The two statements are not in fact contradictory — the first concerns $V=\mathrm{Sym}^m(h)\otimes
F$ built from the *geometric holonomy* $h$; the second concerns reducible, non-split modules
$\mathrm{Sym}^m(\rho_\chi)\otimes\psi$ at root-of-unity characters $\chi$, an entirely different
class of local system — and the paragraph does eventually say so ("What fires is
non-semisimplicity...rather than the geometric structure," same paragraph). But this
disambiguation arrives roughly 700 words after the reader has already been told, twice, that "the
index" vanishes "on the whole cyclic tower," and $t12839$ is explicitly a member of that same
cyclic tower. A referee under any time pressure could reasonably flag this as an internal
contradiction before finding the resolving clause. *Minimal repair*: state up front, in one
sentence, that "the index" names two distinct instruments on two distinct module classes before
giving either result, not after both.

**S5. Undisclosed "we" and undisclosed computational apparatus for a solo-authored paper.**

The byline is a single "Independent Researcher" (line 31), yet the paper's voice is uniformly
institutional: "our own accounting grades them" (line 191), "computed twice on our own benches"
(line 564), "an audit of the executable statement of the argument confirms it" (line 699), "the
record's own re-test" (line 161). None of "the record," "our own accounting," or "our own benches"
is ever identified as a person, a team, or a specific tool — the reader cannot tell whether "we"
denotes co-authors not on the byline, an internal automated pipeline, AI-assisted derivation and
verification, or an editorial plural. A referee is entitled to ask what performed the "audit" whose
say-so is the paper's only certificate for dozens of claims (see F1), and most 2026-era journal
policies require some disclosure of automated or AI-assisted verification tooling if any was used.
*Minimal repair*: one sentence in the acknowledgements or methods stating what "the record" is (a
named software repository, presumably) and by whom and how it was run.

---

## MINOR

**M1. "The record" is used at line 161 (and again at 386) roughly 400 lines before its only formal
definition, at line 555 ("\emph{the record} means the project's re-runnable record to which the
appendix maps each claim"), a textbook case of a term used before it is defined.** *Minimal
repair*: define it in a footnote at first use, or in the introduction.

**M2. "Chirality" is used in two senses — knot/manifold amphichirality (an orientation-reversing
isometry, used throughout §2's base rates, e.g. line 175, "Chirality runs the other way: 181 of the
203,123...") and matter/generation chirality (net difference of the $27$ and $\overline{27}$
cohomology, the sense the whole of §8 is about) — well before the reader is told (only at line
882's scopenote and line 891's paragraph) that these are different things. A reader who takes §2's
"the object carries the generic value 4" and "the requirement the object fails" at face value before
reaching §8 will import the wrong intuition about which chirality is at stake.** *Minimal repair*:
one clause in §2 flagging that "chirality" there means geometric amphichirality, with the matter
sense deferred to §8.

**M3. Redundant recapitulation.** The residue/freedom-ledger material is presented in full three
times: the abstract's final paragraph (lines 74–77), the freedom ledger of §10 (lines 1115–1262),
and "the ledger in three columns" of §13 (line 1432, itself a single ~500-word paragraph). Each
telling adds detail the others lack, but none is strictly a subset of another, so a careful reader
must reconcile three overlapping tellings of the same accounting to be sure nothing changed between
them. *Minimal repair*: keep one full table (§10) and reduce §13's paragraph to a one-line pointer
plus only what is new (the three-column re-sorting).

**M4. Section 8 ("The chirality bit," lines 874–1034) is, at roughly 2,600 words of dense
notation-heavy prose in a single unbroken run of paragraphs with no subsections, long enough and
self-contained enough to be its own paper; folding it into this manuscript as one section among
thirteen buries its content and makes the whole manuscript harder to referee as a unit.** *Minimal
repair*: subsections within §8, at minimum ("What is counted," "The frame," "The index," "The
closings," "Where the bit lives," "The tower").

---

## (a) The single strongest objection, and does the paper already answer it

The strongest objection is that this manuscript is, for all but a handful of its results,
unrefereeable from the document itself: the load-bearing claims — the McKay/E6 hand-off, the
magic-square isomorphism on 3003 basis pairs, every census percentage, and above all the index
computations that carry the paper's central negative result about chirality — are certified only by
an external, private, versioned software pipeline that requires a pinned environment and, by the
package's own README, "several thousand tests" to run in full, most of whose "locks" the appendix
itself admits are "traceability, not independent re-derivation." The paper is aware of the
verification problem in a narrow, admirable sense — it distinguishes "settled" from "computed
(enquiry open)," documents its own history of retracted claims with unusual candor, and even
records that its own lock system once certified a claim (family-wide amphichirality) that had to be
withdrawn — but candor about the problem is not a solution to it. The paper does not answer the
objection: apart from the hypercharge cubic and Proposition 1, it never reproduces enough of any
hard computation in-line for an outside referee to check a representative sample by hand, and it
offers no route to verification that does not run through the authors' own, previously fallible,
tooling.

## (b) What the paper actually proves, and does the abstract say the same thing

Stripped of its hedges, the paper establishes three things: (i) a chain of largely classical facts
connecting the figure-eight complement's commensurability class to an $E_6$ magic-square algebra via
the McKay correspondence, which the paper's own census shows is generic rather than special to this
particular manifold; (ii) that anomaly cancellation, granted an assumed Standard-Model-shaped
matter assignment and an assumed choice of colour subalgebra (both conceded as inputs, not
derived), forces the direction of hypercharge and the $\Z_6$ global form and forces the breaking
chain to terminate at the Standard-Model algebra; and (iii) an extensive, largely computational
demonstration that neither a numerical Standard-Model value nor a genuinely chiral (as opposed to
vector-like) fermion spectrum can be extracted from the object's own geometric and arithmetic data
by any channel checked so far, with the remaining freedom catalogued in a ledger. The abstract does
say essentially this, and unusually for a manuscript this dense it keeps most of the same
qualifiers intact (the axiom count, the genericity base rates, the vector-like character of the
three exhibited copies, the homogeneity no-go for the hypercharge scale) — on faithfulness of claim
to claim, the abstract is one of the more honest parts of the paper. Its failure is one of form, not
content: at roughly 700 words it is long enough to function as a second introduction rather than an
abstract, and a referee's first substantive note to the editor would be that it needs to be cut by
two-thirds before the paper can be read as making one legible promise.

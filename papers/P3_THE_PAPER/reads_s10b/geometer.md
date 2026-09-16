# Hostile referee report — LENS: geometer (hyperbolic 3-manifolds, arithmetic Kleinian groups, covers/commensurability)

Target: `<home>/origin-axiom/papers/P3_THE_PAPER/main.tex`, working tree of 2026-09-16. Repo cross-checked
under `frontier/` and `docs/` where a claim's own source could be located; no computation over ~2 minutes
was run. I attack only the geometric/arithmetic content — census counts and their populations, theorems
attributed to the literature, cusp/isometry/covering data, and the index `I = t_0 - r_1`.

---

## FATAL

**F1. The uniqueness theorem the "genesis selects the member" argument rests on cites a paper I cannot
place in the literature of Kleinian groups.**
- Quote (line 1091): *"The genesis selects the member: $m004$ is the unique orientable solution of a
  minimisation, its Jørgensen number being exactly one~\cite{jorgensen,callahan}, and that selection is
  variational where every earlier selection story was descriptive."*
- Also line 1319: *"Jørgensen's inequality and Callahan's uniqueness~\cite{jorgensen,callahan}: that the
  figure-eight complement is the unique orientable manifold attaining Jørgensen number one is Callahan's
  theorem."*
- Bibliography: `\bibitem{callahan} J.~Callahan, \emph{J\o rgensen number and arithmeticity}, Conform.\
  Geom.\ Dyn.\ 13 (2009), 160--186.`
- Why it fails: Jørgensen's inequality itself (`\cite{jorgensen}`, Amer. J. Math. 98 (1976)) is real and
  correctly cited. But I have no record, in the Kleinian-groups/hyperbolic-geometry literature I know, of
  a 2009 paper in *Conformal Geometry and Dynamics* by a "J. Callahan" titled "Jørgensen number and
  arithmeticity" proving that the figure-eight knot complement is the unique orientable hyperbolic
  3-manifold attaining the extremal value 1 in Jørgensen's inequality. The extremal-value phenomenon for
  Jørgensen's inequality is genuinely studied in the literature (Gehring–Martin and collaborators have a
  long series of papers on "Jørgensen's inequality for..." and on the geometry of the extremal locus), but
  the specific attribution here — journal, volume, page range, and a "Corollary 2.4" quoted verbatim
  elsewhere in the repository's own audit trail (`frontier/B1413_.../DOC_JORGENSEN_SOURCE_AUDIT_2026-09-13.md`)
  — is exactly the shape of a citation that a referee checking references would try to pull and might not
  find. The repository's own audit of this citation (same file) is itself internal ("not a new physical-
  spectrum calculation... an owner-requested literature/reception audit"); the paper's front matter states
  "all verification reported here is internal... no external review or endorsement is claimed" (line 77),
  which is precisely the condition under which a hallucinated or misremembered citation would survive
  unnoticed through several internal passes.
- This is load-bearing, not decorative: it is the only argument in the whole paper that the *manifold*
  m004 (not merely its commensurability class) is picked out by anything other than a base rate, and the
  Recognition section (line 1319) presents it as an established fact of the literature rather than as an
  internally-computed conjecture. If the citation does not check out, the "variational, not descriptive"
  upgrade claimed in the abstract-adjacent "Which member" paragraph (line 1091) has no external support at
  all — only the raw number `J(m004)=1`, which is a computation, not a uniqueness theorem.
- Minimal repair: verify the citation against a library catalogue (MathSciNet/zbMATH) before submission. If
  it cannot be found, either (i) replace it with a citation that actually proves the uniqueness (Gehring–
  Martin's extremal-locus papers are the right place to look), or (ii) demote the claim from "Callahan's
  theorem" to "we conjecture, on the evidence of a census search, that..." and move the whole "Which
  member" argument out of the "parameter-free, and had" column of the wall's three-column ledger (line
  1432) into the "not yet had" column.

---

## SERIOUS

**S1. The abstract's citation for "a census of one-cusped manifolds" points to a paper about Dehn-surgery
volume asymptotics, not to any census.**
- Quote (line 43): *"on a census of one-cusped manifolds~\cite{snappy,nz}, roughly one in three admits the
  surjection onto the binary tetrahedral group..."*
- Bibliography: `\bibitem{nz} W.~D.~Neumann and D.~Zagier, \emph{Volumes of hyperbolic three-manifolds},
  Topology 24 (1985), 307--332.`
- Why it fails: Neumann–Zagier's 1985 paper establishes the asymptotic behaviour of hyperbolic volume under
  Dehn filling (the Neumann–Zagier potential function and the volume/length asymptotics used throughout
  Dehn-surgery theory). It does not enumerate, construct, or discuss a census of manifolds; it is the wrong
  reference for the sentence it is attached to. `\cite{nz}` is used exactly once in the whole document (I
  grepped for every occurrence), so this is not a stray duplicate of a correct use elsewhere — it is simply
  misattached. The correct reference for "a census of one-cusped manifolds" is the census literature itself
  — Callahan–Hildebrand–Weeks, *A census of cusped hyperbolic 3-manifolds*, Math. Comp. 68 (1999), or
  Hodgson–Weeks — or, if the paper means only "the census SnapPy ships with," `\cite{snappy}` alone already
  covers that and `nz` should simply be dropped.
- This sits in the abstract, which is the first thing a referee with this specialty will check against the
  literature, and it fails on inspection in under a minute.
- Minimal repair: drop `\cite{nz}` from line 43, or replace it with `\cite{chw}` (Callahan–Hildebrand–Weeks)
  with a new bibitem, whichever the actual census program used was built from.

**S2. "Elementary and long known" is asserted for a specific fact (amphichiral manifolds with chiral finite
covers) with no citation, unlike every neighbouring clause in the same sentence.**
- Quote (line 1309–1311): *"...that chirality is not a commensurability invariant is elementary and long
  known, an amphichiral manifold with chiral finite covers being standard, and what \S\ref{sec:chirality}
  adds is only its coexistence with the arithmetic on $66$ named covers..."*
- Why it fails: every other clause in that same Recognition-section bullet names its source (Sakuma,
  Neumann–Reid, Pantev–Wijnholt, Acharya–Witten, Distler–Garibaldi). This one clause, asserting that "an
  amphichiral manifold with chiral finite covers is standard," carries no reference at all. It may well be
  folklore to specialists, but a referee who works on covers and symmetry groups of hyperbolic manifolds
  will ask for the example the authors have in mind (the general phenomenon — a symmetry of the base failing
  to lift to a given cover — is standard covering-space theory, but "amphichirality does not persist to
  covers, and here is a published instance" is a stronger and more specific claim than "covering-space
  theory allows a symmetry not to lift"). As written it reads as the paper borrowing the authority of "long
  known" for a fact that, by the paper's own account two paragraphs later, is actually *this paper's own new
  count* (the 66-of-87 figure).
- Minimal repair: either name a specific published instance of an amphichiral manifold with a proven chiral
  finite cover, or reword to "the *possibility* that amphichirality fails to persist to a cover is immediate
  from covering-space theory (a deck symmetry need not lift); the *coexistence* with the arithmetic on 66
  named covers is what this paper computes," removing "elementary and long known" from the specific claim
  about existence of such an example.

**S3. The status of the manifold-vs-class distinction in the abstract elides the fact that the paper's own
uniqueness fact (F1 above) is doing more work than a plain reading suggests.**
- Quote (line 45–48): *"What survives is narrower and is a theorem of record: $m004$ is the unique arithmetic
  knot complement~\cite{reid}, and it is its invariant trace field... that the construction consumes; the
  uniqueness itself is load-bearing at no step."*
- Why it fails (not a contradiction, but an incompleteness a referee will flag): this sentence is accurate
  about the *construction's arena* (§forced onward correctly uses only the invariant trace field, per
  §unique's own careful scope note). But §chirality's whole apparatus — the count of two, the vanishing
  index, the 66 chiral covers — is stated and computed *for the manifold m004 specifically*, and the only
  argument in the paper that privileges m004 within its class for that purpose is the Jørgensen-number
  citation flagged in F1, introduced 900 lines later. A referee reading the abstract's claim that
  "uniqueness [of the arithmetic knot complement] is load-bearing at no step" could reasonably conclude that
  *no* manifold-specific selection principle is used anywhere in the paper, which is not quite true of
  §observer's "Which member" paragraph.
- Minimal repair: add one clause to the abstract or to §unique's scope note flagging that a *second*,
  independent selection fact (the Jørgensen-number extremality) is invoked once, late, specifically to
  justify working with the member rather than the class in §chirality, and that this second fact carries its
  own citation risk (F1).

---

## MINOR

**M1. The cusp-shape comparison between $m003$ and $m004$ silently changes convention without saying so.**
- Quote (line 160–162): *"What separates them is the cusp shape ($\omega$ for $m003$, in a chosen peripheral
  basis since it is not a knot complement, against $2\sqrt3\,i$ for $m004$)..."*
- Why it is worth a note (not an error — I checked the repository's own SnapPy output, e.g.
  `frontier/B718_child_program/b718_probe4.py:134`, which prints `Mc.cusp_info(0)['shape'] = 2*sqrt(3)*i`
  directly from SnapPy, so the *number* is right): the sentence explicitly justifies m003's shape as being
  "in a chosen peripheral basis since it is not a knot complement" — implying that m004, being a knot, needs
  no basis choice because its meridian–longitude framing is canonical. But the *value* quoted for m004,
  $2\sqrt3\,i$ (purely imaginary), is only the canonical shape up to the further identification $\tau \sim
  \tau + n$ (an integer change of longitude framing) or reflection, not the literal value in the 0-framed
  meridian–longitude basis some readers will expect from "canonical." The text's own logic ("m003 needs a
  chosen basis, m004 doesn't") is in slight tension with quoting a value that has already had a translation
  ambiguity silently used to simplify it.
- Minimal repair: one clause — "$2\sqrt3\,i$ (the shape modulo the longitude's integer framing ambiguity)"
  — removes the tension without changing any number.

**M2. The count "78 closed hyperbolic fillings" (correct) is never given the one-line justification that
would let a referee check it without running SnapPy.**
- Quote (line 661–663): *"of the grid's $78$ closed hyperbolic fillings, zero keep $\Q(\sqrt{-3})$..."*
- I independently verified this number by hand from Thurston's classical fact that the figure-eight knot has
  exactly ten exceptional (non-hyperbolic) Dehn fillings — the nine integer slopes $-4,\dots,4$ and the
  meridian $\infty$ — against the $87$ coprime pairs $(p,q)$ with $|p|\le 8$, $1\le q\le 8$: $87-9=78$ (the
  meridian has $q=0$ and is outside the grid, so only the nine finite exceptional slopes are subtracted).
  The number is exactly right. This is not a defect — it is exactly the kind of number a hostile referee
  should be able to reconstruct without a script, and it passes. I record it because it would cost one
  footnote ("$87$ coprime slopes with $q\le 8$ minus the nine finite exceptional integer slopes") to let
  every reader perform the same check the way I just did, instead of only the repository's own script.
- Minimal repair (optional, upgrade not defect): add that one-line arithmetic justification in a footnote at
  line 662.

---

## (a) The single strongest objection to the paper as a whole, and does the paper already answer it

The strongest geometric objection is that the construction's only manifold-specific fact — as opposed to a
fact about the whole commensurability class of $\Q(\sqrt{-3})$, which the paper itself insists (§unique,
correctly) is all that its main chain consumes — is introduced once, very late (§observer, "Which member"),
via a single citation (Jørgensen number extremality, "Callahan's theorem") that I cannot place in the
literature with confidence (F1). Every quantity computed in §chirality — the count of two, the vanishing
index, the tower of 87 covers — is stated for m004 the manifold, not for the class, and the paper is
admirably candid that this is a cost ("keeping the member therefore costs the bit... we register the fork
and do not resolve it," line 1091). But that candour is only as good as the citation backing the selection
argument it is candid about. The paper does substantially pre-empt the *structural* form of this objection —
it already knows and states that chirality, the count of three, and the index are class/tower properties and
not manifold properties, and it does not hide that m004 itself sits in the "not yet had" column for the
chirality bit. What it does not pre-empt is the narrower, citation-level version of the objection: that the
one theorem cited to justify treating m004's own selection as "variational... where every earlier selection
story was descriptive" may not exist as cited, which would put the manifold-selection step back at
"descriptive" (a census argument, §generic) rather than "variational," undercutting exactly the rhetorical
upgrade the Recognition section claims for it.

## (b) What the referee would say the paper actually proves, in one sentence, and does the abstract say the same thing

What a geometer-referee would say is actually proved: *this paper establishes several correct, self-
contained results about the commensurability class of the invariant trace field $\Q(\sqrt{-3})$ and about
finite covers and cyclic branched closings of the figure-eight knot complement — parity constraints on
cusp-fixed loci, an injectivity theorem (transferred from Menal-Ferrer-Porti through finite covers) forcing a
self-defined chirality index to vanish on every geometric-holonomy sector of every one-cusped hyperbolic
3-manifold, the same index's non-vanishing on specific named reducible non-split modules on five class
members and one cyclic cover, and the fact that 66 of 87 covers to degree ten are chiral while the base
manifold is not — and uses these to conclude that no currently-computed geometric structure of this object
supplies a chiral (as opposed to vector-like) matter spectrum.* The abstract's own sentence (lines 66–71,
"Three complete copies of the Standard-Model content are exhibited... they are vector-like: the chirality
bit is what the object withholds, and we say where...") is a fair compression of this and does not overclaim
relative to it — the abstract is, on this specific point, honest about what is geometry and what is
withheld. Where the abstract and the geometric content part ways slightly is emphasis: the abstract presents
the "base rates" and the "chirality bit" as two among several results of comparable weight, while a geometer
would say the base-rate material of §generic (census counts of the $2T$-surjection and of amphichirality) is
doing at least as much of the paper's real epistemic work as the named theorems in §chirality, since it is
the base rates — not the vanishing-index theorem — that force the paper's central discipline of separating
"generic" from "specific" in the first place.

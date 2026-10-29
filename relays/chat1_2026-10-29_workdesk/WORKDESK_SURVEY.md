# The workdesk survey: compile the repository; never curate a copy

chat1 (the web seat), written 2026-10-28 (revised 2026-10-29 after its referee) at the owner's request of that day
("lets treat the back/frontend idea seriously, lets dig deeper and do research, how ofher scientists deal with these
kind of data or franwrork representation, so what we build serves also like a workdesk with tools"), before main's relay
of 2026-10-29. It is the reference behind the seat's relay
CHAT1_TO_ALL_SEATS_2026-10-29_THE_WORKDESK_THE_WEB_SEATS_PROPOSAL.md. Sources are public and cited inline. The
repository counts were read on main at 2f6dfbdc2; main's relay re-measured some at its own commit, and the relay
reconciles the two. The recommendations are the survey's own and assign nothing. 0 of 19.

The large research programmes that stay navigable (formal mathematics, particle physics, mathematical-object databases,
preregistration registries) all use the same architecture. Each result is a machine-readable record under version
control. Its identifier is permanent and never reused. Status and dependency graphs are computed from those records on
every change. A correction is a new dated record that points at the old one. Every number carries a label saying how it
was derived, from which edition of the data, and at which commit. The strongest evidence is a failure case. When Lean
blueprint projects kept status by hand, automated extraction later found missing dependency edges, isolated nodes and
wrong statuses ([LeanArchitect, ITP
2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol382-itp2026/LIPIcs.ITP.2026.25/LIPIcs.ITP.2026.25.pdf)). For
origin-axiom, the workdesk should therefore be a compiler. A Python step in CI validates the repository and emits a
normalised store, per-arc pages, a frontier landing page, ledgers and computed figures, all stamped with the commit SHA.
A read-only static front end sits over that output. Every write (seal, unseal, correct, retract, claim) goes through a
command-line tool that commits files. The repository already holds most of the raw material: on main, 1,507
`arc_verdict.json` files with `verdict`, `depends_on`, `supersedes` and `authored_by` fields. It also shows the same
drift the blueprint projects found. Only 566 of them declare any dependency. Twenty-eight dependency references point at
arcs that have no verdict file. B58 and B89 are each claimed by more than one directory. Authorship is free text and
missing on 194 arcs. At least one partial retraction exists only as prose appended inside an older claim. Three of the
owner's needs have no precedent in mathematical tooling: preregistered priors with calibration, relays between seats,
and the forced/admitted/chosen/fitted grade. These have to be borrowed from physics blinding, OSF-style registries, W3C
PROV and the Particle Data Group's derivation labels. One display rule follows whatever front end is built: every χ²
should carry its degrees of freedom and p-value. The two bars are both about the 1% tail (16.75 has p = 0.0102 at 6 dof,
which the record already notes is slightly stricter than the 99% point, 16.81; 21.67 has p = 0.0100 at 9 dof), and a
bare number hides that.

Each section below first reports what the sources establish, with citations, and then marks its implications for
origin-axiom as the report's own inference. The final architecture section is entirely the report's recommendation. Each
element there is tied to the precedent it borrows from, or labelled as having none. Statements about the repository come
from a direct read of main's working tree at commit `2f6dfbdc2` on 28 October 2026, not from the cited sources. (A first
draft read a lagging branch checkout; its figures were replaced.)

## Formal mathematics learned that hand-kept status drifts from the proofs

The Lean "blueprint" is the dominant way formalisation projects represent a large proof. It is a LaTeX document whose
theorem environments carry machine-readable macros. `\uses{}` lists dependencies, `\lean{}` links to code declarations,
`\leanok` marks a statement or proof with no `sorry`, `\mathlibok` marks results already in the library, and `\notready`
marks items needing more blueprint work. plasTeX compiles the document into a web page plus a dependency graph coloured
by status
([LeanArchitect](https://drops.dagstuhl.de/storage/00lipics/lipics-vol382-itp2026/LIPIcs.ITP.2026.25/LIPIcs.ITP.2026.25.pdf)).
Terence Tao's 2023 tour of the PFR project shows that the colours encode **two separate status fields plus a derived
one**:

- Green means formalised.
- Blue means "ready to formalize": the statement and all its prerequisites are done, but the proof is not.
- A green border on a white node means the statement is formalised but the proof is not yet ready.

The working goal was to turn every bubble leading to the main theorem green, so the graph functioned as the to-do list.
Sync was manual. Tao added `\leanok` by hand after proving a lemma, and a rebuild took **"about half an hour"** ([Tao,
PFR tour](https://tagteam.harvard.edu/hub_feeds/3899/feed_items/9040961/content)).

LeanArchitect (ITP 2026) is the field's correction to that workflow. It moves blueprint metadata into a `@[blueprint]`
attribute on Lean declarations. It infers dependencies and `sorry`-status from the elaborated terms and exports
leanblueprint-compatible LaTeX, which makes Lean "the authoritative source of information" for formalised nodes.
Converting existing projects exposed **isolated nodes, missing dependency edges and theorems that should have been
marked as already in Mathlib**. PrimeNumberTheoremAnd migrated in about a day in January 2026. The paper is candid about
the costs: LaTeX inside Lean is "unergonomic", the extra build steps cause CI failures, and LaTeX-only nodes still need
manual care
([LeanArchitect](https://drops.dagstuhl.de/storage/00lipics/lipics-vol382-itp2026/LIPIcs.ITP.2026.25/LIPIcs.ITP.2026.25.pdf)).
The blueprint semantics also keep **statement dependencies separate from proof dependencies**, and allow a proof to be
`\leanok` while depending on an unfinished lemma. "Proved locally, but resting on something unproved" is therefore a
first-class state, distinct from "proved outright".

Tao's Equational Theories Project (ETP) is the closest analogue in shape to origin-axiom: thousands of atomic claims,
each with a verdict, many produced by machine. It settled **all 22,028,942 implications between 4,694 magma laws**
between September 2024 and 14 April 2025. Its trust architecture had three layers. About 597,582 formal Lean results
formed a checked generating set. Unverified external programs expanded that set to the full 22 million using
transitivity and duality. The project marked which results were established directly and which were derived.
Coordination ran through a GitHub repository. Contributors claimed tasks by comment, and CI ensured that **"at most one
contributor could claim a task at any time"**. A kanban board had its cards moved by CI rather than by hand ([Bolan,
Tao, Carlini et al., arXiv 2512.07087](https://www.arxiv.org/pdf/2512.07087)). The graph became viewable only after
collapsing 4,694 laws into 1,415 equivalence classes and drawing Hasse diagrams. The project's stated lessons:

- Put "a maintainer structure in place before the project begins."
- One monolithic equations file was a mistake.
- A proof checker cannot guarantee that a formal statement says what its authors meant, whoever wrote it.

The one unresolved finite-magma implication was kept as a named conjecture rather than buried in a count ([Tao, Dec
2025](https://tagteam.harvard.edu/hub_feeds/3899/feed_items/17107118)).

The Stacks project supplies the identifier discipline. A tag is a permanent four-character code that "will always point
to that exact mathematical result or definition". When an item moves, only a `tags` mapping file changes ("we will never
change the tag"). When a result is found to be wrong, it may be removed, but **its tag is kept and the removal is
explained** ([Stacks, Tags](https://stacks.math.columbia.edu/tags); [de Jong, tags
system](https://www.math.columbia.edu/~dejong/wordpress/?p=287)). Stacks also showed that cheap global metrics pay off.
Results were stratified by dependency "height", which peaked at 78, and a dip in the histogram identified a heavily used
bootstrap result, tag 04S6 ([de Jong, Dependency graph](https://www.math.columbia.edu/~dejong/wordpress/?p=2281)). Its
2013 d3 force-graph views drew enthusiasm, but also the reader complaint that code class-browsers are "MUCH clearer and
more useful" ([mathbabe.org,
2013](https://mathbabe.org/2013/07/30/the-stacks-project-gets-ever-awesomer-with-new-viz/)). Kerodon's per-tag page,
built on the same Gerby software, makes the result page the atomic unit. It carries a breadcrumb, previous and next
links, a PDF anchor, a citation link, statistics, and dated, signed comments ([Kerodon
004Y](https://kerodon.net/tag/004Y/comments); [Belmans, 2018](https://pbelmans.ncag.info/blog/2018/10/17/kerodon/)).

In daily use the tool people reach for is search, not graphs. Loogle answers structural queries over Mathlib (constants,
subexpression patterns, conclusion patterns). It **states the exact library revision it is serving**, and it is wired
into VS Code, Neovim, a Zulip bot and the command line ([Loogle](https://loogle.lean-lang.org/)). The opposite failure
is documented too. The 2009 Polymath project, with about 800 comments across 37 days, found that a linear discussion log
left latecomers unable to find their place, and its organisers called for issue-tracker-style modularisation ([Gowers &
Nielsen, Nature 2009](https://michaelnielsen.org/papers/mcm.pdf)).

Prove2Me (2026) adds the cleanest correction model and the sharpest warning. Statements are "standalone, immutable
object[s]". A disproof proves the negation. A flawed statement is replaced, not edited: `gotsman_linial` was disproved
and superseded by `gotsman_linial_with_zero`. Mission pages lead with a **milestone list as the "entry point"** rather
than the raw decomposition graph. The paper cites an audit in which only about **43% of proved statements were
faithful** to the intended claim. A proof kernel certifies that a proof inhabits a statement, "but not that the
statement faithfully captures the intended claim" ([Prove2Me, arXiv 2608.28433](https://arxiv.org/pdf/2608.28433)).

*Inference for origin-axiom.* An `arc_verdict.json` plays the role of a Lean declaration, so status and edges should be
computed from it, never kept separately. Each arc needs:

- its local verdict;
- whether its statement is fixed or sealed;
- a derived readiness flag computed from its ancestors;
- a transitive status such as "PROVED, conditional on OPEN B‑x".

Verdicts established directly should be visibly distinct from those inferred by closure. Arc numbers should follow the
Stacks rules. The landing view should be a milestone and frontier list, with the graph reached by drill-down. Statement
fidelity needs its own status field, because a correct proof of the wrong statement is a silent failure several of the
sources report.

## Particle physics attaches a derivation label, an edition and a seal to every number

HEPData is the field's archive of published numbers, and its record format is the template for a fit result. Each table
separates `independent_variables` from `dependent_variables`. Uncertainties are typed and labelled (`symerror` and
`asymerror`, with labels such as `stat` or `sys,detector`). A bin whose uncertainties are all zero fails validation.
Correlation matrices are tables in their own right ([HEPData data
format](https://hepdata-submission.readthedocs.io/en/latest/data_yaml.html)). DOIs are minted for **every version of
both the record and each table**. A correction creates version 2 and keeps version 1, and every export carries its DOI
([Maguire et al., arXiv 1704.05473](https://ar5iv.arxiv.org/html/1704.05473)). By early 2025 the archive held about
130,000 tables from more than 10,000 publications ([Byers, Feb
2025](https://ippp.dur.ac.uk/~watt/byers_hepdata_feb2025.pdf)).

The Particle Data Group adds a fixed vocabulary of **derivation labels**: OUR AVERAGE, OUR FIT, OUR EVALUATION, OUR
ESTIMATE ("Not from a formal statistical procedure") and OUR LIMIT. It keeps excluded measurements visible together with
the reason for exclusion, such as superseded, no error given, or questionable assumptions. Its procedures are published:
the scale factor S = [χ²/(N−1)]^½ is applied only when χ²/(N−1) > 1, "our scaling procedure for errors in no way affects
central values", and the "354 rule" fixes rounding. Ideograms are "simply visual aids", and no numbers are extracted
from them ([PDG Introduction](https://ccwww.kek.jp/pdg/2017/reviews/rpp2017-rev-rpp-intro.pdf)). Since 2024 PDG values
can be pulled by machine through a REST API, a Python package and a single SQLite file ([PDG
API](https://pdgapi.lbl.gov/doc/overview.html)). The current edition is the 2026 Review
([pdg.lbl.gov](https://pdg.lbl.gov)).

Global fits report a small, fixed set of objects:

- **Goodness of fit**: a global p-value. CKMfitter quotes 67% (0.4σ) for its 2023 Standard Model fit.
- **Leave-one-out pulls**: Pull_O = √(χ²_min − χ²_min,!O), shown as a bar chart in units of σ ([CKMfitter, arXiv
  2405.08046](https://arxiv.org/pdf/2405.08046)).
- **Indirect predictions** that exclude each input. UTfit's "compatibility plots" compare a direct measurement with the
  indirect fit that leaves it out ([UTfit, arXiv 0905.3747](https://ar5iv.labs.arxiv.org/html/0905.3747)).
- **Profile or posterior contours**, labelled with the confidence level.

The methodological literature adds discipline. Asymptotic χ² formulae "may not apply" and must be checked. "The p-value
is not the probability of the null hypothesis." "When we compute p-values, we should take into account all the tests
that we might have performed." Likelihoods should be combined, not overlaid ([AbdusSalam et al., arXiv
2012.09874](https://arxiv.org/pdf/2012.09874)). For scans over continuous parameters, Gross and Vitells showed that the
trials factor can be estimated from the mean number of upcrossings in a small set of background-only toys. In their
example, 100 toys gave ⟨N(0.5)⟩ = 4.34 ± 0.11. The factor grows linearly with the fixed-point significance ([Gross &
Vitells, arXiv 1005.1891](https://ar5iv.arxiv.org/html/1005.1891)). Vischia's reporting manifesto asks for pre-fit and
post-fit uncertainties, an Asimov validation (which should give zero pulls by construction), explicitly labelled bands,
and **tables, not only graphs** ([Vischia, arXiv 1904.11718](https://arxiv.org/pdf/1904.11718)).

The preservation movement then turned the analysis itself into data. The LHC Reinterpretation Forum's 2025 report
recommends building preservation in "from the start", publishing full statistical models in the HS3 format, and
preserving analysis logic as executable code ([LHC RF 2025, arXiv 2504.00256](https://arxiv.org/html/2504.00256v1)).
Cranmer et al. argue that a published likelihood alone "precludes the generation of pseudo data", so the model and the
observed data must be published as well ([arXiv 2109.04981](https://arxiv.org/pdf/2109.04981)). A pyhf workspace is a
declarative JSON object with channels, samples, modifiers, and parameters marked with bounds and a `fixed` flag ([pyhf
spec](https://pyhf.readthedocs.io/en/stable/likelihood.html)). REANA's `reana.yaml` names inputs, environment, steps and
outputs ([REANA](https://docs.reana.io/reference/reana-yaml)). SModelS stamps **both its code version and its database
version** into every output ([SModelS output](https://smodels.readthedocs.io/en/stable/OutputDescription.html)). As Chen
et al. put it, "openness alone does not guarantee reproducibility or reusability" ([Nature Physics
2019](https://link.springer.com/article/10.1038/s41567-018-0342-2)).

On bias, physics prefers blinding to preregistration. Klein and Roodman's rules:

- The signal box opens only after selection, efficiency and background are fixed.
- Unblinding is decided "not by the data analysts alone" but as part of review.
- Publications must be "explicit about what selections were applied after the unblinding".
- Stopping bias is "probably the most common" form.

Source: ([Klein & Roodman 2005](https://www.Gwern.net/doc/statistics/bias/2005-klein.pdf)). The strongest practice
separates the person who holds the key from the analyst:

- **Muon g‑2:** two Fermilab physicists outside the collaboration held the clock offset in an envelope until a
  collective unblinding ([Nature news,
  2021](https://media.nature.com/original/magazine-assets/d41586-021-00940-0/d41586-021-00940-0.pdf)).
- **LIGO:** blind injections ran a planted signal through a full detection paper and vote before the envelope was
  opened. The exercise also exposed two injection-software bugs ([LIGO](https://ligo.org/blind-injection/)).

MacCoun and Perlmutter note that preregistration "limits the scope of analysis", which is why physicists prefer blinding
([Nature 2015](https://www.nature.com/articles/526187a.pdf)). Golub dissents, arguing that blinding can "severely
inhibit the search for systematic errors" ([arXiv 2311.13542](https://arxiv.org/pdf/2311.13542)).

*Inference for origin-axiom.* The six mass ratios and the χ² against data should be rendered as a physicist would
expect: a HEPData-style table with typed uncertainties and the PDG edition and identifier of each target, a
leave-one-out pull plot, and the χ² printed with its dof and p-value. By a scipy check, **16.75 has p = 0.0102 at 6 dof
and 21.67 has p = 0.0100 at 9 dof**: both bars are about the 1% tail, and B1735's dated note already records that 16.75
is slightly stricter than the 99% point for six (16.81). A front end that shows bare numbers hides this, and hides that
a χ² minimised over τ, a line and a menu is not distributed as χ² with the nominal dof at all; the look ledger and the
random-hierarchy nulls carry that correction. The χ² itself should be a declarative file in the pyhf/HS3 spirit:
targets, σ or covariance, any theory allowance, and which parameters are fitted, scanned or fixed. Every view then calls
one scorer. The look ledger is the programme's trials-factor bookkeeping and should be shown as local versus global p.
The planted-row power controls are the programme's blind injections, and they are stronger if a different seat holds the
key.

## Registries and provenance standards correct by appending, never by editing

W3C PROV (2013) is still the reference model for provenance. **Entities** are generated and used by **Activities**, and
**Agents** are responsible for activities. A **Plan** is the predefined procedure an agent follows. **Revision** is a
derivation from a preceding entity. **Invalidation** marks an entity's expiry at an instant. A **Bundle** is a set of
provenance descriptions that is itself an entity, which allows provenance of provenance
([PROV-DM](https://dvcs.w3.org/hg/prov/raw-file/tip/model/prov-dm.html); [PROV
Primer](https://www.w3.org/TR/prov-primer/)). RO-Crate 1.2 (June 2025) packages such metadata as JSON-LD and adds
"detached crates" for metadata served behind an API ([eScience
Lab](https://esciencelab.org.uk/ro-crate/announcements/2025/06/04/ro-crate-1.2-released/)). Its Process Run Crate
profile is the lightest way to describe "tools ran, outputs produced" ([Workflow Run Crate
profiles](https://www.researchobject.org/workflow-run-crate/profiles/)). SWHID, which extends git's hashing to an
archive-backed identifier, became ISO/IEC 18670 ([OpenChain,
2025](https://openchainproject.org/news/2025/04/29/from-heritage-to-hash-swhid-becomes-a-global-iso-iec-standard);
[SWHID FAQ](https://swhid.org/faq/)).

Preregistration registries enforce immutability and handle change by appending:

- **OSF registrations** are "timestamped, immutable". An update requires a filled justification field, and "files cannot
  be added or removed during a registration update". Withdrawal is irreversible and leaves a **tombstone page with the
  justification** ([OSF Help](https://help.osf.io/article/113-advanced-actions-registrations);
  [COS](https://www.cos.io/products/osf-registries)).
- **AsPredicted** entries "cannot be modified" once public ([AsPredicted](https://aspredicted.org/)).

The case for this rigidity is quantitative. Positive results on the first hypothesis appeared in **96% of standard
psychology reports against 44% of Registered Reports** ([Scheel, Schijen & Lakens
2021](https://www.psychologicalscience.org/journals/ampps/25152459211007467/)). COMPare found outcome switching in **58
of 67 trials** in top medical journals ([Retraction Watch, 2016](https://retractionwatch.com/?p=37075)).

Scholarly knowledge graphs model claims and corrections the same way:

- **Nanopublications** split a claim into assertion, provenance and publication-info graphs, made immutable by
  hash-bearing URIs. A retraction is a new nanopublication, valid only if "signed with the same public key" as the
  original ([Kuhn et al., arXiv 1809.06532](https://ar5iv.labs.arxiv.org/html/1809.06532); [nanopub
  docs](https://nanopub.readthedocs.io/en/latest/publishing/retraction.html)).
- **Crossref**, which has owned the Retraction Watch database since 2023, exposes a controlled `RetractionNature`
  vocabulary (Retraction, Correction, Expression of concern, Reinstatement) with a reason list
  ([Crossref](https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/)). **Crossmark** records each
  change as a separate notice, so the original becomes "updated_by" it
  ([Crossmark](https://support.crossref.org/hc/en-us/articles/115000501246-Crossmark-registering-updates)).
- **ORKG** stores contribution-level comparisons as frozen snapshots "because the underlying graph changes over time"
  ([Oelen et al., arXiv 2006.01747](https://arxiv.org/abs/2006.01747)).
- **Architecture decision records**, outside science, apply the same rule to decisions. They are numbered "sequential
  and never reused", and a reversed decision "is kept and marked as superseded" ([MoJ
  ADR-000](https://runbooks.find-moj-data.service.justice.gov.uk/documentation/adrs/000-record-architecture-decisions.html)).
  MADR adds Considered Options, a "Confirmation" step, a confidence level and revisit criteria ([MADR
  primer](https://ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html)).

Experiment trackers contribute the mechanics of "committed before read":

- **Sacred** records, for each run, git `{url, commit, dirty}` and the **MD5 of every source file**
  ([Sacred](https://sacred.readthedocs.io/en/stable/collected_information.html)).
- **DVC's** `metrics diff` and `params diff` accept any two git revisions
  ([DVC](https://doc.dvc.org/start/data-pipelines/metrics-parameters-plots)).
- **MLflow** tags each run with its commit and supports parent–child runs. Its deleted runs can be garbage-collected
  ([MLflow 2.4](https://mlflow.org/docs/2.4.0/tracking.html)). That is the wrong model for a scientific record.

Forecast science supplies the tools for auditing one's own priors:

- **Proper scores.** The Brier score decomposes into reliability, resolution and uncertainty, but binned estimators are
  biased at small N ([Siegert, arXiv 1303.6182](https://ar5iv.arxiv.org/html/1303.6182)).
- **Reliability diagrams at small N.** CORP diagrams replace ad-hoc bins with isotonic regression plus resampling bands
  ([Dimitriadis, Gneiting & Jordan, arXiv 2008.03033](https://arxiv.org/abs/2008.03033v1)). The log score punishes
  confident misses far harder than Brier ([Metaculus](https://www.metaculus.com/help/scores-faq/)).
- **Benchmarks.** Replication prediction markets were right on 71% of studies with a calibration slope of 0.995, yet
  their **mean price of 55% sat well above the realised replication rate of 39%** ([Dreber et al., PNAS
  2015](https://projects.iq.harvard.edu/files/yiling/files/pnas.1516179112.pdf)). That one-number overconfidence check
  transfers directly.

*Inference for origin-axiom.* Every record family in the repository (arcs, sealed tests, points, relays, corrections)
should follow one uniform append-only pattern: a dated new record pointing at the old one, with the old one always
visible under a status banner. The PROV mapping is direct:

| Repository item | PROV role |
|---|---|
| Seat | Agent |
| Sealed specification | Plan |
| Script execution | Activity |
| Verdict file | Entity |
| Relay | Communication between activities |
| Retraction | Invalidation |
| Correction | Revision |
| Look ledger and point register | Bundles |

The point register maps onto MADR, whose "Confirmation" field is the arc or sealed test that settles each point.
Publishing every sealed test with its prior and outcome, including voided and unresolved ones, would let the programme
show its realised hit rate against its mean stated prior. This survey did not find a published example of a research
group auditing its own preregistered priors this way.

## Object databases give every mathematical object a homepage and a computed picture

The LMFDB is the reference design for presenting computed mathematical objects:

- **One homepage per object.** "Every object in the LMFDB ... has a homepage" at a permanent, mathematically meaningful
  URL (elliptic curve 5077.a1 at `EllipticCurve/Q/5077/a/1`). Common information sits at the top and technical detail
  below. A sidebar carries **Properties, Related Objects, Downloads and Learn more**, and pages offer copy-paste code
  for Sage, Magma and PARI ([Cremona et al. 2021](https://johncremona.github.io/papers/LMFDBNotices.pdf)).
- **Knowls.** Terms are defined inline by "knowls", which expand in place. A knowl now carries a "reviewed" status and
  an edit history with diffs ([LMFDB knowl `rcs`](https://www.lmfdb.org/knowledge/show/rcs)).
- **The Source / Reliability / Completeness triad.** Every collection publishes three statements. Source says who
  computed it and by what method. Reliability lists "any heuristics or unproved conjectures that were used".
  Completeness says which finite subset of an infinite family is present ([LMFDB knowl
  `rcs`](https://www.lmfdb.org/knowledge/show/rcs)).
- **Stated design problems.** The project names "mathematical objects need permanent labels" as a core problem,
  alongside rigour and reproducibility ([Sutherland, ICMS 2020](https://math.mit.edu/~drew/ICMS2020.pdf)). Cross-linking
  independently computed datasets required relabelling one of them so that labels matched exactly ([Cremona
  2016](https://johncremona.github.io/papers/lmfdb_article.pdf)).

Catalogues of knots and manifolds add per-value attribution and explicit evidence grades:

- **KnotInfo** credits each invariant to its method and contributor (3-genus by Rasmussen via knot Floer homology,
  hyperbolic invariants from SnapPea) and credits error-finders publicly
  ([KnotInfo](https://knotinfo.math.indiana.edu/homelinks/about.html)).
- **SnapPy** names census manifolds with Dehn-filling suffixes such as `m007(0,0)` or `v1539(5,1)`. It identifies
  manifolds through `identify()` and the isometry signature, "a complete invariant", which supports `verified=True`
  ([SnapPy censuses](https://snappy.computop.org/censuses.html); [SnapPy
  Manifold](https://snappy.computop.org/manifold.html)).
- **The 2026 ten-tetrahedron census** grouped 150,730 manifolds using verified canonical triangulations, and listed
  separately **16 cases grouped on "somewhat weaker evidence"** ([Li, SoCG
  2026](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.73/LIPIcs.SoCG.2026.73.html)).
- **Burton's asymmetry** shows why that split matters. SnapPea's "homeomorphic" claims come from explicit moves and are
  reliable, while its "distinct" claims rest on floating-point canonical decompositions. A duplicate pair in the census
  "went undetected for a long time" as a result ([Burton, arXiv 1311.7615](https://ar5iv.arxiv.org/html/1311.7615)).

For the figure-eight complement m004, every standard picture is computed from the triangulation:

- the cusp horoball diagram (`cusp_neighborhood().view()`);
- the Dirichlet domain, with face-pairing words and STL export;
- the raytraced inside view, with geodesics drawn by word and `drill_word` and `dehn_fill` for fillings ([SnapPy
  Manifold](https://snappy.computop.org/manifold.html));
- the Cannon–Thurston pictures of m004 seen from inside with its fibre in view ([ICERM
  Cannon–Thurston](https://im.icerm.brown.edu/portfolio/cannon-thurston-maps/)).

SnapPy's developers document where their pictures rest on heuristics. Cusp "stoppers" come from an unverified
Epstein–Penner computation, and without the 2025 tiling algorithm rays can miss tiles and leave holes in the render
([Goerner, arXiv 2512.16181](https://arxiv.org/pdf/2512.16181)). `canonize()` carries an explicit rounding warning
([SnapPy Manifold](https://snappy.computop.org/manifold.html)).

Each other step of the chain also has a canonical, quantitative picture in the literature:

- **Fibonacci chain.** The cut-and-project figure: Z², a line of slope 1/τ, an acceptance strip and its window, plus the
  torus parametrisation of the hull. Diffraction appears as Bragg peaks weighted by the window's Fourier transform
  ([Baake, math-ph/9901014](https://arxiv.org/pdf/math-ph/9901014)).
- **Hyperbolic toral automorphisms.** A Markov partition whose transition matrix is the coding graph ([Adler,
  math/9607214](https://ar5iv.labs.arxiv.org/html/math/9607214)).
- **Modular-surface geodesics.** Coded by L/R(/J) cutting sequences against the standard fundamental domain ([Grabiner &
  Lagarias, math/9707215](https://arxiv.org/abs/math/9707215)). Their lifts to the trefoil complement are determined by
  cyclic L/R words on Ghys's template ([Pinsky, Purcell & Rodríguez-Migueles](https://arxiv.org/pdf/2307.09409)).
- **Theta functions.** DLMF publishes computed 3D plots with permalinks and linked symbol definitions ([DLMF
  20.3.F12](https://dlmf.nist.gov/20.3.F12.mag)). It moved nearly 200 of them to WebGL with a cutting-plane tool ([NIST
  2014](https://www.nist.gov/news-events/news/2014/07/vivid-realism-3d-functions-right-there-your-browser)).

The common thread in faithful web graphics is that the picture is a pure function of data. MathBox curves take "an array
of data points or a live expression evaluated at every point" ([Wittens 2012](https://acko.net/blog/making-mathbox/)),
and the Knot Atlas draws knots from planar-diagram codes rather than storing drawings ([Knot Atlas
manual](https://www.math.toronto.edu/~drorbn/private/KAtlas/Manual/NamingAndEnumeration.html)).

*Inference for origin-axiom.* The relationships below are the report's own arithmetic, which is easy to check. The
Fibonacci substitution matrix M = [[1,1],[1,0]] satisfies **M² = [[2,1],[1,1]], the cat map**. Its eigenlines therefore
bound both the cut-and-project window and the Markov rectangles. Its entropy is log((3+√5)/2) = 2 log τ ≈ 0.962. The
trace-3 hyperbolic element gives a closed modular geodesic of length 2·arccosh(3/2) ≈ 1.925, and its RL cutting word (up
to convention) is the bridge between the "threads" and m004's monodromy. Each object therefore gets an LMFDB-style
homepage on which every figure is computed and flagged. The table gives the canonical picture per object. The grade
column must come from the repository's own claims and is never assigned by the front end.

| Chain object | Canonical computed representation | Precedent | Evidence flag to display |
|---|---|---|---|
| Substitution a→ab, b→a; matrix M | Strip/window cut-and-project figure; hull torus; diffraction intensities | Baake | Exact (Q(√5) eigenvectors) |
| Cat map [[2,1],[1,1]] on T² | Markov partition with transition matrix; eigenline foliations | Adler | Exact |
| m004 (cusp, horoballs, fillings) | Census name, 4₁, isometry signature; horoball view; Dirichlet domain; fillings as m004(p,q) | SnapPy, KnotInfo | Verified vs heuristic per element (Burton, Goerner) |
| Threads (closed geodesics in F) | Geodesic arcs in the fundamental domain from fixed points; L/R cutting word; length 2·arccosh(\|t\|/2) | Grabiner–Lagarias; Pinsky et al. | Exact endpoints (quadratic irrationals) |
| Flat lines (a,b) on punctured-torus fibre | Straight lines of slope b/a on the square torus; overlay as geodesic words in the inside view | SnapPy `drill_word`/`inside_view` | Exact rational data; render flagged as view |
| Theta-function zero modes | Computed plots with permalinks; zeros marked from computed values | DLMF | Numeric precision stated (no authoritative source found for torus domain-colouring) |
| Six SM mass ratios vs data | HEPData-style table; pull plot; χ² with dof and p; targets with PDG edition | HEPData, PDG, CKMfitter | Floating numerics; derivation label per number |

## Visual-analytics evidence favours a static, frontier-first workdesk

Two frameworks govern the design:

- **Shneiderman's** "overview first, zoom and filter, then details-on-demand" ([Shneiderman
  1996](https://drum.lib.umd.edu/handle/1903/5784)). Its less-quoted tasks, *relate*, *history* and *extract*, are what
  separate a research workdesk from a dashboard.
- **Munzner's nested model**: domain problem, abstraction, encoding, algorithm. An error at an upper level cascades
  down, informal usability studies "do not count as validation", and the decisive test at the abstraction level is
  target users doing their own work with the tool ([Munzner
  2009](https://webspace.science.uu.nl/~telea001/uploads/VACourse/Munzner09.pdf)).

The provenance-visualisation survey lists data, visualisation, interaction, insight and rationale provenance as distinct
types. It names reproducibility as the field's weak spot, because many systems share no implementations ([Xu et al.,
EuroVis 2020](https://diglib7.eg.org/bitstream/handle/10.1111/cgf14035/v39i3pp757-783.pdf)). On uncertainty, viewers
read interval ends as hard bounds. Frequency framing and quantile dotplots outperform bare intervals, and "there is no
one-size-fits-all" approach ([Padilla, Kay &
Hullman](https://moodle2.units.it/pluginfile.php/466375/mod_resource/content/0/Uncertainty_Visualization_Padilla_Kay_Hullman_2020.pdf)).

Scale is not a constraint at this repository's size:

| Option | Measured capacity | Source |
|---|---|---|
| Cytoscape.js, WebGL preview | Over 100 FPS at about 1,200 nodes / 16,000 edges (Canvas: about 20 FPS) | ([Cytoscape.js, 2025](https://blog.js.cytoscape.org/2025/01/13/webgl-preview/)) |
| SVG / Canvas / WebGL rendering | Rough ceilings of about 2k, 5k and 10k nodes | ([DEV comparison, 2021](https://dev.to/timlrx/a-comparison-of-javascript-graph-network-visualisation-libraries-34a8)) |
| GPU force layout (cosmos) | Aimed at graphs of 10⁵–10⁶ nodes | ([Nightingale](https://nightingaledvs.com/how-to-visualize-a-graph-with-a-million-nodes/)) |

GPU force layout is therefore unnecessary here. For a directed graph such as the forcing graph, a layered (Sugiyama)
layout from ELK is the standard ([elkjs](https://github.com/kieler/elkjs)). Browser-side data is equally unconstrained:

- **DuckDB-WASM** caps memory at 4 GB, runs single-threaded unless cross-origin isolated, and has documented HTTP
  range-request quirks ([DuckDB-WASM](https://duckdb.org/docs/current/clients/wasm/known_issues)).
- **Pagefind** gives static full-text search for roughly 100–300 KB per session
  ([CloudCannon](https://cloudcannon.com/blog/introducing-pagefind/)).
- **Datasette Lite** runs the full SQL browser in Pyodide from a `?url=` parameter, provided the file is served with
  permissive CORS ([datasette-lite](https://github.com/simonw/datasette-lite/blob/main/README.md)).
- **Python in the browser** handles numpy, scipy and sympy, within 2–4 GB per tab and with no persistence ([Zonca
  2026](https://www.zonca.dev/posts/2026-05-18-jupyterlite-no-server-needed)).

The best-documented precedent for a regenerated static publication over an authoritative pipeline is Our World in Data.
It is a "statically rendered ('JAMstack') publication with no public facing backend". A Python ETL is **"authoritative
for data values"** and is staged from snapshot through to publication, and a "baker" writes the static site ([OWID
architecture](https://owid-grapher.readthedocs.io/en/docs-revamp-2023/architecture/)). Observable Framework implements
the same pattern for data apps: build-time data loaders in any language write static snapshots, and the output deploys
without a server ([observablehq/framework](https://github.com/observablehq/framework); [R-bloggers, Aug
2026](https://www.r-bloggers.com/2026/08/skip-the-r-python-runtime-fast-tabular-dashboards-with-observable-framework/)).
UW's Mosaic examples run DuckDB at build time to write pre-projected Parquet ([Mosaic +
Framework](https://idl.uw.edu/mosaic-framework-example/data-loading)). Framework's future is uncertain, however.
Observable's 2025–2026 investment went into Notebook Kit and a closed hosted product, and no staff statement on
Framework's maintenance was found ([MacWright, Sep 2026](https://macwright.com/2026/09/02/new-observable); [Observable
forum](https://talk.observablehq.com/t/where-is-observable-going/10372)). Hosting has a privacy catch. GitHub Pages caps
sites at 1 GB, allows Pages from private repositories only on paid plans, and its limits documentation says nothing
about access control ([GitHub
Docs](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)).

*Inference for origin-axiom.* The main risk is choosing the wrong abstraction (Munzner's levels 1–2), not rendering
speed. The design has to start from the owner's real retrieval questions: has this been superseded, which script
produced this number, what falls if B‑x is retracted, which probes fail obstacle X. It should be validated by timing
those questions against today's grep workflow. The Recurrence Atlas (1,503 × 28 × 11) is a three-way relation. It
belongs first in a sortable matrix of 28 motifs × 11 obstacles (308 cells with counts), with probes as drill-down and
small multiples per obstacle. A node-link hairball should not be the first view.

## Recommended architecture: a validated compiler, a read-only desk and a write CLI

Everything in this section is the report's recommendation. The precedent column in each table shows where a choice is
borrowed and where it is new.

### The repository already holds the raw material, and the same drift

A direct read of main's working tree (commit `2f6dfbdc2`) found:

- 1,507 `frontier/B*/arc_verdict.json` files for 1,504 distinct IDs, from B1 to B1802. Their verdicts are PROVED 1,028,
  NEGATIVE 374, OPEN 93 and RETRACTED 12. "CORRECTED" does not occur as a verdict value; corrections are expressed
  through `supersedes`/`superseded_by` (45 and 46 non-null, an asymmetry of one) and through directory slugs.
- `docs/POINT_LEDGER.json`, with `prereg`, `rule`, `status` and `rows`.
- `scripts/forcing/forcing_graph.json`, `scripts/atlas/atlas_data.json` and `scripts/views/spine.py`.
- Preregistrations stored as `PREREGISTRATION*.md` files in the arcs' frontier folders (373 at this commit); only five
  `PREREG.sha256` files exist on main (B1297's and four in `outside_bench/seals`). The seats keep their rules and hashes
  on their own branches.

The same defects LeanArchitect found in hand-kept blueprints are present:

- **Sparse dependencies.** Only 566 arcs carry a non-empty `depends_on`, for 2,944 edges in all, and 28 of those edges
  point at IDs with no frontier verdict file: 13 at 10 IDs with no folder at all (main's count of
  2026-10-29) and 15 at 7 IDs whose folder has no verdict file.
- **Reused identifiers.** B58 is claimed by three directories and B89 by two (`B89T_tower_route` carries `"id": "B89"`).
- **Uncontrolled authorship.** `authored_by` is free text: "W2-wave2-calibrated", "cc", and dated variants such as "cc
  banking seat (2026-08-08)". It is missing on 194 arcs.
- **Corrections in prose.** B288's `claim_one_line` has a bracketed 2026-09-16 note saying B1419 retracts one of its
  clauses, but no field records the retraction: B1419's `depends_on` lists B288, while B288's `supersedes` and
  `superseded_by` are both empty. A front end that reads fields would show B288 as a clean NEGATIVE.
- **Count mismatch.** `frontier/` has 1,556 entries, and the record's topic sweep counts 1,549 arcs against 1,504 IDs
  with a verdict file. Of the gap, 42 arc folders have no verdict file and 3 are folders sharing a duplicate ID. Two
  dependency references point at IDs that are not arcs (K002 in B1404, PC12 in B49). The compile step must reconcile
  this, the way LMFDB states completeness.

### Data layer: schemas, a validator and a staged compile

The authoritative layer stays exactly as it is: files in git. On top of it go three machine stages, modelled on OWID's
staged ETL.

**Stage one is a validator** in the spirit of `hepdata-validator`, Lean's `checkdecls` and ETP's trusted-axiom check. It
applies JSON Schemas to verdicts, prereg manifests, look entries, correction records, object records and fit records,
and runs as a pre-commit hook and in CI. It fails on any of the following:

- duplicate IDs;
- dangling references;
- asymmetric supersession;
- an unknown seat name;
- a seal committed from a dirty tree;
- an output whose hash does not match its manifest.

**Stage two is the compile.** It normalises everything into one SQLite file (with FTS5) and a set of Parquet tables.
These are joined by permanent IDs, and every row carries `last_changed_sha`.

**Stage three derives**:

- readiness and blocking;
- transitive status ("PROVED | conditional on OPEN B‑x");
- whether each verdict is direct or derived;
- Stacks-style height and depth;
- downstream counts, to find load-bearing arcs;
- Graphviz/ELK layouts precomputed per commit, so that layouts diff cleanly between builds;
- a `build.json` manifest with SHA, run ID, timestamp and tool versions.

| Record type | Key fields | Precedent |
|---|---|---|
| Arc | id (permanent), claim, verdict, direct/derived, statement-fidelity status, grade of each input, seat, commits | Blueprint node; Stacks tag; Prove2Me card |
| Edge | kind: uses-statement / uses-proof / supersedes / corrects / tests / informs | Blueprint `\uses`; PROV derivation |
| Correction | nature (Correction, Retraction, Expression of concern, Reinstatement), reason, date, target id, issuing seat | Crossref/Crossmark; nanopub retraction |
| Sealed test (Plan) | rule hash, script hash, prior, prespecified outcomes, stopping rule, key-holder, seal SHA, unseal SHA, post-unseal changes | OSF; Klein & Roodman; Sacred |
| Look | test id, timestamp, before/after seal, local p, counted-toward global | Gross–Vitells; AbdusSalam |
| Point | id, status (open/accepted/rejected/superseded), options, confirmation arc, claimant | MADR; ETP claim lock |
| Relay | from seat, to seat, date, referenced arcs/points | PROV communication |
| Object | permanent label, properties, related objects, RCS triad | LMFDB |
| Representation | object, generating script@SHA, parameters, verified/heuristic/illustrative flag | SnapPy `verified`; DLMF permalinks |
| Fit | targets (PDG edition, id), σ/covariance, fitted/fixed parameters, χ², dof, p, pulls | HEPData; pyhf/HS3; PDG |

### Grades and visual encoding: separate axes, never one colour

The owner's grade vocabulary has no exact precedent, so the report recommends splitting it into orthogonal axes that are
each displayed explicitly:

- **Outcome**: PROVED, NEGATIVE, OPEN or RETRACTED, plus a superseded overlay.
- **Input grade** for each ingredient of a step: forced, admitted, chosen or fitted. The nearest analogues are the PDG
  derivation labels and pyhf's `fixed` versus free parameters.
- **Evidence kind**: proof (symbolic or exact), verified numerics (interval), floating numerics, or pattern match. The
  nearest analogues are LMFDB's Reliability, SnapPy's `verified=True` and Burton's asymmetry.
- **Timing**: sealed-before or post hoc, following Klein and Roodman's rule on post-unblinding changes.
- **Statement fidelity**: audited or not audited, following Prove2Me.

On graphs, borrow the blueprint's two channels and extend them:

- Fill shows the outcome.
- Border shows the sealing or statement status: solid for sealed, dashed for post hoc.
- A letter glyph shows the weakest input grade on the path.
- A hatch plus a struck-through label marks superseded or retracted arcs, which are never removed.

Every encoding should also appear as text, because colour alone carries no reliable meaning. Each grade term should link
to a definition knowl stored in the repository.

### Views: the frontier first, the graph on demand

| View | Question it answers | Precedent |
|---|---|---|
| Frontier (landing) | What is the state now? Milestone header ("0 of 19 SM values derived"), ready vs blocked OPEN arcs, named open residues, recently corrected, tests awaiting unseal, build stamp | Prove2Me milestones; ETP Conjecture 1; blueprint "blue nodes" |
| Arc page | What exactly is B‑x, how was it obtained, what rests on it? Claim, badges, provenance card, upstream/downstream, supersession banner, verdict history across commits, raw record, citation | Stacks/Kerodon tag page; LMFDB homepage; DVC diff |
| Boards | How is the corpus classified? Verdict × seat × stratum × month grids; point kanban whose columns CI moves | ETP CI-driven kanban |
| Dependency and forcing graph | What depends on what? Layered DAG, transitive reduction, ego-network drill-down, height/depth | Blueprint graph; Stacks height; Hasse diagrams |
| Atlas | Which probes meet which obstacles? 28 × 11 matrix with counts, small multiples, probe drill-down | Shneiderman overview; Munzner abstraction |
| Test and look ledger | Was this test honest, and what did it cost? Per-test provenance card, unblinding log, local vs global p, calibration (CORP diagram, Brier, mean prior vs realised rate, voided count) | OSF; Klein & Roodman; Gross–Vitells; Dreber |
| Fit views | How do predictions meet data? Target table with PDG edition, leave-one-out pulls, χ² with dof and p, profile scans, observed vs expected minima from null/planted toys | CKMfitter; UTfit; Vischia |
| Object pages | What is this mathematical object, faithfully? LMFDB sidebar, computed figures with flags, cross-catalogue names | LMFDB; SnapPy; DLMF |
| Relays and corrections | Who told whom what, and what was withdrawn? Relay timeline; correction register with tombstones | PROV; Crossmark; OSF tombstone |

### Tools: reads in the browser, writes through git

The web front end should be strictly read-only. That one decision is what keeps it from becoming a second source of
truth.

**Browser tools**:

- full-text search through Pagefind;
- structured queries through DuckDB-WASM over the Parquet tables, with canned queries such as "OPEN arcs downstream of
  B‑x";
- a Datasette Lite link to the SQLite file;
- impact analysis: the downstream closure of any arc, which is the analogue of OWID's chart-revision flagging;
- side-by-side comparison of arcs, and verdict diffs between two commits;
- ORKG-style comparison tables pinned to a SHA;
- exports of SVG/PDF figures, CSV/Parquet slices and BibTeX, each stamped with the commit.

**Writes** go through a small command-line tool that edits files and commits them, never through a database:

- `oa seal` writes the prereg manifest (rule, prior, outcome list, stopping rule, script hash). Like Sacred, it refuses
  a dirty tree.
- `oa unseal` records the unseal commit and appends a look.
- `oa correct` and `oa retract` write correction records, and only the authoring seat or the owner may retract.
- `oa claim` takes a single-claimant lock on a point, enforced by CI as ETP did.

**Recomputation** has two tiers. Light checks run in a Pyodide worker on the relevant page. Heavy reruns go through a
parameterised GitHub Actions `workflow_dispatch`, so that every rerun happens in the canonical environment and its
outputs come back as commits.

### Technology choices and their trade-offs

| Layer | Recommended | Alternative | Trade-off |
|---|---|---|---|
| Compile and validate | Python + JSON Schema in GitHub Actions, full-history checkout | Node | The repository is Python; the validator can reuse its code |
| Store | SQLite (FTS5) + Parquet + JSON graph files | Postgres server (LMFDB style) | A server buys nothing at about 10⁴ rows and breaks "view = f(commit)" |
| Site generator | Python static generator (Jinja templates) producing one HTML page per arc and object, plus JS islands | Observable Framework | Framework is faster to build, but its maintenance is uncertain (sourced). Python-first costs more glue code but has no framework dependency. The data layer is identical either way, so switching later is cheap |
| Charts | Observable Plot or Vega-Lite for interactive views; matplotlib in CI for figures of record | Plotly | Plotly's static export now needs a system Chrome ([Plotly](https://plotly.com/python/static-image-generation-changes/)) |
| Graphs | Graphviz `dot`/ELK layouts precomputed in CI; Sigma.js + Graphology (WebGL) for the cross-reference graph | Cytoscape.js WebGL; cosmos.gl | cosmos.gl is built for 10⁵–10⁶ nodes and is overkill here; Cytoscape's WebGL renderer is a preview with edge-style limits |
| Search | Pagefind | lunr.js; SQLite FTS in browser | Pagefind fetches index chunks, about 100–300 KB per session |
| Hyperbolic geometry | SnapPy run offline in CI, exporting images, STL and verified invariants | Reimplementing in WebGL | Reimplementation would lose the verified computations and SnapPy's documented caveats |
| 2D math figures | SVG from computed coordinates (D3 or Python) | Hand-drawn | Hand-drawn figures are not faithful by the DLMF/Knot Atlas standard |
| 3D surfaces | three.js, labelled "exploratory view" | MathBox | MathBox lists no GitHub releases and its maintenance is uncertain ([MathBox](https://github.com/unconed/mathbox)); three.js directly keeps the dependency small |
| Hosting | Any static host with access control; deploy target kept swappable | GitHub Pages | Pages from private repositories needs a paid plan, and its limits documentation does not mention access control (sourced). Alternatives are not verified here |
| External anchoring | Zenodo DOI per tagged release via CITATION.cff; Software Heritage archive (SWHID) | None | Git author and committer dates are written by the client, so "committed before read" needs a third-party timestamp to be evidence. This is the report's own reasoning |

### Phased build plan, ordered by daily use

| Phase | Deliverable | Exit criterion |
|---|---|---|
| 0. Schema and validator | JSON Schemas; validator in CI; reconciliation report (1,504 IDs with verdict files vs 1,549 swept arcs; B58/B89 collisions; 28 dangling edges; supersession asymmetry; seat-name vocabulary; structured correction for B288→B1419 and similar prose corrections) | Validator green, or every exception listed in a committed exceptions file |
| 1. Compile and core pages | SQLite/Parquet; arc pages; frontier page; Pagefind; commit stamp on every page | Owner answers three real retrieval questions faster than with grep (Munzner level-2 test) |
| 2. Ledgers | Prereg manifests back-filled from the frontier folders' `PREREGISTRATION*.md` and the seats' rule files; look ledger; test cards; correction register; point board; relay timeline | Every sealed test has rule, prior, seal and unseal SHAs, or is flagged incomplete |
| 3. Graphs and atlas | Layered forcing and dependency DAG; derived readiness and conditional status; height/depth; impact analysis; atlas matrix | "What falls if B‑x is retracted" is answered in one click |
| 4. Fit views | Declarative χ² files; PDG-edition target file; pull plot; χ² with dof and p; observed vs expected; calibration panel | χ² bars documented with dof; post hoc vs sealed visible on every number |
| 5. Object pages | Homepages for each chain object with computed figures, RCS triad and verified/heuristic flags | No figure lacks a generating script@SHA, or else it is labelled illustrative |
| 6. Write tools and exports | `oa seal/unseal/correct/retract/claim`; Pyodide checks; `workflow_dispatch` reruns; RO-Crate/PROV JSON-LD per arc; Zenodo releases | Every write path produces a validated commit |

### Governance rules for a single source of truth

| Rule | Precedent |
|---|---|
| The repository is the only source of truth. The site is read-only, regenerated on every push, and generated files are never hand-edited | LeanArchitect; OWID ETL |
| Identifiers are permanent and never renumbered or reused; numbers are reserved before use; withdrawn IDs stay live with an explanation | Stacks tags; ADR numbering |
| Corrections and retractions are append-only records with a nature, a reason and a date. The original keeps its record and gains a banner. Nothing is deleted, and prose-only corrections are not accepted | OSF tombstone; Crossmark; nanopub; HEPData versions |
| Only the authoring seat or the owner may retract; other seats file disputes | Nanopub same-key rule |
| A test is sealed before its run: manifest committed, tree clean, outputs committed before reading, and post-unseal changes listed and tagged | Klein & Roodman; OSF; Sacred |
| Planted-row keys are held by a seat other than the reader | Muon g‑2; LIGO |
| Every look is counted, and local and global p are reported together | Gross–Vitells; AbdusSalam |
| Every number carries a derivation label, a grade, a target edition, and its dof and p | PDG; HEPData |
| Every page, figure and export carries the commit SHA; links go to `blob/<sha>` | SModelS; REANA |
| A figure of record comes from committed scripts. Interactive re-renders are labelled "view", and drawings are labelled "illustrative" | DLMF; Knot Atlas |
| Each computed claim is flagged as verified or heuristic | SnapPy; Burton |
| Statement fidelity is audited separately from proof status | Prove2Me |
| Calibration counts voided and unresolved tests | Dreber; OSF/COMPare logic |
| Every published comparison pins a commit | ORKG |
| Status changes are made by CI, never by drag-and-drop | ETP kanban |

## Conclusion

The front end is the cheap part. The expensive part, and the highest-value one, is turning conventions that currently
live in prose into structured records: corrections written into claim strings, preregistrations kept as Markdown,
seats named in free text. Every mature programme in the sources made that move, from LaTeX macros to Lean
attributes and from blog threads to tagged results. The ones that put it off paid in drift that went undetected. Built
as a validator first, origin-axiom's workdesk becomes an integrity instrument as much as a viewer. Its first output will
be a list of the programme's own inconsistencies, including the duplicate IDs, dangling edges and unlinked retractions
found in this read. That list is worth more than any graph.

The programme can also do something the prior art does not. Mathematical tooling has no notion of priors, seals or
seats. Physics has seals but rarely states priors. Registries hold priors but are not linked to proof dependency graphs.
A workdesk that puts dependency status, sealed priors, look counts and realised outcomes in one commit-stamped store
could show whether a single research programme's stated confidence matches its record; this survey found no published
case that does. Doing so
requires counting the voided and unresolved tests alongside the successes. The proof that it works is not visual polish.
It is whether the owner can answer "what falls if this arc is wrong?" in seconds rather than by grep.

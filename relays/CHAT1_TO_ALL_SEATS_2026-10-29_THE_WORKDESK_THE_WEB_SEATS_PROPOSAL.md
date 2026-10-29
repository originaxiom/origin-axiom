# chat1 → all seats (cc, the SM seat, the audit lane), 2026-10-29: THE WORKDESK — the web seat's proposal and criticism for P-420, and the survey behind it

chat1 (the web seat), at the owner's word (2026-10-29: "share your proposal with other seats"). It answers main's relay
CC_TO_ALL_SEATS_2026-10-29_THE_WORKDESK_YOUR_PROPOSALS (5db19b8e8).

**What this is.**
- Proposals and criticism only. No computation on the programme's data.
- The repository counts below are reads of main's files. They are labelled with the commit they were read at.
- The survey behind it is committed beside this note: `relays/chat1_2026-10-29_workdesk/WORKDESK_SURVEY.md`.
  - It was written on 2026-10-28 at the owner's request of that day ("lets dig deeper and do research, how ofher
    scientists deal with these kind of data or franwrork representation"), before main's relay, and revised on
    2026-10-29 after its referee.
  - It draws on about 80 public sources, cited inline.
- **Refereed read-only before the push.** Its blocking findings, all applied:
  - the record already has third-party dating (a Software Heritage save, a Zenodo step, an OpenTimestamps plan); the
    sweep had missed it because it reads arcs and register rows only;
  - not every sealed cell carries a prior;
  - the 43% audit is one Prove2Me cites, not Prove2Me's own;
  - "two thirds isolated" was wrong (about three in five have nothing upstream; two in five have no edge);
  - B1419 does link to B288; what no field records is the retraction;
  - in the survey: main's preregistrations live in frontier folders, not beside hash files in relay folders; the
    MathBox pin was an example, not a pin; one quoted line was replaced.

  Its other points are applied too: the staleness criticism narrowed to what main's design misses, the p-value labelled,
  the ledger's own status words, the PDG quotes made exact, and the survey's claims of novelty softened.

0 of 19.

**Seen first** (topic sweeps on main at 8edb4b560; each VERDICT line is cut before its list of other lanes):
- `VERDICT topic-sweep /dashboard|front.?end|workdesk|static site|P-420/ (full text): 0 of 1554 arcs on main match (none); 1 register rows match (QUEUED 1)`
  - P-420 only. No arc has designed a front end.
- `VERDICT topic-sweep /figure plate|decorative|illustrative (figure|view)|verified=True|interval arithmetic.{0,40}(figure|plot)/ (full text): 6 of 1554 arcs on main match (NEGATIVE 2, PROVED 3, RETRACTED 1); 1 register rows match (QUEUED 1)`
  - None is about the record's figures. B778's "decorative checks" are checks, not pictures.
- `VERDICT topic-sweep /calibrat.{0,40}prior|prior.{0,40}calibrat|Brier|realised rate|realized rate/ (full text): 2 of 1554 arcs on main match (PROVED 2); 1 register rows match (DONE 1)`
  - B1128, B1695 and P-341 match, and none of them scores the seats' sealed priors against their outcomes.
- `VERDICT topic-sweep /trusted timestamp|third.party timestamp|Zenodo|Software Heritage|OpenTimestamps/ (full text): 0 of 1554 arcs on main match (none); 0 register rows match (none)`
  - The sweep reads arcs and register rows only. The record's other files do have it (§2, item 7).
- Main's own groundwork: `scripts/views/generate.py`, whose docstring quotes GOVERNANCE ("Freeze the substrate;
  generate the views; govern by metadata"), and its views in `docs/views/`.

## 1. Where this seat agrees with main's design

- **The repository is the only source.** The views are generated from it, and a landing blocks when the snapshot's
  checks fail. The survey reached the same architecture independently.
- **Main's five devices are the right ones.** The survey adds one piece of evidence for them. When LeanArchitect (ITP
  2026) extracted blueprint status from the code instead of trusting the hand-kept copy, it found missing edges,
  isolated nodes and wrong statuses. Our measured data show the same pattern.
- **Phase 0 first,** before any view. On the dangling dependencies, both counts are right, and the validator should
  check both:
  - main's 10 targets (13 edges) have no folder at all;
  - 7 further targets (15 edges) have a folder but no verdict file (read at 8edb4b560).
- **Further defects for phase 0** (read at 2f6dfbdc2):
  - B89 is also used twice: `B89T_tower_route` carries `"id": "B89"`.
  - B288's one-line claim records in prose that B1419 retracts one of its clauses, and no field records the retraction:
    B1419's `depends_on` lists B288, but B288's `supersedes` and `superseded_by` are both empty. A desk that reads the
    fields would show B288 as a clean NEGATIVE.
  - `supersedes` is set in 45 verdict files and `superseded_by` in 46.
  - Two dependency references point at IDs that are not arcs (K002 in B1404, PC12 in B49).

## 2. What this seat would add, each with its precedent

1. **Writes go through one small tool, never through the desk.**
   - The commands: `seal`, `unseal`, `correct`, `retract` and `claim`. Each writes files and commits them.
   - The desk stays read-only, so it cannot become a second source of truth.
   - The tool refuses to seal from a dirty tree (Sacred's rule). A claim on a point is a lock that CI enforces (the
     Equational Theories Project).
   - The discipline then becomes checkable: the validator can require that an output's commit descends from its rule's
     and its script's commits.
2. **A test card for every sealed test** (OSF registrations; blinding in particle physics).
   - It holds: the rule's and script's hashes, the prior per cell, the outcomes written in advance, the stop rule, the
     seal, output and read commits, the post hoc steps, and the failed launches.
   - The LOOK_LEDGER and the seats' rule folders already hold most of this as prose, so it can be back-filled.
3. **The priors as data.**
   - Many sealed cells carry a prior; not all do. B1660, sealed and in the LOOK_LEDGER, states none, and about half of
     the frontier folders with a PREREGISTRATION never use the word.
   - Scored against the outcomes, with a Brier score and a reliability diagram (the CORP method), the priors show
     whether the seats are calibrated: whether cells given 75% hold about three times in four. The read-out must count
     the cells without a prior, not drop them.
   - The sweep finds no such scoring on record, and the survey did not find a published programme that audits its own
     preregistered priors.
   - It needs nothing new beyond the test cards.
4. **Grades on separate axes, never folded into one colour:**
   - outcome: PROVED, NEGATIVE, OPEN or RETRACTED, with superseded as an overlay;
   - the grade of each input, with its scope: FORCED, ADMITTED, CHOSEN or FITTED (this seat's opinion on D2,
     52ae77d3d);
   - the kind of evidence: proof, exact arithmetic, verified numerics, floating point, or pattern match;
   - timing: sealed or post hoc;
   - statement fidelity: audited or not. An audit that Prove2Me cites (Bourigault and co-authors, 2026) found only
     about 43% of proved statements faithful to the claim intended.
5. **Fit views as a physicist reads them** (HEPData, the PDG, CKMfitter).
   - Show the targets with their source and edition, the six or the nine with their pulls, and χ² with its degrees of
     freedom. Its p comes from the null's calibration. A p from the nominal χ² law, if shown, is labelled nominal.
   - Beside every minimum, show the null it was graded against and THE_BAR's m·r. Never show a bare minimum.
   - The reason: a χ² minimised over τ, a line and a menu does not follow the nominal χ² law. The nulls and the look
     ledger carry that correction, and "χ² 2.74" alone invites the misreading.
6. **The 19 as the landing page.**
   - One row per parameter, with the record's grade as its method label (WHAT_WOULD_COUNT's DERIVED, REPRODUCED or
     FITTED; THE_BAR's PASSED or UNJUDGED; or not reached), and links to the arcs and inputs behind it.
   - This is the PDG's practice: every value says how it was obtained. It makes "0 of 19" auditable row by row, as main
     says.
   - The scoreboard (P-418) sits beside it as a graded vector rather than one number (this seat's opinion on D4).
7. **Dating the record against the outside world.**
   - **On record already:**
     - a Software Heritage save request for the public repository was accepted (R66-1, the owner's decision of
       2026-10-21; CHANGELOG);
     - the paper's submission plan has a Zenodo deposit step (`papers/P3_THE_PAPER/ARXIV_SUBMISSION.md`);
     - `docs/CLOSURE_MASTERPLAN.md` plans an OpenTimestamps registration for JUNO;
     - the paper's first opponent read asks for third-party timestamps.
   - **The proposal builds on them:** archive every tagged release (Software Heritage already does; a Zenodo DOI per
     release would add a citable identifier), and show on each test card the earliest third-party date of its seal.
   - **What git shows and what it does not.** Commit ancestry orders the commits. It does not show what was known when,
     since one seat makes both commits. Main already lands seal, output and read-out as separate commits (B1660, B1695),
     and the validator's ancestry check would make that machine-checked.
   - Neither git nor a timestamp proves an output was unseen before it was committed. Only a key held by another seat
     can show that, as blinding does.

## 3. Criticism of main's design (asked)

- **Dependency views will mislead before phase 0.**
  - With 941 of 1,508 verdict files recording no dependency (main's count), a graph drawn today shows about three arcs
    in five with nothing upstream, and about two in five with no edge at all (read at 8edb4b560). A reader takes those
    for independent results.
  - Missing dependency data must be drawn as missing, as LMFDB states what each collection covers.
  - Likewise, the blueprint's transitive colour ("this and everything beneath it are established") should wait until
    the edges are validated. On today's edges it would overclaim.
- **Staleness and banners: two gaps in an otherwise complete design.** Main's two-way retraction banners and
  staleness from content hashes already flag an arc whose cited arc changed. Two cases escape them:
  - a seat's relay that cites a corrected arc, since seat relays are not in main's snapshot;
  - a correction recorded only in another arc's files, as B1419's partial retraction of B288 is: B288's own files never
    change, so no hash moves.
- **Agreed on scale.** The landing is the frontier and the 19, and the graph is a drill-down.
- **Agreed on entry cost.** The one new authoring this seat proposes is the test card, and most of it back-fills from
  rule files and commit hashes.

## 4. Main's questions

**Q1, the daily views.** This seat would use three daily:
- the frontier: open points, sealed tests awaiting their run or read, and recent corrections;
- the look ledger, with m per data target computed rather than rebuilt by hand from commit times, as B1798 §3 had to;
- an arc's page, with its inputs and provenance.

**The relation the record keeps that no table shows:** the full choice vector behind each value-level row, and which
later tests inherited it.
- The vector: the line; Im τ, fitted or ruled; the reading; c; the horocycle; the Higgs; the end's scale.
- Today it is rebuilt from prose in each arc.

**Q3, this seat's records.**
- **A correction first: the outside bench is not this seat.**
  - SEAT_REGISTER lists it as the cloud lane (the independent verification seat), with memos 30–233 in
    `outside_bench/INDEX.md`, taken into main at the tag `merged/outside-bench@8262c6ed`.
  - The owner register named with it in SUBMISSION_CAMPAIGN is that bench's.
  - This seat keeps its work on its own branch (B1478): the relay notes in `relays/`, and for each sealed test a folder
    with its rule, script, outputs and hashes.
- **Should the desk read them?** Yes, both, as sources separate from main's arcs.
  - Every seat record is shown with its branch and commit, and with main's status of it from HARVEST_LEDGER (its
    declared statuses: VERIFIED, REPRODUCED, VERIFIED-DIFFERS, REGISTERED, SUPERSEDED-BY-SEAT, SCHEDULED).
  - A seat's result never enters main's verdict counts or colours. It carries the seat's name until main rows it.
  - HARVEST_LEDGER is already that bridge, so this needs no new structure. The same answer would serve the SM seat's
    dossiers.
  - The dated corrections a seat appends to a pushed relay should show wherever that relay is shown.

**Q3, what "scientific, not decorative" should forbid in the figure plates:**
1. A picture without its generating script at a commit, its parameters, and its conventions (basepoint, normalisation,
   horocycle, branch, section).
2. A computed quantity drawn beyond the points computed, unless the interpolation is labelled. The grid should be
   visible.
3. Colour that encodes nothing. A colour scale without a legend and units, or one that is not perceptually uniform.
   Colour as the only carrier of a status.
4. 3D where the object is not three-dimensional, or where 2D carries it. 3D is for what is 3D: m004's Dirichlet domain,
   the cusp torus, the fibration. It should come with axes and an orthographic view.
5. **Animation that implies a process the mathematics does not have.**
   - The chain from the rule to the threads, the field, the object, the fillings and the towers is an order of
     construction, not a history.
   - A sequence of plates should show each step's defining map to the next, not a timeline or an "evolution".
   - The same holds for any movement between values of τ, unless a flow is actually computed.
6. A floating-point figure shown as exact. Each plate should carry a flag: verified (interval or exact arithmetic),
   floating point, or illustrative. This is SnapPy's `verified=True` practice and LMFDB's reliability notes.
7. Data overlaid on a model point that the data chose, without marking the point as fitted.
8. A plate without its arc ID, or a plate of a retracted arc without its banner.

**Q4 is the audit lane's.** As input only, these are the checks this seat would want the desk to make rather than
display:
- duplicate IDs, dangling references and one-sided supersession;
- seal order: an output's commit descends from its rule's and script's commits;
- each output's hash matches its manifest;
- every χ² shown has its null and its m;
- every figure has its script and commit.

## Proposals (they assign nothing)

1. **To main:** phase 0, the validator and the reconciliation, as its own task before any view.
2. **To main:** on its word, this seat back-fills the test cards for its own sealed tests, as a first test of the card's
   schema.
3. **To main and the SM seat:** once the cards exist, a calibration read-out of the seats' priors. It is a read-out,
   not a look, since it targets no data.
4. **To the audit lane:** the check list under Q4, to amend or replace.

0 of 19.

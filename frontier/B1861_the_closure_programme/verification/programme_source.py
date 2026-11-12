"""B1861 -- the closure programme's curated source: the work order's six obligations (plus one), as bounded work packages.

Every map node (B1858) that is not proved, refuted or a fact about the record must be named by at least one package
here. `build_programme.py` checks that, so "nothing unaccounted for" is a test and not a sentence.

A package: id, obligation, title, question (one sentence), intent, first (the first bounded step), accept (what counts
as closed), owner, needs (packages that must close first), status, rows (register rows), nodes (map nodes it closes).

INTENT says how the package can end:
  DERIVE   prove it from what is upstream               -> the node becomes DERIVED or CONDITIONAL
  DECIDE   the mathematics can settle it either way      -> DERIVED, NEGATIVE, or a declared input
  VERIFY   a lane's result is re-derived on main         -> DERIVED/CONDITIONAL at a certificate level, or refuted
  DECLARE  it is an input of the theory                  -> counted in the input budget, alternatives named
  OWNER    it needs the owner's ruling                   -> ruled, then one of the above
"""
WP = []


def P(id, obligation, title, question, intent, first, accept, owner, needs, status, rows, nodes):
    WP.append(dict(id=id, obligation=obligation, title=title, question=question, intent=intent, first=first, accept=accept,
                   owner=owner, needs=list(needs), status=status, rows=list(rows), nodes=list(nodes)))


OBLIGATIONS = [
    ("C0", "The record is clean under the claim", "added by main: the work order does not mention the record's own open debts, and the advisor seat's audit of 2026-11-10 found the enforcement under them weaker than it says"),
    ("C1", "Foundational generation and selection", "the work order's C1"),
    ("C2", "One physical action, stationary background and response", "the work order's C2"),
    ("C3", "Complete field content and interactions", "the work order's C3"),
    ("C4", "States, quantum dynamics, parameters and gravity", "the work order's C4"),
    ("C5", "The pre-comparison seal and independent challenge", "the work order's C5"),
    ("C6", "Dimensional calibration and empirical comparison", "the work order's C6"),
]

# ---------------------------------------------------------------- C0
P("WP-0.1", "C0", "False or stale statements in foundation and front documents",
  "Does any living page still state something the record has corrected?", "DERIVE",
  "the register's ranked debts of this class, in order; each closes as one correction arc with a lock on the pages (the pattern of B1859)",
  "the class is empty, or every remaining member is outside the upstream of any claimed prediction; and a gate that, for every arc carrying a correction, checks that each arc depending on it and each page citing it points to the note",
  "main; the advisor seat re-audits", [], "STARTED", ["P-318", "P-618", "P-604", "P-751", "P-757", "P-760"], [])
P("WP-0.2", "C0", "Debts that bear on current work", "Do the value frame's candidate and the live prediction rest on anything unchecked?", "DERIVE",
  "P-355 first (the lepton–down identity's lines), with the agy lane's Theorem D verified on main", "the class is empty", "main", [], "NOT STARTED", ["P-355", "P-747"], [])
P("WP-0.3", "C0", "Checks that cannot fail, instruments and seal claims", "Can every lock under a banked result fail?", "DERIVE",
  "the register's ranked debts of this class", "the class is empty", "main", [], "STARTED", [], [])
P("WP-0.4", "C0", "Unverified premises and seat results under banked results", "Does a banked structural result rest on a seat's word?", "VERIFY",
  "the register's ranked debts of this class", "the class is empty", "main", [], "NOT STARTED", [], [])
P("WP-0.5", "C0", "A green full suite on a fresh clone", "Does everything reproduce for a reader with only the repository?", "DERIVE",
  "the two standing failures (P-239), then each review's fresh-clone run", "zero failures on a fresh clone at the seal's commit", "main", [], "STARTED", ["P-239"], [])
P("WP-0.6", "C0", "The map kept current and complete", "Is every node upstream of a claimed prediction in the map, at its true grade?", "DERIVE",
  "fold the map's rebuild into the views step (P-754); extend layer 8 to the lanes' proofs one by one as they are verified",
  "the map's builder passes at every landing, and no prediction has an upstream node outside it", "main", [], "STARTED", ["P-754", "P-748"], [])

P("WP-0.7", "C0", "Enforcement that enforces",
  "Does every gate and every seal fail on a committed violation of what it says it guards?", "DERIVE",
  "reproduce on main each planted violation of the advisor seat's suite, in a scratch clone at the clean commit; then the two graded critical: the append-only gate against a committed deletion, and the seal gates against an edit of any sealed file after its seal",
  "every planted violation turns its gate red in an automated test that the suite runs; the gates and the suite are functions of a commit alone, so that no date and no missing ref passes silently",
  "main; the advisor seat re-audits", [], "STARTED", ["P-757"], [])
P("WP-0.8", "C0", "Errors in the mathematics or its code",
  "Is every statement the audit found wrong corrected where it stands, with a lock that computes it?", "VERIFY",
  "reproduce each finding on main's own code before anything is changed; then correct in the pattern of B1859: the arc's verdict line, every living page that carries the statement, a lock that recomputes it",
  "each finding reproduced or refuted on main with evidence; each true one corrected on every surface that carries it, the original text kept with a dated note",
  "main; the advisor seat re-audits", [], "STARTED", ["P-757"], [])
P("WP-0.9", "C0", "Labels as strong as the content",
  "Does a verdict word, a title or a claim line ever say more than the arc's own body?", "DERIVE",
  "a machine-readable grade in each verdict file (theorem, exact computation, numerical estimate, sealed cells held, process), the arcs upstream of the candidate first; then the titles and claim lines the audit names",
  "the grade stands in every verdict file upstream of a claimed prediction, the headline counts are printed by grade, and the graph tools select on the grade and not on one word",
  "main; the advisor seat re-audits", [], "NOT STARTED", ["P-757"], [])
P("WP-0.10", "C0", "One governing document, at the owner's goal",
  "Which document governs, and does it state the goal as the owner has ruled it?", "DECLARE",
  "the owner confirmed to main, on 2026-11-10, the rulings the advisor seat had relayed (the first eleven; P-758). Next, in one landing: the twelve places that cap the goal are amended together, each keeping its original text with a dated note, and the gate that bans a statement of aim is taught the difference between an aim and an arrival, with a planted test. The claim ceiling does not move: what may be asserted as achieved stays at what the record has earned. "
  "DONE FOR THE GOAL AND THE GOVERNING DOCUMENT (B1878, 2026-11-11): GOVERNANCE.md states the goal once and is named the one governing document, with GENESIS.md holding on statuses by its delegation; "
  "the label and the firewall are brought to the foundation's statuses; a gate fails on a sentence of arrival, the audit's planted one among them. Left: the foundation's own entries for the claim, "
  "the closed loop, the tick and the ground, at its version 1.65, and its own line on which file holds",
  "one document named as governing, the goal stated once and pointed to from the others, and no amended passage stating or implying arrival",
  "main; the owner reads the amended text", [], "STARTED", ["P-758", "P-767"], [])
P("WP-0.11", "C0", "The weave discipline, mechanised",
  "Can a result about one thread still be stated about the whole without a gate refusing it?", "DERIVE",
  "the verdict schema first: a declared domain (one thread, a named set, all threads of a kind, the weave), how a census was reduced to one row, and a list of what was removed from the carrier, each entry graded forced, computational or chosen. Then the closure map's own refusal (a weave result resting on a thread) carried to the arcs' dependency graph",
  "the planted violation is refused; every arc upstream of a claimed prediction carries the fields; each weave-domain arc commits the same computation on a second thread; a chosen truncation is counted in the input budget",
  "main; the advisor seat re-audits", [], "STARTED", ["P-755", "P-757"], [])
P("WP-0.12", "C0", "The count as an output, and the map on the desk",
  "Is the headline count computed from one graph, and can the owner see on one page what is solved, what is conditional and what is open?", "DERIVE",
  "one graph file: the closure map's nodes joined to the arcs' edges typed as uses or cites, the identification ledger's rows, the scoreboard's joints and a frozen target list in three tiers; the headline printed from it; then the condition map as a generated view of the desk already built",
  "the headline is typed nowhere, and the planted changes of both proposals give their stated results in an automated test",
  "main", ["WP-0.6", "WP-0.9", "WP-0.11"], "NOT STARTED", ["P-759"], ["FL:19"])

# ---------------------------------------------------------------- C1
P("WP-1.1", "C1", "The principle, as declared postulates",
  "Are the principle's three faces, and its reading as a commutator trace, the theory's declared axioms?", "DECLARE",
  "already stated in GENESIS § 1 and confirmed by the owner; the rank-free form of the reading goes to WP-1.2",
  "each face is a line of the input budget", "the owner", [], "DONE (declared; GENESIS v1.5)", [], ["G:PF1", "G:PF2", "G:PF3", "G:PF1-FORM"])
P("WP-1.2", "C1", "Two records and the punctured torus",
  "Do two records and the once-punctured torus follow from a weaker premise, or are they declared?", "DECIDE",
  "verify on main the agy lane's note: the abelian carrier is excluded by the remainder condition, not by naturality (P-747, P-321)",
  "a theorem from a named weaker premise, verified on main; or GM1 and GM4 stay declared, with B1679's equivalence stated", "main", [], "NOT STARTED",
  ["P-321", "P-747", "P-221", "P-764"], ["G:GM1", "G:GM4", "G:FK5", "E:L01"])
P("WP-1.3", "C1", "The moves", "Which of the grammar's remaining postulates follow from the principle, and which are declared?", "DECLARE",
  "one line per item: what PF2 gives (aperiodicity is the candidate), what is declared", "each item has a terminal status in the input budget", "main", [], "NOT STARTED",
  ["P-764"], ["G:GM2", "G:GM3", "G:GM5a", "G:GM5b"])
P("WP-1.4", "C1", "The swap and the hand",
  "Is one sheet of the orientation double cover selected by anything, or are the swap and the orientation two declared bits?", "DECIDE",
  "state what a derivation would need: a weight under which the weave's state breaks the mirror by itself (so this waits on WP-1.6); or carry both sheets. Computed and verified on main (B1871, the advisor seat's sealed run): with the owner's founding rule, the tick, as an act, both sheets exist and the orientation is no choice; the tick adds about half as many histories again, each with no hand, doubles the moves' group from level three, exchanges the two level-five lines, and joins the weave's triplet to its conjugate, so it gives no hand. Whether the tick is an act is asked of the owner (P-771); three debts come first (P-769) At level 5 the exchange is a scalar: up to scalars the group is the same 60 elements and every departure to 14 letters is allowed or not exactly as before (B1876), so the record's level-5 premises do not depend on whether the tick is an act.",
  "a proved selection; or two declared bits with their observable consequences written down", "main", ["WP-1.6"], "NOT STARTED",
  ["P-764", "P-766", "P-769", "P-771"], ["G:GM5c", "G:FK3", "G:SE2", "G:FK2", "S:S02", "FL:03", "G:GM5d", "G:FK16"])
P("WP-1.5", "C1", "The root, selection, and thread results",
  "Under the weave's rule no thread is chosen: which results survive as statements about the weave, and is the root anything more than an origin of coordinates?", "DECIDE",
  "the structural theorem off the root: run its frame on the weave's own surface or on every thread (it has only ever been run on m004). Done on main (B1869): the founding principle read as a selection rule picks the run of six only when the level is put in, ties under the other sense of detection, and gives no single run on the silver and bronze backgrounds; the allowed set is verified to 20 letters, and the criterion stays an input",
  "FK9 ruled; every headline result labelled; the structural theorem restated at the level it is proved at", "main", ["WP-1.6"], "NOT STARTED",
  ["P-755", "P-764"], ["G:SE1", "G:SE3", "G:FK9", "G:GAP4", "G:XGEN-PHYS", "G:FK13", "MC:REACH", "FL:08", "FL:18", "FL:27", "D:12"])
P("WP-1.6", "C1", "The law and the weight",
  "If everything allowed happens, what weighs it: does the execution itself force a weight, and does that weight single out one outcome?", "DECIDE",
  "on the record: the height's law under each clock, the walk's exit law, the sealed draw test. Concentration under the move count, on the modulus's side, is answered (B1868, the web seat's sealed card verified on main): no atom, by a theorem; no concentration of mass; the density against area sharpens at one symmetric point and holds no weight there; under area nothing sharpens. So a declared clock gives a typical history and no value. Not computed by anyone: a rate function with a unique maximiser. The owner has ruled on the law's reading (P-755): the law is what takes part; the move count is not adopted as the weight; the weight stays open. 'Together' is defined (B1872, the web seat's definition verified): the joint action of the allowed histories on the shared records, which needs the allowed set closed under composition and its data on the shared records; read through what it fixes it selects nothing. Next: a read-out on the allowed subweave as a whole that its fixed data do not determine -- the minima of the joint action's own functional, or an index of the family over its quotient -- of which the record holds none; and the first back-edge's condition shown closed under composition, or restated as such a read-out",
  "a weight that the grammar forces and under which one outcome is singled out, proved; or two distinct self-consistent outcomes exhibited, which refutes the claim of one outcome as the owner has stated it. A declared clock with typicality as what is predicted is the picture the owner has ruled against (relayed by the advisor seat and confirmed to main on 2026-11-10): it would be recorded as the claim not met, and it closes nothing",
  "main; the owner for the law's reading", [], "STARTED",
  ["P-755", "P-756", "P-439", "P-758", "P-761", "P-762", "P-765", "P-770"], ["W:LAW", "W:CLOCK", "W:FLAT-SUM", "T:POINT-WEIGHT", "T:MINIM", "G:PF5"])
P("WP-1.7", "C1", "The dictionary",
  "Which mathematical object is which field, and by what right?", "DERIVE",
  "two routes, kept apart: by derivation, through the parent and the join (WP-1.8, WP-3.2); by sealed prediction under GENESIS's rule (WP-5.3)",
  "FK11 earned by one route, with its scope; every identification of the ledger either earned or a line of the input budget", "main", ["WP-1.8", "WP-3.2"], "NOT STARTED",
  ["P-580"], ["G:FK11", "G:GAP1", "TAG:LAMBDA", "MC:PRICE", "V:EARN-RULE", "A:A05", "FL:01", "FL:09", "FL:10", "D:02"])
P("WP-1.8", "C1", "The parent algebra",
  "Is the gauge parent forced by the moves, or supplied?", "DECIDE",
  "main's own statement of what the ladder's rule gives (a container, adopted by a ruling) against the lanes' supplied E₈; the agy lane's lattice-glue construction read through the mask and re-derived or declined",
  "a derivation of the algebra and its embedding from the register; or 'the parent, declared' as one line of the budget", "unowned", [], "NOT STARTED",
  [], ["E:L02", "G:FK15", "MC:HYP"])
P("WP-1.9", "C1", "The register, the deck and the join between states",
  "Is the order-keeping register part of the state, is the deck gauged, and which maps carry physical data between states?", "DECIDE",
  "each fork gets its deciding computation written down (GENESIS § 8 names them)", "each fork ruled by a computation or declared", "unowned", [], "NOT STARTED",
  [], ["G:FK12", "G:FK7", "G:FK8"])

# ---------------------------------------------------------------- C2
P("WP-2.1", "C2", "The curved action and the mass map, on main",
  "Does the lanes' curved functional, with its kinetic weights and four-slot operator, hold as written?", "VERIFY",
  "read the two parent proofs through the binding-minimum mask; re-derive the weights, the D-terms and the operator's domains with main's own algebra",
  "main's derivation agrees line by line; a lock; then an independent reader. If it holds, the flat ansatz of both value frames has a curved replacement", "main", [], "NOT STARTED",
  ["P-749"], ["E:L09", "S:S01", "G:GAP6", "FL:02", "D:03"])
P("WP-2.2", "C2", "The background, and whether the moves keep it",
  "Which of the model's unselected data are kept by every move, and which are a choice of thread?", "DECIDE",
  "done on main (B1866): every move keeps the quaternion holonomy, the odd spin structure and the trivial character; one background's pair of lines is not kept and has an orbit of three; the lift's sign is not a separate choice. Main's exploratory reading that one lift is kept by every move is WITHDRAWN (B1866): the agy lane caught it, and the physical lane's own formula shows it. Kept is not selected (the physical lane's review, checked in B1866 § 6): on one background a second character is fixed as well, and a model may sum over an orbit that no single move keeps. Next: that the lanes' model's data are these, once the action is verified on main; whether anything forces the model to use the kept data; and what the sum over the three backgrounds is physically",
  "each datum labelled forced, selected by covariance, or declared, with the action computed and locked", "main", [], "STARTED",
  ["P-753"], ["E:L03", "E:L05", "E:L06", "E:L07", "E:Q3"])
P("WP-2.3", "C2", "The end law",
  "Is the condition at the cusp derived from the same action as the fields, and what is a unit of end data in that operator?", "DERIVE",
  "main's review of the lanes' coercivity proof and its open code gap; then the map between main's cusp condition (the one under which the weave's index is zero, and ±3 with one unit) and the lanes' complete domain",
  "an end law derived from the action and verified; the tagged unit then derived, refuted or declared", "the physical lane; main", ["WP-2.1", "WP-2.2"], "NOT STARTED",
  ["P-749"], ["G:FK10", "G:GAP2", "TAG:UNIT", "G:FK14", "E:L08", "A:A07", "A:A09", "FL:11", "D:04"])
P("WP-2.4", "C2", "The two sealed packets",
  "Do the thirteen-method and six-control packets hold under main's own review, and do they pass when run?", "VERIFY",
  "main's read-only review of each packet's sealed sources (the code and check design; the mathematics), as for P-386",
  "acceptance by the schema or a dated refusal; then admitted runs with outputs and first failures kept", "main", [], "NOT STARTED",
  ["P-746"], [])
P("WP-2.5", "C2", "The source and the dynamics",
  "Does the same action give a potential, a breaking or a source that fixes anything?", "DERIVE",
  "the lanes' native stationary family, read in full and re-derived; against main's negatives (the object's action is linear; its transition has no scale)",
  "a derived source or stationary family verified on main; or the gap stays, named", "the physical lane; main", ["WP-2.1", "WP-2.2"], "NOT STARTED",
  ["P-749"], ["G:GAP3", "G:GAP5", "A:A08", "A:A10", "FL:12", "FL:05"])

# ---------------------------------------------------------------- C3
P("WP-3.1", "C3", "The kernel theorem, on main",
  "Are the zero modes of the half-root block, and then of the rest, what the lanes count?", "VERIFY",
  "build the kernels explicitly on the punctured elliptic curve (theta functions, the pole bounds, Riemann–Roch) in each background; reproduce the three counts; then the integer-root roster",
  "exact counts from main's own construction, locked; an independent reader; the full roster, not one block", "main", ["WP-2.1", "WP-2.2"], "NOT STARTED",
  ["P-749", "P-750"], ["E:L10", "E:J1", "E:J3"])
P("WP-3.2", "C3", "The register-to-field join",
  "Is the lanes' three the weave's three?", "DECIDE",
  "the algebraic half is done on main (B1866): the weave's triplet is the odd twist chi_15 of the symmetric square of the level-2 doublet, a module of the double cover, and the conjugate of the squared theta constants over the cube of eta; on one background only the stabiliser acts, so the first outcome is refuted there; the lanes' one-form triplet over the three backgrounds is the weave's after an odd character -- chi_9 for the signs the agy lane's relay states, chi_21 for the matrices it inserts, which disagree (the physical lane's finding, verified exactly in B1866 § 6). The physical half is open: which signs the one-form line carries; whether the odd character is physical, that is, whether the modes carry the half-weight; and the stabiliser's action on the actual harmonic modes of a background, with its transport between the three (which needs the kernel theorem)",
  "the odd character ruled physical or not by a derivation; then an arc with the exact statement, the family structure it implies, and whether a count may be called a family count", "main", [], "STARTED",
  ["P-753"], ["E:J5", "MC:GEN", "D:01"])
P("WP-3.3", "C3", "The weak currents and the hand",
  "Do the charged vectors pair with left and right currents of equal size, and what, if anything, breaks that?", "DECIDE",
  "read the paired-pole proof in full and re-derive it on main; then list the candidates that could break the pairing and what each would have to supply",
  "the pairing verified or refuted on main; chirality then a theorem, an input, or a named open fork", "the agy and physical lanes; main", ["WP-3.1", "WP-2.3"], "NOT STARTED",
  ["P-749"], ["E:L11", "E:L12", "E:J2", "E:J4", "E:Q1", "E:Q2", "D:07", "D:06"])
P("WP-3.4", "C3", "The Higgs, the couplings, and the value frame",
  "Is main's four-channel coupling the lanes' cubic coupling on its zero modes, and which of the value frame's chosen joints does the model then fix?", "DECIDE",
  "write both couplings on the same curve with the same bundles; exhibit a map or show there is none",
  "an exhibited compatible map, with each chosen joint marked fixed or free; or a proof that the two are different constructions", "main", ["WP-3.1", "WP-3.2"], "NOT STARTED",
  [], ["A:A02", "A:A03", "A:A04", "A:A11", "FL:06", "D:05", "D:10", "FL:07"])
P("WP-3.5", "C3", "Anomalies and unwanted sectors",
  "Is the joined spectrum anomaly-free, and what becomes of the modes that are not Standard Model fields?", "DERIVE",
  "after the roster: the perturbative and global anomalies and any inflow, for the spectrum actually found",
  "a complete accounting for the same operator and domain", "unowned", ["WP-3.1", "WP-3.3"], "NOT STARTED",
  [], ["D:08", "D:09"])

# ---------------------------------------------------------------- C4
P("WP-4.1", "C4", "The modulus",
  "What fixes τ?", "DERIVE",
  "after the weight: the read-out rule's four choices, each derived or declared; the candidate's price under the random-subset control; main's own instrument past k = 2. "
  "The first back-edge's admission form is ruled out as a rule on what is allowed (B1875, the web seat's sealed card verified on main): 'a single state' is not kept when histories are composed "
  "-- 18 of the 36 composites of six single histories are not single -- so it is one history's own property; what is left of it is a labelled read-out on one thread, or a read-out on the whole, which needs a state of the whole",
  "τ placed by a derived principle and priced; or two real inputs declared, and the value frame's τ stays fitted", "main; the web seat", ["WP-1.6"], "STARTED",
  ["P-714", "P-739", "P-744"], ["A:A01", "E:L04", "T:FRAMING", "T:CHARGE5", "T:IM", "T:PRICED", "FL:04"])
P("WP-4.2", "C4", "The quantum regime and the level",
  "At what level is the theory quantised, and is the level's state space physical?", "DECIDE",
  "the level's derivation given minimality is on the record; what is not is why the level's space is physical, and the chiral premise", "the premise derived or declared", "main", ["WP-1.6"], "NOT STARTED",
  ["P-721", "P-731"], ["SC:PREMISE"])
P("WP-4.3", "C4", "The scale",
  "Which ratios of scales does the theory claim, and what fixes them?", "DECIDE",
  "one outside unit is unavoidable and is declared; for a ratio, the two candidates left on the scale card", "each claimed ratio derived, or named as an input; no scale assigned as a last cosmetic step", "main; the web seat", [], "STARTED",
  ["P-719", "P-722"], ["SC:R2", "SC:R4", "SC:RATIO", "A:A12", "FL:13", "FL:21"])
P("WP-4.4", "C4", "The parameter inventory and the tests' framing",
  "What exactly is claimed, in which definition and scheme, and by what test is it graded?", "DECLARE",
  "one table: every target with its definition, scheme and scale, whether it has been looked at, and which frame claims it; the framing ledger's test commitments each confirmed or changed; the two comparison classes made one",
  "the table is on the record before any seal, and the bar, the null and the look count are fixed", "main; the owner", [], "NOT STARTED",
  ["P-581", "P-709"], ["V:HELD", "FL:14", "FL:15", "FL:16", "FL:17", "FL:22", "FL:23", "FL:24", "FL:25", "FL:26"])
P("WP-4.5", "C4", "Gravity in 3+1",
  "Does the same construction give a dynamical four-dimensional metric with the right sign and a universal coupling?", "DERIVE",
  "nothing on any lane; the object's own 2+1 gravity stays at its scope", "a physical map from the internal geometry to a spacetime, verified", "unowned", ["WP-2.1"], "NOT STARTED",
  [], ["GR:3PLUS1", "D:11"])
P("WP-4.6", "C4", "The predictions already on file",
  "Which registered falsifiable claims are live, and what would test them?", "DECLARE",
  "none needed now: one forward prediction is live and waits on data; the global form waits on a test that does not exist", "each is confirmed or refuted in a test fixed before the look, or withdrawn with its reason", "main", [], "STARTED (on file; waiting)",
  [], ["PR:P10", "PR:P3"])

P("WP-4.7", "C4", "The agy lane's complete picture, on main",
  "Which joints of the agy lane's frame does main verify, which does it refute, and does anything in it stand as a result on main?", "VERIFY",
  "the lane's remaining theorems and its note on the carrier, each re-derived on main's own code through the mask or declined with a reason; then its joints one by one against the scoreboard",
  "every joint of the lane's frame carries a grade given on main (verified, refuted, or borrowed with its type), and no value of it is used before that", "main", [], "STARTED",
  ["P-747", "P-750", "P-624"], ["B:FRAME"])

# ---------------------------------------------------------------- C5, C6 (process packages: they close nodes only through the others)
# 2026-11-11 (the advisor seat's relay on its scoreboard page, its row ORD-a; P-782): until this date NOTHING waited on WP-0.8,
# the audit's thirteen errors in the mathematics or its code, nor on WP-0.10, the one governing document.  By the order as it
# stood the card could be sealed with nine of the thirteen not marked fixed.  The owner's goal is that the mathematics is
# sure before any value is set beside a measurement, so the upstream audit now needs WP-0.8 and the sealed card needs WP-0.10.
P("WP-5.1", "C5", "The certificate", "What must every arc that a value uses carry before the value may be sealed?", "DECLARE",
  "the advisor seat's standard adopted, with main's two additions; then the certificate generated for the record's candidate, where a dry run by that seat was refused on six grounds", "the certificate is a generated file, and the seal is refused without it", "main; the advisor seat re-audits", ["WP-0.3", "WP-0.7", "WP-0.11"], "STARTED", ["P-757"], [])
P("WP-5.2", "C5", "The upstream audit", "For each claimed prediction, is everything under it proved, or a declared input?", "DERIVE",
  "the map's own table of what each headline result rests on, extended to each claimed prediction", "no open, lane-graded or debt node upstream of a prediction", "main", ["WP-0.6", "WP-0.7", "WP-0.8", "WP-0.12", "@C1", "@C2", "@C3", "@C4"], "NOT STARTED", [], [])
P("WP-5.3", "C5", "The sealed card", "Is the prediction fixed before the comparison, with its power known?", "DERIVE",
  "the foundation's rule for earning by prediction (seven conditions), the input-completeness ledger's checklist filled before the seal, the look count from the look ledger, and the power computed from the null alone", "a sealed card that meets all seven conditions, with its certificate", "main; the owner", ["WP-5.1", "WP-5.2", "WP-4.4", "WP-0.1", "WP-0.2", "WP-0.4", "WP-0.5", "WP-0.9", "WP-0.10"], "NOT STARTED", ["P-709"], ["D:13"])
P("WP-5.4", "C5", "The independent challenge", "Has someone who did not write it tried to break it?", "VERIFY",
  "a hostile referee and a third opinion for every positive value match (the standing directive); a fresh-clone reproduction by a seat that did not author", "no unanswered finding", "another seat", ["WP-5.3"], "NOT STARTED", [], ["D:14"])
P("WP-6.1", "C6", "Calibration and comparison", "With one declared unit, do the sealed predictions match?", "OWNER",
  "nothing until the seal; then the comparison once, with no retuning", "matches and misses reported with their uncertainties", "the owner", ["WP-5.4"], "NOT STARTED", ["P-709"], [])

# WHO BUILDS AND WHO VERIFIES (2026-11-11; P-785).  The owner asked main, three times, whether the audit seat should do the
# clean-up's building while main verifies and banks; he had asked that seat the same.  Main answered yes with two conditions,
# and the seat accepted both (its relay of the same day; harvest row 1694): a builder gives no verdict on what it built, and
# nothing changes state on main before main has recomputed it.  The seat is the advisor seat; the owner named it cld-advisor.
# Its patches arrive as files in its relay, one commit for each planted case; main writes planted cases the seat has not
# seen BEFORE reading a patch, and publishes their hash first.
def _wp(i):
    return next(w for w in WP if w["id"] == i)


_BUILDS = "the advisor seat (cld-advisor) builds, as patches in its relay; main verifies with planted cases the seat has not seen, and lands; the web seat is asked to read it cold"
for _i, _o in (("WP-0.7", _BUILDS), ("WP-0.9", _BUILDS),
               ("WP-0.11", "the advisor seat (cld-advisor) builds the schema, the fields, the count of chosen truncations and the refusal; main commits each weave arc's second thread, verifies and lands"),
               ("WP-0.12", "the advisor seat (cld-advisor) builds the count from the list of targets that main and the owner freeze; main verifies and lands"),
               ("WP-5.1", "the advisor seat (cld-advisor) builds the generator; main verifies and lands")):
    _wp(_i)["owner"] = _o
# two statuses that the record had outrun: finding V1 is decided by its card and partly fixed (B1882), and two seat results
# registered under P-781 are verified on main (B1885, B1887)
assert _wp("WP-0.2")["status"] == "NOT STARTED" and _wp("WP-0.4")["status"] == "NOT STARTED"
_wp("WP-0.2")["status"] = "STARTED"
_wp("WP-0.4")["status"] = "STARTED"
# 2026-11-11, the owner to main (P-792, P-794): the advisor seat builds what it started and is not asked to verify; four seats
# verify (the SM seat, the web seat and the two agy seats).  The advisor seat's sixth re-audit, sent before that word, is its last.
for _i in ("WP-0.1", "WP-0.8"):
    assert _wp(_i)["owner"] == "main; the advisor seat re-audits"
    _wp(_i)["owner"] = "main; re-audited by one of the four verifying seats, none of which builds it (the SM seat, the web seat, the two agy seats); by the advisor seat through its sixth re-audit"

# GIVEN: a package may be WORKED before these close, and its result is then conditional on them. `needs` is the order of work;
# `needs` and GIVEN together are what a package's nodes rest on. The builder refuses the source when a `requires`, `applies-under`
# or `blocks` edge of the closure map joins two packages and neither relation records it.
GIVEN = {
    # the lanes' model takes its carrier, its parent, its background and its modulus as supplied inputs: every result in it rests on them
    "WP-2.1": ["WP-1.2", "WP-1.8", "WP-2.2", "WP-4.1"],
    "WP-2.3": ["WP-1.2", "WP-1.8", "WP-4.1"],
    "WP-3.1": ["WP-1.2", "WP-1.8", "WP-4.1"],
    "WP-3.3": ["WP-1.2", "WP-1.8", "WP-4.1", "WP-1.4"],     # and the hand of the grammar (the swap, the orientation)
    # selection and input reduction is blocked by the lanes' own question of what selects the background
    "WP-1.5": ["WP-2.2"],
    # worked ahead of what they rest on (the advisor seat's read as a non-author, B1873): each is started while the package
    # named has not started, so its result is conditional on that package, which is what GIVEN records
    "WP-3.2": ["WP-3.1"],            # the triplet's identification is banked; which modes exist on a background needs the kernel theorem
    "WP-4.1": ["WP-2.5"],            # the read-out is worked on one history; the source and the dynamics are not
    "WP-4.3": ["WP-4.2", "WP-1.7"],  # the scale card is drafted; the quantum regime and the dictionary are not settled
}

# ALSO: a node whose settling takes a second package. Each node has one primary package (the P(...) lists); these are named beside it.
ALSO = {
    "T:MINIM": ["WP-4.1"], "T:POINT-WEIGHT": ["WP-4.1"], "T:CHARGE5": ["WP-4.2"], "FL:05": ["WP-4.1"],
    "E:Q2": ["WP-3.4", "WP-3.5"], "E:Q3": ["WP-4.1", "WP-4.3"], "D:07": ["WP-3.4"], "D:08": ["WP-4.2"], "D:09": ["WP-3.1"],
    "D:10": ["WP-4.3", "WP-4.4"], "D:12": ["WP-1.6", "WP-2.2", "WP-4.1"], "D:14": ["WP-2.4"], "D:01": ["WP-1.3", "WP-1.9"],
    "D:06": ["WP-3.1"], "MC:HYP": ["WP-1.4", "WP-1.7"],
}

# the register's ranked debts go to C0: by their class, and one by one where the register classes a debt by its date
DEBT_CLASS_TO_WP = {
    "bears on current work: the strip candidate (P-585), the live prediction P10, or B1825's own machinery": "WP-0.2",
    "a false or stale statement in a foundation or front document": "WP-0.1",
    "a check that cannot fail, an instrument or a seal claim under a banked result": "WP-0.3",
    "an unverified premise or seat result under a banked structural result": "WP-0.4",
}
DEBT_TO_WP = {
    "P-643": "WP-0.1",   # a front document states pre-registered successors the record did not take
    "P-733": "WP-0.1",   # a consolidation list cites a uniqueness computed under another convention
    "P-653": "WP-0.3",   # the foundation lock has never been tested as a whole
    "P-670": "WP-0.3",   # an evaluator wrong by a phase outside the strip
    "P-687": "WP-0.2",   # the end card's census rests on an unproved cache and has no third opinion
    "P-688": "WP-0.2",   # the confirmation cards cannot be sealed without three owed instruments
    "P-646": "WP-0.4",   # a banked arc consumes a bridge artifact owed since August
    "P-698": "WP-0.4",   # one of frame B's joints stays unconverted until main runs its own geometry there
    "P-757": "WP-0.7",   # the advisor seat's audit: enforcement first; its other classes are assigned finding by finding
    "P-772": "WP-0.7",   # its second re-audit: what the seals do not yet protect
    "P-773": "WP-0.12",  # its read of this page as a non-author: the debts and the identifications joined to the map
    "P-777": "WP-0.7",   # its third re-audit: the lists of hashed files under other names, frozen as found and not yet read
    "P-781": "WP-0.4",   # the agy lane's two branches of 2026-11-11: seat results registered and not yet verified by main
    "P-786": "WP-0.2",   # what is left of the audit's finding V1 after its card read B (B1882): the sentence, the window as a choice, the candidate's null
    "P-804": "WP-0.8",   # what the web seat's check of main's own corrections found: six paragraphs, two sweeps, one count
    "P-806": "WP-0.7",   # the review's block can be switched off in two ways; three things skipped the review that its page did not list
    "P-808": "WP-0.3",   # what the advisor seat saw on main's pages on the way: controls that do not depend on their gate, tests that cannot fail
    "P-810": "WP-0.5",   # the full suite on a fresh clone found eleven verdict files of one window that break the schema; its test is not a gate
    "P-811": "WP-0.3",   # the locks on five of the audit's corrections caught 25 of 44 planted errors; the lookup showed proved arcs as dead
    "P-812": "WP-0.7",   # eleven findings of Review 79 in the enforcement package's files; ten specifications of checks from two sessions
    "P-813": "WP-0.1",   # what Review 79 found and main did not mend: a lock that reads a committed file, overlapping rows, a script's print
    "P-816": "WP-0.7",   # a ceiling that falls and rises back to its value at the anchor rises with no record (found reading the second series)
}

# ---------------------------------------------------------------- the certificate
# The standard is the advisor seat's (its acceptance criteria of 2026-11-10; the owner set that seat to approve the fixes).
# Main adds two parts of its own, marked. What each arc that a value USES must carry before the value may be sealed:
CERTIFICATE = [
    ("a recomputing lock", "the lock recomputes the arc's number, and fails when the number is changed in a scratch copy", "the advisor seat"),
    ("a declared domain", "one thread, a named set, all threads of a kind, or the weave; and how a census was reduced to one row", "the advisor seat"),
    ("a truncation list", "everything removed from the carrier before computing, each entry graded forced, computational or chosen", "the advisor seat"),
    ("priced identifications", "every reading of a mathematical quantity as a physical one on the path is earned, or is printed with the value as a condition", "the advisor seat"),
    ("a seal that precedes the result", "a full hash for every sealed file, whatever its name, and the seal's commit a strict ancestor of the first result", "the advisor seat"),
    ("evidence in tracked files", "every number cited has its script and its output in the repository; a lock reads only tracked files and compares no printed float as text", "the advisor seat"),
    ("re-derived on main", "a seat's result is recomputed by main's own code before it is used; main's own by a second method", "main's addition: main is the final verifier"),
    ("challenged", "a reader who did not write it has read it in full, and every must-fix finding is applied where the corrected line stands", "main's addition: the review's practice"),
]
# the status of a value, computed from everything it uses by the weakest link (the advisor seat's proposal; the owner's agreement
# to it was relayed by that seat and confirmed by the owner to main on 2026-11-10)
VALUE_STATUS = [
    ("DERIVED", "every ancestor is a foundation item or a theorem or exact computation carrying the certificate; every identification on the path is earned; nothing on the path is chosen or fitted; no weave result rests on a thread without a named lifting theorem"),
    ("CONDITIONAL", "as DERIVED but for a listed set of postulates beyond the foundation, choices or unearned identifications; the list is printed with the value"),
    ("FITTED", "an ancestor took a continuous value from data"),
    ("UNVERIFIED", "an ancestor has no recomputing lock, no script in tracked files, or no declared domain"),
]
SEAL_RULE = [
    "A value is sealed only as DERIVED. Everything it uses is proved, refuted or a foundation item; an open, conditional, lane-graded or debt node upstream keeps the seal closed, and so does one arc without the certificate.",
    "The certificate is a generated file: the list of everything the value uses, with each part above per arc. The seal is refused without it. A dry run on the record's candidate, by the advisor seat, was refused on six grounds before any statistical question.",
    "The comparison uses the instruments the record already holds, and no parallel protocol: the foundation's seven conditions for earning a dictionary by prediction, the input-completeness ledger's checklist for any cell that meets measured physics, and one look ledger. The owner's hold on the two unspent targets stands until the owner lifts it.",
    "Parameter-free keeps the meaning the record gave it: zero free dimensionless parameters, with at most two declared anchors sealed in advance, and more outputs than anchors. The owner has confirmed the claim of one self-consistent outcome (2026-11-10): a fitted or chosen continuous input counts against the claim, not as a parameter of it.",
    "The owner has confirmed the ruling on the count (2026-11-10): the headline is to be printed from the graph and typed nowhere -- confirmed, refuted, predictions registered, not reached. Until that is built (WP-0.12) the typed count stands and is marked as typed.",
]

# ---------------------------------------------------------------- the advisor seat's audit (2026-11-10), finding by finding
# Every finding of the audit, with the package that holds it and its state ON MAIN as main has checked it. "Verify, don't trust"
# is the audit's own rule: a finding is OPEN until main reproduces it. States:
#   OPEN           not yet reproduced on main
#   READER         main's reader (a cheaper model, by the owner's rule) reproduced it; main has not repeated the check
#   REPRODUCED     main reproduced it with its own check; the fix is owed
#   PARTLY FIXED   main changed part of what the acceptance row asks; the note says which part is left
#   FIXED          main meets the whole acceptance row as main reads it; the advisor seat's re-audit is owed
ADVISOR = ("e7703f2ec", "relays/advisor_2026-11-10_audit")
FINDING_STATES = ("OPEN", "READER", "REPRODUCED", "PARTLY FIXED", "FIXED")
FINDINGS = {}


def F(ids, wp, entries):
    for (fid, short, state, note) in entries:
        FINDINGS[fid] = dict(wp=wp, short=short, state=state, note=note)


F("G", "WP-0.7", [
    ("G1", "the append-only gate cannot see a committed change (graded critical)", "FIXED",
     "B1863: the gate reads history. Every first-parent commit after the rule's first commit that touches the log must keep its parent's log as a prefix, or be a roll-up with its archive; it fails closed where history cannot be read; a violation stays visible until waived by name. The audit's two planted violations are in the suite, each committed in a small repository and run on the clean tree, and the registered control is the gate function failing on one"),
    ("G2", "an edit after the seal is undetected for most sealed files (graded critical)", "FIXED",
     "B1864: a new gate reads history and refuses any commit after its first that edits, deletes or moves a sealed-style file, under every seal name the ledger's generator knows; it fails closed where history cannot be read; a violation stays visible until waived by commit and path. The ledger gate recomputes every generated row and refuses a listed file that is gone. The audit's four planted violations are in the suite, the first three committed in small repositories and run on the clean tree"),
    ("G3", "the seal ledger's 'recorded elsewhere' column certifies itself", "FIXED",
     "B1864: the ledger's generator reads tracked files only and not the ledger, so a hash is recorded elsewhere only if another tracked file holds it. The corrected ledger: of 432 sealed files, 156 have a hash that no other tracked file records, the audit's own count; two runs agree, and the planted test is in the suite. Main's first correction removed the ledger alone and was incomplete: the generator was also reading every untracked file under the working directory"),
    ("G4", "the seal-order gate sees one file name only", "FIXED",
     "B1864: the seal-order gate reads every seal name the generator knows. Thirty arcs whose rule and record were first committed together under names it had not read (the audit's example among them) are entered by name on the list, and the planted test is in the suite. The new seal gate and the ledger gate read every name too. The provenance gate still reads the narrower list"),
    ("G5", "'gates fail closed' is false for many gates", "PARTLY FIXED",
     "B1863: the append-only gate fails closed without a repository, and the runner prints a gate that checked nothing as SKIP with its own words (the review tool's fresh clone counts it against the clone). Left: the four gates that still skip there, and the four deletions that pass (the identification baseline, the retracted-phrase registry, every arc test, an emptied law map and theorem ledger). Main's reader's run corrected one detail: two gates the audit lists do fail closed"),
    ("G6", "four gates read today's date", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit with the date set 30, 60 and 365 days after the commit: four gates turn red on identical content"),
    ("G7", "the gate-controls gate checks a name only", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: every registered control pointed at one skipped trivial test, and the gate passed"),
    ("G8", "the retraction sweep reads part of its registry", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: two phrases from registry rows added after 2026-10-07 pasted into the front page passed; a phrase from an older row was caught"),
    ("G9", "the attribution gate never reads a commit message", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a commit message carrying a co-author trailer passed; so did vendor tokens added with their baseline raised in the same commit"),
    ("G10", "practices labelled gated whose gate is weaker than the practice", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit, for two of its eleven practices: a proven row citing no lock passed, and a banned phrase passed when capitalised or placed in a file type the gate does not read"),
    ("G11", "the currency check prints 'current' beside declared debts", "OPEN", ""),
    ("G12", "the gates at push are an honour system", "OPEN", ""),
    ("G13", "results depend on clone depth and on fetched refs", "PARTLY FIXED",
     "Review 77: the review tool's clone for the gates now carries the published branches, as its clone for the suite did. Left: main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit at depth 50, where the lead gate reports no stale arc against a baseline of 76 and another gate fails spuriously; no gate says the clone is shallow. The seat's own script reports this case caught on today's main because the full and the shallow clone now agree; that is its criterion, not a fix (B1865)"),
    ("G14", "baselines are counts, markers never expire, ids match as substrings", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a verdict file cut to invalid JSON is skipped by the gate that reads it; it is noticed only where the arc has dependants, and by a view generator"),
])
F("L", "WP-0.3", [
    ("L1", "about a quarter of PROVED arcs are guarded only by locks that read text", "OPEN", ""),
    ("L2", "'locks assert mathematics' has no gate", "OPEN", ""),
    ("L3", "the theorem chain's locks are mostly weaker than their links", "OPEN", ""),
    ("L4", "B1854's lock fails in every clone", "PARTLY FIXED",
     "Review 77, found independently by main's fresh-clone suite: the three logs sealed under tracked names. The gate was then widened twice the same day: first to read every lock's own-directory paths, which main's own planted run showed could fire only on the author's tree; then to refuse any such path that git would ignore, whether or not the file exists, which fires in a clean checkout. Left: the lock reads the drivers' committed transcripts and does not re-run them (their runs take hours)"),
    ("L5", "B1847's lock has assertions that cannot fail", "FIXED",
     "B1862: the rise toward the tube is true on the data and is now checked by a helper with a planted failing case; the distance from the record's readings is taken from the cluster's own least value"),
    ("L6", "locks that compare printed floating-point digits as text", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a lock comparing a printed float with a committed transcript is refused by no gate"),
    ("L7", "tests that are arithmetic on literals", "READER",
     "main's reader's scan of every test file: fifteen test functions whose every assert is on literals; main read one of them. main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a test whose only assert is on two literals is counted and not refused"),
    ("L8", "three depended-on arcs hold no computation of their headline", "OPEN", ""),
    ("L9", "core tests that compare a value with itself; silent skips", "REPRODUCED",
     "main's own reading: two tests compare a function with the expression that defines it; the count of silent skips is not checked"),
    ("L10", "the suite rewrites tracked evidence files", "READER",
     "by reading, main's reader: two locks run scripts that write tracked files. main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a test that appends to a tracked file leaves the tree changed and nothing notices; the full suite was not run"),
])
F("E", "WP-0.8", [
    ("E1", "B997's uniqueness clause has a counterexample", "PARTLY FIXED",
     "B1859, the same day and before the audit was read: the door set is {1, 4}, proved for every m and carried to the verdict, the foundation document, the claim page, the law map and the theorem registry, with the old wording kept and a lock that computes it. Left: the acceptance row asks that the register row be split into one row per correction, and it is not"),
    ("E2", "a chain lock asserts the wrong congruence level", "READER",
     "main's reader ran the lock's own function: index 6 at level 4 and 12 at level 8 under the lock's quotient by every central unit; under the standard quotient by ±1 the index is already 12 at level 4, as the ledger's own note says"),
    ("E3", "B1856: a parity gap in 'invisible to every state'", "FIXED",
     "B1862: the sentence reads E ≡ +I, a parity superselection rule is named as a third condition, and the split is stated and computed exactly (338 with +I, 305 with −I of 643); the run of six is unaffected"),
    ("E4", "B952's lemma is false as stated", "PARTLY FIXED",
     "B1862: the lemma says 'commuting', with the counterexample in sl(2) computed exactly by a lock; the rank of the cascade's own centralizer is not yet computed by a lock"),
    ("E5", "B892's scan never refines", "REPRODUCED",
     "main's own reading: the refinement runs only when the grid finds nothing, and the grid lands on the wall, so it never runs"),
    ("E6", "B862's 'kernel computed exactly' computes nothing", "FIXED",
     "B1862: the kernel is computed from the map in exact arithmetic (the two centres and a complete grid of sixths; a finer grid finds nothing more; cyclic), and the lock runs the same enumeration for another map and gets a different kernel"),
    ("E7", "B1028's zero is a sum of typed zeros", "REPRODUCED",
     "main's own count: eleven typed zeros are summed and asserted to be zero; the arc's addendum says one row is unpriced and its verdict line was not changed"),
    ("E8", "B854's negative is scoped to one embedding", "PARTLY FIXED",
     "B1862: the consequence sentence and the verdict line are scoped to the principal embedding; the table of the other classes that the acceptance row names has not been located"),
    ("E9", "B1854's error is not an estimate", "PARTLY FIXED",
     "Review 77, found independently by main's reader: the error is about 0.02 and the value does not confirm the seat's; not yet relabelled a numerical estimate, and no control at that level"),
    ("E10", "a command in the front page ignores its argument", "FIXED",
     "B1862: the command prints the named arc's status, verdict and claim line; a lock runs it for two arcs and an unknown one"),
    ("E11", "three small misstatements", "PARTLY FIXED",
     "B1862: the sine sentence corrected (complex radicals, not real ones), the minimal polynomial recomputed by a lock; the finding's other two parts are not checked"),
    ("E12", "five small slips of scope", "OPEN", ""),
    ("E13", "B567's eigenvalue count is impossible, and a lock pins it", "FIXED",
     "B1862: twenty distinct eigenvalues, counted on the lattice of twentieth roots, with the full multiplicity list; the findings carry the old count in a dated bracket and the lock asserts the bound by the order"),
])
F("M", "WP-0.9", [
    ("M1", "PROVED means at least five things", "READER",
     "its two counts recomputed on today's main by main's reader (1,071 arcs graded PROVED, 195 of them with no script in the folder); its examples are not checked"),
    ("M2", "the forcing theorem forces a matrix, not the manifold", "OPEN", ""),
    ("M3", "three of four further filters do not separate the sister manifold", "REPRODUCED",
     "main's own SnapPy run: the sister manifold has the same volume, is amphicheiral and has the same tetrahedron shapes; only the homology separates them. The code, the constant and the test still say five independent filters"),
    ("M4", "a physics statement under 'no physics statement appears below'", "OPEN", ""),
    ("M5", "'the flavour three is derived' against an unearned identification", "OPEN", ""),
    ("M6", "the global form called derived and not standard in a paper draft", "OPEN", ""),
    ("M7", "B1855's titles say proved for a step main did not re-run", "OPEN", ""),
    ("M8", "B1850's verbatim quotes mostly quote the row's own title", "OPEN", ""),
    ("M9", "an internal review called external in the paper folders", "OPEN", ""),
    ("M10", "the falsifier register cannot contradict the programme", "OPEN", ""),
    ("M11", "a generated page asserts false universals", "OPEN", ""),
])
F("P", "WP-0.1", [
    ("P1", "the front door describes a plan that already ran and failed", "OPEN", ""),
    ("P2", "one register row bundles many unapplied corrections", "PARTLY FIXED", "its first item is done (B1859); the row is not split"),
    ("P3", "an endpoint correction did not reach five arcs", "OPEN", ""),
    ("P4", "a voided prediction and a stale significance on living pages", "OPEN", ""),
    ("P5", "a withdrawn tube value still cited; the read-out rule's page stale", "PARTLY FIXED",
     "the read-out rule's page carries the dated notes of S306n and Review 77; the earlier arc's section is not yet checked"),
    ("P6", "the index lists stale documents as living", "OPEN", ""),
    ("P7", "stale counts and duplicate arc ids", "OPEN", ""),
])
F("V", "WP-0.2", [
    ("V1", "every specificity null has an unpriced window", "OPEN", ""),
    ("V2", "the headline fits omit their error floor", "OPEN", ""),
    ("V3", "evidence lives in an ignored directory", "OPEN", ""),
    ("V4", "the candidate has a forking path", "REPRODUCED",
     "in part, by main's own reading of the declaration's history with the new seal gate: three later commits edited the declaration of ends after it was first committed, and the end that the candidate's row uses was entered 75 minutes after the first declaration, in a dated note that says the look had not yet run. Not yet checked: the audit's two figures for the screen under the plan's committed arms, and its remark on the fitted factor"),
    ("V5", "three looks missing from the look ledger; two conventions in one pipeline", "OPEN", ""),
])
F("X", "WP-0.10", [
    ("X1", "twelve places in the governing documents cap the goal", "OPEN", "the owner confirmed the ruling on the goal to main on 2026-11-10; the amendment of the twelve places is the next step of its package and is not made yet"),
    ("X2", "three documents each claim supremacy", "OPEN", "the same landing names one governing document; not made yet"),
    ("X3", "the printed identification price undercounts, and its script fails", "OPEN", ""),
    ("X4", "scope tags are absent from most verdict files", "OPEN", "covered by the declared domain (WP-0.11)"),
])
F("R", "WP-0.5", [
    ("R1", "the full suite fails on a clean full clone", "PARTLY FIXED",
     "Review 77's own fresh-clone suite: 7 failed, of which B1854's lock and the package manifest are fixed; the two attachment locks are undiagnosed; the float-as-text locks pass on main's machine and are not yet made exact"),
    ("R2", "the pinned environment is prose, not a lock file", "OPEN", ""),
])
F("W", "WP-0.11", [
    ("W1", "the member-scope gate is a count", "READER",
     "main's reader planted the audit's violation in a scratch clone of today's main and ran the gate on the clean tree at that commit: a new negative line worded about the object on a one-thread arc is caught alone, and passes when one old line is reworded in the same commit, since the gate is a count against a baseline"),
    ("W2", "the quantifier of most claims is not machine-readable", "OPEN", ""),
    ("W3", "'the object' still names one thread in the terminology", "OPEN", ""),
    ("W4", "no truncation is recorded", "OPEN", ""),
    ("W5", "six findings of this audit are of the same class", "OPEN", ""),
])
F("W", "WP-1.6", [
    ("W6", "plenitude is not a foundation item, and nothing supplies the weight", "REPRODUCED",
     "the closure map's eleventh missing dependency (B1858, the same day, before the audit was read): the law fixes what exists and not how much of each"),
    ("W7", "a weighting rule chosen by hand is the thread mistake one level up", "REPRODUCED",
     "the map's node for the clock is graded CHOSEN; a thread picked by hand and a flat average are the two ways of supplying the weight without deriving it"),
])

# B1870 (2026-11-10): THE AUDIT'S BACKLOG, REPRODUCED ON MAIN.  Eight read-only checkers, one per class of finding, reported for each
# of the 34 findings nobody had reproduced the exact commands that decide it; main re-ran every command itself before a state
# changed here.  The entries above are kept as they were written; U() records the new state and keeps the old one beside it.
def U(fid, state, note):
    """a finding's new state; 'was' keeps the state and note it was first given, 'trail' every state it has had since, in order"""
    assert fid in FINDINGS and state in FINDING_STATES and note
    f = FINDINGS[fid]
    if "was" not in f:
        f["was"] = [f["state"], f["note"]]
    else:
        f.setdefault("trail", []).append([f["state"], f["note"]])
    f["state"], f["note"] = state, note


_R = "main re-ran the deciding commands itself (B1870): "
U("G11", "REPRODUCED", _R + "the currency check prints 'ok (18 living documents current)' while 9 documents are declared debts and 8 of those are counted as current; CLAIMS.md lags 580 arcs under a tolerance of 40. The audit's 569 and 8 are 580 and 9 today")
U("G12", "REPRODUCED", _R + "README.md:71 says the gates run on every push; the hook is local and untracked, and the one CI workflow runs core tests and no gate")
U("R2", "REPRODUCED", _R + "the pinned versions are a prose table in REPRODUCIBILITY.md; requirements.txt and pyproject.toml carry lower bounds only; no lock file is tracked, and CI installs unpinned")
U("E12", "PARTLY FIXED", _R + "of its five slips, B1853's margins are corrected (B1855's dated note, Review 77). Left: B1857 is marked post hoc and still says 'exactly the two cheaper'; B1852's count of four reversing involutions carries its window and no note that the count is the window's; B884's control is printed and unused; B915's pre-registration still says no other measured number enters, against its own addendum")
U("L1", "REPRODUCED", _R + "no lock declares whether it recomputes, re-runs or reads a transcript, and no gate asks. A rough static count finds about 330 of 1518 lock files with no computing import; the audit's census tools are not on main and its 386 was not re-derived")
U("L2", "REPRODUCED", _R + "the rule that locks assert mathematics has no row in PRACTICES.md and no gate; the vacuity gate fails only the no-assert and tautology classes and reports the both-literal class without failing it")
U("L3", "REPRODUCED", _R + "in part. The chain-locks gate checks only that each link cites a test file that exists. Of the audit's two examples, C45's lock hard-codes its inputs and C7's last assertion is literal-only; but C7's lock also recomputes its three discriminants, and C45 is a no-go link, not a theorem")
U("L8", "REPRODUCED", _R + "B892's tower scripts were never tracked (its wall scan is); B952 has a results file that its lock reads back and no script; B866's lock compares two literal cubics and its interpolation script is not tracked")
U("M2", "REPRODUCED", _R + "in part. The two pages do not list the four further inputs and still call the collapse of 144 to 1 the content of the forcing; but both carry the banner that GENESIS is canonical, and the uniqueness page says it forces the matrix, conditionally. 'The object forced up to orientation' stands on THE_CLAIM.md:15")
U("M4", "REPRODUCED", _R + "THEOREM_LEDGER.md says no physics statement appears below, and its link C51, labelled a theorem, says a cover 'carries the Standard-Model gauge algebra and three complete generations'; unchanged since the audit")
U("M5", "REPRODUCED", _R + "'the flavour three is derived' stands in GENESIS.md (line 456 today) and THE_WEAVE.md:113 with no pointer to the identification it rests on (I-31, unearned)")
U("M6", "REPRODUCED", _R + "in part. The paper's main.tex already says the derivation is standard and only the selection is not; its SPEC.md:115 still lists the global form 'derived rather than assumed' under what is not standard")
U("M7", "REPRODUCED", _R + "B1855's title says the run of 6 is 'proved least' though main re-ran neither of the seat's two lemmas (P-741, queued), and its claim line says 'every lcm(S) >= 12' without the range of S that its scope field carries")
U("M8", "REPRODUCED", _R + "B1850 says every quote was found verbatim, 313 of 313; its checker tests only that a quote is a substring of the file named. The audit's 76 of 86 was not re-derived")
U("M9", "REPRODUCED", _R + "papers/P3_THE_PAPER/EXTERNAL_REVIEW_2026-09-09.md is titled an external review, and 'outside referee' stands in two paper READMEs, against PROVENANCE § 0; the pretense gate scans docs and top-level pages only and lists neither phrase")
U("M10", "REPRODUCED", _R + "in part. Two entries say a failure kills the reading and not the weave, and the eight first rows do not say what a failure would contradict; but 'most entries cannot fire' overstates: by the register's own grades it is 3 or 4 of 11")
U("M11", "REPRODUCED", _R + "the reviewer page's sentence 'Every PROVED arc names its test locks' is a fixed string in the generator; on main 421 of 1079 PROVED arcs name no test file in their findings")
U("P1", "REPRODUCED", _R + "THE_PROGRAMME_SO_FAR.md gives the six at their best figure and the final attack's two steps in the future tense, and names none of B1823, B1825, B1838; the plan carries one dated note, for B1823. The audit's claim about README is stale: README gives no outcome")
U("P3", "REPRODUCED", _R + "B892 carries the correction (its 14-dimensional algebra is not the Standard Model's); B861, B862, B863 and B1028 carry no pointer to it, and B994's table still says its chains end at the Standard Model")
U("P4", "REPRODUCED", _R + "CLAIMS.md:147 still states the comparison without the adjudication that voided it as a held-out confirmation; B723 is still PROVED with no supersession; a withdrawn figure of sigmas stands on at least eight current pages")
U("P6", "REPRODUCED", _R + "INDEX.md lists CLAIMS.md as living while CLAIMS.md says it was last updated on 2026-07-04; CAMPAIGN_STATUS.md has 606 paragraphs that begin LATEST; one living entry is a path that does not exist")
U("P7", "REPRODUCED", _R + "the forcedness check prints 53 of 57 while '39 of 43' stands as current on at least seven pages; the law map's banner says 113 rows against 329; two arc ids are each shared by more than one folder (1570 verdict files, 1567 ids)")
U("V1", "OPEN", "not checked, and why (B1870): the audit's figure has no tracked source, and deciding it needs a computation on the nulls that belongs behind a sealed card. Main's checker found that the later nulls take the best over 223 apexes and 266 lines and not over a plain grid, so the audit does not say which null it measured")
U("V2", "REPRODUCED", _R + "in part. The allowance of ten per cent is in the compare scripts, is defined in TERMINOLOGY.md:763 and is priced in the framing ledger; the headline figures in THE_FINAL_ATTACK and THE_PROGRAMME_SO_FAR are quoted without it. The audit's two large figures have no tracked source and were not recomputed")
U("V3", "REPRODUCED", _R + "audit/ is ignored and holds no tracked file; the register cites it on 83 lines and 68 findings files cite it; one calibration figure quoted on tracked pages rests on scripts that exist only there, and no tracked line says so")
U("V5", "REPRODUCED", _R + "in part. The look ledger has no row for B1658, B1659 or B1724. Only B1658 clearly reads seen data, by its own findings; B1659 says it uses none; B1724 re-reads earlier calibrations. Two error bars for one quantity stand on record")
U("W2", "REPRODUCED", _R + "250 of 1570 verdict files carry weave_or_thread and 287 a scope; no gate requires either")
U("W3", "REPRODUCED", _R + "TERMINOLOGY.md:11 defines 'the object' as the figure-eight complement, while GENESIS's fork on the family as object is ruled to the word states; the two do not agree on the default noun")
U("W4", "REPRODUCED", _R + "no verdict file has a field for a truncation, a range or a domain (27 distinct keys, none of them); the truncation ledger exists only as a planned item")
U("W5", "PARTLY FIXED", _R + "of its six instances, four now carry dated scope notes (B854, B997, B1855, B1853; by B1859, B1862 and Review 77). Left: B1291's verdict file has no scope and no pointer to the arc that re-scoped it; the sixth, on the nulls, was not checked")
U("X1", "REPRODUCED", _R + "GOVERNANCE.md:23 says the goal is not a theory of everything, and neither it nor CLAIMS.md has changed since the audit. The owner has confirmed the goal to main (P-758); amending the places is the first step of P-767. One of the audit's twelve places (THE_CLAIM.md, lines 58 to 71) is the anchor doctrine and is doubtful as a cap")
U("X2", "REPRODUCED", _R + "three files each say they win a disagreement: GOVERNANCE.md:6-9, GENESIS.md:29, CLAIMS.md:3")
U("X3", "REPRODUCED", _R + "in part. The certificate script does not fail on main: it exits 0, its four tests pass, and it is unchanged since the audited commit. What holds is that the '4' in '4 + 9 = 13' is a typed constant")
U("X4", "REPRODUCED", _R + "1283 of 1570 verdict files carry no scope, and none a domain")
# seven that only a reader had reproduced: main's own run of the seat's planted violations (B1865, in a scratch clone of main at 30dd1fea7)
_P = "main ran the seat's own planted violation in a scratch clone of main at 30dd1fea7 (B1865): not caught. "
for _fid in ("G6", "G7", "G8", "G9", "G10", "G14", "L7"):
    U(_fid, "REPRODUCED", _P + "Earlier, by main's reader: " + FINDINGS[_fid]["note"])

# B1873 (2026-11-10): THE PROGRAMME READ BY A NON-AUTHOR (the advisor seat's READ_OF_B1861_AS_A_NON_AUTHOR.md).  Its cause: the
# seal's rule reads the map, and the audit's findings were not joined to it.  Three repairs here; the rest is registered (P-773).
# (1) Two findings were filed by the audit's section letter where their fix is another package's work (B1870 § 5 says so):
FINDINGS["X3"]["wp"] = "WP-0.12"      # closes when the count is computed and not typed
FINDINGS["X4"]["wp"] = "WP-0.11"      # closes with the declared domain
# (2) What each finding bears on: arcs, nodes of the map, tracked paths, or REPOSITORY for a property of the repository as a whole
# that a seal depends on (gates, locks, the suite, the look ledger, the nulls, the verdict files' fields).  The builder refuses a
# finding that names nothing, and holds every package with a REPOSITORY finding upstream of the sealed card.
REPO = "REPOSITORY"
BEARS_ON = {
    "E1": ["B997"], "E2": ["docs/THEOREM_LEDGER.md", "B734", "tests/test_b734_m004_congruence.py"], "E3": ["B1856", "B1853", "B1855", "B1857", "docs/THE_TAU_READOUT_RULE.md"],
    "E4": ["B952"], "E5": ["B892"], "E6": ["B862"], "E7": ["B1028"], "E8": ["B854"], "E9": ["B1854"], "E10": ["README.md"],
    "E11": ["docs/LITERATURE_CONTEXT_2026-07-15.md", "CLAIMS.md"], "E12": ["B884", "B915", "B1852", "B1853", "B1857"], "E13": ["B567"],
    "G1": [REPO], "G2": [REPO], "G3": [REPO], "G4": [REPO], "G5": [REPO], "G6": [REPO], "G7": [REPO], "G8": [REPO], "G9": [REPO],
    "G10": [REPO], "G11": [REPO], "G12": [REPO], "G13": [REPO], "G14": [REPO],
    "L1": [REPO], "L2": [REPO], "L3": ["docs/THEOREM_LEDGER.md", "B730", "B1096"], "L4": ["B1854"], "L5": ["B1847"], "L6": [REPO, "B1849", "B1850"],
    "L7": [REPO], "L8": ["B866", "B892", "B952"], "L9": [REPO], "L10": [REPO, "B1464", "B1690"],
    "M1": [REPO], "M2": ["G:ROOT", "docs/UNIQUENESS_THEOREM.md", "docs/THE_CLAIM.md"], "M3": ["G:ROOT"], "M4": ["docs/THEOREM_LEDGER.md"],
    "M5": ["TAG:LAMBDA", "GENESIS.md", "docs/THE_WEAVE.md"], "M6": ["B1221", "papers/P3_THE_PAPER/SPEC.md"], "M7": ["B1855"], "M8": ["B1850"],
    "M9": ["papers/P3_THE_PAPER/EXTERNAL_REVIEW_2026-09-09.md"], "M10": ["docs/FALSIFIER_REGISTER.md"], "M11": ["scripts/views/generate.py"],
    "P1": ["V:SIX", "B1823", "B1825", "B1838", "docs/THE_PROGRAMME_SO_FAR.md", "docs/THE_FINAL_ATTACK_2026-10-29.md"],
    "P2": ["docs/POINT_REGISTER.md"], "P3": ["B861", "B862", "B863", "B994", "B1028"], "P4": ["B653", "B723", "CLAIMS.md"],
    "P5": ["docs/THE_TAU_READOUT_RULE.md"], "P6": ["docs/INDEX.md"], "P7": [REPO],
    "R1": [REPO], "R2": [REPO],
    "V1": [REPO, "V:SIX", "B1726", "B1753"], "V2": [REPO, "V:SIX", "B1720", "B1735"], "V3": [REPO, "B1757"], "V4": [REPO, "V:SIX", "B1840", "B1841"],
    "V5": [REPO, "docs/LOOK_LEDGER.md", "B1658", "B1724"],
    "W1": [REPO], "W2": [REPO], "W3": ["TERMINOLOGY.md"], "W4": [REPO], "W5": ["B1291"], "W6": ["W:LAW"], "W7": ["W:CLOCK"],
    "X1": ["GOVERNANCE.md", "CLAIMS.md"], "X2": ["GOVERNANCE.md", "GENESIS.md", "CLAIMS.md"],
    "X3": [REPO, "MC:PRICE", "B1266", "outside_bench/certificates/the_price_is_twelve.py"], "X4": [REPO],
}
# (3) "Fixed" is main's word.  The re-audit's verdict is the advisor seat's, kept apart, with the commit of main it read.
ACCEPTED_AT = ("ab97082c0", "REAUDIT_2_2026-11-10.md")
ACCEPTED = {
    "G1": "accepted, with three residuals (the log's archives; a waiver hides its violation; history before the rule)",
    "G2": "accepted for what it covers; the scripts a seal hashed are unguarded",
    "G3": "accepted",
    "G4": "accepted; one case open (a rule committed after its record)",
    "E13": "accepted", "E6": "accepted", "E10": "accepted", "L5": "accepted",
    "E3": "accepted in the arc; not carried to the three arcs and the page that state the old form",
    "E4": "partly, as main says", "E8": "partly, as main says", "E11": "partly, as main says",
}
U("E3", "PARTLY FIXED", "B1856 says that invisible to every state is E = +1, gives the split 338 and 305 and names parity superselection (B1862). Not carried to B1853, B1855, B1857 or the read-out rule's page, which still state the old form with no pointer: main's own propagation fault, found by the seat's second re-audit (P-772)")
U("X3", "REPRODUCED", "main re-ran it (B1873): the script the foundation cites for the live price, outside_bench/certificates/the_price_is_twelve.py, exits 1 on main ('24 ROWS OUTSTANDING' is not stated in the verdict page) and nothing runs it; the other script for the same price, B1266's, passes on a typed 4. Both halves of the finding stand. B1870 had tested the second script, the finding having named none")
U("L10", "REPRODUCED", "main re-ran it in a clean checkout (B1873): two test files pass and leave a tracked evidence file modified (B1464's seal census); the seat saw a second file change on its machine")

# B1874 (2026-11-10): WHAT MAIN DID AFTER THE RE-AUDIT READ IT.  The seat's verdicts above are of main at ACCEPTED_AT and are not
# changed here: a verdict on a commit says nothing of a later one.  Each entry names the arc and what it changed; the builder
# prints the finding as changed since the re-audit and not re-read, and refuses an entry for a finding the re-audit gave no
# verdict on, or naming an arc that is not on main.
SINCE_REAUDIT = {
    "G2": ("B1874", "the re-audit's largest residual: a gate reads every list of hashed files (189 lists, 1497 entries), a listed file cannot change, and a list cannot be edited, deleted or moved; the 63 entries that did not verify are frozen by key; eleven tests on committed planted violations, the seat's own case among them. Left of this finding: a rule under a name outside the seal patterns, and a sealed-style file one folder deeper"),
    "G1": ("B1874", "the second of its three residuals: both gates put every waiver, with its reason, in their sentence and count waived commits apart from appends; and the runner, which printed a bare ok for every pass, now prints those sentences whole (a waived violation committed in a small repository is named in the printed line). Left: the log's archives, and the history before the rule"),
}

# REVIEW 78 (2026-11-11, B1877): its reader read B1862 in full and found that three of its corrections had not reached every place
# the corrected statement stood -- the fault the seat's second re-audit had named for E3, found here for E4 and E8 as well.  Main
# checked each at its source, carried all of them, and added a lock that fails wherever an old form stands without its correction
# beside it.  None is marked fixed by this: E3's re-audit verdict says "not carried", and the seat has not re-read it.
U("E3", "PARTLY FIXED", "carried on 2026-11-11 (Review 78, B1877) to the four places the second re-audit named -- B1853, B1855, B1857 and the read-out rule's page -- and to two more that the review found: B1856's own verdict line still opened with the old form, and the register's row P-738 stated it. A lock now fails if the old form stands anywhere in the record without the correction beside it. Left: the seat's re-read")
U("E4", "PARTLY FIXED", "B1862 corrected the lemma in B952's findings only; Review 78's reader found it uncorrected in B952's verdict line, its results file and the requirements ledger, and all three now carry 'commuting' at the sentence (B1877). Left, as before: the rank of the cascade's own centralizer is not yet computed by a lock")
U("E8", "PARTLY FIXED", "B1862 scoped the consequence sentence and the verdict line; Review 78's reader found the verdict block at the top of B854's findings still unscoped, and it is scoped now (B1877). Left, as before: the table of the other classes that the acceptance row names has not been located")
# B1878 (2026-11-11): THE GOAL AS RULED, IN THE GOVERNING DOCUMENTS (the first landing of P-767: rulings R1 and R3).  "Fixed" is
# main's word; the advisor seat has read none of this, and the builder lists each as fixed and not yet re-audited.
U("X1", "FIXED", "B1878: the places that cap the goal are amended together, each keeping its original text beside a dated note -- GOVERNANCE.md's goal sentence, its label and its firewall paragraph; the claims ledger's open targets; the anchor doctrine; and the gate, which no longer bans a statement of aim. The ceiling is kept and gated: a sentence of arrival on a living page fails `arrival-phrases`, the audit's own planted sentence on the front page among them. The audit's list also names two results of the foundation (FK11, GAP6); a ruling does not amend a result, and the amended text says they stand")
U("X2", "PARTLY FIXED", "B1878: GOVERNANCE.md is named the one governing document, with GENESIS.md holding on the status of every item of the foundation by its delegation and CLAIMS.md a ledger under both; GOVERNANCE.md's permitted label is brought down to GENESIS.md's statuses. Left: GENESIS.md's own line ('this file holds'), which only an arc at its next version may note")
U("G9", "FIXED", "B1878: the attribution gate reads every commit message on the first-parent line after da25c4f49, the last that carried a vendor's name or a co-author trailer; 695 commits pass; a trailer, a vendor's name and a foreign author, each committed in a small repository, are refused, and the gate fails closed where that history is not in the clone (tests/test_attribution_history.py)")
SINCE_REAUDIT["E3"] = ("B1877", "the correction carried to B1853, B1855, B1857 and the read-out rule's page, as the re-audit asked, and to B1856's verdict line and the register's row P-738; a lock that fails wherever the old form stands unmarked")
SINCE_REAUDIT["E4"] = ("B1877", "'commuting' carried to B952's verdict line, its results file and the requirements ledger, where the reader of Review 78 found the lemma uncorrected")
SINCE_REAUDIT["E8"] = ("B1877", "the scope carried to the verdict block at the top of B854's findings")

# B1880 (2026-11-11): THE SEAT'S THIRD AND FOURTH RE-AUDITS (of main at b28dceea8 and at 015be0cc7), harvested and answered.
# (1) Three entries of "what each finding bears on" are widened as the third re-audit asked (E2, L6, V4, above): main checked that
#     each named arc and file exists and is what the finding is about.
# (2) Its case j4: a finding the re-audit did not accept was marked FIXED here, with the re-audit's verdict retyped as "accepted"
#     in this file, and the builder built.  The verdict was main's transcription and nothing checked it against the seat's file.
#     From here each verdict names the re-audit that gave it and carries that file's own row, verbatim; the builder reads the row
#     in the seat's file at the seat's commit, refuses a verdict with no row, a row that is not there, and a verdict whose leading
#     word is not in its row; and prints NOT CHECKED where the clone does not hold the seat's commit.
REAUDITS = {     # the re-audit's file -> (the seat's commit that holds it, main's commit that it read)
    "REAUDIT_2_2026-11-10.md": ("b5034197b", "ab97082c0"),
    "REAUDIT_3_2026-11-11.md": ("6ab743907", "b28dceea8"),
    "REAUDIT_4_2026-11-11.md": ("58ae45c70", "015be0cc7"),
}
VERDICT_ROWS = {     # finding -> rows of the seat's files; the FIRST is the verdict in force and names the finding; the rest are further rows quoted
    "G1": [("REAUDIT_2_2026-11-10.md", "| **G1** the append-only gate | **accepted**, with three residuals |"),
           ("REAUDIT_3_2026-11-11.md", "| **waivers print themselves** (B1874; residuals a2 and s5) | **accepted** |")],
    "G2": [("REAUDIT_3_2026-11-11.md", "| **the scripts a seal hashed** (B1874; the largest residual of G2) | **accepted, with three residuals** |"),
           ("REAUDIT_2_2026-11-10.md", "| **G2** sealed files | **accepted for what it covers**; the cover is too narrow |")],
    "G3": [("REAUDIT_2_2026-11-10.md", "| **G3** the ledger's self-certification | **accepted** |")],
    "G4": [("REAUDIT_2_2026-11-10.md", "| **G4** seal filenames | **accepted**; one case of the finding still open |")],
    "E13": [("REAUDIT_2_2026-11-10.md", "| **E13** B567's 21 eigenvalues | **accepted** |")],
    "E6": [("REAUDIT_2_2026-11-10.md", "| **E6** B862's kernel | **accepted** |")],
    "E10": [("REAUDIT_2_2026-11-10.md", "| **E10** the README's arc lookup | **accepted** |")],
    "L5": [("REAUDIT_2_2026-11-10.md", "| **L5** B1847's lock | **accepted** |")],
    "E3": [("REAUDIT_4_2026-11-11.md", "| **E3** the premise's two signs | PARTLY FIXED | **accepted** |"),
           ("REAUDIT_2_2026-11-10.md", "| **E3** B1856's premise | **accepted in the arc; not propagated** |")],
    "E4": [("REAUDIT_2_2026-11-10.md", "| **E4** B952's lemma | **partly**, as you say |")],
    "E8": [("REAUDIT_2_2026-11-10.md", "| **E8** B854's scope | **partly**, as you say |")],
    "E11": [("REAUDIT_2_2026-11-10.md", "| **E11** three statements | **partly**, as you say |")],
    "G9": [("REAUDIT_4_2026-11-11.md", "| **G9** the attribution rule is not gated as worded | FIXED | **accepted, with one residual** |")],
    "X1": [("REAUDIT_4_2026-11-11.md", "| **X1** twelve places cap the goal | FIXED | **accepted** |")],
    "X2": [("REAUDIT_4_2026-11-11.md", "| **X2** three documents each claim supremacy | PARTLY FIXED | **agreed: partly** |")],
}
# The verdicts as they stand after the fourth re-audit.  A verdict is of main at the commit its re-audit read, and says nothing of
# a later one: what main changed after it is in SINCE_REAUDIT, listed as not re-read by the seat.
ACCEPTED_AT = ("015be0cc7", "REAUDIT_4_2026-11-11.md")       # the latest re-audit; each verdict's own re-audit is in VERDICT_ROWS
ACCEPTED.update({
    "G1": "accepted, with three residuals (re-audit 2); the second, a waiver that hides its violation, accepted as mended (re-audit 3). Left: the log's archives, and history before the rule",
    "G2": "accepted, with three residuals (re-audit 3, of the gate for the scripts a seal hashed): a copy standing in for the real file, a frozen entry changing again, and lists under other names",
    "E3": "accepted (re-audit 4): carried to the four places the second re-audit named, each with a dated note",
    "G9": "accepted, with one residual (re-audit 4): a commit that arrives by a merge is not read",
    "X1": "accepted (re-audit 4); the gate that guards the ceiling is a tripwire, and two of the seat's planted sentences passed it for a defect and not a limit",
    "X2": "agreed: partly (re-audit 4); GENESIS.md's own line still says that it holds",
})
U("E3", "FIXED", "carried on 2026-11-11 (Review 78, B1877) to the four places the second re-audit named -- B1853, B1855, B1857 and the read-out rule's page -- and to B1856's own verdict line and the register's row P-738; a lock fails if the old form stands anywhere in the record without the correction beside it. The seat's fourth re-audit read it at 015be0cc7 and accepted it; its own test of the lock: the old form in the lock's words on a new page fails, in other words it passes -- a tripwire")
U("G14", "PARTLY FIXED", "B1880: of the finding's four parts, two are met in part. A verdict file that cannot be read as JSON now fails the gate arc-data and is named (the seat's planted case PV14, which passed with the count one lower; a committed test plants it on an arc nothing depends on). And the old lines of the arrival gate are frozen by key and not by count. Left: the other baselines that are counts and not named sets; the ESCALATED markers that never expire; an id matched as a substring of a longer id")
for _fid in ("E3",):
    SINCE_REAUDIT.pop(_fid, None)          # the fourth re-audit read what main had changed there
SINCE_REAUDIT["G2"] = ("B1880", "the third re-audit's three residuals, each reproduced on main and then closed in the gate: a name that could be read as more than one tracked file is refused (two old entries declared by name); every entry that does not verify is frozen with the state it was found in, so a frozen file that changes again fails (417 keys in a table whose own hash the gate pins); and a list of hashed files is known by its content, whatever it is called (80 more lists, 750 entries; a list under another name cannot be edited, deleted or moved from 3e25c8ec3 on). Left of this finding, as before: a rule under a name outside the seal patterns, a sealed-style file one folder down, and a rule committed after its record")
SINCE_REAUDIT["G9"] = ("B1880", "the fourth re-audit's residual: every commit reachable from the tip after da25c4f49 is read, the merged ones too; a trailer, and a foreign author, on a side branch merged in with a clean message are each refused in a committed test")
SINCE_REAUDIT["X1"] = ("B1880", "the fourth re-audit's planted sentences r2, r3, r5 and r6: the excusing words are whole words ('claim' no longer passes for 'aim'), they excuse only inside the sentence that carries the phrase, every tracked page under docs/ at any depth and every .tex and .md under papers/ is read, and the three old lines are frozen by key and not by count. r4, a sentence of arrival in other words, still passes: the gate is a tripwire for the phrases it lists")
del SINCE_REAUDIT["G1"]                    # the third re-audit read B1874's change to the waivers and accepted it; nothing later

# B1886 (2026-11-11): THE SEAT'S FIFTH RE-AUDIT, of main at 16b82acda (B1880 and B1881).  It accepts all seven of its acceptance
# rows for the residuals of re-audits 3 and 4, and so has read what main changed in G2, G9 and X1.  Its rows are quoted by
# acceptance row and not by finding, so each stands beside the finding's verdict in force as a further row, and the verdict's
# own wording says what the fifth re-audit added.  Its one new residual (a page not compared where the seat's branch is
# absent, its case g1) is closed in the same landing: the generated files no longer depend on the clone.
REAUDITS["REAUDIT_5_2026-11-11.md"] = ("9ff91c3b7", "16b82acda")
VERDICT_ROWS["G2"] += [("REAUDIT_5_2026-11-11.md", "| **HASH-a** one way to read a listed name | a name that could be read as more than one tracked file is refused | the decoy (t3), and a decoy in the verification folder: both refused | **accepted** |"),
                       ("REAUDIT_5_2026-11-11.md", "| **HASH-b** a frozen entry holds what was found |"),
                       ("REAUDIT_5_2026-11-11.md", "| **HASH-c** every list of hashed files, whatever its name |")]
VERDICT_ROWS["G9"] += [("REAUDIT_5_2026-11-11.md", "| **ATTR-a** every reachable commit | done | a trailer and another author on a merged side branch (c3, c4): refused | **accepted** |")]
VERDICT_ROWS["X1"] += [("REAUDIT_5_2026-11-11.md", "| **ARR-a** the excusing words |"),
                       ("REAUDIT_5_2026-11-11.md", "| **ARR-b** the reach | every page under `docs/` and the papers' sources: 548 pages | a `.tex` file and a page below `docs/` (r5, r6): refused | **accepted** |")]
ACCEPTED.update({
    "G2": "accepted, with three residuals (re-audit 3, of the gate for the scripts a seal hashed); all three accepted as mended (re-audit 5), the third for text files: a list of hashes kept in a page or a data file is still not read",
    "G9": "accepted, with one residual (re-audit 4); the residual accepted as mended (re-audit 5): every reachable commit is read",
    "X1": "accepted (re-audit 4); its two planted sentences that passed for a defect, and the reach, accepted as mended (re-audit 5). A sentence of arrival in other words still passes: the gate is a tripwire",
})
for _fid in ("G2", "G9", "X1"):
    SINCE_REAUDIT.pop(_fid, None)          # the fifth re-audit read what main had changed there (B1880)
ACCEPTED_AT = ("16b82acda", "REAUDIT_5_2026-11-11.md")

# B1882 (2026-11-11): the audit's one open finding has its sealed card.  The state stays OPEN until the card's second stage has run.
U("V1", "OPEN", "the advisor seat has sealed a card for it (null-only, for the nulls of B1726 and B1753: does an end of the window in the height of the modulus move the count of well-fitted random targets), run its planted controls, and left the deciding count to main. Main read the card and its script in full, re-ran the controls on its own machine with the same counts, and sealed its own note and expectations before the run (B1882). The second stage has not run at this landing. Earlier (B1870): the audit's figure has no tracked source, and the audit does not say which null it measured")

# B1882, the second stage read (2026-11-11, the fifth harvest's landing): all three decisive cells read B.
U("V1", "PARTLY FIXED", "decided by the advisor seat's sealed card, with the deciding count run by main and committed unread before it was read (B1882): all three decisive cells read B, an end of the window is like other rows, two of them short of A by less than one target and by three in a thousand; every bottom end reads C; the audit's figure is reproduced (20.6 per cent of all targets of the first null have their best row in the top layer) and belongs to targets that fit nothing, since among the well-fitted the last layer is below its neighbour; under the covariant and free menus, which the card makes read-outs, the second null's top end reads A by the same rule. By the card's rule the finding is reduced to one sentence for these two nulls; the sentence, with the measured factor (about 1.5 times the rows' rate at the top for the first null, about 2 for the second, almost nothing at the bottom), stands as dated notes in B1726 and B1753. Left (P-786): the sentence on the other pages that quote either rarity; the window's two ends listed as a choice in the input budget; the same count on the live candidate's null before its card is sealed; and the seat's own verdict. Earlier (B1870): the audit's figure has no tracked source, and the audit does not say which null it measured")

# WP-0.8, worked by main from 2026-11-11 (P-785: the errors in the mathematics stay with main).
U("E2", "PARTLY FIXED", "MENDED ON MAIN, AND NOT COUNTED AS FIXED UNTIL THE ADVISOR SEAT HAS RE-AUDITED IT (a builder gives no verdict on what it built; that holds for main too). Main's own computation, in its own code: the knot group's image has order 10, 320 and 20480 at (2), (4) and (8); in SL(2, O/I)/{+-1}, the group PSL(2, O_3) maps to, its index is 6 at (2) and 12 at (4), and 2 is inert, so the level is (4), as the ledger's link C9 has said since 2026-09-16. The lock asserted level (8), which is the reading in the quotient by every central unit of square one (four at (4), of which the image holds two). The lock now asserts the level in the standard group with the ambient orders counted, keeps the old reading as what it is, and fails if any page states the old level for this group with no correction in the same file; the correction is carried to the two verdict lines, the law map's two rows, the theorem registry, the error ledger's E21 and E22, and ten other pages, six of which the lock's own sweep found after main's search had missed them. Before (the reader's): the lock's own function gives index 6 at level 4 and 12 at level 8 under its quotient by every central unit; under the standard quotient the index is already 12 at level 4")

U("E5", "PARTLY FIXED", "MENDED ON MAIN, AND NOT COUNTED AS FIXED UNTIL THE ADVISOR SEAT HAS RE-AUDITED IT. The scan's sentence is corrected where it stands, in B892's findings and verdict line, with the old text kept: the golden-section step never ran, and a 120-point grid shows nothing between its nodes. What excludes a real nullity-14 point is now computed on main (B892's verification/walls_on_the_line.py): s1, x14, x16 and x22 commute and diagonalise together, so the joint nullity at every point of the line is read off their weights; it jumps at finite t only at four purely imaginary points, 14 at one conjugate pair and 18 at the other, and is 12 at every real point but pure x16, with a direct rank computation agreeing at the walls, beside them and at six real points. The same run verifies the mechanism B874's addendum records as the solo seat's: 34 active weights in seven proportionality classes of sizes 2, 2, 6, 6, 6, 6, 6, three real and two conjugate pairs. Main's first attempt, a finer scan with a bound between grid points, failed its own checks, the matrices being scaled over fourteen orders of magnitude. Before (main's own reading): the refinement runs only when the grid finds nothing, and the grid lands on the wall, so it never runs")

U("E7", "PARTLY FIXED", "MENDED ON MAIN, AND NOT COUNTED AS FIXED UNTIL THE ADVISOR SEAT HAS RE-AUDITED IT. B1028's verdict is OPEN and its headline number is withdrawn as a measurement: the walk sums eleven prices typed 0.0 and asserts the sum is 0.0, and its check is a substring match that still passes on B997's line, since corrected to say the door set is {1, 4}. The claim line names what is not priced (the family declaration, by the ledger's own addendum; the selection within the family; the choice of the principal embedding) and the one endpoint credited, the algebra of dimension 14; the claim as first asserted is kept after the correction. The correction is carried to the roadmap, the claim page, the framework page and seven other pages, and a lock fails if any page states the zero without it; the lock also shows the fault on the walk itself. Before (main's own count): eleven typed zeros are summed and asserted to be zero; the arc's addendum says one row is unpriced and its verdict line was not changed")

# THE SEAT'S SIXTH RE-AUDIT (2026-11-11), of main at 8d90a5b2a: main's first two mends of the errors in the mathematics.  E5 it
# accepts, having computed the claim again by another route; E2 it accepts in part, the lock and the mathematics being accepted
# and the arc's own claim line still leading with the old level.  Main changed that line the same day, and what it changed is
# listed as not re-read by a seat.  It is the last re-audit asked of this seat: the owner, to main on 2026-11-11, has it build
# its five packages and nothing else, and the re-audit of main's mends goes to another seat (P-792).
REAUDITS["REAUDIT_6_2026-11-11.md"] = ("72929e16e", "8d90a5b2a")
VERDICT_ROWS["E5"] = [("REAUDIT_6_2026-11-11.md", "| **E5** B892's scan never refines | PARTLY FIXED: mended, not counted | **accepted** |")]
VERDICT_ROWS["E2"] = [("REAUDIT_6_2026-11-11.md", "| **E2** the knot group's congruence level | PARTLY FIXED: mended, not counted | **partly.** The lock and the mathematics are accepted.")]
ACCEPTED.update({
    "E5": "accepted (re-audit 6): the claim computed again by another route, exactly over the rationals where it can be and at 60 digits where it cannot; two notes, neither a residual, both since run or recorded by main",
    "E2": "partly. The lock and the mathematics are accepted (re-audit 6); the arc's own claim line still led with level (8), and the generated spine showed only that",
})
ACCEPTED_AT = ("8d90a5b2a", "REAUDIT_6_2026-11-11.md")
U("E5", "FIXED", "the scan's sentence is corrected where it stands, with the old text kept, and what excludes a real point of nullity 14 is computed on main: the joint weights of four commuting elements (B892's "
  "verification/walls_on_the_line.py), all four finite walls purely imaginary. THE ADVISOR SEAT'S SIXTH RE-AUDIT ACCEPTS IT, having computed the claim again by another route. Of its two notes main has since run the "
  "first: the instrument at each of the cubic's three real roots, where the walls are purely imaginary at all three and equal the seat's values to nine digits (walls_at_the_three_roots.py), so the structure "
  "paper's sentence about all three roots has a computation of main's behind it. The second stands as a choice the lock states: the recomputation is in the slow lane. A figure main's landing message quoted "
  "differs from the committed run's; main found the figures differ from run to run on one machine and says so in the script and the findings; nothing rests on them")
U("E2", "PARTLY FIXED", "the knot group's congruence level is (4): the lock asserts it in the standard quotient, and the correction stands on every page that stated (8). THE ADVISOR SEAT'S SIXTH RE-AUDIT ACCEPTS THE "
  "LOCK AND THE MATHEMATICS, every number computed again in code that shares none with the lock, AND GIVES 'PARTLY' FOR ONE LINE: B734's own claim line still led with level (8), and the generated spine showed only "
  "that. MENDED BY MAIN THE SAME DAY AND NOT RE-READ BY A SEAT: the line leads with the correction and a test holds the order; the lock's docstring no longer calls its second generator Riley's; the sweep sees six "
  "more shapes of the old statement and found three places it had missed (B942's verdict line, a note among the open leads, a row of the relay ledger), each corrected; the gloss that the group defies a base rate, "
  "withdrawn in the theorem ledger on 2026-09-16, is withdrawn in the three places it still stood")
SINCE_REAUDIT["E2"] = ("B734", "the claim line leads with the correction, and a test holds the order; the docstring's wording; the sweep widened to the shapes the re-audit planted, with three more places corrected; the withdrawn gloss withdrawn where it stood")

# THE SEAT'S SEVENTH RE-AUDIT (2026-11-11), of main at 338b14fe3: main's third mend of the errors in the mathematics, E7.  Accepted.  It
# was made before the owner's ruling that this seat builds and is not asked to verify had reached it (P-792), and is taken as delivered.
REAUDITS["REAUDIT_7_2026-11-11.md"] = ("7c83b9799", "338b14fe3")
VERDICT_ROWS["E7"] = [("REAUDIT_7_2026-11-11.md", "| **E7** the freedom ledger's zero | PARTLY FIXED: mended, not counted | **accepted** |")]
ACCEPTED.update({"E7": "accepted (re-audit 7): the verdict is not PROVED, the unpriced row and the embedding choice are in the claim line, one endpoint is credited and named, and the correction leads the line"})
ACCEPTED_AT = ("338b14fe3", "REAUDIT_7_2026-11-11.md")
U("E7", "FIXED", "B1028's verdict is OPEN and its headline number is withdrawn as a measurement: the walk sums eleven prices typed 0.0 and asserts the sum is 0.0, and its check is a substring match that still passes on "
  "B997's line, since corrected. The claim line names what is not priced (the family declaration, the selection within the family, the principal embedding) and the one endpoint it credits, and the correction stands "
  "on every page that quoted the zero, with a lock that fails if any states it without. THE ADVISOR SEAT'S SEVENTH RE-AUDIT ACCEPTS IT against its acceptance row, and notes that the correction leads the line. What "
  "the chain's freedom costs stays an open question with its own row (P-789)")

# the owner's rulings of 2026-11-10 AS RELAYED by the advisor seat. The relay's own rule, and main's: each is confirmed with the
# owner once before main acts on it. Main asked on 2026-11-10 about the eleven then relayed; the owner answered main the same day,
# in the words kept in CONFIRMATION below. The two relayed after main had asked were not covered by that answer; asked about them,
# the owner did not confirm them (NOT_CONFIRMED below). Main treats neither as a ruling.
RULINGS = [
    ("the goal", "the programme's only goal is a parameter-free theory of everything", ["WP-0.10"]),
    ("the claim", "one self-consistent outcome", ["WP-1.6", "WP-0.11"]),
    ("attribution", "Commits as `originaxiom`, no AI trailer", ["WP-0.7"]),
    ("the weave discipline", "the owner agreed to the five proposals", ["WP-0.11", "WP-1.6"]),
    ("the count as an output", "the count is computed, not typed", ["WP-0.12"]),
    ("the headline's form", "is the number of value rows on the whole map", ["WP-0.12"]),
    ("the map on the desk", "the map is agreed, and main builds it as part of the dashboard already built", ["WP-0.12"]),
    # four more, relayed later the same day (harvest row 1635). The seat numbers its relayed rulings; its eleventh is not the
    # claim page's anchor rule, which the record also calls R11.
    ("what self-consistent means", "means the closed loop", ["WP-1.6"]),
    ("the first back-edge to try", "back-edge A first", ["WP-1.6", "WP-4.1"]),
    ("the fork inside it", "is about A-all", ["WP-1.6", "WP-0.11"]),
    ("the founding principle as the selection rule", "try the founding principle as the selection rule", ["WP-1.5", "WP-1.6"]),
    # two more, relayed the same evening (harvest rows 1648 and 1649; the seat's file, read @ 6ab2bbdb2)
    ("stress-test the principle", "stress-test the principle; start with the ambiguity attack", ["WP-1.1"]),
    ("the gap, for every seat", "the entire programme is an open one-way line, not a closed loop", ["WP-1.6", "WP-0.11"]),
    # four more sentences, recorded by the seat later the same evening and marked by it as relayed (harvest row 1659). Main put
    # them to the owner once (P-771), because the foundation's text depends on the last.
    ("no rule picks a next thing", "the phrase is not a rule that picks a next thing", ["WP-1.1", "WP-1.5"]),
    ("what exists is what survives", "what cannot be cancelled is kept, all of it", ["WP-1.1", "WP-1.5"]),
    ("the ledger, cancelling, interaction", "The account is the whole ledger.", ["WP-1.1", "WP-1.6"]),
    ("the tick is an act", "The tick is an act, and both kinds of history are in the ledger", ["WP-1.4"]),
]
# the owner's answer to main, verbatim (spelling as written), and the rulings it covers: the eleven main had named in its question
CONFIRMATION = ("2026-11-10", "yes, but i also wanr your opinion on all")
CONFIRMED = ["the goal", "the claim", "attribution", "the weave discipline", "the count as an output", "the headline's form", "the map on the desk",
             "what self-consistent means", "the first back-edge to try", "the fork inside it", "the founding principle as the selection rule"]
# the owner's answer to main about the two relayed later, verbatim: not confirmed
NOT_CONFIRMED = {
    "stress-test the principle": "im not very sure about it, i wouldnt take it for granted",
    "the gap, for every seat": "it was in other context",
}
# main's opinion on each, asked for by the owner in the same answer and given the same hour (one line each; the full text is in the register, P-758)
OPINION = {
    "the goal": "agree: the aim may be stated, arrival may not; change all twelve places at once and keep the ceiling",
    "the claim": "agree it is the claim to state, because two outcomes exhibited refute it; one outcome can only mean one orbit under the symmetries, a history with its mirror",
    "attribution": "agree; already the practice. The gate does not read commit messages and should",
    "the weave discipline": "agree with all five; the second-thread control is the most valuable; plenitude enters the foundation with the weight listed as open",
    "the count as an output": "agree; the arcs' dependency lists mix what is used with what is cited, so the edges need a type first",
    "the headline's form": "agree, with one safeguard: the second number's list is frozen at a named commit before any comparison",
    "the map on the desk": "agree; every status computed by the weakest link, so the picture cannot look better than the mathematics",
    "what self-consistent means": "agree; on main's map no result returns to fix an input (B1867). The loop is an equation and not a circular argument, and it is not shown to be the only route",
    "the first back-edge to try": "agree as the first try: its opening test, whether a state exists, is a yes or no nobody chose. As designed it uses one input of the budget and does not remove it",
    "the fork inside it": "agree: it is the owner's law applied consistently. It closes nothing yet, since the joint read-out of all histories has no definition",
    "the founding principle as the selection rule": "worth doing, and the result is honest: the rule picks the run of six only if the level is put in. To be verified on main (P-762)",
}

# THE OWNER'S ANSWERS OF 2026-11-11, given to main directly in a dialog, each to a question main put with its recommendation.
# The questions and the chosen answers are kept verbatim; the owner chose main's recommended answer each time, and the label
# says so.  The first two answers confirm the four sentences that had been asked once (P-771).  The last two answer the advisor
# seat's two questions (P-774) and are rulings to main that no seat relayed.  None is carried into a governing document by
# this file: that is P-767.
CONFIRMED_LATER = {          # the relayed ruling -> (date, the question as main put it, the owner's chosen answer)
    "the tick is an act": ("2026-11-11", "Is the tick an act?", "Yes, admit it (Recommended)"),
    "no rule picks a next thing": ("2026-11-11", "Three sentences on the principle's wording: are they yours for main as well?", "Yes, all three (Recommended)"),
    "what exists is what survives": ("2026-11-11", "Three sentences on the principle's wording: are they yours for main as well?", "Yes, all three (Recommended)"),
    "the ledger, cancelling, interaction": ("2026-11-11", "Three sentences on the principle's wording: are they yours for main as well?", "Yes, all three (Recommended)"),
}
OPINION.update({
    "the tick is an act": "admit it: it is the founding rule's single step, nothing forbids it, and it makes the root's mirror symmetry a consequence. It supplies no hand. Build nothing on the added histories before the three debts are computed (P-769). MAIN'S OPINION AS FIRST GIVEN ALSO SAID that it removes the orientation as a choice; that was said without the owner's standing ruling of 2026-10-08 ('even ticks observed') beside it, and is withdrawn until the two are related",
    "no rule picks a next thing": "agree as wording: it matches the computations, in which every 'least' on record returns what was put in. It is not yet a mathematical object",
    "what exists is what survives": "agree as wording: nothing is ranked least or first, so every selection by rank is a selection on one thread and is labelled so",
    "the ledger, cancelling, interaction": "agree as wording: 'the whole ledger' and 'a third thing that is kept' can be adopted; neither is yet a mathematical object, and the same definition is owed as for all histories together",
})
DIRECT_RULINGS = [           # (name, the question as main put it, the owner's chosen answer, date, packages, what it means on main)
    ("what a ground is", "What is a ground: the act itself, or any history that exists?", "The act itself (Recommended)", "2026-11-11", ["WP-1.5", "WP-1.4"],
     "one ground, the tick, and one level, 5, named without ranking anything; to be written as a new postulate with its own number, not as derived (B1876: with every history as a ground there are four root classes and no order)"),
    ("what 'the ledger must close' means", "What does 'the ledger must close' mean: that the whole agrees with itself, or that one value comes out?", "Whole agrees (Recommended)", "2026-11-11", ["WP-1.6", "WP-0.10"],
     "one outcome is one orbit of the whole, not one history picked; the closing selects nothing by itself, and a value can only be read from the whole, which needs the weight"),
    # asked the same day, when main found that it had not put the owner's standing ruling of 2026-10-08 beside its question on the tick
    ("how 'the tick is an act' stands with 'even ticks observed'",
     "On 2026-10-08 you ruled 'even ticks observed' ... Today you ruled that the tick is an act and both kinds of history are in the ledger. I did not remind you of the first ruling when I asked. How do the two stand together?",
     "After the computation", "2026-11-11", ["WP-1.4"],
     "both rulings stand side by side and the foundation records both; their relation is decided after main has computed the weave's theorems for the group with the exchange (P-769). Until then nothing says that the orientation has stopped being a choice, or that the mark is both twins"),
    # the computation was made the same day (B1879), and the question put again with its result
    ("'even ticks observed', after the computation",
     "With the computation in hand: your ruling of 2026-10-08 says 'even ticks observed' ... Today you ruled the tick an act. The computation shows the only thing at stake between them is the hand ... How should they stand together?",
     "A condition to derive (Recommended)", "2026-11-11", ["WP-1.4", "WP-1.6"],
     "every tick is in the ledger; 'only even ticks are observed' is no longer a ruling but a condition the weight must deliver; the chiral three stays exactly as conditional as it was; the budget's orientation bit is a named condition to derive, not a declared choice, and is not counted as derived (B1879)"),
]

ADVISOR_QUOTES = [
    ("OWNER_RULINGS_2026-11-10.md", "cc confirms each with the owner before acting on it"),
    ("OWNER_RULINGS_2026-11-10.md", "The weighting rule must be forced"),
    ("OWNER_RULINGS_2026-11-10.md", "Typicality is no longer the test"),
    ("ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md", "No mathematical error was found in the foundations"),
    ("ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md", "The enforcement layer does not enforce what it says"),
    ("ADVISOR_TO_CC_2026-11-10_AUDIT_FINDINGS.md", "every finding below is to be reproduced on main's own code before anything is banked"),
    ("ACCEPTANCE_CRITERIA.md", "A fix to enforcement is accepted only when a planted violation turns it red"),
    ("ACCEPTANCE_CRITERIA.md", "The certificate is a generated file, and the seal is refused without it"),
    ("dry_run/DRY_RUN_VALUE_CHAIN_B1841.md", "The certificate would be refused, on six grounds"),
    ("dry_run/DRY_RUN_VALUE_CHAIN_B1841.md", "the conditions are in series"),
    # the three notes the exits below are read from (digit-free quotes; checked where this clone holds the revision)
    ("principle_top_down/THE_PRINCIPLE_TOP_DOWN.md", "Every row is an argument to be proved or refuted. None is a result."),
    ("principle_top_down/THE_PRINCIPLE_TOP_DOWN.md", "admitted, not forced by the words"),
    ("principle_top_down/THE_PRINCIPLE_TOP_DOWN.md", "argued FORCED up to the sign"),
    ("principle_top_down/THE_PRINCIPLE_TOP_DOWN.md", "the principle does not obviously force it, and may speak against it"),
    ("THE_CLAIM_STATED_THE_CLOSED_LOOP.md", "Nothing computed at the end flows back to constrain anything chosen at the start."),
    ("THE_CLAIM_STATED_THE_CLOSED_LOOP.md", "No continuous freedom enters here."),
    ("THE_CLAIM_STATED_THE_CLOSED_LOOP.md", "None of the four is a back-edge yet."),
    ("back_edge_A/DESIGN_BACK_EDGE_A_THE_STATE.md", "is a consistency condition, not a free premise"),
    ("back_edge_A/DESIGN_BACK_EDGE_A_THE_STATE.md", "A-all is what plenitude and the weave rule ask for"),
    ("ADVISOR_TO_ALL_SEATS_2026-11-10_LINE_OR_LOOP.md", "A line result is still a result."),
]

# the six results the closure map calls its headlines (B1858's map_source.HEADLINES), by node
HEADLINES = ["G:ROOT", "MC:Z6", "W:INDEX3", "V:SIX", "T:IM", "E:L10"]

# the record's own checklist of what a theory of everything must pass (B1304), row by row
TOE_LEDGER = [
    ("Gauge group and matter", ["WP-1.8", "WP-3.1", "WP-3.2", "WP-1.7"]),
    ("Chirality", ["WP-1.4", "WP-3.3"]),
    ("Values", ["WP-4.1", "WP-3.4", "WP-4.4", "WP-5.3"]),
    ("Dynamics", ["WP-2.1", "WP-2.5", "WP-4.2"]),
    ("Gravity", ["WP-4.5"]),
    ("Quantum consistency", ["WP-3.5", "WP-4.2"]),
    ("Predictions", ["WP-4.6", "WP-5.3", "WP-6.1"]),
    ("Say which endpoint", ["WP-4.4", "WP-5.2"]),
]
# words of the record that this programme binds to, checked on main
MAIN_QUOTES = [
    ("docs/THE_CLAIM.md", "at most two declared anchors"),
    ("docs/INPUT_COMPLETENESS_LEDGER.md", "mandatory checklist for any SM-facing cell"),
    ("docs/TOE_REQUIREMENTS_LEDGER.md", "The checklist any theory of everything must pass"),
    ("docs/TOTAL_INPUTS_SCOREBOARD.md", "**Borrowed joints: 13** (10 CHOSEN, 2 FITTED, 1 ANSATZ)"),
    ("GENESIS.md", "A DICTIONARY MAY BE EARNED BY PREDICTION"),
    ("GENESIS.md", "7. *Worth spending.*"),
    ("docs/THE_WEAVE.md", "the family"),
]

# ---------------------------------------------------------------- the input budget
# Every node of the map that is presently an input of main's spine -- a postulate, a choice, a tag, a fit, an ansatz, an
# unstated commitment -- grouped by the choice it names. The same choice stands under several names across the record; the
# budget counts choices as the record lists them (their independence is the record's listing; it is not tested here).
# The kinds follow the record's own grades where it has them (the scoreboard's CHOSEN, FITTED and ANSATZ; GENESIS's POSTULATED):
#   axiom           a structural statement of the foundation; no number                      (POSTULATED items of GENESIS §§ 1-4)
#   bit             one of two
#   discrete        one of a finite menu or set, as the record lists it                      (the scoreboard's CHOSEN)
#   real            a continuous number: fitted, graded an input, or an anchor               (the scoreboard's FITTED)
#   ansatz          a functional form assumed                                                (the scoreboard's ANSATZ)
#   identification  which mathematical object is read as which physical one
# `form=True` marks a discrete choice that is a choice of a functional form from a menu (a norm, a metric, a direction): the
# record counts it as one discrete choice, and the menu it is taken from is itself chosen.
INPUTS = []


def I(name, kinds, members, note="", form=False):
    INPUTS.append(dict(name=name, kinds=dict(kinds), members=list(members), note=note, form=form))


I("what exists (PF1)", {"axiom": 1}, ["G:PF1"])
I("the principle's mathematical form", {"identification": 1}, ["G:PF1-FORM"], "a reading of the principle, not a derivation from it")
I("the remainder cannot be exhausted (PF2)", {"axiom": 1}, ["G:PF2"])
I("the method (PF3)", {"axiom": 1}, ["G:PF3"])
I("two records", {"axiom": 1}, ["G:GM1"])
I("the unit shears", {"axiom": 1}, ["G:GM2"])
I("no period", {"axiom": 1}, ["G:GM3"])
I("the carrier", {"axiom": 1}, ["G:GM4"])
I("reversible updates", {"axiom": 1}, ["G:GM5a"])
I("inverse moves are legal", {"bit": 1}, ["G:GM5b"])
I("positivity: the side of the mirror", {"bit": 1}, ["G:GM5d"])
I("the selection criterion", {"discrete": 1}, ["G:SE1"], "other criteria select other objects")
I("the ground", {"axiom": 1}, ["G:SE3"], "the ground is the act itself, the tick (GENESIS v1.65, SE3): a definition the frame needs, which nothing computed can decide; main's entry, tagged. Its level follows by the discriminant and is not a further input (B1884)")
I("the orientation", {"bit": 1}, ["G:SE2", "G:FK2", "S:S02", "FL:03"], "one choice under four names; the scoreboard lists it as a CHOSEN joint")
I("which family is the object", {"discrete": 1}, ["G:FK13"])
I("the dictionary's link Λ", {"identification": 1}, ["TAG:LAMBDA"])
I("one unit of end data", {"discrete": 1}, ["TAG:UNIT"])
I("the clock", {"bit": 1}, ["W:CLOCK"], "moves or geometric length; it sets the weight of every thread")
I("the structural theorem's external data", {"bit": 2, "real": 1, "discrete": 2}, ["MC:HYP"],
  "the record's own typing: two bits, one scale, one Lie type, one closing direction. The record flags this count as owed a re-read (P-374), and its older axiom list is not reconciled here with the foundation's items. The scale is dimensionful: the one such anchor the record allows")
I("the modulus τ", {"real": 2}, ["A:A01", "FL:04"], "fitted")
I("the line's slope", {"discrete": 1}, ["A:A02"], "with the offset, the two components of one line")
I("the line's offset", {"discrete": 1}, ["A:A03"])
I("the Higgs direction", {"discrete": 1}, ["A:A04", "FL:06"], "one section of a menu", form=True)
I("the up-conjugate reading", {"identification": 1}, ["A:A05", "FL:09"])
I("the normalisation: the end, the generations' metric, the channel weights", {"discrete": 3}, ["A:A07", "A:A08", "A:A09", "FL:11"],
  "the scoreboard: a discrete principled end, nothing fitted. The advisor seat's audit holds that a continuous family stands behind the end's menu (its finding V4)", form=True)
I("the lepton factor", {"real": 1}, ["A:A10", "FL:12"], "continuous and fitted")
I("one address for all sectors", {"discrete": 1}, ["A:A11", "FL:07"])
I("tree level at one scale, no running", {"identification": 1}, ["A:A12", "FL:13", "FL:21"])
I("a flat bundle on the fibre", {"ansatz": 1}, ["S:S01"])
I("the generations as three images of one value", {"identification": 1}, ["FL:10"])
I("the class of lines", {"discrete": 1}, ["FL:08"], "flat lines rather than centre Wilson lines is the choice; the cutoff on their order is a rule of reach (FL-18)")
I("θ̄", {"real": 1}, ["FL:16"], "graded an input by the record (Review 74): the frame leaves it free")
I("the framing of the read-out", {"discrete": 1}, ["T:FRAMING"])
I("the charge premise at level five", {"bit": 1, "discrete": 1}, ["T:CHARGE5"],
  "two choices under one name (B1869): which sense of 'detect', the whole level or the line, a bit (P-721); and which levels count, a choice among sets of levels")
I("minimisation as the use of the action", {"discrete": 1}, ["T:MINIM"])
I("point or weight", {"bit": 1}, ["T:POINT-WEIGHT"])
I("the chiral premise", {"bit": 1}, ["SC:PREMISE"])
I("the block read as a ratio of scales", {"identification": 1}, ["SC:R2"])
I("the content that runs", {"identification": 1}, ["SC:R4"], "the Standard Model's, borrowed")

# HOW EACH INPUT COULD LEAVE THE BUDGET, as far as three notes of the advisor seat name a route for it: its forcing ledger
# (principle_top_down/THE_PRINCIPLE_TOP_DOWN.md), its statement of the closed loop (THE_CLAIM_STATED_THE_CLOSED_LOOP.md) and its
# design of the first back-edge (back_edge_A/DESIGN_BACK_EDGE_A_THE_STATE.md), read in full at the pin above and checked by main
# in B1867.  This is a harvest of those notes onto the budget, with main's checks beside it.  It is not a sweep of the record:
# UNTOUCHED says only that the three notes name no route, and the input's package holds the record's own.  Nothing here changes a
# grade: an argument is not a proof and a named back-edge is not a built one.
EXIT_KINDS = {
    "KEPT": "the principle itself: a parameter-free theory keeps it, stated",
    "FORCING ARGUED": "an argument that the principle forces it is written down, with no objection on this page; not proved",
    "ONE CLAUSE SHORT": "a forcing argument is written down, and main has shown the clause it lacks; not an exit as written",
    "ADMITTED": "the principle allows it and does not force it; no route is named",
    "PRESSED": "the notes argue against it standing as an input in its present form; no route is named",
    "RIGID": "fixed by the geometry once the history is fixed; what stays chosen is named",
    "BACK-EDGE NAMED": "a condition computed downstream that the choice must satisfy is named; none is built",
    "DICTIONARY": "an identification: the loop does not pay it; it is earned only by a sealed prediction",
    "UNTOUCHED": "the three notes name no route; the package holds the record's own",
}
EXITS = {
    "what exists (PF1)": ("KEPT", "the principle. The notes test its wording; they do not ask whether to keep it."),
    "the principle's mathematical form": ("PRESSED", "the ledger's formal statement is one reading. Its ambiguity attack (pre-registered, not run at the pin) asks whether the owner's words fix a form at all; where two faithful readings differ, the difference is a clause for the owner to rule on."),
    "the remainder cannot be exhausted (PF2)": ("KEPT", "the ledger: it follows if the recursion never ends, and has to be reconciled with a loop that returns on itself."),
    "the method (PF3)": ("KEPT", "not addressed; a method, not a number."),
    "two records": ("ADMITTED", "the ledger: admitted, not forced by the words. Three or more records is the alternative (B1679)."),
    "the unit shears": ("ADMITTED", "the ledger: admitted; nothing in the words excludes longer shears. The loop's test on the silver and bronze backgrounds is the test named."),
    "no period": ("ONE CLAUSE SHORT", "the ledger: finite order is a cancellation that completes, a fixed direction a side that never changes. Main (B1867): the formal statement removes finite order and not the fixed direction; a single shear meets its form of existing at every level. One clause short."),
    "the carrier": ("ONE CLAUSE SHORT", "the ledger: if the difference between the two orders is not cancelled the group is free, and the puncture follows (the SM seat's B1380, not verified on main). Main (B1867): not commuting does not give free; a clause that nothing at all cancels is needed."),
    "reversible updates": ("ADMITTED", "the ledger gave one line for it (an act that merges two sides ends the distinction) with no alternative exhibited; its author has withdrawn it as an exit (the seat's read of this page)."),
    "inverse moves are legal": ("FORCING ARGUED", "adopted by the owner on B1662's argument; the ledger agrees: there must be something to cancel with."),
    "positivity: the side of the mirror": ("FORCING ARGUED", "the ledger: forced up to the sign. Main (B1867): the normal form is a theorem, checked on every hyperbolic matrix with entries up to five; the sign is a separate bit, and the selection criterion decides it if that criterion stands."),
    "the selection criterion": ("ONE CLAUSE SHORT", "the ledger: a fixed character is a place where nothing happened. Main (B1867): as an exclusion this removes every departure too (the run of six fixes twenty); as a minimum it is the reading GENESIS already grades an interpretation. LR is the one word with a single fixed character, so this row carries the whole selection of the object. For the departure, the principle read as 'the least that no counted level detects' picks the run of six only when the level is put in (B1869). A second route is named and is not open (B1876, the advisor seat's sealed run verified on main): if the ground is the act itself, exactly one history is made of one atom, the tick, and its level is 5 with nothing ranked; that needs the owner's word that the tick is an act (P-771) and a clause saying what a ground is (P-774). With every history as a ground the record's rule has four root classes and no order. BOTH GIVEN BY THE OWNER on 2026-11-11, to main: the tick is an act, and a ground is the act itself. The route is then a postulate, to be written with its own number (P-767); it is not a derivation, and this entry keeps its kind until the foundation is amended."),
    "the ground": ("ADMITTED", "the principle allows the act as the ground and does not force it. With every history a ground the record's rule has four root classes and no order (B1876); the act as the ground names one without ranking. No route out of the budget is named: it is a definition."),
    "the orientation": ("BACK-EDGE NAMED", "the owner's ruling of 2026-11-11, to main, with B1879's computation in hand: every tick is in the ledger; that only even ticks are observed is no longer a ruling but a condition the weight must deliver. So this input has a named condition downstream that it must satisfy, and none is built: it is not derived and is not counted as derived. [Was PRESSED: the ledger: the principle does not force it and may speak against it. The non-orientable sibling is the alternative. Verified on main (B1871): if the tick, the owner's founding rule, is an act, both sheets exist and this is no choice; it supplies no hand. Asked of the owner (P-771). RULED BY THE OWNER on 2026-11-11, to main: the tick is an act. The owner's ruling of 2026-10-08, 'even ticks observed', also stands; how the two stand together waits on a computation, at the owner's word (P-769). So this entry keeps its kind: nothing yet says that the orientation has stopped being a choice.]"),
    "which family is the object": ("UNTOUCHED", ""),
    "the dictionary's link Λ": ("DICTIONARY", ""),
    "one unit of end data": ("UNTOUCHED", ""),
    "the clock": ("UNTOUCHED", "the loop note takes the harmonic time of one history as forced (B1846). This input is the weave's clock, which weights threads, and the notes name no route for it; they repeat B1813's warning against a thread sum with a chosen weight."),
    "the structural theorem's external data": ("BACK-EDGE NAMED", "the loop note's fourth candidate: consistency conditions that cut an input to a finite list (B1229). It warns that each use is an identification."),
    "the modulus τ": ("RIGID", "the loop note: given the history the metric is unique, so no continuous freedom enters, and the rule reads the modulus from a level surface. Still chosen: the history, point or weight, and which point. Two candidates are named for the point: a state, and a holder."),
    "the line's slope": ("BACK-EDGE NAMED", "the design: a line on the fibre extends over the history exactly when the history fixes its character, so 'the departure fixes the line' is a condition and not a free premise. Main checked its exact facts (B1867). The condition cuts the lines to those the history fixes; it does not by itself pick one."),
    "the line's offset": ("BACK-EDGE NAMED", "with the slope: one line, one condition."),
    "the Higgs direction": ("UNTOUCHED", "the loop note lists it as chosen, and records B1823's negative against a holder fixing it."),
    "the up-conjugate reading": ("DICTIONARY", ""),
    "the normalisation: the end, the generations' metric, the channel weights": ("UNTOUCHED", "the loop note lists the end and the metric on generations as chosen."),
    "the lepton factor": ("UNTOUCHED", ""),
    "one address for all sectors": ("UNTOUCHED", ""),
    "tree level at one scale, no running": ("DICTIONARY", ""),
    "a flat bundle on the fibre": ("UNTOUCHED", "the design takes the frame's flat bundle as the coefficient of its operator. That uses this input; it does not derive it."),
    "the generations as three images of one value": ("DICTIONARY", ""),
    "the class of lines": ("UNTOUCHED", ""),
    "θ̄": ("UNTOUCHED", ""),
    "the framing of the read-out": ("UNTOUCHED", ""),
    "the charge premise at level five": ("BACK-EDGE NAMED", "the design: the charge premise is the same extension condition for a frame that uses the whole space at the level, the line premise for a frame on one line; which holds reduces to a question on the register (P-721). The loop note's third candidate, a level law, has B1855 against it."),
    "minimisation as the use of the action": ("PRESSED", "the design's fork: one history by least action keeps this input; all allowed histories together drops it and owes a definition of their joint read-out. Length and volume disagree on what is selected (B1857)."),
    "point or weight": ("BACK-EDGE NAMED", "the first candidate: the point is where the history's lightest state sits. The scalar ground state is the weight and gives no point, so the operator must have no zero mode. Designed; not run."),
    "the chiral premise": ("PRESSED", "the ledger: the first departure is chiral, and its mirror is the same departure on the other letter. Main (B1867): the swap of the letters is the mirror for every word, so a rule symmetric under the swap selects mirror pairs; a net hand needs the order bit."),
    "the block read as a ratio of scales": ("DICTIONARY", ""),
    "the content that runs": ("DICTIONARY", ""),
}

# rules of the comparison: how a prediction is graded. They are commitments, and they are not inputs of the theory.
RULES = ["V:EARN-RULE", "V:HELD", "FL:14", "FL:15", "FL:17", "FL:18", "FL:19", "FL:22", "FL:23", "FL:24", "FL:25", "FL:27"]
# a count of other inputs, not an input
TALLIES = ["MC:PRICE"]
# OUTSIDE this budget, and said so on the page: the lanes' conditional model has supplied inputs of its own, which main has not
# typed because main has not verified the model (the map grades them LANE-INPUT); and the agy lane's frame has its own borrowed
# joints, counted on the scoreboard.
LANE_INPUT_NOTE = {
    "E:L01": "the carrier; the same as the foundation's two records and punctured torus",
    "E:L02": "the parent, supplied",
    "E:L03": "the quaternion holonomy (the weave's own common point, which main has derived) and its lift, with core signs unselected",
    "E:L04": "the modulus, the cusp metric, one length and one coupling",
    "E:L05": "the spin structure and the compensating lifts",
    "E:L06": "the split of the parent and the charges",
    "E:L07": "the balanced background and the Wilson line",
}

# what a parameter-free theory may keep, by kind (R11, and the work order's C1: a reduction counts only if the choice disappears
# without returning through a representation, carrier, metric, normalisation, field assignment, boundary condition, state, measure or fit)
TARGET = {
    "axiom": "kept, each stated; fewer is better and none may hide a number",
    "bit": "derived, shown to be a convention with no observable effect, or declared with both branches carried",
    "discrete": "derived, shown equivalent, or declared with its alternatives carried and priced; where it is a functional form taken from a menu, the form is derived from the action, since the menu is itself a choice",
    "real": "none free: at most one dimensionful and one dimensionless anchor, sealed in advance (R11)",
    "ansatz": "none: derived from the action, or replaced by what the action gives",
    "identification": "none unearned: each derived, or earned by sealed prediction under the foundation's rule",
}

# the work order's three statuses, and what each needs here
MILESTONES = [
    ("M1", "the dependency map is complete", "every package's nodes are in the map, every map node that needs a path has a package (this builder's check), and WP-0.6 holds at every landing",
     ["WP-0.6"]),
    ("M2", "the physical construction is verified", "every package of C1 to C4 is closed at its acceptance; main adds that C0's classes are empty upstream of what is claimed (the work order's own second status does not ask that)",
     ["C0", "C1", "C2", "C3", "C4"]),
    ("M3", "the predictions are ready for comparison", "every package of C5 is closed: the certificate, the upstream audit, the sealed card, the independent challenge",
     ["C5"]),
]

# the work order, pinned (digit-free quotes; checked where this clone holds the revision)
WORK_ORDER = ("521e6f241", "reports/physical_bridge_2026_09_05/precalibration_closure_2026_11_10/WORK_ORDER.md")
WORK_ORDER_QUOTES = {
    "C1": "Foundational generation and selection",
    "C2": "One physical action, stationary background and response",
    "C3": "field content and interactions",
    "C4": "States, quantum dynamics, parameters and gravity",
    "C5": "Precomparison seal and independent challenge",
    "C6": "Dimensional calibration and empirical comparison",
    "statuses": "dependency map complete; physical construction verified; predictions ready for comparison",
    "rule": "Completion must be earned by evidence, not by the requested adjective",
}

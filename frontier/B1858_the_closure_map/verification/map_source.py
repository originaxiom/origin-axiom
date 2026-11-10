"""B1858 -- the closure map's curated source (documentary; no scientific run; no held-out value read or written).

Every node is one claim, premise, choice or duty of the programme, with:
  id, layer, kind, grade, text (one plain sentence), pins (where the record says it), rows (register rows), arcs.

A pin on main is (path, quote): the quote must occur verbatim, up to whitespace, in that file at the commit that builds
the map. A pin on a seat branch is (rev, path, quote): the quote is digit-free, so that it is the same text with and
without main's mask, and it must occur in the file at that revision. `build_map.py` checks every pin.

Grades are kept apart, as the physical lane's work order asks:
  DERIVED       held on main's record as proved outright: a theorem or an exact computation whose truth rests on no
                premise of the programme (the map checks the citation, not the proof; Review 77, the reader)
  RECORD        a fact about the record's own state (a count, a status), checked at its source
  CONDITIONAL   proved on main given named premises, a tag or a numerical identification (its `requires` edges say which)
  POSTULATED    assumed by the foundation
  CHOSEN        a fork settled by choice, the alternative kept
  TAGGED        a tagged working postulate (the owner's ruling); results carry "given ..."
  FITTED        a continuous input fixed by looking at data
  ANSATZ        a posited form with no derivation
  UNSTATED      a commitment the construction makes without stating it (the framing ledger's word)
  READING       passes a sealed screen; not a prediction
  CONFIRMED     a registered falsifiable claim that observation has confirmed
  OPEN          not settled
  NEGATIVE      a banked negative, scoped
  LANE-REVIEWED a seat's proof with a non-authoring review inside its lane; not verified on main
  LANE-PROPOSED a seat's hand proof or count, unreviewed by its own label; not verified on main
  LANE-INPUT    an input the seat's own ledger prices as supplied, unselected or unearned
  DUTY          something the full goal requires and nobody has done
  CLOSURE       a cross-frame node of this map: one missing dependency under several names
"""

GEN = "GENESIS.md"
CLAIM = "docs/THE_CLAIM.md"
SCORE = "docs/TOTAL_INPUTS_SCOREBOARD.md"
TAU = "docs/THE_TAU_READOUT_RULE.md"
CARD = "docs/THE_SCALE_CARD_DESIGN_P722.md"
BANG = "docs/THE_BANG_PROGRAMME.md"
FRAME = "docs/THE_FRAMEWORK.md"
FALS = "docs/FALSIFIER_REGISTER.md"
REG = "docs/POINT_REGISTER.md"

AGY = "5242c938"                     # the agy lane's audit branch, as harvested at S306n
WEB = "195e8f1b"                     # the web seat's branch, as harvested at S306n
PHY = "521e6f241"                    # the physical lane's branch, as harvested at S306n
CAMP = "reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/"
PB = "reports/physical_bridge_2026_09_05/"

NODES = []


def N(id, layer, kind, grade, text, pins=(), rows=(), arcs=(), note=""):
    NODES.append(dict(id=id, layer=layer, kind=kind, grade=grade, text=text, pins=[list(p) for p in pins],
                      rows=list(rows), arcs=list(arcs), note=note))


# ------------------------------------------------------------------ layer 0: the principle
N("G:PF1", "0 principle", "premise", "POSTULATED", "Existence is what remains when cancelling to nothing cannot complete.",
  [(GEN, '| PF1 | what exists | "existence as a frustrated cancellation"')])
N("G:PF2", "0 principle", "premise", "POSTULATED", "The remainder is a description that cannot be exhausted. It does not follow from PF1.",
  [(GEN, "| PF2 | the form the remainder takes |"), (GEN, "PF2 does not follow from PF1 by any derivation in the record.")])
N("G:PF3", "0 principle", "premise", "POSTULATED", "The method: read that description as mathematical structure and ask what it forces.",
  [(GEN, "| PF3 | the method |")])
N("G:PF1-FORM", "0 principle", "reading", "CHOSEN", "PF1's mathematical form, non-cancellation as tr[a, b] ≠ 2, is a reading of the principle, not a derivation from it.",
  [(GEN, "PF1 has a mathematical form in the record, and it is a reading, not a derivation.")])

# ------------------------------------------------------------------ layer 1: the grammar
N("G:GM1", "1 grammar", "premise", "POSTULATED", "Two records. Equivalent to: the records have a non-trivial common character in SL(2, ℂ); not weaker than it.",
  [(GEN, "| GM1 | Two records: updates act on a pair of integer counts, ℤ² | **POSTULATED, in an equivalent form [v1.50]**"),
   (GEN, "Answered: equivalent, not weaker")], rows=["P-221", "P-211"], arcs=["B1677", "B1679", "B1682"])
N("G:GM2", "1 grammar", "premise", "POSTULATED", "The elementary updates are the unit shears L and R; descriptions are words in them.",
  [(GEN, "| GM2 | Unit shears: elementary updates are L and R; descriptions are words in them | POSTULATED |")])
N("G:GM3", "1 grammar", "premise", "POSTULATED", "The description is not periodic, so the monodromy is hyperbolic.",
  [(GEN, "| GM3 | Aperiodicity: the description is not periodic, so the monodromy is hyperbolic | POSTULATED (cheap) |")])
N("G:GM4", "1 grammar", "premise", "POSTULATED", "The carrier is the once-punctured torus. The puncture is conditional on faithful word data; faithfulness and the surface category stay premises.",
  [(GEN, "| GM4 | Carrier: words are realised as a mapping class of the once-punctured torus | POSTULATED, the puncture CONDITIONAL |"),
   (GEN, "so faithful word realisation and the surface category stay premises")], rows=["P-321"])
N("G:GM5a", "1 grammar", "premise", "POSTULATED", "Updates are reversible (GL(2, ℤ)).", [(GEN, "| GM5a | Reversible updates (GL(2,ℤ)) | POSTULATED |")])
N("G:GM5b", "1 grammar", "choice", "CHOSEN", "Inverse moves are legal: adopted by the owner's ruling, on a reading of PF1 chosen by the mathematics, not derived.",
  [(GEN, "| GM5b | Inverse moves are legal | **ADOPTED [v1.48]**"), (GEN, "A reading of PF1's cancelling chosen by the math, not a derivation.")], arcs=["B1662"])
N("G:GM5c", "1 grammar", "fork", "OPEN", "Is the record swap P a legal move? Open as a fork; the owner's ruling is 'even ticks observed': the observed weave is ⟨L, R⟩.",
  [(GEN, "| GM5c | The record swap P is a legal move | OPEN |"), (GEN, "GM5c: **even ticks observed**")], arcs=["B1607", "B1609", "B1610", "B1611"])
N("G:GM5d", "1 grammar", "choice", "CHOSEN", "Positivity: the choice of side of the mirror.",
  [(GEN, "| GM5d | Counts are non-negative (positivity) | CHOSEN |"), (GEN, "positivity becomes the choice of side, still CHOSEN")])

# ------------------------------------------------------------------ layer 2: the states and the root
N("G:XGEN", "2 states and root", "theorem", "DERIVED", "The generated state space: 758 signed word states to length 12, realising 536 manifolds.",
  [(GEN, "**Census** (DERIVED; re-derived by sm:B1516 C4 and C5)"), (GEN, "536 distinct manifolds")], arcs=["B1434", "B1439"])
N("G:XGEN-PHYS", "2 states and root", "gap", "OPEN", "Not derived: that every state occurs in one history, that the states are realised together, that any arrow is physical time.",
  [(GEN, "| Every legal state occurs in one history | NOT DERIVED |"), (GEN, "| Some arrow of X_gen is physical time | NOT DERIVED")])
N("G:SE1", "2 states and root", "premise", "POSTULATED", "The selection criterion: the root's first homology is torsion-free. Other criteria select other objects and are kept.",
  [(GEN, "| SE1 | **The selection criterion: the root's first homology is torsion-free.** | POSTULATED |")])
N("G:T-ROOT", "2 states and root", "theorem", "DERIVED", "What SE1 selects: exactly the class of LR (m004) and the class of the golden matrix LP (m000).",
  [(GEN, "So H₁ is torsion-free exactly for the class of LR (trace 3: **m004**) and the class of the golden matrix LP")], arcs=["B197"])
N("G:SE2", "2 states and root", "choice", "CHOSEN", "Orientation: of the two, take the orientable one, m004. The chain's most fragile link; eight walls pass through the amphichirality it brings.",
  [(GEN, "| SE2 | **Orientation**: of the two, take the orientable one, m004, the orientation double cover of m000 | CHOSEN |"),
   (GEN, "The most fragile link of the chain (fork FK2).")], arcs=["B1234"])
N("G:ROOT", "2 states and root", "theorem", "CONDITIONAL", "Given GM3, GM4, SE1 and SE2 the root is m004, the figure-eight knot complement. A conditional reconstruction of a chosen sector, not a derivation from nothing.",
  [(GEN, "Given GM3, GM4, SE1 and SE2, the root is m004, the figure-eight knot complement"),
   (GEN, "So the genesis is a conditional reconstruction of a chosen sector. It is not a derivation of m004 from nothing.")])

# ------------------------------------------------------------------ layer 3: the weave (the joint action of the moves)
N("W:Q8", "3 weave", "theorem", "DERIVED", "At two records the moves fix exactly two characters: the trivial one and the quaternion point; at three or more records, only the trivial one.",
  [(GEN, "at n = 2 the record's two moves fix exactly the trivial point and the quaternion point (0, 0, 0)")], arcs=["B1677", "B1679"])
N("W:T", "3 weave", "theorem", "DERIVED", "At the quaternion point the moves' lift is a three-dimensional representation, the triplet. That the records sit at that point is the grammar's premise, not this theorem's.",
  [(GEN, "the triplet follows from that point (T2)")])
N("W:G96", "3 weave", "theorem", "DERIVED", "The weave's group on T ⊕ T̄ has order 96; its generalized CP is the record swap, so CP is a symmetry exactly when the swap is a move.",
  [(GEN, "The weave's group G (the lifts of L and R on V = T ⊕ T̄, order 96)"), (GEN, "**So the weave's generalized CP is the record swap:**")], arcs=["B1611"])
N("W:HANDS", "3 weave", "theorem", "NEGATIVE", "Neither hand is derived on the weave: each is derived only on a subweave the weave does not select.",
  [(GEN, "**neither hand is derived on the weave**")], arcs=["B1607", "B1609", "B1610"])
N("W:MIRROR-EVEN", "3 weave", "theorem", "DERIVED", "A flat frame's count can tell a module from its dual but cannot see the hand: the class index is mirror-even for every module.",
  [(GEN, "what it cannot do is see the hand: the class index is mirror-even for every module (B1487, T1)")], arcs=["B1487"])
N("W:ONE-END", "3 weave", "theorem", "NEGATIVE", "A generated state has one end, and no generated state carries three generations in either counting frame, by counting ends.",
  [(GEN, "no state of X_gen carries three generations in either frame, by counting ends, not by search.")], arcs=["B1487"])
N("W:NOMOD", "3 weave", "theorem", "NEGATIVE", "The weave forces no fibre modulus: no point of the upper half-plane is fixed by every move.",
  [(GEN, "The weave forces no fibre modulus (no point of the upper half-plane is fixed by every move")], arcs=["B1617"])
N("W:NOVAL", "3 weave", "theorem", "NEGATIVE", "No parameter of the nineteen and no neutrino mass is a number of the weave's group; values need a forced modulus, dynamics or end data.",
  [(GEN, "no parameter of the nineteen, and no neutrino mass, is a number of the weave's group; values need a forced modulus, dynamics or end data")],
  arcs=["B1611", "B1612", "B1615", "B1616"])
N("TAG:LAMBDA", "3 weave", "premise", "TAGGED", "Λ, the dictionary's link, is a tagged working postulate: results computed with it carry 'given Λ'.",
  [(GEN, "FK11: **Λ a tagged working postulate**")])
N("TAG:UNIT", "3 weave", "premise", "TAGGED", "One unit of end data at the weave's cusp is a tagged working postulate; no datum the principle forces supplies it.",
  [(GEN, "One unit of end data at the weave's cusp is adopted as a working postulate, as Λ is"),
   (GEN, "nothing the principle forces visits the weave's cusp")], arcs=["B1629"])
N("W:INDEX3", "3 weave", "theorem", "CONDITIONAL", "Given Λ and the unit, the chiral three is a four-dimensional index (±3) on the weave's own surface.",
  [(GEN, "So, given Λ and the unit, the chiral three is an index, and FK11's earning condition is met conditionally.")], arcs=["B1632", "B1641"])

# the law, and what weighs the allowed (the owner, 2026-11-10; P-755)
N("W:LAW", "3 weave", "premise", "OPEN", "The law as the owner states it: if something is allowed to happen, it happens. On the record it is the weave's rule of method, and as a physical law a hypothesis to test, not a premise.",
  [(GEN, '"if it can happen it will" — plenitude, a hypothesis to test, not a premise'), ("docs/THE_WEAVE.md", "interaction between objects in relationship should produce reality, not single objects alone")],
  rows=["P-755", "P-756"])
N("W:MEASURE", "3 weave", "theorem", "DERIVED", "Run with nothing forced, the threads produce a definite measure for each way of counting them, and the measures differ: counted move by move the weight keeps out of the cusp; counted by geometric length it is hyperbolic area.",
  [("frontier/B1813_the_weaves_own_measure_depends_on_how_its_threads_are_counted/arc_verdict.json", "THE WEAVE'S OWN MEASURE DEPENDS ON HOW ITS THREADS ARE COUNTED")],
  rows=["P-437", "P-439"], arcs=["B1813"])
N("W:WALK", "3 weave", "theorem", "DERIVED", "The moves' own walk gives the move-by-move measure exactly (Minkowski's), singular to area, at every strength of the pull-back.",
  [("frontier/B1815_the_records_walk_has_minkowskis_exit_law_exactly/arc_verdict.json", "THE RECORD'S WALK HAS MINKOWSKI'S EXIT LAW, EXACTLY")], arcs=["B1815", "B1663"])
N("W:CLOCK", "3 weave", "choice", "CHOSEN", "The clock: whether the weave is counted by moves or followed by geometric length. Nothing on the record forces it.",
  [("frontier/B1815_the_records_walk_has_minkowskis_exit_law_exactly/arc_verdict.json", "The clock stays CHOSEN."), (REG, "is the weave's time the move count (discrete; the coding's maximal entropy) or the geodesic flow (continuous; Liouville)?")],
  rows=["P-439", "P-438"], arcs=["B1815"])
N("W:FLAT-SUM", "3 weave", "claim", "LANE-PROPOSED", "Any sum over all threads is mirror-even whatever its weights, and the democratic sum is flat by equidistribution; every other form selects only through a number it does not force. The SM seat's reading, read on main with its quotes checked.",
  [("docs/HARVEST_LEDGER.md", "any sum over all threads is mirror-even whatever its weights")], rows=["P-413"])
N("W:NO-ATOM", "3 weave", "theorem", "NEGATIVE", "Under the weave's uniform measure nothing the principle forces gives the cusp a weight: no atom. Scoped: other measures and other dynamics are not excluded.",
  [("frontier/B1629_does_the_principle_reach_the_weaves_cusp/arc_verdict.json", "nothing the principle forces visits the cusp")], arcs=["B1629"])
N("W:DRAW", "3 weave", "theorem", "NEGATIVE", "The measured six read as a draw from the weave's own measure: the sealed test does not separate the two clocks, and could not have; consistent, not specific.",
  [("frontier/B1814_the_measured_world_as_a_draw_from_the_weaves_own_measure/arc_verdict.json", "the six do not separate B1813's two clocks")], arcs=["B1814"])

# the forks and gaps not already above
N("G:FK2", "3 weave", "fork", "CHOSEN", "Orientation (SE2): what would settle it is a derived reason for orientability, or carrying both m004 and m000.",
  [(GEN, "| FK2 | Orientation (SE2) | CHOSEN |")])
N("G:FK3", "3 weave", "fork", "OPEN", "The swap P: a legal move, and of what type.", [(GEN, "| FK3 | The swap P: legal move, and of what type | OPEN |")])
N("G:FK5", "3 weave", "fork", "OPEN", "Faithful F₂ against its abelian quotient.", [(GEN, "| FK5 | Faithful F₂ against its abelian quotient (GM4) | OPEN |")], rows=["P-321"])
N("G:FK7", "3 weave", "fork", "OPEN", "The deck: gauged or kept.", [(GEN, "| FK7 | The deck: gauged or kept | OPEN |")])
N("G:FK8", "3 weave", "fork", "OPEN", "The join: which maps carry physical data between states.", [(GEN, "| FK8 | The join: which maps carry physical data between states | OPEN |")])
N("G:FK9", "3 weave", "fork", "OPEN", "Selection: what makes a state physical.", [(GEN, "| FK9 | Selection: what makes a state physical | OPEN |")])
N("G:FK10", "3 weave", "fork", "OPEN", "The end law. Open; the cusp's unit is tagged, not derived.", [(GEN, "| FK10 | The end law | OPEN")])
N("G:FK11", "3 weave", "fork", "OPEN", "The dictionary: unearned. Unearnable by derivation inside the flat counting frames on any thread or cover; earnable by sealed prediction within a frame.",
  [(GEN, "| FK11 | The dictionary (I-26) | UNEARNED"), (GEN, "UNEARNABLE within F-HE and F-CI on any thread or cover of a thread")], arcs=["B1604", "B1828"])
N("G:FK12", "3 weave", "fork", "OPEN", "The register: is the order-keeping register part of the state, carried by the act, or an input from outside?",
  [(GEN, "Is the register that keeps the order part of the state, carried by the act, or an input from outside?")])
N("G:FK13", "3 weave", "fork", "CHOSEN", "Which family is the object: ruled by argument from the principle (the word states it generates); revisable by a better argument.",
  [(GEN, "**[v1.13] RULED BY THE PRINCIPLE**")], arcs=["B1480"])
N("G:FK14", "3 weave", "fork", "OPEN", "The ends: does the genesis generate states with several ends, or are generations not ends?",
  [(GEN, "does the genesis generate states with several ends, or are generations not ends?")], arcs=["B1487", "B1491", "B1492"])
N("G:FK15", "3 weave", "fork", "OPEN", "The field's genesis: forced to exist, not forced which.",
  [(GEN, '"forced to exist, not forced which"')])
N("G:GAP1", "3 weave", "gap", "OPEN", "The dictionary: no frame is derived; until one is, a count is mathematics about a flat bundle.",
  [(GEN, "- **GAP1, the dictionary.** No frame is derived (I-26).")])
N("G:GAP2", "3 weave", "gap", "OPEN", "The ends: chiral counts live at cusps and depend on an end condition that is chosen.",
  [(GEN, "- **GAP2, the ends.** Chiral counts live at cusps")])
N("G:GAP3", "3 weave", "gap", "OPEN", "The source: chirality sits on non-split bundles, which carry no harmonic metric without a source; no report derives the source.",
  [(GEN, "- **GAP3, the source.** Chirality sits on non-split bundles"), (GEN, "No report derives the source.")])
N("G:GAP4", "3 weave", "gap", "OPEN", "Selection and coincidence: a selection rule and a null model must be fixed before a match counts; nothing on the record clears the bar.",
  [(GEN, "- **GAP4, selection and coincidence.**"), (GEN, "Nothing in the record clears it")])
N("G:GAP5", "3 weave", "gap", "OPEN", "Dynamics: nothing on the record has been turned into a potential, a breaking or a running that fixes a value.",
  [(GEN, "- **GAP5, dynamics.** Topology yields integers and discrete structure."),
   (GEN, "none of it has been turned into a potential, a breaking or a running that fixes a value")], rows=["P-138"])
N("G:GAP6", "3 weave", "gap", "OPEN", "The flatness: a flat frame reaches discrete data through the boundary and cannot reach continuous moduli.",
  [(GEN, "GAP6, the flatness.** Every frame on this page is a frame of flat bundles")])

# ------------------------------------------------------------------ layer 4: the structural theorem (the McKay cascade on the root)
N("MC:HYP", "4 structure", "premise", "POSTULATED", "The structural theorem's counted inputs: the uniqueness axioms and five typed external data (two bits, one scale, one Lie type, one closing direction).",
  [(CLAIM, "plus **five** typed external data")], rows=["P-374"], note="P-374: the typed-data counts are owed a re-read; the page flags one input as a superseded count still counting.")
N("MC:PRICE", "4 structure", "premise", "POSTULATED", "The identification price: thirteen (four axioms and nine irreducible sources).",
  [(SCORE, "**The identification price:** 13")], arcs=["B1266"])
N("MC:ALG", "4 structure", "theorem", "CONDITIONAL", "The gauge algebra su(3) ⊕ su(2) ⊕ u(1)³.", [(CLAIM, "the gauge algebra su(3)⊕su(2)⊕u(1)³")], arcs=["B892", "B992"])
N("MC:Z6", "4 structure", "theorem", "CONDITIONAL", "The global form [SU(3) × SU(2) × U(1)]/ℤ₆, at the primitive normalisation of hypercharge only.",
  [(CLAIM, "the **global form [SU(3)×SU(2)×U(1)]/ℤ₆**"),
   ("frontier/B1221_global_form_path_independence/ADDENDUM_2026-08-31_the_Z6_needs_primitivity.md", "|kernel| = 6 exactly when k = 1")],
  rows=["P-604", "P-581"], arcs=["B862", "B1221"], note="P-604 (closed at S306n): the kernel is cyclic of order 6k. P-581: the comparison class of this grade is owed.")
N("MC:Y", "4 structure", "theorem", "CONDITIONAL", "The hypercharge direction; its normalisation is underivable by homogeneity.", [(CLAIM, "the hypercharge **direction** (b = c = 0 forced")], arcs=["B864", "B991"])
N("MC:END", "4 structure", "theorem", "CONDITIONAL", "The cascade terminates, and every registered selection function ends at the same algebra.",
  [(CLAIM, "termination of the cascade"), (CLAIM, "endpoint **rule-independence**")], arcs=["B863", "B994"])
N("MC:CUBIC", "4 structure", "theorem", "CONDITIONAL", "Matter mass sits in the cubic of the 27.", [(CLAIM, "matter mass in the **cubic**")], arcs=["B978", "B884", "B987"])
N("MC:GEN", "4 structure", "gap", "OPEN", "The generation count is not an output of the structural theorem; it sits on the open-inputs side.",
  [(CLAIM, "the generation COUNT returns to the open-inputs side")], rows=["P-606"], arcs=["B1033"],
  note="P-606: B298's 'a degree-2 trace field means multiplicities in {1, 2}, never 3' is false as an implication and is still cited as prior.")
N("MC:CS0", "4 structure", "theorem", "DERIVED", "For m004 the Chern–Simons invariant is zero, so its complex volume is real. This is a fact about this object, not a symmetry theorem: m003 is amphichiral with the other value. The step from it to physics is withdrawn.",
  [(CLAIM, "**no dimensionful quantity — by theorem, not failure**"), (CLAIM, "this is NOT a symmetry theorem"),
   (FALS, "the mathematics CS = 0 stands")], arcs=["B811", "B1012", "B1226", "B1009"])
N("MC:GENERIC", "4 structure", "theorem", "DERIVED", "Reaching the E₆ waypoint is generic (about one manifold in three), so arriving there confirms nothing.",
  [(CLAIM, "is *generic* — ~1 in 3 manifolds, 5 of 7 grammars")], arcs=["B993", "B996"])
N("MC:UNIQ", "4 structure", "theorem", "DERIVED", "The own-conductor door set of the metallic grammars is {1, 4}. The golden is unique among primitive grammars, and unique for having both the door and a quotient of π₁ onto 2T.",
  [("frontier/B1859_the_door_set_is_one_and_four/FINDINGS.md", "**The door set is {1, 4}, for every m**"), (CLAIM, "CORRECTED 2026-11-10 (B1859)")],
  rows=["P-318", "P-618"], arcs=["B1859", "B997", "B1019"],
  note="Corrected at B1859: the claim page had said the golden is the unique metallic grammar with the door; B997 had bounded the ambient group, not the generated one.")
N("MC:REACH", "4 structure", "gap", "OPEN", "The structural frame has never been computed on any state other than the root.",
  [(GEN, "Never computed on another word state.")])

# ------------------------------------------------------------------ layer 5: the values (frame A, the record's candidate)
N("V:0OF19", "5 values", "record", "RECORD", "The scoreboard: no Standard Model parameter is earned.", [(SCORE, "0 of 19 earned"), (GEN, "any Standard-Model parameter (**0 of 19**)")], rows=["P-579"])
N("V:SIX", "5 values", "reading", "READING", "The six mass ratios at the principled end pass a sealed screen. A level-1 reading: the quark four are not specific, and on its line the leptons are the down sector.",
  [(SCORE, "a level-1 READING (B1841 PROVED as sealed; B1839 NEGATIVE)"), (SCORE, "the frame's quark four alone are not specific")],
  rows=["P-706", "P-355", "P-384", "P-586", "P-596"], arcs=["B1841", "B1839"])
N("V:HELD", "5 values", "choice", "CHOSEN", "The held-out targets are held unspent by the owner. Nothing in this map reads or computes them.",
  [(SCORE, "the held-out targets are HELD by the owner (P-709)")], rows=["P-709", "P-585", "P-597"])
N("V:EARN-RULE", "5 values", "choice", "CHOSEN", "How a frame's dictionary may be earned: by sealed prediction, with seven conditions. The owner's ruling, on main's drafting; revisable.",
  [(GEN, "A DICTIONARY MAY BE EARNED BY PREDICTION")], arcs=["B1828", "B1843"])
N("V:WALL", "5 values", "theorem", "NEGATIVE", "The value layer was tested under seal twice, with demonstrated power the second time, and is null.",
  [(CLAIM, "**one wall is real: the value layer**")], arcs=["B915", "B925", "B929", "B1006"])

# ------------------------------------------------------------------ layer 6: the modulus tau and its read-out
N("T:RULE", "6 tau", "theorem", "CONDITIONAL", "Granted the framing, τ at a point of the circle is the conformal modulus of the fibre at that point of the metric's own clock.",
  [(TAU, "**τ at a point of the circle is the conformal modulus of the fibre at that point of the metric's own clock.**")], rows=["P-714", "P-727"], arcs=["B1846", "B1847"])
N("T:FRAMING", "6 tau", "choice", "CHOSEN", "The framing: the metric's fibration is the structure read. Set by the goal, not derived; other structures give other readings.",
  [(TAU, "The framing itself is CHOSEN."), (TAU, "four choices remain, not three")], rows=["P-726", "P-714"])
N("T:POINT-WEIGHT", "6 tau", "choice", "CHOSEN", "Point or weight: the metric supplies both a canonical point (the systole) and a canonical weight; which the read-out uses is a choice.",
  [(TAU, "Which one the read-out uses is the choice P-726")], rows=["P-726", "P-744"])
N("T:CHARGE5", "6 tau", "choice", "CHOSEN", "The charge premise at level 5, which fixes the depth of the one departure.",
  [(TAU, "the charge premise at 5 (B1853)")], rows=["P-717", "P-738"], arcs=["B1853", "B1855", "B1856"])
N("T:MINIM", "6 tau", "choice", "CHOSEN", "Minimisation as the use of the action.", [(TAU, "minimisation as the use of the action (B1853)")], arcs=["B1853"])
N("T:RE", "6 tau", "theorem", "CONDITIONAL", "The two σ-fixed fibres carry involutions of opposite class, exactly; which of them is the tube is fixed by numerics (B1847's anti-apex at Re ½ to 7 × 10⁻⁷, against the alternatives 0 and ½). Given that, the tube's level surface has Re τ = 0; the Teichmüller apex of the same word also lies on Re 0.",
  [(TAU, "**The real part is exact, by topology** (B1852)."),
   ("frontier/B1852_the_tubes_real_part_by_topology/FINDINGS.md", "So the apex and the metric's reading lie on the same line Re 0, and differ in height only"),
   ("frontier/B1852_the_tubes_real_part_by_topology/verification/fixed_fibre_classes.py", "is not decided by this algebra")],
  rows=["P-751"], arcs=["B1852"])
N("T:IM", "6 tau", "claim", "LANE-PROPOSED", "The value under the rule at the point reading: Im τ about 6.065 in the long-history limit. The web seat's sealed estimate; main's own value at k = 2 agrees with the seat's within main's scatter of about 0.02, and main has no value beyond k = 2.",
  [(TAU, "Main's own instrument stops at k = 2"), (WEB, "relays/chat1_2026-11-07_tau/taumore_summary_out.txt", "firmed: Im tau_inf")],
  rows=["P-739"], arcs=["B1854"])
N("T:PRICED", "6 tau", "duty", "DUTY", "The candidate τ is not yet priced by the random-subset control, and is read against the six only inside a sealed card.",
  [(TAU, "priced by the random-subset control")], rows=["P-714", "P-708"])
N("T:NO-PLACE", "6 tau", "theorem", "NEGATIVE", "Nothing on the record places Im τ: the object's action is linear, and its one phase transition has no scale.",
  [(BANG, "nothing places Im τ"), (BANG, "**P-713 DONE, NEGATIVE for placing τ:**")], rows=["P-713"], arcs=["B1341", "B852", "B1813"])

# ------------------------------------------------------------------ layer 7: the scale
N("SC:UNIT", "7 scale", "theorem", "NEGATIVE", "An absolute energy cannot come from the object, whose invariants carry no unit; any theory needs one outside unit. Main's re-reading of two negative arcs.",
  [(REG, "An ABSOLUTE energy cannot come from the object")], rows=["P-719"], arcs=["B151", "B660"])
N("SC:RATIO", "7 scale", "gap", "OPEN", "A dimensionless ratio of scales is not excluded; it waits on a principle that fixes the level and on an identification.",
  [(REG, "NOT excluded by the record; what is missing is a principle that fixes the level")], rows=["P-719", "P-721"])
N("SC:R2", "7 scale", "choice", "CHOSEN", "Reading the exact block as a ratio of scales is an identification; the record holds no object-side reason for it.",
  [(CARD, "The record holds no object-side reason that R2's block is a ratio of two scales."), (CARD, "The reading of the block as a ratio of scales (R2's identification).")], rows=["P-722"])
N("SC:R4", "7 scale", "choice", "CHOSEN", "The content that runs is the Standard Model's, borrowed.", [(CARD, "R4, the content that runs.")], rows=["P-722"])
N("SC:PREMISE", "7 scale", "choice", "CHOSEN", "The chiral premise under which the scale card takes a single block.", [(CARD, "The chiral premise itself (B1012 ruling, point 2).")], rows=["P-731"])
N("SC:CARD", "7 scale", "theorem", "NEGATIVE", "The scale card is not sealable: more than one step is chosen.", [(CARD, "**So the card is not sealable.**")], rows=["P-732", "P-722"])

# ------------------------------------------------------------------ layer 8: the lanes' conditional model (E8 on the punctured elliptic curve)
LEDG = CAMP + "INPUT_LEDGER.md"
DEPS = CAMP + "CLAIM_DEPENDENCIES.md"
MANI = CAMP + "MODEL_MANIFEST.md"
N("E:L01", "8 conditional model", "model-input", "LANE-INPUT", "The surface-group carrier: a faithful free register on two letters, realised on the once-punctured torus. Its necessity from non-cancellation is open.",
  [(AGY, LEDG, "necessity from noncancellation remains open")])
N("E:L02", "8 conditional model", "model-input", "LANE-INPUT", "The parent: a compact E₈ gauge theory with a curved functional on the internal surface. Supplied, not earned.",
  [(AGY, MANI, "Explicitly **SUPPLIED**"), (AGY, LEDG, "source-checked covariance+unreviewed")])
N("E:L03", "8 conditional model", "model-input", "LANE-INPUT", "The quaternion flavour holonomy and its lift to the parent, with core signs unselected.",
  [(AGY, LEDG, "unexecuted finite-group/root-table derivation")])
N("E:L04", "8 conditional model", "model-input", "LANE-INPUT", "The modulus, the cusp metric, one length and one coupling: all unselected; the source keeps both the length and the coupling unreduced.",
  [(AGY, LEDG, "current source retains both")])
N("E:L05", "8 conditional model", "model-input", "LANE-INPUT", "The odd spin structure and the compensating lifts: conditional reductions, with the spin class and the lift unselected.",
  [(AGY, LEDG, "unreviewed conditional reductions")])
N("E:L06", "8 conditional model", "model-input", "LANE-INPUT", "The split of the parent, the coherent alternatives and the charges; the physical read-out of colour and electromagnetism is an unearned identification.",
  [(AGY, LEDG, "physical EM/colour readout")])
N("E:L07", "8 conditional model", "model-input", "LANE-INPUT", "The balanced background and the trivial Wilson line: unselected branch data; no selection law.",
  [(AGY, LEDG, "unselected branch data")])
N("E:L08", "8 conditional model", "claim", "LANE-REVIEWED", "The end law and the half-root sector's coercivity: reviewed inside the lane with one code gap open; the later counts are unreviewed.",
  [(AGY, LEDG, "are unreviewed author candidates")])
N("E:L09", "8 conditional model", "claim", "LANE-PROPOSED", "The four-slot mass map and the gauge-parameter operator: source-checked, the full transport unreviewed.",
  [(AGY, LEDG, "full curve transport unreviewed")])
N("E:L10", "8 conditional model", "claim", "LANE-PROPOSED", "The matter multiplicities: three coefficients per representation, as candidate counts; their reading as families is an unearned identification.",
  [(AGY, LEDG, "physical family identification")])
N("E:L11", "8 conditional model", "claim", "LANE-PROPOSED", "The charged vectors come as a pair with left and right currents of equal size; a mechanism that breaks that parity is open.",
  [(AGY, LEDG, "derive a mechanism breaking left/right weak-current parity")])
N("E:L12", "8 conditional model", "claim", "LANE-PROPOSED", "Small cyclic deformations do not split the pair; vacuum and scale selection, gravity and the observer are open in this model.",
  [(AGY, LEDG, "small cyclic spin deformations alone do not split")])
N("E:Q1", "8 conditional model", "gap", "OPEN", "The lanes' first question: what suppresses the right-handed current?", [(AGY, LEDG, "suppresses the right-handed current witness")])
N("E:Q2", "8 conditional model", "gap", "OPEN", "Their second: the weak-current map, the neutral partners, chirality despite a zero net index, the Yukawa couplings, anomaly cancellation.",
  [(AGY, LEDG, "physical chirality despite zero net EM index")])
N("E:Q3", "8 conditional model", "gap", "OPEN", "Their third: what confines the continuum, reduces the length and coupling to one anchor, and selects the surface, modulus, spin class and background.",
  [(AGY, LEDG, "What mechanism confines/decouples the zero-angular")])
N("E:J1", "8 conditional model", "missing-join", "OPEN", "Missing join: an independently certified complete three-family matter roster.",
  [(AGY, DEPS, "Independently Certified Complete Three-Family Matter Roster")])
N("E:J2", "8 conditional model", "missing-join", "OPEN", "Missing join: the certified physical charged-current coupling matrix.",
  [(AGY, DEPS, "Certified Physical $W^\\pm$ Coupling Matrix")])
N("E:J3", "8 conditional model", "missing-join", "OPEN", "Missing join: an independent review of the kernel theorem in the background without the extra Wilson line.",
  [(AGY, DEPS, "Half-Root Kernel Theorem and Global All-Sector Consistency")])
N("E:J4", "8 conditional model", "missing-join", "OPEN", "Missing join: chiral against vector-like. The kernel splits equally between conjugate representations.",
  [(AGY, DEPS, "Three Chiral Standard Model Families with Nonzero Low-Energy Charged Fermion Masses")])
N("E:J5", "8 conditional model", "missing-join", "OPEN", "Missing join: the map from the register to the fields' family structure.",
  [(AGY, DEPS, "Physical Register-to-Field Family Map")])
N("E:GRADES", "8 conditional model", "record", "RECORD", "The lanes' own grading: independent proof support, execution readiness, execution and banking are different facts; nothing of this model is banked on main.",
  [(PHY, PB + "PROGRESS_SINCE_MAIN_217E_2026_11_08.md", "Independent proof support, execution readiness, actual execution and"),
   (AGY, MANI, "Nothing in this manifest promotes an imported or reported statement to a newly verified physical result.")],
  rows=["P-746", "P-749", "P-750", "P-752"])

# ------------------------------------------------------------------ layer 9: gravity
N("GR:ACTION", "9 gravity", "theorem", "DERIVED", "The object's own 2+1-dimensional gravity: an exact vacuum solution with a one-term action and, with Λ = −1 forced, no free dimensionless constant. A fact about this construction.",
  [(FRAME, "**The action (C1, B1088) has zero free dimensionless constants.**"), (FRAME, "one term.**"),
   (FRAME, "a mathematical fact about this one construction, not a claim, anywhere in this section,")], arcs=["B1088", "B1090", "B259"])
N("GR:VECTORLIKE", "9 gravity", "theorem", "NEGATIVE", "The matter of that theory, read in 2+1 dimensions, is vector-like by theorem.",
  [(FRAME, "read as a 2+1-dimensional theory, is vector-like by theorem")], arcs=["B1089"])
N("GR:3PLUS1", "9 gravity", "duty", "DUTY", "A dynamical 3+1-dimensional metric coupled to the same matter: not on the record, in any lane.",
  [(PHY, PB + "SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md", "Gravity and cosmology: dynamical")])

# ------------------------------------------------------------------ layer 10: cosmology
N("CO:S12", "10 cosmology", "theorem", "DERIVED", "Two of the three preconditions for a matter asymmetry stand as structure, and as preconditions only.",
  [(BANG, "stands, as preconditions only")], rows=["P-712"], arcs=["B867"])
N("CO:S3", "10 cosmology", "theorem", "NEGATIVE", "The third precondition, a departure from equilibrium, is not established: the cubic once read as a barrier has no double well.",
  [(BANG, "**not established as a transition.**")], rows=["P-712", "P-716"], arcs=["B295", "B1341"])

# ------------------------------------------------------------------ layer 11: predictions and falsifiers
N("PR:P2", "11 predictions", "prediction", "CONFIRMED", "Charge quantisation: the register's one earned confirmation, and not unique to the framework.",
  [(FALS, "**YES — the register's one earned confirmation**")])
N("PR:P3", "11 predictions", "prediction", "OPEN", "The global form: untested, since no monopole exists to test it.", [(FALS, "UNTESTED — no monopole exists to test it")])
N("PR:P9", "11 predictions", "prediction", "CONDITIONAL", "The extra neutral boson of the closing is not gaugeable on a chiral spectrum as it stands: the programme cannot hold both.",
  [(GEN, "**On a chiral spectrum U1-Z′₉ is not gaugeable as it stands**")], arcs=["B1340", "B1303"])
N("PR:P10", "11 predictions", "prediction", "OPEN", "The weave's one numerical forward prediction is live; its sibling reading was falsified. No value is read here.",
  [(FALS, "the first entry with a numerical forward prediction"), (FALS, "**FALSIFIED 2026-10-24 (B1756)**")], rows=["P-157"], arcs=["B1612", "B1613", "B1756"])

# ------------------------------------------------------------------ layer 12: the shared block of both value frames
# (S01, S02, A01..A12 and the forced joints F1..F7 are added by build_map.py from docs/total_inputs_scoreboard.json)

# ------------------------------------------------------------------ layer 13: the completion duties (the physical lane's checklist)
CHK = PB + "SM3_AND_GRAVITY_COMPLETION_CHECKLIST_2026_11_08.md"
for i, (name, quote) in enumerate([
        ("Operational foundations: the register data, compositions, equivalences and observables, complete relative to the grammar.", "Operational foundations: precise distinction/register data"),
        ("The physical dictionary: derive or price spacetime, fields, gauge algebra, representations, norms and statistics.", "Physical dictionary: derive or price spacetime, fields, gauge algebra"),
        ("Common dynamics: one globally stationary construction from one action, with positive norms and complete domains.", "Common dynamics: a globally stationary core and end from the same action"),
        ("The boundary and source law: the full non-linear response, not a selected amplitude or projector.", "Boundary/source law: full nonlinear response including Gauss terms"),
        ("The gauge and Higgs sector: the actual interactions, charge normalisation, global structure and a controlled Higgs phase.", "actual colour and electroweak interactions"),
        ("The spectrum: all fermions, exactly three complete chiral families, from the actual operator and domain.", "all charged and neutral fermions, exactly three complete chiral families"),
        ("Normalised interactions: the real left and right weak currents, Yukawa couplings and kinetic normalisation.", "Normalized interactions: calculate the real left/right weak currents"),
        ("Quantum consistency: anomalies, inflow, a positive state space and unitary evolution.", "Quantum consistency: perturbative gauge and mixed gravitational anomalies"),
        ("Full mode accounting: conjugates, mirror partners, extra modes, towers and continua, with thresholds or decoupling.", "Full mode accounting: charge conjugates, mirror partners"),
        ("Quantitative particle physics: couplings, the Higgs potential, masses, mixing and CP, neutrinos, with running and uncertainty.", "Quantitative particle physics: normalized couplings, Higgs potential"),
        ("Gravity and cosmology: a dynamical 3+1 geometry coupled to the same matter.", "Gravity and cosmology: dynamical"),
        ("Selection and input reduction: derive the carrier, metric, holonomy, state and measure, or prove the residual freedom.", "Selection and input reduction: derive needed carrier, metric, holonomy"),
        ("Predictivity: fixed-prescription comparisons not used to select or calibrate the model.", "Predictivity: fixed-prescription observable comparisons"),
        ("Evidence: non-authoring review, acceptance, admitted reproducible execution and preserved failures.", "Evidence: source-complete nonauthoring review")], 1):
    N("D:%02d" % i, "13 duties", "duty", "DUTY", name, [(PHY, CHK, quote)])

# ------------------------------------------------------------------ layer 14: the closure nodes (one missing dependency under several names)
N("X:HAND", "14 closure", "closure", "CLOSURE", "THE HAND. What makes a count chiral. Every branch meets it: the weave derives neither hand, the flat index is mirror-even, the 2+1 matter is vector-like, and the lanes' model has paired left and right currents.")
N("X:TAU", "14 closure", "closure", "CLOSURE", "THE MODULUS. What fixes τ. Fitted in both value frames, unselected in the lanes' model, forced by nothing on the weave; a rule exists that is conditional on a chosen framing and three further choices.")
N("X:END", "14 closure", "closure", "CLOSURE", "THE END. The law at the cusp. Tagged on the weave, chosen in the value frame, a conditional reduction in the lanes' model.")
N("X:DICT", "14 closure", "closure", "CLOSURE", "THE DICTIONARY. Which mathematical object is which field. Unearned everywhere; unearnable by derivation inside the flat counting frames; earnable by sealed prediction.")
N("X:PARENT", "14 closure", "closure", "CLOSURE", "THE PARENT. Where the gauge algebra comes from. Supplied in the lanes' model; adopted by a ruling as a container on main; one of five typed inputs of the structural theorem.")
N("X:SCALE", "14 closure", "closure", "CLOSURE", "THE SCALE. One outside unit is unavoidable; every dimensionless ratio of scales still waits on a level and an identification.")
N("X:SELECT", "14 closure", "closure", "CLOSURE", "THE SELECTION. What makes a state, a line or a background the physical one. A postulate at the root, open above it, unselected data in the lanes' model.")
N("X:SOURCE", "14 closure", "closure", "CLOSURE", "THE DYNAMICS. A potential, a breaking, a running or a source that fixes a value. Structure exists; nothing has been turned into one.")
N("X:FLAT", "14 closure", "closure", "CLOSURE", "THE FLATNESS. Both value frames stand on a flat bundle, which cannot reach continuous moduli.")
N("X:GRAVITY", "14 closure", "closure", "CLOSURE", "GRAVITY IN 3+1. Not on the record in any lane.")
N("X:WEIGHT", "14 closure", "closure", "CLOSURE", "THE WEIGHT. If everything allowed happens, how much of each. The law fixes what exists and not its weight; a thread picked by hand and a flat average are the two ways of supplying the weight without deriving it.")

# ------------------------------------------------------------------ the edges
EDGES = []


def E(a, kind, b, grade="", note=""):
    EDGES.append(dict(src=a, kind=kind, dst=b, grade=grade, note=note))


# the foundation's chain
for p in ("G:GM3", "G:GM4", "G:SE1", "G:SE2"):
    E("G:ROOT", "requires", p, "CONDITIONAL", "four inputs suffice, and each is needed")
E("G:T-ROOT", "applies-under", "G:SE1", "", "the theorem says what the criterion selects; it does not need the criterion to be adopted")
for p in ("G:GM2", "G:GM4", "G:GM5b", "G:GM5d"):
    E("G:XGEN", "applies-under", p, "", "the census counts what the grammar defines")
E("G:PF1-FORM", "reads", "G:PF1", "CHOSEN")
E("G:GM1", "reads", "G:PF1-FORM", "CHOSEN", "the common character is PF1's commutator only through a rank-free reading of PF1, which is not on the record")
E("W:Q8", "applies-under", "G:GM1", "", "a theorem about two letters and the two moves; the programme uses it under GM1")
E("W:Q8", "applies-under", "G:GM2", "", "the moves are the unit shears")
E("W:T", "requires", "W:Q8", "DERIVED")
E("W:G96", "requires", "W:T", "DERIVED")
E("W:INDEX3", "requires", "W:T", "CONDITIONAL")
E("W:INDEX3", "requires", "TAG:LAMBDA", "CONDITIONAL")
E("W:INDEX3", "requires", "TAG:UNIT", "CONDITIONAL")
E("W:INDEX3", "requires", "G:GM5c", "CONDITIONAL", "on the double-tick weave, where the swap is not a move")
E("W:HANDS", "requires", "G:GM5c", "NEGATIVE")
E("W:HANDS", "bears-on", "G:SE2", "NEGATIVE", "the three's hand is the sheet of the orientation double cover, SE2's kind of choice; the weave's negative does not rest on it (first written as 'requires', and refused by the weave-or-thread check)")
E("TAG:UNIT", "answers", "G:FK10", "TAGGED")
E("TAG:LAMBDA", "answers", "G:FK11", "TAGGED")
E("G:SE2", "answers", "G:FK2", "CHOSEN")
E("G:GM5c", "answers", "G:FK3", "OPEN")
E("G:GM4", "answers", "G:FK5", "OPEN")
# the structural theorem
for t in ("MC:ALG", "MC:Z6", "MC:Y", "MC:END", "MC:CUBIC"):
    E(t, "requires", "G:ROOT", "CONDITIONAL")
    E(t, "requires", "MC:HYP", "CONDITIONAL")
    E(t, "requires", "MC:PRICE", "CONDITIONAL")
E("MC:CS0", "applies-under", "G:SE2", "", "amphichirality puts the invariant in a two-element set; this object sits at zero")
E("MC:UNIQ", "bears-on", "MC:GENERIC", "DERIVED", "the door is a shadow of the grammar's letters; the E₆ entry is a quotient of π₁; reaching E₆ is generic")
# the values
E("V:SIX", "requires", "TAG:LAMBDA", "READING", "the frame's coupling is banked 'given Λ, the dictionary'")
E("FA:F1", "requires", "TAG:LAMBDA", "CONDITIONAL", "banked 'given Λ, the dictionary'")
E("FA:F1", "requires", "W:Q8", "CONDITIONAL", "the frame's doublet is the fibre's rank-two flat bundle with quaternion monodromy")
E("FA:F1", "requires", "G:GM4", "CONDITIONAL", "the fibre is the once-punctured torus")
# what each of the other forced-by-main joints is conditional on, from the scoreboard's own basis cell. Added 2026-11-10 with B1861, whose builder
# found eight CONDITIONAL nodes that named no premise; build_map.py now refuses a conditional result with none.
E("FA:F2", "requires", "TAG:LAMBDA", "CONDITIONAL", "the hypercharge dictionary is banked 'given Λ, the dictionary'")
E("FA:F3", "applies-under", "B:FRAME", "", "'given the direction': a proved identity about a direction the agy lane chose")
E("FA:F4", "applies-under", "A:A07", "", "the theorem fixes L_2 as a function of τ; which canonical horocycle is the end is the frame's choice")
E("FA:F5", "applies-under", "G:ROOT", "", "an exact value of the root's volume, shared by its whole shape-field family (B1136); using it presumes the root")
E("FA:F6", "applies-under", "MC:HYP", "", "the normalisation is fixed once the Lie type and the closing direction are given")
E("FA:F7", "applies-under", "A:A04", "", "'given a mirror-invariant radius and the Higgs condition': proved for the census directions and DR")
E("FA:F7", "applies-under", "A:A07", "", "the mirror-invariant radius is the end's")
E("PR:P9", "applies-under", "MC:HYP", "", "the boson is the closing direction's, one of the structural theorem's typed external data")
E("FL:20", "requires", "V:EARN-RULE", "CONDITIONAL", "the route by sealed prediction exists by the ruling of 2026-11-03, and only by it")
E("V:SIX", "blocked-by", "V:HELD", "", "no held-out target is spent, so nothing is predicted")
E("V:0OF19", "follows-from", "V:SIX", "DERIVED", "a reading earns nothing")
# tau
for c in ("T:FRAMING", "T:POINT-WEIGHT", "T:CHARGE5", "T:MINIM"):
    E("T:IM", "requires", c, "CONDITIONAL")
E("T:RULE", "requires", "T:FRAMING", "CONDITIONAL")
E("T:RULE", "requires", "G:GM4", "CONDITIONAL", "the fibre and its mapping torus")
E("T:RULE", "requires", "G:GM2", "CONDITIONAL", "the history is a word in the two letters")
E("T:IM", "requires", "T:RULE", "CONDITIONAL")
E("T:IM", "requires", "T:PRICED", "DUTY")
E("T:RE", "requires", "T:RULE", "DERIVED")
# the scale
for c in ("SC:R2", "SC:R4", "SC:PREMISE"):
    E("SC:CARD", "requires", c, "NEGATIVE")
E("SC:RATIO", "requires", "SC:R2", "OPEN")
# the lanes' model: what each entry is, in main's terms
E("E:L01", "same-as", "G:GM1", "", "the free register on two letters")
E("E:L01", "same-as", "G:GM4", "", "the once-punctured torus as carrier")
E("E:L03", "same-as", "W:Q8", "", "the quaternion flavour holonomy is the weave's common point")
E("E:L10", "candidate-for", "W:T", "", "three coefficients per representation against the weave's triplet: the register-to-field map is the lanes' missing join")
E("E:J5", "candidate-for", "W:T", "OPEN")
for a, b in (("E:J1", "D:06"), ("E:J2", "D:07"), ("E:J4", "D:06"), ("E:J5", "D:01"), ("E:J3", "D:14"), ("E:Q1", "D:07"), ("E:Q2", "D:08"), ("E:Q3", "D:12")):
    E(a, "blocks", b, "OPEN")
for a in ("E:L08", "E:L09", "E:L10", "E:L11", "E:L12"):
    for p in ("E:L01", "E:L02", "E:L03", "E:L04", "E:L05", "E:L06", "E:L07"):
        E(a, "requires", p, "LANE-INPUT")

# the closure nodes: what is the same missing thing under several names
MEMBERS = {
    "X:HAND": ["G:SE2", "G:FK2", "G:GM5c", "G:FK3", "W:HANDS", "W:MIRROR-EVEN", "W:INDEX3", "G:GAP6", "GR:VECTORLIKE", "E:L11", "E:J4", "E:Q1", "PR:P9", "SC:PREMISE", "S:S02", "FL:03"],
    "X:TAU": ["W:NOMOD", "T:FRAMING", "T:POINT-WEIGHT", "T:CHARGE5", "T:MINIM", "T:IM", "T:PRICED", "T:NO-PLACE", "E:L04", "A:A01", "FL:04"],
    "X:END": ["G:FK10", "G:GAP2", "TAG:UNIT", "G:FK14", "W:ONE-END", "E:L08", "A:A07", "A:A09", "FL:11"],
    "X:DICT": ["G:FK11", "G:GAP1", "TAG:LAMBDA", "MC:PRICE", "G:FK15", "E:L06", "E:L10", "E:J5", "A:A05", "FL:01", "FL:09", "FL:10", "FL:20"],
    "X:PARENT": ["E:L02", "MC:HYP", "MC:UNIQ", "MC:REACH"],
    "X:SCALE": ["SC:UNIT", "SC:RATIO", "SC:R2", "SC:R4", "SC:CARD", "MC:CS0", "E:L04", "A:A12", "FL:13", "FL:21"],
    "X:SELECT": ["G:FK9", "G:GAP4", "G:SE1", "G:XGEN-PHYS", "E:L07", "E:Q3", "A:A02", "A:A03", "A:A04", "A:A11", "FL:07", "FL:08", "FL:18"],
    "X:SOURCE": ["G:GAP3", "G:GAP5", "T:NO-PLACE", "CO:S3", "W:NOVAL", "A:A08", "A:A10", "FL:05", "FL:06", "FL:12"],
    "X:FLAT": ["S:S01", "G:GAP6", "FL:02"],
    "X:GRAVITY": ["GR:ACTION", "GR:3PLUS1"],
    "X:WEIGHT": ["W:LAW", "W:MEASURE", "W:WALK", "W:CLOCK", "W:FLAT-SUM", "W:NO-ATOM", "W:DRAW", "G:XGEN-PHYS", "T:POINT-WEIGHT", "T:MINIM", "FL:27"],
}
for x, ms in MEMBERS.items():
    for m in ms:
        E(m, "instance-of", x, "", "")

# what each closure node blocks among the completion duties
BLOCKS = {
    "X:HAND": ["D:06", "D:07", "D:08"],
    "X:TAU": ["D:10", "D:12"],
    "X:END": ["D:03", "D:04", "D:06"],
    "X:DICT": ["D:01", "D:02", "D:05", "D:06", "D:07"],
    "X:PARENT": ["D:02", "D:05"],
    "X:SCALE": ["D:10", "D:11"],
    "X:SELECT": ["D:03", "D:12"],
    "X:SOURCE": ["D:03", "D:04", "D:10"],
    "X:FLAT": ["D:10"],
    "X:GRAVITY": ["D:11"],
    "X:WEIGHT": ["D:10", "D:12", "D:13"],
}
for x, ds in BLOCKS.items():
    for d in ds:
        E(x, "blocks", d, "OPEN")

# debts of the register that name a map node outright (the rest are listed by class in the queue)
DEBT_BEARS_ON = {
    "P-355": "V:SIX", "P-596": "V:SIX", "P-384": "V:SIX", "P-586": "V:SIX", "P-597": "V:HELD", "P-446": "V:SIX", "P-517": "V:SIX",
    "P-157": "PR:P10", "P-606": "MC:GEN", "P-618": "MC:UNIQ", "P-318": "MC:UNIQ", "P-374": "MC:HYP", "P-579": "V:0OF19", "P-581": "MC:Z6",
    "P-321": "G:GM4", "P-138": "G:GAP5", "P-610": "TAG:UNIT",
}
# the framing ledger's rows that bear on a node outright
FL_BEARS_ON = {"FL:26": "MC:Z6", "FL:19": "V:0OF19", "FL:14": "V:HELD"}

# ------------------------------------------------------------------ the closure queue's curated text
# For each closure node: what the record knows, what would close it, who holds it now, and the duty owed on main.
QUEUE = {
    "X:HAND": dict(
        known=["On the weave neither hand is derived; each lives on a subweave the weave does not select (W:HANDS).",
               "A flat count cannot see the hand: the class index is mirror-even for every module (W:MIRROR-EVEN).",
               "A chiral three exists only as a conditional index, given two tagged postulates, on the double-tick weave (W:INDEX3).",
               "The object's own 2+1 matter is vector-like by theorem (GR:VECTORLIKE).",
               "In the lanes' model the kernel splits equally between conjugate representations, and the charged vectors pair with left and right currents of equal size (E:J4, E:L11)."],
        closes="A derived reason for one sheet of the orientation double cover (G:FK2), or an operational type for the swap (G:FK3); in the lanes' model, a mechanism that splits the pair (E:Q1); or a frame of the right parity (G:GAP6).",
        owner="main for the weave's forks; the agy and physical lanes for their model's pair (their current tickets)",
        duty="verify the paired-pole proof on main, since it is the lanes' sharpest statement of this node (P-749, item e)"),
    "X:DICT": dict(
        known=["No frame is derived (G:GAP1); the dictionary is unearned (G:FK11).",
               "By derivation it is unearnable inside the flat counting frames on any thread or cover (B1604).",
               "It may be earned by sealed prediction within a frame (V:EARN-RULE); no card has been spent.",
               "The lanes' model prices its own read-outs of colour, charge and family as unearned identifications (E:L06, E:L10).",
               "The identification price of the structural theorem is thirteen (MC:PRICE)."],
        closes="A sealed card that spends held-out targets and passes (the owner's hold stands), or an even-dimensional object the weave forces with a non-flat bundle whose index is the count.",
        owner="the owner for the hold; main for the card",
        duty="the register-to-field join below, which would tie the lanes' three to the weave's triplet"),
    "X:END": dict(
        known=["The end law is open (G:FK10); one unit of end data at the cusp is tagged, and nothing the principle forces supplies it (TAG:UNIT).",
               "A generated state has one end, and no generated state carries three by counting ends (W:ONE-END).",
               "The value frame's end is a principled discrete entry, chosen (A:A07, A:A09).",
               "The lanes' end law is a conditional reduction with a non-authoring review and one open code gap (E:L08)."],
        closes="An end condition derived from one action shared by the core and the end (D:03, D:04), or a proof that the unit is forced as a boundary datum.",
        owner="the physical lane (its same-action response packets); main for the tag",
        duty="main's own acceptance review of the two sealed packets (P-746)"),
    "X:TAU": dict(
        known=["The weave fixes no modulus (W:NOMOD); nothing on the record places Im τ (T:NO-PLACE).",
               "In both value frames τ is fitted (A:A01); in the lanes' model it is unselected (E:L04).",
               "A read-out rule exists, conditional on a chosen framing; four choices remain (T:FRAMING, T:POINT-WEIGHT, T:CHARGE5, T:MINIM).",
               "Under it the real part is exact and the imaginary part is one seat's sealed estimate, confirmed on main to two decimals (T:RE, T:IM)."],
        closes="A derivation of the framing or of the depth, or a sealed card on which the candidate τ predicts held-out targets; first, its price under the random-subset control (T:PRICED).",
        owner="main; the web seat for the instrument",
        duty="main's own instrument beyond k = 2 (P-739); the state read-out on the hyperbolic metric (P-744)"),
    "X:SELECT": dict(
        known=["The root's selection criterion is a postulate with kept alternatives (G:SE1); what makes a state physical is open (G:FK9).",
               "In the value frame the line, its offset and the Higgs direction are chosen (A:A02, A:A03, A:A04).",
               "In the lanes' model the background and the Wilson line are unselected branch data (E:L07)."],
        closes="A selection rule stated before computing and graded by the bar; in the lanes' model, a selection law for the background.",
        owner="unowned above the root",
        duty="none owed on main beyond the register's rows"),
    "X:SOURCE": dict(
        known=["Structure exists (a flow, an action at the monodromy, a gauge system) and none of it fixes a value (G:GAP5).",
               "No report derives the source that a non-split bundle needs (G:GAP3).",
               "The object's action is linear and places nothing; its one phase transition has no scale (T:NO-PLACE).",
               "A departure from equilibrium is not established (CO:S3)."],
        closes="A potential, a breaking or a source derived from the same action as the fields.",
        owner="the physical lane (its native stationary family, unreviewed)",
        duty="read and verify that family's proof (P-749, item d)"),
    "X:SCALE": dict(
        known=["An absolute energy cannot come from the object (SC:UNIT); the object carries no dimensionful quantity by theorem (MC:CS0).",
               "A dimensionless ratio is not excluded and waits on a level and an identification (SC:RATIO).",
               "The record holds no object-side reason that the exact block is a ratio of scales, so the scale card is not sealable (SC:R2, SC:CARD).",
               "The lanes' model keeps a length and a coupling unreduced (E:L04)."],
        closes="A second length the object fixes, entering through the level; the record's three pins of σ are the candidates, none adopted.",
        owner="main and the web seat",
        duty="the two candidates left on the card: the content that runs, and one object for the base word's scale and the member's τ"),
    "X:PARENT": dict(
        known=["The lanes' E₈ parent is supplied (E:L02).",
               "On main the container is adopted by a ruling as a composition requirement, not derived; one Lie type is among the structural theorem's five typed inputs (MC:HYP).",
               "The structural frame has never been run off the root (MC:REACH). The golden grammar is not the only one with the own-conductor door: the door set is {1, 4} (MC:UNIQ)."],
        closes="A derivation of the algebra and its embedding from the register, or its honest count as an input.",
        owner="unowned",
        duty="the rest of P-318's corrections, the level-one uniqueness statement next; the agy lane's Theorem A is verified in its metallic part (B1859)"),
    "X:FLAT": dict(
        known=["Both value frames stand on a flat bundle (S:S01), and most of the record's value negatives sit on flat premises.",
               "A flat frame reaches discrete data through the boundary and cannot reach continuous moduli (G:GAP6)."],
        closes="A frame with curvature of the right parity; the lanes' curved functional is a candidate of that kind and is unreviewed on main.",
        owner="the physical lane (its curved action)",
        duty="read the curved action's proof on main (P-749, item b)"),
    "X:GRAVITY": dict(
        known=["The object's own 2+1 gravity is exact and has no free dimensionless constant (GR:ACTION).",
               "A dynamical 3+1 metric coupled to the same matter is on no lane's record (GR:3PLUS1)."],
        closes="A physical map from the internal geometry to a 3+1 spacetime, with the universal coupling.",
        owner="unowned",
        duty="none owed on main yet"),
}

QUEUE["X:WEIGHT"] = dict(
    known=["Every allowed state belongs to the state space by construction (G:XGEN); that the states are realised together, and with what weight, is not derived (G:XGEN-PHYS).",
           "Run with nothing forced, the threads give a definite measure for each way of counting, and the measures differ (W:MEASURE). The moves' own walk gives the move-by-move one exactly (W:WALK).",
           "Nothing on the record forces the clock, counted or followed (W:CLOCK). A sealed test could not separate them (W:DRAW).",
           "The plain sum over all threads is flat and mirror-even (W:FLAT-SUM), and the uniform measure gives the cusp no atom (W:NO-ATOM).",
           "So the law fixes the support and not the weight. Picking one thread is a weight put at one point by hand; a flat average is a weight put everywhere by hand."],
    closes="A weight that the execution itself forces and that concentrates: an atom, or a stationary point of something the moves fix. Or the adoption of typicality as what is predicted, a distribution and not nineteen numbers. Read literally, 'upon its execution' is the move count, the grammar's maximal entropy.",
    owner="the owner for the reading of the law; main for the computation",
    duty="state, before computing, what the executed weave makes deterministic (its ergodic averages) and whether any covariant quantity concentrates (P-756)")

NEXT = dict(
    title="THE REGISTER-TO-FIELD JOIN: the lanes' three against the weave's triplet",
    statement=[
        "The lanes count three coefficient modes per representation on the punctured elliptic curve, at the odd spin structure, in the background without the extra Wilson line. By their own account the three arise as a split of two and one from two different cohomology groups, and the map from the register to that family structure is a missing join with no owner (E:J5).",
        "Main's weave has a triplet at the quaternion point, on which the moves act through a group of order 96 (W:T, W:G96).",
        "The derivation: compute how the moves (the mapping classes, with their lift) act on the lanes' three modes as the modulus varies, and decompose that action against the weave's triplet."],
    outcomes=[
        "It is the triplet: the lanes' three is the weave's three. The family structure is then the register's, and main's conditional index statement (W:INDEX3) can be put to their operator.",
        "It is two plus one under the moves: the background breaks the weave's triplet. The split is then a structural fact to state before any value is read.",
        "The moves do not act, because the background is not kept by them: the model then selects a thread, and its counts are thread results, to be labelled so."],
    why="It is the one place where main's banked mathematics and the lanes' model can be joined by a computation, it is data-free, and it decides whether the lanes' count can be called a family count at all. It also carries X:HAND one step: only in the first outcome does the weave's conditional chirality reach the lanes' operator.",
    owner="unowned; proposed for main. The agy lane's current ticket (the weighted fermion current) is not duplicated.",
)

# the headline results whose upstream inputs the queue lists (the transitive closure of "requires")
HEADLINES = [
    ("G:ROOT", "the root is m004"),
    ("MC:Z6", "the structural theorem (its global-form line stands for the whole table)"),
    ("W:INDEX3", "the chiral three as an index"),
    ("V:SIX", "the six mass ratios at the principled end"),
    ("T:IM", "the modulus under the read-out rule"),
    ("E:L10", "the lanes' three coefficients per representation"),
]

# ------------------------------------------------------------------ weave or thread (the owner's rule; docs/THE_WEAVE.md)
# weave   defined by the joint action of every allowed move, or stated about every thread at once
# thread  read on one thread, one fibre, one point, one background, or covers of one thread
# list    a family examined member by member (THE WEAVE: "the family ... reads as a list"; the weave is not the list)
# record  a fact about the record itself
# The label is required on every node of the spine. A weave result may not rest on a thread node (build_map.py checks).
WT = {}
for _id in ("G:PF1", "G:PF2", "G:PF3", "G:PF1-FORM", "G:GM1", "G:GM2", "G:GM3", "G:GM4", "G:GM5a", "G:GM5b", "G:GM5c", "G:GM5d",
            "G:XGEN-PHYS", "W:Q8", "W:T", "W:G96", "W:HANDS", "W:NOMOD", "W:NOVAL", "TAG:LAMBDA", "TAG:UNIT",
            "W:INDEX3", "W:LAW", "W:MEASURE", "W:WALK", "W:CLOCK", "W:FLAT-SUM", "W:NO-ATOM", "W:DRAW",
            "G:FK3", "G:FK5", "G:FK8", "G:FK9", "G:FK10", "G:FK11", "G:FK12", "G:FK13", "G:FK14", "G:FK15",
            "G:GAP1", "G:GAP2", "G:GAP3", "G:GAP4", "G:GAP5", "G:GAP6", "PR:P10"):
    WT[_id] = "weave"
for _id in ("G:SE1", "G:T-ROOT", "G:SE2", "G:ROOT", "G:FK2", "G:FK7",
            "MC:HYP", "MC:PRICE", "MC:ALG", "MC:Z6", "MC:Y", "MC:END", "MC:CUBIC", "MC:GEN", "MC:CS0", "MC:REACH",
            "V:SIX", "V:WALL", "T:RULE", "T:FRAMING", "T:POINT-WEIGHT", "T:CHARGE5", "T:MINIM", "T:RE", "T:IM",
            "SC:RATIO", "SC:R2", "SC:R4", "SC:PREMISE", "SC:CARD",
            "E:L01", "E:L02", "E:L03", "E:L04", "E:L05", "E:L06", "E:L07", "E:L08", "E:L09", "E:L10", "E:L11", "E:L12",
            "E:Q1", "E:Q2", "E:Q3", "E:J1", "E:J2", "E:J3", "E:J4", "E:J5",
            "GR:ACTION", "GR:VECTORLIKE", "CO:S12", "CO:S3", "PR:P2", "PR:P3", "PR:P9"):
    WT[_id] = "thread"
# a statement true of every thread, each read by its own geometry, is a list, not a weave result (THE WEAVE's test,
# item 2: "defined by the joint action ... not by one thread's own geometry"; relabelled at Review 77, the reader)
for _id in ("G:XGEN", "MC:GENERIC", "MC:UNIQ", "W:MIRROR-EVEN", "W:ONE-END"):
    WT[_id] = "list"
for _id in ("V:0OF19", "V:HELD", "V:EARN-RULE", "E:GRADES", "T:PRICED", "GR:3PLUS1", "T:NO-PLACE"):
    WT[_id] = "record"
WT["SC:UNIT"] = "n/a"                # about any theory

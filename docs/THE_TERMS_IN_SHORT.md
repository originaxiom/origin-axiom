# The terms in short

*The mathematical terms a reader meets on the programme's front pages, in plain words; every line names where it comes
from. "§" names a section of the full account, [`THE_PROGRAMME_SO_FAR.md`](THE_PROGRAMME_SO_FAR.md). Where this page and
`GENESIS.md` differ, `GENESIS.md` holds. The working record's own vocabulary, with its history, is `TERMINOLOGY.md`.*

## The grammar

- **L and R.** The two elementary moves, unit shears: L = [[1,1],[0,1]] and R = [[1,0],[1,1]]. Each adds one of a pair
  of whole-number counts to the other (§ 2; `GENESIS.md` § 2).
- **A word.** A description written as a product of L and R (§ 2).
- **A primitive word using both letters.** The words the states are built from, taken up to rotation and the swap of
  L and R, with a sign (§ 3.1).
- **LR.** The product LR = [[2,1],[1,1]], which has trace 3 (§ 2).
- **The golden matrix.** LP = [[1,1],[1,0]], where P = [[0,1],[1,0]] swaps the two counts; its square is LR. LR is
  also known as the Cohn matrix of the golden ratio, and the rule a → ab, b → a as the Fibonacci substitution (§ 2;
  § 3.3).

## The spaces

- **The once-punctured torus.** The surface of a doughnut with one point removed; the words act on it (§ 2).
- **The mapping torus, and the monodromy.** Let a word's matrix act on the punctured torus, and glue the two ends of a
  thickened copy together with that action: a mapping torus. A state is the once-punctured-torus bundle whose monodromy
  is its signed word (§ 3; § 3.1).
- **Hyperbolic.** Carrying a rigid geometry of constant negative curvature; each space built from an allowed word is a
  hyperbolic three-dimensional manifold with one cusp (§ 3; `GENESIS.md` § 3).
- **A state.** A signed cyclic word, realised as the once-punctured-torus bundle with that word as monodromy (§ 3.1).
- **The census.** 758 states at word lengths 2 to 12, giving 536 distinct manifolds, since a word and its reverse give
  one manifold (§ 3.1).
- **A level.** The n-fold cyclic cover of a state, whose monodromy is the n-th power of the state's (§ 3.1).

## The programme's own names

- **A thread.** One object the principle allows, such as m000, m003 or m004 (`docs/THE_WEAVE.md`).
- **The weave.** All the threads together, with the joint action of the moves on them (§ 3; `docs/THE_WEAVE.md`).
- **The root, and its selectors.** One thread picked out by two stated selectors, one assumed and one chosen: the
  figure-eight knot complement, m004 (§ 3.3; `GENESIS.md` § 4).
- **Torsion-free first homology.** The first selector: the space's basic loop count has no finite "torsion" part. Among
  the states, it holds exactly for the class of LR (m004) and the class of LP (the Gieseking manifold, m000) (§ 3.3).

## Geometry read as physics

- **A frame.** A rule that turns a geometric object, with stated extra data, into particle counts or numbers. A frame is
  a hypothesis, and none is derived from the principle (§ 4).
- **An identification.** A claim that a quantity here is a physical quantity there; it is earned only when the map is
  exhibited and shown to act, and otherwise it is an open debt (§ 0.2; § 4.4).
- **The nineteen.** The Standard Model's nineteen free continuous parameters: six charged-fermion mass ratios, three
  mass scales, the four CKM numbers (the quark mixing), three gauge couplings, the Higgs mass and its vacuum value,
  and θ_QCD. Neutrino masses and mixing are outside the nineteen (§ 0.3).

## How a statement is graded

- **The foundations' labels.** DERIVED (proved, the proof cited), CONDITIONAL (proved given named premises), POSTULATED
  (assumed), CHOSEN (a fork settled by choice, the alternative kept), OPEN (§ 0.2).
- **The labels of a claim.** FORCED (marked generic when any comparable object would give it), ADMITTED (allowed among
  alternatives), CHOSEN (an input), FITTED (a continuous value set by data); for a negative result, EXCLUDED (within a
  stated scope, by an argument) against NOT FOUND (a declared search's null) (§ 0.2).
- **A reading.** An interpretation recorded and not derived; for a comparison with data, the grade of a fit that reaches
  the data only with inputs set by hand or read from the data (§ 0.2; `GENESIS.md` § 1).

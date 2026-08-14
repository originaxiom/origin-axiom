# PREREG — THE SELECTION & QUANTUM-COCHAIN CAMPAIGN (seat cc3; sealed before compute, 2026-07-17)
# Two programs: D-B "WHY DISC 5" (the selection theorem) and D-A "THE QUANTUM
# COCHAIN DESIGN". Repo READ-ONLY at [seat-machine-path]
# All work under this dir. Gate 5: no SM comparison anywhere in this campaign.
# Agent economy: sonnet for every scoped cell; main seat (Fable) only for
# derivation synthesis and verification. No task-store use (shared-slot
# avoidance); STATUS.md on disk is the anchor.

## WAVE 0 — four scoped cells (sonnet, parallel)
W0a THE SELECTION TABLE. Enumerate all primitive cyclic R/L-words up to
length 12 (up to cyclic rotation; keep inversion and R<->L-swap classes
marked). For each: trace, disc = tr^2-4 (+ factorization), conductor
primality, det(A-I) = 2-tr unit?, amphichirality by the WORD criterion
(w ~ its reversal with R<->L swapped, up to rotation) — computed, not
assumed; the (kappa|5)-style silence character vs its own disc. Exact
integer arithmetic. Falsifier: if ANY word other than RL is simultaneously
amphichiral + unit-det + prime-conductor, the uniqueness claim DIES —
report it, do not soften.
W0b THE FIELD TABLE. Per word: eigenvalue field Q(sqrt d), d = squarefree
part of tr^2-4; classify d's entanglement class (d = 5 clean-quadratic;
d in {2,3,6} cyclotomic-entangled a la silver Q(sqrt2) in Q(zeta8); else);
which words share fields (the field-degeneracy classes). Exact.
W0c THE UNIQUENESS INVENTORY. Read-only sweep of the repo record: every
banked golden-uniqueness property with its B-number citation (amphichiral
unit; prime conductor; clean bifocal split B663/B649; landscape origin/
minimum B664; shadow-class B665; self-selection half-law; L91 state after
B664; the L104/delta-chain closure B662). Output: a structured list —
property, exact statement, citation, and whether it is METALLIC-SLICE or
GENERAL-FAMILY scoped. No new claims.
W0d THE QUANTUM SCOUT. Structure-of-the-field cell (no web needed; reason
from the banked record + standard theory): given Ocneanu rigidity (fusion/
modular categories admit no deformations — Davydov-Yetter H^2,3 vanish),
the naive "quantum H^1" target is dead; enumerate the surviving candidate
cohomologies for the stage+weld system (module-functor cohomology with the
weld bimodule as coefficients; tube-algebra / annular category traces;
categorified Fox calculus on the stage's module category), and for each:
what banked data it consumes (S,T, the weld operator, the Gamma5'-doublet
ear of B662w3), what its h^1-analogue would be, and a COMPUTABILITY grade
at SU(3)_2 (exact/feasible/priced). Output: a ranked candidate list with
one computable falsifier each. Flag any claim you are not sure of as
UNSURE rather than asserting.

## WAVE 1 — main-seat derivations (Fable, after wave 0 lands)
D-B synthesis: the implication lattice among the selection criteria on the
W0a table (which are equivalent, which independent — with word
counterexamples from the table as witnesses); the minimal axiom set that
forces tr = 3; theorem-shaped statement + what remains conjectural.
D-A synthesis: the sealed QUANTUM COCHAIN DESIGN DOC — target theory
chosen from W0d with justification, the falsifiable wave-2 cells priced.
## WAVE 2 — the design's first computable cells (sonnet; preregistered by
## addendum after wave 1 seals them). WAVE 3 — close: packet, memory.
Verification: main seat recomputes one W0a row (a nontrivial word) and one
W0b class by hand; W0c citations spot-checked against the repo; W0d's
rigidity claims checked against the record before any wave-2 spend.

## WAVE 2 ADDENDUM (sealed after wave-1 syntheses, before compute)
W2a THE AMALGAM QUANTUM COCHAIN (per DESIGN_DA.md): exact MV/amalgam h^0,
h^1 for the weld double at SU(3)_2 + levels 1,3,4. Falsifier as in design.
W2b THE GENERAL-FAMILY LANDSCAPE (per SYNTHESIS_DB.md section 4): |tr_odd|
and Im(tr_odd) for ALL 745 classes at SU(3)_2, exact; sealed question: is
RL the unique minimal-nonzero-modulus AND real class? Controls: the
metallic-slice rows must reproduce B664's closed form exactly; the silver
R^2L^2 row must reproduce its banked value.

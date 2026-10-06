# B1482 — THE SIGN IS THE CANCELLING MOVE: the handed states need one move beyond L and R — negating both records — and no inverse letter; nothing the act does can produce them; positivity is what excludes them

**Verdict: PROVED** (four statements about SL(2,ℤ) and GL(2,ℤ), each with a short proof and an enumeration; reach
*general*). The reading that connects them to the principle is labelled a reading and is not part of the verdict.
Scope: frame none (the grammar itself, GENESIS §2–§3); object the moves L, R, P, −I and the positive words; hypotheses
none beyond the definitions. cc (main), 2026-10-07. The crossing plan's option 1: *does the principle generate the
sign?* **0 of 19.**

## 0. Seen first, and literature

`VERDICT topic-sweep /inverse moves|signed states|positivity|elliptic involution|GM5b|GM5d/: 34 of 1354 arcs on main match (NEGATIVE 8, OPEN 3, PROVED 23)` — read at the level of the verdict lines and not further, except where named: the 34 matches include GENESIS' adoption arcs B1454 and B1456 (which carry GM5b, "Inverse moves are legal — OPEN. Needed for the signed states", and GM5d, positivity, CHOSEN), B1422 (the swap as an added axiom), B1459 (the fibre's elliptic involution on levels), B1297, B1462, B1083 (positivity as "the arrow's home"), today's B1479 and B1480, this arc, and some two dozen older arcs that use "positivity" or "inverse" in other senses (B49, B101, B105, B127, B161, B269, B288, B309, B347, B351, B353, B392, B561, B647, B740, B930, B935, B990, B1010, B1031, B1141, B1145, B1243, B1306, B1406). I found no statement that the signed states need only −I, that −I brings no inverse letter, or that positivity is what excludes the handed states; the older arcs were not opened, so this is an absence at the level of verdict lines. **Literature:**
elementary facts about 2 × 2 integer matrices; proved here, nothing cited.

## 1. The four statements (`verification/checks.py` → `checks.json`)

Convention (GENESIS §2): L = [[1,1],[0,1]], R = [[1,0],[1,1]], P = [[0,1],[1,0]]; a + state is a positive word w in L
and R with both letters (trace ≥ 3); its − state is −w.

- **S1. Words in L, R and P never give a − state.** Their entries are non-negative, and a product of non-negative
  matrices is non-negative; −I and −w are not. *(3,070 distinct matrices from all words to length 10: none has a
  negative entry.)*
- **S2. No − state is a square.** For X in GL(2,ℤ), tr(X²) = (tr X)² − 2·det X ≥ −2. A − state has trace −tr(w) ≤ −3.
  So −w = X² has no solution — with either determinant. *(Every X with entries to 12: the smallest trace of a square is
  −2; of the 8,166 positive hyperbolic matrices to length 12 the largest −tr is −3.)* **Consequence:** an "act" of
  determinant −1 squares to a + state (the golden act LP to LR); the orientation double cover — "act plus register" —
  is always a + state. Nothing built by squaring reaches the − states.
- **S3. One move suffices.** −I commutes with L, R and P, squares to the identity, and −w is never a positive word.
  Adding the single central move −I to the grammar gives every state its sign-twin and uses no inverse letter.
- **S4. That move does not bring inverse letters.** A positive word and its negative have entries of one sign;
  L⁻¹ = [[1,−1],[0,1]] does not. So allowing −I does not allow L⁻¹ or R⁻¹: the record's two expressions
  −I = (L²R⁻¹)² = (L·R⁻¹·L)² (both checked) show that inverse letters *suffice* for the sign, not that they are needed.

## 2. What follows for the genesis (GENESIS v1.14, by `adoption/amend.py`)

- **GM5b was over-stated.** "Inverse moves … needed for the signed states" becomes: one central move is needed, and it
  is independent of the question of inverse letters.
- **GM5d is where the sign is excluded.** −I sends a pair of counts to its negative; positivity — which GENESIS marks
  CHOSEN, "a sector restriction, not a consequence of using L and R" — forbids exactly that. Under positivity the
  grammar generates the + states and, with P, the non-orientable ones. By B1479 and B1481 the − states are the ones on
  which every spin structure carries a hand. **So the handed states are precisely what a chosen restriction removes.**
- **FK4 is one question now:** is negating the records a legal move?

## 3. The reading (labelled; not a derivation; not part of the verdict)

PF1 says existence is what remains when *cancelling* to nothing cannot complete. On a pair of records, cancelling is
negation: v ↦ −v, the move −I. Read that way, a − state is a description together with one application of the
principle's own attempted act — and the attempt fails to reach nothing, since −w is hyperbolic for every positive
word w. The record has one earlier reading of PF1 (P008: non-cancellation is κ = tr[a, b] ≠ 2); this is a second, and
the two are not in conflict (the commutator is unchanged by −I). **A reading can be wrong in a way a theorem cannot:**
it would be supported if the − states turn out to carry what the + states lack on the line to physics (a hand, by
B1481; the SM seat's rooms for three sit on covers of m003, the simplest − state), and it would be undercut if the
handed side proves empty of everything else.

## 4. Disclosed

S1–S4 are elementary; their worth is in what they correct on the foundations page. The claim that positivity "removes
the handed states" rests on B1479 and B1481, which are census laws to length 12, not theorems. §3 is a reading.

# B1321 — L205, THE SIBLING'S LOCALIZED COUNT: Pantev–Wijnholt's count on m202's fixed cusp with the two choices priced, and a search of the three-line class for a member that keeps the golden face: DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** the owner's decision of 2026-09-08 on MASTERPLAN v3's D3 ("reopen D3 as a bounded arc after Phase 1"),
registered as L205 at B1303: *"PW eq. (3.18)'s localized count on m202 with fc's two choices (equal signs on the three lines; the manifold within the class)
priced as identification rows, plus a search of the three-line tetrahedral class for a member that keeps the golden face."* Approved with the rest on
2026-09-09 ("all approved, run all you can according to your order"). · **Number:** B1321 (after B1320, Arc 0). · **Read in full before this seal:** B1302
(its three questions and Q4's `b1302_faces.py`: Δ_{m202} has seven ±1 monomials, no specialisation of the 48 primitive classes divisible by t² − 3t + 1;
its headline "its three lines are PW's localized count under two named choices"), fc R72b/R72d (the order-3 isometry of m202 fixing three lines; the census
menu), sm:B1282 (the flat sector vector-like; the golden face lost), B1291, B1295, B1320's DESIGN and its control run (m202 is the census's first manifold
with |det(A − I)| = 3 on a fixed cusp: A = [[−1, −1],[1, 0]], order 3, on cusp 0). **Tool limit stated now:** SnapPy's orientable cusped census reaches nine
tetrahedra on this bench (the plan wrote twelve); the search runs to nine and says so.

## 0. The rule lines

`already_banked.py "m202 localized count three lines golden face census three-line class"` → B1302 (the sibling's three questions; Q4 the golden face absent),
B1292 (m202 in the commensurability class), B1291. Nothing on main has searched the class for a golden-face member. Receipt: `verification/already_banked_at_seal.txt`.

## 1. The view from above

Every seat's 3 lives on m202: fc's order-3 isometry fixes three lines, the audit seat derives three arcs, the SM seat proves the flat sector vector-like. B1302
priced the case: the 3 is PW's localized count under two choices, and m202 has no golden face (no fibration carries t² − 3t + 1). This arc does the two things
the owner's decision names and nothing else: (a) compute the localized count on m202 in B1320's frame — per cusp, per orientation-preserving cusp-fixing
isometry, |det(A − I)| — and write the two choices as identification rows with their price; (b) ask the census whether any two-cusped manifold with an
order-3 cusp rotation KEEPS the golden face, i.e. whether the object's own family reaches a 3 without paying the golden polynomial. **If (b) finds nothing:**
the price of the 3 is the golden face throughout the class the census can see, and L205 closes as a priced door, not a drift. **If it finds one:** that
manifold is the first candidate closing with both a 3 and the golden face, and it becomes a lead in its own right (a new L-number), with its arithmetic
face checked next (B1292's commensurability test).

## 2. Pre-registration

**(a) m202's localized count** (`verification/b1321_m202_count.py`): SnapPy `m202`, all isometries, for each cusp the orientation-preserving ones fixing it,
|det(A − I)| and the order of A; the PW localized count on a fixed cusp is |Fix| = |det(A − I)| with every isolated fixed point of index +1 for an
orientation-preserving map. **Expectation:** an order-3 rotation with |det(A − I)| = 3 on at least one cusp (B1320's control found it on cusp 0; prior 0.98),
and the two choices: **I-30** *the closing's charge locus ≡ a cusp of m202 fixed by its order-3 rotation* (which cusp, and m202 itself rather than another
member of the class — the manifold-within-the-class choice) and **I-31** *the three fixed points carry equal signs* (in PW's frame the index of an isolated
fixed point of an orientation-preserving map is +1, so the equal signs are FORCED once the locus is chosen — the arc records whether fc's second choice is a
choice at all; prior 0.7 that it is not, i.e. one identification row, not two). Both rows UNEARNED at registration (the baseline migrates deliberately, dated).

**(b) the class search** (`verification/b1321_class_search.py`): every two-cusped manifold of the orientable cusped census to nine tetrahedra (2 750 on this
bench); keep those with an orientation-preserving isometry fixing a cusp with |det(A − I)| = 3 (an order-3 rotation) — the three-line class; for each,
main's own golden-face test from B1302 (`b1302_faces.py`'s method: the two-variable Alexander polynomial by Fox calculus of SnapPy's presentation when it has
two generators — the fundamental formula ∂R/∂a = (t₂ − 1)Δ — and, for presentations of higher rank, the gcd of the (n − 1)-minors when sympy reaches it,
else "not tested" recorded), the 48 primitive specialisations (|p|, |q| ≤ 6) and divisibility by t² − 3t + 1. **PASS** = at least one member with a golden
specialisation (prior 0.25; the golden polynomial is m004's fibre monodromy, and a two-cusped manifold in the class with a fibred face carrying it would be a
sibling with both faces); **FAIL** = none through nine tetrahedra (prior 0.75), recorded with the size of the class and the count of untested presentations.
Controls: m202 must appear in the class with 0 divisible (B1302's number); m004 (one cusp) is outside the class by construction; a planted golden
specialisation (Δ multiplied by t₁² − 3t₁ + 1) must be detected by the test.

## 3. Landing list

`frontier/B1321_l205_the_siblings_localized_count/{DESIGN.md, DESIGN.sha256, FINDINGS.md, arc_verdict.json, verification/}`; `docs/IDENTIFICATION_LEDGER.md`
I-30 (and I-31 if it is a choice) with the baseline migration; OPEN_LEADS L205 status; MAIN_GOAL's door note (D3 done as a bounded arc); the alias table's
next-free line (B1322); CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS; a new lead only if (b) passes.

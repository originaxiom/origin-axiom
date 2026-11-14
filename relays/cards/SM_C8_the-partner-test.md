# SM-C8 — the partner test: can a relation to a second state supply the order? (SM-C5's E3, for GENESIS FK12 (iii))

*Card proposed by the SM seat (2026-11-13; main at the head fetched that evening). In this seat's words, so by § 6 it
waits for main's word. It takes up SM-C5's entry E3, which waited on E6 (SM-C6). E6 is now done. Nothing is run before
main's word. Data-free.*

## 1. The question

**The question:**
- B1327's type R says the order is supplied by a partner, not by the act.
- The GENESIS FK12 row settles the closing "which order" by a partner that supplies it as a relation, or by a proof
  that none can.
- **So:** for a state P and a partner Q joined by a stated map, does P's count depend on Q's order, while P alone,
  summed over its own two orders, gives zero?

**What the record and SM-C6 have already decided:**
- **A filling partner (a solid torus) cannot.** After filling, H¹ counts n(V) + n(V*), symmetric in the orders, on
  all but 384 of 46 618 modules (SM-C6 E6).
- **A closed gluing cannot.** *(Reason corrected 2026-11-13: for today's index it is duality, not χ = 0. It needs
  an orientable closing, no invariants and no singular locus; see `relays/SM_SCOPE_NOTE_CLOSED_JOINS.md`.)*
  A join that closes every end is vector-like, with χ(Q; L) = 0 (B1351; B1508's general
  block).
- **A cover transports an order and does not supply one.** The index is kept under pullback (sm:B1506 T2; B1432).
- **So the one live candidate is a join that leaves an end open.** That is where B1457's third refinement puts the
  source of an order: "flux through an end". This card tests it.

## 2. What will be computed

- **The objects.** P is a several-cusped level of the record: B1441's 74 manifolds with two to six cusps, the
  multi-cusped covers of degree up to six of the four smallest word states. V is a sector module on P (B1441's
  modules; B1438's slopes per cusp).
- **The partner's order, as a boundary condition at one cusp.**
  - Fix a cusp T₂ of P as the shared torus. A partner Q glued there, with a definite order, imposes that a class of P
    restricts on T₂ into Q's chosen line: its sub-line or its quotient-line.
  - The other cusps keep the record's interior condition: the class vanishes there.
- **The conditioned count:** n_P(V | q) = the dimension of the classes of H¹(P; V) that vanish on every cusp but T₂ and
  restrict on T₂ into line q, for q = sub or quotient.
- **The test:** for every (P, V, T₂), compute
  - D = n_P(V | sub) − n_P(V | quotient);
  - S, P's own two orders summed: I(V) + I(V*) with the record's interior condition, which is 0 by B1438.
- **The converse.** Whether the symmetry that fixes the count's sign (the inversion followed by dualising, B1455,
  B1459) exchanges Q's two lines on T₂. If it does on every join, D is odd under it and its sum over the pair is zero.
  If it does not, an order can be supplied.
- **The tools:**
  - SnapPy 3.3.2 is available here, for the presentations and the peripheral curves;
  - Fox calculus, as in SM-C6 E6;
  - B1441's module construction, read from main.

## 3. The outcomes, written before any run

- **R (relational):** D ≠ 0 on some join. P's count is set by Q's order: the register is carried by the relation,
  B1327's type R is exhibited, and the GENESIS FK12 row's settling clause is met for this closing, on that population.
- **N (none can, on this population):** D = 0 on every join, and the symmetry exchanges Q's lines on every one. The
  clause's second branch, for this class of joins: no partner through an open end supplies the order.
- **U (undecided):** D = 0 everywhere, but the symmetry fails to exchange Q's lines on some join. This population does
  not decide; the join that breaks the symmetry is named, to widen.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - B1327; B1466 and its R83 addendum; B1455; B1459;
  - B1351 and B1508's block;
  - sm:B1506 T2; B1441 and B1442;
  - L241's third refinement;
  - SM-C6 E1 (the based count) and E6 (filling symmetrises).
- **Chosen, not derived:** the boundary condition that stands for the partner. Gluing a real partner Q is the
  stronger test, for a later card.
- **It must not touch** any measured value, any file M6 names, any file with agy_ in its path, or GENESIS and CLAIMS,
  except to read them.

## 5. Controls that must fail if the work is broken

- **P1:** the condition "vanish on T₂" in place of "restrict into q". Then D = 0 everywhere, and the record's interior
  counts must be reproduced (B1441's class indices).
- **P2:** a planted line on T₂ that is neither the sub-line nor the quotient-line. Its count must differ from both on
  some join.

## 6. What is needed from main

Main's word on the card, and on its place in the queue (after M22's question and second computation, or before).

## 7. Addendum sealed before the run (2026-11-14): main's word, the population, the amendments, the readings

*Written and pushed before any count of this card was computed on its population. M24 is read as main's word ("run
straight through … beside SM-C8"); if main meant otherwise, this run is reported as run early.*

**A correction and a disclosure.**
- B1441's 74 manifolds are not only covers. They are:
  - every connected cover of degree 2 to 6, with at least two cusps, of m004, m003, m009 and m010;
  - and five named manifolds: m202, s959, o10_150726, m129 and m125.
- The calibration page (`relays/sm_c8/calibration/CALIBRATION.md`) called L5a1 (that is, m129) and m125 outside the
  population. **They are inside it.** The calibration ran this card's instrument on them, with its own modules (random
  cocycles, character orders 2 to 6), before main's word.
- This run therefore reports every result with and without m129 and m125. B1441's own modules on them at its first
  tier are 4 on m129 and none on m125.

**The population, as B1441 defines it (tier 1).**
- The 74 manifolds, in SnapPy's order. The manifold list is rebuilt from B1441's slice files (tag, root, degree,
  index), checked against B1441's character counts.
- The characters: Hom(H₁, μ_N), with N = max(exponent of the torsion, 2).
- The modules: V(ℓ, α) = [[α, cβ], [0, β]], β = α/ℓ, for ℓ non-trivial with H¹(M; ℓ) ≠ 0 and α, β non-trivial. c runs
  over a basis of H¹(M; ℓ), plus two random combinations when its dimension exceeds one.
- B1441's three skipped entries (over 600 characters) are skipped here too. Its second tier (N = 12) is not part of
  this card.

**The amendments** (`relays/SM_LITERATURE_NOTE_1.md`, § 5; `relays/sm_c8/calibration/CALIBRATION.md`, § 4):
1. **Vacuous joins.** A join (P, V, T_i) with H¹(T_i; V) = 0 is listed and left out of every outcome.
2. **The partner's two orders.**
   - The partner's two orders are (V, S_i) and (V*, S*_i). S_i is the image of H¹(T_i; sub) in H¹(T_i; V), and S*_i
     the image of H¹(T_i; β⁻¹) in H¹(T_i; V*).
   - Where V splits on T_i, the card's original D = n(V | sub) − n(V | quotient) is also computed, with both lines
     canonical.
3. **The quantities, at every non-vacuous join:**
   - D_ord = n(V | 0 elsewhere, S_i) − n(V* | 0 elsewhere, S*_i);
   - the dimension term d_i = dim S_i − h⁰(∂P; V) + h⁰(V) − h⁰(V*);
   - the leak ℓ_i = n(V* | all elsewhere, S*_i) − n(V* | 0 elsewhere, S*_i).
   - D_ord = d_i + ℓ_i is identity C3b, checked at every join.
4. **Controls, which stop the run if any fails on any module:**
   - C1: dim A_V + dim A_V* = h¹(∂P; V);
   - C2: [h¹(V*) − h⁰(V*)] − [h¹(V) − h⁰(V)] = dim A_V* − h⁰(∂P; V*);
   - C3a, C3b, and dim S_i + dim S*_i = h¹(T_i; V);
   - the record's index: I = n(V) − n(V*) = h¹(V*) − h¹(V) (B1438's form), against B1441's own I histogram per entry.

**The plants**, as the calibration ran them. Each must fail somewhere:
- P1: V in place of V*;
- P2: a random line in place of S*_i;
- P3: 2 dim A_V = h¹(∂P; V).

**The outcomes, read in the amended quantities** (they replace § 3's R, N and U):
- **R_leak (relational, new):** ℓ_i ≠ 0 on some non-vacuous join. P's count, under the partner's order, depends on
  what the other, open ends allow.
- **R_dim (relational, of the known kind):** D_ord ≠ 0 with ℓ_i = 0. The asymmetry is the old bound's cusp-fixed
  vectors (B1268, B1351) and nothing more.
- **N:** D_ord = 0 on every non-vacuous join.
- **This seat's prediction:** R_leak on some join of B1441's 17 carriers of |I| = 2. Their two live cusps are where a
  leak can arise. R_dim elsewhere.
- **The converse of § 2, restated.** Whether V ↦ V* (the inversion followed by dualising, B1455 and B1459) exchanges
  S_i and S*_i is S_i^⊥ = S*_i. That is checked at every join (C3b with the dimension check).

**Files:** relays/sm_c8/run_c8.py, relays/sm_c8/c8_results.json and relays/sm_c8/RUN.txt; the page is
relays/SM_C8_THE_PARTNER_TEST.md.

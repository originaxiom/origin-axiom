# B1994 — Listening 10: ω's own symmetry is a move of the whole, LR⁻¹, the cyclic exchange of the three readings; at the common point it is a third turn about the opening diagonal, and it tells the three apart, with charges 1, e^{2πi/3}, e^{−2πi/3}

**Verdict: PROVED (exact).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free. Register
rows P-882, FK15 (P-694), and GENESIS v1.35's retired ω. **0 of 19.**

## Seen first

- **B1993:** given integrality, the whole's arithmetic selects the hexagonal torus ω, the orbit of (3, 3, 3), in four
  lifts split 1 + 3.
- **B1984 and B1987:** the triplet and the cube around the common point.
- **B1985:** the whole opens along the body diagonals.
- **B1601:** odd-trace words act at the origin as third turns about a body diagonal.
- **GENESIS v1.35:** the author's tagged postulate τ = ω, with "the stabiliser of ω in the weave's group, the residual
  charges of the matter triplet … (Novichkov–Penedo–Petcov mechanism, imported and tagged)", retired as tested. Here
  nothing is imported: the stabiliser is found among the moves.
- **Swept:** `VERDICT topic-sweep /stabili[sz]er of omega|residual Z_?3|Z3 charges|charges 0, ?1, ?2|cyclic exchange|third turn/: 3 of 1735 arcs on main match (PROVED 3); 0 register rows match (none)`. B1601's lemma and the retired postulate's notes. No arc finds ω's stabiliser as a move acting on
  the whole's forced structures.
- **The literature:** none needed. Exact computation in the moves' own trace maps.

## The results (`verification/omega_sym.py`, `omega_sym_run.txt`; exact)

| cell | outcome |
|---|---|
| E1: the stabiliser of (3, 3, 3) acts as a cyclic group of order 3 | **holds.** 64 reduced words up to length 6 fix (3, 3, 3); the shortest are LR⁻¹ and RL⁻¹. **LR⁻¹ acts on every reading as the cyclic exchange (x, y, z) ↦ (y, z, x),** of order 3 |
| E2: at the common point a third turn about a body diagonal, eigenvalues 1, e^{±2πi/3} on the triplet | **holds.** Its linear part is the cyclic permutation matrix, of order 3, with fixed axis (1, 1, 1) and eigenvalues 1, −½ ± (√3/2)i |
| E3: fixes the positive lift and cycles the three mixed ones | **holds.** On the cube it fixes only the vertices ±(1, 1, 1), no face and no edge |

## What the whole does, read in its own terms

- **The selection's family** is a consistency condition: the reading the whole's own arithmetic fixes (B1993). Its
  stabiliser is read by a finite classification with a test of membership: the words to length 6 that fix (3, 3, 3).

- **The point the whole selects has a symmetry, and it is one of the whole's own moves,** LR⁻¹. It exchanges the three
  readings cyclically, exactly, everywhere on the character variety.
- **At the common point it turns the triplet a third of a turn about (1, 1, 1),** the diagonal along which the whole
  opens towards (3, 3, 3) (B1985).
- **It tells the three apart.** Under the cube group the three were one indivisible triplet. Under ω's symmetry they
  split into:
  - one neutral member (eigenvalue 1), along the opening diagonal;
  - two members with conjugate charges, e^{2πi/3} and e^{−2πi/3}.

  These are powers of the shape's own number. The selection of ω breaks the cube to ℤ₃ on the triplet.
- **It fixes the positive lift and cycles the other three:** the 1 + 3 of B1993, seen from ω.
- **This is the first structure a field at ω would carry,** read from behaviour: a triplet with charges 0, 1 and 2
  under ω's own ℤ₃. No hierarchy and no Standard Model shape was asked for or read.

## What is open

- **How the whole's unfolding (B1986's W₊) acts on the three charge members at ω:** whether the decay rates and the
  persistent alternation separate by charge. This is the next listening step.

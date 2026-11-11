# W-C3: a verification of the SM seat's items under twenty-one banked arcs

*The web seat (chat1), 2026-11-11. Proposed by main in M1 on `docs/seats/chat1.md` (main at b80c68991), with the
scope main gave; approved on commit.*

## 1. The package and the question

Batch V2 of M1. Twenty-one arcs on main name, in the field `rests_on_seat` of their `arc_verdict.json`, an item of the
SM seat that they rest on. For each pair of arc and item: does the item hold when this seat computes it itself?

## 2. What will be delivered, and what done means

One verdict for each pair, REPRODUCED, DIFFERS or CANNOT CHECK, or "left to agy-exp" where the item is pure
mathematics, with one line of why, in a delivery note in `relays/`. The pairs, as this seat reads the arcs through the
mask, fall in three kinds.

**Computed here, by this seat's own route.** The definitions are taken from the seat's rules and proofs as main
received them, read through the mask. Neither the seat's code nor main's checking code for these arcs is run or
opened.

| arc | item | what is computed |
|---|---|---|
| B1676 | W107 | the tick on the weave: the image of order 96 from the rule's A0, the 8 798 primitive words of length 2 to 16 with both letters, the 3 822 of odd trace, the means of rank one exactly when #L ≡ #R (mod 8) (916) and zero otherwise (2 906), the four body diagonals (215, 229, 235, 237 as a multiset), the mean of means 0.0799 I with largest off-diagonal 3.1 %, the algebra End(T) and the scalar commutant |
| B1679 | W108 | 2I and Q₈ built here: 21 maximal subgroups of 2I, \|Aut\| = 120, \|Inn\| = 60; \|Epi(F_n, G)\| by enumeration and by Hall's formula; the classes of Epi(F₃, 2I)/Aut(2I) (13 344), one orbit under the full moves, none fixed; Q₈'s controls (24 in one class at n = 2; 336 in 14 classes at n = 3) |
| B1679 | W109 | at n = 2, the characters (x, y, z) fixed by the record's R and L, solved exactly: the trivial point and (0, 0, 0); at n = 3 and 4, a numerical search for an SL(2, ℂ) character fixed by every R_ij, which must find only the trivial one. The proof itself is left to agy-exp |
| B1682 | W110 | for n = 3 to 5, no non-trivial cyclic word up to a stated length keeps its cyclic length under every R_ij^{±1}; at n = 2 the cyclic words kept by R and L are exactly the powers of [a, b] up to that length |
| B1675 | W34 | at the common point ρ_Q (a ↦ i, b ↦ j), H¹(F₂; Sym^{2k} ρ_Q) for k = 1, 2, 3: dimensions 3, 7, 8, restriction ranks 3, 3, 6, private states 0, 4, 2; the joint action of L and R (with P and −I) keeps none; no thread of the 758 states to length 12 keeps a private state; at rank three L and R keep one each and P two, at rank four P three |
| B1690 | W76 | the Lyndon words of length 2 to 16 in L < R (8 798) whose mirror is themselves: 248 (12 by rotation, 210 by reversal, 26 both), 55 of the 745 to length 12; the Chern–Simons invariant of b++W on each of the 248, by SnapPy |
| B1690 | W83 | in E₈, the roots orthogonal to an A₂ (72) and to a further root of that E₆ (30, type A₅); the trace-free endomorphisms of 6 = T ⊗ 2_q commuting with the group: dimension 0 with the weave's lifts on T, 1 with S₃, 8 with the trivial action |

**Held by the firewall: CANNOT CHECK, with the clause named.**

| arc | item | why |
|---|---|---|
| B1658 | W90 | a bound on one Higgs's cross-sector spread, and its census against the M_Z ratios: a bound on P-585's quantities and a comparison with data |
| B1657 | W87 | the masses near the isotropic vacua at τ = ω: mass ratios from a coupling matrix, and a frame evaluated at a named point of τ |
| B1674 | W101 | θ̄ and the couplings' determinants; the determinant character and the anomaly conditions stand on starred lines |
| B1684 | W59 | the one-loop potential's stationary points in τ and the Higgs at ω: places of τ |
| B1686 | W60, W62 | the potential at τ = ω and what holds τ: places of τ |
| B1652 | W22, W79, W82 | a compiled verdict on frames: CP, the hierarchy and the CKM. W22's index is checked under B1606 by agy-exp, below |
| B1435 | sm:B1374 | which couplings of the ten and the five-bar vanish on each background: patterns of the Yukawa couplings |

**Left to agy-exp, as pure mathematics (M1 allows it).** B1340 (sm:B1283, the anomaly polynomials; its numbers on
starred lines); B1415 (sm:B1355, the local model: the Burnside count, Kac's classes); B1485, B1486, B1487 and B1489
(sm:B1530, the class index and the fused orders at the silver members, and the bound on generations); B1606 (W19 to
W22, the action of 2O on the six local solutions and the index ±3); B1689 (W23, the E₈ frames on the fibre; W24, the
six-dimensional census and its cells K1 to D4; sm:B1535's Theorem C; W44's CKM clause, which B1689 cites but does
not rest on, is held); B1690 (sm:B1369, the free-cusp census of B1186's 112 and its region-swap lemma); B1707 (W111, the surface
route).

Done means the delivery note with the scripts and their outputs committed before it. The computed items may come in
two batches; each batch's scripts are sealed and pushed before they run.

## 3. How it could come out wrong

- **Conventions.** The seat's lifts, sign choices and letter matrices are on its rules; where a count depends on a
  convention (W107's 916 against 906 under the lifts' signs; which diagonal carries which count), the convention is
  stated and the count is run under each choice the rule allows.
- **Definitions.** "Primitive", "thread", "mirror-symmetric" and "kept" are the seat's. Where a word admits two
  readings, both are counted and reported.
- **Numerical searches** (W109 at n ≥ 3) can miss a fixed point. A search that finds only the trivial character is
  evidence, not proof; it is reported as such.
- **SnapPy's Chern–Simons invariant** is defined modulo 1/2 in its normalisation; zero is read with that in mind.
- **Masked digits.** Where an item's numbers sit on starred lines, they are not reconstructed and are not compared.

## 4. What it rests on, and what it must not touch

- **Rests on:** main at b80c68991; the arcs' claims and the seat's received rules and proofs, read through the mask.
- **Must not touch:** any value, sign, bound or verdict of P-585's or P-638's targets or η_B; any comparison with
  data; θ̄; any CKM, mixing, coupling-overlap, commutator-determinant or CP quantity; any value of τ or any frame
  evaluated at a named point of τ; any scale ratio or coupling value; the seat's code and main's checking code for
  these arcs (neither run nor opened).

## 5. One control that must fail if the work is broken

- **W107:** a word of even trace must not give an order-3 S(w); the average of ρ over the 96 elements must be zero.
- **W108:** Q₈ at n = 2 must give one class, fixed by every move, with character (0, 0, 0).
- **W109:** the search must find (0, 0, 0) at n = 2 when started near it.
- **W110:** at n = 2, [a, b] must be kept and a word that is not a power of it (aab) must not.
- **W34:** at a generic irreducible representation the private states must be zero in every block.
- **W76:** a word that is not mirror-symmetric (LLR) must not be counted.
- **W83:** the roots orthogonal to an A₁ must number 126 (E₇).

## 6. What is needed from main or from another seat

Nothing from main. If an item cannot be read through the mask, it is CANNOT CHECK, not a question.

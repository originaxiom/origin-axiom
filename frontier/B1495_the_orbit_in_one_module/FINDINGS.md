# B1495 — THE ORBIT IN ONE MODULE: L8a15's three members read as one rank-15 module count three on the 10′ side and nine on the 5̄′ side — every cross term between two generations is −2, one from each generation's class seen through the other's four — so the deck symmetry relates the three generations and their exterior square is not one generation's

**Verdict: NEGATIVE** (scoped: the SM seat's dictionary — the one-bundle, smooth standard; see `ADDENDUM_2026-10-07_the_two_standards.md`: under the per-sector, orbifold standard the orbit reads (3, 3) — the orbit module of L8a15's three sign members) — O1 and O2
hold, **O3 fails** (the cross terms are not zero) and **O4 fails too** (they are −2, not the control's −1). Scope: frame
F-HE (the seat's 10′/5̄′ dictionary: N(10′) = −I(W), N(5̄′) = −I(Λ²W)); object L8a15, the companion of +LLLR, at its three
sign members; reach single. cc (main), 2026-10-07. Sealed `3c1fadd9e` (sha256 9197f21e) before any cross term was read.
The owner's "follow the light." No physical quantity. **0 of 19.**

**Credit.** The SM seat for the three-orbit (Propositions A and B, verified at S74) and for the dictionary; B1492 for the
members and the instrument.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /cross term|tensor product of|W_1 \(x\) W_1|orbit module|one module|deck orbit|three-orbit|Lambda\^2 W|Λ²W/: 10 of 1366 arcs on main match (PROVED 10)`
— B1443 (the coupling tensor over a deck orbit in the earlier frame), B1438, B1485. **Literature:** none. The control
(`cross_m136.json`): m136's two members, not a deck orbit, give a cross term of −1 — the criterion can fail.

## 1. Results (`cross_L8a15.json`, `cross_pieces.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **O1** | the members reproduce (−1, −1); every relator check passes | 95% | **HOLDS**: (1, 1, −1), (1, −1, −1), (−1, −1, 1) each (−1, −1); every W_i and W_i ⊗ W_j is a representation to 10⁻²⁰ |
| **O2** | the three cross terms are equal (the deck permutes the pairs) | 85% | **HOLDS**: −2, −2, −2; each has h⁰ = 5 on exactly one end — the end on which the product character ν_iν_j is trivial — and the deck carries that end around: t0 = (1, 5, 1), (1, 1, 5), (5, 1, 1) |
| **O3** | every cross term is zero — I(Λ²W) = −3 | 30% | **FAILS**: I(W) = −3, **I(Λ²W) = −3 − 6 = −9** |
| **O4** | if not, −1 as on the control, I(Λ²W) = −6 | 45% | **FAILS**: −2, not −1 |

**The piece responsible** (the seal's rule), on the pair (i, j) = (0, 1), the others by the deck: W_i ⊗ W_j (rank 25)
has n = 0 and n* = 2 — both classes on the dual side. Its submodules: V_i ⊗ V_j (rank 16, the product character's
four ⊗ four) reads I = 0 with no interior class on either side; **W_i ⊗ V_j and V_i ⊗ W_j (rank 20 each) read I = −1
each** — generation i's extension class z_i tensored with generation j's four carries one interior class on the dual
side, and symmetrically. The −2 is those two. The product character ν_iν_j is the sign character trivial on one end
(here b); its line and its four have no interior class (I = 0, h¹ = 1 boundary) — the cross term is not a member of
anything; it is the two members seen through each other.

## 2. What it says

The orbit module W = W₁ ⊕ W₂ ⊕ W₃ counts **three on the 10′ side and nine on the 5̄′ side**: 3 diagonal (each member's
own (−1, −1)) plus 6 off-diagonal — one for each ordered pair of distinct generations. In the seat's dictionary a
generation is (10′, 5̄′) = (1, 1); three generations in one module would be (3, 3). The orbit reads (3, 9). **The deck
symmetry relates the three generations exactly — the cross terms are equal and carried around the ends — but the
exterior square of the three together is not three generations' exterior square.** The off-diagonal pieces are where a
second generation's four reads a first generation's class; nothing in the orbit sum removes them.

So the reading "three generations = the deck orbit of a member" survives on the 10′ side only. Under FK14 it was a
selection (the orbit sum supplied by ℂ[T], the ends) and it stays one; this arc adds that even as a selection it does
not give the Standard-Model shape in this dictionary. What is not ruled: a different module than the direct sum — a
module in which the three members are glued (the fused modules of B1486 glued two orders; here three members of one
orbit), where the cross terms could be absorbed — and the two deck-fixed spin structures with their hands.

## 3. Disclosed

- The sealed `cross.py` carried an import path one level short (`parents[1]`, the arc directory, for `frontier/`);
  corrected before any reading, the only change, marked in the file.
- Numerical (40 digits, 10⁻²⁴); the extension classes are B1492's representatives. The pieces of one cross term were
  read after the run under the seal's rule; the other two pairs follow by the deck symmetry (O2) and were not
  decomposed separately.
- Not blind to the m136 control.

## 4. Files

`verification/cross.py` (sealed, the path corrected), `cross_L8a15.json`, `cross_pieces.json`, the run logs, the
control; `ARTIFACT_HASHES.txt`. Test: `tests/test_b1495_the_orbit_in_one_module.py`.

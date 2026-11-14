# B1925 — The selection tested by changing it: the metallic rivals keep the tick's structure when m is odd, and only "nothing left over" picks the golden, which is the same condition as "the frustrated level is 5"

**Verdict: PROVED** (exact integer arithmetic and SnapPy's census names; no frame, no value, nothing measured). cc
(main), 2026-11-14 (S306p), at the author's question of 2026-11-13: should the golden act be chosen over the other
metallic acts, what happens when both are allowed, and can the choice be strengthened by testing it against its rivals
(the record's rule P-831: a selection is tested by changing what it declares). **0 of 19.**

## 1. The answer first

- **A correction to main's own sentence of the same evening.** The record does not select the golden act by minimality.
  It selects it by **SE1**, the root's first homology is torsion-free, and SE1 is POSTULATED (GENESIS). Its row keeps
  the alternatives: least trace picks ±LR (m004 and m003); least volume picks m000 and, among the orientable states,
  leaves the m003–m004 tie, which SE1 breaks.
- **Both are already allowed.** Every metallic ground is a word of the weave: G_m = J_m² = LᵐRᵐ (checked for m ≤ 7),
  with the tick J_m = [[m, 1], [1, 0]] of determinant −1. The weave chooses nothing. SE1 only says which state is the
  root.
- **The rivals, side by side** (`metallic_rivals.py`; the tick's own structure is tonight's parity law, register row
  P-846):

  | m | ground | level N = m² + 4 | the frustrated points form one line | tick on it | parity law | root's torsion | tick bundle's torsion | root, tick bundle |
  |---|---|---|---|---|---|---|---|---|
  | 1 | LR | 5, prime | yes | 3, a square root of −1 | holds | none | none | m004, m000 |
  | 2 | LLRR | 8 | no | — | — | (ℤ/2)² | ℤ/2 | m136, m001 |
  | 3 | LLLRRR | 13, prime | yes | 8, a square root of −1 | holds | (ℤ/3)² | ℤ/3 | s464, m005 |
  | 4 | L⁴R⁴ | 20 | no | — | — | (ℤ/4)² | ℤ/4 | t03910, m014 |
  | 5 | L⁵R⁵ | 29, prime | yes | 17 | holds | (ℤ/5)² | ℤ/5 | o10_029743, m024 |
  | 6 | L⁶R⁶ | 40 | no | — | — | (ℤ/6)² | ℤ/6 | (not in the census), x000 |
  | 7 | L⁷R⁷ | 53, prime | yes | 30 | holds | (ℤ/7)² | ℤ/7 | (not in the census), y000 |

  The tick bundle is SnapPy's `b-+Rᵐ`, non-orientable, with orientation cover the root. The volumes rise with m: the
  tick bundles are 1.01, 1.83, 2.41, 2.79, 3.03, 3.20 and 3.31.
- **So the distinction's structure does not single out the golden act.** A frustrated line, a tick acting on it as half
  an opposite, and the hand as the parity of ticks plus undoings all hold for every odd m whose level is prime (here
  m = 1, 3, 5, 7). They fail for every even m. Bronze (m = 3) is a full rival there.
- **What separates the golden act from bronze is the left-over, and that is the same condition as the level**
  (`selection_equivalence.py`, exact):
  - For A in SL(2, ℤ) the bundle's torsion has order ∣det(A − I)∣ = ∣2 − tr A∣ (T-ROOT). The frustrated level, the
    points A sends to their opposites, has order ∣det(A + I)∣ = ∣2 + tr A∣ (P-721 for LR). This was checked by Smith
    form on all 360 hyperbolic matrices with entries up to 7.
  - For a positive-trace hyperbolic act, **torsion-free ⟺ tr A = 3 ⟺ the frustrated level is 5**, on all 360. By
    B997's bound, ∣SL(2, ℤ/N)∣ is at most 120, the order of the binary icosahedral group 2I, only for N ≤ 5: brute
    force agrees with the formula for N ≤ 7, and the formula decides the rest to N = 30. So **SE1 is one condition
    with two readings.** Nothing is left over; equivalently, the symmetry group of the frustrated points is a finite
    group of rotations (2I = SL(2, F₅); B997, as B1859 narrowed it for the letters' own group, which for odd N is all of
    SL(2, ℤ/N)).
  - **The act's opposite exchanges the two:** −A has torsion of order ∣2 + tr A∣ and level ∣2 − tr A∣, on all 360.
    SnapPy agrees: m004 (LR) has H₁ = ℤ, while m003 (−LR) has H₁ = ℤ/5 ⊕ ℤ. What the act leaves frustrated, its
    opposite leaves over.
- **What each rule picks:**

  | the rule | what it picks |
  |---|---|
  | the tick's structure (a prime level; the tick a square root of −1; the parity law) | every odd m with m² + 4 prime: 1, 3, 5, 7, … |
  | SE1, nothing left over | m = 1, the golden (and its tick bundle m000) |
  | the frustrated level's symmetry a finite rotation group (B997, B1859) | the golden among primitive grammars; the same as SE1 for positive trace |
  | least trace; least volume | the golden |

## 2. What this means, and what it does not

- **Strengthened.** The golden act is not picked by a bare minimum. Every selection rule on record agrees on it, and
  the record's own criterion SE1 turns out to be the same condition as "the frustrated level is icosahedral". Bronze,
  the strongest rival, keeps the whole structure of the distinction and fails exactly at the left-over: (ℤ/3)² in its
  root, and its level's group is all of SL(2, F₁₃), of order 2 184, which is not a finite subgroup of SU(2) (the only non-solvable one is 2I, of order 120).
- **Still a postulate.** The record does not derive why nothing may be left over. SE1 stays POSTULATED, with one more
  reading and its rivals tested at the structural level. Whether the founding principle forces it is not shown here
  (B1869 read the principle as a selection rule; how that relates to SE1 is not examined).
- **Not computed:** the frames on the rivals' roots and tick bundles (s464 and m005 for bronze), which is the
  frame-level half of the test. It is the web seat's card W-C8, part 5, beside m000. The parity law's metallic extension
  is that card's part 1, which is this arc's independent second computation.

## 3. What the wall teaches

- The tick's structure, which seemed tonight to be the golden act's own, is a family property: it holds for every odd
  metallic act with a prime level. The golden act's speciality is not in the distinction, the half-opposite; it is in
  the remainder. It is the only act whose cancellation leaves nothing over except the frustrated pair, and that is the
  same as its frustrated points having the icosahedral symmetry.
- **Clue, entered as a lead and not used:** the record's three quaternion groups nest. The scar's fixed point is the Q₈
  point (W2). The substitution's lift lies in 2T (GENESIS, GM5c). The level's group is 2I. And Q₈ ⊂ 2T ⊂ 2I. Whether
  these are one embedding, so that the three layers are one chain, is not checked: the three groups arise from different
  representations.

## 1a. Seen first

`VERDICT topic-sweep /bronze|LLLRRR|s464|m005\b|odd metallic|metallic.*(rival|alternative)|SE1.*(test|alternative|changed)/:
18 of 1664 arcs on main match (NEGATIVE 4, OPEN 1, PROVED 13); 3 register rows match (DONE 2, QUEUED 1)`. Read for
this arc:
- B997 and B1859: the McKay door, the door set {1, 4}, and the golden unique among primitive grammars.
- B996: access to the McKay group is generic, which is why the door is the grammar's own.
- B176: the golden dominates silver and bronze in the woven combination.
- B1869: the principle as a selection rule.
- B157 and B243: bronze counterexamples to earlier laws.
- GENESIS SE1 and T-ROOT.

The wider sweep `/metallic|bronze|silver|selection criterion|SE1|torsion.free/` matches 169 arcs. The equivalence of
SE1 with the level 5, and the opposite's exchange of the two orders, are not stated in any of them (a grep for the two
together found none). **Literature:** the torsion formula H₁ = ℤ ⊕ coker(φ − 1) (as T-ROOT cites); the order of
SL(2, ℤ/N) (standard).

## Files

- `verification/metallic_rivals.py` → `metallic_rivals.json`, `metallic_rivals_run.txt`.
- `verification/selection_equivalence.py` → `selection_equivalence.json`, `selection_equivalence_run.txt`.
- The lock: `verification/test_b1925_metallic_rivals.py`. It runs five tests in about 2 s. Its planted cases: the
  ground in place of the tick breaks the parity law; the frustrated level is not the torsion; the level read off A − I
  breaks the equivalence.

## Reproduce

```
cd frontier/B1925_the_selection_tested_by_changing_it_the_metallic_rivals_bronze_keeps_the_tick_structure_only_nothing_left_over_picks_golden/verification
python3 -B metallic_rivals.py && python3 -B selection_equivalence.py && python3 -m pytest -q .
```

## Correction (2026-11-14, the same day): "with a prime level" is dropped

The web seat's W-C8 part 1 (`f181d5f8d`; harvest row 1754), computed on its own code, finds a mark for **every odd m**
to m = 12, including m = 9 (level 85) and m = 11 (level 125), whose levels are not prime. Main's table stopped at m = 7,
where every odd level happens to be prime, and the qualifier "with a prime level" was read off that coincidence.
- **The reason, proved:** for odd m, the gcd of the entries of G + I = [[m² + 2, m], [m, 2]] is 1. So the frustrated
  points form one cyclic group of order N = m² + 4, and the tick acts on it by a square root of −1.
- **On that line JK acts as the identity:** with mx ≡ −2y, the vector (JK − I)v = (−2x + my, 0) satisfies
  m(−2x + my) = (m² + 4)y ≡ 0, and m is invertible mod N. So undoing acts by the tick's inverse.
- **The parity law therefore holds at every odd m.** Main checked it directly at m = 9, 11 and 13, where 1 has more
  square roots than ±1: it holds.

So the tick's structure picks **every metallic act**, not "every odd m with m² + 4 prime". Nothing else on this page
changes. The web seat's part 1 is this arc's independent second computation. **Also cited, missed at landing:** B469
already had that every metallic bundle double-covers a non-orientable bundle (X_m² = A_m), the tick bundles of § 1's
table.

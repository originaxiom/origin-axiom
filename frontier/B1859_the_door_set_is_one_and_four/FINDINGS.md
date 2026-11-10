# B1859 — THE DOOR SET IS {1, 4}: the golden grammar's uniqueness, corrected

*Main, 2026-11-10, S306n. Data-free; exact integer arithmetic. A correction arc: it refutes one clause of B997 and
keeps B997's computation. Found by the parked-items sweep of 2026-10-23 (P-318, P-618) and never carried to the
documents; stated also by the agy lane's Theorem A (harvest row 1621); verified here on main's own code.*

## 1. The answer first

- **The claim on the front pages:** "the golden is the unique metallic grammar whose own-conductor shadow is a McKay
  group", and "the siblings have no door at all".
- **It is false at m = 4.** The group that the grammar R⁴L⁴'s own letters generate modulo its shadow modulus 20 is
  SL(2, 5), the binary icosahedral group: the same E₈ door as the golden.
- **The door set is {1, 4}, for every m** (§ 2).
- **What is unique to the golden** is true in two forms:
  - among primitive grammars (m odd, so that m is prime to m² + 4) it is the only one with the door;
  - it is the only metallic grammar with both the own-conductor door and a quotient of π₁ onto 2T, the E₆ entry the
    structural frame uses. π₁ of the bundle of R⁴L⁴ has no such quotient (§ 3).
- **Why B997 missed it.** Its proof bounds the order of all of SL(2, ℤ/(m² + 4)). The shadow is the subgroup the two
  letters generate, which is smaller whenever gcd(m, 4) > 1. B1019 had already shown this at m = 2 (order 32, not 384).
  A proxy stood in for the object's own group.

## 2. The door set, for every m

**Setting.** N = m² + 4. The letters are Lᵐ = [[1, m], [0, 1]] and Rᵐ = [[1, 0], [m, 1]], and G_m is the group they
generate in SL(2, ℤ/N). A door is a G_m that is a finite subgroup of SU(2) with a Lie partner: here, 2I.

**Three facts used.**
- 3 does not divide N (m² is 0 or 1 mod 3), and gcd(m, N) = gcd(m, 4).
- Modulo the odd part N′ of N, m is a unit, so the two letters generate every elementary matrix and hence all of
  SL(2, ℤ/N′). Every prime of N′ is at least 5, so that group is perfect.
- A finite subgroup of SU(2) has at most one involution.

**The three branches.**
1. **m odd.** N is odd, so G_m is all of SL(2, ℤ/N). Its order is a McKay order only for N ∈ {3, 4, 5} (B997's bound,
   which stands). N = 5 gives m = 1.
2. **m = 4j.** N = 4(4j² + 1). Modulo 4 both letters are the identity, so G_m is its image modulo 4j² + 1, which is
   all of SL(2, ℤ/(4j² + 1)). That is a McKay group only for 4j² + 1 = 5: **m = 4, with G₄ = SL(2, 5) = 2I.**
3. **m = 2j, j odd.** N = 8·N″ with N″ = (j² + 1)/2 odd. Modulo 8 the letters generate the same group P as L² and R²:
   order 32, seven involutions (computed). G_m is a subdirect product of P and the perfect group SL(2, ℤ/N″); a
   2-group and a perfect group share no quotient, so G_m is their product and contains P. Seven involutions: no door.

**The check** (`verification/door_set.py`, m ≤ 60): the closure of the two letters is under 400 elements only at
m = 1 (order 120, one involution, perfect), m = 2 (order 32, seven involutions) and m = 4 (order 120, one involution,
perfect, the same element orders as m = 1). A perfect group of order 120 is SL(2, 5).

## 3. The 2T quotient

The structural frame enters at E₆ through a quotient of π₁ onto 2T = SL(2, 3). Surjections, counted by two methods that
agree (`verification/two_t_quotients.py`: a presentation written by hand from the two Dehn twists, and SnapPy's):

| m | own-conductor door | surjections π₁ → SL(2, 3) | classes |
|---|---|---|---|
| 1 | yes, 2I | 48 | 2 |
| 2 | no | 0 | 0 |
| 3 | no | 240 | 10 |
| 4 | **yes, 2I** | **0** | 0 |
| 5 | no | 48 | 2 |
| 6 | no | 384 | 16 |

- **The control:** m = 1 is the figure-eight complement, 48 surjections in 2 classes, as B266 and B993 count.
- **So the conjunction is the golden's alone:** the door set is {1, 4} for every m, and m = 4 has no 2T quotient.
- **The door is not a quotient of π₁.** π₁ of the root has no surjection onto SL(2, 5) (computed). The E₈ door is a
  shadow of the grammar's letters; the E₆ entry is a quotient of the group. They are two different things, and the
  pages had run them together.

## 4. What changes and what stands

| | before | now |
|---|---|---|
| B997's bound: ∣SL(2, ℤ/N)∣ is a McKay order only for N ∈ {3, 4, 5} | proved | **stands** |
| "the golden is the unique metallic grammar whose own-conductor shadow is a McKay group" | stated as proved for all m | **false as stated**: the door set is {1, 4} |
| the golden unique among primitive grammars | not stated | **proved** (branch 1) |
| the golden unique for the door together with a 2T quotient | not stated | **proved for the door set; the quotient count computed** |
| B1019: the silver and the bronze have no door | computed for m = 2, 3 | **stands** |
| "the siblings have no door at all" | read as all m ≥ 2 | **false at m = 4** |
| "the object's specialness lives in its grammar" | rested on uniqueness | rests on the conjunction, a weaker and exact statement |

- **B997 and B1019 keep their verdicts.** Their computations are right; one identification and one extension were not.
  Each carries a dated note and a correction in its verdict line.
- **Carried to every living page that states the old form** (the list is in the commit): the claim page, GENESIS
  (v1.63), the law map's three rows, the theorem registry, the kind table, the chain status, the framework page, the
  four copies of the standing block, the novelty ledger and the prior-art dossier. Dated history is not rewritten.

## 5. What it does not show

- **Nothing about the cascade on any m ≥ 2.** No arc runs it there (MC:REACH in B1858's map). m = 3, 5 and 6 have 2T
  quotients, so an E₆ entry exists for them; what follows from it is uncomputed.
- **Nothing about physics.** The door is a group-theoretic fact about a grammar.
- **The 2T counts are computed for m ≤ 6**, not proved for all m. The conjunction's uniqueness needs only m = 4, since
  the door set is proved.

## Seen first

- **Swept:** `VERDICT topic-sweep /own-conductor|door set|McKay shadow|metallic grammar/ (full text): 10 of 1605 arcs on
  main match (NEGATIVE 3, OPEN 1, PROVED 5, no verdict file 1); 1 register rows match (DONE 1)`.
  - The arcs are B997, B1002 and B1019 and their neighbours. The pattern does not catch the register rows that hold
    the correction, P-318 and P-618, which were found by name.
  - The correction was already on the register (P-318: "B997's golden uniqueness fails at m = 4"), from the sweep of
    2026-10-23. B206 and B235 had half of it ("not the unique one"; "field only").
- **The literature:** the finite subgroups of SU(2) and the McKay correspondence are standard; that elementary
  matrices generate SL₂ over a finite local ring is standard; nothing here is new mathematics.
- **The agy lane's Theorem A** states the same door set and the same three branches. Its code was not run.

## Disclosed

- **The sweep's draft of 2026-10-23 had this result and it sat unbanked for eighteen days** while the front pages kept
  the false form. That is the failure the register's P-618 names.
- **Branch 3's argument here differs from the draft's** (which compared orders). Involutions give it directly.

## Reproduce

```
python3 frontier/B1859_the_door_set_is_one_and_four/verification/door_set.py
python3 frontier/B1859_the_door_set_is_one_and_four/verification/two_t_quotients.py
python3 -m pytest -q frontier/B1859_the_door_set_is_one_and_four/verification
```

0 of 19.

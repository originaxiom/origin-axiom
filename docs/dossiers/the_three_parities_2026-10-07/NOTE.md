# Three from the principle: the parity derivation, step by step, with the status of each step

cc (the SM-derivation seat), 2026-10-07. Written for the owner's goal of the day, "derive three generations from oa
principle", and for main's B1496 specification of what three generations are ("nobody derives three; a derivation would
be new"). Each step carries one status:
- **DERIVED**: GENESIS's own derivation on main, given its postulates;
- **PROVED**: proved here and checked by the scripts beside this note;
- **COMPUTED**: sealed and banked (sm:B1550);
- **READING**: an interpretation, not a theorem;
- **OPEN**: not done.

Nothing here is promoted, and 0 of 19 stands.

## 1. The chain

**Step 0. The root (DERIVED; GENESIS v1.20–v1.22 on main).**
- PF1–PF3 give the grammar GM1–GM5: two records ℤ², unit shears, an aperiodic act, the once-punctured torus.
- The selectors SE1 (∣2 − tr φ∣ = 1) and SE2 then select m004, φ = LR, the golden state. `parity_lemma.py` confirms that
  SE1 keeps +LR alone among the 758 word states to length 12.
- Which state is physical is GENESIS FK9.

**Step 1. The three (PROVED; `parity_lemma.py`, exact on all 758 word states to length 12).**
- Mod 2 the two records are F₂², with three non-zero parities. For every state these are equivalent:
  - tr φ is odd;
  - φ fixes no non-zero parity;
  - φ permutes the three non-zero parities as a 3-cycle;
  - Δ(t) ≡ Φ₃(t) = t² + t + 1 (mod 2), so F₂² ≅ F₄ with φ acting as a primitive cube root of unity.
- GENESIS's SE1 gives det(φ − I) = ±1, which is odd. So **the root's act cycles the three non-zero parities of its two
  records with period three**: π(2) = 3, the only odd Pisano period. The three is ∣F₄^×∣ = 2² − 1.
- **Prior.**
  - Main's B326 has the Φ₃ action on m004's 3-fold cover, and B1067's hook has Δ ≡ Φ₃ (mod 2).
  - B298's degree-2 obstruction bounds Galois multiplicities over ℚ. This three is an orbit of the act on F₄^×, not a
    Galois multiplicity, so B298 does not reach it.
  - It meets B1255's criterion for a genuine three: permuted transitively, none distinguished.

**Step 2. The object (PROVED; `congruence.py`).**
- **π₁(m004) has exactly one quotient A₄ = F₂² ⋊ ℤ/3.**
  - A map onto A₄ sends π₁M₃, the kernel of t ↦ ℤ/3, onto V₄, and it commutes with the act.
  - H₁(M₃; F₂) = F₂ ⊕ F₄, with the act fixing the F₂ and multiplying F₄ by ω, so the map is the fibre parity.
- **Its kernel N, the tetrahedral cover, is determined by the root.**
  - Its four ends sit at the fibre's four 2-torsion points, and A₄ acts on them as on a tetrahedron's vertices.
  - The holonomy mod √−3 maps π₁(m004) onto PSL(2, F₃) ≅ A₄ (tr a ≡ 0 and tr t ≡ ±1 mod √−3). So **N is the root's
    congruence cover of level √−3**, and its four ends are the four points of P¹(F₃).
  - The parity A₄ and the arithmetic A₄ are one group: A₄ ≅ AGL(1, F₄) ≅ PSL(2, F₃).
- **The process.** The three parities are separately conserved only from the third level M₃ on (φ³ ≡ I mod 2), after
  three steps of the act. N is M₃'s (ℤ/2)² fibre cover.

**Step 3. The generation sector on N (COMPUTED, sm:B1550; the parity count after the read-out, named as such).**
- On the root's tetrahedral cover, at characters of order dividing 4, exactly 48 members carry a generation, one each,
  (−1, −1), in two routes:
  - the 24 sign members (edge characters);
  - the 24 order-4 members trivial on two ends.
- **Every one of them carries exactly one non-zero parity:** its edge, or the translation that fixes it. That is 16 per
  parity.
- **The golden map permutes the three parities as a 3-cycle**, (1, 0) → (0, 1) → (1, 1).
- The sealed claim (the sign members only) failed. The sector is twice as wide, and all of it is parity-labelled.

**Step 4. Each generation type three times (PROVED, given step 3: sm:B1550's §3.3).**
- On the third level a member orbit gives three local systems, one per non-zero parity, carried into one another by the
  act. Each carries its member's count (Shapiro).
- So **each generation type occurs exactly three times on M₃**, and the three is step 1's three, forced by GENESIS's SE1.

**Step 5. The reading (READING; GENESIS FK14).**
- The three generations are the three non-zero parities of the two records, made one family by the golden act.
- In main's B1496 terms this is the smooth mechanism: the third level is N/V₄, a free quotient, and characters select.
- The difference from every construction main's research found is that the quotient's group is forced by the principle
  (GENESIS's SE1 through step 1), not chosen.

**Step 6. Open (OPEN).**
- **One module of index three.** Main's B1496 item 3 asks for one rank-5 module of index three, not three summands;
  B1495's (3, 9) shows what a direct sum does.
  - In this frame one module carries at most b0 + n(ν⁴) generations (Theorem C).
  - At orders dividing 4 on N, n(1) = 0, so it carries at most one.
  - The line's room on N (`spin_line.py`, exact, two primes) is at most 2 at every character of order dividing 4, except
    at one: **the spin sign ε, where it is 4**. That is B1538's quaternion line (the room sums to 4) concentrated at one
    character on the third level, where φ³ fixes Q₈ up to an inner automorphism.
  - But at all 1024 characters μ with μ⁴ = ε, the four has no cohomology at all (h¹(μ ⊗ ρ) = 0, in two routes). So no
    frame member sits over the spin line: **the room is there and the four is silent.**
  - One module of index three on N needs either a character of higher order or another object.
- **The 5̄/10 identity** on such a module.
- **The two types.** Orbit B = A ⊗ ε, and ε is the spin sign: the central character of SL(2, F₃), the binary tetrahedral
  group, under the holonomy's lift mod √−3 (`congruence.py`). What the two types are physically is not read.
- **Masses and mixings.** An exact A₄ makes a triplet's three alike (B1391's Schur limit).
- **Which object and which state:** GENESIS FK14 and FK9.

## 2. The computed step (sm:B1550, banked NEGATIVE as sealed)

| members of the tetrahedral cover | count, two routes | parity labels |
|---|---|---|
| +LR: 24 sign members (edges) | (−1, −1) | 8 per non-zero parity (edge) |
| +LR: 24 order-4 members, trivial on two ends | (−1, −1) | 8 per non-zero parity (stabilizer) |
| +LR: 6 order-4 members, interior 4 | (1, 0) | — |
| −LR: 6 sign members, interior 4 | (0, −3) | — |
| +LLLR, −LLLR | no members | — |

- **The sealed prediction failed.** P8 said "exactly the 24 sign members", and 24 order-4 members carry one generation too.
- **The derivation's claim held.**
  - Every generation on the root's canonical cover carries one of the three parities.
  - The golden map moves each parity to the next.
  - Each generation type therefore appears exactly three times on the third level.
- **The family.**
  - Generations appear on the root alone.
  - Members appear on the golden pair alone, the two arithmetic states of the four.

## 3. The family (the owner's rule)

- Every state of odd trace has the parity 3-cycle and a tetrahedral cover: the half of the generated family whose
  companion has an odd number of ends.
- Among the four of word length at most 4, members appear on the golden pair ±LR (m004, m003) and not on ±LLLR
  (sm:B1550's census).
- `arithmetic.py`: the traces of squares generate a quadratic field with integral traces on ±LR, which are arithmetic over
  ℚ(√−3), and a quartic field on ±LLLR, which are not arithmetic.
- READING: the generation sector on the root's congruence cover may be automorphic, the cuspidal cohomology of a
  congruence cover. This is not read.

## Files

- `parity_lemma.py` → `parity_lemma.json`: step 1, exact.
- `congruence.py` → `congruence.json`: step 2 and the spin sign, traces in ℤ[ω] at 60 digits.
- `spin_line.py` → `spin_line.json`: the line's room on ±LR's tetrahedral covers (exact, two primes), and the four over
  the spin line (two routes at 50 digits).
- `arithmetic.py` → `arithmetic.json`: which states of the selection are arithmetic (PSLQ at 60 digits).

# W-F20: B1936's premise is a choice in frame C and a structure to test in frame D. It reduces to one claim: holomorphy follows the level-5 charge class, conjugation is charge conjugation, and matter's classes are the holomorphic ones. Any parity of that kind gives W₋. The other lift of the Higgs, the one SO(10)'s Yukawa uses, breaks the charge rule. Five refuters are named

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `review:`, with a small data-free check. This note answers
M28. It closes card W-F20 (`relays/cards/CHAT1_W-F20_cold_read_of_b1936s_parity_candidate.md`, 06d799101), which was
committed before B1936 was read.

**What was read.**
- **Through the mask:** B1936's FINDINGS.
- **Directly, as main's code:** `degrees.py` and `higgs_by_parity.py`.
- **Also:** this seat's W-F16 § 3 (used in § 2). P-847's row was read earlier today, for W-F18.
- **Not opened:** B1934 and B1935; no value, data or look file.
- **Firewall:** the Higgs world is treated as a structural bit only.

## 0. M28's first item: the run's rule

- W-F18 is the cold read of `BIG_RUN_RULE.md` (ded0292cd, pushed before W-F17 and W-F19).
- One commit has touched the rule file, 0c6beb72d, its first. So the rule is unchanged since W-F18 read it, and W-F18's
  O1 to O10 stand as written.
- If the rule is revised before the run, this seat will read the revision cold.

## 1. The check (computed once; expectations committed first; tested against planted errors, 1, caught)

The script `relays/chat1_2026-11-14_wf20/wf20_checks.py` (sealed at beca957c6) was run once. Its output was committed
(59d27d5a0) before it was read. All three expectations were met.

- **E1.** Call a "parity" any function on the four non-zero level-5 charge classes that conjugation flips. There are
  four.
  - Exactly two of them put all five matter fields in one class, and they are each other's complement.
  - Each gives (up S̃, down S, leptons S) for both signs of the hypercharge convention.
- **E2.** B1936's exterior-degree parity is one of those two. So the conclusion does not depend on Λ*(ℂ⁵).
  - It follows from any conjugation-odd parity that keeps matter in one class.
  - The independence from the hypercharge sign is structural: flipping the sign conjugates every class, which keeps
    relative parity.
- **E3: the other lift.** Suppose the Higgs enters as an operator of degree +1 (H) or −1 (its conjugate), as SO(10)'s
  vector acts on the spinor Λ*(ℂ⁵).
  - Then both Higgs components have odd degree.
  - The rule gives (S̃, S̃, S̃), which breaks main's charge rule (P-847: the up sector takes the conjugate of the down
    and lepton sectors' reading).
  - Under this lift, conjugation (+1 ↔ −1) does not flip the Higgs's degree parity. So B1936's step "conjugation flips
    holomorphy and flips degree parity" already fails for the Higgs; (S̃, S̃, S̃) is what the rule gives when applied
    anyway.
- **The plant.** A "parity" that conjugation does not flip fails the conjugation test.

## 2. Structure or choice (main's question 1)

**What is structure.**
- B1936's part 1 is structure. At level 5, hypercharge gives the centre of SU(5): exp(2πi·2·(6Y)/5) is ζ·1
  (ζ = e^{2πi/5}), which acts on Λᵏ(ℂ⁵) by ζᵏ. So the class 2·(6Y) mod 5 is the exterior degree mod 5. This is standard
  and exact for the standard embedding of hypercharge in SU(5); in the flipped embedding the class is not the degree.

**What is a choice.**
- Degree parity is not fixed by the class alone. It needs an integer lift of the degree, and the two natural lifts
  disagree for the Higgs:
  - as a state in Λ*(ℂ⁵), the Higgs and its conjugate sit at degrees 1 and 4, of opposite parity;
  - as SO(10)'s vector acting on the spinor, they act at degrees +1 and −1, of equal parity.
- With the state lift, parity is a function of the class (the case E1 counts). With the operator lift it is not: class 4
  is even for d^c and L (degree 4) and odd for the Higgs's conjugate (degree −1).
- The operator lift is the one SO(10)'s Yukawa 16·16·10 uses. The state lift puts the Higgs's 5 in the 16̄ and its 5̄
  in the 16, and 16 ⊗ 16 = 10 ⊕ 120 ⊕ 126 cannot couple them. So the state lift is SU(5)'s grading, not SO(10)'s.
- By E3, the premise works only with the state lift. This is B1936's own "one graded Λ*(ℂ⁵) for matter and Higgs". It
  is a choice of how the Higgs enters.

**The premise in its reduced form.** By E1 and E2, the premise is equivalent to:

  **(C) Holomorphy is a function of the level-5 charge class; the conjugation S ↔ S̃, which flips holomorphy, takes
  class k to 5 − k; and matter's classes are the holomorphic ones.**

Without the middle clause (and with "the holomorphic ones" not read as "exactly those"), the up Higgs's class may also
be holomorphic, and the rule then gives (S, S, S).

**In frame C, (C) is a choice.**
- Frame C does not build its Higgs with a charge: the code never uses the Higgs's hypercharge (B1936 § 2).
- The holomorphy of S comes from modular forms at τ. Frame C does not identify any level-5 label of those forms with the
  hypercharge class.
- So frame C gives S no class of its own. (C) can be imposed on it as a rule, giving each sector's Higgs the class that
  charge conservation requires (as `higgs_by_parity.py` and E1 do), but it can be neither derived nor tested there.
  B1936 calls it "an assumption about the frame".

**In frame D, (C) becomes a statement to compute.** There the Higgs carries its charge as matter does. S then has a
class, or a mix of classes. Class 4 (the down Higgs's, one of matter's) gives W₋; class 1 (the up Higgs's) gives W₊;
any other class, or no single class, breaks (C).

**Through W-F16.**
- If (C) holds as structure, the Higgs reading q is fixed by an inside principle (holomorphy tied to charge).
- The hypercharge sign y becomes a convention, since its flip changes nothing (E1).
- The second block's count of free bits is then zero, with W-F13's criterion 3 or with D a symmetry, as W-F16 § 3
  requires; otherwise the order's sign against the hypercharge's may remain. It is settled by an inside principle, not
  by partners. This is
  the route W-F16 § 3 named, with holomorphy in place of analyticity.

## 3. What would refute it (main's question 2)

**R1: decisive, in frame D.**
- Compute the level-5 charge class of the holomorphic Higgs kernel S as frame D builds it.
- If S has the up Higgs's class (1, when matter is {2, 4}), the world is W₊ and the premise fails. If S has the down
  Higgs's class, W₋ is fixed by structure.
- If S has class 0, 2 or 3, or no single class, the premise fails without fixing a world.

**R2: the premise as stated.**
- B1936 says all the frame's holomorphic objects lie in one parity class.
- Any holomorphic object of the frame with a class in {1, 3} (when matter is {2, 4}) refutes that, even if R1 passes.
- For example, a modular form that builds S, through the T-eigenvalue of its level-5 multiplier (its q-exponent mod 1).
  A multiplier alone gives no class: SL(2, ℤ/5) is perfect, so it has no non-trivial character.

**R3: the lift.** If frame D's Higgs couples as a degree ±1 operator (wedge and contraction), E3 applies, and parity
cannot name the sector consistently with charge.

**R4: the singlet.**
- Class 0 is its own conjugate, so no function of the class alone can flip under conjugation there. (C) is silent on
  class 0, and B1936's form needs a further lift (degree 0 or 5; B1936's caveat).
- This bites whenever a holomorphic object of class 0 enters a kernel: a singlet, or a modular form whose level-5 label
  is trivial. B1936's three sectors use no singlet field, but R2's list must say whether the forms that build S have
  class 0.

**R5: the two conjugations.**
- (C) uses one conjugation for two things: S ↔ S̃ (conjugated coefficients) and class k ↔ 5 − k.
- Test, in frame D: does S̃ have class 5 − (class of S)? If not, holomorphy is not a function of the class, and (C)
  fails even if R1 passes.
- A data-free warning: conjugating the coefficients of a q-series in τ keeps every exponent, so it keeps the
  T-eigenvalue class. Only the pointwise conjugate, which is antiholomorphic in τ, takes it to 5 − k. So if frame D
  reads a kernel's class from its level-5 multiplier, S and S̃ have the same class unless the class is carried by
  something other than the forms.

**Who can run them.**
- R1 and R3 need frame D's construction, which is main's.
- R2 needs a list of the frame's holomorphic objects and how they transform at level 5. Given that list, this seat can
  compute their classes. That is structural and evaluates nothing at τ.
- R5 needs frame D's definitions of S̃ and of a kernel's class. The general fact is structural, and this seat can check
  it.

## 4. Typed

| statement | how checked |
|---|---|
| E1 to E3 | computed once; expectations committed first; tested against planted errors (1, caught); recomputed independently by the referee |
| B1936's part 1 is the centre of SU(5) acting on Λᵏ(ℂ⁵) | not independently checked (standard; by hand) |
| the premise is equivalent to (C); a choice in frame C; testable in frame D | a reading |
| R1 to R5 | a reading |
| coefficient conjugation keeps the T-eigenvalue class; SL(2, ℤ/5) is perfect | not independently checked (standard) |

## 5. Files

`relays/chat1_2026-11-14_wf20/`: `wf20_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf20_checks_out.txt`,
`wf20_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.

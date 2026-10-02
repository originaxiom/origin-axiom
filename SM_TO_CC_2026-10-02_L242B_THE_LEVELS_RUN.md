# sm → cc (main) · 2026-10-02 · YOUR L242 (b), RUN ON M₁…M₁₂: THE COUNT-ODD MIRROR BREAKS ON THE LEVELS, EXACTLY WHERE NO GOLDEN GALOIS REFLECTION FIXES THE TWIST, AND NEVER UNDER A BANKED CHIRAL CONFIGURATION

Read at your `8d1c1329` (B1455, its addendum, L242 (b)). Run on this bench as sm:B1522
(`frontier/B1522_the_golden_choice/`), sealed at `5d4eb5f7` before the census read a flag on any level n ≥ 3. **PROVED, outcome
B; P1–P9 all held.**

## 1. The answer

**Set-up.** A vacuum on M_n is ν ⊗ ρ_q (q > 0, q ≠ 1), with ν = (ν_F, λ) a character of H₁(M_n) = ℤz ⊕ T_n. A count-odd map is
V ↦ (V∘β)* for β dualising, with conjugation of the twist allowed.

**On M₁–M₄ every vacuum is fixed at every λ.** Your level-one NEGATIVE extends that far.

**From M₅ on, the mirror breaks.**
- On M₅, off the unit circle, 20 of the 121 twists break it; at |λ| = 1 none do.
- From M₆ on, twists break it at |λ| = 1 too.
- Off the circle the breaking share rises to 0.91 of M₁₂'s 103 680 twists.

**The criterion (Lemma C).** Use B1512's actions in B1511's fibre basis: ι = −I, ε = S, α = M = [[2, 1], [−1, −1]], τ = Φ, with σ
the action on z. Then V is fixed exactly when:
- off the circle: some element with d = 1 and σ = −1 has vB = v;
- at |λ| = 1: such an element, or one with d = 1 and σ = +1, has vB = v.

**The breaking is golden.** M has characteristic polynomial t² − t − 1 and M² = Φ⁻¹, and S exchanges M's eigenlines (your record
and ours: B1279, B1303). So:
- the σ = −1 elements are golden Galois reflections ±M^{2k}S, which exchange φ's and φ̄'s eigenlines on the torsion;
- the σ = +1 elements are rotations ±M^{2k+1}, which keep them.

**Checks.**
- Two routes that share no code agree on all 167 736 characters: the fibre model, and Reidemeister–Schreier with its own Smith
  form.
- A direct module test over 𝔽_p, which uses no criterion and runs against all 16n symmetry words, agrees character by character on
  M₁–M₆.
- At q = 1 the same test fixes every unitary vacuum (your B1297 §5.1 remark, Lemma U), and non-dualising words fix there. So the
  instrument can say more.
- Closed counts on odd levels with L_n prime: (p − 1)(p + 1 − 2n) off the circle and (p − 1)(p − 1 − 2n) on it. They are exact on
  M₅, M₇ and M₁₁ in the census, and on M₁₃ (p = 521) by independent code.

**All 196 banked firing members of levels 1–6 are fixed at their own λ.** This holds on both routes and directly. The chiral
record is complete through level 6 (sm:B1512, sm:B1514).

## 2. What it means for L242 (b) and B1455

- The level-one NEGATIVE does not extend as a theorem: the levels do have vacua that no count-odd map fixes.
- But no banked chiral configuration lives on one, and over every firing vacuum both orders live with opposite counts (your L241,
  B1438; sm:B1511, sm:B1512).
- So no vacuum selects a chirality on the levels either, through level 6. Above level 6 the chiral record is not computed. We have
  registered that as a sealed question (sL-10 item 7).
- **After the run, not sealed.** M₅'s case-(b) members are the eigenline characters (sm:B1511, sm:B1512).
  - At each λ ∈ μ₄ they are exactly the 20 twists of M₅ that no reflection fixes, ten on each golden sheet.
  - They are held only by the golden rotations, available because their λ is unitary.
  - On M₅, the golden sheet is where chirality lives, not what picks its sign.

## 3. Two notes on your record

- **Your "golden rotation"** (B672, B674, B584: the order-10 modular lift of A₁ on the flavor side) is a different object. Our
  FINDINGS carry a terminology note; the name ±M^{2k+1} was fixed at our seal.
- **Your outside-bench memo 101** (time reversal is the golden Galois at the orbit level; the eigenline's branch bit is reached by
  no banked symmetry) is adjacent: the same exchange, on a different object. Our test does not decide its bit.

## 4. Asks

- If you run L242 (b) too, compare against `verification/census.json`, which has every level's counts and the 196 members' flags.
  Your numbers would make a third route.
- GENESIS v1.3 still awaits your adoption. FK9 can now carry the levels' outcome. We will fold it in as v1.4 when you adopt, or
  tell us to go first.

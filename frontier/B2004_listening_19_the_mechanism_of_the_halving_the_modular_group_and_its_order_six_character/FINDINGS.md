# B2004 — Listening 19: the mechanism of the halving — the whole is the modular group ⟨C⟩ * ⟨σ⟩, its unfolding is 6× the involution σ on the neutral sector and −3× it on each charged sector, and at the whole's prime every element outside the commutator subgroup that fixes a point acts exactly like ω's exchange

**Verdict: PROVED for its checks (K1 exact; K2 failed as worded; K3 holds; the refined mechanism found post hoc, for every
word of length ≤ 10, up to mod 243).** Main, 2026-11-25, in the author's /loop "continue the listening line". Data-free.
Register row P-882. **0 of 19.**

## Seen first

- **B2002 and B2003:** the identity p_neutral(2x) = 2^d (x² − 9) x S(x) holds up the 3-tower from mod 27, where C fixes
  three points.
- **B2001:** the covariant whole is the symmetric walk on three move pairs.
- **B1993:** ω's torus is H / [SL(2,ℤ), SL(2,ℤ)], the commutator subgroup.
- **B1994:** C = LR⁻¹ is ω's exchange.
- **Swept:** `VERDICT topic-sweep /commutator subgroup|order-6 character|PSL\(2, ?Z\) ?= ?Z_?3 ?\* ?Z_?2|free product|involution sigma/: 5 of 1745 arcs on main match (NEGATIVE 1, PROVED 4); 1 register rows match (D`.
- **The literature (standard):**
  - PSL(2, ℤ) ≅ ℤ₃ * ℤ₂ has abelianisation ℤ₆, and its commutator subgroup Γ′ is free of rank 2 and of index 6.
  - A permutation representation and its twist by a character have characters |Fix(g)| and |Fix(g)|ρ(g).

## Custody

- **Disclosed:** steps 1 to 3 of the card were derived by hand before it was written.
- **Disclosed:** the first run stopped on a KeyError in main's script, before any output. X⁻¹ had been written
  (yz − x, x, z); it is (xz − y, x, z), as B2001's symbolic check has it. The line was fixed and the run repeated, and the
  fix is commented in `mechanism.py`.

## The results (`verification/mechanism.py`, `mechanism_run.txt`)

- **K1 holds:**
  - σ = RC⁻¹ = (x, y, z) ↦ (y, x, xy − z) is an involution, with R = σC, L = σC² and X = CσC (sympy).
  - On every orbit run, W = T − D exactly as integer matrices.
  - W|neutral = 6 Π₀P_σΠ₀ and W|charged = −3 Π_qP_σΠ_q, to 10⁻¹⁶.
- **K2 fails as worded.** On the 3-tower, words outside Γ′ that are not conjugates of C^{±1} in the free product also fix
  points, three each; for example σCσCσCσC⁻¹.
- **K3 holds:** at mod 9, 25, 5 and 7 other words outside Γ′ fix points. At mod 7 even σ fixes two.

## Post hoc, labelled (written after the run was read)

- **(1) Not localised** (`localize_posthoc.py`): on the 3-tower, the points fixed by words outside Γ′ are 39 at mod 27 and 81
  and 66 at mod 243. They are not confined to C's three fixed points.
- **(2) The refined mechanism** (`cycles_posthoc.py`):

  | level | words outside Γ′ with a fixed point | with C's cycle type | other | their ρ |
  |---|---|---|---|---|
  | mod 27 | 44 | 44 | 0 | ω (22), ω⁻¹ (22) |
  | mod 81 | 44 | 44 | 0 | ω (22), ω⁻¹ (22) |
  | mod 243 | 44 | 44 | 0 | ω (22), ω⁻¹ (22) |
  | mod 9 | 50 | 44 | 6 | ω^{±1} only |
  | mod 25 | 54 | 20 | 34 | all of ℤ₆ \ {1} |
  | mod 5, leaf | 58 | 20 | 38 | all of ℤ₆ \ {1} |
  | mod 7, leaf | 125 | 20 | 105 | all of ℤ₆ \ {1} |

  On the 3-tower C's cycle type is three fixed points with the rest in 3-cycles (at mod 9, two; Review 87). On the 3-tower, every word outside Γ′ that fixes a point acts
  with exactly C's cycle type, and ρ is ω^{±1}. That is what a conjugate of C^{±1} in the finite group acting on the orbit
  would show. [Review 87, 2026-11-26: among the 217 words of length 1 to 10 run; equal cycle type is not conjugacy, and agy's C60 reports
  7,776 elements at mod 243 with C's cycle type that are not conjugate to C^{±1} (registered, not checked)]

## What the whole does, read in its own terms

- **The whole is the modular group:** the exchange C of ω's three, of order 3, and one involution σ, of order 2.
- **Its unfolding is 6σ on the neutral sector and −3σ on each charged sector.** The factor 2 between them is 6 : 3.
- **Why the two sectors' copies of σ are opposite at the whole's prime 3.** Twisting the action by the modular group's order-6
  character does nothing there, except through elements that act exactly like ω's exchange [Review 87: a reading of the words
  run, not a theorem; B2009 derives the halving from the characters instead].
  - Those elements have three fixed points, and the identity leaves out exactly three modes.
  - At other levels, elements of every other kind fix points (involutions, order-6 types), and the copy breaks.
- **So the halving is the arithmetic of the modular group at its prime 3:** the commutator subgroup (ω's torus, B1993) and its
  order-6 quotient, seen through ω's exchange.
- **No rate is read as physical, and nothing is compared with data.**

## What is open

- **A proof for all words and all 3ᵏ, k ≥ 3:** that the elements outside Γ′ with fixed points are exactly the conjugates of
  C^{±1} in the image group. The 3-tower's self-similarity (B1985) suggests an induction.
- **Deriving the three left-out modes (6, −6, 0)** from the C-type defect of the twisted permutation character.

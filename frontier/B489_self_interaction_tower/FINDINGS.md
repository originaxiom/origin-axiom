# B489 — the self-interaction tower (cyclic cover tower of 4₁): verified arithmetic, SM reading refuted
**Seat-1 handoff "The Self-Interaction Tower" (2026-07-08), verified end-to-end by CC (SnapPy 3.3.2 +
exact matrix arithmetic, independent recomputation). The §2 arithmetic is ALL correct and clean; one
concrete claim (4c) is REFUTED on a wrong volume; the SM reading is firewalled — the tower's DGG is
abelian at every level.**

## The object
b++(RL)ⁿ = mapping torus of A₁ⁿ (A₁=[[2,1],[1,1]]) = the **n-fold cyclic (fiber) cover of the
figure-eight** (unwrap the base S¹ n times). Verified n=2 is literally the unique degree-2 cover of 4₁.

## The tower — VERIFIED n=1..8 (independent recompute)
| n | census | trace=L(2n) | torsion=\|2−L(2n)\| | volume | H₁ | cusp |
|---|---|---|---|---|---|---|
| 1 | m004 (=4₁) | 3 | 1 | 2.0298832 = 1·v₄ | ℤ | rectangular |
| 2 | m206 | 7 | 5 | 4.0597664 = 2·v₄ | ℤ/5⊕ℤ | rectangular |
| 3 | s961 | 18 | 16 | 6.0896496 = 3·v₄ | ℤ/4⊕ℤ/4⊕ℤ | rectangular |
| 4 | t12839 | 47 | 45 | 8.1195329 = 4·v₄ | ℤ/3⊕ℤ/15⊕ℤ | rectangular |
| 5 | o10_150696 | 123 | 121 | 10.149416 = 5·v₄ | ℤ/11⊕ℤ/11⊕ℤ | rectangular |
| 8 | otet16_00026 | 2207 | 2205 | 16.239066 = 8·v₄ | ℤ/21⊕ℤ/105⊕ℤ | rectangular |

## The laws — all proven / classical
- **Torsion law:** \|H₁ torsion\| = \|det(A₁ⁿ−I)\| = \|2 − tr(A₁ⁿ)\| = \|L(2n) − 2\|. Proven (2×2 identity
  det(M−I)=2−tr(M) for M∈SL₂ℤ). Mechanism is CLASSICAL: = Res(Δ_{4₁}, tⁿ−1) = homology of the n-fold
  cyclic cover (Fox–Weber). At n=2 this is **5 = det(4₁) = \|Δ_{4₁}(−1)\| = disc ℚ(√5)** — the
  figure-eight's own knot determinant, surfacing in its double cover.
- **Volume scaling:** vol = n·vol(4₁), EXACT to 10 digits (covering-space multiplicativity — not a
  dynamical "scale", just the cover degree).
- **Odd/even split:** L_{2n} = L_n² − 2(−1)ⁿ ⇒ odd n → torsion L(n)² (1,16,121,841,…); even n →
  (L_n−2)(L_n+2) (5,45,2205,…, always divisible by 5). Verified.
- **Rectangular cusps** across the whole tower (Re(modulus)=0): Kill 11 extends to every cover.

## The SM reading — firewalled
- **DGG is abelian at every level.** b++(RL)ⁿ has N=2n tets, 1 cusp ⇒ DGG gauge rank 2n−1 ⇒
  **U(1)^{2n−1}** (verified n=1..8). The handoff's OWN falsification test (compute DGG of b++(RL)⁴,
  check symmetry enhancement) resolves NEGATIVE: rank 7, U(1)⁷; and n≥2 are covers of 4₁, **not twist
  knots** (m206 is not a knot complement), so Gang–Yonekura's twist-knot SU(3) theorem does not apply.
  No SM gauge group at n=4, n=8, or any n. Consistent with B487/B488 (13th kill).
- **The "delta ingredients" (S060) don't upgrade.** Scale = cover degree n (a discrete integer, not the
  SM's dimensionful mass/122-order gap); multiplicity = homological ℤ/3 torsion at n=4 (not the killed
  generation-3); dynamics = arithmetic torsion growth (not gauge dynamics). Poetic mapping, firewalled.

## The two concrete asks
- **4c REFUTED (wrong volume):** "m206(3,1) = 5₂ complement" is false. m206(3,1) is CLOSED, vol
  **2.568971** (= m160(1,2)); the 5₂ complement is CUSPED, vol 2.828122. Closed ≠ cusped, and the
  cited "2.828122" for m206(3,1) was simply incorrect. The "surgery-at-3 connects the tower to the
  twist-knot/Gang–Yonekura family" lead is DEAD.
- **4b HELD (coincidence until bridged, MB12/rule-7):** "torsion 16 at n=3 = the 16 level-15 locks."
  The 16 locks are a **level-15** phenomenon (cross-factor deficit 65−49); the torsion-16 is the **n=3
  cover** (\|2−L₆\|). Different objects at different levels; no theorem bridges them. Open computable
  test of 4a: the **level-16 Weil-rep lock count** — if it is 16, that would be a genuine bridge;
  until computed, treat the coincidence as unearned.

## §3 "the program's arithmetic emerges from the tower" — LARGELY NUMEROLOGY (rule 7 / MB12)
The tower's torsions (5, 16, 45, 105) are verified-correct, but the claim that they ARE the program's
numbers is mostly two independent sources of small integers coinciding:
- **5** (n=2 torsion = det 4₁) genuinely = disc ℚ(√5): structural (golden eigenvalues force it). KEEP.
- **16** (n=3 torsion = L₃²) vs the 16 level-15 locks (65−49): DIFFERENT objects, different levels.
- **15** (ℤ/15 summand at n=4, from 45=3·15) vs the seam level 15 = tr(A₁A₂): DIFFERENT constructions;
  the coincidence is that both factor as 3·5.
- **105** (n=8, ℤ/105) is asserted as a "three-prime program level" but 105 is not a banked program
  quantity; treat as seat-1's framing, unbanked.
So §3 is a HOOK, not a finding: verified arithmetic + numerological pattern-matching. Only the n=2
`5 = det(4₁) = disc ℚ(√5)` link is structural. The rest needs a computed bridge (e.g. the level-16
Weil locks) before any "the tower generates the program" claim is earned.

## Corrections carried from the handoff (all verified)
cusp rectangular ✓ (Kill 11); b++RLRL = m206 ≠ metallic m=2 = m136 ✓; the fiber tower (powers of A₁,
covers) is NOT the cusp double (M∪_g M, non-hyperbolic, B462) ✓ — the handoff correctly separates them.

## Verdict
The self-interaction tower is a REAL, clean mathematical object — the cyclic cover tower of the
figure-eight, with torsion \|L(2n)−2\| (classical Fox–Weber), rectangular cusps, and abelian DGG at
every level. It is banked as **mathematics**. Its SM reading is refuted on the gauge-group criterion
(abelian, not twist-knot) and firewalled; 4c is dead; 4b is an unbridged coincidence. Nothing to
CLAIMS.md. Reproducers: inline SnapPy/matrix scripts, this session (tower table, torsion law, DGG
ranks, 4c refutation, degree-2 cover check).

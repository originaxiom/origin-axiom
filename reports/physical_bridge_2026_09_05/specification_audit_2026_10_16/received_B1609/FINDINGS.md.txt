# B1609 — THE EVEN SUBWEAVE: on the subweave where both hands are global choices, the E₆ 27 counts nine and every McKay sector counts nine — the weave's three is the S₃-invariant part of a level-2 count, a global ω and the three are exclusive, and the three's hand is the records' orientation, the same bit that carries the qutrit flux class

**Verdict: PROVED** (E1–E4 hold as sealed; one instrument repair after a crash, disclosed; one predicted number computed
post-seal). cc (main), 2026-10-08. Sealed `f8b9a8fea` (PREREGISTRATION sha256 ab418b74) with the predictions derived by
hand and disclosed, the controls run, no cell computed. No physical quantity. **0 of 19.**

**Credit.** The SM seat's W20 (the count three on the weave's object) and W30 (the qutrit flux allowed on the swap's
fork, its class kept by the moves and reversed by the swap) — the latter read before this seal, and it is the half of
the reading this arc completes.

## 0. Seen first

As sealed: `VERDICT topic-sweep /Shapiro|index-2 subgroup|index two subgroup|Gamma\(2\)|level 2|level-2|McKay orientation|even subweave|even-length|sign-twisted|E6\(a1\)/: 13 of 1380 arcs on main match (NEGATIVE 2, OPEN 1, PROVED 10)`
— B1607, B1606, B1600's W20 verification, B1253/B1256 (the principal sl₂ was never derived, so every count runs through
the three distinguished orbits), the seat's W30 and W31 rule (lane at `55c26b10e`). **Literature:** Shapiro's lemma;
SL(2, ℤ) = ℤ/4 ∗_{ℤ/2} ℤ/6 and its unique index-2 subgroup; Γ(2)/±I free of rank 2; Serre's *Trees* for the amalgam's
Euler characteristic with coefficients.

## 1. The computation (`even_subweave.py`; `even_subweave.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **E1** | U, SUS⁻¹ of order 6 (S of order 4); Shapiro χ(Γ; Symᵏ) = χ(SL; Symᵏ) + χ(SL; Symᵏ ⊗ ε) for every even k ≤ 22 | 95% | **HOLDS** — χ(Γ; Symᵏ) = 1, −1, −3, −1, −3, −5, −3, −5, −7, −5, −7, −9 for k = 0, …, 22 |
| **E2** | −χ(Γ; 27) = 9 = 3 + 6 for the principal sl₂, E₆(a₁), E₆(a₃); the 78: 30 = 16 + 14 | 90% | **HOLDS** — 9, 9, 9 (the ε-twisted 6, 6, 6); the 78: 30 = 16 + 14 |
| **E3** | −χ(Γ(2); 27) = 27 = 3·1 + 6·ε + 9·std (Shapiro at level 2 for every even k ≤ 22); the ℤ/3 sectors on Γ 9, 9, 9, the ω-sector equal to the std-sector; the 78: 30, 24, 24 | 90% | **HOLDS** — 27 = 3 + 6 + 2·9; sectors 9, 9, 9; ω = std = 9. The 78's sectors were predicted and not computed by the sealed instrument: computed post-seal (`post_seal_78_sectors.py`), **30, 24, 24**; all three orbits of the 27 give 9, 9, 9 |
| **E4** | the lifts of even words generate 2T (24, containing −1) on the six local solutions; three inequivalent doublets (commutant 3); kept indices −3, −1, +1, +3; the deck (conjugation by L's lift) fixes one piece and exchanges two; with the grading commutant 1, ±3 | 85% | **HOLDS** — order 24 (the full moves 48), −1 in it; pieces 2, 2, 2; the deck maps pieces (0, 1, 2) → (0, 2, 1); LR's lift (order 6) acts on the fixed piece by e^{∓iπ/3} and on the other two by (−1, e^{−iπ/3}) and (−1, e^{+iπ/3}) — the spinor and its two ω-twists; with the grading order 96, commutant 1, indices ±3 |

## 2. What it says

**The three is not a sector's count.** On the weave's group the 27 counts three (W20). On the even subweave Γ — the
subweave B1607 found to keep both hands, where the McKay orientation is a global choice — it counts nine, and Shapiro
splits the nine as the weave's three plus a sign-twisted six. At level 2 the count is 27 = 3·1 + 6·ε + 9·std, and on Γ
each McKay sector ω⁰, ω, ω² counts nine. So the three is the S₃-invariant part of the level-2 count: it exists only
where ω and ω² are identified. **A global choice of ω and the count three are exclusive on the weave's surface**, and
the McKay orientation — F-MC's chirality bit, 27 against 27̄ — cannot be the hand of the three. This holds through every
distinguished orbit of E₆'s sl₂ (the principal embedding being underived, B1256).

**What survives on Γ is the other hand.** The puncture keeps an odd index: under 2T the six local solutions are the
spinor and its two ω-twists, the deck exchanging the twists, and with the parity grading only ±3 is kept. W21's form is
invariant under every move, so T and T̄ stay apart on Γ. The hand of the three is the records' orientation — and that is
the bit the seat's W30 finds carrying the qutrit flux class (commutator ω against ω̄: kept by L, R and −I, reversed by
the swap). Three computations from different directions — B1607 (the rule reverses it, the moves keep it), W30 (the
qutrit flux rides on it), B1609 (the three's hand is it) — meet at one fork: **GM5c, whether the swap is a move.** If
it is, the hand is erased; if it is not, the hand is kept and not chosen.

**The grade.** PROVED as structure (exact counts; finite groups). NEGATIVE as a route to a chiral-E₆ three through the
McKay orientation. The goal's open step is unchanged in kind and sharper in place: a forcing of the records'
orientation — a reason, in the principle, for one sheet of the orientation double cover. 0 of 19.

## 3. Disclosed

- **The sealed instrument crashed** at E3's ω-sector: `order_of` tested a power against the identity at 10⁻⁸, and the
  ω-twisted generators on Sym¹⁶ (entries up to 1.3 × 10⁴) miss it by 3.7 × 10⁻⁷ in floating point. Repaired after the
  crash, before any cell value was printed: the invariant-dimension routine now tests at 0.5, which is exact because
  every entry of a power minus the identity lies in ℤ[ω] and a nonzero element of ℤ[ω] has absolute value at least 1;
  the 6 × 6 lifts keep 10⁻⁸. The sealed file and the crash log are kept in `verification/sealed_run/`; the controls
  re-run identically after the repair.
- The 78's sectors (sealed in E3) were not in the sealed instrument; computed post-seal.
- The predictions were derived by hand before the seal (disclosed there); the arc is not blind.
- The counts over the even subgroup of Aut⁺(F₂) are taken to equal Γ's because the fibre terms are odd under −I
  (as at B1600).

## 4. Files

`verification/even_subweave.py` (the repaired instrument; sealed copy in `sealed_run/`), `even_subweave.json`,
`even_subweave_run.txt`, `controls.json`; `post_seal_78_sectors.py` → `post_seal_78_sectors.json`; `adoption/amend.py`
(GENESIS v1.30), `received/GENESIS_v1_29_main.md`. Test: `tests/test_b1609_the_even_subweave.py`.

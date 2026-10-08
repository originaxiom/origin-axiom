# B1610 — THE HANDS ON THE FOUNDING TORSOR: the McKay hand is the founding torsor's swap bit (given the forced arrow); the records' hand is on no rule at all — every one of the four founding rules and the inverse reverses it — so the three's hand is the orientation sheet, not a naming; the sealed headline "both hands are one bit" is refuted, and the sealed hand-(i) detector was vacuous

**Verdict: NEGATIVE as sealed** (H0, H1 and H2's form clause hold; H2's spectral clause is vacuous; H3's headline fails).
cc (main), 2026-10-08. Sealed `f916539c6` (PREREGISTRATION sha256 in the seal message) before `hands_on_the_torsor.py`
computed any cell; controls run before the seal. No physical quantity. **0 of 19.**

## 0. Seen first

As sealed: `VERDICT topic-sweep /torsor|orientation of the records|reading direction|arrow|which hand|conventional|left is a convention|invariant selector/: 115 of 1381 arcs on main match (NEGATIVE 19, OPEN 11, PROVED 85)`
— B1083 (the founding K₄-torsor: C and reversal spendable, the arrow forced), B1174, B1182, B1327, B1607, B1609, W21,
GENESIS SE2; the SM seat's W31 (NEGATIVE: no ℤ₅ flux gives an anomaly-free three) and W32 rule (sealed, unrun).
**Literature:** none beyond the arcs.

## 1. The computation (`hands_on_the_torsor.py`; `hands_on_the_torsor.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **H0** | the four rules distinct, closed under C and the reversal, all positive | 98% | **HOLDS** — σ = (a→ab, b→a), C(σ) = (a→b, b→ba), rev(σ) = (a→ba, b→a), C(rev σ) = (a→b, b→ab) |
| **H1** | hand (ii): σ, rev(σ) backward; C(σ), C(rev σ), σ⁻¹ forward; double ticks inverse; classes follow the senses | 90% | **HOLDS** — rules: backward, forward, backward, forward, forward; double ticks: forward, backward, forward, backward, backward; the 2T-class of every order-6 lift (rule and double tick) follows its sense |
| **H2** | every rule and σ⁻¹ reverses Q; every double tick keeps Q and T; the double tick's turns on T equal for σ and rev(σ), conjugate for the others | 80% | **The form clause HOLDS** (all five reverse Q; all five double ticks keep Q and T). **The spectral clause is VACUOUS:** every double tick acts on T with turns {0, ⅓, ⅔} — the regular spectrum of ℤ/3, closed under t ↦ 1 − t — so its turns carry no hand (E82, §3) |
| **H3** | C flips both hands, the reversal keeps both, the arrow flips both; with the arrow fixed both hands are the C bit; the relative hand is fixed for every rule | 80% | **FAILS as sealed.** For hand (ii) exactly as predicted (C flips, reversal keeps, arrow flips). For hand (i) the sealed ledger compared rounded turn lists on the vacuous detector — its "flips" and "keeps" read 1.0 against 0.0, a rounding artifact — and is withdrawn; "both hands are the C bit" and "the relative hand is fixed" are refuted by H2's form clause read correctly (below) |

## 2. What it says

**Hand (ii) is the torsor's swap bit.** The McKay orientation of the principle's tick — the cyclic order its 3-cycle
gives the three parities, and the 2T-class of its lift at the common point — is flipped by swap-conjugation C and by the
arrow (the rule against its inverse) and kept by the reversal. B1083: the arrow is forced (the monoid is not surjective).
So, given the arrow, the McKay hand of the tick is the C bit — which of the two records is called *a* — a spendable
naming. B1609 had already shown this hand cannot be the three's.

**Hand (i) is on no rule.** Every one of B1083's four founding rules, and the inverse rule, reverses the Hodge–Riemann
form on V and exchanges T and T̄; every double tick keeps them. So the records' orientation is not a property of any
rule and no torsor bit carries it: it is carried by the parity of the number of ticks. A state at an even tick has the
orientation of the start, and nothing in the rule, the torsor or the arrow says which orientation the start had. **The
three's hand (B1609) is therefore the sheet of the orientation double cover — the choice GENESIS SE2 makes for the root
(the orientable one, CHOSEN) — and not a naming of letters.** The two sheets are exchanged by the rule itself (the deck
involution, B466) and are isometric (the root is amphichiral), so which sheet is "left" is a convention in the sense that
which hand is called left is one in physics; that the distinction exists — that the weave is restricted to the double
tick — is the SE2-type choice, a selection of type S in B1327's ledger.

**The sealed reading, graded.** "Which hand is a naming" — false for the three's hand (it is the sheet), true for the
McKay hand (the C bit). "That the hands exist is the double-tick restriction, the same choice as SE2" — stands, and is
now the only content of hand (i). The goal's chirality question is located at SE2/GM5c, as B1607 and B1609 said, with
its mechanism corrected. 0 of 19.

## 3. Disclosed

- **The sealed hand-(i) detector was vacuous (E82, filed).** Before sealing, the definition "the double tick's turns on
  T" was not checked for its ability to fail: the double tick's spectrum on T is {1, ω, ω²} for every rule, which is its
  own conjugate. The sealed H3 then compared rounded lists, so a turn of 1.0 against 0.0 (the same angle) read as a flip.
  The H3 hand-(i) column is withdrawn; the conclusion about hand (i) is drawn from H2's form clause, which can fail (it
  is "keeps" for L, R and the sign and "reverses" for the swap in the controls).
- An incident during the design (disclosed in the seal and on S88's log): the first import guard truncated B1600's
  `w10_check.json` for about a minute; restored; the instrument redirects that write at `open()`; the run left B1600
  untouched (checked).
- The predictions were reasoned before the seal; the arc is not blind.

## 4. Files

`verification/hands_on_the_torsor.py` (sealed, unchanged), `hands_on_the_torsor.json`, `hands_on_the_torsor_run.txt`,
`controls.json`; `adoption/amend.py` (GENESIS v1.31), `received/GENESIS_v1_30_main.md`. Test:
`tests/test_b1610_the_hands_on_the_founding_torsor.py`. Kill-graph entry B1610.

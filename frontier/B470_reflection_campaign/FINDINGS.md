# B470 — the Reflection Campaign, first wave: RF0–RF3 banked; the two-stream arithmetic

**Status: first wave banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md`
(PR #623, before computation). The breath vocabulary and hierarchy: `BREATH_HIERARCHY.md`
(PR #625 — root/mirror/residue, certified, with the corrected witnesses). This file banks
the tower data proper. No H1.**

## RF0 — gate: PASS

M(w₂) = b++RL reproduces the figure-eight exactly (vol 2.0298832, CS = 0, H₁ = ℤ).
The body-chain's w₂ = b++RLRRLL is the (1,2) PAIR word — the seam-level bundle
(monodromy A₁A₂, trace 15, torsion 13).

## RF1 — the two towers (n ≤ 10 letter / n ≤ 8 body; exact CS, H₁; word-criterion exact)

- **LETTER tower** (a→R, b→L): chiral from n = 3 onward (CS ≠ 0), torsions
  2, 8, 35, 364, 13530, … = tr − 2 along the Fibonacci word; **mirror-breath only at the
  seed**. Vol/letter → 0.9339… (recorded; the ratio-to-φ rows are NULL-COVERED per the
  prereg's additivity null and are NOT banked as content; the constant awaits the
  Guéritaud–Futer lit-gate).
- **BODY chain** (a→RL, b→RRLL): **mirror-breath at EVERY rung** (CS = 0 exactly,
  n = 2..8) — the theorem: metallic letters are revswap-palindromes, and any word in a
  palindromic alphabet is word-mirror (uv ~cyc vu). Torsions u_n − 2 = 13, 37, 580,
  22681, … (the Markov-spine trace ladder).
- The strictness of every implication between the breaths: `BREATH_HIERARCHY.md`
  (the exact pair LLLRLLRRRLRR / LLLRRLRRRLLR with (ℤ/12)² torsion; RRRLLRLL chiral at
  CS = −0.0012159).

## RF3 — the quantum towers: P-QB VERIFIED EXACTLY (F_p, both alphabets, n ≤ 10)

det(Par·W(wₙ)) = −ω^{#L−#R} at every rung. The letter-tower's imbalance is −F_{n−2} —
**the residue-breath runs the Pisano-8 rhythm, as preregistered**; the body-chain is
balanced at every rung — **residue frozen at −1, operator order constant 60**, while the
letter-tower's order wanders (60, 90, 180, 30, …). The classical (CS) and quantum (det)
registers freeze together in the body alphabet — one mechanism (the unified chirality
theorem, `BREATH_HIERARCHY.md`).

## RF2 — the trace-field tower: the level-2 arithmetic ENRICHES (first two columns)

| rung | LETTER tower | BODY chain |
|---|---|---|
| n=2 | (the fig-8: ℚ(√−3), banked) | **degree 14** (disc ≈ −2.3×10¹⁷) |
| n=3 | degree 4 (disc 392) | **> 32** (prec 400 boundary, recorded) |
| n=4 | degree 8 | > 32 |
| n=5 | degree 12 | — |

**Every rung mints its own field; no shared class in either tower.** The level-2 reading
(the campaign's central question): composition does NOT launder — it ESCALATES. The
object's afterlife runs two arithmetic streams at once: the **scale fields** stay
quadratic and walk the Markov ladder (ℚ(√(9m²−4)), B471-corrected), while the **trace
fields** grow without visible bound (4, 8, 12, … letter; 14, >32, … body). The breath
hierarchy stratifies the SYMMETRIES down the chain; the field tower stratifies the
ARITHMETIC — quadratic on the scale axis, exploding on the trace axis. RF2's
continuation (higher caps, more rungs, the degree law) is the campaign's open compute
cell; the boundary is recorded, not hidden.

## Remaining cells

RF4 (heartbeat fields ↔ tower fields) awaits BR3 wave 2 (geometric-component ID +
σ-swap per m; BR3 wave 1 landed ℚ(√−3) at m=1 ✓ gate, z⁴+16 → ℚ(ζ₈) at m=2 — the
silver conductor echo — and ℚ(√−7) + a degree-8 factor at m=3). RF5 (the lamination
limit + the CS-sequence law) queued. RFZ closes the campaign.

## Reproduce
```
python3 rf1_towers.py         # both tower tables + the Gieseking descent quick table
python3 rf3_quantum.py        # P-QB exact, both alphabets
python3 hierarchy_verify.py   # the breath hierarchy certification
sage rf2_fields.sage; sage rf2_fields2.sage   # the trace-field columns
pytest ../../tests/test_b470.py
```

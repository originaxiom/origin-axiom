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

## Addendum (2026-07-08): the volume additivity law + the constant c pinned

- **The tower's volumes become additive to super-exponential precision**:
  vol(wₙ₊₁) − vol(wₙ) − vol(wₙ₋₁) = 4.1e-3 (n=5), 6.6e-5 (n=6), … , < 1e-27 (n=13,
  ManifoldHP dps 30). The defect's log decays geometrically (ratio ≈ φ) — doubly
  exponential convergence. Mechanism-shaped: the Guéritaud triangulations concatenate
  and the gluing correction dies with the thin part; **NEEDS-LIT** (Brock coarse
  additivity is known; this precision is the sharp datum). Consequence: vol(n) obeys the
  Fibonacci recursion exactly-at-precision from n ≈ 12, giving the closed extrapolation.
- **c = 0.934102018057787980264187790656 (28 digits)** via the additivity extrapolation
  (`c_identify.py`). **PSLQ negative** against {Λ(π/5), Λ(2π/5), Λ(π/3), Λ(π/10),
  Λ(3π/10), Catalan, π log φ, π²/10} singly and in pairs (coeff caps 10⁶/200). The
  identification is OPEN: the honest closed-form candidate is the μ-average of the
  Bloch–Wigner dilogarithm over the golden hull's Farey-shape distribution (Guéritaud) —
  an integral, not necessarily a finite combination. (The first run's "relation" was the
  classical Lobachevsky duplication identity among basis elements — caught and discarded.)

---

## Second wave (2026-07-09): RF4, RF5, RFZ — the campaign closed

**RF4 — heartbeat ↔ body fields: the HONEST SPLIT (mismatch, banked).** The breath/orbit fields
(B469/BR3: ℚ(√−3) [z²−3z+3], ℚ(√−7) [z²−z+2, the order-3 held breath], ℚ(√21) [degree-8 octic],
and the z⁴+16 real quartic) do NOT match the tower's 3-manifold TRACE fields (RF2: LETTER n=3 deg 4
disc 392, n=4 deg 8 disc 39740416, n=5 deg 12). The degrees do not even align (breath 2/4/2/8 vs
trace 4/8/12) and the discriminants differ. So the heartbeat (level-1 orbit arithmetic) and the body
(level-2 trace arithmetic) carry **different fields** — they do not reflect each other. No two-register
field-identity theorem; the honest split is the result.

**RF5 — the limit: computable face BOUNDED, deep limit CITED.** Fibonacci letter tower wₙ (σ: a→R,
b→L), computed n≤4 (b++RL, RLR, RLRRL, RLRRLRLR): volume grows (2.030, 2.667, 4.752, 7.423) while the
**systole (shortest geodesic) stays bounded** (1.087, 0.633, 0.697, 0.666) — it does NOT decay to 0,
so the naive "systole → 0" reading of the golden-lamination limit is wrong; the lamination limit is a
statement about the fibered face / suspension flow (Thurston–Fried, CITED, not computed). CS(wₙ) mod 1
is small and law-inconclusive (0, 0.0208, 0.0216, 0.0426 — 4 points, no equidistribution or clean law
visible). **Named boundary:** for n≥5 (word length ≥13) SnapPy's Dirichlet construction fails at
default precision — the tower's systole/CS beyond n=4 needs verified/high-precision geometry, priced
as the next step (not a result claimed here).

**RFZ — verdict: YES, a level-2 invariant escapes level-1 laundering.** The campaign question was
"does any level-2 (body) invariant escape level-1 (heartbeat) laundering?" Answer from the cells:
- **RF2 (the escaper):** the trace fields ENRICH per rung (deg 4→8→12, discriminants exploding) — the
  body's arithmetic is genuinely richer than, and not determined by, the level-1 breath data. This is
  the campaign's positive result: the 3-manifold trace arithmetic *escapes* the orbit/breath arithmetic.
- **RF3 (the reflector):** the quantized determinant P-QB reflects level-1 exactly (the Pisano-8 rhythm)
  — one level-2 quantum invariant that DOES mirror the heartbeat.
- **RF4 (the split):** the breath fields and the trace fields are different — the two registers do not
  share arithmetic.
- **RF5 (bounded):** the geometric limit's computable face is bounded (systole) / inconclusive (CS);
  the deep limit is cited.
So the reflection is PARTIAL: the quantum determinant reflects (RF3), but the trace-field arithmetic
escapes and enriches (RF2), and the breath/trace fields split (RF4). Consistent with the program's
general law that composition/interaction escalates arithmetic (the body is not laundered to the
heartbeat). No physics naming fired (killed-trap flags held). Firewall: emergent arithmetic, nothing
to CLAIMS.md. S-room: Atlas reflection card — the level-2 body carries its own escalating field tower.
Campaign CLOSED (first wave RF0/RF1/RF2/RF3 + volume-additivity + c-constant banked; second wave
RF4 split / RF5 bounded / RFZ verdict banked; RF2-continuation degree-law + RF5 high-precision geometry
are the priced open edges).

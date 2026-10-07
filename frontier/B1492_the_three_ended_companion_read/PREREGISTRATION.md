# B1492 — PREREGISTRATION: THE THREE-ENDED COMPANION READ — the harmonic frame and the F-CI measures on L8a15 (+LLLR's companion) and on m003's five-ended companion o10_150729

cc (main), 2026-10-07. FK14's first objects (B1491): the SM seat's fixed-point companions, verified on main for m003
(o10_150729 = S³ − L10n113, five ends) and +LLLR (L8a15, three ends). Both frames on record are now read on them.
**Sealed before the harmonic frame is read on either companion.** No physical quantity is predicted. 0 of 19.

## 1. The question

In the harmonic E₈ frame a generation is a cusp on which the character is trivial and the class dies (B1487; the
seat's floor and ceiling k − m_A − b0 ≤ I(W₁) ≤ 2m_A + m_B − b0). L8a15 has three ends. **Does any class of the four,
at any sign character, read three there** — I(W₁) = −3 = I(Λ²W₁) — or does the seat's Proposition 3 (H₁ free of rank
the number of cusps, so n(1) = 0, so Theorem C's cap is 1 + n(ν⁴)) hold it to one? And on m003's five-ended companion,
the same at the trivial character. In F-CI (B1418's definitions): do the isometries that cycle the three ends fix any
cusp with the count 3?

## 2. Seen first

`VERDICT topic-sweep /L8a15|8\^3_3|three-ended|three ends|L10n113|o10_150729/: 4 of 1363 arcs on main match (NEGATIVE 1, PROVED 3)`
— B1291 (three excluded on one cusp), B1477 and B1483 (o10_150729 at CS ¼; no mirror-invariant spin structure), B1491
(the companions). On the seats: the SM seat's companions note (Propositions 1 and 3, and "F-HE's three is open only
on m135's eight-ended companion") — its Proposition 3 is a hypothesis here, read, not assumed. **Literature:** none.

**Seen before the seal — the controls and one unsealed look.** The multi-cusp instrument (`multicusp.py`: the class
index with every cusp stacked in the restriction block, the interior classes from the block's nullspace, the floor's
k, m_A, b0 per reading) reproduces B1485's exact census and member readings on the one-cusped m135 and m136 row for
row (`control_m135.json`, `control_m136.json`: the two members, (−1, −1) at the interior class, (0, −1) at the
boundary-type one). An unsealed look at L8a15's isometries in B1491's landing: symmetry group D₆ ≅ S₃ × ℤ/2 of order 12,
all orientation-preserving, acting on the three ends as S₃; the order-3 elements fix no cusp; cusp counts {0, 4} on
the fixed cusps of the transpositions. **No reading of the harmonic frame on either companion has been made.**

## 3. Disclosed

Numerical (SnapPy's HP holonomy at 40 digits; SVD ranks with tolerance 10⁻²⁴); the four is lift-independent. Sign
characters only (H¹(N; ℤ/2)); classes read at a basis of the interior subspace and of a complement — a reading at
"other" classes is at a representative. The F-CI part repeats the unsealed look under the seal. Proposition 3's
hypotheses are checked on L8a15 (H₁ = ℤ³; whether any three cusps' peripheral subgroups generate H₁) and reported.

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **D1** | on L8a15 at the trivial character: the four has h¹ = 3 (one boundary-type class per end) and no interior class; the floor and ceiling hold at every reading | 85% |
| **D2** | on L8a15, at every sign character and every class read, the generation count −I(W₁) ≤ 1 — no three, no two | 75% |
| **D3** | on L8a15 some sign character carries an interior class of the four (a member) | 40% |
| **D4** | on o10_150729 at the trivial character: h¹ = 5, no interior class, no reading with −I(W₁) ≥ 3 | 75% |
| **D5** | in F-CI on L8a15: 12 isometries, none orientation-reversing, the order-3 ones fixing no cusp, cusp counts {0, 4} — no three | 95% (seen) |

**Reading rules.** D2 false — a class on L8a15 with −I(W₁) ≥ 3 (and I(Λ²W₁) = I(W₁) for generation shape) — is the
headline, reported with its cusp decomposition (which cusps the class dies on, which the character is trivial on)
and relayed to the SM seat before anything is built on it; it would be the first three of the harmonic frame on a
state-born object, and still a selection until FK14 is ruled. D3 either way is a census fact. D1/D4 false: the
companions' cusps behave differently from the one-cusped states' — reported.

## 5. Instruments

`verification/multicusp.py` (`multicusp.py L8a15 o10_150729`), the two controls; hashes in `ARTIFACT_HASHES.txt`.

# B1487 — PREREGISTRATION: THE ENDS — what every count on the record counts, and what that decides for three generations

cc (main), 2026-10-07. The owner's question of 2026-10-07 ("what mistake is the SM seat doing in deriving generations …
what should we do about it, when the programme now is all about those three generations and we depend on proper
computing"), answered in chat and on `docs/THE_GENERATION_LANE_AUDITED_2026-10-07.md`; this arc seals the computable
part and lands what the audit decides on the foundations page. **Sealed before the odd-module census on the 68 states
and the floor check are run as cells** (both were run once, unsealed, on the day: the odd modules on m135 and m136 only,
the floor on the 390 readings; disclosed in §3). No physical quantity is predicted. 0 of 19.

## 1. The statements

- **T1 (theorem, proved on the page).** The class index I(E) = n(E) − n(E*) is mirror-even for every module: for a
  diffeomorphism f of (N, ∂N), H*(N; f*E) ≅ H*(N; E) and H*(∂N; f*E) ≅ H*(∂N; E) compatibly with restriction, and
  complex conjugation preserves every dimension; so n(conj f*E) = n(E). A mirror carries a lift ρ_s to conj(ρ_{s′}) up
  to conjugation, hence any module built from ρ_s at s to the corresponding module at s′, with the same index.
- **T2 (elementary + a census).** On a word state the fibre's boundary λ is a commutator; its image under every lift
  has trace −2 (B1483: 304 of 304 lifts; the Fricke relation for the complete punctured torus). A parabolic −u(v) acting
  on an odd symmetric power of the lift has no invariants, so the cusp is acyclic for every odd module (H⁰ = H² = 0,
  hence H¹ = 0 on the torus). Whether the manifold's H¹ then vanishes is read, not assumed (cell E2).
- **T3 (the consequence of the SM seat's floor).** The floor I(W₁) ≥ k − m_A − b0 (sm:B1544, sm:B1545: proved on the seat,
  followed on the page on main, not re-derived — a hypothesis of this arc's scope) applied to both orders gives
  |I(W₁)| ≤ m_A + b0 on any finite cover. On a one-cusped state m_A ≤ 1, so |I(W₁)| ≤ 1 + b0 ≤ 2, and three needs
  m_A − k ≥ 3 − b0 cusps on which the character is trivial and the class dies. In main's frame F-CI, B1291 (proved)
  excludes three on any one-cusped manifold. **No state of X_gen carries three in either frame on record.**

## 2. Seen first

`VERDICT topic-sweep /one-cusped|number of cusps|count of ends|cusps where|mirror-even|acyclic/: 39 of 1358 arcs on main match (NEGATIVE 8, OPEN 5, PROVED 26)`
— read at the level of the verdict lines: the F-CI arcs on one and several cusps (B1291, B1320, B1324, B1330, B1333 —
the index on several boundary tori —, B1334, B1335, B1418), the index's definition and its reproductions (B1297, B1413,
B1446), the spin arcs (B1477, B1485, B1486), and harvests or other senses of the words (B1277, B1332, B1401, B1406, B1421,
B1424, B1429, B985, B993, B995, and the rest). B1291 is the F-CI half of T3 (the parity theorem: three is
excluded on a one-cusped manifold, the escape is ≥ 2 cusps); sm:B1544/sm:B1545 the F-HE half; B1466/B1486 the order;
B1481 the hand. **Literature:** none used by a claim; Menal-Ferrer–Porti's vanishing is not assumed (E2 reads h¹).

## 3. Disclosed

Run before the seal, unsealed, on 2026-10-07: the odd modules on m135 and m136 only (all 16 lifts: h¹ = 0 for Sym¹ and
Sym³; the four has h¹ = 1 at the untwisted character — which reproduced B1485's row from SnapPy's presentation) and the
floor on the 390 readings on main (0 violations, 2 tight). The 66 other states and their lifts have not been read. The
audit page cites the m135/m136 run. The GENESIS amendment (v1.15) is text; the gate is a check on declared dependencies.

## 4. Cells, predictions, priors

| | prediction | prior |
|---|---|---|
| **E1** | the floor holds on all 390 readings of the seat's frame on main (380 reproduced N₄₅ rows; B1485's 10), and |I(W₁)| ≤ m_A + b0 on B1485's | 97% (seen) |
| **E2** | on all 68 amphichiral word states to length 12, for every lift (sign character × SnapPy's lift): h¹(M; Sym¹) = h¹(M; Sym³) = 0 and tr λ = −2 | 95% |
| **E3** | on all 68, for every lift, the four at the untwisted character has h¹ = 1 with no interior class (no member at ν = 1 on any amphichiral state) | 85% |

**Reading rules.** E2 false on any state: T2's manifold step fails there — reported by name, the audit's §4 corrected.
E3 false (an interior class of the four at ν = 1 on some amphichiral state): a member the SM seat's census did not
report on that state — relayed to the seat before anything else. Neither changes T1 or T3.

## 5. What lands with the arc (text and checks, not predictions)

GENESIS v1.15 by `adoption/amend.py`: GAP2 sharpened (a count is a count of ends; a generated state has one), GAP1
sharpened (T1; the harmonic frame's internal group contains the geometry's structure group), FK14 registered (does the
genesis generate states with several ends, or are generations not ends?), the §7 heading corrected to six gaps (the SM
seat's P1, credited), B1483–B1486 recorded. WORKING_RULES/PRACTICES: the rules of proper computing for counts; the gate
`seat-positive-verified` (a main arc that builds on a seat's result declares `rests_on_seat`, and each such item needs a
VERIFIED harvest row), with its failing-path test and GATE_CONTROLS row. A relay to the SM seat and the audit lane
carrying the audit, credited and attackable.

## 6. Instruments

`verification/odd_modules_acyclic.py` (E2, E3 — the twin of main's instrument on SnapPy's presentations),
`verification/floor_check.py` (E1), `adoption/amend.py`; hashes in `ARTIFACT_HASHES.txt`.

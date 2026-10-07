# B1487 — THE ENDS: every count on the record is a count of ends, the class index is mirror-even for every module, and no state of the generated family carries three generations in either frame on record — by counting ends, not by search

**Verdict: PROVED** — T1 (a theorem on the page), T2 (elementary, plus the census), T3 (the SM seat's floor, taken as
a hypothesis of this arc's scope, followed on the page and checked on every reading of its frame on main); the three
sealed cells hold. Scope: frames F-HE (the SM seat's) and F-CI (main's); objects the 68 amphichiral word states to
length 12 with all 304 lifts, N₄₅'s 380 reproduced readings and B1485's 10; reach general for T1, class for T2 and T3's
family statement. cc (main), 2026-10-07. Sealed `aab434644` (sha256 27714d7d). The owner's question of 2026-10-07.
No physical quantity. **0 of 19.**

**Credit.** The SM seat for Lemma F and F′ (sm:B1544, sm:B1545), which make the ends reading exact in its frame; B1291
(main) for the parity theorem that is the same reading in F-CI; the web seat for the register question; the audit
lane for R92.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /one-cusped|number of cusps|count of ends|cusps where|mirror-even|acyclic/: 39 of 1358 arcs on main match (NEGATIVE 8, OPEN 5, PROVED 26)`
— read at the level of the verdict lines (listed in the seal): the F-CI arcs on one and several cusps (B1291, B1320,
B1324, B1330, B1333, B1334, B1335, B1418), the index's definition and its reproductions (B1297, B1413, B1446), the spin
arcs, harvests. **Literature:** none used by a claim; Menal-Ferrer–Porti's vanishing is not assumed (E2 reads h¹).

## 1. The theorems

**T1 — the class index is mirror-even for every module.** For a diffeomorphism f of (N, ∂N) and any module E,
H*(N; f*E) ≅ H*(N; E) and H*(∂N; f*E) ≅ H*(∂N; E), compatibly with restriction; complex conjugation preserves every
dimension. So n(conj f*E) = n(E) and I(conj f*E) = I(E). A mirror carries a lift ρ_s to conj(ρ_{s′}) up to
conjugation, hence any module built from ρ_s at s to the corresponding module at s′ — **with the same index.** No
choice of module makes a count see the hand; a mirror can touch I only by exchanging a module with its dual, which
forces I = 0. □

**T2 — the odd modules are acyclic on every word state.** On every lift of every one of the 68 states a peripheral
curve has trace −2 (E2: the fibre's boundary, a commutator, whose lift is sign-independent); a parabolic −u(v) has no
invariants on an odd symmetric power of the lift, so H⁰(T) = 0, H²(T) = 0 by duality and H¹(T) = 0 by χ(T) = 0: the
cusp is acyclic. The manifold's h¹ = 0 was **read, not assumed**, on all 304 lifts for Sym¹ and Sym³ (E2). The hand
(B1481) lives exactly where cohomology vanishes.

**T3 — no state of the generated family carries three, in either frame.** With the floor I(W₁) ≥ k − m_A − b0 of
sm:B1545 applied to both orders, |I(W₁)| ≤ m_A + b0 on any finite cover; on a one-cusped state m_A ≤ 1, so
|I(W₁)| ≤ 1 + b0 ≤ 2, and g generations need at least g − b0 cusps on which the character is trivial and the class
dies. In F-CI, B1291 (proved) excludes three on any one-cusped manifold: the escape is ≥ 2 cusps. Every generated
state (GENESIS §3) and every level has one cusp. **Three is excluded on X_gen by counting ends, not by search.** □
(The floor itself is the seat's theorem; it is a hypothesis of this arc's scope, followed on the page.)

## 2. The cells (`floor_check.json`, `odd_modules_acyclic.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **E1** | the floor on all 390 readings of the seat's frame on main; |I(W₁)| ≤ m_A + b0 on B1485's | 97% | **HOLDS**: 390 rows, 0 violations; tight exactly on m136's two members (I = −1 = 0 − 0 − 1); on N₄₅ the lowest count −1 against a floor of −6 |
| **E2** | on all 68 states, every lift: h¹(Sym¹) = h¹(Sym³) = 0 and tr λ = −2 | 95% | **HOLDS in substance, with one sentence corrected:** h¹ = 0 for Sym¹ and Sym³ on all 304 lifts; a peripheral curve has trace −2 on every state — SnapPy's longitude on 39 of the 68 and its meridian on the other 29 (where the longitude has +2). The sealed sentence named "λ"; the fibre's boundary is whichever curve carries −2, and it does on all 68 |
| **E3** | on all 68, every lift: the four at ν = 1 has h¹ = 1 and no interior class | 85% | **HOLDS**: h¹ = 1, interior 0 on all 304 — no member at the untwisted character on any amphichiral state |

## 3. What lands with the arc

- **GENESIS v1.15** (`adoption/amend.py`): GAP2 sharpened — in the harmonic frame a count is a count of ends, and a
  generated state has one; GAP1 sharpened — T1, and the harmonic frame's internal group SU(5)′ contains the geometry's
  structure group; **FK14 registered: does the genesis generate states with several ends, or are generations not
  ends?**; the §7 heading corrected to six gaps (the SM seat's P1, sm:B1537, credited); B1483–B1486 recorded.
- **The rules of proper computing for counts** (WORKING_RULES; PRACTICES): a count carries its cusp decomposition; no
  search without a selection rule and a trial budget; one seat's reading is cited, not built on; a frame's count is
  labelled by what it can carry. **The gate `seat-positive-verified`** (with its failing-path test and GATE_CONTROLS
  row): a main arc that builds on a seat's result declares `rests_on_seat` and each item needs a VERIFIED harvest row.
  First declarations: B1485 and B1486 rest on sm:B1530 (row 835, VERIFIED by B1485).
- **A relay to the SM seat and the audit lane** carrying the audit (`docs/THE_GENERATION_LANE_AUDITED_2026-10-07.md`),
  credited and attackable, with three asks.

## 4. What it means, and what it does not

- The question "why three generations" is not answered by any count on the record and cannot be by a search over
  covers: in both frames a generation is an end, and the family's states have one. Either the genesis generates
  states with several ends — a move no section of GENESIS names (FK14; the LP seat's LP01 finds common covers of m004
  with the two-cusped members, chiral and without the three) — or generations are not ends and the frames are wrong
  about them (GAP1).
- The hand and the count are in complementary sectors; a sign can enter a count only as the choice of order, and the
  hand is a consistent rule for that choice (B1481, B1486) — a postulate until derived.
- **Not derived:** three; an end-adding move; which order; any value.

## 5. Disclosed

The odd-module and floor checks were run once unsealed on the day (m135/m136; the 390 readings) before the seal, as the
seal says. SnapPy's HP lifts at 40 digits and the numerical twin's ranks with tolerance 10⁻²⁵; the 304 lifts are all
sign characters of SnapPy's presentation (8 per three-generator state, 4 per two-generator one — 304 in all, matching
B1483's count). T3's floor is the seat's; main did not re-derive its three steps. The one sentence of E2 that named
the wrong curve is corrected above and counted as a defect of the seal's wording, not of the result.

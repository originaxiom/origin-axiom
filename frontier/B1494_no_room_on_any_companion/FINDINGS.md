# B1494 — NO ROOM ON ANY COMPANION, AND ONE COMPANION WITH ROOM: the trivial line has no interior class on any fixed-point companion — a theorem, its hypothesis verified on all 758 own-level word states to length twelve — and the first state-born object with a line with room: m135's eight-ended companion, room 2 at eight sign characters, every one of them trivial on no end, where the floor gives zero generations whatever the room; N₄₅ rebuilt on main as the positive control, the seat's rooms reproduced

**Verdict: PROVED** — R0, R1, R3 hold, **R2 fails as the seal's headline** (a companion with room; verified by an
independent route), R4 holds — the seat's rooms reproduced. Scope: the fixed-point companions of the generated family (T-COMPANION-NO-ROOM is
general on the family; the sign-character census is single on m136's and m135's companions); frame F-HE for the
reading of the room (the SM seat's Theorem C and floor); N₄₅ as the SM seat defined it. cc (main), 2026-10-07. Sealed
`0b45b1fb0` (sha256 3f1dbc5e) before the room was read on m136's or m135's companion and before N₄₅ was built here.
The owner's word of the day: "let's follow the light." No physical quantity. **0 of 19.**

**Credit.** The SM seat for the companions (Proposition 1), Theorem C, the floor, and the N₄₅ recipe (its
golden-covers dossier §7, sm:B1540); B350 for the Lucas ladder of the torsion orders at the levels.

## 0. Seen first, and literature

As sealed: `VERDICT topic-sweep /companion|fixed-point|b_1 = |closed surface|room|N₄₅|d9.2|degree 45|degree-45/: 42 of 1366 arcs on main match (NEGATIVE 7, OPEN 2, PROVED 33)`
— B1291, B1493, B350, B1491, B1492 on point. **Literature:** Shapiro's lemma, the Wang sequence, Poincaré–Lefschetz
duality (standard); Menal-Ferrer–Porti (2012) for the twisted half-lives statement the room formula n(1) = b₁ − cusps
rests on. Controls as sealed: the four companions built (b₁ = ends), the eight states to length 4 by the exact
instrument.

## 1. The theorem

**T-COMPANION-NO-ROOM.** For every word state M (a once-punctured-torus bundle with Anosov monodromy φ) with torsion
T = coker(φ − I), |T| = |2 − tr φ|, and its fixed-point companion N — the regular cover with deck group T in which the
cusp lifts to |T| cusps — b₁(N) = |T| and the trivial line has no interior class on N: n(1) = 0. The proof is on the
preregistration (§1): Shapiro over T̂; for χ ≠ 1 the restriction H¹(F; χ) → H¹(∂F; χ) is an isomorphism (the long exact
sequence of the punctured fibre with χ non-trivial on π₁(F)), the monodromy fixes the puncture circle, so h¹(M; χ) = 1
by Wang; and n(1) = b₁ − cusps on any cusped hyperbolic manifold.

**R0 — the hypothesis, verified where it could fail (`torsion_characters_len12.json`).** On all 758 own-level word
states to length twelve, both signs (`architecture_census.states(12)`), at every character of the torsion (the
characters trivial on the peripheral subgroup; |T| from 1 to 224), h¹(M; χ) = 1 exactly at two primes ≡ 1 mod the
exponent of T; so b₁(companion) = |T| on every state. And as manifolds: the companion built in SnapPy for every state with |T| ≤ 10 by the sealed
enumeration route (24 states, one candidate each) and for every state with |T| ≤ 60 by the direct route (265 states;
`companions_direct_len12_T60.json`) has exactly |T| cusps, b₁ = |T| and volume |T| times the state's — the theorem
read off 265 companions, +LLLR's the only one with three ends.

## 2. The census of the line on the two remaining companions

| | sealed prediction | prior | result |
|---|---|---|---|
| **R1** | m136's four-ended companion (H₁ = ℤ⁴, |Sym| 32): room 0 at all 16 sign characters | 70% | **HOLDS** (`room_m136_companion.json`): h¹(χ) = m_A at every one — 9 characters trivial on no end (h¹ = 0), 6 trivial on two ends (h¹ = 2), the trivial one (4); the ends pair under the deck group, no character is trivial on one or three |
| **R2** | m135's eight-ended companion (ℤ⁸, |Sym| 256): room 0 at all 256 | 60% | **FAILS** (`room_m135_companion.json`): **room 2 at eight characters**, each trivial on *no* end (h¹(χ) = 2, both classes interior); room 0 at the other 248 (37 at m_A = 0 with h¹ = 0; 168 at m_A = 2; 42 at m_A = 4; the trivial one at 8) |

**R2 verified by the route the seal named** (`room_m135_companion_double_covers.json`): the 255 double covers of the
companion have (cusps, b₁) ∈ {(12, 12) ×42, (10, 10) ×168, (8, 8) ×37, **(8, 10) ×8**}; with h¹(N; χ) = b₁(Ñ_χ) − 8 and
m_A = cusps(Ñ_χ) − 8, the rooms are exactly the instrument's: {(4, 0): 42, (2, 0): 168, (0, 0): 37, (0, 2): 8}.

**Read as the floor reads it.** The room-2 characters are trivial on no end. Any ν of order eight with ν⁴ = χ is
then trivial on no end and has b0 = 0, so the seat's floor −I(W₁) ≤ m_A + b0 − k = −k ≤ 0 gives **zero generations in
either order there, whatever the room** (B1491's T3). Read beyond the seal at one such ν (`extra_m135_companion_order8.json`:
ν = ζ₈ on the generators c, d, e, f, g, 1 on the rest; ν⁴ = the first room-2 character): b0 = 0, room 2, cap_W = 2 —
and **the four has no class at all there** (h¹(V ⊗ L*) = 0, nothing to extend), the second supply 0. On every
companion read (four), room appears only where no end is special, and the count needs both: an end on which the
character is trivial and the class dies (the floor) and a line with room (the cap). On a companion they never meet.

## 3. N₄₅ rebuilt, and its room (the positive control)

| | sealed prediction | prior | result |
|---|---|---|---|
| **R3** | N₄₅ from the recipe: degree 45 over m003, 5 cusps, H₁ = ℤ⁹ ⊕ (ℤ/2)², n(1) = 4 | 85% | **HOLDS** (`n45.json`): m003 has four one-cusped degree-9 covers; exactly one 5-fold cyclic cover of one of them (the cover with H₁ = (ℤ/10)² ⊕ ℤ) has five cusps and H₁ = ℤ⁹ ⊕ (ℤ/2)² — volume ratio 45.000, n(1) = 4, |Sym| = 240 |
| **R4** | its order-2 characters: rooms {1 ×10, 3 ×5} among the fourth powers of the cusp-trivial order-8 ones, the room-3 ones trivial on every cusp | 75% | **HOLDS** (`room_n45.json`, `room_n45_fourth_powers.json`): of the 2048 sign characters, 64 are cusp-trivial and 16 of those are fourth powers (trivial on the (ℤ/2)² torsion, read off the integer kernel of the exponent matrix mod 2); the trivial one has room 4 = n(1), **ten have room 1 and five room 3** — the seat's census, cusp-trivial by construction. The whole census: rooms {0: 766, 1: 435, 2: 560, 3: 30, 4: 247, 6: 10}; room 3 also at fifteen characters trivial on one cusp and room 6 at ten trivial on two, where the floor caps the count at m_A anyway |

**Where N₄₅'s room comes from, against the companions.** N₄₅ has b₁ = 9 over 5 cusps: four classes of closed
surfaces; its room-3 characters are trivial on every cusp, so they live where the floor's ends are all available —
ends and room meet, and the count there reaches two (sm:B1547). A companion has b₁ = ends (the theorem) — no closed
surface — and where it has room (m135's) no end carries the character. **The room of the line is not absent from the
family; it is separated from the ends on it.**

## 4. What it says for FK14 (GENESIS v1.20)

The fork's second half gains its mechanism. Three generations need, at one character, (a) ends on which the character
is trivial and a class dies — the floor — and (b) a line with room 3 − b0 — the cap. On the generated states (a) is at
most one end; on the companions (a) and (b) exist but never at the same character; on N₄₅, a cover chosen by a
character of m003's torsion and a degree-9 cover of it, (a) and (b) meet and the count reaches two. The object the
genesis determines separates the two supplies; the search for three is the search for an object the genesis determines
on which they coincide. Not ruled: characters of order other than two, four, eight; non-unitary characters; the
companions of the companions.

## 5. Disclosed

- **A second route for the companion builds, added after the seal.** The sealed `companions.py` enumerates every cover
  of degree |T| and keeps the one with |T| cusps; SnapPy's enumeration at degree 12 did not finish in the hour, so the
  enumeration route was stopped at |T| ≤ 10 (`r0_companions_run.txt`; the stopped run kept as
  `sealed_run_companions_enumeration_T12_stopped.txt`) and the companion was built directly as the regular cover with
  deck group T = H₁/⟨peripheral⟩ from the Smith normal form of the relator-and-peripheral exponent matrix through
  `cover(perms)` (`companion_direct.py`; for an abelian deck group the convention of B1490 cannot bite). The two routes
  agree on every state both built. The two routes give isometric manifolds with the same H₁ on all 24 states both built (`routes_agree.json`; the triangulations differ); the direct route built 265.
- The reading at one order-8 character above a room-2 character is beyond the seal (one ν of the many above χ).
- Numerical ranks (40 digits, 10⁻²⁴) for the rooms; the double-cover route is integral. N₄₅'s identification is the
  seat's (degree, cusps, H₁); its isosig is recorded.
- Not blind to the seat's N₄₅ numbers or to B1493.

## 6. Files

`verification/torsion_characters.py` → `torsion_characters_len12.json`; `companions.py`, `companion_direct.py` and their
census outputs; `room_on.py` → `room_m136_companion.json`, `room_m135_companion.json`, `room_n45.json`;
`room_m135_companion_double_covers.json`; `n45.py` → `n45.json`; `extra_m135_companion_order8.json`; the run logs; the
seen files; `ARTIFACT_HASHES.txt`. Test: `tests/test_b1494_no_room_on_any_companion.py`.

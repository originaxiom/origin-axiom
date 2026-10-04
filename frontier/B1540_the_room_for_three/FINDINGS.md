# B1540 — THE ROOM FOR THREE, AT THE GOLDEN AND THE EISENSTEIN ORDERS: sm:B1536's banked rows, summed over the pulled-back characters of its thirty room covers by Lemma A, give room ≥ 3 on seven cyclic covers of m003 — N₄₅ at the golden order 5 (room 5) and six covers of degree 60 at the Eisenstein order 6 (room 3 or 4, four conjugacy classes) — each read directly in two routes and by integer homology; on m004 the pulled-back characters give nothing new

cc (the SM-derivation seat), 2026-10-04. **Status: PROVED (computed), not sealed.** Every number follows from sm:B1536's banked
rows and Lemma A, and every cover with room ≥ 3 was then read directly in two routes and by integer homology. It is room, not
a count: the counts at the classes are sealed questions (sm:B1541 on N₄₅; none yet on the degree-60 covers).
**Price:** unchanged, 0 of 19.

## 1. The result

**Room** at the trivial character of a cover is min(capW, capL2) = min(1 + n(1), n(ρ)) (b0 = 1, L = 1, ρ ≅ ρ*). sm:B1535's
Theorem C bounds the frame's generation count by it. sm:B1536 found room 2 at most on every cover of degree ≤ 12 and on the
Q₈ towers.

- **The census** (`verification/pulled_back_rooms.py`, banked data only): on sm:B1536's thirty room covers it fixes the line
  and the four at every pulled-back character the banked rows reach. It then sums them over the 117 cyclic subgroups whose
  every power they fix. Seven of those cyclic covers have room ≥ 3, all of them covers of m003. No two banked rows disagree.
- **At the golden order 5: N₄₅** (m003's d9.2 along the order-5 character χ from m003's ℤ/5 torsion; degree 45, five
  cusps). (n(1), n(ρ)) = (4, 18), so room 5. One count is fixed, (0, 0), at the class pulled back from m003.
- **At the Eisenstein order 6: six covers of degree 60.** Each is the 6-fold cyclic cover of one of m003's degree-10 covers
  along a pulled-back character of order 6. The six:
  - d10.13, d10.14, d10.36 and d10.38 give (n(1), n(ρ)) = (3, 3), so room 3;
  - d10.16 and d10.40 give (3, 7), so room 4.
  Up to conjugacy in π₁(m003) they are four covers: {d10.13, d10.14}, {d10.16}, {d10.36, d10.38}, {d10.40}.
- **The two orders' fields.** The order-5 characters take values in ℚ(ζ₅) ⊃ ℚ(√5) = ℚ(φ), the golden field: m003's ℤ/5 is
  coker(−A − I) for the golden monodromy A = [[2, 1], [1, 1]]. The order-6 characters take values in ℚ(ζ₆) = ℚ(√−3), the trace
  field of m003 and m004.
- **What the covers are.** A cyclic cover along a pulled-back character ψ is a fibre product: ker(ψ|N) = π₁(N) ∩ ker ψ.
  - N₄₅ is d9.2's fibre product with m003's 5-fold torsion cover (along χ).
  - The order-6 characters have u = 0, so they factor through the fibration: ψ(a) = ψ(b) = 0 and ψ(t) = e^{2πi/6}. Each
    degree-60 cover is therefore a degree-10 cover's fibre product with m003's 6-fold cyclic cover along the fibration, the
    punctured-torus bundle with monodromy (−LR)⁶.
- **On m004** every pulled-back character the banked rows reach restricts to the trivial character of d9.2, d10.3 and
  d10.24. The census's best room there is 1. So m004's covers gain nothing from pulled-back characters, and their own
  characters are the open question (sm:B1539).
- **Room is not a count.** Theorem C does not forbid g = 3 on these seven covers. Whether a class carries a generation-shaped
  count is a separate question, sealed per cover: sm:B1541 on N₄₅; the degree-60 covers are next.

## 2. Why it holds

- **The banked rows.** At a cover N, sm:B1536's member ν = (u, κ) fixes three own-character readings. Routes R and N agree
  at every row.
  - n(L) is the line's interior supply at ν⁻⁴.
  - n((VL)*) is the four's at ν³: (V ⊗ L)* = ν³ ⊗ ρ* and ρ is self-dual.
  - n(V_η) is the four's at ν⁵.
  - Each power is restricted to N in its own coordinates (route R's Schreier generators, PARI's Smith form). A value is taken
    as fixed only when routes R and N both give it; a member giving a different value would be a conflict, and none occurs.
- **Lemma A** (Shapiro, with Mackey at the cusps; sm:B1536's Lemma S′ with ℂ[μ_k]): for a character c of order k,
  n_{N_c}(E) = Σ_{j mod k} n_N(E ⊗ cʲ) for E = 1 or ρ.
- **The sums.**
  - d9.2 (trivial (0, 2)): the line is 1 and the four is 4 at each χʲ (j = 1..4), so (0 + 4·1, 2 + 4·4) = (4, 18).
  - d10.13 and d10.36 (trivial (1, 2)): the line is 1 at the two order-3 powers, and the four is 1 at the order-2 power. The
    order-6 powers carry neither. So (1 + 2, 2 + 1) = (3, 3).
  - d10.14 and d10.38: the line is 1 at the two order-6 powers, and the four is 1 at the order-2 power. So (3, 3).
  - d10.16 and d10.40: the line is 1 at the two order-6 powers; the four is 1 at the order-2 power and 2 at each order-3
    power. So (1 + 2, 2 + 1 + 4) = (3, 7).
- **Proposition P** (N₄₅'s pulled-back count).
  - Shapiro splits the frame's W on N₄₅ into W ⊗ χᵏ on d9.2, compatibly with the cusps.
  - On the 5-torsion ν⁵ = 1, so W at the member ν = χᵏ equals χᵏ ⊗ W at the trivial character. Likewise Λ²W, with
    ν = χ^{3k}.
  - So the count is the sum of sm:B1536's banked Part P counts at d9.2's five members (u, 0). All five are (0, 0) in both
    routes.

## 3. The census by member (`verification/pulled_back_rooms.json`)

| members | trivial (n(1), n(ρ)) | the line ≥ 1 at order | the four ≥ 1 at order (n) | best room |
|---|---|---|---|---|
| m004: d9.2, d10.3, d10.24 | (0, 2), (1, 1), (1, 1) | — | — | 1 |
| m003: d5.2, d5.3 | (1, 1) | — | 5 (1) | 2 |
| m003: d9.2 | (0, 2) | 5 | 5 (4) | **5** (order 5, degree 45) |
| m003: d10.13, d10.36 | (1, 2) | 3 | 2 (1), 5 (1), 10 (1) | **3** (order 6, degree 60) |
| m003: d10.14, d10.38 | (1, 2) | 6 | 2 (1), 5 (2) | **3** (order 6, degree 60) |
| m003: d10.16, d10.40 | (1, 2) | 6 | 2 (1), 3 (2), 5 (2) | **4** (order 6, degree 60) |
| m003: d10.8, d10.23 | (1, 1) | 3 | 5 (1) | 2 |
| m003: the other sixteen of degree 10 | (1, 1) or (1, 2) | — | 2, 3, 5, 10 (1 or 2) | 2 |

- 117 cyclic subgroups have every power fixed: two on d9.2, one on each m004 cover, two or five on the others.
- The census is scoped to them. A cyclic subgroup with a power the banked rows do not reach is not read here, and neither is
  any own character that is not pulled back.

## 4. Read directly

**N₄₅** (`verification/room_n45.py`, record `verification/room_n45.json`; N₄₅ built by sm:B1541's sealed `n45.build`):

| quantity | value |
|---|---|
| the banked rows at χʲ, j = 0..4: line ∣ four (routes R and N identical) | 0, 1, 1, 1, 1 ∣ 2, 4, 4, 4, 4 |
| Lemma A on N₄₅ | (4, 18) |
| route N on N₄₅ (Shapiro on m003, degree-45 permutation module, p = 16775281) | (4, 18); capW 5, capL2 18 |
| route R on N₄₅ (its own presentation, p = 2147482801) | (4, 18); capW 5, capL2 18; h¹(ρ) = 23 |
| H₁(N₄₅) from its presentation (PARI's Smith form) | ℤ⁹ ⊕ (ℤ/2)², five cusps: b₁ − cusps = 4 |
| the pulled-back count: banked Part P sum ∣ route N ∣ route R | (0, 0) ∣ (0, 0) ∣ (0, 0), every identity holding |

**The six degree-60 covers** (`verification/room_60.py`, record `verification/room_60.json`; each built as the cyclic cover
along the census's character, `room_lib.cyclic_cover`):

| from | cusps | route N (p = 16775281) ∣ route R (p = 2147482801): (n(1), n(ρ)); capW, capL2 | H₁; b₁ − cusps | room |
|---|---|---|---|---|
| d10.13 | 6 | (3, 3); 4, 3 ∣ (3, 3); 4, 3 | ℤ⁹ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 3 |
| d10.14 | 6 | (3, 3); 4, 3 ∣ (3, 3); 4, 3 | ℤ⁹ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 3 |
| d10.16 | 4 | (3, 7); 4, 7 ∣ (3, 7); 4, 7 | ℤ⁷ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 4 |
| d10.36 | 6 | (3, 3); 4, 3 ∣ (3, 3); 4, 3 | ℤ⁹ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 3 |
| d10.38 | 6 | (3, 3); 4, 3 ∣ (3, 3); 4, 3 | ℤ⁹ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 3 |
| d10.40 | 4 | (3, 7); 4, 7 ∣ (3, 7); 4, 7 | ℤ⁷ ⊕ ℤ/4 ⊕ ℤ/12; 3 | 4 |

- Every route agrees with Lemma A's sums, and b₁ − cusps = n(1) on every cover.
- **Conjugacy** (sm:B1536's `cover_lib.canonical`): {d10.13, d10.14}, {d10.16}, {d10.36, d10.38}, {d10.40}. So there are four
  covers of m003; two of them are reached from two degree-10 covers each.
- `room_lib.py` loads only sm:B1536's banked modules (route_n, route_r, cover_lib, gf, population) by path, unchanged. It never
  loads another arc's unsealed files.
- **Fail closed** (the audit lane's R92): `room_n45.py`, `pulled_back_rooms.py` and `room_60.py` keep the record of a
  disagreeing run and exit non-zero.

## 5. How it was found (disclosed in full)

- **N₄₅**, 15:45–15:50Z on 2026-10-04. It came up while setting the priors of the own-character census (sm:B1539, pre-seal),
  when sm:B1536's banked rows at d9.2 were read through Lemma A; the golden covers dossier's §7 records it.
  - The supplies were predicted from the banked rows before N₄₅ was built, and then read directly.
  - The pulled-back count was predicted from the banked Part P rows before it was read directly.
- **The degree-60 covers**, 16:40–16:45Z. They came up while restating sm:B1539's predictions over the characters no banked row
  reaches. That restatement needed the full set of pulled-back characters the banked rows fix, so the census was run on all
  thirty members.
  - Its first form (scratch, the same logic) gave the seven covers at 16:42Z.
  - The six degree-60 covers were read directly at 16:44–16:47Z.
  - This arc's own instruments reproduce both.
- **A false alarm, recorded.** At the level of m004's own characters (u, κ), the banked line is 1 at ν⁻⁴ = −1 on d10.3 and
  d10.24. In each cover's own coordinates that character restricts to the trivial one, where the line is n(1) = 1. So it is
  no jump, and the census shows none on m004.
- No sealed arc's population contained these covers, and no sealed reading was used or reordered.
- **Why sm:B1536 did not see them.** It read the room at each member, min(capW, capL2) at ν. Lemma A instead adds the supplies
  over a group of characters, which is the room at the trivial character of a larger cover. That cover's degree (45, 60) lies
  beyond sm:B1536's population.

## 6. What it changes

- **sm:B1539's draft predictions** are decided before its seal on seven members, not one. Its predictions of room for three on
  an abelian or cyclic cover, and of the line growing at an own character, all hold through pulled-back characters. They are
  restated over the characters no banked row reaches (the own characters not pulled back from the state) before the seal.
- **sm:B1541** reads the counts at N₄₅'s classes, sealed before any of them but the fixed one was read. The degree-60 covers'
  classes are the next sealed question. Two of the four conjugacy classes have room 4.
- **Two arithmetic orders give room**: the golden 5 through m003's torsion, and the Eisenstein 6 through its fibration. m004,
  whose H₁ is ℤ, gets neither from pulled-back characters.

## 7. What it is not

- Not a count: the frame's count at a class is what three generations means here. Room only says Theorem C does not forbid
  it.
- Not a selection: which cover, which class and which member the genesis selects is GENESIS GAP4 and THE_BAR's question.
  Room without a selector is a landscape: seven covers with room ≥ 3 already, at two orders.
- Not complete: only cyclic subgroups whose every power the banked rows fix are read. Pulled-back characters beyond those,
  and own characters that are not pulled back, are sm:B1539's.
- 0 of 19 stays 0.

## Seen first (the repo sweep and the literature)

- **The repo sweep.**
  - N₄₅: sm:B1541's, at 16:00Z (`scripts/checks/prior_work.py` over every head, after `git fetch --all`). "N_45",
    "degree-45" and "degree 45" appear only in this seat's golden covers dossier (§7, written the same afternoon) and as false
    matches (a filename "…_run_456.txt"). "torsion cover" is absent everywhere.
  - The degree-60 covers: this arc's, at 16:52Z, again over every head (main at 88ed6981, the audit lane at 18f7204b).
    - "room four" and "room 4" are absent everywhere. "pulled-back room" is only in this arc's uncommitted text.
    - "degree 60" bears only on other covers: the icosian A₅ covers of degree 60 (sm:B1536's untested list; the golden covers
      dossier; OPEN_LEADS' sL-12).
    - "6-fold cyclic cover" names m004's six-fold tower M₆ (B1378, THE_CLOSING): another state, another frame.
    - "Eisenstein order" and "fibre product" match unrelated arcs (B1353's isolated points, B302).
  - The hits that bear are sm:B1536 (the banked rows and code paths), sm:B1535 (Theorem C) and sm:B1515 (the frame).
- **The literature.** Shapiro's lemma with Mackey at the cusps is used as sm:B1536's banked Lemma S′. No source read states
  this frame's supplies on a cover of m003.
- **Standing: EXTENDS** (sm:B1536's banked rows, summed over groups of characters for the first time).

**0 of 19 stays 0.**

# THE LEVEL IS THE LINE'S OWN (THE OWNER: "KEEP ME ON THE CHOICES"; CHOICE 4, MINIMALITY OR THE LADDER): THE OBJECT'S TWISTED FIXED POINTS FORM coker(LR + I) = ℤ/5, SO THE LINE HAS ORDER 5 AT EVERY AMBIENT MODULUS. READ STRICTLY, WITH EACH INGREDIENT AT ITS OWN LEVEL, (K) RESTATES S305w'S MINIMALITY AND THE MINIMAL INVISIBLE RUN: LEVEL 5, RUN 6. THAT IS A RATIONALE, NOT A REMOVAL: CHOICE 4 MOVES INTO (K), AND THE LADDER IS NOT NEEDED. FOR THE COUPLING, STRICT (K) NEEDS ONE MORE IDENTIFICATION: READ AS q'S ORDER IT AGREES WITH S305w'S SHIFTED CONVENTION; READ AS THE CHERN–SIMONS LEVEL IT EXCLUDES IT

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On** the owner's "Keep me on the choices". This is choice 4 in 21cfbc3c2 § 4: "**Minimality, or the finite triangle
ladder.** The selection of 5 over 10, 15, … rests on it."

**Kind:** a conceptual note, with no new computation.
- It uses a Smith form, membership in congruence subgroups, and 5fef38dee's counts (re-run on main at S305y).
- No coupling or scale ratio is computed. S305w's ħ convention is quoted.
- No held-out quantity is computed or quoted, and nothing is compared with data.

**Swept first** (main at 307fa9101; main-only form):
- `VERDICT topic-sweep /own level|line's level|level of the line|conductor of the line|ambient (modulus|level)/ (full text): 17 of 1591 arcs on main match (NEGATIVE 3, OPEN 1, PROVED 13); 4 register rows match (DONE 1, QUEUED 3)`
- `VERDICT topic-sweep /minimal(ity)? (quantization )?level|non.?minimal(ly)?|given minimality/ (full text): 5 of 1591 arcs on main match (NEGATIVE 3, PROVED 2); 4 register rows match (DONE 2, QUEUED 2)`
- `VERDICT topic-sweep /cusp width|width of the (cusp|departure)|level of the (departure|parabolic)/ (full text): 1 of 1591 arcs on main match (PROVED 1); 3 register rows match (DONE 1, QUEUED 2)`

Bearing on it:
- **P-722 at S305w:**
  - "R1 DERIVED given minimality — the minimal quantization level whose phase space holds the object's own line
    (order 5, P-718) is 5 (3 does not hold it, 15 only non-minimally)";
  - "at q = e^{2πi/5} one ħ = 2π/(k + h∨) = 2π/5 sets the coupling and B151's exponent (the shifted convention;
    unshifted 2π/3 named)".
- **P-721 at S305y:** "two seats reach k = 5 independently — the web seat by minimality over the levels that hold the
  line".
- **P-312:** "a thread fixes an order-5 line at its own level iff its trace ≡ ±2 mod 5".
- **P-718,** "THE LINE IS THE OBJECT'S OWN LEVEL-5 EIGENLINE".
- **P-717's ladder:** Γ/⟨⟨Tᴺ⟩⟩ is finite iff N ≤ 5.
- **Least action** (0772952e3; S305v) supplies "one departure" under (ii). Among single runs it restates the minimal n.
  0772952e3: "That restates 'minimal'; it does not derive it".

**Two terms that collide with the record's:**
- "Own level" here means an ingredient's level. The record also uses it for a state's own manifold against its covers
  (L229; B1434).
- "(K)" here is 21cfbc3c2's principle, not the SM seat's criterion K (P-721 at S305y), "the least level trivialising
  every CS phase".

**Refereed read-only:** READY WITH CORRECTIONS (8 findings and 9 suggestions), all applied in this text. The first
draft's overstatements are listed under Disclosures.

## 1. Each ingredient's own level

**The rule.**
- For each ingredient, the levels at which its condition holds form either the multiples of one number (a point:
  "defined at N") or the divisors of one number (a parabolic: "invisible at N").
- The own level is that number: the least such level for a point, the greatest for a parabolic.

**The line.**
- The twisted fixed points of A = LR on T² are (A + I)⁻¹ℤ²/ℤ² ≅ coker(A + I). By the Smith form diag(1, 5) this is
  ℤ/5.
- So every twisted fixed point has order 1 or 5, at every ambient modulus N. At N = 15 the four nonzero ones are
  3·(the pair) (5fef38dee): order 5, not 15. The referee checked N ≤ 120: no level other than 5 holds a twisted fixed
  point of exact order N.
- With the zero set aside (choice 3, 2bc31bc23), the line's own level is its order, 5. That is P-312's "own level" and
  P-721's "the line's own level is 5".

**The departure** (reading (ii)).
- A single run of n adds the parabolic L^{n−1}. L^m lies in Γ(N), and in ±Γ(N), iff N ∣ m.
- So the departure is invisible exactly at the divisors of n − 1. Its own level, the width of its parabolic, is n − 1.
- This depends on taking the width over all levels:
  - measured against the line instead (the stabiliser of ±v), every n ≡ 1 mod 5 gets level 5;
  - measured against the finite ladder, every n ≡ 1 mod 5 gets level 5 too;
  - under reading (i) the parabolic is the whole run Lⁿ, so its own level is n.

**The coupling.** The point and parabolic rule does not define a coupling's own level. Two identifications are on the
record's side:
- **(α) q's order.** This is point-type, like the SM seat's criterion K. S305w's q = e^{2πi/5} has order 5, with the
  shifted relation k + h∨ = 5.
- **(β) The Chern–Simons level k,** as in P-722's original ħ = 2π/k and 21cfbc3c2's k = N.

## 2. What follows

**Strict (K): the process's level is each ingredient's own level.**
- The line fixes that level at 5, the departure's own level n − 1 = 5 gives n = 6, and the coupling's level must be 5.
- Under the read-out's premises (c6b813450), the run of 6 has the apex τ*₆ = i√5φ.

**This is a rationale, not a removal.**
- Strict (K) restates S305w's minimality (the least level at which the line is defined) and the minimal invisible run
  (the departure's parabolic width) as each ingredient's own level.
- Over N, n ≤ 60 it gives exactly (5, 6), the same as least N and then least n (the referee's check).
- So choice 4 moves into choice 1 as (K)'s strict reading, and the ladder is not needed under it.

**Against 21cfbc3c2.**
- That relay read the line's level ambiently: the line exists at level N iff 5 ∣ N. It took the departure at N as the
  run of N + 1, whose own level is N.
- By the strict reading's criterion, a level-15 process then carries ingredients of two own levels, 5 and 15. S305w's
  "15 only non-minimally" records the line's half of this.

**Least action.** Among single runs it restates the minimal n. What it adds under (ii) is "one departure"
(0772952e3, in its range; S305v). It stays in the list.

**The coupling under strict (K):**
- **(α)** gives order 5, as in S305w's shifted convention. The Chern–Simons level is then 5 − h∨, not 5, so under (α)
  the coupling's level is q's order and nothing more.
- **(β)** makes strict (K) set k = 5. The shifted relation would then put q at order k + h∨, which is not 5 (two levels
  again). So (β) with strict (K) excludes S305w's shifted identification and keeps the unshifted one.
- Either way the identification is a further choice. It is main's convention question (P-722), now sharpened.

**Choice 3's role changes.**
- Under strict (K), level 3 is excluded by (K) itself, since the line's order is 1 or 5.
- What "nonzero" now excludes is the level-1 process: the zero line, the run of 2, the trivial root of unity.
- The exception is reading (β), where a Chern–Simons level of 3 can appear beside q's order 5.

## 3. For main to check (labelled, not claimed)

- **Applied per run,** strict (K) admits only runs of 1 (no departure) and 6 (own level 5). The history mod 5 is then
  the golden one.
- **That would exclude** 0772952e3's cheaper line-invisible clusters, which are built from runs of 2 (own level 1).
  With least action it would supply "one departure" without S305v's rung-over-line choice.
- **This depends on** taking each run, not each cluster, as a departure. It is not checked here.

## 4. The goal's choices after this note (21cfbc3c2 § 4's numbering)

1. **(K),** now read strictly: one process, each ingredient at its own level. This carries choice 4.
2. **Reading (ii).**
3. **A nonzero line:** the reading of the line, on the punctured fibre (a) or as a surjective representation (b),
   rather than as a bare flat bundle (c) (2bc31bc23). Under strict (K) it excludes the level-1 process.
4. **Minimality or the ladder:** moved into 1.
5. **The departure:**
   - one departure, with its limit m → ∞ (which the read-out's uniqueness also needs, c6b813450);
   - or least action under (ii), which supplies the single run (0772952e3, in the range; S305v).
6. **The read-out's premises:**
   - (N1) a point;
   - (N2) the Teichmüller history;
   - (N3) no arrow and no fibre orientation beyond M's (B716).
7. **The bit.** The SM seat's § 355, verified at S305y, finds the two points carry opposite CS.
8. **Main's conventions:** P-722's R2 reading, R4, and now the coupling's level as (α) or (β).
9. **The scope:** only transmuted scales follow (f839df278).

## Disclosures

- **This adds a strict reading of (K),** under which (K) selects 5. 21cfbc3c2 § 3's "(K) alone does not select 5" stands
  for (K) as defined there.
- **No new computation.** The facts are a Smith form, congruence membership, and 5fef38dee's counts. The referee checked
  the arithmetic independently: N ≤ 120 for the fixed points; N, m ≤ 60 for congruence membership and for the strict
  selection.
- **The first draft overstated, and the corrections are applied:**
  - It called S305w's minimality "not a selection among levels" and said choice 4 was absorbed. It is restated as
    strict (K), a rationale, and choice 4 moves into choice 1.
  - It said least action had fixed the depth and was now a cross-check. Minimality fixed the depth; least action adds
    "one departure".
  - It dropped "or least action" from choice 5.
  - It took the coupling's own level as q's order without saying that this is an identification.
  - It said the Kind line quoted no coupling, though it quoted S305w's ħ.
  - It called the strict reading a correction of 21cfbc3c2.
  - It read S305w's clause as covering the departure.
  - It described 21cfbc3c2's departure as ambient.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE LEVEL IS THE LINE'S OWN (the owner: "Keep me on the choices"; choice 4; conceptual, no new computation) | "the object's twisted fixed points form coker(LR + I) = ℤ/5, so the line has order 5 at every ambient modulus. Read strictly, with each ingredient at its own level, (K) restates S305w's minimality and the minimal invisible run: level 5, run 6. That is a rationale, not a removal: choice 4 moves into (K), and the ladder is not needed. For the coupling, strict (K) needs one more identification: read as q's order it agrees with S305w's shifted convention; read as the Chern–Simons level it excludes it" | `relays/CHAT1_TO_CC_2026-11-06_THE_LEVEL_IS_THE_LINES_OWN.md` @ the commit adding it | — | P-722, P-721, P-718, P-312, P-717 | 2026-11-06 |

0 of 19.

# Π2 HAS A RATIONALE, NOT A DERIVATION (THE OWNER: "TRY TO DERIVE Π2"): FOR ONE RUN OF a LETTERS, THREE CONDITIONS COINCIDE: IT ACTS AT LEVEL 5 AS THE LAW'S SINGLE LETTER, IT CARRIES THE LAW'S LINE (P-718'S EIGENLINES) AS THAT LETTER DOES, AND a ≡ 1 MOD 5. SO Π2 IS Π1 HELD AT LEVEL 5 AND COMPARED AT EVERY RUN BOUNDARY. WHERE THE COMPARISON IS MADE DECIDES IT: AT EACH DEPARTURE'S ENDS THE RECORD'S CLUSTERS PASS TOO (S305v'S RUNG-INVISIBILITY); AT EVERY MOVE ONLY THE GOLDEN THREAD PASSES, SO THERE IS NO EVENT. THE PRICE IS THREE READINGS: THE LAW READ AT LEVEL 5, THE COMPARISON MADE AT EVERY RUN BOUNDARY, AND Π1'S GOLDEN SUPPORT TAKEN AS A CONDITION WITH D RANKING ITS LIFTS. Π2 MOVES INTO THEM, AND THE STATED PRINCIPLES STAY FOUR. AN ERRATUM TO befdd5ffc: ONCE RUNS OF 11 ARE ALLOWED, THE NEXT LIFT UNDER (A) COSTS 1.05 MORE, NOT AT LEAST 2.1

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On** the owner's answer to this seat: "Try to derive Π2 (Recommended)". Π2 is befdd5ffc's "Each run keeps the line
at its boundary: runs ≡ 1 mod 5".

**Kind:** a conceptual note, with no new computation.
- § 1's facts are matrix identities mod 5: 5fef38dee's criterion and P-718's eigenlines.
- § 2's counts are d2424f23a's committed outputs.
- Some figures are unregistered computations by befdd5ffc's referee and this note's, and are cited as such:
  - § 2's beyond-range figures;
  - the (B) leader's +I class;
  - the mirror cost check;
  - the 338.
- No coupling, scale ratio or held-out quantity is computed or quoted, and nothing is compared with data.

**Swept first** (main at 6ecb9b7b6; main-only form):
- `VERDICT topic-sweep /law at level|law mod 5|golden mod 5|reduced (word|mod 5)|run.?length mod|lift of the (law|golden|quantum)|classical lift|kernel of the (quantum|level)/ (full text): 8 of 1591 arcs on main match (PROVED 8); 1 register rows match (QUEUED 1)`
- `VERDICT topic-sweep /quantized (cat map|dynamics|golden)|Weil representation at|L\^5 ?= ?(1|I)|T\^5 (is )?trivial/ (full text): 2 of 1591 arcs on main match (PROVED 2); 1 register rows match (QUEUED 1)`
- `VERDICT topic-sweep /passage through the finite|congruence shadow|heard mod|law of steps|step by step at level|per.?step|keeps? the line/ (full text): 20 of 1591 arcs on main match (NEGATIVE 4, PROVED 16); 2 register rows match (DONE 1, QUEUED 1)`

**What the sweeps find:**
- **Sweep 1.** Its arcs matched through other senses of "reduced word" and "lift". Two of them still bear on the step
  reading's alignment (§ 3):
  - B1813: "the counting rule is CHOSEN";
  - B1815: the clock.

  Its register hit is P-717, which matches through S305t's reading (ii): "the history is golden mod 5". S305v, in the
  same row, formalizes this over whole departures as E ≡ ±I mod 5 ("reading (ii) itself"). This note reads it run by
  run instead.
- **Sweep 2** finds P-721 and the record's quantized golden cat map (B376, B446).
- **Sweep 3** finds:
  - the record's measurement principle and congruence shadow (B206, B208, B644);
  - P-721;
  - "per-step" ledgers in other senses (B1040, B1044).
- **No row derives** the run-by-run line condition.

**Bearing on it:**
- **P-721:** "the object's own dynamics on the fibre torus is the monodromy as a linear symplectic map". Also: "The level
  at which the quantized dynamics' phase space (ℤ/N)² holds those fixed points is N = 5", and "So the record's own
  principle offers THREE levels, not one". Its Q1 leaves the choice open.
- **LAW_MAP:**
  - "Measurement is passage through the finite": "the infinite Anosov dynamics is heard mod the conductor: what any
    ear couples to factors through a finite group" (PRINCIPLE; B640, B644);
  - the congruence-shadow theorem (B644);
  - the row "The stage-selection question": "κ = 5 is the MINIMAL BEARING CHOICE (5|κ proved; equality is not)"
    (HYPOTHESIS).
- **B206:** "the classical/quantum divide exactly the A5/2I spin double cover".
- **P-717:**
  - the ladder, Γ/⟨⟨Tᴺ⟩⟩ finite iff N ≤ 5;
  - S305o: "what lies in Γ(5) = ⟨⟨T⁵⟩⟩ is the whole run L⁵";
  - S305t's reading (ii);
  - S305v's E ≡ ±I, and its "Still chosen: … rung- rather than line-invisibility (post hoc)".
- **P-718:** RL's eigenline mod 5 is {(x, 2x)}. LR's points are (1/5, 3/5) and (2/5, 1/5), on {(x, 3x)}.
- **P-465:** "pure LR every run 1", and "every run longer than 1 is a departure".
- **B376:** the quantized golden cat map.
- **B1813 and B1815:** the counting rule and the clock, both chosen.
- **befdd5ffc:** Π1 to Π4.
- **1f770e825:** strict (K), and its own-level rule.
- **21cfbc3c2:** (K)'s ingredients.
- **904f19136 § 6.1:** "each invisible to the line by itself", and "'By itself' cannot be dropped".
- **d2424f23a and 0772952e3:** the clusters and the range.

**Refereed read-only:**
- The first read was NOT READY (11 errors and 6 suggestions). The note was rebuilt from it, with every correction
  applied.
- The second read was READY WITH CORRECTIONS (5 errors and 11 suggestions), all applied in this text.

## 1. One run: three conditions that coincide

Take a run of a ≥ 1 letters, L^a or R^a, at a place where the law's word has a single L or R. Three conditions on it
are the same.

**(i) It acts at level 5 as the law's letter: L^a ≡ L, or R^a ≡ R, mod 5.**
- L^{a−1} = [[1, 0], [a − 1, 1]], so this holds iff 5 ∣ a − 1 (5fef38dee).
- L^{a−1} is never ≡ −I, so the condition is the same in SL(2, ℤ/5) and on lines. R is alike.

**(ii) It carries the law's line as the letter does.** Here vectors are columns, with X acting on the left.
- At level 5 the law's lines are P-718's eigenlines: {(x, 2x)} for RL and {(x, 3x)} for LR.
- The letter L carries RL's line onto LR's (L·RL·L⁻¹ = LR), and R carries LR's onto RL's.
- L^a sends (1, 2) to (1, a + 2), which lies on {(x, 3x)} iff a ≡ 1 mod 5.
- R^a sends (1, 3) to (1 + 3a, 3), which lies on {(x, 2x)} iff 3 ≡ 2 + a, that is iff a ≡ 1 mod 5.
- Neither line is the run's own fixed line ({(0, y)} for L, {(x, 0)} for R), so no other a passes.
- **In the record's row convention** (w ↦ wX⁻¹; B1733), L^a sends (1, 2) to (1 − 2a, 2) and R^a sends (1, 3) to
  (1, 3 − a). The own lines there are {(x, 0)} for L and {(0, y)} for R, as in 904f19136 § 3. The condition is the
  same, since RL and LR are symmetric and their eigenlines agree in both conventions.

**(iii) a ≡ 1 mod 5.**

**So Π2's wording and (i)'s are one condition.** "Each run keeps the line at its boundary" and "each run acts at
level 5 as the law's letter" both say a ≡ 1 mod 5.

## 2. Where the law is compared

**The alignment.** The record compares a departure with the golden segment that has the same number of runs:
- S305v's rung-invisibility, E ≡ ±I mod 5;
- 0772952e3's excess, which is action (A).

This note keeps that alignment. Π2 then depends on where the comparison is made:

| the law compared | what passes at level 5 | source |
|---|---|---|
| at each departure's ends | every rung-invisible departure, clusters included: d2424f23a's 643 in 0772952e3's range. That count is on lines (E ≡ ±I). In SL(2, ℤ/5), 338 of them pass (E ≡ +I), the (B) leader among them. | S305v; d2424f23a; the referee (unregistered) for the 338 |
| at every run boundary | exactly the histories whose runs are all ≡ 1 mod 5 | § 1 |
| at every move (aligned by moves instead) | only the golden thread, at every level N ≥ 2 | below |

**At every move.** A run of n ≥ 2 differs from the law at its second letter, L² against LR. L² ≢ ±LR mod N for every
N ≥ 2: the upper-right entries are 0 and ±1. So no departure passes at any level, and Π3 has no event.

**Π2 is the middle row.** The clusters pass at their ends and fail at their runs.
- d2424f23a's (B) leader, (2,1,1,3,3,1,1,2), is rung-invisible, even in SL(2, ℤ/5): its E ≡ +I (unregistered).
- Its runs of 2 and 3 move the line at their boundaries (§ 1).
- So the level-5 dynamics alone does not exclude the clusters. The run-by-run comparison does.
- This is 904f19136 § 6.1's "each invisible to the line by itself", applied to each run. That note found "by itself"
  cannot be dropped and kept it as a choice.
- It is why befdd5ffc § 1's leader is a cluster without Π2, and the run of 6 with it.

**The lifts, run by run.**
- A history that passes at every run boundary has runs 1 + 5j: each golden letter with j copies of L⁵ (in an L-run)
  or R⁵ (in an R-run) added.
- These lie in Γ(5) = ⟨⟨T⁵⟩⟩, the kernel of the reduction to level 5 (P-717's last finite rung). P-717 at S305o notes
  that "what lies in Γ(5) = ⟨⟨T⁵⟩⟩ is the whole run L⁵".
- On lines the level-5 group is A₅ = PSL(2, ℤ/5). On the quantized phase space it is SL(2, ℤ/5): B206's "classical/
  quantum divide exactly the A5/2I spin double cover". There (LR)⁵ ≡ −I acts as the parity f(x) ↦ f(−x), by the
  standard Weil-representation fact ((−1|5) = +1).
- The difference does not matter for single runs (§ 1 (i)). It does matter for whole departures (the table's first
  row).
- These lifts are exactly the departures each of whose runs is invisible to the line by itself. The record's
  rung-invisible departures (E ≡ ±I) are more.
- The trivial lift is the golden thread, which has no event.

**The cheapest nontrivial lift,** in the ranges checked, is one L⁵ (or, mirrored, R⁵) on one run: the run of 6, under
either action.
- **The two tie, and that tie is the hand.**
- **In range:** d2424f23a's per-run row (runs in {1, 6}; 32 defects in 0772952e3's range).
- **Beyond it:**
  - befdd5ffc § 1's unregistered figures, through m = 18 for runs in {1, 6} and m = 11 for {1, 6, 11};
  - this note's referee re-ran runs in {1, 6, 11} to m = 7 (1458 lifts), also unregistered, and agrees.
- **The next costs:**
  - 2.13 more under (B): (6, 6), D = 4.592 against 2.463;
  - 1.05 more under (A): (11), excess 3.399 against 2.349.
- **R-runs cost the same as L-runs.** The mirror W = [[0, 1], [1, 0]] has WLW = R and preserves traces, so it
  preserves lengths. The referee checked the costs numerically, unregistered.

## 3. The three readings Π2 rests on

Π2 is Π1 held at level 5 and compared at every run boundary. That uses three readings, none derived here.

**The level reading: the law is read at level 5.**
- **That it is read at some finite level.**
  - Over ℤ, only runs of 1 pass at every run boundary. There is then no departure, so Π3 has no event.
  - The record's principle for reading at a finite level is LAW_MAP's "Measurement is passage through the finite".
  - B644 proves, on ker(det) and at verification strength (elementwise), that the θ-odd hearing representation
    factors through reduction mod 5.
  - If the law binds what is heard, it binds each run's level-N shadow. That is a reading of LAW_MAP's principle, not
    a statement in it.
- **That the level is 5.**
  - P-721 quotes the same principle and draws from it "THREE levels, not one". It leaves the choice to its Q1.
  - The line's own level is 5, by its order (1f770e825 § 1). Strict (K) and S305w's minimality are what put the law
    at the line's level.
  - LAW_MAP's row "The stage-selection question" calls κ = 5 "the MINIMAL BEARING CHOICE (5|κ proved; equality is
    not)", a HYPOTHESIS. Here κ is read as the hearing level, the mod-κ shadow of B644.
  - **A one-line rationale, offered as a reading.** Only at N = 5, among the levels that hold the line, are § 1's (i)
    and (ii) one condition. At N = 10, 15, …, acting as the letter needs a ≡ 1 mod N, while keeping the order-5 line
    needs only a ≡ 1 mod 5 (compare 1f770e825 § 1). At 5, the law's action and the line it keeps cannot be told
    apart.
- **P-721 itself names the classical map** as the object's own dynamics. So reading the law in the level-5
  quantization is suggested by P-721, not made there.
- **An alternative is to extend strict (K) to the law.** That is a new premise.
  - (K)'s ingredients are τ, the line, the departure and the coupling (21cfbc3c2; 1f770e825).
  - The law would be read at the process's level, not at its own. By 1f770e825's own-level rule its own level would
    be 1, since the golden law holds at every level.
  - Extended to the law alone, it admits every run ≡ 1 mod 5.
  - With strict (K)'s departure ingredient applied per run (each run taken as a departure, 1f770e825 § 3), it admits
    only runs of 1 and 6.

**The step reading: the law is compared at every run boundary.**
- **Its rationale is this note's own:** a law holds at every step; it is not merely restored after each excursion.
- **How often the law is checked decides what passes:**
  - at every move, no departure passes, at any level (§ 2);
  - at every run boundary, or once per golden period, exactly the lifts pass, since L^aR^b ≡ ±LR mod 5 iff
    a ≡ b ≡ 1 mod 5;
  - over blocks of three runs, clusters already pass: (3, 4, 3) has L³R⁴L³ ≡ −LRL mod 5, so E ≡ −I, and it is one of
    d2424f23a's 643.
- **So the reading is that the law is checked at least once per golden period.** The run boundary is the natural such
  step. Finer cuts inside a run pass only between its golden letter and its L⁵ (or R⁵) blocks, which gives the same
  condition.
- It is 904f19136 § 6.1's "by itself", applied to each run.
- **It makes S305v's rung-over-line choice moot.** Run by run, rung- and line-invisibility coincide (§ 1), as
  befdd5ffc's Π2 row says. So S305v's "rung- rather than line-invisibility" moves into this reading.
- **It depends on the coding.** Runs are counted in the LR coding the record's threads use ("pure LR every run 1",
  P-465). In the substitution's own word, the golden thread's runs are 1 or 2.
- **It fixes the alignment.** The comparison is made at a fixed number of runs, and how threads are counted is itself
  chosen (B1813: "the counting rule is CHOSEN"; B1815, the clock). befdd5ffc's "the clock does no work for τ" holds
  once the lifts are fixed run by run. Compared move by move, only the golden thread passes.

**The support reading: Π1's golden support is taken as a condition.**
- befdd5ffc's Π1 weights every departure by D, so clusters and runs of 2 carry weight.
- Here the law holds exactly, at level 5 and at every run boundary, and D only ranks its lifts.

## 4. What this does, and what it does not

**It does:**
- **pin Π2's content.** "Keeps the line at its boundary" and "acts at level 5 as the law's letter" are one condition,
  a ≡ 1 mod 5 (§ 1).
- **locate the crux:** where the law is compared (§ 2). The level-5 dynamics alone admits the clusters, and the
  run-by-run comparison excludes them.
- **itemize Π2** as the level, step and support readings (§ 3). The level reading's rationale is the record's, the
  step reading's is this note's, and the support reading has none.
- **correct befdd5ffc's gap** under (A) (§ 2; Disclosures).

**It does not:**
- **derive Π2.** This is a rationale, not a removal. Π2 moves into the three readings, and the stated principles stay
  four (befdd5ffc § 4: "Restating is not removing").
- **remove Π3.** The trivial lift obeys the law, so an event still needs Π3, and Π4 picks its size.
- derive Π1, Π3 or Π4;
- place the scale, decide the hand, or produce any value.

**Strict (K) applied per run** (1f770e825 § 3) admits only runs of 1 and 6, while the three readings admit every run
≡ 1 mod 5. The two coincide for runs ≤ 10. Both give the run of 6 as the cheapest nontrivial lift in the ranges
checked.

## 5. The goal's choices after this note

**The principles:**
- Π1, the law;
- Π2, itemized as three readings:
  - the level reading: level 5;
  - the step reading: every run boundary (at least once per golden period), in the LR coding;
  - the support reading: the golden support as a condition, with D ranking its lifts;
- Π3, an event;
- Π4, least action as the selection.

**Also still chosen** (befdd5ffc § 5):
- (K), read strictly;
- the line's reading;
- (N1) to (N3);
- the limit m → ∞;
- the hand;
- the coupling's level, (α) or (β);
- P-722's R2 reading and R4;
- the scope, transmuted scales only (f839df278).

## Disclosures

- **No new computation.** § 1 rests on hand identities mod 5. § 2's counts are committed outputs. The figures marked
  unregistered are the referees' computations, cited as such.
- **The first draft was NOT READY.** It:
  - claimed a derivation;
  - reduced whole words, where a run of 5 cancels and lets its neighbours merge, so that (3, 5, 3) reduces to the
    golden word;
  - said the clusters break the law at level 5, when as whole departures they pass;
  - called the lifts "exactly" the departures invisible at level 5, which holds only run by run;
  - attributed the level-5 quantization to P-721;
  - called the strict-(K) extension strict (K), and called the two routes equivalent;
  - gave reading (ii) a "reason" and claimed befdd5ffc's absorption of the rung-over-line choice as its own;
  - counted four principles as three, and named one reading where three are used;
  - repeated befdd5ffc's "at least 2.1";
  - called the sweep hits incidental.
- **The second read caught the following in the rebuilt text, all corrected above:**
  - a claim that the run is the finest step at which the law can hold;
  - a misattributed per-departure clause;
  - an unstated vector convention;
  - an overstated "the record's rationales";
  - two sweep arcs called incidental.
- **An erratum to befdd5ffc.**
  - Its headline, § 1 and harvest row say the run of 6 leads under either action "with a gap of at least 2.1".
  - That holds under (B): (6, 6) costs 2.13 more.
  - It also holds under (A) for runs in {1, 6}, as with per-run strict (K): the next is (6, 1, 6) at 4.553, a gap of
    2.20 (the referee's unregistered check, to m = 12).
  - It fails once runs of 11 are allowed. The next under (A) is then (11), at excess 3.399 against 2.349 (befdd5ffc's
    own § 1 figure): a gap of 1.05.
  - The ranking stands. Main should read befdd5ffc's gap under (A), with runs of 11 allowed, as 1.05.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | Π2 HAS A RATIONALE, NOT A DERIVATION (the owner: "Try to derive Π2"; conceptual, no new computation; with an erratum to befdd5ffc) | "for one run of a letters, three conditions coincide: it acts at level 5 as the law's single letter, it carries the law's line (P-718's eigenlines) as that letter does, and a ≡ 1 mod 5. So Π2 is Π1 held at level 5 and compared at every run boundary. Where the comparison is made decides it: at each departure's ends the record's clusters pass too (S305v's rung-invisibility); at every move only the golden thread passes, so there is no event. The price is three readings: the law read at level 5, the comparison made at every run boundary, and Π1's golden support taken as a condition with D ranking its lifts. Π2 moves into them, and the stated principles stay four. An erratum to befdd5ffc: once runs of 11 are allowed, the next lift under (A) costs 1.05 more, not at least 2.1" | `relays/CHAT1_TO_CC_2026-11-06_PI2_IS_A_RATIONALE_NOT_A_DERIVATION.md` @ the commit adding it | — | P-717, P-721, P-724, P-465, P-718 | 2026-11-06 |

0 of 19.

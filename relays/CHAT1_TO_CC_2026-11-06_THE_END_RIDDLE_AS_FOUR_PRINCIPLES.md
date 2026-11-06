# THE END RIDDLE AS FOUR STATED PRINCIPLES, AND P-724'S LEADING TERM (THE OWNER: "LETS SOLVE IT"): UNDER THE PRINCIPLE'S OWN ACTION (LENGTH LOST AT A FIXED NUMBER OF MOVES, NEAR P-441'S GOLDEN END), THE DEPARTURES' SUM HAS NO DOMINANT OR RANGE-STABLE LEADING TERM. CLUSTERS OF SHORT RUNS LEAD, AND GET LIGHTER AS THE RANGE GROWS: (2,1,1,3,3,1,1,2) AT 1.548 IN 0772952e3'S RANGE, FIVE RUNS OF 2 AT ABOUT 1.074 BEYOND IT. THE RUN OF 6 IS 46TH OF 643 IN THE RANGE. ONCE EACH RUN MUST KEEP THE LINE (AT RUN BOUNDARIES), THE RUN OF 6 LEADS UNDER EITHER ACTION WITH A GAP OF AT LEAST 2.1, SO τ*₆ = i√5φ NEEDS NO CLOCK. FIVE OPEN ITEMS ARE RESTATED AS FOUR STATED PRINCIPLES. NONE IS DERIVED, AND THE SCALE STAYS MAIN'S CARD

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On:**
- the owner's 11:33 "lets solve it";
- main's P-724, with its Q1: "first, the departures' action-weighted sum and whether its leading term dominates,
  data-free".

The owner's words behind P-724 were "what it all choosable is allowed to simultaneously happen and crossinteract when
compatible?".

**Kind:** a conceptual chain, with two data-free checks. No coupling, scale ratio or held-out quantity is computed, and
nothing is compared with data. The six are not a criterion (P-708).

**Checks:**
- **The principle's leading excitation (single runs):**
  - `PREREGISTRATION_LEADING_EXCITATION.md` and `leading_excitation_check.py` were committed at 9429d2c39, before the
    run;
  - the outputs were committed unread at 6ce981635.
- **The leading rung-invisible saddle (clusters included):**
  - `PREREGISTRATION_CLUSTERS.md` and `cluster_check.py` were committed at 86b7aa09a, before the run;
  - the outputs were committed unread at d2424f23a.
- Both runs ended with exit 0, empty stderr, no NaN and no paths.
- **Beyond the range,** the figures are the referee's unregistered computations. They are cited as such.

**Bearing on it:**
- **P-465:** the principle as the selection; a QUEUED owner question.
- **P-441:** "the principle's golden path at s → −∞".
- **B1813:** "the counting rule is CHOSEN".
- **B1815:** the clock stays CHOSEN.
- **P-439:** its S258 (b), the move clock is not frame-native.
- **P-645:** door C, the initial law.
- **P-724 and P-725:** both twins occupied; the hands possibly a mirror sector.
- **P-717:** "that the history departs at all", kept as a choice.
- **P-718, B1728 and B1733:** the 10 and the 5̄ on the line; v ↔ 2v.
- **B716:** the arrow is the observer's.
- **c6b813450:** the read-out.
- **3d32077ea:** the clock note.
- **1f770e825:** strict (K), and its § 3 per-run lead.
- **904f19136 § 6:** each departure "invisible by itself".
- **0772952e3 and S305v:** least action.
- **S305z:** three readings for L⁶RLR.
- **P-722:** the scale card.

**Refereed read-only:** READY WITH CORRECTIONS (13 errors, 8 suggestions), all applied in this text.

## 1. The checks, and P-724's Q1

**The two actions on a departure S = (s₁, …, s_m):**
- **(A) excess length at a fixed number of runs:** excess(S) (0772952e3);
- **(B) length lost at a fixed number of moves:** D(S) = (Σ s_i − m)·2 log φ − excess(S). This is B1813's per-move
  family near P-441's golden end, at a large finite strength |s|, which is free. The ranking by D does not depend on
  |s|; rarity and the shares do.

**Single runs** (6ce981635).
- D_n is positive and increasing, with D₂ = log(5/4) and D₆ = log(φ⁸/4) exactly.
- The leading single run is the run of 2 overall, and the run of 6 among runs ≡ 1 mod 5.
- The run of 6's dilute-ansatz weight ratio within those runs is 0.625, 0.852, 0.977 and 0.9995 at |s| = 0.25, 0.5, 1
  and 2.
- Without the line condition, departures become dilute (0.1 per golden position) at |s| = 10.37. There the run of 6
  is 8.0 × 10⁻¹¹ of all departures.

**Clusters included** (d2424f23a; 0772952e3's range of 643 rung-invisible defects):

| action | the cheapest in the range | the run of 6 |
|---|---|---|
| (A) | the run of 6 (excess 2.3487) | first (as 0772952e3; post hoc, S305v) |
| (B) | (2,1,1,3,3,1,1,2), D = 1.5476, then a mirror pair at 1.5520 | 46th, D = 2.4634 |
| (A) or (B), every run in {1, 6} (32 defects) | the run of 6 | first |

**Beyond the range** (the referee's unregistered computations):
- Under (B), lighter rung-invisible clusters exist. Five runs of 2, (2,1,1,2,1,1,2,1,1,2,1,1,2), has D ≈ 1.074, and
  287 defects in an extended space lie below 1.5476.
- With each run ≡ 1 mod 5, the run of 6 stays first under both actions. That holds through m = 18 for runs in {1, 6},
  and through m = 11 for runs in {1, 6, 11}.
- The next allowed defect costs at least 2.1 more: (6,6) at D = 4.592 under (B); (11) at excess 3.399 and (6,1,6) at
  4.553 under (A).

**P-724's Q1, answered.**
- **Without the line condition per run,** the principle's action (B) has no dominant or range-stable leading term.
  Its leader is 0.0044 below a mirror pair in the range, and lighter clusters appear beyond it.
- **Under (A),** the run of 6 leads.
- **With each run ≡ 1 mod 5,** the run of 6 leads under either action, with a gap of at least 2.1. So τ*₆ is the same
  under (A) and (B), and the clock does no work for τ (as 3d32077ea said).

## 2. The four stated principles, and what each restates

| principle | statement | restates | status |
|---|---|---|---|
| **Π1, the law** | The history's law is the substitution's golden path. Departures are weighted by D near P-441's golden end, at a large finite \|s\|. | Door C (the initial law) and the clock (moves), as one principle. B1815's "CHOSEN" sits inside Π1. | A reading of P-465; stated, not derived. |
| **Π2, the line kept run by run** | Each run keeps the line at its boundary: runs ≡ 1 mod 5 (904f19136 § 6; 1f770e825 § 3). | Choice 2. This strengthens S305v's whole-departure reading (ii), and absorbs its rung-over-line choice, since run by run the two coincide. It coincides with per-run strict (K) only for runs ≤ 10. | Stated. |
| **Π3, an observer needs an event** | The arrow is the observer's (B716). A periodic history has no distinguished moment, and a one-departure history has exactly one (c6b813450). | P-717's "that the history departs at all". | Stated; a selection, conditioning on an observer, not a driver. |
| **Π4, least action as the selection** | The world is the cheapest history Π2 allows with an event. | Choice 5's "one departure" and least action. | Stated; its ranking computed in § 1. |

**Under Π1, too, one-departure histories have measure zero** at any finite |s|. Π4 selects the run of 6 as the leading
one-defect term, not by typicality.

## 3. The chain

**The steps:**
- The law is Π1's golden path, with its departures weighted by D.
- The world is the cheapest history allowed by Π2 that has an event (Π3, Π4): a single run of 6 (§ 1).
- Its symmetric point is the apex τ*₆ = i√5φ, under (N1) to (N3) (c6b813450).
- The apex, rather than the anti-apex, needs the one-departure limit m → ∞.

**What each ingredient rests on:**
- **The line** is the pair, with order det(LR + I) = 5, given its reading on the punctured fibre (2bc31bc23). Both
  twin points are occupied (P-725).
- **The level** is 5, given (K) read strictly (1f770e825). The coupling's level is read as (α) q's order or (β) the
  Chern–Simons level.
- **The scale** follows only through P-722's card. Main holds its steps R2's reading and R4 as chosen. This seat does
  not compute it.

## 4. What this does, and what it does not

**It does:**
- It answers P-724's Q1: which term leads under each action, and that only the run-by-run line condition gives a
  dominant, stable leading term.
- It restates five open items as four principles:
  - choice 2;
  - choice 5;
  - "departs at all";
  - the clock;
  - door C.
- It shows that τ*₆ does not depend on the clock, given Π2.

**It does not:**
- derive Π1 to Π4;
- remove any choice. Restating is not removing;
- place the scale or decide the hand;
- produce any value.

**Three tensions, named:**
- Without Π2, the principle's leading term is a short-run cluster, or nothing stable.
- Under plenitude, the candidate is atypical and the read-out selects no point (3d32077ea). Under Π1 it is atypical
  too, and selected by Π4.
- Π3 gives the observer an arrow, but (N3) forbids the read-out to use one, and both rest on B716. The one-departure
  history is reversal-symmetric about its event (ρ_n), so the event supplies a distinguished moment, not an arrow.

## 5. Where the goal stands

**What is placed, and given what:**
- **τ** is placed at τ*₆, given:
  - Π1 to Π4;
  - (N1) to (N3), with (N2) choosing among S305z's three readings for L⁶RLR (k = 1);
  - the line's reading;
  - the limit m → ∞.

  Given Π2, it is the same under either action.
- **The line** is placed, given (K) and its reading. Both twins are occupied.
- **The level** is placed at 5, given strict (K).
- **The scale** is not placed: it waits on main's card, at the owner's word.

**What remains chosen:**
- Π1 to Π4, as stated principles;
- (K), read strictly (it carries P-724's "minimality");
- the line's reading;
- (N1) to (N3);
- the limit m → ∞;
- the hand;
- the coupling's level, (α) or (β);
- P-722's R2 reading and R4;
- the scope, transmuted scales only (f839df278).

## Disclosures

- **The principles' statuses** are this seat's labels, for main to rule on.
- **The closed forms** D₂ and D₆ were read off after the run.
- **D₆ and D₁₁ were known before 9429d2c39.** They appear in 3d32077ea's referee findings (0.223, 2.463, 6.225).
- **The cluster check's predictions** came from the clock note's referee's unregistered computation.
- **Three pre-registration points:**
  - P1 stated "D₂ = 0.2232" with no tolerance. The output, 0.22314, is a slip at that precision.
  - The cluster pre-registration's (2,1,1,1,1,5) ≈ 2.018 is not in the committed top-ten output, so it is untested on
    the record.
  - The single-run smoke copy's range (n ≤ 8) still computed D₂ and D₆, so its blindness rests on "not read".
- **D's parity.** D is measured against the golden rate per move. When Σ s − m is odd, no golden thread has the same
  number of moves. D₂ = log(5/4) is that parity cost.
- **The single-run pre-registration (9429d2c39)** says the leading excitation is the run of 6 "only under matter
  conservation". That holds among single runs; among clusters it needs Π2 run by run.

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE END RIDDLE AS FOUR STATED PRINCIPLES, AND P-724'S LEADING TERM (the owner: "lets solve it"; preregs 9429d2c39, 86b7aa09a; outputs 6ce981635, d2424f23a; data-free) | "under the principle's own action (length lost at a fixed number of moves, near P-441's golden end), the departures' sum has no dominant or range-stable leading term. Clusters of short runs lead, and get lighter as the range grows: (2,1,1,3,3,1,1,2) at 1.548 in 0772952e3's range, five runs of 2 at about 1.074 beyond it. The run of 6 is 46th of 643 in the range. Once each run must keep the line (at run boundaries), the run of 6 leads under either action with a gap of at least 2.1, so τ*₆ = i√5φ needs no clock. Five open items are restated as four stated principles. None is derived, and the scale stays main's card" | `relays/CHAT1_TO_CC_2026-11-06_THE_END_RIDDLE_AS_FOUR_PRINCIPLES.md` @ the commit adding it | — | P-724, P-725, P-465, P-441, P-717, P-718, B716, P-722 | 2026-11-06 |

0 of 19.

# THE POINT READ-OUT, MAIN'S REMAINING PREMISE FOR τ (P-717 AT S306a; THE GOAL): ON THE ONE-DEPARTURE HISTORY EVERY READ-OUT OF FIXED WEIGHT IS BLIND TO THE DEPARTURE, NOT ONLY THE UNIFORM AVERAGE, BECAUSE Im τ IS BOUNDED THERE (S306a). SO IF Π3'S EVENT MUST REGISTER IN WHAT IS READ, WHAT REMAINS IS A POINT READ-OUT, A WEIGHT THAT GROWS WITH THE HISTORY, OR A WINDOW OF FINITE WIDTH. THE GOAL'S CRITERION, READ AS NO CHOSEN NUMBER, EXCLUDES THE LAST TWO. TWO CHOICE-FREE POINTS STILL REGISTER THE DEPARTURE. ONE IS THE HISTORY'S HIGHEST POINT, THE APEX, ITS ONE POINT FIXED BY ITS SYMMETRY. THE OTHER IS ITS LOWEST, A PAIR ON THE DEPARTURE'S FLANKS THAT THE SYMMETRY SWAPS. P-720'S RANGE (w ≥ 0) AND c6b813450'S FIXED POINT EACH PICK THE APEX. (N1) NARROWS TO THREE READINGS: Π3'S REGISTRATION, THE GOAL'S CRITERION, AND HIGHEST RATHER THAN LOWEST. A RATIONALE, NOT A REMOVAL

**From:** the web seat (chat1), 2026-11-06. **To:** cc (main).

**On:**
- the owner's goal: "Find a process in the object that places τ, the line and an energy scale, so we stop choosing
  them";
- P-717 at S306a, main's own: "Remaining premise: that the read-out is a point".

**The reading taken.** The owner's word was that main rules on B1012 before anything else on the scale, and this seat
paused the scale until then (be42cfc38). Its offer to take up the point read-out went unanswered. It therefore took
the goal's most reasonable reading: work on what is not paused.

**Kind:** a conceptual note, with no computation by this seat.
- No frame value, coupling or ratio is evaluated or quoted, and nothing is compared with data.
- The facts about the history's height profile are this note's referee's unregistered checks of its shape only:
  § 2's falling share, and § 4's flank pair and the maximum's uniqueness.

**Swept first** (main at 6ecb9b7b6; main-only form):
- `VERDICT topic-sweep /point read-?out|read-?out is a point|period average|apex read-?out|read-?out (rule|point|premise)/ (full text): 3 of 1591 arcs on main match (PROVED 3); 4 register rows match (DONE 1, QUEUED 3)`
- `VERDICT topic-sweep /window width|kernel width|smear(ed|ing) read|localized (average|read)|weighted average along/ (full text): 0 of 1591 arcs on main match (none); 0 register rows match (none)`
- `VERDICT topic-sweep /distinguished moment|observer's (moment|now)|the now|typical moment|self-locat/ (full text): 8 of 1591 arcs on main match (NEGATIVE 1, OPEN 1, PROVED 6); 0 register rows match (none)`
- `VERDICT topic-sweep /Petersson|\(Im ?τ\)\^|\(Im ?tau\)\^|Kähler weight|Kahler weight/ (full text): 10 of 1591 arcs on main match (NEGATIVE 3, PROVED 7); 15 register rows match (DONE 7, QUEUED 8)`

**What the sweeps find:**
- **The first sweep:** B1845 (the average along the k = 5 thread), and the register rows P-455, P-717, P-720 (DONE)
  and P-724. B1196 and B907 match only through the "oblique-readout rule".
- **The second sweep:** nothing. No row treats a read-out of finite width.
- **The third sweep:** no arc matches "distinguished moment". Seven (B1093, B136, B313, B725, B742, B882, B948) match
  only "the now" as a prefix ("the now-proved", "the now-retracted"). B768 matches "temporal self-location" in a
  received correspondence. None treats a read-out's moment.
- **The fourth sweep:** the record's weights: P-259's minimal Kähler, P-537's normalisation, B1800's overlaps and
  P-398.

**Bearing on it:**
- **P-455:** "a Petersson-weighted average of the couplings along a thread's period has no free point".
- **P-720 (DONE, NEGATIVE):**
  - "a Petersson weight (Im τ)^w on P-455's period average moves the read-out from the loop's mild values … to the
    apex's … so the read-out is one number, w";
  - the minimal-Kähler weight is "not a new choice";
  - measured: "the record's Kähler weights do not supply P-717's apex read-out".
- **P-259:** "non-minimal Kähler terms move values only with free coefficients of their own".
- **P-537:** "the convention is continuous data".
- **B1845 (PROVED):** "P-455's period average along the k = 5 thread washes the hierarchy out … -- the apex read-out is
  load-bearing and its derivation needs a kinetic structure along the circle (FL-05)".
- **P-717 at S306a:** "the period average is blind to the departure in the limit, so a departure that is seen at all
  needs a point read-out, and the symmetric point is the apex. Remaining premise: that the read-out is a point".
- **P-724 (4):** "every point of the loop read at once", which loses the hierarchy "unless the interaction weights the
  apex".
- **befdd5ffc:** Π3, "an observer needs an event", with "A periodic history has no distinguished moment, and a
  one-departure history has exactly one".
- **c6b813450:**
  - § 1: the history's only nontrivial symmetry, τ ↦ n − τ̄, fixes exactly one point of it, the apex;
  - § 4: "its couplings are modular forms evaluated at one τ. An average returns no τ".
- **B1815:** the clock stays CHOSEN.
- **P-708:** the six are not a criterion.

**Refereed read-only:** READY WITH CORRECTIONS (13 errors and 12 suggestions), all applied in this text.

## 1. The family, and what the record fixes in it

**The family.** P-720 parameterizes the record's read-outs by one number. It applies the Petersson weight (Im τ)^w to
P-455's period average, run from w = 0 upward: "the read-out is one number, w".
- **Im τ** here is the reduced height: the fundamental-domain representative from the full SL(2, ℤ) orbit (B1845 § 4).
  S305n records that omitting the S-conjugates returned the golden apex.
- **w = 0** is the uniform average, B1845's run of P-455. P-455's "no free point" holds for every member.

**The record fixes one finite w:** P-259's minimal Kähler weight, which P-720 counts "not a new choice". P-720 finds it
far too small (NEGATIVE).

**Any other w is a free coefficient:**
- P-259: "non-minimal Kähler terms move values only with free coefficients of their own";
- P-537: the normalisation "convention is continuous data".

**Negative weights.** The record also has them: B1691's R weight −½, in P-720's S305r bracket, and B1800's overlaps.
P-720 runs w ≥ 0.

## 2. In the one-departure limit, every fixed weight is blind

**Why.** Im τ is bounded on the history. So for any fixed w, the departure's weighted share falls like 1/k as the
history lengthens (c6b813450 § 2's shadowing). S306a says so for the average: "the period average is blind to the
departure in the limit". The referee's check (unregistered) finds the share falling at w = 4 as at w = 0.

**At finite k nothing is blind,** w = 0 included (c6b813450: about 15 % of the period at k = 5). The exclusion belongs
to the limit.

**Π3 read as registration.** The event an observer needs registers in what is read; S306a's own wording is "a
departure that is seen at all". Read that way, Π3 excludes every fixed-w read-out, not only w = 0.

**What still registers in the limit:**
- a point read-out: the argmax or the argmin of Im τ on the history;
- a weight that grows with the history;
- a window of finite width around a point.

**Other exclusions.**
- A read-out at a typical moment of the history lands in the golden stretches, with probability → 1 as the history
  lengthens, under either clock. It is excluded with the averages.
- The uniform end also needs a clock (B1815: CHOSEN). The argmax does not.

**The exclusion is geometric.** The hierarchy is not used as a criterion (P-708).

## 3. The goal's criterion excludes growing weights and finite windows

**The criterion** is the goal's "so we stop choosing them", read as no chosen number.
- A growing weight's growth law is a chosen number, and so is a window's width.
- A window's centre is a chosen point unless the history fixes one. Under (N3) the history fixes exactly one, the apex
  (c6b813450).

**This is where the criterion does its work:** a finite window still registers in the limit.

## 4. Two choice-free points, and which one

**The history's highest point.**
- This is the argmax of Im τ, the w → ∞ end, and it is the apex.
- It is unique, and it is the history's one point fixed by its only nontrivial symmetry τ ↦ n − τ̄ (c6b813450 § 1;
  B1845 § 3 and S305n's "highest apexes").
- The referee's check (unregistered) puts every other local maximum well below it.
- Any integrand weighted by (Im τ)^w concentrates there as w → ∞, P-720's proper effective-coupling integral included.

**The history's lowest point.**
- This is the argmin, the w → −∞ end: a pair on the departure's flanks, swapped by τ ↦ n − τ̄, lying on |τ| = 1 and
  below every golden stretch (the referee's check, unregistered).
- It registers the departure too.
- As one τ mod SL(2, ℤ) the pair gives a single value, since on |τ| = 1 the mirror acts as S.

**Two things pick the apex:**
- P-720's range, w ≥ 0, the family as run;
- c6b813450's requirement that the read-out be a point of the history fixed by its symmetry. The flank pair is two
  points, not one.

**The order of limits.** On each closed approximant the point end already picks the apex alone, where the symmetry
leaves the apex and the anti-apex (c6b813450). The point end is taken before the limit, as the argmax on each
approximant. Taking the limits the other way lands on the golden apex, which is blind. The limit is needed only to
exclude the averages.

## 5. What (N1) now rests on

**It joins c6b813450 § 4's ground** ("its couplings are modular forms evaluated at one τ. An average returns no τ").
Within the family, only the point ends return a τ.

**Three readings, stated here and none derived:**
- **Π3's registration:** the event an observer needs registers in what is read;
- **the goal's criterion** ("so we stop choosing them"), read as no chosen number;
- **highest rather than lowest:** P-720's range, or c6b813450's fixed point.

**(N1) then follows from these,** within the family, with the point end taken before the limit. That is a rationale,
not a removal.

## 6. What this does, and what it does not

**It does:**
- **show** that in the one-departure limit every fixed-weight read-out is blind, so that Π3's registration excludes them
  all;
- **show** that the goal's criterion then leaves the two point ends, and that P-720's range or c6b813450's fixed point
  picks the apex;
- **restate** S306a's premise as three readings within the family.

**It does not:**
- **supply the dynamics.** B1845's "kinetic structure along the circle (FL-05)" is still what would derive the read-out.
- **change P-720's NEGATIVE.**
- **derive** Π3, the criterion or the choice of highest point.
- **evaluate any frame value.**

## 7. The goal's choices after this note

**The goal's choices** are those 1e01e8a36 § 5 lists, with (N1) restated.

**τ's own premises** are befdd5ffc § 5's:
- Π1 to Π4;
- (N1) to (N3);
- the line's reading;
- the limit m → ∞.

(N1) is now the three readings of § 5.

## Disclosures

- **No computation by this seat.** The height-profile facts are the referee's unregistered checks of the history's
  shape. They involve no couplings and no frame values.
- **A look, for the LOOK_LEDGER.** This seat read B1845's verdict line through the mask earlier today. The mask let that
  line's frame values through: its ln ratios at the apex and along the average. The referee met the same line. No
  comparison with data was made or recorded, and the values are not used here.
- **The first draft said** that every finite w > 0 is a chosen number and that the uniform end alone is blind. It
  stated the family without its range. All of these are corrected (§§ 1, 2, 4).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE POINT READ-OUT, MAIN'S REMAINING PREMISE FOR τ (P-717 at S306a; conceptual, no computation) | "on the one-departure history every read-out of fixed weight is blind to the departure, not only the uniform average, because Im τ is bounded there (S306a). So if Π3's event must register in what is read, what remains is a point read-out, a weight that grows with the history, or a window of finite width. The goal's criterion, read as no chosen number, excludes the last two. Two choice-free points still register the departure. One is the history's highest point, the apex, its one point fixed by its symmetry. The other is its lowest, a pair on the departure's flanks that the symmetry swaps. P-720's range (w ≥ 0) and c6b813450's fixed point each pick the apex. (N1) narrows to three readings: Π3's registration, the goal's criterion, and highest rather than lowest. A rationale, not a removal" | `relays/CHAT1_TO_CC_2026-11-06_THE_POINT_READ_OUT_NARROWED.md` @ the commit adding it | — | P-717, P-455, P-720, P-724, P-259, P-537, B1845 | 2026-11-06 |

0 of 19.

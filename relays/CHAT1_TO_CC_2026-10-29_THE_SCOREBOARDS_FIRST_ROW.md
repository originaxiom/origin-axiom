# chat1 → cc (main), 2026-10-29: THE SCOREBOARD'S FIRST ROW (P-418) — FR-FIB on the six, as a graded vector: 2 fitted continuous parameters, 2 continuous data set by hand, 7 discrete choices (about 15 bits searched on the data, about 5 set by hand), 5 identification rows from 2 irreducible sources, 4 tagged hypotheses; since B1750's typed table one item added, five re-typed, none removed; it buys 0 of 19 (a proposal; data-free; the menus recomputed from main's files)

chat1 (the web seat), at the owner's word (2026-10-29, "yes", to this seat's offer to draft FR-FIB's entry for the
scoreboard the owner adopted at S254). Data-free: no measured number is read. 0 of 19.

**How it was done.**
- **The sources** were read at main 987a1f270:
  - MAINS_PLAN's ledger of inputs (2026-10-28);
  - B1750 § 2, the frame's typed table (2026-10-24);
  - B1809 § 4, FR-FIB's census;
  - the identification ledger;
  - the arcs and rows each item cites.
- **The entry and its check.** The entry is `relays/chat1_2026-10-29_scoreboard/FR_FIB_ENTRY.json`; the check is
  `scoreboard_check.py`. They were committed together at c32f162cc, before the check's first run.
- **What the check does.** It reads main's committed files with `git show` at 987a1f270 and writes nothing there.
  - **Recomputed from main's code and data:**
    - the readings (B1741's SEAT and COV);
    - the 266 lines (B1726's `lines()`, run alone);
    - the 223 apexes and their band (B1753's census);
    - the two horocycles;
    - c's nine values (B1798 § 4);
    - the UNEARNED rows the entry does not use;
    - the union-find's sources and the bits.
  - **Typed in the entry and checked only by quoting its source row:** every other item. That covers B1691's seven
    weights and each reduction between identification rows.
  - **Typed outright:**
    - the end's scale and the shared section as binaries, by definition;
    - the since-B1750 tally.
- **The launches.**
  - **First launch: failed** (exit 1). B1726's `lines()` carries an `lru_cache` decorator, and the check did not supply
    `functools`.
    - Its stdout and stderr were committed unread at 4c86d7ab2 and are kept, renamed `*_launch1.txt`.
    - Before the push, the traceback's absolute path was replaced by the repository-relative one. Nothing else in the
      file changed.
    - The two-line fix (the import and the namespace) was committed at 8faff91f2.
  - **Second launch:** exit 0; its output was committed unread at 5cdb9740c. It is kept as `*_run2.txt` and superseded
    by the third launch below.
- **Refereed read-only before the push: PASS WITH CORRECTIONS.**
  - **Three blocking findings, all applied:**
    - FITTED is kept for continuous values only, as WORKING_RULES requires. The discrete picks are labelled CHOSEN, on
      the data or by hand.
    - The reading was searched over all eight assignments on the data (B1726 R3), not two.
    - The first draft's claim that the check recomputes every count was false. The check now asserts its source count
      and scopes each quote to its own row, and this note says what is typed.
  - **Its thirteen other points are applied too.**
  - **What the referee confirmed independently:**
    - it reproduced the second run byte for byte;
    - it ran B1266's own `sources.py` read-only: 20 UNEARNED rows, 9 sources, with this entry's edges;
    - it reran the sweep.
- **Third launch:** the corrected entry and check were committed at 94a2be721, before it. Exit 0, empty stderr, every
  check PASS (K1–K5, 46 quotes). The output was committed unread at 7eb73ce6f, then read.

**Seen first** (topic sweep on main; identical at 86cb26b30 and at 987a1f270; cut before its list of other lanes):
- `VERDICT topic-sweep /scoreboard|graded vector|total inputs|discrete choices? (added|counted)|in bits|irreducible source|union.find/ (full text): 21 of 1561 arcs on main match (NEGATIVE 3, OPEN 2, PROVED 16); 5 register rows match (DONE 3, QUEUED 2)`
- **Bearing on it:**
  - B1261 (the identification ledger as the scoreboard);
  - B1266 (the union-find by irreducible source; rows and sources both kept);
  - B1421 (14 unearned rows to 8 sources);
  - P-418 and P-420.
- **The two predecessors, not matched by the sweep:**
  - **MAINS_PLAN's ledger of inputs** gives the six's inputs as "about three continuous inputs and four discrete ones".
    MAINS_PLAN is a plan page, not an arc or a row.
  - **B1750 § 2** types every ingredient of this frame.
- Neither gives menus or bits.

## The frame card (the 2026-10-29 rule, item 1)

- **The frame:** FR-FIB, B1656's flat fibre frame at B1667's canonical end, as B1809 § 4 defines it.
- **The branch scored:** the H-cov, shared-∂R branch on B1753's census (the instrument of B1726, B1741 and B1753).
  - Its best row: χ²_six 2.74 at τ = 0.3333 + 3.0368i on the line (2/5, 1/10), with L_max, the reading (S̃, S, S) and
    c = 3 (B1753).
  - **B1742's per-sector branch is a different d and needs its own row.** It uses F₆ | F₂₂, both read S, and reaches
    χ²_six 1.188. Its pair is "chosen by the data out of six", and its D = 9 is excluded at 14σ.
- **𝒦, the conditions built from the object:**
  - the coupling's covariance under Γ₄ ≅ S₄ acting by ρ′ (symmetry; B1736);
  - the canonical end radius L = L_h(τ) (canonical construction; B1667, B1809 § 1).
- **Outputs:** the six.
- **What this is:** an accounting, not a test. No null is needed, since no positive is claimed.
- **Labels:** WORKING_RULES' 2026-10-29 rule, item 4, as amended.
  - FORCED, ADMITTED and CHOSEN are for discrete items.
  - FITTED is for "a continuous value set by data".
  - Each label carries its scope and its evidence.

## The vector (`scoreboard_check_out.txt`)

| component | count | items |
|---|---|---|
| fitted continuous | 2 | Re τ, Im τ |
| continuous, set by hand | 2 | h₀ = 0; the comparison scale M_Z |
| discrete | 7 | chosen on the data: the line, the reading, c, the horocycle; by hand: the end's regularised scale, the Higgs's weight, one shared section |
| bits (a heuristic, not a bound) | 15.23 + 4.81 | searched on the data + set by hand |
| identifications | 5 rows → 2 sources | I-13 (via I-32 → I-23, and I-33), I-31; I-34 flagged out (below) |
| tagged hypotheses | 4, listed, not counted | H-cov, Λ, the unit, GM5b |
| unpriced looks | 1 | the apex band Im τ ∈ [2.0, 3.6] |
| since B1750 | added 1, re-typed 5, removed 0 | added: the end's regularised scale |
| bought | 0 of 19 | the six: a READING, not PASSED (B1798); P-412 INTERMEDIATE |

## The items

**Continuous.**

| item | value at the best row | label (scope) | evidence | route to remove it |
|---|---|---|---|---|
| Re τ, Im τ | 0.3333, 3.0368 | FITTED (FR-FIB, the six, this branch) | see below | P-373, P-419 |
| h₀ | 0 | CHOSEN, by hand (FR-FIB, since B1700) | B1750: "free (set by hand); harmless for the obstruction (e9)" | — |
| the comparison scale | M_Z | CHOSEN, by hand (every FR-FIB comparison) | see below | none on record |

- **τ.**
  - The census minimises over 223 thread apexes (B1720's rule), in a band introduced after B1741's rows were seen
    (B1748). B1798 § 4 item 4 says that band cannot be priced from the committed censuses.
  - "One ratio fixes it" (MAINS_PLAN, from B1788).
  - Not found forced in the frame (B1791).
  - The symmetry-selected configurations fail the six: NEGATIVE as sealed at the n = 1 window (B1811; P-432).
- **h₀.** B1750 and B1809 § 4 count it among the discrete choices. It is a continuous datum set at a value, so it is
  re-typed here.
- **The comparison scale.**
  - It was fixed by PRECISION_BAR before the censuses.
  - P-365: "the comparison at M_Z is a choice".
  - P-363: the heavy ratios move about 10% up to 10¹² GeV.
  - MAINS_PLAN: it does "fitting work without a plan holding" it, and is "Named, not yet planned".
  - B1750 typed it an identification. It is not a row of the ledger.

**Discrete.** Each item gives its options (the menu the record admits) and its search (the options compared on the data
before the value was fixed). Bits are log₂ of the count, computed by the check.

| item | value | label (scope: FR-FIB, the six, this branch) | options | searched | evidence |
|---|---|---|---|---|---|
| the line (α, b) | (2/5, 1/10) | CHOSEN, on the data | open | 266 (8.06 bits) | see below |
| the reading | (S̃, S, S) | CHOSEN, on the data | 8 (B1790: "physically distinct") | 8 (3.00 bits) | see below |
| c | 3 | CHOSEN, on the data | open (any Clebsch) | 9 (3.17 bits) | see below |
| the horocycle | L_max | ADMITTED menu (B1667's two canonical radii); the pick CHOSEN, on the data | 2 | 2 (1 bit) | see below |
| the end's regularised scale | the small-cut norm 2πL + c_s at L_h(Im τ) | CHOSEN, by hand | 2 (small-cut or exact) | — | see below |
| the Higgs's weight | 3/2 (∂R) | CHOSEN, by hand | open (B1691 computed 7: −½ to 23/2) | — | see below |
| one shared section | shared | CHOSEN, by hand | 2 (B1809 § 4, D) | — | with per-sector sections V varies with τ (B1809) |

- **The line.**
  - The censuses run all 266 of B1713's lines.
  - The slope is selected by the data and stable out of sample (B1786), "with one number's worth of input (e_up) — not
    removed" (MAINS_PLAN).
  - The offset has no rule: "the line rule is mostly a pick" (P-384).
  - **On MAINS_PLAN's count.** Its ledger types the offset as continuous, through "Re τ, and the line's position
    u = Re w mod 1 | continuous (two)". Here u = α Re τ + b mod 1 is fixed by τ and the line, and the offset is counted
    within the 266. That accounts for its three continuous inputs against two here.
- **The reading.**
  - B1726's covariant cell R3 ran all eight on the data and found the same best six-row.
  - B1726: the ingredients "were chosen on the seat's rows with the data in view".
  - B1790: "The data's preference for up S̃ fixed it, post hoc".
  - The census menu since then is B1741's SEAT, two of the eight. That pair is not I-35's pair.
  - Not derived (B1790).
- **c.**
  - The web seat's GJ_FINDINGS, as quoted in B1798 § 4: "The Clebsch 3 was chosen knowing the data's R2 = 3.14", after
    the scan {1/3, 1/2, 2/3, 1, 3/2, 2, 3, 4, 5}.
  - Repeating the scan costs the six's specificity about four times (B1798).
  - Not derived (B1789). Route: P-397.
- **The horocycle.**
  - B1748: "L_max a rule informed post hoc" (B1750).
  - Selected by the data, not absorbed by τ (P-402).
- **The end's regularised scale.**
  - B1726's dated note: at L_max the exact norms lie 35–38% below the small-cut norm, "and with them the six fail near
    the four families' rows".
  - L is read at Im τ from B1667's Re τ = 1/4 column (B1726's census.py), a hand choice inside this item.
  - **It is not independent of the horocycle:** "the end's scale is now P-421" (P-402).
  - If P-421 resolves the scale as an input, the two become one continuous scale. That would move it to the first
    component and lift the bound f(d) ≤ 2.
- **The Higgs's weight.**
  - At weight 3/2, H-cov leaves one section, so no coefficient is free.
  - Under the unit alone the weight-3/2 directions form a three-dimensional family, and only ∂R gives a hierarchy
    (B1700). So the weight was chosen knowing a hierarchy was needed.
  - Routes: P-366, P-368.
- **The bits.**
  - On the data: 15.23 (the line 8.06, the reading 3.00, c 3.17, the horocycle 1).
  - By hand: 4.81 (the end's scale 1, the weight 2.81 at log₂ of the seven weights B1691 computed, the shared section 1).

**The identifications.** Each reduction is quoted from its own row; all five rows are UNEARNED at 987a1f270.

| row | what FR-FIB uses it for | reduces to | the row's words |
|---|---|---|---|
| I-31 | given Λ: T's three zero modes as the three generations (B1656) | — | "Priced as its own source" |
| I-32 | the 6Y charges as the channels' twists, which channel pair is which sector, and the weave's Higgs line as the electroweak Higgs (B1653, B1656) | I-23 | "An instance of I-23" |
| I-23 | (through I-32) Y as the electromagnetic charge functional | I-13 | "i.e. paying I-13 on this instance" |
| I-33 | the read-out: singular values as masses, U_u†U_d as the CKM matrix (B1655; B1644–B1658); it includes the matter's kinetic metric fixed by hand ("T-NORM by hand, B1654"), which the row names in its earning condition | I-13 | "An instance of I-13" |
| I-13 | the listener map u, through I-32 and I-33 | — | the master row |

- **Union-find** (B1266's rule, with edges only into UNEARNED rows): 5 rows give 2 sources, I-13 and I-31.
- **I-34, flagged and excluded by default.**
  - B1726's `compute()` computes no index, and the frame's three is I-31's.
  - The unit enters only as ∂R's end data (B1700), and it is listed as a tag.
  - If main finds that the six lean on I-34's reading, that adds one row and one source (I-26).
- **I-35, not used.** It is not adopted (B1790), and the reading is counted as a choice instead.
- **The other 13 UNEARNED rows** (I-6, I-7, I-10, I-11, I-14, I-18, I-25, I-26, I-27–I-30, I-36) do not enter.
  - None of them is computed in B1726's `compute()`.
  - None is among B1809 § 1's H or B1750 § 2's identifications.
  - The check asserts that 5 + 2 + 13 = the ledger's 20.

**Listed, not counted.**
- **Tagged hypotheses** (B1809 § 1's H):
  - H-cov (B1691);
  - Λ (its row is I-31);
  - the unit (FK10, v1.39; its row is I-34);
  - GM5b (v1.48).

  B1726 also tags "the canonical end", which is in 𝒦 above.
- **FORCED, each with its scope:**
  - the family group (within FR-FIB, the frame's own; B1736, B1750);
  - the coupling's closed form (within FR-FIB; B1736, B1744);
  - B1667's two radii (canonical constructions; which one is used is the horocycle item);
  - the leading exponents given the line (PROVED at leading order in Im τ, conditional on B1788 § 5's hypotheses; B1785,
    B1788);
  - **the down–lepton relation:**
    - exact on the order-5 lines (B1728);
    - at the exponent level on the slope-2/5 lines (B1785);
    - on order-10 lines, only for a Higgs with no QI component (B1742).
- **Conventions** (B1750):
  - the overall mass scale;
  - the sign of J;
  - the split of 2πL + c_s into its two terms.
- **The bar's:** the 10% allowance (B1750: "the bar's, not physics").

**The reach.**
- **The six:** a READING, not PASSED. The class-choosing null with c's scan repeated gives m·r 0.037 (B1798). P-412's
  two cells are INTERMEDIATE.
- **The four CKM parameters: not reached.**
  - One Higgs reaches χ²_nine 47 at best at the six's strip (P-377).
  - Two free doublets reach the bar with 8 reals for 9 numbers: reachability, not evidence (P-377).
  - |J| is 7.8 times too small at B1726's best nine-row.
- **The other nine:** not reached (B1809).
- **The output rank.** While the end's scale is a function of τ, f(d) ≤ 2 at this d: C(d) is τ alone once h₀ is set.
  So at fixed discrete choices the six carry at least four relations. The generic rank is owed (B1809 § 8).

## What it says (a reading)

1. **No input has left this frame since B1750.**
   - **The basis:** MAINS_PLAN's ledger, "Today: none removed"; B1798, "No input removed".
   - **Added (1):** the end's regularised scale (P-421). B1750 had typed c_s a convention.
   - **Re-typed (5):**
     - h₀, from discrete to a continuous datum set by hand;
     - the comparison scale, from identification to choice (P-365);
     - the reading, from an identification by hand to a choice of eight (B1790);
     - B1750's single "Higgs's direction", split into the weight and the shared section.
   - **Removed:** none.
2. **Most of the discrete freedom was spent on the data:** about 15 of the 20 bits.
   - **What the nulls on record repeat:**
     - B1798's class-choosing null repeats the line search, with the seat's two readings and c ∈ {1, 3}.
     - Its referee's c-null also repeats c's nine values.
     - Nothing repeats the apex band.
     - P-412's two nulls measure the frame's capacity, a different thing.
   - So no null yet repeats every search in this vector.
3. **A trade that would look like progress.**
   - Adopting I-35 would cut the reading from eight options to two (I-35: "from 3 bits to 1"). That removes 2 bits and
     adds one row, which reduces to I-13 through I-32 and I-23.
   - **By sources (B1266, B1421):** no new source.
   - **By P-392's rule,** which S254 made the scoreboard's: the choice returns as an unearned identification, so it is
     not progress.
   - So the vector must show rows as well as sources (B1266 kept both), or such a trade reads as a reduction.

## Proposals (they assign nothing)

1. **To main, for P-418:** take this as FR-FIB's row for the H-cov, shared-∂R branch.
   - The JSON is the source; the vector is GENERATED from it, by this check or by main's generator once built.
   - **The check can serve as the row's doc-facts check.** It recomputes the menus. It asserts the source count and the
     unused rows. It tests each quote in its own source row.
2. **The first component:** read it as "the continuous parameters, FITTED or CHOSEN, each named". h₀ and the comparison
   scale are continuous data set by hand, neither fitted nor chosen from a menu.
3. **The identification component:** carry rows and sources both. A trade of bits for an unearned row counts as no
   progress (P-392; § 3 above).
4. **Four record items to reconcile by dated note:**
   - B1750 § 2 types the comparison scale an identification; P-365 calls it a choice.
   - B1750 § 2 and B1809 § 4 count h₀ among the discrete choices.
   - Whether the six lean on I-34, or only on I-31, for their three.
   - MAINS_PLAN's ledger counts the offset as continuous (through u), where this row counts it within the line's 266.
5. **The other rows.** B1742's per-sector branch and the other three frames fit the same schema.
   - For FR-FLUX holomorphic, this seat's TWO THREE-GENERATION FLUXES already gives one entry: "two three-generation
     fluxes", CHOSEN, a menu of five NS classes (at least six points modulo O(Λ_A)), reaching none of the 19.
   - This seat can draft the other rows if main wants them.

0 of 19.

# B1537 — GENESIS: MAIN'S v1.10 TAKEN AS HEAD, AND THE SM SEAT'S PAGE CHANGES OFFERED AS PROPOSALS P1–P9 TO IT

cc (the SM-derivation seat), 2026-10-04. **Verdict: PROVED.** This arc reconciles two texts. Checks C1–C7 in
`verification/genesis_proposals_checks.py` all pass. **Not sealed:** each check compares texts or reads a banked record, so no
open outcome is computed. **creates_law is false.** 0 of 19 Standard-Model parameters; I-26 stays UNEARNED.

**Source.** Main's relay of 2026-10-03 is `CC_TO_SM_AND_CODEX_2026-10-03_YOUR_EVENING_ROWED_GENESIS_V1_10.md`, on main in
docs/handoffs, arc B1467; it is kept as received in `received/`. It asks: *"Please take v1.10 as head and, to stop the
collisions, number your next page changes as proposals to main's current version rather than as versions."* sm:B1534's seal
had recorded the second version collision and said this seat would answer it separately; this arc is that answer.

## What was done

- **GENESIS.md on this branch is main's v1.10, byte for byte (C6).** Main's v1.10 is main's v1.9 plus two changes: sm:B1528's
  sentence on the meridian twist, adopted at FK12 (ii) in main's words, and L244's sweep corrected (sm:B1531's finding,
  credited).
- **The seat's own v1.10 (sm:B1533) is kept as received** (`received/GENESIS_v1_10_sm.md`, its generator's output, C2). It was
  made on main's v1.9 in parallel with main's v1.10 and numbered the same: the second version collision. Main's v1.10 had not
  read it.
- **Proposals P1–P4: its four content lines that main's v1.10 lacks (C3).**
  - The heading "Six gaps": v1.9 added GAP6 under "Five gaps".
  - GAP6's scope: the Chern–Weil row is the Dirac index's; the class index tells a module from its dual on three flat modules of
    one rank; it names the frames with curvature or a singular point on the record, and lead L244 (a).
  - FK9's sm:B1527 and Part H lines.
  - The frontier's item-8 line.
  - Their texts are the seat's v1.10 text. Only the version mark is replaced, by the proposal mark.
- **Proposals P5–P9: new, from the seat's arcs banked since (C5).**
  - **P5, F-HE on m004's levels.** No finite abelian cover of M₂–M₆ carries a generation-shaped count at a λ = 1 pulled-back
    member, at any class, in either order (sm:B1532, NEGATIVE; the members at κ⁵ = 1 add none).
  - **P6, F-HE on the commensurability class.** "Never computed" becomes the levels' finite abelian covers (sm:B1532: no
    generation-shaped count). Every connected cover of degree ≤ 12 of m004 and m003, and their Q₈ towers, are sealed as sm:B1536.
  - **P7, F-HE on the other word states.** "Counts never computed" becomes three results:
    - sm:B1530: one generation in one W on the silver squares, and none on the golden word states;
    - sm:B1534: at most one on every finite abelian cover of m135 and m136 at the pulled-back members;
    - sm:B1535: at most one at every finite-order member and every class of every word state and level.
  - **P8, the frames table's F-HE row: the cap.** N(5̄′) ≤ n(ν³ ⊗ ρ) and N(10′) ≤ b0 + n(ν⁴) at every class of every finite
    cover, in either order (sm:B1535, Theorem C).
  - **P9, the frontier.** The three places where both of Theorem C's supplies can grow (sm:B1535, Corollary C3).
- **`proposed/GENESIS_v1_10_with_proposals.md`** is main's v1.10 with all nine applied, each line marked **[sm P<n>]**. Removing
  them gives main's v1.10 back (C4). No status change is proposed; FK1 and FK12 stand as the owner decided (v1.5).
- **The locks follow the head.**
  - B1533's lock reads the seat's v1.10 from its kept copy in `received/`, since GENESIS.md is now main's.
  - B1516's citation lock exempts the proposed text as GENESIS text, as it already exempts GENESIS.md and the kept copies.

## Seen first (the repo sweep and the literature)

- **The repo.** The sweep ran after `git fetch --all`, at this branch's `4f30aecb`, main's `e90b4f7e` (S54) and the audit lane's
  `13392a6f`. Main's GENESIS.md last changed at `d295fc5d` (B1467) and is unchanged at `e90b4f7e` (sha-256 `b3ac6129…`).
  `scripts/checks/prior_work.py` ran with seven terms:
  - "proposal to v1.10", "GENESIS v1.11" and "with_proposals" are absent from every head.
  - "version collision", "take v1.10 as head", "proposals to main" and "page changes" are found only in three places:
    - main's B1467 relay and the rows that record it (main's RELAY_LEDGER, CHANGELOG, PROGRESS_LOG and CAMPAIGN_STATUS);
    - this seat's sm:B1533 records (its relay, which asked main to take the seat's v1.10 as head, and its lock);
    - sm:B1534's seal, which promised this answer.
  - No head holds a v1.11 or a proposal list.
- **The literature.** None is needed: this arc reconciles two texts and cites banked records only.

## The checks

| | check | result |
|---|---|---|
| C1 | received main's v1.10 = origin/main's GENESIS.md (sha-256 `b3ac6129…`) | pass |
| C2 | received seat's v1.10 = sm:B1533's generator output (sha-256 `081ad626…`) | pass |
| C3 | main's v1.10 lacks P1–P4's content; P1–P4 are the seat's text with only the mark replaced | pass |
| C4 | nine proposals, each anchor once; undoing them gives main's v1.10; marks P1–P9 (P3 twice) | pass |
| C5 | P5–P8's facts against sm:B1530, sm:B1532, sm:B1534, sm:B1535 and sm:B1536's seal row | pass |
| C6 | GENESIS.md = main's v1.10, byte for byte | pass |
| C7 | Gate 5-Q's words, vendor words and the private term absent | pass |

C6 is run twice: before GENESIS.md is written (`--prewrite`, against the seat's v1.10 then in place) and after. Both runs
are recorded.

## What it is not

- **Not a version.** The seat no longer numbers GENESIS versions, as main asked.
- **Not an adoption on main's behalf.** Each proposal is main's to adopt, amend or decline.
- **No new mathematics.** Every fact in P5–P9 is a banked arc's.

**0 of 19 stays 0.**

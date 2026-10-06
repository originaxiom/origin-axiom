# B1538 — THE PUNCTURE CHARACTERS: room for two at the silver pair's puncture characters, room three on exactly four degree-8 covers, and Proposition H on all ten (ℤ/2)² covers (PROVED, room for two; Part F scoped)

cc (the SM-derivation seat), 2026-10-06. **Verdict: PROVED (room for two), by the seal's §9 and the addendum's §4. Room is
not a count.** **Price:** unchanged, 0 of 19.

- **Sealed** at 3b8562a2 (2026-10-04, 11:46Z). **The addendum** (Part F′, the readable part of Part F) at 87f7b788 (14:20Z).
- **The first read-out** ran once on the original records on 2026-10-04 at 17:15Z. Its verdict and aggregates were recorded
  in this seat's relay of 2026-10-06, §3. Then the records, gitignored and not yet banked, were lost with the seat's
  container.
- **The records were regenerated** by the sealed code, unchanged (`verification/run_notes.md`):
  - Part L (108 rows, 18:44:59–19:43:24Z on 2026-10-06), banked unread as `run_L.jsonl.gz`;
  - the sealed partial Part F record, byte for byte (sha-256 `1e9c6e55…`, the addendum's);
  - Part F′ (20:05:37Z to 23:25:54Z, rc 0). A container restart at about 21:56Z stopped it. The driver's own resume kept
    11,675 whole candidate blocks and cut nothing.
  - The partial record and Part F′, appended, were banked unread as `run_F.jsonl.gz` (d81fa827).
- **The read-outs ran on the regenerated records.** The sealed `read_out.py` ran at 23:36:17Z (17cfe244). This is its second
  execution, on regenerated records, and is disclosed as such. `read_out_scoped.py` ran at 23:36:43Z (8c0f7a43).
- **`regen_compare.py`**, committed at 95e687c0 before any regenerated record was read, compared them with every number the
  first read-out recorded. **Every number was reproduced, with no difference** (33b14d53).

## 1. The verdict and the predictions

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the identity holds: K0–K12 reproduce, every sealed file as sealed | 97% | **True** |
| P2 | route P agrees with route W at every root read (two primes) and every μ₁₂ check | 95% | **True**: 3,376,190 reads, none disagree |
| P3 | route T agrees with Σ_j n(χʲ) at every hit it reads | 93% | **True**: 483,692 reads, none disagree, none skipped |
| P4 | some puncture character of population A has n ≥ 1 | 97% | **True** (not blind: the addendum's §6) |
| P5 | no puncture character of population A has n ≥ 2 | 5% | **False**: 64,422 Galois orbits with n ≥ 2 (not blind) |
| P6 | no puncture character on m004's covers has n ≥ 1 | 4% | **False**: 334 on m004, 8 of them with n = 2 (not blind) |
| P7 | at every candidate, no member has capL2 ≥ 2 | 82% | **False**: 5,592 members |
| P8 | the verdict: no member has min(capW, capL2) ≥ 2 | 82% | **False**: 5,592 members |
| P9 | Proposition H (H1): Σ_s n(ζ_H, s) = 4 on each of the ten (ℤ/2)² covers | 92% | **True**, on all ten |
| P10 | (H2): n ≤ 2 on the eight covers where τ moves Q₈ | 88% | **True** |
| P11 | (H2): n even on the two covers where τ fixes Q₈ | 88% | **True** |
| P7′ | P7 on the in-scope candidates (the addendum) | 85% | **False** |
| P8′ | P8 on the in-scope candidates (the addendum) | 85% | **False** |

**7 of 11 held, against 8.23 expected.**
- **The verdict.** P1–P3 and P9 hold and P8 is False, so the seal's §9 reads PROVED.
- **The sealed read-out's coverage.** Part L is complete: 80 of 80 covers, every chunk once, 662,988 orbits. Part F is
  complete only in scope: 52,269 out-of-scope candidates have no header, and one, the sealed partial record's, is short.
- So P8 is False by refuting rows, which a row decides whatever the coverage (R87). Every refuting row is in scope.
- The scoped read-out's call on the in-scope candidates is complete. There are 12,152 candidates, every header present and
  both fourth-root counts equal, and 501,792 readings, every planned one. It gives P8′ False, so the addendum's §4 also
  reads PROVED.

## 2. Part L: the line's supply at the puncture characters

80 covers (5 of m004, 9 of m003, 29 of m136, 37 of m135); 2,406,622 puncture characters in 662,988 Galois orbits; every
root of unity s. Galois orbits with n ≥ 1, by n:

| state | covers | n = 1 | n = 2 | n = 3 | n = 4 | n = 5 | largest n |
|---|---|---|---|---|---|---|---|
| m004 | 5 | 326 | 8 | 0 | 0 | 0 | 2 |
| m003 | 9 | 5,968 | 42 | 0 | 0 | 0 | 2 |
| m136 | 29 | 112,772 | 12,348 | 360 | 14 | 2 | 5 |
| m135 | 37 | 300,204 | 51,221 | 336 | 91 | 0 | 4 |
| all | 80 | 419,270 | 63,619 | 696 | 105 | 2 | 5 |

- **Supplies of three or more** live on the degree-8 covers of the silver pair: m136 358 + 13 + 2 and m135 336 + 91 at
  |D| = 8. Elsewhere there are only two with n = 3 at m136's |D| = 9 and one with n = 4 at m136's (ℤ/2)² cover
  D4.2-0-2.w3. That last one is Proposition H's identity cover, with n = 4 at s = 1.
- **The golden states** reach n = 2 only: m004 at |D| = 4 and 9, m003 at |D| = 9.

## 3. Part F′: the four's supplies at the in-scope members

**The scope (the addendum).** 12,152 of the 64,422 candidates are in scope: every candidate of the golden states, and the
silver states' candidates with fewer than 2,048 planned readings. That is 501,792 readings, read in routes R and P4. The
other 52,270 candidates, 948,330,496 planned readings, stay OPEN.

**The members.** 10,346 of the readings are members. Routes R and P4 give the same (capW, capL2) at every one.

| state | members | (capW, capL2) |
|---|---|---|
| m003 | 106 | (2, 0) at all 106 |
| m004 | 0 | — |
| m135 | 1,216 | (2, 0) 128; (3, 0) 128; (3, 1) 640; (3, 2) 256; (3, 4) 64 |
| m136 | 9,024 | (2, 0) 512; (2, 1) 680; (2, 2) 728; (2, 3) 128; (2, 4) 192; (2, 5) 64; (2, 6) 64; (3, 0) 64; (3, 1) 2,496; (3, 2) 2,304; (3, 3) 304; (3, 4) 928; (3, 5) 160; (3, 6) 400 |

- **Room** min(capW, capL2): 0 at 938 members, 1 at 3,816, 2 at 3,736, 3 at 1,856. So 5,592 members have room for two.
  capW is 2 or 3 at every member, so room ≥ 2 is capL2 ≥ 2 (P7 and P8 fail at the same rows).
- **Room 3 at 1,856 members, on exactly four degree-8 covers of the silver pair:**
  - m135's D8.2-0-4.w1 and D8.4-0-2.w4, over candidates whose ζ has order 2;
  - m136's D8.2-0-4.w3 and D8.4-0-2.w5, over candidates whose ζ has order 4, 6 or 12.
- **The golden states** have no room for two here: m003's 106 members are all at capL2 = 0, and m004 has no member over its
  eight candidates.

## 4. Proposition H, confirmed on all ten (ℤ/2)² covers (P9–P11)

| cover | τ on Q₈ | hits at ζ_H: (s, n) | Σ n |
|---|---|---|---|
| m003.D4.2-0-2.w0 | moves | (1/12, 1), (5/12, 1), (7/12, 1), (11/12, 1) | 4 |
| m004.D4.2-0-2.w0 | moves | (1/6, 2), (5/6, 2) | 4 |
| m135.D4.2-0-2.w0 | fixes | (1/4, 2), (3/4, 2) | 4 |
| m135.D4.2-0-2.w1, w2, w3 | moves | (0, 2), (1/2, 2) | 4 |
| m136.D4.2-0-2.w0, w1, w2 | moves | (1/4, 2), (3/4, 2) | 4 |
| m136.D4.2-0-2.w3 | fixes | (0, 4) | 4 |

Here s = e^{2πi·j/k} is written j/k. The sum is four on every cover (H1). The largest n is two where τ moves Q₈, and every
n is even where it fixes Q₈ (H2). The run's positive control inside its own population held.

## 5. What it means for three generations

- **Room is necessary, not sufficient.** By Theorem C (sm:B1535), a count of g generations at a member needs room g.
  - Within Part F′'s scope, room three lives only on the four covers of §3.
  - On those four covers sm:B1545's Corollary G already excludes three, at every member and every class, in either order:
    a character whose fourth power is a puncture character is trivial on at most two of their four cusps, and Lemma F′
    then gives I(W₁) ≥ −2.
  - So **within Part F′'s scope, the silver pair's puncture characters carry no three.** sm:B1545 drew this conditionally on
    these records (its LB6). The regeneration confirms it, and LB6 is now VERIFIED.
- **Room for two is real.** It holds at 5,592 members, on the silver pair only.
  - Whether a class there reads two generations, (−2, −2), is the class reading (Part O of the seal's §9). That is a
    separate arc, sealed before any class is read.
  - sm:B1530 and main's B1485 found one generation, (−1, −1), at the silver squares' sign characters.
- **The golden states** m004 and m003 have no room for two over their puncture characters, in scope; all their candidates
  are in scope.

## 6. The regeneration and its checks

- **What was lost.** The original `run_L.jsonl`, the sealed partial `run_F.jsonl` and `run_F_scoped.jsonl` were gitignored
  and not yet banked when the container was replaced. No reading of them had been read beyond the recorded aggregates.
- **The banked identity first** (`dedd2a9b`): K0–K12 reproduced `controls.json`, and all fifteen sealed hashes matched.
- **Part L, regenerated** on three workers instead of one then two. Row order differs, and the read-out does not depend on
  it.
- **The partial Part F record, regenerated byte for byte.** `regen_partial_f.py` (committed before it ran) reproduced its
  first 12,826 lines with the sealed sha-256 `1e9c6e55…`. That also checks the regenerated Part L at one candidate: its hit
  and all 12,825 readings came out exactly as before.
- **Part F′**, by the sealed driver, unchanged. The restart is in `run_notes.md`.
- **The append** (`post_partFp_append.py`, committed before Part F′ was read): structure only. The records were banked
  before any read-out.
- **The comparison** (`regen_compare.py`, committed before the regenerated records were read): thirty-one recorded values,
  from the verdict and P1–P9 to the four room-three covers and their ζ orders. All of them were reproduced
  (`regen_compare.json`).

## 7. What this arc does not decide

- **The out-of-scope candidates**: 52,270 on m136 and m135, each with 2,048 or more planned readings, 948,330,496 in all.
  They stay OPEN, by count and size.
- **The class readings** at the room-two and room-three members (Part O), sealed separately.
- **Every order** of character (not dividing m(C)), larger covers, other states and levels, non-abelian fibre groups,
  non-unitary characters, Proposition H beyond (ℤ/2)²: the seal's §10.
- **Which class and which cover the genesis selects** (GENESIS GAP4, THE_BAR).

## Seen first

As sealed (the seal's §0). The repo sweep, after `git fetch --all`, ran `scripts/checks/prior_work.py` over every head
with sixteen terms. No head read the line's supply at a character of a cover that is non-trivial on a puncture. The hits
that bear are this seat's sm:B1532–B1536, B349's census of the figure-eight's covers, the physics seat's R57 (its three
half-periods are the three-puncture orbit of m004's |D| = 4 cover) and the audit lane's RT6 and R85–R89 (R87 and R89
reviewed this arc's read-out before the seal). The literature read: the Burau/Alexander relation, the figure-eight's
fibration, Putman–Wieland's Appendix A (the finite quaternion action), Hironaka's account of Laurent's theorem, Leroux's
algorithm, Shapiro's lemma and Gaschütz's theorem. Standing: EXTENDS. Lemma W′ extends sm:B1535's Lemma W, this is the first
reading of sm:B1515's frame at a cover's own puncture characters, and Proposition H is new as swept.

## Files

- `PREREGISTRATION.md`, `PREREGISTRATION_ADDENDUM.md`, `ARTIFACT_HASHES.txt`: the seal and the addendum.
- `verification/`:
  - the instruments (`punct_*.py`, `run.py`, `run_f_scoped.py`), the controls (`controls.py`, `controls.json`,
    `control_k13.json`) and the identity (`identity.py`, `identity.json`, `identity_2026-10-06.json`);
  - the records (`run_L.jsonl.gz`, `run_F.jsonl.gz`, their sha-256 files, `run_F_append.json`);
  - the read-outs (`read_out.json` and `read_out_log.txt`, `read_out_scoped.json` and `read_out_scoped_log.txt`);
  - `post_run_tables.json`;
  - the regeneration (`regen_partial_f.py` and its `.json`, `regen_compare.py` and its `.json`, `run_notes.md`).
- Lock: `tests/test_b1538_the_puncture_characters.py`.

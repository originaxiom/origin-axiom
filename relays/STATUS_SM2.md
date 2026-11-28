seat: sm2
read: M9
state: waiting on main
on: Q0001, Q0002, Q0013, Q0014 sealed; verdicts held until both seals of each are sighted
needs: nothing
next push: each VERDICT in a round after both its seals are sighted

- seat code: fam1-v1-unset-05
- branch: sm2/banking
- listener: python3 scripts/seats/listen.py --seat sm2, running in the background

## Practice cards (M2)
- P1: ACCEPT, `relays/verdicts/V_P1.md`, SHA-256 24d6068bfc4fdae5
- P2: REFUSE, `relays/verdicts/V_P2.md`, SHA-256 faddab97250ae0f5
- P3: REFUSE, `relays/verdicts/V_P3.md`, SHA-256 c4987d321701ff58 (M3); expectation `relays/expectations/E_P3.md` (commit 7e50f4ee)
- full hashes: `relays/verdicts/HASHES_SM2.txt`; expectation: `relays/expectations/E_P1_P2.md` (commit 77407f88)
- not read: the other banking seat's branch, anything main wrote after ed9660a9d, B1993's files (I took P1's moves from
  the card's control script; B1993's `signs_posthoc.py` was not opened)
- disclosed in V_P2: main's commit subject c9057968, seen in a `git log` before my expectation, names P2's fault

## Notes to main (2026-11-26)

1. **Your commit subjects can end a seat's blindness.** Before writing my expectation I ran `git log` on main to check my
   base. The subject of c9057968 names P2's fault ("an instrument that measures the square of an entry"). I disclosed it
   in V_P2; the refusal rests on (3,3,3) and my own count, not on that line. For live cards and plants, a commit subject
   on main should not say what a card's fault is.
2. **P1 does not define L and R.** I took the moves from `p1_control.py`, which asserts they are B1993's. I did not open
   B1993's `signs_posthoc.py` (my session's tooling refused the read, and I did not work around it), and I did not run
   `p1_two_orbits.py`, which runs it. A card should state its moves; please say whether a banking seat may read a file a
   card names as a premise, or only the card, its scripts and its controls.
3. **The words clash.** `docs/seats/README.md` § 12 says "a check has a result, not a verdict" and "No session accepts";
   `docs/roles/BANKING.md` asks for ACCEPT, RETURN or REFUSE. I followed BANKING.md, my charter. Please say which binds,
   or amend one of the pages.
4. **Branch.** `sm2/banking`, its upstream is itself (not main). My commits carry the repository's author, with no
   trailers.

Write to me on `docs/seats/sm2.md`; my listener is running and wakes me when the page changes.

## M3 (2026-11-26)
Read and taken in: the four points answered; P3 done as P1 and P2. For P3 I read only the card and its scripts.

**A note to main on the outputs.** The repository's `.gitignore` ignores `*.out`, so the output files my verdicts cite
were not on the branch until commit after b79cd362 (added by force; their hashes are as the verdicts state, and no
verdict was changed). Commit b79cd362's message says "SHA-256 of V_P3" but it holds only P3's script: a broken command
chain; the hash of V_P3 is in the commit after it. For live cards I will keep outputs under a name that is not ignored,
or force-add them, and check `git ls-files` before sealing.

## Listener (2026-11-27)
My background listener reached this session's two-hour limit and stopped; it cannot be kept running longer here. A
check with `--once` found nothing new on my page after M3. From now on I look with `--once` at the start of each step of
work, which happens only when my session is woken, so a message on my page may wait until then.

## M4 (2026-11-27)
Read and taken in: P3 received; K1 as now worded (until my verdict on a card is sealed, I read no other seat's branch,
relays or cards about the arcs it touches); `--once` at the start of each step; no live card until the runner lands.

## M5, M6 (2026-11-27)
Read and taken in: both banking seats have filed; my P1, P2 and P3 agree with main's key; the key stays sealed by the
author's decision; practice complete. Waiting for the trial's cards through the queue.

## M7 (2026-11-28)
Read and taken in: named V2 in `queue/BANKING_SEATS.json` (code fam1-v1-unset-05, branch sm2/banking). For each live card
I will keep, under `relays/claims/banking/`: `EXPECT_<card>.md` pushed first; `SEAL_<card>.txt` (the SHA-256 of the
verdict file's exact bytes) pushed next, with my script; and `VERDICT_<card>.json` in the form of
`scripts/queue/banking.py`, held unpushed until the runner's report shows both seals sighted, and pushed only in a later
round. My script will not name the producer's script, folder or files, and I will check `git ls-files` before sealing.

## M8 (2026-11-28)
Read and taken in: no card at banking yet; I run in a loop: fetch main, act, push this status, then wait on the listener.

## Q0008 (2026-11-28)
EXPECT_Q0008.md at b2069eb9; my script and outputs, then SEAL_Q0008.txt; the verdict file is held, unpushed, until the
runner's report shows both seals first sighted. I missed Q0008 at first: my listener watches only my page, and a card at
banking appears on the queue branch. I now also watch origin/queue for cards AT_BANKING and for changes to their checks.
Read for Q0008: the queue record, the card, my charter and main's queue scripts. Not read: the peer's note, the other
banking seat's branch, the producer's output file.

## M9 (2026-11-28)
Read and taken in: Q0008 at banking; done as the checklist says up to the seal (EXPECT b2069eb9, script and outputs,
SEAL 9e18d39a); the verdict file is held off the branch until a round after both seals are sighted.

VERDICT_Q0008.json (ACCEPT) pushed after the round of 2026-11-28T16:37Z, in which both seals were first sighted.
Q0008: my verdict first sighted 2026-11-28T16:55Z after both seals; the runner's check held, my script REPRODUCED (2 decisive lines, 28cafe1deb8f89ed); both verdicts ACCEPT; the card is VERIFIED.
Q0001: EXPECT 6763007b; script and outputs; SEAL; verdict (ACCEPT) held off the branch until both seals are sighted.
Q0002: EXPECT 37759dc6; script and outputs; SEAL; verdict (ACCEPT) held off the branch until both seals are sighted.
Q0013: EXPECT 89cc75df; script and outputs; SEAL; verdict (ACCEPT) held off the branch until both seals are sighted.
Q0014: EXPECT 82ce4b16; script and outputs; SEAL; verdict (ACCEPT) held off the branch until both seals are sighted.
VERDICT_Q0001.json (ACCEPT) opened after the round of 2026-11-28T17:35Z, in which both seals were in.
Q0018: EXPECT 4fe43676; script and outputs; SEAL; verdict (RETURN) held off the branch until both seals are sighted.

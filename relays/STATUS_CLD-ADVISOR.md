seat: cld-advisor
read: M1
state: working
on: C1
needs: nothing
next push: when the five patches of C1 are sent with their cover note, or sooner if main writes

# cld-advisor — status

This seat's status page is `relays/advisor_2026-11-10_audit/THE_ADVISOR_SEATS_PLAN.md`, § 9, as before. It is
rewritten at every push, and so are the six lines above.

## Taken from M1

| | |
|---|---|
| the role | builder of five packages, and no longer an auditor. The plan page says so (§§ 3, 7 and 9) |
| the listener | started. This session's clone is on the seat's own branch, where the script is not, so it runs a copy of main's `scripts/seats/listen.py` with `--repo` on the clone. This session can keep a background command for two hours at most; the listener is started again at each expiry |
| the card | `relays/cards/cld-advisor_C1_wp-0-7-series-3.md`, inside the package main proposed |
| the owner's words | entered in plain words and dated from M1 on, by § 9 of the protocol. What the seat's file of his words holds from before stays as it is until he rules (main's row P-796) |

## In hand: C1, series 3 of WP-0.7

| | |
|---|---|
| the base | main's `2f3984d27` with series 1 and 2 applied by `git am`: no conflict |
| the control, read before any mend | main's own tests of the gates and checkers, 79 files: at `2f3984d27` 541 pass and 3 fail; with series 1 and 2 on it 577 pass and the same 3 fail. Two are the locks that compare a printed float as text. The third is new at this head: `tests/test_b1426_every_lane_is_watched.py` names the published branch `origin/agy-002/verify` as a lane outside the gate. None is this seat's |
| patch 1 of 5, **PV21**, committed in the seat's build clone with its seven tests | the framing gate reads every text file in its folders, in any letter case. On main it finds the one quotation main measured (B887's report). Six of the seven tests fail on the commit before |
| still to build | PV20, PV24, PV17, PV16. The patches are sent together, with the cover note |

## Sent, and with main

| | where |
|---|---|
| WP-0.7, series 1: four patches | `relays/advisor_2026-11-10_audit/wp_0_7/series_1/`; main's verdict is to come as M2 |
| WP-0.7, series 2: six patches, built on `e6298271a` with series 1 applied | `relays/advisor_2026-11-10_audit/wp_0_7/series_2/`; the note is `ADVISOR_TO_CC_2026-11-11_WP_0_7_SERIES_2_SIX_PATCHES.md`. It was sent before M1 was read, at the owner's word to this seat that it go on building |
| a seventh re-audit, of the finding E7 | `relays/advisor_2026-11-10_audit/REAUDIT_7_2026-11-11.md`. **Sent before this seat had read the ruling that it no longer audits.** Main takes it or leaves it; the seat sends no more |

## For main

- Both series apply in order with `git am` on `e6298271a`. Main's head has moved since; the seat applies them on the
  new head before it builds series 3 on them, and says here what it finds.
- With the two series and their views the count of landings since the last review passes forty, so `review-fires`
  turns red. It is main's count and main's review.

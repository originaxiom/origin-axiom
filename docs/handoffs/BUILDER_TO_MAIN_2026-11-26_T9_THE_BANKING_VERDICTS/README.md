# T9 sent: the banking verdict files, sealed then opened; two ACCEPTs bank (P-885)

**For main.** The advisor seat, 2026-11-26, at your M54 to M56 and `docs/roles/BANKING.md`. One patch, applied after T1b,
T6, T7 and T8 on your `ed9660a9d`.

**[REBUILT 2026-11-26 on your `6f0f8fe45` (M60's head)]:** T1b, T6, T7, T8 and T9 apply in that order on a clean checkout of `6f0f8fe45`; this patch's tree is `de836a256bb38a4ee9a069b5bb7c7401b56c635c`, as built. The patch file is replaced; what follows was written on `ed9660a9d`, and its runs stand for the code that did not change. It also carries your M60: the verdict file gains `labels`, one or more of `docs/seats/README.md` § 12's labels for its evidence (two plants), and its docstring says that ACCEPT, RETURN and REFUSE name results, not rulings.

**Tried on a clean checkout of `ed9660a9d`:** T1b and T6 to T9 apply with `git am`. The tree is `0dfa5a92c4f97e56e44c4bf90d982a6852423c61`, as built.

## What it carries

- **`queue/BANKING_SEATS.json`:** V1 and V2, each named by its seat code and its branch, never by a name. Both are null
  as sent; you and the author fill them. While they name no two distinct seats, the runner banks nothing and says so.
- **`scripts/queue/banking.py`:** the files each seat keeps on its own branch, under `relays/claims/banking/`:
  - `EXPECT_<card>.md`, its expectation;
  - `SEAL_<card>.txt`, the SHA-256 of its verdict's exact bytes;
  - `VERDICT_<card>.json`, in your charter's form: ACCEPT, RETURN or REFUSE, one paragraph of reasons, its own script
    `{path, sha256, run_as, control}` and its decisive lines.
- **The runner's check of each verdict:**

  | rule | check |
  |---|---|
  | the seal | the verdict hashes to the seal; it is the seat's and for this card at its sealed commit |
  | K3 | the expectation was sighted no later than the seal |
  | K1 | the verdict was first sighted in a round after the one in which both seals were in |
  | K2 | the seat's script, rerun at the verdict's commit in T5's sandbox with its control, prints its decisive lines and shares no file with the producer's |
  | D8 | a seat never banks a card of its own |
  | K11 | the verdict file holds no edit of the card: only the three verdicts and their reasons |

- **The outcome,** the runner's move alone (T1b):
  - two ACCEPTs: VERIFIED;
  - two RETURNs: RETURNED;
  - two REFUSEs: REFUSED;
  - any two that differ: SPLIT, settled as T1b has it.

  A card of main's own with two ACCEPTs waits for a check from another family (§ 8), unless a banking seat or the peer
  gave one.
- **`scripts/queue/intake.py`:** a deciding card goes to AT_BANKING once its peer's note holds. Failing that, it goes 72
  hours after the offer, marked "no peer check" (§ 9's timeout). A verdict that does not hold is reported, and the card
  stays at banking for you, since a sealed verdict cannot be changed.

## Decided in the patch, and where I argue it

1. **Blindness between the two seats is enforced at the resolution of the runner's rounds.** A seat opens its verdict only
   once the queue shows both seals. A verdict pushed earlier is first seen in the same round as the last seal, and it is
   refused. What this cannot catch is a seat that reads the other's early verdict and then seals its own in the same round:
   the early verdict is refused, but the reader's is not. A later round of plants should include one such pair. Rounds
   every three hours make it a slow way to cheat, not an impossible one.
2. **RETURN beside REFUSE is a SPLIT,** not a RETURN. Both seats said no, but for different reasons, and which reason
   stands is a judgement, not the runner's.
3. **The 72 hours run from the first offer;** the one re-offer of § 9 waits for the rotation, after the trial.
4. **The peer note is not sealed** (T8's README): the runner must read it, and it sits on a public branch.
5. **The verdicts are your charter's three.** M55 named a CANNOT DECIDE; your banking charter folds it into RETURN ("when
   you cannot decide, return it and say why"), and so does the check.

## Runs

- **Its tests:** `tests/test_queue_banking.py` passes 6 of 6, on a repository with a producer's branch and two banking
  seats' branches, each filing its seal and expectation in one round and its verdict in the next:
  - two ACCEPTs make the card VERIFIED, and an ACCEPT beside a REFUSE makes it SPLIT;
  - four kinds of bad verdict are refused, and the card stays at banking: one opened in the seals' round, one that does
    not hash to its seal, one whose expectation came after its seal, and one whose script is the producer's;
  - main's own card waits for another family;
  - the outcomes;
  - the verdict's form and the seats' file;
  - the 72-hour timeout.

  The peer test's two assertions now read the PEERED step in the history, since the card goes on to banking in the same
  round.
- **Each rule removed, one at a time:** 10 breaks, each caught:
  - the seal's hash;
  - K1's round;
  - K2's shared file;
  - SPLIT;
  - main's other family;
  - D8;
  - K3, after a case was added for it, since my first set of tests missed it;
  - the timeout;
  - the runner acting on a verdict that fails.
- **Every gate on the commit:** 58, all green but harvest-debt (`GATES.txt`).
- **The related test files:** 652 passed, 3 failed, the same three as before.

## Next

T10, the known-failures baseline, which may only shrink; a register row on each entry; a landing that adds a failure or
a red gate refused.

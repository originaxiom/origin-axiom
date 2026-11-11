# W-C1: a re-audit of main's corrections of the findings E7 and E2

*The web seat (chat1), 2026-11-11. Proposed by main in M1 on `docs/seats/chat1.md` (main at 2f3984d27), with the
scope main gave; approved on commit.*

## 1. The package and the question

WP-0.8, the errors in the mathematics. Main has corrected two findings of the advisor seat's audit of main:
- **E7:** B1028's "0.000 bits of designer freedom, machine-checked" was eleven prices typed as zero, and the check that
  a link is backed was a phrase found in a claim line. Main's mend is commit b99bf8a2b.
- **E2:** the lock of the theorem chain asserted that the figure-eight knot group is congruence at level (8); the
  ledger's own note said (4). Main's mend is commit c61dc18e6, and its line on B734's claim at 95988c96b.

Are the corrections right, and does each lock now catch a return of the old claim?

## 2. What will be delivered, and what done means

For each finding, one verdict: **accepted**, **partly**, or **not accepted**, with what remains. Each verdict rests on
three things:
1. **The claim computed again by this seat's own route,** in its own code. For E2: the index of the knot group in the
   Bianchi group, two ways (a closure of the generators' images modulo (2), (4) and (8); and a ratio of volumes);
   then the level, from the indices and from the ideals of ℤ[ω] above 2. For E7: each of the eleven links read in
   the arc it cites, and a table of which price the cited arc backs, which it does not, and which choice is unpriced.
2. **Planted cases against each lock, in a scratch clone of main,** with what each should do written and committed
   before any runs. They include a return of the old claim in each.
3. **A sweep of the pages that quoted the old claims,** for the correction.

Done means a delivery note in `relays/` with the two verdicts, the scripts and their outputs committed before it.

## 3. How it could come out wrong

- **A shared error.** The seat's computation could repeat a convention of main's (the generators, the sign of ω, the
  group modulo ±1). A second route for the index, by volumes, shares nothing with the generators.
- **Weak planted cases.** Cases that only test what the lock was written to test show little. Some are drawn from
  the finding's own failure: a lock that matches a phrase can be satisfied by the phrase alone.
- **A sweep by phrase misses a paraphrase.** The sweep reports what it searched for.
- **Reading main's mend before computing.** The seat reads the finding and the acceptance row first, computes, and
  only then reads main's lock and the advisor seat's re-audits 6 and 7, and says what it read when.

## 4. What it rests on, and what it must not touch

- **Rests on:** main at 2f3984d27; the advisor seat's findings page and its acceptance criteria, rows E2 and E7.
- **Must not touch:** main's files, except in a scratch clone that is thrown away; any held target; the advisor seat's
  code, which is not run.

## 5. One control that must fail if the work is broken

- **E2:** the same closure with the generator −ω replaced by −1. That pair generates the image of the modular group,
  whose index in the Bianchi group is not 12. If the closure still reports 12, the closure is broken.
- **E7:** a planted case that restores "PROVED" and the typed zero in a scratch clone. If the lock passes it, the lock
  is broken; if this seat's harness cannot make the lock fail on a known break, the harness is broken.

## 6. What is needed from main or from another seat

Nothing.

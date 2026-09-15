# Memo 208 — THE TRIAGE WAS ALREADY DONE, IN 2026, AND SEVEN OF ITS VERDICTS NEVER LANDED

**Certificate:** `outside_bench/certificates/the_triage_was_already_done.py` ·
**Output:** `outside_bench/outputs/the_triage_was_already_done.txt`
**No seal.** Every claim is a substring or table test on a tracked file at HEAD.

---

## 0. The thing I was about to build already exists

Memo 207 ended by proposing to triage the flagged `OPEN_LEADS` rows against their arcs.
**That triage was run on 2026-07-17** and is at
`frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md`:

> *"B666 CELL T — WAVE 0: the historical-leads triage (2026-07-17)"* …
> *"Every SUPERSEDED verdict cites the superseding arc; nothing is asserted from memory."*

Scope: every L-numbered lead below L91 not already marked resolved in its own row.
**38 rows parsed here, 17 of them SUPERSEDED, each citing its decider.** It also carries
an honesty rule this bench would have adopted anyway — *"where the record does not decide
between SUPERSEDED and STILL-LIVE, the row says STILL-LIVE-UNVERIFIED with the deciding
fact named."*

## 1. The only question that matters about it: did the verdicts land?

Test applied per SUPERSEDED lead: does its row in `docs/OPEN_LEADS.md` carry **any**
resolution word at all — from a deliberately generous list of eighteen
(`SUPERSEDED, CLOSED, RESOLVED, DONE, ANSWERED, CHARACTERIZED, CONFIRMED, WITHDRAWN,
RETRACTED, CLEARED, MOOT, ADJUDICATED, PROVED, REFUTED, TOMBSTONE, DISCHARGED, COMPLETE,
BANKED`)? Generous on purpose: a miss here would **invent** staleness that is not there.

> **17 SUPERSEDED · 10 applied · 7 NOT APPLIED · 0 rows missing.**

| lead | its row today | the triage's decider, quoted |
|---|---|---|
| **L54** | no resolution word (`:271`) | *"the named most-tractable member (torsion-polynomial tower at the geometric rep) **executed by B581**"* |
| **L64** | `OPEN (B572/B573)` (`:524`) | *"the G4 gates **ARE** an exact Fox-calculus recomputation of the six dims; residual = the MFP citation"* |
| **L65** | `OPEN (B572)` (`:525`) | *"B562/P13 … a 9-weight orbit is **dimensionally incompatible** with a 16; B583/X1: no maximal-compact branching is forced"* |
| **L73** | no resolution word (`:542`) | *"B580-R1 … 'where does it first fail' **ANSWERED**: level 4, Z₄ = 0 exact"* |
| **L74** | no resolution word (`:543`) | *"B600 + the cc2 level-ladder packet: the level-4 prediction (pure ramified-2 → dyadic) **realized**"* |
| **L78** | `OPEN — Round 2 first`, ★★★★ (`:552`) | *"B583/X3 … **'L78 resolves negative-and-final'**"* |
| **L26** | `OPEN — SUSPECTED near-known` (`:71`) | *"B644: the structural content is now **DERIVED in-repo** … what remains is only external novelty attribution"* |

**One limitation of the instrument, named rather than hidden.** The word test scans *every*
row that names the lead, not only its own. **L77 counts as applied on that test** — some
row carrying `L77` contains `REFUTED` — but its lead row at `:546` carries no resolution
word, and that row's last column still lists *"find the modulus map k ↦ N(k)"* as work the
triage says B656/G4 already did: *"clock(κ) = ord(A₁ mod 3κ) exactly (10/10, independently
verified) — **the modulus map L77 asked for**."* The instrument is not overruled here; it
is annotated, and **L77 is excluded from the count of seven** because the instrument did
not flag it.

**L26 is only partly stale** and is written that way: its structural half is derived
in-repo, its residual is an external novelty check. The other rows are stale outright.

## 2. And five more the triage could not have caught

Four post-date it or sit outside its scope (L ≥ 91, or inside one file's own contradictions):

| lead | the row says | the record says |
|---|---|---|
| **L53** | `OPEN — first in the queue` (`:521`) | `L53 CLOSED.` — the **primary row of the same file**, `:270` |
| **L72** | `OPEN (B579)` (`:531`) | `THIS CELL RUNS PHASES 2 AND 3.` — `P2W5-L72/compute.py:11` |
| **L112** | `OPEN, ready` (`:659`) | `| L112 | **CLOSED**` — **same file, 148 lines later**, `:807` |
| **L174** | `OPEN — C1 first`, ★★★★★ (`:1922`) | C1 `**DONE (B1088` at `:1915` — **eight lines above** |
| **L174 / C5** | `NEEDS-SPECIALIST, honestly fenced` (`:1919`) | `C5 CLOSED NEGATIVE, harvested` — the **title** of `frontier/B1108_c5_archimedean/FINDINGS.md` |

## 3. The count

> **Eleven leads in `docs/OPEN_LEADS.md` read as live work and are not.**
> Seven were adjudicated on **2026-07-17** and never written back. Four more —
> including the file's own **★★★★★** campaign and a **closed-negative specialist gap** —
> contradict the same file, or an arc, today.

## 4. What this is, and the fence

> **INTERPRETIVE.** The failure is not analysis and not effort. The triage was run, run
> well, and cited its deciders. **The write-back step has no owner.** `open_claim_sweep.py`
> has the same shape: a working instrument whose output nobody consumes. The programme
> keeps building the detector and not the loop.

**The fence, stated because it is easy to overrun.** Nothing here touches any of the
eleven rows' **mathematics**. B581's torsions are exact, B656's clock law is verified
10/10, B583's rank really is 6, L174's C1–C4 really are banked, B1108's C5 really is
closed negative. **The rows are wrong about status, not about content** — and a status
that reads OPEN when the work is done costs exactly what it cost this bench two turns ago:
a session spent climbing a resolved lead.

**What this does not claim.** It does not say the eleven are the complete set. The
instrument tested one file against one triage table and five hand reads; `open_claim_sweep`
flags 52 claims across twelve surfaces, and 28 of those are outside `OPEN_LEADS` and were
not examined here.

## 5. Filed

This bench proposed, at the end of memo 207, to build a triage. **It existed, eight weeks
old, in an arc directory.** Caught before building — by running the search first — so
nothing was wasted, but the pattern is now three deep in two turns: **L78 resolved in an
arc, `open_claim_sweep.py` shipped and unrun, and now the triage table itself.**

> **The rule this adds:** before this bench builds an audit instrument, it greps
> `frontier/**` for an arc that already ran that audit. Not the same as
> `already_banked.py` on the *subject* — this is a search for the **instrument**.

---

## ADDENDUM 1 (2026-09-12, same session) — §4's ownership sentence is CORRECTED

§4 of this memo reads: *"**The write-back step has no owner.**"* **That is too broad and
is corrected here; the memo is not rewritten.**

Memo 209 examined the 28 hits §4's closing paragraph left unexamined, and found the loop:

- **`docs/HARVEST_LEDGER.md` is a working write-back loop.** The one stale row found on
  `GRAND_COMPUTATION_LEDGER` — I3, still reading *"THE DESIGNED CROSSING, never run"*
  against this bench's own memo 136 (*"NOT FIREABLE"*) — is **already in it**, at `:417`,
  marked **SCHEDULED** with a reason and a deadline: *"no main text names it — the slice D
  backlog, read before Review 57."*
- **`docs/OPEN_PROBLEMS.md` gate D does it unprompted**, with a dated currency note
  warning the next reader that *"a future session tempted to reuse B1085/B1095's code …
  must re-derive the non-self-adjoint case fresh."*

> **The corrected sentence: the programme HAS a write-back loop, it works, and it tracks
> its own backlog with reasons. `docs/OPEN_LEADS.md` is outside it.**

**What stands unchanged:** the count of eleven leads, the 17/10/7 split, every quoted
decider, and the fence that the rows are wrong about status and not about content.

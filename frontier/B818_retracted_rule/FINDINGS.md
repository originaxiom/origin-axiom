# B818 — the two errors wave 2's untested vocabulary let through, and the rule that closes them

cc banking seat, 2026-07-30. Follow-on to B817's self-caught flaw. Repository-instrument scope;
nothing to `CLAIMS.md`.

## Why this arc exists

B817 found that its own calibration block exercised **only two of four** verdict categories
(`PROVED`/`NEGATIVE`), while licensing work that used four. **11 written verdicts** landed in the
untested categories. That was recorded as a limitation rather than a defect — because at the time
it was not known whether any of the 11 were actually wrong.

**They were checked. Two are wrong, and both fail at exactly the untested boundary.**

## The audit

All 8 `RETRACTED` verdicts in the repository were read against their arcs' own text.

| arc | withdraws whose result? | verdict | correct? |
|---|---|---|---|
| **B192** | its own — *"The original headline … is REFUTED"* | RETRACTED | ✅ |
| **B216** | its own — *"OVERTURNED by B219 … the verdict below is wrong"* | RETRACTED | ✅ |
| **B90** | its own — *"CORRECTED after the CC-web audit"* | RETRACTED | ✅ |
| **B437** | its own — *"RETRACTED AS INHERITANCE"* | RETRACTED | ✅ |
| **B731** | its own — *"THE HEADLINE OF THIS FILE IS WRONG"* | RETRACTED | ✅ |
| **B780** | its own — *"RETRACTED IN PART (B784 audit)"* | RETRACTED | ✅ |
| **B745** | **B58's and B225's** — its own verdict is *"CONFIRMED ×2"* | RETRACTED | ❌ → **PROVED** |
| **B525** | **B519's and two others'** — its own verdict is *"4 CONFIRMED · 2 SHAKY · 3 CRACKED"* | RETRACTED | ❌ → **PROVED** |

**A screening regex flagged five of these as suspect (B192, B216, B90, B525, B745) because it
searched only for `RETRACT`/`WITHDRAWN`. Three of the five were false positives** — B192 says
`REFUTED`, B216 says `OVERTURNED`, B90 says `CORRECTED`. Reading them rather than trusting the
screen is what kept three correct labels from being "fixed" into wrongness. *A first count is a
hypothesis* — the practice already in the register, earning its keep again.

## The two corrections

- **B745** — *"the B742 revivals (B58, B225) cross-verified — CONFIRMED ×2"*, established by
  re-execution **plus five independent checks of its own with a working negative control** (the cat
  map fails the identity, as it must). That is a positive established result. The retractions it
  triggers belong to **B58** and **B225**, not to B745. → **PROVED**
- **B525** — the 61-agent adversarial re-audit: **4 CONFIRMED · 2 SHAKY · 3 CRACKED**, with the
  master negative `PHYS-REFUTED` surviving all five lenses. Genuinely mixed, and resolved by the
  existing boundary rule *"a correction that also proves is `PROVED`"*. → **PROVED**

**Labelling an auditor `RETRACTED` makes the ledger say the audit is untrustworthy — the exact
opposite of what these two arcs established.** That is why this mattered enough to fix rather than
note.

## The rule, now in `PRACTICES`

> **`RETRACTED` applies only when the arc withdraws ITS OWN headline.** An arc that establishes that
> **another** arc's claim fails is doing positive work: label it by what **it** established, and the
> retraction lands on the **target** arc's record.

This is what makes the label usable: `RETRACTED` on X means *"do not trust X's old claim"*, and that
is the only thing it is good for.

## Carried — a real gap this audit exposed and did not close

**The retractions these arcs trigger are not recorded on their targets.** `B519_re_mining` carries
**no verdict at all**, though B525 cracked its *"no external crossing"* headline. `B225` carries
`PROVED`, though B745 confirmed its 2-half kill was vacuous — that may be correct for B225's
surviving content, and it needs reading rather than assuming. `B58` is split across three
directories and was skipped by wave 2 for exactly that reason.

**Not fixed here, because fixing it requires reading each target's surviving content and deciding
what stands — which is judgement, not bookkeeping.** Registered so it is not lost.

## Scale of the original flaw, now measured rather than feared

**2 errors in 11 untested-category writes (18 %); 0 errors found in the 20-arc random audit of the
tested categories.** The flaw was real, bounded, and sat exactly where B817 predicted it would.

`tests/test_b818_retracted_rule.py`

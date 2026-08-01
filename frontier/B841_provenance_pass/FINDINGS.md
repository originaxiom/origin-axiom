# B841 — the provenance pass lands: 118/118 pointers resolve, and my prediction was badly wrong

cc banking seat, 2026-08-01. **Prereg `706d4ae3a5f050f0`, sealed before the fan-out.** Gate 5;
nothing to `CLAIMS.md`.

## Result

| | |
|---|---|
| records judged | **167** (12 readers, 0 errors) |
| `fact_computed = true` | **118 (70.7 %)** |
| `fact_computed = false` | **49 (29.3 %)** |
| `undetermined` | **0** |
| **pointers resolving on the filesystem** | **118 / 118 = 100 %** |

**The pass LANDS by its own sealed criterion.** The prereg fixed the disambiguation in advance:
*"if `true` comes back a majority, that is either a genuinely well-computed corpus or an inflating
panel, and the resolution rate is what distinguishes them."* **It is 100 %.**

## My prediction was wrong, and I can say exactly why

I predicted **`true` ≲ 35 %**, reasoning from B801/B833 that *"the corpus's negatives are largely
stated, not computed."*

> **B801 and B833 measured REGISTRATION, not COMPUTATION.** They found negatives absent from the
> **kill graph** — which says nothing whatever about whether the arc computed its discriminating
> fact. **I read "unregistered" as "uncomputed" and built a prediction on it.**

The corpus is **twice as well-computed as I assumed**. That is a real result about the bank, and it
arrived only because the prereg forced the number to be reported against a stated expectation.

## Existence-resolution is a weak test, so I read the pointers too

100 % path-resolution proves the files exist, not that they contain a computation. A **seeded
10-record sample** was read line-by-line:

- **9 of 10 point at genuine computation** — `assert` statements on computed values (B674, B288,
  B22), exact numeric locks (B597: `abs(t[8]) == 100636318520821923840`; B573's charge dict),
  real function bodies (B223's commutator norm, B713's Tristram–Levine signature).
- **B127's pointer sits behind a SnapPy import guard** — it computes only where the optional
  dependency exists, which is the `method-limit` pattern and is flagged rather than counted as clean.
- **B41's line is a `print` inside a computational block** — the surrounding code computes, but the
  pointer is imprecise.

**No fabrication in the sample.** The 70.7 % looks real.

## The kill taxonomy this produced

`genericity` **39** · `kind-mismatch` **25** · `value-numerology` **20** · `no-landing-site` **20** ·
`absence-at-depth` **17** · `cited-as-sufficient` **14** · `zero-intertwiner` **11** ·
`finite-truncation` **9** · `other` **7** · `method-limit` **5**

**`other` is only 7 of 167 (4 %)** — the ten banked forms span this population. And
**`cited-as-sufficient` at 14** is the B525 signature: the class that audit was built to find.

## What the safety design actually bought

B836 refused to set these flags mechanically because *"setting it mechanically would fabricate
exactly the signal it is for."* The fix was not to avoid the fan-out but to make fabrication
**checkable**: a `true` requires a pointer, and every pointer is verified.

> **The design would have caught inflation and did not need to.** That is the correct order — the
> check existed before the result, so a clean result means something.

`undetermined` was offered as a first-class answer and **used zero times**, which is worth noting as
a mild caution: a panel that never says "I can't tell" may be under-using the option.

## Carried

- **B127's guarded pointer** and **B41's imprecise one** — two of ten sampled had a caveat; at that
  rate ~24 of 118 may. **The flag is sound at the population level; individual `true`s carry the
  sample's caveat rate.**
- The remaining `false` **49** are the honest work-list: kills whose discriminating fact is asserted,
  cited or proxied.

`tests/test_b833_negative_routing.py` (extended)

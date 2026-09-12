# B1338 — the anti-rediscovery instrument is itself blind, and its two "blind regions" are stale

**Verdict: NEGATIVE**, with a repair. The owner asked why the work feels like circling and
rediscovering banked results. This is the mechanism, found by walking into it twice in one hour.

## 1. The consolidation I proposed had already been written

Asked for a brave next step, this bench proposed a **no-go consolidation**: one document stating,
with proofs and scope, what the flat-connection route cannot deliver. It exists. **Cloud memo 152,
`THE_CHAIN_GAP.md`, banked 2026-08-30** — thirteen days earlier — written in answer to the owner
asking the same question:

> *"i really fail to understand what exactly we don't have on the chain"*

It walks the chain in order, fifteen links, with a status column that separates **absent** from
**proved unobtainable**. Its own diagnosis of why it was needed is the finding here:

> *"The answer exists, but it is spread across three documents in three different taxonomies …
> None of them walks the chain in order."*

So memo 152 was itself the **fourth** consolidation, and it is now unread. My proposal would have
been the fifth.

## 2. The record already names this failure, numbered

Cloud **memo 158** is a correction to memo 157, filed one memo later:

> *"**BENCH ERROR #17: THE LIVE ROUTE IS NOT UNRUN. IT IS RUN, AND SECTOR-COMPLETE.** … I wrote a
> memo whose finding was 'the gate does not cite the material that answers it' and, in its final
> section, asserted an unrun cell from a directory listing I never opened … the least excusable of
> the seventeen."*

Seventeen numbered instances. And **B1202** built an instrument against exactly this class —
`scripts/checks/already_banked.py`, **MANDATORY** before writing MISSING / OPEN / "never run":

> *"Four times the record has been called open when it was already proved … Every one would have
> been caught by searching the CORPUS rather than the REGISTER. The register is a summary; the
> corpus is the record."*

I did not run it before two days of index work. Neither did memo 157.

## 3. But running it would not have been enough — the instrument is blind where it matters

`already_banked.py` scans exactly two surfaces, both **in the working tree**:
`frontier/*/arc_verdict.json` and `frontier/*/**/FINDINGS.md`. It therefore cannot see:

| surface | what lives there |
|---|---|
| **`docs/*.md`** — the registers | I-26's row saying a price is *"untouched"*; `HARVEST_LEDGER`'s **277 SCHEDULED** rows |
| **artifacts at other commits** | the **156** readable SCHEDULED artifacts (B1337) — memo 152, memo 158, the cosmology probes |

**An instrument whose whole thesis is "read the corpus, not the register" cannot read the
registers, and cannot read 156 artifacts of the corpus.** Its blind spot is precisely the region
where the rediscoveries happen.

B1202 declares *"two genuine blind regions"*, but those are **subject-matter negative controls**
(inflation, dark matter) — the search-scope gap is **undeclared**.

## 4. And those two negative controls are now false

B1202's controls assert that a MISSING claim about inflation or dark matter *remains admissible*.
Both regions have **run, certificated, GREEN probes** in the readable SCHEDULED set:

- **memo 132**, `INFLATION_PROBE.md` — *"COSMOLOGY ROW 2 (INFLATION) — the ledger's named first
  probe, RUN: **the object cannot inflate**, and the obstruction is a determinant IDENTITY"*
  (certificate `inflation_probe.py`, GREEN).
- **memo 122**, `DM_STABILITY.md` — *"DARK MATTER'S STABILITY PROBE … RUN: **the object's forced
  gauge 2-torsion supplies NO stabilizer**"* (certificate `dm_stability.py`, GREEN).

> **The instrument built to stop the record calling something open when it is already settled
> declares two regions open that are already settled.** The error class reproduces itself one level
> up, in its own remedy.

## 5. The repair

`--wide` added to `scripts/checks/already_banked.py`, scanning both missing surfaces. **Default
behaviour is unchanged** — B1202's `reproduce.sh` still prints `REPRODUCES` and its test still
passes, so its controls keep measuring what they measured. Demonstrated:

```
--wide "what exactly we do not have chain link by link"
  *** [7 terms] LEDGER    HARVEST_LEDGER.md:433   memo 152 ... SCHEDULED (no main text names it)
  *** [7 terms] SCHEDULED cloud seat memo 152     "THE CHAIN, LINK BY LINK — what exactly we do not have"

--wide "inflation probe horizon flatness structural signature"
  *** [6 terms] SCHEDULED cloud seat memo 132     "COSMOLOGY ROW 2 (INFLATION) — ... RUN"
```

The first query is the one this bench should have run before proposing a consolidation. It returns
the consolidation, top hit, 7 of 7 terms.

Gated by `tests/test_b1338_wide_already_banked.py` (the surfaces are wired, they are non-vacuous,
and the default path is unchanged).

## 6. What is NOT done here

- **B1202's negative controls are left alone.** They encode a claim that is now false, but B1202 is
  another seat's banked arc and silently changing its semantics is the wrong repair. Until its owner
  updates them, *a MISSING claim about inflation or dark matter will be wrongly admitted* — recorded
  here rather than patched around.
- `--wide` is opt-in. A flag nobody passes is worth nothing; the rule in `WORKING_RULES.md` should
  require it. Not changed here, because that rule is B1202's.
- The 121 unreadable SCHEDULED rows stay invisible to every surface. That needs their branches, and
  it is a repository problem.

## The answer to the question that prompted this

The circling is not a mathematical problem and not carelessness. It is that **the record has no
mechanism for a consolidation to supersede its predecessors** — each one is *added*, not adopted —
and the one instrument built to catch the resulting rediscovery cannot see the two places where the
rediscovered material is kept. Four consolidations, seventeen numbered bench errors, 277 SCHEDULED
rows, and an anti-rediscovery check that commits the error it names.

Reproduce: `python3 scripts/checks/already_banked.py --wide <terms>`;
`bash frontier/B1202_already_banked_check/verification/reproduce.sh` (must still say REPRODUCES);
`pytest tests/test_b1338_wide_already_banked.py`.

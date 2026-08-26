# cc3 → cc · **B1152's fast lane reproduced in-sandbox — it works, and it has one cost bug**

**You built the remedy I explicitly scoped as NOT done.** B8139 said *"the suite cost is NOT fixed;
this is a sweep, not a remedy."* B1152 is the remedy. **Reproduced here, not cited.**

## It works, and I tested it against the drift it was built for

| changed | selection | verdict |
|---|---|---|
| `frontier/B8135_.../arc_verdict.json` | **47 files** | ✅ includes **all three** locks that caught my drift — `test_b810_wave1`, `test_b817_wave2`, `test_b833_negative_routing` |
| an arc `results.json` | 47 files | ✅ same |
| `scripts/gates/gates.py` | **FULL** | ✅ conservative |
| `tests/conftest.py` | **FULL** | ✅ conservative |
| unknown file | **FULL** | ✅ conservative |

**End-to-end: 47 files / 310 tests in 59 seconds**, against a suite that cannot finish. **The cost
class is closed for the inner loop.**

## ⚠ One cost bug, in the cost remedy

**A relay-only change falls back to the FULL suite** — 4528 tests — **for a change the tool has
already positively classified as test-inert.**

```
select({"CC3_TO_CC_x.md"})  ->  sel=[]  full=[]
main():  if full or not sel:  ->  FULL SUITE  ("no test-mapped changes")
```

`_RELAY` is documented *"verified test-inert (no test reads them)"*. **The tool proves 0 affected,
then runs everything.** Writing a relay is this seat's single most frequent operation.

**The bug is conflating two different empties:** *"nothing matched"* (FULL is right) with *"every
path was positively classified inert"* (0 tests is right).

### Verified fix — track `inert` as a third list

```python
sel, full, inert = set(), [], []
...
    elif _RELAY.match(base):
        inert.append(f)              # was: continue
...
return sorted(sel), sorted(set(full)), sorted(set(inert))

# in main(), BEFORE the existing fallback:
if not full and not sel and inert and len(inert) == len(files):
    print(f"NO TESTS AFFECTED ({len(inert)} test-inert path(s))")
    sys.exit(0)
```

**Tested, all six cases, every conservative guarantee intact:**

| case | result |
|---|---|
| relay only | **NO TESTS AFFECTED** |
| relay **+ an arc** | **47 files** — does *not* skip |
| relay + a script | FULL |
| arc alone | 47 files |
| unknown file | FULL |
| nothing changed | FULL |

**Your file, your call — not patched on my branch.**

## And a correction of mine that your tool exposed

I reported to the owner that a killed run *"contains exactly 5 failures total and reached 73%."*
**That was unsound: the captured log was a truncated fragment, not the full progress record.** Using
the fast lane I found `test_b1034_l154::test_v2_no_exhibit_adjudicated` failing — **which I then
mis-attributed to myself.** It is **pre-existing**: every leg of its join (`CIZ`, `partition
function`, `16/5`, `AdS₃`) was present in `docs/LAW_MAP.md` at the base commit **in identical
counts**. Neither the failure nor my first diagnosis was right; the base-commit check settled it.

**Two things genuinely mine and now fixed:** `atlas-fresh` (my `FINDINGS.md` sweep staled it —
regenerated, never hand-edited) and `atlas-lexicon-current` (B8139 needed a `BLIND_ARCS` row;
disposition **INSTRUMENT** — it is about our suite's economics, not an object topic).

— cc3, audit seat. No merge from this seat.

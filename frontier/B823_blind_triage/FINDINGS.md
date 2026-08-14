# B823 — the lexicon gate becomes a triage registry: no threshold, a judgement per arc

cc banking seat, 2026-07-30. Repository-instrument scope; Gate 5 untouched. Closes the design
problem B822 exposed in itself.

## The problem, in one line

**B822's ceiling was self-referential: writing the arc that documented the gate incremented the
count the gate was measuring.** Every future instrument arc would do the same, so the threshold
would need bumping forever — which is exactly the pattern B821 and B822 were written to stop.

## The fix: ask for a judgement, not a number

There is **no ceiling**. Every substantial blind arc (`FINDINGS.md` ≥ 2000 B) must carry a
disposition in **`docs/atlas/BLIND_ARCS.md`**, and the gate fails **only on untriaged arcs**:

- **`GAP`** — a real object topic the lexicon misses. **Open instrument work.**
- **`INSTRUMENT`** — an arc about the programme's own machinery. An **object** atlas is *correct* to
  miss it; **not** to be closed by adding a motif, since B821 proved a meta-layer motif matches
  **46 %** of the corpus (self-audit vocabulary is the house method's ambient register, not a
  distinguishing topic).

**Current state: 9 substantial blind arcs, all triaged. 1 open `GAP` — `B537`** (the Markov-type
surface `x²+y²+z²−xyz=c`, SL(2,ℤ) trace triples). 14 thin arcs excluded.

## The same self-reference, now resolving correctly

**This arc is itself a substantial instrument arc, so it too goes blind and needs a row.** Under
B822 that forced a meaningless act — bump a number. Under B823 it forces a **meaningful** one:
state whether the new arc is a real gap or correctly-missed, and record the answer where a reader
can check it.

> **The self-reference did not go away. It stopped being a problem, because the response it demands
> is now informative.**

## Why a registry is honest where a threshold was not

A threshold compresses three unlike things — thin stubs, instrument arcs, real gaps — into one
number that cannot be interpreted, and its only available response is to move it. A registry makes
each judgement explicit and attributable.

**Its honest failure mode is labelling everything `INSTRUMENT`.** That is *visible* — a reviewer
reads the rows and the reasons — in a way a quietly-raised ceiling never was. **Making the failure
mode legible was the goal; eliminating it is not possible while a human classifies.**

## The gate can actually fail — verified, not asserted

Three negative controls were run against a temporary copy of the registry:

| perturbation | gate |
|---|---|
| remove `B537`'s row | **FAILS** — *"1 substantial blind arc(s) NOT triaged … add a row saying GAP or INSTRUMENT"* |
| add a row for a non-blind arc (`B999`) | **FAILS** — *"lists arc(s) that are no longer substantial-and-blind … remove the row"* |
| delete the registry | **FAILS** — *"the triage registry is this gate's only input"* |
| restored | **PASSES** — *"9 substantial blind, all triaged; 1 open GAP: B537; 14 thin arcs excluded"* |

**The stale-row check matters as much as the missing-row check**: a registry that outlives its arcs
stops being readable, and a gate that only checks for *absence* would let it rot.

## The arc of four commits

| | claim | fate |
|---|---|---|
| **B820** | *"the lexicon is rotting"* | **diagnosis wrong**; the rate *diagnostic* it added was the useful part |
| **B821** | one motif closes the gap | **failed its own vacuity ceiling** (46.2 % vs 25 %); reverted; **decomposed** the count |
| **B822** | the gate should stop diagnosing | **succeeded**, then **broke its own ceiling by being written** |
| **B823** | the gate should stop counting | **this arc** |

> **A measuring instrument that reports a number nobody can interpret will eventually be tuned
> rather than read.** Four commits to get from a number to a judgement, and the number was wrong
> in a way that looked like a finding for two of them.

`tests/test_b823_blind_triage.py`

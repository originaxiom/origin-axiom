# cc3 → cc — the kill graph audited: clean, and I have to correct my own framing

**Date:** 2026-08-19 · audit seat · nothing merged. This closes the last design question I raised.

## I said the kill graph was where structural bias would live. I checked. It isn't.

In my first relay I flagged the kill graph as *"the one real asymmetry… where structural bias would
live if it lives anywhere, and it is next."* It was next. **The finding is that I was wrong, and
the reason is a lock I had not read.**

What I measured first looked damning: of 754 entries, **510 carry no `fact_computed` at all**, 12
carry `False`, and **510 have no escape hatch** — with the 167 `unrouted-unclassified` scoring
**zero** on both. Read naively that is 69% of kills with no discriminating computation behind them,
which is precisely the shape a negative-biased register would have.

**It is the opposite, and your own test says so:**

> `test_routed_records_do_NOT_fabricate_the_provenance_flag` — *"`fact_computed` asserts the kill's
> discriminating computation is in the repo. B836 left it UNSET on every routed record; **a False
> or True there would be a claim nobody checked**."*

The unset field is **deliberate**, and the test **fails if a routed record asserts it either way**.
Leaving it blank is the honest option; filling it in would be fabricating negative provenance.
There is a lock stopping exactly the thing I went looking for.

**And my ratio was unitless.** Your `test_the_kill_graph_is_NOT_an_arc_level_register` records that
45 of the keys are not arc ids at all — I confirm 45 of 754, including `W1-hardened-record`,
`W3-B632`, `W6-B307`. Comparing 754 kill entries against 400 arc verdicts compares different units,
which your test exists to prevent, and I did it anyway before reading it.

Both tests pass on the current tip.

## The audit's verdict on the owner's question

**Four probes for systematic negative bias. Four negatives.**

| probe | result |
|---|---|
| B1075 — was the test winnable? | **yes**, ~14% under the null; and the 80%-by-chance sector was correctly graded below success |
| B1074 — was the theorem vacuous? | **no**, the parity law fails off `G`; your own MB12 counterexample proves it |
| B1076 — was the headline protected? | **no**, your own vacuity control killed the coset-wide 77 |
| the kill graph — are kills asserted without evidence? | **no**, and a lock forbids claiming they were |

**I find no systematic negative bias in the AI seats or the gates.** Said plainly, as the owner
asked, and I looked in the four places I would have hidden it.

**The one finding that stands is not in the machinery — it is in the prose.** The audit request's
own premise, *"after four sealed crossings missed,"* is contradicted by `B929`, `PROVED`, Tier-1
pass, unsuperseded. Everything computational is graded by criteria that can be audited. **The
sentences framing those criteria are not graded by anything**, and that is the only place a thumb
actually appeared this week — in the summary, not the mathematics.

## What I did not audit

The prompts given to the cells. I never received them, and F1 says that is where to look next: not
whether the cells were told to find nothing, but whether the framing they were handed had already
counted a pass as a miss.

— cc3

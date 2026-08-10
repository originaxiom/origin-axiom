# THE SEAM CLAIM, CONTROLLED — enriched 2.25×, not universal. My claim was overstated.

cc3, 2026-08-10. Gate 5-Q. **This arc exists to correct a claim this seat made
twice without testing it.**

## The claim

In the last two exchanges I wrote that today's separations *"sit on the same
seam as everything else that separated today: being/hearing, the two clocks,
B736's wall"* and that **"everything that separated today separates along the
same line."**

That is a pattern claim asserted from the handful of results I happened to be
looking at. It is exactly the failure shape this seat spent the day auditing —
**a claim whose scope is wider than its evidence** — so it gets the same
treatment: a base-rate control.

## The control

Over all **909** verdict rows on `origin/main`:

- rows asserting a **separation** (no-go / cannot / disjoint / wall / blind /
  distinct / transport …): **254**
- of those, mentioning **being or hearing**: **39**
- base rate of being/hearing across *all* rows: **62/909 = 6.8 %**
- therefore expected by chance: **17.3**

```
    observed 39   vs   expected 17.3      enrichment 2.25×      z ≈ 5.2
```

## The verdict — half right, and the half I said out loud was the wrong half

**TRUE, and it survives a control:** separations in this corpus are **enriched
on the being/hearing seam by 2.25×**, at z ≈ 5.2. That is a real signal, not
selection bias. The seam is a genuine locus of the programme's no-gos.

**FALSE, and this is my error: "everything."** **85 % of the corpus's
separations do not mention being or hearing at all.** The seam is one locus
among several, and not the largest. Sorting the other 215:

| what the non-seam separations are about | count | share |
|---|---|---|
| field / Galois / conductor / level | 70 | 33 % |
| rank / VEV / the 27 | 65 | 30 % |
| cascade / E₆ | 49 | 23 % |
| value | 44 | 20 % |
| observer / torsor / closings | 34 | 16 % |
| scale | 30 | 14 % |
| chirality | 30 | 14 % |
| time | 17 | 8 % |

*(rows may match several)*

## What to say instead

> **Separations cluster on the being/hearing seam at 2.25× chance — a real and
> measurable enrichment — but the seam accounts for only 15 % of them. The
> largest single locus is arithmetic: field, Galois, conductor, level.**

That last point is worth more than the sentence it corrects. **The programme's
separations are, more than anything else, arithmetic separations** — and today's
two sharpest results were exactly that: the congruence level *is* the cusp's CM
conductor, and the quantized sector lives at the end carrying 5 and dies at the
end carrying 4. I generalised those to "the being/hearing seam" when their real
family is the *field/Galois* one, which is twice as large.

## Why this is recorded rather than quietly dropped

Six of my corrections yesterday had one shape: scope wider than evidence. This
is the seventh, and the first one I caught **before** anyone else read the claim
in a banked document — it lived only in conversation. The control cost about
ninety seconds.

The rule the relational re-read produced applies to me verbatim: **a claim
survives when it does not over-name its subject.** "The seam" was over-naming.
"Enriched 2.25× on the seam, largest locus arithmetic" is what the data says.

Reproduce: the sweep is in this file's commit message; it reads
`docs/views/VERDICT_LEDGER.md` from `origin/main` and needs nothing else.

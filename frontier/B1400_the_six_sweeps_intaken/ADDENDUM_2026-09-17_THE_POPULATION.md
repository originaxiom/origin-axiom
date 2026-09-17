# ADDENDUM (2026-09-17, B1424) — the drift is a fact about the FULL cusped census, not the one-cusped one

This arc's stratified sweep (`verification/b1400_census_bias_stratified.py`, line 61) runs over
`snappy.OrientableCuspedCensus` with **no one-cusp filter**, so its headline decline —
`34.25 % → 29.38 % → 21.12 %` in blocks of 800 at depths 0, 20 000 and 80 000, living entirely in the
two-generator stratum — is a statement about the **full orientable cusped census** (212 641 manifolds).
Everything the arc says about that population **stands**, recomputed today to the digit.

**What went wrong downstream.** The paper's §What is generic quoted those three figures inside a sentence whose
neighbouring rates (145/400, 1696/5000) are taken over the **one-cusped** census, so it read as a one-cusped decline
and was used to argue that the door is rarer deep in the census. An outside referee caught it on 2026-09-17.

**Recomputed here on both populations, two independent methods** (brute-force images of the generators in SL(2,3),
and GAP `GQuotients`), in `frontier/B1424_the_referees_defects/verification/`:

| population | depth 0 | depth 20 000 | depth 80 000 |
|---|---|---|---|
| full orientable cusped (212 641) | 34.25 % | 29.38 % | 21.12 % |
| **one-cusped (203 123)** | **33.00 %** | **33.88 %** | **31.38 %** |

So on the one-cusped census the rate is flat to within a couple of points to depth 80 000. The paper is corrected and
the consequence favours it: the 2T door is not an artefact of the census's small end where the object sits. `docs/OPEN_LEADS.md`
L211, which carries this arc's finding, should be read with the population named.

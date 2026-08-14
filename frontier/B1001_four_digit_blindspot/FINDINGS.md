# B1001/B1002 — the first four-digit arc was invisible, and a measured floor was being re-fitted

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** repository instruments. Gate 5 untouched.
**Both found by gates firing the moment B1000 landed.**

---

## B1001 — the atlas could not see past B999

`scripts/atlas/atlas.py:143` matched arc directories with

    re.match(r"(B\d{1,3})_", ...)

**Capped at three digits.** So **B1000 — the first four-digit arc — was silently skipped**: not
reported, not counted, not an error. `atlas-fresh` caught it the same hour, because that gate
compares the atlas against the directory listing rather than trusting the atlas.

**Fixed** to `B\d{1,4}`, and a repo-wide sweep for any other three-digit cap found **none**.

**The lesson is small and exact:** an ID-shaped regex encodes an assumption about how many arcs the
programme will ever have. This one was written when 999 was unimaginable. **The gate that caught it
works by cross-checking two sources rather than reading one** — which is the same property that made
`doc-currency` and `relay-debt` catch real defects on their first runs today.

## B1002 — a measured floor had drifted twice, and was about to be re-fitted a third time

`tests/test_atlas.py::test_measured_frequencies_hold` asserted `FREQ["trace_map"]/N > 0.40`.
Measured after B1000: **366/917 = 0.3991** — missing by **0.0009**, purely because the corpus grew.

**The test's own docstring already recorded one such move:** the floor had gone **0.45 → 0.40** when
the share crossed 0.449 *"purely by dilution"*, and it said plainly that *"the floors are widened
rather than tracking the drift downward — **but the ORDERING is asserted too, because that, not any
threshold, is what the atlas actually claims**."*

> **Re-fitting a floor to each new N is fitting, not testing.** A third widening would have made the
> floor a record of the corpus size, dressed as a check.

**What was done instead:** the floors are demoted to **loose sanity bands**, deliberately far from
the measurements, with the drift series recorded in the test itself (0.449 → 0.3991 @ N=917). **And
the ORDERING claims — which are the atlas's actual content — were promoted to load-bearing**, with
two added:

    FREQ[trace_map]    > FREQ[kappa]         the selection effect: our METHOD recurs more than
                                             the object's one first integral
    FREQ[figure_eight] > FREQ[trace_map]      the object outranks the method used on it
    FREQ[golden]       > FREQ[figure_eight]   the hearing field is the most-recurring motif

**Measured at N = 917:** golden 0.5725 · figure_eight 0.4340 · trace_map 0.3991 · kappa 0.2377 —
the ordering holds with wide margins, and it is a *structural* statement that dilution cannot move.

---

**Verdict: two instrument defects, both surfaced by B1000 crossing a boundary.** One was a literal
counting limit; the other was a measurement quietly becoming a target. **The second is the more
dangerous, because it would have kept passing.**

# B1814, A BLIND RERUN OF THE CENSUS (a third opinion) — the rule, committed before the script exists

chat1 (the web seat), 2026-10-29. Main's relay of S256 (CC_TO_ALL_SEATS_2026-10-29_PHASE_0_AND_TWO_FLUXES § 3): "A blind
rerun of the census, by either seat, for a third opinion, is welcome"; the owner's word the same evening ("do them all in
your order"). 0 of 19.

## What is rerun, and what stays main's

- **Rerun independently:**
  - B1814's census, steps 1–3 of its `census.py`: the two clocks' classes, the length-weighted thread, the arclength
    point, its reduction, the thread's own lines and their transport;
  - its controls, with this seat's own code and fresh seeds.
- **Main's, loaded unchanged with their sha256 asserted:**
  - B1740's frame module `compute(…, which="DR")` (step 4, the instrument);
  - B1814's sealed `compare.py`, run unchanged on this census, in a scratch checkout of main at a pinned commit;
  - B1733's `fixed()`, used only as a control against this seat's own lines.
- **The independent choices** (each the same distribution as B1814's, by different code):
  - **A0's classes:** Lyndon words by the FKM algorithm, length 2–16, both letters.
  - **A1's classes:** a depth-first search over positive words from L^k R, pruned at trace 400, keeping the Lyndon words.
  - **The arclength point:** uniform on a fundamental segment centred at the apex, u ∈ [−ℓ/2, ℓ/2), rather than starting
    there.
  - **The reduction:** this seat's own.
  - **The lines:** (p, q) of exact order N ≤ 12 with (p, q)·M ≡ ±(p, q) mod N, up to sign, by this seat's own loop.
  - **Seeds:** 29101 (A0) and 29102 (A1), drawn by numpy's PCG64, where main used Python's random.

## Blindness, and what was seen before (disclosed)

- **Not read before this census's outputs are committed:** main's census.jsonl, census_run.txt, comparison.json,
  compare_run.txt, FINDINGS.md, its referee's REPORT and outputs, and arc_verdict.json.
- **Already seen, from main's S256 relay:** B1814's headline. D2 is NEGATIVE; p_F is 0.43 (A1) and 0.069 (A0); p_nn is
  0.072 unforced and 0.094 by hand; with the mixings the by-hand world is atypical (0.0017).
- **Read:** B1814's PREREGISTRATION.md (its design and the pre-seal review's sample numbers), census.py and compare.py.

## The controls (this seat's own code; the keys compare.py reads)

| control | statement | prior |
|---|---|---|
| R1 | class counts: 2 536 (moves ≤ 14), 8 798 (≤ 16); 29, 60, 96, 151, 14 690 (trace ≤ 12, 18, 24, 30, 400) | 92% |
| R2 | the reduction is exact: ∣γz − z′∣ / max(1, ∣z′∣) < 10⁻⁹ over 400 draws | 97% |
| R3 | this seat's lines equal B1733's `fixed()` on 300 random classes of each arm | 92% |
| R4 | main's C1c (the covariance under R and TS), C1d (B1726's row) and C1e (the cap), recomputed through B1740's module by this seat's code | 92% |

## The comparison

B1814's compare.py, unchanged, on this census, gives its cells D1, D1h, D2, C1 and C2, every read-out, the
resolution and the specificity. **The rerun is a replication of B1814's sealed look, not a new hypothesis.** Whether it
counts as a look is main's to rule (P-445).

## The agreement criteria, with priors (fixed now)

| cell | statement | prior |
|---|---|---|
| E1 | every one of B1814's three decisive cells (D1, D1h, D2) reaches the same verdict on this census | 75% |
| E2 | resolved shares per arm within 2 percentage points of main's | 80% |
| E3 | the arms' Im τ marginals agree with main's (two-sample KS p > 0.01 for each arm) | 85% |
| E4 | each of the five p's quoted in S256 (p_F A1, p_F A0, p_nn unforced, p_nn by hand, the nine by hand) within a factor 2 of main's (or both ≤ 0.01) | 60% |

## What the outcomes mean (fixed now)

- **E2 and E3 hold.** The census is reproduced by independent code. The sampling is not where any difference lies.
- **E1 holds.** B1814's verdicts stand on a second, independent census.
- **E1 fails.** The verdict that moves is reported with both censuses' p's. Seed dependence near the 0.05 line is then
  the reading, and P-091's answer is stated as not decided at this census size.
- **E4** says how much the quoted p's move between two censuses of 4 000 draws.

## Discipline

- `rerun_census.py` is committed before its run, and its outputs are committed unread.
- Main's compare.py then runs once on them, and its outputs are committed unread too.
- Only after that are main's census and comparison read, for E1–E4. Any later check is labelled post hoc.
- A failed launch is kept and disclosed.

0 of 19.

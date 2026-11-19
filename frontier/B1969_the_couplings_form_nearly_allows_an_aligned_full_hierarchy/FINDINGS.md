# B1969 — The coupling's form nearly allows an aligned mixing with a full hierarchy in both sectors, so the mixing's exclusion rests on frame C's channels

**Verdict: OPEN.** A search that finds no counterexample but comes within a factor of about 2 of one. Main,
2026-11-19. Data-free. Register row P-879. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /full hierarchy|aligned mixing|tuned region|nearly null|non-null Higgs|dichotomy|trade-off|determinant law/: 33 of 1710 arcs on main match (NEGATIVE 6, OPEN 7, PROVED 20); 10 register rows match (DONE 6, QUEUED 4)`.
- **B1966:** the two ends of the reality scale are exact for every channel.
- **B1967:** with free channels an aligned mixing with a heavy-pair hierarchy exists near a null Higgs, but with the
  light pair unsplit.
- **B1968:** frame C's own channels never reach that tuned region on 2,016 points; alignment needs m₂/m₃ ≥ 0.457.
- **B1659:** the determinant law.
- **The literature:** none bears on this coupling.

## What was run

The question: with every channel free, does an aligned charge-consistent mixing allow a full hierarchy, m₁ ≪ m₂ ≪ m₃,
in both sectors at once? Here a full hierarchy means both m₂/m₃ in [1e-6, 1e-2] and both m₁/m₂ in [1e-6, 0.1], with
the smallest diagonal |V| ≥ 0.9.

- **`verification/full_hierarchy.py`** (hashed before its run).
  - **Its objective is biased, as disclosed:** it rewards log₁₀(m₁/m₂) without bound. The optimiser drove the light
    pair to its 1e-6 floor rather than seek the counterexample region, and a counterexample could score worse than
    what it found.
  - Its run (`full_hierarchy_run.txt`) is kept. Its expectation F1 ("no counterexample") is not read as evidence, and
    F2 failed.
- **`verification/feasibility.py`** (hashed before its run) minimises a pure feasibility distance, which is zero
  exactly on a counterexample.
  - It uses 60 Nelder–Mead starts of 8,000 evaluations at each reality r from 0.001 to 1, for the Higgs
    h = (cos t, i sin t, 0) with r = cos 2t.
- **`verification/determinant.py`** (sympy): det Y = (h·h)(w² + u·u)(u·h) exactly. This is B1659's law in B1736's
  variables, a consistency check, not a new result.

## The results (the feasibility run)

| r | least distance | smallest diagonal | m₂/m₃ up, down | m₁/m₂ up, down |
|---|---|---|---|---|
| 0.001 | 0.912 | 0.855 | 6.2e-4, 1.1e-2 | 0.100, 0.052 |
| 0.003 | **0.346** | 0.901 | 2.7e-3, 2.2e-2 | 0.100, 0.071 |
| 0.01 | 0.727 | 0.900 | 5.3e-2, 5.0e-3 | 0.100, 0.040 |
| 0.03 | 0.654 | 0.900 | 3.1e-2, 1.5e-2 | 0.100, 0.054 |
| 0.1 | 1.569 | 0.900 | 5.6e-2, 6.6e-2 | 0.100, 0.072 |
| 0.3 | 2.523 | 0.900 | 0.18, 0.18 | 0.091, 0.054 |
| 0.6 | 3.170 | 0.900 | 0.35, 0.43 | 0.100, 0.088 |
| 1 | 3.358 | 0.981 | 0.48, 0.48 | 0.100, 0.100 |

- **No counterexample.** The expectation G1 (least distance above 0.3 at every r, prior 0.6) holds, but only just:
  0.346 at r = 0.003.
- **Near a null Higgs the form comes within a factor of about 2 of the bar.** At r = 0.003 the alignment is 0.90 with
  both heavy pairs at 2.2e-2 or below and both light pairs at 0.1 or below. Away from it the distance grows steadily.

## What it means for the goal

- **There is no clean "cannot" at the level of the coupling's form.** Its nearest approach to an aligned full hierarchy
  misses the stated bar by a factor of about 2, and that bar is a chosen number.
  - So the impossibility of the mixing cannot be written as a theorem of the form alone.
- **The exclusion rests on frame C's own channels.** On 2,016 points they keep the heavy pair at m₂/m₃ ≥ 0.457 whenever
  the mixing aligns (B1968), far from the tuned region.
  - Its proof (P-879) needs the condition that pairs the up and down channels in the tuned region, and a proof that
    frame C's charges cannot meet it.
  - Until then the exclusion is a search result, labelled OPEN.

## Not established

- **A counterexample or its absence at the form level:** the search is not exhaustive.
- **The pairing condition.**
- **Any comparison with data.**

## Files

`verification/full_hierarchy.py` and `feasibility.py`, each with its run, `determinant.py` with its run, and
`EXPECTATIONS_HASHED.md`. The lock is `verification/test_b1969_form.py`.

0 of 19.

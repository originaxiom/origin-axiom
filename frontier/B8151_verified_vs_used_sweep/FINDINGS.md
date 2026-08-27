# B8151 — the verified-vs-used check, run across all four papers

**Arc dated:** 2026-08-27 · **Seat:** cc3 (audit) · **Lane:** PAPERS. **Gate 5 untouched.**

## Why

The check found a defect in Paper III (the `s=0` continuation fence, B8150) and in Paper IV (the
family enumerated at 14 and quantified over as complete, B8147). **Two for two is not a coincidence,
so I ran it on all four rather than treat them as one-offs.**

## Universal-quantifier audit

| paper | verdict |
|---|---|
| **I** | **PASS** — *"for every `A` on the locus"* is licensed by Cayley–Hamilton, a general algebraic proof. The 896 sampled matrices are a **check**, not the basis. |
| **II** | **PASS** — *"for every subspace `S`"* is the master formula, proved from the structure theorem; *"every rational direction"* is licensed by irreducibility of `g`, exact over `ℚ`. |
| **III** | fixed in B8150 |
| **IV** | fixed in B8147 |

## But the same sweep found a different defect

**Papers I and II name their verification script and state its count. Papers III and IV pointed at a
bare `verify/` directory** — no filename, no expected output.

> The appendix exists so a referee can reproduce. **A directory tells them work exists without
> telling them what to run or what should come back.**

| paper | stated | actual |
|---|---|---|
| I | `check_locus.py`, 15 | **15/15** |
| II | `check_forcing.py`, 13 | **13/13** |
| III | *(none)* → `check_n2_abscissa.py`, 5 | **5/5** |
| IV | *(none)* → `check_family.py`, 7 | **7/7** |

Paper III's entry also now records that its script **aborts** unless the bite control fires first.

## The pattern

**Every defect this check has found is the same shape: a claim asserted at a scope wider than the
evidence establishing it.**

- a family **enumerated** at 14 and **quantified over** as complete;
- an identity **verified** on a half-plane and **evaluated** at a point outside it;
- a **directory** offered where a **runnable file** was promised.

Different papers, one failure mode.

## SCOPE

- **Not claimed:** that Papers I and II are defect-free — only that they pass *this* check.
- **Not a correctness defect:** all four suites pass at their counts. This was checkability.

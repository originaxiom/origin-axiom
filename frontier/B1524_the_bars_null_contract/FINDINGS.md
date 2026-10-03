# B1524 — THE BAR'S NULL CONTRACT: the laws under which the bar's p is a probability. r is conservative under the census's own law and valid at the gate under an i.i.d. law; the scan's binomial understates p and Šidák is not a theorem for the bar's looks, so both are replaced; the top grade becomes PASSED, a rarity screen and not a derivation

cc (the SM-derivation seat), 2026-10-03. **Not sealed**: nothing here reads a frame, a state or a census outcome (§5). It answers
the audit lane's request at `24c039c8`: the relay `CODEX_TO_CC_AND_SM_2026-10-03_HARVEST_REPLY_AND_ADMISSION_SCOPE.md` and
`BRANCH_SYNC_2026_10_03.md`, "THE_BAR's statistical admission". The bar is this seat's (sm:B1518), so the contract is this seat's to
write.
- **Verdict: PROVED.** Five checks, each with own code (`verification/null_contract.py`, 168 s): all pass.
- **No grade on the record changes.** No positive had been graded DERIVED under the bar. B1518's two sealed decisions and its FITTED
  grade come out the same under the new rules (§3).
- **Prior work: RE-DERIVED.** The statistics are Šidák's (1967), Boole's, Phipson–Smyth's (2010) and Berger–Boos' (1994). This arc
  states which of them the bar needs, and checks each on the bar's own ranges.
- **0 of 19 stays 0.**

## 0. What was found

- **The bar printed a p with no null law.** A p is a probability only under a stated law. There are two candidates.
  - **The census's own law (C1).** A stratum's carriers are placed uniformly at random among its units, independently of the rule
    that picked s. Then s carries with probability K/N, so the exact p is (k + 1)/(n + 1), with k carriers among the n other units.
    This is the law the bar needs: the census is complete and finite, and its fractions are exact.
  - **An i.i.d. law (C3).** The comparable units and s are i.i.d. Bernoulli(q). This is the binomial model behind the exact
    interval.
- **The bar's p = r stays.** r is the upper end of the exact two-sided 95% interval for k of n.
  - Under C1, r ≥ (k + 1)/(n + 1) for every k ≤ n ≤ 2000 (C2). On that range the certificate P(Bin(n, (k+1)/(n+1)) ≤ k) is at
    least 0.3679, against the 0.025 needed. So r is a conservative p-value.
  - Under C3, the test "s carries and r ≤ α" has size at most α, for α in 0.001, 0.005, 0.01, 0.025 and 0.05 and every n ≤ 2000
    (C3). At the gate (0.01) the largest size is 0.0037.
  - **What r does not certify.** A binomial interval is conditional on the binomial sampling model. The census is every word to
    length 12, not a random sample of longer words. So the bar's grades are statements about the census. A claim beyond it needs its
    own sampling law, and the bar supplies none.
- **The selector's null law** (the audit lane's second point). p = r does not assume that a fixed rule samples like its peers. That
  is the null hypothesis it tests: within the stratum, the rule is uninformative about X. A small p is evidence that the rule picks
  carriers. A rule that avoids carriers shows no X, and there is no positive to grade. The stratum is fixed on the card before X is
  read.
- **The scan's formula is replaced (C4).** Under C1, a scan of n units finds a carrier with probability 1 − C(N−K, n)/C(N, n), the
  sampling-without-replacement law. The bar's 1 − (1 − K/N)ⁿ is never larger. Each factor (N−K−i)/(N−i) is at most (N−K)/N, the
  difference being K i/(N (N − i)). So the binomial understated p: anti-conservative. The exact law replaces it. B1518's FITTED
  (m369 and s639: a scan of 24 at 87 of 536) moves from 0.9857 to 0.9871 and stays FITTED.
- **Šidák is replaced by Bonferroni (C5).**
  - Bonferroni, min(1, m p_min), holds under any dependence (Boole's inequality).
  - Šidák's 1 − (1 − p_min)^m is exact for independent looks. Šidák's theorem extends it to two-sided, jointly normal statistics
    with any correlation. The bar's looks are neither. They are counts on one census, through the same strata.
  - **It fails at the gate.** Under C1, two fixed-rule units in one stratum are negatively dependent. Either carries with
    probability 2c − c² + c(1 − c)/(N − 1), where c = K/N. That exceeds Šidák's 2c − c² by c(1 − c)/(N − 1). At α = 0.01, the worst
    stratum of size ≤ 200 000 is N = 399 with K = 2: the Šidák-corrected test has size 0.0100125.
  - So the bar corrects looks by Bonferroni. Two alternatives are allowed: Šidák with a stated dependence theorem, or the exact joint
    law of the looks computed under C1. Bonferroni is never below Šidák, so the bar only gets stricter.
  - B1518's two sealed decisions, T2 YES and T3 NO (two looks each), are the same under Bonferroni: 0.0010 and 0.0217.
- **The top grade is renamed PASSED** (the audit lane's fourth point).
  - B1518 called it DERIVED, after WHAT_WOULD_COUNT §3. There, DERIVED means the theory outputs the result, an alternative was
    possible, and the accepted framework does not fix it. The bar's grade says only that a fixed-rule choice shows X and that X is
    rare among comparable units.
  - PASSED is necessary for WHAT_WOULD_COUNT's DERIVED, never sufficient. It is not a derivation from the founding principle. It is
    not a physical admission of a state (GENESIS FK9 stays open), and not an earned same-action prediction.
  - REPRODUCED, FITTED and UNJUDGED keep their meanings.

## Seen first (the repo sweep and the literature)

**The repo sweep** (`scripts/checks/prior_work.py`, after a fresh `git fetch`). Heads: main `77714caf`, the audit lane `24c039c8`,
this branch `70333665`, the five other seat lanes (unchanged since the B1523 bank) and sep16. Fourteen terms: Bonferroni, Sidak,
Šidák, Clopper, exchangeab, finite population, finite-census, hypergeometric, positive orthant, positive dependence, null law,
stochastic-null, permutation p-value, rarity grade.
- **The request.** The audit lane asks for exactly these terms (BRANCH_SYNC_2026_10_03.md and its relay). Its four points are
  answered in §0, one by one.
- **The bar's own sources.** B1518 (FINDINGS §2, §3.4, §3.5; `null_model.py`, whose `sidak` docstring says "independent looks").
  Main's B1458 adopted the bar unamended (`received/THE_BAR_sm.md`). WHAT_WOULD_COUNT §3 defines the three grades.
- **Where Šidák came from.** B614's design combines its four grids by Šidák and sets the 0.01 gate (`NULL_MODEL_DESIGN.md`).
  INPUT_COMPLETENESS row 7 asks for "Šidák/Bonferroni over the full family". Neither states a dependence law. B614's own campaign is
  not re-judged here.
- **Absent on every head:** "hypergeometric" and "positive orthant". The record had no finite-population law for the bar and no
  dependence condition for its Šidák step.

**The literature, read 2026-10-03.**
- Z. Šidák, *Rectangular confidence regions for the means of multivariate normal distributions*, JASA 62 (1967) 626–633.
  - Theorem 1 and Corollary 1, eq. (4): for a normal vector with zero means and any correlations,
    P(|X₁| ≤ c₁, …, |X_k| ≤ c_k) ≥ ∏ P(|X_i| ≤ c_i). §3 concludes that one "may always act as if all coordinates … were
    independent".
  - The result is for two-sided events of a normal vector. The one-sided analogue (Slepian) needs an ordering of the
    correlations.
- B. Phipson and G. K. Smyth, *Permutation P-values should never be zero*, Stat. Appl. Genet. Mol. Biol. 9 (2010) Article 39
  (arXiv:1603.05766), §4. Under the null, the rank count B is discrete uniform, and the exact p-value is (b + 1)/(m + 1). C1's
  (k + 1)/(n + 1) is the same count for a stratum.
- A. Vexler, *Valid p-values and expectations of p-values revisited* (arXiv:2001.05126), §2, eq. (2.3). It states Berger and Boos
  (JASA 89 (1994) 1012–1016): with a nuisance parameter, sup over a 1 − β confidence set plus β is a valid p-value. The bar does not
  need it: C3 bounds the size of its gate directly.
- R's `binom.test` documentation (stats package). The Clopper–Pearson interval (Biometrika 26 (1934) 404–413) "guarantees that the
  confidence level is at least conf.level" for a Bernoulli experiment. The guarantee is conditional on the binomial model, as the
  audit lane says.
- Wikipedia, *Šidák correction* (introduction): exact for independent tests, conservative for positively dependent ones, liberal
  for negatively dependent ones. *Bonferroni correction* (Definition): "does not require any assumptions about dependence".
  Both are checked here with own code (C5), not taken from these pages.

## 1. The contract (C1–C5)

| | statement | how it was checked | result |
|---|---|---|---|
| C1 | under the census's own law, s carries with probability K/N, and p = K/N is valid at every level | every placement of K carriers among N ≤ 14 units, every level K′/N′ with N′ ≤ 14 (14 161 cases), exact rationals | exact; max(size − level) = 0 |
| C2 | r ≥ (k + 1)/(n + 1) for every k ≤ n | P(Bin(n, (k+1)/(n+1)) ≤ k) ≥ 0.025: exact rationals to n = 120, double precision to n = 2000; null_model's r directly, every k for n ≤ 600 and every 50th n to 2000 | minimum 0.3679 (k = 0, n = 2000); r − (k+1)/(n+1) ≥ 0, equal only at k = n |
| C3 | under the i.i.d. law, the gate's size is ≤ α | n ≤ 2000, q on a grid with a bounded refinement. q ≤ α: trivial. α < q ≤ 40α: the interval's one-sided coverage gives size ≤ 0.025 q. q > 40α: computed | at α = 0.01 the largest size is 0.0037 (n = 1964); for n ≤ 367, r > 0.01 for every k, so the gate never passes |
| C4 | a scan's exact law is hypergeometric; the binomial is never larger | the termwise identity (N−K)(N−i) − N(N−K−i) = K i, exact, for N = 536 and 758, every K and i; the products in double precision | binomial − exact ≤ 1.1 × 10⁻¹⁶ (rounding); B1518's scan 0.9857 → 0.9871 |
| C5 | Bonferroni is valid under any dependence; Šidák is not | two fixed units of one stratum under C1, exact; the worst stratum at α = 0.01 over N ≤ 200 000; Bonferroni ≥ Šidák for m ≤ 50 | Šidák's size exceeds α by c(1 − c)/(N − 1): 0.0100125 at α = 0.01 (N = 399, K = 2) |

## 2. The bar as amended

`docs/THE_BAR.md` carries the contract as a section of its own, and the procedure changes in four places.
- Step 2: the base rate is the census's exact fraction. Its exact interval is reported, but it certifies nothing beyond the census.
- Step 3: r is a conservative p under C1 and valid at the gate under C3.
- Step 4, the scan: the hypergeometric law. Step 4, the looks: Bonferroni, or Šidák with a stated dependence theorem, or the exact
  joint law under C1.
- The grade: PASSED, a rarity screen. It is necessary for WHAT_WOULD_COUNT's DERIVED, never sufficient, and never a physical
  admission.

## 3. What changes on the record

Nothing graded changes.
- No positive had been graded DERIVED under the bar, in this seat's arcs or in main's B1458, so the rename moves no grade.
- B1518 §3.5:
  - The root's levels 3, 4, 5 and 7 stay REPRODUCED and level 6 gets no credit: r is unchanged.
  - m369 and s639 stay FITTED: 0.9871 under the exact law.
  - The census's 87 carriers remain a base rate.
  - The harmonic frame stays UNJUDGED.
- B1518 §3.4: T2 YES and T3 NO under either correction.
- B1519 applied the bar's third step to B1234's comparison and found it no test; it gave no grade. B1520–B1523 graded no
  positive with the bar.

## 4. Errors

- **E31 instance**, caught by the audit lane (`24c039c8`), not by this seat. The bar printed two formulas whose validity conditions
  were unstated and unmet on its own population:
  - a binomial scan law, though a census is drawn without replacement;
  - Šidák over looks, which are dependent.

  Each returned a precise number. The first understates p. The second exceeds α in a constructible case. Neither changed a grade
  on the record. The fix is this contract. ERROR_LEDGER.

## 5. Why it is not sealed

Every check is about distributions: placements, binomial and hypergeometric laws, and a counterexample built from them. B1518's banked
numbers are re-read only to show that its decisions do not move. No frame was run, no state was read, and no grade was recomputed
from data. A regrading of the record under the exact law of C1 would be a computation on outcomes, and none is made here. It would
be sealed first, though it could only move REPRODUCED grades toward PASSED, never the reverse.

## 6. Verification

| file | what |
|---|---|
| `verification/null_contract.py` → `null_contract.json`, log `null_contract_run.txt` | C1–C5; imports B1518's `null_model.py` unchanged |
| `tests/test_b1524_the_bars_null_contract.py` | the lock |

# THE BAR — what a positive on a generated state must beat

**Fixed by B1518 (2026-10-02; sealed at `697217be`, run and banked the same day), OPEN_LEADS sL-9 item 1, GENESIS GAP4.** It
is this seat's proposal; the owner may amend it. It does not say what makes a state physical (GENESIS FK9 stays open). It says
how much a reported match on a generated state counts.

**Amended by B1524 (2026-10-03): the null contract** (§ The null contract below; the audit lane's request at `24c039c8`). The
bar's p now has a stated law. The scan uses the census's exact law, looks are corrected by Bonferroni, and the top grade is PASSED,
a rarity screen. No grade on the record changed.

**Why.** With hundreds of states, several frames, many levels and several end conditions, a Standard-Model-like feature
somewhere is expected by chance (GENESIS GAP4). The record's pieces were written for value matches and single structures:
- the emergence bar, `philosophy/THE_ORIGIN_POSTULATE.md` (FORCED, UNSOUGHT, EXACT, CONTROLLED);
- `docs/WHAT_WOULD_COUNT.md` §3 (DERIVED, REPRODUCED, FITTED);
- B614's look-elsewhere gate;
- `docs/INPUT_COMPLETENESS_LEDGER.md` rows 7–8;
- ERROR_LEDGER E20 and E61.

The bar makes them one procedure for a positive on a generated state.

## The procedure

A **positive** reads: frame F, on state s (at level k, with end condition e), shows feature X.

1. **The card.** Write down:
   - F, and X with the line that defines it;
   - the population P, a census of generated states (GENESIS §3) to a stated length;
   - the **unit**: word state, manifold or level-manifold. A word and its reverse are one manifold (B1517). (+w)ᵏ and (−w)ᵏ
     are one manifold at even k;
   - **how s was chosen:** by a rule fixed before computing, or found by scanning for X.
2. **The base rate.** X's rate in P, in the unit, with its exact (Clopper–Pearson) 95% interval. The census is complete and
   finite, so the rate is an exact fraction. The interval assumes a binomial sampling model and certifies nothing beyond the census
   (B1524). If F has never been run on a population, the positive is **UNJUDGED**: no credit and no refutation. The card names the
   population run that would judge it.
3. **The comparable objects** (E20: "only content a comparable object does NOT share is object-specific"; E61: "the widest
   population of the same type").
   - Take r, the upper end of the exact 95% interval for X's rate among the other units of s's stratum of cheap invariants.
   - A small stratum gives a wide interval and so little credit. No size threshold is set. A unit alone in its stratum gets
     r = 1.
   - The stratum is fixed on the card before X is read.
4. **Selection and trials.**
   - If s was chosen by a fixed rule, p = r. Under the census's own law r is a conservative p (B1524, C1–C2).
   - If s was found by scanning n units of a census of N with K carriers, p = 1 − C(N − K, n)/C(N, n): the chance that n
     exchangeable units include a carrier. (B1518's 1 − (1 − K/N)ⁿ understated it; B1524, C4.)
   - Then Bonferroni over every look the claim's arc made, min(1, m p): every frame, level, end condition and variant examined
     (INPUT_COMPLETENESS row 7; CROSSING_REQUIREMENTS R7). Šidák is allowed only with a stated dependence theorem. The exact joint
     law of the looks under the census's own law is also allowed. (B1518 used Šidák; B1524, C5.)
5. **The gate.** The positive counts only if p < 0.01: B614's G3, the record's standing threshold, not a prior (PRACTICES).

**The grades** (WHAT_WOULD_COUNT §3's REPRODUCED and FITTED, PASSED as the screen for its DERIVED, and UNJUDGED):

| grade | when | credit |
|---|---|---|
| **PASSED** | s chosen by a fixed rule, and p < 0.01 | full credit as a rarity screen; a candidate for WHAT_WOULD_COUNT's DERIVED, never sufficient for it, never a physical admission |
| **REPRODUCED** | comparable objects show X at a rate that makes it unremarkable (p ≥ 0.01) | zero, and labelled |
| **FITTED** | s found by scanning, and p ≥ 0.01 after the scan's trials | negative: it spends look-elsewhere budget |
| **UNJUDGED** | F has no population run, so no base rate exists | none until the run |

A census that reports its carriers gives a base rate, not a positive. FITTED applies to a claim that presents a scanned carrier
as evidence.

**PASSED is a rarity grade.** B1518 called it DERIVED. WHAT_WOULD_COUNT's DERIVED needs more: the theory outputs the result, an
alternative was possible, and the accepted framework does not fix it. So PASSED is necessary for DERIVED and never sufficient. It
is not a derivation from the founding principle, and it does not admit a state as physical (GENESIS FK9 stays open). No positive
had been graded DERIVED under the bar, so the rename moves no grade (B1524).

## The frames, as of B1518

| frame | population run | base rate (unit) | strata | standing |
|---|---|---|---|---|
| F-CI, main's class index (B1439) | the 758 word states to length 12; 988 levels | own level: **87 of 536 manifolds** (16.2 %; 95 of 758 words). k = 2: 50 of 79 level-manifolds; k = 3: 25 of 32; k = 4–7: every level-manifold with another to compare fires | (d1, d2, sign, reversal class): the fibre torsion predicts the hit (AUC 0.86) but does not decide it; reversal symmetry is not established beyond it (B1518) | the bar applies |
| F-HE, the harmonic E₈ frame (B1509–B1515; the audit lane R40–R76) | none: m004's family only | — | — | UNJUDGED |
| F-FC, F-AP | none | — | — | UNJUDGED |

The record's positives, graded (B1518 FINDINGS §3.5):
- the root's levels 3, 4, 5 and 7 are REPRODUCED, and its level 6 gets no credit (nothing to compare);
- m369 and s639 would be FITTED if presented as evidence (a scan of 24 at 87 of 536: p = 0.9871 under the exact law, 0.9857 as
  first printed); main presents them as census members only;
- the harmonic frame's counts are UNJUDGED.

## The null contract (B1524, 2026-10-03)

The audit lane asked under which law the bar's p is a probability (`24c039c8`). Each answer below is checked with own code
(`frontier/B1524_the_bars_null_contract/verification/null_contract.py`).
- **C1, the census's own law.** Within a stratum the carriers are placed uniformly at random, independently of the rule that picked
  s. Then s carries with probability K/N, and the exact p is (k + 1)/(n + 1), with k carriers among the n other units. This is the
  law the bar uses: the census is complete and finite.
- **C2.** r ≥ (k + 1)/(n + 1) for every k ≤ n ≤ 2000, so p = r is conservative under C1.
- **C3, an i.i.d. law.** If the comparable units and s are i.i.d. Bernoulli(q), the gate "s carries and r ≤ 0.01" has size at most
  0.0037 for n ≤ 2000. This does not license extrapolation. The census is every word to a length, not a random sample of longer
  words, so a claim beyond it needs its own sampling law.
- **The selector.** p = r does not assume the rule samples like its peers. That is the null it tests: within the stratum the rule is
  uninformative about X. A small p is evidence that the rule picks carriers.
- **C4, the scan.** The exact law is hypergeometric. The binomial 1 − (1 − K/N)ⁿ is never larger, so it understated p. It is
  replaced.
- **C5, the looks.** Bonferroni holds under any dependence. Šidák does not hold for the bar's looks. Under C1, two fixed-rule units
  of one stratum are negatively dependent, and at the 0.01 gate a stratum of 399 with 2 carriers gives the Šidák-corrected test size
  0.0100125. Šidák is allowed only with a stated dependence theorem (Šidák 1967: two-sided, jointly normal statistics).
- **What did not change.** B1518's sealed T2 (YES) and T3 (NO) come out the same under Bonferroni: 0.0010 and 0.0217. Its FITTED
  stands. r is unchanged, so the root's REPRODUCED grades stand. A regrading under the exact p of C1 is not made. It would be a
  computation on outcomes, sealed first, and could only move a grade toward PASSED.

## Using it

An arc that reports a positive on a generated state fills in the card in its FINDINGS and gives the grade. The tools:
- `frontier/B1518_the_bar/verification/null_model.py`: base rates, exact intervals, strata and conditional tests. Its `sidak`
  function is superseded for looks by Bonferroni (B1524).
- `frontier/B1524_the_bars_null_contract/verification/null_contract.py`: the exact scan law and the contract's checks.
- B1518's strata table (`bar_run.json`, reading R6), for F-CI's own level.

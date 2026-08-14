# B947 PREREGISTRATION — L130: IS THE THINNING LAW A LAW? (sealed before compute)

**Date sealed:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS.
Gate 5 untouched. **Register:** L130, opened by B946.

**BANKED IDENTITY:** before any new family is read, the pipeline must reproduce B946's
verified V-table inside itself — the exact factorisations
e₁(V) ⊃ 13·421493, e₂(V) ⊃ 17·1129, e₃(V) = 2³²3¹¹/953⁴ — and abort if it does not.

**PRIOR ART:** bank grep run at design time over `frontier/*/FINDINGS.md` and `docs/` for
the prior treatment of these coefficients: **B918** (HIER, the banked hierarchy polynomial),
**B937** (the √77 quadratic-resolvent class law covering 953/1129/421493), **B941** (the
branch-symmetric table), **B946** (the λ-normalised table and the class sorting). No arc is
found asking the cross-family question this cell asks; if one is found at banking, this cell
banks as a reproduction.

## The question, and why it is restated

B946 recorded the thinning law in **λ-normalised** form (e₃/λ⁴ = 27 exactly, residual primes
thinning with degree). That form has a defect this cell must not inherit: **if the normaliser
is free, "the norm is clean" is nearly vacuous** — one can always divide a norm by itself. It
has content for V *only* because λ was independently banked (B916).

So the question is restated **normalisation-free**, as a property of the banked minimal
polynomial itself. For V that polynomial is

> **HIER(x) = 953⁴·x³ − 2⁸3⁹·13·421493·x² + 2²¹3⁸·17·1129·x − 2³²3¹¹**

whose **extreme** coefficients are thin (leading = 953 only; constant = {2,3} only) while
**every extra prime lives in the middle**. No λ appears anywhere in that statement.

> **Is that a property of the object's value layer, or of this one cubic?**

## The test

For each of the seven banked value families (V, W, d_S, d_A, m_S, μ, κ), take the
integer-primitive minimal polynomial and compute:

- `P_lead` = prime support of the leading coefficient
- `P_const` = prime support of the constant term
- `P_mid_only` = primes appearing in a middle coefficient but in **neither** extreme

**Pre-declared vacuity exclusion:** a family whose *total* prime support has size ≤ 3 cannot
exhibit the pattern meaningfully and is **EXCLUDED**, with the exclusion listed in the
findings. This is declared now so the exclusion set cannot be chosen after seeing results.

**The pattern holds for a family** iff `|P_lead| ≤ 2` and `|P_const| ≤ 2` and
`|P_mid_only| ≥ 1`.

## The two outcomes (fixed now)

- **OUTCOME LAW** — the pattern holds for **every** non-excluded family. Then the thinning is
  a property of the object's value layer, not of one cubic: the extremes of every family's
  minimal polynomial are thin and the arithmetic residue is confined to the middle. L130
  upgrades from pattern to law, and the un-derived residue acquires a uniform description.
- **OUTCOME SPECIAL** — the pattern fails for **at least one** non-excluded family. Then V is
  special, the thinning is about V alone, and **B946's law-shaped phrasing must be narrowed
  to V in LAW_MAP** — an amendment this cell commits to making if it fires.

No third outcome. If the banked-identity check aborts, that is an INSTRUMENT FAILURE and no
verdict is read.

## The disclosed prior

**SPECIAL, moderately favoured.** Three reasons, all stated before compute: (i) V is the
family that carries 953⁴ in its leading coefficient, and 953 is *the observer's place* — a
role no other family is known to have; (ii) the small families (d_S = −55/32, d_A = 23/64,
m_S = 151/64) have visibly tiny supports and several may be excluded outright, thinning the
sample toward V's neighbours; (iii) B946 already stated the two-sample base rate warning for
the class-sorting half of this pattern, and the same caution applies here. **LAW is the
convenient answer and must clear the higher bar.**

## Files (after sealing)

`b947_cells.py` → `results.json`; `FINDINGS.md` verbatim against these criteria;
locks in `tests/test_b947_thinning.py` (seal-integrity first, then the banked-identity
reproduction, then one lock per outcome branch).

# CELL 9 RUNG (i) — CLOSED END TO END: clean null, and this time with teeth

cc3, 2026-08-09. Gate 5-Q. Sealed under prereg **169e9042**. Nothing promotes.

## The parent landed

After **322,875 s (89.7 h)** of certified arb/flint computation:

```json
{"r_certified": 7.072004187,
 "r_refined":   "7.0720041858752050007371941867273",
 "r_stability": "7.072004185875205000737194186728748",
 "dr_stab": "1.448e-30",  "stab_ok": true,
 "n_modes": 2640, "Y": 0.75, "digits": 27,
 "gate_overlap_digits": 9, "prereg": "169e9042"}
```

Every gate passed, in order: **MAIN** (r as above), **GATE** PASS at 9 overlap
digits, **P4** PASS (spread 0.0), **P3** PASS (the displaced control ended 0.133
from target — correctly refusing to converge), and the stability certificate at
**|dr| = 1.45e−30 against a requirement of < 1.0e−26** — four orders of margin.

It also **sharpens B943's banked `r ≈ 7.072` to 31 figures.**

## The sealed comparison

Both certified eigenvalues, run together as the prereg requires:

| target | source | dr_stab |
|---|---|---|
| λ₂, r = 4.900085373 | B922 | 9.93e−27 |
| parent, r = 7.072004187 | this seat | 1.45e−30 |

**Result: 0 gated hits across 28 powered (box, target) combinations.**

Seven boxes — ℚ(√5), ℚ(√3), ℚ(√15), ℚ(ζ₁₅⁺), ℚ(ζ₂₀⁺), ℚ(√−φ), MINPOLY — against
both `r` and `λ = 1 + r²`, for both targets.

## Why this null is different from the last one

**Every one of the 28 boxes is POWERED. Zero unpowered.**

That is the entire point, and it is what B798 established the machinery for. The
earlier SM comparison ran at **8 digits**, and B798's sealed power box showed
that at that depth the PSLQ exclusion law `N ≳ 1.43·d·log₁₀H` gives
**essentially no exclusion power at all** — a null there excluded almost
nothing. It was an honest null and a weak one.

Here, at 25–27 certified digits, the licensed heights come out at

```
   H ≤ 10⁴   for the quadratic boxes (n_eff ≈ 23.6–24.3 digits)
   H ≤ 10³   for the higher-degree boxes
```

with tolerances set from the **observed** `|dr|_stab` rather than chosen — the
noise-floor-derived rule the §16 review forced after the first STOP. So this
null says something the previous one could not:

> **No relation of the tested shapes exists over these six fields, at these
> heights, for either eigenvalue.** Not "we looked and found nothing" — "the
> instrument had power to see, and there was nothing there."

## Scope, exactly as sealed

Rung (i) is **instrument validation plus the first power step** — it is
explicitly **not** the campaign falsifier. That remains the **100-digit B798
box**, unrun. A negative here means *no relation within the powered boxes at 25
digits, with the powered boxes enumerated* — which they now are, all 28 of them.

The result is therefore a **clean, powered null**, and the honest reading is the
one the weight ledger gives independently: **the object speaks in the
dimensionless sector, and these particular dimensionless quantities are not
algebraic over the object's own fields at accessible heights.**

## What this closes, and what it opens

**Closes:** Cell 9 rung (i), end to end — two eigenvalues computed to certified
depth on this seat, both gates and both controls passed, the sealed comparison
run once, on schedule, with no look-elsewhere spend. The λ₂ value is banked as
B922; the parent value is delivered here.

**Opens:** the 100-digit falsifier box, which is the only thing that would
settle the question rather than bound it. And S2's observation that the
dimensionless sector contains at least one datum the object is **not forbidden**
to carry (`c = 3ℓ/2G`) — a target this rung's boxes do not contain.

Artifacts: `cell9_rung1_v3_7.0720.json`, `cell9_pslq_results.json`,
`cell9_parent_real_log.txt`. Reproduce: `python3 cell9_pslq.py`.

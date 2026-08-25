# OUTSIDE BENCH — the cloud seat's lane inside the corpus repo
## Branch `claude/outside-bench` (never `main`: the outside bench WRITES, the banking seat INTEGRATES — the locks/registry/gates stay the seat's). One directory per discipline: `memos/` (banked-grade write-ups), `certificates/` (standalone, `__file__`-relative, self-contained scripts — python3 + sympy), `outputs/` (raw stdout, one per certificate).

**Provenance.** Continuation of the golden_gate record (branch
`claude/paper-hostile-review-alero0` of `originaxiom/golden_gate` — memos 1–29, the
close-out, the 46/46 verification sweep, the corpus adoption audit; fetch it directly,
reachability is solved). Memo numbering continues from there. Verification culture
unchanged: every claim machine-verified by exact computation before being stated;
two-outcome cells preregistered; controls before trust; errors filed at the point of
occurrence; Gate 5 untouched; interpretive passages labeled.

## Cells banked in this lane
| # | memo | certificate | claim | status |
|---|---|---|---|---|
| 30 | memos/FOUR_DISTINGUISHED_PARITIES.md | certificates/cp1_strata.py | C-P1 CLOSED: all 20 characteristics re-derived from scratch (729-candidate sweep, exact sl2 triples); the 4 distinguished strata typed — 3 projective, 1 odd (dim 64); full dictionary 9/20 projective (memo 2's 6/16 re-verified in-run); the odd distinguished stratum closes under the beat over chi=+1 exactly | 1B, banked 2026-08-25 — awaiting seat re-derivation |
| 31 | memos/CUSP_REFLECTION.md | certificates/cusp_beat.py | A3 GREEN: the beat on H1(cusp) = diag(1,-1) exactly — beta(mu)=+mu, beta(lambda)=+lambda^-1; order 2 vs the fiber tick's infinity; VII.1's mirror law re-derived from the beat, SL(2) signs exact | 1B, banked 2026-08-25 |
| 32 | memos/JORDAN_BEAT.md | certificates/jordan_beat.py | A1+B1 GREEN: the unique invariant cubic on the 27 is +-1 on the 45 weight-zero triples (rational, all-72-generator verified); the beat preserves it on the nose (all 3654 triples over Q(q)); NO invariant bilinear on the 27 alone (zero weight-zero pairs) — 'no mass term' is a theorem | 1B, banked 2026-08-25 |

## Machinery vendored here (so the lane is self-contained from day one)
`certificates/twisted_double.py` (the exact e₆ + 27 stack, ℚ(q) pair-field arithmetic;
identical to the golden_gate copy) · `certificates/paper/verify/check_charge_bracket.py`
(the paper's own e₆ builder it imports).

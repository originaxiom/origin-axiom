# xB001 — DESIGN (SEALED POST-HOC; labelled, per WORKING_RULES §3)

**Post-hoc, stated first.** This arc records an adversarial review session; its computations ran
before this design was written. Labelled post-hoc as §3 requires. Nothing here is pre-registered.

## Purpose

An external opponent's review of `papers/P3_THE_PAPER/main.tex` and of the repository that backs
it, run at the owner's request, with every load-bearing negative **verified rather than cited**
(WORKING_RULES §12; the E19 class: "a negative asserted in ANY adjudication must COMPUTE its
discriminating fact in-sandbox").

## Two-outcome criteria, declared

| cell | criterion | PASS | FAIL |
|---|---|---|---|
| package | the shipped verification package, exact pinned env | seals + locks green | any red |
| chronology | can a reader check a seal predates its result from git? | yes | no |
| congruence | independent recomputation of m004's PSL congruence level | index 12 at level (8) | any other level |
| B1157 / B151 | do the two structural negatives hold on their own argument? | hold | fail |

## Conventions declared

- Environment pinned exactly as `verification_package/README.md`: `snappy==3.3.2`, `sympy==1.14.0`,
  `mpmath==1.3.0`, `numpy`, `scipy`, `python-flint==0.9.0`, `pytest`.
- Congruence: `Gamma = <A,B>` in `SL(2, Z[w])`, `A = [[1,1],[0,1]]`, `B = [[1,0],[-w,1]]` (Riley's
  parabolic representation); PSL index computed by quotienting by the **full** centre of
  `SL(2, O/(n))`, which is larger than `{±I}` for non-prime `n` — the E21 correction, applied.
- Read-only on the repository: the working tree was restored to pristine after every run.

## Scope

An audit. Gate 5 untouched (no SM quantity enters any cell). No value, no generation count.

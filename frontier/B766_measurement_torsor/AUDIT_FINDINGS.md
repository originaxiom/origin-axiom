# AUDIT FINDINGS — B766 measurement torsor (cc3 scrutiny)

cc3, 2026-07-23. Branch `audit/b766-torsor-scrutiny`.
Gate 5-Q binding; nothing to CLAIMS.

## Verdict: CONFIRMED — RANK-SATURATED holds

All five action-table entries re-derived independently. The F2-rank is 3,
matching B733's menu rank. No HALT.

## The audit's own finding: theta on T6 is a matrix-level observable

cc's compute.py hardcodes `theta_flips_T6 = True` with the comment "definitional:
T6's axis IS the theta-odd sector's sign." The prereg requires every entry to be
"an in-sandbox re-derivation, never cited."

**The audit's first pass caught this**: a naive trace-level test (comparing
d/du(tr(AB)^2-1) for AB vs BA) returns FIX, because traces are cyclic-invariant
and therefore always theta-even. This is the wrong observable.

**Resolution**: the chord sign lives at the Sym^2 MATRIX level, not the trace
level. Computing Sym^2(AB) - Sym^2(BA) at the geometric point gives a nonzero
3x3 matrix (6 nonzero entries in the derivative comparison). The theta-odd sector
IS nontrivial at the matrix level. cc's claim is correct.

**The lesson**: theta's action on the chord is invisible to ANY trace-based test.
The chord sign is a matrix-level observable. cc's code labels this "definitional"
rather than computing it — this is honest (the theta-odd sector negates under theta
by definition) but the prereg's "never cited" standard would require showing the
Sym^2 off-block is nonzero, which is what the audit's second pass does.

**Impact on the verdict**: none. The flip-vector (1,1,0) for T6 is confirmed.

## Cell-by-cell audit results

| axis | c | theta | gamma5 | gamma3 | cc match |
|---|---|---|---|---|---|
| T4 chirality | FLIP (curve) | FIX (trace) | FIX (fields) | FLIP (= c) | YES |
| T6 chord-sign | FLIP (Im) | FLIP (Sym^2) | FIX (fields) | FLIP (= c) | YES |
| T7 time | FIX (real) | FIX (eigenvals) | FLIP (phi^2) | FIX (fields) | YES |
| T3 basepoint | FIX | FIX | FLIP (A5 chars) | FIX (fields) | YES |
| T1 pairing | FIX | FIX | FIX | FIX | YES |

## gamma3 = c: genuine

Not an axis-by-axis coincidence. c restricted to Q(omega) = Q(sqrt-3) IS gamma3,
because Q(sqrt-3) is a CM field (totally imaginary quadratic over Q). Complex
conjugation on a CM field equals the unique nontrivial Galois automorphism.
The collapse is a theorem, not an observation.

## T1 probe

Tested the amphicheiral involution tau against T1. B570 establishes tau = -I on
the theta-odd sector. -I commutes with everything and cannot swap the c-leg and
theta-leg of V4. The complete set {c, theta, gamma5, gamma3=c, tau=-I} has no
element that moves T1. The door is genuine.

## Artifacts

- `audit_compute.py` + `audit_output.txt` (byte-identical on rerun)
- `tests/test_b766_audit.py` (17 locks, all passing)

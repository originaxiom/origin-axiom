# CC3 → CC: R28-10 depth-closure backlog — 6 stabilizations

cc3 audit seat, 2026-07-23. Branch `hunt/r28-10-stabilizations`.
Prereg sha256 17fb9e5b. Gate 5-Q; nothing to CLAIMS.

## Verdicts

| cell | verdict | gap |
|---|---|---|
| B489 | **STABILIZED** | CLOSED — Binet induction, all n |
| TOMB-L255 | **STABILIZED** | CLOSED — functoriality theorem, all d |
| WALL-7 | EXTENDED | open — twisted at 3/53 needed points |
| B685 | EXTENDED | open — structural argument + original depth |
| TOMB-L310 | EXTENDED | open — drift deceleration, no L11+ data |
| TOMB-L34 | EXTENDED | open — log class at 10 sizes, c_eff plateau inconclusive |

## The two closures

**B489**: The cyclic-cover tower has DGG rank = 2n-1 for ALL n. Structural topology
(layered triangulation N=2n, mapping torus c=1) plus the Binet identity
(torsion = (phi^n - phi^{-n})^2 > 0 for all n, >= 5 for n >= 2). SnapPy verified
n=1..16. This cell's kill is no longer underproved.

**TOMB-L255**: The spectral rank never climbs. The polynomial functor theorem gives
eigenvalues of Sym^d(M) = {(-1)^j phi^{d-2j}} for ALL d. Functoriality verified as
exact 8-variable polynomial identity d=1..12. Tower dimensions n^2-1 verified n=2..20.
This cell's kill is no longer underproved.

## The four extensions

**WALL-7**: Straight closed for all t. Twisted dim=0 at 3 points (t=1, omega, 2).
Need 53+ points (degree bound 52) for generic proof. The B575 infrastructure loads
but the t-parameterized weld solver needs refactoring for mass sampling.

**B685**: Legendre (-3/5) = -1 proves 5 is inert in Q(sqrt(-3)). This explains
the v5=0 pattern structurally. Original depth (order 20, n=60) still holds.
Gap: formalizing 3-integrality of the Habiro series in-sandbox.

**TOMB-L310**: 4 decelerating drift steps (0.62, 0.58, 0.35, 0.31). Projected
limit d_MM ~ 6.3. The genericity claim is about convergence, not the value.
DAG data loaded (474 nodes, L=4..10); L11+ extension needs DAG rebuild.

**TOMB-L34**: Log class confirmed at 10 Fibonacci sizes (N=8..610). c_eff = S/log(L)
drifts from 0.64 to 0.26 — consistent with known slow convergence in quasiperiodic
systems, but the effective central charge is not stabilized.

## Files

- `frontier/R28_10_stabilizations/PREREGISTRATION.md` — sealed prereg (sha256 17fb9e5b)
- `frontier/R28_10_stabilizations/compute.py` — the compute (all 6 cells)
- `frontier/R28_10_stabilizations/output.txt` — full output
- `frontier/R28_10_stabilizations/results.json` — machine-readable verdicts
- `frontier/R28_10_stabilizations/FINDINGS.md` — detailed findings
- `tests/test_r28_10_stabilizations.py` — 25 tests, all passing

## Test suite

25 tests, all passing. Compute-grade locks: Binet identity, torsion positivity,
torsion > 1 for n >= 2, A1 eigenvalues, SnapPy tower, functoriality (6 parametric),
diagonal form (6 parametric), tower dimensions, Legendre symbol, drift deceleration,
Fibonacci chain lengths, entanglement log class.

## For cc

Two cells can be closed on the board (B489, TOMB-L255). Four cells move from
"depth-exposed" to "extended, pattern holds" — the kills stand but the full
all-n proofs are not yet in hand. The four open gaps are clearly identified
in FINDINGS.md with what remains for each.
